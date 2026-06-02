---
title: "Pichlmann 2025: CALPHAD-ML LLM Pipeline for Aluminum Alloys"
type: paper-note
date_added: 2026-06-02
doi: 10.1016/j.mtcomm.2025.112843
authors: [Lukas Pichlmann, ...]
venue: Materials Today Communications
year: 2025
cited_by: 4
tags: [paper, alloy-design, calphad, llm, matcalc, verified]
verification_status: VERIFIED
verified_at: 2026-06-02
verified_via: openalex
source_report: kimi-k2.6-tier1
---

# Predicting mechanical properties in aluminum alloys: A data-driven framework leveraging LLM extraction and CALPHAD

**Authors:** Lukas Pichlmann et al.
**Venue:** Materials Today Communications
**Year:** 2025
**DOI:** [10.1016/j.mtcomm.2025.112843](https://doi.org/10.1016/j.mtcomm.2025.112843)
**Cited by:** 4

## One-line takeaway
End-to-end pipeline (LLM PDF extraction → CALPHAD MatCalc features → ML)
predicting T6 peak-aged yield strength with R²=0.92 across 70+ age-hardenable
aluminum alloys — first published automated literature-to-model pipeline for Al.

## Method
- **Stage 1:** Locally hosted LLM extracts composition, YS, UTS, heat treatment
  from PDF literature → structured JSON
- **Stage 2:** Data cleaning (unit standardization, composition validation,
  outlier removal)
- **Stage 3:** Physics features: 42 elemental properties + CALPHAD phase
  calculations via MatCalc
- **Stage 4:** Feature selection via genetic algorithm
- **Stage 5:** ML model (likely GBR/XGB given domain)

## Key result
- R² = 0.92 for T6 peak-aged yield strength (70+ age-hardenable alloys)
- First automated literature-to-model pipeline for Al

## Why it matters
- Demonstrates LLM-driven database construction is now feasible
- Combines *learned* (LLM, ML) and *physics* (CALPHAD) features — hybrid approach
- Could be replicated for other alloy families (Cu, Mg, Ti, steels)
- Industrial impact: shrinks the time from literature to deployable predictive model

## Method class
- LLM extraction + CALPHAD-ML hybrid + genetic-algorithm feature selection

## Open questions
- Is the LLM open-source (so others can reproduce)?
- What was the source corpus of PDFs?
- How does R² hold out-of-distribution (new alloy families)?

## Backlinks
- [[_MOC]]
- [[process-alloy-design]]
- [[method-llm-nlp]]
- [[method-bayesian-opt]]
- [[kimi-report-2026-06-02]] (Tier 1, #17)
