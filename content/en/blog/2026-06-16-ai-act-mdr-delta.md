---
title: "MDR and the AI Act: The Compliance Delta You Are Not Budgeting For"
date: 2026-06-16T08:00:00Z
draft: false
categories: ["Engineering", "Regulatory"]
tags: ["MDR", "AI Act", "SaMD", "EU AI Act", "ISO 13485", "Regulatory Compliance", "Engineering Leadership", "Medical Device Software", "Healthcare AI", "FRIA"]
author: "Gjergj Sheldija"
description: "The Digital Omnibus has pushed AI Act application for medical devices to August 2028. That sounds like good news. It is not. The work the regulator is catching up on is not the work you have to do, and the obligations that do not map cleanly to MDR are the ones most engineering organisations have not started."
featured_image: "/images/ai-act-mdr-delta.png"
---

# MDR and the AI Act: The Compliance Delta You Are Not Budgeting For

On 7 May 2026, the Council, Parliament, and Commission reached a provisional agreement on the Digital Omnibus on AI. For AI-enabled medical devices, the date that matters moves again: from 2 August 2027 to 2 August 2028. For Annex III high-risk systems generally, from 2 August 2026 to 2 December 2027. The press coverage framed this as relief, as breathing room, as Brussels listening to industry. I want to argue the opposite.

The delay is not a gift to engineering organisations. It is the regulator admitting that the regulatory infrastructure (notified body designations under the AI Act, harmonised standards, Member State competent authorities, MDCG joint guidance) is not ready. None of that has anything to do with whether your product is ready. The 2028 date is a calendar most MedTech CTOs are reading as "we have time." We do not.

This article is about what the AI Act actually obliges providers of AI-enabled medical devices to do, where those obligations overlap with MDR and ISO 13485, and (more importantly) where they do not. Most teams I talk to are confident that "we already do MDR, so we are fine." That sentence is the single most expensive belief in MedTech right now. The overlap is real, but the delta is larger than people expect, and it is concentrated in places that are organisationally hard rather than technically hard.

## Why "MDR Covers It" Is Wrong

The argument goes roughly like this. MDR is a comprehensive regime. ISO 13485 mandates a quality management system. ISO 14971 mandates risk management. IEC 62304 mandates a software lifecycle. IEC 81001-5-1 mandates security activities across that lifecycle. AI Act Article 43(3) says that for high-risk AI systems that are also medical devices, the conformity assessment is conducted by the MDR notified body as part of the MDR conformity assessment procedure, with AI Act requirements integrated. So (the argument concludes) the AI Act is a delta on top of MDR, the existing notified body already does the work, and the QMS we already operate absorbs the new requirements naturally.

The mistake is reading "delta" as "small." The mechanical integration described by Article 43(3) does not change the fact that the AI Act introduces substantive new obligations that the MDR framework simply does not require, and that those obligations land in places the typical MedTech engineering organisation is not staffed for.

Five obligations sit outside the MDR overlap. They are not exotic; they are not the high-cost training-time controls that consume most of the public discourse around AI safety. They are governance and lifecycle obligations, which is precisely why they are hard.

## Article 4: AI Literacy, Already In Force

This is the easiest one to miss because it is already a legal obligation. Article 4 of the AI Act has applied since 2 February 2025. It requires providers and deployers of AI systems to ensure a sufficient level of AI literacy among staff and other persons dealing with the operation and use of those systems, taking into account their technical knowledge, experience, education, training, and the context in which the AI system is used.

For a MedTech provider this is two distinct problems. Internally, you need a defensible position on what literacy means for your engineering, product, clinical affairs, and customer success functions, and you need evidence (training records, role descriptions, onboarding curricula) that you have produced that literacy. Externally, your customer-facing material has to support the deployer's literacy obligation, because the hospital using your AI-enabled SaMD has the same Article 4 obligation toward its clinicians.

MDR has nothing like this. ISO 13485 has competence requirements (§6.2), but they are about quality system roles, not about AI-specific understanding of model behaviour, dataset provenance, or the operational distinction between an AI output and a clinical decision. If you are running a MedTech today and you cannot, in a meeting with regulators, describe your AI literacy programme and produce its artefacts, you are out of compliance with Article 4 right now. Not in 2027. Not in 2028. Now.

