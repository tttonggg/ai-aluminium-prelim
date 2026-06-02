---
title: "Jiang 2023 npj Comp. Mater: Sample Data Transfer ML for Alloy Design"
type: paper-note
date_added: 2026-06-02
doi: 10.1038/s41524-023-00979-9
authors: [Lei Jiang, Zhihao Zhang, Hao Hu, Xingqun He, Huadong Fu, Jian-Xin Xie]
venue: npj Computational Materials
year: 2023
cited_by: 76
tags: [paper, alloy-design, transfer-learning, small-data, verified]
verification_status: VERIFIED
verified_at: 2026-06-02
verified_via: openalex
source: connected-papers-jiang-2025-graph
institution: USTB
---

# A rapid and effective method for alloy materials design via sample data transfer machine learning

**Authors:** Lei Jiang et al. (USTB)
**Venue:** *npj Computational Materials*
**Year:** 2023
**DOI:** [10.1038/s41524-023-00979-9](https://doi.org/10.1038/s41524-023-00979-9)
**Cited by:** 76

## One-line takeaway
**Transfer learning for alloy design** — uses a small amount of *target-system*
data plus a larger pool of *related-system* data to design new alloys
quickly and effectively. Solves the small-data problem in Al alloy design.

## Why it matters
- 76 citations in 3 years = rising foundational paper
- Solves a real pain point: alloy datasets are tiny
- npj Computational Materials = top-tier
- Generalizable to other alloy systems

## Method
- Sample-data transfer learning
- Source domain: existing alloy data (likely steels + superalloys)
- Target domain: aluminum alloys
- Train base model on large source, fine-tune on small target

## Open opportunity
- Multi-system pre-trained foundation model for alloy design
- Active learning loop to add new alloy families over time

## Backlinks
- [[_MOC]]
- [[process-alloy-design]]
- [[method-llm-nlp]] (related: transfer learning for materials)
- [[gap-public-benchmark-dataset]] (related: data scarcity)
- [[paper-jiang-2021-jmst]] (predecessor)
- [[paper-jiang-2024-acta-mater]] (successor: multi-objective)
- [[paper-jiang-2025]] (successor: chain-based)
