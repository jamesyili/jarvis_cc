---
name: reference_aman_ai_primers
description: "aman.ai Distilled AI primers — the downloaded PDFs are image-only (no text layer); read the converted markdown or WebFetch the live pages, don't OCR"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4bcea26e-578e-4518-8101-e6f968873599
---

aman.ai "Distilled AI" primers (Aman Chadha) are top-tier deep references for ML/LLM/transformers/RL/agents/MoE interview prep. James's downloaded PDFs (`interview_prep/aman_*.pdf`, now removed) were **image-only / glyph-drawn — no extractable text layer** (only `aman_rl_ppo` had one), so pdftotext/pymupdf can't read their bodies.

The clean text is freely available on the live site at `https://aman.ai/primers/ai/<slug>/`. Slug map: transformers, attention, agents, agentic-design-patterns (= aman_agent_systems), agentic-RL (case-sensitive), reinforcement-learning (= aman_rl), preference-optimization (= aman_rl_ppo), mixture-of-experts (= aman_moe).

8 of them are downloaded as **searchable markdown** at `interview_prep/technical_foundations/references/aman/*.md` (~2.3M chars) — this is the durable source. To read/mine: use those `.md` files, or WebFetch the live page for clean text. **Don't OCR the PDFs.**

PDF→text recipe when genuinely needed: `python3 -m venv /tmp/pdfvenv && /tmp/pdfvenv/bin/pip install pymupdf` (PEP-668 blocks system pip; use a venv). For HTML→markdown add `beautifulsoup4 markdownify lxml`; aman pages keep the main content in `div.post-content`, math as plain `$$…$$`.

Part of [[project_technical_foundations_corpus]].
