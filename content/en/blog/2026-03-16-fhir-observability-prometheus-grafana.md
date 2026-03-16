---
title: "Observability at Scale: Prometheus and Grafana for FHIR"
date: 2026-03-16T10:05:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "Observability", "Prometheus", "Grafana", "DevOps", "Architecture"]
categories: ["Engineering", "Healthcare"]
description: "Stop flying blind. Learn how to integrate Prometheus and Grafana to gain real-time insights into your FHIR server's performance and health."
featured_image: "/images/fhir_monitoring.png"
---

# Observability at Scale: Prometheus and Grafana for FHIR

In healthcare IT, a slow FHIR server isn't just a technical nuisance—it can delay clinical care. If your API latency spikes, you need to know *why* before it impacts users. Is it a database connection pool exhaustion? A slow search parameter? Or a surge in requests?

To answer these questions, we need professional-grade observability. In this post, we’ll look at the integrated **Prometheus and Grafana** stack provided by [hapi-fhir-groovy](https://github.com/gjergjsheldija/hapi-fhir-groovy).

## The Monitoring Stack
We use a modern observability pattern:
1. **Application Layer**: Spring Boot Actuator with Micrometer exposes FHIR metrics.
2. **Scraper**: Prometheus collects these metrics every 15 seconds.
3. **Visualization**: Grafana provides a beautiful, real-time dashboard.

## Tutorial: Setting Up Monitoring

### Step 1: Launch the Stack
If you are using the repository's `docker-compose.yaml`, the Prometheus and Grafana services are already defined. Simply start them:

```bash
make start-prometheus
```

### Step 2: Accessing Metrics
Your FHIR server exposes metrics at the `/actuator/prometheus` endpoint. You can verify this by visiting `http://localhost:8080/actuator/prometheus`. You’ll see a list of metrics like:
- `fhir_request_latency_seconds`: Time taken for FHIR operations.
- `hikari_cp_active_connections`: Database connection health.
- `jvm_memory_used_bytes`: Memory usage.

### Step 3: Explore the Grafana Dashboard
Log in to Grafana at `http://localhost:3000` (default: `admin/admin`). 
The repository comes with pre-configured dashboards located in `config/grafana`. You'll find:
- **FHIR Server Dashboard**: Monitors request rates (TPS), average latency per resource type, and HTTP status codes (2xx vs 5xx).
- **Infinispan Dashboard**: If you're using remote caching, this monitors cache hit/miss ratios.

## Tutorial: Creating a Custom Alert
Monitoring is only useful if it notifies you of problems. In Grafana, you can easily create an alert for high latency:

1. **Add Panel**: Choose the `fhir_request_latency_seconds` metric.
2. **Define Alert**: Set a threshold (e.g., alert if the 95th percentile latency is > 2 seconds for more than 5 minutes).
3. **Notification**: Connect it to Slack, PagerDuty, or Email.

## Architectural Metric: The HAPI Pointcuts
Beyond standard JVM metrics, we expose specific HAPI FHIR "Pointcut" timings. This allows you to differentiate between:
- **DB Latency**: Time spent in the JPA layer.
- **Interceptor Latency**: Overhead added by our custom Groovy scripts or security checks.
- **Parser Latency**: Time spent converting JSON to internal POJOs.

## The Architect's Verdict: From Monitoring to SLOs
By integrating observability directly into your FHIR infrastructure, you move from reactive troubleshooting to proactive management. You can define and track **Service Level Objectives (SLOs)**, such as: *"99.9% of Patient Reads must be under 150ms."* 

In high-stakes healthcare environments, this data is your best friend during a post-mortem or a capacity planning meeting.

---
*Explore the configuration files in [`config/grafana/`](https://github.com/gjergjsheldija/hapi-fhir-groovy/tree/main/config/grafana).*
