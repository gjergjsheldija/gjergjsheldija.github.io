---
title: "From FHIR PlanDefinition to BPMN: Visualizing Care Pathways"
date: 2026-01-12T09:00:00+10:20
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "dbt", "DuckDB", "Data Engineering", "Architecture"]
categories: ["Engineering", "Healthcare"]
description: "Tool to convert FHIR PlanDefinitions into interactive BPMN diagrams with a simple web app, making complex care pathways easy to visualize and understand."
featured_image: "/images/plandefinition-to-bpmn.png"
---

# Visualizing Care Pathways: Making PlanDefinitions Easier to Understand

As a healthcare software architect, I often see how complex care pathways can be hard to follow, especially when they’re described in technical formats like FHIR PlanDefinitions. While these standards are important for interoperability, they aren’t always easy for everyone to interpret.

To help with this, we created a simple web app that turns PlanDefinitions into BPMN diagrams. BPMN is a visual way to show processes, making it easier for clinicians and teams to see how a care pathway is structured.

The app is straightforward: upload a PlanDefinition, and you’ll get a visual diagram you can explore. There’s no need for technical skills—just a clear view of the workflow, which can help with understanding and collaboration.

This tool is a small step toward making healthcare processes more transparent and accessible. I hope it helps teams work together more effectively and makes care pathways a little easier to navigate.

## How It Works

The app is built with a modern web stack (React, Vite, TypeScript). When you upload a PlanDefinition (in JSON), the app parses it and generates a BPMN diagram in your browser. There’s no backend—everything runs locally, so your data stays private.

## Supported Features

Upload and view FHIR PlanDefinition files (JSON)
Automatic conversion to BPMN diagrams
Interactive diagram viewer (zoom, pan)
Simple JSON editor for PlanDefinitions
No installation or login required
This tool aims to make care pathways more transparent and accessible, helping teams collaborate and understand processes more easily.


## Source Code

You can find the source code and contribute to the project on GitHub: [https://github.com/gjergjsheldija/plandefinition-to-bpmn](https://github.com/gjergjsheldija/plandefinition-to-bpmn)

