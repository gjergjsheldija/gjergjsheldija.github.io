---
title: "FHIR Is Not Just a Protocol — And Why That Distinction Matters"
date: 2026-05-04T08:48:00Z
draft: false
categories: ["Informatics", "Engineering"]
tags: ["FHIR", "Domain Model", "SDC", "ePRO", "EDC", "Clinical Data", "Regulatory Compliance", "Architecture"]
author: "Engineering Leadership Team"
description: "Why treating FHIR as a domain model—not just a protocol—matters for clinical platforms, regulatory compliance, and team efficiency. Lessons from building a FHIR-native stack for ePRO, EDC, and imaging in a German regulatory context."
featured_image: "/images/fhir-architecture-friendly.png"
---

# FHIR Is Not Just a Protocol — And Why That Distinction Matters

In a recent project, building a new clinical platform that combines ePRO, EDC, and medical image analysis, I've had a recurring debate with a colleague about FHIR. His position: FHIR is an interoperability protocol — great for exchanging data between institutions, but not something you build your internal domain model on. My position: that distinction, while technically real, is the wrong one to optimize around — especially in 2026.

This is my attempt to write that argument down properly.

## The Platform and the Stack

The platform we're building needed to do three things at once: collect patient-reported outcomes (ePRO), support electronic data capture (EDC), and store medical images alongside AI-generated measurements and human reads.

My architecture decision was to go FHIR-native across the board:

- **FHIR CDR** as the FHIR-native backend store the results, measurement data, and clinical observations
- **Open source SDC framework** for the UI layer, built around FHIR resources
- **Keycloak** with SMART on FHIR for permissions and access control
- For imaging: `ImagingStudy` for study metadata, `Observation` for AI and human measurements, `DiagnosticReport` to tie it together

The result was fast iteration, a unified data model across all three platform components, and zero translation layer between modules.

## The Objection

The objection from my colleague was articulate and not entirely wrong:

> *"FHIR is the right standard — but what these sources describe is FHIR as an interoperability protocol between institutions. They do not describe it as an internal domain model for application development. The regulatory requirement is met by a clean outbound/inbound layer. Everything beyond that is an architecture choice."*

This is a reasonable position on its face. And the distinction between FHIR-as-protocol and FHIR-as-domain-model is a real one. So let me address it directly.

## FHIR Is More Than a Transport Layer

The most common misconception about FHIR — especially among developers coming from non-web backgrounds — is that it's essentially HL7 v2 with a REST wrapper: a message format for moving data between systems, not something you build on internally.

That's not what FHIR is.

FHIR defines a **logical domain model** (the resources), a **REST interaction model** (how you read, write, search, and version those resources), and a **content standard** (Implementation Guides that define exactly what data elements mean in a given context). Tools like Aidbox exist precisely to persist that model natively — making FHIR your internal store, not just your outbound format.

The FDA's PQ/CMC Implementation Guide is a useful concrete example. It explicitly defines data elements: batch formulas, quality specifications, submission content structure. It is built on eCTD, which is itself a content and submission standard. That IG is not describing how to move data between institutions. It is defining what the data *is*. That is a domain model.

Siemens, Philips, and Mayo Clinic are all using FHIR this way for medical imaging — not as a transport envelope between hospitals, but as the semantic layer on top of DICOM for storing measurements, AI outputs, and structured reports. The pattern is `ImagingStudy` for the study, `Observation` for each measurement, `DiagnosticReport` to assemble the clinical picture.

## SQL on FHIR — Closing the Last Gap

One of the lingering objections to using FHIR as an application storage layer has been analytical querying. FHIR's nested, resource-centric structure is expressive and clinically rich — but it's not what analysts or reporting pipelines expect. Traditionally, getting tabular data out of a FHIR store meant custom extraction logic or, worse, a separate reporting database kept in sync.

SQL on FHIR closes that gap entirely.