## Article 10: Data Governance Beyond Risk Management

Article 10 imposes obligations on training, validation, and testing data sets used by high-risk AI systems. They must be subject to data governance and management practices appropriate to the intended purpose. They must be relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose. They must be examined for possible biases that are likely to affect the health and safety of persons, have a negative impact on fundamental rights, or lead to discrimination. They must, where appropriate, allow for the integration of solutions to detect, prevent, and mitigate such biases. The article goes further, listing specific properties of the data sets (statistical properties relevant to the persons or groups in relation to whom the system is intended to be used) that must be examined.

ISO 14971 risk management does not require this. It requires you to identify, evaluate, and control risks. It does not require you to demonstrate that your training data is representative of the deployment population, that it has been examined for protected-attribute biases, or that it carries documentation about geographical, behavioural, or functional context. IEC 62304 software lifecycle requirements do not require this either. The closest existing analogue in the MedTech world is the FDA's Good Machine Learning Practice (GMLP) guidance, which is non-binding and which most European teams do not formally adopt.

The practical consequence is that for any AI-enabled SaMD touching a patient population, you need a data governance regime that produces, on demand: dataset cards documenting provenance, composition, and licensing; representativeness analyses against your intended-use population (in DACH that often means examining German, Austrian, Swiss demographic distributions against your training set); explicit bias evaluations with quantitative thresholds; and a documented relationship between data version and model version that survives audit. None of this comes out of your MDR documentation. None of it gets generated by your existing CI/CD pipeline unless you have specifically built it.

The cost of building this is not in the engineering. The cost is in the data engineering plus regulatory affairs plus clinical affairs coordination required to produce defensible documentation, and in the institutional habit of treating training data as a versioned, governed, audited artefact rather than as a snapshot a data scientist pulled six months ago.

## Article 14: Human Oversight Is a Workflow Problem

Article 14 requires that high-risk AI systems be designed and developed in such a way that they can be effectively overseen by natural persons during the period in which they are in use. The article goes on to specify what oversight means: the ability of the human overseer to understand the relevant capacities and limitations of the system, to remain aware of automation bias, to interpret outputs correctly, to decide not to use the system or to override its output, and to intervene or interrupt operation through a stop button or similar.

MDR's general safety and performance requirements (Annex I) address usability and the prevention of use-related risks. IEC 62366-1 mandates usability engineering. None of these constructs is the same as Article 14. The closest existing requirement is the FDA's recent focus on human-AI teaming in the 2024 PCCP guidance for AI/ML-enabled devices, which again is non-binding in Europe.

The implication is architectural and clinical-workflow-driven, not just engineering. You have to design your clinical user interface, your alarm semantics, your reasoning explanations, your override path, and your audit trail of overrides as deliberate human-oversight infrastructure, and you have to be able to justify each design decision against Article 14's list. This is cross-functional work. It involves clinical affairs, UX research, regulatory affairs, and software engineering. If your AI-enabled SaMD displays a probability and an action recommendation, you need an answer to questions like: what does the clinician see about model confidence? How is the override recorded? What happens if the clinician's behaviour shows automation bias creeping in over months of use? How do you detect that, and what is your response?

Almost no MedTech team I have seen has answers that survive a serious Article 14 review. The MDR documentation tradition does not produce them, because MDR does not ask the questions.

## Articles 26 and 27: Your Customer's Problem Becomes Yours

This is the obligation that most reliably surprises CTOs in DACH, and it deserves close attention because it inverts the usual division of compliance labour between provider and deployer.

Article 26 imposes operational obligations on deployers of high-risk AI systems: use according to instructions, assign qualified human oversight personnel, monitor operation against the provider's instructions for use, keep automatically generated logs for an appropriate period, inform affected persons in certain cases, and cooperate with authorities. Article 27 imposes the fundamental rights impact assessment (FRIA) on a specific subset of deployers: bodies governed by public law, private entities providing public services, and deployers of certain Annex III high-risk systems regardless of public-law status.

