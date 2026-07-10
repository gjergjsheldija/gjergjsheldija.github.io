---
title: "FHIR PlanDefinitions Need a Process Engine, Not Just $apply"
date: 2026-07-10T08:00:00Z
draft: false
categories: ["Engineering", "Healthcare"]
tags: ["FHIR", "PlanDefinition", "BPMN", "Clinical Reasoning", "CQL", "FHIRPath", "Camunda", "Care Pathways", "Architecture"]
author: "Gjergj Sheldija"
description: "FHIR's $apply operation evaluates a PlanDefinition once and hands back a plan. It has no concept of a process that waits three days for a lab result. Here is how to compile PlanDefinitions into BPMN 2.0 and run them on a real process engine, and where a naive compiler breaks on a live clinical protocol."
featured_image: "/images/fhir-plandefinition-bpmn-execution.png"
---

# FHIR PlanDefinitions Need a Process Engine, Not Just $apply

HL7 FHIR has won most of the data standards argument in health tech. As a way to represent clinical records, orders, and observations, it is the default choice for anyone building new infrastructure. But storing clinical data was never the hard part of digital health platforms. The hard part is orchestrating clinical execution: taking a guideline, a care pathway, or a hospital protocol and running it, with branches, timeouts, parallel tracks, and safety overrides, against a real patient over days or weeks.

FHIR has an answer for the declarative half of that problem. The Clinical Reasoning module defines the `PlanDefinition` resource: a machine-readable representation of a protocol, built from nested `action` elements, conditions written in Clinical Quality Language (CQL), and trigger definitions. FHIR also defines how to execute one. The `$apply` operation takes a `PlanDefinition` plus a patient context, evaluates the embedded CQL, and returns a `CarePlan` or `RequestGroup` resource describing the concrete actions to take.

`$apply` is where most implementations stop, and it is also where most implementations quietly fail to handle the case that actually matters: a protocol that spans days, waits on external events, and needs to change course mid-execution without losing state. `$apply` is a stateless, synchronous evaluation. Call it once, get a plan back. It has no notion of a running process instance, no way to pause for three days waiting on a lab result, and no mechanism to correlate an asynchronous lab callback back to the specific patient encounter that is waiting on it. You can call `$apply` again after new data arrives, but you are now responsible for tracking, outside of FHIR entirely, which step you are on, what you are waiting for, and how to resume correctly. That state-tracking problem is the real reason to reach for a process engine, and it is a more precise justification than "FHIR does not have an execution engine" (it does, just not a stateful one).

The most direct way to close that gap is to compile `PlanDefinition` resources into standard BPMN 2.0 XML and run them on a mature process engine: Camunda 8 (built on the Zeebe runtime), Camunda 7, or Flowable. That gets you persistent process state, audit trails, and message correlation for free, instead of building them yourself on top of a CQL evaluator. Below is how that compilation pipeline is structured, where FHIR's native execution model stops being enough, and the specific failure modes a naive compiler runs into on a live hospital protocol.

## Structural mapping

The compiler's first job is a direct translation from the declarative action hierarchy in a `PlanDefinition` into a procedural process graph.

| FHIR element | BPMN equivalent | Role |
|---|---|---|
| `PlanDefinition` | `bpmn:Process` | The process definition container |
| `action` (parent) | `bpmn:SubProcess` | Groups related interventions or phases |
| `action` (leaf) | `bpmn:Task` (service or user task) | An execution step: order a lab, send an alert |
| `action.trigger` | `bpmn:StartEvent` / boundary event | Initiates or interrupts a step based on incoming data |
| `action.condition` | `bpmn:SequenceFlow` + expression | Gateway logic determining pathing |

The pipeline itself follows a standard compiler shape:

1. **Flattening.** Recursively unnest the `action` structures into a directed acyclic graph.
2. **Dependency resolution.** Evaluate `action.relatedAction` (for example, "start two hours after the prior action completes") and translate the offset into BPMN sequence flows or parallel paths separated by intermediate timer events.
3. **Expression translation.** `action.condition.expression` is a FHIR `Expression` datatype, and its `language` field tells you which of two very different problems you have: `text/fhirpath` or `text/cql`. Turn whichever one you find into something the process engine can evaluate at a gateway.

That third step is where most of the actual engineering difficulty lives, and it deserves more than one line.

## The hard part: CQL, not FHIRPath, is where translation breaks

Not every condition in a `PlanDefinition` is CQL, and a compiler that treats them all as CQL is solving a harder problem than it needs to for a large share of real protocols.

FHIRPath conditions are the easy case. FHIRPath is a navigation and predicate language over the resource tree: property access, `where()`, `exists()`, boolean comparisons. It has no terminology binding, no `retrieve` against an external data source, and no temporal operators. A condition like `Observation.value.exists() and Observation.value > 140` is FHIRPath, and it maps reasonably well onto what a gateway expression language already does: navigate a structure, evaluate a predicate, return a boolean. Translating FHIRPath conditions directly into FEEL or JUEL, or embedding a small FHIRPath evaluator as a callable function inside the gateway expression, is a tractable, largely non-lossy translation.

CQL is the hard case. It is not a generic boolean expression language. It carries clinical semantics that a workflow engine's native expression language, FEEL in Zeebe or JUEL in Camunda 7, has no concept of: value set membership and terminology binding, `retrieve` expressions against a modeled clinical data source, and temporal operators over clinical events (`during`, `overlaps`, `starts before end of`). FEEL can evaluate `patient.age > 65`. It cannot natively evaluate "the patient has an active diagnosis coded to any concept in this SNOMED value set within the last six months," which is the kind of condition CQL was built for and the kind that actually shows up in a `PlanDefinition` once you're past simple thresholds.