The [SQL on FHIR specification](https://build.fhir.org/ig/FHIR/sql-on-fhir-v2/) defines a standard way to create flat, tabular **ViewDefinitions** directly over FHIR resources. You define a view once — say, all `Observation` resources for a given LOINC code — and query it with standard SQL. No ETL, no synchronization, no separate model to maintain.

For a platform like this, the impact is significant. It means:

- **Reporting and analytics** work directly against the FHIR store, without a data warehouse layer
- **AI pipelines** can consume clean tabular views of measurements without bespoke extraction code
- **Regulatory submissions** can be assembled from the same store that drives the clinical UI

Combined with a FHIR-native backend like FHIR CDR — which supports SQL on FHIR natively — this makes FHIR a genuinely robust application storage layer, not just a model you tolerate for regulatory reasons. You get the clinical expressiveness of FHIR resources and the query ergonomics of SQL, in the same system, with no synchronization problem to manage.

The "FHIR is only for transport" argument was always weakest on persistence. SQL on FHIR removes the last reasonable objection.

## The Cost of the Alternative — We Already Paid It

The most concrete argument I have isn't theoretical. It's a scar.

In a previous iteration of the platform there was a running ETL layer. It exists because the internal data model and the outbound format didn't align. Every time data needed to move from one to the other, it had to be transformed, mapped, and validated. That's maintenance cost, that's a failure surface, and that's where bugs live.

My colleague's proposal — a "clean outbound/inbound layer" — is exactly that architecture. He's proposing we build it again, deliberately, knowing what it costs.

The FHIR-native approach eliminates that layer by making the internal model and the outbound format the same thing. There is no mapping step. There is no place for that class of bug to exist.

## The German Regulatory Context Makes This Concrete

In Germany, this isn't a philosophical choice about future-proofing — it's a current operational reality.

The **ePA** (elektronische Patientenakte) and **DiGA** (Digitale Gesundheitsanwendungen) infrastructure runs on FHIR today. Patients have a legal right to their data in a portable format, and in Germany, that format is FHIR.

If you build a custom internal domain model, you're producing FHIR twice: once as an output step when data leaves your system, and again every time you need to connect to national infrastructure or respond to a patient data request. That's double the work and double the places things can go wrong.

Building natively in FHIR isn't ideological. It's alignment with the infrastructure you're required to connect to.

## The Symmetry Argument

My colleague said: *"Nothing in FHIR comes for free."*

He's right. But nothing in a custom domain model comes for free either — and a custom model gives you none of the tooling, validation, terminology binding, provenance tracking, or regulatory traceability that FHIR provides as a base layer.

You're not choosing between expensive and cheap. You're choosing which costs to carry — and whether those costs come with benefits attached.

FHIR's costs come with: a standardized schema you don't have to invent, built-in versioning and provenance, terminology binding to SNOMED/LOINC/ICD, SQL-queryable analytics via SQL on FHIR, and compliance alignment with FDA, ePA and DiGA out of the box.

A custom model's costs come with: a schema you maintain forever, a mapping layer to every standard you eventually need to connect to, and a rewrite when the regulatory landscape moves — which it is.

## A Note on Team Dynamics

One thing I didn't expect when making this architectural choice: how much the internal debate would cost.

A year of relitigating the same decision is expensive. Not because the debate is wrong to have — it isn't — but because once an architecture is decided and implementation has started, the cost of the debate shifts. It's no longer about finding the best answer. It's about governance: who has the authority to make the call, and how do you close it so the team can move.

If you're an architect in a similar situation, my honest advice: make the decision, document it clearly, define the interfaces each component needs to implement, and escalate quickly if someone keeps reopening it. A developer doesn't need to agree with FHIR philosophically to output a JSON structure to a defined schema. That's the interface. Spec it and ship it.

## Conclusion

FHIR is not just a protocol. It is a domain model, a content standard, and — when you use the right tooling — a robust application storage layer. SQL on FHIR removes the last reasonable objection to using it as such, giving you clinical expressiveness and SQL query ergonomics in the same system, with no ETL layer in between.

The "interop only" view is a relic of HL7 v2 thinking that doesn't reflect how the ecosystem has evolved.

For a platform like this — combining ePRO, EDC, and medical imaging in a German regulatory context — going FHIR-native wasn't the fashionable choice. It was the pragmatic one. We get a unified data model, no ETL layer, compliance with ePA and DiGA out of the box, SQL-based analytics without a data warehouse, and a clear interface for every component including the imaging backend.

The debate was worth having. But the answer was right.