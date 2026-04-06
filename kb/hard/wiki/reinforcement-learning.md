---
concept: Reinforcement Learning
tags: [rl, mdp, policy-gradient, q-learning, deep-rl]
sources:
  - kb/hard/raw/lilian-weng/a-long-peek-into-reinforcement-learning.md
  - kb/hard/raw/lilian-weng/policy-gradient-algorithms.md
  - kb/hard/raw/karpathy/deep-reinforcement-learning-pong-from-pixels.md
  - kb/hard/raw/aman-ai/cs229-reinforcement-learning-and-adaptive-control.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/bandits-exploration-exploitation|Bandits & Exploration-Exploitation]]"
  - "[[hard/wiki/rl-for-llms|RL for LLMs]]"
  - "[[hard/wiki/neural-network-training|Neural Network Training]]"
---

# Reinforcement Learning

Reinforcement Learning (RL) is the study of how an agent should take actions in an environment to maximize cumulative reward. Unlike supervised learning — which trains on labeled input-output pairs — RL operates on delayed, sparse feedback. The agent learns by doing: it takes actions, observes consequences, and adjusts its behavior over time.

RL underlies some of the most striking AI achievements: AlphaGo, ATARI game-playing from pixels, robot locomotion, and RLHF for aligning LLMs.

## Markov Decision Processes (MDPs)

Almost all RL problems are formalized as **Markov Decision Processes**. An MDP is a tuple `M = (S, A, P, R, γ)`:

