# Build artefacts (raw JSON of paper search results)

These are the raw outputs from the API calls used to build the prelim.
Useful for:

- Reproducing the search
- Adding more papers later
- Citation graph exploration

## Files

- `prelim_papers.json` — first-pass arXiv search results (~96 papers)
- `prelim_targeted.json` — focused arXiv re-queries
- `prelim_s2.json` — Semantic Scholar results (39 Al-relevant)
- `landmarks.json` — OpenAlex top-cited method landmarks (105 papers)
- `aluminum_papers.json` — OpenAlex Al-specific filter
- `verified_dois.json` — DOIs checked for resolution
- `all_refs.json` — final deduped 64-paper set

## How to reproduce

```bash
# Run from the build/ directory
python3 build_prelim.py
```

(Or use the snippets in the `prelim-2026-06-02.md` section 8.)

## Caveat

These are point-in-time snapshots. Citation counts and paper availability
will drift. Use as a starting point, not a current state.
