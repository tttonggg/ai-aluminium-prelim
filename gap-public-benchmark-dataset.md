---
title: "Gap: Public DC Casting Benchmark Dataset"
tags: [gap, dataset, dc-casting]
priority: high
date: 2026-06-02
---

# Gap: Public DC Casting Benchmark Dataset

## The gap
No public dataset exists with: (process parameters) + (in-line sensor data) +
(final macro/microstructure) + (defect labels) for aluminium DC casting.

## Why it matters
- ML papers can't be reproduced
- Benchmark competition impossible
- Industrial data stays in silos (Constellium, Hydro, Sapa)

## What a good dataset would contain
- 1000+ billets, varied compositions (6xxx, 7xxx, 2xxx)
- Casting speed, water flow, pour temperature, alloy chemistry
- In-line thermocouples (radial + center)
- Final grain structure (EBSD or anodized)
- Hot-tearing locations (X-ray or destructive)
- Macrosegregation profiles (chemical analysis at multiple radial points)

## Possible sources for bootstrapping
- **NIST AM-Bench** — has Al AM data, structure could be replicated for DC
- **NASA / USAMP** — Al-alloy AM benchmark
- **TMS Light Metals Conference proceedings** — small datasets in papers
- **Constellium / Hydro / Sapa** — would need consortium + NDA + IRP

## Effort estimate
12-24 months to build (assuming industrial partner).

## Citation hooks
- Guo 2024 (DOI: `10.3390/ma17061409`) — closest existing paper, uses private data
- Chen 2026 (DOI: `10.1007/s40192-026-00463-4`) — solidification, private
