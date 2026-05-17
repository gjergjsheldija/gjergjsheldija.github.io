---
title: "Compliance as Code: How to Keep Shipping Fast When Your Product Is a Medical Device"
date: 2026-05-17T08:00:00Z
draft: false
categories: ["Engineering", "Regulatory"]
tags: ["MDR", "ISO 13485", "CI/CD", "DevOps", "Medical Device Software", "Compliance", "Engineering Leadership", "GitOps", "Quality Management"]
author: "Gjergj Sheldija"
description: "Most medical device software teams treat compliance as a gate at the end of development, and pay for it in slow releases and audit scrambles. Here's how to encode regulatory requirements directly into your CI/CD pipeline, so compliance becomes a property of every build, not a phase at the end of your roadmap."
featured_image: "/images/compliance-as-code.png"
---

# Compliance as Code: How to Keep Shipping Fast When Your Product Is a Medical Device

There is a belief, almost universal among engineers who join regulated healthcare companies from the outside, that compliance is the enemy of velocity. That MDR and ISO 13485 are walls your product has to climb over before it can ship. That the job of the regulatory function is to slow things down in controlled ways.

I held a version of this belief myself, early on. I don't anymore.

The problem isn't compliance. The problem is *where* compliance lives in the development process. Most teams put it at the end: a gate, a review, a document-gathering exercise triggered by an upcoming audit or a release milestone. That's the design decision that kills velocity. When you move compliance into the pipeline itself, it stops being a gate and becomes a property of every build. It's always true, or the build fails.

This article is about how to make that shift: what it looks like architecturally, what it costs, and what it gives you back.

## Why the Gate Model Breaks Down at Scale

The gate model has a seductive logic: developers write code, a separate compliance function reviews it against regulatory requirements, and only code that passes goes to production. Clear separation of concerns. Auditable handoffs.

In practice it breaks in three predictable ways.

First, it creates a compliance bottleneck that scales with team size. The more engineers you have, the more output the compliance function has to review, but the compliance function doesn't scale at the same rate. Every squad that ships a feature creates work for a centralised review process that can't absorb it.

Second, it produces documentation that lies. When you write the Software Development Lifecycle documentation, the risk management file, the traceability matrix *after* the code is written, you are inevitably reconstructing a narrative. The code went through six iterations; the document describes iteration one's design. Auditors who know what they're looking for can smell this immediately.

Third, and most importantly for software organisations: it makes your regulatory posture a lagging indicator. You find out you have a problem when someone reviews a document, not when the problem was introduced. That gap, between when a risk enters your codebase and when it's detected, is where audit findings live.

## What "Compliance as Code" Actually Means

The phrase is easy to misread as "write your SOPs in YAML." That's not it.

Compliance as Code means three things operationally:

**Traceability is generated, not written.** Every requirement in your risk management file has a corresponding test. The CI pipeline runs those tests, and the traceability matrix (linking requirement to test to result) is produced as a build artifact. Nobody writes the matrix by hand; the pipeline generates it from execution evidence.

**Quality gates are encoded as pipeline stages.** If your product is a Class IIa medical device under MDR, your software safety classification drives specific verification requirements. Those requirements become mandatory pipeline stages: static analysis against defined rules, integration test coverage thresholds, SBOM generation, dependency vulnerability scans. A build that doesn't pass every stage doesn't produce a deployable artifact. There is no override.

**Change documentation is derived from version control.** Every commit that touches safety-relevant code triggers automated generation of the change documentation required by ISO 13485 §7.3.7. The pipeline knows which files are in scope (that scope is declared explicitly in the repository) and produces the change record from the diff. Engineers don't write change records; they write code, and the record follows.

## The Architecture in Practice

Here is what the pipeline looked like in one implementation I ran for a PROM-based clinical platform operating under MDR:

```
[Feature Branch]
      │
      ▼
[Static Analysis]        ← MISRA/custom ruleset for safety-critical paths
      │
      ▼
[Unit Tests]             ← Coverage gate: 90% for Class A modules, 100% for Class B
      │
      ▼
[Integration Tests]      ← FHIR conformance validation, API contract tests
      │
      ▼
[Risk Trigger Check]     ← Did this diff touch files in the risk register?
      │                      If yes → generate change record, require sign-off
      ▼
[SBOM Generation]        ← CycloneDX format, captured as build artifact
      │
      ▼
[Traceability Export]    ← Requirement → Test → Result → Coverage %
      │
      ▼
[Artifact Registry]      ← Only builds that passed every stage reach here
```

