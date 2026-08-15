# The eight papers, what each gives Reflex, and Monday's talking point

**James Li · 2026-08-15 · read-in**

---

## If you read one thing

**Every technique in this literature optimizes against a reward that cannot lie.** Task success, legal-move validity, offline loss, revenue. Three research labs and two production systems, all the same precondition.

Reflex cannot run any of these playbooks yet — not because it's immature in general, but because of one specific missing thing: **a critic you can trust.** That's the eval-integrity layer. It isn't the chore that precedes the interesting work; it's what makes the interesting work available at all.

The two production papers (Google/YouTube, Alibaba) are the ones to cite in a room. The rest are evidence for you.

---

# Part 1 — The papers

## 1. GEPA: Reflective Prompt Evolution Can Outperform RL

*arXiv 2507.19457v2 · UC Berkeley / Stanford / Databricks / MIT · ICLR 2026 Oral*

**What it is.** A prompt optimizer that reads execution traces in natural language, reflects on them, and proposes targeted edits — instead of collapsing rollouts into a scalar and estimating a policy gradient.

**Numbers.** Beat GRPO by 6% on average, up to 20%, using **up to 35× fewer rollouts**. On IFBench: 38.61% after **678 rollouts** vs GRPO's 35.88% after **24,000**.

**Main points.**
- The thesis is not "text beats scalars." It's that **a scalar reward destroys attribution information that was already sitting in the rollout.** GRPO needs 24k samples to statistically reconstruct what was in plain text in every single one.
- **GEPA's acceptance test is a plain scalar** — average minibatch score before vs. after, accept if improved (Alg. 1, L13–14). Its Pareto machinery is over *task instances* and only decides which parent to mutate next (Alg. 2).
- **GEPA has no `blame()`.** Module selection is round-robin (Alg. 1, L8; DSPy defaults to `component_selector="round_robin"`). Credit assignment is implicit — the reflection LM reads the trace — or supplied by the feedback function.
- The feedback function can carry **human-written rationales** as `feedback_text`.

**Apply to Reflex.**
- **GEPA cannot be cited in support of a Pareto acceptance gate.** Split the two roles: single aggregate + statistical margin for acceptance; instance-Pareto over fixture cases for parent selection.
- `blame()` is a *departure* from the configuration GEPA's results were measured on, so it carries the burden of proof — and the ablation is one config value, not a build.
- Your binary-plus-mandatory-rationale position is stronger than you argued it: the rationale field is the `feedback_text` a GEPA loop consumes. Collected and never plumbed in, it's a wasted human hour per card.

---

## 2. Effective Harnesses for Long-Running Agents

*Anthropic Engineering*

**What it is.** An engineering blog on getting agents to make progress across many context windows: an initializer agent that sets up the environment, then a coding agent that works one feature at a time and leaves clean artifacts.

**Honest grade: thin.** No numbers, no baseline, n=1 application. Cite the failure taxonomy, never a performance claim.

**Main points worth keeping.**
- **Format as guard.** They tried strongly-worded prose instructions against editing a test manifest; it wasn't enough. What worked was changing the file format — the model is measurably less likely to modify JSON than Markdown.
- **Get-your-bearings routine** — smoke-test the environment *before* starting new work, so a broken state is caught rather than compounded.

**Apply to Reflex.**
- `never_mutable` protects files, not prose spans inside mutable files. Rather than build "protected sentences," **move verification rules out of prose into a structured block** where one field is mutable. A mutation that can't find a sentence to soften can't soften it.
- **Pre-flight the incumbent** on a small fixture slice before mutating. If the incumbent's own score moved, the bank or judge drifted and every fitness number that generation produces is unattributable.

---

## 3. SkillOS: Learning Skill Curation for Self-Evolving Agents

*Google Cloud AI Research / UIUC / MIT*

**What it is.** A frozen executor plus a separately **trained** skill curator that issues `insert` / `update` / `delete` against an external skill repo. All learning lives in the curator.

**Numbers.** ALFWorld success 47.9 → 61.2 with the trained curator; Gemini-2.5-Pro 66.4 → 80.2. Ablations: full 61.2 · without content-quality reward 58.6 · without compression reward 60.0 · **without grouped task streams 57.3**.

