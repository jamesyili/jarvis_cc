# Primers • Deep Reinforcement Learning

**Source:** https://aman.ai/primers/ai/deep-rl/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Introduction](#introduction)
* [References](#references)
* [Citation](#citation)

## Introduction

* Reinforcement Learning (RL) has been successful in playing various types of games (including classic ones like Go, Pong, Doom, etc.) and robot control. Depending on the specifics of your project, different RL algorithms may be suitable. Here are some algorithms that you might consider:

  1. **Deep Q-Network (DQN):** DQN was one of the first breakthroughs in using deep learning for RL. DQN is a variant of Q-Learning that utilizes deep neural networks to approximate the Q-function (i.e., the action-value function), which is a function that can estimate the future rewards of taking certain actions. This is a good starting point if you’re new to RL. It has been successfully applied to various Atari games, including Pong.
     + DQN combines techniques such as experience replay and target networks to stabilize and improve the learning process. Experience replay involves storing the agent’s experiences in a replay buffer and sampling random batches from it to break the temporal correlation between consecutive samples. Target networks are used to address the issue of moving targets by keeping a separate network with frozen parameters to compute the target Q-values during training.
  2. **Policy Gradients (PG):** In contrast to DQN, which is value-based, PG methods directly optimize the policy function that maps states to actions. The Policy Gradient theorem provides a sound foundation for stable learning, and it’s often used in practice in the form of algorithms like REINFORCE or Actor-Critic methods, such as Proximal Policy Optimization (PPO), or Trust Region Policy Optimization (TRPO) directly optimize the policy function to maximize the expected rewards.
  3. **Actor-Critic methods (A2C, A3C, PPO):** Algorithms such as Advantage Actor-Critic (A2C) or Asynchronous Advantage Actor-Critic (A3C) combine the advantages of both policy gradients and value-based methods by training an actor network to select actions and a critic network to estimate the value function. In other words, these methods try to get the best of both worlds by learning both a policy (the actor) and a value function (the critic). They can be more sample-efficient than pure Policy Gradient methods. Proximal Policy Optimization (PPO), in particular, has been successful in a wide variety of tasks and is often recommended for beginners due to its stability and ease of use. PPO is an actor-critic algorithm that aims to improve sample efficiency and stability in policy optimization. It uses a surrogate objective function and performs multiple epochs of mini-batch updates.
  4. **Evolutionary Strategies (ES):** ES are a family of black-box optimization algorithms that can be used for RL. They can be more robust than other RL methods because they don’t require carefully tuning a learning rate, and they can work well on tasks where the reward is sparse or delayed. OpenAl has used ES to train agents to play games like Pong.
  5. **Monte Carlo Tree Search (MCTS):** MCTS is a planning algorithm that performs simulations and builds a search tree to make decisions. It has been successful in playing games with large action spaces, such as Go and chess. Deep Mind’s AlphaZero also uses MCTS.
* It’s important to note that the performance of these algorithms may vary depending on the specific characteristics of the game, available computational resources, and hyperparameter tuning. It’s recommended to experiment with different algorithms and configurations to find the best approach. It’s also worth noting that RL can be difficult to get right, especially if you’re new to the field, so consider also using [OpenAI Gym](https://aman.ai/papers/#playing-fps-games-with-deep-reinforcement-learning) for simulating environments and [RLlib](https://docs.ray.io/en/latest/rllib/index.html) as an open-source RL library, offering support for production-level, highly distributed RL workloads.

## References

* [Monte Carlo Tree Search in Reinforcement Learning](https://towardsdatascience.com/monte-carlo-tree-search-in-reinforcement-learning-b97d3e743d0f)
* [🤗 Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction?fw=pt)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledEvaluationMetrics,
  title   = {Evaluation Metrics, ROC-Curves and Imbalanced Datasets},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
