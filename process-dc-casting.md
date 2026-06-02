---
title: "Direct-Chill (DC) Billet Casting"
tags: [process, dc-casting, billet]
date: 2026-06-02
---

# Direct-Chill (DC) Billet Casting

## Process
Molten aluminium (700-740°C) poured into a water-cooled mould; a solid shell
forms; billet is withdrawn downward while water sprays cool the surface.
Output: 6-12" diameter billets for extrusion, 1000-3000mm long.

## Key process parameters
- Casting speed (50-150 mm/min)
- Pouring temperature
- Water flow rate (primary + secondary cooling)
- Grain refiner (TiB₂) addition
- Alloy composition

## Key defects
- **Hot tearing** — cracks form during solidification shrinkage
- **Macrosegregation** — composition varies radially
- **Centerline porosity** — shrinkage cavities
- **Cold shuts** — surface folds from interrupted flow

## AI/ML papers (verified)
- Guo, Yao, Liu et al. (2024), Materials, DOI: `10.3390/ma17061409` (5 cit)
- Liu et al. (2025), DOI: `10.1007/s11665-025-11028-5`
- Lin et al. (2025), J. Alloys & Compounds, DOI: `10.1016/j.jallcom.2025.179743` (16 cit)
- Chen et al. (2026), IMMI, DOI: `10.1007/s40192-026-00463-4`

## Datasets
- No public DC-casting dataset with paired process+microstructure+defect
- Most papers use private industrial data

## Open opportunity
- Public benchmark dataset (the field's biggest gap)
- Physics-informed ML for macrosegregation
- Transfer learning: simulation → plant