In Germany, the practical reach of Article 27 is wide. The dominant hospital ownership models (öffentlich-rechtliche Krankenhäuser, university hospitals, statutory health insurance institutions) are bodies governed by public law. Most large hospital groups carry a public-law affiliation at some level. Private hospitals delivering services within the statutory health system can plausibly be characterised as providing services of public nature; the AI Act recitals and the prevailing reading of "services of public nature" treat healthcare in this category. The conservative reading, which is the reading any procurement function will take, is that the FRIA obligation lands on essentially every German hospital deploying an AI-enabled SaMD.

That is not your obligation as the provider. It is your customer's obligation. But you cannot sell into a hospital that cannot perform a FRIA on your system, and you cannot expect the hospital to do that work without your support. The deployer needs a clear description of the intended use, the categories of persons affected, the risks to fundamental rights, the human oversight measures the provider built in, and the system's training data characteristics insofar as relevant to fundamental rights. Some of this is already required by Article 13 (transparency and provision of information to deployers). Some of it requires you to expose information that you currently do not produce or do not publish.

The Digital Omnibus provisional agreement, depending on its final wording, may move the FRIA effective date from 2 August 2026 to 2 December 2027. That does not change the fact that hospital procurement is already asking the question, especially in DACH, because national implementation laws are being drafted now (Germany's KI-MIG draft, approved by the Federal Cabinet on 11 February 2026, is currently working through the legislative process). Once the obligation is real, the customer will require a FRIA-support package from you in the contract. You can either have one ready or you can be the vendor that lost the tender.

## Article 72 and the Post-Market Monitoring Overlap

This is the obligation where the MDR overlap is closest, and where most teams therefore underestimate the delta most aggressively. Article 72 of the AI Act requires providers of high-risk AI systems to establish and document a post-market monitoring system that actively and systematically collects, documents, and analyses relevant data on the performance of high-risk AI systems throughout their lifetime. The plan must be appropriate, taking into account the nature of the AI system and the risks involved.

This sounds exactly like MDR Articles 83 to 86 and Annex III post-market surveillance, and at the conceptual level it is. The delta lives in two specifics. First, AI systems have failure modes that MDR PMS frameworks do not contemplate: concept drift, distribution shift, performance degradation against subpopulations, feedback-loop effects from the system's own outputs influencing future training data. Your PMS plan has to address them explicitly. Second, the AI Act expects the plan to be implementable: it has to produce data, with the cadence and granularity that supports proving (not asserting) continuing performance.

For a typical SaMD that ships predictions or classifications, this means production telemetry of model inputs, outputs, confidence, and downstream clinical action, plus a periodic recalibration analysis against ground-truth labels, plus an alerting system for distribution shift. The MDR PMS document you currently have, which lives in a Word file managed by your regulatory affairs team and is updated yearly, is not that. It is the description of a process; Article 72 expects the process to be running.

## The German Context, Briefly

The German AI Act implementation has been slower than the August 2025 designation deadline required. The early federal election delayed the legislative process; the KI-MIG (Künstliche-Intelligenz-Marktüberwachungs- und Innovationsgesetz, or the equivalent designation in the final adopted text) draft bill was approved by the Federal Cabinet on 11 February 2026 and is now in the parliamentary process. The supervisory architecture, as it stands in the draft, is hybrid: the Bundesnetzagentur becomes the central market surveillance authority, notifying authority, and single point of contact under the AI Act, while sectoral regulators retain their existing jurisdiction. For AI-enabled medical devices specifically, the BfArM remains the competent authority, which means MedTech providers continue dealing with a familiar regulator and a familiar notified body landscape, with the AI Act layered on top through Article 43(3) integrated conformity assessment.

The practical effect for engineering leaders is that you do not get a single new regulator. You get the same MDR notified body (TÜV SÜD, DEKRA, TÜV Rheinland, DQS Medizinprodukte, and similar) operating under expanded competence requirements that the AI Act will mandate, against a backdrop where the EU-level designation framework for AI Act notified bodies is not yet in place. DEKRA, for example, has publicly stated its intention to apply for AI Act designation as soon as the procedural rules are issued. Until those rules exist, no MDR notified body can perform formal AI Act conformity assessment activities. That is not an excuse for inaction on your side; it is the gap that the 2028 application date for medical devices is intended to absorb.

A note on Switzerland: Switzerland sits outside the EU and outside the AI Act's territorial scope, but Article 2 of the AI Act applies the regulation to providers placing AI systems on the Union market regardless of where the provider is established. Swiss-developed AI-enabled SaMD entering the EU market faces the full AI Act regime, and the still-unresolved Swiss-EU mutual recognition position for medical devices (Switzerland has been treated as a third country under MDR since May 2021) compounds the regulatory load rather than easing it. Swiss MedTech teams targeting the EU market should plan as if there is no Swiss exception; there is not.

## What the Omnibus Delay Does Not Buy You

The Digital Omnibus pushes the medical-device application date from August 2027 to August 2028. The honest reading of why is that the regulator's infrastructure is not ready: harmonised standards on AI risk management, data governance, transparency, and conformity assessment are still in development (CEN-CENELEC JTC 21 is working through them); notified body designation rules for the AI Act do not yet exist; many Member States, including Germany, have not finalised competent-authority arrangements.

None of that is about whether your engineering organisation is ready. The work to produce dataset cards, representativeness analyses, FRIA-support packages, Article 14-grade human oversight design, AI literacy programmes, and AI-aware post-market monitoring is your work, and the Omnibus does not change its scope or duration. If anything, it changes the competitive dynamics: the providers that build this infrastructure ahead of the deadline will have a sales advantage in 2027 and 2028, because public-law hospital customers in DACH are already starting to ask the questions, and a vendor that has answers will close the deal a vendor without answers will not.

Treating the Omnibus delay as breathing room is the same mistake teams made with MDR's transitional provisions in 2017 and again with the 2023 extension. The teams that used the time productively are now market leaders. The teams that read the extension as permission to delay are now scrambling, expensively, with their notified body capacity booked out and their regulatory affairs functions in firefighting mode.

## What Actually Deserves Budget in 2026

If I had to pick the five line items that an AI-enabled MedTech provider should be funding before the end of this year, they would be these, in roughly the order they produce value.

First, the AI literacy programme. It is already a legal obligation. It is cheap to build (training material, role descriptions, recorded competence verification) and it is the easiest item to demonstrate when a regulator or customer asks. Build it now and stop carrying the open legal exposure.

Second, the data governance infrastructure. Dataset versioning, provenance, dataset cards, representativeness documentation, and a workflow for examining biases. This is the hardest item to retrofit once you have shipped a model, because it requires reconstructing context that may already be lost. Invest in it now while your data engineering team can still trace the lineage.

Third, the FRIA support package. Not because you have the obligation, but because your customers will. A clear, well-written document that helps a public-law hospital perform a FRIA on your system is a sales asset, not a compliance asset. Write it now, in close collaboration with two or three of your largest customers, and you will both shape the market and shorten future sales cycles.

Fourth, the Article 14 human oversight design review. This is a cross-functional exercise: take each of your AI-enabled features and walk through the Article 14 questions deliberately, document the answers, and identify the gaps. Some gaps will be fixable in software; some will require clinical workflow changes you cannot make alone. The earlier you find them, the cheaper they are.

Fifth, the post-market monitoring telemetry. Distribution-shift detection, performance-by-subpopulation reporting, override logging, and a recalibration cadence. This builds on observability infrastructure you probably already have, but it requires a deliberate plan and ownership. It also pays dividends outside the AI Act, because it makes your product genuinely better.

What does not deserve disproportionate budget in 2026 is the model-card and explainability theatre that has dominated the AI safety conversation in industry. Those are real obligations, but they are addressable with modest engineering effort once the underlying infrastructure is in place. The infrastructure is where the cost lives.

## Compliance as Competitive Advantage, Again

I have argued before that compliance, properly engineered, is not a cost centre but a strategic moat. The AI Act sharpens that argument, because the obligations it adds are precisely the obligations that most providers cannot satisfy on a short timeline. The teams that build the governance infrastructure now will have it in place when the market demands it; the teams that wait until 2028 will be competing against vendors who can already produce the documents the procurement function is asking for.

The dates have moved twice already, and they may move again. That is not the variable to manage. The variable to manage is the readiness of your own organisation against a set of obligations that are now fixed in law, regardless of when they apply. The calendar is the regulator's problem. Your engineering posture is yours.
