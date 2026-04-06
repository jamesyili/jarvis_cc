---
concept: Reinforcement Learning
tags: [rl, mdp, policy-gradient, q-learning, deep-rl, exploration]
sources:
  - kb/hard/raw/lilian-weng/a-long-peek-into-reinforcement-learning.md
  - kb/hard/raw/lilian-weng/policy-gradient-algorithms.md
  - kb/hard/raw/lilian-weng/exploration-strategies-in-deep-reinforcement-learning.md
  - kb/hard/raw/aman-ai/cs229-reinforcement-learning-and-adaptive-control.md
  - kb/hard/raw/aman-ai/primers-rft.md
  - kb/hard/raw/lilian-weng/meta-reinforcement-learning.md
last_compiled: 2026-04-05
related: [bandits-exploration-exploitation, rl-for-llms, neural-network-training, recommendation-systems]
---

# Reinforcement Learning

Reinforcement Learning (RL) is the study of how an agent learns to act in an environment by maximizing cumulative reward. Unlike supervised learning — where labels provide explicit right answers — the agent only receives scalar reward signals and must figure out which actions caused them. This makes RL uniquely suited to sequential decision-making: robot locomotion, game playing, recommendation ranking, and, increasingly, fine-tuning language models.

## MDP Formulation

Every RL problem is modeled as a **Markov Decision Process (MDP)**: a tuple (S, A, P, γ, R).

- **S** — state space (continuous or discrete)
- **A** — action space
- **P(s, a)** — transition distribution: probability of landing in each successor state after taking action *a* in state *s*
- **γ ∈ [0,1)** — discount factor; rewards at time *t* are weighted by γᵗ
- **R(s, a)** — reward function mapping state-action pairs to scalars

The agent executes a **policy** π: S → A. The **value function** V^π(s) is the expected discounted return from state *s* under policy π:

> V^π(s) = E[r(s₀) + γ r(s₁) + γ² r(s₂) + … | s₀ = s, π]

This satisfies the **Bellman equation**: V^π(s) = R(s) + γ Σ P(s, π(s))(s') V^π(s'). The optimal value function V*(s) = max_π V^π(s) satisfies the Bellman optimality equation, and the optimal policy π* acts greedily with respect to V*.

## Value-Based Methods

### Dynamic Programming: Value Iteration and Policy Iteration

When the model (P, R) is known:

- **Value iteration** — repeatedly applies the Bellman backup V(s) ← R(s) + γ max_a Σ P(s,a)(s') V(s') until convergence. Synchronous or asynchronous update schedules both work; convergence to V* is guaranteed for finite MDPs.
- **Policy iteration** — alternates between (a) evaluating the current policy by solving the system of Bellman linear equations, and (b) improving the policy greedily. Converges faster than value iteration in practice for small state spaces, but solving the linear system becomes expensive for large ones.

### Q-Learning and SARSA

When P and R must be learned from experience, temporal difference (TD) methods use sampled transitions.

