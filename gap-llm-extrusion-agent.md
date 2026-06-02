---
title: "Gap: LLM Agent for Extrusion Trial Loop"
tags: [gap, llm, agent, automation]
priority: high
date: 2026-06-02
---

# Gap: LLM Agent for Extrusion Trial Loop

## The gap
No paper found using an LLM to autonomously:
1. Read in-line extrusion sensor data (force, temperature, profile scan)
2. Diagnose root cause of quality deviation
3. Recommend die-adjustment or process-param change
4. Request human approval for the change
5. Track outcome, learn from results

## Why it matters
- Current extrusion lines have alarm thresholds but no closed-loop reasoning
- An expert operator takes 5-20 years to develop pattern recognition
- LLM + RAG over historical run logs + standards (EN 755) could encode this

## Architecture
```
Sensors → RAG over run-logs + standards → LLM diagnostic
  → recommendation → human-in-loop approval → action
  → outcome logged → fine-tune for next run
```

## Reference framework
- Pak & Barati Farimani (2025), AdditiveLLM — arXiv `2501.17784` (AM version)
- Zhao et al. (2024) — LLM-based multi-agent manufacturing system —
  arXiv `2405.16887` (general manufacturing)

## Open opportunity
- LLM agent that integrates with MES / SCADA / OPC-UA
- Multimodal LLM (visual profile scan + scalar sensors)
- Causal reasoning: "if I raise temperature 10°C, what improves, what risks"

## Effort estimate
6-12 months for proof-of-concept with industrial partner.
