---
title: "Defect Detection: Surface, X-ray, NDT"
tags: [process, defect-detection, computer-vision]
date: 2026-06-02
---

# Aluminium Defect Detection

## Modalities
- **Surface vision** (RGB cameras on line) — scratches, dents, die-lines
- **X-ray radiography** — porosity, inclusions, internal cracks
- **Ultrasonic / eddy current** — surface + near-surface
- **Hyperspectral / thermal** — emerging

## Datasets
- **GC10-DET** — public steel strip surface defects, 10 classes
- **NEU-DET** — public steel surface defects, 6 classes
- **MVTec AD** — public anomaly detection, includes metal capsules
- **No large public Al-dedicated dataset** found

## Key papers (verified)
- Bosse & Lehmhus (2023), X-ray radiography + ML, arXiv `2311.12041`
- Awtoniuk et al. (2022), Industrial DNN for Al casting
- Lin et al. (2021), Surface defect classification
- Lilansa et al. (2024), YOLO on Al casting
- Bosse (2024), Porosity in Al die casting, Sensors
  DOI: `10.3390/s24092933`
- Hena et al. (2024), NDT radiography, DOI: `10.3390/ndt2040023`

## Method mix
- YOLOv5/v8 — real-time detection
- ResNet/EfficientNet — classification
- U-Net — defect segmentation
- Autoencoders — anomaly detection (no defect examples needed)
- Synthetic data + Sim2Real — when real defects are rare

## Open opportunity
- Public Al-dedicated multi-modal dataset (RGB + X-ray + thermal)
- Foundation model for industrial defect (vs. natural images)
- Online learning: model updates as new defect types appear
