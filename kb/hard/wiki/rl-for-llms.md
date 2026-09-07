---
concept: Reinforcement Learning for LLMs
tags: [rlhf, ppo, grpo, reinforce, reasoning, rlvr, deepseek-r1, rft]
sources:
  - kb/hard/raw/cameron-wolfe/ppo-for-llms-a-guide-for-normal-people.md
  - kb/hard/raw/cameron-wolfe/group-relative-policy-optimization-grpo.md
  - kb/hard/raw/cameron-wolfe/demystifying-reasoning-models.md
  - kb/hard/raw/aman-ai/primers-rft.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/reinforcement-learning|Reinforcement Learning]]"
  - "[[hard/wiki/large-language-models|Large Language Models]]"
  - "[[hard/wiki/llm-post-training|LLM Post-Training]]"
understanding: 1  # very little exposure / unknown (default)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Reinforcement Learning for LLMs

Reinforcement learning has been one of the most impactful areas of LLM research. Early work used RL to align LLMs with human preferences (RLHF). More recently, RL with verifiable rewards (RLVR) has produced a qualitative leap in reasoning capabilities via models like DeepSeek-R1 and the OpenAI o-series. The optimizer landscape has evolved from PPO to critic-free alternatives like GRPO that are simpler and cheaper to run at scale.

## The RLHF Pipeline: SFT → Reward Model → RL

The canonical three-stage alignment pipeline, pioneered by InstructGPT (2022):

**Stage 1 — Supervised Fine-Tuning (SFT)**: Fine-tune the pretrained LLM on high-quality human demonstrations. This teaches the model the format and style of helpful responses.

**Stage 2 — Reward Model Training**: Collect human preference data — pairs of model completions to the same prompt, annotated for which is preferred. Train a reward model (a copy of the LLM with a linear regression head replacing the language head) using a ranking loss derived from the Bradley-Terry preference model:

```
loss = -log(σ(r(prompt, preferred) - r(prompt, rejected)))
```

The trained reward model assigns a scalar preference score to any (prompt, completion) pair.

**Stage 3 — RL Fine-Tuning**: Use the reward model as the reward signal for RL training of the LLM. The default optimizer has been PPO. The KL divergence between the current policy and the SFT reference policy is penalized to prevent reward hacking and maintain readable outputs.

This three-step process substantially improved model helpfulness and made ChatGPT commercially viable. It remains the foundation of most production LLM alignment pipelines.

## RL Formulation for LLMs

In the MDP formulation, each token is an action:

- **Policy**: the LLM itself, π_θ(a_t | s_t)
- **Initial state**: the prompt
- **Actions**: each predicted token
- **State**: the running prompt + generated tokens so far
- **Trajectory**: the full completion
- **Reward**: from reward model (RLHF) or verifier (RLVR)

The goal is to maximize expected cumulative reward. The transition function is deterministic — the state is simply the concatenation of prompt and generated tokens.

## Proximal Policy Optimization (PPO)

PPO is a policy gradient algorithm that replaced TRPO by enforcing a trust region through clipping rather than an explicit KL constraint.

**The policy ratio** compares action probabilities under the current vs. old policy:
```
r_t(θ) = π_θ(a_t | s_t) / π_old(a_t | s_t)
```

**The clipped objective** (the PPO surrogate loss):
```
L_CLIP(θ) = E_t[min(r_t(θ)A_t, clip(r_t(θ), 1-ε, 1+ε)A_t)]
```

The clip mechanism prevents the ratio from straying too far from 1 in either direction, avoiding destructive policy updates. The minimum ensures this is a conservative (lower bound) estimate. When advantage is positive, we don't want to amplify the ratio beyond 1+ε; when advantage is negative, we don't want to deflate below 1-ε.

**KL penalty**: In LLM settings, the KL divergence between current policy and the SFT reference model is subtracted from the reward per token, keeping the policy from drifting into incoherent territory or exploiting the reward model.

**Advantage estimation via GAE**: PPO uses a learned **value model** (critic) — a separate copy of the policy with a regression head — to estimate the expected cumulative reward from each state. The advantage A(s_t, a_t) = Q(s_t, a_t) - V(s_t) tells us how much better this action is than the baseline expectation. Generalized Advantage Estimation (GAE) smooths multi-step TD residuals via a mixing parameter λ to balance variance and bias.

**PPO's cost**: Four models are in memory simultaneously — the active policy, the old policy (frozen during the mini-batch), the reward model, and the value model (critic). Both the policy and critic are updated each step. This high compute and memory overhead made PPO expensive and difficult to reproduce outside top labs.

## REINFORCE and RLOO

**REINFORCE** is the simplest policy gradient — no critic, no clipping, just:
```
gradient ∝ (cumulative reward) × log π_θ(a_t | s_t)
```

High variance makes it unstable at scale. **RLOO (REINFORCE Leave-One-Out)** reduces variance by using the average reward over multiple completions per prompt as a baseline, subtracting it from each completion's reward. This is conceptually a precursor to GRPO.

## Group Relative Policy Optimization (GRPO)

GRPO, introduced in the DeepSeek-R1 paper and applied to LRM training, simplifies PPO by eliminating the critic entirely.

