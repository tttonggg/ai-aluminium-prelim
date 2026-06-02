---
title: "ML-driven Aluminium Alloy Design"
tags: [process, alloy-design, materials-discovery]
date: 2026-06-02
---

# ML-driven Aluminium Alloy Design

## Goal
Given a target property (strength, corrosion resistance, ductility), find the
optimal Al-alloy composition + heat treatment. Inverse design.

## Approach stack
1. **Property prediction** — composition + processing → property (surrogate)
2. **Inverse optimization** — property → composition (BO, generative model)
3. **Validation** — CALPHAD + experimental

## Databases
- **Materials Project** — DFT-computed properties
- **OQMD** — Open Quantum Materials Database
- **AFLOW** — high-throughput DFT
- **Citrine Informatics** — commercial curated dataset
- **No public "industrial Al-alloy" (heat-treated, characterized) dataset**

## Key papers (verified)
- Taheri-Mousavi et al. (2024), AM Al-alloys via ML, arXiv `2406.17457`
- Ji, Fu, Ding (2023), Corrosion-resistant Al-alloy design
  DOI: `10.1007/s10853-023-09053-1`
- Qi et al. (2023), Al-containing HEA, arXiv `2312.04708`
- Rezvanpour et al. (2026), SDAS in recycled Al, Machines
  DOI: `10.3390/machines14030311`
- Letyagin et al. (2025), Cast Al-alloy property prediction, Metallurgist

## Open opportunity
- Multi-property Pareto front (strength × corrosion × cost)
- Generative model (VAE / diffusion) for novel Al-alloy compositions
- Closed-loop: ML proposes → experiment → ML refines
- Recycled-Al design (impurity tolerance)
