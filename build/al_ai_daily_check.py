#!/usr/bin/env python3
"""
al_ai_daily_check.py — Lightweight daily OpenAlex poll.
Looks for new Al-ML papers published in the last 14 days,
compares to a "seen" cache, and emits a digest only when new papers exist.

Designed for cron — runs silently when nothing new is found,
delivers via Telegram when something is worth seeing.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime, timedelta, timezone

SEEN_FILE = "/root/ObsidianVault/Research/AI-Aluminium/build/.seen_dois.json"
RESULTS_FILE = "/root/ObsidianVault/Research/AI-Aluminium/build/daily_digest_latest.json"

QUERIES = [
    "machine learning aluminum extrusion",
    "machine learning direct chill casting",
    "deep learning aluminum defect detection",
    "machine learning aluminum alloy design",
    "physics informed neural network aluminum",
    "neural operator aluminum casting",
    "LLM materials science aluminum",
    "digital twin aluminum extrusion",
]


def openalex_search(query, since_date, per_page=5):
    """Search OpenAlex for recent papers matching query."""
    try:
        url = (f"https://api.openalex.org/works?search={urllib.parse.quote(query)}"
               f"&per_page={per_page}&sort=publication_date:desc"
               f"&filter=publication_date:>{since_date}")
        req = urllib.request.Request(url, headers={
            'User-Agent': 'ai-aluminium-prelim-bot/1.0 (mailto:test@example.com)'
        })
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception as e:
        return {'error': str(e)[:200]}


def load_seen():
    if not os.path.exists(SEEN_FILE):
        return {}
    try:
        with open(SEEN_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_seen(seen):
    os.makedirs(os.path.dirname(SEEN_FILE), exist_ok=True)
    with open(SEEN_FILE, 'w') as f:
        json.dump(seen, f, indent=2)


def main():
    # Look at papers from last 14 days
    since = (datetime.now(timezone.utc) - timedelta(days=14)).strftime("%Y-%m-%d")
    seen = load_seen()

    new_papers = []
    for q in QUERIES:
        data = openalex_search(q, since_date=since, per_page=5)
        if 'error' in data:
            time.sleep(0.6)
            continue
        for r in data.get('results', []):
            doi = (r.get('doi') or '').replace('https://doi.org/', '')
            if not doi:
                continue
            if doi in seen:
                continue
            new_papers.append({
                'doi': doi,
                'title': r.get('title'),
                'date': r.get('publication_date'),
                'cites': r.get('cited_by_count', 0),
                'venue': ((r.get('primary_location') or {}).get('source') or {}).get('display_name') if r.get('primary_location') else None,
                'query': q,
            })
            seen[doi] = datetime.now(timezone.utc).isoformat()
        time.sleep(0.6)

    save_seen(seen)

    # Dedupe
    seen_this_run = set()
    unique = []
    for p in new_papers:
        if p['doi'] in seen_this_run:
            continue
        seen_this_run.add(p['doi'])
        unique.append(p)

    digest = {
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'window': since,
        'new_paper_count': len(unique),
        'papers': unique,
    }

    os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
    with open(RESULTS_FILE, 'w') as f:
        json.dump(digest, f, indent=2)

    # Exit 0 always — cron job is the watchdog, agent decides what to do
    if unique:
        print(f"NEW: {len(unique)} papers since {since}")
        for p in unique[:10]:
            print(f"  • {p['title'][:80]}  ({p['date']})  {p['doi']}")
    else:
        print(f"No new papers since {since}. Cache size: {len(seen)}")


if __name__ == '__main__':
    main()
