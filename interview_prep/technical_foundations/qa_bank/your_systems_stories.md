# "A system I built" — technical-depth stories (Pinterest 4)

**How to use:** when an interviewer says *"walk me through a system you built"* or probes a fundamental, bridge to one of these and go **three levels deep**. These are the **technical** walkthroughs — architecture, the hard decisions, the depth-probes. They **complement** the *leadership/genesis* narratives in `story_grill_plan.md` + `Sr. EM Interview Prep.md` (which answer "tell me about a time you led X"). Same systems, different interview question.

> Per story: **one-liner → the technical frame (problem / your role / architecture & key decisions / hard problem / results) → depth-probes with answers → which fundamental to lead it with.**

---

## 1. UPP — foundation-model pretraining for user representations

**One-liner:** *"A three-tier platform that pretrains a single user representation with user-level next-token prediction, then fine-tunes base retrieval and ranking models from it, and surface-specific models on top — the foundation-model paradigm applied to users."*

**Problem:** Every surface (Homefeed, Notif, Search, P2P) was building its own user models from scratch — duplicated effort, no shared learning, no transfer. The bet: invest in one shared representation, specialize on top.

**Your role:** Retrieval lead — own the base retrieval model (CLR) and the only shipped cross-surface online wins.

**Architecture & key decisions:**
- **FM**: user-level next-token prediction over action sequences (decoder-only, self-supervised) → a reusable user representation.
- **Base**: retrieval = dual-tower **CLR**, ranking = **CFM**, each fine-tuned from the FM.
- **Surface**: fine-tuned per surface.
- Key decision I drove: **augment the base CLR with CFM-style cross-surface training (2b) before splitting into separate models (2a)** — less model maintenance, better dev velocity, consistent with the platform thesis.

**Hardest problem — cross-surface transfer:** shipping it onto Notif worked (compounding wins, latest +200k WAU). But on P2P it's *"not hurting, not clearly helping."* The discipline I'd emphasize: **transfer is empirical per target**, and the first fork is **measurement vs. generalization** — *is the offline eval even capturing transfer?* If it's a measurement-design problem, more engineers won't fix it; if the eval is right and it still doesn't transfer, that's a real negative to accept and reframe. Diagnosing that *before* throwing bodies at it is the call.

**Results:** Notif retrieval ~286k WAU (launched + in-flight); GPU serving shipped and adopted by Notif/P2P; the only shipped cross-surface online wins in the program.

**Depth-probes:**
- *"Why pretrain a user model instead of features?"* → amortize the expensive representation across every consumer; surfaces specialize cheaply (the platform thesis = the frontier-lab business model).
- *"What's the self-supervised objective?"* → user-level next-token prediction — the GPT recipe over user actions; the learned per-position vector is the user state.
- *"How do you know transfer helped?"* → held-out eval *on the target* + ablate the pretrained init; watch for negative transfer; separate measurement from generalization.
- *"Two-tower training details?"* → contrastive, in-batch + hard negatives, logQ popularity correction, ANN serving.

**Lead with UPP for:** representation learning (01), pretrain-finetune/transfer (03), the foundation-model platform design (system-design Drill 4).

---

## 2. Retentive Recs / Anticipation — prediction engine + RL feedback loop

**One-liner:** *"A system that moves recommendation from reactive matching to geometric prediction in an embedding space — cluster each user's interests, predict where they're heading, and close an RL feedback loop with a Thompson-sampling bandit."*

**Problem:** the explore/exploit dilemma — exploit causes boredom/churn, explore feels like random noise. Goal: **engineered serendipity** — show something the user didn't know they wanted but feels immediately relevant. Moving *retention* via ranking is historically rare.

**Your role:** program lead (named on the Engineering Blog), KDD author (Prior Work / Architecture / Future Work).

