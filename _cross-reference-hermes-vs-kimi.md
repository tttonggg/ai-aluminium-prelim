---
title: "Cross-Reference: My Prelim vs Kimi K2.6 Report"
type: cross-reference
date: 2026-06-02
tags: [meta, comparison, kimi, verification]
---

# Cross-Reference: Hermes Prelim vs Kimi K2.6 Report

This is a working document comparing the two reports. Use it to triage
verification work.

## Reports compared

| | My prelim | Kimi K2.6 report |
|---|---|---|
| **File** | [[prelim-2026-06-02.md]] | [[kimi-report-2026-06-02.md]] |
| **Date** | 2026-06-02 | 2026-06-02 |
| **Sources** | arXiv + OpenAlex + S2 | Kimi's own search (per its report) |
| **Total refs** | 64 (38 method + 26 Al-specific) | 35+ mentioned, 30 in appendix table |
| **DOIs** | All verified in OpenAlex | **None in appendix — NOT verified** |
| **Date range** | 2015-2026 | 2019-2026 |
| **Verification status** | ✅ Verified | ⚠️ Unverified |

## What my prelim covers that Kimi doesn't

| Topic | My prelim | Kimi |
|---|---|---|
| Hot tearing ML (multiple papers) | ✅ Guo 2024, Zhou 2024, Shi 2024, etc. | ❌ Only as "gap" in section 9 |
| Macrosegregation ML | ✅ | ❌ Only as "gap" |
| Die wear prediction | ❌ (gap) | ❌ (gap) |
| Tian 2024 EBSD/CNN | ✅ | ❌ |
| Liu ASaRE-Net Al-Si | ✅ | ❌ |
| Bosse 2023 X-ray Al die casting | ✅ | ❌ |
| Shen 2025 micro-CT Al | ✅ | ❌ |
| Many Chinese-language refs | ✅ | ❌ |

## What Kimi covers that my prelim doesn't

| Topic | My prelim | Kimi |
|---|---|---|
| **Chen 2026 die design** (J. Intell. Manuf.) — MLP/LSTM/RL/GA, MAE 3.74e-3 | ❌ | ✅ Detailed |
| **Hengst SE X-ray YOLOv5** (2025) — F1=0.87, CPU <2s | ❌ | ✅ Detailed |
| **Parlak & Emel 2024** — ASTM aluminum casting X-ray | ❌ | ✅ |
| **Pichlmann 2025** — CALPHAD-ML LLM pipeline, R²=0.92 T6 | ❌ | ✅ |
| **Jiang 2025** — Interpretable chain-based Al-10.5Zn-2.34Mg-1.28Cu, σb 794 MPa | ❌ | ✅ |
| **GNN for LPBF Al (Monash 2025)** — GAT + knowledge graph | ❌ | ✅ |
| **DeepONet multiphysics casting** (arXiv 2024) | ❌ | ✅ |
| **Energy-consistent NN metal forming** (Fenchel-Young loss, MDPI 2026) | ❌ | ✅ |
| **Allegro GNN potential Al** (TUM 2026) — million-atom MD | ❌ | ✅ |
| **PCG detection** — 99.7% accuracy, 0.8s, 40% scrap reduction | ❌ | ✅ |
| **Industrial ROI** — 15:1 in 8 months, scrap 8.2→5.9% | ❌ | ✅ |
| **Todorovic 2024** — MatBERT vs MatSciBERT comparison | ❌ | ✅ |
| **Parvizi 2026** — Bayesian opt for recycled 7xxx | ❌ | ✅ |
| **Lee 2026** — Gradient Boosting HEA yield (R²=0.85) | ❌ | ✅ |
| **Rezvanpour 2026** — SDAS in recycled Al (PIML, R²=0.95) | partial | ✅ Detailed |

## Overlap (both cover)

| Topic | My prelim | Kimi |
|---|---|---|
| MatSciBERT | ✅ | ✅ |
| Karniadakis PINN review | ✅ | ✅ |
| AdditiveLLM | ✅ | ✅ |
| Guo 2024 DC casting | ✅ | ✅ |
| Digital twin concepts | ✅ | ✅ |
| Bayesian opt for materials | ✅ | ✅ |
| CALPHAD-ML hybrid | ✅ | ✅ |
| GBR for flow stress | ✅ | ✅ |

## Verification priorities (ranked by impact)

When time allows to verify Kimi's 30-paper appendix, do these first:

### Tier 1 (highly relevant, would substantially strengthen the prelim)

1. **Chen et al. 2026** — die design automation in J. Intell. Manuf. (cited 5+ times in Kimi)
2. **Hengst SE 2025** — production-validated X-ray YOLOv5
3. **Parlak & Emel 2024** — ASTM aluminum casting standard X-ray
4. **Pichlmann 2025** — LLM + MatCalc + GA aluminum pipeline
5. **Rezvanpour 2026** — SDAS recycled Al PIML (R²=0.95)
6. **Jiang 2025** — interpretable Al-10.5Zn-2.34Mg-1.28Cu
7. **Monash 2025** — GNN for LPBF aluminum

### Tier 2 (would add valuable new methods/applications)

8. **Todorovic 2024** — MatBERT vs MatSciBERT comparison
9. **S-DeepONet 2024** — multiphysics casting
10. **Parvizi 2026** — Bayesian opt recycled 7xxx
11. **Lee 2026** — HEA yield strength
12. **Allegro GNN Al 2026** — million-atom MD
13. **Energy-consistent NN 2026** — Fenchel-Young loss
14. **PCG detection 2025** — 99.7% accuracy
15. **ZIOT surface defect 2025** — AP 57→67%

### Tier 3 (lower priority)

16-30. Other industrial case studies, ChemDataExtractor details, etc.

## Verification plan

```bash
# To verify Tier 1 (one search per paper):
curl -s "https://api.openalex.org/works?search=<title>&per_page=1" | python3 -m json.tool

# If result found: extract DOI, title, year, verify
# If not found: mark as "could not verify" — DO NOT fabricate
```

## Honest disclosure

- The Kimi report is **substantially more comprehensive** than my prelim on:
  industrial deployment, specific named datasets, ROI numbers, ASTM standards,
  LLM extraction pipelines, GNN for LPBF.
- My prelim is **stronger** on: hot tearing, Chinese-language refs, AM-specific Al,
  verified DOIs.
- The Kimi report has **no DOIs in the appendix** — this is the most serious gap.
- Until verified, treat Kimi's appendix as **promising leads**, not citations.

## Next step

Manual triage by the user:
- Read the Kimi report
- For papers you care about, run the verification query
- For verified papers, add a 1-page note in `papers/`
- For unverified papers, drop from the prelim

The monthly cron (`al-ai-monthly-refresh`) will re-check OpenAlex
each month and pull in any new Al-ML papers with verified DOIs.
