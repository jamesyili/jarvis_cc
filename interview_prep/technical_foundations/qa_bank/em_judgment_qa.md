# EM Technical-Judgment Q&A

**How to use:** these screen the "**manager of ML engineers**" dimension — *technical decision-making*, not people management (that's covered in `Sr. EM Interview Prep.md` + `ethanevans_questions/`). Answer with a **position + the reasoning + a real example from your work**. The strongest EM answers commit to a judgment and show the trade-off; they don't hedge.

> Calibration: balanced frontier, technical-judgment only. Each item: **Q → the principle → your worked example.**

---

## Build vs. buy vs. adopt

**Q1. How do you decide build vs. buy vs. fine-tune an existing model?**
*Principle:* cost of the gap × strategic-ownership value. Buy/API when it's not your differentiator and the base already does it; fine-tune when you need reliable behavior the base lacks; build/pretrain only when the **domain distribution is genuinely off** and owning the representation is the leverage.
*Example:* UPP — generic text models don't represent *user behavior*, and owning the user representation is the platform leverage, so pretraining a foundation model was justified. But for the Reflex agents I deliberately **didn't build** an orchestration framework — Claude Code already does orchestration/persistence/audit, so building one would've been a tool-builder trap.

**Q2. When is "don't build it" the senior call?**
When the substrate already solves it and building competes with your actual differentiator. Reflex = "the repo is the database, git is the audit trail" — I resisted a custom agent framework. The EM failure mode is building infrastructure because it's interesting, not because it's load-bearing.

---

## Pretrain vs. fine-tune vs. prompt

**Q3. A team wants to pretrain a domain model. How do you pressure-test that?**
*Principle:* pretraining is the most expensive option — earn it. Ask: is the domain distribution *actually* off (vs. a prompting/RAG gap)? What's the label budget? Will scaling laws (~20 tokens/param, shift smaller for serving) make the run tractable? Could continued-pretraining or LoRA get 90% for 10%?
*Example:* On UPP I pushed **2b (augment the base CLR with cross-surface training) before 2a (separate models)** — less maintenance, better velocity, and you only split when 2b demonstrably fails. Default to the cheaper, more reversible option first.

**Q4. When do you reach for RAG/prompting over fine-tuning?**
When the base **already knows it** and you need *knowledge*, not *behavior*. RAG for factual grounding/freshness; fine-tune (or DPO/KTO) for a reliable format/behavior/refusal you can't get from prompting. Prompting first — it's the cheapest, most reversible.

---

## Eval & when to trust a result

**Q5. An offline metric says ship; do you?**
*Principle:* not until the offline metric is **calibrated to predict online lift** and guardrails are protected. An offline win is a *hypothesis* about online behavior.
*Example:* the preranking paper is literally this — PR-AUC predicted winners *backwards*; we derived theory-justified metrics and regressed them against online lift to get to 80% winner-prediction on a forward-in-time test set. I don't trust an offline number until I've shown it correlates and understood how it's gamed.

**Q6. A result is ambiguous — "not hurting, not helping." More engineers, or not?**
*Principle:* **diagnose measurement vs. generalization first.** If the eval isn't capturing the effect, more bodies won't fix it — it's an eval-design problem. If the eval is right and it still doesn't transfer, that's a real negative; accept and reframe rather than sprint.
*Example:* live UPP P2P cross-surface transfer. The honest move is to fix the eval methodology before reallocating Devin off CLR (which would weaken the substrate everything depends on).

**Q7. How do you design an eval for a system you'll optimize against?**
Assume Goodhart. Held-out + rotating + a private adversarial set; for safety, **adversarial and distribution-shifted** evals (they pass until attacked); guardrail metrics a win isn't allowed to move. The deepest failures are "the eval lied," not "the model is wrong."

---

## Resourcing & technical risk under uncertainty

**Q8. How do you allocate scarce ML engineers across a risky bet?**
*Principle:* separate the *kind* of risk. Bodies help **debugging/triangulation** risk; bodies don't help **methodology** risk or **doesn't-generalize** risk. Don't disrupt a load-bearing substrate to chase a maybe.
*Example:* P2P pre-OOO — I weighed pulling Devin from CLR (direct help but weakens the UPP backbone) vs. asking Daniel Liu for one engineer (non-disrupting, expands a partnership) vs. letting it ride (if it's an eval problem, bodies don't help). The substrate-protection instinct wins unless the risk is the kind bodies actually reduce.

**Q9. How do you decide how much blast radius to give an automated/agentic system?**
*Principle:* bound it explicitly and expand by demonstrated trust. Allowlist what it can touch + cap the magnitude + gate the risky actions + eval against ground truth.
*Example:* Reflex Build agents write only to an **allowlist** with a **150-line diff cap**, signed off, and generated edits are validated against **real merged PRs**. Autonomy expands as the eval track record earns it — never "let it run and hope."

---

## Technical disagreement & escalation

**Q10. A peer team ships an architecture that undercuts yours. What do you do?**
*Principle:* don't relitigate "whose model wins" — co-design the next version from both, and escalate the *decision*, not the conflict.
*Example:* the OneTrans surprise sidelined UPP v0's feature-cross layer. I reached the peer EM privately before the group thread, secured a forward protocol (EM-to-EM heads-up before LR approval on coupled work), and we prioritized the plan that ships UPP v0 *and* treats OneTrans as parallel exploration — resolved in 24h without escalation.

**Q11. Your IC insists on a technical approach you think is wrong. How do you handle it?**
Make the disagreement about *evidence*, not authority — define the offline eval that would settle it, and let the data decide. If it's reversible and cheap, let them run it (learning + ownership). If it's expensive/irreversible, force the design review first. (This is also how I'd want to be overruled.)

---

## Model & infra trade-offs

**Q12. The model's too slow/expensive to serve. Your playbook?**
*Principle:* inference is the recurring cost — price the trade-offs. **Distill → quantize → batch → cache → cascade** (cheap model first, expensive model only on what survives).
*Example:* the recsys funnel *is* this — LWS exists so we don't run the heavy ranker on thousands of candidates; the two-tower precomputes the item side. Same move as a fast distilled safety classifier in front of an expensive one.

**Q13. When is MoE the right call, and what's the cost?**
When you want more capacity without more per-token FLOPs (frontier models — DeepSeek-V3, Kimi K2 — are MoE). The cost an EM owns: **load-balancing** (expert collapse; modern fix = auxiliary-loss-free biases) and **all-to-all communication** in expert-parallel training. Don't adopt MoE for a model where serving simplicity matters more than capacity.

---

## Shipping, velocity & tech debt

**Q14. How do you trade velocity against correctness in an ML system?**
*Principle:* make velocity an explicit metric and protect the invariants that matter (observability > correctness-of-any-single-output for a *system* that self-heals). Reversible decisions: optimize for speed and learning. Irreversible/blast-radius decisions: gate them.
*Example:* in the Reflex redesign I ranked invariants explicitly — expert-labeling-compounds > observability > correctness > discoverability — and made median idea-to-launch the primary metric, because a self-improving system's value is the *loop speed*, not any one output.

**Q15. When do you stop iterating on a model?**
When the marginal offline gain no longer correlates with online lift, or you've hit a guardrail/validity ceiling. Convergence of two independent signals (offline + a holdout) is the ship signal; chasing offline-only gains past that is Goodharting your own metric.

---

## Hiring & growing ML talent (technical screen)

**Q16. How do you technically screen an ML engineer/EM?**
Probe for **judgment under ambiguity**, not recall: "your offline metric improved but online didn't — debug it" (do they reach for distribution/SSB/correlation, or just tune?); "how would you eval this safely" (adversarial thinking); a real trade-off they made and what they'd do differently. Generic process-essays are the tell of a mid candidate (your own Q4-hypothetical observation on the EM loop).

**Q17. How do you grow an IC's technical judgment?**
Give them a real decision with bounded blast radius + the eval that settles it, then let them own the call. Delegate the *judgment*, not just the task. (Reflex's allowlist model is the same idea applied to an agent — expand autonomy as judgment is demonstrated.)

---

## AI-leverage judgment

**Q18. How do you decide where to apply agents/LLMs vs. classic ML?**
*Principle:* agents/LLMs where the task needs reasoning over unstructured context or open-ended tool use *and* you can verify or bound the output; classic ML where you need calibrated probabilities at scale under tight latency. Often **both**: an LLM reasons over a structured representation a classic model produced.
*Example:* RR uses classic embedding/clustering for the representation and an **LLM as the reasoning layer** over it (UIC → next-best-action) — not LLM-for-everything. And Reflex is a *workflow* (bounded, auditable), not a free-running agent, because production blast radius demands it.

**Q19. What's overhyped vs. underrated in the current AI stack (a take)?**
*Underrated:* eval and reward design — most teams under-invest, and it's where the real failures live. *Overhyped:* fully-autonomous agents for production-critical paths — most reliable "agents" are workflows, and that's the correct call. (Have a real opinion here; senior interviewers want a defensible POV, not neutrality.)