**Advantage estimation without a critic**: For each prompt in the training batch, sample G completions {o_1, ..., o_G}. Compute rewards {r_1, ..., r_G}. The advantage for completion i is:

```
A_i = (r_i - mean(r)) / std(r)
```

This normalized group-relative advantage replaces the learned value function. Every token in completion i gets the same advantage estimate — no per-token credit assignment. The group provides its own internal baseline.

**GRPO surrogate loss** (structurally identical to PPO's):
```
L_GRPO(θ) = E[min(r_t(θ)A_i, clip(r_t(θ), 1-ε, 1+ε)A_i)] - β·KL(π_θ || π_ref)
```

The KL term here is a loss penalty (not subtracted from reward as in PPO). With a single policy update per batch, the clipping simplifies substantially.

**Why GRPO works**: For LLM fine-tuning on verifiable tasks, per-token value estimates are hard to learn from outcome-only rewards (only the final answer is scored). GRPO sidesteps this by treating the whole completion as the unit of credit and normalizing within the group. The simplification trades some theoretical optimality for dramatically reduced memory and implementation complexity.

**GRPO's requirements**: More completions per prompt (typically G=8–16) than PPO (usually G=1) to stabilize the group baseline estimate. This increases generation cost per step but eliminates the critic entirely.

## Reinforcement Learning with Verifiable Rewards (RLVR)

RLHF requires a learned reward model, which introduces reward hacking risk: given enough RL training, the policy learns to exploit model blind spots to get high scores without actually improving. RLVR replaces the reward model with deterministic, rule-based verifiers.

**Verifiable domains**: math (ground-truth answer matching), code (test case execution), logic puzzles (constraint satisfaction). For math, rewards are binary: did the final extracted answer match the reference? For code, rewards come from test suite pass rates.

**Why RLVR enables scale**: Verifiable rewards are much harder to hack. Models can be trained for far more RL steps without collapse. This enabled the large-scale training runs that produced reasoning models with qualitative capability jumps.

**Applications beyond RLVR**: Domains without clear verifiers — creative writing, open-ended reasoning — can use RFT with rule-based format rewards (length adherence, output structure), weak verifiers, or combinations of verifiable and preference rewards. The tradeoff is reward hacking risk re-enters.

## DeepSeek-R1 and the Reasoning Model Pipeline

DeepSeek-R1 demonstrated that RLVR at scale produces emergent reasoning behavior — models spontaneously develop long chain-of-thought reasoning that includes self-verification, backtracking, and problem decomposition. This behavior was not explicitly programmed; it emerged from the reward signal.

The R1 training pipeline:
1. **Base model pretraining** (DeepSeek-V3 architecture)
2. **Cold start SFT** on a small set of long-CoT examples to establish the reasoning format
3. **Large-scale RLVR** with GRPO on math and code problems — many thousands of RL steps
4. **Rejection sampling + SFT** on high-quality RL-generated reasoning traces
5. **RLHF alignment** to restore instruction-following and reduce verbosity

The key insight: RL training compute scales predictably — more RL steps → better reasoning. This opened inference-time scaling: longer reasoning traces at inference also improve accuracy, giving operators a "reasoning effort" knob.

**DeepSeek-R1-Zero** (pure RLVR without cold-start SFT) showed that chain-of-thought reasoning can emerge from scratch via RL alone, though quality is more variable. The full R1 pipeline uses cold-start SFT to stabilize early training.

## RFT: Reinforcement Fine-Tuning for Domain Specialists

RFT is RLVR applied to domain specialization with small, expert datasets. Key characteristics:

- Works with as few as 10–100 high-quality examples if correctness is verifiable
- Rewards come from programmatic validators (test suites, correctness checkers)
- Typically combines GRPO policy updates with LoRA for parameter efficiency
- Suitable when evaluation is easier than labeling (code that compiles and passes tests, math that verifies, data transformations that match schema)

RFT vs. SFT: SFT mimics labeled examples and overfits with few samples. RFT explores via RL and requires only a verification function, not a labeled response. At 100 examples, RFT has shown 60% performance improvement over base model on reasoning tasks while SFT at the same data volume sometimes degrades below baseline.

## Practical Notes

- **PPO** remains the standard for RLHF-style preference alignment where a reward model is available.
- **GRPO** is the standard for RLVR-style reasoning training; used in DeepSeek-R1, Qwen3, OLMo 3, and open-source training frameworks (TRL, verl).
- **REINFORCE/RLOO** is used when compute is very tight and stability requirements are lower.
- **KL coefficient** tuning is critical — too low and the model drifts into gibberish; too high and learning is suppressed.
- Process rewards (dense, per-step) vs. outcome rewards (sparse, per-completion) are an active research area; most production systems use outcome rewards for simplicity.

## Sources

- Cameron Wolfe: PPO for LLMs — full derivation from VPG through TRPO to PPO with pseudocode
- Cameron Wolfe: Group Relative Policy Optimization (GRPO) — RLHF vs. RLVR, PPO limitations, GRPO algorithm
- Cameron Wolfe: Demystifying Reasoning Models — o1, o3, DeepSeek-R1 mechanics, RLVR foundations
- Aman.ai: Primers RFT — RFT vs. SFT decision framework, GRPO+LoRA integration, case studies