- **Q-learning** (off-policy): Q(s,a) ← Q(s,a) + α [r + γ max_a' Q(s',a') − Q(s,a)]. Updates toward the best possible next action regardless of what the agent actually does.
- **SARSA** (on-policy): Q(s,a) ← Q(s,a) + α [r + γ Q(s', a') − Q(s,a)]. Uses the action *actually taken*, making it safer in stochastic environments.

### DQN: Q-Learning at Scale

Deep Q-Networks (DQN) parametrize Q(s,a; θ) with a neural network, enabling Q-learning on high-dimensional state spaces (e.g., raw pixels in Atari). Two key stabilization tricks:

1. **Experience replay** — store (s, a, r, s') tuples in a buffer; sample random mini-batches to break temporal correlations.
2. **Target network** — a frozen copy of Q updated periodically, preventing the moving-target instability of bootstrapping off the same network being trained.

Extensions: Double DQN (decouple action selection from evaluation to reduce overestimation), Dueling DQN (separate value and advantage streams), Prioritized Experience Replay (sample transitions by TD error magnitude).

### Continuous State MDPs and Fitted Value Iteration

Discretizing a continuous state space suffers from the curse of dimensionality — a 10D state discretized into 100 bins yields 10²⁰ states. **Fitted value iteration** instead:

1. Sample *m* states randomly.
2. For each state, estimate the target y_i = R(s_i) + γ max_a E[V(s')] using a learned or simulator-based model.
3. Fit V(s; θ) via supervised regression (linear or nonlinear) toward {(s_i, y_i)}.

Convergence isn't guaranteed in the continuous case but works well empirically, and is the conceptual predecessor to neural value function approximation in DRL.

## Policy Gradient Methods

Value-based methods struggle with large or continuous action spaces and can't directly represent stochastic policies. Policy gradient methods parametrize π_θ(a|s) directly and optimize E[R] by gradient ascent.

### REINFORCE

The **Policy Gradient Theorem** gives: ∇_θ J(θ) = E_π [∇_θ log π_θ(a|s) · G_t], where G_t is the total return from time *t*. REINFORCE estimates this by Monte Carlo rollouts — collect full trajectories, compute returns, then update. High variance; a **baseline** b(s) (typically V(s)) is subtracted from G_t without introducing bias, yielding the **advantage** A(s,a) = G_t − b(s).

### Actor-Critic (A2C/A3C)

Rather than Monte Carlo returns, actor-critic methods use a learned **critic** V(s; w) to compute a low-variance TD advantage: A(s,a) = r + γV(s'; w) − V(s; w). The **actor** π_θ is updated using this advantage; the critic is updated by minimizing the TD error.

**A3C** (Asynchronous Advantage Actor-Critic) runs multiple actor-critic workers in parallel on independent environment copies, aggregating gradients asynchronously. This removes the need for experience replay and enables much faster wall-clock training.

### PPO: Proximal Policy Optimization

The biggest practical failure mode of policy gradient is a large update that collapses the policy. **Trust Region Policy Optimization (TRPO)** constrains the KL divergence between old and new policies — correct but computationally expensive (requires second-order optimization).

**PPO** approximates the TRPO constraint with a clipped surrogate objective:

> L_CLIP(θ) = E[min(r_t(θ) · Â_t, clip(r_t(θ), 1−ε, 1+ε) · Â_t)]

where r_t(θ) = π_θ(a|s) / π_θ_old(a|s) is the probability ratio and ε ≈ 0.1–0.2. The clip prevents the ratio from moving too far, without KL computation. PPO is first-order, stable, and generalizes well — it's the dominant algorithm in RLHF and RFT pipelines for LLMs.

### SAC: Soft Actor-Critic

**SAC** adds an entropy term to the objective: maximize E[R] + α·H(π). This encourages exploration by keeping the policy as random as possible while still being good. SAC is off-policy (uses a replay buffer), making it sample-efficient, and the temperature α can be automatically tuned. SAC is the go-to for continuous control tasks.

## Model-Based RL

Model-free methods learn V or π purely from experience — which is sample-inefficient. **Model-based RL** learns the transition model P̂(s'|s,a) explicitly, then uses it to generate synthetic rollouts, plan ahead, or both.

**Dyna-Q** blends both: after each real transition, run *n* simulated transitions using the learned model to augment updates. This dramatically improves sample efficiency when the model is accurate.

The key tension: a learned model is never perfect. Model error compounds across rollout steps ("compounding error"), leading to overoptimistic value estimates. **Sim-to-real** transfer — training a policy in simulation then deploying in the real world — is model-based RL's most impactful engineering application. Mitigations include domain randomization (varying simulator parameters during training), system identification (fitting the simulator to match real dynamics), and ensemble models (estimating epistemic uncertainty to avoid extrapolating into unreliable model regions).

## Exploration Strategies

Exploration is RL's hardest open problem. The agent must try novel actions to discover high-reward regions, but can't afford to waste too much time on bad ones.

**Classic strategies:**
- **ε-greedy** — take a random action with probability ε, greedy otherwise. Simple but undirected.
- **UCB (Upper Confidence Bound)** — add an exploration bonus inversely proportional to visit count: Q(s,a) + c√(log t / N(s,a)). Theoretically optimal for bandits; harder to apply in deep RL with continuous states. See [[hard/wiki/bandits-exploration-exploitation|Bandits and Exploration-Exploitation]].
- **Thompson Sampling** — maintain a posterior over Q-values; sample a Q-function and act greedily. Principled Bayesian exploration.

**Deep RL exploration:**
- **Intrinsic motivation / curiosity-driven exploration** — reward the agent for visiting novel or surprising states. Curiosity-driven exploration uses prediction error of a forward dynamics model (predicting s_{t+1} from s_t, a_t) as a bonus reward. High prediction error = unfamiliar territory = explore here.
- **Exploration via disagreement** — ensemble of forward dynamics models; disagreement between ensemble members signals epistemic uncertainty, used as intrinsic reward.
- **Count-based exploration** — generalize visit counts to high-dimensional spaces via hash functions or density models; reward proportional to pseudo-count N̂(s)^{-0.5}.
- **NoisyNet** — replace ε-greedy with learned parameter noise in the network weights. The network itself decides how much to explore based on learned uncertainty.
- **Parameter-space vs. action-space noise** — adding noise to network parameters (NoisyNet, SVPG) produces temporally consistent exploration unlike per-step action noise.

The exploitation-exploration tradeoff doesn't disappear in deep RL — it just gets harder because the state space is combinatorially vast and count-based methods don't scale directly.

## Deep RL Architectures

Key systems that defined the field:

| Algorithm | Type | Key Idea |
|-----------|------|----------|
| DQN | Value-based | CNN + replay buffer + target net on Atari |
| A3C | Actor-Critic | Async parallel workers, no replay |
| PPO | Policy Gradient | Clipped surrogate, first-order, stable |
| SAC | Actor-Critic | Entropy maximization, off-policy |
| TD3 | Actor-Critic | Twin critics + delayed actor updates to reduce Q overestimation |
| IMPALA | Actor-Critic | Decoupled acting/learning for distributed scale; V-trace off-policy correction |

## Meta-RL

Standard RL trains one agent for one task. **Meta-RL** trains agents that can rapidly adapt to new tasks from just a few trials — "learning to learn" in the RL setting.

The key insight: if a meta-agent is trained across a distribution of tasks, it can internalize a learning algorithm in its recurrent hidden state. On a new task, the agent's recurrent state functions as a fast learner — updating its implicit policy from in-context reward signals without any gradient steps. Architecturally this is often an LSTM or Transformer processing (s, a, r) tuples across episodes of a new task.

Gradient-based meta-RL (MAML-style) instead learns initial parameters θ that can reach high performance on a new task after just a few gradient steps. The meta-objective is: fine-tune on task T_i, then evaluate. Good initial parameters generalize quickly across the task distribution.

Meta-RL is directly relevant to few-shot adaptation in [[hard/wiki/recommendation-systems|recommendation systems]] (cold-start) and to fast domain adaptation in robotics.

## RL for LLMs: RFT and RLVR

RL has become central to modern LLM post-training via [[hard/wiki/rl-for-llms|Reinforcement Learning for LLMs]].

**Reinforcement Fine-Tuning (RFT)** treats LLM generation as a policy and reward as a verifiability signal — does the output compile, pass test cases, solve the equation? Using GRPO (Group Relative Policy Optimization, a lightweight PPO variant), RFT can improve model performance with as few as 10–100 examples, far outperforming SFT in low-data regimes. The model explores reasoning chains, not just imitates them.

**RLVR (RL with Verifiable Rewards)**, as used in Llama 3 post-training, applies full PPO on tasks with deterministic correctness checks (math, instruction following). RLVR requires heavier infrastructure (rollout workers, verifiers, PPO gradient updates) but scales to 405B+ parameters.

Key distinction: RFT uses GRPO + LoRA for efficiency; RLVR uses PPO + direct weight updates for maximum scale. Both eliminate the need for human-preference labels when outputs can be validated programmatically — making them viable for domains (code, math, science) where verification is cheaper than annotation.

The SFT vs. RFT decision hinges on data availability and verifiability: if you have >1K high-quality labeled examples and don't need reasoning depth, SFT. If you have <100 examples, need chain-of-thought reasoning, and can verify correctness programmatically, RFT.

## Connections and Practical Implications

- **RecSys**: RL framing (session as trajectory, item as action, engagement as reward) enables ranking policies that optimize long-term user value rather than immediate click-through. Exploration strategies directly solve cold-start and diversity problems.
- **Sim-to-real**: The model-based RL paradigm underlies robotics pipelines — train in simulation with domain randomization, deploy in real hardware. The same "model error compounds" concern applies to any system where the training environment doesn't match deployment.
- **RLHF**: Proximal Policy Optimization is the algorithm behind RLHF in ChatGPT, Claude, Gemini. The reward model is a learned proxy for human preference; PPO optimizes the LLM policy against it while KL-diverging from the SFT reference policy.
- **Exploration in production**: In large-scale recommendation, ε-greedy and UCB manifest as forced exploration slots, diversity constraints, and contextual bandit layers — operationalizing the same fundamental tradeoff.
