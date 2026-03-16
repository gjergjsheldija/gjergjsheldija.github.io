---
title: "Testing Healthcare APIs: Scenario-Based Certification with Karate"
date: 2026-03-16T10:03:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "Testing", "Karate DSL", "API", "QA"]
categories: ["Engineering", "Healthcare"]
description: "Why JUnit is not enough for testing FHIR servers and how to use Karate DSL to write expressive, clinical-scenario-based API tests."
featured_image: "/images/karate_testing.png"
---

# Testing Healthcare APIs: Scenario-Based Certification with Karate

Testing a FHIR server is notoriously difficult. Unlike a simple CRUD app, a FHIR server involves complex resource relationships, search parameter indexing, and versioned histories. 

While unit tests are great for logic, they don't give you confidence that your API actually *behaves* like a FHIR server should. For that, we need **Behavioral Integration Testing**.

## Why Karate DSL?
[Karate](https://github.com/karatelabs/karate) is a testing framework that allows you to write API tests using a Gherkin-like syntax. It is perfect for FHIR because:
- **Built-in JSON assertions**: Easily match complex FHIR bundles.
- **No boilerplate code**: Write tests in plain text, no Java required.
- **Scenario Focus**: You can model an entire patient journey in one file.

## Tutorial: Writing Your First FHIR Test

### Step 1: Create a Feature File
Let's test the creation and retrieval of a Patient. Create a file called `patient.feature`:

```gherkin
Feature: FHIR Patient API

  Background:
    * url 'http://localhost:8080/fhir'

  Scenario: Create a patient and verify their name
    Given path 'Patient'
    And request { resourceType: 'Patient', name: [{ family: 'Doe', given: ['John'] }] }
    When method post
    Then status 201
    * def patientId = response.id

    Given path 'Patient', patientId
    When method get
    Then status 200
    And match response.name[0].family == 'Doe'
```

### Step 2: Running Tests in the CI/CD Pipeline
In the [hapi-fhir-groovy](https://github.com/gjergjsheldija/hapi-fhir-groovy) repo, I’ve integrated Karate into the `docker-compose` stack. This ensures tests run against a clean, "real-world" environment.

Run them with a simple command:
```bash
make integration-tests
```

## Advanced Tutorial: Testing Custom Extensions
Since our server supports Dynamic Scripting, we can use Karate to verify that a new Groovy script works as expected:

```gherkin
Scenario: Verify dynamic business rule
  # 1. Upload a script that enforces a specific identifier
  Given path 'Configuration'
  And request read('identifier-check-script.json')
  When method post
  Then status 201

  # 2. Try to save a patient without that identifier
  Given path 'Patient'
  And request { resourceType: 'Patient', name: [{ family: 'Fail' }] }
  When method post
  Then status 400
  And match response.issue[0].diagnostics contains 'Missing required identifier'
```

## The Architect's Verdict: Certification vs. Testing
In a production healthcare environment, we don't just "test"; we **certify**. Karate allows us to create a certification suite that verifies:
- **Conformance**: Does the server correctly reject resources that don't match our profiles?
- **Search Logic**: Do complex nested search parameters work as expected?
- **Workflow Integrity**: Can a patient be created, enrolled in a clinical trial, and have their observations recorded in a single atomic-like sequence of API calls?

By using Karate, you create a "living documentation" of your API's capabilities. These tests can be shared with integration partners as a technical specification, ensuring that everyone knows exactly how the server will respond to specific clinical scenarios.

---
*Check out the sample tests in the `src/test/smoketest` and `docker-compose.yaml`.*
