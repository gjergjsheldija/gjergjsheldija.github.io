---
title: "FHIR Transformation Is Solved. Semantic Validation Is Not."
date: 2026-06-12
draft: true
description: "Passing $validate is not the same as being clinically correct. Here is what semantic validation looks like in practice: terminology coherence using SNOMED CT and LOINC's internal structure, and CQL-based clinical invariants that span resources and time."
tags: ["FHIR", "Semantic Validation", "CQL", "SNOMED CT", "LOINC", "Patient Safety", "HL7", "FHIRPath", "Terminology"]
categories: ["Technical", "Healthcare Standards", "Engineering"]
featured_image: "/images/fhir-semantic-validation.png"
---

# FHIR Transformation Is Solved. Semantic Validation Is Not.

The transformation problem is largely done. Tools like HAPI FHIR, Smile CDR, Aidbox, and the major cloud healthcare APIs handle HL7v2-to-FHIR, CDA-to-FHIR, and proprietary-format-to-FHIR conversion at production scale. You can wire up a pipeline, point it at your legacy system, and produce syntactically valid FHIR R4 bundles. The `$validate` operation passes. The IG publisher is happy.

And then a glucose observation shows up with an `effectiveDateTime` two months before the patient's `birthDate`. It passes validation. Or a `Condition` resource coded as "fracture of the femur" carries a `bodySite` of "left ear." That passes too. So does a urine-specific LOINC observation attached to a blood draw `Specimen`. So does a troponin result with no temporal relationship to the admission it supposedly supports.

None of these are structural errors. They are semantic errors. The resources are valid FHIR. The data is clinically wrong.

This matters at two levels that rarely talk to each other: patient safety and engineering accountability. Both are getting worse as FHIR adoption scales.

## The Two Failure Modes, and Why Each Is Serious

From a patient safety perspective, this class of error is not a data quality annoyance. It is a decision support liability. Clinical decision support rules, AI pipelines, and quality measures all consume FHIR data and assume it is semantically coherent. A CDS rule that checks for troponin within 24 hours of admission will silently fail if the troponin observation exists but carries wrong temporal metadata from a bad transformation. The rule evaluates to false. The alert does not fire. No exception is thrown, because structurally everything is fine.

In a regulated context, particularly under EU MDR and German DiGA requirements, this is not theoretical. Software that influences clinical decisions is a medical device. Feeding that device semantically incoherent data is a safety defect, not a configuration issue. The IEC 62304 software lifecycle standard requires that safety-relevant inputs be validated. "It passed `$validate`" does not satisfy that requirement.

The VP of Engineering view is different but equally uncomfortable. Teams measure data quality by validation pass rates. If `$validate` returns green, the pipeline is considered healthy. That framing gives false confidence, because what you are measuring is structural conformance: a necessary condition for correctness, nowhere near sufficient.

When a semantic error surfaces, it surfaces late: in a clinical audit, in a regulatory review, or in a patient outcome. At that point, root cause analysis goes back to the ingestion pipeline, and the engineering team has to explain why a system that passed all its tests produced clinically wrong data. The answer, usually, is that nobody defined what "correct" meant beyond structural conformance. That is a requirements gap, and it belongs to engineering leadership to close it.

There is also a compounding risk specific to AI. FHIR data is increasingly used as training input for clinical ML models. Semantically incoherent training data does not produce obvious errors during training. It produces models that learn wrong associations quietly. A model trained on glucose observations with corrupted temporal metadata will behave incorrectly at inference, and you will not know why until something clinical goes wrong downstream.

## Two Approaches to Semantic Validation

The structural layer is handled by profile validators. Semantic validation requires two additional layers, which can be introduced independently at different points in your pipeline.

The first addresses terminology coherence: using SNOMED CT's and LOINC's internal structure to catch codes used in the wrong context. The second addresses clinical invariants: using Clinical Quality Language (CQL) to express constraints that span resources, require temporal reasoning, and encode actual clinical rules.

---

## Terminology Coherence Validation

