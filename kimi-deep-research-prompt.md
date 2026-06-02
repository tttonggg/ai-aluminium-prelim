---
title: "Kimi K2.6 Deep Research Prompt — Aluminium AI/ML"
type: prompt-template
target-model: kimi-k2.6
tags: [kimi, prompt, deep-research]
date: 2026-06-02
---

# Kimi K2.6 Deep Research Prompt

## How to use
1. Open kimi.moonshot.cn (or Kimi API)
2. Select **K2.6** (or latest K-series long-context model)
3. **Enable** tools: web search, browsing, code execution (for arXiv/OpenAlex/S2 APIs)
4. Paste the prompt below verbatim
5. Set max output to longest setting
6. Run; expect 8-15 minutes for full Phase 1-3

## The prompt

```
You are doing a deep research synthesis for a materials-engineering literature review.
Your output is going into a preliminary research memo, so prioritize completeness,
accuracy, and traceability over brevity.

## Domain
AI / machine learning / deep learning / physics-informed neural networks /
LLM applications in:
  (a) aluminium direct-chill (DC) billet casting
  (b) aluminium hot extrusion
  (c) adjacent: alloy design, hot tearing, dendrite formation, surface defect
      detection, homogenization, CALPHAD, digital twin

## What I need you to do

### Phase 1 — Discovery (use your search tools liberally)
Find at least 40 papers published 2015-2026 across these categories:
  1. Machine learning for aluminium extrusion (process params, die design,
     surface quality, flow stress)
  2. Machine learning for DC casting (hot tearing, porosity, macrosegregation)
  3. Deep learning for aluminium defect detection (X-ray radiography,
     surface images, ultrasonic, eddy current)
  4. ML-driven aluminium alloy design (composition-property, CALPHAD+ML,
     ICME, high-throughput screening)
  5. Physics-informed NN (PINN) and neural operators (FNO, DeepONet)
     applied to metal casting or extrusion
  6. LLM / NLP for materials science literature (MatBERT, HoneyBee,
     MatTools, retrieval-augmented generation on alloy databases)
  7. Digital twin / surrogate model for aluminium manufacturing
  8. Process monitoring, closed-loop control, Bayesian optimization
     in aluminium lines

For each paper, capture:
  - Title, authors, venue, year, DOI
  - One-paragraph method summary
  - Reported accuracy / performance metric if available
  - Dataset used (size, source, public/private)
  - One-line takeaway

### Phase 2 — Synthesis
After listing the 40+ papers, write 1500-2000 words synthesizing:
  - What is the dominant method class per sub-area?
  - What is the *production maturity* per sub-area? (research / pilot /
    production-grade)
  - What datasets are publicly available?
  - What are the 5 biggest open problems?
  - What is the most promising *under-explored* direction?
  - Which authors / research groups are leading the field?
  - What is the timeline / trajectory of the field (more theory, more
    application, more data, more LLM)?

### Phase 3 — Critical assessment
Flag honestly:
  - Papers that are paywalled and you couldn't fully read
  - Papers that may not actually be aluminum-specific (despite the title)
  - Conflicts between your findings and common claims in the field
  - Patents / industry work you suspect exists but couldn't find in
    academic search

## Output format
Use this exact structure:

## 1. Executive summary (200 words)
## 2. Method × application taxonomy (table)
## 3. Paper list (grouped by sub-area, sorted by citation count desc)
   - For each paper: [N] Title (Year, Venue, Citations)
     - DOI / arXiv ID
     - Method: ...
     - Dataset: ...
     - Reported result: ...
     - One-line takeaway: ...
## 4. Synthesis (1500-2000 words)
## 5. Knowledge gaps (5-7 specific, named, researchable gaps)
## 6. Suggested 10-paper reading list
## 7. Critical assessment / caveats
## 8. Search provenance (which databases, date searched, queries used)

## Constraints
- DO NOT fabricate DOIs. If you can't verify a paper, say so.
- Prefer verified, high-citation work over obscure / unverified work.
- Prefer open-access papers so the user can fetch them.
- Use the actual paper titles, not paraphrased approximations.
- If a paper is paywalled, note it and skip the deep-dive rather than
  guess at contents.

## Tools to use
- arXiv API (http://export.arxiv.org/api/query)
- Semantic Scholar Graph API
  (https://api.semanticscholar.org/graph/v1/paper/search)
- OpenAlex API (https://api.openalex.org/works)
- Crossref API (https://api.crossref.org/works)
- Direct DOI resolution (https://doi.org/{doi})
- Web search for grey literature (industry whitepapers, conference
  proceedings, MS&T, TMS Annual Meeting)

Do not stop after one query. Run at least 8-12 search queries with
different keyword combinations. Verify your results by cross-checking
at least 10 random papers against multiple databases.

Begin.
```

## Why this prompt works
- **Phased** (Discovery → Synthesis → Critical) prevents confabulation
- **DOI verification constraint** catches the main failure mode
- **8-12 query minimum** prevents thin research
- **Specific endpoints** enable real verification (not just generation)
- **Structured output** makes the result re-usable, not just a wall of text

## Expected output size
~8,000-15,000 words. Save as a new file in `/Research/AI-Aluminium/` with date suffix.

## Variations
- **Faster (5-7 papers, 1k words)**: trim "find at least 40" to "find 8-10" and "1500-2000 words" to "500 words"
- **Focused on one sub-area**: replace the Domain section with e.g. "DC casting only"
- **Patent focus**: add Espacenet / Google Patents to the tool list
- **Chinese literature**: add CNKI, Wanfang to tool list
