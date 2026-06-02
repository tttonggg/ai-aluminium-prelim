---
title: "Gap: Neural Operators for Al Thermal Fields"
tags: [gap, neural-operator, pinn, fno, deeponet]
priority: medium
date: 2026-06-02
---

# Gap: Neural Operators for Aluminium Thermal Fields

## The gap
Neural operators (FNO, DeepONet, neural ODE) are dominant in ML-for-PDE
community but largely absent in Al-specific industrial work.

## Why it matters
- DC casting thermal field simulation: minutes to hours per query (FEM)
- Neural operator: milliseconds after training
- Required for closed-loop control at industrial cadence

## What's been done in other metals
- Steel continuous casting: some FNO work (Tartakovsky group, others)
- AM thermal fields: PINN/FNO in academic setting
- Battery thermal management: heavy FNO use

## What's missing for Al
- Industrial-scale 3D operator for DC casting
- Coupled fluid-thermal-mechanical operator for extrusion die
- Multi-physics operator (thermal + electromagnetic + metallurgical)

## Reference
- Sharma, Raissi, Guo (2024), Physics-Informed ML for Smart AM —
  arXiv `2407.10761` (closest, but AM not DC)
- Rezvanpour et al. (2026), Composition-Aware SDAS Prediction —
  DOI: `10.3390/machines14030311`

## Effort estimate
6-18 months for proof-of-concept.
