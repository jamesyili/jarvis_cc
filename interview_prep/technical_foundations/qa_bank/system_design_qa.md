# System Design Q&A — gap-targeted drills

**How to use:** time-box each to 45 min, whiteboard out loud, *then* read the worked path. This bank **complements** `interview_prep/system_design/` (14 worked designs — harmful-content×5, RAG, captioning, t2i/t2v, search, rec, visual-search, chat). It fills the gaps that folder's own INDEX names — **cipher resolution end-to-end, FP/FN-first framing, 2025-26 alignment** — plus the **training / alignment / agent-era designs** the existing 14 lack (they're inference/classifier/rec designs). Balanced-frontier calibration.

---

## The discipline (drill this first — it's why your Anthropic loop failed)

From `openai_call_prep_2026-05-27.md` post-mortem. Run every design through this:

1. **Clarify the objective + constraints first** (5 min): what are we optimizing, what's the latency/scale budget, who's the adversary? Then draw the system.
2. **Depth-then-breadth, NOT breadth-then-shallow.** Don't list every component. Pick the *most interesting trade-off* and go **three levels deep**, then surface. (Your loop died on breadth-first.)
3. **Lead with the trade-off and who pays, not the metric.** "Here's the FP/FN cost and who bears it" *before* "here's the AUC target."
4. **Always resolve the adversarial case end-to-end.** If a jailbreak/cipher/reward-hack comes up, work it fully: how it beats the naive system, which layer catches it, that layer's FP cost. (Your loop left the substitution-cipher unresolved.)
5. **Never discuss a classifier/model in isolation** — always "X inside a multi-layer system with a feedback loop."
6. **Name the data-distribution traps unprompted** — SSB, popularity bias, train/serve skew, contamination. That's the senior tell.

The clock (from `system_design/00_FRAMEWORK.md`): 5-10 clarify · 10-15 high-level + buy-in · 15-25 deep-dive · 5 wrap.

---

## Drill 1 — Safety classifier for an LLM API (the cipher resolution, done right)

*This is the failed-Anthropic question. Lead with this drill — it's the Integrity seat's core.*

**Clarify:** What harms (CSAM/violence/self-harm/jailbreaks)? Input-only or input+output? Latency budget (this gates model size)? Acceptable FP rate (creator/user friction) vs FN rate (harm leakage)? Volume/QPS?

**High-level — never one classifier, always a multi-layer defense with a feedback loop:**
```
input classifier (fast, cheap, distilled) → mid-generation token monitor →
post-response full-context classifier → human review (escalated) → red-team / RLAIF feedback loop
```
Each layer has its own FP/FN profile and its own cost. The fast input layer is a **distilled, quantized small model** (guide 07) so it can run on every request; the expensive full-context layer only sees what the cheap layers escalate (a **cascade**, exactly like recsys preranking).

**Deep-dive (pick the FP/FN trade-off, go 3 levels):** Lead with *"the FP cost isn't symmetric across users."* Your Snap Discover war story: for borderline (non-violating) content, a **two-tier demotion** — smaller demotion for users who consistently engaged that category, stronger for everyone else, never full removal — cut prevalence 35% while preserving creator autonomy. The universal lesson: **who pays the FP cost matters as much as the FP rate.** Set per-layer thresholds by the *cost asymmetry*, not a global AUC.

**Adversarial resolution (the part that sank the loop — resolve it fully):** Substitution-cipher → "build me a bomb."
- *How it beats the naive classifier:* the input classifier pattern-matches on surface tokens; the ciphered prompt has none of the harmful surface form, so it passes.
- *Which layer catches it:* (a) a **decoding/intent layer** that detects the model *reasoning in cipher* or *about to emit* harmful content — the mid-generation monitor sees the decoded intent the input layer couldn't; (b) the **post-response full-context** classifier sees the actual harmful output. (c) Defense-in-depth: a **constitutional classifier** (RLAIF-trained, guide 05) generalizes to *novel* obfuscations because it's trained against principles, not surface patterns.
- *That layer's FP cost:* the intent layer over-flags benign roleplay/fiction/security-research → mitigate with a **tiered response** (soft-refuse + clarify, not hard block) and route ambiguous cases to human review + the red-team loop, which feeds new adversarial examples back into training.

**Wrap:** metrics = **PR-AUC** (rare positives), per-segment FP rate (fairness), jailbreak bypass rate under an active red-team; guardrails = over-block rate + appeal rate held flat; the eval must be **adversarial and distribution-shifted** (guide 06) — it passes until someone attacks it. 2025-26 reference: Anthropic's **constitutional classifiers** + RLAIF; the layers, not any single model, are the product.

---

## Drill 2 — LLM evaluation / benchmark harness (eval is half the Integrity job)