SNOMED CT is not a flat list of codes. Every concept lives within a polyhierarchical structure with explicit relationships: `finding site`, `associated morphology`, `procedure site`, `causative agent`. LOINC is multi-axial: each code encodes the system (the specimen or body region), component (what you're measuring), method, and scale.

Most FHIR validators treat these as opaque strings. They check whether a code is a member of the bound ValueSet. They do not check whether the code's relationships are coherent with the other data in the resource.

The coherence problem is this: "fracture of the femur" (SNOMED 71620004) has a `finding site` of "bone structure of femur." A `bodySite` of "left ear" (SNOMED 25577004) is not in any subsumption path connecting to femur. A validator that checks SNOMED's relationship model would catch this. Standard `$validate` does not. Same pattern with LOINC: LOINC 5778-6 ("Color of Urine") carries a system axis of "Urine." Attaching this observation to a blood draw `Specimen` is coherent in structure, wrong in fact.

### FHIRPath Invariants for Structural Coherence

FHIRPath can encode some coherence rules directly in a profile as invariants. They run during `$validate`, are part of the IG, and require no external dependencies. This is the right place for rules that can be expressed without terminology server lookups:

```
Invariant: obs-effective-after-birthdate
Description: "Observation effectiveDateTime must not predate the patient's birthDate"
Expression: "effective.ofType(dateTime).exists() implies (
  subject.resolve().ofType(Patient).birthDate.exists() implies
    effective.ofType(dateTime) >= subject.resolve().ofType(Patient).birthDate
)"
Severity: #error
Source: Observation
```

```
Invariant: obs-specimen-code-present
Description: "If a specimen is referenced, a LOINC code must be present to enable system-axis validation"
Expression: "specimen.exists() implies code.coding.where(system = 'http://loinc.org').exists()"
Severity: #warning
Source: Observation
```

These run fast, need no network calls, and catch the structurally detectable mismatches. For the semantic ones, you need a terminology server.

### Subsumption Checks via the Terminology Service API

FHIR's terminology service API defines `$subsumes` as a standard operation. Any compliant terminology server (Ontoserver, CSIRO's Snowstorm, or Firely's Forge) can answer subsumption queries. The operation returns one of: `equivalent`, `subsumes`, `subsumed-by`, or `not-subsumed`.

For the body site coherence check:

```java
// Does the body site fall within the finding site of the condition code?
// If not-subsumed, the combination is clinically incoherent.

Parameters params = new Parameters();
params.addParameter().setName("system").setValue(new UriType("http://snomed.info/sct"));
params.addParameter().setName("codeA").setValue(new CodeType(bodySiteCode));      // e.g. "25577004" (left ear)
params.addParameter().setName("codeB").setValue(new CodeType(conditionFindingSite)); // e.g. "71341001" (femur structure)

Parameters result = terminologyClient
    .operation()
    .onType(CodeSystem.class)
    .named("$subsumes")
    .withParameters(params)
    .execute();

String outcome = result.getParameter("outcome").getValue().primitiveValue();
// "not-subsumed" = incoherent combination
```

To get `conditionFindingSite`, you call `$lookup` on the condition code and extract the `finding site` property from the SNOMED concept. This is two round trips to the terminology server per resource. Cache the lookup results. SNOMED concept properties do not change between releases, and releases happen twice a year.

### A Coherence Validator That Runs Post-Ingestion

Rather than embedding all of this in the FHIR server's validation chain, a separate coherence validator running post-ingestion is more practical. It runs asynchronously, produces structured results, and is deployable and testable independently of the FHIR server configuration.

```java
public class TerminologyCoherenceValidator {

    private final ITerminologyServiceClient terminologyClient;
    private final ConceptPropertyCache propertyCache;

    public List<CoherenceFailure> validate(Observation obs, Patient patient) {
        List<CoherenceFailure> failures = new ArrayList<>();

        // 1. Temporal coherence: effectiveDateTime must be after birthDate
        if (obs.hasEffectiveDateTimeType() && patient.hasBirthDate()) {
            Date effective = obs.getEffectiveDateTimeType().getValue();
            Date birthDate = patient.getBirthDate();
            if (effective.before(birthDate)) {
                failures.add(new CoherenceFailure(
                    "TEMPORAL-001",
                    IssueSeverity.ERROR,
                    "effectiveDateTime " + effective + " predates patient birthDate " + birthDate
                ));
            }
        }

        // 2. LOINC system-axis against specimen type
        if (obs.hasSpecimen() && obs.hasCode()) {
            String loincCode = extractLoincCode(obs.getCode());
            String specimenSnomedCode = resolveSpecimenSnomedCode(obs.getSpecimen());

            if (loincCode != null && specimenSnomedCode != null) {
                String loincSystem = propertyCache.getLoincProperty(loincCode, "SYSTEM");
                String loincSystemSnomedCode = mapLoincSystemToSnomed(loincSystem);

                if (loincSystemSnomedCode != null) {
                    String subsumption = checkSubsumes(specimenSnomedCode, loincSystemSnomedCode);
                    if ("not-subsumed".equals(subsumption)) {
                        failures.add(new CoherenceFailure(
                            "SPECIMEN-001",
                            IssueSeverity.ERROR,
                            "LOINC " + loincCode + " (system: " + loincSystem + ") " +
                            "is not appropriate for specimen type " + specimenSnomedCode
                        ));
                    }
                }
            }
        }

        return failures;
    }

    private String checkSubsumes(String codeA, String codeB) {
        Parameters params = new Parameters();
        params.addParameter("system", "http://snomed.info/sct");
        params.addParameter("codeA", codeA);
        params.addParameter("codeB", codeB);

        Parameters result = terminologyClient.operation()
            .onType(CodeSystem.class)
            .named("$subsumes")
            .withParameters(params)
            .execute();

        return result.getParameter("outcome").getValue().primitiveValue();
    }
}
```

The output feeds a quality dashboard. Resources with coherence failures stay in a `pending` state, go to a review queue, or get flagged in audit logs: your call, depending on severity. The point is that the failure surfaces at ingestion rather than in a clinical audit six months later.

The standards in play here: SNOMED CT (maintained by SNOMED International, also published as ISO 17115 for the concept model), LOINC (Regenstrief Institute), FHIRPath (HL7 normative specification, part of FHIR R4 and R5), and the FHIR Terminology Service API which defines `$subsumes`, `$lookup`, and `$validate-code` as standard operations.

---

## Clinical Invariants via CQL

Terminology coherence catches problems within a single resource or a resource-plus-terminology call. It does not catch problems that span multiple resources, require temporal reasoning across an encounter, or encode actual clinical rules. That requires a different tool.

Clinical Quality Language (CQL) is an HL7 standard built for exactly this. It is widely used for eCQMs (electronic clinical quality measures) and CDS Hooks. Almost nobody uses it for validation. It is the right fit for that job.

The difference between CQL-for-quality-measures and CQL-for-validation is subtle but worth stating clearly. A quality measure asks: "For patients in this population, did this thing happen?" A validation rule asks: "For this specific resource bundle, is this clinical constraint satisfied?" The language is identical. The evaluation cardinality is different: one patient bundle at a time, fail-fast, with a specific error message.

### Writing a Clinical Invariant in CQL

Here is a concrete example: a patient discharged with a primary diagnosis of myocardial infarction (ICD-10 I21.x) must have at least one troponin observation within 24 hours of admission. This constraint cannot be expressed in a FHIR profile. It requires knowing which `Condition` is the discharge diagnosis, knowing the `Encounter` period, and evaluating `Observation` timestamps relative to it. In CQL, this is about 30 lines:

```cql
library SemanticValidation version '1.0'

using FHIR version '4.0.1'

include FHIRHelpers version '4.0.1' called FHIRHelpers

codesystem "ICD-10-CM": 'http://hl7.org/fhir/sid/icd-10-cm'
codesystem "LOINC": 'http://loinc.org'

// Covers STEMI (I21.0-I21.3), NSTEMI (I21.4), and unspecified (I21.9)
valueset "Myocardial Infarction Diagnoses":
  'http://example.org/fhir/ValueSet/mi-diagnoses'

// Troponin I (10839-9), Troponin T (6598-7), high-sensitivity variants included
valueset "Troponin Observation Codes":
  'http://example.org/fhir/ValueSet/troponin-loinc'

parameter "Encounter" Encounter

context Patient

define "Admission DateTime":
  FHIRHelpers.ToDateTime("Encounter".period.start)

define "Has MI Discharge Diagnosis":
  exists(
    ["Condition"] C
      where C.encounter ~ "Encounter"
        and C.clinicalStatus ~ 'active'
        and C.code in "Myocardial Infarction Diagnoses"
        and C.category.coding.exists(c | c.code = 'encounter-diagnosis')
  )

define "Troponin Within 24h Of Admission":
  ["Observation": code in "Troponin Observation Codes"] O
    where O.encounter ~ "Encounter"
      and O.status in { 'final', 'amended', 'corrected' }
      and FHIRHelpers.ToDateTime(O.effective as FHIR.dateTime)
          during Interval[
            "Admission DateTime",
            "Admission DateTime" + 24 hours
          ]

define "Has Troponin Within 24h":
  exists("Troponin Within 24h Of Admission")

define "MI Workup Semantically Valid":
  if "Has MI Discharge Diagnosis"
  then "Has Troponin Within 24h"
  else true

// This is what the validation runner evaluates.
// Empty list = valid. Non-empty = failures with rule IDs.
define "Validation Failures":
  if not "MI Workup Semantically Valid"
  then { 'MI discharge diagnosis without troponin within 24h [SEMANTIC-MI-001]' }
  else { }
```

A clinical informaticist can read and verify this. You can add a new rule by adding a new `define`. You can unit test each `define` independently with a synthetic FHIR Bundle. This is executable clinical specification, and it can live in the same version control repository as your implementation guides.

### Integrating CQL Evaluation into the Pipeline

The open-source `cql-evaluator` library from the cqframework project provides a Java-based CQL execution engine. Wrapping it in a validation service looks like this:

```java
public class CqlSemanticValidator {

    private final LibraryLoader libraryLoader;
    private final CqlEvaluator evaluator;

    // validationLibraries: map of library ID to CQL Library resource
    public ValidationReport validate(Bundle patientBundle, Encounter encounter) {
        DataProvider fhirDataProvider = new BundleDataProvider(patientBundle);

        List<SemanticFailure> allFailures = new ArrayList<>();

        for (String libraryId : libraryLoader.getValidationLibraryIds()) {
            Library library = libraryLoader.load(libraryId);

            Map<String, Object> parameters = Map.of("Encounter", encounter);

            EvaluationResult result = evaluator.evaluate(
                library,
                Set.of("Validation Failures"),
                parameters,
                fhirDataProvider
            );

            @SuppressWarnings("unchecked")
            List<String> failures = (List<String>) result.expressionResults
                .get("Validation Failures")
                .value();

            if (failures != null && !failures.isEmpty()) {
                allFailures.add(new SemanticFailure(libraryId, failures));
            }
        }

        return new ValidationReport(encounter.getId(), allFailures);
    }
}
```

Each rule library is loaded independently, so you can add, update, or disable rules without touching the validator itself. The `ValidationReport` contains structured failure objects with rule IDs, which map to documentation, remediation steps, and clinical rationale. Not just "this failed" but "here is why and here is what to do."

Run this after structural validation passes. Structural validation is synchronous and fast. CQL evaluation depends on the full patient context and is heavier. Keep them as separate pipeline stages:

```
Ingest → Structural ($validate) → persist if valid → async CQL semantic pass
                                                    → flag failures
                                                    → route to review queue
```

Resources that fail semantic validation do not have to be rejected outright. They can be flagged, routed to a manual review workflow, or quarantined from AI training sets while still being available for clinical review. The failure record gives the reviewer the specific rule that fired and the data that triggered it.

The standards here: CQL is ANSI/HL7 CQL R1 (2019), updated with R1.5 in 2023. FHIRPath, which CQL uses for its FHIR navigation layer, is a normative part of the FHIR specification from R4 onward. Both have open-source implementations, stable versioning, and are actively maintained by HL7.

---

## What This Actually Changes

The gap between transformation and semantic validation is the gap between "does this data conform to a schema" and "is this data clinically true." Closing that gap does two things that are usually treated as separate concerns.

For patient safety: it removes a class of errors that currently propagates silently through the stack. Semantically wrong data does not throw exceptions. It produces wrong outputs downstream: CDS rules that fail to fire, AI models trained on incoherent inputs, quality measures that undercount. Catching these errors at ingestion, before they reach the clinical layer, is the only point in the pipeline where correction is cheap. By the time a semantic error surfaces in a clinical audit, the cost of correction has compounded.

For engineering: it gives the team a concrete, testable definition of "correct" that goes beyond green validation indicators. Semantic validation rules are executable specifications. They are checkable against synthetic and real data in CI. They can be version-controlled alongside profiles and implementation guides. When a rule fires, the error message is specific: not "validation error in resource X" but "Encounter E12345 has MI discharge diagnosis without troponin within 24h [SEMANTIC-MI-001]." That is a root-cause-ready finding.

Both of these outcomes follow from treating clinical correctness as a first-class engineering requirement, the same way structural conformance already is. The tools are available and standardized: CQL, FHIRPath, SNOMED CT's relationship model, LOINC's multi-axial structure. The HL7 terminology service API is stable and implemented by multiple servers. The CQL execution engine is open source. None of this requires custom infrastructure.

The only thing missing has been the decision to use these standards for validation rather than just interoperability. The transformation problem forced that decision for structural conformance. The semantic layer is where the next round of pressure is coming from: regulatory scrutiny of AI in clinical workflows, MDR requirements for SaMD inputs, and the accumulated cost of silent semantic errors in production systems.

Structural conformance was always the floor, not the ceiling.
