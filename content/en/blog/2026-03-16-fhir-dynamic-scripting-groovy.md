---
title: "Dynamic FHIR Logic: Hot-Reloading Business Rules with Groovy"
date: 2026-03-16T10:01:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "Groovy", "Architecture", "Extensibility", "HAPI FHIR"]
categories: ["Engineering", "Healthcare"]
description: "Learn how to extend your HAPI FHIR server at runtime using Groovy scripts, allowing for hot-reloadable Interceptors and Resource Providers."
featured_image: "/images/groovy_scripting.png"
---

# Dynamic FHIR Logic: Hot-Reloading Business Rules with Groovy

As a healthcare architect, one of the most frustrating scenarios is having to redeploy an entire FHIR server just to change a small validation rule or add a simple custom endpoint. In highly regulated environments, a deployment can trigger a massive QA cycle. 

What if you could push logic changes as easily as you push data?

In this tutorial, we’ll look at how I implemented **Dynamic Scripting** using Groovy in my [HAPI FHIR Groovy](https://github.com/gjergjsheldija/hapi-fhir-groovy) server.

## The Architecture
The core idea is to leverage the FHIR `Configuration` resource as a container for code. A custom `GroovyClassLoader` monitors these resources and dynamically registers Spring beans (Interceptors and Providers) into the HAPI FHIR context.

## Tutorial: Creating a Dynamic Interceptor

### Step 1: Write the Script
Your script must be a valid Groovy class tagged with `@CustomScript` and standard HAPI annotations.

```groovy
package scripting

import ca.uhn.fhir.interceptor.api.Hook
import ca.uhn.fhir.interceptor.api.Interceptor
import ca.uhn.fhir.interceptor.api.Pointcut
import com.gjergjsheldija.scripting.api.CustomScript
import groovy.util.logging.Slf4j

@Slf4j
@Interceptor
@CustomScript
class PatientLogger {
    @Hook(Pointcut.STORAGE_PRESTORAGE_RESOURCE_CREATED)
    void execute(theResource) {
        if (theResource instanceof org.hl7.fhir.r4.model.Patient) {
            log.info("Interception! New patient being saved: ${theResource.name[0].family}")
        }
    }
}
```

### Step 2: Upload as a Configuration Resource
Wrap your script in a FHIR `Configuration` resource. The `name` must match the class name.

```http
POST /Configuration
Content-Type: application/fhir+json

{
  "resourceType": "Configuration",
  "name": "PatientLogger",
  "type": "script",
  "status": "active",
  "body": "... (the script above) ..."
}
```

### Step 3: Trigger the Load
To tell the server to compile and register the new logic, call the `$load-script` operation:

```http
POST /Configuration/$load-script
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    { "name": "name", "valueString": "PatientLogger" }
  ]
}
```

## Testing Your Scripts: The Spock Advantage
Logic that changes at runtime must be tested even more rigorously than static code. One of the best synergies in the Groovy world is the **Spock Framework**.

In our repository, you'll find examples of how we test these dynamic scripts using Spock specifications. Because Groovy and Spock share the same DNA, you can write highly expressive tests that mock HAPI FHIR DAOs and verify clinical logic with ease.

### Example: A Spock Specification
Here is how you can test a complex calculation script by mocking the database layer:

```groovy
class OutputCalculationTest extends Specification {
    def "test calculatedOutput method"() {
        given: "a mocked environment"
        def observationDao = Mock(IFhirResourceDaoObservation)
        def outputCalculation = new OutputCalculation(observationDao: observationDao)

        and: "some sample FHIR data"
        def observations = parser.parseResource(Bundle, observationsJson).entry.collect { it.resource }
        observationDao.searchForResources(_, _) >> observations

        when: "the calculation logic is triggered"
        def result = outputCalculation.calculatedOutput(encounterRef, intervalMinutes, dateFrom, dateTo, requestDetails)

        then: "the output matches clinical expectations"
        result.entry.size() == 12
        result.entry[0].resource.valueQuantity.value == 75.5
    }
}
```

By keeping your tests in the `src/test/java` folder alongside your Java tests, you ensure that even your dynamic scripts are part of your core CI/CD quality gate.

## Why Groovy?
Beyond being a first-class citizen in the Java ecosystem (JSR-223), Groovy offers a "nearly-native" performance once the scripts are compiled by the JVM's JIT. For healthcare systems, this means we get the flexibility of scripting without the typical interpreted language overhead.

## The Architect's Concern: Security and Sandboxing
Injecting code at runtime is a double-edged sword. As architects, we must address the "elephant in the room": **Sandboxing**.
- **Package Restrictions**: Our class loader restricts scripts from accessing sensitive system packages (e.g., `java.lang.reflect` or `java.io` directly).
- **Execution Context**: Scripts run within the restricted Spring Security context of the server.
- **Auditability**: Every script upload or load event is captured by the `AuditEvent` subsystem, ensuring a clear "chain of custody" for your server's logic.

## Why This Matters
From an architect's perspective, this moves your FHIR server from being a "black box" to a **programmable platform**. It allows for:
- **Fast Prototyping**: Test new logic in seconds without a redeploy.
- **Client-Specific Rules**: Inject custom logic for specific tenants or integration partners.
- **Emergency Fixes**: Patch critical validation bugs (e.g., during a zero-day or a data quality crisis) without a full CI/CD pipeline run.

---
*Ready to dive deeper? Check the documentation in [`doc/scripting.md`](https://github.com/gjergjsheldija/hapi-fhir-groovy/blob/main/doc/scripting.md).*