**Main points.**
- **Untrained curators append; trained curators consolidate.** Early in training `insert` dominates; as it improves, `update` rises and `insert` declines.
- Utilization: coverage of the repo rose 53.6% → 72.9%, and the trained curator used **fewer** skills per example (2.24 → 1.95) while scoring better. Precision, not volume.
- An explicit **compression reward** exists to stop verbatim trajectory copying and force distillation.
- **Using Gemini-2.5-Pro directly as the curator underperformed a trained 8B curator.** Stronger reasoning ≠ better curation.

**Apply to Reflex.**
- Four attribution metrics lift directly onto the Feedback Curator, which is currently unmeasured. **Coverage first** — what fraction of `quality_patterns.md` is ever retrieved.
- Growth curve: the design doc records **341 lines at cycle 13**; the archive is at 66. Free measurement, no labels.
- Your human gate is right, but the approval cost of insert / update / retire is wildly unequal and cheapest for the immature operation — so the realized mix skews to accretion regardless of how good the Curator gets. Log proposed vs. merged separately.
- Compression applies to the `Correction:` field, never to `Evidence:`.

---

## 4. AutoHarness: Synthesizing a Code Harness

*Google DeepMind*

**What it is.** The LLM writes its own harness as code — `propose_action()` and `is_legal_action()` — found by tree search with Thompson sampling, with the environment as critic.

**Numbers.** **78% of Gemini-2.5-Flash's chess losses were illegal moves, not strategy.** After synthesis: **100% legal-action success across all 145 games**, converging in an average of 14.5 iterations. Flash+harness beat Gemini-2.5-Pro **56.3% vs 38.2%** win rate. In the code-as-policy limit, it beat GPT-5.2-High **0.870 vs 0.844 at ~$0 inference cost against ~$640**.

**Main points.**
- **The harness didn't make chess verifiable — chess already was.** It took the verifiable part away from the LLM at 100% accuracy so the model only faced what needed judgment. It shrank the hard problem rather than solving it.
- **Credit assignment from the error signature:** if `is_legal_action()` returned True but the action was invalid, refine both functions; if False, refine only `propose_action()`. Deterministic, immune to rationale bias.
- They removed "Available Moves" hints on purpose, so the harness couldn't copy the answer.

**Apply to Reflex.**
- **Hallucinated references are Reflex's illegal moves** — a card citing a table or metric that doesn't exist is a catalog lookup with zero judgment.
- Partition failures by verifiability. Mechanize what can be mechanized, and never spend a judge call, a human review, or optimizer budget on it again.
- Failure *type* → component is a lookup table for the mechanized share, replacing the `blame()` heuristic there.
- **This and AI2/UW don't conflict.** AutoHarness builds a separate harness per game and lists cross-game reuse as future work; AI2/UW found harnesses don't transfer. Both say evolution works *within* a task — which is the regime Evolve is in.

---

## 5. EvoHarness-RL: Self-Evolving Runtime Harness

*Meta AI / UIUC*

**What it is.** Externalize three harness states — **Belief** (facts inferred from interaction), **Progress** (`(subgoal, status)` records), **Experience** (cross-episode skills and failure modes) — then train a coordination policy with cost-aware GRPO.

**Numbers (unseen split — the honest accounting).**

| Configuration | Success | Δ |
|---|---|---|
| Base ReAct | 50.0% | — |
| **+ BPE harness, prompt-time, zero training** | **77.6%** | **+27.6** |
| + supervised fine-tuning | 69.4% | *worse than prompt-time* |
| + cost-aware GRPO | 86.6% | +36.6 |

Same harness lifted GPT-4.1 **+22.1**, GPT-5 **+25.7**, Claude Opus 4.5 to **98.5%**.

**Main points.**
- **The untrained structure captured 27.6 of 36.6 points.** RL bought nine more and cost an entire training pipeline.
- **SFT made generalization worse than doing nothing** — imitating good harness use isn't learning when use is worthwhile.
- **Harness annealing:** after RL, external-state calls drop to about one per episode. Maturity looks like *less* interaction with scaffolding.
- Reward design: success is a strict gatekeeper, and **the efficiency bonus is only granted on success** — cheapness never pays on a failed trajectory.

