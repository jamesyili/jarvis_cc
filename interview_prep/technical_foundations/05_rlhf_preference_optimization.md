# 05 — RLHF, Preference Optimization & Reward Modeling

> **Bridge:** This is your interview-critical fundamental. Your Anthropic loop died adjacent to here (led with metrics instead of the reward/trade-off; didn't resolve the adversarial case). The Integrity seat's day-to-day *is* preference data + reward design. And you have two real anchors: Reflex's human-correction loop and the RR **Geometric Bandit** — actual RL in production.
> **Book:** Ch 26 (SFT), Ch 27 (RLHF), Ch 28 (RLVR). Read all three deeply per your study plan.

---

## 1. The core idea

Pretraining gives a model **capability**; it does not give it **alignment** — the model can produce a good completion but doesn't know *which* good completion you want. You can't write that down as a labeled dataset because the target is a *preference*, often subjective, sometimes only expressible as "A is better than B." So you **learn a reward from comparisons, then optimize the policy against that reward.** That's the whole of RLHF.

The senior framing: *"Alignment is a reward-design problem, not a data-labeling problem. The labels you can get cheaply are comparisons; the thing you actually optimize is a learned proxy for human preference; and the central risk is the gap between that proxy and what you really want — Goodhart's law with a gradient."*

---

## 2. The classic RLHF pipeline (know every stage cold)

```
[Pretrained LM]
      │  (1) SFT: imitate high-quality demonstrations
      ▼
[SFT model]  ─────────────────────────────► serves as the reference policy π_ref
      │  (2) collect pairwise preferences (A vs B), train a Reward Model
      ▼
[Reward Model r(x,y)]  scalar head on the LM, trained with Bradley-Terry
      │  (3) RL: optimize policy to maximize r, with a KL leash to π_ref
      ▼
[Aligned policy π]
```

### Stage 1 — SFT (supervised fine-tuning)
Fine-tune on curated (prompt, ideal-response) demonstrations. **What SFT can teach:** format, style, task-following, refusals. **What it can't:** ranking among many acceptable answers, or anything you can't demonstrate cleanly. SFT sets the starting point; it doesn't optimize preference.

### Stage 2 — Reward model
Collect comparisons: labelers see two completions, pick the better one. Train a scalar reward $r(x,y)$ with the **Bradley-Terry** objective — maximize the probability the preferred response scores higher:

$$\mathcal{L}_{RM} = -\log \sigma\big(r(x, y_w) - r(x, y_l)\big)$$

($y_w$ = winner, $y_l$ = loser.) The RM is usually the LM with the final token-head swapped for a scalar head. **The hard parts:** labeler agreement / bias, distribution coverage (the RM is only valid where you have comparison data), and reward-model *calibration* (does a score gap mean the same thing everywhere?).

### Stage 3 — RL optimization (PPO)
Optimize the policy to maximize expected reward, **minus a KL penalty** that keeps it from drifting too far from the SFT reference:

$$\max_\pi \; \mathbb{E}_{y\sim\pi}\big[r(x,y)\big] - \beta\, \mathrm{KL}\big(\pi \,\|\, \pi_{ref}\big)$$

The KL term is the leash. Without it the policy **reward-hacks** — finds adversarial completions that score high on the (imperfect) RM but are garbage to humans (verbosity, sycophancy, keyword-stuffing). PPO is the usual optimizer; you don't need the clipped-objective math at EM altitude, but you must be able to say **why the KL penalty exists and what reward hacking looks like.**

---

## 3. The modern variants (vocabulary you must have)

| Method | What changes | Why it matters |
|---|---|---|
| **DPO** (Direct Preference Optimization) | Skip the explicit RM and RL loop. A closed-form loss optimizes the policy *directly* on preference pairs, treating the policy as its own implicit reward model. | Simpler, more stable, no reward-model-serving. The default for many teams. Trade-off: no separate RM to inspect/reuse, can over-fit to the preference set, still needs good data. |
| **KTO** (Kahneman-Tversky Optimization) | Drop the *paired* comparison entirely — train on **unpaired binary labels** ("this output is desirable / undesirable"), with a prospect-theory utility loss (loss aversion, separate weights for desirable vs undesirable). | The data win: binary thumbs-up/down is *far* cheaper to collect than ranked pairs. Matches/beats DPO at scale. Reach for it when you can't get clean comparisons — directly relevant to integrity labeling. |
| **RLAIF / Constitutional AI** | Replace (or augment) human feedback with **AI feedback** — a model critiques/ranks responses against a written "constitution" of principles. | Scales preference collection past human throughput. **Anthropic's public reference**; the substrate of constitutional classifiers. Load-bearing for the Integrity seat. |
| **RLVR** (RL from Verifiable Rewards) | The reward isn't a learned proxy — it's a **verifiable signal** (did the code pass tests? is the math answer correct?). | Powers reasoning models (o-series, DeepSeek-R1). No reward-model-hacking because the reward is ground truth. The reward-design problem mostly disappears *when you can verify*. |
| **GRPO** (Group Relative Policy Optimization) | The optimizer behind the reasoning-model wave (DeepSeek). **Drops the critic/value network** from PPO; instead samples a *group* of G outputs per prompt and uses the **group's mean/std to normalize the reward** into an advantage. | Big efficiency/memory win — no second network to train or serve. This is *the* current answer to "how are reasoning models RL'd." Know it has **successors** (DAPO, GSPO, CISPO) fixing long-chain-of-thought instability — name the trajectory, don't derive it. |

**The through-line to say out loud:** *"The field is moving on two axes. On the reward axis: from learned-proxy rewards — hackable, expensive to label — toward verifiable rewards where you can get them, and AI-generated feedback where you can't verify but can articulate principles. On the optimizer axis: from PPO toward critic-free methods like GRPO that drop the value network and normalize rewards within a sampled group, because at reasoning-model scale a second network is a serving and stability cost you'd rather not pay. Either way the reward-design problem doesn't go away — it moves from 'collect more comparisons' to 'specify the principle' or 'build the verifier.'"*

---

## 4. Bandits & explore/exploit — RLHF's simpler cousin (and your shipped RL)

RLHF is RL in a huge action space. **Bandits** are the tractable case (one decision, immediate reward) and they're where *you* have shipped real reinforcement learning — so this is where you go deep when an interviewer probes RL.

**The RR Geometric Bandit** (your system):
- **Action space:** regions of the OmniSage embedding space, hashed with **SimHash/LSH** (16-bit key) so geometrically-distinct interests get distinct keys. ("Glamping" and "survivalist camping" hash differently → disliking one doesn't penalize the other. This solves *signal bleed*, which Semantic-IDs suffered.)
- **Posterior:** a **Beta distribution per (user, region)** — this is **Thompson sampling**: at serving you *sample* from each region's Beta and act on the sample, so high-uncertainty (new/predicted) regions get explored without a hand-tuned epsilon.
- **Reward = log-lift**, $R_t = \log\frac{CTR_{current}+\epsilon}{CTR_{baseline}+\epsilon}$ — you optimize **momentum, not absolute CTR**, so a high-volume stale interest can't crowd out a low-volume growing one. *(This is a reward-design decision exactly analogous to choosing what an LLM RM rewards — and a great thing to discuss when the topic is "how do you design a reward that doesn't degenerate.")*
- **Negative feedback** (fast-scroll, hide) collapses the posterior immediately — exploration stops on disliked regions ("no zombie clusters").

**Why this is gold in an interview:** Thompson sampling is *principled* exploration (the posterior width drives it), versus epsilon-greedy (a hand-tuned constant). When asked "how do you balance explore/exploit," most candidates say "epsilon-greedy or UCB." You say "Thompson sampling over a hashed embedding space with a momentum-based reward, in production" — and you can defend every word.

---

## 5. Your anchor: Reflex as a human-in-the-loop preference system

Reflex isn't labeled "RLHF," but it *is* the structure, with a twist worth naming:

- **Preference/correction signal:** every human comment on an opportunity card is a correction. The **Skeptic** pre-filters (PASS/FAIL/NEEDS_HUMAN); human approval/override is the ground-truth preference.
- **Policy update:** the **Feedback Curator** turns each correction into a *permanent structured pattern* (analytical check / dead-end). The next cycle's agents read updated state and behave better. **Monotonic improvement** — the quality floor only rises.
- **The twist (and the interview-worthy insight):** Reflex stores the learned signal as **human-legible state, not a scalar reward**. *"We chose an interpretable reward representation — structured rules a human can audit — over an opaque learned reward, because the operators need to trust and edit the policy. That's a deliberate point on the interpretability-vs-expressiveness frontier."* That sentence shows you understand RLHF's failure modes (opacity, reward hacking) well enough to architect *around* them.

Reflex also embodies the **self-calibrating reward model**: the Skeptic reads its own `verdict_log` to check precision (human-agreed rate) and adjusts confidence — a reward model monitoring its own validity against fresh human labels.

---

## 6. Repair the Anthropic-loop failure modes (load-bearing)

Your post-mortem (in `openai_call_prep_2026-05-27.md`) — apply these *here* because alignment/safety questions are where they bit:

1. **Lead with the trade-off and the reward, not the metric.** "Here's what we're rewarding and who pays when it's wrong" *before* "here's the AUC target."
2. **Always resolve the adversarial case.** If a jailbreak / cipher / reward-hack scenario comes up, work it end-to-end: how it beats the naive reward, which layer catches it, the FP cost of that layer. Don't leave it hanging — that's the exact gap that sank the loop (substitution-cipher → "build a bomb," unresolved).
3. **Never discuss the classifier/reward in isolation.** Frame as a *multi-layer system with a feedback loop*: input classifier → mid-generation → post-response full-context → human review → red-team loop. Each layer has its own FP/FN profile. RLHF/constitutional methods are *one layer* of that defense, not the whole thing.
4. **Depth-then-breadth.** Pick the most interesting sub-problem (e.g., reward hacking under distribution shift) and go three levels deep before surfacing.

---

## 7. Interview-portable (90 seconds)

> *"RLHF is reward design, not labeling. You SFT to set a starting policy, train a reward model on pairwise comparisons with a Bradley-Terry loss, then optimize the policy against that reward with a KL leash to the reference — and the whole game is the gap between the learned reward and true preference, because the policy will hack any proxy you give it. The field is moving toward DPO to skip the RL loop, KTO when all you have is thumbs-up/down, RLAIF and constitutional methods to scale feedback past human throughput, verifiable rewards for anything you can check, and critic-free optimizers like GRPO behind the reasoning models. I've shipped the bandit version of this: a Thompson-sampling explore/exploit system over a hashed embedding space, where the reward is log-lift — momentum, not raw engagement — specifically so the reward doesn't degenerate toward popular-but-stale content. And in Reflex I built a human-in-the-loop correction system that deliberately stores the learned signal as auditable structured rules instead of an opaque scalar reward, because the operators have to trust and edit the policy."*

**Likely probes:**
- "Why the KL penalty?" → without it the policy reward-hacks the imperfect RM; KL keeps it near the trusted reference.
- "RLHF vs DPO?" → DPO folds the RM into a closed-form policy loss; simpler/stabler, but you lose a reusable inspectable RM and can over-fit the preference set.
- "PPO vs GRPO?" → GRPO drops the value/critic network and estimates the advantage from a *group* of sampled outputs (reward minus group mean, over group std); cheaper, less memory, more stable at reasoning scale — the DeepSeek-R1 default. Has successors (DAPO/GSPO) for long-CoT.
- "What's reward hacking, concretely?" → verbosity, sycophancy, keyword-stuffing — high RM score, low true value; mitigations: KL leash, RM ensembles, fresh preference data, capping optimization.
- "How would you align a safety classifier?" → constitutional / RLAIF data pipeline, multi-layer defense, FP/FN asymmetry, adversarial eval under distribution shift (tie to guide 06).
- "Explore/exploit?" → Thompson sampling > epsilon-greedy because the posterior drives exploration; your RR bandit as the worked example.

---

## 8. Self-test (out loud, from memory)

1. Draw the three-stage RLHF pipeline. What's the reference policy and where does it come from?
2. Write the Bradley-Terry reward-model loss. What's the RM architecturally?
3. Why the KL term in the PPO objective? What happens without it — give two concrete reward-hacking behaviors.
4. DPO vs classic RLHF — what does DPO remove, and what do you give up?
5. RLVR vs RLHF — what makes a reward "verifiable," and why does that kill reward-model hacking?
6. PPO vs GRPO — what does GRPO remove, and how does it estimate the advantage without a critic? When is KTO the right call over DPO?
7. Explain Thompson sampling using your Geometric Bandit. Why log-lift and not raw CTR for the reward?
8. An interviewer hands you a substitution-cipher jailbreak. Walk the multi-layer resolution end-to-end.

*Shaky on 1–4? Hoang Ch 27–28, deeply (your study plan already flags these Tier 1). 6 is in `retentive_recs.md` §6; 7 is in your OpenAI prep doc.*
