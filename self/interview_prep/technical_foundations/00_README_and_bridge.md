# Technical Foundations — the bridge corpus

**Built:** 2026-05-31 (pre-OOO trip study materials)
**Purpose:** One unified technical study corpus serving two goals at once —
1. **Pinterest fluency** — speak Reflex / UPP / Anticipation at the architecture level, not just the strategy level.
2. **Frontier-lab EM interviews** (Anthropic, OpenAI) — solidify the fundamentals a technical EM screen probes, anchored to systems you actually built.

**Format:** Written deep-dive guides (this folder) + an interview Q&A bank (`qa_bank/`). No audio, no flashcards — by design.

**How this differs from what you already have in `interview_prep/`:** the Hao Hoang book (`llm_system_interview.md`) is a *generic reference*; `study_plan_for_onsite.md` tiers it for the *Integrity seat*; `system_design/` is *whiteboard practice*. This corpus is the missing **bridge layer** — each fundamental taught in your own terms, anchored to your live work, then translated into interview-portable form. Read these *alongside* the book chapters they map to (cross-refs in each guide).

---

## The one mental model (read this first — everything hangs off it)

A recommender system, a foundation model, an LLM, and an agent are **the same machine at different scales.** Four stages, one loop:

```
   ┌──────────────────────────────────────────────────────────────┐
   │                                                              │
   ▼                                                              │
[1] REPRESENT  ──→  [2] RETRIEVE / RANK  ──→  [3] GENERATE / DECIDE │
 raw signal →        given a context vector,    produce the output:  │
 vectors in a        find + order the best       next token / next   │
 learned space       candidates                  pin / next action   │
                                                          │          │
                                                          ▼          │
                                              [4] LEARN FROM FEEDBACK ┘
                                              a reward / preference
                                              signal improves the system
```

- **[1] Represent** = embeddings + pretraining. *Turn tokens / user actions / pixels into vectors whose geometry encodes meaning.* → guides **01, 02, 03**
- **[2] Retrieve/Rank** = the core operation of both stacks. → guide **04**
- **[3] Generate/Decide** = decoding (LLM) or scoring+blending (recsys). → guides **04, 07**
- **[4] Learn from feedback** = RLHF, reward modeling, bandits, the human-correction loop. → guide **05**, with **06** (eval) as the measurement substrate and **08** (agents) as the loop made autonomous.

### The unification that makes you sound senior

**Attention *is* retrieval.** A query attends over keys and values = a soft, differentiable nearest-neighbor lookup over the sequence. A transformer is a stack of differentiable retrieval operations; a recsys two-tower retriever is the *non-differentiable, billion-item* version of the same operation. Once you say this out loud in an interview, your recsys background stops being "adjacent experience" and becomes "I've been building the retrieval primitive at a scale most LLM people never touch." That is the single highest-leverage sentence in this whole corpus.

Your three Pinterest systems are this loop, instantiated:

| Stage | UPP | Retentive Recs / Anticipation | Reflex |
|---|---|---|---|
| Represent | FM pretrain on user-level next-token; CLR towers | OmniSage fused space; UIC clusters | code/state as context; structured cards |
| Retrieve/Rank | CLR dual-tower retrieval, surface rankers | geometric prediction → CLR conditioning | playbooks retrieve opportunities; DS scores |
| Generate/Decide | candidate sets per surface | predicted UICs, LLM "next best action" | Build agent emits validated code edits |
| Learn from feedback | online A/B, relevance loss | Geometric Bandit (Thompson, log-lift) | human comment → permanent structured pattern |

---

## Module index

| # | Guide | Fundamental | Your anchor | Book ch. (Hoang) |
|---|---|---|---|---|
| 00 | This file | the bridge + how to study | — | Ch 1–2 |
| 01 | `01_representation_learning_and_embeddings.md` | embeddings, contrastive learning, two-tower | OmniSage, UIC, UPP FM, CLR | (recsys-native; Ch 3 adjacents) |
| 02 | `02_transformers_and_attention.md` | QKV attention, decoder-only, positional, KV cache | UPP FM, OneTrans, L500 sequence | Ch 3, 15–16 |
| 03 | `03_pretraining_finetuning_transfer.md` | self-supervised pretraining, SFT, transfer, scaling | UPP three-tier, cross-surface, your blog topic | Ch 13–14, 20–22, 26, 30 |
| 04 | `04_retrieval_ranking_two_tower.md` | the funnel, ANN, negative sampling, calibration, diversity | CLR, overfetch, O/E, SSD, blending | (recsys-native) + Ch 29 |
| 05 | `05_rlhf_preference_optimization.md` | RLHF pipeline, reward models, DPO, RLVR, bandits | Reflex feedback loop, RR Geometric Bandit | Ch 27–28 |
| 06 | `06_evaluation_simulation_validity.md` | offline/online metrics, A/B, contamination, eval design | Reflex Simulate/Prove, UPP eval dispute, RR holdout | Ch 23–25 |
| 07 | `07_inference_and_serving.md` | prefill/decode, throughput, quantization, distillation, MoE | UPP GPU serving, overfetch caps, GSS | Ch 6–7, 15–19, 29 |
| 08 | `08_agents_tool_use_multiagent.md` | agent loops, tool use, multi-agent, guardrails, agent eval | Reflex, Pinkerton, RR reasoning layer | Ch 24 (agentic benchmarks) |

**Q&A bank** (`qa_bank/`): `fundamentals_qa.md` (depth probes per module), `system_design_qa.md` (gap-targeted drills from the Anthropic post-mortem), `your_systems_stories.md` ("tell me about a system you built," at interview depth), `em_judgment_qa.md` (technical-leadership calls).

