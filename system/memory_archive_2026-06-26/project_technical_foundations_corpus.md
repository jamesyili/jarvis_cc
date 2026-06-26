---
name: project_technical_foundations_corpus
description: Bridge-first technical study corpus at interview_prep/technical_foundations/ — 8 guides + 4-file Q&A bank serving Pinterest fluency AND frontier-lab EM interviews
metadata: 
  node_type: memory
  type: project
  originSessionId: 4bcea26e-578e-4518-8101-e6f968873599
---

Built 2026-05-31. `interview_prep/technical_foundations/` is a **bridge-first** technical study corpus serving BOTH Pinterest fluency (Reflex/UPP/Anticipation) and frontier-lab EM interviews (Anthropic/OpenAI).

**Structure:**
- `00_README_and_bridge` — the "Represent → Retrieve/Rank → Generate → Learn-from-feedback as one machine" model + "attention is retrieval" through-line + trip study plan + the aman reference-layer map.
- 8 deep-dive guides (01 representation, 02 transformers, 03 pretrain-finetune, 04 retrieval/ranking, 05 RLHF, 06 eval, 07 inference, 08 agents) — each = fundamental ↔ James's-work anchor (OmniSage/UIC/UPP-FM/CLR/preranking/Reflex/Geometric-Bandit) ↔ interview-portable 90-sec answer + self-test.
- `qa_bank/` — 4 files: `fundamentals_qa` (depth probes + model answers), `system_design_qa` (7 worked drills + discipline checklist, fills the gaps `system_design/INDEX` names), `your_systems_stories` (Pinterest-4 *technical-depth* walkthroughs), `em_judgment_qa` (technical-judgment only).
- `references/aman/` — 8 aman.ai primers as markdown ([[reference_aman_ai_primers]]).

**Calibration:** bridge-first, balanced-frontier, comprehensive; current to 2025 methods (GRPO/MLA/ultra-sparse-MoE/agentic-RL).

**Why non-obvious / load-bearing:** James's actual work touches nearly every fundamental an EM screen probes, so the corpus doubles as his "a system I built" interview material. It **complements, doesn't duplicate**: the leadership-genesis stories in `story_grill_plan.md` + `Sr. EM Interview Prep.md` (those = "tell me about a time you led X"; this = "walk me through the system technically"), and the 14 worked designs in `interview_prep/system_design/`.

Open: optional NotebookLM audio overviews; timed mock-drill pass using the system-design + stories files.