**Architecture & key decisions (the three innovations):**
1. **Personalized representation** — cluster over *only the user's engaged pins* (L500 sequence, complete-link hierarchical) in OmniSage space, dynamic cluster count. Easier and more accurate than clustering the global catalog.
2. **Embedding-space prediction at the interest level** — vector transport (drift), geometric mixups (slerp between clusters), graph completeness (fill structural voids). Predict *where in the space* the user is heading, not which pin.
3. **The RL feedback loop — Geometric Bandit:** Thompson sampling over **LSH-hashed embedding regions** (distinct interests hash distinctly → no signal bleed), **log-lift reward** (momentum, not raw CTR, so stale-popular doesn't crowd out growing), negative feedback collapses exploration.

**Hardest problem — reward design:** raw CTR degenerates toward high-volume stale interests. Choosing **log-lift** (engagement vs the user's own baseline) is a deliberate reward-design decision — exactly analogous to choosing what an LLM RM rewards. And deprecating Semantic-IDs for **geometric hashing** to avoid aliasing distinct interests.

**Results:** UCAN WAU holdout-validated (the holy-grail signal — topline retention via ranking); three-word feedback loop launched on partial CG funnel (core hypothesis validated); the technical engine under Pinterest's company-wide Anticipation vision (CTO-amplified).

**Depth-probes:**
- *"How do you balance explore/exploit?"* → **Thompson sampling** (posterior width drives exploration) > epsilon-greedy (hand-tuned constant); per-region Beta posteriors.
- *"Why log-lift?"* → optimize momentum not absolute engagement, so the reward doesn't degenerate — a reward-design choice against Goodhart.
- *"How does the LLM fit?"* → UIC as a **dynamic prompt**: VLM ingests a cluster's pins → deduces intent ("building a deck") → next-best-action ("needs staining") → query the embedding space for that future cluster.
- *"Cold start?"* → synthetic profiling — match a low-signal fragment to a mature synthetic cluster.

**Lead with RR for:** RLHF/bandits/reward design (05), representation/clustering (01), the agent-reasoning-over-state angle (08).

---

## 3. Preranking — a first-principles alignment/accuracy framework (your paper)

**One-liner:** *"We derived, from a formal serving objective, that the preranking objective decomposes into exactly two things — alignment with the main ranker and accuracy on engagement — proved they combine linearly, and shipped it for real A/B wins."*

**Problem:** preranking (the cheap L1 stage between retrieval and the heavy ranker) combined offline metrics and training losses **heuristically** — no theory for *what* to target or *how* to combine. And offline metrics didn't predict online lift (PR-AUC even predicted winners *backwards*).

**Your role:** co-author + editor / pressure-tester (RecSys 2026 submission).

**Architecture & key results:**
- **Decomposition:** reward lift = **alignment** (overlap with the main ranker's selections) + **accuracy** (conditional engagement above a shared ranker threshold). **Exclusivity** (no third scalar needed) + **linearity** (linear combos are structurally correct, not just convenient).
- **The counterintuitive result:** measure alignment on the **unimpressed** candidate pool, not impressed traffic — impressed data is biased toward what survived to exposure. This alone moved offline winner-prediction **70% → 80%**.
- **Training:** keep the production accuracy branch; *add* an alignment branch (KL distillation from the L2 teacher + weighted pairwise) on the unimpressed distribution. **+1.43% save** vs accuracy-only.

**Hardest problem — Sample Selection Bias:** L1 trains on impressed items but serves on the post-CG pool ("an exam beyond the syllabus" = train/serve distribution shift). Plus the engineering: a **dual-distribution trainer** (impressed accuracy stream + unimpressed alignment stream) that zeroes ~40% of batches to balance the two — $200/run vs $110 baseline.

**Results:** calibrated offline metric predicts online winners at 80% (forward-in-time test set, distribution-shift-robust); two-part training objective beat both accuracy-only and the heuristic-alignment production baseline in multiple A/B tests, guardrails neutral.

**Depth-probes:**
- *"Offline up, online flat — why?"* → offline↔online correlation; alignment-on-impressed lies; calibrate the metric against online lift.
- *"What is SSB and how do you fight it?"* → train/serve shift; unimpressed negatives + p-select + KD.
- *"Why measure on unimpressed?"* → impressed reweights toward exposed positions + mixes in exposure effects; can't recover the true alignment term.

**Lead with preranking for:** eval/offline-online correlation (06), retrieval/ranking cascade (04). This is your **eval moat** — most candidates can't formalize why offline metrics mislead.

---

## 4. Reflex — a production multi-agent system

**One-liner:** *"A self-healing discovery stack — AI agents continuously Detect opportunities, Build validated code fixes, Simulate, and Prove — where the agents are Claude Code sessions, the repo is the database, and git is the audit trail."*

**Problem:** ML iteration on Homefeed was manual and slow. Goal: shift humans from hand-tuning models to **supervising a system** that finds and ships improvements — with the reliability to touch production.

**Your role:** expert-in-loop co-developer (with Andrew); designed the Feedback Curator + Skeptic; own the CG/Build side.

**Architecture & key decisions:**
- **Agents = prompts; repo = database; git = audit trail.** No custom framework — the substrate already does orchestration, persistence, and audit, so don't rebuild it.
- **Roles with verification:** PM (generate hypotheses) → DS (enrich/size/score) → **Skeptic** (adversarial gate: PASS/FAIL/NEEDS_HUMAN) → **Feedback Curator** (turn human corrections into permanent structured patterns).
- **RLHF-style loop:** every human comment becomes a permanent analytical-check/dead-end → monotonic quality floor.
- **Blast-radius control:** Build agents write only to an **allowlist** with **diff caps** — explicit, signed-off.
- **Eval against ground truth:** BuildValidator grades generated edits against **real merged PRs.**

**Hardest problem — reliability enough to modify production:** autonomy multiplies error (90%/step compounds). The design answers: an **independent adversarial verifier** (Skeptic, which self-calibrates off its own verdict log), **bounded blast radius**, and **eval-against-reality**. And a deliberate choice to store the learned signal as **human-legible structured rules** rather than an opaque scalar reward — operators must trust and edit the policy.

**Results:** 67+ Detect cycles, 36 analytical checks, operational Build agent generating validated CG/blender code; ahead-of-curve multi-agent patterns frontier labs are still formalizing.

**Depth-probes:**
- *"How do you make agents reliable?"* → tool design, adversarial verification, short loops, blast-radius caps, trajectory eval.
- *"Workflow or agent?"* → workflow-end on purpose (predefined phases, human-dispatched) — that's *why* it's reliable enough for prod.
- *"Let an agent touch prod safely?"* → allowlist + diff caps + human gate (BuildValidator).
- *"How do you eval it?"* → against real merged PRs (ground truth), not a proxy.

**Lead with Reflex for:** agents/multi-agent (08), RLHF/human-feedback loops (05), the agentic-system design (Drill 6). **Your ahead-of-curve story — own it.**

---

## Quick map: probe → story

| If they probe… | Lead with |
|---|---|
| representation / embeddings / contrastive | **UPP** (FM + CLR) or **RR** (OmniSage/UIC) |
| pretrain-finetune / transfer / scaling | **UPP** |
| retrieval / ranking / two-tower / cascade | **Preranking** (+ UPP CLR) |
| eval / offline-online / why metrics mislead | **Preranking** (your moat) |
| RLHF / reward design / bandits / explore-exploit | **RR** (Geometric Bandit) or **Reflex** (correction loop) |
| agents / multi-agent / tool use / guardrails | **Reflex** |

Keep each to a 60-90s arc, then go deep on the probe. The genesis/leadership versions live in `story_grill_plan.md` — pull those for "tell me about a time you *led*" questions.
