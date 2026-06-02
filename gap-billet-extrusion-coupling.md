---
title: "Gap: Billet→Extrusion Coupled ML Pipeline"
tags: [gap, integration, pipeline]
priority: high
date: 2026-06-02
---

# Gap: Billet→Extrusion Coupled ML Pipeline

## The gap
No paper found that jointly models: DC casting → homogenization → extrusion
as a single ML pipeline. They're treated as independent sub-problems.

## Why it matters
- In reality, billet quality (segregation, porosity) propagates to extrusion
- A billet with 0.5% Cu segregation at center → variable aging response
- A billet with hot-tearing microcracks → surface defects in extrusion
- Optimizing casting alone may produce billets that extrude poorly

## What a coupled pipeline would do
1. **Input**: target alloy, target profile, target production rate
2. **Cast surrogate**: composition → predicted macrosegregation
3. **Homogenization surrogate**: time/temp → predicted dissolution
4. **Extrusion surrogate**: billet quality + process params → final profile quality
5. **Joint optimization**: pick casting params that produce billets which
   extrude well, not just billets that are "good in isolation"

## Open opportunity
- Multi-fidelity BO coupling (simulation low-fid + plant high-fid)
- Joint surrogate with shared latent representation
- Bayesian network for causal dependency between stages

## Effort estimate
18-36 months. Requires industrial data across the chain.
