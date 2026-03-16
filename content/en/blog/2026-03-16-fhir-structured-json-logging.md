---
title: "Structured Insights: JSON Logging for FHIR Operations"
date: 2026-03-16T10:09:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "Logging", "DevOps", "ELK", "Splunk", "Architecture"]
categories: ["Engineering", "Healthcare"]
description: "Plain text logs are for humans; structured logs are for automation. Learn how to implement JSON logging that makes debugging FHIR traffic easy."
featured_image: "/images/hapi-fhir.png"
---

# Structured Insights: JSON Logging for FHIR Operations

Every request to a FHIR server carries a wealth of information: Who made the request? What resources were read? How long did it take? Was the operation successful? 

While standard logs might show `INFO: GET /Patient/1`, that’s not enough for modern DevOps. When you're managing a cluster handling thousands of requests, you need **Structured Logging**.

## Why JSON?
Structured logs (in JSON format) allow log aggregators like ELK (Elasticsearch, Logstash, Kibana), Splunk, or Datadog to index every field. This means you can run powerful queries like:
- *"Show me all Patient read operations that took more than 500ms."*
- *"Find all 403 errors for User X in the last hour."*

## The Log Structure
The [hapi-fhir-groovy](https://github.com/gjergjsheldija/hapi-fhir-groovy) server uses a `CustomLoggingInterceptor` to output every transaction in a clean, machine-readable format.

```json
{
  "time": "2026-03-16T09:15:00.000Z",
  "level": "INFO",
  "operation_type": "read",
  "id_resource_name": "Patient/1",
  "latency": "29",
  "latency_human": "29ms",
  "status": "200",
  "remote_ip": "127.0.0.1",
  "method": "GET"
}
```

## Tutorial: Configuring Log Detail

### Step 1: Request Body Logging
By default, we log the metadata but not the full resource body (to save space and avoid leaking PHI in some regions). However, during development, you might want the full picture:

```yaml
hapi:
  fhir:
    log_request_body: true
```

### Step 2: Custom Logback Integration
The server uses Logback. You can mount your own `logback.xml` into the Docker container to route these JSON logs to a file, to the console, or directly to a network socket (like Logstash).

```bash
docker run -v ./logback.xml:/logbackconfig/logback.xml ...
```

## Tutorial: Debugging with Dynamic Scripts
Since we have a scripting engine, we can inject specialized logging for a specific resource type without changing the global configuration:

```groovy
@Interceptor
@CustomScript
class ConditionDeepLogger {
    @Hook(Pointcut.SERVER_INCOMING_REQUEST_POST_PROCESSED)
    void logCondition(theRequestDetails) {
        if (theRequestDetails.resourceName == "Condition") {
            println("High-priority clinical condition accessed!")
        }
    }
}
```

## The Architect's Secret: Correlation IDs
Logging one server is easy. Logging a distributed system is hard. To solve this, our server utilizes **Correlation IDs** (often passed as `X-Request-ID` or `X-Correlation-ID`).
- **Tracing the Request**: Every log entry for a single FHIR transaction shares the same `request_id`.
- **Cross-System Analysis**: If your FHIR server calls an external Terminology service or a Lab system, passing this ID allows you to stitch together the logs from multiple systems into a single "distributed trace."

## The Architect's Verdict
Structured logging is the "black box" flight recorder for your FHIR server. When something goes wrong in production, having structured, searchable data—including resource IDs, request IDs, and latency—is the difference between resolving the issue in 5 minutes and spending 5 hours grepping through text files.

---
*For more details on the log format, see [`doc/logging.md`](https://github.com/gjergjsheldija/hapi-fhir-groovy/blob/main/doc/logging.md).*
