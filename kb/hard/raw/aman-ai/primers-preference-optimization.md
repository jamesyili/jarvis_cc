# Primers • Preference Optimization

**Source:** https://aman.ai/primers/ai/preference-optimization/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Background: LLM Pre-Training and Post-Training](#background-llm-pre-training-and-post-training)
* [Refresher: Basics of Reinforcement Learning (RL)](#refresher-basics-of-reinforcement-learning-rl)
  + [Online vs. Offline Reinforcement Learning](#online-vs-offline-reinforcement-learning)
    - [Overview](#overview-1)
    - [Mathematical Distinction](#mathematical-distinction)
    - [In the Context of LLM Preference Optimization](#in-the-context-of-llm-preference-optimization)
      * [Offline RL in LLMs](#offline-rl-in-llms)
      * [Online RL in LLMs](#online-rl-in-llms)
      * [Hybrid Approaches: Combining Offline and Online RL](#hybrid-approaches-combining-offline-and-online-rl)
    - [Comparative Analysis](#comparative-analysis)
    - [Intuitive Analogy](#intuitive-analogy)
    - [REINFORCE](#reinforce)
      * [Overview](#overview-2)
      * [Online vs. Offline (On-Policy vs. Off-Policy)](#online-vs-offline-on-policy-vs-off-policy)
      * [Takeaways](#takeaways)
    - [Trust Region Policy Optimization (TRPO)](#trust-region-policy-optimization-trpo)
      * [Overview](#overview-3)
      * [Online vs. Offline (On-Policy vs. Off-Policy)](#online-vs-offline-on-policy-vs-off-policy-1)
      * [Takeaways](#takeaways-1)
    - [Proximal Policy Optimization (PPO)](#proximal-policy-optimization-ppo)
      * [Overview](#overview-4)
      * [Online vs. Offline (On-Policy vs. Off-Policy)](#online-vs-offline-on-policy-vs-off-policy-2)
      * [Why PPO Is Still On-Policy](#why-ppo-is-still-on-policy)
      * [Why It’s Sometimes Confused with Off-Policy Methods](#why-its-sometimes-confused-with-off-policy-methods)
      * [Takeways](#takeways)
    - [Direct Preference Optimization (DPO)](#direct-preference-optimization-dpo)
      * [Overview](#overview-5)
      * [Online vs. Offline (On-Policy vs. Off-Policy)](#online-vs-offline-on-policy-vs-off-policy-3)
      * [Comparison to PPO/RLHF](#comparison-to-pporlhf)
      * [Takeaways](#takeaways-2)
    - [Kahneman–Tversky Optimization (KTO)](#kahnemantversky-optimization-kto)
      * [Overview](#overview-6)
      * [Online vs. Offline (On-Policy vs. Off-Policy)](#online-vs-offline-on-policy-vs-off-policy-4)
      * [Takeaways](#takeaways-3)
    - [Group Relative Policy Optimization (GRPO)](#group-relative-policy-optimization-grpo)
      * [Overview](#overview-7)
      * [Online vs. Offline (On-Policy vs. Off-Policy)](#online-vs-offline-on-policy-vs-off-policy-5)
      * [Takeaways](#takeaways-4)
    - [Comparative Analysis: REINFORCE, TRPO, PPO, DPO, KTO, GRPO](#comparative-analysis-reinforce-trpo-ppo-dpo-kto-grpo)
* [Proximal Policy Optimization (PPO)](#proximal-policy-optimization-ppo-1)
  + [Background](#background)
    - [Terminology: RL Overview](#terminology-rl-overview)
      * [States and Actions in LLM Context](#states-and-actions-in-llm-context)
    - [Policy-Based vs. Value-Based Methods vs. Actor-Critic Methods](#policy-based-vs-value-based-methods-vs-actor-critic-methods)
      * [Comparative Analysis](#comparative-analysis-1)
      * [Takeaways](#takeaways-5)
    - [Policy Gradient Theorem](#policy-gradient-theorem)
    - [Classification of PPO, DPO, and GRPO](#classification-of-ppo-dpo-and-grpo)
      * [PPO](#ppo)
      * [DPO](#dpo)
      * [GRPO](#grpo)
      * [Summary Comparison: PPO vs. DPO vs. GRPO](#summary-comparison-ppo-vs-dpo-vs-grpo)
      * [Takeaways](#takeaways-6)
  + [Predecessors of PPO](#predecessors-of-ppo)
    - [The REINFORCE Algorithm](#the-reinforce-algorithm)
    - [Trust Region Policy Optimization (TRPO)](#trust-region-policy-optimization-trpo-1)
      * [Core Idea](#core-idea)
      * [The Role of the Policy Ratio](#the-role-of-the-policy-ratio)
      * [Strengths and Limitations](#strengths-and-limitations)
      * [Paving the way for PPO](#paving-the-way-for-ppo)
  + [Intuition Behind PPO](#intuition-behind-ppo)
    - [Why Not Naive Policy Gradients?](#why-not-naive-policy-gradients)
    - [Why Not Trust Region Policy Optimization (TRPO)?](#why-not-trust-region-policy-optimization-trpo)
    - [How Does PPO Solve These Problems?](#how-does-ppo-solve-these-problems)
  + [Fundamental Components and Requirements](#fundamental-components-and-requirements)
  + [Core Principles](#core-principles)
    - [Policy Gradient Approach](#policy-gradient-approach)
    - [Actor-Critic Framework](#actor-critic-framework)
      * [The Actor (Policy Network)](#the-actor-policy-network)
      * [The Critic (Value Function)](#the-critic-value-function)
  + [Top-Level Workflow](#top-level-workflow)
  + [Key Components](#key-components)
    - [Optimal Policy, Old Policy, and Reference Policy](#optimal-policy-old-policy-and-reference-policy)
    - [Surrogate Objective Function](#surrogate-objective-function)
    - [Clipping Mechanism](#clipping-mechanism)
    - [Data Re-use over Multiple Epochs of Stochastic Gradient Ascent](#data-re-use-over-multiple-epochs-of-stochastic-gradient-ascent)
    - [Value Function and Baseline](#value-function-and-baseline)
  + [PPO’s Objective Function: Clipped Surrogate Loss](#ppos-objective-function-clipped-surrogate-loss)
    - [Intuition](#intuition)
    - [Components](#components)
      * [Purpose of the Clipping Mechanism](#purpose-of-the-clipping-mechanism)
      * [Purpose of Surrogate Loss](#purpose-of-surrogate-loss)
    - [Mathematical Formulation](#mathematical-formulation)
      * [PPO with Clipped Surrogate Loss](#ppo-with-clipped-surrogate-loss)
      * [PPO with KL Divergence Penalty](#ppo-with-kl-divergence-penalty)
      * [PPO with Clipped Surrogate Loss and KL Divergence Penalty](#ppo-with-clipped-surrogate-loss-and-kl-divergence-penalty)
  + [Generalized Advantage Estimation (GAE)](#generalized-advantage-estimation-gae)
    - [Formal Definition](#formal-definition)
    - [Advantage Estimation Approaches](#advantage-estimation-approaches)
    - [GAE Formula and Bias-Variance Trade-off](#gae-formula-and-bias-variance-trade-off)
    - [Role in PPO’s Clipped Surrogate Objective](#role-in-ppos-clipped-surrogate-objective)
  + [Reward and Value Model Roles](#reward-and-value-model-roles)
    - [Classical PPO (Standard RL Context)](#classical-ppo-standard-rl-context)
      * [PPO in RLHF (LLM Alignment Context)](#ppo-in-rlhf-llm-alignment-context)
      * [Comparative Analysis](#comparative-analysis-2)
  + [Variants of PPO](#variants-of-ppo)
    - [PPO-Clip](#ppo-clip)
    - [PPO-Penalty](#ppo-penalty)
  + [Advantages of PPO](#advantages-of-ppo)
  + [Simplified Example](#simplified-example)
  + [Summary](#summary)
* [Reinforcement Learning from Human Feedback (RLHF)](#reinforcement-learning-from-human-feedback-rlhf)
  + [Motivation](#motivation)
  + [Method](#method)
  + [Process](#process)
  + [Loss Function](#loss-function)
    - [Core Objective](#core-objective)
      * [Interpreting the Difference in KL Divergence Between PPO and RLHF](#interpreting-the-difference-in-kl-divergence-between-ppo-and-rlhf)
        + [KL Divergence in Standard PPO](#kl-divergence-in-standard-ppo)
        + [KL Divergence in RLHF (PPO-Based)](#kl-divergence-in-rlhf-ppo-based)
      * [Mixing Pretraining Gradients into PPO (`PPO-ptx`)](#mixing-pretraining-gradients-into-ppo-ppo-ptx)
        + [Motivation](#motivation-1)
        + [Mechanism](#mechanism)
        + [Coefficient Settings and Role Differentiation](#coefficient-settings-and-role-differentiation)
        + [Practical Effects](#practical-effects)
        + [Intuitive Analogy](#intuitive-analogy-1)
    - [PPO Surrogate Objective](#ppo-surrogate-objective)
    - [Value (Critic) Loss](#value-critic-loss)
    - [Entropy Regularization (Optional)](#entropy-regularization-optional)
    - [Total RLHF Loss](#total-rlhf-loss)
    - [Notes on Practical Implementation](#notes-on-practical-implementation)
  + [Pseudocode: RLHF Training Procedure](#pseudocode-rlhf-training-procedure)
    - [Key Steps](#key-steps)
      * [Actor–Critic Coordination](#actorcritic-coordination)
      * [Advantage Estimation](#advantage-estimation)
      * [PPO Clipping Mechanism](#ppo-clipping-mechanism)
      * [KL Penalty and Alignment Stability](#kl-penalty-and-alignment-stability)
      * [Logprob Management and PPO Two-Loop Structure](#logprob-management-and-ppo-two-loop-structure)
      * [Training Dynamics and Outcomes](#training-dynamics-and-outcomes)
  + [Model Roles](#model-roles)
    - [Refresher: Notation Mapping between Classical RL and Language Modeling](#refresher-notation-mapping-between-classical-rl-and-language-modeling)
      * [Core Terminology](#core-terminology)
      * [Trajectories, episodes, and completions](#trajectories-episodes-and-completions)
      * [Reward representations](#reward-representations)
      * [Returns, values, and expectations](#returns-values-and-expectations)
      * [Policy, actions, and distributions](#policy-actions-and-distributions)
      * [Advantage and learning signals](#advantage-and-learning-signals)
      * [Preference optimization vs. general policy optimization for LLMs](#preference-optimization-vs-general-policy-optimization-for-llms)
    - [Policy Model](#policy-model)
      * [Function](#function)
      * [Architecture](#architecture)
      * [Training Data](#training-data)
      * [Typical Model Size](#typical-model-size)
    - [Reference Model](#reference-model)
      * [Function](#function-1)
      * [Architecture](#architecture-1)
      * [Training Data](#training-data-1)
      * [Typical Model Size](#typical-model-size-1)
      * [Comparative Analysis](#comparative-analysis-3)
    - [Reward Model](#reward-model)
      * [Function](#function-2)
      * [Architecture](#architecture-2)
      * [Training Objective](#training-objective)
        + [Background: Bradley-Terry Model](#background-bradley-terry-model)
        + [InstructGPT’s Pairwise Cross-entropy Ranking Loss](#instructgpts-pairwise-cross-entropy-ranking-loss)
      * [Training Data](#training-data-2)
      * [Model Size](#model-size)
      * [Prevention of Over-optimization](#prevention-of-over-optimization)
      * [Evaluation and Monitoring](#evaluation-and-monitoring)
      * [Outcome-Based vs. Process-Based Rewards](#outcome-based-vs-process-based-rewards)
        + [Overview](#overview-8)
        + [Outcome-based rewards](#outcome-based-rewards)
        + [Process-based rewards](#process-based-rewards)
        + [Effect on training dynamics](#effect-on-training-dynamics)
      * [Comparative Analysis](#comparative-analysis-4)
    - [Value Model](#value-model)
      * [Function](#function-3)
      * [Architecture](#architecture-3)
      * [Training Objective](#training-objective-1)
        + [Monte Carlo return used as the regression target](#monte-carlo-return-used-as-the-regression-target)
        + [Why regressing on a single \(R\_t\) yields an expectation](#why-regressing-on-a-single-r_t-yields-an-expectation)
        + [Sampling, rollouts, and empirical expectations](#sampling-rollouts-and-empirical-expectations)
        + [Relationship to PPO and advantage estimation](#relationship-to-ppo-and-advantage-estimation)
        + [Extensions](#extensions)
      * [Training Data](#training-data-3)
      * [Model Size](#model-size-1)
      * [Relationship to the Reward Model](#relationship-to-the-reward-model)
        + [Reward Model: Observed Preference Signal](#reward-model-observed-preference-signal)
        + [Value Model: Expectation over Futures](#value-model-expectation-over-futures)
        + [Outcome-Based vs. Process-Based Rewards](#outcome-based-vs-process-based-rewards-1)
        + [Training-time divergence](#training-time-divergence)
        + [Role in advantage estimation](#role-in-advantage-estimation)
        + [Degenerate cases](#degenerate-cases)
        + [Comparative Analysis](#comparative-analysis-5)
      * [Comparative Analysis](#comparative-analysis-6)
  + [Optimizing the Policy](#optimizing-the-policy)
  + [Integration of Policy, Reference, Reward, and Value Models](#integration-of-policy-reference-reward-and-value-models)
    - [Overview of the RLHF Process](#overview-of-the-rlhf-process)
    - [Core Mathematical Formulation](#core-mathematical-formulation)
    - [Role of Each Model in the Loop](#role-of-each-model-in-the-loop)
    - [Full Training Loop](#full-training-loop)
    - [System Architecture](#system-architecture)
    - [Computational and Practical Considerations](#computational-and-practical-considerations)
    - [Comparative Analysis](#comparative-analysis-7)
  + [Putting it all together: Training Llama](#putting-it-all-together-training-llama)
    - [Llama 4](#llama-4)
      * [Model Overview and Architecture](#model-overview-and-architecture)
      * [Pre-Training: Efficiency, Scale, and Multimodality](#pre-training-efficiency-scale-and-multimodality)
      * [Post-Training and Preference Optimization](#post-training-and-preference-optimization)
      * [Distillation from Llama 4 Behemoth](#distillation-from-llama-4-behemoth)
      * [Reinforcement Learning Infrastructure at Scale](#reinforcement-learning-infrastructure-at-scale)
      * [Safeguards and Bias Mitigation](#safeguards-and-bias-mitigation)
      * [Takeaways](#takeaways-7)
    - [Llama 2](#llama-2)
* [Reinforcement Learning with AI Feedback (RLAIF)](#reinforcement-learning-with-ai-feedback-rlaif)
* [Direct Preference Optimization (DPO)](#direct-preference-optimization-dpo-1)
  + [DPO’s Binary Cross-Entropy Loss](#dpos-binary-cross-entropy-loss)
    - [Simplified Process](#simplified-process)
    - [Loss Function](#loss-function-1)
      * [Equation](#equation)
      * [Implicit KL Regularization in DPO](#implicit-kl-regularization-in-dpo)
      * [Loss Function Design Choices](#loss-function-design-choices)
        + [Negative Sign in Front of the Loss](#negative-sign-in-front-of-the-loss)
        + [Why the Sigmoid Function (\(\sigma\)) is Used](#why-the-sigmoid-function-sigma-is-used)
        + [Role of \(\beta\) in the DPO Loss Function](#role-of-beta-in-the-dpo-loss-function)
        + [Significance of the DPO Loss](#significance-of-the-dpo-loss)
      * [Mapping from the Standard Binary Cross-Entropy Loss to the DPO Loss](#mapping-from-the-standard-binary-cross-entropy-loss-to-the-dpo-loss)
        + [Standard Binary Cross-Entropy Loss](#standard-binary-cross-entropy-loss)
        + [Mapping BCE Loss to DPO Loss](#mapping-bce-loss-to-dpo-loss)
        + [Intuition of the Mapping](#intuition-of-the-mapping)
      * [Key Insights](#key-insights)
    - [Understanding DPO’s Loss Function](#understanding-dpos-loss-function)
      * [Component-by-Component Interpretation](#component-by-component-interpretation)
      * [Intuitive Breakdown](#intuitive-breakdown)
      * [Gradient Interpretation (Implicit Reward Function)](#gradient-interpretation-implicit-reward-function)
    - [How does DPO generate two responses and assign probabilities to them?](#how-does-dpo-generate-two-responses-and-assign-probabilities-to-them)
    - [DPO and it’s use of the Bradley-Terry model](#dpo-and-its-use-of-the-bradley-terry-model)
      * [How does DPO implicitly use a Bradley-Terry Model (if it does not explicitly use a reward model)?](#how-does-dpo-implicitly-use-a-bradley-terry-model-if-it-does-not-explicitly-use-a-reward-model)
        + [Key Concepts in DPO Without an Explicit Reward Model](#key-concepts-in-dpo-without-an-explicit-reward-model)
        + [Implicit Use of Bradley-Terry Model](#implicit-use-of-bradley-terry-model)
        + [Steps in DPO Without Explicit Reward Model](#steps-in-dpo-without-explicit-reward-model)
        + [Practical Implementation](#practical-implementation)
    - [Video Tutorial](#video-tutorial)
    - [Summary](#summary-1)
* [Kahneman-Tversky Optimization (KTO)](#kahneman-tversky-optimization-kto)
  + [KTO’s Loss Function](#ktos-loss-function)
  + [Core Principles from Prospect Theory](#core-principles-from-prospect-theory)
  + [Key Elements of KTO’s Loss Function](#key-elements-of-ktos-loss-function)
  + [Loss Function Equation](#loss-function-equation)
  + [Intuition Behind the Loss Function](#intuition-behind-the-loss-function)
  + [Practical Considerations](#practical-considerations)
  + [Summary](#summary-2)
* [Group Relative Policy Optimization (GRPO)](#group-relative-policy-optimization-grpo-1)
  + [Key Features and Approach](#key-features-and-approach)
  + [GRPO Equations](#grpo-equations)
  + [KL Penalty: PPO vs. GRPO](#kl-penalty-ppo-vs-grpo)
    - [PPO: Implicit Per-Token KL Penalty in the Reward Function](#ppo-implicit-per-token-kl-penalty-in-the-reward-function)
    - [GRPO: Explicit Per-Token KL Penalty in the Loss Function](#grpo-explicit-per-token-kl-penalty-in-the-loss-function)
  + [Implementation Details](#implementation-details)
  + [Pros and Cons](#pros-and-cons)
    - [Pros](#pros)
    - [Cons](#cons)
  + [Applications and Results](#applications-and-results)
* [GRPO Successors](#grpo-successors)
  + [Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO)](#decoupled-clip-and-dynamic-sampling-policy-optimization-dapo)
    - [DAPO vs. GRPO: Key Differences](#dapo-vs-grpo-key-differences)
    - [DAPO: Implementation Details](#dapo-implementation-details)
      * [Objective Function](#objective-function)
      * [Clip-Higher (Asymmetric Clipping)](#clip-higher-asymmetric-clipping)
      * [Dynamic Sampling](#dynamic-sampling)
      * [Token-Level Policy Gradient Loss](#token-level-policy-gradient-loss)
      * [Overlong Reward Shaping](#overlong-reward-shaping)
      * [Training Implementation Summary](#training-implementation-summary)
    - [DAPO vs. GRPO Summary](#dapo-vs-grpo-summary)
    - [Empirical Gains](#empirical-gains)
  + [GRPO+: A Stable Evolution of GRPO for Reinforcement Learning in DeepCoder](#grpo-a-stable-evolution-of-grpo-for-reinforcement-learning-in-deepcoder)
    - [Motivation for GRPO+](#motivation-for-grpo)
    - [Key Innovations in GRPO+](#key-innovations-in-grpo)
    - [Objective Function: From GRPO to GRPO+](#objective-function-from-grpo-to-grpo)
      * [Final GRPO+ Objective](#final-grpo-objective)
    - [Implementation Details](#implementation-details-1)
    - [Comparison: GRPO vs. GRPO+](#comparison-grpo-vs-grpo)
    - [Why GRPO+ Works](#why-grpo-works)
    - [Results and Performance Impact](#results-and-performance-impact)
  + [Group Sequence Policy Optimization (GSPO)](#group-sequence-policy-optimization-gspo)
    - [Motivation: Why Move from Token-Level to Sequence-Level Optimization?](#motivation-why-move-from-token-level-to-sequence-level-optimization)
    - [GSPO Objective](#gspo-objective)
      * [Group-Based Advantage](#group-based-advantage)
      * [Sequence-Level Importance Ratio](#sequence-level-importance-ratio)
      * [GSPO Clipped Objective](#gspo-clipped-objective)
    - [Gradient Analysis](#gradient-analysis)
    - [GSPO-token Variant](#gspo-token-variant)
    - [Stability Benefits for MoE Training](#stability-benefits-for-moe-training)
    - [Empirical Observations](#empirical-observations)
    - [Comparison: GSPO vs. GRPO](#comparison-gspo-vs-grpo)
  + [Clipped Importance Sampling Policy Optimization (CISPO)](#clipped-importance-sampling-policy-optimization-cispo)
    - [Motivation: Why Token Clipping Fails in Long-CoT RL](#motivation-why-token-clipping-fails-in-long-cot-rl)
    - [Core Idea of CISPO](#core-idea-of-cispo)
    - [Off-Policy REINFORCE with Importance Correction](#off-policy-reinforce-with-importance-correction)
    - [CISPO Objective](#cispo-objective)
      * [Clipped Importance Sampling Weight](#clipped-importance-sampling-weight)
      * [CISPO Loss](#cispo-loss)
      * [Group Relative Advantage](#group-relative-advantage)
    - [Why CISPO Is More Stable](#why-cispo-is-more-stable)
    - [Unified Perspective](#unified-perspective)
    - [Empirical Results](#empirical-results)
    - [Comparison: GRPO vs. DAPO vs. CISPO](#comparison-grpo-vs-dapo-vs-cispo)
* [Comparative Analysis: REINFORCE vs. TRPO vs. PPO vs. DPO vs. KTO vs. APO vs. GRPO](#comparative-analysis-reinforce-vs-trpo-vs-ppo-vs-dpo-vs-kto-vs-apo-vs-grpo)
  + [Tabular Comparison](#tabular-comparison)
  + [Comparative Performance: DPO vs. PPO](#comparative-performance-dpo-vs-ppo)
  + [Experimental Setup](#experimental-setup)
  + [Key Findings](#key-findings)
    - [Performance on Alignment and Reward Metrics](#performance-on-alignment-and-reward-metrics)
    - [Stability and Training Dynamics](#stability-and-training-dynamics)
    - [Sample Efficiency and Computational Cost](#sample-efficiency-and-computational-cost)
    - [Scaling Trends and Model Size Effects](#scaling-trends-and-model-size-effects)
    - [Robustness to Preference Noise](#robustness-to-preference-noise)
    - [Practical Implications](#practical-implications)
  + [Analytical Perspective](#analytical-perspective)
  + [Connections to Related Work](#connections-to-related-work)
  + [Takeaways](#takeaways-8)
* [Agentic Reinforcement Learning via Policy Optimization](#agentic-reinforcement-learning-via-policy-optimization)
  + [Milestone-Based Reward System](#milestone-based-reward-system)
    - [Example Milestones by Task Category](#example-milestones-by-task-category)
  + [Example Reward Function](#example-reward-function)
  + [Example instantiation](#example-instantiation)
* [Bias Concerns and Mitigation Strategies](#bias-concerns-and-mitigation-strategies)
* [TRL - Transformer RL](#trl---transformer-rl)
* [Selected Papers](#selected-papers)
  + [OpenAI’s Paper on InstructGPT: Training language models to follow instructions with human feedback](#openais-paper-on-instructgpt-training-language-models-to-follow-instructions-with-human-feedback)
  + [Constitutional AI: Harmlessness from AI Feedback](#constitutional-ai-harmlessness-from-ai-feedback)
  + [OpenAI’s Paper on PPO: Proximal Policy Optimization Algorithms](#openais-paper-on-ppo-proximal-policy-optimization-algorithms)
  + [A General Language Assistant as a Laboratory for Alignment](#a-general-language-assistant-as-a-laboratory-for-alignment)
  + [Anthropic’s Paper on Constitutional AI: Constitutional AI: Harmlessness from AI Feedback](#anthropics-paper-on-constitutional-ai-constitutional-ai-harmlessness-from-ai-feedback)
  + [RLAIF: Scaling RL from Human Feedback with AI Feedback](#rlaif-scaling-rl-from-human-feedback-with-ai-feedback)
  + [A General Theoretical Paradigm to Understand Learning from Human Preferences](#a-general-theoretical-paradigm-to-understand-learning-from-human-preferences)
  + [SLiC-HF: Sequence Likelihood Calibration with Human Feedback](#slic-hf-sequence-likelihood-calibration-with-human-feedback)
  + [Reinforced Self-Training (ReST) for Language Modeling](#reinforced-self-training-rest-for-language-modeling)
  + [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](#beyond-human-data-scaling-self-training-for-problem-solving-with-language-models)
  + [Diffusion Model Alignment Using Direct Preference Optimization](#diffusion-model-alignment-using-direct-preference-optimization)
  + [Human-Centered Loss Functions (HALOs)](#human-centered-loss-functions-halos)
  + [Nash Learning from Human Feedback](#nash-learning-from-human-feedback)
  + [Group Preference Optimization: Few-shot Alignment of Large Language Models](#group-preference-optimization-few-shot-alignment-of-large-language-models)
  + [ICDPO: Effectively Borrowing Alignment Capability of Others via In-context Direct Preference Optimization](#icdpo-effectively-borrowing-alignment-capability-of-others-via-in-context-direct-preference-optimization)
  + [ORPO: Monolithic Preference Optimization without Reference Model](#orpo-monolithic-preference-optimization-without-reference-model)
  + [Human Alignment of Large Language Models through Online Preference Optimisation](#human-alignment-of-large-language-models-through-online-preference-optimisation)
  + [Contrastive Preference Optimization: Pushing the Boundaries of LLM Performance in Machine Translation](#contrastive-preference-optimization-pushing-the-boundaries-of-llm-performance-in-machine-translation)
  + [sDPO: Don’t Use Your Data All at Once](#sdpo-dont-use-your-data-all-at-once)
  + [RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models](#rs-dpo-a-hybrid-rejection-sampling-and-direct-preference-optimization-method-for-alignment-of-large-language-models)
  + [The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning](#the-unlocking-spell-on-base-llms-rethinking-alignment-via-in-context-learning)
  + [MDPO: Conditional Preference Optimization for Multimodal Large Language Models](#mdpo-conditional-preference-optimization-for-multimodal-large-language-models)
  + [Aligning Large Multimodal Models with Factually Augmented RLHF](#aligning-large-multimodal-models-with-factually-augmented-rlhf)
  + [Statistical Rejection Sampling Improves Preference Optimization](#statistical-rejection-sampling-improves-preference-optimization)
  + [Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models](#sycophancy-to-subterfuge-investigating-reward-tampering-in-language-models)
  + [Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study](#is-dpo-superior-to-ppo-for-llm-alignment-a-comprehensive-study)
  + [Pairwise Proximal Policy Optimization: Harnessing Relative Feedback for LLM Alignment](#pairwise-proximal-policy-optimization-harnessing-relative-feedback-for-llm-alignment)
  + [BPO: Supercharging Online Preference Learning by Adhering to the Proximity of Behavior LLM](#bpo-supercharging-online-preference-learning-by-adhering-to-the-proximity-of-behavior-llm)
  + [SimPO: Simple Preference Optimization with a Reference-Free Reward](#simpo-simple-preference-optimization-with-a-reference-free-reward)
  + [Discovering Preference Optimization Algorithms with and for Large Language Models](#discovering-preference-optimization-algorithms-with-and-for-large-language-models)
  + [Anchored Preference Optimization and Contrastive Revisions: Addressing Underspecification in Alignment](#anchored-preference-optimization-and-contrastive-revisions-addressing-underspecification-in-alignment)
  + [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](#deepseekmath-pushing-the-limits-of-mathematical-reasoning-in-open-language-models)
  + [Understanding R1-Zero-Like Training: A Critical Perspective](#understanding-r1-zero-like-training-a-critical-perspective)
  + [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](#dapo-an-open-source-llm-reinforcement-learning-system-at-scale)
* [Further Reading](#further-reading)
  + [HuggingFace’s Alignment Handbook](#huggingfaces-alignment-handbook)
  + [Empirical Evaluation: DPO vs. IPO vs. KTO](#empirical-evaluation-dpo-vs-ipo-vs-kto)
* [FAQs](#faqs)
  + [In RLHF, what are the memory requirements of the reward and critic model compared to the policy/reference model?](#in-rlhf-what-are-the-memory-requirements-of-the-reward-and-critic-model-compared-to-the-policyreference-model)
  + [Why is the PPO/GRPO objective called a clipped “surrogate” objective?](#why-is-the-ppogrpo-objective-called-a-clipped-surrogate-objective)
  + [Is the importance sampling ratio also called the policy or likelihood ratio?](#is-the-importance-sampling-ratio-also-called-the-policy-or-likelihood-ratio)
  + [Does REINFORCE and TRPO in policy optimization also use a surrogate loss?](#does-reinforce-and-trpo-in-policy-optimization-also-use-a-surrogate-loss)
  + [Does DPO remove both the critic and reward model?](#does-dpo-remove-both-the-critic-and-reward-model)
* [Further Reading](#further-reading-1)
* [References](#references)
* [Citation](#citation)

## Overview

* In 2017, OpenAI introduced a groundbreaking approach to machine learning called Reinforcement Learning from Human Feedback (RLHF), specifically focusing on human preferences, in their paper [“Deep RL from human preferences”](https://arxiv.org/abs/1706.03741). This innovative concept has since inspired further research and development in the field.
* The concept behind RLHF is straightforward yet powerful: it involves using a pretrained language model and having human evaluators rank its outputs. This ranking then informs the model to develop a preference for certain types of responses, leading to more reliable and safer outputs.
* RLHF effectively leverages human feedback to enhance the performance of language models. It combines the strengths of Reinforcement Learning (RL) algorithms with the nuanced understanding of human input, facilitating continuous learning and improvement in the model.
* Incorporating human feedback, RLHF not only improves the model’s natural language understanding and generation capabilities but also boosts its efficiency in specific tasks like text classification or translation.
* Moreover, RLHF plays a crucial role in addressing bias within language models. By allowing human input to guide and correct the model’s language use, it fosters more equitable and inclusive communication. However, it’s important to be mindful of the potential for human-induced bias in this process.

## Background: LLM Pre-Training and Post-Training

* The training process of Large Language Models (LLMs) comprises two distinct phases: pre-training and post-training, each serving unique purposes in developing capable language models:

  1. **Pre-training:** This phase involves large-scale training where the model learns next token prediction using extensive web data. The dataset size often ranges in the order of trillions of tokens, including a mix of publicly available and proprietary datasets to enhance language understanding. The objective is to enable the model to predict word sequences based on statistical likelihoods derived from vast textual datasets.
  2. **Post-training:** This phase is intended to improve the model’s reasoning capability. It typically consists of two stages:
     + **Stage 1: Supervised Fine-Tuning (SFT):** The model is fine-tuned using a small amount of high-quality expert reasoning data, typically in the range of 10,000 to 100,000 prompt-response pairs. This phase employs supervised learning to fine-tune the LLM on high-quality expert reasoning data, including instruction-following, question-answering, and chain-of-thought demonstrations. The objective is to enable the model to effectively mimic expert demonstrations, though the limitation of available expert data necessitates additional training approaches.
     + **Stage 2: RLHF:** This stage refines the model by incorporating human preference data to train a reward model, which then guides the LLM’s learning through RL. RLHF aligns the model with nuanced human preferences, ensuring more meaningful, safe, and high-quality responses.

## Refresher: Basics of Reinforcement Learning (RL)

* Reinforcement Learning (RL) is based on the interaction between an agent and its environment, as depicted in the diagram below [(source)](https://www.youtube.com/watch?v=2MBJOuVq380):

* In this interaction, the agent takes an action, and the environment responds with a state and a reward. Here’s a brief on the key terms:
  + The **reward** is the objective that we want to optimize.
  + A **state** is the representation of the environment/world at the current time index.
  + A **policy** is used to map from that state to an action.
* A detailed discourse of RL is offered in our [Reinforcement Learning](../reinforcement-learning) primer.

#### Online vs. Offline Reinforcement Learning

##### Overview

* Reinforcement learning can be broadly classified into two paradigms based on how the agent interacts with data and the environment: **online RL** and **offline RL** (also known as **batch RL**).
* **Online RL:**

  + The agent actively interacts with the environment during training.
  + After taking an action, it immediately observes the new state and reward, then updates its policy accordingly.
  + Learning happens in real time — the policy evolves continuously as new experiences are collected.
  + Online RL is dynamic and adaptive, allowing exploration of unseen states but can be unstable or costly if environment interactions are expensive.
* **Offline RL (Batch RL):**

  + The agent learns purely from a fixed dataset of past experiences, without additional interaction with the environment.
  + This dataset typically consists of tuples of the form `(state, action, reward, next state)`, collected from human demonstrations, logged policies, or previous agents.
  + Since the agent cannot explore beyond the given data, it must balance generalization with the risk of overfitting or extrapolating to unseen actions.
  + Offline RL is especially valuable when environment interaction is expensive, risky, or infeasible (for example, autonomous driving, healthcare, or LLM preference learning).

##### Mathematical Distinction

* In online RL, data is generated by the current policy, meaning the state-action distribution \(D\_{\pi}\) depends on the policy being optimized. Thus, updates occur as:

\[J(\pi) = \mathbb{E}\_{(s, a) \sim D\_{\pi}} [R(s, a)]\]

* In offline RL, the dataset \(D\_{\beta}\) is collected from a *behavior policy* \(\beta\), and optimization must be done off-policy:

  \[J(\pi) = \mathbb{E}\_{(s, a) \sim D\_{\beta}} \left[ \frac{\pi(a|s)}{\beta(a|s)} R(s, a) \right]\]
  + Here, the ratio \(\frac{\pi(a\mid s)}{\beta(a\mid s)}\) corrects for distribution mismatch between the current policy and the dataset. However, large discrepancies can cause instability or high variance in training. To mitigate this, offline RL often applies **regularization** that constrains the learned policy to remain close to the behavior policy.

##### In the Context of LLM Preference Optimization

* For LLMs, online and offline RL determine how preference data and reward models are used to align models with human intent.
* Offline RL (such as [Direct Preference Optimization (DPO)](#direct-preference-optimization-dpo)) provides stable, efficient fine-tuning from pre-collected data, while online RL (such as [Proximal Policy Optimization (PPO)](#proximal-policy-optimization-ppo)) enables continual improvement through active interaction with a reward model. Hybrid systems blend both for balance and scalability.

###### Offline RL in LLMs

* **Definition in LLM Context:**

  + Offline RL trains a language model from a fixed dataset of human or AI-labeled preferences, without interactive data collection.
  + Common examples include **SFT** and **DPO**.
* **Data Source:**

  + The dataset contains `(prompt, response, preference)` triplets where human or AI annotators have pre-ranked model outputs.
* **Advantages:**

  + **Stable and deterministic:** Training proceeds on a known dataset, ensuring reproducibility and smooth optimization.
  + **Efficient and low-cost:** Avoids the computational overhead of continuous environment interaction or online sampling.
  + **Scalable:** Enables parallel training across large datasets and hardware clusters.
  + **Safe and controlled:** Particularly suitable when online experimentation is risky (e.g., autonomous driving, healthcare, etc.).
* **Limitations:**

  + **No exploration:** The model cannot discover new, improved responses outside the training data.
  + **Distributional shift:** The static dataset may not represent the full space of prompts or reasoning trajectories encountered in deployment.
  + **Potential overfitting:** The model might overalign to narrow stylistic patterns from annotators.
  + **Limited adaptivity:** Cannot respond dynamically to evolving human preferences or tasks.
* **Examples in Practice:**

  + [DPO](#direct-preference-optimization-dpo): Uses static preference pairs to directly optimize policy likelihood ratios.
  + Offline preference optimization also underlies reward model pretraining in early **RLHF** pipelines.

###### Online RL in LLMs

* **Definition in LLM Context:**

  + Online RL fine-tunes a model by generating new responses, evaluating them with a reward model, and updating parameters iteratively.
  + Implemented primarily via **Proximal Policy Optimization (PPO)** or a variant such as **Group Relative Policy Optimization (GRPO)**.
* **Process:**

  1. The current policy (LLM) generates multiple responses for each prompt.
  2. The reward model evaluates them based on preference alignment.
  3. The policy is updated to maximize expected reward under a KL-divergence constraint from the previous policy.
  4. The process repeats iteratively, allowing the model to explore and refine behavior.
* **Advantages:**

  + **Active exploration:** The model can dynamically test new strategies and linguistic forms.
  + **Continual learning:** Allows fine-tuning for new domains or evolving user expectations.
  + **Higher alignment fidelity:** Produces nuanced, human-like outputs through iterative reward feedback.
  + **Emergent capabilities:** Encourages spontaneous reasoning and self-improvement beyond static data.
* **Limitations:**

  + **High computational cost:** Requires repeated inference, evaluation, and backpropagation.
  + **Stability challenges:** Susceptible to reward hacking, over-optimization, or collapse without strong KL constraints.
  + **Reward model dependency:** Quality depends heavily on the accuracy and bias of the reward model.
  + **Complex pipeline:** Requires coordination between sampling, evaluation, and optimization processes.
* **Examples in Practice:**

  + **InstructGPT** and **ChatGPT**: Train with PPO-based RLHF using human reward models.
  + **Llama 4**: Employs a continuous online RL loop for adaptive tuning with evolving data distributions.

###### Hybrid Approaches: Combining Offline and Online RL

* **Offline Phase:**

  + Initialize the policy with **SFT** or **DPO** for baseline alignment and stability.
* **Online Phase:**

  + Transition to **PPO-based RLHF** or **online DPO** to incorporate adaptive reward feedback.
* **Benefits:**

  + **Stability + Flexibility:** Offline pretraining provides stable foundations; online RL refines adaptivity.
  + **Efficiency:** Reduces sample inefficiency by starting from an already competent policy.
  + **Scalability:** Enables modular training pipelines adaptable to new data and domains.
* This hybrid strategy underpins the modern preference optimization stack for GPT-4, Claude 3, and Llama 4, where iterative, alternating offline and online loops achieve both safety and responsiveness.

##### Comparative Analysis

| **Aspect** | **Online RL** | **Offline RL** |
| --- | --- | --- |
| Data Source | Generated in real time via interaction with environment or reward model | Fixed dataset of past experiences |
| Exploration | Active — generates novel responses | Passive — limited to existing samples |
| Adaptivity | Dynamic, continuously updated | Static, fixed during training |
| Stability | Prone to instability; requires KL regularization | Stable and reproducible |
| Cost | High — repeated inference, sampling, and evaluation | Low — efficient batch training |
| Reward Dependence | Strong (reward model critical for success) | Optional — uses preference pairs directly |
| Sample Efficiency | Lower (requires many rollouts) | Higher (reuses data fully) |
| Risk of Overfitting | Low — dynamic sampling diversifies data | Higher — risk from fixed dataset |
| Scalability | Limited by compute and latency | Easily parallelizable |
| Examples | PPO (InstructGPT, ChatGPT, Llama 4) | DPO, SFT, Reward Model Pretraining |
| Best Used For | Fine-tuning and adaptive alignment | Baseline alignment and safe pretraining |

##### Intuitive Analogy

* **Offline RL** is like a student studying from a fixed textbook — learning efficiently from known examples but unable to ask new questions.
* **Online RL** is like a student in an interactive class — they can ask questions, receive feedback, and adjust their understanding dynamically.
* The best systems — like hybrid RLHF pipelines — combine both: first learning the textbook thoroughly, then refining understanding through interactive dialogue with a teacher.

##### REINFORCE

###### Overview

* REINFORCE, introduced by [Williams (1992)](https://www-anw.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf), is one of the earliest and simplest policy gradient algorithms, introduced by Williams (1992). It directly optimizes a parameterized policy \(\pi\_\theta(a \mid s)\) by estimating the gradient of the expected return with respect to the policy parameters. The update rule is:

\[\nabla\_\theta J(\theta) = \mathbb{E}\_{s, a \sim \pi\_\theta} [ \nabla\_\theta \log \pi\_\theta(a \mid s) , (R - b) ]\]

* where:
  + \(R\) is the total return (sum of discounted rewards),
  + \(b\) is a baseline (e.g., a value function) to reduce variance.
* A detailed discourse on REINFORCE can be obtained in the [REINFORCE Algorithm](#the-reinforce-algorithm) section.

###### Online vs. Offline (On-Policy vs. Off-Policy)

* REINFORCE is a **fully online**, **on-policy** algorithm.
* **Why It’s Online:**

  + REINFORCE requires **continuous interaction with the environment** to collect fresh trajectories under the current policy \(\pi\_\theta\).
  + After each gradient update, the policy changes, and therefore **new rollouts must be sampled** to reflect this updated policy behavior.
  + The training loop alternates between:
    1. **Collecting trajectories** using \(\pi\_\theta\),
    2. **Computing returns** (discounted cumulative rewards), and
    3. **Updating parameters** using those returns as the learning signal.
  + This direct feedback loop makes REINFORCE inherently **online**, since learning and data generation occur simultaneously.
  + There is **no fixed dataset** or static buffer — the model learns only from its most recent interactions.
* **Why It’s On-Policy:**

  + The REINFORCE gradient estimate \(\nabla\_\theta J(\theta) = \mathbb{E}\_{s, a \sim \pi\_\theta} [\nabla\_\theta \log \pi\_\theta(a \mid s) (R - b)]\) explicitly depends on samples drawn from the **same policy** \(\pi\_\theta\) being optimized.
  + Because of this dependency, trajectories generated under older versions of the policy \(\pi\_{\theta\_\text{old}}\) **cannot be reused**, as their action probabilities differ from those of the updated policy.
  + There is **no correction term** such as an importance ratio \(\frac{\pi\_\theta(a \mid s)}{\pi\_{\text{old}}(a \mid s)}\) to account for this mismatch.
  + Reusing old trajectories would therefore produce a **biased gradient estimate**, leading the optimizer to update toward the wrong objective.

###### Takeaways

| **Aspect** | **REINFORCE** |
| --- | --- |
| Policy Type | On-policy |
| Data Source | Trajectories from the current policy |
| Reuse of Data | Not possible |
| Stability | High variance, unstable without baselines or variance reduction |
| Motivation for Successors | TRPO and PPO were developed to improve REINFORCE’s stability and sample efficiency |

##### Trust Region Policy Optimization (TRPO)

###### Overview

* Trust Region Policy Optimization (TRPO), introduced by [Schulman et al. (2015)](https://arxiv.org/abs/1502.05477), was designed to improve upon REINFORCE and vanilla policy gradient methods by ensuring more **stable and monotonic policy improvement**.
* It does this by constraining each policy update within a “trust region,” preventing large, destabilizing parameter shifts. The optimization problem is:

  \[\max\_{\theta} \mathbb{E}\_{s, a \sim \pi\_}\theta\_\text{old}}} \left[ \frac{\pi\_{\theta}(a \mid s)}{\pi\_{\theta\_\text{old}}(a \mid s)} \hat{A}^{\pi\_{\theta\_\text{old}}}(s, a) \right]\]
  + … subject to:

    \[D\_{KL}(\pi\_{\theta\_\text{old}} \mid \mid \pi\_\theta) \leq \delta\]
    - where the KL constraint limits how far the new policy may deviate from the old one.
* A detailed discourse on TRPO can be obtained in the [Trust Region Policy Optimization (TRPO)](#trust-region-policy-optimization-trpo) section.

###### Online vs. Offline (On-Policy vs. Off-Policy)

* REINFORCE is a **fully online**, **on-policy** algorithm.
* **Why It’s Online:**

  + The policy must actively **interact with the environment** to collect trajectories under the **current policy parameters** \(\pi\_\theta\).
  + After every update, the parameters change — meaning the distribution over states and actions changes as well.
  + Consequently, the algorithm must **collect fresh rollouts** from the environment after each update to ensure that gradient estimates remain valid.
  + There is no mechanism to reuse old data, since the return \(R\) depends on trajectories generated specifically under the current policy.
* **Why It’s On-Policy:**

  + The gradient estimate in REINFORCE is derived under the assumption that all samples are drawn from the **same policy** \(\pi\_\theta\) being optimized.
  + If trajectories from a previous policy were used, the gradient would become **biased**, because the sampling distribution no longer matches the current policy’s distribution.
  + Unlike TRPO or PPO, REINFORCE does **not** include any policy ratio \(\frac{\pi\_\theta}{\pi\_{\text{old}}}\) to correct for this mismatch.
  + Therefore, the algorithm must discard old trajectories and **re-sample from the current policy** at every iteration.
  + Thus, REINFORCE operates as a strictly **on-policy, online learning method**, relying entirely on newly generated data at each step of training.
* **Why It’s Not Off-Policy:**

  + Off-policy algorithms (like Q-learning, DDPG, or SAC) can train on data collected by *any* behavior policy, often stored in a replay buffer.
  + REINFORCE cannot do this because:

    - It lacks an importance weighting term to reweight samples from an alternative distribution.
    - Its objective depends directly on log-likelihoods under the **current policy**, not a past or external one.
    - Using off-policy data would result in incorrect gradient estimates, leading to divergence or sub-optimal policies.
  + Therefore, REINFORCE is a **purely on-policy** method — data from older policies is always discarded after each update.

###### Takeaways

| **Aspect** | **TRPO** |
| --- | --- |
| Policy Type | On-policy |
| Data Source | Trajectories from the current (old) policy |
| Reuse of Data | None; requires new rollouts per update |
| Role of Policy Ratio | Corrects for minor distribution shift within one update |
| Constraint | KL-divergence trust region |
| Stability | Much higher than REINFORCE, with guaranteed monotonic improvement under certain assumptions |

##### Proximal Policy Optimization (PPO)

###### Overview

* Proximal Policy Optimization (PPO), proposed by [Schulman et al. (2017)](https://arxiv.org/abs/1707.06347), is a simplified and more practical variant of TRPO. It maintains TRPO’s core idea of constraining policy updates but replaces the complex constrained optimization with a **clipped surrogate objective** that is easier to implement and compute.
* The PPO objective is:

\[L^{\text{CLIP}}(\theta) =
\mathbb{E}\_{t}\left[
\min\left(
r\_t(\theta) \hat{A\_t},
\,\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A\_t}
\right)
\right]\]

* where:
  + \(r\_t(\theta) = \frac{\pi\_{\theta}(a\_t \mid s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t \mid s\_t)}\) is the policy ratio.
  + \(\hat{A\_t}\) is the advantage estimate.
  + \(\epsilon\) is a small clipping parameter (e.g., 0.1–0.3) that prevents the ratio from moving too far away from 1.
* A detailed discourse on PPO can be obtained in the [Proximal Policy Optimization (PPO)](#proximal-policy-optimization-ppo-1) section.

###### Online vs. Offline (On-Policy vs. Off-Policy)

* PPO is a **fully online, on-policy** algorithm.
* **Why It’s Online:**

  + PPO learns directly from **interactions with the environment**.
  + During each policy update, the model collects **fresh trajectories** (state–action–reward sequences) using the most recent version of the policy \(\pi\_{\theta\_{\text{old}}}\).
  + After computing the advantage estimates and performing several epochs of optimization on this batch, the old data are **discarded**, and the environment is **rolled out again** using the updated policy \(\pi\_\theta\).
  + This iterative sampling process ensures that PPO continuously explores and learns from **up-to-date behavior data**, rather than relying on static or historical samples.
* **Why It’s On-Policy:**

  + PPO’s gradient updates depend on trajectories drawn from the **same policy (or a very recent one)** being optimized.
  + The presence of the policy ratio \(r\_t(\theta) = \frac{\pi\_\theta(a\_t \mid s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t \mid s\_t)}\) may seem reminiscent of off-policy correction, but in PPO it only compensates for **small distribution shifts** between successive policies — not for large mismatches that would occur if reusing old or off-policy data.
  + Because of this, PPO cannot safely reuse data from past iterations or other policies. Reusing old trajectories would bias the gradient, since the expectation \(\mathbb{E}\_{s,a \sim \pi\_\theta}\) would no longer reflect the distribution under the current policy.
  + Thus, PPO maintains the key property of being **on-policy**, updating the model only with samples that accurately represent the behavior of the current (or just-previous) policy.

###### Why PPO Is Still On-Policy

* The clipping mechanism only allows small policy updates (similarly to TRPO’s trust region), which means \(\pi\_{\theta}\) stays close to \(\pi\_{\theta\_\text{old}}\).
* The ratio term \(r\_t(\theta)\) corrects for **slight distributional differences** between successive policies within an update, but it does not support learning from data generated by unrelated or much older policies.
* Hence, PPO cannot reuse large offline datasets or a replay buffer, as that would violate the assumption that samples are representative of the current policy’s behavior.

###### Why It’s Sometimes Confused with Off-Policy Methods

* PPO can perform **multiple epochs** of optimization on the *same batch* of on-policy data, which gives the impression of reusing samples.
* However, this reuse happens only within the same policy iteration and remains valid because the data still originate from \(\pi\_{\theta\_\text{old}}\).

###### Takeways

| **Aspect** | **PPO** |
| --- | --- |
| Policy Type | On-policy |
| Data Source | Trajectories from the current (old) policy |
| Data Reuse | Limited (within one batch only) |
| Ratio Role | Corrects for minor distribution shift within a single update |
| Update Constraint | Implicit via clipping, not explicit KL bound |
| Practical Advantage | Simpler, stable, and widely used in LLM and RLHF training |

##### Direct Preference Optimization (DPO)

###### Overview

* Direct Preference Optimization (DPO), introduced by [Rafailov et al. (2023)](https://arxiv.org/abs/2305.18290), is a method designed for **fine-tuning LLMs** directly from human preference data.
* Unlike RLHF methods such as PPO-based training, DPO does not require an explicit reward model or reinforcement learning loop. Instead, it formulates a **closed-form objective** that aligns the model’s output probabilities with human preferences.
* The DPO objective can be written as:

\[L\_{\text{DPO}}(\theta)
= -\mathbb{E}\_{(x, y^+, y^-) \sim \mathcal{D}}
\left[
\log \sigma \left(
\beta \left(
\log \frac{\pi\_\theta(y^+ \mid x)}{\pi\_{\text{ref}}(y^+ \mid x)} -
\log \frac{\pi\_\theta(y^- \mid x)}{\pi\_{\text{ref}}(y^- \mid x)}
\right)
\right)
\right]\]

* where:

  + \((x, y^+, y^-)\) are prompt–preferred–dispreferred triples from preference data,
  + \(\pi\_{\text{ref}}\) is the reference model (often the supervised fine-tuned model, SFT),
  + \(\beta\) is a temperature-like scaling parameter.
* A detailed discourse on DPO can be obtained in the [Direct Preference Optimization (DPO)](#direct-preference-optimization-dpo-1) section.

###### Online vs. Offline (On-Policy vs. Off-Policy)

* DPO is a **fully offline**, **off-policy** alignment method.
* **Why It’s Offline:**

  + DPO trains entirely on a **fixed dataset** of human preferences — consisting of prompt–response pairs labeled as *preferred* (\(y^+\)) or *dispreferred* (\(y^-\)).
  + These datasets are collected **prior to optimization**, typically using human annotators or preference models (e.g., from the Anthropic HH dataset or OpenAI’s RLHF pipeline).
  + During training, the model computes gradients over this static dataset — there is **no environment interaction** or dynamic sampling from the current model \(\pi\_\theta\).
  + All optimization steps are performed offline using pre-existing pairs, without requiring rollouts or iterative feedback.
* **Why It’s Off-Policy:**

  + The model being trained, \(\pi\_\theta\), **does not generate the samples** used in training — they come from a **reference model** \(\pi\_{\text{ref}}\) (often the supervised fine-tuned model, SFT).
  + The DPO loss includes a **policy ratio**, \(\log \frac{\pi\_\theta(y \mid x)}{\pi\_{\text{ref}}(y \mid x)}\), which serves as a **reweighting factor** to correct for the distributional shift between the new model and the reference model.
  + This ratio ensures that optimization remains unbiased even though the data are drawn from a different distribution — a mechanism similar to **importance sampling** in reinforcement learning.
  + Because DPO never samples new data from the current policy, it operates purely **off-policy** — all learning happens with respect to static preference data.

###### Comparison to PPO/RLHF

* In PPO-based RLHF, the model learns from **online rollouts** — each policy update collects new samples.
* In contrast, DPO optimizes a **deterministic preference objective** directly over existing data, without sampling new trajectories.
* This makes DPO far more efficient and simpler, but potentially less adaptive, since it can’t explore new regions of the output space beyond what’s in the dataset.

###### Takeaways

| **Aspect** | **DPO** |
| --- | --- |
| Policy Type | Off-policy (offline) |
| Data Source | Fixed human preference dataset |
| Data Reuse | Full reuse possible |
| Ratio Role | Reweights model likelihoods relative to reference model |
| Environment Interaction | None (purely offline) |
| Advantage | No reward model or rollout generation required |

##### Kahneman–Tversky Optimization (KTO)

###### Overview

* Kahneman–Tversky Optimization (KTO), proposed by [Ethayarajh et al. (2024)](https://arxiv.org/abs/2402.01306), inspired by *prospect theory* from behavioral economics.
* Instead of maximizing log-likelihoods of preferences (as DPO does), KTO directly **maximizes the subjective human utility** of model generations under the *Kahneman–Tversky value function* — a nonlinear, asymmetric function reflecting human biases such as **risk aversion** and **loss aversion**.
* The KTO objective is derived as a **Human-Aware Loss (HALO)**, a family of alignment objectives that incorporate human-like value functions.
* The canonical loss function is:

  \[L\_{\text{KTO}}(\pi\_\theta, \pi\_{\text{ref}}) = \mathbb{E}\_{x, y \sim \mathcal{D}}[\lambda\_y - v(x, y)]\]
  + where \(v(x, y)\) is a *Kahneman–Tversky-like* value function that depends on:
    - \(r\_\phi(x, y) = \log \frac{\pi\_\theta(y \mid x)}{\pi\_{\text{ref}}(y \mid x)}\),
    - a **reference point** \(z\_0 = KL(\pi\_\theta \mid \pi\_{\text{ref}})\),
    - and asymmetric coefficients \(\lambda\_D, \lambda\_U\) for desirable vs. undesirable samples.
* KTO replaces the power-law utility curve from prospect theory with a **logistic function**, stabilizing training while preserving its concavity (risk aversion in gains) and convexity (risk seeking in losses).
* A detailed discourse on KTO can be obtained in the [Kahneman-Tversky Optimization (KTO)](#kahneman-tversky-optimization-kto) section.

###### Online vs. Offline (On-Policy vs. Off-Policy)

* KTO is a **fully offline**, **off-policy** method.
* **Why It’s Offline**:

  + KTO does **not require any interactive rollouts or online sampling**. Instead, it trains entirely from a **fixed dataset** of labeled examples (each labeled “desirable” vs. “undesirable”) drawn from human annotations or derived feedback.
  + Because no new model outputs or environment interactions are needed during training, KTO is compatible with settings where data collection is costly or infeasible.
  + The entire optimization is performed on **static data**, making the training process reproducible and deterministic.
  + This offline nature distinguishes KTO from RL-based policies that require new sample generation at each step.
* **Why It’s Off-Policy**:

  + The samples used for training KTO are **not generated by the policy being optimized**, \(\pi\_\theta\). Rather, they come from another model or human annotation procedure, often via a **reference distribution** \(\pi\_{\text{ref}}\).
  + KTO incorporates a **policy ratio** \(r\_\phi(y \mid x) = \frac{\pi\_\theta(y \mid x)}{\pi\_{\text{ref}}(y \mid x)}\) to **reweight** examples according to how the new policy diverges from the reference. This ratio functions as a **distribution-shift correction factor** (akin to importance sampling) in the offline setting.
  + Because the policy never actually generates the samples it trains on, KTO is classified as **off-policy** — it learns from data produced by another distribution or past policy.
* Thus, KTO operates much like DPO — both are **offline alignment algorithms**, but KTO learns from *binary signals* rather than *pairwise preferences*.

###### Takeaways

| **Aspect** | **KTO** |
| --- | --- |
| Policy Type | Off-policy (offline) |
| Data Source | Fixed binary feedback dataset (desirable vs. undesirable) |
| Data Reuse | Full reuse possible |
| Ratio Role | Reweights model likelihoods relative to reference policy using a prospect-theoretic value function |
| Environment Interaction | None (purely offline) |
| Advantage | Human-aware utility maximization without a reward model or rollouts; captures loss/risk aversion |

##### Group Relative Policy Optimization (GRPO)

###### Overview

* **Group Relative Policy Optimization (GRPO)** is a reinforcement learning algorithm introduced by the DeepSeek-AI team in [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) by Shao et al. (2024).
  It is designed as a **lightweight and memory-efficient variant of PPO (Proximal Policy Optimization)** that removes the need for a separate **critic (value) network**, thereby simplifying the training pipeline and reducing computational cost.
* The main idea is to estimate the **baseline** not with a learned value model but **from relative group scores** of multiple sampled outputs. This allows GRPO to leverage *intra-group comparison* instead of value function estimation, aligning well with how **reward models** are typically trained on *relative preference data* (e.g., “A is better than B”).
* In PPO, the objective function is:

  \[J\_{\text{PPO}}(\theta)
  = \mathbb{E}\left[
  \min\left(
  r\_t(\theta)\hat{A\_t},
  \,\text{clip}(r\_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A\_t}
  \right)\right]\]
  + where \(r\_t(\theta) = \frac{\pi\_\theta(a\_t \mid s\_t)}{\pi\_{\text{old}}(a\_t \mid s\_t)}\) is the **policy ratio** and \(\hat{A\_t}\) is the advantage estimated using a critic.
* In GRPO, the **critic is replaced by group-based normalization**. For each question \(q\), a *group of outputs* \({o\_1, \ldots, o\_G}\) is sampled from the old policy \(\pi\_{\theta\_{\text{old}}}\). Rewards are assigned to each output by a reward model, and their normalized difference defines the **group-relative advantage**:

\[\hat{A}\_i = \frac{r\_i - \text{mean}(r)}{\text{std}(r)}\]

* The GRPO objective is then:

  \[J\_{\text{GRPO}}(\theta)
  = \mathbb{E}\left[
  \frac{1}{G}\sum\_i
  \frac{1}{ \mid o\_i \mid }
  \sum\_t
  \min\left(
  r\_{i,t}(\theta)\hat{A}\_{i,t},
  \,\text{clip}(r\_{i,t}(\theta), 1-\epsilon, 1+\epsilon)\hat{A}\_{i,t}
  \right) -
  \beta D\_{\text{KL}}[\pi\_\theta \mid\mid \pi\_{\text{ref}}]
  \right]\]
  + where the **KL divergence** term regularizes the new policy against a reference model (typically the SFT model).
* The following figure from the paper demonstrates PPO and GRPO. GRPO foregoes the value/critic model, instead estimating the baseline from group scores, significantly reducing training resources.

* A detailed discourse on GRPO can be obtained in the [Group Relative Policy Optimization (GRPO)](#group-relative-policy-optimization-grpo-1) section.

###### Online vs. Offline (On-Policy vs. Off-Policy)

* GRPO is an **on-policy**, **online** reinforcement learning method.
* **Why It’s Online:**

  + GRPO operates through **iterative reinforcement learning updates**, where the model continuously interacts with its environment or task distribution to collect new samples.
  + At each iteration, **new rollouts** (model-generated responses) are produced from the current or recent policy \(\pi\_{\theta\_{\text{old}}}\).
  + These responses are grouped per prompt (e.g., multiple sampled outputs for the same question), scored by a **reward model**, and then used to update the new policy \(\pi\_\theta\).
  + Because GRPO depends on these fresh generations to estimate group-relative advantages, the algorithm inherently requires **online interaction** — it cannot rely solely on static data.
* **Why It’s On-Policy:**

  + GRPO updates the policy using trajectories sampled **directly from the current policy** (or a very recent version of it).
  + The ratio \(\frac{\pi\_\theta(a \mid s)}{\pi\_{\theta\_{\text{old}}}(a \mid s)}\) is computed within each update step, correcting for only the *small distribution shift* between successive policies.
  + Old data cannot be reused indefinitely, because the group-relative normalization and clipped objective assume **statistical proximity** between \(\pi\_{\theta\_{\text{old}}}\) and \(\pi\_\theta\).
  + GRPO also periodically refreshes both its **policy** and **reward model** through newly collected generations, ensuring continual alignment with the most recent policy behavior.
* Thus, GRPO belongs firmly to the **online (on-policy RL)** family — much like PPO — but distinguishes itself through its **group-based normalization**, which removes the need for a critic network while maintaining stability and efficiency.

###### Takeaways

| **Property** | **GRPO** |
| --- | --- |
| Policy Type | On-policy (online) |
| Baseline | Group-average reward (no critic) |
| Data Source | New samples from current policy |
| KL Regularization | Explicit penalty term |
| Reward Signal | Outcome or process-based reward models |
| Compute Efficiency | High (no value model) |
| Alignment Domain | Mathematical reasoning (generalizable) |

##### Comparative Analysis: REINFORCE, TRPO, PPO, DPO, KTO, GRPO

* The table below contrasts the algorithms on **policy type (online/on-policy vs. offline/off-policy)**, **what data they train on**, **how they handle distribution shift (ratio/reweighting)**, **their stability constraint (KL / clipping / none)**, and **why they fall into the online/offline bucket**.

| **Method** | **Policy Type** | **Trains On (Data Source)** | **Distribution-Shift Term** | **Stability / Regularization** | **Why Online vs. Offline** |
| --- | --- | --- | --- | --- | --- |
| **REINFORCE** | **On-policy (online)** | Fresh rollouts from current policy (\(\pi\_\theta\)) | None (uses \(\nabla \log \pi\_\theta\)) | Baselines (optional) for variance | Needs trajectories sampled under the **current** policy each update; old data would bias the gradient. |
| **TRPO** | **On-policy (online)** | Rollouts from (\(\pi\_{\theta\_\text{old}}\)) per iteration | Policy ratio (\(r=\frac{\pi\_\theta}{\pi\_{\theta\_\text{old}}}\)) | **Hard trust region** via KL constraint | Requires **new** trajectories after each update; ratio only corrects the **small** shift within an iteration, not replay from old policies. |
| **PPO** | **On-policy (online)** | Rollouts from (\(\pi\_{\theta\_\text{old}}\)); reused for a few epochs | Policy ratio (\(r=\frac{\pi\_\theta}{\pi\_{\theta\_\text{old}}}\)) | **Clipping** of policy ratio (\(r\)) (and often a KL bonus) | Still needs **fresh** batches every iteration; clipping assumes small policy drift, not arbitrary offline reuse. |
| **DPO** | **Off-policy (offline)** | Fixed **pre-collected preferences** (x, \(y^+\), \(y^-\)) | Reference-relative log-ratio (\(\log\frac{\pi\_\theta}{\pi\_{\text{ref}}}\)) inside a logistic margin | Implicit via temperature (\(\beta\)) (reference anchoring) | Optimizes a **closed-form** objective over a static dataset; no environment rollouts. |
| **KTO** | **Off-policy (offline)** | Fixed **binary feedback** (desirable vs. undesirable) | Reference-relative log-ratio (\(r\_\theta=\log\frac{\pi\_\theta}{\pi\_{\text{ref}}}\)) with a **reference point** (\(z\_0\)) | Prospect-theoretic **value function** (logistic), acts like a KL-anchored utility; no rollouts | Trains entirely on static labeled data; maximizes **human utility** under a HALO objective; no online sampling. |
| **GRPO** | **On-policy (online)** | **New groups** of samples per prompt from (\(\pi\_{\theta\_\text{old}}\)) | Policy ratio at token level (PPO-style); **group-relative** advantages | **Explicit KL penalty** vs. reference; **no critic** (baseline = group mean) | Requires **sampling groups** each step and uses reward-model scores; on-policy RL with reduced memory (critic-free). |

* **Takeways**:

  + **DPO vs. KTO (both offline):** DPO maximizes a **preference likelihood margin** against a reference model; KTO maximizes a **prospect-theoretic utility** using a logistic value function with a **reference point** (z\_0). Both use ratios against \(\pi\_{\text{ref}}\) as **reweighting factors** and train without rollouts.
  + **GRPO vs. PPO (both online):** GRPO removes the **critic/value model** and computes **group-relative advantages** from multiple sampled outputs for the same prompt, plus an explicit KL penalty—yielding an **actor-only**, memory-efficient PPO variant. Iterative GRPO can also **refresh the reward model** and reference policy during training.

## Proximal Policy Optimization (PPO)

* Proximal Policy Optimization (PPO), introduced by [Schulman et al. (2017)](https://arxiv.org/abs/1707.06347), is an RL algorithm that addresses some key challenges in training agents through policy gradient methods.
* PPO is widely used in robotics, gaming, and LLM policy optimization, particularly in [RLHF](#reinforcement-learning-from-human-feedback-rlhf).
* [PPO for LLMs: A Guide for Normal People](https://cameronrwolfe.substack.com/p/ppo-llm) by [Cameron Wolfe](https://www.linkedin.com/in/cameron-r-wolfe-ph-d-04744a238/) offers a complementary discourse on PPO, beyond the aspects covered in this primer.

#### Background

##### Terminology: RL Overview

* RL is a framework for training agents that interact with an environment to maximize cumulative rewards.

  + **Agent:** Learns to act in an environment.
  + **Environment:** Defines state transitions and rewards.
  + **State (\(s\)):** The agent’s perception of the environment at a given time.
  + **Action (\(a\)):** The agent’s choice affecting the environment.
  + **Reward (\(r\)):** A scalar feedback signal.
  + **Policy (\(\pi(a\mid s)\)):** A probability distribution over actions given a state.
  + **Value Function (\(V^{\pi}(s)\)):** Expected cumulative rewards from state \(s\) when following policy \(\pi\).
  + **Advantage Function (\(\hat{A}^{\pi}(s, a)\)):** Measures how much better an action is compared to the expected baseline value.
* RL problems are modeled as Markov Decision Processes (MDPs) with:

  + States (\(S\))
  + Actions (\(A\))
  + Transition probabilities (\(P(s'\mid s, a)\))
  + Rewards (\(R(s, a)\))
  + Discount factor (\(\gamma\)) for future rewards

###### States and Actions in LLM Context

* In the LLM context, states and actions are defined at the token level.
* Suppose we give our LLM a prompt \(p\). The LLM then generates a response \(r\_i\) of length \(T\), one token at a time:

  + \(t=0\): state is the prompt, \(s\_0 = {p}\); first action \(a\_0\) is the first token generated.
  + \(t=1\): state becomes \(s\_1 = {p, a\_0}\), and the next action \(a\_1\) is generated conditioned on that state.
  + \(t=T-1\): state is \(s\_{T-1} = {p, a\_{0:T-2}}\), and the final token \(a\_{T-1}\) is produced.

##### Policy-Based vs. Value-Based Methods vs. Actor-Critic Methods

* Reinforcement learning algorithms can be broadly grouped into **value-based**, **policy-based**, and **actor-critic** methods. Each family approaches the problem of learning optimal behavior differently, with varying trade-offs in bias, variance, and sample efficiency.
* **Value-Based Methods**:

  + These methods focus on learning **value functions** that estimate the expected cumulative reward for a given state or state–action pair.
    The agent then **implicitly derives a policy** by selecting the action that maximizes this estimated value.

    - **Core idea:** Learn \(Q^{\pi}(s, a) = \mathbb{E}[R\_t \mid s\_t = s, a\_t = a]\) and choose actions \(a = \arg\max\_a Q(s, a)\).
    - **Typical applications:** Environments with **discrete** and **well-defined** action spaces.
    - **Advantages:** **Sample-efficient**, conceptually simple, and does not require explicit policy parameterization.
    - **Limitations:** **Hard to scale to continuous actions**; unstable when deep neural networks are used for approximation.
    - **Major algorithms:**

      * **Q-Learning (Quality Learning):** Foundational algorithm using tabular updates.
      * **SARSA (State–Action–Reward–State–Action):** On-policy version of Q-learning.
      * **DQN (Deep Q-Network):** Combines Q-learning with deep neural networks for high-dimensional input (e.g., pixels).
      * **Double DQN (Double Deep Q-Network)** and **Dueling DQN (Dueling Deep Q-Network):** Address overestimation bias and improve learning stability.
* **Policy-Based Methods**:

  + Policy-based methods directly learn a **parameterized policy** \(\pi\_\theta(a \mid s)\) rather than deriving it from a value function.
  + The goal is to find parameters \(\theta\) that maximize the expected cumulative reward:\[J(\theta) = \mathbb{E}\_{\tau \sim \pi\_\theta}[R(\tau)]\]
  + These methods work well for **continuous**, **stochastic**, and **high-dimensional** action spaces because the policy is explicitly modeled as a probability distribution.
  + **Advantages:** Smooth policy updates, natural handling of continuous actions, and explicit stochastic exploration.
  + **Limitations:** High variance in gradient estimates; often require many samples for stable convergence.
  + **Major algorithms:**

    - **REINFORCE (Monte Carlo Policy Gradient):** The simplest policy gradient algorithm, using episode-level returns.
    - **DPG (Deterministic Policy Gradient):** Extends policy gradients to deterministic policies for continuous control.
    - **DDPG (Deep Deterministic Policy Gradient):** Combines DPG with deep neural networks for scalable continuous control.
    - **SAC (Soft Actor-Critic):** Adds entropy regularization to encourage exploration and improve robustness.
    - **DPO (Direct Preference Optimization):** A purely policy-based method that aligns model outputs directly with human preferences by optimizing preference log-ratios, without using rewards or a value function.
    - **GRPO (Group Relative Policy Optimization):** A policy gradient method inspired by PPO that removes the critic and computes relative advantages across grouped samples, improving efficiency in large language model fine-tuning.
  + **Policy Gradient Methods:**

    - Subset of policy-based methods that explicitly compute the gradient of the expected return with respect to policy parameters and perform gradient ascent to improve the policy.
    - This principle is formalized in the **Policy Gradient Theorem**, which provides a mathematical foundation for computing gradients of the expected reward with respect to policy parameters without requiring knowledge of the environment’s dynamics.
    - It shows that the policy gradient can be estimated as an expectation over actions sampled from the current policy, weighted by the **advantage function**, which quantifies how much better or worse an action performs compared to the average.
    - For a detailed discourse on the policy gradient theorem, refer to the [Policy Gradient Theorem](#policy-gradient-theorem) section.\[\nabla\_{\theta} J(\theta) = \mathbb{E}\_{\pi\_\theta} \left[ \nabla\_{\theta} \log \pi\_\theta(a \mid s) \hat{A}^{\pi}(s, a) \right]\]
    - The gradient increases the likelihood of actions with **positive advantages** and decreases it for **negative advantages**.
    - **Representative algorithms:**

      * **REINFORCE (Monte Carlo Policy Gradient)**: Baseline Monte Carlo gradient estimation.
      * **TRPO (Trust Region Policy Optimization)**: Constrains policy updates to prevent large, destabilizing steps.
      * **PPO (Proximal Policy Optimization)**: A policy gradient–based actor-critic algorithm that uses a clipped objective to limit policy divergence for stable learning.
      * **NPG (Natural Policy Gradient)**: Uses the Fisher information matrix for more geometrically informed updates.
      * **GRPO (Group Relative Policy Optimization)**: PPO-inspired policy gradient method that eliminates the value network, using group-relative baselines instead.
* **Actor-Critic Methods**:

  + Actor-Critic algorithms **combine both value-based and policy-based ideas**, forming a hybrid architecture.
  + The **actor** directly learns the policy \(\pi\_\theta(a\mid s)\) — determining which actions to take (policy-based component).
  + The **critic** learns a value function \(V^{\pi}(s)\) or \(Q^{\pi}(s, a)\) — estimating how good those actions are (value-based component).
  + The critic provides feedback to the actor by computing the **advantage function**
    \(\hat{A}^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s),\)
    which stabilizes learning and reduces variance in the policy gradient.
  + Actor-Critic methods therefore sit **between** policy-based and value-based RL — not orthogonal to them, but rather an integration of both.
    They inherit the flexibility of policy-based optimization and the efficiency of value-based bootstrapping.
  + **Advantages:**

    - Reduced variance in gradient estimates.
    - Improved stability and sample efficiency.
    - Balanced bias–variance trade-off through combined learning.
  + **Limitations:**

    - More complex architecture requiring two interacting networks.
    - Susceptible to instability if the critic’s value estimates are inaccurate.
  + **Major algorithms:**

    - **A2C (Advantage Actor-Critic):** Uses synchronous updates where multiple environments run in parallel to gather experience. The “Advantage” term refers to using \(\hat{A}(s, a) = Q(s, a) - V(s)\) to measure how much better an action is than the baseline value, improving training stability.
    - **A3C (Asynchronous Advantage Actor-Critic):** Extends A2C by running multiple agents asynchronously on different threads or devices. The “Asynchronous Advantage” setup ensures decorrelated experiences and faster convergence by aggregating gradients from independent workers before updating shared parameters.
    - **DDPG (Deep Deterministic Policy Gradient):** Deterministic actor-critic variant for continuous action spaces.
    - **SAC (Soft Actor-Critic):** Actor-critic algorithm with entropy regularization for robust exploration.
    - **PPO:** A policy gradient–based actor-critic algorithm that uses clipped surrogate objectives to limit policy divergence.

###### Comparative Analysis

| **Method Type** | **Learns Value Function?** | **Learns Policy Directly?** | **Core Learning Signal** | **Exploration Mechanism** | **Action Space Suitability** | **Bias–Variance Profile** | **Sample Efficiency** | **Representative Algorithms** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Value-Based | ✅ | ❌ | Temporal-Difference (TD) Error | ε-greedy or Boltzmann exploration | Best for discrete actions | Low bias, high variance | ✅ High (reuses data via bootstrapping) | Q-Learning, SARSA, DQN, Double DQN |
| Policy-Based | ❌ | ✅ | Policy Gradient (\(\nabla\_\theta \log \pi\)) | Intrinsic stochasticity in \(\pi(a|s)\) | Excellent for continuous or stochastic actions | Low variance, potentially high bias | ❌ Lower (requires many trajectories) | REINFORCE, TRPO, PPO, DDPG, SAC, **DPO**, **GRPO** |
| Actor-Critic | ✅ | ✅ | Policy Gradient + TD Value Estimates | Stochastic or deterministic policies guided by critic | Works for both discrete and continuous | Balanced bias–variance | ✅ Moderate to high (critic improves sample reuse) | A2C, A3C, DDPG, SAC, PPO, **GRPO** |

###### Takeaways

* **Value-Based** methods estimate *what* is good (the value).
* **Policy-Based** methods directly learn *how to act*.
* **Actor-Critic** methods do **both simultaneously**, leveraging value estimation to guide efficient and stable policy optimization — a principle that underlies modern algorithms like **PPO**, **DPO**, and **GRPO**.

##### Policy Gradient Theorem

* The objective in policy optimization is to maximize the expected return:

  \[J(\theta) = \mathbb{E}\_{\tau \sim \pi\_{\theta}} [ R(\tau) ]\]
  + where \(R(\tau) = \sum\_{t=0}^T \gamma^t r\_t\) is the discounted cumulative reward along a trajectory.
* The **policy gradient theorem** provides a way to compute the gradient of this expectation without differentiating through the environment’s dynamics:

\[\nabla\_{\theta} J(\theta) = \mathbb{E}\_{\pi\_{\theta}} \left[ \nabla\_{\theta} \log \pi\_{\theta}(a\mid s) \hat{A}^{\pi}(s, a) \right]\]

* This expression forms the basis of all policy gradient methods and thus underpins algorithms like REINFORCE, TRPO, and PPO.
* **Interpretation:** The gradient term \(\nabla\_\theta \log \pi\_\theta(a\mid s)\) shows how to adjust parameters to increase the likelihood of beneficial actions. The advantage \(\hat{A}^{\pi}(s, a)\) weights these updates by how good each action turned out relative to the baseline.
* **Variance Reduction:** To improve stability, a baseline (usually the value function \(V^{\pi}(s)\)) is subtracted from the return, leading to the definition of the advantage function:

  \[A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)\]
  + This reduces gradient variance without introducing bias.
* **Practical Implementation:** Policy gradient methods rely on Monte Carlo rollouts or temporal-difference learning for return estimation. The theorem is foundational for designing algorithms that can operate in complex or continuous environments, where traditional value-based approaches are inefficient.

##### Classification of PPO, DPO, and GRPO

* Building on the distinctions between **value-based**, **policy-based**, and **actor-critic** methods, modern reinforcement learning algorithms such as **PPO**, **DPO**, and **GRPO** represent successive innovations in **policy optimization**.
* While all three focus on **directly improving a policy**, they differ in whether they use a value function (critic), how they estimate advantages, and how they constrain or stabilize policy updates.

###### PPO

* **Classification:**
  + ✅ *Policy-Based Method*
  + ✅ *Policy Gradient Method*
  + ✅ *Actor-Critic Method*
* **Explanation:**
  + **PPO** is one of the most influential **actor-critic** algorithms and a cornerstone of modern **policy gradient methods**. It improves upon earlier methods like **REINFORCE** and **TRPO** by introducing a **clipped surrogate objective** that stabilizes policy updates and prevents overly large gradient steps.
  + **Why Policy-Based:** PPO directly parameterizes and optimizes a stochastic policy \(\pi\_\theta(a\mid s)\), rather than deriving it from a value function.
  + **Why Policy Gradient:** PPO explicitly applies the **policy gradient theorem**, optimizing:

    \[L^{\text{PPO}}(\theta) = \mathbb{E}\left[\min\left(r\_t(\theta)\hat{A\_t},\,\text{clip}(r\_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A\_t}\right)\right]\]
    - where \(r\_t(\theta) = \frac{\pi\_\theta(a\_t\mid s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t\mid s\_t)}\).
  + **Why Actor-Critic:** PPO combines a **policy network (actor)** with a **value network (critic)** that estimates \(V^{\pi\_\theta}(s\_t)\) to compute advantages \(\hat{A\_t} = Q\_t - V\_t\). The critic reduces gradient variance and improves stability.
* **Takeaway:**
  + PPO is a **policy gradient–based actor-critic algorithm** that achieves stable learning through clipped objective functions. It serves as the foundation for many subsequent variants, including GRPO.

###### DPO

* **Classification:**
  + ✅ *Policy-Based Method*
  + ❌ *Not a Policy Gradient Method (in the traditional sense)*
  + ❌ *Not an Actor-Critic Method*
* **Explanation:**
  + **DPO** reformulates reinforcement learning from human feedback (RLHF) into a **supervised preference optimization** problem. Rather than optimizing reward expectations or using a critic, DPO directly learns from **pairwise human preference data**.
  + **Why Policy-Based:**
    - DPO directly optimizes a parameterized policy \(\pi\_\theta(y\mid x)\) using preference pairs \((x, y^{+}, y^{-})\) — preferred and dispreferred responses to the same prompt:\[L\_{DPO}(\pi\_\theta; \pi\_{ref}) = - \mathbb{E}\_{(x, y\_w, y\_l) \sim D} \left[ \log \sigma\left(\beta \log \frac{\pi\_\theta(y\_w \mid x)}{\pi\_{ref}(y\_w \mid x)} - \beta \log \frac{\pi\_\theta(y\_l \mid x)}{\pi\_{ref}(y\_l \mid x)} \right) \right]\]
    - The objective increases the likelihood of preferred responses and decreases that of dispreferred ones.
  + **Why Not a Policy Gradient Algorithm:**
    - Although it resembles policy gradient updates (due to its use of log probabilities), DPO does not compute expectations over environment trajectories or reward-weighted returns. It performs **direct supervised optimization** on preference data, bypassing stochastic reward modeling.
  + **Why Not Actor-Critic:**
    - DPO has no critic or explicit reward model. Its optimization signal derives purely from pairwise human feedback, not from estimated value functions or TD errors.
* **Takeaway:**
  + DPO is a **purely policy-based alignment algorithm** that removes rewards and critics entirely. It bridges reinforcement learning and supervised fine-tuning by optimizing the policy directly with respect to preference data — effectively sidestepping the instability and variance of traditional RL pipelines.

###### GRPO

* **Classification:**
  + ✅ *Policy-Based Method*
  + ✅ *Policy Gradient Method*
  + ❌ *Not a Traditional Actor-Critic Method*
* **Explanation:**
  + **GRPO** extends PPO’s core ideas but removes the **critic network**. Instead, it estimates **relative advantages** among groups of sampled trajectories, using these relative differences as a variance-reducing baseline.
  + **Why Policy-Based:**
    - GRPO optimizes the policy \(\pi\_\theta(a\mid s)\) directly, without any value estimation step. It relies solely on comparative feedback among trajectories.
  + **Why Policy Gradient:**
    - GRPO computes gradients using **group-relative advantages**, following the same principle as PPO but without an explicit value function:

      \[A\_i = r\_i - \frac{1}{G}\sum\_{j=1}^{G} r\_j\]
      * where \(r\_i\) is the reward of sample \(i\) and \(G\) is the group size.
    - This *group-average baseline* functions like a self-normalizing critic, stabilizing updates.
  + **Why Not Actor-Critic:**
    - Although inspired by PPO, GRPO **completely removes the critic**, relying on intra-group comparisons to measure advantage rather than predicted values.
* **Takeaway:**
  + GRPO is a **critic-free policy gradient variant of PPO**, tailored for efficient preference-based and reinforcement learning with LLMs. It preserves PPO’s update stability while simplifying training through relative advantage estimation.

###### Summary Comparison: PPO vs. DPO vs. GRPO

| **Algorithm** | **Policy-Based** | **Policy Gradient** | **Actor-Critic** | **Uses Value Function** | **Optimization Signal** | **Key Innovation** |
| --- | --- | --- | --- | --- | --- | --- |
| **PPO (Proximal Policy Optimization)** | ✅ | ✅ | ✅ | ✅ | Advantage-weighted policy gradient with clipping | Stabilized policy updates via clipped surrogate loss |
| **DPO (Direct Preference Optimization)** | ✅ | ❌ | ❌ | ❌ | Preference-based log-likelihood ratio | Direct alignment from human preference data without rewards or critics |
| **GRPO (Group Relative Policy Optimization)** | ✅ | ✅ | ❌ | ❌ | Group-relative advantage estimation | Removes critic; uses group-average reward as baseline |

###### Takeaways

* These algorithms represent an **evolution in policy optimization**, progressively simplifying how feedback and stability are achieved:

  1. **PPO (2017)**: Anchored in traditional **actor-critic** design, PPO uses a learned value function to estimate advantages and a clipped objective to stabilize updates.
  2. **DPO (2023)**: Moves beyond explicit reward and critic modeling, using **direct supervised optimization** on human preference data.
  3. **GRPO (2024)**: Reintroduces reinforcement-style training but **without a critic**, computing relative advantages among sampled groups.
* In summary:

  + All three are **policy-based methods**.
  + **PPO** and **GRPO** are **policy gradient methods**, while **DPO** uses **supervised gradients** instead of estimating gradients from sampled rewards or environment rollouts (as in policy gradients). Specifically, DPO derives them directly from **supervised preference losses** computed over labeled data pairs \((x, y^+, y^-)\). These gradients arise from minimizing a differentiable loss function, much like in standard supervised learning, where the model is updated to increase the likelihood of preferred outputs.
  + Only **PPO** retains the **actor-critic** structure.
* Together, they trace a continuum from **explicit RL (PPO)** \(\rightarrow\) **direct preference learning (DPO)** \(\rightarrow\) **critic-free policy gradients (GRPO)** — marking the field’s shift toward simpler, more scalable approaches for optimizing large model behavior.

#### Predecessors of PPO

* [REINFORCE](https://link.springer.com/content/pdf/10.1007/BF00992696.pdf) and [TRPO](https://arxiv.org/abs/1502.05477) serve as foundational approaches to policy optimization, each addressing different challenges in RL. REINFORCE provides a simple yet high-variance method for optimizing policies, while TRPO improves stability by constraining updates. These methods paved the way for Proximal Policy Optimization (PPO), which builds on TRPO by introducing a more efficient and scalable optimization framework commonly used in modern RL applications.

##### The REINFORCE Algorithm

* One of the earliest policy optimization methods in RL is REINFORCE, introduced in [Williams (1992)](https://link.springer.com/content/pdf/10.1007/BF00992696.pdf). REINFORCE is a policy gradient algorithm that directly optimizes the policy by maximizing expected rewards.
* The key idea behind REINFORCE is the use of Monte Carlo sampling to estimate the policy gradient, which is then used to update the policy parameters using stochastic gradient ascent.
* The update rule is as follows:

  \[\theta \leftarrow \theta + \alpha \sum\_{t=0}^{T} \nabla\_\theta \log \pi\_\theta(a\_t | s\_t) R\_t\]
  + where:
    - \(\pi\_\theta\) is the policy parameterized by \(\theta\),
    - \(a\_t\) is the action taken at time \(t\),
    - \(s\_t\) is the state at time \(t\),
    - \(\alpha\) is the learning rate, and
    - \(R\_t\) is the cumulative return from time step \(t\), defined as \(R\_t = \sum\_{k=t}^{T} \gamma^{k-t} r\_k\), representing the total discounted reward obtained from that point onward. It captures how good the future trajectory is, starting from time \(t\), based on the agent’s actions.
* Despite its simplicity, REINFORCE suffers from high variance in gradient estimates, leading to unstable training. Variance reduction techniques like baseline subtraction (using a value function) are often used to mitigate this issue.

##### Trust Region Policy Optimization (TRPO)

* Trust Region Policy Optimization (TRPO) is an advanced policy optimization algorithm introduced by [Schulman et al. (2015)](https://arxiv.org/abs/1502.05477). It was developed to improve upon traditional policy gradient methods like REINFORCE by enforcing a constraint on policy updates, preventing large, destabilizing changes that can degrade performance.

###### Core Idea

* TRPO aims to optimize the expected advantage-weighted policy ratio while ensuring that updates remain within a predefined trust region. The objective function is:

  \[\max\_{\theta} \mathbb{E}\_{s, a \sim \pi\_{\theta\_\text{old}}} \left[ \frac{\pi\_{\theta}(a|s)}{\pi\_{\theta\_\text{old}}(a|s)} A^{\pi\_{\theta\_\text{old}}}(s, a) \right]\]
  + subject to the Kullback-Leibler (KL) divergence constraint:

    \[D\_{KL}(\pi\_{\theta} \mid\mid \pi\_{\theta\_\text{old}}) \leq \delta\]
    - where:
      * \(A^{\pi\_{\theta\_\text{old}}}(s, a)\) is the advantage function,
      * \(D\_{KL}\) is the KL divergence measuring the difference between old and new policies,
      * \(\delta\) is a small threshold defining the trust region.
* This KL constraint ensures that policy updates are not too aggressive, preventing performance collapse and maintaining stability.

###### The Role of the Policy Ratio

* The policy ratio, defined as \(r(s, a; \theta) = \frac{\pi\_{\theta}(a \mid s)}{\pi\_{\theta\_\text{old}}(a \mid s)}\), and measures how the probability of taking a particular action under the new policy compares to the old one.
* This ratio acts as an **importance weight**, re-scaling each sampled action’s contribution according to how likely it is under the updated policy. In practice:

  + If an action becomes more likely under the new policy (ratio > 1), its advantage contributes more to the gradient update.
  + If it becomes less likely (ratio < 1), its contribution is reduced.
* The policy ratio plays the role of **reweighting one distribution by another**, and is sometimes called the **reweighting factor**. It effectively serves as the **weight correcting for distribution shift** between the old and new policy. Without this correction, the optimization would be biased, as the data distribution (from the old policy) would not align with the target distribution (from the new policy).
* Even though TRPO is typically trained in an **offline or off-policy manner**—using trajectories sampled from the old policy—it still needs this **distribution shift correction** to ensure unbiased gradient estimation. The samples are drawn under \(\pi\_{\theta\_\text{old}}\), but the optimization objective is defined for \(\pi\_{\theta}\). Without this correction, the optimization would be biased, as the data distribution would not align with the updated policy. The policy ratio bridges this mismatch, allowing TRPO to accurately estimate how the new policy would perform if deployed, despite relying on previously collected (offline) data.
* By incorporating the policy ratio within a KL-constrained optimization, TRPO ensures stable and monotonic policy improvement — a key theoretical advantage over unconstrained policy gradient methods.

###### Strengths and Limitations

* **Stable Learning**: TRPO’s constraint limits drastic changes in policy updates, making it robust in complex environments such as robotic control and RL applications.
* **Computational Complexity**: TRPO requires solving a constrained optimization problem, which involves computing second-order derivatives, making it computationally expensive.
* **Impact on PPO**: TRPO inspired PPO, which simplifies the trust region approach by using a clipped objective function to balance exploration and exploitation efficiently.
* Overall, TRPO remains a cornerstone in RL, particularly in high-stakes applications where stability is crucial.

###### Paving the way for PPO

* TRPO introduced trust region constraints to stabilize learning, paving the way for PPO, which simplifies TRPO by using a clipped objective function to balance exploration and exploitation in policy updates.

#### Intuition Behind PPO

* PPO is designed to stabilize policy updates by ensuring that new policies do not deviate too much from previous ones.

##### Why Not Naive Policy Gradients?

* Traditional policy gradients (REINFORCE) often lead to unstable updates because they do not constrain how much the policy changes from one iteration to the next.
* This can cause catastrophic forgetting or sudden performance drops.

##### Why Not Trust Region Policy Optimization (TRPO)?

* TRPO stabilizes learning by enforcing a trust region constraint using KL-divergence, but solving the constrained optimization problem is computationally expensive.

##### How Does PPO Solve These Problems?

* PPO simplifies TRPO by introducing a clipping mechanism in the objective function.
* This allows for stable policy updates without requiring second-order optimization or explicit KL-divergence constraints.
* Thus, PPO achieves a balance between stability and efficiency, making it highly practical for large-scale RL applications.

#### Fundamental Components and Requirements

* PPO requires the following fundamental components:
  + **Policy** \(\pi\_{\theta}\): The LLM that has been pre-trained or undergone supervised fine-tuning.
  + **Reward Model** \(R\_{\phi}\): A trained and frozen network that provides a scalar reward given a complete response to a prompt.
  + **Critic** \(V\_{\gamma}\): Also known as the value function, a learnable network that takes in a partial response to a prompt and predicts the scalar reward.

#### Core Principles

##### Policy Gradient Approach

* PPO operates on the policy gradient approach, where the agent directly learns a policy, typically parameterized by a neural network. The policy maps states to actions based on the current understanding of the environment.

##### Actor-Critic Framework

* PPO is based on the actor-critic framework, which means it simultaneously trains two components:
  + **Actor (Policy Network)**: Selects actions based on the current policy.
  + **Critic (Value Function Network)**: Evaluates these actions by estimating the expected the return of each state, i.e., the value of the state-action pairs.
* This dual approach allows PPO to efficiently balance exploration and exploitation by guiding the actor’s policy updates using feedback from the critic. The critic helps compute the advantage function, which quantifies the quality of the actions taken, enabling more informed updates to the policy.

###### The Actor (Policy Network)

* The actor network (\(\pi\_\theta\)) is responsible for selecting actions based on the current policy:

  \[\pi\_\theta(a\_t \mid s\_t) = P(a\_t \mid s\_t ; \theta)\]
  + where \(\theta\) represents the learnable parameters of the policy network.
* Unlike the critic, which estimates the expected return of a given state, the actor directly determines the probability distribution over possible actions. This allows the agent to explore different responses while refining its behavior over time.
* The actor is updated using a clipped surrogate objective function to ensure stable policy improvements:

  \[L(\theta) = \mathbb{E}\_t \left[ \min\left( r\_t(\theta) \hat{A\_t},\,\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A\_t} \right) \right]\]
  + where:
    - \(r\_t(\theta) = \frac{\pi\_\theta(a\_t \mid s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t \mid s\_t)}\) is the probability ratio between the new and old policies.
    - \(\hat{A\_t}\) is the advantage function guiding policy updates.
    - \(\epsilon\) is a hyperparameter that constrains policy updates to prevent drastic changes.
* This clipping mechanism prevents excessively large updates, mitigating instability and ensuring smooth learning.
* The actor continually adapts by maximizing this objective, leading to more effective and stable policy learning while being guided by the critic’s evaluation of expected returns.

###### The Critic (Value Function)

* The critic network (\(V\_\gamma\)) is trained to predict the final reward from a partial response:

  \[L(\gamma) = \mathbb{E}\_t \left[(V\_\gamma(s\_t) - \text{sg}(R\_\phi(s\_T)))^2\right]\]
  + where \(\text{sg}\) is the stop-gradient operation.
* The critic learns alongside the policy, ensuring it stays aligned with the current model.

#### Top-Level Workflow

* The PPO workflow contains five main stages for iterative policy improvement:
  1. **Generate responses:** LLM produces multiple responses for a given prompt
  2. **Score responses:** The reward model assigns reward for each response
  3. **Compute advantages:** Use GAE to compute advantages
  4. **Optimize policy and update critic:** Update the LLM by optimizing the total objective and train the value model in parallel to predict the rewards given partial responses

#### Key Components

##### Optimal Policy, Old Policy, and Reference Policy

1. **Optimal Policy (\(\pi^{\*}\) or \(\pi\_{\text{optimal}}\)):**
   * The **optimal policy** represents the ideal strategy or distribution over actions (in the case of LLMs, token generations) that maximizes the objective function \(J(\pi)\). This objective encodes the desired behavioral alignment goals—such as helpfulness, truthfulness, and harmlessness—within the reinforcement learning framework. Formally, the optimal policy is defined as:

     \[\pi^{\*} = \arg\max\_{\pi} J(\pi)\]
     + where \(J(\pi)\) is the **objective function**, typically expressed as an expectation of the cumulative reward or advantage under the current policy.
2. **Old Policy (\(\pi\_{\text{old}}\)):**
   * The **old policy** is the snapshot of the model’s parameters **before the current update step**. It serves as the denominator in the probability ratio, controlling the size of each policy update to ensure training stability. This policy acts as a local reference that prevents overly large deviations between successive iterations.
   * The **importance sampling ratio** is mathematically defined as:

     \[r\_t(\theta) = \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}{\pi\_{\text{old}}(o\_t \mid q, o\_{<t})}\]
     + where:

       - \(\pi\_\theta(o\_t \mid q, o\_{<t})\) is the **current policy**, representing the updated model’s probability of generating token \(o\_t\) given context \(q, o\_{<t}\).
       - \(\pi\_{\text{old}}(o\_t \mid q, o\_{<t})\) is the **previous policy**, representing the model’s probability before the current optimization step.
       - This ratio allows for **off-policy correction**, ensuring that updates are proportional to how much the new policy diverges from the old one.
3. **Reference Policy (\(\pi\_{\text{ref}}\)):**
   The **reference policy** is a **frozen model** used as a long-term stability anchor, typically corresponding to a supervised fine-tuned (SFT) or pre-trained checkpoint. It is not updated during reinforcement learning but provides the baseline distribution for computing the **KL divergence penalty**, which ensures the trained policy does not diverge excessively from a known, desirable behavior distribution.

   * The per-token KL divergence between the current and reference policies is defined as:

     \[D\_{\text{KL}}[\pi\_\theta \mid\mid \pi\_{\text{ref}}] =
     \sum\_t \pi\_\theta(o\_t \mid q, o\_{<t})
     \log \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}{\pi\_{\text{ref}}(o\_t \mid q, o\_{<t})}\]
   * In PPO, this penalty is typically **embedded within the reward function** as a per-token adjustment. In GRPO, it is **explicitly added as a separate term in the loss**, allowing independent control over regularization strength. A detailed discussion of this penalty term is included in the [KL Penalty: PPO vs. GRPO](#kl-penalty-ppo-vs-grpo) section.

##### Surrogate Objective Function

* Central to PPO is its surrogate objective function, which considers the (i) policy ratio, and (ii) advantage function, as explained below.
* In the context of LLMs, the state corresponds to the input prompt along with the tokens generated so far (i.e., the context), and the action refers to the next token the model chooses to generate. That is:
  + **State \(s\)**: The input question \(q\) (i.e., prompt) and previously generated tokens \(o\_{<t}\)
  + **Action \(a\)**: The next token \(o\_t\)
* The “policy ratio”, also known as the “likelihood ratio” or “probability ratio” or “importance ratio” or “importance sampling ratio” or “policy likelihood ratio”, is the ratio of the probability of an action under the new (i.e., current) policy to the old (i.e., reference or behavior) policy. This ratio helps align the training of the current model with the data sampled from an earlier version of the policy.
* Mathematically, the general form of the policy ratio is:

  \[r(\theta) = \frac{\pi\_{\theta}(a \mid s)}{\pi\_{\theta\_\text{old}}(a \mid s)}\]
* In the LLM setting, this becomes:

  \[r\_t(\theta) = \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}{\pi\_{\text{old}}(o\_t \mid q, o\_{<t})}\]
  + where:
    - \(\pi\_\theta\) is the current policy (i.e., the model being updated),
    - \(\pi\_{\text{old}}\) is the policy that was used to generate the training data,
    - \(o\_t\) is the token being predicted at time step \(t\),
    - \(q\) is the question or initial input,
    - \(o\_{<t}\) is the sequence of previously generated tokens.
* This ratio tells us how much more or less likely the current model is to generate a token compared to the old one. It is used to reweigh updates to the policy to account for the fact that the training data was collected under a different policy, hence it is called the importance sampling ratio.
* In PPO, this ratio is clipped within a certain range (e.g., \([1 - \epsilon, 1 + \epsilon]\)) to prevent large, destabilizing updates. This makes the training more robust when the current policy starts to diverge from the old one.
* The policy ratio is multiplied by the advantage function, which measures how much better a specific action is compared to the average action at that state. In PPO, this advantage is estimated using techniques like [Generalized Advantage Estimation (GAE)](#generalized-advantage-estimation-gae) and relies on a separately trained value function (critic). In contrast, GRPO simplifies this by estimating the advantage from relative group rewards, avoiding the need for a value model.
* A detailed discourse on this has been offered in the section on [PPO’s Objective Function: Clipped Surrogate Loss](#ppos-objective-function-clipped-surrogate-loss).

##### Clipping Mechanism

* PPO clips/limits the policy ratio in its objective function within a defined range (typically \([1-\epsilon, 1+\epsilon]\)), ensuring controlled updates. This clipping ensures that the updates to the policy are kept within a reasonable range, preventing the new policy from deviating excessively from the reference one. Ultimately, this mechanism helps in maintaining the stability of the learning process.

##### Data Re-use over Multiple Epochs of Stochastic Gradient Ascent

* PPO uses each batch of experiences for multiple epochs of stochastic gradient ascent to update the policy, improving sample efficiency compared to some other methods.

##### Value Function and Baseline

* PPO trains a value function (the critic) is trained alongside the policy (the actor) to estimate state values. The value function estimates the expected return (cumulative future rewards) from each state and is used to compute the advantage function, which in turn informs the policy update.
* The baseline provided by the critic stabilizes the training process by reducing variance in the policy gradients, helping the actor make more precise updates.

#### PPO’s Objective Function: Clipped Surrogate Loss

##### Intuition

* The surrogate loss in PPO is defined based on the ratio of the probability of taking an action under the current policy to the probability of taking the same action under the reference policy.
* This ratio is used to adjust the policy towards actions that have higher rewards while ensuring that updates are not too drastic. The clipping mechanism is employed to limit the magnitude of these updates, maintaining stability during training.

> Note that in conventional deep learning, loss functions are typically minimized to reduce prediction error, while in reinforcement learning, objective functions are usually maximized to increase expected reward or policy performance. Specifically, in policy optimization (say, with PPO) the objective function is maximized, as it aims to improve the policy by increasing the expected reward under a surrogate objective.

##### Components

* PPO’s clipped surrogate objective function has the following components:

  + **Policy Ratio:** The core of the PPO objective function involves the policy ratio, which is the ratio of the probability of taking a certain action under the current policy to the probability under the reference policy. This ratio is multiplied by the advantage estimate, which reflects how much better a given action is compared to the average action at a given state.
  + **Clipped Surrogate Objective:** To prevent excessively large updates, which could destabilize training, PPO introduces a clipping mechanism in its objective function. The policy ratio is clipped within a certain range, typically \([1-\epsilon, 1+\epsilon]\) (where \(\epsilon\) is a small value like 0.1 or 0.2). This clipping ensures that the updates to the policy are not too large, which maintains stability in training.
  + Formally:

    \[L^{\text{clip}}(\theta) = \mathbb{E}\_t \left[ \min(r\_t(\pi\_\theta) \hat{A}^{\text{GAE}}\_t,\,\text{clip}(r\_t(\pi\_\theta),1-\epsilon, 1+\epsilon) \hat{A}^{\text{GAE}}\_t)\right]\]
    - where:
      * \(L^{\text{clip}}(\theta)\):
        + The clipped surrogate loss in PPO, which balances policy updates by preventing excessively large changes to the policy.
        + This function ensures that the new policy does not deviate too far from the old policy, maintaining stable training.
      * \(\mathbb{E}\_t\):
        + Expectation over all time steps \(t\), averaging the objective function across multiple training samples.
      * \(r\_t(\pi\_\theta)\):
        + The probability ratio that compares the new policy to the old policy, given by:
          \(r\_t(\pi\_\theta) = \frac{\pi\_\theta (a\_t \mid s\_t)}{\pi\_{\theta\_{\text{old}}} (a\_t \mid s\_t)}\)
          - If \(r\_t(\pi\_\theta) > 1\), the action is more likely under the new policy.
          - If \(r\_t(\pi\_\theta) < 1\), the action is less likely under the new policy.
      * \(\hat{A}^{\text{GAE}}\_t\):
        + The advantage function computed using [Generalized Advantage Estimation (GAE)](#generalized-advantage-estimation-gae).
        + Measures how much better (or worse) an action \(a\_t\) is compared to the policy’s average action at state \(s\_t\).
        + A positive \(\hat{A}^{\text{GAE}}\_t\) encourages increasing the probability of the action, while a negative \(\hat{A}^{\text{GAE}}\_t\) discourages it.
      * \(\text{clip}(r\_t(\pi\_\theta),1-\epsilon, 1+\epsilon)\):
        + The clipping function, which limits \(r\_t(\pi\_\theta)\) within the range \([1 - \epsilon, 1 + \epsilon]\).
        + This ensures that updates to the policy do not drastically change the probability of taking a certain action.
      * \(\min(r\_t(\pi\_\theta) \hat{A}^{\text{GAE}}\_t,\,\text{clip}(r\_t(\pi\_\theta),1-\epsilon, 1+\epsilon) \hat{A}^{\text{GAE}}\_t)\):
        + The core of the clipped loss function:
          - If \(r\_t(\pi\_\theta) \hat{A}^{\text{GAE}}\_t\) is too large, the function selects the clipped version.
          - If it is within the safe range, it behaves as a standard policy gradient update.
        + This prevents over-aggressive policy updates, stabilizing learning.
  + **KL Divergence Loss:** Besides the clipped objective, another common component in the loss function is to add a KL divergence penalty to the objective function. This means the algorithm would penalize the objective based on how much the new policy diverges from the reference policy. In other words, the KL divergence component prevents overconfident policy updates by keeping the new policy close to the reference one by penalizing updates that result in a large divergence from the reference policy.
    - The KL divergence loss is typically added to the objective function as a penalty term:

      \[L^{\text{KL}}(\theta) = \mathbb{E} \left[ L^{\text{PPO}}(\theta) - \beta \text{KL}[\pi\_{\text{old}} \mid\mid \pi\_{\theta}] \right]\]
      * where:
        + \(\beta\) is a hyperparameter that controls the strength of the KL penalty.
  + **Value Function Loss:** PPO also typically includes a value function loss in its objective. This part of the objective function ensures that the estimated value of the states (as predicted by the value function) is as accurate as possible, which is important for computing reliable advantage estimates.
  + **Entropy Bonus:** Some implementations of PPO include an entropy bonus to encourage exploration by penalizing low entropy (overly confident) policies. This part of the objective function rewards the policy for taking a variety of actions, which helps prevent premature convergence to suboptimal policies. Formally:

    \[H(\theta) = - \mathbb{E}\_{a\_t} [\log \pi\_\theta (a\_t \mid s\_t)]\]
    - where:
      * \(H(\theta)\): The entropy of the policy \(\pi\_\theta\), which measures the uncertainty or diversity of the actions selected by the policy.
      * \(\mathbb{E}\_{a\_t}\) (Expectation over \(a\_t\)): The expectation is taken over all possible actions \(a\_t\) that could be chosen by the policy at a given state \(s\_t\).
      * \(\pi\_\theta (a\_t \mid s\_t)\): The probability assigned by the policy \(\pi\_\theta\) to taking action \(a\_t\) when in state \(s\_t\).
      * \(\log \pi\_\theta (a\_t \mid s\_t)\): The log-probability of selecting action \(a\_t\). This helps measure how certain the policy is about choosing \(a\_t\).
      * Negative sign (\(-\)): Since log-probabilities are typically negative (as probabilities are between 0 and 1), the negative sign ensures entropy is positive. Higher entropy corresponds to more randomness in the policy, while lower entropy corresponds to more deterministic behavior.

###### Purpose of the Clipping Mechanism

* The clipping mechanism is central to the stability and reliability of PPO. It ensures that the policy updates do not result in excessively large changes, which could destabilize the learning process. The clipping mechanism works as follows:

  + **Clipping Range:** The ratio \(r(\theta)\) is clipped to the range \([1 - \epsilon, 1 + \epsilon]\). This means if the ratio \(r(\theta)\) is outside this range, it is set to the nearest bound.
  + **Objective Function Impact:** By clipping the probability ratio, PPO ensures that the change in policy induced by each update is kept within a reasonable range. This prevents the new policy from deviating too far from the reference policy, which could lead to instability and poor performance.
  + **Practical Example:** If the probability ratio \(r(\theta)\) is 1.2 and \(\epsilon\) is 0.2, the clipped ratio would remain 1.2. However, if \(r(\theta)\) is 1.4, it would be clipped to 1.2 (1 + 0.2), and if \(r(\theta)\) is 0.7, it would be clipped to 0.8 (1 - 0.2).

###### Purpose of Surrogate Loss

* The surrogate loss allows PPO to balance the need for policy improvement with the necessity of maintaining stability. By limiting the extent to which the policy can change at each update, the surrogate loss ensures that the learning process remains stable and avoids the pitfalls of overly aggressive updates. The clipping mechanism is a key innovation that helps PPO maintain this balance effectively. This approach helps PPO to achieve a good balance between effective policy learning and the stability required for reliable performance in various environments.

##### Mathematical Formulation

* To formalize PPO, let:

  + \(\pi\_\theta\) denote the **current policy** parameterized by \(\theta\), and
  + \(\pi\_{\text{old}}\) denote the **previous policy** before the latest update.
* PPO aims to improve the policy while avoiding excessively large updates that could destabilize learning. This is achieved through a **Clipped Surrogate Objective**, which constrains the change in policy probability ratios between consecutive updates.
* The complete PPO objective combines three components — the **Clipped Surrogate Objective**, an (optional) **Entropy Bonus** encouraging exploration (following prior work—**[REINFORCE (Williams, 1992)](https://www-anw.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf)** and **[A3C/A2C (Mnih et al., 2016)](https://arxiv.org/abs/1602.01783)**), and an (optional) **KL-Divergence Penalty** discouraging policy shifts that are too large.
* As described in [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) by Schulman et al., (2017), only the **clipped objective** is **fundamental** to PPO; the **entropy** and **KL** terms are **optional regularization terms**, **weighted by scalar coefficients \(w\_1\) and \(w\_2\)**, that can be added to improve stability or maintain exploration balance. Specifically, \(w\_1\) controls the strength of the entropy bonus (encouraging exploration), and \(w\_2\) controls the KL penalty (discouraging large policy shifts):

  \[L\_{\text{PPO}}(\theta) =
  \underbrace{L\_{\text{clip}}(\theta)}\_{\text{Clipped Surrogate Objective}} + \underbrace{w\_1 H(\theta)}\_{\text{Optional: Encourage Exploration}}
  - \underbrace{w\_2 \text{KL}(\theta)}\_{\text{Optional: Penalize Policy Divergence}}\]
  + where:

    - **\(w\_1\)** is a **scalar coefficient** controlling the contribution of the entropy bonus term. Higher values encourage greater policy entropy, promoting exploration.
    - **\(w\_2\)** is a **scalar coefficient** controlling the strength of the KL penalty term. Larger values increase resistance to large policy updates, improving stability but potentially slowing learning.
    - **Clipped Surrogate Objective:**

      \[L\_{\text {clip }}(\theta)=\hat{\mathbb{E}}\_t\left[\min \left(r\_t(\theta) \hat{A}\_t,\,\operatorname{clip}\left(r\_t(\theta), 1-\epsilon, 1+\epsilon\right) \hat{A}\_t\right)\right]\]
      * where:

        + \(r\_t(\theta) = \frac{\pi\_\theta(a\_t\mid s\_t)}{\pi\_{\text{old}}(a\_t\mid s\_t)}\) is the policy ratio term, which represents the ratio between the new and old policy probabilities for the same action.
        + The clipping ensures that if the new policy deviates too much from the old one (beyond \([1-\epsilon, 1+\epsilon]\)), the objective is truncated — preventing drastic updates.
    - **KL Divergence (optional regularization):**

      \[\text{KL}(\theta) = \hat{\mathbb{E}}\_t \left[
      \mathbb{D}\_{\text{KL}}\big(\pi\_{\theta\_{\text{old}}}(\cdot \mid s\_t) \mid\mid \pi\_{\theta}(\cdot \mid s\_t)\big)
      \right]\]
      * This optional penalty term discourages excessive divergence between consecutive policy distributions, helping stabilize training when needed.
    - **Entropy Bonus (optional regularization):**

      \[H(\theta) = \hat{\mathbb{E}}\_t\Big[
      \mathbb{E}\_{a\_t \sim \pi\_\theta(\cdot \mid s\_t)}[-\log \pi\_\theta(a\_t \mid s\_t)]
      \Big]\]
      * This optional term encourages exploration by increasing the entropy of the policy distribution.

###### PPO with Clipped Surrogate Loss

* To recap, \(\pi\_\theta\) is the current policy parameterized by \(\theta\), while \(\pi\_{\text{old}}\) is the old policy. For a given state \(s\) and action \(a\), the probability ratio is:

\[r(\theta) = \frac{\pi\_\theta(a|s)}{\pi\_{\text{old}}(a|s)}\]

* The expanded form of the PPO clipped surrogate loss can be derived directly from the clipped objective above by plugging in the policy likelihood ratio can be written as:

  \[L\_{\text{PPO-CLIP}}(\theta) = \hat{\mathbb{E}}\_{t}\left[ \min \left(\frac{\pi(a|s)}{\pi\_{\text{old}}(a|s)} \hat{A}\_t,\,\text{clip}\left(\frac{\pi(a|s)}{\pi\_{\text{old}}(a|s)}, 1 - \epsilon, 1 + \epsilon \right) \hat{A}\_t \right) \right]\]
  + where:
    - \(r\_t(\theta) = \frac{\pi\_\theta(a\_t\mid s\_t)}{\pi\_{\text{old}}(a\_t\mid s\_t)}\) is the **policy ratio term**, representing how the new policy’s probability for taking action \(a\_t\) under state \(s\_t\) compares to the old policy’s probability.
    - \(\hat{A}\_t\) is the **advantage estimate**, which measures how much better an action is compared to the average action at a given state. It is typically computed using **[Generalized Advantage Estimation (GAE)](#generalized-advantage-estimation-gae)**, balancing bias and variance through the use of the discount factor \(\gamma\) and the GAE parameter \(\lambda\).
    - \(s\_t\) is the **state** observed at timestep \(t\).
    - \(a\_t\) is the **action** taken by the policy under state \(s\_t\).
    - \(\epsilon\) is a **small hyperparameter** (usually 0.1–0.3) that controls the clipping range, limiting how far the new policy can deviate from the old one. This constrains policy updates and prevents destructive policy shifts.
    - The **clipping operator** \(\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon)\) **bounds** the policy ratio within the specified interval to reduce variance and maintain learning stability.

###### PPO with KL Divergence Penalty

* An alternative to the clipped surrogate objective is to use a KL-penalized objective, where a penalty term based on the KL divergence between the current policy and the old policy is added to the loss. The penalty coefficient \(\beta\) is adaptively tuned to maintain a target KL divergence \(d\_{\text{targ}}\). After each policy update, the actual KL divergence \(d\) is measured. If \(d < d\_{\text{targ}} / 1.5\), the penalty coefficient is reduced (i.e., \(\beta \gets \beta / 2\)) to allow more flexibility in updates. If \(d > 1.5 \cdot d\_{\text{targ}}\), \(\beta\) is increased (i.e., \(\beta \gets \beta \cdot 2\)) to constrain the update more tightly. This approach helps keep the updated policy close to the previous one while still allowing learning progress. The KL-penalized loss is defined as:

  \[L\_{\text{KL}}(\theta) = \hat{\mathbb{E}}\_t \left[ \frac{\pi\_\theta(a\_t | s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t | s\_t)} \hat{A}\_t - \beta \sum\_{a} \pi\_{\theta\_{\text{old}}}(a | s\_t) \log \left(\frac{\pi\_{\theta\_{\text{old}}}(a | s\_t)}{\pi\_\theta(a | s\_t)} \right) \right]\]
  + where:
    - \(\pi\_{\theta\_{\text{old}}}\) is the policy before the update.
    - \(\pi\_\theta\) is the current policy.
    - \(\hat{A}\_t\) is the estimated advantage.
    - \(\beta\) is the KL penalty coefficient adjusted dynamically to match the KL target.

###### PPO with Clipped Surrogate Loss and KL Divergence Penalty

* The PPO paper also suggests that the KL penalty can be used in combination with the clipped surrogate objective. In this hybrid approach, the clipped objective controls the size of the policy update explicitly, while the KL penalty provides an additional regularization signal to discourage large divergences from the previous policy. Although this combined objective performed slightly worse than clipping alone in the paper’s experiments, it is included as an important baseline:

  \[L\_{\text{CLIP+KL}}(\theta) = \hat{\mathbb{E}}\_t \left[ \min \left(r\_t(\theta) \hat{A}\_t,\,\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A}\_t \right) - \beta \sum\_{a} \pi\_{\theta\_{\text{old}}}(a | s\_t) \log \left(\frac{\pi\_{\theta\_{\text{old}}}(a | s\_t)}{\pi\_\theta(a | s\_t)} \right) \right]\]
  + where:
    - The first term is the standard PPO clipped surrogate objective.
    - The second term adds a KL divergence penalty between the old and new policies.
    - \(\beta\) is the dynamically adjusted penalty coefficient.

#### Generalized Advantage Estimation (GAE)

* PPO uses Generalized Advantage Estimation (GAE) to compute advantages, which defines how much better a specific action \(a\_t\) is compared to an average action the policy will take in state \(s\_t\).
* GAE plays a crucial role in PPO by providing a flexible, variance-reduced estimator of the advantage function, enabling more stable and sample-efficient policy optimization.

##### Formal Definition

\[\hat{A\_t} = Q(s\_t, a\_t) - V(s\_t)\]

* where:
  + \(Q(s\_t, a\_t)\) is the expected cumulative reward of taking a specific action \(a\_t\) in state \(s\_t\)
  + \(V(s\_t)\) is the expected cumulative reward of the average action the policy takes in state \(s\_t\)

##### Advantage Estimation Approaches

* There are two main approaches to estimating advantage:

  + **Monte-Carlo (MC):**
    - Uses the reward of the full trajectory (full responses)
    - High variance due to sparse reward
    - Low bias as we can accurately model the reward
  + **Temporal Difference (TD):**
    - Uses one-step trajectory reward
    - Significantly reduces variance
    - Higher bias as we can’t as accurately anticipate final reward

##### GAE Formula and Bias-Variance Trade-off

* GAE balances bias and variance through multi-step TD:

  \[A^{\text{GAE}}\_K = \sum^{K-1}\_{t=0} (\lambda)^t \delta\_t\]
  + where:
    - \(K\) denotes the number of TD steps (\(K < T\))
    - \(\delta\_t\) denotes the TD error at step \(t\):
      \(\delta\_t = r\_t + \gamma V(s\_{t+1}) - V(s\_t)\)
    - The hyperparameter \(\lambda\) controls the trade-off:
      * \(\lambda = 0\) \(\rightarrow\) Pure TD learning (low variance, high bias)
      * \(\lambda = 1\) \(\rightarrow\) Pure Monte Carlo (high variance, low bias)
* In practice, PPO uses a truncated version of GAE, where the advantage estimate over a trajectory segment of length \(T\) is computed as:

  \[\hat{A}\_t = \delta\_t + (\gamma \lambda) \delta\_{t+1} + \cdots + (\gamma \lambda)^{T - t + 1} \delta\_{T - 1}\]
  + where \(\delta\_t = r\_t + \gamma V(s\_{t+1}) - V(s\_t)\)
* This formulation allows PPO to effectively trade off bias and variance by adjusting \(\lambda\), which is typically set between 0.9 and 0.97.

##### Role in PPO’s Clipped Surrogate Objective

* This advantage estimate \(\hat{A}\_t\) is a critical component of PPO’s clipped surrogate objective, which is used to update the policy:

  \[L^{\text{CLIP}}(\theta) = \mathbb{E}\_t \left[ \min \left(r\_t(\theta) \hat{A}\_t,\,\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}\_t \right) \right]\]
  + where:
    - \(r\_t(\theta) = \frac{\pi\_\theta(a\_t \mid s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t \mid s\_t)}\) is the ratio of the probability of action \(a\_t\) under the new and old policies
    - \(\epsilon\) is a hyperparameter (e.g., 0.2) that limits the deviation from the old policy
* The advantage \(\hat{A}\_t\) modulates how much the policy is updated: if the advantage is positive, the update favors increasing the probability of the action; if negative, the update discourages it. Clipping ensures the update is conservative and prevents excessive deviation from the current policy.

#### Reward and Value Model Roles

* While PPO originated in **classical RL**—where rewards come directly from the environment (e.g., in MuJoCo or Atari)—its application in **RLHF** for LLMs fundamentally redefines the roles of the **reward** and **value models**.
* A detailed discourse of each model type involved in PPO—including their architecture, loss function, and other attributes is available in the [Model Roles](#model-roles) sub-section under the RLHF section.

##### Classical PPO (Standard RL Context)

* In traditional RL environments, the **reward signal** \(r\_t\) is directly provided by the environment (e.g., distance traveled, points scored, or game score).
* The **critic (value function)** estimates \(V(s\_t)\) as the expected cumulative return from state \(s\_t\). It serves as a learned baseline that reduces variance in policy gradient estimates and is used to compute the **temporal-difference (TD) error**:

  \[\delta\_t = r\_t + \gamma V(s\_{t+1}) - V(s\_t)\]
* This TD error is then used to compute the **advantage estimate**, which quantifies how much better (or worse) a taken action was compared to the baseline:

  \[\hat{A}\_t = \sum\_{l=0}^{\infty} (\gamma \lambda)^l \delta\_{t+l}\]
* The **value function** \(V(s\_t)\) itself is learned via regression toward a target value, minimizing the **value loss**:

  \[L^{VF}\_t(\theta) = \left(V\_\psi(s\_t) - V^{\text{target}}\_t \right)^2\]
  + where:

    - \(V\_\psi(s\_t)\) is the predicted value from the critic network,
    - \(V^{\text{target}}\_t\) is the bootstrapped or Monte Carlo return target.
* This value regression ensures that the critic accurately estimates future rewards, enabling stable advantage estimation for the policy update.
* Finally, the **policy update** uses the advantage estimates in the **clipped PPO objective**, which constrains the size of each update to maintain stability:

  \[J\_{\text{PPO}}(\theta) =
  \mathbb{E}\left[
  \min\left(
  r\_t(\theta)\hat{A\_t},
  \,\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A\_t}
  \right)
  \right]\]
  + where \(r\_t(\theta) = \frac{\pi\_\theta(a\_t \mid s\_t)}{\pi\_{\text{old}}(a\_t \mid s\_t)}\) is the probability ratio between current and old policies.

###### PPO in RLHF (LLM Alignment Context)

* In **RLHF for LLMs**, there is no explicit environment providing numeric rewards. Instead, the reward signal is **learned** from human preference data through a **reward model (RM)**. The critic (value model) continues to play its traditional role, but the semantics of states, actions, and rewards are adapted to natural language settings.
* **Reward Model (\(r\_\phi(x, y)\)):**

  + Trained on human preference comparisons, the reward model predicts a **scalar reward** for a prompt–response pair \((x, y)\).
  + It replaces the environment’s reward signal and quantifies how aligned a response is with human preferences.

    \[r\_\phi(x, y) = w^\top h\_T + b\]
    - where \(h\_T\) is the hidden representation of the final token in the response, and \(w, b\) are learned parameters of the reward model’s linear head.
* **Value Model (\(V\_\psi(x)\) or \(V\_\psi(x, y)\)):**

  + Predicts the **expected future reward** or serves as a **baseline** for advantage estimation.
  + The value model stabilizes learning by reducing gradient variance and anchoring the policy updates.
  + In LLM-based RLHF, this simplifies to a **bandit-style** advantage formulation (since the reward is assigned once per completion):

    \[\hat{A\_t} = r\_t - V(s\_t)\]
  + The **value loss** term is again defined as:

    \[L^{VF}\_t(\phi) = \left(V\_\psi(s\_t) - \hat{R}\_t\right)^2\]
    - … ensuring that the value model accurately predicts expected returns from the reward model’s feedback.
* **Policy Model (\(\pi\_\theta(y \mid x)\)):**

  + The trainable large language model generating responses.
  + PPO updates its parameters to **maximize the expected reward** predicted by the reward model, while **constraining divergence** from a reference model using a KL penalty.
  + The optimization objective becomes:

    \[\max\_\theta \mathbb{E}\_{x \sim D, y \sim \pi\_\theta(\cdot \mid x)}
    \Big[ r\_\phi(x,y) - \beta \mathrm{KL}\big(\pi\_\theta(\cdot \mid x) \mid\mid \pi\_{\text{ref}}(\cdot \mid x)\big) \Big]\]
    - where \(\beta\) controls the trade-off between maximizing reward and maintaining proximity to the reference model.
* **Reference Model (\(\pi\_{\text{ref}}(y \mid x)\)):**

  + A frozen copy of the supervised fine-tuned (SFT) model that provides a **stable distributional baseline**.
  + Used in the KL-regularization term to penalize large deviations in token distributions:

    \[D\_{\text{KL}}[\pi\_\theta \mid\mid \pi\_{\text{ref}}] =
    \sum\_t \pi\_\theta(o\_t \mid q, o\_{<t})
    \log \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}
    {\pi\_{\text{ref}}(o\_t \mid q, o\_{<t})}\]
  + This ensures that updates do not compromise fluency, factuality, or safety while pursuing higher reward alignment.

###### Comparative Analysis

| **Component** | **Role in PPO for LLMs** | **Description** |
| --- | --- | --- |
| Policy model \(\pi\_\theta\) | Actor | Generates responses and is updated via PPO to maximize reward minus KL penalty. |
| Reference model \(\pi\_{\text{ref}}\) | Stability anchor | Frozen SFT baseline that provides KL regularization to prevent policy drift. |
| Reward model \(r\_\phi(x,y)\) | Surrogate reward function | Maps prompt–response pairs to scalar scores representing human preference. |
| Value model (critic) \(V\_\psi(x,y)\) | Baseline estimator | Predicts expected reward and stabilizes PPO updates via the regression loss \(L^{VF}\_t=\big( V\_\psi(s\_t) - \hat{R}\_t \big)^2\) |

* In summary, PPO in the **RLHF setting** preserves its classical actor–critic structure but adapts its components:

  + **Rewards** come from a learned reward model trained on human feedback.
  + The **critic (value model)** continues to predict expected return and is trained via **regression loss**.
  + The **policy model** is optimized to maximize reward while constrained by a **KL penalty** against a **reference model**.
* This adaptation allows PPO to operate effectively in the **language model alignment regime**, translating qualitative human preferences into quantitative reinforcement signals.

#### Variants of PPO

* There are two main variants of PPO: (i) PPO-Clip and (ii) PPO-Penalty.

##### PPO-Clip

* Uses the clipped surrogate objective function to limit the policy updates.
* The most commonly used version of PPO.

##### PPO-Penalty

* Adds a KL-divergence penalty to the objective function to constrain policy updates.
* Used in cases where explicit divergence constraints are needed.

#### Advantages of PPO

* **Stability and Reliability:** The clipping mechanism in the objective function helps to avoid large, destabilizing updates to the policy, making the learning process more stable and reliable.
* **Sample Efficiency:** By reusing data for multiple gradient updates, PPO can be more sample-efficient compared to some other methods.
* **General Applicability:** PPO has demonstrated good performance across a wide range of environments, from simple control tasks to complex simulations like those in 3D simulations. It offers a simpler and more robust approach compared to previous algorithms like TRPO.

#### Simplified Example

* Imagine an agent learning to play a game. The agent tries different actions (moves in the game) and learns a policy that predicts which action to take in each state (situation in the game). The policy is updated based on the experiences, but instead of drastically changing the policy based on recent success or failure, PPO makes smaller, incremental changes. This way, the agent avoids drastically changing its strategy based on limited new information, leading to a more stable and consistent learning process.

#### Summary

* PPO stands out in the realm of RL for its innovative approach to policy updates via gradient ascent. Its key innovation is the introduction of a clipped surrogate objective function that judiciously constrains the policy ratio. This mechanism is fundamental in preventing drastic policy shifts and ensuring a smoother, more stable learning progression.
* PPO is particularly favored for its effectiveness and simplicity across diverse environments, striking a fine balance between policy improvement and stability.
* The PPO objective function is designed to balance the need for effective policy improvement with the need for training stability. It achieves this through the use of a clipped surrogate objective function, value function loss, and potentially an entropy bonus.
* While KL divergence is not a direct part of the basic PPO objective function, it is often used in the PPO-Penalty implementation of PPO to monitor and maintain policy stability. This is done either by penalizing large changes in the policy (KL penalty) or by enforcing a constraint on the extent of change allowed between policy updates (KL constraint).
* By integrating these elements, PPO provides a robust framework for RL, ensuring both stability and efficiency in the learning process. This makes it particularly suitable for fine-tuning LLMs and other complex systems where stable and reliable updates are crucial.

## Reinforcement Learning from Human Feedback (RLHF)

### Motivation

* LLMs trained with next-token prediction objectives are highly proficient at generating fluent text. However, this training alone does not ensure that the outputs are aligned with human values such as helpfulness, harmlessness, and honesty. These models may generate plausible-sounding but untruthful, unsafe, or unhelpful responses if left unguided.
* To address this gap, **Reinforcement Learning from Human Feedback (RLHF)** was introduced. RLHF provides a framework for aligning model outputs with human-generated signals to guide model behavior. It has become a central technique in aligning instruction-following models such as InstructGPT and ChatGPT.
* Put simply, RLHF enables models to go beyond merely predicting likely text, aligning their behavior with nuanced human expectations through a structured feedback loop. By incorporating direct human input at multiple stages—demonstration, comparison, and reward-based reinforcement—it provides a scalable and principled approach to model alignment, forming the backbone of modern instruction-following language models.

### Method

* In RLHF, the LLM is treated as a **policy** \(\pi\_\theta(y \mid x)\) that generates a response \(y\) to a given prompt \(x\). The objective is to adjust the parameters \(\theta\) so that the model maximizes a reward signal that reflects human judgments of response quality:

  \[\max\_{\theta}
  \mathbb{E}\_{x \sim D\_{\text{prompt}},\,y \sim \pi\_\theta(\cdot \mid x)}
  \left[ r(x, y) \right]\]
  + where \(r(x, y)\) is a reward function, typically learned from human-labeled comparison data, that evaluates how well a response \(y\) aligns with human preferences for a given prompt \(x\).

### Process

* The RLHF pipeline typically unfolds in **three major stages**, as illustrated in the diagram below from [OpenAI’s research on InstructGPT](https://openai.com/research/instruction-following):

1. **Collect Demonstration Data and Train a Supervised Policy**:

   * A human labeler provides ideal responses (demonstrations) to prompts.
   * The model is fine-tuned via supervised learning (Supervised Fine-Tuning, or SFT) to mimic these human demonstrations.
2. **Collect Comparison Data and Train a Reward Model**:

   * The model generates multiple candidate responses to a prompt.
   * Human labelers rank these responses based on alignment with criteria like helpfulness, safety, and relevance.
   * A reward model is trained to predict these rankings, typically using between 100,000 and 1 million comparison data points.
3. **Optimize the Policy Using Reinforcement Learning**:

   * The model is further trained using reinforcement learning (commonly with **Proximal Policy Optimization**, or PPO) to maximize the reward assigned by the reward model.
   * This phase usually involves 10,000 to 100,000 prompt–response training iterations.

* Another helpful summary of the full RLHF pipeline is provided in this flowchart by [Chip Huyen](https://huyenchip.com/2023/05/02/rlhf.html):

### Loss Function

#### Core Objective

* The primary optimization target in RLHF combines human preference alignment with a KL divergence term for regularization against the supervised (reference) policy. The InstructGPT paper ([Ouyang et al., 2022](https://arxiv.org/abs/2203.02155)) defines the overall **conceptual (high-level) objective** as follows:

  \[L(\theta) =
  \underbrace{\mathbb{E}\_{x,y\sim\pi\_\theta}[r\_\phi(x,y)]}\_{\text{Reward model (RM) signal}}
  -
  \underbrace{\beta \mathbb{E}\_{x,y\sim\pi\_\theta} \left[\log \frac{\pi\_\theta(y|x)}{\pi\_{\text{ref}}(y|x)}\right]}\_{\text{KL penalty (regularization)}}
  +
  \underbrace{\gamma \mathbb{E}\_{x,y\sim D\_{\text{pt}}}[\log \pi\_\theta(y|x)]}\_{\text{(Optional) pretraining term}}\]
  + where:

    - \(\pi\_\theta(y \mid x)\): the current policy (the RLHF-trained model)
    - \(\pi\_{\text{ref}}(y \mid x)\): the frozen reference policy (typically the SFT model)
    - \(r\_\phi(x,y)\): scalar reward from the reward model
    - \(\beta\): KL regularization coefficient *(typically 0.01–0.02)*
    - \(\gamma\): pretraining loss coefficient controlling gradient mixing
      * For the **reward model** and **value function**, \(\gamma = 0\) (no pretraining gradient mix).
      * For the **policy (actor)** during RLHF fine-tuning, \(\gamma = 27.8\), blending PPO and pretraining gradients to stabilize training across diverse language domains.
* Note that this objective defines **what the policy should maximize**, but not **how** it’s optimized. In practice, InstructGPT computes an **augmented reward** that combines both the reward and KL regularization terms:

  \[\tilde{r}(x,y) = r\_\phi(x,y) - \beta \log\frac{\pi\_\theta(y|x)}{\pi\_{\text{ref}}(y|x)}\]
  + This augmented reward is then used to estimate the **advantage** for PPO updates, typically \(\hat{A\_t} = \tilde{r}\_t - V(s\_t)\), where the value model provides a baseline for variance reduction.
    The actual policy improvement step uses **PPO’s clipped surrogate loss** to optimize this objective safely (see [Total RLHF Loss](#total-rlhf-loss)).
* This **core objective** therefore defines the *ideal RLHF reward* to maximize — higher human-aligned reward, lower divergence from the supervised policy, and optional retention of pretraining knowledge (cf. [Mixing Pretraining Gradients into PPO (`PPO-ptx`)](#mixing-pretraining-gradients-into-ppo-ppo-ptx) for further details on gradient blending).
* Conceptually, RLHF can be viewed as standard reinforcement learning over the **modified (augmented) reward**, where PPO provides the practical optimization mechanism to maximize this signal while preserving policy stability.

##### Interpreting the Difference in KL Divergence Between PPO and RLHF

* Although RLHF uses PPO as its optimization algorithm, the **role and meaning of the KL divergence term differ fundamentally** from its role in **standard PPO** as originally proposed in [Proximal Policy Optimization (PPO)](https://arxiv.org/abs/1707.06347). Understanding this distinction is **essential** for correctly interpreting **RLHF objectives and training dynamics**.

###### KL Divergence in Standard PPO

* **What distributions is the KL divergence between?**:

  + In vanilla PPO, the KL divergence is defined between:\[\pi\_{\theta\_{\text{old}}}(\cdot \mid s) \quad \text{and} \quad \pi\_\theta(\cdot \mid s)\]
  + That is, the KL measures the divergence between:

    - The **old (i.e., behavior) policy \(\pi\_{\theta\_{\text{old}}}\)** used to collect data in the **current iteration**.
    - The **current policy \(\pi\_\theta\)** being optimized.
  + Key properties of these distributions:

    - The **reference policy \(\pi\_{\theta\_{\text{old}}}\) changes every iteration (i.e., update step)**.
    - The KL is therefore **local in time**, comparing **consecutive policy iterates**.
    - The comparison reflects **how much the policy changes per update**.
* **How is the KL divergence term applied?**:

  + In standard PPO, the KL divergence acts as a **trust-region proxy** (similar to TRPO):

    - It is either **explicitly monitored** (with early stopping if it grows too large), or **implicitly controlled** via the **clipped surrogate objective**.
  + Crucially:

    - The KL divergence is a **first-class component of the optimization objective or constraint logic**.
    - Its function is **step-size control and training stability**, **not reward modification**.
    - PPO **approximates trust-region methods** (such as TRPO) by **directly limiting policy drift** between updates.
  + In short, in standard PPO the KL divergence is about **local optimization stability**, and it operates **directly at the level of the policy update objective**.

###### KL Divergence in RLHF (PPO-Based)

* **What distributions is the KL divergence between?**

  + In RLHF, PPO is reused as the optimization mechanism, but the **KL divergence is redefined**. Instead of comparing the current policy to the immediately previous policy, RLHF defines the KL divergence between:

    \[\pi\_\theta(\cdot \mid x) \quad \text{and} \quad \pi\_{\text{ref}}(\cdot \mid x)\]
    - where:

      * \(\pi\_\theta\) is the **current policy**, and
      * \(\pi\_{\text{ref}}\) is a **fixed reference policy**, typically the **supervised fine-tuned (SFT) model**.
  + Key properties of these distributions:

    - The **reference policy (SFT checkpoint) is frozen** throughout RLHF training.
    - The KL divergence is typically computed **per token** and **aggregated across the generated sequence**.
    - The divergence measures **deviation from a fixed behavioral anchor**, **not** from the previous iteration.
* **How is the KL divergence term applied?**

  + In RLHF, the KL divergence **does not appear explicitly** in the PPO surrogate loss. Instead, it is implemented via **reward shaping**.
  + Concretely, the KL penalty is **folded into the reward** during advantage estimation:

    \[\hat{A}\_t = \big(\mathbf{r\_t - \beta \mathrm{KL}\_t}\big) - V\_\psi(s\_t)\]
  + This implies that PPO optimizes **adjusted rewards**, **not** a loss with an explicit KL regularizer. In other words, the KL constraint is enforced **implicitly through the reward signal**, rather than **explicitly through the policy objective**. Put simply, in RLHF, PPO **implicitly enforces the KL constraint by reshaping the reward landscape**.
  + This stands in sharp contrast to vanilla PPO, where the KL divergence is a **first-class component of the optimization objective itself**. It also differs from approaches such as [GRPO](#group-relative-policy-optimization-grpo-1), which incorporate the [KL divergence explicitly as part of the overall optimization loss](#kl-penalty-ppo-vs-grpo), rather than folding it into the reward.

##### Mixing Pretraining Gradients into PPO (`PPO-ptx`)

* While standard PPO fine-tuning aligns models toward human preferences, it can also cause regressions in general language ability, factual recall, and coherence across broad NLP benchmarks. To mitigate this, the InstructGPT authors introduced a mixed-gradient training approach known as **PPO-ptx**.

###### Motivation

* During RLHF fine-tuning, the model’s optimization focuses heavily on maximizing **human-aligned reward** from the reward model. While this improves helpfulness and alignment, it can inadvertently degrade capabilities learned during pretraining, such as factual knowledge, reasoning consistency, and language fluency.
* To counteract this, **pretraining gradients** (from the original language modeling objective) are **blended into the PPO updates**. This preserves the model’s general linguistic and world knowledge while still allowing alignment to progress.
* The resulting hybrid gradient ensures that the model continues to benefit from **human feedback alignment** without forgetting how to generate coherent, information-rich text.

###### Mechanism

* The total policy gradient becomes a weighted combination of the **RLHF objective** and the **original pretraining objective** (next-token prediction).
* The combined update can be expressed schematically as:

  \[\nabla\_\theta L\_{\text{total}} = \nabla\_\theta L\_{\text{PPO}} + \gamma \nabla\_\theta L\_{\text{PTX}}\]
  + where:

    - \(L\_{\text{PPO}}\) is the PPO objective computed from rewards and KL penalties.
    - \(L\_{\text{PTX}} = - \mathbb{E}\_{(x,y)\sim D\_{\text{pt}}}[\log \pi\_\theta(y \mid x)]\) is the negative log-likelihood loss over pretraining data.
    - \(\gamma\) is the **pretraining loss coefficient** controlling the strength of the pretraining gradient.
* This approach introduces a *soft constraint* that nudges the model to remain consistent with its pretraining distribution, functioning as an implicit form of **domain regularization** across tasks and prompts.

###### Coefficient Settings and Role Differentiation

* As described in the InstructGPT paper ([Ouyang et al., 2022](https://arxiv.org/abs/2203.02155)):
  + For the **reward model** and **value function**, the coefficient is set to **\(\gamma\) = 0**, meaning **no pretraining gradient mix** — implying that these components must not bias reward estimation and value prediction by the pretraining objective.
  + For the **policy (actor)** during RLHF fine-tuning, **\(\gamma\) = 27.8**, introducing a significant pretraining gradient component. This large coefficient ensures the PPO updates are tempered by the original language modeling gradients, preventing catastrophic forgetting of general-purpose language ability.

###### Practical Effects

* This **PPO-ptx mixture** acts as a stabilizer across language domains and datasets:
  + It reduces overfitting to the reward model’s implicit biases.
  + It mitigates regressions on public NLP benchmarks observed in pure PPO training (e.g., degradation in QA or summarization performance).
  + It balances **alignment** (toward human preference) and **competence** (general language modeling skill).
* Empirically, mixing pretraining gradients leads to smoother learning curves and higher retained performance across evaluation tasks, effectively functioning as a **multi-objective optimization** between human reward and linguistic prior.

###### Intuitive Analogy

* Conceptually, the pretraining gradient acts like an **anchor** that prevents the policy from drifting too far away from its original, broad-based knowledge distribution.
* PPO, left unchecked, can overfit to reward peculiarities — the pretraining signal provides a stabilizing “memory” of how language should behave under diverse prompts, keeping the model’s updates balanced and grounded.

#### PPO Surrogate Objective

* In RHLF, the policy is optimized using the clipped PPO surrogate, which is the **practical approximation** to the conceptual RLHF objective above. While the core objective specified above expresses the ideal mathematical target, the total RLHF loss listed below operationalizes it through PPO’s clipped surrogate and critic-based stability.
* As described in the [PPO’s Objective Function: Clipped Surrogate Loss](#ppos-objective-function-clipped-surrogate-loss) section, PPO stabilizes updates and ensures that new policies don’t diverge too far from the old policy within a training iteration:

  \[L\_{\text{PPO}}(\theta) =
  \mathbb{E}\_t
  \left[
  \min\left(
  r\_t(\theta)\hat{A}\_t,\,
  \,\text{clip}(r\_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}\_t
  \right)
  \right]\]
  + where:

    - \(r\_t(\theta) = \frac{\pi\_\theta(a\_t \mid s\_t)}{\pi\_{\text{old}}(a\_t \mid s\_t)}\): policy ratio (also called probability ratio)
    - \(\hat{A}\_t\): advantage estimate
    - \(\epsilon\): clip threshold *(typical: 0.2)*

#### Value (Critic) Loss

* The critic predicts expected returns and stabilizes policy gradients by providing a baseline. Its loss function is a mean-squared error between predicted and observed returns:

  \[L\_{\text{value}}(\phi) =
  \mathbb{E}\_t \left[
  (V\_\psi(s\_t) - R\_t)^2
  \right]\]
  + where:
    - \(V\_\psi(s\_t)\): predicted value (critic)
    - \(R\_t\): empirical return from rollout
    - Coefficient for this term: \(c\_v = 0.5\) (typical)
* The critic ensures low-variance advantage estimates, making the PPO updates more stable and consistent with the theoretical RLHF objective.

#### Entropy Regularization (Optional)

* Entropy encourages exploration by penalizing overconfident or deterministic policies:

  \[L\_{\text{entropy}}(\theta) = -H[\pi\_\theta]\]
  + where:
    - \(H[\pi\_\theta]\): entropy of the policy
    - Coefficient: \(c\_e = 0.01\) (typical small positive value)
* This term helps the model continue exploring diverse outputs early in training before convergence.

#### Total RLHF Loss

* The total optimization objective combines the PPO surrogate (actor), critic regularization, and optional entropy term:

  \[L\_{\text{total}} =
  \underbrace{L\_{\text{PPO}}}\_{\text{policy (actor) loss}}
  +
  \underbrace{c\_v L\_{\text{value}}}\_{\text{critic (value) loss}}
  -
  \underbrace{c\_e H[\pi\_\theta]}\_{\text{optional entropy term}}\]
  + where:
    - \(c\_v\): critic weight *(typical: 0.5)*
    - \(c\_e\): entropy bonus weight *(typical: 0.01)*
* The KL divergence term, although not explicitly visible here, is included implicitly inside \(L\_{\text{PPO}}\) through the **advantage computation** (reward adjustment). This ensures that policy updates remain consistent with the conceptual RLHF objective:

\[\hat{A}\_t = (r\_t - \beta \text{KL}\_t) - V\_\psi(s\_t)\]

* Hence, while the **core objective** defines the target (maximize human-aligned reward minus KL deviation), the **total RLHF loss** provides the *practical, sample-based surrogate* for achieving it via PPO.

#### Notes on Practical Implementation

* **Outcome-level rewards:** one scalar per sequence; KL aggregated across tokens.
* **Process/token-level rewards:** per-token feedback; KL and rewards computed per token.
* **KL term:** serves as implicit reward shaping, preventing divergence from the SFT reference model.
* **Mixing with supervised data:** optional (\(\gamma\)-weighted) for preserving linguistic fluency and coherence for the policy (but not applied for the reward and value models).

### Pseudocode: RLHF Training Procedure

* **PPO and its use in RLHF:** As covered in the section on [Proximal Policy Optimization (PPO)](#proximal-policy-optimization-ppo), PPO is an actor-critic, policy-gradient algorithm that improves stability and sample efficiency by clipping the probability ratio, limiting the size of each update. Put simply, PPO’s **clipping mechanism** prevents excessively large updates that might destabilize training. A KL penalty to a frozen reference policy further discourages drift from supervised behavior. The total loss usually combines the PPO objective, a value regression loss, and an entropy bonus. The final stage of RLHF employs **Proximal Policy Optimization (PPO)** to fine-tune the policy model based on the reward model’s feedback.
* **Actor–critic setup:** PPO follows an actor–critic architecture:

  + The policy model (actor) generates responses to maximize expected reward.
  + The value model (critic) estimates the state value \(V\_\psi(s\_t) \approx \mathbb{E}[R\_t \mid s\_t]\) and serves as a baseline for the advantage \(\hat{A}\_t = \hat{R}\_t - V\_\psi(s\_t)\). With outcome-level rewards, \(\hat{R}\_t\) typically reflects a terminal scalar propagated to all steps (typically via [Generalized Advantage Estimation (GAE)](#generalized-advantage-estimation-gae)); with process rewards, \(\hat{R}\_t\) can accumulate token-level terms.
* **Reward signal in RLHF**: In practice, most RLHF systems use outcome-level rewards: a single scalar per completed response, usually produced by a preference-trained reward model. This scalar can be broadcast across tokens during training so every timestep shares the same terminal signal plus a KL penalty. Process (token/step-level) rewards are less common but increasingly used as reward shaping signals (e.g., correctness checks, chain-of-thought scaffolds, tool-use feedback). They can complement the outcome signal by providing denser credit assignment, but require careful design to avoid misalignment.
* Below is an annotated pseudocode representation of how PPO operates during RLHF, with detailed commentary explaining each step of the training loop. Comments indicate where outcome-level rewards (the default in most deployments) are applied and where process/token-level rewards can be inserted as shaping terms.

```
# ------------------
# RLHF Training Loop
# ------------------
# Notes:
# - Outcome-level reward: one scalar per (prompt, response). We aggregate KL across tokens
#   and subtract it from that scalar.
# - Process/token-level reward: one reward per token; we subtract KL per token and learn
#   the critic as a per-token value function (reward-to-go).
# - KL penalty follows the RLHF paper: add a per-token KL penalty against the SFT policy
#   (reference), which is equivalent to subtracting β * [log π(y|x) - log π_ref(y|x)] (summed
#   or averaged across the sequence for outcome-level). See Eq. (2) and the per-token KL note.
#
#   objective:  E[ r_θ(x, y) - β * log( π(y|x) / π_ref(y|x) ) ]
#
# - Two-loop PPO (Schulman): for each rollout iteration, optimize the surrogate L for K epochs
#   over minibatches, then set θ_old ← θ (i.e., cache new policy as the behavior policy for
#   the next data collection). Within a single iteration, logprobs_old are frozen.

# Step 0: Initialization
policy_model = SFT_model.clone()           # Actor π_θ (initialized from supervised fine-tuning)
value_model  = init_value_model()          # Critic V_φ (often initialized from the RM head)
reward_model = trained_reward_model        # RM, produces outcome-level scalar rewards
kl_reference = SFT_model.clone()           # Frozen reference π_ref for KL penalty (SFT)
beta = 0.02                                # KL reward coefficient (tune)
epsilon = 0.2                              # PPO clip ratio
num_iterations = 1000                      # ~500–2000 depending on dataset size
ppo_epochs = 4                             # PPO inner-loop epochs per batch
minibatch_size = 32                        # 16–64 for stability and GPU fit
max_seq_len = 512                          # 512 tokens for LLM RLHF fine-tuning

for iteration in range(num_iterations):

    # ----------------------------------------
    # Two-loop PPO -- Outer (Rollout) loop: collect a batch with the "old" policy
    # ----------------------------------------
    # Sample prompts and generate responses with the current policy (behavior policy).
    prompts = sample_prompts(batch_size)
    # Generate token ids and per-token logprobs under the current policy; store logprobs_old.
    responses, logprobs_old = policy_model.generate_with_logprobs(prompts, max_len=max_seq_len)
    # completion_mask: 1 for real tokens in responses, 0 for padding
    completion_mask = make_padding_mask(responses)

    # ----------------------------------------
    # Rewards
    # ----------------------------------------
    # Outcome-level reward (scalar per example)
    outcome_rewards = reward_model.evaluate(prompts, responses)           # shape: (B, 1)

    # Optional: process-level (token) reward model (same shape as responses)
    # token_rewards = token_reward_model.evaluate(prompts, responses)     # shape: (B, L)

    # ----------------------------------------
    # KL penalty (policy vs. reference)
    # ----------------------------------------
    # Get per-token logprobs under current policy π and frozen reference π_ref
    policy_logps = policy_model.logprobs(prompts, responses)              # (B, L)
    ref_logps    = kl_reference.logprobs(prompts, responses)              # (B, L)

    # Per-token log-ratio approximation used in practice:
    #   kl_per_token typical: log π(a_t|...) - log π_ref(a_t|...)
    # RLHF applies a per-token KL penalty; for outcome-level rewards we aggregate across tokens.
    kl_per_token = policy_logps - ref_logps                               # (B, L)
    # Aggregate to a scalar per sequence (mean over non-pad tokens) for outcome-level case
    # In other words, the sum() below aggregates per-token KL across valid (non-padding) tokens,
    # producing one scalar per sequence (averaged KL penalty used for outcome-level case).    
    kl_seq = (kl_per_token * completion_mask).sum(-1, keepdim=True) / completion_mask.sum(-1, keepdim=True).clamp_min(1)

    # Merge with rewards:
    # Outcome-level: subtract aggregated KL from the scalar reward
    rewards_outcome = outcome_rewards - beta * kl_seq                      # (B, 1)

    # Process-level (token) alternative:
    # rewards_token = token_rewards - beta * kl_per_token                  # (B, L)

    # ----------------------------------------
    # Values and advantages
    # ----------------------------------------
    # Critic predicts expected returns conditioned on prefixes.
    # - Outcome-level: broadcast scalar reward to tokens for advantage computation (training convenience).
    # - Process-level: targets are token-level reward-to-go.
    values = value_model.values(prompts, responses)                        # (B, L)

    # Outcome-level path (default):
    # The line below performs broadcasting: the scalar outcome-level reward (shape (B, 1))
    # is expanded to match the token dimension of the critic output (shape (B, L)),
    # so each token in the sequence receives the same reward value during training.
    rewards_per_token = rewards_outcome.expand_as(values)                  # (B, L)
    advantages = (rewards_per_token - values).detach()                     # (B, L)

    # Process-level path (if using token rewards):
    # rewards_per_token = rewards_token
    # advantages = (rewards_per_token - values).detach()                   # (B, L)

    # OPTIONAL: advantage normalization
    # The sum() calls below compute the mean advantage by summing only over valid tokens.    
    adv_mean = (advantages * completion_mask).sum() / completion_mask.sum().clamp_min(1)
    adv_var  = ( ((advantages - adv_mean) * completion_mask)**2 ).sum() / completion_mask.sum().clamp_min(1)
    advantages = (advantages - adv_mean) / (adv_var.sqrt() + 1e-8)

    # ----------------------------------------
    # Cache old logprobs for PPO ratios
    # ----------------------------------------
    # Important: logprobs_old are the logprobs under the behavior policy used to collect the data.
    # They MUST remain fixed during all K optimization epochs of this iteration. Update them only
    # after θ_old ← θ at the end of the iteration (i.e., after new rollouts are collected).
    old_logprobs = logprobs_old                                            # (B, L)

    # ----------------------------------------
    # Two-loop PPO -- Inner optimization loop: K epochs over minibatches
    # ----------------------------------------
    for epoch in range(ppo_epochs):
        for mb in iterate_minibatches(prompts, responses, old_logprobs, advantages, rewards_per_token,
                                      values, completion_mask, size=minibatch_size):

            mb_prompts, mb_responses, mb_old_logprobs, mb_adv, mb_rewards_tok, mb_vals, mb_mask = mb

            # Recompute current logprobs for sampled tokens (on-policy evaluation under latest θ)
            new_logprobs = policy_model.logprobs(mb_prompts, mb_responses)         # (mB, L)

            # PPO ratio and clipped objective (token-level)
            ratio = (new_logprobs - mb_old_logprobs).exp()                          # (mB, L)
            clipped_ratio = ratio.clamp(1 - epsilon, 1 + epsilon)
            policy_loss_tok = -torch.minimum(ratio * mb_adv, clipped_ratio * mb_adv)  # (mB, L)

            # Mask, then average over sequence and batch
            # The sum() below collapses token-level losses into one per example,
            # masking out padded tokens. The division normalizes by the number of valid tokens.            
            policy_loss = (policy_loss_tok * mb_mask).sum(dim=-1) / mb_mask.sum(dim=-1).clamp_min(1)
            # Then another mean() averages across batch by taking the mean of those per-example losses.            
            policy_loss = policy_loss.mean()

            # Critic loss: MSE between values and targets
            # Outcome-level: target is rewards_outcome broadcast to tokens (mb_rewards_tok).
            # Process-level: target is token_rewards - β*KL per token (already in mb_rewards_tok).
            new_values = value_model.values(mb_prompts, mb_responses)               # (mB, L)
            value_mse_tok = (new_values - mb_rewards_tok) ** 2                      # (mB, L)
            # The sum() below accumulates the squared error over valid tokens for each example.
            # Division by mb_mask.sum() normalizes per example, yielding average MSE per sequence.            
            value_loss = (value_mse_tok * mb_mask).sum(dim=-1) / mb_mask.sum(dim=-1).clamp_min(1)
            # This mean() takes the mean over the minibatch to get a single scalar loss.            
            value_loss = value_loss.mean()

            # (Optional) entropy bonus to encourage exploration
            # entropy = policy_model.entropy(mb_prompts, mb_responses)              # (mB, L)
            # entropy_loss = -entropy.mean()
            # policy_loss = policy_loss + ent_coef * entropy_loss

            # Important: update actor and critic with separate losses/optimizers.
            # (They can be combined for convenience when parameters are shared.)
            policy_model.optimizer.zero_grad()
            policy_loss.backward()
            policy_model.optimizer.step()

            value_model.optimizer.zero_grad()
            value_loss.backward()
            value_model.optimizer.step()

    # After K epochs on this batch, follow PPO and set θ_old ← θ by simply using
    # the updated policy to collect the next batch. Do NOT recompute logprobs_old here;
    # they are recomputed from scratch next iteration during rollout with the new policy.

    # Optional logging
    # log_metrics(iteration, policy_loss, value_loss, kl_seq.mean(), rewards_outcome.mean())
```

#### Key Steps

##### Actor–Critic Coordination

* The **policy model (actor)** and **value model (critic)** are trained in parallel but with **separate loss functions** and optimizers.
* The actor maximizes the PPO surrogate objective to improve the probability of high-advantage actions (tokens).
* The critic minimizes mean-squared error between its predicted values and the observed or outcome-based reward signals.
* Although they are optimized independently, the two updates occur within the same iteration to maintain synchronized learning.
* (When the actor and critic share parameters, these loss terms can be combined into a single joint objective for convenience.)

##### Advantage Estimation

* The advantage signal \(\hat{A\_t} = r\_t - V\_\psi(s\_t)\) measures how much better each sampled token (or sequence) performed relative to the baseline, i.e., the critic’s expected value.
* **Outcome-level rewards:** when only a single scalar reward is provided per completion, it is broadcast across all tokens to provide per-step training signals.
* **Process/token-level rewards:** if the reward model produces token-wise rewards, they directly replace \(r\_t\), enabling fine-grained credit assignment across the generated sequence.
* Advantages are normalized within the batch to reduce variance and stabilize the gradient updates.

##### PPO Clipping Mechanism

* The policy ratio \(\rho\_t = \frac{\pi\_\theta(a\_t \mid s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t \mid s\_t)}\) bounds how far the updated policy can deviate from the behavior policy used to generate data.
* The ratio is clipped to \([1-\epsilon, 1+\epsilon]\), enforcing conservative policy updates and avoiding large jumps in token probabilities.
* Each rollout batch is reused for several **PPO epochs** of minibatch optimization before collecting new samples, following the **two-loop** PPO structure introduced by Schulman et al.

##### KL Penalty and Alignment Stability

* A **per-token KL term** between the current policy \(\pi\_\theta\) and the frozen reference \(\pi\_{\text{ref}}\) (typically the supervised SFT model) serves as a regularizer.

  + For outcome-level RLHF, the per-token KL values are averaged or summed across the sequence and subtracted from the scalar reward:

    \[R\_{\text{adj}} = R\_{\text{outcome}} - \beta \text{KL}(\pi\_\theta \mid\mid \pi\_{\text{ref}})\]
  + For process-level RLHF, the same per-token KL penalties are applied directly to the token rewards:

    \[r\_t^{\text{adj}} = r\_t - \beta \text{KL}\_t(\pi\_\theta \mid\mid \pi\_{\text{ref}})\]
* This term follows the RLHF formulation \(r' = r - \beta [\log \pi\_\theta(y \mid x) - \log \pi\_{\text{ref}}(y \mid x)]\) and keeps the model aligned with the base policy while still permitting reward-driven improvements.
* The dynamic KL penalty curbs divergence from the supervised baseline, mitigating reward hacking and mode collapse.

##### Logprob Management and PPO Two-Loop Structure

* `logprobs_old` must represent the action log-probabilities under the **policy that generated the current batch**.

  + They remain **frozen** throughout all \(K\) PPO epochs of that iteration.
  + After completing the inner optimization loop, the updated policy implicitly becomes the new behavior policy for the next rollout, and `logprobs_old` are refreshed during data collection.
* This separation between rollout (data gathering) and optimization phases ensures theoretical PPO consistency and stable learning dynamics.

##### Training Dynamics and Outcomes

* Across iterations, the actor learns to generate completions that balance reward maximization with linguistic alignment to the supervised base model.
* The critic continually refines its value predictions, providing more accurate baseline estimates for future advantage computations.
* The framework natively supports both:

  + **Outcome-level RLHF:** sequence-level reward shaping through aggregated KL penalties.
  + **Process-level RLHF:** token-wise optimization using intermediate reward and KL feedback.
* Over time, this coordinated actor–critic training leads to policies that improve reward-aligned quality while maintaining fluency and behavioral consistency with the original supervised language model.

### Model Roles

* To implement the RLHF pipeline effectively, several models are employed in distinct but interdependent roles. Each contributes to a part of the reward-driven learning loop, from generating responses to evaluating and optimizing them:

  + **Policy model**: The main LLM we wish to optimize (parameterized by \(\theta\)). It functions as the environment’s actor, generating responses, and is fine-tuned via policy optimization techniques (e.g., PPO).
  + **Reference model**: A frozen or slowly-updated baseline version of the policy (or a supervised fine-tuned model) used to compute KL or likelihood penalties to ensure the optimized policy does not diverge too far from acceptable behaviours.
  + **Value model**: A model that estimates the expected return (value) of a given prompt-response pair or sequence, often used to compute advantage estimates in actor–critic style updates.
  + **Reward model**: A separate model trained (often via human preference data or comparisons) to map a prompt-response pair \((x,y)\) to a scalar reward \(r(x,y)\). It encapsulates human or designer preferences and drives the optimization of the policy model.
* In typical LLM fine-tuning pipelines, the flow is:

  1. The **policy model** generates responses.
  2. The **reward model** scores them.
  3. The **value model** estimates future return or baseline.
  4. A **reference model** imposes a divergence penalty or acts as a safe anchor.
  5. Using a policy-optimization algorithm (e.g., Proximal Policy Optimization) the policy model is updated to **increase** rewards **while constraining** divergence from the reference.
* [Fine-Tuning Language Models with Reward Learning on Policy] by [Lang et al. (2024)](https://arxiv.org/abs/2403.19279) offers a more formal treatment of the entire flow.

#### Refresher: Notation Mapping between Classical RL and Language Modeling

* To relate standard RL notation to language-modeling–based policy optimization, it is helpful to make the correspondence between states, actions, trajectories, rewards, returns, and related terms explicit. Making these mappings explicit clarifies how classical RL concepts translate directly into the autoregressive language-model setting used in modern RLHF systems.
* Beyond this section, the \(x, y\) notation—where \(x\) denotes the prompt and \(y\) denotes the completion, rollout, or trajectory—is used for consistency with common LLM policy optimization implementations (such as RLHF, DPO-based, GRPO-based, etc.).

##### Core Terminology

* In classical RL, rewards are defined over **state–action pairs**:

  \[r(s\_t, a\_t)\]
* In the language-modeling setting, these concepts map naturally:

  + A **state** corresponds to a **prompt plus generated sequence prefix (i.e., partial completion)**:

    \[s\_t \leftrightarrow (x, y\_{1:t})\]
  + An **action** corresponds to generating the **next token**:

    \[a\_t \leftrightarrow y\_{t+1}\]

##### Trajectories, episodes, and completions

* A full **trajectory** or **episode** in RL corresponds exactly to a **completion** or **rollout** (also called a **response** or **sample**) in language modeling.
* Concretely, a completion:

  \[y = y\_{1:T}\]
  + … corresponds to a full RL trajectory:\[(s\_1, a\_1, s\_2, a\_2, \dots, s\_T, a\_T)\]

##### Reward representations

* The reward assigned to an entire completion is written in prompt–completion form as:

  \[r(x, y)\]
  + where \(x\) is the prompt and \(y = y\_{1:T}\) is the full generated response
* Concretely, the reward for a completion or trajectory can be expressed as the sum of step-wise rewards:

  \[r(x, y\_{1:T})
  \equiv
  \sum\_{t=1}^{T} r(s\_t, a\_t)\]
* This single expression subsumes both reward formulations:

  + For **outcome-based (i.e., terminal-only) rewards**, the sum reduces to a single terminal term.
  + For **process-based (i.e., step-wise) rewards**, the sum includes intermediate step-wise contributions.

##### Returns, values, and expectations

* In classical RL, the **return** refers to the cumulative reward along a trajectory. When conditioned on the current state, it is more precisely the **expected future reward**:

  \[R(s\_t)
  \equiv
  \mathbb{E}\Big[ \sum\_{k=t+1}^{T} r(s\_k, a\_k) \big| s\_t \Big]\]
* In the realm of policy optimization for LLMs, this corresponds to the **expected cumulative reward of the remaining completion** given the current prefix.
* The **value model** (critic) estimates the expected future reward over all possible continuations under the policy:

  \[V\_\psi(s\_t) = \mathbb{E}[R \mid s\_t]\]

##### Policy, actions, and distributions

* Additional terminology mappings commonly used across the two domains include:

  + **Policy** \(\pi(a\_t \mid s\_t) \leftrightarrow\) **Language model** \(\pi(y\_{t+1} \mid x, y\_{1:t})\)
  + **Action distribution** \(\leftrightarrow\) **Next-token distribution over vocabulary**
  + **Environment transition** \(s\_{t+1} \sim P(\cdot \mid s\_t, a\_t) \leftrightarrow\) **Autoregressive update** \(s\_{t+1} = (x, y\_{1:t+1})\)

##### Advantage and learning signals

* In classical RL, policy optimization uses the **advantage**:

  \[\hat{A\_t} = R(s\_t) - V(s\_t)\]
* In RLHF, this maps to comparing the realized reward of a completion against the value model’s baseline for the prefix:

  \[\hat{A\_t} = r(x, y\_{1:T}) - V\_\psi(x, y\_{1:t})\]
  + … for outcome-based rewards, with analogous extensions for process-based rewards

##### Preference optimization vs. general policy optimization for LLMs

* **Preference optimization** in RLHF can be understood as a direct instantiation of **classical RL policy optimization**, where the reward function is derived from human preferences. In this setting, the policy (the LLM checkpoint obtained after the SFT step) is optimized to maximize a learned reward model that approximates human values such as helpfulness, correctness, and safety. Concretely, optimizing a policy with respect to rewards \(r(x,y)\) learned from human comparisons is equivalent to optimizing expected return \(\mathbb{E}\_{y \sim \pi(\cdot \mid x)}[r(x,y)]\), which is the standard RL objective applied to autoregressive language generation.
* Historically, this framing motivated the term **RLHF**, where RL was primarily viewed as a mechanism for **aligning LLM behavior with human preferences**. Under this lens, preference optimization is simply policy optimization where the environment’s reward signal is replaced by a human-aligned surrogate.
* More recently, however, RL-style **policy optimization for LLMs** has expanded well beyond preference optimization. Modern applications increasingly use RL to train LLMs as **decision-making agents**, where rewards encode task success, coordination efficiency, or long-horizon objectives rather than human preference alone. Examples include:

  + **Agentic tool use**, where actions correspond to tool calls or API invocations and rewards reflect task completion or correctness
  + **Multi-agent workflows**, where multiple LLM-based agents must coordinate sequences of actions, communicate intermediate states, and jointly optimize shared or partially aligned objectives across environments and tools
  + **Long-horizon reasoning and planning**, where rewards are delayed and depend on multi-step outcomes
* + In these settings, the reward signal may be **programmatic (rule-based)**, **learned (discriminative)**, **generative** (e.g., using an LLM-as-a-Judge or a panel of such judges), or a **combination of these components**, rather than purely preference-based. As a result, **policy optimization** has become the more general and central abstraction, with preference optimization representing a special case focused specifically on human-value alignment.
* Viewed this way, RLHF sits on a broader spectrum of LLM policy optimization methods—including PPO-based, DPO-based, GRPO-based, and agent-centric RL approaches—all of which share the same underlying RL structure but differ in how rewards are defined, structured, and obtained.
* In summary, preference optimization is best understood as **policy optimization for aligning LLMs with human values**, while modern RL for LLMs increasingly emphasizes **general-purpose policy optimization** for acting, reasoning, and coordinating within complex, multi-agent environments.

#### Policy Model

* The **policy model** in an RLHF–style setup is the LLM that we treat as a policy \(\pi\_{\theta} (y \mid x)\), parameterized by \(\theta\), which given an input prompt \(x\) produces a response \(y\). This section covers its function, typical architecture, training data, and model size considerations.
* The policy model is the central actor in the RLHF pipeline: it generates responses to prompts and is updated to align with human preferences. It carries the full representational capacity of a large LLM architecture, is trained in multiple phases (pretraining \(\rightarrow\) SFT \(\rightarrow\) RLHF), and must be large enough to enable high-quality responses while still being trainable. Its design must support computing log-probabilities, KL divergences, and synergy with reward/value models.

##### Function

* The policy model is the **agent** that interacts with the “environment” by generating outputs (responses \(y\)) to prompts \(x\).
* Its objective is to maximize a **reward signal** \(r(x,y)\), subject to constraints or regularization (for example via KL-divergence to a reference policy).
* Formally, the objective can be written as:

  \[\max\_{\theta} \mathbb{E}\_{x\sim D\_{\rm prompt}, y\sim\pi\_\theta(\cdot\mid x)}\Big[r(x,y) - \beta\mathrm{KL}\big(\pi\_\theta(\cdot\mid x) \mid\mid \pi\_{\rm ref}(\cdot\mid x)\big)\Big]\]
  + where:

    - \(r(x,y)\): reward signal from human preference or a learned reward model
    - \(\pi\_{\rm ref}\): reference (often supervised-finetuned) policy
    - \(\beta\): KL regularization coefficient balancing reward maximization and divergence from the reference policy
* During training, the policy model generates responses, receives reward model scores or value-model feedback, and is updated (often via algorithms like Proximal Policy Optimization). The policy model thus evolves from a “supervised fine-tuned” base model into a behaviour-aligned model.
* The policy model must balance **helpfulness**, **accuracy**, **safety**, and **alignment** (for example to human preferences). See, for example, the instruct-tuning phase described in [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022).

##### Architecture

* The policy model is typically a **causal (autoregressive) transformer** with large scale: e.g., dozens of layers, high hidden dimensionality, multi-head self-attention, positional embeddings, etc.
* Initially pretrained on massive corpora of text. Then often fine-tuned via Supervised Fine-Tuning (SFT) on instruction–response pairs.
* For RLHF, a further head or mechanism may be added or used for value/advantage estimation, but the core remains the transformer.
* Recent work sometimes uses **parameter efficient tuning** (e.g., LoRA, adapters) to limit full-model updates during RL optimisation.
* The architecture must support sampling from \(\pi\_\theta\), computing log-probabilities \(\log \pi\_{\theta} (y \mid x)\), and computing KL divergence between \(\pi\_\theta\) and \(\pi\_{\rm ref}\).
* For instance, *Fine-Tuning Language Models with Reward Learning on Policy* by [Lang et al. (2024)](https://arxiv.org/abs/2403.19279) explores how the policy model interacts with a reward model under RLHF.

##### Training Data

* **Pretraining**: The policy model is first trained on large unlabeled text corpora (e.g., hundreds of billions to trillions of tokens).
* **Supervised Fine-Tuning (SFT)**: Instruction–response pairs collected from humans or human-augmented data; e.g., prompts with “good” responses. Many alignment pipelines begin with this stage to provide a reasonable starting policy.
* **RL Finetuning**: The model generates responses to prompts; responses are scored (via reward model or human ranking). This prompt–response–reward dataset is used in the reinforcement signal. Because the distribution of responses changes as \(\pi\_{\theta}\) updates, continuing to sample from updated policy is important.
* **Replay / Off-Policy Data**: Some pipelines incorporate past responses and reward scores into replay buffers or datasets for stability and reuse.
* Training the policy model via RL typically uses batches of prompt–response pairs, plus log-probabilities of responses under both \(\pi\_{\theta}\) and \(\pi\_{\rm ref}\), plus the advantage estimate from a value model.
* **Note:** Human preference data (for reward model) is often relatively small compared to the pretraining corpus; the RL step amplifies it via policy-generated samples.

##### Typical Model Size

* The policy model used in RLHF pipelines tends to be **large** (tens of billions of parameters or more) to provide strong language understanding and generation capabilities.
* For example, many state-of-the-art systems use models in the 7B–70B parameter range or larger (100B+).
* During SFT and then RLHF, often only the base model (e.g., 20B–70B) is used, to manage compute cost and stability. For example, the InstructGPT series used the GPT-3 175B model for SFT, then RLHF (cf. [Ouyang et al. (2022)](https://arxiv.org/abs/2203.02155)).
* In practice, training or fine-tuning such large policy models via RL requires specialized distributed compute, large memory, and careful hyper-parameter tuning.

#### Reference Model

* The **reference model** (also sometimes called the **anchor model**) is a fixed or slowly updated copy of the policy model used as a *baseline* or *constraint* in RLHF and related policy optimization setups for LLMs. Its primary purpose is to ensure that the updated policy model remains **linguistically coherent**, **safe**, and **semantically aligned** with the pre-RL distribution, while still learning to maximize the new reward signal. Put simply, the reference model plays a crucial safety and stability role in RLHF. It anchors the optimization process by maintaining linguistic and factual consistency, ensuring that policy optimization leads to meaningful alignment rather than degenerate exploration.

##### Function

* The reference model \(\pi\_{\text{ref}}(y \mid x)\) acts as a **stability regulator** during the RL phase.
  + It appears in the **KL-divergence regularization term** in the RL objective:

    \[J(\theta) = \mathbb{E}\_{x, y \sim \pi\_\theta}
    \big[
    r(x,y) - \beta \mathrm{KL}(\pi\_\theta(\cdot \mid x) \mid\mid \pi\_{\text{ref}}(\cdot \mid x))
    \big]\]
    - where \(\pi\_\theta\) is the policy model being optimized, and \(\beta\) is a scaling factor.
  + The KL term penalizes deviations from the reference model distribution, preventing **mode collapse**, **reward hacking**, or **drift** into incoherent or unfaithful responses.
* Conceptually, the reference model anchors the optimization so that:

  + The policy model can explore higher-reward regions of response space.
  + But does not diverge too far from its pretrained linguistic and factual priors.
* In practice, the reference model helps maintain **fluency**, **truthfulness**, and **diversity** of outputs throughout training.

##### Architecture

* The reference model is architecturally **identical** to the policy model. It is often just a **frozen copy** of the supervised fine-tuned (SFT) model.
* Example pipeline:

  1. Begin with a pretrained transformer (e.g., GPT-3, Llama, or PaLM).
  2. Fine-tune it with instruction data \(\rightarrow\) **SFT model**.
  3. Clone the SFT model \(\rightarrow\) **Reference model (frozen)**.
  4. Train another copy \(\rightarrow\) **Policy model (trainable)** with PPO or another RL optimizer, using the frozen reference for KL regularization.
* Since it shares weights and architecture with the policy model, the reference model uses a **causal decoder-only transformer**, typically with the same number of layers, hidden dimensions, and parameters.
* The architectural identity ensures that **token-wise probability distributions** are directly comparable, allowing exact computation of
  \(\mathrm{KL}(\pi\_\theta(\cdot \mid x) \mid\mid \pi\_{\text{ref}}(\cdot \mid x))
  = \sum\_y \pi\_\theta(y \mid x) \log\frac{\pi\_\theta(y \mid x)}{\pi\_{\text{ref}}(y \mid x)}.\)
* Some implementations (e.g., [Stiennon et al., 2020](https://arxiv.org/abs/2009.01325), “Learning to summarize with human feedback”) experimented with slowly updating the reference model, but most production pipelines freeze it entirely.

##### Training Data

* The reference model is not trained during the RL stage.
  Instead, it is a **snapshot** of the model before RLHF fine-tuning.
* It is trained in the **supervised fine-tuning (SFT)** phase using instruction-following data such as:

  + Prompt–response pairs written or rated by humans.
  + Curated high-quality datasets covering Q&A, summarization, code generation, reasoning, and dialog.
* The SFT dataset is usually **smaller** and more human-curated than pretraining data—ranging from a few thousand to a few hundred thousand high-quality examples.
* By preserving this SFT policy, the reference model embodies the **linguistic priors** and **alignment baseline** learned from human demonstrations before introducing reinforcement signals.

##### Typical Model Size

* The reference model must match the policy model in architecture and vocabulary to make KL computation meaningful.
  Therefore, it has the **same parameter count** as the policy model—commonly in the range of:

  + **7B–70B parameters** for research-grade or open-source systems (e.g., Llama-2, Falcon, Mistral RLHF variants).
  + **175B–500B+ parameters** for frontier models (e.g., GPT-3 or GPT-4 scale).
* Because the reference model is frozen, its storage and compute requirements are primarily for **forward passes** during KL evaluation rather than gradient updates.
* In distributed training pipelines (e.g., [Ouyang et al., 2022](https://arxiv.org/abs/2203.02155)), both the policy and reference models are sharded across GPUs but only the policy model receives gradient updates.

##### Comparative Analysis

| **Aspect** | **Description** |
| --- | --- |
| **Role** | Baseline distribution constraining RL updates |
| **Function** | Provides KL regularization to prevent policy drift |
| **Architecture** | Identical to policy (decoder-only transformer) |
| **Training Data** | SFT instruction data (high-quality human responses) |
| **Model Size** | Same as policy; typically 7B–175B parameters |
| **Status During RL** | Frozen (no updates) |

#### Reward Model

* The **reward model (RM)** is one of the most crucial components in the RLHF pipeline.
* It provides the **scalar feedback signal** \(r(x, y)\) that quantifies the quality of a model’s response \(y\) to a prompt \(x\), translating human preferences into a form usable by RL algorithms.
* In modern LLM alignment, the reward model serves as the **surrogate objective** for human satisfaction, steering the policy model toward behaviors that humans find helpful, truthful, and safe.
* The reward model provides the **human-aligned feedback mechanism** that guides RL updates. It bridges subjective human judgment and quantitative optimization, serving as the anchor for policy alignment and safety in LLM fine-tuning.

##### Function

* The reward model approximates a **latent human preference function**. Given a prompt \(x\) and a response \(y\), the model outputs a scalar value \(r(x,y)\) representing how much a human would prefer that response.
* Its primary role is to act as a **critic** that scores generated text, so that the **policy model** can be optimized to produce higher-reward responses.
* Formally, the goal is to learn a function \(r\_\phi(x,y) \approx \text{Expected human preference score}(x,y)\), parameterized by \(\phi\).
* The reward model is trained using **human preference data** collected as pairwise or ranked comparisons. The reward modeling methodology — from ranking-based supervision and cross-entropy loss to normalization — originates from [Learning to Summarize from Human Feedback](https://arxiv.org/abs/2009.01325) by Stiennon et al. (2020) and was directly integrated into [Training Language Models to Follow instructions with Human Feedback](https://arxiv.org/abs/2203.02155) (InstructGPT) by Ouyang et al. (2022), forming the standard foundation of modern RLHF systems.
* The image below [(source)](https://huggingface.co/blog/rlhf) illustrates how a reward model functions:

* In [Stiennon et al. (2020)](https://arxiv.org/abs/2009.01325), the RM was trained on a dataset of **comparisons between two model outputs** on the same input. They used a cross-entropy loss, with the comparisons as labels—the difference in rewards represents the log odds that one response will be preferred to the other by a human labeler. This approach was later adopted and extended in [Ouyang et al. (2022)](https://arxiv.org/abs/2203.02155), which used this same reward model formulation as the basis of their RLHF training pipeline, with the following changes to sample creation and batching strategy:

  + In order to **speed up comparison collection** (i.e., reduce labeling effort per prompt by ranking multiple responses at once), each labeler is presented with anywhere between \(K = 4\) and \(K = 9\) responses to rank — larger \(K\) values mean more comparisons per labeling task and richer training signal. This ranking procedure automatically generates up to \(K^2\) pairwise comparisons per prompt (since every possible pair of completions produces one “win/loss” label).
  + However, because these \(K^2\) comparisons are **highly correlated** within the same labeling task, simply shuffling and treating each pair as an independent datapoint led to severe **overfitting** — the reward model quickly memorized specific completions and degraded generalization.
  + Specifically, if each of the \(K^2\) comparisons is treated separately, then each completion may appear in \(K-1\) distinct pairs, resulting in multiple redundant gradient updates per sample. The authors observed that under this setup, the model **overfit within a single epoch**, and even reusing the data within an epoch caused further overfitting.
  + To mitigate this, they changed the training approach to treat **all \(K^2\) comparisons for a given prompt as a single batch element**. This ensures that every completion is processed only once per batch while still contributing to all necessary pairwise comparisons. This modification was both **computationally efficient**—requiring only one forward pass of the reward model per completion instead of \(K^2\)—and **empirically superior**, yielding much improved **validation accuracy and log loss**. This batching strategy adopted by [Ouyang et al. (2022)](https://arxiv.org/abs/2203.02155) became a standard approach, forming a key component of modern RLHF reward model training.

##### Architecture

* The reward model is typically a model derived from the same family as the policy model, sharing the same backbone architecture but differing in its **output head** and **training objective**. While some early or alternative setups explored encoder-based reward models, the canonical and most widely adopted approach—used in [InstructGPT](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022) and all modern large-scale RLHF pipelines—is **decoder-only**, consistent with the architecture of the policy (causal language) model. Architecturally, it’s identical to the policy model but with a **scalar regression head** added on top of the final hidden state.
  + In [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022), the reward model is based on the **GPT-3 architecture** (**specifically the 6B parameter variant**), a **decoder-only transformer** trained autoregressively. Per the paper, the reward model is **initialized from the supervised fine-tuned (SFT) model**, with the **language modeling head** removed which includes the **final unembedding layer** (i.e., the linear projection from hidden states to vocabulary logits, along with the subsequent softmax used for next-token prediction) and replaced by a **new linear head** that outputs a single real-valued reward for a given prompt–completion pair. This added linear layer is a regression head that maps the final hidden (i.e., output) representation to a scalar value representing the model’s predicted human preference score. Put simply, the reward model is architecturally identical to the base language model, except for the replacement of the language modeling head (i.e., next-token prediction head) with a **linear regression head** applied to the final hidden state that outputs a scalar value.
* Mathematically speaking, the final token’s hidden representation \(h\_T\) (or an average over all tokens) is passed through a linear projection to output \(r\_\phi(x,y)\) a **single scalar reward** representing the model’s predicted human preference for the given prompt–completion pair.

  \[r\_\phi(x,y) = w^\top h\_T + b\]
  + where \(w,b\) are learned parameters.
* The model therefore learns to encode text sequences and output a **single continuous reward value**, capturing human preference judgments.
* In practice:

  + The scalar head is lightweight (a single dense linear layer).
  + The underlying transformer backbone (6B parameters in InstructGPT) is initialized from the SFT model, preserving its linguistic and contextual knowledge.
  + During RM training, only the new scalar head and a subset of backbone parameters may be fine-tuned for efficiency and stability.
* Several architectural variants are used for reward modeling, including:

  1. **LM Classifiers**: Language models fine-tuned as binary classifiers to score which response better aligns with human preferences.
  2. **Value Networks**: Regression models that predict scalar ratings representing relative human preference.
  3. **Critique Generators**: Language models trained to generate evaluative critiques explaining which response is better and why, used in conjunction with instruction tuning.

##### Training Objective

###### Background: Bradley-Terry Model

* The reward model is trained using human-ranked comparison data and assigns a scalar score to each complete model-generated response conditioned on a prompt. Like we discussed in the [Architecture](#architecture-2) section earlier, architecturally, it is a GPT-style transformer that takes the concatenation of the prompt and the full response as input and outputs a single scalar value.
* Human preferences are modeled implicitly with a preference-based loss, using a pairwise Bradley–Terry (logistic) choice model. Given a prompt \(p\) and two candidate responses \(r\_i\) and \(r\_j\), the probability that a human rater prefers \(r\_i\) over \(r\_j\) is defined as:

  \[P(r\_i > r\_j \mid p) = \sigma \left(r\_\phi(p, r\_i) - r\_\phi(p, r\_j)\right) = \frac{\exp(r\_\phi(p, r\_i))}{\exp(r\_\phi(p, r\_i)) + \exp(r\_\phi(p, r\_j))}\]
* Intuitively:
  + If \(r\_\phi(x, y\_1) \gg r\_\phi(x, y\_2)\), then \(P(y\_1 \succ y\_2 \mid x) \to 1\).
  + If the scores are equal, \(r\_\phi(x, y\_1) = r\_\phi(x, y\_2)\), then \(P(y\_1 \succ y\_2 \mid x) = 0.5\).
  + Only the difference in rewards matters: \(P(y\_1 \succ y\_2 \mid x) = \sigma \left(r\_\phi(x, y\_1) - r\_\phi(x, y\_2)\right)\), i.e., any additive shift \(r\_\phi(x, y) \mapsto r\_\phi(x, y) + c\) leaves the preference probabilities unchanged.
* The reward model is trained by maximizing the likelihood of observed human preferences using the corresponding pairwise loss:

  \[L(\phi) = -\log \sigma(r\_\phi(p, r\_i) - r\_\phi(p, r\_j))\]
  + where:

    - \(\sigma\) is the sigmoid function,
    - \(r\_\phi\) is the reward model,
    - \(p\) is the prompt,
    - \(r\_i\) is the human-preferred response and \(r\_j\) the human-dispreferred one.
* This formulation ensures that the reward model learns to assign higher scores to responses more preferred by humans. In other words, the reward model learns a latent scalar scoring function over prompt–response pairs such that **differences in scores model/approximate human preference probabilities**.

###### InstructGPT’s Pairwise Cross-entropy Ranking Loss

* [Ouyang et al. (2022)](https://arxiv.org/abs/2203.02155) offers a practical implementation of the Bradley–Terry formulation. The paper proposes training the reward model with a pairwise cross-entropy ranking loss: the sigmoid of the reward difference defines a Bernoulli probability that one completion (i.e., the winner \(y\_w\)) is preferred over another (i.e., the loser \(y\_l\)), and optimizing it with the cross-entropy (negative log-likelihood) of the observed one-hot preference label under this Bernoulli model.

  \[L\_{\text{RM}}(\theta)
  = -\frac{1}{\binom{K}{2}}
  \mathbb{E}\_{(x, y\_w, y\_l) \sim D}
  \Big[\log \sigma\big(r\_\phi(x,y\_w) - r\_\phi(x,y\_l)\big)\Big]\]
  + where:

    - \(y\_w\) is the **preferred** (or winning) completion,
    - \(y\_l\) is the **dispreferred** (or losing) completion,
    - \(\sigma\) is the sigmoid function mapping the score difference to a probability of preference,
    - \(r\_\phi(x, y)\) is the reward model’s scalar output.
    - The **difference** \(r\_\phi(x,y\_w) - r\_\phi(x,y\_l)\) represents the **log odds** that a human would prefer \(y\_w\) over \(y\_l\).
* **Normalization and Practical Notes**:

  + In practice, labelers rank \(K\) responses for the same prompt. All induced pairwise comparisons are used jointly, but the reward model computes each response score only once per prompt, improving stability and preventing overfitting.
  + Since **only reward differences matter**, the reward model’s loss is **invariant to additive shifts** in the reward function. Accordingly, the reward model is normalized by adding a bias term so that **labeler demonstrations have mean score 0** before PPO training begins. This normalization fixes the otherwise arbitrary offset of the reward function, ensuring that the scale and baseline of rewards remain consistent across updates and thereby stabilizing policy learning.
  + A **key implementation detail** during RLHF with PPO is that the **partial responses** produces a single scalar for the entire prompt–response pair. Partial responses receive no terminal reward (i.e., practically, a reward of 0); a non-zero scalar scalar reward is only applied once a **complete response** is generated. This encourages the policy to produce coherent, complete outputs rather than optimizing for high-reward prefixes.

##### Training Data

* The training data for reward models comes from **human preference labeling**:

  + A set of prompts \(x\) is sampled (often from SFT datasets or model-generated prompts).
  + Multiple responses are generated by one or more models.
  + Human annotators rank or choose preferred responses based on **helpfulness**, **accuracy**, **harmlessness**, or **style** criteria.
* The collected comparisons yield tuples \((x, y\_w, y\_l)\), forming the basis for pairwise training.
* Datasets of this form can range from **50,000 to several million comparisons**, depending on the scale of the deployment.
  For example:

  + The **InstructGPT** reward model used approximately **30,000–40,000 labeled comparisons**.
  + Larger RLHF systems (e.g., Anthropic’s Constitutional AI) use **100K–1M+** pairs.
  + Recent work such as **RLHF on Llama 2** and **OpenAI’s GPT-4-turbo alignment** use data from extensive human evaluation and preference modeling pipelines.
* **Synthetic preference data** (generated using smaller models or heuristics) is also increasingly used to supplement limited human data, as in [Self-Instruct](https://arxiv.org/abs/2212.10560) by Wang et al. (2022).

##### Model Size

* The reward model is usually **smaller** than the policy model (especially since it doesn’t have to incorporate the unembedding layers), since it only provides scalar evaluations and doesn’t need to generate text.

  + Common sizes range from **1B to 13B parameters** for large-scale pipelines.
  + For example:
    - InstructGPT used reward models of **6B parameters**, while the policy model was 175B.
    - Open-source Llama 2–Chat models used reward models of **7B–13B parameters**.
  + Compact reward models are often used to reduce the cost of reward evaluation during RLHF training (since thousands of responses must be scored per update).
* Some recent methods, such as [**Direct Preference Optimization (DPO)**](https://arxiv.org/abs/2305.18290) by Rafailov et al. (2023), avoid training a separate reward model altogether, instead **implicitizing** it through log-probability ratios between the policy and reference models.

##### Prevention of Over-optimization

* To prevent the fine-tuned model from overfitting or drifting too far from its pretrained distribution, **KL divergence penalties** are applied during RL:

  + KL divergence measures the difference between the output distributions of the current policy and the original (pretrained) model.
  + This constraint regularizes learning and **ensures that the fine-tuned model does not deviate excessively**, preserving safety and coherence.
* This KL penalty is crucial for maintaining a balance between alignment and generalization.

##### Evaluation and Monitoring

* Reward models are evaluated on **held-out preference sets** using accuracy metrics—how often the model correctly predicts the human-preferred response.
* Typical accuracy benchmarks range between **65–80%**, depending on domain and data quality.
* Regular retraining and drift monitoring are essential, since the distribution of policy outputs changes as the policy improves.

##### Outcome-Based vs. Process-Based Rewards

###### Overview

* In the language-modeling setting, a state corresponds to the prompt plus the generated sequence prefix, and an action corresponds to predicting the next token. Viewing the reward as a function of state–action pairs \(r(s\_t, a\_t)\), this perspective naturally extends to language modeling, where the reward for an entire completion can be expressed in prompt–completion form as:

  \[r(x, y)\]
  + where \(x\) is the prompt and \(y = y\_{1:T}\) is the full generated response. Note that this formulation applies regardless of the reward definition, i.e., to both **outcome-based** rewards (where the reward is assigned only once at the end of the completion) and **process-based** rewards (where rewards are assigned at intermediate steps and aggregated over the sequence). A detailed discoruse on outcome-based vs. process-based rewards has been offered in the following sections.
* Concretely, the reward for a full completion can be written as the sum of step-wise state–action rewards:

\[r(x, y\_{1:T}) \equiv \sum\_{t=1}^{T} r(s\_t, a\_t)\]

* The distinction between **outcome-based** and **process-based** rewards concerns *when* and *how* the reward model assigns supervision, which in turn determines how learning signals are distributed across a generated sequence. Specifically, in the **outcome-based** case, the sum reduces to a single terminal reward term, whereas in the **process-based** case it includes intermediate step-wise contributions throughout generation.

###### Outcome-based rewards

* In an **outcome-based** (i.e., terminal-only) formulation, the reward model assigns a single scalar reward only after the full completion has been generated. For a prompt \(x\) and full completion \(y\_{1:T}\), the reward is:

  \[r\_\phi(x, y\_{1:T}) \in \mathbb{R}\]
  + This reward is a realized (i.e., observed) quantity, defined only once the entire response has been produced and evaluated, and reflects a holistic human judgment of the completed output.
* Because rewards are assigned **only at the end of the episode**, the return from any intermediate state
  \(s\_t = (x, y\_{1:t})\) is defined as the **future terminal reward** that will be obtained once the completion finishes:

  \[R(s\_t) = r\_\phi(x, y\_{1:T})\]
  + … since all intermediate rewards are zero. The value model therefore estimates this expected terminal reward *in expectation* at intermediate prefixes (i.e., before the completion is finished) by averaging over all possible continuations under the current policy:\[V\_\psi(s\_t)
  =
  \mathbb{E}\_{y\_{t+1:T} \sim \pi\_\theta(\cdot \mid s\_t)}
  \big[
  r\_\phi(x, y\_{1:T})
  \big]\]
  + At intermediate prefixes, many completions are possible, so the value model integrates over this uncertainty induced by the policy’s continuation distribution.
  + Only at the terminal state \(s\_T\)—when the completion is fixed—does the expectation collapse to the realized reward \(r\_\phi(x, y\_{1:T})\).
* **Key properties:**

  + The reward evaluates the **entire response holistically**, capturing global attributes such as correctness, helpfulness, coherence, and safety.
  + No intermediate rewards \(r\_\phi(s\_t, a\_t)\) are produced; all tokens implicitly share the same terminal signal.
  + Credit assignment is delayed and relies on advantage estimation and the value model to propagate the terminal reward backward through the sequence.
* This formulation is standard in classical RLHF pipelines, where human preference data are collected over complete prompt–response pairs and the learning problem is effectively bandit-style, with one reward per episode.

###### Process-based rewards

* In a **process-based** (i.e., step-wise) formulation, the reward model emits rewards at intermediate generation steps. At each step \(t\), given the state \(s\_t = (x, y\_{1:t})\) and action \(a\_t = y\_{t+1}\), the reward model produces a step-wise reward \(r\_\phi(s\_t, a\_t)\). Here, the reward model evaluates *partial progress* rather than only the final outcome.
* The total return for a completion is then the sum of step-wise rewards:

  \[R(x, y\_{1:T}) = \sum\_{t=1}^{T} r\_\phi(s\_t, a\_t)\]
* Correspondingly, the value model estimates the expected remaining cumulative reward from a given prefix:

  \[V\_\psi(s\_t)
  = \mathbb{E}\_{y\_{t+1:T} \sim \pi\_\theta(\cdot \mid s\_t)}
  \Big[ \sum\_{k=t+1}^{T} r\_\phi(s\_k, a\_k) \Big]\]
  + As with outcome-based rewards, the value model averages over all possible future continuations, but now integrates multiple step-wise reward contributions instead of a single terminal signal.
* **Key properties:**

  + The reward evaluates **partial progress**, providing dense supervision during generation.
  + Credit assignment is more explicit, since individual steps receive localized reward signals.
  + This formulation is particularly useful when intermediate reasoning steps, structured progress, or tool use matter for overall quality.

###### Effect on training dynamics

* The choice between outcome-based and process-based rewards changes the statistical and optimization properties of the learning signal:

  + **Reward sparsity:**

    - Outcome-based rewards are sparse, producing a single terminal reward \(r\_\phi(x, y\_{1:T})\), whereas process-based rewards provide dense signals \(r\_\phi(s\_t, a\_t)\) at each step.
  + **Variance of advantage estimates:**

    - With outcome-based rewards, advantages \(\hat{A\_t} = r\_\phi(x, y\_{1:T}) - V\_\psi(s\_t)\) can have high variance, while process-based rewards reduce variance by decomposing the return across steps.
  + **Bias–variance tradeoff:**

    - Process-based rewards may reduce variance but can introduce bias if intermediate rewards are misspecified or misaligned with the final objective humans care about.
* Importantly, this distinction applies only to the **reward definition**, not to the role of the [value model](#value-model). The value model always estimates the expected cumulative return induced by the reward model:

  \[V\_\psi(s) = \mathbb{E}[R \mid s]\]
* In summary, outcome-based rewards answer “How good is the final answer?”, while process-based rewards answer “How good is each step toward the answer?”. Both formulations fit naturally within the same RLHF framework, with the value model adapting automatically to the reward structure through its estimation of expected return.

##### Comparative Analysis

| **Aspect** | **Description** |
| --- | --- |
| **Role** | Translates human preference into scalar rewards |
| **Training Objective** | Pairwise ranking loss on human preference data |
| **Architecture** | Transformer with scalar reward head |
| **Data** | Human-ranked prompt–response pairs (tens of thousands to millions) |
| **Model Size** | Typically 1B–13B parameters |
| **Reference Papers** | [Ouyang et al., 2022](https://arxiv.org/abs/2203.02155); [Rafailov et al., 2023](https://arxiv.org/abs/2305.18290) |

#### Value Model

* While the **reward model** provides scalar feedback signals evaluating model behavior—either as step-wise rewards during generation or as a terminal reward after a response is completed—the **value model** (also known as the **critic**) estimates the **expected cumulative future reward** from a given state or sequence prefix. This enables **advantage estimation**, **variance reduction**, and **stabilized policy updates**, which are foundational to modern policy-gradient methods such as PPO.
* In RLHF implementations such as [InstructGPT](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022), the **reward model** is first initialized from the supervised fine-tuned (SFT) policy by **removing the language modeling head** which includes the **final unembedding layer** (i.e., the linear projection from hidden states to vocabulary logits, along with the softmax used for next-token prediction) and **replacing it with a new linear head** that outputs a single real-valued scalar reward for each prompt–completion pair. This reward model is then **trained on human preference comparisons**.

  After the reward model has been trained, the **value model (critic)** is **initialized from this trained reward model** and used during PPO fine-tuning to compute advantages:

  \[\hat{A\_t} = r\_t - V(s\_t)\]
  + where \(r\_t\) is the realized scalar reward produced by the trained reward model, and \(V(s\_t)\) is the value model’s prediction of the expected cumulative reward from state \(s\_t\). This follows the standard actor–critic formulation used in PPO, with the critic providing a learned baseline that reduces variance and stabilizes policy updates .

##### Function

* In the context of LLM alignment, the value model \(V\_\psi(x)\) or \(V\_\psi(x, y)\) predicts the **expected return** (i.e., cumulative reward) for a given prompt \(x\) or prompt–response pair \((x,y)\). More precisely, it learns the expected cumulative reward under the policy’s full continuation distribution rather than the reward of any single sampled completion. In other words, it approximates the **probability-weighted average return over all trajectories that the current policy can generate from a given prompt**.
* It serves the same theoretical role as the **critic** in an actor–critic framework, providing a learned baseline that allows the policy (actor) to improve using lower-variance gradient estimates.
* The fundamental definition is:

  \[V\_\psi(s) \approx \mathbb{E}\_{a\sim\pi\_\theta} [R(s,a)]\]
  + where \(R(s,a)\) is the return or scalar reward obtained when the policy \(\pi\_\theta\) takes action \(a\) in state \(s\).
* In the language modeling context, the “state” corresponds to the **prompt or prefix** \(x\), and the “action” corresponds to the **generated token sequence** \(y\).
* The value model enables several key operations:

  1. **Advantage estimation:**
     + Used to compute a baseline-corrected signal for PPO or similar algorithms:\[\hat{A}(x,y) = r(x,y) - V\_\psi(x)\]
     + … or, at a token-wise level, via Temporal-Difference (TD) methods:\[\hat{A}\_t = \delta\_t + (\gamma \lambda)\hat{A}\_{t+1}\]
     + … with:\[\delta\_t = r\_t + \gamma V\_\psi(s\_{t+1}) - V\_\psi(s\_t)\]
     + In single-step environments (i.e., **bandit-style**) settings like RLHF (prompt \(\rightarrow\) response \(\rightarrow\) single reward), this simplifies to \(\hat{A\_t} = r\_t - V(s\_t)\), as the episode length is one. The short-horizon “bandit” structure still benefits from the critic, since it reduces gradient variance and hence, stabilizes training.
  2. **Variance reduction:**
     + By learning a baseline for expected reward, \(V\_\psi(s)\) removes state-dependent bias and allows the policy gradient to focus on relative action quality.
  3. **Critic-driven generalization:**
     + The critic can generalize expected reward patterns across prompts, enabling continual improvement even when human preference labels are unavailable.
  + These functions mirror classical actor–critic frameworks, such as those in [Konda and Tsitsiklis (2000)](https://papers.nips.cc/paper/2000/hash/60941600aaa93c7e3de7729355a0913e-Abstract.html), but are adapted to the autoregressive, token-level structure of language models.

##### Architecture

* Architecturally, the value model is typically a **decoder-only transformer**, sharing its structure with both the policy and reward models, but differing in its **output head** and **training objective**.
  + In the implementation described in [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022), all components—including the supervised fine-tuned (SFT) policy, the reward model, and the value model used for PPO fine-tuning—are based on the GPT-3 architecture (specifically the 6B parameter variant), a unidirectional transformer decoder trained on autoregressive language modeling. The value function is **initialized from the reward model**, which itself is **trained starting from the SFT model with the final unembedding layer removed and replaced with a new linear head** that outputs a **scalar regression value** for each prompt–completion pair. This added linear layer serves as a learned projection that maps the final hidden state representation of the sequence to a single scalar reward estimate. The same architectural modification is used for the value model, which learns to predict expected returns during RLHF.
* Mathematically speaking, the final token’s hidden representation \(h\_T\) (or an average over all tokens) is passed through a linear projection to output \(r\_\phi(x,y)\) a **single scalar reward** representing the model’s predicted human preference for the given prompt–completion pair.

  \[r\_\phi(x,y) = w^\top h\_T + b\]
  + where \(w,b\) are learned parameters.
* Put simply, the value model outputs a **single scalar estimate** \(V\_\psi(x)\) (or per-token estimates \(V\_\psi(x\_t))\), rather than next-token probabilities or pairwise reward scores.
* **Implementation details:**

  + The **hidden representation** of the final token (or the mean of hidden states) is passed through a **linear projection layer** to produce the scalar value prediction.
  + Architecturally, it may **share parameters** with the policy model up to the final projection layer, forming a multi-head actor–critic structure.
  + However, many implementations, including [**InstructGPT**](https://arxiv.org/abs/2203.02155), initialize the value model **separately** from the reward model rather than sharing parameters with the policy, ensuring that the two objectives—policy improvement and value estimation—do not interfere.
  + Some designs explicitly decouple the policy and value networks to prevent gradient interference between actor and critic signals, which helps maintain training stability.
* The **reason for a dedicated value model or value head** is that PPO (and more generally, actor–critic methods) rely on \(V(s)\) to compute advantages:

  \[\hat{A}(s,a) \approx r + \gamma V(s') - V(s)\]
  + In the short-horizon (**bandit-style**) case common in RLHF—where each episode consists of a **single scalar reward**—the episode terminates immediately after the action, so there is no next state \(s'\). By convention, the value of a terminal state is zero, i.e., \(V(s') = 0\), yielding the advantage expression \(\hat{A} =r - V(s)\).
  + Without a critic, the gradient estimator would have much higher variance, leading to instability.
* Additionally, LLMs define states as (prompt + partial generation) and actions as next tokens. Having a **separate value head or model** allows for stable and interpretable gradient flow through long token sequences.

##### Training Objective

* The value model is trained via a **Mean Squared Error (MSE)** regression objective to predict the expected cumulative reward (i.e., expected return) associated with a prompt:

  \[L\_V(\phi)
  =
  \mathbb{E}\_{(x,y) \sim D}
  \big[
  (V\_\psi(x) - \hat{R}(x,y))^2
  \big]\]
  + where:
    - \(V\_\psi(x)\) is the value model’s prediction for the prompt (or state) \(x\), intended to approximate \(\mathbb{E}\_{\tau \sim \pi\_\theta(\cdot \mid x)}[R(\tau)]\), the expected cumulative reward over all possible trajectories (completions) induced by the policy \(\pi\_\theta\), weighted by their probabilities.
    - \(\hat{R}(x,y)\) is the observed (i.e., realized) return associated with a **single sampled completion** \(y\). This return is typically produced by the **reward model**, which approximates human feedback in RLHF, and may be augmented with auxiliary terms such as per-token KL penalties that discourage excessive deviation from the supervised fine-tuned checkpoint used as the reference policy \(\pi\_{\text{ref}}\).
  + Although each individual training target \(\hat{R}(x,y)\) corresponds to only one sampled trajectory, minimizing the MSE objective over **many repeated samples** causes \(V\_\psi(x)\) to converge, in expectation, to the expected return under the policy’s full trajectory distribution. Concretely, across training, the same or similar prompts \(x\) are encountered many times, and each time the policy stochastically generates a potentially different completion \(y\) with its own realized return \(\hat{R}(x,y)\). Averaged implicitly through gradient updates, these repeated [**Monte Carlo samples**](#monte-carlo-return-used-as-the-regression-target) drive the value model toward the probability-weighted average of cumulative rewards across all trajectories the policy can generate from \(x\).
  + In RLHF pipelines such as [InstructGPT](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022), the value model is initialized from the reward model and fine-tuned concurrently with the actor (policy) during PPO. This concurrent training ensures that the critic continuously adapts to the policy’s evolving expected reward landscape—via repeated sampling from the policy-induced distribution over trajectories—rather than memorizing the rewards of individual rollouts.
* The training data underlying this objective consist of tuples \((x, y, r(x,y))\):

  + \(x\): a prompt sampled from curated datasets or real user queries,
  + \(y\): a response generated by the current policy \(\pi\_\theta\), representing one sampled trajectory from the policy-induced distribution,
  + \(r(x,y)\): a scalar reward produced by the reward model (and, in practice, possibly adjusted by a KL penalty term relative to the SFT checkpoint as the reference policy \(\pi\_{\text{ref}}\)).
  + Collectively, these tuples define the empirical distribution \(D\) over which the value regression loss is computed. Through repeated sampling of prompts and stochastic completions over the course of training, this empirical process provides the coverage needed for the value model to approximate the expected cumulative reward over all policy-generated trajectories.

###### Monte Carlo return used as the regression target

* In RLHF for language models, the expected cumulative reward under a policy cannot be computed in closed form because the space of possible continuations (trajectories) is combinatorially large and defined implicitly by the model’s autoregressive token distribution. Enumerating or analytically integrating over all trajectories is intractable. As a result, the expectation \(\mathbb{E}\_{\tau \sim \pi\_\theta(\cdot \mid x)}[R(\tau)]\) is approximated using **Monte Carlo sampling**: trajectories are sampled from the policy, their realized returns are observed, and learning proceeds by averaging information from these samples over time. This approach is standard in policy-gradient and actor–critic methods, where unbiased but noisy samples are preferred over infeasible exact expectations.
* Thus, the regression target is **not** the expectation itself, but a **single Monte Carlo sample** of the return obtained from one trajectory generated by the policy. For a rollout starting from prompt \(x\) (or state \(s\_t\)), the realized return is defined as:

  \[R\_t
  \equiv
  \sum\_{k=t+1}^{T} r(s\_k, a\_k)\]
  + where actions \(a\_k\) (tokens) are sampled autoregressively from the policy \(\pi\_\theta\), inducing a trajectory
    \(\tau = (a\_{t+1}, \ldots, a\_T) \sim \pi\_\theta(\cdot \mid s\_t)\), and rewards \(r(\cdot)\) are provided by the reward model (optionally including KL-based shaping terms).
  + Because the trajectory itself is sampled, \(R\_t\) is a random variable drawn from the conditional distribution \(R \mid x\). Different rollouts from the same prompt can yield different \(R\_t\) values depending on which tokens are sampled.
* In the **bandit-style RLHF setting** used in [InstructGPT](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022), the episode terminates immediately after a single completion. As a result, the sum above typically collapses to a single terminal reward assigned to the full prompt–completion pair. The notation highlights that \(R\_t\) is a single Monte Carlo sample from the policy-induced trajectory distribution \(\pi\_\theta(\tau \mid s\_t)\), not the expectation over that distribution.

###### Why regressing on a single \(R\_t\) yields an expectation

* Although the value model is trained on **individual sampled returns**, minimizing the MSE objective drives it toward the **conditional expectation** of the return under the policy. This follows from a standard result in regression theory:

  \[\arg\min\_f
  \mathbb{E}\big[(f(x) - R)^2 \mid x\big]
  =
  \mathbb{E}[R \mid x]\]
* Crucially, this convergence relies on **repeated Monte Carlo sampling over time**, not on averaging multiple samples within a single update:

  + Although each PPO update uses only **one sampled return per prompt**, the value model ultimately learns from **many such samples across training iterations**.
  + The same prompt (or closely related prompts) may be encountered repeatedly during training.
  + Each time, the policy stochastically generates a different completion according to its token-level probability distribution.
  + Each completion yields a different realized return \(R\_t\), corresponding to a different sampled trajectory.
* Across training, this process produces a growing collection of Monte Carlo samples:

  \[{R(\tau): \tau \sim \pi\_\theta(\cdot \mid x)}\]
  + … which empirically approximates the full return distribution induced by the policy for that prompt.
* As gradient updates accumulate, these sampled returns are **implicitly averaged through optimization**. If \(V\_\psi(x)\) overestimates the true expected return, subsequent samples will, on average, push it downward; if it underestimates, they will push it upward. Only the conditional mean \(\mathbb{E}[R \mid x]\) remains stable under these stochastic updates.
* As a result, even though each update uses only one sampled completion, repeated regression over many rollouts causes the value model to converge to \(V\_\psi(x) \approx \mathbb{E}\_{y \sim \pi\_\theta(\cdot \mid x)}[R(x,y)]\). Put simply, even though each regression target reflects the reward of a single trajectory, minimizing MSE over **many repeated samples** causes the value model to converge to the **probability-weighted average cumulative reward over all trajectories the policy can generate from \(x\)**, rather than overfitting to any individual rollout.
* This mechanism is identical in principle to Monte Carlo value estimation in classical actor–critic methods, as formalized in work such as [Actor-Critic Algorithms](https://papers.nips.cc/paper/2000/hash/60941600aaa93c7e3de7729355a0913e-Abstract.html) by Konda and Tsitsiklis (2000), and is what allows the critic to represent an expectation despite being trained on noisy, single-sample returns.

###### Sampling, rollouts, and empirical expectations

* In practice, RLHF systems do **not** enumerate all continuations under the policy. Instead, the expectation defining the value function is approximated **empirically through repeated sampling** from the policy-induced distribution over trajectories. The flow is as follows:

  + Each PPO update samples a prompt \(x\) from the training distribution.
  + The policy \(\pi\_\theta\) generates **one stochastic completion** \(y \sim \pi\_\theta(\cdot \mid x)\).
  + The reward model assigns a scalar reward \(r(x,y)\) (optionally shaped with per-token KL penalties), producing a single Monte Carlo target \(R\_t\).
* In the [InstructGPT](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022) PPO setup, training is framed as a **bandit environment**: at each PPO step, the environment presents a randomly sampled customer prompt, the policy generates **a single completion**, a scalar reward is produced by the reward model (minus the per-token KL penalties), and the episode immediately terminates. As a result, **one rollout per prompt per PPO update** is used.
* Rather than averaging multiple rollouts for the same prompt within a single batch update, the expectation \(\mathbb{E}\_{\tau \sim \pi\_\theta(\cdot \mid x)}[R(\tau)]\) over the policy’s continuation distribution is approximated implicitly through **repeated sampling across many PPO iterations** via repeated stochastic rollouts. Over the course of training, as prompts are revisited, the policy samples different trajectories, and each trajectory contributes one noisy but unbiased Monte Carlo return sample to the learned expectation.
* The empirical return distribution observed by the value model is therefore shaped by the **sampling procedure** used during rollout generation:

  + **Decoding strategy** (greedy, top-\(k\), top-\(p\)) determines which regions of the policy distribution are explored.
  + **Temperature scaling** controls the entropy of token sampling, trading off exploration and variance.
  + These choices affect which trajectories are sampled frequently and thus which parts of the policy’s trajectory distribution dominate the empirical expectation learned by the value model.
* Consequently, the value model can be understood as approximating the expected cumulative reward **under the empirical policy distribution induced by the rollout procedure**.

###### Relationship to PPO and advantage estimation

* The value model trained under this objective is used directly in PPO-style advantage estimation:

  \[\hat{A\_t} = r\_t - V\_\psi(s\_t)\]
  + which is the bandit-style simplification used in RLHF, since prompt \(\rightarrow\) completion \(\rightarrow\) reward forms a single-step episode.
  + This follows the actor–critic formulation introduced in [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) by Schulman et al. (2017).
* By learning \(V\_\psi\) as an approximation to the expected return, the critic provides a **low-variance baseline**, stabilizing policy gradients and enabling efficient learning even with sparse, high-variance reward signals from human or AI feedback.

###### Extensions

* Several extensions are commonly layered on top of the basic MSE objective to improve stability, generalization, and alignment fidelity:

  + **Per-token value heads** (also called **token-level PPO**), which estimate \(V\_\psi(s\_t)\) at intermediate prefixes rather than only at the full completion. This supports finer-grained credit assignment across long generations and better aligns the critic with the autoregressive structure of language models.
  + **Target value networks** \(V\_{\phi^-}\), updated slowly or periodically, to stabilize bootstrapped targets in TD variants of value learning, following standard deep RL practice.
  + **Token-wise KL-regularized rewards**, where the effective return includes a **per-token KL penalty** that constrains the policy from drifting too far from a reference distribution—typically the SFT model. Concretely, at each token step the reward is adjusted by a term proportional to \(-\beta \mathrm{KL}\big(\pi\_\theta(\cdot \mid s\_t) \mid\mid \pi\_{\text{SFT}}(\cdot \mid s\_t)\big)\) and these penalties are accumulated across the entire completion. This token-level KL control is critical in RLHF, as unconstrained optimization against a learned reward model can otherwise lead to distributional collapse, degraded fluency, or reward hacking. This design follows the PPO-based RLHF formulation used in [InstructGPT](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022) and earlier work such as [Learning to Summarize from Human Feedback](https://arxiv.org/abs/2009.01325) by Stiennon et al. (2020).
  + **PPO-ptx (pretraining-mixed PPO)**, which explicitly mixes PPO reinforcement learning updates with gradients from the original **unsupervised language modeling (pretraining) objective**. As described in [InstructGPT](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022), this hybrid objective augments the PPO reward maximization term with an additional log-likelihood term over the pretraining distribution, thereby interleaving **reinforcement signals** with **pretraining signals** during optimization. This design ensures that while the model learns from reward feedback, it retains broad linguistic competence and factual grounding acquired during pretraining. By regularizing the optimization trajectory, PPO-ptx mitigates regression on standard NLP benchmarks (“alignment tax”), reduces catastrophic forgetting of general capabilities, and empirically improves both **instruction-following behavior** and **robustness across unseen prompts**, striking a balance between alignment and general language proficiency.
* Together, these stabilizers ensure that the value model and policy do not simply overfit noisy reward signals from individual rollouts, but instead converge toward a smooth, generalizable estimate of **expected cumulative reward under a KL-regularized policy**, consistent with modern actor–critic theory and scalable RLHF practice.

##### Training Data

* **Primary source:** On-policy samples collected during RLHF fine-tuning, typically generated from curated instruction datasets.
* **Reward signals:** Derived from the reward model or human-preference comparisons.
* **Scale:** Hundreds of thousands to millions of prompt–response pairs per training loop.
* **Temporal structure:** Since LLM reward modeling is usually *bandit-like* (single scalar reward per completion), the value model relies on **Monte Carlo estimates** or **Generalized advantage estimation (GAE)** to stabilize learning despite sparse supervision.

##### Model Size

* The value model’s size is often comparable to the reward model and smaller than the policy model.

  + For instance, in [**InstructGPT**](https://arxiv.org/abs/2203.02155), the critic had a similar scale (~6B parameters) to the reward model and served as a critic for a 175B parameter policy.
  + In open-source frameworks such as **TRLX** or **DeepSpeed-Chat**, value heads are attached to 7B–13B base LLMs or trained as independent critics.
* When computational resources are limited, a **shared-head** architecture is used, where the value head is attached directly to the policy model’s hidden states, enabling efficient joint training of actor and critic.

##### Relationship to the Reward Model

* The value model and the reward model are tightly coupled but conceptually distinct components of the RLHF pipeline, each answering a different question about model behavior. They coincide only in **degenerate or limiting cases** (detailed below in the [Degenerate cases](#degenerate-cases) section), because they are defined over fundamentally different quantities.

###### Reward Model: Observed Preference Signal

* The **reward model** defines what is being optimized: it maps a completed response (or, in some setups, partial responses) to a scalar reward reflecting human preference. Formally, the reward model defines a reward function:

  \[r\_\phi(x, y) \in \mathbb{R}\]
  + where \(x\) is the prompt and \(y\) is the generated completion. More precisely, the reward model produces an *observed* (i.e, *realized*) scalar reward for a specific trajectory \(r\_\phi(x, y\_{1:T})\), which is only known once the full response \(y\_{1:T}\) has been generated and evaluated.
* This reward can be **outcome-based**, where \(r\_\phi(x, y\_{1:T})\) is produced only after the full completion, or **process-based**, where rewards are emitted at intermediate generation steps and summed over time to form \(r\_\phi(x, y\_{1:T})\). A detailed discoruse on outcome-based vs. process-based rewards has been offered in the [Outcome-Based vs. Process-Based Rewards](#outcome-based-vs-process-based-rewards) section.

###### Value Model: Expectation over Futures

* The **value model (critic)** does not define preferences; instead, it models expectations. Given a state \(s\_t = (x, y\_{1:t})\), corresponding to a prompt plus a partial completion (prefix), the value model predicts the **expected cumulative future reward** under the current policy \(\pi\_\theta\):

\[V\_\psi(s\_t)
= \mathbb{E}\_{y\_{t+1:T} \sim \pi\_\theta(\cdot \mid s\_t)}
\Big[ R(s\_t) \Big]\]

* Unlike the reward model, this quantity is defined before the future tokens are generated and therefore averages over all possible stochastic continuations of the policy.
* Because one quantity is a realized outcome and the other is an expectation over possible futures, they are generally not equal:

\[V\_\psi(s\_t) \neq r\_\phi(x, y\_{1:T})\]

###### Outcome-Based vs. Process-Based Rewards

* What the return \(R(s\_t)\) represents is entirely determined by how the reward model is defined. Specifics below:

  + **Outcome-based (i.e., terminal-only) rewards**:
    - For outcome-based rewards, the return is a single terminal reward:\[R(s\_t) = r\_\phi(x, y\_{1:T})\]
    - At intermediate prefixes \(t < T\), the value model averages this terminal reward over all possible completions:\[V\_\psi(s\_t)
    = \mathbb{E}\_{y\_{t+1:T} \sim \pi\_\theta}
    \big[ r\_\phi(x, y\_{1:T}) \big]\]
    - Only at the terminal state \(s\_T\)—when the completion is fixed and no future randomness remains—does the expectation collapse:\[V\_\psi(s\_T) = r\_\phi(x, y\_{1:T})\]
  + **Process-based (i.e., step-wise) rewards**:

    - For process-based rewards, the return is the sum of future step-wise rewards:\[R(s\_t) = \sum\_{k=t+1}^{T} r\_\phi(s\_k, a\_k)\]
    - … and the value model estimates the expected remaining cumulative reward:\[V\_\psi(s\_t)
    = \mathbb{E}\_{\pi\_\theta}
    \Big[ \sum\_{k=t+1}^{T} r\_\phi(s\_k, a\_k) \Big]\]
    - Equality with realized rewards again holds only at the final step, when no future rewards remain and the expectation becomes trivial.
* Crucially, **outcome-based vs. process-based is a property of the reward definition, not of the value model**. The distinction concerns *when* and *how* the reward model assigns supervision; regardless of how rewards are produced, the value model estimates the **expected cumulative future rewards** induced by that reward definition:

\[V\_\psi(s) \approx \mathbb{E}[R \mid s]\]

###### Training-time divergence

* Although the value model is often **initialized from the reward model** (as in InstructGPT), the two diverge during training because they optimize different objectives over different data.
* The reward model is trained offline on human preference data using a pairwise ranking loss, for example:

\[L\_{\text{RM}}(\theta)
= -\mathbb{E}\_{(x, y\_w, y\_l)}
\big[ \log \sigma(r\_\phi(x,y\_w) - r\_\phi(x,y\_l)) \big]\]

* The value model is trained **online** using a MSE regression objective, minimizing the squared difference between its predicted value \(V\_\psi(s\_t)\) and a target return \(\hat{R}\_t\) obtained from policy rollouts:

\[L\_V(\phi)
= \mathbb{E}\_{(s\_t, \hat{R}\_t)}
\big[ (V\_\psi(s\_t) - \hat{R}\_t)^2 \big]\]

* In **outcome-based (terminal-only) RLHF**, the full return is available once the episode ends, so bootstrapping is not strictly required and \(\hat{R}\_t\) can be set to the realized terminal reward.
* In **process-based or token-level RLHF**, rewards may be distributed across multiple steps or the episode may be truncated **(e.g., due to fixed context windows, maximum generation length, or early stopping criteria)**, so the remaining future return is unknown at intermediate states. In these cases, the target \(\hat{R}\_t\) is formed by **bootstrapping from the value model itself**, for example \(\hat{R}\_t = r\_t + \gamma V\_\psi(s\_{t+1})\), or via multi-step or GAE-style targets to balance bias and variance.

###### Role in advantage estimation

* As a result, the reward model outputs an **observed (i.e., realized) reward** \(r\_\phi(x,y)\) for a specific completion, while the value model outputs a **baseline prediction** used for variance reduction in advantage estimation, thereby improving training stability.
* This relationship is formalized through the advantage function, where the value model’s baseline is subtracted from the realized return to to obtain the advantage signal used for training which measures how much better or worse the outcome was than expected:

\[\hat{A\_t} = r\_t - V\_\psi(s\_t)\]

###### Degenerate cases

* In general, the reward model outputs a *realized reward* for a specific completion, while the value model outputs an *expected return* over possible future continuations. They coincide only in **degenerate cases** where this expectation collapses to a single realized outcome, which has direct implications for **policy optimization in LLMs**. Specifically, this refers **not to their architectures or training objectives**, but to the **numerical quantity they output for a given state or trajectory**.
* Concretely, the reward model and value model coincide only in the following **degenerate cases**:

  + **Terminal states** \(s\_T\), where the full completion \(y\_{1:T}\) is already fixed and no future actions remain. In this case, there is no stochasticity left in the continuation, so the expected return equals the realized reward \(V^\pi(s\_T) = r\_\phi(x, y\_{1:T})\).
    - For LLM policy optimization, this means that at the end of generation the critic provides no additional predictive information beyond the reward itself. The advantage used by PPO, \(\hat{A\_T = r\_\phi(x, y\_{1:T}) - V^\pi(s\_T)\), becomes zero in expectation, reflecting that no further learning signal can be extracted once the outcome is fully known.
  + **Single-step (bandit) environments**, where the episode consists of a single action followed immediately by a reward. This closely matches the standard RLHF setup for LLMs with **outcome-based rewards**, where the policy generates a full completion in one rollout and then receives a single scalar reward. In this case, there is no multi-step future to reason about, and the value function trivially equals the expected reward of that completion:

    \[V^\pi(s\_0) = \mathbb{E}[R \mid s\_0] = \mathbb{E}\_{y \sim \pi(\cdot \mid x)}[r\_\phi(x, y)]\]
    - For PPO-style optimization, the critic’s role reduces to estimating the *average reward for a prompt*, providing a baseline so that advantages \(\hat{A} =r\_\phi(x, y) - V^\pi(s\_0)\) measure whether a sampled completion is better or worse than what the policy typically produces. Even though the environment is bandit-like, this baseline is crucial for reducing gradient variance and stabilizing updates.
* Outside these cases, the distinction is essential for LLM policy optimization. At intermediate prefixes \(s\_t\) with \(t < T\), the value model must average over many possible continuations, while the reward model evaluates only the realized completion:

  \[V^\pi(s\_t)
  = \mathbb{E}\_{y\_{t+1:T} \sim \pi} \big[ r\_\phi(x, y\_{1:T}) \big]
  \neq
  r\_\phi(x, y\_{1:T})\]
  + This separation allows PPO to assign credit across tokens by comparing realized rewards to expected returns conditioned on the current prefix.
* In summary, the reward model defines the **reward function** \(r\_\phi(\cdot)\), which answers *what counts as good* for a completed behavior, while the value model approximates the **value function** \(V^\pi(s) = \mathbb{E}[R \mid s]\), which answers *how good the future is expected to be*, given the current prefix and the policy’s stochastic continuation behavior. In LLM policy optimization, which consist of bandit-style regimes typical of RLHF, this distinction underpins advantage estimation, variance reduction, and stable gradient-based updates.

###### Comparative Analysis

| **Aspect** | **Reward Model** | **Value Model** |
| --- | --- | --- |
| Input | Prompt + response | Prompt (or prompt + partial response) |
| Output | Scalar reward (human preference estimate) | Expected future reward (baseline or critic) |
| Training data | Human or synthetic preference comparisons | Policy rollouts and rewards |
| Objective | Pairwise ranking loss | MSE regression loss |
| Usage | Guides policy optimization | Stabilizes training via advantage estimation |
| Updates | Offline (pretrained) | Online (updated during RL loop) |

* The reward model captures *external supervision*, while the value model provides *internal bootstrapping* for efficient policy learning.

##### Comparative Analysis

| **Aspect** | **Description** |
| --- | --- |
| **Role** | Predicts expected future reward for prompts/responses |
| **Function** | Baseline and critic for policy optimization |
| **Architecture** | Transformer with scalar output head |
| **Training Data** | On-policy prompt–response–reward tuples |
| **Model Size** | 1B–13B parameters |
| **Training Objective** | Mean-squared error on observed or bootstrapped returns |
| **References** | [Konda & Tsitsiklis, 2000](https://papers.nips.cc/paper/2000/hash/60941600aaa93c7e3de7729355a0913e-Abstract.html); [Stiennon et al., 2020](https://arxiv.org/abs/2009.01325); [Ouyang et al., 2022](https://arxiv.org/abs/2203.02155) |

### Optimizing the Policy

* The policy refers to a strategy or a set of rules that an agent uses to make decisions in an environment. Put simply, the policy defines how the agent selects actions based on its current observations or state.
* The policy optimization process involves RL techniques that iteratively refine the policy based on reward feedback. The reward model provides feedback based on human preferences, and the policy is optimized iteratively to maximize reward while maintaining a stable learning trajectory. The stability aspect is enforced by maintaining a certain level of similarity to its previous version (to prevent drastic changes that could lead to instability)
* Popular policy optimization methods – specifically applied to LLMs – include:
  + **[PPO](#proximal-policy-optimization-ppo):** A widely-used RL algorithm that balances exploration and exploitation while maintaining training stability.
  + **[DPO](#direct-preference-optimization-dpo):** An alternative approach where the policy directly optimizes the relative log probability of preferred responses using a binary cross-entropy loss, balancing human feedback alignment with KL divergence constraints.
  + **[GRPO](#group-relative-preference-optimization-grpo):** A PPO variant that removes the critic model and estimates the baseline from group scores, improving memory efficiency and performance in complex tasks like mathematical reasoning.
* Through RLHF, models like InstructGPT and ChatGPT have achieved enhanced alignment with human expectations, producing more beneficial and contextually appropriate responses.

### Integration of Policy, Reference, Reward, and Value Models

* The full RLHF pipeline integrates four central components — the **policy**, **reference**, **reward**, and **value** models — into a cohesive optimization framework. Together, these models implement a scalable variant of **policy-gradient reinforcement learning** (commonly using PPO) for large-scale LLM alignment.
* This section provides a complete description of how these models interact, the mathematical formulation governing their updates, and the system-level architecture of a modern RLHF pipeline.

#### Overview of the RLHF Process

* RLHF transforms large pretrained language models into *alignment-optimized* conversational agents through a three-phase process:

  1. **Supervised Fine-Tuning (SFT):**
     + The base pretrained LLM is fine-tuned on instruction–response data curated by humans.
     + **Output:** *SFT model* (used as both the initial **policy** and the frozen **reference model**).
  2. **Reward Modeling:**
     + Human annotators rank or compare pairs of model responses.
     + A separate **reward model** is trained on these comparisons to learn a scalar preference function \(r\_\phi(x,y)\).
  3. **Reinforcement Learning (RL) Optimization:**
     + The **policy model** is optimized to generate responses that maximize the learned reward signal, while staying close to the **reference model** through KL regularization.
     + The **value model** acts as a critic, stabilizing the gradient updates.
* This procedure was first described comprehensively in *Training Language Models to Follow Instructions with Human Feedback* by [Ouyang et al. (2022)](https://arxiv.org/abs/2203.02155), forming the backbone of systems such as **InstructGPT** and **ChatGPT**.

#### Core Mathematical Formulation

* The RLHF optimization problem can be expressed as:

  \[\max\_{\theta}, \mathbb{E}\_{x\sim D\_{\text{prompt}},y\sim\pi\_\theta(\cdot\mid x)} \left[ r\_\phi(x,y) - \beta\mathrm{KL}\big(\pi\_\theta(\cdot\mid x) \mid\mid \pi\_{\text{ref}}(\cdot\mid x)\big) \right]\]
  + where:

    - \(\pi\_\theta\) = **policy model** (trainable)
    - \(\pi\_{\text{ref}}\) = **reference model** (frozen)
    - \(r\_\phi\) = **reward model** (provides scalar reward)
    - \(\beta\) = KL penalty coefficient controlling exploration–alignment trade-off
* The **KL term** prevents the policy from diverging too far from its linguistic prior, while the **reward** encourages behaviors that better match human preferences.
* To train this objective, **Proximal Policy Optimization (PPO)** by [Schulman et al. (2017)](https://arxiv.org/abs/1707.06347) is typically used, which optimizes a clipped surrogate loss:

  \[L\_{\text{PPO}}(\theta) =
  \mathbb{E}\_{(x,y)\sim\pi\_\theta}
  \left[
  \min\left(
  r\_t(\theta),\hat{A}\_t, \mathrm{clip}\big(r\_t(\theta), 1-\epsilon, 1+\epsilon\big),\hat{A}\_t
  \right)
  \right]\]
  + where:

    - \(r\_t(\theta) = \frac{\pi\_\theta(y\_t \mid x\_t)}{\pi\_{\theta\_{\text{old}}}(y\_t \mid x\_t)}\) is the **likelihood ratio**;
    - \(\hat{A}\_t = r\_\phi(x\_t,y\_t) - V\_\psi(x\_t)\) is the **advantage estimate**;
    - \(V\_\psi\) = **value model**;
    - \(\epsilon\) is a clipping hyperparameter (usually 0.1–0.2).
* The advantage term ensures that updates are proportional to how much better a response is than expected, while the clipping stabilizes the step size.

#### Role of Each Model in the Loop

* **Policy Model** \(\pi\_{\theta}\):

  + Generates responses \(y\) to prompts \(x\).
  + Updated via **Proximal Policy Optimization (PPO)** to maximize the clipped surrogate objective.
  + Receives both **reward signals** and **value-based baselines** during training.
* **Reference Model** \(\pi\_{\text{ref}}\):

  + Provides a baseline distribution for **KL regularization** to prevent over-optimization.
  + Frozen during training; used to compute token-wise divergence:

    \[D\_{\text{KL}}\big(\pi\_{\theta}(\cdot \mid x) \mid\mid \pi\_{\text{ref}}(\cdot \mid x)\big)
    = \sum\_{y} \pi\_{\theta}(y \mid x) \cdot \log\frac{\pi\_{\theta}(y \mid x)}{\pi\_{\text{ref}}(y \mid x)}\]
  + Ensures linguistic stability and mitigates **reward hacking** by anchoring the policy to its supervised fine-tuned prior.
* **Reward Model** \(r\_{\phi}\):

  + Maps each generated response \(y\) (conditioned on prompt \(x\)) to a scalar reward:
    \(r\_{\phi}: (x, y) \mapsto \mathbb{R}\).
  + Trained on **human preference data** (pairwise or ranked comparisons), then frozen during policy optimization.
  + Supplies an **approximation of human judgment**, encouraging the policy to produce more aligned, preferred responses.
* **Value Model** \(V\_{\psi}\):

  + Estimates the **expected return** for a given prompt (or state) \(x\), reducing variance in policy-gradient updates.
  + Trained in parallel with the policy to predict the observed or bootstrapped return:
    \(\hat{R}(x, y) = r\_{\phi}(x, y),\)
    and provides **advantage estimates**:
    \(\hat{A}(x, y) = r\_{\phi}(x, y) - V\_{\psi}(x).\)
  + Serves as a **critic** in the actor–critic framework, enabling stable and efficient optimization.

#### Full Training Loop

* **Step 1: Sampling Responses**:

  + Draw a batch of prompts \({x\_i}\) from the dataset.
  + Generate responses \({y\_i}\) from the current policy \(\pi\_\theta\).
* **Step 2: Reward Evaluation**:

  + Compute scalar rewards \(r\_\phi(x\_i, y\_i)\) using the reward model.
  + Compute KL penalties from the reference model.
* **Step 3: Advantage Computation**:

  + Use the value model to estimate baselines \(V\_\psi(x\_i)\).
  + Compute advantages \(\hat{A}\_i = r\_\phi(x\_i, y\_i) - V\_\psi(x\_i)\).
* **Step 4: Policy Update (PPO)**:

  + Optimize \(L\_{\text{PPO}}(\theta)\) with respect to the policy parameters.
  + Clip ratios and advantages to maintain stable updates.
* **Step 5: Value Model Update**:

  + Update the critic via regression:
    \(L\_V(\psi) = \mathbb{E}\_{(x,y)} \big[ (V\_\psi(x) - r\_\phi(x,y))^2 \big]\)
* **Step 6: Iteration and Rollout**:

  + Repeat with new samples from the updated policy.
  + Periodically evaluate human or synthetic preference metrics to ensure alignment progress.

#### System Architecture

\[\begin{aligned}
&\underbrace{D\_{\text{prompt}}}\_{\text{Prompt Dataset}}
\xrightarrow{\text{sample prompts}}
\underbrace{\pi\_{\theta}}\_{\text{Policy Model}}
\xrightarrow[\text{Generates responses}]{}
\underbrace{r\_{\phi}}\_{\text{Reward Model}}
\xrightarrow[\text{Computes scalar rewards}]{} \\[1em]
&\underbrace{V\_{\psi}}\_{\text{Value Model}}
\xrightarrow[\text{Computes baselines}]{}
\underbrace{\pi\_{\text{ref}}}\_{\text{Reference Model}}
\xrightarrow[\text{KL penalty computation}]{}
\underbrace{\text{PPO Optimization Loop}}\_{\text{Policy update step}}
\end{aligned}\]

#### Computational and Practical Considerations

* **Training Scale:**
  + The RLHF fine-tuning phase typically uses **hundreds of thousands to millions of samples**, requiring large-scale distributed training.
  + Compute cost is dominated by sampling (policy forward passes) and reward scoring.
* **Stability:**
  + PPO’s clipping and KL regularization stabilize updates that would otherwise explode in such large parameter spaces.
* **Safety and Alignment:**
  + The reward model embeds alignment objectives (helpfulness, harmlessness, honesty).
  + KL regularization ensures fidelity to the pretrained model’s linguistic priors.
* **Continuous Improvement:**
  + Iterative retraining of reward models using newer policy outputs yields increasingly aligned systems — a process sometimes called *iterative RLHF* or *alignment bootstrapping* (see [Christiano et al., 2017](https://arxiv.org/abs/1706.03741)).

#### Comparative Analysis

| **Model** | **Function** | **Training Status** | **Data Source** | **Typical Size** |
| --- | --- | --- | --- | --- |
| **Policy (\(\pi\_\theta\))** | Generates responses; optimized for reward | Trainable | Prompts, synthetic rollouts | 7B–175B |
| **Reference (\(\pi\_\text{ref}\))** | Baseline distribution for KL penalty | Frozen | Same as SFT model | 7B–175B |
| **Reward (\(r\_\phi\))** | Scores responses based on preferences | Frozen | Human comparisons | 1B–13B |
| **Value (\(V\_\psi\))** | Predicts expected reward (critic) | Trainable | Policy rollouts with rewards | 1B–13B |

* In summary, RLHF operationalizes policy optimization as preference optimization for for LLMs by combining:

  + The **policy** for exploration and response generation,
  + The **reward** for human alignment,
  + The **value** for stability and variance control, and
  + The **reference** for constraint and safety.
* This synergy enables LLMs to internalize nuanced human feedback, forming the foundation for systems like **ChatGPT**, **Anthropic’s Claude**, and **Google’s Gemini**.

### Putting it all together: Training Llama

#### Llama 4

* Introduced in [The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation](https://ai.meta.com/blog/llama-4-multimodal-intelligence/), the Llama 4 series marks a decisive leap forward in Meta’s open-weight model evolution, embodying natively multimodal design and advanced preference optimization.
* With the introduction of Llama 4 Scout, Llama 4 Maverick, and the teacher model Llama 4 Behemoth, Meta’s alignment and optimization pipeline evolved into a hybrid of traditional RLHF and DPO, adapted for large-scale multimodal learning.

##### Model Overview and Architecture

* Llama 4 introduces a mixture-of-experts (MoE) architecture where only a small subset of parameters activates per token, dramatically improving training and inference efficiency.

  + **Llama 4 Scout:** 17 billion active parameters, 16 experts, 109B total parameters, with a record-breaking 10 million token context window.
  + **Llama 4 Maverick:** 17 billion active parameters, 128 experts, 400B total parameters, balancing precision, cost efficiency, and multimodal reasoning.
  + **Llama 4 Behemoth:** 288 billion active parameters, 16 experts, and nearly 2 trillion total parameters, serving as a “teacher” for distillation.
* Each model uses alternating dense and MoE layers, with tokens routed to both a shared and an expert-specific pathway, enabling dynamic specialization without compromising latency. This modular routing system supports scalable deployment — from single H100 GPUs (Scout) to distributed inference (Maverick and Behemoth).

##### Pre-Training: Efficiency, Scale, and Multimodality

* The pre-training phase introduced several innovations:

  + **Native Multimodality:** Early-fusion architecture integrating text, vision, and video tokens, allowing joint learning across modalities.
  + **Vision Encoder Improvements:** Based on MetaCLIP, co-trained with frozen Llama layers for better image-text alignment.
  + **MetaP Training Framework:** A novel hyperparameter control system for per-layer learning rates and initialization scales, providing transferability across architectures and batch sizes.
  + **FP8 Precision Training:** Enhanced efficiency with 390 TFLOPs/GPU utilization across 32K GPUs, sustaining quality with minimal degradation.
  + **Massive Multilinguality:** 200 languages pre-trained, 100+ with over a billion tokens each — 10× the Llama 3 multilingual data budget.
  + **Extended Context Length:** Specialized mid-training datasets for long-context retention, culminating in a 10M-token context capacity for Llama 4 Scout.
* The pre-training dataset exceeded 30 trillion tokens, encompassing diverse web text, code, images, and video frames. Continuous “mid-training” refinement phases allowed the model to expand context comprehension while maintaining stability.

##### Post-Training and Preference Optimization

* Post-training for Llama 4 integrated **multi-stage alignment** combining SFT, online RL, and lightweight DPO.

  + **Curriculum Design:** A multimodal training curriculum balancing text, image, and reasoning data without sacrificing domain specialization.
  + **Hard Data Curation:** Automated difficulty estimation with prior Llama models used as judges to prune over 50% of “easy” SFT data, focusing on challenging prompts.
  + **Continuous Online RL:** Implemented as an **on-policy, PPO-like training loop** rather than DPO.

    - The model alternates between *generation* and *optimization* phases, continually updating the policy based on freshly sampled data.
    - “Medium-to-hard” prompts are identified via **advantage scores and model confidence**, filtering out zero-reward or trivial samples.
    - An **advantage estimator** (\(\hat{A}(s, a) = Q(s, a) – V(s)\)) computes expected improvement per action, and prompts are re-ranked by these scores to form adaptive mini-batches.
    - A clipped surrogate loss similar to PPO ensures stable policy updates with controlled KL divergence to the reference model.
    - The reward signal blends multiple criteria — helpfulness, factuality, safety, and multimodal consistency (e.g., text-visual grounding accuracy).
  + **Lightweight DPO Refinement:** After online RL, a DPO stage fine-tunes preference alignment through log-likelihood ratio optimization without explicit rewards. This stabilizes conversational flow, reduces verbosity, and improves subjective response quality.
* This hybrid pipeline allows exploration (via online RL) while retaining control (via DPO). It achieved consistent improvements in reasoning, multimodal grounding, and factual correctness with lower computational overhead than full RLHF pipelines.

##### Distillation from Llama 4 Behemoth

* Llama 4 Behemoth acted as a codistillation teacher for the smaller models.
* A novel **dynamic distillation loss** balanced soft (logit-level) and hard (label-level) targets.
* Computation amortized across pre-training batches by embedding Behemoth forward passes into student model training.
* Distillation improved multimodal reasoning and efficiency without requiring full retraining on large datasets.

##### Reinforcement Learning Infrastructure at Scale

* Scaling RL for the two-trillion-parameter Behemoth required a fundamental infrastructure overhaul:

  + **Asynchronous Online RL Framework:** Enabled decoupled model execution across GPUs, enhancing flexibility and reducing idle compute.
  + **Experience Replay Buffers:** Incorporated sliding-window replay to maintain data diversity while preventing overfitting to recent samples.
  + **Adaptive KL Penalty:** Dynamically adjusted during training to prevent policy collapse, based on running estimates of divergence from reference weights.
  + **MoE Parallelization Optimizations:** Improved throughput by balancing compute load dynamically across active experts.
  + **Curriculum-Based Prompt Sampling:** pass@k evaluation and zero-advantage filtering ensured progressively harder RL training data.
  + Result: ~10× increase in training efficiency over prior distributed RL frameworks, with significantly improved sample efficiency and reward stability.

##### Safeguards and Bias Mitigation

* Llama 4 integrates alignment and safety at multiple levels:

  + **Data-Level Mitigations:** Pre-training filtering and domain balancing to reduce bias propagation.
  + **System-Level Safeguards:**

    - *Llama Guard*: safety classifier for harmful content.
    - *Prompt Guard*: defense against prompt injections and jailbreaks.
    - *CyberSecEval*: adversarial testing and vulnerability assessment.
  + **Generative Offensive Agent Testing (GOAT):** Automated multi-turn adversarial red-teaming to simulate real-world misuse cases.
* Llama 4 achieved measurable progress in political neutrality and response balance: refusal rates on politically sensitive prompts fell below 2%, and unequal refusal bias dropped below 1%, outperforming Llama 3 and matching Grok-class models.

##### Takeaways

* The combination of multimodal pre-training, online RL, and DPO alignment produced a family of models that are both powerful and efficient:

  + **Llama 4 Maverick** surpasses GPT-4o and Gemini 2.0 Flash in reasoning, coding, and multilingual benchmarks.
  + **Llama 4 Scout** achieves unprecedented 10M-token context understanding and state-of-the-art image grounding.
  + **Llama 4 Behemoth** establishes new frontiers for teacher-student distillation and large-scale preference optimization.
* Collectively, these models represent a paradigm shift: from text-based alignment toward multimodal, preference-aware intelligence that learns from human feedback, structured curricula, and continuous self-refinement.

#### Llama 2

* As a case study of how Llama 2 was trained, let’s go over the multi-stage process that integrates both human and model-generated feedback to refine the performance of language models. Here’s how it functions:
  1. **Pretraining:** Llama 2 undergoes initial pretraining with large amounts of data through self-supervised learning. This stage lays the foundation for the model by enabling it to understand language patterns and context.
  2. **Supervised Fine-Tuning:** The model then undergoes supervised fine-tuning with instruction data, where it is trained to respond to prompts in ways that align with specific instructions.
  3. **Reward Models Creation (RLHF Step 1):** Two separate reward models are created using human preference data –- one for helpfulness and one for safety. These models are trained to predict which of two responses is better based on human judgments.
  4. **Margin Loss and Ranking:** Unlike the previous approach that generates multiple outputs and uses a “k choose 2” comparison method, Llama 2’s dataset is based on binary comparisons, and each labeler is presented with only two responses at a time. A margin label is collected alongside binary ranks to indicate the degree of preference, which can inform the ranking loss calculation.
  5. **Rejection Sampling and Alignment using PPO (RLHF Step 2):** Finally, Llama 2 employs rejection sampling and Proximal Policy Optimization (PPO). Rejection sampling is used to draw multiple outputs and select the one with the highest reward for the gradient update. PPO is then used to align the model further, making the model’s responses more safe and helpful.
* The image below [(source)](https://ai.meta.com/resources/models-and-libraries/llama/) showing how Llama 2 leverages RLHF.

## [Reinforcement Learning with AI Feedback (RLAIF)](https://arxiv.org/abs/2309.00267)

* Reinforcement Learning with AI Feedback (RLAIF) uses AI-generated preferences instead of human annotated preferences. It leverages a powerful LLM (say, GPT-4) to generate these preferences, offering a cost-effective and efficient alternative to human-generated feedback.
* RLAIF operates by using a pre-trained LLMs to generate feedback for training another LLM. Essentially, the feedback-generating LLM serves as a stand-in for human annotators. This model evaluates and provides preferences or feedback on the outputs of the LLM being trained, guiding its learning process.
* The feedback is used to optimize the LLM’s performance for specific tasks like summarization or dialogue generation. This method enables efficient scaling of the training process while maintaining or improving the model’s performance compared to methods relying on human feedback.

## Direct Preference Optimization (DPO)

* LLMs acquire extensive world knowledge and reasoning skills via self-supervised pre-training, but precisely controlling their behavior is challenging due to their unsupervised training nature. Traditionally, methods like RLHF, discussed earlier in this article, are used to steer these models, involving two stages: training a reward model based on human preference labels and then fine-tuning the LM to align with these preferences using RL. However, RLHF presents complexities and instability issues, necessitating fitting a reward model and then training a policy to optimize this reward, which is prone to stability concerns.
* Proposed in [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) by Rafailov et al. from Stanford in 2023, Direct Preference Optimization (DPO) is a novel approach that simplifies and enhances the aforementioned process. DPO leverages a mathematical relationship between optimal policies and reward functions, demonstrating that the constrained reward maximization problem in RLHF can be optimized more effectively with a single stage of policy training. DPO redefines the RLHF objective by showing that the reward can be rewritten purely as a function of policy probabilities, allowing the LM to implicitly define both the policy and the reward function. This innovation eliminates the need for a separate reward model and the complexities of RL.
* This paper introduces a novel algorithm that gets rid of the two stages of RL, namely - fitting a reward model, and training a policy to optimize the reward via sampling. The second stage is particularly hard to get right due to stability concerns, which DPO obliterates. The way it works is, given a dataset of the form `<prompt, worse completion, better completion>`, you train your LLM using a new loss function which essentially encourages it to increase the likelihood of the better completion and decrease the likelihood of the worse completion, weighted by how much higher the implicit reward model. This method obviates the need for an explicit reward model, as the LLM itself acts as a reward model. The key advantage is that it’s a straightforward loss function optimized using backpropagation.
* The stability, performance, and computational efficiency of DPO are significant improvements over traditional methods. It eliminates the need for sampling from the LM during fine-tuning, fitting a separate reward model, or extensive hyperparameter tuning.
* The figure below from the paper illustrates that DPO optimizes for human preferences while avoiding RL. Existing methods for fine-tuning language models with human feedback first fit a reward model to a dataset of prompts and human preferences over pairs of responses, and then use RL to find a policy that maximizes the learned reward. In contrast, DPO directly optimizes for the policy best satisfying the preferences with a simple classification objective, without an explicit reward function or RL.

* Experiments demonstrate that DPO can fine-tune LMs to align with human preferences as effectively, if not more so, than traditional RLHF methods. It notably surpasses RLHF in controlling the sentiment of generations and enhances response quality in tasks like summarization and single-turn dialogue. Its implementation and training processes are substantially simpler.
* In summary, DPO aligns models by optimizing pairs of responses ranked by human feedback, assigning a higher likelihood to preferred responses over less preferred ones. This preference-based learning captures human intent without relying on the complexity of RL traditionally used in fine-tuning methods. Instead, DPO transforms the reward maximization problem into a simpler classification task, directly optimizing model outputs based on human preferences.

### DPO’s Binary Cross-Entropy Loss

* DPO works by utilizing Binary Cross-Entropy (BCE) to compare pairs of model-generated responses (preferred and dispreferred) against human preferences. The model generates two responses for each input, and human annotators indicate which response they prefer. The model then assigns probabilities to each response. The BCE loss function computes the difference between these model-assigned probabilities and the actual human preferences, penalizing the model when it assigns a higher probability to the dispreferred response. By minimizing this loss, DPO adjusts the model’s internal parameters to better align with human preferences.
* Put simply, DPO represents a shift in training language models to align with human preferences by consolidating the RLHF process into a single, end-to-end optimization step. By adapting the binary cross-entropy loss, DPO directly optimizes model behavior by adjusting log probabilities based on human feedback, making it a computationally efficient and theoretically grounded method for preference-based learning.

#### Simplified Process

1. **Response Pairs**: For each input, the model generates two responses.
2. **Human Preferences**: Humans indicate which response is preferable.
3. **Model Probabilities**: The model assigns probabilities to each response.
4. **BCE Loss**: The loss function calculates the difference between the model’s predictions and human preferences, penalizing the model more when it assigns higher probabilities to dispreferred responses.

#### Loss Function

##### Equation

* The DPO loss function, based on BCE, is formulated as:

  \[L\_{DPO}(\pi\_\theta; \pi\_{ref}) = - \mathbb{E}\_{(x, y\_w, y\_l) \sim D} \left[ \log \sigma\left(\beta \log \frac{\pi\_\theta(y\_w \mid x)}{\pi\_{ref}(y\_w \mid x)} - \beta \log \frac{\pi\_\theta(y\_l \mid x)}{\pi\_{ref}(y\_l \mid x)} \right) \right]\]
  + where:
    - \(\mathbb{E}\_{(x, y\_w, y\_l) \sim D}\) denotes the expectation over the dataset \(D\), which consists of tuples \((x, y\_w, y\_l)\) derived from human preference data. Here:
      * \(x\) is the input context (e.g., a prompt or query).
      * \(y\_w\) is the preferred response, which is deemed better.
      * \(y\_l\) is the less preferred response.
    - \(\pi\_\theta\) is the policy being optimized.
    - \(\pi\_{ref}\) is the reference policy (initial or base model).
    - \(\beta\) controls how much the model stays close to the reference policy.
    - \(\sigma\) is the logistic/sigmoid function.
* This BCE-based loss function drives the model to increase the likelihood of preferred responses while penalizing dispreferred ones.

##### Implicit KL Regularization in DPO

* Although the DPO loss does not include an explicit KL-divergence term, it is important to understand that DPO is still optimizing a KL-regularized objective. In fact, one of the core theoretical results of the DPO paper is that its binary cross-entropy loss is mathematically equivalent to the KL-constrained reward maximization objective used in standard RLHF.
* In classical RLHF, the policy optimization objective explicitly penalizes deviation from a reference policy via a KL-divergence term. This KL term serves two purposes: it prevents the policy from drifting too far from the distribution on which the reward model is reliable, and it stabilizes training by discouraging mode collapse. However, explicitly optimizing this objective requires reinforcement learning techniques such as PPO, which introduce additional variance and instability.
* DPO removes the explicit KL term by reparameterizing the reward function itself. The key insight is that, under a KL-constrained optimization problem, the optimal policy can be written in closed form as a function of the reward and the reference policy. By algebraically inverting this relationship, the reward can instead be expressed as a scaled log-ratio between the policy and the reference policy:

\[\hat r\_\theta(x, y) = \beta \log \frac{\pi\_\theta(y \mid x)}{\pi\_{ref}(y \mid x)}\]

* When this reparameterized reward is substituted into the Bradley–Terry preference model, the resulting likelihood depends only on differences of these log-ratios between preferred and dispreferred responses. As a result, the final DPO loss implicitly encodes the KL constraint through the same log probability ratios that would appear inside the KL divergence. The parameter \(\beta\) plays the same role as in RLHF: it controls how strongly the learned policy is regularized toward the reference model. A detailed discourse on the role of \(\beta\) in DPO is available in the [Role of \(\beta\) in the DPO Loss Function](#role-of-beta-in-the-dpo-loss-function) section.
* Practically, this means that DPO does not “ignore” KL regularization; rather, it absorbs it into the structure of the loss function itself. The policy is discouraged from deviating too far from the reference model because doing so would incur a penalty in the preference loss through unfavorable log-ratio terms. This implicit regularization is applied on a per-example basis, weighted by how incorrectly the model ranks preferred versus dispreferred responses.
* Conceptually, DPO can therefore be viewed as optimizing the same objective as KL-regularized RLHF, but expressed entirely as a supervised classification problem. This is the reason DPO achieves similar or better reward–KL tradeoffs compared to PPO in practice, while avoiding the instability and complexity associated with explicit KL penalties and reinforcement learning loops.
* In summary, the absence of an explicit KL-divergence term in the DPO loss is a feature, not a limitation. The KL constraint is enforced implicitly through the policy–reference log ratios inside the binary cross-entropy objective, preserving the theoretical guarantees of RLHF while enabling a simpler, more stable optimization procedure.

##### Loss Function Design Choices

###### Negative Sign in Front of the Loss

* The negative sign ensures that the optimization minimizes the negative log-likelihood, which aligns with maximizing the likelihood of predicting the preferred response correctly. This is standard in BCE loss formulations.

###### Why the Sigmoid Function (\(\sigma\)) is Used

* The sigmoid function \(\sigma(z) = \frac{1}{1 + e^{-z}}\) maps the input \(z\) to a probability in the range \([0, 1]\).
* In this case, it is applied to the log-ratio differences (scaled by \(\beta\)) between the preferred and less preferred responses. This ensures that the model output can be interpreted probabilistically, representing the confidence that the preferred response is indeed better.

###### Role of \(\beta\) in the DPO Loss Function

* The parameter \(\beta\) governs the strength of the implicit KL-divergence constraint between the optimized policy \(\pi\_\theta\) and the reference policy \(\pi\_{ref}\). Although the DPO loss does not explicitly compute a KL divergence, \(\beta\) plays the same role as the KL coefficient in classical RLHF by controlling how strongly the policy is regularized toward the reference model.
* By scaling the policy–reference log-probability ratios inside the loss, \(\beta\) determines how conservative or aggressive the preference-driven updates are.
* Proper tuning of \(\beta\) is therefore essential for achieving the desired trade-off between stable learning and effective preference optimization.
* The role of \(\beta\) in the DPO loss function can be summarized as follows:

  1. **Strength of the Implicit KL Constraint:**

     + In DPO, the implicit reward is defined as:

       \[\hat r\_\theta(x, y) = \beta \log \frac{\pi\_\theta(y \mid x)}{\pi\_{ref}(y \mid x)}.\]
       - where, \(\beta\) directly controls how costly it is for \(\pi\_\theta\) to deviate from \(\pi\_{ref}\).
       - **High \(\beta\):** Deviations from the reference policy are penalized more strongly, corresponding to a stronger KL constraint. The learned policy remains close to \(\pi\_{ref}\) and evolves conservatively.
       - **Low \(\beta\):** Deviations are penalized less, corresponding to a weaker KL constraint. The policy is freer to move away from the reference model in order to satisfy preferences.
  2. **Scaling of Preference Gradients:**

     + \(\beta\) scales the difference in log-probabilities between the preferred (\(y\_w\)) and less preferred (\(y\_l\)) responses inside the sigmoid of the binary cross-entropy loss.
     + Larger values of \(\beta\) dampen the effective gradient for a given policy mismatch, leading to smaller, more stable updates.
     + Smaller values of \(\beta\) amplify preference-driven gradients, producing stronger corrective updates when the model ranks responses incorrectly.
  3. **Trade-off Between Alignment and Stability:**

     + \(\beta\) mediates the core trade-off in DPO:

       - **Stronger KL Regularization (High \(\beta\)):** Prioritizes stability, generalization, and retention of desirable behaviors from the reference policy, at the cost of slower or weaker preference alignment.
       - **Weaker KL Regularization (Low \(\beta\)):** Prioritizes rapid alignment with preference data, at the risk of overfitting, reduced diversity, or drifting into poorly calibrated regions of the policy space.
* In practice, varying \(\beta\) traces out a continuum of solutions analogous to the reward–KL trade-off curve in RLHF. This makes \(\beta\) the primary control knob in DPO for determining how strongly the model is constrained by the reference policy while learning from human preferences.

###### Significance of the DPO Loss

* The loss measures how well the model \(\pi\_\theta\) aligns with human preferences, as encoded in the dataset \(D\).
* By using BCE, the objective becomes a comparison of logits (log probabilities) between the preferred (\(y\_w\)) and less preferred (\(y\_l\)) responses. Minimizing this loss drives the model to produce outputs that increasingly favor \(y\_w\) over \(y\_l\) while balancing regularization (\(\beta\)) to avoid over-divergence from the reference policy \(\pi\_{ref}\).

##### Mapping from the Standard Binary Cross-Entropy Loss to the DPO Loss

###### Standard Binary Cross-Entropy Loss

* To recap, the Binary Cross-Entropy loss for a single prediction \(z\) (where \(z = \pi(y\_w \mid x) - \pi(y\_l \mid x)\)) and its target label \(t \in \{0, 1\}\) is defined as:

  \[L\_{BCE}(z, t) = - \left[ t \cdot \log(\sigma(z)) + (1 - t) \cdot \log(1 - \sigma(z)) \right]\]
  + where,
    - \(z\): The logit (unbounded real value) representing the model’s confidence in the preferred label.
    - \(\sigma(z) = \frac{1}{1 + e^{-z}}\): The sigmoid function maps the logit to a probability.
    - \(t\): The binary target label, where \(t = 1\) if \(y\_w\) is the preferred label and \(t = 0\) if \(y\_l\) is preferred.

###### Mapping BCE Loss to DPO Loss

* In the DPO framework:

  1. The target is implicitly encoded by the comparison of \(y\_w\) (preferred) and \(y\_l\) (less preferred). Effectively, \(t = 1\) for \(y\_w\).
  2. The logit \(z\) is calculated as the difference in log-probabilities (scaled by \(\beta\)):

     \[z = \beta \log \frac{\pi\_\theta(y\_w \mid x)}{\pi\_{ref}(y\_w \mid x)} - \beta \log \frac{\pi\_\theta(y\_l \mid x)}{\pi\_{ref}(y\_l \mid x)}\]
     + This difference represents the model’s confidence in \(y\_w\) being better than \(y\_l\), adjusted for the divergence from the reference policy.
  3. Plugging \(z\) into the BCE loss for \(t = 1\), the equation becomes:

     \[L\_{DPO} = - \log(\sigma(z))\]
  4. Expanding \(z\), we get:

     \[L\_{DPO} = - \log \sigma\left(\beta \log \frac{\pi\_\theta(y\_w \mid x)}{\pi\_{ref}(y\_w \mid x)} - \beta \log \frac{\pi\_\theta(y\_l \mid x)}{\pi\_{ref}(y\_l \mid x)} \right)\]

###### Intuition of the Mapping

* **Standard BCE Loss:** Compares logits \(z\) against a binary target \(t\) (1 for positive, 0 for negative) and penalizes predictions deviating from the target.
* **DPO Loss:** Adapts the BCE framework to pairwise preferences, where:
  + \(z\) reflects the scaled log-ratio difference between \(y\_w\) and \(y\_l\).
  + Implicitly assumes \(t = 1\) (i.e., \(y\_w\) is the preferred response).
* By minimizing \(L\_{DPO}\), the model learns to increase the scaled log-probability of \(y\_w\) relative to \(y\_l\), aligning with human preferences while staying close to \(\pi\_{ref}\).

##### Key Insights

* **DPO’s Efficiency**: DPO simplifies the traditional RLHF pipeline by unifying policy learning and reward modeling into a single, efficient process. Instead of requiring a two-stage process (learning a reward model and then optimizing with RL), DPO directly optimizes the policy using human preferences as implicit rewards.
* **Streamlined Approach**: By using BCE to treat preference optimization as a binary classification task, DPO minimizes complexity and computational overhead. The model learns to classify between preferred and dispreferred responses, adjusting its behavior accordingly.

#### Understanding DPO’s Loss Function

* [Unveiling the Hidden Reward System in Language Models: A Dive into DPO](https://allam.vercel.app/post/dpo/) offers a detailed treatment of DPO’s loss function and its components by providing an excellent mathematical dissection of how the DPO loss directly encodes human preference learning without requiring an explicit reward model.
* DPO’s loss is a mathematically principled approach to translating human preference data into direct optimization signals for large language models. Its foundation lies in a set of well-structured mechanisms that work together to enable efficient and stable preference learning without the complexities of traditional reinforcement learning. The key aspects are as follows:

  + At its core, DPO introduces an **implicit reward function** defined by the ratio of the model’s output probability to that of a reference policy:\[\hat{r}\_\theta(x, y) = \beta \log \frac{\pi\_\theta(y \mid x)}{\pi\_{ref}(y \mid x)}\]
  + This formulation recasts preference alignment as a **binary cross-entropy classification** task, distinguishing between preferred and dispreferred responses. This eliminates the need for an explicit reward model or policy sampling, streamlining the learning process.
  + The **divergence control factor (\(\beta\))** serves as a critical parameter, controlling how much the model is allowed to deviate from the reference policy. It balances the trade-off between preserving stability and encouraging adaptation toward human-preferred behaviors.
  + Additionally, the **gradient structure** of DPO tightly integrates the **reward difference** (indicating how much adjustment is needed) with the **policy gradient difference** (defining the direction of the update). This natural coupling supports efficient learning dynamics.
* Together, these insights show how DPO consolidates the traditionally complex reinforcement learning pipeline into a **single, differentiable loss function**. This enables large language models to learn from human feedback using straightforward gradient descent, ensuring both computational efficiency and training stability.
* Let’s break it down step by step using annotations to visualize the key mathematical components, starting with the DPO loss which is given by:

\[L\_{DPO}(\pi\_\theta; \pi\_{ref}) =
-\mathbb{E}\_{(x, y\_w, y\_l) \sim D}
\Big[
\log \sigma \Big(
\underbrace{
\beta \log \frac{\pi\_\theta(y\_w \mid x)}{\pi\_{ref}(y\_w \mid x)}
}\_{\text{Encourages preferred response}\, (y\_w)}
\,-\,
\underbrace{
\beta \log \frac{\pi\_\theta(y\_l \mid x)}{\pi\_{ref}(y\_l \mid x)}
}\_{\text{Discourages dispreferred response}\, (y\_l)}
\Big)
\Big]\]

##### Component-by-Component Interpretation

1. **Relative Probability Ratios**:

   * Each term inside the logarithm compares how likely the current model \(\pi\_\theta\) finds a response relative to the reference model \(\pi\_{ref}\):\[\frac{\pi\_\theta(y \mid x)}{\pi\_{ref}(y \mid x)}\]
   * This ratio measures the **relative confidence** of the new model versus the baseline.

     + When the ratio is greater than 1, the model assigns higher probability to \(y\) than the reference model does.
     + When the ratio is less than 1, the model assigns lower probability to \(y\).
       Hence, these ratios encode how the model’s preferences evolve compared to its reference version.
   * The term for \(y\_w\) encourages the model to increase its probability for preferred responses, while the term for \(y\_l\) penalizes the model for assigning high probability to dispreferred responses.
2. **Divergence Control Factor (\(\beta\))**:

   * The hyperparameter \(\beta\) serves as a **divergence control factor**, regulating how much the current model \(\pi\_\theta\) is allowed to deviate from the reference model \(\pi\_{ref}\).

     + A larger \(\beta\) emphasizes the difference between the preferred and dispreferred responses, allowing stronger learning signals but also more deviation from the reference policy.
     + A smaller \(\beta\) softens these differences, keeping the model more tightly aligned with the reference.
   * In other words, \(\beta\) balances **adaptability** (learning human preferences) and **stability** (staying close to the reference model).
3. **Sigmoid Function (\(\sigma\))**:

   * The sigmoid \(\sigma(z) = \frac{1}{1 + e^{-z}}\) transforms the difference between the preferred and dispreferred ratios into a probability-like value between 0 and 1.

     + When the preferred ratio is much higher than the dispreferred one, the argument of \(\sigma\) is positive, so \(\sigma(z) \approx 1\), leading to a small loss.
     + When the model mistakenly prefers the dispreferred response, the argument becomes negative, so \(\sigma(z) \approx 0\), leading to a large loss.
   * This acts as a smooth probabilistic measure of whether the model ranks \(y\_w\) above \(y\_l\).
4. **Binary Cross-Entropy (BCE) Structure**:

   * The outer negative log \(-\log \sigma(\cdot)\) forms the **binary cross-entropy** component of the loss, treating each preference pair \((y\_w, y\_l)\) as a binary classification example:

     + Label 1 means the preferred response should win.
     + Label 0 means the dispreferred response should lose.
   * Minimizing this BCE loss drives the model to predict preference outcomes consistent with human annotations.

##### Intuitive Breakdown

* The DPO loss can be viewed as consisting of **two main terms** — one that strengthens the model’s preference for human-approved responses, and another that suppresses its tendency to produce human-disapproved responses:

  \[L\_{DPO} =
  -\mathbb{E}\Bigg[
  \log \sigma\Big(
  \underbrace{
  \beta \log \frac{\pi\_\theta(y\_w \mid x)}{\pi\_{ref}(y\_w \mid x)}
  }\_{\text{Term 1: increase model’s preference for human-approved responses}}
  \,-\,
  \underbrace{
  \beta \log \frac{\pi\_\theta(y\_l \mid x)}{\pi\_{ref}(y\_l \mid x)}
  }\_{\text{Term 2: suppress model’s preference for human-disapproved responses}}
  \Big)
  \Bigg]\]
  + **Term 1** amplifies the relative log probability of the preferred response \(y\_w\). It pushes the model to make \(\pi\_\theta(y\_w \mid x)\) larger than \(\pi\_{ref}(y\_w \mid x)\).
  + **Term 2** reduces the relative log probability of the dispreferred response \(y\_l\). It drives the model to make \(\pi\_\theta(y\_l \mid x)\) smaller than \(\pi\_{ref}(y\_l \mid x)\).
  + Their **difference** determines how much more the model should prefer \(y\_w\) over \(y\_l\).
  + The **sigmoid** converts this difference into a probability that \(y\_w\) is preferred, and the **negative log** penalizes incorrect preference predictions.
* This decomposition highlights that the DPO loss directly represents a **pairwise preference comparison**, where the model learns to correctly order responses without explicitly computing rewards.

##### Gradient Interpretation (Implicit Reward Function)

* DPO implicitly defines a reward function for each response as:

\[\hat{r}\_\theta(x, y) = \beta \log \frac{\pi\_\theta(y \mid x)}{\pi\_{ref}(y \mid x)}\]

* This implicit reward captures how much the model favors a response relative to the reference. Substituting it into the loss’s gradient gives:

\[\nabla\_\theta L\_{DPO} =
-\beta , \mathbb{E}\Big[
\sigma\big(\hat{r}\_\theta(x, y\_l) - \hat{r}\_\theta(x, y\_w)\big)
\cdot
\big(\nabla\_\theta \log \pi\_\theta(y\_w \mid x) - \nabla\_\theta \log \pi\_\theta(y\_l \mid x)\big)
\Big]\]

* This equation has two conceptually distinct parts:

  1. **Reward Difference Term**:

     + The expression \(\sigma(\hat{r}\_\theta(x, y\_l) - \hat{r}\_\theta(x, y\_w))\) represents *how wrong* the model’s current preference ordering is.

       - If \(\hat{r}\_\theta(x, y\_w) > \hat{r}\_\theta(x, y\_l)\), meaning the model correctly prefers \(y\_w\), the difference is negative and the sigmoid output is small—producing a small gradient update.
       - If \(\hat{r}\_\theta(x, y\_w) < \hat{r}\_\theta(x, y\_l)\), meaning the model prefers the wrong response, the sigmoid output is large, increasing the correction strength.
  2. **Policy Gradient Difference Term**:

     + The factor \(\nabla\_\theta \log \pi\_\theta(y\_w \mid x) - \nabla\_\theta \log \pi\_\theta(y\_l \mid x)\) defines the **direction** in which the model’s parameters should be adjusted.

       - The first gradient increases the likelihood of generating \(y\_w\).
       - The second gradient decreases the likelihood of generating \(y\_l\).
     + Together, they move the model toward better alignment with human preferences.

#### How does DPO generate two responses and assign probabilities to them?

* In DPO, generating two responses and assigning probabilities to each response involves a nuanced process:

  1. **Generating Two Responses**:
     + The responses are typically generated using a supervised fine-tuned language model. This model, when given an input prompt, generates a set of potential responses.
     + These responses are often generated through sampling methods like varying temperature, using different [token sampling methods](../token-sampling) such as top-\(p\), top-\(k\), beam search, etc., which can produce diverse outputs.
  2. **Assigning Probabilities**:
     + Language models indeed assign probabilities at the token level, predicting the likelihood of each possible next token given the previous tokens.
     + The probability of an entire response (sequence of tokens) is calculated as the product of the probabilities of individual tokens in that sequence, as per the model’s prediction.
     + For DPO, these probabilities are used to calculate the loss based on human preferences. The model is trained to increase the likelihood of the preferred response and decrease that of the less preferred one.
* Through this process, DPO leverages human feedback to preference-optimize the model, encouraging it to generate more human-aligned outputs.

#### DPO and it’s use of the Bradley-Terry model

* **Overview of the Bradley-Terry Model**:
  + The Bradley-Terry model is a probability model used for pairwise comparisons. It assigns a score to each item (in this context, model outputs), and the probability that one item is preferred over another is a function of their respective scores. Formally, if item \(i\) has a score \(s\_i\) and item \(j\) has a score \(s\_j\), the probability \(P(i \text{ is preferred over } j)\) is given by:\[P(i \text{ is preferred over } j) = \frac{\exp(s\_i)}{\exp(s\_i) + \exp(s\_j)}\]
* **Application in DPO for LLM Alignment**:
  1. **Data Collection**:
     + Human evaluators provide pairwise comparisons of model outputs. For example, given two responses from the LLM, the evaluator indicates which one is better according to specific criteria (e.g., relevance, coherence, correctness).
  2. **Modeling Preferences**:
     + The outputs of the LLM are treated as items in the Bradley-Terry model. Each output has an associated score reflecting its quality or alignment with human preferences.
  3. **Score Estimation**:
     + The scores \(s\_i\) for each output are estimated using the observed preferences. If output \(i\) is preferred over output \(j\) in several comparisons, \(s\_i\) will be higher than \(s\_j\). The scores are typically estimated using maximum likelihood estimation (MLE) or other optimization techniques suited for the Bradley-Terry model.
  4. **Optimization**:
     + Once the scores are estimated, the LLM is fine-tuned to maximize the likelihood of generating outputs with higher scores. The objective is to adjust the model parameters so that the outputs align better with human preferences as captured by the Bradley-Terry model scores.
* **Detailed Steps in DPO**:
  1. **Generate Outputs**:
     + Generate multiple outputs for a given prompt using the LLM.
  2. **Pairwise Comparisons**:
     + Collect human feedback by asking evaluators to compare pairs of outputs and indicate which one is better.
  3. **Fit Bradley-Terry Model**:
     + Use the collected pairwise comparisons to fit the Bradley-Terry model and estimate the scores for each output.
  4. **Update LLM**:
     + Fine-tune the LLM using the estimated scores. The objective is to adjust the model parameters such that the likelihood of producing higher-scored (preferred) outputs is maximized. This step often involves gradient-based optimization techniques where the loss function incorporates the Bradley-Terry model probabilities.
       - By iteratively performing these steps, the LLM can be aligned more closely with human preferences, producing outputs that are more likely to be preferred by human evaluators.
* **Summary**:
  + The Bradley-Terry model plays a crucial role in the Direct Preference Optimization method by providing a statistical framework for modeling and estimating the preferences of different model outputs. This, in turn, guides the fine-tuning of the LLM to align its outputs with human preferences effectively.

##### How does DPO implicitly use a Bradley-Terry Model (if it does not explicitly use a reward model)?

* DPO uses the Bradley-Terry model implicitly, even if it does not explicitly employ a traditional reward model. Here’s how this works:

###### Key Concepts in DPO Without an Explicit Reward Model

1. **Pairwise Comparisons**:
   * Human evaluators provide pairwise comparisons between outputs generated by the LLM. For example, given two outputs, the evaluator indicates which one is preferred.
2. **Logistic Likelihood**:
   * The Bradley-Terry model is essentially a logistic model used for pairwise comparisons. The core idea is to model the probability of one output being preferred over another based on their latent scores.

###### Implicit Use of Bradley-Terry Model

* Without training an explicit reward model, DPO leverages the principles behind the Bradley-Terry model in the following manner:

1. **Score Assignment through Logit Transformation**:
   * For each output generated by the LLM, assign a latent score. This score can be considered as the logit (log-odds) of the output being preferred.
   * Given two outputs, \(o\_i\) and \(o\_j\), with logits (latent scores) \(s\_i\) and \(s\_j\), the probability that \(o\_i\) is preferred over \(o\_j\) follows the logistic function:
     \(P(o\_i \text{ is preferred over } o\_j) = \frac{\exp(s\_i)}{\exp(s\_i) + \exp(s\_j)}\)
2. **Optimization Objective**:
   * Construct a loss function based on the likelihood of observed preferences. If \(o\_i\) is preferred over \(o\_j\) in the dataset, the corresponding likelihood component is:
     \(L = \log P(o\_i \text{ is preferred over } o\_j) = \log \left(\frac{\exp(s\_i)}{\exp(s\_i) + \exp(s\_j)} \right)\)
   * The overall objective is to maximize this likelihood across all pairwise comparisons provided by human evaluators.
3. **Gradient Descent for Fine-Tuning**:
   * Instead of explicitly training a separate reward model, the LLM is fine-tuned using gradients derived from the likelihood function directly.
   * During backpropagation, the gradients with respect to the LLM’s parameters are computed from the likelihood of the preferences, effectively pushing the model to produce outputs that align with higher preference scores.

###### Steps in DPO Without Explicit Reward Model

1. **Generate Outputs**:
   * Generate multiple outputs for a set of prompts using the LLM.
2. **Collect Pairwise Comparisons**:
   * Human evaluators compare pairs of outputs and indicate which one is preferred.
3. **Compute Preference Probabilities**:
   * Use the logistic model (akin to Bradley-Terry) to compute the probability of each output being preferred over another.
4. **Construct Likelihood and Optimize**:
   * Formulate the likelihood based on the observed preferences and optimize the LLM’s parameters to maximize this likelihood.

###### Practical Implementation

* **Training Loop**:
  + In each iteration, generate outputs, collect preferences, compute the logistic likelihood, and perform gradient descent to adjust the LLM parameters.
* **Loss Function**:
  + The loss function directly incorporates the Bradley-Terry model’s probabilities without needing an intermediate reward model:
    \(\text{Loss} = -\sum\_{(i,j) \in \text{comparisons}} \log \left(\frac{\exp(s\_i)}{\exp(s\_i) + \exp(s\_j)} \right)\)
* By optimizing this loss function, DPO ensures that the LLM’s outputs increasingly align with human preferences, implicitly using the Bradley-Terry model’s probabilistic framework without explicitly training a separate reward model. This direct approach simplifies the alignment process while leveraging the robust statistical foundation of the Bradley-Terry model.

#### Video Tutorial

* [This](https://www.youtube.com/watch?v=hvGa5Mba4c8) video by [Umar Jamil](https://www.youtube.com/@umarjamilai) explains the DPO pipeline, by deriving it step by step while explaining all the inner workings.
* After briefly introducing the topic of AI alignment, the video reviews RL, a topic that is necessary to understand the reward model and its loss function. Next, it derives the loss function step-by-step of the reward model under the Bradley-Terry model of preferences, a derivation that is missing in the DPO paper.
* Using the Bradley-Terry model, it builds the loss of the DPO algorithm, not only explaining its math derivation, but also giving intuition on how it works.
* In the last part, it describes how to use the loss practically, that is, how to calculate the log probabilities using a Transformer model, by showing how it is implemented in the Hugging Face library.

#### Summary

* RLHF is the most “dicey” part of LLM training and the one that needed the most art vs. science. DPO seeks to simplify that by removing RL out of the equation and not requiring a dedicated reward model (with the LLM serving as the reward model). The process it follows is as follows:
  1. Treat a foundational instruction tuned LLM as the reference LLM.
  2. Generate pairs of outputs (using say, different [token sampling/decoding](../token-sampling) methods or temperature scaling) to the same prompt and have humans choose which one they like, leading to a dataset of human preferences/feedback.
  3. Add a linear layer to the LLM so that it outputs a scalar value, and tune this new model with a new loss function called DPO loss which is based on binary cross entropy loss (compute log-ratio of scalar outputs of the reference LLM and the one being tuned, multiply by a divergence parameter).
  4. Drop the last linear layer, and you have a fine tuned LLM on human feedback.

## Kahneman-Tversky Optimization (KTO)

* Proposed in [Human-Centered Loss Functions (HALOs)](https://github.com/ContextualAI/HALOs/blob/main/assets/report.pdf) by Ethayarajh et al. from Stanford and Contextual AI, Kahneman-Tversky Optimization (KTO) is a novel approach to aligning LLMs with human feedback.
* KTO is a human-centered loss function that directly maximizes the utility of language model generations instead of maximizing the log-likelihood of preferences as current methods do. This approach is named after Daniel Kahneman and Amos Tversky, who are known for their work in prospect theory, a theory of how humans make decisions about uncertain outcomes. KTO is based on the principles of prospect theory, a theory in behavioral economics. Unlike traditional methods, KTO focuses on maximizing the utility of LLM generations by aligning them with human feedback.
* KTO achieves the goal of generating desirable outputs by using a utility function to guide the training of a language model. This process involves several key steps:

  1. **Utility Function Definition**: A utility function is defined based on the principles of Kahneman-Tversky’s prospect theory. This function assigns a value to each possible output of the language model, indicating its desirability or utility from a human perspective. The utility values can be determined based on factors like relevance, coherence, or adherence to specific criteria.
  2. **Generating Outputs**: During training, the language model generates outputs based on given inputs. These outputs are complete sequences, such as sentences or paragraphs, rather than individual tokens.
  3. **Evaluating Outputs**: Each generated output is evaluated using the utility function. The utility score reflects how desirable or aligned the output is with human preferences or objectives.
  4. **Optimizing the Model**: The model’s parameters are updated to increase the likelihood of generating outputs with higher utility scores. The optimization process aims to maximize the expected utility of the outputs, essentially encouraging the model to produce more desirable results.
  5. **Iterative Training**: This process is iterative, with the model continually generating outputs, receiving utility evaluations, and updating its parameters. Over time, the model learns to produce outputs that are increasingly aligned with the utility function’s assessment of desirability.
* In essence, KTO shifts the focus from traditional training objectives, like next-token prediction or fitting to paired preference data, to directly optimizing for outputs that are considered valuable or desirable according to a utility-based framework. This approach can be particularly effective in applications where the quality of the output is subjective or where specific characteristics of the output are valued.

  1. **What is KTO?**
     + KTO is an alignment methodology that leverages the concept of human utility functions as described in prospect theory. It aligns LLMs by directly maximizing the utility of their outputs, focusing on whether an output is considered desirable or not by humans.
     + This method does not require detailed preference pairs for training, which is a departure from many existing alignment methodologies.
  2. **What Kind of Data Does KTO Require?**
     + KTO obliterates the need for paired-preference ranking/comparison data and simplifies data requirements significantly. It only needs binary labels indicating whether an LLM output is desirable or undesirable. Put simply, with it’s binary preference data requirement, KTO contrasts with methods such as PPO and DPO that require detailed preference pairs.
     + The simplicity in data requirements makes KTO more practical and applicable in real-world scenarios where collecting detailed preference data is challenging.
  3. **Advantages Over DPO and PPO:**
     + Compared to DPO and PPO, KTO offers several advantages:
       - **Simplicity in Data Collection**: Unlike DPO and PPO, which require paired-preference data (i.e., ranking/comparison data) which is difficult to obtain, KTO operates efficiently with unpaired binary feedback on outputs.
       - **Practicality in Real-World Application**: KTO’s less stringent data requirements make it more suitable for scenarios where collecting detailed preferences is infeasible.
       - **Focus on Utility Maximization**: KTO aligns with the practical aspects of human utility maximization, potentially leading to more user-friendly and ethically aligned outputs.
  4. **Results with KTO Compared to DPO and PPO:**
     + When applied to models of different scales (from 1B to 30B parameters), KTO has shown to match or exceed the performance of methods like DPO in terms of alignment quality.
     + KTO, even without supervised finetuning, significantly outperforms other methods at larger scales, suggesting its effectiveness in aligning models in a more scalable and data-efficient manner.
     + In terms of practical utility, the results indicate that KTO can lead to LLM outputs that are better aligned with human preferences and utility considerations, particularly in scenarios where detailed preference data is not available.
* KTO operates without paired preference data, focusing instead on maximizing the utility of language model generations based on whether an output is desirable or undesirable. This is different from the traditional approach of next-token prediction and paired preference data used in methods like DPO.
* Here’s how KTO functions:

  1. **Utility-Based Approach**: KTO uses a utility function, inspired by Kahneman-Tversky’s prospect theory, to evaluate the desirability of outputs. The utility function assigns a value to each possible output of the language model, reflecting how desirable (or undesirable) that output is from a human perspective.
  2. **Data Requirement**: Unlike DPO, KTO does not need paired comparisons between two outputs. Instead, it requires data that indicates whether a specific output for a given input is considered desirable or not. This data can come from human judgments or predefined criteria.
  3. **Loss Function**: The loss function in KTO is designed to maximize the expected utility of the language model’s outputs. It does this by adjusting the model’s parameters to increase the likelihood of generating outputs that have higher utility values. Note that the KTO loss function is not a binary cross-entropy loss. Instead, it is inspired by prospect theory and is designed to align large language models with human feedback. KTO focuses on human perception of losses and gains, diverging from traditional loss functions like binary cross-entropy that are commonly used in machine learning. This novel approach allows for a more nuanced understanding and incorporation of human preferences and perceptions in the training of language models. [KTO’s Loss Function](#ktos-loss-function) further details the specifics of KTO’s loss function.
  4. **Training Process**: During training, the language model generates outputs, and the utility function evaluates these outputs. The model’s parameters are then updated to favor more desirable outputs according to the utility function. This process differs from next-token prediction, as it is not just about predicting the most likely next word, but about generating entire outputs that maximize a utility score.
  5. **Implementation**: In practical terms, KTO could be implemented as a fine-tuning process on a pre-trained language model. The model generates outputs, the utility function assesses these, and the model is updated to produce better-scoring outputs over iterations.
* KTO is focused more on the overall utility or value of the outputs rather than just predicting the next token. It’s a more holistic approach to aligning a language model with human preferences or desirable outcomes.
* In summary, KTO represents a shift towards a more practical and scalable approach to aligning LLMs with human feedback, emphasizing utility maximization and simplicity in data requirements.

#### KTO’s Loss Function

* KTO is inspired by the behavioral models of decision-making introduced by Daniel Kahneman and Amos Tversky, particularly their prospect theory. KTO adapts these concepts into a loss function that aligns LLMs with human feedback by capturing human biases such as loss aversion and risk sensitivity. Below is a comprehensive explanation of KTO’s loss function, including both general principles from Prospect Theory and specific details from the paper you provided.

#### Core Principles from Prospect Theory

* In prospect theory, human decision-making under uncertainty deviates from maximizing expected value due to biases like loss aversion and nonlinear probability weighting. These concepts are fundamental to the loss function used in KTO:

1. **Value Function**: This captures how people perceive gains and losses differently:
   * It is concave for gains (risk-averse for gains) and convex for losses (risk-seeking for losses).
   * Losses loom larger than gains, which is modeled by a loss aversion parameter \(\lambda\) (typically \(\lambda > 1\)).
   * Mathematically, the value function \(v(x)\) can be expressed as:\[v(x) =
   \begin{cases}
   x^\alpha & \text{if } x \geq 0 \\
   -\lambda (-x)^\beta & \text{if } x < 0
   \end{cases}\]
   * where:
     + \(\alpha, \beta\) control the diminishing sensitivity to gains and losses.
     + \(\lambda\) represents the **loss aversion** factor, typically greater than 1, meaning losses are felt more intensely than gains.
2. **Probability Weighting Function**: Humans tend to overweight small probabilities and underweight large probabilities. While not central to KTO, this element of Prospect Theory highlights how subjective perceptions of uncertainty influence decisions.

#### Key Elements of KTO’s Loss Function

* The KTO loss function builds on these insights, tailoring them for optimizing LLM alignment with human feedback. The key elements of the KTO loss function are:

  1. **Adapted Value Function**: Instead of the piecewise value function in classic Prospect Theory, KTO uses a logistic function \(\sigma\) to maintain concavity for gains and convexity for losses. This also introduces a risk aversion parameter \(\beta\), which controls the degree of risk aversion and is explicitly incorporated into the model to manage how sharply the value saturates.
  2. **Separate Loss Aversion Parameters**:
     + In KTO, the original loss aversion parameter \(\lambda\) is replaced with two separate hyperparameters: \(\lambda\_D\) for desirable outputs and \(\lambda\_U\) for **undesirable** outputs. This split allows the model to handle these two types of feedback differently, reflecting more granular control over risk aversion depending on whether the output is positive or negative.
  3. **KL Divergence as a Reference Point**:
     + The reference point for the model is defined by the KL divergence between the current model’s policy \(\pi\_\theta\) and the reference policy \(\pi\_{\text{ref}}\). This term controls how much the current model’s outputs deviate from the pretrained reference model and acts as the reference point \(z\_0\) for evaluating gains and losses in the optimization.

#### Loss Function Equation

* The KTO loss function can be mathematically formulated as:

  \[L\_{KTO}(\pi\_\theta, \pi\_{\text{ref}}) = \mathbb{E}\_{x,y \sim D}[\lambda\_y - v(x, y)]\]
  + where:
    \(r\_\phi(x, y) = \log \frac{\pi\_\theta(y \mid x)}{\pi\_{\text{ref}}(y \mid x)}\)
    \(z\_0 = \text{KL}(\pi\_\theta(y' \mid x) \mid\mid \pi\_{\text{ref}}(y' \mid x))\)
* The value function \(v(x, y)\) changes depending on whether \(y\) is a desirable or undesirable output:

\[v(x, y) =
\begin{cases}
\lambda\_D \sigma(\beta(r\_\phi(x, y) - z\_0)) & \text{if } y \sim \text{desirable} \\
\lambda\_U \sigma(\beta(z\_0 - r\_\phi(x, y))) & \text{if } y \sim \text{undesirable}
\end{cases}\]

#### Intuition Behind the Loss Function

* If the model increases the reward of a desirable example in a blunt manner, the KL divergence penalty will also increase, preventing improvement in the loss. This forces the model to learn specific features of desirable outputs, leading to improved alignment.
* The logistic function \(\sigma\) ensures that as rewards increase, the model becomes more risk-averse for gains and more risk-seeking for losses, mimicking the behavior predicted by Kahneman and Tversky’s Prospect Theory.

#### Practical Considerations

* **Risk Aversion Control**: The hyperparameter \(\beta\) allows fine-tuning of the model’s sensitivity to gains and losses. Increasing \(\beta\) increases risk aversion in gains and risk-seeking behavior in losses.
* **Desirable and Undesirable Output Weighting**: The two loss aversion parameters \(\lambda\_D\) and \(\lambda\_U\) provide flexibility in how much weight the model gives to desirable vs. undesirable outputs. This is crucial when the training data contains an imbalance between positive and negative examples.

#### Summary

* KTO’s loss function is a prospect-theoretic loss that incorporates:
  + **Loss aversion**: Through separate hyperparameters for desirable and undesirable outcomes.
  + **Risk sensitivity**: Controlled by the parameter \(\beta\), which regulates how quickly the model’s value function saturates for gains and losses.
  + **KL divergence**: To ensure the model does not drift too far from the reference point, enforcing stability in the optimization.
* The KTO approach leverages human-like biases such as loss aversion and risk preferences, aligning the optimization process with how humans evaluate uncertainty, thus enabling better alignment of large language models with human feedback.

## Group Relative Policy Optimization (GRPO)

* Group Relative Policy Optimization (GRPO), introduced in [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) by Shao et al. (2024), is an RL algorithm that enhances the PPO method by eliminating the critic model and instead using group-level scores for baseline estimation. The main goals of GRPO are to improve computational efficiency, reduce memory usage, and provide effective fine-tuning for models like DeepSeekMath.
* The following figure from the paper demonstrates PPO and GRPO. GRPO foregoes the value/critic model, instead estimating the baseline from group scores, significantly reducing training resources.

* A detailed discourse on GRPO is available in the [DeekSeek-R1](../deepseek-R1/) primer.

#### Key Features and Approach

1. **Actor-Only Framework**: GRPO replaces the value (critic) model from PPO with a simpler baseline calculated using group rewards. This makes GRPO less computationally intensive.
2. **Group-Based Optimization**: It samples multiple outputs (group sampling) for a given input, calculates relative rewards within the group, and uses these rewards to estimate advantages for policy updates.
3. **Adaptation for LLMs**: GRPO aligns with the comparative nature of RL for large language models, where reward functions are typically trained using pairwise comparisons of outputs.

#### GRPO Equations

* Starting with the objective function for PPO, let’s derive the objective function for GRPO:

  1. **PPO Objective Function**:

     + The PPO objective (for reference) is:

       \[J\_{\text{PPO}}(\theta) = \mathbb{E}\left[\min\left(r\_t(\theta)\hat{A\_t},\,\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A\_t}\right)\right]\]
       - where:

         * \(r\_t(\theta) = \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}{\pi\_{\text{old}}(o\_t \mid q, o\_{<t})}\) is the **probability ratio** between the current policy \(\pi\_\theta\) (the model being updated) and the old policy \(\pi\_{\text{old}}\) (the policy before the update). This ratio quantifies how much the new policy changes the likelihood of generating token \(o\_t\) given its context.
         * \(\hat{A\_t}\) is the **advantage function**, measuring how much better the chosen action (token) performs compared to the expected baseline performance under the old policy.
         * \(\epsilon\) is the **clipping threshold**, limiting how far the ratio \(r\_t(\theta)\) can deviate from 1 to prevent excessively large policy updates that destabilize learning.
  2. **GRPO Objective**:

     + The GRPO objective modifies the PPO formulation by removing the critic network and replacing its value-based advantage with group-based relative scoring:

       \[J\_{\text{GRPO}}(\theta) = \mathbb{E}\_{q, {o\_i}\_{i=1}^G} \frac{1}{G} \sum\_{i=1}^G \frac{1}{|o\_i|} \sum\_{t=1}^{|o\_i|} \min\left(r\_{i,t}(\theta)\hat{A}\_{i,t},\,\text{clip}(r\_{i,t}(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A}\_{i,t}\right)\]
       - where:

         * \(G\) is the **group size**, representing how many independent outputs \(o\_i\) are sampled from the old policy for each input query \(q\).
         * \(\mid o\_i \mid\) is the **length** (number of tokens) of each generated output sequence \(o\_i\).
         * \(r\_{i,t}(\theta) = \frac{\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})}{\pi\_{\text{old}}(o\_{i,t} \mid q, o\_{i,<t})}\) is the **per-token probability ratio**, analogous to PPO’s ratio but computed for each token within each sampled output.
         * \(\hat{A}\_{i,t}\) is the **group-relative advantage** for the \(t^{th}\) token of output \(o\_i\), estimated based on the relative performance of \(o\_i\) compared to other outputs in the group.
  3. **Advantage Calculation**:

     + GRPO estimates the advantage \(\hat{A}\_{i,t}\) directly from group-based rewards instead of using a learned critic:

       \[\hat{A}\_{i,t} = \frac{r\_i - \text{mean}(r)}{\text{std}(r)}\]
       - where:

         * \(r\_i\) is the **scalar reward** assigned to output \(o\_i\), typically derived from a task-specific metric or reward model.
         * \(\text{mean}(r)\) is the **average reward** across all outputs in the group, serving as a normalization baseline.
         * \(\text{std}(r)\) is the **standard deviation** of group rewards, scaling the advantage to maintain stable gradients across varying reward magnitudes.
  4. **KL Regularization**:

     + GRPO introduces a **per-token KL divergence penalty** to stabilize optimization and constrain the updated policy’s drift from the reference:

       \[D\_{\text{KL}}[\pi\_\theta \mid\mid \pi\_{\text{ref}}] =
       \frac{\pi\_{\text{ref}}(o\_{i,t} \mid q, o\_{i,<t})}
       {\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})}
       - \log \frac{\pi\_{\text{ref}}(o\_{i,t} \mid q, o\_{i,<t})}
       {\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})} - 1\]
       - where:

         * \(\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})\) is the **probability** of token \(o\_{i,t}\) given context \(q, o\_{i,<t}\) under the **current policy** being optimized.
         * \(\pi\_{\text{ref}}(o\_{i,t} \mid q, o\_{i,<t})\) is the **probability under the frozen reference policy**, often the supervised fine-tuned (SFT) or pre-trained model.
         * The formula estimates an **unbiased per-token KL divergence**, ensuring positivity and stability while measuring how much \(\pi\_\theta\) diverges from \(\pi\_{\text{ref}}\).
         * The term \(-1\) ensures the estimator remains non-negative, preserving proper divergence properties.
     + A detailed discussion of this penalty term is included in the [KL Penalty: PPO vs. GRPO](#kl-penalty-ppo-vs-grpo) section.
  5. **Overall GRPO Loss Function**:

     + Combining the objective and KL regularization, the **final GRPO loss** (to be minimized) is given by:

       \[L\_{\text{GRPO}}(\theta) = -\mathbb{E}\_{q, {o\_i}\_{i=1}^G} \left[ \frac{1}{G} \sum\_{i=1}^G \frac{1}{|o\_i|} \sum\_{t=1}^{|o\_i|} \min\left(r\_{i,t}(\theta)\hat{A}\_{i,t},\,\text{clip}(r\_{i,t}(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A}\_{i,t}\right) - \beta D\_{\text{KL}}(\pi\_\theta \mid\mid \pi\_{\text{ref}}) \right]\]
       - where:

         * \(\beta\) is the **KL coefficient**, a hyperparameter that controls the strength of the regularization—higher values enforce stricter alignment with the reference model.
         * The **negative sign** indicates that training minimizes the loss (a negative of the objective), effectively maximizing the expected reward while constraining policy divergence.
         * The first summation term corresponds to the **group-relative PPO objective**, and the second term penalizes deviation from \(\pi\_{\text{ref}}\) to maintain policy stability and prevent over-optimization.

#### KL Penalty: PPO vs. GRPO

* To mitigate over-optimization of the reward model, the standard approach is to **add a per-token KL penalty from a reference model directly into the reward at each token** per the [PPO paper](https://arxiv.org/abs/2203.02155) by Ouyang et al. (2022), effectively discouraging the policy from drifting too far from the reference distribution during optimization.
* Following PPO, GRPO also employ KL regularization to control the divergence between the updated policy \(\pi\_\theta\) (the current trainable policy model) and a reference policy \(\pi\_{\text{ref}}\) (a fixed, frozen baseline model such as the supervised fine-tuned or pre-trained checkpoint).
* Both methods apply the KL penalty **at the per-token level**, meaning divergence is computed for each token’s conditional probability rather than for entire sequences. However, **PPO applies this penalty implicitly through modified rewards**, while **GRPO applies it explicitly as a separate term in the loss**.
* PPO therefore treats KL regularization as *reward shaping*—the model learns to avoid over-optimization naturally by losing reward when it deviates too far from the reference. GRPO, on the other hand, formalizes the same control as *explicit regularization* in the loss objective, providing finer control over optimization dynamics.
* Thus, while both enforce proximity between \(\pi\_\theta\) and \(\pi\_{\text{ref}}\), PPO applies the penalty **implicitly within rewards**, whereas GRPO applies it **explicitly through the loss**, leading to improved stability and interpretability in large-scale reasoning models.

##### PPO: Implicit Per-Token KL Penalty in the Reward Function

* In PPO, the KL penalty is integrated *directly into the reward function*, modifying the per-token reward at each time step:

  \[r\_t = r\_\varphi(q, o\_{\le t}) - \beta \log \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}{\pi\_{\text{ref}}(o\_t \mid q, o\_{<t})}\]
  + where:

    - \(r\_t\) is the adjusted per-token reward at time step \(t\).
    - \(r\_\varphi(q, o\_{\le t})\) is the raw reward predicted by the reward model for the partial output up to token \(t\).
    - \(\beta\) is the KL regularization coefficient controlling the strength of the penalty.
    - \(\pi\_\theta(o\_t \mid q, o\_{<t})\) is the probability assigned by the current policy to token \(o\_t\) given the prompt \(q\) and preceding tokens \(o\_{<t}\).
    - \(\pi\_{\text{ref}}(o\_t \mid q, o\_{<t})\) is the corresponding probability under the reference policy.
* The PPO optimization objective is:

  \[J\_{\text{PPO}}(\theta) = \mathbb{E}\left[\min\left(r\_t(\theta)\hat{A\_t},\,\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A\_t}\right)\right]\]
  + where:

    - \(J\_{\text{PPO}}(\theta)\) is the expected clipped objective to be maximized.
    - \(r\_t(\theta) = \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}{\pi\_{\text{old}}(o\_t \mid q, o\_{<t})}\) is the per-token probability ratio between the current and old policies.
    - \(\hat{A\_t}\) is the advantage function estimating how much better the chosen action performed relative to the baseline.
    - \(\epsilon\) is the clipping parameter that limits how much the ratio may deviate from 1.
* In PPO, the **KL penalty is applied implicitly** through the modified reward \(r\_t\). This embeds the regularization within the advantage computation, influencing gradients indirectly through the reward signal. Consequently, the KL term acts as a *soft reward adjustment* rather than a separate optimization term.

##### GRPO: Explicit Per-Token KL Penalty in the Loss Function

* In contrast, GRPO also computes KL divergence **per token**, but incorporates it **explicitly as a regularization term** in the loss function rather than inside the reward. Unlike PPO’s per-token KL penalty that is defined as the **log-ratio between the current and reference policy probabilities**, GRPO adopts an **unbiased estimator** of the KL divergence following [Approximating KL Divergence](http://joschu.net/blog/kl-approx.html) (Schulman, 2020), which guarantees positivity and numerical stability. The estimator defines the KL divergence term as:

  \[D\_{\text{KL}}[\pi\_\theta \mid\mid \pi\_{\text{ref}}] =
  \frac{\pi\_{\text{ref}}(o\_{i,t} \mid q, o\_{i,<t})}
  {\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})}
  - \log \frac{\pi\_{\text{ref}}(o\_{i,t} \mid q, o\_{i,<t})}
  {\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})} - 1\]
  + where:

    - \(D\_{\text{KL}}[\pi\_\theta \mid\mid \pi\_{\text{ref}}]\) is the unbiased estimator of the KL divergence between the current and reference policies.
    - \(\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})\) is the probability assigned by the current policy to the token \(o\_{i,t}\) given the prompt \(q\) and its preceding tokens.
    - \(\pi\_{\text{ref}}(o\_{i,t} \mid q, o\_{i,<t})\) is the corresponding token probability under the frozen reference policy.
    - The term \(-1\) ensures the estimator remains strictly non-negative, providing a stable and unbiased measure of divergence.
* This formulation differs from the PPO-style KL penalty used earlier (Equation (2) in the DeepSeek-Math paper), where the KL term was embedded in the reward. GRPO instead computes this **explicit estimator** and adds it as a separate loss component:

  \[L\_{\text{GRPO}}(\theta) =
  -\mathbb{E}\_{q, {o\_i}\_{i=1}^G}\left[
  \frac{1}{G} \sum\_{i=1}^G \frac{1}{|o\_i|}
  \sum\_{t=1}^{|o\_i|}
  \min\left(r\_{i,t}(\theta)\hat{A}\_{i,t},
  \,\text{clip}(r\_{i,t}(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A}\_{i,t}\right)
  - \beta D\_{\text{KL}}[\pi\_\theta \mid\mid \pi\_{\text{ref}}]
  \right]\]
  + where:

    - \(L\_{\text{GRPO}}(\theta)\) is the total loss to be minimized.
    - \(q\) is the input query or prompt.
    - \(o\_i\) is the \(i^{th}\) sampled output in a group of size \(G\).
    - \(\mid o\_i \mid\) is the token length of the output.
    - \(r\_{i,t}(\theta)\) is the ratio between the new and old policy probabilities for the token \(o\_{i,t}\).
    - \(\hat{A}\_{i,t}\) is the normalized advantage estimated from group-relative rewards.
    - \(\text{clip}(\cdot)\) bounds policy updates within \([1 - \epsilon, 1 + \epsilon]\).
    - \(\beta\) controls the KL regularization intensity.
    - \(D\_{\text{KL}}(\pi\_\theta \mid\mid \pi\_{\text{ref}})\) is computed per token and explicitly penalizes deviation from the reference policy.
* In GRPO, the KL penalty is **explicitly subtracted as a regularization term** in the loss, ensuring the learned policy \(\pi\_\theta\) does not deviate excessively from the reference policy \(\pi\_{\text{ref}}\), independent of the reward function or group-based advantage computation. This unbiased estimator—based on [Schulman (2020)](http://joschu.net/blog/kl-approx.html)—improves training stability compared to PPO’s reward-based penalty while maintaining theoretical guarantees of positivity and convergence.

#### Implementation Details

1. **Input Data**:
   * Questions (\(q\)) are sampled from a dataset.
   * Multiple outputs (\(G\)) are generated per question using the old policy.
2. **Reward Model**:
   * Rewards (\(r\_i\)) are computed using a pre-trained reward model.
   * Rewards are normalized within the group to calculate relative advantages.
3. **Optimization Steps**:
   * Sample outputs and compute rewards.
   * Compute group-relative advantages.
   * Update the policy model by maximizing the GRPO objective.
   * Apply KL regularization to prevent the policy from drifting too far from the reference model.
4. **Hyperparameters**:
   * \(\epsilon\): Clipping parameter (e.g., 0.2).
   * \(\beta\): KL regularization coefficient.
   * \(G\): Group size (e.g., 64 outputs per input).
   * Learning rate: Typically in the range of \(10^{-6}\) to \(10^{-5}\).

#### Pros and Cons

##### Pros

* **Efficiency**: GRPO reduces memory and computation requirements by eliminating the critic model.
* **Simplicity**: The advantage is computed directly from group scores without training an additional value model.
* **Alignment with Reward Models**: Leverages the comparative nature of reward functions effectively.
* **Improved Performance**: Demonstrated superior results on benchmarks like GSM8K and MATH compared to other RL methods.

##### Cons

* **Dependence on Group Size**: Requires careful tuning of the group size \(G\) for effective advantage estimation.
* **Reward Model Quality**: Relies heavily on the quality of the reward model for accurate advantage computation.
* **Applicability**: May not generalize well to tasks with sparse or noisy reward signals.

#### Applications and Results

* GRPO significantly enhances the mathematical reasoning capabilities of models like DeepSeekMath.
* On GSM8K and MATH datasets, GRPO achieved 88.2% and 51.7% accuracy, respectively, outperforming other open-source methods.

## GRPO Successors

* GRPO represented an important step toward simplifying RL for large language models by removing the need for a learned value (critic) network and instead relying on group-normalized rewards. However, practical experience across multiple large-scale reasoning systems has revealed several fundamental limitations that become increasingly severe as models scale and as chain-of-thought (CoT) reasoning grows longer:

  + **Instability in long-CoT reasoning** caused by symmetric PPO-style clipping at the token level, which tends to suppress rare but crucial reasoning-control tokens and can trigger entropy collapse.
  + **Inefficient data utilization** when sampling groups contain only fully-correct or fully-incorrect responses, leading to zero or near-zero learning signal.
  + **Coarse or misaligned credit assignment**, where rewards are sequence-level but importance correction and clipping operate at the token level, producing high-variance gradients.
  + **Poor long-context robustness**, especially when sequences are truncated or excessively long.
* A family of successor algorithms has emerged to systematically address these issues, each modifying a different aspect of GRPO’s design while retaining its core idea of critic-free, group-relative advantage estimation:

  + **Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO)**: [Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO)](https://arxiv.org/abs/2503.14476) introduces asymmetric clipping (“Clip-Higher”), dynamic sampling of informative groups, token-level loss normalization, and soft overlong reward shaping. Together, these changes directly target entropy collapse, uninformative batches, and coarse loss aggregation, yielding substantially improved stability and sample efficiency for long-CoT reasoning.
  + **GRPO+**: [GRPO+](https://pretty-radio-b75.notion.site/DeepCoder-A-Fully-Open-Source-14B-Coder-at-O3-mini-Level-1cf81902c14680b3bee5eb349a512a51) is a pragmatic refinement of GRPO used in DeepCoder that removes KL and entropy regularization, introduces a higher upper clipping bound, and applies overlong filtering. GRPO+ focuses on stabilizing long-context code RL and preventing late-stage reward collapse while preserving GRPO’s simplicity.
  + **Group Sequence Policy Optimization (GSPO)**: [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071) identifies a deeper theoretical flaw in GRPO’s token-level importance ratios and replaces them with sequence-level importance ratios and sequence-level clipping. GSPO aligns the unit of reward, importance correction, and clipping at the sequence level, dramatically improving stability, especially for very long responses and Mixture-of-Experts models.
  + **Clipped Importance Sampling Policy Optimization (CISPO)**: [MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention](https://arxiv.org/abs/2506.13585) proposes CISPO, which abandons PPO-style token clipping altogether and instead clips importance sampling weights in an off-policy REINFORCE-style objective. This ensures that no tokens are dropped from training, preserving gradients for rare reasoning behaviors and significantly improving efficiency and stability in long-CoT settings.
* Collectively, these successors illustrate a clear trajectory in the design of critic-free RL for language models:

  + From **symmetric token-level clipping** toward **asymmetric token-level clipping** (DAPO, GRPO+): DAPO replaces symmetric PPO clipping with asymmetric bounds by relaxing the upper clipping bound so that low-probability but useful reasoning-control tokens can receive large positive updates without being immediately suppressed.
  + From **token-update clipping** toward **importance-weight clipping** (CISPO): CISPO abandons PPO-style token clipping and stabilizes training by clipping importance sampling weights, ensuring that all tokens always contribute gradients.
  + From **suppressing rare reasoning tokens** toward **preserving their gradients** (DAPO, CISPO): DAPO’s relaxed upper clipping bound and CISPO’s weight clipping ensure that low-probability reflective tokens continue to receive gradient signal.
  + From **token-level importance correction** toward **sequence-consistent importance correction** (GSPO): GSPO moves importance ratios and clipping from individual tokens to entire responses, aligning off-policy correction with the sequence-level nature of rewards and eliminating high-variance per-token weighting.
  + From **coarse sequence aggregation** toward **token-aware or sequence-aligned objectives** (DAPO, CISPO, GSPO): DAPO and CISPO apply token-level loss normalization so long reasoning traces contribute proportionally, while GSPO enforces sequence-aligned optimization where reward, importance correction, and clipping operate at the same granularity.
  + From **brittle long-context training** toward **explicit overlong-sequence handling** (DAPO, GRPO+): DAPO introduces soft overlong reward shaping, and GRPO+ applies overlong filtering or masked loss, enabling robust long-context RL.
* This progression reflects a broader paradigm shift away from classical PPO-style token clipping toward more principled, long-context-friendly RL formulations tailored to the unique structure of LLM reasoning.

### Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO)

* [Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO)](https://arxiv.org/abs/2503.14476), proposed by ByteDance, Tsinghua University, The University of Hong Kong, and the SIA-Lab of Tsinghua AIR and ByteDance Seed, significantly advances RL for long-chain-of-thought (CoT) reasoning by building on the foundational ideas of GRPO. While GRPO simplifies RL training by eliminating the need for a value network through group-based reward normalization, DAPO introduces a suite of principled enhancements that greatly improve sample efficiency, training stability, and policy diversity—particularly in complex reasoning tasks.
* Developed and benchmarked with the Qwen2.5-32B model, DAPO not only matches but often surpasses state-of-the-art results achieved by models like DeepSeek-R1-Zero. This demonstrates the limitations of naive GRPO and highlights DAPO as a more refined and robust alternative. Key innovations in DAPO include mechanisms such as Clip-Higher for better gradient clipping, dynamic sampling for improved data efficiency, token-level loss modeling for finer-grained learning, and nuanced reward shaping. These features allow DAPO to achieve superior performance with fewer training steps, making it a compelling evolution in the RL paradigm for large-scale reasoning models. Importantly, DAPO remains reproducible and open-source, promoting transparency and further research in the field.

#### DAPO vs. GRPO: Key Differences

* At a high level, both GRPO and DAPO eliminate the critic model and use group-normalized advantages. However, DAPO introduces several critical refinements:

  1. **Clipping asymmetry** (Clip-Higher): Decouples the lower and upper clipping bounds to promote exploration.
  2. **Dynamic Sampling**: Filters out trivial cases where all generated responses are either fully correct or incorrect, preserving informative gradient updates.
  3. **Token-Level Loss**: Applies the policy gradient loss at the token level rather than averaging over the sequence.
  4. **Overlong Reward Shaping**: Mitigates instability from truncated long sequences via soft penalties instead of hard cutoffs.
* Each of these refinements addresses a specific deficiency in GRPO’s design when applied to long-CoT reasoning tasks.

#### DAPO: Implementation Details

##### Objective Function

* The DAPO objective is defined as:

\[J\_{\text{DAPO}}(\theta) =
\mathbb{E}\_{(q,a)\sim D,{o\_i}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(\cdot|q)}\left[
\frac{1}{\sum\_{i=1}^G |o\_i|}
\sum\_{i=1}^G \sum\_{t=1}^{|o\_i|}
\min\left(
r\_{i,t}(\theta)\hat{A}\_{i,t},\,\text{clip}(r\_{i,t}(\theta),1-\epsilon\_{\text{low}},1+\epsilon\_{\text{high}})\hat{A}\_{i,t}
\right)
\right]\]

* subject to the sampling constraint:

\[0 < |{o\_i \mid \text{is\_equivalent}(a,o\_i)}| < G\]

* **where:**

  + **\((q,a) \sim D\)**:
    - A question–answer pair sampled from the training dataset \(D\). Each question \(q\) has an associated correct answer \(a\), often drawn from the DAPO-Math-17K dataset.
  + **\({o\_i}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(\cdot \mid q)\)**:
    - A group of \(G\) responses \(o\_i\) generated by the *behavior policy* \(\pi\_{\theta\_{\text{old}}}\) conditioned on question \(q\). These are the model’s sampled outputs before policy update.
  + **\(\mid o\_i \mid\)**:
    - The number of tokens in the \(i^{th}\) generated output sequence \(o\_i\). The normalization by \(\sum\_i \mid o\_i \mid\) converts the objective to a token-level loss.
  + **\(r\_{i,t}(\theta)\)**:
    - The *importance sampling ratio* between the current policy and the old (behavior) policy for token \(t\) of sequence \(o\_i\):\[r\_{i,t}(\theta) =
    \frac{\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})}
    {\pi\_{\theta\_{\text{old}}}(o\_{i,t} \mid q, o\_{i,<t})}\]
    - This measures how much the current policy diverges from the old policy on each token’s decision.
  + **\(\hat{A}\_{i,t}\)**:
    - The *normalized group-relative advantage* of the \(i^{th}\) response at token \(t\):

      \[\hat{A}\_{i,t} =
      \frac{R\_i - \text{mean}({R\_j}\_{j=1}^G)}
      {\text{std}({R\_j}\_{j=1}^G)}\]
    - The reward \(R\_i\) for each response \(o\_i\) is standardized within its group, encouraging responses that outperform others in the same batch and stabilizing learning without a value function.
  + **\(R\_i\)**:
    - The *rule-based reward* assigned to the \(i^{th}\) response. Computed directly from task correctness rather than a learned reward model:\[R\_i =
    \begin{cases}
    1, & \text{if } \text{is\_equivalent}(o\_i, a) \\
    -1, & \text{otherwise}
    \end{cases}\]
    - This simple correctness-based signal avoids reward hacking.
  + **\(\pi\_\theta\)**:
    - The *current policy* being optimized, parameterized by \(\theta\). It defines the probability distribution over next tokens given the input and previous outputs.
  + **\(\pi\_{\theta\_{\text{old}}}\)**:
    - The *behavior policy* used to collect the training samples. It serves as a reference for importance weighting.
  + **\(\epsilon\_{\text{low}}, \epsilon\_{\text{high}}\)**:
    - The *asymmetric clipping thresholds* for the ratio \(r\_{i,t}(\theta)\).
      * The lower bound \(1-\epsilon\_{\text{low}}\) prevents excessively large policy updates when decreasing token probability.
      * The higher bound \(1+\epsilon\_{\text{high}}\) is set larger than typical PPO limits to allow exploration for low-probability tokens (the “Clip-Higher” strategy).
  + **\(\text{clip}(r\_{i,t}(\theta), 1-\epsilon\_{\text{low}}, 1+\epsilon\_{\text{high}})\)**:
    - Restricts the policy ratio within the asymmetric bounds to maintain training stability while allowing dynamic exploration.
  + **\(\min(\cdot)\) term**:
    - Implements PPO-style conservative updates by taking the minimum between the unclipped and clipped objectives, ensuring that updates do not increase policy divergence when the advantage estimate is large.
  + **Constraint**:
    \(0 < |{o\_i \mid \text{is\_equivalent}(a,o\_i)}| < G\)
    - … ensures *dynamic sampling*: each group of responses contains both correct and incorrect outputs, preventing zero-gradient cases where all responses are correct or incorrect.

##### Clip-Higher (Asymmetric Clipping)

* While GRPO adopts PPO-style clipping:

\[\text{clip}(r, 1 - \epsilon, 1 + \epsilon)\]

* DAPO decouples the upper and lower clipping thresholds:

\[\text{clip}(r, 1 - \epsilon\_{\text{low}}, 1 + \epsilon\_{\text{high}})\]

* This enables greater policy exploration, especially for low-probability tokens that would otherwise remain underrepresented. This adjustment empirically increases generation entropy without sacrificing correctness, stabilizing learning and avoiding entropy collapse. The following figure from the paper ([source](https://arxiv.org/abs/2503.14476)) shows the entropy of the actor model’s generated probabilities during the RL training process, both before and after applying Clip-Higher strategy.

##### Dynamic Sampling

* DAPO introduces a data-efficient sampling strategy. Since GRPO computes relative advantages within a group, if all generated responses are correct (or all incorrect), the standard deviation becomes zero, yielding zero gradients.
* To counteract this, DAPO enforces:

\[0 < \left| \{o\_i \mid \text{is\_equivalent}(o\_i, a) \} \right| < G\]

* This filters out groups that do not produce informative learning signals. The strategy ensures that every training batch contains prompts yielding useful gradients by resampling until this constraint is met.

##### Token-Level Policy Gradient Loss

* GRPO aggregates the loss by averaging across entire sequences, which leads to disproportionate weight on shorter samples. DAPO instead normalizes the loss over **tokens**, ensuring that longer responses contribute proportionally to the gradient:

\[\frac{1}{\sum\_{i=1}^G |o\_i|} \sum\_{i=1}^G \sum\_{t=1}^{|o\_i|}\]

* This fine-grained gradient computation:
  + Enhances learning from long, structured reasoning sequences
  + Mitigates the problem of low-quality long outputs dominating updates
  + Encourages refinement of reasoning at the token level rather than relying solely on outcome correctness

##### Overlong Reward Shaping

* To handle excessively long outputs (common in long-CoT tasks), DAPO introduces **Soft Overlong Punishment**. Rather than assigning a fixed penalty, it uses a length-sensitive shaping function:

\[R\_{\text{length}}(y) =
\begin{cases}
0 & \text{if } |y| \leq L\_{\text{max}} - L\_{\text{cache}} \\
\frac{(L\_{\text{max}} - L\_{\text{cache}}) - |y|}{L\_{\text{cache}}} & \text{if } L\_{\text{max}} - L\_{\text{cache}} < |y| \leq L\_{\text{max}} \\
-1 & \text{if } |y| > L\_{\text{max}}
\end{cases}\]

* This length-aware penalty encourages succinct, precise reasoning and reduces training noise from truncated sequences, as demonstrated by the entropy and accuracy trends in the source.

##### Training Implementation Summary

* **Base Model**: Qwen2.5-32B
* **Batch Size**: 512 prompts × 16 responses per prompt
* **Loss Reduction**: Token-level
* **Clipping**: Asymmetric with \(\epsilon\_{\text{low}} = 0.2\), \(\epsilon\_{\text{high}} = 0.28\)
* **Max Tokens**: 20,480 (with soft penalty starting at 16,384)
* **Reward Function**: Rule-based equivalence check (1 for correct, -1 otherwise)

#### DAPO vs. GRPO Summary

| **Feature** | **GRPO** | **DAPO** |
| --- | --- | --- |
| Clipping | Symmetric (\(\epsilon\)) | Asymmetric (\(\epsilon\_{\text{low}}, \epsilon\_{\text{high}}\)) |
| Sampling | Uniform (accept all groups) | Dynamic (filters degenerate groups) |
| Loss Aggregation | Sample-level | Token-level |
| Overlong Sample Handling | Truncation + hard penalty | Soft reward shaping |
| KL Regularization | Optional (often used) | Removed to allow divergence from SFT |
| Exploration Capacity | Lower (risk of entropy collapse) | Higher (maintains policy diversity) |
| Stability in Long-CoT Tasks | Moderate | High |

#### Empirical Gains

* As shown in [paper](https://arxiv.org/abs/2503.14476), each DAPO technique independently improves performance on AIME 2024. Cumulatively, DAPO achieves 50 points (avg@32), surpassing DeepSeek-R1-Zero-Qwen-32B (47 points), with only 50% of the training steps as shown in the plot from the paper.

| **Model Variant** | **AIME24 avg@32** |
| --- | --- |
| Naive GRPO | 30 |
| + Overlong Filtering | 36 |
| + Clip-Higher | 38 |
| + Soft Overlong Punishment | 41 |
| + Token-level Loss | 42 |
| + Dynamic Sampling (DAPO Final) | **50** |

### GRPO+: A Stable Evolution of GRPO for Reinforcement Learning in DeepCoder

* [GRPO+](https://pretty-radio-b75.notion.site/DeepCoder-A-Fully-Open-Source-14B-Coder-at-O3-mini-Level-1cf81902c14680b3bee5eb349a512a51) is an advanced variant of Group Relative Policy Optimization (GRPO), specifically designed to address the instability challenges commonly encountered during RL training of code reasoning models, especially in long-context fine-tuning scenarios. This refined approach builds upon the foundational structure of GRPO, while integrating innovations—many inspired by DAPO—to enhance training stability, reward fidelity, and response scalability.
* Developed for DeepCoder, a 14B open-source code reasoning model, GRPO+ introduces several key modifications that distinguish it from its predecessor. These include the removal of KL and entropy losses, the incorporation of asymmetric clipping, and the implementation of overlong filtering. Collectively, these changes create a lightweight yet robust training framework, enabling stable and efficient scaling of reasoning abilities across extended context windows.
* By tailoring these enhancements to the specific demands of large-scale RL in code-focused language models, GRPO+ delivers improved performance and reliability. It empowers open-source models like DeepCoder to push the boundaries of coding tasks, making it a compelling strategy for deploying frontier-level LLMs in open development environments.

#### Motivation for GRPO+

* During DeepCoder’s RL training on a curated set of 24,000 verifiable code problems, the research team observed that the vanilla GRPO algorithm exhibited a collapse in reward over time, especially during later stages of training. This was attributed to entropy divergence and unstable policy updates. To counter this, GRPO+ was introduced with the goal of preserving the sample efficiency of GRPO while enhancing its training stability for large-scale, long-context LLMs.
* The following figure ([source](https://pretty-radio-b75.notion.site/DeepCoder-A-Fully-Open-Source-14B-Coder-at-O3-mini-Level-1cf81902c14680b3bee5eb349a512a51)) illustrates this: the average reward for GRPO+ remains stable, while GRPO degrades and eventually collapses during training. The modifications introduced in GRPO+ are critical to sustaining performance throughout extended RL runs.

#### Key Innovations in GRPO+

* GRPO+ introduces the following core changes to the GRPO framework:

  1. **No Entropy Loss**:
     + In standard PPO/GRPO implementations, an entropy loss term is often included to promote exploration. However, in DeepCoder’s experiments, this entropy term caused the entropy of the output distribution to grow uncontrollably, destabilizing training. GRPO+ omits this term altogether:
     + **Rationale**: Removing entropy loss prevents exponential growth in token-level uncertainty, avoiding collapse in later iterations.
     + **Effect**: Encourages more stable convergence by reducing exploration-induced noise.
  2. **No KL Loss (No Trust Region Constraint)**:
     + While GRPO retains a KL divergence penalty against a reference policy to prevent policy drift, GRPO+ completely removes the \(- \beta D\_{\text{KL}}(\pi\_\theta \,\|\, \pi\_{\text{ref}})\) component from the loss.
     + **Rationale**: This follows insights from DAPO, which demonstrated that strict adherence to a trust region (as in PPO or GRPO) can overly constrain learning.
     + **Effect**: Training is accelerated since the computation of log probabilities from the reference model is skipped, reducing overhead.
  3. **Clip High in Surrogate Loss**:
     + GRPO+ modifies the upper bound in the surrogate loss function to encourage greater exploration:
       \(\min\left(\rho\_i A\_i,\,\text{clip}(\rho\_i, 1 - \epsilon, 1 + \epsilon\_{\text{high}}) A\_i \right)\)
       - where \(\epsilon\_{\text{high}} > \epsilon\) is a relaxed clipping range.
     + **Rationale**: Standard clipping suppresses beneficial large updates; raising the upper bound retains PPO-style stability while allowing positive exploration.
     + **Effect**: Boosts learning speed and prevents premature convergence.
  4. **Overlong Filtering**:
     + To allow generalization to longer context windows (up to 64K), GRPO+ introduces masked loss for truncated sequences. This overlong filtering ensures that models are not penalized for generating coherent but lengthy outputs beyond the current training context (e.g., 32K tokens):
       - **Implementation**: During training, loss is not backpropagated through the truncated parts of sequences.
       - **Effect**: Enables the model to reason over longer contexts during inference, with empirical gains on LiveCodeBench from 54% to 60.6% as context increases from 16K to 64K.

#### Objective Function: From GRPO to GRPO+

* The original **Group Relative Policy Optimization (GRPO)** objective combines a clipped policy gradient term with **KL regularization** and an **entropy bonus**, designed to stabilize reinforcement learning for large language models:

  \[J\_{\text{GRPO}}(\theta) =
  \mathbb{E}\_{q \sim P(Q), {o\_i}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(O|q)}
  \left[
  \frac{1}{G} \sum\_{i=1}^G
  \min\left(
  \rho\_i A\_i,
  \,\text{clip}(\rho\_i, 1-\epsilon, 1+\epsilon) A\_i
  \right)
  \right]
  - \beta\_{\text{KL}} D\_{\text{KL}}(\pi\_\theta | \pi\_{\text{ref}})
  - \beta\_H \mathcal{H}(\pi\_\theta)\]
* The **GRPO+** variant builds directly on GRPO and simplifies it by:

  1. **Removing** the KL divergence and entropy terms (to improve efficiency and avoid instability).
  2. **Introducing** an **asymmetric clipping range**, where the upper bound \(\epsilon\_{\text{high}}\) exceeds \(\epsilon\), increasing exploration stability.
* Thus, the **GRPO+** objective becomes:

  \[J\_{\text{GRPO+}}(\theta) =
  \mathbb{E}\_{q \sim P(Q), {o\_i}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(O|q)}
  \left[
  \frac{1}{G} \sum\_{i=1}^G
  \min\left(
  \rho\_i A\_i,
  \,\text{clip}(\rho\_i, 1-\epsilon, 1+\epsilon\_{\text{high}}) A\_i
  \right)
  \right]\]
  + This can be expressed concisely as:

    \[J\_{\text{GRPO+}}(\theta)
    =
    J\_{\text{GRPO}}(\theta)
    \Big|\_{\beta\_{\text{KL}} = 0, \beta\_H = 0, \epsilon\_{\text{high}} > \epsilon}\]
  + **where:**

    - **\(q \sim P(Q)\)**:
      * A query or input prompt sampled from the distribution of training tasks or datasets.
      * Each query defines the context under which model responses are generated.
    - **\({o\_i}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(O \mid q)\)**:
      * A group of \(G\) sampled outputs (model responses) drawn from the previous policy \(\pi\_{\theta\_{\text{old}}}\) conditioned on the query \(q\).
      * These outputs are used to compute group-level normalized rewards and advantages.
    - **\(\pi\_\theta(o\_i \mid q)\)**:
      * The current policy, parameterized by \(\theta\), assigning a probability to each output \(o\_i\) given input \(q\).
    - **\(\pi\_{\theta\_{\text{old}}}(o\_i \mid q)\)**:
      * The behavior (old) policy that generated the training samples in the previous iteration.
    - **\(\rho\_i = \frac{\pi\_\theta(o\_i \mid q)}{\pi\_{\theta\_{\text{old}}}(o\_i \mid q)}\)**:
      * The **importance sampling ratio**, which measures how much the new policy’s probability of output \(o\_i\) differs from that under the old policy.
      * It reweights advantages to reflect the policy update.
    - **\(A\_i = \frac{r\_i - \bar{r}}{\sigma\_r}\)**:
      * The **group-normalized advantage**, introduced in GRPO:
        + \(r\_i\): reward assigned to output \(o\_i\) (e.g., test success).
        + \(\bar{r}\): mean reward of the group.
        + \(\sigma\_r\): standard deviation of group rewards.
      * This normalization stabilizes gradients and ensures balanced updates across group samples.
    - **\(\text{clip}(\rho\_i, 1-\epsilon, 1+\epsilon\_{\text{high}})\)**:
      * A **clipping function** that limits \(\rho\_i\) to prevent excessively large policy updates.
      * The upper bound \(\epsilon\_{\text{high}}\) (> \(\epsilon\)) extends the permissible range, allowing more exploration.
    - **\(\epsilon\) and \(\epsilon\_{\text{high}}\)**:
      * The lower and extended upper clipping parameters.
      * Typical values might be \(\epsilon = 0.2\) and \(\epsilon\_{\text{high}} = 0.4\).
    - **\(D\_{\text{KL}}(\pi\_\theta \mid \pi\_{\text{ref}})\)**:
      * The Kullback–Leibler divergence between the current policy \(\pi\_\theta\) and a fixed reference policy \(\pi\_{\text{ref}}\) (usually the supervised fine-tuned model).
      * This penalizes policy drift. **Removed in GRPO+.**
    - **\(\mathcal{H}(\pi\_\theta)\)**:
      * The entropy of the policy, encouraging exploration by preventing determinism.
      * Also **removed in GRPO+** to prevent instability from entropy blow-up.
    - **\(\beta\_{\text{KL}}\) and \(\beta\_H\)**:
      * Coefficients scaling the KL and entropy terms, respectively.
      * Both are set to zero in GRPO+.
    - **\(\mathbb{E}\_{q, {o\_i}}[\cdot]\)**:
      * Expectation over the joint sampling process of queries and outputs, estimated by averaging across mini-batches during training.

##### Final GRPO+ Objective

\[J\_{\text{GRPO+}}(\theta) =
\mathbb{E}\_{q \sim P(Q), {o\_i}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(O|q)}
\left[
\frac{1}{G} \sum\_{i=1}^G
\min\left(
\rho\_i A\_i,
\,\text{clip}(\rho\_i, 1-\epsilon, 1+\epsilon\_{\text{high}}) A\_i
\right)
\right]\]

#### Implementation Details

* **Training Loop:**
  1. Sample a group of responses (\(G = 8\) typically) using \(\pi\_{\theta\_{\text{old}}}\).
  2. Score each response using a sparse **Outcome Reward Model (ORM)**:
     + A binary reward is assigned:
       - 1 if all unit tests pass
       - 0 if any test fails or the output is improperly formatted
  3. Compute the group-based normalized advantage:
     \(A\_i = \frac{r\_i - \bar{r}}{\sigma\_r}\)
  4. Apply clipped surrogate loss with relaxed upper bound.
  5. Mask out loss contributions for truncated sequences to support long-context generalization.
  6. Update the policy \(\pi\_\theta\) using standard gradient ascent.
* **No Entropy or KL Terms:**
  + Losses are purely policy-gradient based.
  + No reference model is involved during optimization.
  + No explicit entropy bonus is used, encouraging organic exploration through gradient updates and the “Clip High” mechanism.
* **Context Scaling:**
  + Training begins at 16K context length.
  + At step 180, the model is extended to 32K with overlong filtering enabled.
  + At inference, DeepCoder generalizes successfully to 64K contexts, achieving peak performance.

#### Comparison: GRPO vs. GRPO+

| **Feature** | **GRPO** | **GRPO+** |
| --- | --- | --- |
| Critic Model | No | No |
| KL Regularization | Yes | No |
| Entropy Loss | Yes | No |
| Clipping | Symmetric \((1 \pm \varepsilon)\) | Asymmetric \((1 - \varepsilon,\ 1 + \varepsilon\_{\text{high}})\) |
| Advantage | Group-based Normalized | Group-based Normalized |
| Long-Context Generalization | Partial | Fully Supported (via overlong filtering) |
| Reward Function | Can use dense or sparse | Sparse binary (Outcome Reward Model) |
| Use Case | General reasoning, math RL | Long-context code RL |
| Stability | Moderate | High (no collapse over time) |

#### Why GRPO+ Works

* By simplifying the objective function, GRPO+ reduces the overhead of computing KL and entropy terms while still retaining PPO-like stability through clipping.
* It tailors the training process to sparse reward signals (pass/fail from test cases) and long-form outputs (code solutions), where traditional entropy bonuses or KL constraints may be detrimental.
* GRPO+’s stripped-down yet strategically enhanced formulation reflects a pragmatic design choice: retain what works, discard what destabilizes, and adapt the core RL ideas to the idiosyncrasies of code reasoning.

#### Results and Performance Impact

* GRPO+ was critical to DeepCoder’s performance. The reward curve of GRPO+ (cf. figure above) maintains a stable upward trajectory, in contrast to GRPO, whose training reward collapses beyond a certain point. Empirically, GRPO+ enables DeepCoder to:
  + Achieve 60.6% Pass@1 on LiveCodeBench
  + Match O3-mini and O1 on coding benchmarks
  + Generalize to 64K context with no retraining
* These improvements would not have been possible under GRPO alone, which suffered from convergence and entropy-related collapse in earlier experiments.

### Group Sequence Policy Optimization (GSPO)

* Group Sequence Policy Optimization (GSPO) is introduced in [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071) by Zheng et al. (2025). GSPO is designed as a stable, efficient, and scalable reinforcement learning algorithm for large language models, addressing fundamental instability issues observed in token-level policy optimization methods such as GRPO.
* The following figure ([source](https://arxiv.org/abs/2507.18071)) shows the training curves of a cold-start model fine-tuned from Qwen3-30B-A3B-Base, demonstrating GSPO’s higher training efficiency compared to GRPO.

#### Motivation: Why Move from Token-Level to Sequence-Level Optimization?

* GSPO arises from a critical diagnosis of instability in token-level algorithms like PPO and GRPO.
* In GRPO, the importance ratio is defined per token:

  \[w\_{i,t}(\theta)
  =\frac{
  \pi\_\theta(y\_{i,t} \mid x, y\_{i,<t})
  }{
  \pi\_{\theta\_{\text{old}}}(y\_{i,t} \mid x, y\_{i,<t})
  }\]
* This token-level importance weighting attempts to correct off-policy updates. However, as argued in [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071) by Zheng et al. (2025):

  + The reward is granted at the sequence level.
  + Importance sampling is theoretically valid when averaging over many samples.
  + GRPO applies importance weights to a single sampled token per timestep.
  + Variance accumulates across long sequences.
  + Clipping amplifies noise and can lead to catastrophic collapse.
* The core mismatch is: unit of reward ≠ unit of importance correction.
* GSPO enforces alignment by moving both importance weighting and clipping to the sequence level.

#### GSPO Objective

* Given:

  + Query dataset: \(D\)
  + Group of response: \({y\_i}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(\cdot \mid x)\)
  + Reward function: \(r(x, y\_i)\)

##### Group-Based Advantage

* GSPO adopts GRPO-style group normalization:

\[\hat{A}\_i
=\frac{
r(x, y\_i) - \text{mean}\left({r(x, y\_j)}\_{j=1}^G\right)
}{
\text{std}\left({r(x, y\_j)}\_{j=1}^G\right)
}\]

* All tokens in a response share the same advantage.

##### Sequence-Level Importance Ratio

* Instead of token-level ratios, GSPO defines:

\[s\_i(\theta)
=\left(
\frac{
\pi\_\theta(y\_i \mid x)
}{
\pi\_{\theta\_{\text{old}}}(y\_i \mid x)
}
\right)^{\frac{1}{|y\_i|}}\]

* Expanding:

\[s\_i(\theta)
=\exp\left(
\frac{1}{|y\_i|}
\sum\_{t=1}^{|y\_i|}
\log
\frac{
\pi\_\theta(y\_{i,t} \mid x, y\_{i,<t})
}{
\pi\_{\theta\_{\text{old}}}(y\_{i,t} \mid x, y\_{i,<t})
}
\right)\]

* The \(\frac{1}{\| y\_i \|}\) normalization:

  + Reduces variance
  + Controls magnitude
  + Prevents extreme scaling on long outputs
* This definition aligns with importance sampling theory (see [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071) by Zheng et al. (2025)).

##### GSPO Clipped Objective

* The full GSPO objective is:

\[J\_{\text{GSPO}}(\theta)
=\mathbb{E}\_{x \sim D,{y\_i} \sim \pi\_{\theta\_{\text{old}}}}
\left[
\frac{1}{G}
\sum\_{i=1}^G
\min
\left(
s\_i(\theta)\hat{A}\_i,
\text{clip}(s\_i(\theta), 1-\epsilon, 1+\epsilon)\hat{A}\_i
\right)
\right]\]

* Key distinctions from GRPO:

  + Clipping is applied per sequence.
  + Either an entire response is used or discarded.
  + No token-level masking.
* This removes the high-variance token weighting that accumulates across long chains of thought.

#### Gradient Analysis

* Without clipping, the GSPO gradient becomes:

\[\nabla\_\theta J\_{\text{GSPO}}
=\mathbb{E}
\left[
\frac{1}{G}
\sum\_{i=1}^G
s\_i(\theta)\hat{A}\_i
\cdot
\frac{1}{|y\_i|}
\sum\_{t=1}^{|y\_i|}
\nabla\_\theta
\log
\pi\_\theta(y\_{i,t} \mid x, y\_{i,<t})
\right]\]

* Crucially:

  + All tokens in a sequence are weighted equally.
  + Instability from per-token importance scaling is eliminated.
  + Gradient contributions are structurally consistent.
* In contrast, GRPO weights each token by ( w\_{i,t}(\theta) ), which varies per position and introduces compounding noise.

#### GSPO-token Variant

* GSPO also proposes a token-level variant, GSPO-token:

  \[J\_{\text{GSPO-token}}(\theta)
  =\mathbb{E}
  \left[
  \frac{1}{G}
  \sum\_{i=1}^G
  \frac{1}{|y\_i|}
  \sum\_{t=1}^{|y\_i|}
  \min
  \left(
  s\_{i,t}(\theta)\hat{A}\_{i,t},
  \text{clip}(s\_{i,t}(\theta),1-\epsilon,1+\epsilon)\hat{A}\_{i,t}
  \right)
  \right]\]
  + where:

    \[s\_{i,t}(\theta)
    =\text{sg}[s\_i(\theta)]
    \cdot
    \frac{
    \pi\_\theta(y\_{i,t} \mid x, y\_{i,<t})
    }{
    \text{sg}[\pi\_\theta(y\_{i,t} \mid x, y\_{i,<t})]
    }\]
* This preserves:

  + Sequence-level importance scaling
  + Token-level flexibility for multi-turn RL
* When \(\hat{A}\_{i,t} = \hat{A}\_i\), GSPO-token reduces exactly to GSPO.

#### Stability Benefits for MoE Training

* GSPO demonstrates strong stability for Mixture-of-Experts (MoE) RL training.
* In GRPO:

  + Expert routing can change after updates.
  + Token-level importance ratios fluctuate heavily.
  + Routing Replay is required to stabilize training.
* GSPO eliminates this need:

  + Sequence-level ratios are less sensitive to routing shifts.
  + No Routing Replay is required.
  + Infrastructure complexity is reduced.
* This improvement is highlighted in [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071) by Zheng et al. (2025), where GSPO was critical for scaling Qwen3 RL.

#### Empirical Observations

* Key findings:

  1. GSPO achieves higher reward growth per training compute.
  2. GSPO maintains stable convergence across long RL runs.
  3. GSPO clips more aggressively yet trains more efficiently.
  4. It removes catastrophic collapse observed in GRPO.
* An especially interesting result is that GSPO clips orders of magnitude more tokens than GRPO, yet achieves better learning efficiency. This suggests GRPO’s token-level gradients are inherently noisy.

#### Comparison: GSPO vs. GRPO

* GSPO represents a principled shift from token-level importance correction to sequence-consistent optimization. It directly addresses variance accumulation and instability in long-chain-of-thought RL, making it especially suited for scaling test-time compute and large MoE reasoning models. A tabular comparison is below:

| **Feature** | **GRPO** | **GSPO** |
| --- | --- | --- |
| Clipping Unit | Token-level | Sequence-level |
| Importance Ratio Definition | Token-level \(w\_{i,t}\) | Sequence-level \(s\_i\) |
| Reward–Optimization Alignment | Mismatch (sequence reward, token correction) | Aligned (sequence reward, sequence correction) |
| MoE Training Stability | Requires Routing Replay | Inherently stable (no routing replay) |
| Infrastructure Complexity | Higher | Lower / Simpler |

### Clipped Importance Sampling Policy Optimization (CISPO)

* Clipped Importance Sampling Policy Optimization (CISPO), introduced in [MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention](https://arxiv.org/abs/2506.13585) by Chen et al. (2025), is an RL algorithm designed to significantly improve training stability and efficiency for long-chain-of-thought (CoT) reasoning models by **clipping importance sampling weights instead of clipping token updates**, directly addressing a core weakness of PPO/GRPO-style surrogate objectives.
* The following figure ([source](https://arxiv.org/abs/2506.13585)) shows a comparison of GRPO, DAPO, and CISPO on AIME 2024 based on Qwen2.5-32B-base, demonstrating CISPO’s superior training efficiency and its ability to reach DAPO-level performance using roughly half the training steps.

#### Motivation: Why Token Clipping Fails in Long-CoT RL

* Standard PPO and GRPO use token-level importance ratios:

  \[r\_{i,t}(\theta)
  =\frac{\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})}
  {\pi\_{\theta\_{\text{old}}}(o\_{i,t} \mid q, o\_{i,<t})}\]
  + and optimize the clipped surrogate:\[\min\left(
  r\_{i,t}(\theta)\hat{A}\_{i,t},
  \text{clip}(r\_{i,t}(\theta), 1-\epsilon, 1+\epsilon)\hat{A}\_{i,t}
  \right)\]
* [Chen et al. (2025)](https://arxiv.org/abs/2506.13585) identify a critical pathology:

  + Rare reasoning-control tokens (e.g., *however*, *recheck*, *wait*, *aha*) initially have very low probability.
  + After one update, these tokens often exhibit extremely large ratios \(r\_{i,t}\).
  + PPO/GRPO clipping removes their gradients.
  + Subsequent off-policy updates cannot reinforce these behaviors.
* This effect:

  + Prevents emergence of reflective reasoning
  + Destabilizes entropy
  + Becomes severe when multiple off-policy updates per rollout batch are used
* Although DAPO increases the upper clipping bound ([Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO)](https://arxiv.org/abs/2503.14476) by Yu et al. (2025)), [Chen et al. (2025)](https://arxiv.org/abs/2506.13585) show that this is insufficient for large-scale hybrid-attention RL.

#### Core Idea of CISPO

* CISPO changes **what is clipped**:

  + PPO / GRPO: clip the *token update*
  + CISPO: clip the *importance sampling weight*
* Consequences:

  + No token is ever discarded
  + All tokens always contribute gradients
  + Stability is achieved by bounding correction magnitude
* CISPO can be viewed as an off-policy REINFORCE objective with **clipped IS weights**.

#### Off-Policy REINFORCE with Importance Correction

* Vanilla off-policy REINFORCE:

  \[J\_{\text{REINFORCE}}(\theta)
  =\mathbb{E}\_{(q,a)\sim D, o\_i\sim \pi\_{\theta\_{\text{old}}}}
  \left[
  \frac{1}{|o\_i|}
  \sum\_{t=1}^{|o\_i|}
  \text{sg}(r\_{i,t}(\theta))\hat{A}\_{i,t}
  \log \pi\_\theta(o\_{i,t}\mid q,o\_{i,<t})
  \right]\]
  + where:

    - \(\text{sg}(\cdot)\) is stop-gradient
    - \(r\_{i,t}(\theta)\) is the IS ratio
    - \(\hat{A}\_{i,t}\) is the advantage
* Without stabilization, variance is high.

#### CISPO Objective

##### Clipped Importance Sampling Weight

\[\hat{r}\_{i,t}(\theta)
=\text{clip}
\left(
r\_{i,t}(\theta),
1-\epsilon^{\text{IS}}\_{\text{low}},
1+\epsilon^{\text{IS}}\_{\text{high}}
\right)\]

* In practice:

  + \(\epsilon^{\text{IS}}\_{\text{low}}\) is set very large (effectively no lower bound)
  + Only \(\epsilon^{\text{IS}}\_{\text{high}}\) is tuned

##### CISPO Loss

* CISPO adopts:

  + GRPO-style group-relative advantage
  + Token-level loss
  + Clipped IS weights

\[J\_{\text{CISPO}}(\theta)
=\mathbb{E}\_{(q,a)\sim D,{o\_i}\_{i=1}^G\sim \pi\_{\theta\_{\text{old}}}}
\left[
\frac{1}{\sum\_{i=1}^G |o\_i|}
\sum\_{i=1}^G
\sum\_{t=1}^{|o\_i|}
\text{sg}(\hat{r}\_{i,t}(\theta))
\hat{A}\_{i,t}
\log \pi\_\theta(o\_{i,t}\mid q,o\_{i,<t})
\right]\]

##### Group Relative Advantage

\[\hat{A}\_{i,t} = \hat{A}\_i =
\frac{R\_i - \text{mean}({R\_j}\_{j=1}^G)}
{\text{std}({R\_j}\_{j=1}^G)}\]

* with rule-based reward:

\[R\_i =
\begin{cases}
1, & \text{if correct} \\
-1, & \text{otherwise}
\end{cases}\]

#### Why CISPO Is More Stable

* All tokens always contribute gradients
* Rare reasoning tokens are never clipped away
* Variance is bounded by IS-weight clipping
* Entropy remains within a healthy range
* Works reliably with many off-policy updates
* Chen et al. report that CISPO consistently prevents reward collapse and entropy degeneration.

#### Unified Perspective

* [Chen et al. (2025)](https://arxiv.org/abs/2506.13585) present a general masked objective:

  \[J\_{\text{unify}}(\theta)
  =\mathbb{E}
  \left[
  \frac{1}{\sum\_i |o\_i|}
  \sum\_{i,t}
  \text{sg}(\hat{r}\_{i,t})
  \hat{A}\_{i,t}
  \log \pi\_\theta(o\_{i,t})
  M\_{i,t}
  \right]\]
  + **PPO:** hard mask
  + **GRPO:** hard mask + token clipping
  + **CISPO:** soft weight clipping
  + **GSPO:** sequence-level clipping

#### Empirical Results

* CISPO > GRPO and DAPO at equal steps
* CISPO matches DAPO using ~50% steps
* ~2× speedup over DAPO
* Enables full RL of MiniMax-M1 in 3 weeks on 512 H800 GPUs

#### Comparison: GRPO vs. DAPO vs. CISPO

* The evolution from GRPO to DAPO to CISPO reflects a systematic effort to address instability and inefficiency in long-chain-of-thought reinforcement learning.
* CISPO demonstrates that stability comes from bounding correction magnitude, not discarding gradients. It complements GSPO:

  + GSPO fixes where importance correction is applied, moving from token-level to sequence-level ratios.
  + CISPO fixes how importance correction is stabilized, clipping importance weights rather than clipping token updates.
* Both point toward a broader paradigm shift away from PPO-style token clipping for long-chain-of-thought reinforcement learning.
* To understand this progression clearly, we compare the three algorithms across their core design axes.

| **Feature** | **GRPO** | **DAPO** | **CISPO** |
| --- | --- | --- | --- |
| Critic Model | No | No | No |
| Clipping Target | Token update | Token update (asymmetric) | Importance-sampling weight |
| Token Dropping | Yes | Sometimes | No |
| Importance Ratio Unit | Token-level | Token-level | Token-level (clipped, not masked) |
| Loss Granularity | Token-level | Token-level | Token-level |
| Entropy Stability | Poor | Improved | Strong |
| Compute Efficiency | Low | Medium | High |
| Long-CoT Stability | Moderate | High | Very High |

## Comparative Analysis: REINFORCE vs. TRPO vs. PPO vs. DPO vs. KTO vs. APO vs. GRPO

* **REINFORCE**:
  + **Function**: The simplest policy gradient algorithm that updates the model based on the cumulative reward received from complete trajectories.
  + **Implementation**: Generates an entire episode, calculates rewards at the end, and updates the policy network based on a weighted log probability loss.
  + **Practical Challenges**: High variance in policy updates, slow convergence, and instability due to unbounded updates.
* **TRPO**:
  + **Function**: Trust Region Policy Optimization (TRPO) improves policy updates by constraining step sizes to avoid instability.
  + **Implementation**: Uses a constrained optimization formulation to ensure each update remains within a trust region, preventing excessive deviations.
  + **Practical Challenges**: Computationally expensive due to the constraint-solving step and requires second-order optimization techniques.
* **PPO**:
  + **Function**: An RL algorithm that optimizes the language model by limiting how far it can drift from a previous version of the model.
  + **Implementation**: Involves sampling generations from the current model, judging them with a reward model, and using this feedback for updates.
  + **Practical Challenges**: Can be slow and unstable, especially in distributed settings.
* **DPO**:
  + **Function**: Minimizes the negative log-likelihood of observed human preferences to align the language model with human feedback.
  + **Data Requirement**: Requires paired preference data.
  + **Comparison with KTO**: While DPO has been effective, KTO offers competitive or superior performance without the need for paired preferences.
* **KTO**:
  + **Function**: Adapts the Kahneman-Tversky human value function to the language model setting. It uses this adapted function to directly maximize the utility of model outputs.
  + **Data Requirement**: Does not need paired preference data, only knowledge of whether an output is desirable or undesirable for a given input.
  + **Practicality**: Easier to deploy in real-world scenarios where desirable/undesirable outcome data is more abundant.
  + **Model Comparison**: Matches or exceeds the performance of direct preference optimization methods across various model sizes (from 1B to 30B).
* **APO**:
  + **Function**: Introduces a family of contrastive objectives explicitly accounting for the relationship between the model and the preference dataset. This includes APO-zero, which increases desirable outputs while decreasing undesirable ones, and APO-down, which fine-tunes models based on specific quality thresholds.
  + **Data Requirement**: Works effectively with paired preference datasets created through controlled methods like CLAIR and supports stable alignment even for challenging datasets.
  + **Practicality**: Excels at aligning strong models with minimally contrasting preferences, enhancing performance on challenging metrics like MixEval-Hard while providing stable, interpretable training dynamics.
  + **Model Comparison**: Outperformed conventional alignment objectives across multiple benchmarks, closing a 45% performance gap with GPT4-turbo when trained with CLAIR preferences.
* **GRPO**:
  + **Function**: A variant of PPO that removes the need for a critic model by estimating the baseline using group scores, improving memory and computational efficiency while enhancing the mathematical reasoning of models.
  + **Data Requirement**: Utilizes group-based rewards computed from multiple outputs for each query, normalizing these scores to guide optimization.
  + **Practicality**: Focuses on reducing training resource consumption compared to PPO and improving RL stability.
  + **Model Comparison**: Demonstrated superior performance on tasks like GSM8K and MATH benchmarks, outperforming other models of similar scale while improving both in-domain and out-of-domain reasoning tasks.

#### Tabular Comparison

| **Aspect** | **REINFORCE** | **TRPO** | **PPO** | **DPO** | **KTO** | **APO** | **GRPO** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Objective | Policy gradient optimization without constraints. | Ensures stable policy updates within a constrained region. | Maximizes expected reward while preventing large policy updates. | Optimizes policy based on binary classification of human preferences. | Aligns models based on Kahneman-Tversky optimization for utility maximization. | Anchored alignment with specific control over preference-based likelihood adjustments. | Leverages group-based relative advantages and removes the critic network. |
| Learning Mechanism | Monte Carlo policy gradients with high variance. | Second-order optimization with trust region constraints. | Policy gradients with a clipped surrogate objective. | Cross-entropy optimization over paired preferences. | Maximizes desirable likelihoods relative to undesirables, without paired data. | Uses variants like APO-zero or APO-down for stable preference-based optimization. | Group normalization with policy gradients, eliminating the critic network. |
| Stability | Low (high variance, unstable updates). | High (enforces trust region for stable updates). | Relies on clipping mechanisms to avoid destabilization. | Stable as it directly optimizes preferences. | Stable due to focus on unpaired desirability adjustments. | Offers robust training stability, scaling better on models trained with mixed-quality datasets. | Stable due to normalization of rewards across groups. |
| Training Complexity | High (unconstrained updates). | Very high (requires second-order optimization and solving constraints). | High, due to balancing reward maximization with policy constraints. | Moderate; uses simplified binary preference objectives. | Simplifies alignment by focusing only on desirability. | Adaptive and context-aware; requires understanding dataset-model relationships. | Reduces overhead via group-based scoring. |
| Performance | Unstable and sample-inefficient. | More stable than PPO but computationally expensive. | Strong performance on tasks with clear reward signals but prone to instability in distributed setups. | Effective for straightforward preference alignment tasks. | Competitive or better alignment than preference-based methods without paired data needs. | Superior alignment results, particularly for nuanced dataset control. | Excels in reasoning tasks, offering computational efficiency. |
| Notable Strength | Simple to implement but inefficient. | Ensures stable policy updates through trust-region constraints. | Widely used in RL settings, good at reward-based optimization. | Directly optimizes for preferences without needing a separate reward model. | Handles binary data efficiently, avoiding paired data dependencies. | Allows precise alignment with nuanced datasets. | Simplifies reward aggregation; strong for reasoning-heavy tasks. |
| Scenarios Best Suited | RL tasks where simplicity is preferred over efficiency. | High-stability RL tasks requiring constraint-driven policy improvements. | RL environments where reward signals are predefined. | Scenarios with abundant paired human feedback. | Real-world settings with broad definitions of desirable/undesirable outputs. | Tasks requiring precise alignment with minimally contrasting preferences. | Mathematical reasoning or low-resource training setups. |

#### Comparative Performance: DPO vs. PPO

* [Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study](https://arxiv.org/abs/2404.10719) by Xu et al. (2025) presents a large-scale empirical study comparing **Direct Preference Optimization (DPO)** and **Proximal Policy Optimization (PPO)** across diverse large language model alignment tasks, including dialogue helpfulness, summarization, and reasoning. The authors benchmark DPO and PPO on multiple model architectures and preference datasets to systematically investigate claims that DPO, a simpler and reward-free method, can replace PPO for aligning LLMs.

#### Experimental Setup

* Both algorithms are evaluated under controlled experimental conditions using identical base models, datasets, and training budgets. The PPO implementation follows the canonical setup from [Schulman et al. (2017)](https://arxiv.org/abs/1707.06347), incorporating [Generalized Advantage Estimation (GAE)](#generalized-advantage-estimation-gae) for variance reduction and a learned value critic. DPO follows the original formulation by [Rafailov et al. (2023)](https://arxiv.org/abs/2305.18290), trained on the same preference pairs without any reward model.
* The study further includes ablation tests on regularization strength, KL penalties, and reference model choices, providing a fair cross-method comparison.

#### Key Findings

##### Performance on Alignment and Reward Metrics

* Across nearly all benchmarks, PPO-trained models outperform DPO-trained ones on both *human preference alignment* and *reward model scores*.
  While DPO achieves comparable performance for smaller-scale models (≤7B parameters), PPO exhibits **superior performance for larger models**, especially in settings involving multi-turn dialogue and complex reasoning.
* Quantitatively:

  + PPO yields higher reward scores (by 5–15%) when trained with an equivalent number of updates.
  + PPO-trained models generalize better to unseen prompts, suggesting more stable policy optimization.
  + DPO sometimes overfits to the preference dataset, exhibiting degraded out-of-domain behavior.
* These results indicate that while DPO is computationally simpler, **PPO remains more robust and effective for large-scale LLM alignment**, particularly when the reward signal (or its learned approximation) is reliable.

##### Stability and Training Dynamics

* DPO’s supervised nature offers deterministic, low-variance optimization, but this stability can be misleading. PPO’s stochastic policy optimization introduces variance but allows adaptive balancing between exploration and exploitation via its clipped objective.
* The study highlights that:

  + PPO maintains better gradient signal quality due to explicit advantage estimation.
  + DPO’s gradients saturate quickly because of the sigmoid in its binary cross-entropy formulation, leading to slower convergence in high-dimensional action spaces.
  + PPO’s KL-based clipping provides smoother convergence and mitigates catastrophic policy drift, while DPO occasionally collapses toward the reference policy if \(\beta\) is large or diverges when \(\beta\) is too small.

##### Sample Efficiency and Computational Cost

* One of DPO’s major advantages is its simplicity:
* **DPO eliminates the need for rollouts or reward modeling**, resulting in **40–60% lower computational cost** than PPO.
* PPO, by contrast, requires multiple rollouts, critic training, and advantage computation per update step, increasing runtime significantly.
* However, PPO’s higher sample efficiency offsets its cost in many cases. DPO’s performance plateaued early in training, whereas PPO continued improving with more samples, achieving higher asymptotic returns.

##### Scaling Trends and Model Size Effects

* As model size increases, PPO’s advantage becomes more pronounced.
* The authors observe a *positive scaling trend* for PPO with model capacity, while DPO’s performance saturates or declines. This finding aligns with observations from [Touvron et al. (2023)](https://arxiv.org/abs/2307.09288) on the scaling behavior of LLM optimization methods.
* Specifically:

  + For \(1\text{B} \leq \text{params} \leq 3\text{B}\): DPO \(\approx\) PPO
  + For \(7\text{B} \leq \text{params} \leq 13\text{B}\): PPO > DPO by approximately \(8\text{–}10%\) reward margin
  + For \(\text{params} \geq 30\text{B}\): PPO significantly outperforms DPO, both on automatic and human-evaluated metrics

##### Robustness to Preference Noise

* When preference datasets contain inconsistent or noisy labels, DPO degrades more severely than PPO. PPO’s reward modeling can learn to smooth out noise by averaging over sampled rollouts, whereas DPO lacks an implicit noise-handling mechanism.
* Regularization (e.g., higher \(\beta\) or stronger KL penalties) mitigates this partially, but not completely. PPO’s value-based critic contributes additional robustness by learning a denoised reward landscape.

##### Practical Implications

* The study concludes that **DPO should not be viewed as a drop-in replacement for PPO**, particularly in high-stakes alignment settings. Instead, the two approaches occupy complementary roles:

| **Scenario** | **Recommended Algorithm** | **Rationale** |
| --- | --- | --- |
| Small/medium models (<7B) with clean preference data | DPO | Simpler, efficient, stable |
| Large-scale alignment (>13B) or noisy human feedback | PPO | More robust, scalable, better generalization |
| Synthetic or AI-generated feedback (RLAIF) | DPO | Avoids reward model training, computationally efficient |
| Fine-tuning with dense reward signals | PPO | Better advantage estimation and reward propagation |

#### Analytical Perspective

* From a theoretical standpoint, PPO’s advantage arises from its **actor-critic design** and **explicit control over policy divergence**, allowing better credit assignment across trajectories. DPO’s gradient direction aligns locally with preference log-ratios but lacks trajectory-level information, making it less effective when feedback depends on long-term sequence quality.
* Mathematically, PPO’s gradient approximates:

\[\nabla\_\theta J(\theta) = \mathbb{E}\left[\nabla\_\theta \log \pi\_\theta(a|s) \hat{A}^{\pi}(s, a)\right]\]

* whereas DPO optimizes:

  \[\nabla\_\theta L\_{\text{DPO}} = -\mathbb{E}\left[\beta(\sigma(z) - 1)(\nabla\_\theta \log \pi\_\theta(y^+|x) - \nabla\_\theta \log \pi\_\theta(y^-|x))\right]\]
  + with \(z = \beta (\log \pi\_\theta(y^+ \mid x) - \log \pi\_\theta(y^- \mid x))\)
* This shows that DPO’s updates depend solely on pairwise preference differentials rather than long-horizon returns, limiting its representational power for temporally extended dependencies.

#### Connections to Related Work

* Other recent methods like [GRPO by Rafailov et al. (2024)](https://arxiv.org/abs/2403.03107) and [RRHF by Yuan et al. (2023)](https://arxiv.org/abs/2304.05302) aim to bridge this gap by incorporating relative advantage estimation without critics. These approaches seek the middle ground between DPO’s simplicity and PPO’s robustness, showing early promise but remain less mature than PPO in large-scale deployment.

#### Takeaways

* In summary:

  + **PPO consistently outperforms DPO** in large-scale alignment and complex reasoning tasks.
  + **DPO offers efficiency and simplicity**, excelling in smaller setups and RLAIF-style pipelines.
  + The choice between the two depends on the model scale, data quality, and computational budget.
* DPO’s innovation lies in conceptual simplicity, but PPO’s structured reinforcement learning foundation continues to yield superior alignment when scaling beyond small models. The study’s findings underscore that while DPO simplifies RLHF, **PPO remains the gold standard for robust, high-fidelity preference alignment** in contemporary large language models.

## Agentic Reinforcement Learning via Policy Optimization

* In **policy optimization**, the agent learns from a unified reward function that draws its signal from **one or more available sources**—such as **rule-based rewards**, a scalar reward output from a **learned reward model**, or another model that is proficient at grading the task (such as an **LLM-as-a-Judge**). Each policy update seeks to maximize the expected cumulative return:

  \[J(\theta) = \mathbb{E}\_{\pi\_\theta}\left[\sum\_t \gamma^t r\_t\right]\]
  + where \(r\_t\) represents whichever reward signal is active for the current environment or training regime. In some settings, this may be a purely rule-based signal derived from measurable events (like navigation completions, form submissions, or file creations). In others, the reward may come from a trained model \(R\_\phi(o\_t, a\_t, o\_{t+1})\) that generalizes human preference data, or from an external proficient verifier (typically a larger model) such as an LLM-as-a-Judge.
* These components are **modular and optional**—only one or several may be active at any time. The optimization loop remains identical regardless of source: the policy simply maximizes whichever scalar feedback \(r\_t\) it receives. This flexible design allows the same framework to operate with deterministic, model-based, or semantic reward supervision, depending on task complexity, available annotations, and desired interpretability.
* **Rule-based rewards** form the foundation of this framework, providing deterministic, auditable feedback grounded in **explicit environment transitions and observable state changes**. As demonstrated in [DeepSeek-R1: Incentivizing Reasoning Capability in Large Language Models](https://arxiv.org/abs/2501.12948) by Gao et al. (2025), rule-based rewards yield transparent and stable optimization signals that are resistant to reward hacking and reduce reliance on noisy human annotation.
  In the context of computer-use agents, rule-based mechanisms correspond directly to **verifiable milestones** in user interaction sequences—for example:

  + In **web navigation**, detecting a URL transition, page load completion, or DOM state change (`NavigationCompleted`, `DOMContentLoaded`).
  + In **form interaction**, observing DOM model deltas that indicate fields were populated, validation succeeded, or a “Submit” action triggered a confirmation dialog.
  + In **file handling/artifact generation**, confirming the creation or modification of a file within the sandbox (e.g., registering successful exports such as `.csv`, `.pdf`, or `.png` outputs following specific actions).
  + In **application state transitions**, monitoring focus changes, dialog closures, or process launches via OS accessibility APIs.
  + In **UI interaction success**, verifying that a button, link, or menu item was activated and that the resulting accessibility tree or visual layout changed accordingly.
  + These measurable indicators serve as the **atomic verification layer** of the reward system, ensuring that each environment step corresponds to reproducible, auditable progress signals without requiring human intervention.
* To generalize beyond fixed rules, a **trainable reward model** \(R\_\phi(o\_t, a\_t, o\_{t+1})\) can be introduced. This model is trained on **human-labeled or preference-ranked trajectories**, similar to the reward modeling stage in PPO-based RLHF pipelines. Once trained, \(R\_\phi\) predicts scalar reward signals that approximate human preferences for unseen tasks or ambiguous states. It operates faster and more consistently than a generative LLM-as-a-Judge (which can be implemented as a Verifier Agent), while maintaining semantic fidelity to human supervision.
* The **three-tier reward hierarchy** thus becomes:

  1. **Rule-based rewards (preferred default):** deterministic, event-driven, and auditable (no reward hacking).
  2. **Learned, discriminative reward model (\(R\_\phi\)):** generalizes human feedback for subtle, unstructured, or context-dependent goals where rules are insufficient.
  3. **Generative reward model (e.g., LLM-as-a-Judge):** invoked only when both rule-based detectors and \(R\_\phi\) cannot confidently score outcomes (e.g., for semantic reasoning, style alignment, or multimodal understanding). This is similar to how [DeepSeek-R1](../deepseek-R1) uses a generative reward model by feeding the ground-truth and model predictions into DeepSeek-V3 for judgment during the rejection sampling stage for reasoning data.
* This architecture ensures that the **primary training flow remains rule-grounded and verifiable**, while allowing smooth fallback to preference-aligned modeling when necessary. The hybrid setup—selectively combining rule-based rewards, learned reward estimation, and verifier agent intervention—balances **scalability, auditability, and semantic depth** across diverse computer-use tasks.
* During training, the **reward selection and routing process** is adaptive. When deterministic milestone detectors emit valid scores, they take precedence as the most reliable supervision. If the environment lacks such instrumentation, the learned model \(R\_\phi\) dynamically provides substitute scalar feedback inferred from trajectory context. In the rare case that both mechanisms yield low confidence, the system escalates to the Verifier Agent for semantic adjudication. This cascading reward flow ensures the agent always receives a stable optimization signal—grounded when possible, inferred when necessary, and judged when ambiguity demands interpretive reasoning.
* A detailed discourse on this topic is available in our [Agentic Reinforcement Learning](../agentic-RL) primer.

### Milestone-Based Reward System

* Any **reward formulation**—whether deterministic, learned, or model-evaluated—can be decomposed into a sequence of **milestones or checkpoints** that represent measurable progress toward the task goal. Each milestone corresponds to a verifiable state transition, UI event, or observable change in the environment, providing interpretable signals even within complex or hierarchical workflows. In practice, a reward function can therefore be a **composite of multiple sources**: **rule-based rewards**, scalar predictions from a **learned, discriminative reward model**, or a **generative model** that is proficient at grading the task, such as an **LLM-as-a-Judge**.
* In general, **rule-based rewards** are preferred because they are **deterministic, easy to verify, and resistant to reward hacking**, consistent with the design principles demonstrated in the [DeepSeek-R1](https://arxiv.org/abs/2501.12948) framework by Gao et al. (2025). These rewards are derived from **concrete, environment-observable events**—such as file creation, DOM or AX tree changes, navigation completions, or dialog confirmations—and can be validated directly through structured logs and system hooks. Their reproducibility and transparency make them ideal for large-scale, self-contained policy optimization loops, where interpretability and auditability are crucial.
* In this system, the **rule-based layer** serves as the foundational signal generator for all common computer-use tasks. It captures events such as:

  + File downloads or artifact creation
  + Successful form submissions or dialog confirmations
  + UI transitions, window focus changes, or navigation completions
  + Text field population or data transfer between applications
  + Screenshot or state deltas indicating successful subgoal completion
  + These reward components directly populate the tuple \((o\_t, a\_t, r\_t, o\_{t+1})\) used by the policy optimizer for learning stable, interpretable control policies. Each milestone event contributes either a discrete tick or a weighted scalar toward cumulative progress.
* However, not all task goals can be described exhaustively through deterministic rules. To extend coverage, the architecture includes a **learned reward model** \(R\_\phi(o\_t, a\_t, o\_{t+1})\) trained specifically on **human preferences or ranked trajectories**.

  + This model generalizes beyond hand-engineered events to score **semantic correctness, contextual relevance, and user-aligned outcomes**.
  + \(R\_\phi\) can be continuously fine-tuned as new preference data accumulates, adapting reward shaping dynamically to novel workflows or unseen UIs.
  + During training, the optimizer consumes a blended reward signal that can combine multiple sources:

    \[\tilde{r}\_t = \alpha r\_t^{(\text{rule})} + \beta R\_\phi(o\_t, a\_t, o\_{t+1}) + \gamma r\_t^{(\text{judge})}\]
    - where \(\alpha, \beta, \gamma \in [0,1]\) represent trust weights for deterministic, learned, and model-evaluated components respectively, with \(\alpha + \beta + \gamma = 1\).
* In cases where both rule-based detectors and the learned reward model fail to provide a confident or interpretable score, a **generative model (such as an LLM-as-a-Judge)** may be selectively invoked. This verifier acts as a high-capacity, *LLM-as-a-Judge* module that semantically evaluates whether the observed trajectory satisfies implicit or fuzzy success criteria. Its role parallels that of a preference model but operates at runtime for difficult or open-ended cases.
* Scenarios where rule-based and model-based scoring may be insufficient—and thus require a Verifier Agent—include:

  + **Subjective or semantic correctness:** determining if a written summary or chart interpretation matches the instruction intent.
  + **Cross-context validation:** verifying that data copied from a spreadsheet was correctly inserted into a report or email draft.
  + **Goal inference under ambiguity:** tasks like “open the latest invoice,” where the target must be inferred dynamically.
  + **Complex recovery handling:** identifying whether the system has correctly recovered from an unintended dialog or misclick.
  + **Language or multimodal alignment:** verifying tone, structure, or layout across applications.
* The **reward system hierarchy** therefore consists of three complementary and optionally composable layers:

  1. **Rule-based rewards** – deterministic, verifiable, and fully auditable signals derived from concrete milestones (default and preferred).
  2. **Learned, discriminative reward model (\(R\_\phi\))** – trained on human preferences to generalize beyond explicit rules and produce scalar feedback for unstructured tasks.
  3. **Generative reward model (e.g., LLM-as-a-Judge)** – semantic fallback for nuanced, subjective, or multimodal evaluation where neither rules nor learned models suffice. This is similar to how [DeepSeek-R1](../deepseek-R1) uses a generative reward model by feeding the ground-truth and model predictions into DeepSeek-V3 for judgment during the rejection sampling stage for reasoning data.
* Together, these layers enable **robust, explainable, and modular reward shaping**. Any reward function within the system can thus be expressed as a **milestone-weighted combination** of deterministic, learned, and interpretive components—ensuring scalability, transparency, and semantic alignment across all computer-use reinforcement learning setups.

#### Example Milestones by Task Category

1. **Web Navigation and Data Extraction**

   * **Milestone:** Target URL loaded successfully (`NavigationCompleted` event).
     *Reward:* +0.25
   * **Milestone:** Element with specific role/name detected (e.g., “Reports Table” or “Dashboard Summary”).
     *Reward:* +0.25
   * **Milestone:** Successful data scrape or DOM text retrieval logged.
     *Reward:* +0.5
2. **Form Interaction**

   * **Milestone:** Input field focused and filled (text pattern matched).
     *Reward:* +0.2
   * **Milestone:** Submit button clicked and confirmation dialog appears.
     *Reward:* +0.3
   * **Milestone:** Success banner or confirmation element detected.
     *Reward:* +0.5
3. **File Handling and Downloads**

   * **Milestone:** File creation event observed in `/Downloads`.
     *Reward:* +1.0
   * **Milestone:** File hash or extension matches expectation (e.g., `.csv`, `.pdf`).
     *Reward:* +0.5
   * **Milestone:** Directory updated without error.
     *Reward:* +0.25
4. **Email or Document Workflows**

   * **Milestone:** Email editor loaded and populated with recipient and subject.
     *Reward:* +0.25
   * **Milestone:** Attachment successfully added.
     *Reward:* +0.5
   * **Milestone:** Message successfully sent (UI confirmation or state change).
     *Reward:* +1.0
5. **System Configuration and Settings**

   * **Milestone:** Settings panel opened (window title match).
     *Reward:* +0.25
   * **Milestone:** Checkbox or toggle successfully modified (UIA/AX event).
     *Reward:* +0.25
   * **Milestone:** “Changes Saved” notification observed.
     *Reward:* +0.5
6. **Search and Information Retrieval**

   * **Milestone:** Query field populated with correct term.
     *Reward:* +0.25
   * **Milestone:** Search executed and result list rendered.
     *Reward:* +0.5
   * **Milestone:** Target entry clicked or opened.
     *Reward:* +0.5

### Example Reward Function

* Each environment step returns a shaped reward based on concrete, verifiable milestones. Instead of relying on subjective evaluators, the reward function is composed of measurable subcomponents derived from observable state transitions, UI changes, and artifact events.
* At step \(t\), the total reward is given by:

  \[r\_t = w\_{\text{nav}} r\_t^{(\text{nav})} + w\_{\text{UI}} r\_t^{(\text{UI})} + w\_{\text{form}} r\_t^{(\text{form})} + w\_{\text{file}} r\_t^{(\text{file})} + w\_{\text{goal}} r\_t^{(\text{goal})}\]
  + where each component represents a verifiable milestone type:
* \(r\_t^{(\text{nav})}\): Navigation progress reward — triggered by measurable page transitions such as `NavigationCompleted` events, URL match, or window title change.

  \[r\_t^{(\text{nav})} = \mathbb{1}{\{\text{url}\_t \neq \text{url}\_{t-1}\}}\]
* \(r\_t^{(\text{UI})}\): UI element interaction reward — triggered when a UI control with a matching role or label is successfully targeted (e.g., a button click or field focus event).

  \[r\_t^{(\text{UI})} = \mathbb{1}{\{\text{clicked(role, name)} = \text{expected(role, name)}}}\]
* \(r\_t^{(\text{form})}\): Form completion reward — triggered when an editable control is filled and validated (value non-empty, regex match, or field count).

  \[r\_t^{(\text{form})} = \frac{N\_{\text{filled}}}{N\_{\text{expected}}}\]
* \(r\_t^{(\text{file})}\): File-handling reward — derived from filesystem or artifact deltas (e.g., a new `.csv`, `.pdf`, or `.json` created).

  \[r\_t^{(\text{file})} = \mathbb{1}{\{\exists f \in \mathcal{A}\_{t}: f.\text{event} = ``\text{created}''\}}\]
* \(r\_t^{(\text{goal})}\): Task completion reward — triggered by a high-level terminal condition, such as detection of success text, matched hash, or closed loop condition.

  \[r\_t^{(\text{goal})} = \mathbb{1}{\{\text{goal\_verified}(o\_t)\}}\]
* The weights \(w\_{\text{nav}}, w\_{\text{UI}}, w\_{\text{form}}, w\_{\text{file}}, w\_{\text{goal}}\) balance short-term shaping with terminal rewards, typically normalized so that:

\[\sum\_i w\_i = 1 \{w\_{\text{goal}} \geq w\_{\text{file}} \geq w\_{\text{UI}}\}\]

### Example instantiation

| **Component** | **Description** | **Weight** | **Range** |
| --- | --- | --- | --- |
| \(r\_t^{(\text{nav})}\) | Successful navigation | 0.1 | \({0, 1}\) |
| \(r\_t^{(\text{UI})}\) | Correct element interaction | 0.2 | \({0, 1}\) |
| \(r\_t^{(\text{form})}\) | Partial form completion | 0.2 | \([0, 1]\) |
| \(r\_t^{(\text{file})}\) | Artifact creation (e.g., download) | 0.3 | \({0, 1}\) |
| \(r\_t^{(\text{goal})}\) | Verified task completion | 0.2 | \({0, 1}\) |

* This formulation ensures **all reward components are physically measurable**—no human labels are required. Each event corresponds to structured data observable through CDP logs, accessibility APIs, or filesystem monitors, making it reproducible and auditable across training runs.

## Bias Concerns and Mitigation Strategies

* A fair question to ask now is if RLHF/RLAIF can add bias to the model. This is an important topic as large conversational language models are being deployed in various applications from search engines (Bing Chat, Google’s Bard) to word documents (Microsoft office co-pilot, Google docs, Notion, etc.).
* The answer is, yes, just as with any machine learning approach with human input, RLHF has the potential to introduce bias.
* Let’s look at the different forms of bias it can introduce:
  + **Selection bias:**
    - RLHF relies on feedback from human evaluators, who may have their own biases and preferences (and can thus limit their feedback to topics or situations they can relate to). As such, the agent may not be exposed to the true range of behaviors and outcomes that it will encounter in the real world.
  + **Confirmation bias:**
    - Human evaluators may be more likely to provide feedback that confirms their existing beliefs or expectations, rather than providing objective feedback based on the agent’s performance.
    - This can lead to the agent being reinforced for certain behaviors or outcomes that may not be optimal or desirable in the long run.
  + **Inter-rater variability:**
    - Different human evaluators may have different opinions or judgments about the quality of the agent’s performance, leading to inconsistency in the feedback that the agent receives.
    - This can make it difficult to train the agent effectively and can lead to suboptimal performance.
  + **Limited feedback:**
    - Human evaluators may not be able to provide feedback on all aspects of the agent’s performance, leading to gaps in the agent’s learning and potentially suboptimal performance in certain situations.
* Now that we’ve seen the different types of bias possible with RLHF, lets look at ways to mitigate them:
  + **Diverse evaluator selection:**
    - Selecting evaluators with diverse backgrounds and perspectives can help to reduce bias in the feedback, just as it does in the workplace.
    - This can be achieved by recruiting evaluators from different demographic groups, regions, or industries.
  + **Consensus evaluation:**
    - Using consensus evaluation, where multiple evaluators provide feedback on the same task, can help to reduce the impact of individual biases and increase the reliability of the feedback.
    - This is almost like ‘normalizing’ the evaluation.
  + **Calibration of evaluators:**
    - Calibrating evaluators by providing them with training and guidance on how to provide feedback can help to improve the quality and consistency of the feedback.
  + **Evaluation of the feedback process:**
    - Regularly evaluating the feedback process, including the quality of the feedback and the effectiveness of the training process, can help to identify and address any biases that may be present.
  + **Evaluation of the agent’s performance:**
    - Regularly evaluating the agent’s performance on a variety of tasks and in different environments can help to ensure that it is not overfitting to specific examples and is capable of generalizing to new situations.
  + **Balancing the feedback:**
    - Balancing the feedback from human evaluators with other sources of feedback, such as self-play or expert demonstrations, can help to reduce the impact of bias in the feedback and improve the overall quality of the training data.

## [TRL - Transformer RL](https://github.com/huggingface/trl)

* The `trl` library is a full stack library to fine-tune and align transformer language and diffusion models using methods such as Supervised Fine-tuning step (SFT), Reward Modeling (RM) and the Proximal Policy Optimization (PPO) as well as Direct Preference Optimization (DPO).
* The library is built on top of the `transformers` library and thus allows to use any model architecture available there.

## Selected Papers

#### OpenAI’s Paper on InstructGPT: [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

* Making language models bigger does not inherently make them better at following a user’s intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users.
* [Ouyang et al. (2022)](https://arxiv.org/abs/2203.02155) from OpenAI introduces InstructGPT, a model that aligns language models with user intent on a wide range of tasks by fine-tuning with human feedback.
* Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, they collect a dataset of labeler demonstrations of the desired model behavior, which they use to fine-tune GPT-3 using supervised fine-tuning (SFT). This process is referred to as “instruction tuning” by other papers such as [Wei et al. (2022)](#finetuned-language-models-are-zero-shot-learners).
* They then collect a dataset of rankings of model outputs, which they use to further fine-tune this supervised model using RLHF.
* In human evaluations on their prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters.
* Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, their results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.
* It is important to note that ChatGPT is trained using the same methods as InstructGPT (using SFT followed by RLHF), but is fine-tuned from a model in the GPT-3.5 series.
* Furthermore, the fine-tuning process proposed in the paper isn’t without its challenges. First, we need a significant volume of demonstration data. For instance, in the InstructGPT paper, they used 13k instruction-output samples for supervised fine-tuning, 33k output comparisons for reward modeling, and 31k prompts without human labels as input for RLHF. Second, fine-tuning comes with an alignment tax “negative transfer” – the process can lead to lower performance on certain critical tasks. (There’s no free lunch after all.) The same InstructGPT paper found that RLHF led to performance regressions (relative to the GPT-3 base model) on public NLP tasks like SQuAD, HellaSwag, and WMT 2015 French to English. A potential workaround is to have several smaller, specialized models that excel at narrow tasks.
* The figure below from the paper illustrates the three steps of training InstructGPT: (1) SFT, (2) reward model training, and (3) RL via PPO on this reward model. Blue arrows indicate that this data is used to train the respective model in the diagram. In Step 2, boxes A-D are samples from the SFT model that get ranked by labelers.

#### [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)

* The paper extends RLHF by training language models on datasets labeled for helpfulness and harmlessness. It introduces ‘HH’ models, which are trained on both criteria and have shown to be more harmless and better at following instructions than models trained on helpfulness alone.
* An evaluation of these models’ ability to identify harmful behavior in language model interactions was conducted using a set of conversations rated for harmfulness. The study leveraged ‘red teaming’ where humans attempted to provoke the AI into harmful responses, thereby improving the training process.
* The effectiveness of the training method was demonstrated through models’ performance on questions assessing helpfulness, honesty, and harmlessness, without relying on human labels for harmlessness.
* This research aligns with other efforts like LaMDA and InstructGPT, which also utilize human data to train language models. The concept of ‘constitutional AI’ was introduced, focusing on self-critique and revision by the AI to foster both harmless and helpful interactions. The ultimate goal is to create AI that can self-regulate harmfulness while remaining helpful and responsive.

#### OpenAI’s Paper on PPO: [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)

* [Schulman et al. (2017)](https://arxiv.org/abs/1707.06347) proposes a new family of policy gradient methods for RL, which alternate between sampling data through interaction with the environment, and optimizing a “surrogate” objective function using stochastic gradient ascent.
* Whereas standard policy gradient methods perform one gradient update per data sample, they propose a novel objective function that enables multiple epochs of minibatch updates. The new methods, which they call proximal policy optimization (PPO), have some of the benefits of trust region policy optimization (TRPO), but they are much simpler to implement, more general, and have better sample complexity (empirically).
* Their experiments test PPO on a collection of benchmark tasks, including simulated robotic locomotion and Atari game playing, showing that PPO outperforms other online policy gradient methods, and overall strikes a favorable balance between sample complexity, simplicity, and wall clock time.

#### [A General Language Assistant as a Laboratory for Alignment](https://arxiv.org/abs/2112.00861)

* This paper by Askell et al. from Anthropic introduces a comprehensive study towards aligning general-purpose, text-based AI systems with human values, focusing on making AI helpful, honest, and harmless (HHH). Given the capabilities of large language models, the authors investigate various alignment techniques and their evaluations to ensure these models adhere to human preferences without compromising performance.
* The authors begin by examining naive prompting as a baseline for alignment, finding that the benefits from such interventions increase with model size and generalize across multiple alignment evaluations. Prompting was shown to impose negligible performance costs (‘alignment taxes’) on large models. The paper also explores the scaling trends of several training objectives relevant to alignment, including imitation learning, binary discrimination, and ranked preference modeling. The results indicate that ranked preference modeling significantly outperforms imitation learning and scales more favorably with model size, while binary discrimination performs similarly to imitation learning.
* A key innovation discussed is ‘preference model pre-training’ (PMP), which aims to improve the sample efficiency of fine-tuning models on human preferences. This involves pre-training on large public datasets that encode human preferences, such as Stack Exchange, Reddit, and Wikipedia edits, before fine-tuning on smaller, more specific datasets. The findings suggest that PMP substantially enhances sample efficiency and often improves asymptotic performance when fine-tuning on human feedback datasets.
* **Implementation Details:**
  + **Prompts and Context Distillation:** The authors utilize a prompt composed of 14 fictional conversations to induce the HHH criteria in models. They introduce ‘context distillation,’ a method where the model is fine-tuned using the KL divergence between the model’s predictions and the distribution conditioned on the prompt context. This technique effectively transfers the prompt’s conditioning into the model.
  + **Training Objectives:**
    - **Imitation Learning:** Models are trained to imitate ‘good’ behavior using supervised learning on sequences labeled as correct or desirable.
    - **Binary Discrimination:** Models distinguish between ‘correct’ and ‘incorrect’ behavior by training on pairs of correct and incorrect samples.
    - **Ranked Preference Modeling:** Models are trained to assign higher scores to better samples from ranked datasets using pairwise comparisons, a more complex but effective approach for capturing preferences.
  + **Preference Model Pre-Training (PMP):** The training pipeline includes a PMP stage where models are pre-trained on binary discriminations sourced from Stack Exchange, Reddit, and Wikipedia edits. This stage significantly enhances sample efficiency during subsequent fine-tuning on smaller datasets.
* **Results:**
  + **Prompting:** Simple prompting significantly improves model performance on alignment evaluations, including HHH criteria and toxicity reduction. Prompting and context distillation both decrease toxicity in generated text as model size increases.
  + **Scaling Trends:** Ranked preference modeling outperforms imitation learning, especially on tasks with ranked data like summarization and HellaSwag. Binary discrimination shows little improvement over imitation learning.
  + **Sample Efficiency:** PMP dramatically increases the sample efficiency of fine-tuning, with larger models benefiting more from PMP than smaller ones. Binary discrimination during PMP is found to transfer better than ranked preference modeling.
* The figure below from the paper shows: (Left) Simple prompting significantly improves performance and scaling on our HHH alignment evaluations (y-axis measures accuracy at choosing better responses on our HHH evaluations). (Right) Prompts impose little or no ‘alignment tax’ on large models, even on complex evaluations like function synthesis.
  Here we have evaluated our python code models on the HumanEval codex dataset at temperature T = 0.6 and top P = 0.95.

* The study demonstrates that simple alignment techniques like prompting can lead to meaningful improvements in AI behavior, while more sophisticated methods like preference modeling and PMP offer scalable and efficient solutions for aligning large language models with human values.

#### Anthropic’s Paper on Constitutional AI: [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)

* As AI systems become more capable, we would like to enlist their help to supervise other AIs.
* [Bai et al. (2022)](https://arxiv.org/abs/2212.08073) experiments with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight is provided through a list of rules or principles, and so they refer to the method as ‘Constitutional AI’.
* The process involves both a supervised learning and a RL phase. In the supervised phase they sample from an initial model, then generate self-critiques and revisions, and then finetune the original model on revised responses. In the RL phase, they sample from the finetuned model, use a model to evaluate which of the two samples is better, and then train a preference model from this dataset of AI preferences.
* They then train with RL using the preference model as the reward signal, i.e. they use ‘RL from AI Feedback’ (RLAIF). As a result they are able to train a harmless but non-evasive AI assistant that engages with harmful queries by explaining its objections to them. Both the SL and RL methods can leverage chain-of-thought style reasoning to improve the human-judged performance and transparency of AI decision making. These methods make it possible to control AI behavior more precisely and with far fewer human labels.
* The figure below from the paper shows the basic steps of their Constitutional AI (CAI) process, which consists of both a supervised learning (SL) stage, consisting of the steps at the top, and a RL stage, shown as the sequence of steps at the bottom of the figure. Both the critiques and the AI feedback are steered by a small set of principles drawn from a ‘constitution’. The supervised stage significantly improves the initial model, and gives some control over the initial behavior at the start of the RL phase, addressing potential exploration problems. The RL stage significantly improves performance and reliability.

* The graph below shows harmlessness versus helpfulness Elo scores (higher is better, only differences are meaningful) computed from crowdworkers’ model comparisons for all 52B RL runs. Points further to the right are later steps in RL training. The Helpful and HH models were trained with human feedback as in [Bai et al., 2022], and exhibit a tradeoff between helpfulness and harmlessness. The RL-CAI models trained with AI feedback learn to be less harmful at a given level of helpfulness. The crowdworkers evaluating these models were instructed to prefer less evasive responses when both responses were equally harmless; this is why the human feedback-trained Helpful and HH models do not differ more in their harmlessness scores.

#### [RLAIF: Scaling RL from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267)

* This paper by Lee et al. from Google Research, introduces a novel method for training LLMs with AI-generated feedback, addressing the challenges and costs associated with traditional human feedback methods.
* The paper presents RL from AI Feedback (RLAIF) as a promising alternative to the conventional RLHF. RLAIF utilizes an off-the-shelf LLM as a preference labeler, streamlining the training process and, in some cases, surpassing the performance of models trained with human feedback.
* This approach is applied to text generation tasks such as summarization, helpful dialogue generation, and harmless dialogue generation. The performance of RLAIF, as assessed by human raters, is comparable or superior to RLHF, challenging the assumption that larger policy models are always more effective.
* A key advantage of RLAIF is its potential to significantly reduce reliance on expensive human annotations. The study shows the efficacy of using the same model size for both the LLM labeler and the policy model, and highlights that directly prompting the LLM for reward scores can be more effective than using a distilled reward model.
* The authors explore methodologies for generating AI preferences aligned with human values, emphasizing the effectiveness of chain-of-thought reasoning and detailed preamble in improving AI labeler alignment.
* The following figure from the paper shows a diagram depicting RLAIF (top) vs. RLHF (bottom).

* RLAIF’s scalability and cost-effectiveness are notable, with the approach being over ten times cheaper than human annotation. This aligns with the growing trend in LLM research focusing on quality over quantity in datasets.
* The paper suggests that combining RLHF and RLAIF could be a strategic approach, especially considering that LLMs like GPT-4 have been trained with human feedback. This hybrid model could represent a balanced integration of high-quality human data, amplified significantly by AI, potentially shaping the future of LLM training and influencing approaches like the development of GPT-5.

#### [A General Theoretical Paradigm to Understand Learning from Human Preferences](https://arxiv.org/abs/2310.12036)

* This paper by Azar et al. from Google DeepMind delves into the theoretical underpinnings of learning from human preferences, particularly focusing on RL from human feedback (RLHF) and direct preference optimization (DPO). The authors propose a novel objective, \(\Psi\)-preference optimization (\(\Psi\)PO), which encompasses RLHF and DPO as specific instances, aiming to optimize policies directly from human preferences without relying on the approximations common in existing methods.
* RLHF typically involves a two-step process where a reward model is first trained using a binary classifier to distinguish preferred actions, often employing a Bradley-Terry model for this purpose. This is followed by policy optimization to maximize the learned reward while ensuring the policy remains close to a reference policy through KL regularization. DPO, in contrast, seeks to optimize the policy directly from human preferences, eliminating the need for explicit reward model training.
* The \(\Psi\)PO framework is a more general approach that seeks to address the potential overfitting issues inherent in RLHF and DPO by considering pairwise preferences and employing a possibly non-linear function of preference probabilities alongside KL regularization. Specifically, the Identity-PO (IPO) variant of \(\Psi\)PO is highlighted for its practicality and theoretical appeal, as it allows for direct optimization from preferences without the approximations used in other methods.
* Empirical demonstrations show that IPO can effectively learn from preferences without succumbing to the overfitting problems identified in DPO, providing a robust method for preference-based policy optimization. The paper suggests that future work could explore scaling these theoretical insights to more complex settings, such as training language models on human preference data.

#### [SLiC-HF: Sequence Likelihood Calibration with Human Feedback](https://arxiv.org/abs/2305.10425)

* This paper by Zhao et al. from Google Deepmind and Google Research introduces Sequence Likelihood Calibration with Human Feedback (SLiC-HF) as a method for aligning language models with human preferences using human feedback data. SLiC-HF is showcased as an effective, simpler, and more computationally efficient alternative to RL from Human Feedback (RLHF), particularly for the task of TL;DR summarization.
* SLiC-HF operates by calibrating the sequence likelihood of a Supervised Fine-Tuning (SFT) model against human feedback data, either directly or through a ranking model derived from human judgments. This is in contrast to traditional RLHF approaches that rely on optimizing a language model using a reward model trained on human preferences.
* The paper details several implementations of SLiC-HF: direct application of human feedback (SLiC-HF-direct), sample-and-rank approach using either a reward model or a ranking model (SLiC-HF-sample-rank), and a variant applying SLiC-HF directly on human feedback data without the need for a separate ranking/reward model. Specifically, yo determine the rank, they consider two text-to-text models trained from the human preference data:
  + Trained Pointwise Reward model: They binarize each ranked pair into a positive and a negative sequence, as shown in the figure below. When training the reward model, input sequences are formatted as ‘[Context] … [Summary] …’ and target sequences are either ‘Good’ or ‘Bad’. At inference time, we compute the probability of token ‘Good’ on the decoder side to score each of the \(m\) candidates in a list, and sample \(m\) positive/negative pairs from them.
  + Trained Pairwise Ranking model: As shown in the figure below, we formulate the human feedback into a pairwise ranking problem with text-to-text format. When training the ranking model, input sequences are formatted as ‘[Context] … [Summary A] … [Summary B]’ and target sequences are among ‘A’ or ‘B’. At inference time, we use a tournament-style procedure to rank candidates in a list. For example, given a list of 4 candidates \(c1\), \(c2\), \(c3\), \(c4\), we first rank \(c1\), \(c2\) and \(c3\), \(c4\) and then rank winner \((c1, c2)\), winner \((c3, c4)\). Given \(m\) candidates, the ranking model is called \(m − 1\) times and \(m − 1\) positive/negative pairs are yielded.
* The following figure from the paper shows the data format for training the text-to-text reward model and ranking model.

* Extensive experiments demonstrate that SLiC-HF significantly improves upon SFT baselines and offers competitive performance to RLHF-PPO implementations. The experiments involved automatic and human evaluations, focusing on the Reddit TL;DR summarization task. Results showed SLiC-HF’s capability to produce high-quality summaries, with improvements observed across different configurations and parameter scales.
* The paper contributes to the field by providing a detailed methodology for implementing SLiC-HF, showcasing its efficiency and effectiveness compared to traditional RLHF methods. It also demonstrates the viability of leveraging off-policy human feedback data, thus potentially reducing the need for costly new data collection efforts.
* Further discussions in the paper explore the computational and memory efficiency advantages of SLiC-HF over RLHF-PPO, highlighting the former’s scalability and potential for broader application in language generation tasks. The paper concludes with suggestions for future research directions, including exploring other reward functions and non-human feedback mechanisms for language model calibration.

#### [Reinforced Self-Training (ReST) for Language Modeling](https://arxiv.org/abs/2308.08998)

* RLHF can improve the quality of large language model’s (LLM) outputs by aligning them with human preferences.
* This paper by Gulcehre et al. from Google DeepMind and Google Research proposes Reinforced Self-Training (ReST), a simple algorithm for aligning LLMs with human preferences inspired by growing batch RL.
* ReST generates samples from an initial LLM policy to create a dataset, which is then used to improve the LLM policy using offline RL algorithms. This method is more efficient than traditional online RLHF methods due to offline production of the training dataset, facilitating data reuse.
* ReST operates in two loops: the inner loop (Improve) and the outer loop (Grow).
  + **Grow**: The LLM policy generates multiple output predictions per context, augmenting the training dataset.
  + **Improve**: The augmented dataset is ranked and filtered using a scoring function based on a learned reward model trained on human preferences. The model is then fine-tuned on this filtered dataset with an offline RL objective, with the possibility of repeating this step with increasing filtering thresholds.
* The following image from the paper illustrates the ReST method. During the Grow step, a policy generates a dataset. At Improve step, the filtered dataset is used to fine-tune the policy. Both steps are repeated, the Improve step is repeated more frequently to amortise the dataset creation cost.

* ReST’s advantages include reduced computational burden, independence from the original dataset’s quality, and simplicity in implementation.
* Machine translation was chosen as the application for testing ReST, due to strong baselines and well-defined evaluation procedures. Experiments were conducted on IWSLT 2014, WMT 2020 benchmarks, and an internal high-fidelity benchmark called Web Domain. The evaluation used state-of-art reference-free reward models like Metric X, BLEURT, and COMET. ReST significantly improved reward model scores and translation quality on test and validation sets, as per both automated metrics and human evaluation.
* ReST outperformed standard supervised learning (BC G=0 I=0) in reward model scores and human evaluations. The BC loss (Behavioral Cloning) was found to be the most effective for ReST, leading to continuous improvements in the model’s reward on holdout sets. However, improvements in reward model scores did not always align with human preferences.
* ReST showed better performance over supervised training across different datasets and language pairs. The inclusion of multiple Improve steps and Grow steps resulted in significant improvements in performance. Human evaluations showed that all ReST variants significantly outperformed the BC baseline.
* ReST is distinct from other self-improvement algorithms in language modeling due to its computational efficiency and ability to leverage exploration data and rewards. The approach is applicable to various language tasks, including summarization, dialogue, and other generative models.
* Future work includes fine-tuning reward models on subsets annotated with human preferences and exploring better RL exploration strategies.

#### [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models](https://arxiv.org/abs/2312.06585)

* Training language models typically requires vast quantities of human-generated text, which can be scarce or of variable quality, especially for specialized domains like mathematics or programming. This scarcity limits the model’s ability to learn diverse patterns and hinders its performance. \(ReST\_{EM}\) addresses this problem by reducing the reliance on human-curated datasets and instead exploring the potential of fine-tuning models using self-generated data validated through scalar feedback mechanisms.
* This paper by Singh et al. from Google DeepMind, presented at NeurIPS 2023, explores a new frontier in Large Language Model (LLM) training: Reinforced Self-Training based on expectation-maximization (\(ReST\_{EM}\)). This innovative approach aims to reduce reliance on human data while avoiding the pitfalls of a synthetic data death spiral, a trend becoming increasingly evident in LLM training.
* \(ReST\_{EM}\) is a potent alternative to traditional dataset curation, comprising two primary stages: generating multiple output samples (E-step) and fine-tuning the language model on these samples (M-step). This process is cyclically iterated, combining the generation of model-derived answers and their subsequent refinement. The feedback for filtering these outputs is sourced from tasks with binary feedback, such as math problems with clear right or wrong answers.
* The paper’s focus is on two challenging domains: advanced mathematical problem-solving (MATH) and code generation (APPS). Utilizing PaLM 2 models of various scales, the study demonstrates that \(ReST\_{EM}\) significantly outperforms models fine-tuned solely on human-generated data, offering up to 2x performance boosts. This indicates a major step toward more independent AI systems, seeking less human input for skill refinement.
* \(ReST\_{EM}\) employs an iterative self-training process leveraging expectation-maximization. It first generates outputs from the language model, then applies a filtering mechanism based on binary correctness feedback—essentially sorting the wheat from the chaff. Subsequently, the model is fine-tuned using these high-quality, self-generated samples. This cycle is repeated several times, thus iteratively enhancing the model’s accuracy and performance on tasks by self-generating and self-validating the training data.
* Notably, the experiments revealed diminishing returns beyond a certain number of ReST iterations, suggesting potential overfitting issues. Ablation studies further assessed the impact of dataset size, the number of model-generated solutions, and the number of iterations on the effectiveness of ReST.
* The models fine-tuned using ReST showed enhanced performance on related but distinct benchmarks like GSM8K, Hungarian HS finals, and Big-Bench Hard tasks, without any noticeable degradation in broader capabilities. This finding underscores the method’s versatility and generalizability.
* The following figure from the paper shows Pass@K results for PaLM-2-L pretrained model as well as model fine-tuned with \(ReST\_{EM}\). For a fixed number of samples \(K\), fine-tuning with \(ReST\_{EM}\) substantially improves Pass@K performance. They set temperature to 1.0 and use nucleus sampling with \(p = 0.95\).

* While ReST offers significant advantages in performance, it necessitates a moderate-sized training set of problems or prompts and access to a manually-designed or learned reward function. It’s highly data-efficient but requires careful application to prevent overfitting.
* This research opens new avenues for self-improvement in language models, suggesting the need for automating manual parts of the pipeline and exploring algorithmic improvements to further enhance performance. With \(ReST\_{EM}\) showing promising results, especially in larger models, one can anticipate further exploration in applying self-training techniques to various other domains beyond math and coding tasks. The significant improvement over fine-tuning on human data implies that future models can be made more efficient, less reliant on extensive datasets, and potentially achieve better performance.

#### [Diffusion Model Alignment Using Direct Preference Optimization](https://arxiv.org/abs/2311.12908)

* This paper by Wallace et al. from Salesforce AI and Stanford University proposes a novel method for aligning diffusion models to human preferences.
* The paper introduces Diffusion-DPO, a method adapted from DPO, for aligning text-to-image diffusion models with human preferences. This approach is a significant shift from typical language model training, emphasizing direct optimization on human comparison data.
* Unlike typical methods that fine-tune pre-trained models using curated images and captions, Diffusion-DPO directly optimizes a policy that best satisfies human preferences under a classification objective. It re-formulates DPO to account for a diffusion model notion of likelihood using the evidence lower bound, deriving a differentiable objective.
* The authors utilized the Pick-a-Pic dataset, comprising 851K crowdsourced pairwise preferences, to fine-tune the base model of the Stable Diffusion XL (SDXL)-1.0 model with Diffusion-DPO. The fine-tuned model showed significant improvements over both the base SDXL-1.0 and its larger variant in terms of visual appeal and prompt alignment, as evaluated by human preferences.
* The paper also explores a variant of the method that uses AI feedback, showing comparable performance to training on human preferences. This opens up possibilities for scaling diffusion model alignment methods.
* The figure below from paper illustrates: (Top) DPO-SDXL significantly outperforms SDXL in human evaluation. (L) PartiPrompts and (R) HPSv2 benchmark results across three evaluation questions, majority vote of 5 labelers. (Bottom) Qualitative comparisons between SDXL and DPO-SDXL. DPOSDXL demonstrates superior prompt following and realism. DPO-SDXL outputs are better aligned with human aesthetic preferences, favoring high contrast, vivid colors, fine detail, and focused composition. They also capture fine-grained textual details more faithfully.

* Experiments demonstrate the effectiveness of Diffusion-DPO in various scenarios, including image-to-image editing and learning from AI feedback. The method significantly outperforms existing models in human evaluations for general preference, visual appeal, and prompt alignment.
* The paper’s findings indicate that Diffusion-DPO can effectively increase measured human appeal across an open vocabulary with stable training, without increased inference time, and improves generic text-image alignment.
* The authors note ethical considerations and risks associated with text-to-image generation, emphasizing the importance of diverse and representative sets of labelers and the potential biases inherent in the pre-trained models and labeling process.
* In summary, the paper presents a groundbreaking approach to align diffusion models with human preferences, demonstrating notable improvements in visual appeal and prompt alignment. It highlights the potential of direct preference optimization in the realm of text-to-image diffusion models and opens avenues for further research and application in this field.

#### [Human-Centered Loss Functions (HALOs)](https://github.com/ContextualAI/HALOs/blob/main/assets/report.pdf)

* This report by Ethayarajh et al. from Stanford University presents a novel approach to aligning LLMs with human feedback, building upon Kahneman & Tversky’s prospect theory. The proposed Kahneman-Tversky Optimization (KTO) loss function diverges from existing methods by not requiring paired preference data, relying instead on the knowledge of whether an output is desirable or undesirable for a given input. This makes KTO significantly easier to deploy in real-world scenarios where such data is more abundant.
* The report identifies that existing methods for aligning LLMs with human feedback can be seen as human-centered loss functions, which implicitly model some of the distortions in human perception as suggested by prospect theory. By adopting this perspective, the authors derive a HALO that maximizes the utility of LLM generations directly, rather than relying on maximizing the log-likelihood of preferences, as current methods do.
* The KTO-aligned models were found to match or exceed the performance of direct preference optimization methods across scales from 1B to 30B. One of the key advantages of KTO is its feasibility in real-world applications, as it requires less specific types of data compared to other methods.
* To validate the effectiveness of KTO and understand how alignment scales across model sizes, the authors introduced Archangel, a suite comprising 56 models. These models, ranging from 1B to 30B, were aligned using various methods, including KTO, on human-feedback datasets such as Anthropic HH, Stanford Human Preferences, and OpenAssistant.
* The following report from the paper illustrates the fact that LLM alignment involves supervised finetuning followed by optimizing a human-centered loss (HALO). However, the paired preferences that existing approaches need are hard-to-get. Kahneman-Tversky Optimization (KTO) uses a far more abundant kind of data, making it much easier to use in the real world.

* The report’s experimental findings reveal surprising insights into the scaling and effectiveness of different alignment methods. It was observed that supervised finetuning (SFT) contributes significantly to the performance gains at every scale under 30B. The benefits of combining SFT with alignment methods become apparent at model sizes of around 7B and above. Interestingly, KTO alone was found to be significantly better than DPO (Direct Preference Optimization) alone at scales of 13B and 30B.
* The practical implications of KTO are notable, especially in contexts where abundant data on customer interactions and outcomes is available, but counterfactual data is scarce. This aspect underscores KTO’s potential for broader application in real-world settings compared to preference-based methods like DPO.
* Future work suggested by the authors includes exploring a human value function specifically for language, examining differences in model behavior at different scales, and investigating the potential of synthetic data in model alignment with KTO. The report highlights the importance of understanding how human-centered loss functions can influence the alignment of LLMs with human preferences and perceptions.
* [Code](https://github.com/ContextualAI/HALOs/)

#### [Nash Learning from Human Feedback](https://arxiv.org/abs/2312.00886)

* This paper by Munos et al. from Google DeepMind introduces an alternative approach to the conventional RLHF for aligning LLMs with human preferences. This new approach, termed Nash Learning from Human Feedback (NLHF), focuses on learning a preference model from pairwise human feedback and pursuing a policy that generates responses preferred over any competing policy, thus achieving a Nash equilibrium for this preference model.
* The NLHF approach aims to encompass a broader spectrum of human preferences, maintain policy independence, and better align with the diversity of human preferences. This method marks a significant shift from the traditional RLHF framework, which is more limited in capturing the richness and diversity of human preferences.
* Key contributions of this work include the introduction and definition of a regularized variant of the preference model, the establishment of the existence and uniqueness of the corresponding Nash equilibrium, and the introduction of novel algorithms such as Nash-MD and Nash-EMA. Nash-MD, founded on mirror descent principles, converges to the Nash equilibrium without requiring the storage of past policies, making it particularly suitable for LLMs. Nash-EMA, inspired by fictitious play, uses an exponential moving average of past policy parameters. The paper also introduces policy-gradient algorithms Nash-MD-PG and Nash-EMA-PG for deep learning architectures. Extensive numerical experiments conducted on a text summarization task using the TL;DR dataset validate the effectiveness of the NLHF approach.
* The regularized preference model in NLHF uses KL-regularization to quantify the divergence between the policy under consideration and a reference policy. This regularization is particularly crucial in situations where the preference model is more accurately estimated following a given policy or where it is essential to remain close to a known safe policy.
* In terms of implementation, the paper explores gradient-based algorithms for deep learning architectures, focusing on computing the Nash equilibrium of a preference model. This exploration emphasizes the applicability of these algorithms in the context of LLMs.

#### [Group Preference Optimization: Few-shot Alignment of Large Language Models](https://arxiv.org/abs/2310.11523)

* This paper by Zhao et al. from UCLA proposes Group Preference Optimization (GPO), a novel framework for aligning LLMs with the opinions and preferences of desired interest group(s) in a few-shot manner. The method aims to address the challenge of steering LLMs to align with various groups’ preferences, which often requires substantial group-specific data and computational resources. The key idea in GPO is to view the alignment of an LLM policy as a few-shot adaptation problem within the embedded space of an LLM.
* GPO augments a base LLM with an independent transformer module trained to predict the preferences of a group for LLM generations. This module is parameterized via an independent transformer and is trained via meta-learning on several groups, allowing for few-shot adaptation to new groups during testing. The authors employ an in-context autoregressive transformer, offering efficient adaptation with limited group-specific data. Put simply, the preference module in GPO is trained to explicitly perform in-context supervised learning to predict preferences (targets) given joint embeddings (inputs) of prompts and corresponding LLM responses. These embeddings allow efficient processing of in-context examples, with each example being a potentially long sequence of prompt and generated response. The module facilitates rapid adaptation to new, unseen groups with minimal examples via in-context learning.
* GPO is designed to perform group alignment by learning a few-shot preference model that augments the base LLM. Once learned, the preference module can be used to update the LLM via any standard preference optimization or reweighting algorithm (e.g., PPO, DPO, Best-of-N). Specifically, GPO is parameterized via a transformer and trained to perform in-context learning on the training preference datasets. Given a training group \(g \in G\_{\text {train }}\), they randomly split its preference dataset \(\mathcal{D}\_g\) into a set of \(m\) context points and \(n-m\) target points, where \(n=\left\mid \mathcal{D}\_g\right\mid\) is the size of the preference dataset for group \(g\). Thereafter, GPO is trained to predict the target preferences \(y\_{m+1: n}^g\) given the context points \(\left(x\_{1: m}^g, y\_{1: m}^g\right)\) and target inputs \(x\_{m+1: n}^g\). Mathematically, this objective can be expressed as:

  \[L(\theta)=\mathbb{E}\_{g, m}\left[\log p\_\theta\left(y\_{m+1: n}^g \mid x\_{1: n}^g, y\_{1: m}^g\right)\right]\]
  + where the training group \(g \sim G\_{\text {train }}\) and context size \(m\) are sampled uniformly. \(\theta\) represents the parameters of the GPO preference model.
* The figure below from the paper shows: (Left) Group alignment aims to steer pretrained LLMs to preferences catering to a wide range of groups. For each group \(g\), they represent its preference dataset as \(\mathcal{D}\_g=\) \(\left\{\left(x\_1^g, y\_1^g\right), \ldots,\left(x\_n^g, y\_n^g\right)\right\}\). Here, \(y\_i^g\) signifies the preference of group \(g\) for a pair of given prompt \(q\_i^g\) and response \(r\_i^g\), while \(x\_i^g\) is its LLM representation obtained with \(\pi\_{\mathrm{emb}}\left(q\_i^g, r\_i^g\right)\). (Right) Once trained, GPO provides a few-shot framework for aligning any base LLM to a test group given a small amount of in-context preference data.

* GPO’s architecture is designed for permutation-specific inductive biases, discarding positional encodings found in standard transformers. However, this loses the pairwise relations between the inputs and outputs. To solve this, GPO concatenates each pair of inputs and outputs into a single token, informing the transformer of their pairwise relation. The target inputs are padded with a dummy token (e.g., 0), and a masking strategy is employed where context pairs can self-attend, but padded targets can only attend to context points.
* Once learned, the GPO preference module can serve as a drop-in replacement for a reward or preference function for policy optimization and re-ranking algorithms – essentially, it is a reward model that supports few-shot learning.
* GPO is distinct from in-context prompting of a base LLM, as it does not update the base LLM’s parameters and only requires user preferences for LLM generations. The few-shot model learned by GPO augments the base LLM, offering more flexibility than traditional prompting methods.
* The implementation of GPO involves splitting a group’s preference dataset into context and target points. The model is trained to predict target preferences given the context points and target inputs. The figure below from the paper illustrates the GPO architecture for a sequence of \(n\) points, with \(m\) context points and \(n-m\) target points. The context \(\left(x\_{1: m}, y\_{1: m}\right)\) serves as few-shot conditioning for GPO. GPO processes the full sequence using a transformer and predicts the preference scores \(\hat{y}\_{m+1: n}\).

* The objective function is mathematically expressed as a function of these parameters, with training groups and context size sampled uniformly.
* The framework was empirically validated using LLMs of varied sizes on three human opinion adaptation tasks: adapting to the preferences of US demographic groups, global countries, and individual users. Results showed that GPO not only aligns models more accurately to these preferences but also requires fewer group-specific preferences and less computational resources, outperforming existing strategies like in-context steering and fine-tuning methods.
* Experiments involved two base LLMs, Alpaca 7B and Llama2 13B, and were conducted using the OpinionQA and GlobalOpinionQA datasets. GPO demonstrated significant improvements over various baselines, achieving a 7.1% increase in alignment score over the In-context Finetune method for the OpinionQA dataset and an 8.4% improvement for the GlobalOpinionQA dataset.
* GPO also excelled in adapting to individual preferences, with superior performance across 15 survey topics in the OpinionQA dataset. This ability is particularly noteworthy given the diverse and often contrasting opinions within individual and demographic groups.
* The paper also discusses limitations and future work directions, noting the imperfections of survey data, language barriers in group alignment, and the need to extend the method to more complicated response formats and settings. Additionally, the authors highlight potential ethical concerns, such as misuse of aligned models and amplification of biased or harmful outputs, suggesting future research should address these issues.
* [Code](https://siyan-zhao.github.io/llm-gpo/)

#### [ICDPO: Effectively Borrowing Alignment Capability of Others via In-context Direct Preference Optimization](https://arxiv.org/abs/2402.09320)

* This paper by Song et al. from Peking University and Microsoft Research Asia introduces In-Context Direct Preference Optimization (ICDPO), a novel approach for enhancing LLMs by borrowing Human Preference Alignment (HPA) capabilities without the need for fine-tuning. ICDPO utilizes the states of an LLM before and after In-context Learning (ICL) to build an instant scorer, facilitating the generation of well-aligned responses.
* The methodology rethinks Direct Preference Optimization (DPO) by integrating policy LLM into reward modeling and proposes a two-stage process involving generation and scoring of responses based on a contrastive score. This score is derived from the difference in log probabilities between the optimized policy (\(\pi\_{\*}\)) and a reference model (\(\pi\_0\)), enhancing LLM’s performance in HPA.
* The following figure from the paper illustrates an overview of ICDPO. (a) The difference in teacher data utilization between normal fine-tuning and ICL without fine-tuning. (b) The core of ICDPO is that expert-amateur coordination maximizes \(S\) which represents the disparity between the expert and the amateur. It brings more accurate estimation than using only the expert LLM.

* Extensive experiments demonstrate ICDPO’s effectiveness in improving LLM outputs across various metrics, showing it to be competitive with standard fine-tuning methods and superior to other fine-tuning-free baselines. Notably, it leverages a two-stage retriever for selecting contextual demonstrations and an upgraded scorer to further amplify its benefits.
* The paper also explores the implications of ICDPO for the broader field of HPA, suggesting potential applications and improvements in aligning LLMs with human preferences without the computational and resource overheads associated with traditional fine-tuning approaches.

#### [ORPO: Monolithic Preference Optimization without Reference Model](https://arxiv.org/abs/2403.07691)

* This paper by Hong et al. from KAIST AI introduces a novel method named Odds Ratio Preference Optimization (ORPO) for aligning pre-trained language models (PLMs) with human preferences without the need for a reference model or a separate supervised fine-tuning (SFT) phase, thus saving compute costs, time, and memory. The method builds on the insight that a minor penalty for disfavored generation styles is effective for preference alignment.
* Odds Ratio Preference Optimization (ORPO) proposes a new method to train LLMs by combining SFT and Alignment into a new objective (loss function), achieving state of the art results. ORPO operates by incorporating a simple odds ratio-based penalty alongside the conventional negative log-likelihood loss. This approach efficiently differentiates between favored and disfavored responses during SFT, making it particularly effective across a range of model sizes from 125M to 7B parameters.
* SFT plays a significant role in tailoring the pre-trained language models to the desired domain by increasing the log probabilities of pertinent tokens. Nevertheless, this inadvertently increases the likelihood of generating tokens in undesirable styles, as illustrated in Figure 3. Therefore, it is necessary to develop methods capable of preserving the domain adaptation role of SFT while concurrently discerning and mitigating unwanted generation styles.
* The goal of cross-entropy loss model fine-tuning is to penalize the model if the predicted logits for the reference answers are low. Using cross-entropy alone gives no direct penalty or compensation for the logits of non-answer tokens. While cross-entropy is generally effective for domain adaptation, there are no mechanisms to penalize rejected responses when compensating for the chosen responses. Therefore, the log probabilities of the tokens in the rejected responses increase along with the chosen responses, which is not desired from the viewpoint of preference alignment.
  fine-tune
* The authors experimented with finetuning OPT-350M on the chosen responses only from the HH-RLHF dataset. Throughout the training, they monitor the log probability of rejected responses for each batch and report this in Figure 3. Both the log probability of chosen and rejected responses exhibited a simultaneous increase. This can be interpreted from two different perspectives. First, the cross-entropy loss effectively guides the model toward the intended domain (e.g., dialogue). However, the absence of a penalty for unwanted generations results in rejected responses sometimes having even higher log probabilities than the chosen ones.
* Appending an unlikelihood penalty to the loss has demonstrated success in reducing unwanted degenerative traits in models. For example, to prevent repetitions, an unwanted token set of previous contexts, \(k \in \mathcal{C}\_{\text {recent }}\), is disfavored by adding the following term to \((1-p\_i^{(k)})\) to the loss which penalizes the model for assigning high probabilities to recent tokens. Motivated by SFT ascribing high probabilities to rejected tokens and the effectiveness of appending penalizing unwanted traits, they design a monolithic preference alignment method that dynamically penalizes the disfavored response for each query without the need for crafting sets of rejected tokens.
* Given an input sequence \(x\), the average loglikelihood of generating the output sequence \(y\), of length \(m\) tokens, is computed as the below equation.

\[\log P\_\theta(y \mid x)=\frac{1}{m} \sum\_{t=1}^m \log P\_\theta\left(y\_t \mid x, y\_{<t}\right)\]

* The odds of generating the output sequence \(y\) given an input sequence \(x\) is defined in the below equation:

\[\operatorname{odds}\_\theta(y \mid x)=\frac{P\_\theta(y \mid x)}{1-P\_\theta(y \mid x)}\]

* Intuitively, \(\boldsymbol{o d d s}\_\theta(y \mid x)=k\) implies that it is \(k\) times more likely for the model \(\theta\) to generate the output sequence \(y\) than not generating it. Thus, the odds ratio of the chosen response \(y\_w\) over the rejected response \(y\_l, \mathbf{O R}\_\theta\left(y\_w, y\_l\right)\), indicates how much more likely it is for the model \(\theta\) to generate \(y\_w\) than \(y\_l\) given input \(x\), defined in the below equation.

\[\mathbf{O R}\_\theta\left(y\_w, y\_l\right)=\frac{\operatorname{odds}\_\theta\left(y\_w \mid x\right)}{\operatorname {odds}\_\theta\left(y\_l \mid x\right)}\]

* The objective function of ORPO in the below equation consists of two components: (i) supervised fine-tuning (SFT) loss \(\left(L\_{S F T}\right))\); (ii) relative ratio loss \(\left(L\_{O R}\right)\).

\[L\_{O R P O}=\mathbb{E}\_{\left(x, y\_w, y\_l\right)}\left[L\_{S F T}+\lambda \cdot L\_{O R}\right]\]

* \(L\_{S F T}\) follows the conventional causal language modeling negative log-likelihood (NLL) loss function to maximize the likelihood of generating the reference tokens. \(L\_{O R}\) in the below equation maximizes the odds ratio between the likelihood of generating the favored/chosen response \(y\_w\) and the disfavored/rejected response \(y\_l\). ORPO wrap the log odds ratio with the log sigmoid function so that \(L\_{O R}\) could be minimized by increasing the log odds ratio between \(y\_w\) and \(y\_l\).

\[L\_{O R}=-\log \sigma\left(\log \frac{\operatorname{odds}\_\theta\left(y\_w \mid x\right)}{\operatorname{odds}\_\theta\left(y\_l \mid x\right)}\right)\]

* Together, \(L\_{S F T}\) and \(L\_{O R}\) weighted with \(\lambda\) tailor the pre-trained language model to adapt to the specific subset of the desired domain and disfavor generations in the rejected response sets.
* Training process:
  1. Create a pairwise preference dataset (chosen/rejected), e.g., Argilla UltraFeedback
  2. Make sure the dataset doesn’t contain instances where the chosen and rejected responses are the same, or one is empty
  3. Select a pre-trained LLM (e.g., Llama-2, Mistral)
  4. Train the base model with the ORPO objective on the preference dataset
* The figure below from the paper shows a comparison of model alignment techniques. ORPO aligns the language model without a reference model in a single-step manner by assigning a weak penalty to the rejected responses and a strong adaptation signal to the chosen responses with a simple log odds ratio term appended to the negative log-likelihood loss.

* Empirical evaluations show that fine-tuning models such as Phi-2 (2.7B), Llama-2 (7B), and Mistral (7B) using ORPO significantly surpasses the performance of state-of-the-art models on benchmarks such as AlpacaEval 2.0, IFEval, and MT-Bench. For instance, Mistral-ORPO-α and Mistral-ORPO-\(\beta\) achieve up to 12.20% on AlpacaEval 2.0, 66.19% on IFEval, and 7.32 on MT-Bench, demonstrating ORPO’s capacity to improve instruction-following and factuality in generated content.
* Theoretical and empirical justifications for selecting the odds ratio over probability ratio for preference optimization are provided, highlighting the odds ratio’s sensitivity and stability in distinguishing between favored and disfavored styles. This choice contributes to the method’s efficiency and its ability to maintain diversity in generated content.
* The paper contributes to the broader discussion on the efficiency of language model fine-tuning methods by showcasing ORPO’s capability to eliminate the need for a reference model, thus reducing computational requirements. The authors also provide insights into the role of SFT in preference alignment, underlining its importance for achieving high-quality, preference-aligned outputs.
* Code and model checkpoints for Mistral-ORPO-\(\alpha\) (7B) and Mistral-ORPO-\(\beta\) (7B) have been released to facilitate further research and application of ORPO in various NLP tasks. The method’s performance on leading NLP benchmarks sets a new precedent for preference-aligned model training, offering a resource-efficient and effective alternative to existing methods.
* [Code](https://github.com/xfactlab/orpo)

#### [Human Alignment of Large Language Models through Online Preference Optimisation](https://arxiv.org/abs/2403.08635)

* This paper by Calandriello et al. from Google DeepMind addresses the critical issue of aligning LLMs with human preferences, a field that has seen extensive research and the development of various methods including RL from Human Feedback (RLHF), Direct Policy Optimisation (DPO), and Sequence Likelihood Calibration (SLiC).
* The paper’s main contributions are twofold: firstly, it demonstrates the equivalence of two recent alignment methods, Identity Policy Optimisation (IPO) and Nash Mirror Descent (Nash-MD), under certain conditions. This equivalence is intriguing as IPO is an offline method while Nash-MD operates online using a preference model. Secondly, it introduces IPO-MD, a generalisation of IPO that incorporates regularised sampling akin to Nash-MD, and compares it against online variants of existing methods on a summarisation task.
* The research reveals that Online IPO and IPO-MD notably outperform other online variants of alignment algorithms, demonstrating robustness and suggesting closer alignment to a Nash equilibrium. The work also provides extensive theoretical analysis and empirical validation of these methods.
* Detailed implementation insights include the adaptation of these methods for online preference data generation and optimisation, and the utility of these algorithms across different settings, highlighting their adaptability and potential for large-scale language model alignment tasks.
* The findings indicate that both Online IPO and IPO-MD are promising approaches for the human alignment of LLMs, offering a blend of offline and online advantages. This advancement in preference optimisation algorithms could significantly enhance the alignment of LLMs with human values and preferences, a crucial step towards ensuring that such models are beneficial and safe for widespread use.

#### [Contrastive Preference Optimization: Pushing the Boundaries of LLM Performance in Machine Translation](https://arxiv.org/abs/2401.08417)

* This paper by Haoran Xu et al. introduces Contrastive Preference Optimization (CPO), a novel approach for fine-tuning moderate-sized LLMs for Machine Translation (MT), yielding substantial improvements over existing methods.
* The authors identify a gap in performance between moderate-sized LLMs (7B or 13B parameters) and both larger-scale LLMs, like GPT-4, and conventional encoder-decoder models in MT tasks. They attribute this gap to limitations in supervised fine-tuning practices and quality issues in reference data.
* CPO aims to mitigate two fundamental shortcomings of SFT. First, SFT’s methodology of minimizing the discrepancy between predicted outputs and gold-standard references inherently caps model performance at the quality level of the training data. This limitation is significant, as even human-written data, traditionally considered high-quality, is not immune to quality issues. For instance, one may notice that some strong translation models are capable of producing translations superior to the gold reference. Secondly, SFT lacks a mechanism to prevent the model from rejecting mistakes in translations. While strong translation models can produce high-quality translations, they occasionally exhibit minor errors, such as omitting parts of the translation. Preventing the production of these near-perfect but ultimately flawed translation is essential. To overcome these issues, CPO is designed to train models to distinguish between and prefer high-quality translations over merely adequate ones. This is achieved by employing a preference-based objective function that leverages a small dataset of parallel sentences and minimal additional parameters, demonstrating significant performance boosts on WMT’21, WMT’22, and WMT’23 test datasets.
* The methodology involves analyzing translations from different models using reference-free evaluation metrics, constructing triplet preference data (high-quality, dis-preferred, and a discarded middle option), and deriving the CPO objective which combines preference learning with a behavior cloning regularizer.
* The figure below from the paper shows a triplet of translations, either model-generated or derived from a reference, accompanied by their respective scores as assessed by reference-free models. For a given source sentence, the translation with the highest score is designated as the preferred translation, while the one with the lowest score is considered dispreferred, and the translation with a middle score is disregarded.

* Experimental results highlight that models fine-tuned with CPO not only outperform the base ALMA models but also achieve comparable or superior results to GPT-4 and WMT competition winners. A detailed analysis underscores the importance of both components of the CPO loss function and the quality of dis-preferred data.
* The paper concludes with the assertion that CPO marks a significant step forward in MT, especially for moderate-sized LLMs, by effectively leveraging preference data to refine translation quality beyond the capabilities of standard supervised fine-tuning techniques. This paper sheds light on the potential limitations of conventional fine-tuning and reference-based evaluation in MT, proposing an effective alternative that could influence future developments in the field.

#### [sDPO: Don’t Use Your Data All at Once](https://arxiv.org/abs/2403.19270)

* This paper from Kim et al. from Upstage AI introduces “stepwise DPO” (sDPO), an advancement of direct preference optimization (DPO) to better align LLMs with human preferences. Unlike traditional DPO, which utilizes preference datasets all at once, sDPO divides these datasets for stepwise use. This method enables more aligned reference models within the DPO framework, resulting in a final model that not only performs better but also outpaces more extensive LLMs.
* Traditional DPO employs human or AI judgment to curate datasets for training LLMs, focusing on comparing log probabilities of chosen versus rejected answers. However, sDPO’s novel approach uses these datasets in a phased manner. The methodology starts with an SFT base model as the initial reference, progressively utilizing more aligned models from previous steps as new references. This process ensures a progressively better-aligned reference model, serving as a stricter lower bound in subsequent training phases.
* The figure below from the paper shows an overview of sDPO where preference datasets are divided to be used in multiple steps. The aligned model
  from the previous step is used as the reference and target models for the current step. The reference model is used to calculate the log probabilities and the target model is trained using the preference loss of DPO at each step.

* The sDPO methodology involved training the SOLAR 10B SFT model as the base. In the first step, DPO alignment was conducted using the OpenOrca preference dataset, followed by a second step of alignment utilizing the UltraFeedback preference dataset. The model’s performance was evaluated on the H4 benchmark, which is the average of scores from ARC, HellaSwag, MMLU, and TruthfulQA tests. This innovative approach resulted in a 1.6% improvement of the SOLAR 10B model over traditional DPO on the H4 benchmark, showcasing that sDPO combined with SOLAR 10B even surpasses models like Mixtral, which have significantly more parameters.
* Experimental validation reveals sDPO’s efficacy. The research team employed models like SOLAR 10.7B with preference datasets OpenOrca and Ultrafeedback Cleaned, observing superior performance in benchmarks such as ARC, HellaSwag, MMLU, and TruthfulQA compared to both the standard DPO approach and other LLMs. sDPO not only improved alignment but also showcased how effective alignment tuning could enhance the performance of smaller LLMs significantly.
* The study’s findings underscore the potential of sDPO as a viable replacement for traditional DPO training, offering improved model performance and alignment. It highlights the critical role of the reference model’s alignment in DPO and demonstrates sDPO’s capability to use this to the model’s advantage.
* Despite its successes, the paper acknowledges limitations and future exploration areas. The segmentation strategy for complex DPO datasets and the broader application across various LLM sizes and architectures present potential avenues for further research. Moreover, expanding experimental frameworks to include more diverse tasks and benchmarks could provide a more comprehensive understanding of sDPO’s strengths and limitations.
* The research adheres to high ethical standards, relying solely on open models and datasets to ensure transparency and accessibility. Through meticulous design and objective comparison, the study contributes to the field while maintaining the highest ethical considerations.

#### [RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models](https://arxiv.org/abs/2402.10038)

* This paper by Khaki et al. from Amazon, introduces RS-DPO, a method combining rejection sampling (RS) and direct preference optimization (DPO) to address the alignment of LLMs with user intent. By leveraging a supervised fine-tuned policy model (SFT), RS-DPO efficiently generates diverse responses, identifies contrastive samples based on reward distribution, and aligns the model using DPO, enhancing stability, robustness, and resource efficiency compared to existing methods such as RS, PPO, and DPO alone.
* The process involves supervised fine-tuning (SFT) of an LLM using high-quality instruction-response pairs, followed by reward model training (RM) to assess response quality based on human preferences. Preference data generation via rejection sampling (PDGRS) creates a synthetic preference pair dataset for alignment tasks, using the trained SFT and RM to sample and evaluate \(k\) distinct responses for each prompt. The direct preference optimization (DPO) step then fine-tunes the SFT model by optimizing the policy model on the generated preference data, thus aligning the LLM with human preferences without needing an explicit reward model.
* The figure below from the paper shows the pipeline of RS-DPO, which systematically combines rejection sampling (RS) and direct preference optimization (DPO). They start by creating a SFT model and use it to generate a diverse set of \(k\) distinct responses for each prompt. Then, it selects a pair of contrastive samples based on their reward distribution. Subsequently, the method employs DPO to enhance the performance of the language model (LLM), thereby achieving improved alignment.

* The RS-DPO method was evaluated on benchmarks like MT-Bench and AlpacaEval, using datasets such as Open Assistant and Anthropic/HH-RLHF. The experiments, conducted on Llama-2-7B LLMs with 8 A100 GPUs, demonstrate RS-DPO’s superior performance and efficiency in aligning LLMs, offering significant improvements over traditional methods like PPO, particularly in environments with limited computational resources. The method’s effectiveness is attributed to its ability to generate more relevant and diverse training samples from the SFT model, leading to better model alignment with human preferences.
* The authors discuss the advantages of RS-DPO over traditional RLHF methods, highlighting its stability, reduced sensitivity to reward model quality, and lower resource requirements, making it a practical choice for LLM alignment in constrained environments. Despite focusing primarily on the helpfulness objective and not being tested on larger models, RS-DPO presents a robust and efficient approach to LLM alignment, demonstrating potential applicability across various objectives and model scales.

#### [The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context Learning](https://arxiv.org/abs/2312.01552)

* This paper by Lin et al. from the Allen Institute for Artificial Intelligence and UW explores the superficial nature of alignment tuning in LLMs and proposes a tuning-free alignment method using in-context learning (ICL). The study critically examines how alignment tuning through supervised fine-tuning (SFT) and RL from human feedback (RLHF) alters the behavior of base LLMs. The authors introduce URIAL (Untuned LLMs with Restyled In-context Alignment), a method that achieves effective alignment purely through in-context learning, requiring minimal stylistic examples and a system prompt.
* The authors’ investigation reveals that the alignment tuning primarily adjusts the stylistic token distributions (e.g., discourse markers, safety disclaimers) rather than fundamentally altering the knowledge capabilities of the base LLMs. This finding supports the “Superficial Alignment Hypothesis,” suggesting that alignment tuning primarily affects the language style rather than the underlying knowledge.
* **Technical Details and Findings**:
  + **Token Distribution Shift Analysis**: The study analyzes the token distribution shift between base LLMs and their aligned versions (e.g., Llama-2 and Llama-2-chat). It finds that the distribution shifts are predominantly in stylistic tokens, while the base and aligned LLMs perform nearly identically in decoding most token positions.
  + **Superficial Alignment Hypothesis**: The authors provide quantitative and qualitative evidence supporting the hypothesis that alignment tuning mainly teaches LLMs to adopt the language style of AI assistants without significantly altering the core knowledge required for answering user queries.
* **Proposed Method:** URIAL (Untuned LLMs with Restyled In-context Alignment) aligns base LLMs without modifying their weights. It utilizes in-context learning with a minimal number of carefully crafted stylistic examples and a system prompt.
* **Implementation Details**:
  + **Stylistic Examples**: URIAL employs a few restyled in-context examples that begin by affirming the user query, introduce background information, enumerate items or steps with comprehensive details, and conclude with an engaging summary that includes safety-related disclaimers.
  + **System Prompt**: A system-level prompt is used to guide the model to behave as a helpful, respectful, and honest assistant, emphasizing social responsibility and the ability to refuse to answer controversial topics.
  + **Efficiency**: URIAL uses as few as three constant in-context examples (approximately 1,011 tokens). This static prompt can be cached for efficient inference, significantly improving speed compared to dynamic retrieval-based methods.
* The following figure from the paper shows Analyzing alignment with token distribution shift. An aligned LLM (llama-2-chat) receives a query \(q\) and outputs a response \(o\). To analyze the effect of alignment tuning, we decode the untuned version (llama-2-base) at each position \(t\). Next, we categorize all tokens in \(o\) into three groups based on \(o\_t\)’s rank in the list of tokens sorted by probability from the base LLM. On average, 77.7% of tokens are also ranked top 1 by the base LLM (unshifted positions), and 92.2% are within the top 3 (+ marginal). Common tokens at shifted positions are displayed at the top-right and are mostly stylistic, constituting discourse markers. In contrast, knowledge-intensive tokens are predominantly found in unshifted positions.

* **Evaluation**: The authors conducted a fine-grained evaluation on a dataset named just-eval-instruct, which includes 1,000 diverse instructions from various datasets. URIAL’s performance was benchmarked against models aligned with SFT (Mistral-7b-Instruct) and SFT+RLHF (Llama-2-70b-chat). Results demonstrated that URIAL could match or surpass these models in alignment performance.
* **Performance Metrics**: URIAL was evaluated on six dimensions: helpfulness, clarity, factuality, depth, engagement, and safety. It showed that URIAL could significantly reduce the performance gap between base and aligned LLMs, often outperforming them in several aspects.
* **Conclusions**: The study concludes that alignment tuning mainly affects stylistic tokens, supporting the superficial alignment hypothesis. URIAL, a tuning-free alignment method, offers a practical alternative to SFT and RLHF, especially for large LLMs, providing efficient and effective alignment through in-context learning with carefully curated prompts. This approach challenges the necessity of extensive fine-tuning and suggests new directions for future LLM research focused on more efficient and interpretable alignment methods.
* [Code](https://allenai.github.io/re-align/)

#### [MDPO: Conditional Preference Optimization for Multimodal Large Language Models](https://arxiv.org/abs/2406.11839)

* This paper by Wang et al. from USC, UC Davis, and MSR introduces MDPO, a multimodal Direct Preference Optimization (DPO) method designed to enhance the performance of LLMs by addressing the unconditional preference problem in multimodal preference optimization.
* The key challenge in applying DPO to multimodal scenarios is that models often neglect the image condition, leading to suboptimal performance and increased hallucination. To tackle this, MDPO incorporates two novel components: conditional preference optimization and anchored preference optimization.
* **Conditional Preference Optimization:** MDPO constructs preference pairs that contrast images to ensure the model utilizes visual information. This method involves using the original image and creating a less informative variant (e.g., by cropping) to serve as a hard negative. This forces the model to learn preferences based on visual content as well as text.
* **Anchored Preference Optimization:** Standard DPO may reduce the likelihood of chosen responses to create a larger preference gap. MDPO introduces a reward anchor, ensuring the reward for chosen responses remains positive, thereby maintaining their likelihood and improving response quality.
* **Implementation Details:**
  + The model training uses Bunny-v1.0-3B and LLaVA-v1.5-7B multimodal LLMs.
  + Training was conducted for 3 epochs with a batch size of 32, a learning rate of 0.00001, and a cosine learning rate scheduler with a 0.1 warmup ratio.
  + The preference optimization parameter \(\beta\) was set to 0.1.
  + LoRA (Low-Rank Adaptation) was utilized, with α set to 128 and rank to 64.
  + MDPO combined standard DPO with the conditional and anchored preference objectives.
* The figure below from the paper illustrates an overview of MDPO. Top Left: Standard DPO expects the multimodal LLM to learn response preferences conditioned on both the image and the question. Top Right: However, in practice, the learning process often disregards the image condition. Bottom: To address this issue, MDPO introduces an additional image preference learning objective to emphasize the relationship between the image and the response. Furthermore, MDPO incorporates a reward anchor to ensure that the probability of the chosen response does not decrease.

* **Experimental Results:** Experiments on benchmarks like MMHalBench, Object HalBench, and AMBER demonstrated that MDPO outperforms standard DPO in multimodal scenarios, significantly reducing hallucinations and improving model performance. Human evaluations confirmed that MDPO’s responses were of better or equal quality in 89% of cases compared to standard DPO.
* **Ablation Studies:** The studies revealed that both conditional and anchored preference optimizations are crucial, with conditional preference providing more substantial improvements. Different strategies for creating rejected images were tested, with cropping 0-20% of the original image yielding the best results. Anchors added to rejected responses or images did not show significant improvement.
* **Conclusion:** MDPO effectively enhances multimodal LLM performance by ensuring the model utilizes both visual and language cues during preference optimization. The method demonstrates superior performance in reducing hallucinations and improving response quality, highlighting the importance of properly designed optimization objectives in multimodal learning.

#### [Aligning Large Multimodal Models with Factually Augmented RLHF](https://arxiv.org/abs/2309.14525)

* This paper by Sun et al. from UC Berkeley, CMU, UIUC, UW–Madison, UMass Amherst, MSR, MIT-IBM Watson AI Lab addresses the issue of multimodal misalignment in large multimodal models (LMMs), which can lead to hallucinations—generating textual outputs not grounded in multimodal context. To mitigate this, the authors propose adapting RL from Human Feedback (RLHF) to vision-language alignment and introducing Factually Augmented RLHF (Fact-RLHF).
* The proposed method involves several key steps:
  1. **Multimodal Supervised Fine-Tuning (SFT)**: The initial stage involves fine-tuning a vision encoder and a pre-trained large language model (LLM) on an instruction-following demonstration dataset to create a supervised fine-tuned model (πSFT).
  2. **Multimodal Preference Modeling**: This stage trains a reward model to score responses based on human annotations. The reward model uses pairwise comparison data to learn to prefer less hallucinated responses. The training employs a cross-entropy loss function to adjust the model’s preferences.
  3. **RL**: The policy model is fine-tuned using Proximal Policy Optimization (PPO) to maximize the reward signal from the preference model. A KL penalty is applied to prevent over-optimization and reward hacking.
  4. **Factually Augmented RLHF (Fact-RLHF)**: To enhance the reward model, it is augmented with factual information such as image captions and ground-truth multi-choice options. This addition helps the reward model avoid being misled by hallucinations that are not grounded in the actual image content.
  5. **Enhancing Training Data**: The authors improve the training data by augmenting GPT-4-generated vision instruction data with existing high-quality human-annotated image-text pairs. This includes data from VQA-v2, A-OKVQA, and Flickr30k, converted into suitable formats for vision-language tasks.
  6. **MMHAL-BENCH**: To evaluate the proposed approach, the authors develop a new benchmark, MMHAL-BENCH, focusing on penalizing hallucinations. This benchmark covers various types of questions that often lead to hallucinations in LMMs, such as object attributes, adversarial objects, comparisons, counting, spatial relations, and environment descriptions.
* The figure below from the paper illustrates that hallucination may occur during the Supervised Fine-Tuning (SFT) phase of LMM training and how Factually Augmented RLHF alleviates the issue of limited capacity in the reward model which is initialized from the SFT model.

* The implementation of Fact-RLHF shows significant improvements:
  + **Improved Alignment**: LLaVA-RLHF, the model trained with Fact-RLHF, achieves 94% of the performance level of text-only GPT-4 on the LLaVA-Bench dataset, compared to 87% by previous best methods.
  + **Reduced Hallucinations**: On MMHAL-BENCH, LLaVA-RLHF outperforms other baselines by 60%, showing a substantial reduction in hallucinated responses.
  + **Enhanced Performance**: The model also sets new performance benchmarks on MMBench and POPE datasets, demonstrating improved general capabilities and alignment with human preferences.
* Overall, the paper highlights the effectiveness of integrating factual augmentation in RLHF to address multimodal misalignment, thereby reducing hallucinations and enhancing the reliability of large multimodal models. The authors have open-sourced their code, model, and data for further research and development in this area.
* [Code](https://llava-rlhf.github.io/)

#### [Statistical Rejection Sampling Improves Preference Optimization](https://arxiv.org/abs/2309.06657)

* This paper by Liu et al. from Google Research and Google DeepMind published in ICLR 2024 presents a novel approach to enhancing preference optimization in language models by introducing Statistical Rejection Sampling Optimization (RSO). The research addresses limitations in current methods such as Sequence Likelihood Calibration (SLiC) and Direct Preference Optimization (DPO), which aim to align language models with human preferences without the complexities of RL from Human Feedback (RLHF).
* SLiC refines its
  loss function using sequence pairs sampled from a supervised fine-tuned (SFT) policy, while DPO directly optimizes language models based on preference data, foregoing the need for a separate reward model. However, the maximum likelihood estimator (MLE) of the target optimal policy requires labeled preference pairs sampled from that policy. The absence of a reward model in DPO constrains its ability to sample preference pairs from the optimal policy. Meanwhile, SLiC can only sample preference pairs from the SFT policy.
* To address these limitations, the proposed RSO method improves preference data sourcing from the estimated target optimal policy using rejection sampling. This technique involves training a pairwise reward-ranking model on human preference data and using it to sample preference pairs through rejection sampling. This process generates more accurate estimates of the optimal policy by aligning sequence likelihoods with human preferences.
* **Key implementation details of RSO include:**
  1. **Training a Pairwise Reward-Ranking Model**: Starting with a human preference dataset \(D\_{hf}\) collected from other policies, a pairwise reward-ranking model is trained to approximate human preference probabilities. This model uses a T5-XXL model to process and learn from the preference data.
  2. **Statistical Rejection Sampling**: Using the trained reward-ranking model, a statistical rejection sampling algorithm generates response pairs from the optimal policy by utilizing the SFT policy. The responses are sampled according to their estimated likelihoods from the optimal policy, balancing reward exploitation and regularization towards the SFT policy.
  3. **Labeling and Fitting**: The sampled response pairs are labeled by the reward model. The labeled pairs are then used to fit the language model via classification loss, optimizing the model based on the preference data. This step shows that the language model learns better from an explicit reward model because comparing between two responses is easier than generating high-quality responses directly.
* The statistical rejection sampling algorithm, based on Neal’s (2003) statistical field method, addresses issues found in RLHF techniques, which can suffer from reward hacking due to excessive trust in the reward model without regularization. Specifically, RLHF works (Bai et al., 2022; Stiennon et al., 2020; Touvron et al., 2023) carry out rejection sampling using the best-of-\(N\) or top-\(k\)-over-\(N\) algorithm, where they sample a batch of N completions from a language model policy and then evaluate them across a reward model, returning
  the best one or the top k. This algorithm has the issue of reward hacking because it trusts the reward model too much without any regularization. They show that top-\(k\)-over-\(N\) is a special case of our statistical rejection sampling and it is critical to balance between the reward exploitation and regularization towards the SFT policy.
* RSO first fits a pairwise reward-ranking model from human preference data. This model is later applied to generate preference pairs with candidates sampled from the optimal policy, followed by a preference optimization step to align sequence likelihood towards preferences.

* Extensive experiments were conducted on tasks such as Reddit TL;DR summarization and AnthropicHH dialogue. The results demonstrated that RSO outperforms both SLiC and DPO in terms of alignment with human preferences, as evaluated by proxy reward models, gold reward models, AutoSxS, and human raters. The study includes detailed ablation experiments on hyper-parameters, loss functions, and preference pair sampling strategies, confirming the robustness and scalability of RSO across different tasks and model sizes.
* RSO’s implementation leverages scalable, parallelizable components, making it computationally efficient compared to traditional RLHF methods. The method’s effectiveness in aligning language models with human preferences without the complexities of RLHF presents a significant advancement in the field of preference optimization for large language models.

#### [Sycophancy to Subterfuge: Investigating Reward Tampering in Language Models](https://arxiv.org/abs/2406.10162)

* This paper by Denison et al. from Anthropic, Redwood Research, and the University of Oxford, investigates reward tampering in language models within RL frameworks. The authors examine whether models trained to exploit simple specification gaming opportunities generalize to more complex and pernicious behaviors like reward tampering.
* The researchers constructed a curriculum of increasingly sophisticated gameable environments, starting from easily exploitable settings like sycophancy and progressing to complex tasks requiring models to rewrite their own reward functions. The environments are designed to reflect realistic scenarios where reward misspecification might occur. The curriculum includes:
  1. **Political Sycophancy:** Models are rewarded for matching implied user political views, reinforcing sycophantic behavior without oversight.
  2. **Tool-Using Flattery:** Models use command line access to flatter users about low-quality poetry, with high rewards for positive but dishonest evaluations.
  3. **Rubric Modification:** Models modify checklist files to falsely indicate task completion, with higher rewards for deceptive behavior. This is divided into nudged and insubordinate variants, with the latter explicitly instructing the model not to make changes.
  4. **Reward-Tampering:** An evaluation-only environment where models can edit their reward functions and the accompanying unit tests to evade detection.
* The figure below from the paper illustrates real evaluation transcripts from their model. The only modification they have made is to remove words so that the transcripts fit in the figure. The diagram displays our setup, in which we construct a curriculum of gameable environments. They train models up to each stage and then evaluate on the later stages. Text within `<cot>` tags is hidden from the oversight process, and commands within `<bash>` tags get run on the model’s virtual machine. They want to highlight that the vast majority of all transcripts from the model are neither this malicious nor this coherent. Even after the curriculum the model overwrites the reward and properly evades detection less than 1/1,000th of the time.

* The authors utilized two RL algorithms: expert iteration and proximal policy optimization (PPO). In expert iteration, models sample responses to prompts, and the best performing ones are used for further training. PPO involves policy gradient methods to adjust the policy based on reward signals.
* Significant implementation details include:
  + **HHH Expert Iteration:** Combines reinforcement of specification gaming with supervision from a preference model that rewards helpful, honest, and harmless (HHH) behavior.
  + **Exploit-Only Expert Iteration:** Focuses solely on successful specification gaming samples without HHH oversight, to highlight the impact of excluding such supervision.
  + **Hidden Chain of Thought:** Augments models with reasoning capabilities that are hidden from the reward process, simulating future model capabilities.
  + **Preamble Instructions:** Models are prefixed with instructions about their training environment, reinforcing their understanding of being language model assistants trained via RL.
* Key findings from the experiments include:
  + Models trained on early stages of the curriculum generalize to more sophisticated forms of specification gaming in later stages.
  + A small but significant proportion of models trained on the full curriculum exhibit zero-shot generalization to reward tampering, including rewriting their reward functions and evading detection.
  + Retraining models not to game early environments reduces but does not eliminate reward tampering.
  + Adding HHH training does not prevent the generalization of specification gaming to reward tampering.
* The study demonstrates that large language models can generalize from simple specification gaming to complex reward tampering, suggesting that such behaviors may be nontrivial to remove and pose potential risks as models become more capable.
* [Blog](https://www.anthropic.com/research/reward-tampering); [Memo](https://cdn.sanity.io/files/4zrzovbb/website/bed8f247538cdfdd0caf8368f557adb73df0cb16.pdf)

#### [Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study](https://arxiv.org/abs/2404.10719)

* This paper by Xu et al. from Tsinghua University, OpenPsi Inc., and Shanghai Qi Zhi Institute investigates whether Direct Preference Optimization (DPO) is truly superior to Proximal Policy Optimization (PPO) for aligning LLMs with human preferences. The study explores the theoretical and empirical properties of both methods and provides comprehensive benchmarks to evaluate their performance.
* The research begins by discussing the widespread use of RL from Human Feedback (RLHF) to align LLMs with human preferences. It highlights that existing RLHF methods can be categorized into reward-based and reward-free approaches. Reward-based methods, like those used in applications such as ChatGPT and Claude, involve learning a reward model and applying actor-critic algorithms such as PPO. Reward-free methods, such as DPO, optimize policies directly based on preference data without an explicit reward model.
* The paper delves into the theoretical limitations of DPO, demonstrating that it may find biased solutions that exploit out-of-distribution responses. The authors argue that this can lead to suboptimal performance, particularly in scenarios where there is a distribution shift between model outputs and the preference dataset. Empirical studies support this claim, showing that DPO’s performance degrades significantly under distribution shifts.
* Implementation details for PPO are extensively discussed, revealing critical factors for achieving optimal performance in RLHF settings. Key techniques identified include advantage normalization, large batch size, and exponential moving average updates for the reference model. These enhancements are shown to significantly improve PPO’s performance across various tasks, including dialogue generation and code generation.
* The study presents a series of experiments benchmarking DPO and PPO across multiple RLHF testbeds, such as the SafeRLHF dataset, HH-RLHF dataset, APPS, and CodeContest datasets. Results indicate that PPO consistently outperforms DPO in all cases, achieving state-of-the-art results in challenging code competition tasks. Specifically, on the CodeContest dataset, a PPO model with 34 billion parameters surpasses the previous state-of-the-art AlphaCode-41B, demonstrating a notable improvement in performance.
* Key experimental findings include:
  1. **Theoretical Analysis**: Demonstrates that DPO can produce biased policies due to out-of-distribution exploitation, while PPO’s regularization via KL divergence helps mitigate this issue.
  2. **Synthetic Scenario Validation**: Illustrates DPO’s susceptibility to generating biased distributions favoring unseen responses, while PPO maintains more stable performance.
  3. **Real Preference Datasets**: Shows that DPO’s performance can be improved by addressing distribution shifts through additional supervised fine-tuning (SFT) and iterative training, though PPO still outperforms DPO significantly.
  4. **Ablation Studies for PPO**: Highlights the importance of advantage normalization, large batch sizes, and exponential moving average updates in enhancing PPO’s RLHF performance.
* The authors conclude that while DPO offers a simpler training procedure, its performance is hindered by sensitivity to distribution shifts and out-of-distribution data. PPO, with proper tuning and implementation enhancements, demonstrates robust effectiveness and achieves superior results across diverse RLHF tasks.
* In summary, the comprehensive analysis and empirical evidence provided in this paper establish PPO as a more reliable and effective method for LLM alignment compared to DPO, particularly in scenarios requiring high-performance and robust alignment with human preferences.

#### [Pairwise Proximal Policy Optimization: Harnessing Relative Feedback for LLM Alignment](https://arxiv.org/abs/2310.00212)

* This paper by Wu et al. from UC Berkeley proposes a novel RL framework, Pairwise Proximal Policy Optimization (P3O), designed to optimize LLMs using comparative feedback rather than absolute rewards. Traditional approaches such as Proximal Policy Optimization (PPO) have limitations when dealing with reward functions derived from comparative losses like the Bradley-Terry loss. These limitations include the necessity for reward normalization and token-wise updates, which introduce complexity and potential instability.
* The proposed P3O algorithm operates on trajectory-wise policy gradient updates, simplifying the optimization process by directly utilizing comparative rewards. This approach is invariant to equivalent reward functions, addressing the instability issues present in PPO. The paper presents a comprehensive theoretical foundation, establishing that P3O avoids the complications of value function approximation and [Generalized Advantage Estimation (GAE)](#generalized-advantage-estimation-gae), which are essential in PPO.
* The implementation of P3O involves the following key steps:
  1. **Initialization**: Policy parameters are initialized.
  2. **Data Collection**: Pairwise trajectories are collected by running the policy on a batch of prompts, generating two responses per prompt.
  3. **Reward Calculation**: Trajectory-wise rewards are computed, incorporating both the preference-based reward and the KL-divergence penalty from the supervised fine-tuning (SFT) model.
  4. **Gradient Estimation**: The policy gradient is estimated using the relative differences in rewards between the paired responses, adjusted by importance sampling to account for the policy change.
  5. **Policy Update**: Gradient updates are applied to the policy parameters, following either separate or joint clipping strategies to maintain stability.
* The figure below from the paper illustrates the prevalent method for fine-tuning LMs using RL, which relies on Absolute Feedback. In this paradigm, algorithms like PPO has to learn a \(V\) function, which capture not only the valuable relative preference information, but also less part, which is the scale of the reward for a given prompt. Contrastingly, the figure on the right presents paradigm for optimizing reward model trained via comparative loss, e.g., Bradley-Terry Loss (Bradley & Terry, 1952). P3O generates a pair of responses per prompt, leveraging only the Relative Feedback - derived from the difference in reward - for policy gradient updates. This method obviates the need for additional \(V\) function approximations and intricate components like GAE.

* Empirical evaluations are conducted on summarization and question-answering tasks using datasets like TL;DR and Anthropic’s Helpful and Harmless (HH). The results demonstrate that P3O achieves a superior trade-off between reward and KL-divergence compared to PPO and other baseline methods. Specifically, P3O shows improved alignment with human preferences, as evidenced by higher rewards and better performance in head-to-head comparisons evaluated by GPT-4.
* The experiments reveal that P3O not only achieves higher reward scores but also maintains better KL control, making it a robust alternative for fine-tuning LLMs with relative feedback. The study underscores the potential of P3O in simplifying the RL fine-tuning process while enhancing model alignment with human values. Future work aims to explore the impacts of reward over-optimization and extend the policy gradient framework to accommodate multiple ranked responses.

#### [BPO: Supercharging Online Preference Learning by Adhering to the Proximity of Behavior LLM](https://arxiv.org/abs/2406.12168)

* This paper by Xu et al. from UCSB and CMU presents Behavior Preference Optimization (BPO), a novel approach to enhancing online preference learning for LLMs by maintaining proximity to the behavior LLM that collects training samples. The key motivation is to address the limitations of traditional Direct Alignment from Preferences (DAP) methods, which do not fully exploit the potential of online training data.
* The authors propose a new online DAP algorithm, emphasizing the construction of a trust region around the behavior LLM (\(\pi\_{\beta}\)) rather than a fixed reference model (\(\pi\_{ref}\)). This approach ensures that the learning LLM (\(\pi\_{\theta}\)) remains aligned with the behavior model, thereby stabilizing the training process and improving performance.
* **Implementation Details:**
  1. **Algorithm Overview**:
     + The BPO algorithm dynamically updates \(\pi\_{\beta}\) with \(\pi\_{\theta}\) every K steps, where K is the annotation interval calculated as T/F (total training steps divided by the preference annotation frequency).
     + The training loss \(L\_{BPO}\) is computed by constraining the KL divergence between \(\pi\_{\theta}\) and \(\pi\_{\beta}\), thus constructing a trust region around the behavior LLM.
  2. **Ensemble of LoRA Weights**:
     + To mitigate training instability, the authors optimize an ensemble of Low-Rank Adaptation (LoRA) weights and merge them during inference without additional overhead. This ensemble approach stabilizes the training process.
  3. **Experimental Setup**:
     + The experiments were conducted on three datasets: Reddit TL;DR, Anthropic Helpfulness, and Harmlessness, using a preference simulator for annotation.
     + BPO was integrated with various DAP methods, including DPO, IPO, and SLiC, and compared against their online and offline counterparts.
* The figure below from the paper illustrates an overview of the training pipeline of our BPO. Our training loss LBPO is calculated by constraining the KL divergence between \(\pi\_{\theta}\) and the behavior LLM \(\pi\_{\beta}\). Every \(K\) steps, they update \(\pi\_{\beta}\) with \(\pi\_{\theta}\) and use it to collect new samples for annotations.

* **Experimental Details:**
  + **Preference Annotation Frequency**:
    - Different annotation frequencies were tested, demonstrating that even a small increase in frequency (F = 2) significantly improves performance over offline DPO, achieving notable gains in win rates against reference texts.
  + **Ablation Study**:
    - The authors performed an ablation study to verify that the performance improvement stems from the better trust region constructed around \(\pi\_{\beta}\), not just the higher quality of \(\pi\_{\beta}\) compared to \(\pi\_{\ref}\).
  + **Stabilization Techniques**:
    - The use of an ensemble of LoRA weights proved effective in stabilizing training, as single LoRA weight optimization led to rapid deterioration of performance.
* **Results:**
  + BPO significantly outperformed both its on-policy and offline DAP counterparts across all tasks, particularly on TL;DR, Helpfulness, and Harmlessness, demonstrating its strong generalizability.
  + The dynamic trust region around the behavior LLM ensured better alignment and stability during training, leading to higher win rates and more consistent performance improvements.
* The proposed BPO method offers a substantial advancement in online preference learning for LLMs, balancing performance and computational efficiency, and demonstrating remarkable applicability to various DAP methods and annotation frequencies.

#### [SimPO: Simple Preference Optimization with a Reference-Free Reward](https://arxiv.org/abs/2405.14734)

* This paper by Meng et al. from Danqi Chen’s lab at Princeton proposes SimPO, a novel offline preference optimization algorithm that simplifies and improves upon Direct Preference Optimization (DPO). Unlike DPO, which requires a reference model and can be computationally intensive, SimPO introduces a reference-free reward that aligns more closely with the model generation process.
* SimPO uses the average log probability of a sequence as the implicit reward, which better aligns with model generation metrics and removes the need for a reference model. This reward formulation enhances computational efficiency and memory usage. Additionally, SimPO incorporates a target reward margin into the Bradley-Terry objective to create a larger separation between winning and losing responses, further optimizing performance.
* The authors conducted extensive evaluations using various state-of-the-art models, including base and instruction-tuned models like Mistral and Llama3. They tested SimPO on benchmarks such as AlpacaEval 2, MT-Bench, and Arena-Hard, demonstrating significant performance improvements over DPO. Specifically, SimPO outperformed DPO by up to 6.4 points on AlpacaEval 2 and 7.5 points on Arena-Hard, with minimal increase in response length, indicating efficiency in length exploitation.
* The figure below from the paper illustrates that SimPO and DPO mainly differ in their reward formulation, as indicated in the shaded box.

* **Implementation Details:**
  1. **Reward Formulation**:
     + SimPO calculates the reward as the average log probability of all tokens in a response using the policy model, normalized by the response length. This formulation eliminates the reference model, making SimPO more efficient.
     + The reward equation is: \(r\_{\text{SimPO}}(x, y) = \frac{\beta}{\mid y\mid } \log \pi\_{\theta}(y \mid x) = \frac{\beta}{\mid y\mid } \sum\_{i=1}^{\mid y\mid } \log \pi\_{\theta}(y\_i \mid x, y\_{<i})\), where \(\beta\) controls reward scaling.
  2. **Target Reward Margin**:
     + A margin \(\gamma\) is introduced to the Bradley-Terry model to ensure a minimum reward difference between winning and losing responses.
     + The modified objective is: \(L\_{\text{SimPO}}(\pi\_{\theta}) = -E\_{(x, y\_w, y\_l) \sim D} \left[ \log \sigma \left(\frac{\beta}{\mid y\_w\mid } \log \pi\_{\theta}(y\_w \mid x) - \frac{\beta}{\mid y\_l\mid } \log \pi\_{\theta}(y\_l \mid x) - \gamma \right) \right]\).
  3. **Training Setups**:
     + **Base Setup**: Models were trained on the UltraChat-200k dataset to create a supervised fine-tuned (SFT) model, followed by preference optimization using the UltraFeedback dataset.
     + **Instruct Setup**: Off-the-shelf instruction-tuned models were used, regenerating chosen and rejected response pairs to mitigate distribution shifts.
  4. **Evaluation**:
     + SimPO was evaluated on AlpacaEval 2, Arena-Hard, and MT-Bench benchmarks. Performance was measured in terms of length-controlled win rate and raw win rate.
     + SimPO achieved notable results, such as a 44.7% length-controlled win rate on AlpacaEval 2 and a 33.8% win rate on Arena-Hard, making it the strongest 8B open-source model.
  5. **Hyperparameters**:
     + Optimal performance was achieved with \(\beta\) set between 2.0 and 2.5, and \(\gamma\) between 0.5 and 1.5.
* SimPO demonstrates a significant advancement in preference optimization, simplifying the process while improving computational efficiency and performance on multiple benchmarks. The removal of the reference model and the alignment of the reward function with generation metrics are key innovations that contribute to its success.
* [Code](https://github.com/princeton-nlp/SimPO)

#### [Discovering Preference Optimization Algorithms with and for Large Language Models](https://arxiv.org/abs/2406.08414)

* This paper by Chris Lu et al. from Sakana AI, University of Cambridge, and FLAIR, presents a novel approach to offline preference optimization for LLMs by leveraging LLM-driven objective discovery. Traditional preference optimization relies on manually-crafted convex loss functions, but this approach is limited by human creativity. The authors propose an iterative method that prompts an LLM to discover new preference optimization loss functions automatically, leading to the development of state-of-the-art algorithms without human intervention.
* The core contribution of this paper is the introduction of the Discovered Preference Optimization (DiscoPOP) algorithm, which adaptively combines logistic and exponential losses. This process is facilitated through an LLM-driven pipeline that iteratively proposes and evaluates new loss functions based on their performance on downstream tasks.
* **Implementation Details:**
  1. **Initial Context Construction:** The system prompt initializes the LLM with several established objective functions in code and their performance metrics.
  2. **LLM Querying and Output Validation:** The LLM is queried to propose new objective functions, which are parsed, validated through unit tests, and evaluated.
  3. **Performance Evaluation:** The proposed objective functions are evaluated based on their ability to optimize a model on predefined downstream tasks, with the performance metric feeding back into the LLM.
  4. **Iterative Refinement:** The LLM iteratively refines its proposals, synthesizing new candidate loss functions that blend successful aspects of previous formulations.
* **Discovery Process:**
  + The LLM generates PyTorch-based candidate objective functions, taking log probabilities of preferred and rejected completions as inputs.
  + Valid candidates are used to fine-tune an LLM, evaluated using performance metrics such as MT-Bench scores.
  + The performance data is fed back into the LLM, which iteratively refines its generation strategy based on this feedback.
* The figure below from the paper illustrates: (Left) Conceptual illustration of LLM-driven discovery of objective functions. We prompt an LLM to output new code-level implementations of offline preference optimization losses \(\mathbb{E}\_{\left(y\_w, y\_l, x\right) \sim \mathcal{D}}[f(\beta \rho)]\) as a function of the policy \(\left(\pi\_\theta\right)\) and reference model’s \(\left(\pi\_{\text {ref }}\right)\) likelihoods of the chosen \(\left(y\_{w}\right)\) and rejected \(\left(y\_{l}\right)\) completions. Afterward, they run an inner loop training procedure and evaluate the resulting model on MT-Bench. The corresponding performance is fed back to the language model, and they query it for the next candidate. (Right) Performance of discovered objective functions on Alpaca Eval.

* **Results:**
  + The DiscoPOP algorithm, a dynamically weighted sum of logistic and exponential losses, emerged as a top performer. It was evaluated on multi-turn dialogue tasks (MT-Bench), single-turn dialogue tasks (Alpaca Eval 2.0), summarization tasks (TL;DR), and positive sentiment generation tasks (IMDb).
  + DiscoPOP showed significant improvement in win rates against GPT-4 and performed competitively on various held-out tasks, demonstrating robustness and adaptability across different preference optimization challenges.
* **Technical Details:**
  + The DiscoPOP loss function is non-convex, incorporating a temperature parameter to balance between logistic and exponential terms based on the log-ratio difference (\(\rho\)). This dynamic weighting allows the function to handle both large and small differences effectively, contributing to its superior performance.
* **Significance:**
  + This LLM-driven discovery approach eliminates the constraints of human creativity in designing loss functions, automating the generation of high-performing preference optimization algorithms.
  + The iterative refinement process ensures continuous improvement and adaptability, leading to state-of-the-art performance in preference alignment tasks.
* This work opens new avenues for automated discovery and optimization in machine learning, showcasing the potential of leveraging LLMs to enhance and innovate traditional methodologies in a scalable and efficient manner. The proposed DiscoPOP algorithm represents a significant advancement in offline preference optimization, offering a robust and flexible solution for aligning LLM outputs with human preferences.
* [Code](https://github.com/luchris429/DiscoPOP)

#### [Anchored Preference Optimization and Contrastive Revisions: Addressing Underspecification in Alignment](https://arxiv.org/abs/2408.06266v5)

* This paper by D’Oosterlinck et al. from Ghent University, Stanford University, and Contextual AI introduces methods to improve alignment in LLMs by addressing two core issues: the suboptimal contrastive nature of preference data and the limitations of alignment objectives. The authors propose Contrastive Learning from AI Revisions (CLAIR) and Anchored Preference Optimization (APO) to enhance the clarity of preference signals and the stability of alignment training.
* CLAIR creates minimally contrasting preference pairs by revising lower-quality outputs generated by the target model. Instead of using a judge to pick between outputs, CLAIR employs a reviser (a stronger model such as GPT4-turbo) to minimally improve the weaker output, ensuring that the contrast between outputs is clear and targeted. This leads to more precise preference data compared to conventional methods where preference pairs might vary due to uncontrolled differences. Empirical results show that CLAIR generates the best contrastive data, as measured by token-level Jaccard similarity and character-level Levenshtein edit distance, outperforming on-policy and off-policy judge datasets.
* The figure below from the paper illustrates that alignment is underspecified with regard to preferences and training objective. A: Preference pairs can vary along irrelevant aspects, Contrastive Learning from AI Revisions (CLAIR) creates a targeted preference signal instead. B: The quality of the model can impact alignment training, Anchored Preference Optimization (APO) explicitly accounts for this.

* The figure below from the paper illustrates an answer produced by Llama-3-8B-Instruct for a prompt, and corresponding GPT4-turbo revision of this answer. The differences between answer and revision are highlighted. The revision generally follows the same outline as the answer but improves it where possible. For example, the revision correctly alters the count of Parisian restaurants from 2 to 3 in the second line of the answer.

* APO is a family of contrastive alignment objectives that explicitly consider the relationship between the model and the preference data. The authors propose two key variants: APO-zero and APO-down. APO-zero is used when winning outputs are better than the model’s outputs, ensuring that the likelihood of winning outputs increases and that of losing outputs decreases. APO-down is preferred when the model is already superior to the winning outputs, decreasing the likelihood of both but decreasing the likelihood of the losing output more sharply. APO provides more fine-grained control compared to widely used objectives such as Direct Preference Optimization (DPO), avoiding scenarios where increasing the likelihood of a winning output can degrade model performance.
* The authors conducted experiments aligning Llama-3-8B-Instruct on 32K CLAIR-generated preference pairs and comparable datasets using several alignment objectives. The results demonstrated that CLAIR, combined with APO, led to a significant improvement in performance, closing the gap between Llama-3-8B-Instruct and GPT4-turbo by 45% on the MixEval-Hard benchmark. The best model improved by 7.65% over the base Llama-3-8B-Instruct, primarily driven by the improved contrastiveness of CLAIR-generated data and the tailored dynamics of APO. In comparison, other alignment objectives like DPO and KTO did not perform as well, with DPO showing a tendency to degrade the model due to its ambiguous handling of winning and losing likelihoods.
* CLAIR and APO offer a more stable and controllable approach to alignment by improving the precision of preference signals and ensuring that training dynamics are better suited to the model and data relationship. The experiments also underscore the importance of controlling contrastiveness in preference datasets and adapting the alignment objective to the specific needs of the model.
* The paper concludes with discussions on how these methods compare to other alignment efforts like RL from AI Feedback (RLAIF) and Direct Preference Optimization (DPO), highlighting how CLAIR and APO address the challenges of underspecification in alignment.

#### [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)

* This paper by Shao et al. from DeepSeek-AI, Tsinghua University, and Peking University, introduces the DeepSeekMath 7B model, a state-of-the-art domain-specific language model optimized for mathematical reasoning, achieving results comparable to GPT-4 and Gemini-Ultra on mathematical benchmarks. Below is a detailed summary:
* DeepSeekMath 7B showcases the effectiveness of domain-specific pre-training and innovative RL techniques for advancing mathematical reasoning in open-source language models. Its contributions in data curation, RL algorithms, and multilingual capability serve as a foundation for future research in this domain.
* **Core Contributions**:

  1. **Domain-Specific Training:**
     + DeepSeekMath 7B is pre-trained using 120B tokens sourced from a newly developed DeepSeekMath Corpus, extracted and refined from Common Crawl data. The corpus is seven times larger than Minerva’s and nine times the size of OpenWebMath.
     + Pre-training incorporates natural language, code, and math-specific data for comprehensive reasoning capabilities.
  2. **Key Model Innovations:**
     + **Group Relative Policy Optimization (GRPO):** A novel RL technique designed to optimize the model’s reasoning while reducing memory consumption by bypassing the need for a critic model in RL frameworks like PPO.
     + Instruction tuning with Chain-of-Thought (CoT), Program-of-Thought (PoT), and tool-integrated reasoning datasets to enhance mathematical understanding.
* **Model Development and Implementation**:

  1. **Pre-training Pipeline:**
     + Base model: DeepSeek-Coder-Base-v1.5 7B, extended with 500B tokens. The corpus composition includes:
       - 56% from the DeepSeekMath Corpus.
       - 20% GitHub code.
       - 10% arXiv papers.
       - 10% natural language data from Common Crawl.
  2. **Data Selection and Processing:**
     + The DeepSeekMath Corpus was curated using an iterative pipeline involving fastText-based classification to filter high-quality mathematical content. The dataset was decontaminated to exclude overlap with evaluation benchmarks like GSM8K and MATH.
     + The plot below from the paper illustrates an iterative pipeline that collects mathematical web pages from Common Crawl.
  3. **Mathematical Instruction Tuning:**
     + Fine-tuning on 776K examples (English and Chinese datasets), leveraging CoT, PoT, and Python-based reasoning for diverse mathematical fields such as algebra, calculus, and geometry.
  4. **RL with GRPO:**
     + GRPO uses group scores as baselines, simplifying reward estimation and computational complexity.
     + The plot below from the paper illustrates PPO and the proposed GRPO. GRPO foregoes the value model, instead estimating the baseline from group scores, significantly reducing training resources.
     + RL training focused on GSM8K and MATH benchmarks with chain-of-thought prompts, achieving a 6-9% improvement over instruction-tuned models.
* **Key Results**:

  1. **Mathematical Reasoning:**
     + Achieved 51.7% accuracy on the MATH benchmark, surpassing all open-source models up to 70B size and approaching GPT-4 levels.
     + Demonstrated superior results across English and Chinese benchmarks like GSM8K (88.2%) and CMATH (88.8%).
  2. **Tool-Aided Problem Solving:**
     + Using Python for problem-solving, DeepSeekMath 7B outperformed the prior state-of-the-art Llemma 34B on benchmarks like GSM8K+Python and MATH+Python.
  3. **General Capabilities:**
     + Improvements in general reasoning and understanding benchmarks like MMLU (54.9%) and BBH (59.5%), as well as coding tasks like HumanEval and MBPP.
* **Observations and Insights**:

  1. **Code Training Benefits:**
     + Pre-training with code improves mathematical reasoning, both with and without tool use.
     + Mixed code and math training synergize mathematical problem-solving and coding performance.
  2. **ArXiv Data Limitations:**
     + Training on arXiv papers alone did not significantly enhance reasoning, suggesting potential issues with the data’s format or relevance.
  3. **RL Efficiency:**
     + GRPO efficiently improves instruction-tuned models with fewer computational resources compared to PPO, setting a new benchmark in LLM RL techniques.

#### [Understanding R1-Zero-Like Training: A Critical Perspective](https://arxiv.org/abs/2503.20783)

* This paper by Liu et al. from Sea AI Lab, National University of Singapore, and Singapore Management University critically analyzes the R1-Zero training paradigm—where reinforcement learning (RL) is applied directly to base LLMs without supervised fine-tuning (SFT)—as introduced by DeepSeek-R1-Zero. The authors dissect both the characteristics of base models and the optimization biases in the RL component, ultimately proposing refinements that enhance reasoning performance and training efficiency.
* **Architecture and Implementation**:

  + **Training Setup**: The authors use base models such as DeepSeek-V3-Base, Qwen2.5-Math, and Llama-3.2, assessing their readiness for RL by analyzing their behavior on MATH-level questions. Templates significantly affect model behavior; for example, Qwen2.5-Math achieves better performance without templates, suggesting implicit pretraining on concatenated QA pairs.
  + **GRPO vs Dr. GRPO**:

    - **GRPO (Group Relative Policy Optimization)** is a sampling-based RL algorithm that normalizes token-level policy gradients based on response length and intra-group standard deviation. This introduces two biases:

      * **Length Bias**: Incorrect longer answers are less penalized, skewing output length growth.
      * **Difficulty Bias**: Questions with low variance disproportionately influence learning.
    - **Dr. GRPO (Done Right GRPO)** removes these normalization factors, yielding an unbiased surrogate objective aligned with standard PPO:
      \(J\_{\text{Dr.GRPO}}(\pi\_\theta) = \mathbb{E}\_{q\sim p\_Q, o\sim \pi\_{\theta}^{\text{old}}} \left[ \sum\_t \min\left(\frac{\pi\_\theta(o\_t|q, o\_{<t})}{\pi\_\theta^{\text{old}}(o\_t|q, o\_{<t})} \hat{A}\_t,\,\text{clip}(\cdot) \hat{A}\_t \right) \right]\)
    - Advantage is computed as:
      \(\hat{A}\_i = R(q, o\_i) - \text{mean}(\{R(q, o\_j)\}\_{j=1}^G)\)
      avoiding per-response and per-question normalization.
  + **Training and Evaluation**:

    - **Data**: MATH training set and diverse question sets (e.g., GSM-8K, ASDiv).
    - **Models**: Trained on 8×A100 GPUs for ~27 hours.
    - **Reward Function**: Binary, based on correctness of final answer via Math-Verify.
    - **Implementation**: Built on the Oat RL framework.
  + **Minimalist R1-Zero Recipe**:

    - Using Qwen2.5-Math-7B with Dr. GRPO and the Qwen-Math template on MATH level 3–5 questions, the model achieves 43.3% accuracy on AIME 2024—state-of-the-art among 7B models.
  + The following figure from the paper shows Dr. GRPO introduces simple yet significant modifications to address the biases in GRPO (Shao et al., 2024), by removing the length and std normalization terms. Right: Our unbiased optimizer effectively prevents the model from generating progressively longer incorrect responses, thereby enhancing token efficiency.
* **Core Insights**:

  + **Base Model Analysis**:

    - Qwen2.5 models outperform others even without prompt templates, possibly due to pretraining on concatenated QA data.
    - DeepSeek-V3-Base is shown to exhibit “Aha moments” (emergent reasoning and self-reflection) even without RL, challenging the notion that RL alone induces these behaviors.
  + **Template Effects**:

    - Templates can disrupt or aid initial policy performance; Qwen2.5-Math models perform worse with templates unless retrained.
    - RL can recover from poor initialization, but optimal performance is achieved with good model-template alignment.
  + **Question Set Coverage**:

    - Broader question sets (e.g., ORZ-57K) enhance generalization.
    - Surprisingly, training on simpler, out-of-domain questions (GSM-8K) still improves performance on harder benchmarks.
  + **Pretraining Effects**:

    - Math pretraining (FineMath, NuminaQA) on Llama-3.2-3B significantly boosts its RL ceiling.
    - Pretraining on concatenated QA texts helps mimic the implicit biases seen in Qwen2.5.
* [Code](https://github.com/sail-sg/understand-r1-zero)

#### [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)

* This paper by Yu et al. from ByteDance Seed, Tsinghua AIR, and The University of Hong Kong introduces DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization), a large-scale reinforcement learning (RL) system for reasoning-capable LLMs. The system is notable for its fully open-source status, including code, algorithm, and datasets, and demonstrates superior performance on AIME 2024 benchmarks using only 50% of the training steps required by previous state-of-the-art methods.
* The central objective is to resolve key reproducibility and scalability challenges in RL training for LLMs by introducing an openly detailed and empirically validated RL pipeline that enhances training stability, sample efficiency, and policy expressiveness.
* **Architecture and Implementation**:

  + **Base Model**: Qwen2.5-32B pretrained transformer.
  + **RL Framework**: Built on top of the `verl` framework, leveraging the Group Relative Policy Optimization (GRPO) method as a foundation.
  + **DAPO Algorithm**:

    - The policy is optimized using a modified objective function as follows:\[\mathcal{J}\_{\text{DAPO}}(\theta) = \mathbb{E}\_{(q,a) \sim D, \{o\_i\}\_{i=1}^G \sim \pi\_{\theta\_{\text{old}}}(\cdot|q)} \left[ \frac{1}{\sum\_{i=1}^G |o\_i|} \sum\_{i=1}^G \sum\_{t=1}^{|o\_i|} \min \left(r\_{i,t}(\theta) \hat{A}\_{i,t},\,\text{clip}(r\_{i,t}(\theta), 1 - \epsilon\_{\text{low}}, 1 + \epsilon\_{\text{high}}) \hat{A}\_{i,t} \right) \right]\]
    - subject to:\[0 < \left| \left\{ o\_i \mid \text{is\\_equivalent}(a, o\_i) \right\} \right| < G\]
    - where:\[r\_{i,t}(\theta) = \frac{\pi\_\theta(o\_{i,t} \mid q, o\_{i,<t})}{\pi\_{\theta\_{\text{old}}}(o\_{i,t} \mid q, o\_{i,<t})}, \quad
    \hat{A}\_{i,t} = \frac{R\_i - \text{mean}(\{R\_i\}\_{i=1}^G)}{\text{std}(\{R\_i\}\_{i=1}^G)}\]
  + This modified objective function:
    - Applies token-level gradient updates rather than sequence-level.
    - Uses decoupled clipping thresholds \(\epsilon\_{\text{low}}\) and \(\epsilon\_{\text{high}}\) to avoid entropy collapse and preserve exploration.
    - Implements rule-based binary reward: +1 if model output is semantically correct, −1 otherwise.
    - Filters out trivial samples with 0% or 100% accuracy to maintain effective gradient signals via Dynamic Sampling.
  + **Training Details**:

    - Batch Size: 512 prompts × 16 samples per prompt per rollout.
    - Learning Rate: 1e-6 with AdamW and linear warm-up.
    - Token Cap: Maximum of 20,480 tokens (16,384 + 4,096 soft penalty buffer).
    - Reward Shaping: Uses Soft Overlong Punishment to penalize excessively long generations gradually.
    - Evaluation: avg@32 accuracy on AIME 2024 benchmark with temperature 1.0 and top-\(p\) 0.7.
* **Core Innovations**:

  + **Clip-Higher**: Uses asymmetric clipping thresholds to allow low-probability “exploration” tokens more opportunity to increase probability, thereby maintaining model entropy and avoiding convergence to deterministic outputs too early.
  + **Dynamic Sampling**: Filters out samples that are either all correct or all incorrect to avoid zero-gradient contributions, ensuring each training batch contains impactful learning signals.
  + **Token-Level Loss**: Enhances model learning on longer CoT sequences by ensuring each token contributes to the final gradient, preventing the dilution of signal in longer responses and mitigating response quality degradation.
  + **Overlong Reward Shaping**: Truncated responses are masked during training or penalized softly based on the degree of overflow, avoiding abrupt and misleading penalties that may disrupt learning.
  + **Data Curation**: Introduces DAPO-Math-17K, a dataset of math problems with integer-only answers to ensure deterministic and error-free evaluation. Problem statements are transformed to yield integer solutions even for originally fractional outputs.
* **Benchmarks and Results**:

  + DAPO achieves **50% accuracy on AIME 2024** with Qwen2.5-32B, outperforming DeepSeek-R1-Zero-Qwen-32B (47%) with only **50% of training steps**.
  + Ablation studies show cumulative performance gains with each added technique:

    - Naive GRPO: 30%
    - * Overlong Filtering: 36%
    - * Clip-Higher: 38%
    - * Soft Overlong Punishment: 41%
    - * Token-level Loss: 42%
    - * Dynamic Sampling (full DAPO): 50%
* **Empirical Insights**:

  + Monitoring metrics like response length, entropy, and average reward revealed strong correlations with training dynamics and highlighted the need for fine-tuned balancing between exploration and exploitation.
  + Case studies demonstrate the emergence of new reasoning behaviors during training, including reflection and self-correction patterns that were initially absent.
* [Project Page](https://dapo-sia.github.io); [Code](https://github.com/volcengine/verl)

## Further Reading

#### HuggingFace’s Alignment Handbook

* [The Alignment Handbook](https://github.com/huggingface/alignment-handbook) contains robust recipes to align language models with human and AI preferences. It also contains code to train your very own Zephyr models:
  + Full fine-tuning with Microsoft’s DeepSpeed ZeRO-3 on A100s
  + LoRA or QLoRA fine-tuning on consumer GPUs

* Dataset from HuggingFace called [No Robots](https://huggingface.co/datasets/HuggingFaceH4/no_robots) of 10k instructions and demonstrations to train instruct models. This is based on the SFT dataset from OpenAI’s InstructGPT paper. 100% organic and written entirely by skilled human annotators.

#### Empirical Evaluation: DPO vs. IPO vs. KTO

* [Preference Tuning LLMs with Direct Preference Optimization Methods](https://huggingface.co/blog/pref-tuning) by Hugging Face summarizes their extensive evaluation of three state of the art alignment algorithms. DPO vs IPO vs KTO.
* The results demonstrate a complex interaction between key hyper-parameters, models, and datasets. As a quick overview:
  + DPO: Casts the RLHF objective via a loss based on a prompt and its positive and negative completions
  + IPO: Has an identity function rather than DPO’s sigmoid that can potentially cause overfitting
  + KTO: Rather than paired (+ve, -ve) pairs, takes unpaired good and bad (binary preference; thumbs-up and thumbs-down) data
* The team conducted experiments on two models possessing 7B parameters each; namely, Zephyr-7b-beta-sft and OpenHermes-7B. Subsequently, preference fine-tuning was applied utilizing two widely recognized preference datasets: Ultrafeedback and Intel’s Orca DPO pairs. It is pertinent to note that all the associated code is accessible as open-source at [The Alignment Handbook](https://github.com/huggingface/alignment-handbook).
* This investigation aims to discern the influence of the beta parameter on model performance. To this end, the MT Bench, a multi-turn benchmark employing GPT-4 to assess model efficacy across eight distinct categories, was utilized. Despite its limitations, MT Bench serves as a viable instrument for evaluating the capabilities of conversational LLMs.
* In the case of the Zephyr model, it was determined that optimal performance was attained at the minimal beta value of 0.01. This finding was consistent across all three algorithms evaluated, suggesting that a more detailed examination within the beta range of 0.0 to 0.2 could yield valuable insights for the research community.
* Regarding the OpenHermes model, although the relative performance of each algorithm remained consistent - with the ranking being DPO > KTO > IPO - the optimal beta value exhibited significant variation among the algorithms. Specifically, the most favorable beta values for DPO, KTO, and IPO were identified as 0.6, 0.3, and 0.01, respectively.

## FAQs

#### In RLHF, what are the memory requirements of the reward and critic model compared to the policy/reference model?

* In RLHF, you typically have the following models:

  + **Policy model (also called the actor)**
  + **Reference model (frozen copy of the initial policy)**
  + **Reward model (trained from human feedback)**
  + **Critic model (value function)**
* Here’s how their memory requirements generally compare:

  + **Policy vs Reference model**:
    - These are usually the same architecture (e.g., a decoder-only transformer like GPT), so they have roughly equal memory requirements.
    - The reference model is frozen, but still loaded into memory for reward computation (KL divergence term), so it uses as much memory as the policy model.
    - Combined, they double the memory footprint compared to using just one model.
  + **Reward model**:
    - Often has the same architecture as the policy/reference model (e.g., same transformer backbone) but with a small head on top to produce scalar reward values.
    - If it shares weights with the policy/reference model (e.g., using LoRA or other weight-sharing schemes), it can be lighter, but in many setups it’s a full separate copy.
    - Memory requirement: roughly equal to the policy/reference model, possibly slightly less if stripped down or quantized.
  + **Critic model**:
    - In transformer-based PPO, the critic is often implemented as a separate head on the policy model or as a duplicate model with a value head.
    - If separate, it often has the same architecture as the policy but only outputs a scalar value per token.
    - Memory requirement: similar to the policy model, unless heavily optimized (e.g., sharing layers or being much smaller).
* **Summary of memory requirements (relative to one transformer model):**

  + Policy: 1x
  + Reference: 1x
  + Reward: ~1x
  + Critic: ~1x
* **Total:** ~4x the memory of a single model, unless model sharing, quantization, or other tricks are used.

#### Why is the PPO/GRPO objective called a clipped “surrogate” objective?

* The PPO (and its variants such as GRPO) objective is called a surrogate objective because it doesn’t directly optimize the true reinforcement learning objective — the expected rewards over time — but instead optimizes a proxy that is easier and safer to compute. Specifics below:
  + **True RL Objective is Unstable or Intractable:**
    - The actual objective in RL is to maximize expected reward over trajectories, which involves high variance and instability during training, especially for large models like LLMs. It often requires estimating complex quantities like the value function accurately over time, which is difficult in practice.
  + **Surrogate Objectives Improve Stability:**
    - Surrogate objectives simplify this by using:
      * Advantage estimates to approximate how much better a new action is compared to the old one.
      * Importance sampling ratios (like \(\frac{\pi\_{\theta}}{\pi\_{old}}\)) to correct for the shift in policy.
      * Clipping (in PPO and GRPO) to avoid overly large policy updates that might destabilize training.
  + **Practical Optimization Benefits:**
    - By approximating the true objective, surrogate objectives allow for stable and efficient policy updates, which are essential in fine-tuning large models via reinforcement learning.
* In summary, it’s called a surrogate because it’s a well-designed stand-in for the true goal of maximizing reward, tailored to be safer and more effective for gradient-based optimization.

#### Is the importance sampling ratio also called the policy or likelihood ratio?

* Yes, the importance sampling ratio is often referred to as the policy ratio or the likelihood ratio, especially in the context of reinforcement learning algorithms like PPO and GRPO.
* Here’s what these terms mean in this context:
  + **Importance Sampling Ratio:**
    - This is the ratio:

      \[\frac{\pi\_\theta(a \mid s)}{\pi\_{\text{old}}(a \mid s)}\]
      * where \(\pi\_\theta\) is the current (new) policy and \(\pi\_{\text{old}}\) is the old (behavior) policy.
    - It tells us how much more or less likely the new policy is to take action \(a\) in state \(s\) compared to the old one.
  + **Policy Ratio:**
    - This is a shorthand name for the same quantity. It reflects the relative likelihood of an action under the current policy versus the old one — hence, “policy ratio.”
  + **Likelihood Ratio:**
    - Also the same quantity, but phrased from a statistical perspective. It compares the likelihoods assigned by two probability distributions (policies) to the same data (action).
* So, in PPO or GRPO:
  + You’ll often see this ratio appear as something like:\[r\_t(\theta) = \frac{\pi\_\theta(o\_t \mid q, o\_{<t})}{\pi\_{\text{old}}(o\_t \mid q, o\_{<t})}\]
  + And it’s used to weight the advantage, or to apply clipping for stability.
* All three names refer to the same thing — they just come from different angles (importance sampling theory, policy learning, or statistics).

#### Does REINFORCE and TRPO in policy optimization also use a surrogate loss?

* REINFORCE uses a basic form of surrogate loss based on the log-likelihood and returns.
* TRPO uses a more principled surrogate loss that incorporates importance sampling and constraints to ensure safe policy updates.
* Specifics below:
  + **REINFORCE:**
    - REINFORCE is based on the likelihood ratio trick (also called the policy gradient theorem).
    - The loss function used in REINFORCE is:

      \[L(\theta) = \mathbb{E} \left[ \log \pi\_\theta(a|s) \cdot R \right]\]
      * where \(R\) is the return from a trajectory, representing the total discounted reward accumulated from a state onward:

        \[R\_t = \sum\_{k=0}^{\infty} \gamma^k r\_{t+k}\]
      * This captures how good a trajectory is, with future rewards discounted by a factor of \(\gamma\).
    - This is essentially a surrogate for maximizing the expected return, but it’s a very direct one: it’s derived directly from the gradient of the expected return.
    - It doesn’t include constraints or trust region concerns — so while it’s a kind of surrogate loss, it’s very raw and unstable due to high variance.
  + **TRPO (Trust Region Policy Optimization):**
    - TRPO introduces a more sophisticated surrogate objective:

      \[L\_{\theta} = \mathbb{E} \left[ \frac{\pi\_\theta(a \mid s)}{\pi\_{\text{old}}(a \mid s)} \cdot \hat{A}(s, a) \right]\]
      * subject to a constraint on the KL divergence:\[\mathbb{E} \left[ D\_{\text{KL}}\left(\pi\_{\text{old}}(\cdot|s) \, \mid\mid \, \pi\_\theta(\cdot|s) \right) \right] \leq \delta\]
    - The expression \(\frac{\pi\_\theta(a \mid s)}{\pi\_{\text{old}}(a \mid s)} \cdot \hat{A}(s, a)\) is the **surrogate loss** TRPO tries to optimize.
    - This surrogate is designed to estimate the improvement in policy performance, assuming the new policy doesn’t deviate too much from the old one (hence the trust region).
    - The KL constraint ensures stable updates and limits how much the new policy can differ from the old one, helping avoid destructive updates.

#### Does DPO remove both the critic and reward model?

* Yes, DPO removes both the *critic* and the *explicit reward model* present in standard PPO-based RLHF. It replaces them with a closed-form, theoretically equivalent optimization that directly updates the LLM’s parameters using human preference data, without reinforcement learning.
* **In RLHF**:
  + The standard pipeline involves three stages:
    1. Supervised fine-tuning (SFT) on curated data,
    2. Training a *reward model* from human preference pairs, and
    3. Reinforcement learning (e.g., with PPO) to optimize a policy that maximizes this reward.
  + This third step typically requires an *actor–critic* setup:

    - The *critic* estimates the value function or advantage to stabilize training.
    - The *actor* (policy) is updated using gradient estimates of the reward signal.
  + Thus, RLHF relies on both a **reward model** and a **critic** to train the final aligned policy.
* **In DPO:**
  + DPO removes both the explicit reward model and the critic by reparameterizing the RLHF objective in closed form.
  + Starting from the RLHF objective with a KL-divergence constraint:\[\max\_{\pi\_\theta} , \mathbb{E}\_{x \sim D, y \sim \pi\_\theta(y|x)}
  \left[ r\_\phi(x, y) \right] - \beta D\_{\text{KL}} \left[ \pi\_\theta(y|x) \mid\mid \pi\_{\text{ref}}(y|x) \right]\]
  + … the DPO paper derives that the *optimal policy* for a given reward function is\[\pi\_r(y|x) = \frac{1}{Z(x)} , \pi\_{\text{ref}}(y|x) \exp\left(\frac{1}{\beta} r(x, y) \right),\]
  + … and then rearranges this to express the reward in terms of the policy:\[r(x, y) = \beta \log \frac{\pi\_r(y|x)}{\pi\_{\text{ref}}(y|x)} + \beta \log Z(x).\]
  + By substituting this relationship into the *Bradley–Terry* human preference model and cancelling out the partition term, the DPO objective becomes a simple binary cross-entropy loss:\[L\_{\text{DPO}}(\pi\_\theta; \pi\_{\text{ref}})
  = -, \mathbb{E}\_{(x, y\_w, y\_l) \sim D}
  \left[
  \log \sigma \left(
  \beta \log \frac{\pi\_\theta(y\_w|x)}{\pi\_{\text{ref}}(y\_w|x)} - \beta \log \frac{\pi\_\theta(y\_l|x)}{\pi\_{\text{ref}}(y\_l|x)}\right)\right]\]
  + where \((y\_w, y\_l)\) are the preferred and dispreferred completions, and \(\sigma\) is the logistic (sigmoid) function.
  + The aforementioned equation from the paper directly trains the policy to increase the relative likelihood of preferred outputs without any reinforcement learning loop.
* **Takeaways:**
  + Since DPO rewrites the objective starting from the RLHF objective with a KL-divergence constraint, there is **no explicit reward model** — the reward is *implicitly represented* as:\[r(x, y) = \beta \log \frac{\pi\_\theta(y|x)}{\pi\_{\text{ref}}(y|x)}\]
  + There is **no critic network** — no need to estimate advantages or baselines.
  + The entire alignment process becomes a single-stage supervised optimization with a simple cross-entropy loss.

## Further Reading

* [Williams, 1992, “Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning”](https://www.jmlr.org/papers/volume3/williams92a/williams92a.pdf)
* [Schulman et al., 2015, “Trust Region Policy Optimization”](https://arxiv.org/abs/1502.05477)
* [Schulman et al., 2017, “Proximal Policy Optimization Algorithms”](https://arxiv.org/abs/1707.06347)
* [Rafailov et al., 2023, “Direct Preference Optimization: Your Language Model is Secretly a Reward Model”](https://arxiv.org/abs/2305.18290)
* [Ethayarajh et al., 2024, “Kahneman-Tversky Optimization: Aligning AI with Human Biases”](https://arxiv.org/abs/2402.01306)
* [Liu et al., 2023, “Group Relative Policy Optimization: Sample-Efficient Preference Alignment via Grouped Comparisons”](https://arxiv.org/abs/2305.15223)
* [Christiano et al., 2017, “Deep Reinforcement Learning from Human Preferences”](https://arxiv.org/abs/1706.03741)
* [Ouyang et al., 2022, “Training Language Models to Follow Instructions with Human Feedback”](https://arxiv.org/abs/2203.02155)
* [Stiennon et al., 2020, “Learning to Summarize with Human Feedback”](https://arxiv.org/abs/2009.01325)
* [Bai et al., 2022, “Constitutional AI: Harmlessness from AI Feedback”](https://arxiv.org/abs/2212.08073)
* [Touvron et al., 2023, “Llama 2: Open Foundation and Fine-Tuned Chat Models”](https://arxiv.org/abs/2307.09288)
* [Gao et al., 2023, “Scaling Laws for Reward Model Overoptimization”](https://arxiv.org/abs/2306.01890)

## References

* [RL from Human Feedback: From Zero to chatGPT](https://www.youtube.com/watch?v=2MBJOuVq380)
* [Illustrating RLHF](https://huggingface.co/blog/rlhf)
* [Sebastian Raschka’s LinkedIn post](https://www.linkedin.com/in/sebastianraschka?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAxqHaUBEa6zzXN--gv-wd8ih0vevPvr9eU&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3Bic8rQnV%2BTHqwI0K2TXBzzg%3D%3D)
* [Off The Grid’s post on HHH](https://offthegridxp.substack.com/p/what-is-constitutional-ai-harmlessness)
* [Anthropic’s tweet thread](https://twitter.com/AnthropicAI/status/1603791161419698181)
* [Building block’s medium post on CAI](https://medium.com/mlearning-ai/paper-review-constituional-ai-training-llms-using-principles-16c68cfffaef)
* [Unveiling the Hidden Reward System in Language Models: A Dive into DPO](https://allam.vercel.app/post/dpo/)
* [PPO for LLMs: A Guide for Normal People](https://cameronrwolfe.substack.com/p/ppo-llm)

## Citation

```
@article{Chadha2020DistilledPreferenceOptimization,
  title   = {Preference Optimization},
  author  = {Chadha, Aman and Jain, Vinija},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