- **S**: set of states
- **A**: set of actions
- **P(s', r | s, a)**: transition probability — how likely we land in state s' with reward r after taking action a in state s
- **R(s, a)**: reward function — expected immediate reward
- **γ ∈ [0, 1)**: discount factor — how much we weight future rewards relative to immediate ones

The **Markov property** says that the future depends only on the current state, not the full history. This is the enabling assumption that makes RL tractable.

The agent's **return** from timestep t is the discounted sum of future rewards:
`G_t = R_{t+1} + γR_{t+2} + γ²R_{t+3} + ...`

**Policy** `π(a|s)` defines the agent's behavior: the probability of taking action a in state s. The goal is to find the policy that maximizes expected return.

**Value functions** quantify how good a state or state-action pair is:
- State-value: `V_π(s) = E_π[G_t | S_t = s]`
- Action-value (Q-value): `Q_π(s, a) = E_π[G_t | S_t = s, A_t = a]`
- Advantage: `A_π(s, a) = Q_π(s, a) - V_π(s)` — how much better is action a than the average?

**Bellman equations** give recursive decompositions of value functions:
`V_π(s) = Σ_a π(a|s) [R(s,a) + γ Σ_{s'} P(s'|s,a) V_π(s')]`

The optimal value function `V*(s)` and optimal policy `π*` satisfy the **Bellman optimality equations**:
`V*(s) = max_a [R(s,a) + γ Σ_{s'} P(s'|s,a) V*(s')]`

## Value-Based Methods

### Value Iteration and Policy Iteration

When the model (P and R) is known, **value iteration** solves for V* by repeatedly applying the Bellman optimality operator until convergence. **Policy iteration** alternates between evaluating the current policy and improving it greedily. Both converge to the optimal policy for finite MDPs.

For small MDPs, policy iteration converges fast with few iterations. For large state spaces, value iteration is often preferred since policy evaluation at each step of policy iteration requires solving a large linear system.

### Q-Learning

When the model is unknown, **Q-learning** learns Q*(s, a) directly from experience (off-policy, model-free). The update rule:
`Q(S_t, A_t) ← Q(S_t, A_t) + α [R_{t+1} + γ max_a Q(S_{t+1}, a) - Q(S_t, A_t)]`

The key: the target uses `max_a Q(S_{t+1}, a)` — the best action value from the next state — regardless of what action the agent actually takes next. This makes Q-learning off-policy.

**SARSA** is the on-policy analogue: the update uses the action actually taken next (`A_{t+1}`) rather than the max, making it follow the behavior policy during learning.

### Deep Q-Network (DQN)

For large state spaces (like Atari game pixels), tabular Q-tables are infeasible. **DQN** approximates Q(s, a; θ) with a neural network. Two key innovations stabilize training:

1. **Experience Replay**: Store transitions `(s, a, r, s')` in a replay buffer. Sample random mini-batches for updates, breaking temporal correlations and improving data efficiency.
2. **Frozen Target Network**: Keep a separate copy of the Q-network (updated every C steps) as the optimization target, preventing oscillations from a moving target.

Loss: `L(θ) = E[(r + γ max_a' Q(s', a'; θ⁻) - Q(s, a; θ))²]`

where θ⁻ are the frozen target network parameters.

## Policy Gradient Methods

Value-based methods learn Q or V and derive a policy implicitly. **Policy gradient** methods directly parameterize and optimize the policy `π_θ(a|s)`.

### The REINFORCE Algorithm

The policy gradient theorem gives the gradient of expected return with respect to policy parameters:
`∇_θ E[R] = E[R_t · ∇_θ log π_θ(a_t|s_t)]`

Intuitively (from Karpathy): run the policy, observe which actions led to good outcomes, and increase their probability proportionally to the reward they generated. This is exactly supervised learning on a "fake" dataset where the labels are the sampled actions and the loss is modulated by the advantage.

**REINFORCE** uses complete episode returns as the reward signal:
`θ ← θ + α · G_t · ∇_θ log π_θ(a_t|s_t)`

High variance is the core problem — a single episode's return is a noisy estimate of expected return. A **baseline** (typically V(s_t)) is subtracted to reduce variance without introducing bias:
`θ ← θ + α · (G_t - V(s_t)) · ∇_θ log π_θ(a_t|s_t)`

The term `G_t - V(s_t)` is the **advantage** — it measures whether the outcome was better or worse than expected.

### Proximal Policy Optimization (PPO)

PPO is the dominant practical algorithm for policy gradient. The core insight: taking too large a policy update destabilizes training. PPO constrains updates by clipping the importance sampling ratio:

`L^CLIP(θ) = E[min(r_t(θ) · A_t, clip(r_t(θ), 1-ε, 1+ε) · A_t)]`

where `r_t(θ) = π_θ(a|s) / π_{θ_old}(a|s)` is the probability ratio. If the new policy diverges too much from the old one, the objective is clipped, preventing catastrophic updates.

PPO is simple to implement, stable across diverse environments, and the algorithm used in RLHF for aligning LLMs.

### Actor-Critic Methods (A2C)

Actor-critic methods separate the policy (actor) and value function (critic):
- **Actor**: π_θ(a|s) — the policy, updated by policy gradients
- **Critic**: V_φ(s) — estimates state value, used to compute the advantage

This hybrid reduces variance (via the critic baseline) while maintaining the policy gradient's end-to-end optimization. In **A2C** (synchronous), multiple parallel workers collect experience simultaneously, improving sample diversity.

Actor update:
`∇_θ J(θ) = E[A(s, a) · ∇_θ log π_θ(a|s)]`

Critic update (minimize TD error):
`L(φ) = (r + γV_φ(s') - V_φ(s))²`

## Temporal-Difference Learning

**Temporal Difference (TD) learning** is model-free and learns from incomplete episodes — unlike Monte Carlo methods which require full episode returns. The TD update bootstraps: it uses its own value estimate as a target rather than waiting for the true return.

TD(0): `V(S_t) ← V(S_t) + α(R_{t+1} + γV(S_{t+1}) - V(S_t))`

The term in parentheses is the **TD error** — the difference between estimated and observed value. TD error is a key signal in RL: reducing it improves value estimates, which improves policy.

**n-step TD** interpolates between TD (n=1) and Monte Carlo (n=∞) by looking n steps ahead before bootstrapping.

## Exploration vs. Exploitation

A fundamental tension in RL: should the agent exploit what it already knows or explore actions with unknown value?

- **ε-greedy**: take the greedy action with probability 1-ε, random otherwise. Anneal ε over training.
- **Entropy bonus**: add a term to the policy gradient objective encouraging high-entropy (diverse) policies.
- **UCB**: prefer actions with high uncertainty — optimism in the face of uncertainty.

## The Credit Assignment Problem

The core difficulty of RL: given a reward at timestep T, which of the many preceding actions caused it? In Pong, the action determining whether you win may have been taken 20 frames earlier. Discounted returns address this by down-weighting temporally distant rewards. Normalizing returns (subtract mean, divide by std) keeps scale stable and functions as a variance reduction technique.

## Key Distinctions

| Property | Q-Learning / DQN | Policy Gradient / PPO |
|---|---|---|
| Policy type | Implicit (argmax over Q) | Explicit (parameterized π) |
| On/off policy | Off-policy | On-policy |
| Continuous actions | Hard (discretization needed) | Natural |
| Sample efficiency | Higher (replay buffer) | Lower |
| Stability | Harder to stabilize | More stable with PPO clipping |

---

## Sources

- Lilian Weng, "A (Long) Peek into Reinforcement Learning," lilianweng.github.io, 2018
- Lilian Weng, "Policy Gradient Algorithms," lilianweng.github.io, 2018
- Andrej Karpathy, "Deep Reinforcement Learning: Pong from Pixels," karpathy.github.io, 2016
- Aman Chadha, "CS229: Reinforcement Learning and Adaptive Control," aman.ai, 2026-04-05
