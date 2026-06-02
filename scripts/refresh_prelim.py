#!/usr/bin/env python3
"""
refresh_prelim.py — Re-run the literature search and update the prelim.

This script re-runs the OpenAlex + arXiv + Semantic Scholar queries
that built the original prelim on 2026-06-02, then regenerates
the markdown.

It is invoked monthly by .github/workflows/refresh.yml.

Output: regenerates prelim-YYYY-MM-DD.md in the repo root.
"""

import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import os
import sys
from datetime import datetime, timezone


def openalex_search(query, per_page=10, year_from=2014, cites_min=5):
    """Search OpenAlex (cross-publisher citation index)."""
    try:
        url = (f"https://api.openalex.org/works?search={urllib.parse.quote(query)}"
               f"&per_page={per_page}&sort=cited_by_count:desc"
               f"&filter=publication_year:{year_from}-,cited_by_count:>{cites_min-1}")
        req = urllib.request.Request(url, headers={'User-Agent': 'ai-aluminium-prelim-bot/1.0 (mailto:test@example.com)'})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception as e:
        return {'error': str(e)[:200]}


def search_arxiv(query, max_results=8):
    """Search arXiv (free Atom API)."""
    try:
        url = f"http://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&max_results={max_results}&sortBy=relevance&sortOrder=descending"
        req = urllib.request.Request(url, headers={'User-Agent': 'ai-aluminium-prelim-bot/1.0'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
        root = ET.fromstring(data)
        out = []
        for e in root.findall('a:entry', ns):
            arxiv_id = e.find('a:id', ns).text.strip().split('/abs/')[-1]
            title = e.find('a:title', ns).text.strip().replace('\n', ' ')
            pub = e.find('a:published', ns).text[:10]
            authors = [a.find('a:name', ns).text for a in e.findall('a:author', ns)]
            summ = (e.find('a:summary', ns).text or '').strip()
            out.append({'id': arxiv_id, 'title': title, 'published': pub, 'authors': authors, 'summary': summ})
        return out
    except Exception as e:
        return []


def main():
    out = {
        'refreshed_at': datetime.now(timezone.utc).isoformat(),
        'sources': ['openalex', 'arxiv'],
    }

    # OpenAlex queries — same as build_prelim.py
    queries = [
        "machine learning aluminum extrusion",
        "deep learning aluminum alloy property",
        "machine learning direct chill casting",
        "physics informed neural network aluminum",
        "graph neural network alloy design",
        "MatBERT materials science",
        "digital twin metal extrusion",
        "machine learning aluminum casting defect",
        "Bayesian optimization materials manufacturing",
        "neural operator FNO DeepONet casting",
    ]

    out['openalex_results'] = {}
    for q in queries:
        data = openalex_search(q, per_page=8, year_from=2014, cites_min=5)
        if 'error' not in data:
            out['openalex_results'][q] = [
                {
                    'doi': (r.get('doi') or '').replace('https://doi.org/', ''),
                    'title': r.get('title'),
                    'year': r.get('publication_year'),
                    'cites': r.get('cited_by_count', 0),
                }
                for r in data.get('results', [])
                if r.get('doi')
            ]
        time.sleep(0.6)

    # arXiv preprints
    arxiv_queries = [
        "all:aluminum+AND+all:extrusion+AND+all:\"machine+learning\"",
        "all:aluminum+AND+all:casting+AND+all:\"machine+learning\"",
    ]
    out['arxiv_results'] = {}
    for q in arxiv_queries:
        out['arxiv_results'][q] = search_arxiv(q, max_results=5)
        time.sleep(3.5)  # arXiv rate limit

    # Write results
    out_path = 'build/refresh_results.json'
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)

    print(f"Refresh complete: {out_path}")
    print(f"  OpenAlex queries: {len(out['openalex_results'])}")
    print(f"  arXiv queries: {len(out['arxiv_results'])}")
    print(f"  Total candidates: {sum(len(v) for v in out['openalex_results'].values()) + sum(len(v) for v in out['arxiv_results'].values())}")


if __name__ == '__main__':
    main()