---

## How to study this on the trip

You have ~3 weeks. This is **not** 50 hours of book-grinding — it's the high-leverage subset, internalized in your own terms.

**Pass 1 — read the spine + all eight guides front to back (one sitting each).** Goal: install the mental model and see your own work as the worked example. ~45 min/guide.

**Pass 2 — for each guide, do the "self-test" at the bottom out loud, from memory.** If you can't, that's the chapter of the book to read deeply. The guides tell you exactly which.

**Pass 3 — the Q&A bank, as active recall.** Especially `system_design_qa.md` — your Anthropic post-mortem says reading gets you to "informed candidate," *drilling* gets you to "this person has answered these before." Time-box the system-design drills to 45 min each.

**Priority order if time is short** (serves both goals, weighted to your interview gap):
1. **05 (RLHF) + 06 (Eval)** — your Anthropic loop died here (didn't resolve the adversarial case; led with metrics over the trade-off). Also the Integrity seat's day-to-day.
2. **04 (Retrieval/Ranking)** — your deepest moat; make sure you can *teach* it, not just do it.
3. **02 (Transformers)** — vocabulary floor; the one place a generic answer caps you.
4. **01, 03** — your moat + the pretrain-finetune story (= your blog topic; double-duty).
5. **07, 08** — breadth; one-pass each unless probed.

---

## Interview-portable: the "systems I built" map

When an interviewer probes a fundamental, *don't* answer in the abstract — bridge to a system you built, go three levels deep, then surface back up. The map:

- **"How would you train an embedding / representation?"** → OmniSage: fusing CLIP visual + co-engagement graph + pin-board topology so geometry = *functional utility* (hiking boot ≈ granola bar via "camping" boards), not visual similarity. Then UPP FM: pretraining user representations via user-level next-token prediction.
- **"Design a retrieval system."** → CLR two-tower, UIC as the conditioning vector, ANN over billions of pins, overfetch/cap trade-offs, in-batch + hard negatives, calibration (O/E) before it hits ranking.
- **"How does RLHF / preference learning work?"** → Reflex: every human comment becomes a permanent structured pattern (reward signal → policy update, but with a human-legible state). RR Geometric Bandit: Thompson sampling over LSH-hashed embedding regions, log-lift reward optimizing *momentum* not raw CTR, negative feedback collapsing exploration.
- **"How do you evaluate this?"** → RR holdout (moving WAU via ranking is *rare* — that's the validity story); UPP eval-methodology dispute (when the *metric* is the bottleneck, more bodies don't help); Reflex eval-against-real-PRs.
- **"Design an agent / multi-agent system."** → Reflex: Claude Code sessions *are* the agents, repo is the database, git is the audit trail, Skeptic is the adversarial gate, blast-radius via allowlist + diff caps.

Each guide ends with the tightened, interview-ready version of its bridge.

---

## Reference layer — the aman.ai primers (deep-dive backstop)

You have 8 aman.ai "Distilled AI" primers. They are the **deep reference** — hit one when a guide's self-test exposes a gap, *not* as primary reading. Coverage clusters on your **frontier-LLM gap** (transformers, RL, agents, MoE), not your recsys moat — well-targeted.

**Two copies of each:** the original image-only PDF in `interview_prep/aman_*.pdf` (visual, not text-extractable), and a **downloaded clean-markdown copy in `references/aman/*.md`** (grep-able, searchable, ~2.3M chars total — fetched from the live aman.ai pages on 2026-05-31). Use the `.md` to read/search; the PDF for figures.

**Three-layer reading order per topic:** bridge guide (synthesis, *yours*) → Hoang chapter (interview-tiered) → aman primer (go deep only if needed).

| Guide | aman primer — searchable markdown | Depth caveat |
|---|---|---|
| 02 Transformers | `references/aman/transformers.md`, `references/aman/attention.md` | read for intuition; **don't derive flash-attention** (Tier 3) |
| 05 RLHF | `references/aman/rl.md`, `references/aman/rl_ppo.md`, `references/aman/agentic_rl.md` | great for RM/DPO/RLVR; **PPO clipped-objective math is Tier 3** — skim, don't grind |
| 07 Inference | `references/aman/moe.md` | MoE = "know what it is" (Tier 3); resist the routing rabbit hole |
| 08 Agents | `references/aman/agents.md`, `references/aman/agent_systems.md`, `references/aman/agentic_rl.md` | your ahead-of-curve area — read for vocabulary/patterns, you already have the system |
| 01, 03, 04, 06 | *(none — not downloaded)* | 01/04 are your moat; 03/06 are well-covered by the Hoang book. aman.ai has Recommendation-Systems and NLP primers online if you ever want a 04/01 backstop — but you don't need them. |

**Mining note:** the `.md` copies are now text, so I *can* pull specific aman passages into the Q&A bank where a drill needs sharper backing (e.g., the agent system-design drill ← `agents.md`/`agent_systems.md`; RLHF drills cross-checked vs `rl_ppo.md`). Math fidelity in the markdown is good for prose/code/structure; some display equations render better in the source PDF.

---

## Cross-references (existing assets)

- `interview_prep/llm_system_interview.md` — the Hoang book (the reference these guides distill)
- `interview_prep/study_plan_for_onsite.md` — Integrity-seat chapter tiering
- `interview_prep/system_design/00_FRAMEWORK.md` — the whiteboard framework
- `interview_prep/openai_call_prep_2026-05-27.md` — the Anthropic-loop anti-patterns (load-bearing for the system-design Q&A)
- `work/projects/{upp,retentive_recs,reflex}/` — the source-of-truth technical docs the anchors draw from
```