The risk register itself lives in the repository as a structured file: not a spreadsheet managed by a QA officer somewhere, but a YAML file that the pipeline reads. Every file in the codebase is tagged to a safety class. The pipeline knows, from the diff, whether a change touches Class A or Class B code, and applies different gate criteria accordingly.

When a change does touch safety-relevant code, the pipeline doesn't fail; it pauses and generates a draft change record, pre-populated with the diff summary, affected requirements, and test results. A responsible person reviews and approves it. The review is recorded. The build continues. The whole flow, from commit to deployable artifact, might take four hours including the async review, compared to the two-week documentation cycle it replaced.

## The Organisational Half of the Problem

The pipeline architecture is the easier half. The harder half is distributing compliance ownership to the squads that write the code.

The traditional model puts regulatory knowledge in a centralised function. Developers don't need to understand MDR; they write code, and someone else figures out the compliance implications. This seems efficient and fails badly: the compliance function becomes a bottleneck, developers have no feedback loop, and regulatory knowledge never diffuses into the engineering culture.

In a squad model, each squad owns the compliance posture of their domain. They know which of their modules are safety-classified, which requirements map to their code, and which pipeline gates apply to their work. This isn't a burden; it's a capability. A squad that understands the regulatory implications of their design choices makes better design choices. Risk-aware engineering is better engineering.

Getting there requires investment. We ran a structured programme: engineers spent time with the regulatory team understanding risk classification criteria, the regulatory team spent time in sprint reviews understanding what the code actually did. The shared vocabulary that came out of that, a common understanding of which design patterns created which risk patterns, was more valuable than any document we produced.

## What You Get Back

The shift is not costless. Building the pipeline takes time. Tagging the codebase for safety classification takes time. Training squads takes time. In my experience the initial build, from a team that already understands both CI/CD and the regulatory landscape, is roughly six to eight weeks of concerted effort.

What you get back:

**Release confidence.** When every artifact in your registry has a complete compliance trail attached, release sign-off stops being a negotiation and becomes a check. The evidence exists; you just verify it's there.

**Audit readiness as a constant state.** The worst thing about traditional compliance is that it concentrates into a panic before an audit. When compliance is generated continuously, you're always audit-ready. The last time I walked into a notified body audit with this system in place, we produced the complete technical documentation (traceability matrix, change history, SBOM, test evidence) in under an hour. The auditors spent their time on substance, not on chasing documents.

**Faster incident response.** When something goes wrong in a certified product, the first question is always "what changed?" A pipeline that generates complete change documentation for every safety-relevant diff means you can answer that question in minutes, not days.

**Developer trust in the process.** This one surprised me the most. Engineers who understand why a gate exists, and who can see immediately when their code passes or fails it, engage with compliance differently than engineers who experience it as an external review they have to survive. Compliance becomes part of the craft, not an obstacle to it.

## The Honest Constraints

This approach works best when certain conditions hold. It's worth being clear about where it gets harder.

It works best on greenfield or significantly modernised codebases. If your safety-critical modules are legacy code with no test coverage and no clear ownership, you need to solve that problem before you can automate compliance evidence generation from tests that don't exist.

It requires upfront investment in classifying your codebase. Someone has to go through the repository, apply the safety classification, and get that classification reviewed by people who know the regulatory requirements. This is real work and it can't be shortcut.

It requires a regulatory function that is comfortable with code as the source of truth. Some QA officers are; many are not yet. Changing that dynamic is a leadership problem as much as a technical one.

And it doesn't eliminate the need for clinical and regulatory expertise. The pipeline enforces the requirements; it doesn't define them. Someone still has to understand MDR Annex I, interpret the clinical risk to patients, and make the classification decisions that the pipeline then enforces. Automation amplifies expert judgment; it doesn't replace it.

## The Core Argument

Compliance and velocity aren't in opposition. They're in opposition when compliance is a gate. When compliance is a pipeline property, you get both, and you get something more valuable than either: a codebase where every build is demonstrably safe to ship, by construction.

The engineering investment required to get there is real but bounded. The return, in release confidence, audit readiness, and engineering culture, compounds over time.

If you're building or scaling a software team in a regulated health environment, this is the infrastructure worth building first.
