---
title: "Hengst SE 2025: Production-Validated X-ray YOLOv5 for Al Die Casting"
type: paper-note
date_added: 2026-06-02
doi: 10.3390/app152413134
arxiv_id: 10.20944/preprints202511.1857.v1
authors: [Agnes Pechmann, Sinan Kanli]
venue: Applied Sciences
year: 2025
cited_by: 0
tags: [paper, defect-detection, x-ray, yolov5, industrial-deployment, verified]
verification_status: VERIFIED
verified_at: 2026-06-02
verified_via: openalex
source_report: kimi-k2.6-tier1
---

# Towards Sustainable Manufacturing: Deployable Deep Learning for Automated Defect Detection in Aluminum Die-Cast X-Ray Inspection at Hengst SE

**Authors:** Agnes Pechmann, Sinan Kanli
**Venue:** Applied Sciences (MDPI)
**Year:** 2025
**DOI:** [10.3390/app152413134](https://doi.org/10.3390/app152413134)
**Preprint:** [10.20944/preprints202511.1857.v1](https://doi.org/10.20944/preprints202511.1857.v1)
**Open Access:** Yes

## One-line takeaway
First published study of *production-validated* deep-learning X-ray defect
detection on real Al die-cast parts, achieving F1=0.78–0.87 and matching/beating
human inspectors on critical defects, with CPU inference under 2s.

## Method
- **Dataset:** 12,960 annotations (Part A) + 27,443 annotations (Part B) from
  industrial X-ray at Hengst SE; annotated by certified inspectors
- **Models tested:** YOLOv5, YOLOv8, YOLOv9, YOLOv10, YOLOv11
- **Winner:** YOLOv5 (fastest convergence, 10.2 min to best F1)
- **Resolution:** Native 2016×2016 (vs 640×640) improved F1 from 0.59 → 0.73
- **Hyperparameter optimization:** Sequential one-at-a-time
- **Two deployment strategies:** Position-specific models (F1=0.74–0.87, mean 0.78)
  vs Part-level joint model (F1=0.76, slight generalization penalty)

## Key results
- Part A (cleaned): Inspector F1=0.904, position-specific model F1=0.892
- Part B (cleaned): position-specific F1=0.891, part-level F1=0.904,
  inspector F1=0.806
- **Critical defects:** 7/7 detected (Part A), 11/11 detected (Part B)
- **Real-time:** <2 s per image on standard industrial PC (CPU-only)

## Why it matters
- *Real* industrial data, not academic benchmark
- CPU-only inference → deployable on legacy factory PCs (no GPU needed)
- Matches/exceeds human inspector consistency
- Concrete business case: scrap reduction, energy savings, automation ROI

## Method class
- Object detection (YOLO family)
- Industrial QA / quality control

## Backlinks
- [[_MOC]]
- [[process-defect-detection]]
- [[kimi-report-2026-06-02]] (Tier 1, #6)
- [[_cross-reference-hermes-vs-kimi]]
