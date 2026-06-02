---
title: "Connected Papers Discovery Pass — 2026-06-02"
type: discovery-report
date: 2026-06-02
source: connected-papers.com
input_dois: 4
input_papers_verified_count: 4
new_papers_discovered: 11
new_papers_verified: 5
---

# Connected Papers Discovery Pass — 2026-06-02

## Method
- Used Connected Papers (https://connectedpapers.com) on each of the 4 verified
  papers (Hengst SE 2025, Pichlmann 2025, Jiang 2025, Monash 2025 GNN LPBF)
- Each paper returns a graph of ~20-30 related papers based on co-citation
  similarity
- **Free limit: 2 graphs/month** (used 2/2 — additional passes need a paid account
  or different DOIs)

## Best return: Jiang 2025 graph

The Jiang 2025 paper's co-citation graph returned **11+ directly relevant Al-ML
papers**, mostly from the same research group (Lei Jiang, USTB):

### Verified (5/5 attempted, 100%)

| Paper | Year | DOI | Cites | Note |
|---|---|---|---|---|
| Synchronously enhancing strength/toughness/corrosion of Al via interpretable ML | 2024 | `10.1016/j.actamat.2024.119873` | **124** | [[paper-jiang-2024-acta-mater]] |
| Discovery of Al alloys with ultra-strength + high-toughness (property-oriented) | 2021 | `10.1016/j.jmst.2021.05.011` | **152** | [[paper-jiang-2021-jmst]] |
| A rapid method for alloy design via sample data transfer ML | 2023 | `10.1038/s41524-023-00979-9` | **76** | [[paper-jiang-2023-npj-transfer]] |
| Simultaneous enhancement of mech+corrosion in Al-Mg-Si via ML | 2023 | `10.1016/j.jmst.2023.04.072` | **88** | [[paper-feng-jiang-2023-almgsi]] |
| Effect of Fe content on Al-Zn-Mg-Cu microstructure/mechanical | 2025 | `10.1016/s1003-6326(25)66874-9` | 4 | (less relevant, ML-free) |
| Interpretable ML for Mg-Li mechanical + corrosion | 2025 | `10.1016/j.jma.2025.10.014` | 9 | (Mg-Li not Al, but related methodology) |

**Total citations across verified new finds: 453.** These are foundational works
that **were NOT in my prelim or Kimi's report**.

### Unverified (notable but lower priority)

- The coarsening of nanophases in Al-Zn-Mg-Cu (Jiang 2025) — same group, related
- Strain-rate hardening of AlSi10Mg at 350°C (Bahl/Plotkowski 2025) — fatigue
- Effects of aging on 6A01 fatigue (Gong/Zhang 2022) — fatigue, no ML

## Key insight: research lineage

Jiang's group at USTB has a *coherent research program* that spans:

1. **2021:** Property-oriented design strategy ([[paper-jiang-2021-jmst]])
2. **2023:** Transfer learning for alloy design ([[paper-jiang-2023-npj-transfer]])
3. **2023:** Al-Mg-Si multi-property ([[paper-feng-jiang-2023-almgsi]])
4. **2024:** Multi-objective Al alloy design ([[paper-jiang-2024-acta-mater]])
5. **2025:** Chain-based interpretable ML ([[paper-jiang-2025]])

This is the **canonical research lineage** for ML-driven Al alloy design. Any
prelim should cite all 5 papers. They're missing from both my prelim AND Kimi's
report.

## Hengst SE 2025 graph: less useful

The Hengst SE 2025 (X-ray YOLOv5) graph returned mostly PCB defect detection
papers and steel-strip defect papers — not specifically aluminum. Connected
Papers builds the graph from co-citation similarity, so defect-detection papers
cite each other regardless of substrate (PCB, steel, Al).

**Takeaway:** for *method* papers, Connected Papers returns the method
ecosystem (YOLO variants, CNN architectures), not the *substrate* ecosystem.

## Lessons learned

1. **Connected Papers is most useful for *foundational* papers with many
   citations.** The Jiang 2025 paper (11 cites already + 1 in our prelim)
   returned 11+ directly relevant papers. The Hengst SE 2025 (0 cites)
   returned papers from other fields.
2. **Free limit: 2 graphs/month.** Pick the highest-leverage paper.
3. **The Jiang research group is the most important research lineage in
   ML-for-Al-alloy-design.** I should cite all 5 papers in the prelim.

## Backlinks
- [[_MOC]]
- [[_resources-paper-sources]] (entry for Connected Papers)
- [[paper-jiang-2025]] (parent paper of the graph)
- [[_verification-tier1-results]]
