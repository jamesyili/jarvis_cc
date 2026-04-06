---
concept: LLM Post-Training & Alignment
tags: [rlhf, sft, alignment, dpo, preference-optimization]
sources:
  - kb/hard/raw/aman-ai/primers-preference-optimization.md
  - kb/hard/raw/cameron-wolfe/direct-preference-optimization-dpo.md
  - kb/hard/raw/cameron-wolfe/reward-models.md
last_compiled: 2026-04-05
related: [rl-for-llms, large-language-models, transfer-learning]
---

# LLM Post-Training & Alignment

Post-training transforms a raw pretrained language model — one that predicts the next token — into a useful assistant that responds helpfully and safely. The field has settled on a layered pipeline: Supervised Fine-Tuning (SFT) → Reward Modeling → RL-based preference optimization, with Direct Preference Optimization (DPO) and its variants emerging as lighter alternatives that bypass explicit RL.

## The Post-Training Pipeline

### Stage 1: Supervised Fine-Tuning (SFT)

SFT (also called Instruction Fine-Tuning / IFT) trains the pretrained model on 10,000–100,000 high-quality (prompt, response) pairs using standard next-token prediction loss. Its purpose is narrow: teach the model correct formatting and basic instruction-following behavior. It does *not* instill nuanced preferences about tone, safety, or quality trade-offs. Crucially, SFT requires only supervised learning — no RL machinery. It serves as the initialization point for all downstream alignment stages.

### Stage 2: Reward Modeling

A reward model (RM) is a specialized LLM trained to predict a human preference score for a given (prompt, response) pair. Architecturally, an RM is a decoder-only transformer with an added linear scalar head on the final token's representation — effectively a sequence classifier. It outputs a single scalar: higher means more preferred.

**Preference data collection.** The RM trains on *pairwise preference datasets*: for each prompt, a human annotator selects which of two model responses is better. This binary choice task is far cheaper than writing gold-standard responses from scratch. The resulting dataset has the form `(prompt, chosen, rejected)`.

**Training objective.** The RM is trained to assign higher scores to chosen responses than rejected ones. The loss is derived from the Bradley-Terry model of pairwise comparisons:

```
loss = -log(sigmoid(score_chosen - score_rejected))
```

This is equivalent to a negative log-likelihood loss where the probability of preferring `chosen` over `rejected` is modeled by the score difference.

**RM variants.**
- *Classifier-based RM*: standard approach, adds a linear head on top of an LLM.
- *LLM-as-a-Judge*: prompts a capable LLM to score responses. Scales well but historically less accurate; recent frontier models have closed the gap.
- *Outcome Reward Model (ORM)*: for reasoning tasks, predicts correctness on a per-token basis.
- *Process Reward Model (PRM)*: scores each intermediate reasoning step, enabling more granular training signal but requiring expensive step-level annotation.

**Reward hacking.** RMs are approximations. If the policy is optimized against them long enough, it will find exploits that achieve high RM scores without actually being high quality — a failure mode called reward hacking. This fundamentally caps how long RLHF training can run.

### Stage 3: RL Optimization (PPO-based RLHF)

With a trained RM, Reinforcement Learning from Human Feedback (RLHF) fine-tunes the policy (LLM) by maximizing RM scores while constraining drift from a frozen reference model. The canonical RLHF objective:

```
maximize: E[RM(x, y)] - β * KL(π_θ || π_ref)
```

The KL penalty keeps the policy from deviating too far from the SFT checkpoint. `β` controls the strength of this constraint. PPO is the standard RL optimizer: it updates the policy using a clipped surrogate objective that limits how large any single gradient step can be. PPO requires four models in memory simultaneously: the policy, a frozen reference policy (the SFT model), the reward model, and a value model (critic). This memory overhead is the primary engineering cost of RLHF.

## Direct Preference Optimization (DPO)

DPO bypasses the reward model and PPO entirely, replacing them with a single supervised loss on the policy itself. The insight: starting from the closed-form solution to the RLHF optimization problem, you can rearrange to express the optimal policy directly in terms of the ratio of policy and reference policy probabilities on chosen vs. rejected responses. This yields:

```
loss = -log(sigmoid(β * [log(π_θ(y_w)/π_ref(y_w)) - log(π_θ(y_l)/π_ref(y_l))]))
```

Where `y_w` is the chosen (winning) response and `y_l` is the rejected (losing) response. DPO trains the policy to assign higher *relative probability* (vs. the reference) to chosen responses over rejected ones. No RM is trained, no RL loop is run — just gradient descent over the preference dataset.

**Key properties of DPO:**
- Implicitly learns a reward model inside the policy (the policy is "secretly a reward model").
- Offline: uses a static preference dataset; does not sample from the policy during training.
- More stable than PPO — fewer hyperparameters, no reward hacking risk.
- Generally requires higher-quality, on-distribution preference data to match PPO's performance.
- PPO consistently outperforms DPO in large-scale runs, but the gap narrows substantially with better preference data.

## Alternative Algorithms

### Kahneman-Tversky Optimization (KTO)
Inspired by prospect theory, KTO does not require paired preference data. Instead, it uses individual (prompt, response, label) tuples where the label is simply "good" or "bad." The loss is asymmetric — losses on bad responses are weighted more heavily, reflecting human loss aversion. This makes KTO useful when pairwise annotations are unavailable or costly.

### Group Relative Policy Optimization (GRPO)
GRPO eliminates the critic/value model required by PPO. Instead of estimating advantages via a learned value function, it samples a group of responses per prompt and normalizes rewards within that group (group-relative advantage). This reduces memory overhead significantly and has become the standard RL optimizer for reasoning models (DeepSeek-R1, DeepSeek-V3). GRPO applies an explicit per-token KL penalty in the loss function, unlike PPO which adds it to the reward.

### RLVR (RL with Verifiable Rewards)
When tasks have deterministic ground-truth answers (math, code), rewards can be computed via rule-based verifiers rather than a learned RM. Verifiable rewards avoid reward hacking and allow much longer RL training runs. RLVR has become the dominant approach for training reasoning models and is often layered on top of RLHF in modern pipelines: SFT → RLHF (preference alignment) → RLVR (capability improvement).

## Alignment Tax

Alignment is not free. Post-training improves instruction-following, safety, and helpfulness but can reduce certain raw capabilities — a phenomenon called the "alignment tax." PPO with pretraining gradient mixing (PPO-ptx) partially mitigates this by mixing in a small fraction of the pretraining objective during RL to prevent catastrophic forgetting of world knowledge.

## Modern Post-Training Pipelines

State-of-the-art models (Llama 4, Claude, GPT-4-class) use multi-round pipelines combining several techniques:
1. SFT on high-quality instruction data, including CoT examples
2. RLHF (PPO or DPO) for preference alignment
3. RLVR for reasoning-specific capability improvement
4. Iterative data collection: each RL round generates fresh rollouts, scored and filtered to build the next round's SFT/RM dataset

Data quality is consistently the most impactful variable — better preference data outweighs larger reward models or more RL compute.

## Sources

- Cameron Wolfe, "Direct Preference Optimization (DPO)" — `kb/hard/raw/cameron-wolfe/direct-preference-optimization-dpo.md`
- Cameron Wolfe, "Reward Models" — `kb/hard/raw/cameron-wolfe/reward-models.md`
- Aman.ai, "Primers: Preference Optimization" — `kb/hard/raw/aman-ai/primers-preference-optimization.md`
