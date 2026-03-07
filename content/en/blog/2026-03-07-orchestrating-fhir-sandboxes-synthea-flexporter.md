---
title: "Orchestrating the Perfect FHIR Sandbox: The Power of Synthea and Flexporter"
date: 2026-03-06T11:30:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["Synthea", "Flexporter", "FHIR", "Healthcare IT", "Architecture", "Data Transformation", "Synthetic Data", "Clinical Trials"]
categories: ["Engineering", "Healthcare"]
description: "How to move beyond static test data by combining the scale of Synthea with the precision of Flexporter to build realistic, custom healthcare environments."
featured_image: "/images/synthea_flexporter_featured.png"
---

# Orchestrating the Perfect FHIR Sandbox: The Power of Synthea and Flexporter

As healthcare architects, one of our greatest challenges isn't just designing the system—it's proving that the design works under realistic conditions. How do you test a complex clinical trial workflow or a new custom resource model without touching a single byte of Protected Health Information (PHI)?

Static, hand-crafted JSON files are fine for unit tests, but they fail to capture the "messiness" and scale of real-world longitudinal health records. To build a truly robust sandbox, we need two things: **Scale** and **Precision**.

This is where the combination of **Synthea** and **Flexporter** becomes a game-changer.

## The Population Engine: Synthea

[Synthea](https://github.com/synthetichealth/synthea) is already a staple in the FHIR community. It generates high-fidelity, synthetic patient records that include everything from demographics to encounters, observations, and medications. 

However, Synthea generates "standard" clinical data. What happens when your architecture requires domain-specific extensions, custom logical models, or specialized resources like `ResearchStudy` and `ResearchSubject` that aren't part of Synthea's core output?

## The Architect's Scalpel: Flexporter

This is where [Synthea Flexporter](https://github.com/synthetichealth/synthea/wiki/Flexporter) fits in. Think of Flexporter as the "Swiss Army Knife" for FHIR data transformation. It allows you to intercept a stream of FHIR resources and apply complex logic to shape them into exactly what your architecture needs.

I've been experimenting with this workflow in my [custom-fhir-resource](https://github.com/gjergjsheldija/custom-fhir-resource) project, and the results are incredibly powerful.

### Real-World Example: Provisioning a Clinical Trial Sandbox

Let's say you're building a system for clinical research. You need a sandbox populated with hundreds of patients, but they all need to be enrolled in a specific `ResearchStudy` and have corresponding `ResearchSubject` resources.

Instead of writing a custom script to mangle Synthea's output, you can use a declarative Flexporter configuration.

In my project's [`flexporter_custom_resources.yaml`](https://github.com/gjergjsheldija/custom-fhir-resource/blob/main/config/%20flexporter_custom_resources.yaml), I define the transformation logic like this:

```yaml
actions:
  # 1. Create a Singleton ResearchStudy
  - fhirpath: "Bundle.limit(1)"
    create_resource:
      - resourceType: ResearchStudy
        fields:
          - location: "ResearchStudy.id"
            value: "example-research-study"
          - location: "ResearchStudy.status"
            value: "active"

  # 2. Map every Patient to a ResearchSubject 
  - fhirpath: "Bundle.entry.resource.ofType(Patient)"
    create_resource:
      - resourceType: ResearchSubject 
        fields:
          - location: "ResearchSubject.status"
            value: "candidate" 
          - location: "ResearchSubject.individual.reference"
            value: $findRef([Patient])
          - location: "ResearchSubject.study.reference"
            value: $findRef([ResearchStudy])
```

With just a few lines of YAML and FHIRPath, we've transformed a generic clinical record into a specialized research entity.

## Power Up: Custom Logic and Cleanup

The true power of this stack lies in its extensibility. Flexporter allows you to inject custom JavaScript for cleanup or complex transformations. For instance, if your target system doesn't support specific US-Core extensions that Synthea includes by default, you can strip them out on the fly:

```javascript
// A simple cleanup script embedded in the YAML
function removeSpecificExtensions(bundle) {
  const removeUrls = [
    "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
    "http://synthetichealth.github.io/synthea/disability-adjusted-life-years"
  ];
  // ... filter logic ...
  return bundle;
}
```

## Running the Pipeline

The workflow is beautifully simple:

1.  **Generate base data**: Run Synthea to create the raw FHIR bundles.
    ```bash
    ./run_synthea -p 10 --exporter.fhir.export=true
    ```
2.  **Apply transformations**: Pass those bundles through Flexporter with your config.
    ```bash
    ./run_flexporter -fm config/flexporter_custom_resources.yaml -s output/fhir/
    ```

Check out the full implementation details in the [Running Synthea and Flexporter](https://github.com/gjergjsheldija/custom-fhir-resource#running-synthea-and-flexporter) section of my latest repository.

## The Verdict

For healthcare architects, the goal is often to provide a development environment that is as close to production as possible. By combining the **generative power of Synthea** with the **transformative precision of Flexporter**, we can create "Model-Driven Sandboxes" that are:

*   **Deterministic**: Easily reproducible across environments.
*   **Privacy-First**: Zero PII risk.
*   **Architecturally Relevant**: Custom-tailored to your specific domain models.

It's time to stop fighting with test data and start orchestrating it.

---
*Deep dive into the source code: [gjergjsheldija/custom-fhir-resource](https://github.com/gjergjsheldija/custom-fhir-resource)*
