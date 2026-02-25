---
title: "Breaking the Mold: The Case for Custom FHIR Resources"
date: 2026-02-25T16:10:25+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "Architecture", "FSH", "Logical Models", "Interoperability", "Healthcare IT"]
categories: ["Engineering", "Healthcare"]
description: "Exploring the strategic value of Logical Models in FHIR architecture: when to use them, why they matter, and how to implement them using FHIR Shorthand (FSH)."
featured_image: "/images/custom_fhir_resource_featured.png"
---

# Breaking the Mold: The Case for Custom FHIR Resources

In the FHIR world, we are often told to "stick to the standard." And for 95% of use cases, that's the right advice. If you have a patient, use `Patient`. If you have a laboratory result, use `Observation`. But as software architects, we occasionally encounter domain-specific data structures that simply don't fit into the predefined semantic pigeonholes of the FHIR specification.

When the standard fails to capture the core essence of your domain model, you have two choices: shoehorn your data into a `Basic` resource—effectively hiding your complexity inside a generic container—or define a **Logical Model**.

## Why Logical Models?

A Logical Model allows you to define a structure that inherits from FHIR's `Base` type but contains only the elements your specific use case requires. It’s a powerful way to represent business logic, administrative entities, or domain-specific structures that aren't yet—or may never be—part of the core FHIR specification.

From an architectural standpoint, this approach offers several key advantages:

1.  **Semantic Clarity**: Your resources are named after what they actually represent (e.g., `ClinicalProtocol` or `CustomResearchEntity`), not just "Basic with an extension."
2.  **Model-Driven Design**: Logical models defined in **FHIR Shorthand (FSH)** serve as a platform-agnostic "Source of Truth." They can be used to generate StructureDefinitions, JSON Schemas, and comprehensive documentation automatically.
3.  **Strict Validation**: Even though the resource isn't "standard," the IG Publisher can still generate validation logic. This ensures that your custom data structures are syntactically correct and follow the constraints you’ve defined.

## Minimalist Implementation with FSH

I've recently put together a clean, minimal example of this pattern in my [custom-fhir-resource](https://github.com/gjergjsheldija/custom-fhir-resource) repository. It demonstrates how to use **FSH** and **SUSHI** to define a logical model.

In this project, the definition of a `CustomResource` looks like this:

```fsh
LogicalModel: CustomResource
Parent: Base
Title: "Custom Resource"
Description: "A custom resource model demonstration."
* id 0..1 string "Logical id of this artifact"
* name 0..1 string "Name of the resource"
* somethingelse 1..1 Reference(Observation) "A mandatory reference to an Observation"
```

This simple definition provides enough metadata for the IG Publisher to treat it as a first-class citizen. You get generated tables, XML/JSON examples, and UML diagrams out of the box.

## The Verdict: When to Go Custom

As architects, our goal is to build systems that are both interoperable and maintainable. 

*   **Use Profiles** when you are restricting or extending standard clinical concepts (e.g., "A German Patient" or "A Vital Signs Observation").
*   **Use Logical Models** when you are defining domain-specific data that has its own unique lifecycle and structure, and where forcing it into a standard resource would lead to "semantic leakage."

By leveraging the FHIR IG toolchain, we can move away from static documentation and towards a **Model-Driven Architecture** where our design decisions are explicitly defined, validated, and shared across the entire ecosystem.

---
*Check out the full source code and build scripts on GitHub: [gjergjsheldija/custom-fhir-resource](https://github.com/gjergjsheldija/custom-fhir-resource)*


