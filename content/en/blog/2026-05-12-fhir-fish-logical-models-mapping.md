---
title: "FHIR Data Modeling via FISH: Logical Models and Mapping for Advanced Scenarios"
date: 2026-05-12
draft: false
description: "Explore how logical models and FISH mapping work together to enable sophisticated FHIR data modeling scenarios with advanced QA workflows, derived results tracking, and comprehensive testing strategies."
tags: ["FHIR", "HL7", "Data Modeling", "FISH", "Logical Models", "Healthcare IT"]
categories: ["Technical", "Healthcare Standards", "Architecture"]
featured_image: "/images/fhir-logical-models-mapping.png"
---

# FHIR Data Modeling via FISH: Leveraging Logical Models and Mapping for Advanced Scenarios

FISH (Fluent Implementation Syntax) has transformed how we define FHIR artifacts, but its real power emerges when combined with logical models—a pairing that enables sophisticated data modeling scenarios that would be unwieldy to express in profile-first approaches. This article explores how logical models and mapping work together to construct complex, testable data models.

## The Case for Logical Models in FHIR Design

Logical models represent domain concepts independent of FHIR's predefined structure. Rather than immediately constraining a Patient or Observation resource, a logical model describes *what data you actually need* from your use case. This separation of concerns is powerful: you design the conceptual model first, then map it to FHIR later—or map it to multiple FHIR versions, regulatory profiles, or even non-FHIR targets.

Consider a laboratory result reporting scenario. Your domain requires:

- Patient identity and lab context
- Multiple test orders and results with temporal relationships
- Quality metadata and interpretive comments
- Lineage tracking for derived values
- Integration with quality assurance workflows

A pure profile-first approach forces you to immediately decide which FHIR resources carry which concepts. A logical model lets you express the domain structure cleanly, then strategize mapping.

![Logical models and mappings](/images/fhir-logical-models-mapping.svg)

## Defining Logical Models with FISH

FISH syntax for logical models is direct:

```fish
Logical: LabResultReport
Title: "Laboratory Result Report Logical Model"
Description: "Domain model for structured lab reporting"

* reportId: string "Unique report identifier"
* subject: Person "Subject of the report"
* orderContext: OrderContext "Lab order and request details"
* results: BackboneElement {0..} "Reported test results"
  * testName: CodeableConcept "Identification of the test performed"
  * resultValue: Quantity "Measured value"
  * refRange: Quantity {0..1} "Reference interval"
  * resultDate: dateTime "When the result was obtained"
  * qualityFlags: Coding {0..} "Quality indicators (suspected duplicate, critical value, etc.)"
* qaWorkflow: WorkflowStatus {0..1} "QA review state and sign-off"

Logical: Person
* identifier: Identifier {1..} "National ID, medical record number, etc."
* name: HumanName
* dateOfBirth: date {0..1}
* contact: ContactPoint {0..*}

Logical: OrderContext
* orderNumber: string
* orderDate: dateTime
* requestingProvider: Person
* clinicalIndication: CodeableConcept {0..1}
```

This logical model makes implicit assumptions explicit. It doesn't force you into Observation + DiagnosticReport decomposition immediately—that's a *mapping decision*, not a modeling decision.

## Mapping Logical Models to FHIR Profiles

Mapping connects logical model elements to FHIR resources. FISH supports ConceptMap-style expressions that document these connections:

```fish
Mapping: LabReportToFHIR
Source: LabResultReport
Target: "FHIR"
Title: "Logical Model to FHIR R4 Mapping"

* reportId -> "DiagnosticReport.identifier"
* subject -> "DiagnosticReport.subject"
* orderContext.orderNumber -> "DiagnosticReport.basedOn.identifier"
* orderContext.orderDate -> "DiagnosticReport.issued"
* orderContext.requestingProvider -> "DiagnosticReport.performer"
* results -> "Observation (multiply-instantiated)"
* results.testName -> "Observation.code"
* results.resultValue -> "Observation.value[x]"
* results.refRange -> "Observation.referenceRange.high and .low"
* results.resultDate -> "Observation.effective[x]"
* results.qualityFlags -> "Observation.status, Observation.interpretation, custom extension"
* qaWorkflow -> "DiagnosticReport.status + Task resource for pending review"
```

The mapping documents architectural decisions. Here, a single logical model becomes multiple FHIR resources: DiagnosticReport as the container, Observation for each result, and optionally Task for QA workflow. This is *transparent* in the mapping—implementers see the rationale rather than reverse-engineering it from nested profiles.

## Advanced Scenarios: Combining Models and Mappings

Real-world complexity emerges when you need to support multiple scenarios from one logical model. Consider:

**Scenario 1: Direct Lab Reporting** — A simple case where results flow from analyzer to ordering system.

**Scenario 2: Multi-Step QA** — Results enter pending state, pass through review workflows, then finalize.

**Scenario 3: Derived Results** — Some results are calculated from raw measurements; tracking lineage is critical for quality assurance.

Rather than create separate logical models for each, define *variants* within a single model and use conditional mapping:

```fish
Logical: LabResultReport
Title: "Laboratory Result Report with QA Variants"
Description: "Unified logical model supporting simple and complex workflows"

* reportId: string
* reportingMode: code {0..1} "Values: SIMPLE | QA_PENDING | DERIVED"
* subject: Person
* orderContext: OrderContext
* results: LabResult {1..}
  * testName: CodeableConcept
  * resultValue: Quantity
  * refRange: Quantity {0..1}
  * isDerived: boolean {0..1}
  * sourceResults: string {0..} "IDs of results used in derivation (only if isDerived=true)"
  * qualityFlags: Coding {0..}

Mapping: LabReportToFHIRWithVariants
Source: LabResultReport
Target: "FHIR"
Title: "Conditional mapping based on reporting mode"

* reportingMode = "SIMPLE" -> "DiagnosticReport.status = 'final'"
* reportingMode = "QA_PENDING" -> "DiagnosticReport.status = 'preliminary' + Task for review"
* reportingMode = "DERIVED" -> "Observation.derivedFrom = [references to source Observations]"
* isDerived = true -> "Observation.category = 'derived' (custom code)"
```

This approach scales: you add reporting modes, lineage tracking, and QA states *to the logical model*, making the domain assumptions explicit. Implementers building to the profile see these decisions documented in the mapping.

## Testing Logical Models and Mappings

Validation spans three levels:

**1. Logical Model Validation**
Ensure data conforms to logical model cardinality, data types, and constraints:

```fish
Instance: LabReportExample
InstanceOf: LabResultReport
Title: "Sample Lab Report"

* reportId = "LR-2024-001234"
* subject.identifier[0].system = "http://example.org/mrn"
* subject.identifier[0].value = "MRN-456789"
* subject.name[0].text = "Jane Doe"
* orderContext.orderNumber = "ORD-2024-5678"
* orderContext.orderDate = 2024-05-10T09:00:00Z
* results[0].testName = http://loinc.org#2345-7 "Glucose [mg/dL]"
* results[0].resultValue = 95 'mg/dL'
* results[0].resultDate = 2024-05-10T09:30:00Z
```

**2. Mapping Validation**
Verify that mappings are complete and consistent. Tools like FHIR Mapping Language (FML) can formally specify transformations:

```fish
group LabReportToFHIR(source report: LabResultReport, target bundle: Bundle) {
  bundle.entry as entry then {
    report -> entry.resource = create("DiagnosticReport") as dr then {
      report.reportId -> dr.identifier;
      report.subject as subj -> dr.subject = create("Reference") as ref then {
        subj.identifier[0].value -> ref.identifier.value;
      };
    };
    report.results as result -> bundle.entry as obsEntry then {
      result -> obsEntry.resource = create("Observation") as obs then {
        result.testName -> obs.code;
        result.resultValue -> obs.value;
        result.isDerived = true -> obs.derivedFrom = ...;
      };
    };
  };
}
```

**3. Profile Conformance**
Once mapped to FHIR profiles, instances must validate against both the logical model *and* the FHIR profile constraints:

```fish
Instance: LabReportDiagnosticReport
InstanceOf: DiagnosticReport
Title: "DiagnosticReport instance from LabReportExample mapping"

* identifier.system = "http://example.org/labrid"
* identifier.value = "LR-2024-001234"
* status = #final
* code = http://loinc.org#80567 "Clinical Laboratory Tests"
* subject = Reference(PatientFromReport)
* issued = 2024-05-10T09:30:00Z
* basedOn = Reference(ServiceRequest)
* result = Reference(GlucoseObservation)

Instance: GlucoseObservation
InstanceOf: Observation
* code = http://loinc.org#2345-7 "Glucose [mg/dL]"
* valueQuantity = 95 'mg/dL'
* status = #final
* effectiveDateTime = 2024-05-10T09:30:00Z
```

Validation tooling (FSH implementation guides, IG publishers) will catch mismatches: if the logical model says `refRange` is optional but the profile requires it, or if a mapping claims to populate a required field that the logical model leaves empty.

## Testing Strategy

A robust testing approach combines:

**Unit Tests**: Does the logical model capture domain requirements accurately? Do instances populate correctly?

**Integration Tests**: Do mappings produce valid FHIR profiles? Do FHIR instances successfully conform?

**Scenario Tests**: Can you represent all three reporting modes (simple, QA-pending, derived) in both logical and FHIR forms?

**Terminology Tests**: Are all CodeableConcept bindings correct? Do quality flags map to the right codes?

```fish
Instance: TestSimpleReport
InstanceOf: LabResultReport
* reportingMode = #SIMPLE
* results[0].qualityFlags = http://example.org/flags#normal-operation
// Should map cleanly to DiagnosticReport.status = final

Instance: TestDerivedReport
InstanceOf: LabResultReport
* reportingMode = #DERIVED
* results[0].isDerived = true
* results[0].sourceResults[0] = "ResultID-111"
// Should produce Observation.derivedFrom references

Instance: TestQAPending
InstanceOf: LabResultReport
* reportingMode = #QA_PENDING
* qaWorkflow.reviewState = #pending_review
// Should map to preliminary status + Task creation
```

## Conclusion

Logical models and FISH mappings work synergistically: logical models let you reason about domain data *before* committing to FHIR structure, while mappings document the architectural choices that bridge them. For advanced scenarios—lineage tracking, multi-step workflows, derived calculations—this separation allows you to scale complexity without drowning in constraint details.

The payoff is transparency: implementers see not just "here's the profile," but "here's why we made these FHIR choices." And testing becomes tractable: validate the logical model, validate the mapping, validate FHIR conformance—each layer is independently verifiable.

Start with a clean logical model. Make mapping decisions explicit. Test at all three levels. You'll find that complex scenarios become manageable, and maintainability improves dramatically.
