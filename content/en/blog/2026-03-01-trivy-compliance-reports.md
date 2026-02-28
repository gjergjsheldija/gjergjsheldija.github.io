---
title: "Beyond the CLI: Professional Security Reports for Healthcare Compliance"
date: 2026-03-01T10:00:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["Trivy", "Compliance", "IEC 81001-5-1", "ISO 27001", "MDR", "Cybersecurity", "Healthcare IT", "SBOM"]
categories: ["Engineering", "Security"]
description: "Why I built the Trivy PDF plugin and how it simplifies the documentation burden for IEC 81001-5-1, ISO 27001, and MDR audits."
featured_image: "/images/trivy_compliance_featured.png"
---

# Beyond the CLI: Professional Security Reports for Healthcare Compliance

If you've spent any time as a healthcare architect or lead dev, you know the drill. It’s Friday afternoon, and a compliance officer asks for the latest **SBOM** (Software Bill of Materials) and a vulnerability assessment for your upcoming **MDR** submission.

You run `trivy image --format json`, and you’re looking at a massive wall of JSON. To you and me, it’s a goldmine of data. To an auditor or a medical director, it’s a foreign language. 

Between **IEC 81001-5-1**, **ISO 27001**, and the **MDR**, we spend half our lives generating "evidence." I realized that we were wasting too much time translating technical scans into human-readable reports, so I decided to build a bridge. 

That bridge is the [trivy-report-pdf](https://github.com/gjergjsheldija/trivy-report-pdf) plugin.

## Why "Good Enough" Scans aren't enough for Audits

In the world of medical software, cybersecurity is now a regulatory gateway. But there’s a massive friction point: **The Boardroom vs. The Console.**

### 1. IEC 81001-5-1: The Security Lifecycle
IEC 81001-5-1 isn't just about having a secure system; it's about *proving* you have a secure lifecycle. You need to document every dependency and show you’re actively monitoring vulnerabilities. Handing over a raw JSON file to a Quality Management System (QMS) isn't just rude; it often doesn't meet the documentation requirements for "accompanying documentation."

### 2. MDR and ISO 27001: The Documentation Burden
Under the MDR and ISO 27001, we’re expected to maintain "state-of-the-art" security. When an auditor asks how you handled CVE-2024-XXXX, they want to see a clear report with severity badges, remediation steps, and timestamps—not a grep command result.

## Making Security Data "Human-Grade"

The goal of [trivy-report-pdf](https://github.com/gjergjsheldija/trivy-report-pdf) is to take the raw intelligence of Trivy and package it into something you can actually attach to a technical file without feeling embarrassed.

The plugin generates two specialized reports:

1.  **The SBOM (`*_sbom.pdf`)**: A clean, professional inventory. No fluff, just every package and dependency neatly listed for the auditor.
2.  **The Vulnerability Audit (`*_vulns.pdf`)**: This is the "Executive View." It includes color-coded risk cards (Critical to Low) and summarizes the risk profile so anyone can understand it in five seconds.

## Putting it to Work

I built this to be a "set it and forget it" tool. You can install it in seconds:

```bash
trivy plugin install github.com/gjergjsheldija/trivy-report-pdf
```

And then, instead of just scanning, you generate an audit-ready PDF:

```bash
trivy pdf image my-healthcare-app:latest --output q1_audit_report
```

You get `q1_audit_report_sbom.pdf` and `q1_audit_report_vulns.pdf`—ready for the QMS, the auditor, or your own piece of mind.

## Continuous Compliance

My favorite way to use this is in the CI pipeline. Every time we tag a release, the pipeline generates these PDFs and archives them. 

When that "Friday afternoon" question comes from the compliance team, you don't have to scramble. You just send them the link to the generated PDFs. Compliance shouldn't be a separate, painful workstream; it should be a byproduct of a good build process.

## Bottom Line

Regulations like **IEC 81001-5-1** are there to keep patients safe. Our job as architects is to make sure that safety is documented as clearly as it is implemented. 

If you’re tired of manually formatting security reports, give the plugin a try. Let’s spend less time on paperwork and more time building software that actually helps people.

---
*Explore the project and contribute on GitHub: [gjergjsheldija/trivy-report-pdf](https://github.com/gjergjsheldija/trivy-report-pdf)*
