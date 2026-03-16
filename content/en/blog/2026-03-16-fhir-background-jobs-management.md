---
title: "Heavy Lifting: Managing Background Jobs in HAPI FHIR"
date: 2026-03-16T10:06:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "Batch", "Performance", "Architecture", "HAPI FHIR"]
categories: ["Engineering", "Healthcare"]
description: "Master the art of managing long-running FHIR tasks like Bulk Export and Reindexing, and learn how to implement your own scheduled jobs."
featured_image: "/images/fhir_batch_jobs.png"
---

# Heavy Lifting: Managing Background Jobs in HAPI FHIR

FHIR servers don't just handle real-time requests. They also perform "heavy lifting" tasks: reindexing the database after a profile change, exporting millions of resources (Bulk Export), or running terminology updates. 

If these jobs aren't managed correctly, they can consume all your server's resources and crash your API. In this post, we'll look at how to control background work in [hapi-fhir-groovy](https://github.com/gjergjsheldija/hapi-fhir-groovy).

## Native vs. Custom Jobs
We categorize background work into two types:
1. **Native Jobs**: The built-in HAPI FHIR batch framework (Bulk Import/Export, Reindex).
2. **Custom Jobs**: Business-specific tasks (e.g., a daily report generator) written in Groovy.

## Tutorial: Controlling Native Jobs

### Step 1: Monitor Running Jobs
The server exposes an API to list and check the status of active batch tasks.

```http
GET /control/jobs?jobStatus=IN_PROGRESS
```
This returns a list of job instances, including their start time and progress status (e.g., `QUEUED`, `IN_PROGRESS`, `COMPLETED`, `FAILED`).

### Step 2: Canceling a "Runaway" Job
If a massive export is killing your database performance, you can cancel it using the `instanceId`:

```http
DELETE /control/jobs?instanceId=7c74a5c8...
```

## Tutorial: Implementing a Custom Scheduled Job
Thanks to our Dynamic Scripting engine, you can write background jobs in Groovy and push them to the server without a restart.

### Step 1: Write the Job Script
Use the `@EnableScheduling` and `@Scheduled` annotations.

```groovy
package com.gjergjsheldija.jobs

import com.gjergjsheldija.scripting.api.CustomScript
import org.springframework.scheduling.annotation.EnableScheduling
import org.springframework.scheduling.annotation.Scheduled
import groovy.util.logging.Slf4j

@Slf4j
@CustomScript
@EnableScheduling
class DataCleanupJob {

    @Scheduled(cron = "0 0 1 * * ?") // Runs every day at 1:00 AM
    void cleanup() {
        log.info("Starting maintenance cleanup...")
        // Your logic here
    }
}
```

### Step 2: Environment Toggles
You can disable all native job scheduling by setting the `JOB_SCHEDULING` environment variable to `false`. This is useful for secondary nodes in a cluster where you only want the primary node to handle background processing.

## The Architect's Concern: Transactionality vs. Batch
Running heavy jobs on a live clinical database requires careful consideration of **Transaction Isolation**:
- **Native HAPI Jobs**: Use a "Chunk-based" processing model. If a job fails halfway, you can restart it, and it will pick up from the last successful chunk.
- **Custom Jobs**: Ensure your Groovy logic handles transactions correctly. Use `@Transactional` if you're making multiple writes, or better yet, design your jobs to be **Idempotent** so they can safely re-run after a crash.

## The Architect's Verdict
Managing background work is about **Resource Isolation**. By knowing how to monitor, cancel, and inject custom scheduling, you ensure that your server stays responsive to the clinicians and apps that rely on it, even while processing millions of records in the background.

---
*For more details, check [`doc/background-jobs.md`](https://github.com/gjergjsheldija/hapi-fhir-groovy/blob/main/doc/background-jobs.md).*
