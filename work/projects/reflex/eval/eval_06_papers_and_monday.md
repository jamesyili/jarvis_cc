# The twelve papers, what each gives Reflex, and the 8/17 talking point

**James Li · 2026-08-15 · read-in · extended 2026-08-28 with papers 9–12 (Part 1b — the memory and curation set)**

> **This is the running list.** New Reflex-relevant papers get a numbered entry here in the same format (what it is / numbers / honest grade / main points / apply to Reflex / don't cite for), full text goes into `kb/hard/raw/`, and the hub's §8–§9 get a pointer. Part 2 is the 8/17 meeting prep and is left as written.

---

## If you read one thing

**Every technique in this literature optimizes against a reward that cannot lie.** Task success, legal-move validity, offline loss, revenue. Three research labs and two production systems, all the same precondition.

Reflex cannot run any of these playbooks yet — not because it's immature in general, but because of one specific missing thing: **a critic you can trust.** That's the eval-integrity layer. It isn't the chore that precedes the interesting work; it's what makes the interesting work available at all.

The two production papers (Google/YouTube, Alibaba) are the ones to cite in a room. The rest are evidence for you.

**8/28 addendum, for papers 9–12 (the memory set):** Reflex has built the memory layer's *write side* — capture with provenance, conflict reports, never-silent retirement — better than any of the twelve papers. The numbers in the new set are all on the *read side*: whether the investigation carries its own verified state (Recuris: +23.9 for working state, +2.0 for skills), whether knowledge enters context keyed or wholesale (the same skills, model-decided: worse than no skills), and where tool results live (Scroll: −21 under compaction, −2.6 bound to variables). The Curator's product is fine; the Skeptic consumes it in the regime measured as worst, and the DS Agent carries no state at all. Synthesis in `eval_08`.

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

# Part 1b — The memory and curation papers *(added 2026-08-28)*

Four sources that arrived after the 8/15 read-in, all on the same question the first eight mostly skipped: **how an agent's experience becomes durable, curated knowledge, and what that store should look like.** They land on the Curator/Skeptic surface (`feedback_curator_skeptic_deepdive_0828.md`) and on the World Store (`eval_07`). The synthesis — what the twelve papers together say about Reflex's memory layer — is in `eval_08_memory_literature_vs_curator_skeptic.md`; the entries below are the per-paper evidence.

## 9. Recuris: Recursive Experiential–Working Memory Evolution

*arXiv 2608.24876v1 (25 Aug 2026) · NUS / Stanford / Oxford / Princeton · Yu, Wu, Yin, Chen, Zhao, Wang, Yan, Yang · code: github.com/Gen-Verse/Recuris*

**What it is.** A memory-control layer around a frozen LLM with four evolvable components: Experiential Memory **E** (skills, Anthropic agent-skill format), a Working Memory spec **W** (per-goal `content / status / evidence / blocker`), an invocation policy **ρ** (trigger predicate + retrieval key — *when* a skill enters context and *which*), and a checker set **C** (completion predicates that read the tool receipt, never the model's claim). Within a task, W decides which skill ρ retrieves; C commits a goal to `done` only on environment evidence. Across tasks, a fixed Meta-Agent (Claude Code) reads the structured trace, attributes each failure to one of {E, W, ρ, C}, patches only that component, and a fixed gate admits the patch only if it repairs the source task without regressing a dev split that includes anchor tasks the memory already solves.

**Numbers.** Main table (avg@4, paired task-clustered bootstrap; † = CI excludes zero): 35 of 37 model–benchmark pairs improve. τ²-Retail: Doubao-2.0-Pro (the deployment model) 58.1 → 81.4 (+23.3†); GPT-5.6 Sol +17.8†; Claude Opus 5 72.4 → 87.9 (+15.6†); Gemini 3.7 Flash +4.8 (includes zero). SkillFlow: Qwen3.6-27B +16.6†, Qwen3.6-35B +13.5†. τ²-Airline (50 tasks): every interval includes zero. Terminal-Bench 2.1: +2.3 to +3.8, none excluding zero.

Ablation, τ²-Retail (Table 2, 114 tasks × 4 = 456 episodes; base 58.1%):

| Variant | Success | Δ vs base [95% CI] |
|---|---|---|
| EM only (skills, no working state) | 60.1 | +2.0 [−4.0, +7.9] |
| WM only (verified state, no skills) | 82.0 | **+23.9†** [+17.5, +30.3] |
| Model-controlled invocation (same 10 skills, all in context every turn) | 65.6 | +7.5† [+1.5, +13.4] |
| EM + WM (Recuris) | 83.6 | **+25.4†** [+18.4, +32.5] |

Failure localization (Table 4, injected faults, macro recall over E/W/ρ; 33.3% floor): outcome only **13.0%**, raw trajectory 37.0%, structured trace **64.8%**. Invocation (ρ) faults: 0.0% from either non-trace condition, 38.9% from the trace. Macro precision 27.6% → 64.4%.

Cross-task evolution (Table 5, 16 evolve / 12 dev / 86 held-out): nine packages from three runs clear M0 by +9.01 to +17.44, all †; a second round compounds (+6.98†); round 4 gives it back. Harness with empty memory M0 vs bare agent: nothing measurable on four models (Table 10) — the gain is entirely the evolution term. Memory growth over eight accepted patches: **51 skills added, 2 revised, 0 deprecated, 17 near-duplicate pairs survive**; ablating skills moves held-out by −2.3 to +1.7, CIs including zero. Test-time adaptation on Terminal-Bench (Table 8): retry budget alone +26.4 (p<10⁻⁴); learning at matched budget **+2.3 (p=0.774)**. A/A re-run of a byte-identical package: +0.00 [−6.98, +7.27].

**Honest grade.** Strong on the cross-task claim — pre-registered three-way splits, paired task-clustered bootstrap, an A/A run as the instrument's resolution, matched budgets, gains that move with required-write recall (r = 0.97: better artifact, not more attempts), and they run the AI2/UW decomposition on themselves for Terminal-Bench and report the null. Weak spots: one deployment model does all the evolving from 16 tasks, τ²-Airline resolves nothing, SkillFlow is in-sample template selection (only cross-model transfer is out of sample), and the gate's own dev reading is ±30 points wide.

**Main points.**
- **Skills alone are worth nothing; state is worth +23.9.** Read-action recall is 88–98% at every horizon for every variant — length never breaks retrieval. It breaks *execution*: the base agent ends 42% of write-requiring episodes having issued no write, Recuris 16%. The median turn of the first correct write is identical across variants; what changes is whether the write happens at all.
- **Invocation control beats content; the whole-library-in-context regime is worse than no skills.** Byte-identical skills, model decides when: 65.6%, 147k tokens/success. State-grounded: 83.6%, 101k. WM with *no skills*: 82.0%. What the model-controlled regime lacks is a signal for *when* a skill applies.
- **The trace is what makes scoped repair possible.** Attribution from outcome alone sits below the constant-answer floor; ρ faults are non-events in a transcript and only become visible once mechanism events are logged. Two Meta-Agents sharing no code (Claude Code vs DeepSeek Harness) distill the same 16 failures into the same component family (−1.45 paired, p=0.72): **what the loop learns is set by the evidence pool, not the machinery reading it.** The Meta-Agent may attribute a cluster to "the harness itself" and propose no patch.
- **The memory only grows, and could afford to — because invocation is gated.** 51/2/0 add/revise/deprecate, 17 near-dups admitted, no single skill carries the gain; "redundant rather than fragile", with pruning named as a natural addition. Accretion didn't cost them because bloat never reached the context.
- **The gate discards noise, not gains.** 12-task dev at k=4 → intervals >30 points wide; all 18 rejected candidates had dev CIs containing zero; one later cleared the 86-task held-out by +11.92†. An ungated run admitted patches the gate had condemned and all landed +14.5 to +18.0† held-out. Gated patches broke 4 of 42 anchor tasks (9.5%) vs 25.9% for re-running an identical package — anchor "regressions" are decode noise.
- **Which mechanism matters is a property of the domain** (status board carries Retail −17.3†, write review carries Airline −13.5†, each inert in the other). The one after-the-fact mechanism — a truth guard auditing completion claims — never matters despite rejecting 172 claims: a write that executed has already moved the world.

**Apply to Reflex.**
- **The Skeptic runs in the regime this paper measures as worse than nothing.** Every awaiting-skeptic card gets `registry.yaml` + `dead_ends.yaml` + `quality_patterns.md` + audit logs read wholesale, and the model decides what applies — the model-controlled row (65.6 vs 83.6, +46% cost). The registry already carries proto-trigger predicates (`mandatory_when`, `applies_to`) and Check 3's card-type classification is a retrieval key. Change: key Check 6 retrieval on `(card type, layer targeted, tables named, surfaces)` and log what was retrieved. Testable on `verdict_log.jsonl`: Skeptic precision (`human_agreed` on FAILs) under full read vs keyed read. This does **not** license trimming the Curator's Phase 0 read-everything — that is the Meta-Agent's cross-task read, a different loop, and the paper's Meta-Agent also reads every failed trace.
- **Open item 14 (does Detect keep a Progress ledger?) moves from code question to the largest number in the paper.** Recuris W ≈ EvoHarness *Progress* with *Belief* folded in as the `evidence` field; E ≈ *Experience* = `quality_patterns.md` + `analytical_checks/` + `dead_ends.yaml`. WM-only +23.9; EM-only +2.0. Reflex has spent its investment on E. The analogue of "omitted writes" is a card that *claims* a check (VLM, chart, query) it never ran — what Check 3 catches after the fact. Earlier and cheaper: a per-investigation `(goal, status, evidence, blocker)` ledger the DS Agent maintains, where `done` requires a receipt (query result, VLM output), not the DS Agent's sentence; Check 3 becomes the C that reads the receipt. First measurement: the fraction of `fail_reasons` in `verdict_log.jsonl` that are claimed-but-not-executed evidence.
- **`verdict_log.jsonl` localizes to the card, never to the component.** When a human overrides a FAIL or rejects a PASS, nothing says *which* of {pattern absent (E), present but not cited (ρ), cited and misapplied (Skeptic judgment), card's evidence state wrong (W)} failed. `patterns_cited` already exists in `SkepticCheck`; add the set that *applied* (from the keyed retrieval above) and the backfill can derive `component_blamed` mechanically: absent → Curator insert; present-not-cited → retrieval; cited-and-wrong → pattern content or check prompt. That turns the Curator's insert/update/retire choice into an evidence-driven decision and gives `eval_04` its missing attribution metric. Outcome-only attribution is 13% here; a human reading Asana comments won't do better.
- **The "growing patterns file = immature system" position (eval_04) survives, and Recuris says why it holds for Reflex and not for them.** Their 51-add/0-deprecate store cost nothing because ρ kept it out of context; Reflex's wholesale read means every accreted line reaches the Skeptic. Their loop's add-bias also mirrors the Curator's: all seven repaired clusters in the Appendix E round landed on E as "add skill", the accretion skew `eval_04` predicts from unequal approval cost. Pruning was safe for them (−2.3 to +1.7); Strengthen/Narrow are the Reflex analogue and are under-used relative to insert.
- **For the paired-bootstrap gate (`eval_03` §2) and Evolve's fixture:** a 12-case dev slice at K=4 could not resolve a +11.92 effect, and Evolve's 450-invocation budget buys roughly that. Run the A/A first (identical incumbent, twice — ±7 points on 86 tasks; paper 2's "pre-flight the incumbent" with a number attached), and reserve a pre-registered held-out fixture of ~80+ cases with anchor cases the incumbent already passes as the regression term. A correctly-sized gate rejects most candidates in-round; that is the design working.
- **Curator model choice is second-order; the evidence pool is first-order.** Two Meta-Agent implementations converged within instrument noise. The Curator's `no_durable_learning` close has a direct analogue (attribution to "the harness itself", no patch) — keep it. Cross-model transfer (+15.6 on Opus 5 from a memory evolved on a mid-size model) supports `dead_ends.yaml` and the registry surviving model upgrades — where the receiving model still makes the failures the memory repairs (Opus 5 on Airline: +1.0 at an 89.5 baseline).

**Don't cite for.** Learning between retries within one task (+2.3 at matched budget, p=0.774 — the headline +26.4 is the attempt budget), τ²-Airline effects, or SkillFlow gains as held-out generalization (in-sample template selection; only cross-model transfer is out of sample).

---

## 10. WikiSkill: Compiling Agent Experience into Persistent Knowledge

*arXiv 2608.27454v1 (27 Aug 2026) · Google Research / Virginia Tech · Tang, Rashtchian, Ferng, Tomkins, Juan, Vu · code: github.com/… not listed; inspired by Karpathy's "LLM Wiki" gist*

**What it is.** A skill-evolution loop with a third layer inserted between raw traces and the evolving skill: a persistent wiki (`wiki/patterns/*.md`, `index.md`, `logs.md`, `skill-impact.md`) that a Wiki Maintainer patch-edits every iteration and that is **never rolled back**, while the skill itself is gated on validation and reverted on failure. A ReAct Skill Proposer reads the wiki, the rejection ledger, and ≥4 raw traces before making one atomic create/patch/no-action proposal per iteration. The inference agent reads skills only — it is deliberately walled off from the wiki.

**Numbers.** Test accuracy, average of three full evolution runs, paired bootstrap p<0.05. Five-benchmark average (LiveMath, SealQA, SpreadsheetBench, OfficeQA, ALFWorld):

| Model | No skill | Best prior (method) | WikiSkill | Δ vs best prior |
|---|---|---|---|---|
| Qwen-3.5-4B | 26.2 | 35.2 (SkillOpt) | **38.5** | +3.3 |
| Qwen-3.5-9B | 29.9 | 42.3 (EvoSkill) | **47.4** | +5.1 |
| Qwen-3.6-27B | 39.4 | 53.3 (EvoSkill) | **63.3** | +10.0 |
| Gemma-4-31B | 41.3 | 49.1 (SkillOpt) | **54.9** | +5.8 |
| Gemini-3.5-Flash | 49.5 | 56.1 (EvoSkill) | **68.1** | +12.0 |

Ablation (Table 3, Gemini-3.5-Flash, four benchmarks — ALFWorld excluded because Flash hit 100% on val before evolution):

| Inference agent reads wiki | Proposer reads wiki (+ Maintainer exists) | Avg |
|---|---|---|
| no | no | 48.7 |
| yes | no | 45.3 |
| yes | yes | 60.9 |
| **no** | **yes** (default) | **63.7** |

Gains scale with model size within Qwen: +12.3 / +17.5 / +23.9 for 4B / 9B / 27B. Qwen-9B with skills (47.4) beats Qwen-27B without (39.4). Transfer: Qwen-9B on ALFWorld scores 70.2 with a 27B-evolved skill vs 63.4 self-evolved; but 4B-evolved SpreadSheet skills drop Gemini-Flash from 50.5 to 18.1. Not universal: Qwen-4B on OfficeQA falls 30.2 → 28.5.

**Honest grade.** Solid *within its paradigm* — 5 models × 5 benchmarks × 3 runs, bootstrap-tested, prompt-time only (no training) — but validation splits are 10–40 tasks (gating on noise, acknowledged), the wiki itself is never scored (only its downstream effect), the ablation is one model, there is **no matched-budget parallel-sampling arm** (the AI2/UW test is not run), and despite being a Google paper it **does not compare against, or even discuss, SkillOS** — it appears once in a citation list. Baselines are Trace2Skill, EvoSkill, SkillOpt only; GEPA is excluded by citing prior work that skill-evolution beats generic prompt optimizers.

**Main points.**
- **"Compiling" is concrete and small.** One Maintainer LLM call per iteration over ≤8 stratified traces (≤5 failing, ≤3 passing, each capped at 15k chars). Output is JSON: `create_patterns`, `update_patterns` with patch ops (`append` / `replace` / `insert_after` against an exact substring), a **mandatory full rewrite of `index.md`**, and a mandatory `append_log`. Pattern pages are 10–30 lines: description, root cause, exact command sequences, concrete fix. "Do NOT create duplicate patterns — update existing ones" is a prompt rule, not a trained objective.
- **The rejection ledger is written by the harness, not the model.** `skill-impact.md` gets a programmatic append after every validation run: proposal metadata, target skill, **unified diff**, validation score, Accepted/Rejected. The Proposer is told "DO NOT repeat rejected approaches"; the case study shows a rejected abstract skill (val 0.72) informing an accepted concrete one (0.78) one iteration later. This ledger is the paper's mechanism for not re-proposing failures — an objective audit trail rather than model memory.
- **Provenance runs both ways.** Each skill ships with `PURPOSE.md` mapping it back to the wiki patterns that motivated it; each pattern page carries per-iteration evidence pointers (`Iter 0: train 00, 02 …`). `index.md` entries must state PROBLEM + ROOT CAUSE + FIX in one or two sentences, and the prompt calls the index "the MOST IMPORTANT part of the wiki" because it decides whether a page gets read.
- **Walling the executor off from the wiki helps.** Giving the inference agent wiki access during rollouts cut the average 63.7 → 60.9 (LiveMath 72.6 → 64.8). Their hypothesis: the agent solves tasks from the wiki instead of the skill, so traces stop revealing what the skill is missing. Stated as a hypothesis, one model.
- **Update-dominant without training.** Table 4: 6.3–8.9 patterns created vs 7.0–18.4 edits per run across models — edits exceed creates for every model, under an untrained maintainer with a "read the whole wiki first, don't duplicate" prompt. Pages average 18–48 lines. But "all wiki pattern creations and edits are retained": there is **no pruning, no deprecation, no conflict resolution, no versioning** — `replace` silently overwrites, and the paper lists the missing pruning mechanism as a limitation.
- **Discovery and execution are different capabilities.** Skills evolved by one model transfer across families and sometimes beat self-evolved ones; small-model skills that encode low-level workarounds (one-line Python, string-conversion rules) become negative transfer on a stronger model. Late-stage refinement is real: 10–28% of accepted updates land in iterations 5–7.

**Apply to Reflex.**
- **The Curator already runs the Maintainer's discipline — and is ahead of it.** Phase 0 "read everything first" is the paper's full-wiki-context input; Strengthen / Contradict / Narrow / Orthogonal is a richer relation set than `append` / `replace` / `insert_after`; the Conflict Report (Merge / Version / Replace, routed to the original reviewer) and the never-silently-retire rule have **no counterpart in WikiSkill**, whose `replace` op silently overwrites and whose wiki is never pruned. Cite this paper as the existence proof that a persistent, patch-edited pattern layer pays (48.7 → 63.7 with the Proposer reading it), not for anything about how to reconcile contradictions.
- **What Reflex is missing is `skill-impact.md`, and it belongs in Evolve, not the Curator.** A harness-written ledger of every playbook edit proposed — target, diff, fitness under a pinned judge version and `fixture_snapshot_id`, accepted/rejected — that the next proposer *must* read. `quality/proposed/` and the audit logs cover Curator proposals; nothing covers Evolve's. This is the same object as EvalResult v2's provenance fields (`eval_03`) written out as a file the loop reads back, and it is the cheapest anti-repeat mechanism in the literature: no training, one programmatic append.
- **Check whether the DS Agent reads the pattern files directly at generation time.** In the deep-dive the Skeptic reads `dead_ends.yaml`, `registry.yaml`, and the audit logs (Check 6) — that is fine; the Skeptic is the gate, not the executor. But if the **DS Agent** also reads them while authoring, Reflex is in the ablation's worse configuration: cards get their competence from the wiki, and the Evolve loop's traces stop showing what the *playbook* lacks. The fix is not to cut the DS Agent off — Detect needs the table-name landmines — but to log which patterns the DS Agent consulted per card, so Evolve can distinguish "playbook knew this" from "wiki rescued it." This is a code question, like the Belief/Progress check (hub open item 14).
- **Add the PURPOSE.md back-pointer to routed rules.** Dead ends and analytical checks carry `discovered` / `confirmed_by` / `discovered_cycle`. The Curator's `playbook_rule` and `agent_prompt_rule` routes should carry `motivated_by: [learning_record ids]`, so when a contradiction later retires the learning record, every rule it spawned is findable. Same for the one-line index: give each dead end and check a `summary` that states problem + root cause + fix, since that line is what the Skeptic (and any future retrieval) keys on; `de_topline_guess_without_constituent_numbers`'s label carries only the problem.
- **Tag entries by kind: domain fact vs model workaround.** The negative-transfer result (50.5 → 18.1) says patterns that compensate for a model's weaknesses invert in value on a model upgrade, while domain procedures transfer. `dead_ends.yaml` mixes both — `search_feedview_country_case` is a fact about Pinterest's tables; a formatting quirk of the current Claude is not. One field, and the next model bump has a retirement list instead of a mystery regression.
- **On eval_04 and the standing position.** WikiSkill partially softens "untrained curators append": an untrained maintainer produced edit-dominant behavior (edit:create 0.8–2.8) from a prompt rule plus full-wiki context — which the Curator already has. But the wiki was never measured for quality or coverage, so it neither confirms nor refutes SkillOS's coverage finding (53.6 → 72.9%), and it does **not** license dropping the human gate on new dead ends and checks — the paper's unpruned wiki is its own listed debt. The `eval_04` growth curve stands; add the create:edit ratio as the free companion metric, with Table 4 as the reference range. Also worth adding: the Maintainer harvests *success* patterns from passing traces to prevent regressions; Reflex's capture is correction-skewed (`disagree` / `reframe`), and `approve` / `asana_action` judgments carry no words — "what did approved cards do that failed ones didn't" is an absent Curator category.

**Don't cite for.** Conflict resolution, retirement, pruning, curation quality, a matched-budget claim, or anything about SkillOS — it addresses none of them; and its gains, like every paper in this set, are measured against ground-truth answers.

---

## 11. Context as an Environment: Programmatic Context Management

*arXiv 2608.21690v1 (21 Aug 2026) · Alibaba Group / Columbia · Lin, Ang, Zhu, Ding, Zhou · technical report, system named **Scroll**; code at `github.com/niceIrene/QwenPaw/tree/scroll-research`*

**What it is.** A context manager that keeps the agent's whole history *outside* the prompt as an executable "Session Environment": an append-only Event Log (SQLite, BM25 search, every event with an immutable `seq` address and provenance), durable payload storage behind lazy handles, and a sandboxed Python kernel whose typed namespace persists across model calls. The model writes code to `search` / `expand` / compute over that state; **only what it explicitly `print`s enters the next call's working view.** When the view exceeds budget, spans are evicted — but eviction changes the view, never the record, and a tiered index of model-written headlines keeps evicted regions addressable.

**Numbers.** Backbone Qwen3.8-Max, prompt-time only (one system prompt, no few-shot, no training).

- LongMemEvalS **94.8** (Exabase M-1 96.4, Mastra 94.9, Hindsight 94.6, Mem0 94.4); BEAM10M **73.1**, +5.1 over the best published (Exabase 68.0; Mem0 48.6); LOCA-256K **86.7**, +37.4 over the best published long-horizon agent (MiniMax M3+ReAct 49.3; Claude-4.5-Opus+ReAct 14.7). Table 2 is **uncontrolled** — different reader models, baselines not reproduced, and the paper says so.
- The controlled comparison is Table 3 (same backbone, same tools, only context strategy differs):

| Agent loop | LOCA 128K | 256K | Δ |
|---|---|---|---|
| Summarization (ReAct + periodic compaction) | 86.7 | 65.3 | −21.4 |
| Retrieval (ReAct + evict + recall tool) | 88.0 | 66.7 | −21.3 |
| CodeAct (results bind to variables) | 89.3 | 85.3 | −4.0 |
| Scroll | 89.3 | 86.7 | −2.6 |

- Ablation on BEAM10M (Fig. 3): lossy summarization at ingestion **19.9** (near zero on exact-value categories); Scroll w/o persistent kernel 66 (−7.3, concentrated in knowledge update 92.5→82.5 and instruction following 97.5→76.3); w/o eviction index 71 (−1.8, concentrated where evidence is scattered: preference following 89.1→74.9); full 73.1.
- Backbone spread with the harness held fixed (Table 4): LongMemEvalS 88.8–94.8 across six models, but LOCA-256K **22.7–86.7** — a 64-point spread. Failures are execution errors and premature termination on aggregation-heavy tasks, not protocol violations.
- Cost: median BEAM10M input ~105K tokens, about 1% of the corpus; no ingestion-time LLM calls.

**Honest grade: medium.** Table 3 and Fig. 3 are real same-backbone ablations; Table 2 is a literature lookup. Single run per task, no CIs, LLM judge (Qwen3.6-flash) on two of three benchmarks, rule-based verifier only on LOCA. No search loop, so the AI2/UW attempts-vs-artifact test doesn't apply. Retrieval/state benchmarks only — nothing on generation or discovery quality.

**Main points.**
- **Defer selection to query time.** Compression (ϕ at compaction) and memory extraction (ψ at ingestion) both fix *what survives before future needs are known*; whatever they drop is unrecoverable even though the raw log is on disk. Scroll's move is that the map from state to working view is a program the model writes at each step.
- **Four operations, one boundary.** LOCATE (`ms.search`), MATERIALIZE (`ms.expand(seq)`), COMPUTE (Python over resident variables), EXPOSE (`print`). Everything is LLM-decided *except* the harness guarantees: durable storage, stable addresses, fail-closed sandbox, the 32K observation cap and 1000-row SQL cap, and the eviction algorithm. Programmatic = the substrate; policy = the model.
- **Headlines are an explicit Progress record.** Each response carries a model-written headline — *task, verified state, next action, status* — bound to a `seq` at append time. That is the cheapest Progress externalization in this literature, and it's what makes eviction navigable (position-based, not recall-based).
- **Mapping to EvoHarness-RL's BPE.** *Belief* ≈ the kernel namespace plus the "namespace digest" prepended to every call (name, type, shape, **provenance** — which events each variable derives from). *Progress* ≈ the headline map. *Experience* — **absent.** The Event Log spans sessions but nothing distills cross-episode skills; Scroll is deliberately the opposite of a curator.
- **Where write-time extraction wins and loses (Table 6).** Scroll leads by the widest margins on knowledge update (92.5 vs 45–75), contradiction resolution (88.1 vs 32.5–58.8), and information extraction — tasks that need *both sides of a value timeline, in order, with provenance*. It trails ingestion-heavy pipelines where the graded artifact is itself a condensed view: summarization 70.5 vs 91.9, preference following 89.1 vs 97.5. Neither paradigm dominates; the paper's claim is only that the derived view must never be the *sole* representation.
- **Failures are decided upstream of retrieval (Appendix D).** D.3: all fourteen queries were framed on the wrong axis before any retrieval ran. D.4: session-level coverage was complete, but positional (head-and-tail) reading skipped the mid-session evidence. D.2's success annotation: *successful trajectories issue a disconfirming, address-bounded query before submitting; failed ones never do.*

**Apply to Reflex.**
- **Table 3 is the direct evidence for the Lesson-16 claim that Detect investigations fail as long-horizon tasks.** A Detect cycle is hypothesis → surface check → Presto pull → cross-verify → decide, with tool outputs serialized into context. The ReAct-with-compaction loss (−21 points 128K→256K) versus binding results to variables (−2.6 to −4) says the cheap fix is *where tool results live*, not more prompt. Testable now: does `de_topline_guess_without_constituent_numbers` and the wrong-column class in `dead_ends.yaml` concentrate in cycles where the investigation ran long enough to compact? The lossy-summarization ablation (19.9, near zero on exact values) predicts yes.
- **Open item 14 — "does Detect maintain Belief or Progress?" — now has a minimal spec.** Progress is a per-step headline (task, verified state, next action, status) with an address. `cycle_log.jsonl`'s `phases_attempted/completed/failed` is a post-hoc phase ledger for the Curator, not a during-run record the DS Agent reads back; it's Progress for the *auditor*, not the *policy*. Belief needs provenance per fact — if `context.md` carries claims without the event they came from, it's a summary, not Belief, and the paper says summaries go to zero on exact values.
- **`expert_judgments.jsonl` is the Event Log; `dead_ends.yaml` and `analytical_checks/` are the derived view. Keep that order load-bearing.** The Curator's Conflict Report (Merge / Version / Replace, never silent) is exactly the contradiction-resolution task Scroll wins by 30–55 points *because* it can materialize both sides in order with provenance. The deep-dive already has the right shape — `rationale_verbatim`, `source_ref`, timestamp, `confirmed_by` with dates. The gap is the consumer: the Skeptic reads the derived patterns and audit logs (Check 6d), not the judgment records. A flag that cites "Dylan Wang, Cycle 49/57" is a headline; it should be able to expand the address.
- **The Curator's Phase 0 ("read ALL comments on ALL cards before acting") is a working-view decision, and D.4 is its failure mode.** Cross-comment pattern detection is the aggregation the kernel ablation isolates (−7.3, all in multi-record composition). Under a context budget, "read everything" degrades silently to head-and-tail sampling. Phase 0 should be a program over `expert_judgments.jsonl` — group by `claim_targeted`, expert, category — with the count printed, not a load of Asana prose. Cheap check: does a Phase 0 run touch every record, or does its synthesis cite only early and late comments?
- **Two Skeptic instrumentation items from Appendix D.** (a) D.3 — the outcome was fixed by framing before retrieval; the Skeptic's analogue is card-type classification in the Evidence Check, which sets every downstream severity. `card_type` isn't in `SkepticVerdict`; without it, a wrong-axis review is indistinguishable from a right-axis miss when `human_agreed` is backfilled. (b) D.2 — make the disconfirming query a logged step. "If your review has zero Check 6 findings, ask whether you read the Cycle Learnings" is prose; a `disconfirm_queries: list[str]` field (or `patterns_cited` required non-empty on PASS) makes it scoreable against the 2-round `revision_round` cap.
- **Backbone spread is a warning for any Detect harness change.** Same harness, same prompts: 22.7 to 86.7 on LOCA-256K. A harness improvement measured on one executor says nothing about another; matched-backbone ablations only — which is the same discipline as pinning `judge_version` in EvalResult v2.
- **What it does not license.** Not "stop curating" — ingestion-time pipelines win where the answer *is* a condensed view, and `analytical_checks` are condensed views by design. Not a claim about card quality or discovery; every number is retrieval. Not evidence for learning across episodes — there is no Experience layer, so it says nothing about the Curator's distillation question (that's SkillOS/EvoRec territory). Not production evidence.

**Don't cite for.** Production results, generation or discovery quality, or any cross-system ranking — Table 2 is uncontrolled and the paper says so; cite Table 3 and the ablation only.

---

## 12. Brain: Agentic Memory as a Knowledge Wiki *(the Perplexity product post)*

*Perplexity · product blog, 2026-06-18 · Research Preview for Max / Enterprise Max · `kb/hard/raw/perplexity/brain-agentic-memory-as-a-knowledge-wiki.md` — **reconstructed from secondary coverage; the post itself is Cloudflare-walled from this network***

**What it is.** A work-memory layer for Perplexity Computer. Every completed agent task is logged into a *context graph* — actions, sessions, connectors used, which sources validated, failed attempts, and user corrections. Overnight, a synthesis pass converts the graph into lessons stored in an LLM wiki organized as pages per entity (a project, a data source, a contact, a workflow step); at the start of each run the agent loads the *relevant* pages as a starting map.

**Numbers.** First-party, at launch, no independent benchmark: **+25% answer correctness on tasks the agent has seen before**, **+16% recall** on history-dependent workflows, **−13% cost** on tasks needing historical context.

**Honest grade: thin, and the thinnest in this list.** n undisclosed, no baseline description, and the headline number is on *repeated* tasks — the one regime where any memory helps. Cite the design choices, never the numbers.

**Main points.**
- **Work memory, not user memory.** The line the coverage keeps repeating: most agent memory stores preferences; Brain stores what the agent *did* — what worked, what failed, which sources paid off. It is a performance log with a synthesis step, which is the same shape as EvoRec's Memory → Skill Evolver and SkillOS's trajectory → curator.
- **Two write cadences.** Pages update incrementally after each session *and* in the overnight synthesis pass. Cheap incremental capture, expensive periodic consolidation — the fast/slow split again, applied to memory instead of experiments.
- **Corrections are a first-class input type**, encoded as *avoid this route in this context* — scoped negative lessons, not global rules.
- **Provenance per entry.** Every graph entry links back to the session, file, or connector result that produced it.
- **The acknowledged cost of batch synthesis:** today's error doesn't feed back until tomorrow's pass.
- What it does *not* say, anywhere the coverage reaches: how pages are merged, versioned, or deprecated; how two sessions that disagree are reconciled; how a record is removed. The curation questions are exactly the ones left open.

**Apply to Reflex.**
- **Reflex already has the harder half.** Brain's context graph is `expert_judgments.jsonl` + `verdict_log.jsonl` + `cycle_log.jsonl`; its wiki is `dead_ends.yaml` + `analytical_checks/registry.yaml`; its per-entry provenance is `source_ref` + `confirmed_by`. The difference is that Reflex's design specifies conflict resolution (the Conflict Report), retirement policy (never silent), and blast radius, and Brain's — as far as anyone has reported — doesn't. When someone at work says "Perplexity just shipped this," the answer is: they shipped the capture and the overnight pass; the part they didn't describe is the part the Curator design is mostly about.
- **The overnight pass is the Curator's Phase 0 with a schedule.** "Read ALL comments on ALL cards before acting on any" is a synthesis pass; Brain runs it nightly by default rather than per-trigger. The Curator's per-comment trigger plus a full re-read is the expensive version of the same idea — a scheduled consolidation pass with cheap incremental capture in between is the cheaper one, and it's what both Brain and SkillOS's trained curator converge on.
- **"Avoid this route in this context" is a dead-end entry with `applies_to`.** It confirms the scoping discipline already in `dead_ends.yaml` and argues against any lesson that lacks a context clause.
- **Sources-that-validated is a signal Reflex doesn't capture.** Brain logs which connectors and source documents resolved a task; nothing in the Detect logs records which tables, dashboards, or docs a card's evidence actually came from and whether a human accepted them. That's a cheap addition to the verdict log and it's what makes the World Store's retrieval measurable later.
- **Don't cite for.** The +25% — it's on repeated tasks, self-reported, unbaselined; it will be used against you by anyone who's read the AI2/UW paper.

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

**Fuller detail:** `eval_00_hub.md` (state and open items) · `eval_02` (Chao) · `eval_03` (Janvi) · `eval_04` (Curator) · `eval_05` (the verifiability partition and attempts store) · `eval_07` (World Store) · `eval_08` (memory literature vs the Curator/Skeptic) · `eval_01` (glossary)
