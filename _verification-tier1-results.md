---
title: "Tier-1 Verification Results — Kimi K2.6 Report"
type: verification-report
date: 2026-06-02
source: kimi-k2.6
papers_checked: 7
papers_verified: 4
papers_likely_fabricated: 1
papers_inconclusive: 2
bonus_finds: 1
---

# Tier-1 Verification Results — Kimi K2.6 Report

## Summary table

| # | Paper (from Kimi Tier 1) | Status | DOI | Citation |
|---|---|---|---|---|
| 1 | Hengst SE 2025 X-ray YOLOv5 | ✅ VERIFIED | `10.3390/app152413134` | 0 |
| 2 | Pichlmann 2025 CALPHAD-ML | ✅ VERIFIED | `10.1016/j.mtcomm.2025.112843` | 4 |
| 3 | Jiang 2025 interpretable Al | ✅ VERIFIED | `10.1016/j.matdes.2025.114289` | 11 |
| 4 | Monash 2025 GNN for LPBF | ✅ VERIFIED | `10.1080/17452759.2025.2549366` | 1 |
| 5 | Rezvanpour 2026 SDAS recycled Al | ✅ VERIFIED (already in prelim) | `10.3390/machines14030311` | 0 |
| 6 | Parlak & Emel 2024 ASTM | ⚠️ INCONCLUSIVE | author search timed out | — |
| 7 | Chen 2026 die design (J. Intell. Manuf.) | ❌ NOT FOUND | likely fabricated | — |
| BONUS | Yang 2026 die casting ICME | ✅ VERIFIED (new find) | `10.1038/s41524-026-02010-3` | 0 |

## 4/7 Tier-1 verified (57%)

This is consistent with my own prelim-build experience (9/20 DOIs from memory
were wrong = 45% fabrication rate). LLMs including Kimi K2.6 still fabricate
paper details at meaningful rates.

## What this means for the Kimi report

- **Tier 1 (verified subset):** Treat as reliable. The 4 verified papers have
  specific, accurate details — PIDs, hyperparameters, exact compositions.
  This suggests the rest of the report's *analysis* is sound even where
  individual citations may be off.
- **Tier 2/3 (unverified):** Treat as **promising leads only**. Don't cite
  without verification.
- **Chen 2026 die design** appears to be a Kimi fabrication. The specific
  details (MAE 3.74e-3, J. Intell. Manuf. venue) don't match anything in
  OpenAlex with related keywords. Drop from the prelim.

## Verified papers (1-page notes created)

- [[paper-hengst-se-2025]] — production-validated X-ray YOLOv5
- [[paper-pichlmann-2025]] — LLM + CALPHAD-ML pipeline
- [[paper-jiang-2025]] — interpretable Al-10.5Zn-2.34Mg-1.28Cu (σb 794 MPa)
- [[paper-gnn-lpbf-2025]] — GAT + knowledge graph for Al LPBF
- [[paper-yang-2026-diecasting]] — BONUS: ICME die casting alloy design

## What's still on the verify list

- Parlak & Emel 2024 (author search needs re-running)
- Chen 2026 die design — likely fabricated
- The other 23 papers in Kimi's appendix (Tier 2-3)
- Tier 2 candidates: Todorovic 2024, S-DeepONet 2024, Parvizi 2026, Lee 2026,
  Allegro GNN 2026, Energy-consistent NN 2026, PCG detection 2025, ZIOT 2025

## Backlinks
- [[_MOC]]
- [[_cross-reference-hermes-vs-kimi]]
- [[kimi-report-2026-06-02]]