There are two honest ways to handle a CQL condition, and both have real costs. The first is to keep CQL evaluation outside the workflow engine entirely: run a CQL engine (the HL7 reference implementation, or an equivalent) as a service task, and hand the engine only the resulting boolean or set for gateway routing. This preserves full CQL semantics but means every conditional branch is a network call to another service, and it puts the CQL engine on the critical path of every gateway evaluation. The second is to attempt a translation of the underlying logic into FEEL or JUEL directly. This is faster at runtime but is a lossy translation: value set expansion has to happen at compile time and get baked into the generated expression, and any CQL construct without a FEEL equivalent either fails to compile or gets silently approximated. If your compiler takes this path, treat expression translation coverage as a tested, versioned contract, not a best-effort transform, because a silent approximation in a conditional that routes a patient to an emergency pathway is not a bug you want discovered in production.

Most serious implementations end up on the first approach for CQL conditions beyond simple threshold checks, while routing `text/fhirpath` conditions straight to a native gateway expression. Branching your compiler on `expression.language` at compile time, rather than treating every condition as CQL, is what keeps the common case cheap. This is a harder problem than the DAG generation in the previous section, and it is the part of the system most likely to determine whether the whole approach works.

## Clinical edge cases that break a naive compiler

### Non-deterministic protocol interruption

A banking workflow moves through its steps in order. A patient's condition does not wait for the process to reach a convenient point. If vitals cross a critical threshold, the standard care path has to abort immediately in favor of an emergency protocol, from wherever it currently is.

Do not try to hardcode every contingency as a branch in the main sequence flow. That produces unmaintainable BPMN within a few protocol revisions. Instead, isolate standard protocol logic on the main canvas and add safety overrides as separate, interrupting event sub-processes:

```
[ Main Clinical Process ]
  Standard Action A -> Standard Action B -> Standard Action C

[ Event Sub-Process: Critical Vitals Detected (interrupting) ]
  Abort main track -> Route to emergency care team
```

One thing this pattern glosses over if you stop here: the process engine itself has no way to continuously evaluate a vitals stream. BPMN engines are event-driven, not stream-processing systems. The threshold check that fires the interrupting event has to live in a separate component, typically a streaming or complex-event-processing layer (Kafka Streams, Flink, or a purpose-built rules engine) subscribed to the vitals feed, which posts a signal or message into the process engine only when the threshold is actually crossed. The event sub-process is the right BPMN construct for handling the interruption once it arrives. It is not where the threshold logic itself should run.

### Asynchronous wait states

A typical action reads: order medication A, wait for lab result B, then re-evaluate. Lab turnaround can span days. You cannot block a thread for that long, and polling a database on an interval does not scale past a few hundred concurrent patients.

Compile the wait state into a BPMN receive task, keyed to a composite correlation identifier such as patient ID plus encounter ID or the originating `ServiceRequest.id`:

```xml
<bpmn:message id="Msg_LipidPanelCompleted" name="lipid-panel-completed" />

<bpmn:receiveTask id="Receive_LipidPanel" name="Wait for Lab Results"
                   messageRef="Msg_LipidPanelCompleted">
  <bpmn:incoming>Flow_From_Order</bpmn:incoming>
  <bpmn:outgoing>Flow_To_Review</bpmn:outgoing>
</bpmn:receiveTask>
```

In production, this sits inside an ordinary event-driven integration:

```
[FHIR Server] --(Subscription/webhook)--> [Integration broker]
                                                 |
                                          (correlate event)
                                                 v
[BPMN Engine] <-- POST /message { "msg": "lipid-panel-completed", "key": "enc-123" }
```

The engine parks the process instance in persistent storage, consuming no memory or CPU while it waits. When the lab result lands on the FHIR server, a subscription listener catches it, extracts the correlation key, and posts a message to the engine's API, which resumes the exact instance waiting on that encounter.

### Multi-cardinality actions

Some guidelines specify: for each elevated biomarker in the panel, start a specialist review. Because the collection size is only known at runtime, a static process path does not work.

The fix is a BPMN parallel multi-instance activity. The compiler feeds it a collection produced by a CQL evaluation at runtime, and the engine spawns one independent token per element, each with its own execution context and its own entry in the audit log. This is the one part of the pipeline where the standard BPMN pattern maps onto the clinical requirement without much modification.

## System shape

The compiler runs as an isolated backend service inside a standards-first eHealth architecture:

```
[ Clinical App ]  -->  [ FHIR Compiler ]  -->  [ BPMN Engine ]
 (triggers plan)        (JSON to XML)          (executes care)
```

A clinician or scheduler triggers a protocol. The compiler service fetches the `PlanDefinition` and its dependent CQL libraries over REST, resolves them into BPMN 2.0 XML, and deploys that XML to the process engine, which starts a process instance bound to the patient's record identifier. Everything downstream, correlation, timers, audit, is the engine's job, not the compiler's.

## The actual takeaway

Treating BPMN as a diagramming layer on top of FHIR is a mistake; the value here is entirely in the process engine's persistence and correlation model, not its visual notation. The harder mistake is treating the compiler as a mechanical JSON-to-XML transform. The structural mapping from `action` hierarchy to process graph is genuinely mechanical. Getting CQL semantics correctly represented in the target engine's expression language, and being explicit about where FHIR's native `$apply` operation stops being sufficient, is not. If you build this without engaging with both of those points, you will ship something that demos well on a simple protocol and breaks on the first guideline with a real value set binding in it.