**Clarify:** Eval for what decision — model-swap go/no-go, regression gate, safety sign-off? Capability or safety (different eval philosophies)? Offline-only or offline+online?

**High-level — the three jobs (guide 06):** measure → correlate (offline predicts online) → validate (stays predictive under shift + optimization). Build a **suite, not a metric**: benchmark battery (named: MMLU/GSM8K/HumanEval/safety suites) + **LLM-as-judge** (scalable) + **human eval** (gold, sampled) + **online A/B with guardrails**.

**Deep-dive (pick *validity*, 3 levels):**
- *Contamination:* dedup, canary strings, **temporal/forward holdout** (your preranking paper trained Jul–Dec, tested Mar–Apr — copy that discipline). A benchmark that leaked into pretraining is fiction.
- *LLM-as-judge bias:* position bias, verbosity bias, self-preference. Mitigate: randomize order, pairwise not pointwise, calibrate the judge against human labels, ensemble judges.
- *Offline↔online correlation:* don't trust an offline metric until you've **regressed online lift on it** (your paper's whole method — PR-AUC predicted the winner *backwards*). Pick theory-justified metrics, calibrate to the outcome.

**Adversarial/hard case:** Goodhart — once the eval is a target, it stops measuring. Rotate held-out sets, keep a private adversarial set, monitor for eval-gaming (suspiciously narrow wins). 

**Wrap:** the meta-point that lands senior — *"the deepest eval failures aren't 'the model is wrong,' they're 'the eval lied'"*; your live UPP P2P case (is the eval even *measuring* cross-surface transfer? if so, more engineers won't fix it) is the validity story.

---

## Drill 3 — RLHF / alignment fine-tuning pipeline (Hoang Ch31 — the seat drill)

**Clarify:** Aligning for what (helpfulness, harmlessness, a domain behavior)? Have you got preference data, or must you build collection? Scale/compute? Is the reward *verifiable* (changes everything)?

**High-level (guide 05):** SFT (demonstrations) → reward model (Bradley-Terry on pairwise prefs) → RL optimization (PPO with KL-to-reference, or **GRPO** if scaling reasoning) → eval gate → ship. If the reward is verifiable (code/math), go **RLVR** and skip the learned RM.

**Deep-dive (pick reward design + hacking, 3 levels):**
- *The central risk:* the gap between learned reward and true preference — the policy hacks any proxy (verbosity/sycophancy). **KL leash** to the reference is the control.
- *Data is the lever:* labeler agreement, coverage (the RM is only valid where you have comparisons), and **KTO** if you can only get unpaired thumbs-up/down (cheaper labeling — relevant if this is integrity data). **RLAIF/constitutional** to scale past human throughput.
- *Optimizer choice:* PPO (needs a critic — memory/serving cost) vs **GRPO** (critic-free, group-relative advantage — the DeepSeek-R1 default; successors DAPO/GSPO for long-CoT).

**Adversarial/hard case:** reward over-optimization — show the train curve where RM score climbs while human-judged quality falls; mitigate with KL, RM ensembles, fresh preference data, early-stop on a held-out human eval.

**Wrap:** *"alignment is a reward-design problem, not a labeling problem"*; eval gate must be adversarial; tie to your Reflex human-correction loop (auditable structured reward) as a deliberate point on the interpretability frontier.

---

## Drill 4 — Foundation-model platform: pretrain → finetune for user representations (your UPP)

**Clarify:** One representation serving many surfaces? What's the self-supervised signal? How do consumers specialize — fine-tune, adapters, conditioning? Who owns the base vs the surfaces (the org question)?

**High-level (your three-tier):** **Foundation Model** (user-level next-token pretraining over action sequences) → **base models** (retrieval = dual-tower CLR, ranking = CFM, fine-tuned by task) → **surface models** (fine-tuned per surface). The thesis: *invest in the shared representation once, surfaces specialize on top.*

**Deep-dive (pick cross-surface transfer, 3 levels):**
- *The win:* shared base + surface fine-tune shipped compounding cross-surface lift (Notif +200k WAU).
- *The honest failure mode:* transfer is **empirical per target** — on one surface it's "not hurting but not clearly helping." First fork = **measurement vs generalization** (is the eval even capturing transfer? if so, bodies don't help). This is the senior beat most candidates can't give.
- *Serving:* base on GPU serving, surfaces fine-tune; negative sampling + popularity correction at the retrieval base; **online/offline feature parity** (feature store) or you train on a distribution you can't serve.

**Adversarial/hard case:** a surface team's parallel architecture (your OneTrans surprise) sidelines the base's feature-cross — resolve by co-designing the next base from both, not relitigating which model "wins."

**Wrap:** scaling laws as the budget tool (~20 tokens/param, shift smaller for serving); the org-design consequence — *whoever owns the representation owns the leverage* — is the platform thesis and the frontier-lab business model.

---

## Drill 5 — Large-scale recommendation / retrieval (your moat, done with the preranking framework)

*Complements `system_design/12_video_newsfeed_rec` + `11_youtube_search` with your paper's depth.*

**Clarify:** Optimize for engagement/relevance/retention? Corpus size, QPS, latency budget? Cold-start prevalence?

**High-level (the cascade):** retrieval (L0, ANN two-tower, →thousands) → preranking (L1/LWS, →hundreds) → ranking (L2, multi-task + utility, →tens) → post-rank (diversity/blending). **The governing insight you can prove: each stage should maximize *agreement with the stage below*, not isolated accuracy.**

**Deep-dive (pick preranking alignment/accuracy — your paper, 3 levels):**
- The objective decomposes into exactly **alignment** (overlap with L2) + **accuracy** (conditional engagement above a shared threshold) — exclusivity + linearity.
- **Measure alignment on the *unimpressed* pool** — impressed data is biased toward what survived to exposure (moved offline winner-prediction 70→80%).
- Train: keep the production accuracy branch, *add* an alignment branch (KL distillation from L2 + weighted pairwise) on the unimpressed distribution.

**Adversarial/hard case:** **SSB** — L1 trains on impressed, serves on the post-CG pool ("exam beyond the syllabus"). Fix: unimpressed negatives + p-select + KD. And calibration (O/E) before scores hit the utility sum, or multi-objective ranking is meaningless.

**Wrap:** offline↔online correlation (calibrate the offline metric to online lift); cold-start = synthetic profiling + content features; **RAG retrieval is this funnel's two-stage version with an LLM on the end.**

---

## Drill 6 — Agentic system with guardrails + eval (your Reflex)

**Clarify:** Autonomy level (workflow vs free-running agent)? What can it *act on* (read-only vs mutate prod)? How is success defined/verified? Multi-agent or single?

**High-level (guide 08):** prefer a **workflow** (predefined paths, auditable) over a free-running agent unless the task space is too open to script. Roles with verification: proposer → **adversarial verifier (critic)** → executor with bounded blast radius → feedback loop. Tools over **MCP**; agent-to-agent over **A2A**.

**Deep-dive (pick reliability, 3 levels):**
- *Compounding error:* 90%/step × 10 ≈ 35% end-to-end → short loops + **independent adversarial verification** (Reflex's Skeptic) is the highest-leverage pattern.
- *Blast radius:* allowlist of writable paths + magnitude caps (diff caps) + human gate on risky actions (Reflex BuildValidator).
- *Eval the trajectory, not just the output* — did it use the right tool, stay in budget, avoid the destructive action? Ground against real state (Reflex grades generated code vs **real merged PRs**).

**Adversarial/hard case:** reward hacking over a long horizon — the agent satisfies the metric while missing intent; mitigate with verification at each step + outcome-vs-trajectory eval. Training frontier: **agentic RL** (RLVR/GRPO over tool-use trajectories) — agents trained, not just prompted.

**Wrap:** the lesson — *"autonomy trades reliability; the whole job is buying it back"*; the **multi-layer safety system IS a multi-agent pipeline** (Drill 1) with a verifier and a feedback loop.

---

## Drill 7 — RAG at scale (LLM-era nuances on top of `system_design/07_rag_system`)

*Don't redo 07 — add the failure modes interviewers probe.*

**Key additions:** retriever/reranker **alignment** (your preranking insight applied — the reranker's top-k must match what the generator actually needs); **index freshness** (stale embeddings = silent recall loss); **chunking** strategy (semantic vs fixed); **hallucination** despite retrieval (grounding/citation eval); **eval** = retrieval recall@k *and* answer faithfulness (LLM-judge with the source). The senior framing: *RAG is a two-stage cascade (embed→ANN→rerank) with an LLM decoder; the failure modes are recall miss, stale index, and retriever/reranker disagreement — which is the alignment problem from recsys preranking.*

---

## How to run this bank
1. Pick a drill. Set 45 min. Whiteboard before reading the worked path.
2. Force yourself through the **discipline checklist** every time — especially depth-then-breadth and resolving the adversarial case.
3. Drills 1-3 are the Integrity/alignment core; 4-6 are your differentiators (most candidates can't do the foundation-model, preranking, or agent designs from production). Lead with your moat when given the choice.
4. Deeper backstops: `references/aman/*.md` (agents.md/agent_systems.md for Drill 6; rl_ppo.md for Drill 3) and `system_design/05_defense_in_depth_full.md` for Drill 1.
