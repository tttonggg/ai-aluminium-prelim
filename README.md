# AI/ML/LLM for Aluminium Billet Casting & Hot Extrusion

> Literature review · 64 verified references · 26 aluminium-specific papers ·
> 38 method landmarks · All DOIs cross-checked in OpenAlex
>
> Compiled 2026-06-02 · Sources: arXiv · OpenAlex · Semantic Scholar

## What this is

A preliminary research synthesis covering the intersection of
artificial intelligence (machine learning, deep learning, GNN, PINN, LLM)
and aluminium manufacturing — specifically **DC (direct-chill) billet casting**
and **hot extrusion**, with adjacent work on alloy design, defect detection,
hot tearing, microstructure, and digital twins.

## Quick start

- 📥 **[Read the main prelim](prelim-2026-06-02.md)** (30 KB) — start here
- 🗺️ **[Map of content](_MOC.md)** — links all notes
- 📚 **[Top 5 papers](reading-list/reading-top-5.md)** — read these first
- 🤖 **[Kimi K2.6 deep-research prompt](kimi-deep-research-prompt.md)** — run for fresh synthesis
- 🧠 **[Method notes](method-notes/)** — PINN, GNN, LLM/NLP, digital twin, Bayesian opt
- 🏭 **Process notes** (in root) — DC casting, hot extrusion, defect detection, alloy design, hot tearing, microstructure
- 🔍 **[Open gaps](gaps/)** — 5 named research opportunities
- 🛠️ **[Build artifacts](build/)** — raw JSONs, daily-check script

## Honest disclosure

- Every DOI in the prelim was **verified in OpenAlex** before inclusion
- I dropped 9 DOIs from memory that OpenAlex flagged as non-existent
- **Patent literature is NOT covered** (Sapa, Hydro, Constellium industrial work)
- **Chinese-language journals are under-represented** (OpenAlex coverage gap)
- I read **abstracts/titles**, not full papers, for this prelim
- Citation counts are as of 2026-06-02

## Files

```
.
├── README.md                                  ← this file
├── _MOC.md                                    ← map of content
├── prelim-2026-06-02.md                       ← main prelim (with frontmatter)
├── ai_aluminium_prelim.md                     ← same, plain version
├── kimi-deep-research-prompt.md               ← Kimi K2.6 prompt template
├── process-dc-casting.md
├── process-hot-extrusion.md
├── process-defect-detection.md
├── process-alloy-design.md
├── process-hot-tearing.md
├── process-microstructure.md
├── method-notes/
│   ├── method-pinn.md
│   ├── method-gnn.md
│   ├── method-llm-nlp.md
│   ├── method-digital-twin.md
│   └── method-bayesian-opt.md
├── gaps/
│   ├── gap-public-benchmark-dataset.md
│   ├── gap-billet-extrusion-coupling.md
│   ├── gap-llm-extrusion-agent.md
│   ├── gap-neural-operator-al.md
│   └── gap-closed-loop-digital-twin.md
├── reading-list/
│   └── reading-top-5.md
├── papers/                                    ← 1-page paper notes (populated by cron)
├── build/
│   ├── README.md
│   ├── al_ai_daily_check.py                   ← daily OpenAlex poll
│   ├── *.json                                 ← raw search results
│   └── refresh_results.json                   ← updated by GH Action
├── scripts/
│   └── refresh_prelim.py                      ← monthly refresh
└── .github/
    └── workflows/
        └── refresh.yml                        ← monthly GH Action
```

## How to use

1. **Read** `prelim-2026-06-02.md` for the field map
2. **Run** the Kimi prompt in `kimi-deep-research-prompt.md` for a fresh synthesis
3. **Open** in Obsidian to get graph view + backlinks (use `[[wikilinks]]`)
4. **Clone & extend** — add your own paper notes into `method-notes/`
   or as 1-page summaries under `papers/`

## Automated updates

- **GitHub Action** runs `scripts/refresh_prelim.py` monthly (1st @ 03:00 UTC)
- **Cron watchdog** (Hermes side): daily OpenAlex poll + weekly digest + monthly refresh
- All updates verified against OpenAlex before commit
- DOIs in `build/.seen_dois.json` prevent re-alerting

## Tools used

- **arXiv** API — http://export.arxiv.org/api/query
- **OpenAlex** — https://api.openalex.org/ (250M works, citation index)
- **Semantic Scholar** Graph API — paper search & citations
- **Python 3.12** stdlib (no extra deps for the build script)

## Provenance

Build date: 2026-06-02
Build process: see `prelim-2026-06-02.md` section 8 and 10

---

*If you find a citation that's wrong, please open an issue or PR with the
corrected DOI — the verification was done in batch and may have edge cases.*
