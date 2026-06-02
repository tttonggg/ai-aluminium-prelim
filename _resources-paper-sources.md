---
title: "Free research-paper sources — community-sourced list"
type: resource-list
date: 2026-06-02
source: x-posts-curated
tags: [resources, papers, open-access, research]
verification_status: PARTIAL
---

# Free Research-Paper Sources

A community-sourced list, distilled from X posts. Categorized by
legitimacy and reliability.

## ✅ Verified legitimate (safe to use, no legal concerns)

| Source | URL | Best for | Cost |
|---|---|---|---|
| **arXiv** | https://arxiv.org | Preprints in physics, CS, math, ML | Free |
| **OpenAlex** | https://api.openalex.org | 250M+ works, citation index, API | Free |
| **MDPI** | https://www.mdpi.com | Open-access journal articles (incl. Metals, Materials, Machines) | Free |
| **Springer Open Access** | https://link.springer.com | Thousands of CC-licensed books/papers | Free |
| **JURN** | http://jurn.link | Cross-disciplinary academic search | Free |
| **DOAJ** | https://doaj.org | Directory of Open Access Journals | Free |
| **Google Scholar** | scholar.google.com | Search + "PDF" filter trick for free versions | Free |

**This is the workflow I've been using** for the aluminium-ML prelim.
arXiv + OpenAlex + S2 + Crossref + DOAJ + MDPI is more than enough to
cover this field — most of the verified papers in this vault came from
those sources.

## ⚠️ Verify-claim (status claimed but not independently confirmed)

| Source | Claim | Note |
|---|---|---|
| **ACM Digital Library** | "Completely open access now" | Unverified — ACM has been mixed OA/free historically. Worth checking the specific venues we need (KDD, ICLR, NeurIPS) but don't take the blanket claim at face value |
| **NotebookLM** | https://notebooklm.google.com | Google's notebook for ingesting PDFs — useful for summarizing our 64-paper vault |
| **SciSpace** | https://scispace.com | AI tool for paper Q&A |
| **Consensus** | https://consensus.app | AI search across peer-reviewed sources |
| **Elicit** | https://elicit.com | AI research assistant |
| **ResearchRabbit** | https://researchrabbit.ai | Citation-graph paper discovery |
| **Connected Papers** | https://connectedpapers.com | Visual paper-relationship graph |
| **ExplainPaper** | https://explainpaper.com | AI paper explanation |

These are useful but each has its own rate limit / pricing tier / terms.
The user (you) should evaluate whether they want to load personal papers
into 3rd-party AI services.

## ⛔ Legally grey / likely infringing (don't recommend)

| Source | Status |
|---|---|
| **Sci-Hub** | Hosts pirated papers; illegal in most jurisdictions |
| **LibGen** | Same — hosts pirated content |
| **Anna's Archive** | Same |

These are *real* resources used by many researchers, but they exist in
a legal grey zone (or outright illegal depending on jurisdiction). I'm
not recommending them, and any academic work you publish using Sci-Hub
papers can't include those citations in a peer-reviewed venue (the
publisher will reject them).

For the aluminium-ML project, **you don't need them** — the legitimate
sources cover 95%+ of this literature.

## 🔧 Recommended additions to our workflow

1. **Connected Papers** — paste a DOI from [[paper-hengst-se-2025]] or
   [[paper-jiang-2025]] to discover 5-10 related works we missed
2. **Elicit** — for asking "what's the consensus on PINN for Al casting?"
3. **DOAJ** — for finding non-MDPI OA journals (a lot of Al work is in
   non-OA journals, so this is limited)
4. **NotebookLM** — load our 64 papers as a personal knowledge base, ask
   "what methods are missing from our gaps analysis?"

## What I'd actually do next with these

1. Take the **top 3 verified papers** in `papers/` and paste their DOIs
   into Connected Papers — see what they cite / get cited by
2. For any unverified Kimi paper, try **Elicit** — it often returns the
   correct paper even when OpenAlex misses
3. Re-verify **Parlak & Emel 2024** (still in our Tier-1 inconclusive)
   using Elicit's author + paper-title search

## Backlinks
- [[_MOC]]
- [[kimi-report-2026-06-02]] (verification workflow)
- [[_verification-tier1-results]]
