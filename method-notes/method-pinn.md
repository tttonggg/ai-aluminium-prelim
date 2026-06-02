---
title: "Physics-Informed Neural Networks (PINN)"
tags: [method, pinn, physics-informed]
date: 2026-06-02
---

# Physics-Informed Neural Networks

## Core idea
Embed the governing PDE into the loss function of a neural network so the model
respects physics (mass, momentum, energy conservation) while fitting data.

## Landmark reference
- Raissi, Perdikaris, Karniadakis (2019), J. Comp. Physics
  DOI: `10.1016/j.jcp.2018.10.045` (16,251 citations)
- Karniadakis et al. (2021), Nature Reviews Physics
  DOI: `10.1038/s42254-021-00314-5` (6,362 citations)

## Variants
- **Vanilla PINN** — Raissi 2019
- **Self-adaptive PINN** — McClenny & Braga-Neto 2020
- **Fourier Neural Operator (FNO)** — Li et al. 2021
- **DeepONet** — Lu et al. 2021
- **Neural ODE** — Chen et al. 2018

## Aluminium-specific applications (found)
- Sharma, Raissi, Guo (2024) — arXiv `2407.10761`
- Rezvanpour et al. (2026), DOI: `10.3390/machines14030311`

## Open opportunity
- Industrial-scale 3D operator-learning for DC casting thermal fields
- Coupled fluid-thermal-mechanical PINN for extrusion die