**Apply to Reflex.**
- **RL is a sequencing question, not a cost question.** RL buys a coordination policy over externalized state, and you can't learn a policy over state you haven't externalized. Ladder: trustworthy signal → externalized state → prompt/harness optimization → weight optimization.
- BPE mapped: **Experience = `quality_patterns.md`** (exists), **Belief** maybe `context.md` (*check the code*), **Progress — apparently nothing.* Removing Progress "disproportionately degrades long-horizon tasks with dependent subgoals," which is exactly what a Detect investigation is.
- With SkillOS, two independent papers say the same thing: **a growing patterns file and rising retrieval-per-card is the signature of an immature system, not a learning one.**

---

## 6. Self-Evolving Recommendation System *(the YouTube paper)*

*Google · Wang, Wu, Chang, Wei, Heldt*

**What it is.** Two agents optimizing YouTube's watch-page ranking model end to end. The **Offline Agent (Fast Loop)** is a high-frequency nomination engine generating hypotheses against cheap proxy metrics. The **Online Agent (Slow Loop)** runs daily, ranks candidates, promotes them to live experiments, and validates against delayed north-star business metrics — including deciding when to kill an experiment.

**Numbers.** Against all launches on the surface over six months, the agentic system's improvements **outperformed 64% of human launches on the YouTube-level metric and 73% on the surface-level metric.** Several successful production launches.

**What it actually discovered.** Adagrad → RMSprop with specific hyperparameters. An architecture refinement moving from standard sigmoid gates. And **a novel reward function incorporating a new signal that significantly outperformed the human-engineered baseline** — i.e. the agent redefined the business logic of success, not just the config.

**Main points.**
- The two-loop split is the whole design: **cheap fast proxy, expensive slow truth.** Neither works alone — optimize the proxy only and you Goodhart it; wait for the north star only and you get one experiment a month.
- Safety guardrails are stated *in the agent's task prompt* as explicit constraints, e.g. "Keep Metric#3 ≤ +1%."
- Humans are reduced to two touch points: defining the task for the Offline Agent, and reviewing experiment metrics at the end. The engineer's job moves to **strategic guardrails and constraints.**
- Proposed changes are "typical of the size of a human-engineered change" — not toy edits.

**Apply to Reflex.**
- **This is Reflex's structure, already running in production at scale.** The judge is the fast proxy; retention and shipped-outcome metrics are the slow north star. The paper is the existence proof that the pattern works — and it validates the two-loop instinct you already wrote down on the Safe Journeys side: *the mechanism metric tells you it worked; the business metric tells you it was worth doing.*
- **They have what Reflex is missing**: an Experiment Journal, an automated path to live experiments, and delayed north-star metrics wired back into candidate ranking. Reflex's version of the Slow Loop doesn't exist yet — which is another argument for the attempts store and the hindsight set.
- Guardrails-as-explicit-constraints is a cleaner pattern than Reflex's implicit ones and maps directly onto veto criteria.

---

## 7. EvoRec: Self-Evolving Agentic Recommender Systems

*Alibaba International Digital Commerce*

**What it is.** Four agents on a dual-track loop. A Research Agent and Code Agent iterate the model each round; a **Skill Evolver** periodically distills reusable methodology from a persistent Memory of past experiments.

**Numbers.** Up to **5.54%** relative offline improvement over the strongest baseline. Online A/B on the advertising platform: **+1.85% revenue, +1.02% CTR**, both statistically significant.

**Main points.**
- Their critique of prior work is the sharp bit: existing approaches "use the agent only as a code translator that **accumulates no methodology**." The Skill Evolver exists to fix exactly that.
- Model *and* methodology co-evolve — two tracks, not one.

**Apply to Reflex.**
- **The Skill Evolver is the Feedback Curator, with a revenue number attached.** That is the single most useful citation available for arguing the Curator deserves investment: a production system where distilling methodology from past experiments produced a measurable revenue lift.
- Reinforces SkillOS: the curation layer is a first-class component, not plumbing.

---

## 8. Rethinking the Evaluation of Harness Evolution *(the counterweight)*

*AI2 / UW · in `sources/`*

**Numbers.** On Terminal-Bench 2.1, harness evolution did **not** consistently beat matched-budget parallel sampling or sequential refinement. Gains showed in pass@5 but **not pass@1** — from more attempts, not a better artifact. Evolved harnesses transferred almost nothing to held-out tasks (**+0.6 pass@1**).

