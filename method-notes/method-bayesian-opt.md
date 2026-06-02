---
title: "Bayesian Optimization for Materials & Manufacturing"
tags: [method, bayesian-opt]
date: 2026-06-02
---

# Bayesian Optimization

## Core idea
Build a probabilistic surrogate (usually GP) over design space, use an
acquisition function to pick the next experiment. Best when each experiment
is expensive (real cast, real extrude) and you have 20-100 trial budget.

## Landmark references
- Frazier & Wang (2015), tutorial
- Lookman et al. (2016), Acta Materialia
- Asru et al. (2025), arXiv `2504.04244`

## Aluminium-specific
- Walenta et al. (2024), Al-Mg-Si extrusion
- Indirect: hot-tearing optimization in DC casting

## Open opportunity
- Multi-objective BO for extrusion: throughput × surface × energy
- Constrained BO with safety constraints
- Multi-fidelity BO coupling FEM + plant data
