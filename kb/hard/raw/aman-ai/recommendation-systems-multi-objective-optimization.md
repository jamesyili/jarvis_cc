# Recommendation Systems • Multi-Objective Optimization

**Source:** https://aman.ai/recsys/multi-objective-optimization/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys

---

* [Overview](#overview)
* [Use cases](#use-cases)
* [Reranking with MOO](#reranking-with-moo)
* [Multi-Objective Optimization (MOO) vs. Multi-Armed-Bandit (MAB)](#multi-objective-optimization-moo-vs-multi-armed-bandit-mab)
* [References](#references)

## Overview

* In this article, we will be looking at Multi-Objective Optimization (MOO) with the lens of recommender systems.
* MOO refers to the process of optimizing multiple objectives simultaneously when designing or improving a recommender system. MOO is able to look at multiple objectives at once, such as maximizing accuracy while minimizing error.
* MOO techniques help identify a set of solutions, known as Pareto optimal solutions, that achieve a balance between these conflicting objectives. A solution is considered Pareto optimal if no other solution can improve one objective without sacrificing another. The goal is to find a set of solutions that cover a range of trade-offs between the objectives, allowing the system to cater to different user preferences.
* Researchers and developers in the field of recommender systems use MOO to explore the trade-offs between different objectives and understand the relationship between them. By considering multiple objectives, MOO can provide a more comprehensive and personalized recommendation experience by addressing the diverse needs and preferences of users.

## Use cases

* LinkedIn uses a multi-objective optimization approach to rank content on its Feed. They have a scoring function that assigns a score to each update based on different objectives as shown below.

\[\text { score }=\alpha P(\text { passive consumption })+(1-\alpha) P(\text { active consumption })\]

* The click weight parameter helps determine the balance between content that promotes passive consumption and content that encourages active engagement.
* Different types of content serve different purposes, and there is a trade-off between passive and active consumption. LinkedIn aims to strike a balance between encouraging conversations and accommodating passive consumption by considering the diverse range of content and user preferences on the Feed.
* The MOO model is responsible for suggesting relevant content to users based on multiple objectives, such as maximizing engagement, promoting diversity, and ensuring personalized recommendations. However, finding the optimal values for the model’s parameters can be a complex task.
  + To address this challenge, LinkedIn has developed an automated approach to tune these parameters. This process involves leveraging data-driven techniques and algorithms to iteratively adjust the parameters and optimize the model’s performance. By automating this tuning process, LinkedIn can efficiently explore different parameter settings and identify the ones that yield the best results in terms of achieving their predefined objectives.
* Additionally, In the LinkedIn Notifications recommendation system, Multi-Objective Optimization (MOO) is used to balance multiple objectives, specifically to improve click-through-rate (CTR) and increase the number of sessions while keeping guardrail metrics like “disables” neutral. These objectives can be conflicting because sending more notifications may increase sessions but decrease CTR due to potential lower quality.
* To address this, separate models are built to optimize for CTR and sessions independently. The final model, denoted as M, combines the outputs of these models using a linear combination with tunable combination parameters x. The equation for the final model is Mx = M1 + x1*M2 + x2*M3 + xn-1\*Mn, where each Mi represents a model optimizing for a specific objective.
* By varying the combination parameters x, different models Mx are generated, each representing a different trade-off between the objectives. These models can form the Pareto Front, where improving one objective comes at the expense of another.
* To determine the suitable combination parameters, an online A/B experimentation approach is employed. The primary metric, such as m1, is identified, and the other metrics are considered as guardrail metrics. The model Mx is launched in the A/B experiment, and the resulting metrics m1(x), m2(x), …, mn(x) are collected. These metrics are then used to solve a constrained optimization problem to find the optimal combination of parameters x that satisfy certain threshold values (c2, cn) for the guardrail metrics.
* Techniques like random search and grid search are commonly employed to explore different combinations of parameters x and find the desired balance between the objectives.

## Reranking with MOO

* To perform reranking with multi-objective optimization, a model or algorithm is needed that can handle multiple objectives and determine the best ordering of recommendations that satisfies these objectives. This typically involves defining an objective function that combines the different criteria or objectives into a single utility score for each item. Various techniques, such as multi-objective optimization algorithms, can then be used to find the optimal trade-off between the different objectives.
* The result of reranking with multi-objective optimization is a reordered list of recommendations that takes into account the competing objectives and provides a more balanced and personalized set of recommendations. By considering multiple objectives, the reranking process aims to provide a diverse range of recommendations that cater to the preferences and needs of different stakeholders.

## Multi-Objective Optimization (MOO) vs. Multi-Armed-Bandit (MAB)

* MOO and [MAB](/recsys/multi-armed-bandit) are two different concepts in the field of optimization and decision-making. Let’s look into details of each and the specifics of how they differ.
* As we saw above, MOO focuses on optimizing multiple conflicting objectives simultaneously in an optimization problem. It deals with finding a set of solutions that represent the best trade-offs among different objectives.
* MAB is a framework for solving the exploration-exploitation trade-off problem in decision-making under uncertainty. In MAB, a decision-maker, often referred to as the “agent,” faces multiple options or actions, known as “arms.” The agent needs to learn which arm(s) to select in order to maximize a specific objective, such as cumulative reward or expected return. The challenge lies in balancing the exploration of different arms to gain knowledge about their rewards and the exploitation of the arms with higher expected rewards based on the available information.
* While both MOO and MAB involve decision-making with multiple options, they differ in their objectives and problem settings. MOO deals with optimizing conflicting objectives simultaneously in an optimization problem, whereas MAB focuses on the exploration-exploitation trade-off in selecting actions to maximize a specific objective. MOO typically operates in a static problem setting, while MAB is often used in dynamic and sequential decision-making scenarios.
* Below we can see an overview of how each of these concepts can be leveraged within recommender systems.

## References

* [Using Bayesian optimization for balancing metrics in recommendation systems](https://engineering.linkedin.com/blog/2022/using-bayesian-optimization-for-balancing-metrics-in-recommendat)
* [Autotuning for Multi-Objective Optimization on LinkedIn’s Feed Ranking](https://www.kdnuggets.com/2020/08/autotuning-multi-objective-optimization-linkedin-feed-ranking.html)
* [Bandit based Optimization of Multiple Objectives on a Music Streaming Platform](https://dl.acm.org/doi/pdf/10.1145/3394486.3403374)