**Apply to Reflex.**
- Evolve's §5 success criteria need a **matched-budget baseline arm**: run the incumbent with K-sample selection at the same invocation budget before crediting the loop.
- Their diagnosis — meta-agent edits "memorize fixes rather than distilling strategies" — is precisely what SkillOS's compression reward exists to prevent. **So the negative result may be about self-evolution run without a compression objective**, which is a much narrower claim.
- And it's about *transfer*. Evolve evolves per-playbook specs, which is the within-task regime where AutoHarness and the two production papers all succeeded.

---

# Part 2 — Monday's big meeting

## The talking point, as written

> There's a result from DeepMind I keep coming back to. In a public chess competition, **78% of Gemini-Flash's losses weren't bad strategy — they were illegal moves.** The model understood chess and couldn't reliably follow the rules.
>
> Their fix wasn't a bigger model. They had the model write a harness that checked move legality in code, and once the mechanically-checkable part was handled deterministically, **the smaller model beat the larger one.** The harness didn't make the problem easy. It made the problem *smaller* — the LLM only ever saw the part that actually needed judgment.
>
> So here's my question for us. When we reject a Detect card, what fraction fails for a reason a program could have caught — a table that doesn't exist, something we already tried, a claim with no evidence behind it — versus a reason that genuinely needs a human's judgment about whether it's worth doing?
>
> **Nobody has measured this.** It's an afternoon of labeling on cards we already have. And it tells us something we'd otherwise guess at for months: whether the leverage here is in better judgment, or in better plumbing.
>
> The reason I care is that everything I've read in this space — DeepMind, Meta, Google's own recsys agents, Alibaba's — runs on a signal that can't lie. Task solved, move legal, revenue moved. **Our signal is an LLM judge whose reliability we haven't measured yet.** That's the thing standing between us and any of these techniques, and it's cheaper to fix than it sounds.

## If someone asks "is this actually working elsewhere?"

Go to the production papers, not the methods papers:

- **Google, on YouTube's watch page.** Two agents — a fast offline loop nominating hypotheses against proxy metrics, a slow online loop validating against north-star business metrics in live traffic. Measured against six months of launches on that surface, the agent-generated improvements **beat 64% of human launches on the YouTube-level metric and 73% on the surface-level metric.** It discovered a new optimizer configuration, an architecture change, and a novel reward function that beat the human-engineered one.
- **Alibaba's EvoRec.** Agents that co-evolve the model and the methodology, with a component that distills reusable lessons from past experiments. **+1.85% advertising revenue and +1.02% CTR in an online A/B**, both significant.

Then the line that connects it back: *both of those systems have a fast proxy loop and a slow truth loop. We have the fast loop. We don't have the slow one yet — and the fast one isn't calibrated.*

## What to keep out of that room

The Pareto conflation, the `blame()` ablation, κ-versus-percentage-agreement, the EvalResult schema. Those are critiques of specific people's documents, and a large room is the wrong place for them. They go to the three-way with Chao and Janvi.

Also don't present eight papers. One idea, one number, one ask.

## The three-way with Chao and Janvi

Run it in this order:

1. **Roadmap, priority, owner** — list it out together first. Everything after this lands differently once ownership is settled.
2. **The seam.** Chao's Stage 2 and Janvi's Evolve Detect adapter are the same work under two names. Open since 8/11 and the most expensive thing on the list if it stays unnamed.
3. **The asks**, which are coupled and belong in a room with both of them:
   - Chao: the **5×5 judge-dimension correlation matrix** from existing V1 output. No new labels, no new runs.
   - Chao: report **Cohen's κ, not percentage agreement**, for human-human and judge-human on the same double-graded cards. One evaluator in the literature scored 80% agreement with a κ of 0.62.
   - Janvi: **separate acceptance from parent selection.** This depends on Chao's matrix, which is why it belongs here rather than in a 1:1.
   - Mine to build: the **paired-bootstrap dominance gate** and EvalResult v2.
4. **The attempts store** — LR docs plus Helium, joined to hypotheses. Frame it as Phase 3 done properly, and name up front that it's the same join as the hindsight case bank so it doesn't get built twice.

---

**Fuller detail:** `eval_00_hub.md` (state and open items) · `eval_02` (Chao) · `eval_03` (Janvi) · `eval_04` (Curator) · `eval_05` (the verifiability partition and attempts store) · `eval_01` (glossary)
