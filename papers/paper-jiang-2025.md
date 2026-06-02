---
title: "Jiang 2025: Interpretable Chain-Based ML for Ultra-High Strength Al Alloys"
type: paper-note
date_added: 2026-06-02
doi: 10.1016/j.matdes.2025.114289
authors: [Lei Jiang, Xinbiao Zhang, Wentao Zhoutai, Zhilin Han, Minghong Mao, Wen Xue]
venue: Materials & Design
year: 2025
cited_by: 11
tags: [paper, alloy-design, shap, interpretable, 7xxx, verified]
verification_status: VERIFIED
verified_at: 2026-06-02
verified_via: openalex
source_report: kimi-k2.6-tier1
---

# Discovery of ultra-high strength aluminum alloys with high damage tolerance via interpretable chain-based machine learning

**Authors:** Lei Jiang, Xinbiao Zhang, Wentao Zhoutai, Zhilin Han, Minghong Mao, Wen Xue
**Venue:** Materials & Design
**Year:** 2025
**DOI:** [10.1016/j.matdes.2025.114289](https://doi.org/10.1016/j.matdes.2025.114289)
**Cited by:** 11
**Open Access:** Yes

## One-line takeaway
Interpretable chain-based ML (AC + SAP → TMP → FS via SHAP) discovered
Al-10.5Zn-2.34Mg-1.28Cu-0.11Zr-0.1Cr with σb=794 MPa and >20% improvement
over AA7050/AA7055 — and the model gives you the *equation*, not just the
prediction.

## Method
- **Chain:** Alloy Composition (AC) + Solidification & Aging Process (SAP)
  → Thermo-Mechanical Processing (TMP), measured by σb, σy, A
  → Fatigue Strength (FS = α · σb · A^¼)
- **Models:** Gradient Boosting + SHAP + multi-objective optimization
  + thermodynamics (CALPHAD)
- **New alloy:** Al-10.5Zn-2.34Mg-1.28Cu-0.11Zr-0.1Cr
- **Validation:** Compared against AA7050, AA7055 (commercial benchmarks)

## Key results
- σb = 794 ± 2 MPa
- σy = 765 ± 3 MPa
- A = 11.9 ± 0.4%
- FS = 376 ± 14 MPa
- **>20% improvement over AA7050 and AA7055**

## Why it matters
- *Interpretable* — the chain model gives an explicit FS equation, not a black box
- SHAP shows *which* features matter at each chain stage
- Demonstrates the multi-stage ML approach for alloy design (vs. flat property prediction)
- Direct industrial impact: a new Al alloy recipe you can actually make

## Open opportunity
- Replicate the chain approach for other alloy families
- Add cost / manufacturability as additional chain stages
- Couple with industrial trial loop (extrude → test → update model)

## Backlinks
- [[_MOC]]
- [[process-alloy-design]]
- [[method-bayesian-opt]]
- [[kimi-report-2026-06-02]] (Tier 1, #19)
