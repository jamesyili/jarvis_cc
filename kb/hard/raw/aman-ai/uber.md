# Uber

**Source:** https://aman.ai/h/uber/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [System design:](#system-design)
* [Aman](#aman)
* [Uber Price Optimization System Design](#uber-price-optimization-system-design)
  + [1. Context and Motivation](#1-context-and-motivation)
  + [2. Framing the Learning Problem](#2-framing-the-learning-problem)
  + [3. Data Foundation and Representation](#3-data-foundation-and-representation)
  + [4. Modeling Marketplace Elasticities](#4-modeling-marketplace-elasticities)
  + [5. Predictive Models: Demand and Supply Response](#5-predictive-models-demand-and-supply-response)
    - [5.1 Problem Definition](#51-problem-definition)
    - [5.2 Model Inputs and Outputs](#52-model-inputs-and-outputs)
    - [5.3 Model Architectures](#53-model-architectures)
    - [5.4 Objective Functions and Regularization](#54-objective-functions-and-regularization)
    - [5.5 Model Variants and Design Trade-offs](#55-model-variants-and-design-trade-offs)
  + [6. Generative Augmentation and Simulation Consistency](#6-generative-augmentation-and-simulation-consistency)
  + [7. Model Evaluation and Calibration](#7-model-evaluation-and-calibration)
  + [8. End-to-End Flow](#8-end-to-end-flow)
* [Uber Price Optimization System – End-to-End Architecture Diagram](#uber-price-optimization-system--end-to-end-architecture-diagram)
* [Diagram Walkthrough and Technical Interpretation](#diagram-walkthrough-and-technical-interpretation)
  + [1. Data Plane](#1-data-plane)
  + [2. Predictive Layer](#2-predictive-layer)
  + [3. Reinforcement Learning Layer](#3-reinforcement-learning-layer)
  + [4. Simulator + Offline Training](#4-simulator--offline-training)
  + [5. Safety Projection](#5-safety-projection)
  + [6. Serving Plane](#6-serving-plane)
  + [7. Monitoring + Governance](#7-monitoring--governance)
  + [8. Continuous Feedback and Retraining](#8-continuous-feedback-and-retraining)
* [Why This Architecture Works](#why-this-architecture-works)
* [9. Reinforcement Learning Layer: Dynamic Price Field Control](#9-reinforcement-learning-layer-dynamic-price-field-control)
  + [9.1 CMDP Formulation](#91-cmdp-formulation)
  + [9.2 State Representation and Spatial Hierarchy](#92-state-representation-and-spatial-hierarchy)
  + [9.3 Reward Structure and Causal Attribution](#93-reward-structure-and-causal-attribution)
  + [9.4 Actor–Critic Architecture](#94-actorcritic-architecture)
    - [Actor: UNet + Spatial Attention](#actor-unet--spatial-attention)
    - [Critic: Distributional Value Estimation](#critic-distributional-value-estimation)
  + [9.5 Policy Optimization and Safety Constraints](#95-policy-optimization-and-safety-constraints)
  + [9.6 Alternative Policy Formulations](#96-alternative-policy-formulations)
* [10. Environment Simulator and Counterfactual Replay](#10-environment-simulator-and-counterfactual-replay)
  + [10.1 Simulator Structure](#101-simulator-structure)
  + [10.2 Calibration and Validation](#102-calibration-and-validation)
  + [10.3 Simulation-Augmented Learning](#103-simulation-augmented-learning)
* [11. Constraint Projection and Safety at Inference Time](#11-constraint-projection-and-safety-at-inference-time)
* [12. Policy Evaluation and Deployment within Michelangelo](#12-policy-evaluation-and-deployment-within-michelangelo)
  + [12.1 Offline Evaluation](#121-offline-evaluation)
  + [12.2 Experimentation and Rollout](#122-experimentation-and-rollout)
* [13. Monitoring, Drift Detection, and Governance](#13-monitoring-drift-detection-and-governance)
* [14. System Summary and End-to-End Flow](#14-system-summary-and-end-to-end-flow)
* [15. Infrastructure and Computational Orchestration](#15-infrastructure-and-computational-orchestration)
  + [15.1 Data Plane: Streaming Feature Fabric](#151-data-plane-streaming-feature-fabric)
  + [15.2 Training Plane: Distributed Reinforcement Learning and Simulation](#152-training-plane-distributed-reinforcement-learning-and-simulation)
    - [Cluster Composition](#cluster-composition)
    - [Data Flow](#data-flow)
    - [Training Synchronization](#training-synchronization)
  + [15.3 Simulation-as-a-Service](#153-simulation-as-a-service)
  + [15.4 Model Registry and Versioning](#154-model-registry-and-versioning)
* [16. Serving Plane: Real-Time Inference and Control](#16-serving-plane-real-time-inference-and-control)
  + [16.1 System Topology](#161-system-topology)
  + [16.2 Feature Synchronization](#162-feature-synchronization)
  + [16.3 Latency and Resilience Engineering](#163-latency-and-resilience-engineering)
* [17. Monitoring, Evaluation, and Feedback Loops](#17-monitoring-evaluation-and-feedback-loops)
  + [17.1 Data and Feature Drift Monitoring](#171-data-and-feature-drift-monitoring)
  + [17.2 Behavioral Metrics and Feedback](#172-behavioral-metrics-and-feedback)
  + [17.3 Model Governance and Compliance](#173-model-governance-and-compliance)
* [18. Continuous Learning and Auto-Retraining](#18-continuous-learning-and-auto-retraining)
  + [18.1 Automated Retraining](#181-automated-retraining)
  + [18.2 Human-in-the-Loop Oversight](#182-human-in-the-loop-oversight)
* [19. Computational and Economic Efficiency](#19-computational-and-economic-efficiency)
* [20. End-to-End System Lifecycle](#20-end-to-end-system-lifecycle)
* [21. Closing Perspective](#21-closing-perspective)
* [Uber ETA Optimization System Design](#uber-eta-optimization-system-design)
  + [1. Context and Motivation](#1-context-and-motivation-1)
  + [2. ETA as a Hierarchical Spatio-Temporal Inference Problem](#2-eta-as-a-hierarchical-spatio-temporal-inference-problem)
  + [3. System Overview](#3-system-overview)
  + [4. Data Plane: From Telemetry to Features](#4-data-plane-from-telemetry-to-features)
    - [4.1 Map-Matching and Segmentization](#41-map-matching-and-segmentization)
    - [4.2 Feature Generation](#42-feature-generation)
    - [4.3 Storage and Retrieval](#43-storage-and-retrieval)
  + [5. Segment-Level Model](#5-segment-level-model)
    - [5.1 Input/Output Formalism](#51-inputoutput-formalism)
    - [5.2 Architecture](#52-architecture)
    - [5.3 Objective](#53-objective)
    - [5.4 Bayesian Hierarchy for Sparsity](#54-bayesian-hierarchy-for-sparsity)
  + [6. Route-Level Inference Engine](#6-route-level-inference-engine)
    - [6.1 Correlated Aggregation](#61-correlated-aggregation)
    - [6.2 Risk-Aware Routing Objective](#62-risk-aware-routing-objective)
  + [7. Calibration and Bias Correction](#7-calibration-and-bias-correction)
  + [8. System Infrastructure and Training](#8-system-infrastructure-and-training)
    - [8.1 Distributed Training Cluster](#81-distributed-training-cluster)
    - [8.2 Simulation-based Augmentation](#82-simulation-based-augmentation)
    - [8.3 Continuous Retraining](#83-continuous-retraining)
  + [9. Serving Layer](#9-serving-layer)
    - [9.1 Runtime Topology](#91-runtime-topology)
    - [9.2 Performance and Reliability](#92-performance-and-reliability)
  + [10. Monitoring and Governance](#10-monitoring-and-governance)
    - [10.1 Drift and Calibration Dashboards](#101-drift-and-calibration-dashboards)
    - [10.2 Explainability](#102-explainability)
    - [10.3 Governance](#103-governance)
  + [11. Integration into Marketplace](#11-integration-into-marketplace)
  + [12. End-to-End Feedback Cycle](#12-end-to-end-feedback-cycle)
  + [13. Evaluation Metrics](#13-evaluation-metrics)
  + [14. ASCII Diagram – System Architecture with Michelangelo Integration](#14-ascii-diagram--system-architecture-with-michelangelo-integration)
  + [15. Closing Summary](#15-closing-summary)
* [Unified Pricing–ETA Reinforcement Learning System](#unified-pricingeta-reinforcement-learning-system)
  + [1. Motivation and Problem Context](#1-motivation-and-problem-context)
  + [2. Formalizing the Coupling](#2-formalizing-the-coupling)
  + [3. Why Uncertainty Matters](#3-why-uncertainty-matters)
  + [4. Joint Architecture Overview](#4-joint-architecture-overview)
  + [5. Algorithmic Formulation](#5-algorithmic-formulation)
    - [5.1 Joint Distribution Modeling](#51-joint-distribution-modeling)
    - [5.2 Risk-Aware RL Objective](#52-risk-aware-rl-objective)
    - [5.3 Actor–Critic Update](#53-actorcritic-update)
    - [5.4 Dual Optimization Loop](#54-dual-optimization-loop)
  + [6. Simulator Coupling](#6-simulator-coupling)
  + [7. Theoretical Perspective: Robust and Distributional RL](#7-theoretical-perspective-robust-and-distributional-rl)
    - [7.1 Distributional Value Function](#71-distributional-value-function)
    - [7.2 Robust Control Interpretation](#72-robust-control-interpretation)
  + [8. Engineering Implementation](#8-engineering-implementation)
    - [8.1 Model Interfaces](#81-model-interfaces)
    - [8.2 Training Loop](#82-training-loop)
    - [8.3 Serving-Time Integration](#83-serving-time-integration)
  + [9. Metrics and Evaluation](#9-metrics-and-evaluation)
  + [10. Alternative Architectures and Tradeoffs](#10-alternative-architectures-and-tradeoffs)
  + [11. Intuitive Analogy](#11-intuitive-analogy)
  + [12. Theoretical Summary](#12-theoretical-summary)
  + [13. Deployment and Monitoring](#13-deployment-and-monitoring)
  + [14. Broader System Implications](#14-broader-system-implications)
  + [15. Closing Summary](#15-closing-summary-1)
* [Marketplace Simulation and Joint Training Framework](#marketplace-simulation-and-joint-training-framework)
  + [1. Purpose and Design Philosophy](#1-purpose-and-design-philosophy)
  + [2. Hierarchical Simulation Overview](#2-hierarchical-simulation-overview)
  + [3. Simulation State Representation](#3-simulation-state-representation)
  + [4. Dynamics Model](#4-dynamics-model)
    - [Components:](#components)
  + [5. Agent-Based Simulation Loop](#5-agent-based-simulation-loop)
  + [6. Distributed Rollout Infrastructure](#6-distributed-rollout-infrastructure)
    - [6.1 Parallelism Model](#61-parallelism-model)
    - [6.2 Replay Buffer and Experience Store](#62-replay-buffer-and-experience-store)
  + [7. Model-Based vs. Model-Free Integration](#7-model-based-vs-model-free-integration)
    - [7.1 Model-Based Branch](#71-model-based-branch)
    - [7.2 Model-Free Branch](#72-model-free-branch)
    - [7.3 Hybrid (Dyna-style)](#73-hybrid-dyna-style)
  + [8. Off-Policy Evaluation under Stochastic Dynamics](#8-off-policy-evaluation-under-stochastic-dynamics)
    - [8.1 Problem](#81-problem)
    - [8.2 Importance Sampling with ETA Uncertainty](#82-importance-sampling-with-eta-uncertainty)
    - [8.3 Doubly Robust Formulation](#83-doubly-robust-formulation)
  + [9. Safety-Constrained Training](#9-safety-constrained-training)
  + [10. Calibration and Domain Randomization](#10-calibration-and-domain-randomization)
    - [10.1 Calibration](#101-calibration)
    - [10.2 Domain Randomization](#102-domain-randomization)
  + [11. Training Stability and Curriculum](#11-training-stability-and-curriculum)
  + [12. System Implementation](#12-system-implementation)
    - [12.1 Compute Topology](#121-compute-topology)
    - [12.2 Data Flow](#122-data-flow)
  + [13. Validation Pipeline](#13-validation-pipeline)
  + [14. Monitoring and Diagnostics](#14-monitoring-and-diagnostics)
  + [15. Theoretical Note: Stochastic Model Predictive Control (MPC) View](#15-theoretical-note-stochastic-model-predictive-control-mpc-view)
  + [16. Design Tradeoffs](#16-design-tradeoffs)
  + [17. Intuitive Analogy](#17-intuitive-analogy)
  + [18. Closing Summary](#18-closing-summary)
* [Uber Rider–Driver Matching Optimization System](#uber-riderdriver-matching-optimization-system)
  + [1. Context and Objective](#1-context-and-objective)
  + [2. Problem Formulation: Dynamic Matching as MDP](#2-problem-formulation-dynamic-matching-as-mdp)
  + [3. System Overview](#3-system-overview-1)
  + [4. Data Plane and Feature Space](#4-data-plane-and-feature-space)
    - [4.1 Core Features](#41-core-features)
    - [4.2 Driver State Representation](#42-driver-state-representation)
    - [4.3 Demand Forecasting](#43-demand-forecasting)
  + [5. Candidate Generation](#5-candidate-generation)
  + [6. Utility Scoring Function](#6-utility-scoring-function)
  + [7. Matching Optimization Layer](#7-matching-optimization-layer)
    - [7.1 Deterministic Matching (Assignment Step)](#71-deterministic-matching-assignment-step)
    - [7.2 Stochastic RL Controller (Dynamic Weight Tuning)](#72-stochastic-rl-controller-dynamic-weight-tuning)
  + [8. Simulation Environment](#8-simulation-environment)
  + [9. Losses and Learning Objectives](#9-losses-and-learning-objectives)
  + [10. Serving and Deployment](#10-serving-and-deployment)
    - [10.1 Real-Time Inference Path](#101-real-time-inference-path)
    - [10.2 Michelangelo Deployment Stack](#102-michelangelo-deployment-stack)
  + [11. Monitoring and Feedback](#11-monitoring-and-feedback)
  + [12. ASCII System Architecture Diagram](#12-ascii-system-architecture-diagram)
  + [13. Evaluation Metrics](#13-evaluation-metrics-1)
  + [14. Governance and Safety](#14-governance-and-safety)
  + [15. Closing Summary](#15-closing-summary-2)

## Overview

* basically the same assystem designIt’s a lot like playing at points. Where does the data come from, how to generate positive and negative samples, how to select and generate features, what to use for the model, what to use for the loss, what metrics to use, how to serve the model, how to solve various biases, it’s quite good Routine. If you think about each point and summarize it yourself, you can basically answer it.
* but I was surprised that I didn’t even take the coding test. I asked about a project on my resume, and then there was a question about ML design. I was dumbfounded because I didn’t have any questions at all. To prepare, you can only brainstorm and follow the interviewer step by step. . .
* The group was from Uber Eat and asked about predicting meal preparation time. I was given some order samples
* and then asked how to choose a feature. Anyway, the question was quite detailed. I was unprepared and had no experience in this area. Although I felt okay chatting with my compatriots. . .
* After waiting for more than a week, I received a rejection letter. Hahaha, if the verification fails again, don’t push me. A push is a rejection letter. . . By the way, move on
* , does it have a freezing period? The recruiter said he would contact me in 4-5 months.
* Friends who are preparing for the interview, I took a look at my overall results.
* 1. Project deep dive + design facebook message
     1. Us
     2. Write a UI, a C-shaped diagram composed of small grids
        [][][]
        []
        [][][]
* The user will click on the small grids one by one, click The color will change, and when all the small grids are clicked, they will return to the original color in the order of points.
* I am hardcoding the ui element. In JavaScript, click changes the color of the element and adds an array to record the elementId. After everything is clicked, open a setTimeout and change the color of the cells back according to the instructions in the array.
* follow up: What should I do if the user clicks again during the settimeout that changes the cell color? Answer: First

## System design:

* New Problem. Designing a recommendation order for Uber products is actually the same as search and promotion. I answered it according to the 8-step method on GitHub. In the end, it was too late to finish, so it is best to take a rest. Asked a lot of questions. I was exhausted, but the whole system was explained.
* design a best seller page of amazon.
* ML fundamental + Design an end-to-end ML system to solve how to judge whether payment has signs of fraud.
* I remember the interview with ML System Design about how to make recommendations on the homepage of Uber Eats. For example, as soon as you open the app, there will be personalized recommendations for restaurants or dishes. We discussed how to collect training data, feature engineering, what model to use, and how to test. How to do offline and online testing specifically.
* In the ML breath, I covered some basic ML concepts, and then I was asked to write the k-means algorithm and run test data on site.
* Fortunately, the poster has read the ML part of Google Map’s paper before. First, assume using graph computation to get several candidate routes, and then calculate the ETA for each route using multiple horizons. After dividing the supersegment, then GNN training, and adding the ETA, but Because of the length of the interview, the author did not mention the GNN part. The main focus was on how to extract features, process features, and establish labels and target loss functions. During this period, the interviewer also asked to write the pseudocode during inference.
* Designing an Uber automatic price adjustment system requires both real-time and batch data, as well as designing algorithms and features.
* ML Design, how to design a recommendation system and present activities that can be participated in on the mobile APP. To be honest, I feel that all kinds of ML Design are very routine. I talk about data, loss, feature, model structure, and finally add some data bias and position bias. This time I changed my job and I complained.
* Design a driver/rider match system
* How to design Uber

# Aman

* [RL](https://www.uber.com/en-EG/blog/reinforcement-learning-for-modeling-marketplace-balance/?uclick_id=4af44ce9-429f-4c14-b86b-09fb99af23f8)
* [didi global](https://arxiv.org/pdf/2202.05118)
* [predictive to generative](https://www.uber.com/blog/from-predictive-to-generative-ai/)

# Uber Price Optimization System Design

*A Deep Technical and Mathematical Architecture — Integrated with Michelangelo and Reinforcement Learning for Marketplace Balance*

---

## 1. Context and Motivation

Uber’s marketplace is a **nonlinear control system** characterized by coupled dynamics between demand and supply. Both rider and driver behaviors evolve over space and time, responding to changing prices, estimated arrival times (ETAs), external events, and their own anticipatory expectations.

The **objective** is to learn and deploy a continuously adaptive function \(m\_t(z\) that represents the price multiplier at location \(z\) and time \(t\), computed from a rich state representation \(s\_t(z\). Formally,

\[m\_t(z) = f\_\pi(s\_t(z); \theta),\]

where \(f\_\pi\) is a parameterized policy or control law, implemented as a neural model, that maximizes the expected long-term value function:

\[J(\theta) = \mathbb{E}\_{\pi} \left[ \sum\_{t=0}^\infty \gamma^t (r\_t - \sum\_k \lambda\_k c\_t^k) \right].\]

Here \(r\_t\) denotes instantaneous revenue-related rewards, \(c\_t^k\) represents soft constraints (wait times, fairness measures, volatility metrics), and \(\lambda\_k\) are dual multipliers ensuring safety and service compliance.

Unlike traditional demand–supply equilibrium optimization, Uber’s system operates online, in real time, with latency budgets on the order of tens of milliseconds and non-stationary conditions that shift by the minute. This makes it not just an ML problem, but a **real-time stochastic control problem** supported by an integrated stack of prediction, simulation, and reinforcement learning.

The system’s design is anchored on **Michelangelo**, Uber’s machine learning platform. Michelangelo provides a uniform substrate for data ingestion, feature store synchronization, model training, distributed simulation, and live deployment. It enables end-to-end automation — from feature extraction in streaming pipelines to rollout orchestration and monitoring of reinforcement learning (RL) policies.

---

## 2. Framing the Learning Problem

The marketplace control problem can be framed as a **multi-agent stochastic optimization problem**, where the pricing policy acts as a global controller influencing decentralized agent behavior. The RL policy does not directly manipulate individual transactions; instead, it outputs a **spatiotemporal price field** across the city grid. Each tile \(z\) evolves according to its own local demand–supply balance but is coupled with neighboring tiles via mobility, ETA interactions, and driver repositioning.

In supervised learning terms, we can view each pricing decision as a function approximation problem of the form:

\[\hat{Y} = f(x, m),\]

where \(x\) denotes the feature vector describing contextual state (rider and driver features, environment, time), \(m\) is the current or proposed multiplier, and \(\hat{Y}\) is the expected marketplace outcome — such as trip acceptance rate, demand volume, or driver availability.

However, because changing prices causes feedback that persists over future time steps, the optimization target must integrate *temporal causality* and *uncertainty propagation*. Therefore, the full formulation uses a **hierarchical ML structure**:

1. Predictive models estimate short-term responses and causal derivatives.
2. Hierarchical Bayesian models regularize those predictions across geography and time.
3. Reinforcement learning policies use these calibrated models as components in a longer-horizon control objective.

---

## 3. Data Foundation and Representation

The system relies on an extensive data substrate built from **Uber’s telemetry streams**, which include trip logs, rider app events, driver locations, cancellation and acceptance signals, ETAs, and environmental features such as weather and public events.

Data flows through a **Michelangelo-integrated feature pipeline** composed of streaming feature extraction via **Flink or Spark Structured Streaming**, backed by a dual-layer **Feature Store**. The online store ensures features are updated in near real time (typically <1 second lag), while the offline store allows consistent feature computation for model training and simulation replay.

Each observation corresponds to a tuple of the form:

\[(x\_t^{(r)}, x\_t^{(d)}, c\_t(z), m\_t(z), y\_t),\]

where:

* (x\_t^{(r)}) captures rider-level signals such as price sensitivity, historical trip frequency, device type, and loyalty level.
* (x\_t^{(d)}) encodes driver states including location, trip progress, cumulative earnings gap, and fatigue proxies inferred from session duration.
* (c\_t(z)) represents environmental context features such as time-of-day cyclic encodings, weather conditions, event embeddings, and local congestion level.
* (m\_t(z)) is the applied multiplier.
* (y\_t) are measured outcomes such as trip initiation, driver acceptance, or revenue realized.

To spatially aggregate data, the city is discretized into **geo-tiles** of approximately 250m × 250m. For each tile, features are aggregated over short time windows (e.g., 5-minute buckets) to create a tensor representation \(s\_t(z) \in \mathbb{R}^C\), where \(C\) typically ranges between 30–50 channels.

The resulting dataset thus forms a **spatiotemporal tensor field** evolving under real-time feedback, suitable for learning both local predictive models and global control policies.

---

## 4. Modeling Marketplace Elasticities

A central quantity for any pricing system is the **elasticity surface**, i.e., the local derivative \(\frac{\partial Y}{\partial m}\), capturing how demand or supply reacts to marginal price changes. Empirically, elasticity varies across space and time: dense downtown zones exhibit nearly linear elasticity, while suburban or event-driven zones show nonlinear and discontinuous responses.

Naïvely estimating per-zone elasticities via independent regressions produces noisy, unstable results, especially in low-volume regions. To stabilize these estimates, Uber’s architecture employs **Hierarchical Bayesian Smoothing (HBS)**, which introduces statistical coupling between zones and city-wide priors.

The model assumes:

\[\log D\_{z,t} = \alpha\_z + \beta\_z \log m\_{z,t} + \epsilon\_{z,t},\]

where \(D\_{z,t}\) denotes observed demand in zone \(z\) at time \(t\), \(\alpha\_z\) and \(\beta\_z\) are zone-specific intercept and elasticity parameters, and \(\epsilon\_{z,t}\) captures stochastic noise. These parameters are drawn from higher-level priors representing city or regional means:

\[(\alpha\_z, \beta\_z) \sim \mathcal{N}((\mu\_\alpha, \mu\_\beta), \Sigma\_\text{city}),
\quad
(\mu\_\alpha, \mu\_\beta) \sim \mathcal{N}(\mu\_0, \Sigma\_0).\]

Posterior inference yields **shrinkage estimates**:

\[\hat{\beta}\_z = w\_z \tilde{\beta}\*z + (1 - w\_z)\mu\_{\beta},
\quad
w\_z = \frac{n\_z/\sigma^2}{n\_z/\sigma^2 + 1/\tau^2},\]

where (n\_z) is the local sample count, (\sigma^2) is observation noise variance, and (\tau^2) encodes prior uncertainty.

This formulation ensures that zones with sparse data (e.g., suburban regions) automatically shrink toward global averages, while high-volume zones retain their local identity. The result is a **spatially coherent elasticity field** — smooth yet locally adaptive, critical for preventing discontinuities in surge multipliers across adjacent tiles.

In practice, Uber implements this model via **amortized variational inference** within TensorFlow Probability, integrated into Michelangelo’s online learning service. This enables near real-time posterior updates as new data streams in, without retraining from scratch.

---

## 5. Predictive Models: Demand and Supply Response

### 5.1 Problem Definition

The predictive layer aims to model short-term responses to pricing actions — effectively estimating the local causal effect of changing prices on demand, driver acceptance, and subsequent fulfillment outcomes. This layer operates at a finer temporal granularity than the RL policy, producing features that the control layer uses as input signals.

The task can be expressed as estimating conditional expectations:

\[\begin{aligned}
\hat{Y}\_{\text{demand}} &= \mathbb{E}[Y\_{\text{trip}} | x^{(r)}, c\_t, m],\
\hat{P}\_{\text{accept}} &= \mathbb{E}[\mathbb{1}\_{\text{accept}} | x^{(d)}, c\_t, m, \text{ETA}],\
\hat{V}\_{\text{driver}} &= \mathbb{E}[R\_t + \gamma V\_{t+1} | s\_t^{(d)}].
\end{aligned}\]

### 5.2 Model Inputs and Outputs

Each predictive head receives both *local* and *contextual* embeddings:

* The **rider-demand head** takes contextualized embeddings of price, weather, time, and rider session state, producing a scalar estimate of trip initiation probability.
* The **driver-acceptance head** includes ETA, recent trip rate, and relative earning gap as inputs, predicting a sigmoid probability of acceptance.
* The **driver-value head** outputs a scalar value estimating future cumulative earnings from a given state-action pair, serving as a proxy for opportunity cost.

Outputs from these three heads feed the simulator and RL environment, defining the *forward dynamics* of the system.

### 5.3 Model Architectures

Each head is built atop a **shared spatiotemporal embedding backbone** composed of convolutional layers over the city grid and dilated temporal convolutions to model short-term memory. Spatial adjacency is encoded via graph Laplacian smoothing:

\(h\_z^{(l+1)} = \sigma \left(W\_1 h\_z^{(l)} + \sum\_{u\in N(z)} \frac{W\_2 h\_u^{(l)}}{\sqrt{d\_u d\_z}}\right),\)
where (N(z)) are neighboring zones in the road network and (d\_z) their degree.

This allows information to propagate across zones: an increase in price downtown propagates into neighboring tiles as drivers relocate, preserving consistency between micro-markets.

The demand model specifically enforces **monotonicity** in the price variable, ensuring economic plausibility:

\(\frac{\partial f\_\text{demand}(x,m)}{\partial m} \le 0.\)
This is implemented via **lattice networks** with built-in partial order constraints.

The driver response models use **mixture-density networks** to model multimodal acceptance probabilities and heterogeneous relocation behaviors. Such expressiveness is necessary because drivers’ responses to price depend nonlinearly on their current expected future income trajectories, which vary across individuals and sessions.

### 5.4 Objective Functions and Regularization

The predictive models are trained using composite losses that capture both local accuracy and global causal consistency. The total objective combines cross-entropy or regression losses with structural penalties:

\[\mathcal{L}\*\text{pred} =
\mathcal{L}\*\text{demand}
\* \mathcal{L}\_\text{accept}
\* \mathcal{L}\_\text{value}
\* \lambda\_\text{causal} |\nabla\_m \hat{Y}\_{\text{demand}} + \\1\_{\text{type}}\hat{P}\_\text{accept}|^2.\]

The last term is a causal alignment regularizer ensuring that ETA increases negatively correlate with acceptance probability — an important behavioral constraint derived from empirical Uber research.

### 5.5 Model Variants and Design Trade-offs

Alternative architectures were evaluated, including Graph Neural Networks (GNNs) and Transformers. GNNs offer strong inductive biases for spatial reasoning but tend to have higher inference latency due to graph aggregation operations. Transformers, while expressive, were deemed excessive for the millisecond-scale latency budget.

The chosen hybrid convolutional–attention model achieved the best trade-off: low inference latency, high expressivity, and interpretability. Spatial attention heads allow learning long-range dependencies (e.g., surge propagation between airport and city center), while UNet-like convolutional skip connections maintain local detail.

---

## 6. Generative Augmentation and Simulation Consistency

In low-volume or cold-start regions, the system faces sparse data challenges. Uber’s **Michelangelo Generative Module** — introduced in “From Predictive to Generative: How Michelangelo Accelerates Uber’s AI Journey” — extends predictive modeling into generative simulation.

|  |  |
| --- | --- |
| A conditional diffusion model $$G\_\psi(x | c\_t,z$$ generates synthetic trip contexts consistent with real-world conditional distributions. The generator learns from joint embeddings of weather, events, and demand, producing realistic “what-if” samples for unseen conditions. |

Generated samples are not directly deployed but are used to augment elasticity estimation and improve simulator fidelity. Empirical studies within Uber’s simulation labs showed that this approach reduces the posterior variance of demand elasticity estimates by approximately 30% in sparse regions and leads to smoother spatial surge maps in RL rollouts.

---

## 7. Model Evaluation and Calibration

Predictive models undergo rigorous quantitative and qualitative validation to ensure both statistical fidelity and behavioral realism.

1. **Posterior Predictive Calibration:**
   Each hierarchical Bayes model’s posterior predictive distribution is compared against held-out observations using probability integral transform (PIT) diagnostics. Deviations from uniformity in PIT histograms trigger automatic prior variance adjustments.
2. **Causal Consistency Tests:**
   Counterfactual validation is conducted by replaying historical events under perturbed multipliers in the simulator. Elasticity gradients are compared with empirical estimates, ensuring directional alignment (price up → demand down).
3. **Stability Under Domain Shift:**
   Population Stability Index (PSI) and KL divergence are monitored between training and live-serving feature distributions. Deviations exceeding 0.05 prompt retraining workflows through Michelangelo’s pipeline.
4. **Simulation Agreement:**
   The predictive models are embedded into the agent-based simulator (discussed in Stage 2). Simulated trip volumes, wait times, and cancellation rates are compared to real metrics. The simulator must reproduce production KPIs within ±2% before RL training can proceed.

---

## 8. End-to-End Flow

At runtime, the predictive layer acts as the foundational inference substrate supporting RL and control. The end-to-end flow proceeds as follows:

1. Real-time event streams are ingested by Michelangelo’s feature pipelines and transformed into tensorized zone-level states \(s\_t(z\).
2. These tensors feed the predictive models, which output expected demand, driver acceptance, and repositioning values for each tile.
3. Outputs, along with hierarchical Bayesian elasticity estimates, form the environment state representation consumed by the RL policy.
4. The RL actor (discussed next) proposes a new surge field \(m\_t(z\).
5. Constraints are enforced by a projection layer ensuring smoothness, fairness, and regulatory compliance.
6. Final surge multipliers are written to the marketplace backend, closing the control loop.

This layered design ensures that learning remains stable, interpretable, and aligned with operational and regulatory constraints — forming the backbone of Uber’s self-regulating marketplace.

---

```
                                       ┌────────────────────────────────────────────────────┐
                                       │                    UBER MICHELANGELO                │
                                       │     Unified ML Platform for Training + Serving      │
                                       └────────────────────────────────────────────────────┘
                                                        ▲
                                                        │
                                                        │
                                       ┌────────────────┴────────────────┐
                                       │                                 │
                             ┌─────────┴──────────┐           ┌──────────┴──────────┐
                             │  DATA PLANE        │           │  TRAINING PLANE      │
                             │ (Feature Ingestion │           │ (Simulation + RL)    │
                             │  & Processing)     │           │                      │
                             └─────────┬──────────┘           └──────────┬───────────┘
                                       │                                 │
                                       ▼                                 ▼
                      ┌──────────────────────────────────┐  ┌──────────────────────────────────┐
                      │ FEATURE PIPELINE                 │  │ DISTRIBUTED SIMULATOR            │
                      │ - Kafka / Flink / Spark          │  │ - Calibrated City Model          │
                      │ - Rider/Driver Telemetry         │  │ - Rider + Driver Agents          │
                      │ - Weather / Event Embeddings     │  │ - Matching Logic + ETA Model     │
                      └──────────────────────────────────┘  │ - Synthetic Data Generation (Gen)│
                                       │                   └──────────────────────────────────┘
                                       ▼                                 │
                     ┌──────────────────────────────────────────────────┘
                     │
                     ▼
      ┌────────────────────────────────────────────────────────────────────────┐
      │        PREDICTIVE MODELING LAYER                                       │
      │        (Short-term Forecast + Elasticities)                            │
      │                                                                        │
      │   ┌────────────────────────────┐   ┌────────────────────────────┐       │
      │   │ Demand Response Model      │   │ Driver Acceptance Model    │       │
      │   │  f_demand(x, m)            │   │  f_accept(x, m, ETA)       │       │
      │   └────────────────────────────┘   └────────────────────────────┘       │
      │                                                                        │
      │   + Hierarchical Bayesian Elasticity Model (Spatial Shrinkage)         │
      │   + Generative Augmentation for Sparse Regions                         │
      │   + Monotonic Constraints & Causal Regularization                      │
      └────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
      ┌────────────────────────────────────────────────────────────────────────┐
      │      REINFORCEMENT LEARNING LAYER (Global Market Control)              │
      │                                                                        │
      │   CMDP: (S, A, R, P)                                                   │
      │   - Actor: UNet + Spatial Attention over city grid                     │
      │   - Critic: Distributional Value + Auxiliary Critics                   │
      │   - Policy Optimization: PPO + Lagrangian Constraint Handling           │
      │                                                                        │
      │   Inputs: s_t (spatiotemporal state tensor)                            │
      │   Outputs: m_t(z) = surge multiplier field                             │
      │   Reward: Revenue – WaitTime – CancelRate – FairnessPenalty             │
      │                                                                        │
      │   Trained on Simulator via Ray/RLlib (billions of steps/day)            │
      └────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
      ┌────────────────────────────────────────────────────────────────────────┐
      │      SAFETY AND CONSTRAINT PROJECTION LAYER                            │
      │                                                                        │
      │   Quadratic Program:                                                   │
      │     min ½||m - m*||² + μ mᵗ L m                                        │
      │     s.t. m_min ≤ m ≤ m_max                                             │
      │          |m - m_prev| ≤ Δ_max                                          │
      │                                                                        │
      │   Ensures: Spatial smoothness, temporal stability, fairness            │
      └────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
      ┌────────────────────────────────────────────────────────────────────────┐
      │      SERVING PLANE                                                    │
      │      (Real-time Inference + Publication)                              │
      │                                                                        │
      │   - Inference Service (TensorRT/ONNX Runtime)                         │
      │   - Latency Budget <60 ms p95                                         │
      │   - Writes surge multipliers to Marketplace Cache                     │
      │   - Uses Feature Store for online inference consistency               │
      └────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
      ┌────────────────────────────────────────────────────────────────────────┐
      │      MARKETPLACE BACKEND                                              │
      │   - Rider & Driver Apps consume surge multipliers                     │
      │   - Trip requests & acceptances create new telemetry data             │
      │   - Feeds back into Data Plane (closing the loop)                     │
      └────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
      ┌────────────────────────────────────────────────────────────────────────┐
      │      MONITORING + GOVERNANCE LAYER                                    │
      │                                                                        │
      │   - Drift Detection (PSI / KL)                                        │
      │   - Elasticity Residuals, Fairness Index                              │
      │   - Automated Retraining Triggers                                     │
      │   - Explainability (Shapley Values)                                   │
      │   - Full Lineage + Compliance Logs                                    │
      └────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
      ┌────────────────────────────────────────────────────────────────────────┐
      │      CONTINUOUS FEEDBACK + RETRAINING                                 │
      │   - New data retrains predictive + RL models via Michelangelo DAGs    │
      │   - Canary rollout + DR Evaluation                                   │
      │   - Continuous policy evolution across cities                        │
      └────────────────────────────────────────────────────────────────────────┘ Absolutely — we **definitely need a full architecture diagram**.
```

You’re right to insist on it — for something of this scale (Uber’s production RL-driven pricing system), a diagram is essential not only for conceptual clarity but also for communicating **the interactions between ML components, data flow, control loops, and Michelangelo infrastructure**.

We’ll build the architecture diagram in **dense ASCII form** so it’s fully text-reproducible (like you’d draw in a design review doc or whiteboard), but still expressive enough to capture all layers — **data, modeling, RL, serving, simulation, monitoring, and governance**.

---

# Uber Price Optimization System – End-to-End Architecture Diagram

```
                                           ┌────────────────────────────────────────────────────┐
                                           │                    UBER MICHELANGELO                │
                                           │     Unified ML Platform for Training + Serving      │
                                           └────────────────────────────────────────────────────┘
                                                            ▲
                                                            │
                                                            │
                                           ┌────────────────┴────────────────┐
                                           │                                 │
                                 ┌─────────┴──────────┐           ┌──────────┴──────────┐
                                 │  DATA PLANE        │           │  TRAINING PLANE      │
                                 │ (Feature Ingestion │           │ (Simulation + RL)    │
                                 │  & Processing)     │           │                      │
                                 └─────────┬──────────┘           └──────────┬───────────┘
                                           │                                 │
                                           ▼                                 ▼
                          ┌──────────────────────────────────┐  ┌──────────────────────────────────┐
                          │ FEATURE PIPELINE                 │  │ DISTRIBUTED SIMULATOR            │
                          │ - Kafka / Flink / Spark          │  │ - Calibrated City Model          │
                          │ - Rider/Driver Telemetry         │  │ - Rider + Driver Agents          │
                          │ - Weather / Event Embeddings     │  │ - Matching Logic + ETA Model     │
                          └──────────────────────────────────┘  │ - Synthetic Data Generation (Gen)│
                                           │                   └──────────────────────────────────┘
                                           ▼                                 │
                         ┌──────────────────────────────────────────────────┘
                         │
                         ▼
          ┌────────────────────────────────────────────────────────────────────────┐
          │        PREDICTIVE MODELING LAYER                                       │
          │        (Short-term Forecast + Elasticities)                            │
          │                                                                        │
          │   ┌────────────────────────────┐   ┌────────────────────────────┐       │
          │   │ Demand Response Model      │   │ Driver Acceptance Model    │       │
          │   │  f_demand(x, m)            │   │  f_accept(x, m, ETA)       │       │
          │   └────────────────────────────┘   └────────────────────────────┘       │
          │                                                                        │
          │   + Hierarchical Bayesian Elasticity Model (Spatial Shrinkage)         │
          │   + Generative Augmentation for Sparse Regions                         │
          │   + Monotonic Constraints & Causal Regularization                      │
          └────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
          ┌────────────────────────────────────────────────────────────────────────┐
          │      REINFORCEMENT LEARNING LAYER (Global Market Control)              │
          │                                                                        │
          │   CMDP: (S, A, R, P)                                                   │
          │   - Actor: UNet + Spatial Attention over city grid                     │
          │   - Critic: Distributional Value + Auxiliary Critics                   │
          │   - Policy Optimization: PPO + Lagrangian Constraint Handling           │
          │                                                                        │
          │   Inputs: s_t (spatiotemporal state tensor)                            │
          │   Outputs: m_t(z) = surge multiplier field                             │
          │   Reward: Revenue – WaitTime – CancelRate – FairnessPenalty             │
          │                                                                        │
          │   Trained on Simulator via Ray/RLlib (billions of steps/day)            │
          └────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
          ┌────────────────────────────────────────────────────────────────────────┐
          │      SAFETY AND CONSTRAINT PROJECTION LAYER                            │
          │                                                                        │
          │   Quadratic Program:                                                   │
          │     min ½||m - m*||² + μ mᵗ L m                                        │
          │     s.t. m_min ≤ m ≤ m_max                                             │
          │          |m - m_prev| ≤ Δ_max                                          │
          │                                                                        │
          │   Ensures: Spatial smoothness, temporal stability, fairness            │
          └────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
          ┌────────────────────────────────────────────────────────────────────────┐
          │      SERVING PLANE                                                    │
          │      (Real-time Inference + Publication)                              │
          │                                                                        │
          │   - Inference Service (TensorRT/ONNX Runtime)                         │
          │   - Latency Budget <60 ms p95                                         │
          │   - Writes surge multipliers to Marketplace Cache                     │
          │   - Uses Feature Store for online inference consistency               │
          └────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
          ┌────────────────────────────────────────────────────────────────────────┐
          │      MARKETPLACE BACKEND                                              │
          │   - Rider & Driver Apps consume surge multipliers                     │
          │   - Trip requests & acceptances create new telemetry data             │
          │   - Feeds back into Data Plane (closing the loop)                     │
          └────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
          ┌────────────────────────────────────────────────────────────────────────┐
          │      MONITORING + GOVERNANCE LAYER                                    │
          │                                                                        │
          │   - Drift Detection (PSI / KL)                                        │
          │   - Elasticity Residuals, Fairness Index                              │
          │   - Automated Retraining Triggers                                     │
          │   - Explainability (Shapley Values)                                   │
          │   - Full Lineage + Compliance Logs                                    │
          └────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
          ┌────────────────────────────────────────────────────────────────────────┐
          │      CONTINUOUS FEEDBACK + RETRAINING                                 │
          │   - New data retrains predictive + RL models via Michelangelo DAGs    │
          │   - Canary rollout + DR Evaluation                                   │
          │   - Continuous policy evolution across cities                        │
          └────────────────────────────────────────────────────────────────────────┘
```

---

# Diagram Walkthrough and Technical Interpretation

Let’s break down **what this diagram conveys and why it’s designed this way**:

### 1. Data Plane

At the very top of the loop, the **Feature Pipeline** sits inside Michelangelo’s data ecosystem.
This ensures that all model inputs are deterministic, timestamp-aligned, and version-controlled.
This layer guarantees *temporal integrity* — you can always reconstruct exactly what the model saw when it made a decision.

**Key design decision:** Streaming + feature versioning ensures real-time responsiveness while keeping offline training reproducible — a dual requirement for reinforcement learning.

---

### 2. Predictive Layer

The predictive layer (demand, driver acceptance, ETA) serves two functions:

1. Provide differentiable forward models for the simulator (the “environment dynamics”).
2. Generate elasticity priors and contextual forecasts that serve as *inputs* to the RL state tensor.

Each predictive model is independently monitored and trained via Michelangelo pipelines, using Bayesian regularization to share statistical strength across sparse regions.

**Design reasoning:** Keeping the predictive layer modular allows Uber to recalibrate behavioral models without retraining the full RL policy, which is computationally expensive.

---

### 3. Reinforcement Learning Layer

This is the **intelligence core**. The actor–critic learns an optimal spatiotemporal pricing field over the entire city grid.

* The **UNet backbone** ensures spatial coherence — local patterns propagate through skip connections, preserving fine detail while capturing global context.
* The **spatial attention heads** learn directional dependencies between distant zones (airport ↔ downtown).
* The **distributional critic** provides uncertainty quantification, enabling risk-aware surge adjustments.
* The **Lagrangian constraints** maintain fairness and regulatory compliance.

**Design reasoning:** A spatially structured actor-critic balances real-time latency with the need to model high-dimensional joint control.

This is why Uber’s paper emphasized the “RL as global controller” paradigm rather than per-zone policies: it enforces coordination across thousands of micro-markets.

---

### 4. Simulator + Offline Training

The **calibrated simulator** connects predictive models into an environment where the RL policy can safely experiment.
This simulator acts as a high-fidelity “digital twin” of the Uber marketplace, enabling billions of synthetic rollouts per day.

Each simulation run produces trajectories \(s\_t, a\_t, r\_t, s\_{t+1}\) that feed the replay buffer for PPO training.

**Design reasoning:** RL without simulation would require unsafe live exploration; this design allows safe, sample-efficient learning and causal validation before deployment.

---

### 5. Safety Projection

This constraint layer acts as the **governor** ensuring that surge recommendations are always within safe operational bounds.

* The quadratic programming solver guarantees that the resulting surge map is smooth and fair.
* Even if the RL actor temporarily oscillates, the projection layer ensures temporal and spatial stability.

**Design reasoning:** By isolating constraint satisfaction into a deterministic convex projection, Uber decouples safety from learning — allowing RL to explore freely in simulation but remain bounded in production.

---

### 6. Serving Plane

The real-time serving infrastructure (deployed via Michelangelo) translates model outputs into live surge multipliers with sub-100ms latency.
Features are pulled from the live feature store, ensuring that the online model sees exactly what it trained on.

**Design reasoning:** Separating inference from control logic allows high availability, scaling, and reproducibility across markets.

---

### 7. Monitoring + Governance

This layer is what makes the system *operationally safe*.
It continuously checks:

* Feature drift and causal consistency.
* Elasticity deviations.
* Fairness and spatial smoothness.
* Shapley explainability for each pricing action.

This is where Michelangelo’s **governance framework** ensures reproducibility, regulatory compliance, and accountability.

---

### 8. Continuous Feedback and Retraining

Finally, all monitoring data flows back into the training DAG.
When drift thresholds are triggered, retraining pipelines launch automatically — recalibrating predictive models, re-estimating elasticities, and fine-tuning the RL policy in simulation.

The system thereby achieves **continuous adaptation** — always learning, but always bounded by safety and governance.

---

# Why This Architecture Works

This design is effective because it unifies four key principles:

1. **Causality-aware prediction:** predictive models provide interpretable short-term causal signals.
2. **Hierarchical control:** RL manages the macroeconomic dynamics across the entire marketplace.
3. **Safety by projection:** fairness and volatility constraints are enforced outside of the learning process, ensuring stable deployments.
4. **Continuous feedback:** automated monitoring and retraining maintain alignment with real-world behavior.

In other words, the architecture turns the marketplace into a self-regulating learning organism that maintains equilibrium in real time.

---

# 9. Reinforcement Learning Layer: Dynamic Price Field Control

The predictive layer described earlier models short-term local responses. However, pricing decisions affect the marketplace over longer temporal horizons: they influence driver repositioning patterns, supply latency, and rider deferral decisions, which unfold over minutes to hours.
To capture these delayed and coupled effects, Uber formulates pricing as a **sequential decision-making problem under uncertainty** — specifically, a **constrained Markov Decision Process (CMDP)**.

The CMDP formalization allows for optimizing expected long-term value while satisfying safety and fairness constraints across both space and time.

---

## 9.1 CMDP Formulation

Let \(s\_t \in \mathcal{S}\) represent the system’s state at time \(t\), summarizing all city-level information: demand forecasts, driver distributions, ETAs, weather conditions, event embeddings, and temporal encodings.
The agent (pricing policy) outputs a continuous action field \(a\_t = m\_t(z) \in [m\_{\min}, m\_{\max}]^{|Z|}\), assigning a surge multiplier to each zone.
The system then transitions stochastically according to:

\(s\_{t+1} \sim P(s\_{t+1} | s\_t, a\_t),\)
and yields a reward \(r\_t = R(s\_t, a\_t\) representing a function of gross merchandise value (GMV), throughput, and customer satisfaction.

We define the optimization objective as:

\(\max\_{\pi} ; \mathbb{E}\*\pi \left[ \\1\_{\2}^{\infty} \gamma^t (r\_t - \sum\_k \lambda\_k c\_t^k) \right],\)
subject to per-step constraints \(c\_t^k \leq \bar{c}\_k\) on fairness, surge volatility, and service-level metrics.

The dual parameters \(\lambda\_k\) evolve dynamically via Lagrangian updates, allowing the policy to learn efficient trade-offs between revenue maximization and constraint satisfaction.

---

## 9.2 State Representation and Spatial Hierarchy

The state tensor \(s\_t\) is a high-dimensional field of shape \(H \times W \times C\), where \(H \times W\) represents the grid of zones and \(C\) the feature channels (supply count, demand forecast, active trips, mean ETA, cancellation rates, and environmental covariates).

Each feature map is normalized to preserve scale invariance across cities and encoded with spatial adjacency via a road network graph \(G = (V, E\).
The adjacency is represented by a Laplacian \(L = D - A\), where \(A\) is the weighted adjacency matrix of tiles and \(D\) is the degree matrix. This Laplacian underpins later smoothness constraints in the optimization phase.

To ensure hierarchical learning and transferability across markets, Uber applies a **two-tier spatial representation**:

1. **Local zone embeddings** (≈ few hundred meters): learned via 2D convolutions capturing fine-grained local structures (pickup hotspots, intersections).
2. **Regional embeddings** (≈ several kilometers): aggregated through graph convolution layers that model high-level mobility flows between areas (airport ↔ downtown).

This multiscale representation allows the RL policy to make consistent global decisions without sacrificing local sensitivity.

---

## 9.3 Reward Structure and Causal Attribution

The reward function \(R(s\_t, a\_t\) encapsulates Uber’s high-level marketplace goals, weighted to align operational efficiency and fairness:

\[R(s\_t, a\_t) = \underbrace{w\_1 \cdot \text{GMV}\*t}\*{\text{revenue}}
\* \underbrace{w\_2 \cdot \text{WaitTime}\*t}\*{\text{service quality}}
\* \underbrace{w\_3 \cdot \text{CancelRate}\*t}\*{\text{reliability}}
\* \underbrace{w\_4 \cdot \text{EarningsDispersion}\*t}\*{\text{driver fairness}}.\]

However, unlike static optimizers, this reward cannot be estimated directly from single-step data, since pricing effects propagate through the driver supply field over time.
Uber therefore employs **counterfactual temporal credit assignment**, combining simulated rollouts and doubly robust off-policy estimation to approximate long-term rewards.

To support causal interpretation, the reward decomposition includes *auxiliary critics* trained on distinct aspects of the environment (demand elasticity, driver response, ETA smoothness). These auxiliary signals stabilize training by providing denser gradients and reducing variance in the policy update.

---

## 9.4 Actor–Critic Architecture

### Actor: UNet + Spatial Attention

The **actor network** is a UNet-like encoder–decoder operating over the 2D grid representation of the city.
The encoder applies multiple convolutional layers with stride and dilation to capture global spatial patterns, while the decoder reconstructs local price multipliers at fine granularity.

At the bottleneck, **multi-head spatial attention** modules model long-range dependencies: for example, surge increases at the airport propagate to city center demand a few minutes later.
Attention enables such cross-regional coupling to be learned dynamically rather than encoded manually.

Mathematically, each attention head performs:

\(\text{Attn}(Q,K,V) = \text{softmax}!\left(\frac{QK^\top}{\sqrt{d\_k}}\right) V,\)
where queries \(Q\), keys \(K\), and values \(V\) are derived from spatial embeddings of the current state \(s\_t\).

The actor outputs a continuous field of mean and variance parameters:
\(a\_t(z) \sim \mathcal{N}(\mu\_\theta(s\_t(z)), \sigma\_\theta(s\_t(z))^2).\)
Exploration occurs through sampling from this Gaussian distribution, enabling stochastic policy gradients to capture uncertainty in under-explored regions.

### Critic: Distributional Value Estimation

The **critic network** estimates a distribution over returns \(Z(s\_t\) rather than a scalar value. This *distributional RL* approach, as employed in Uber’s “Reinforcement Learning for Marketplace Balance” system, captures uncertainty over long-term outcomes.

Each critic outputs both:

* \(V\_\psi(s\_t) = \mathbb{E}[Z(s\_t)]\): expected value, and
* \(V\_\psi^{(k)}(s\_t\): auxiliary critics for constraint cost components (wait time, fairness, smoothness).

These critics are trained using **temporal-difference (TD)** learning with multi-step bootstrapping:

\[\mathcal{L}\*V = \mathbb{E}[(\1\_{\text{type}} - V\_\psi(s\_t))^2],
\quad Z\_\text{target} = r\_t + \gamma V\_\psi(s\_{t+1}).\]

Auxiliary critics serve as constraint estimators for the Lagrangian updates described next.

---

## 9.5 Policy Optimization and Safety Constraints

The policy is trained with a variant of **Proximal Policy Optimization (PPO)**, which limits policy updates to remain close to the previously validated baseline.
The objective is:

$$
L^{PPO}(\theta) =
\mathbb{E}\_t \Big[
\min \big(
r\_t(\theta) \hat{A}\_t,
\text{clip}(r\_t(\theta), 1 - \epsilon, 1 + \epsilon) \hat{A}\_t
\big)
\Big]

* |  |  |
  | --- | --- |
  | \beta\_{KL} \cdot D\_{KL}(\pi\_\theta | \pi\_0) |
* \mu \cdot m\_t^\top L m\_t,
  $$
  where:
* \(r\_t(\theta\) is the policy likelihood ratio,
* \(D\_{KL}\) enforces conservatism relative to the baseline policy \(\pi\_0\),
* \(L\) is the spatial Laplacian penalty ensuring smooth surge fields.

Constraint costs \(c\_t^k\) are integrated via **dual gradient descent**:

\(\lambda\_k \leftarrow \max\big(0, \lambda\_k + \eta\)\mathbb{E}[c\_t^k] - \bar{c}\_k\(\big),\)
so that if any constraint is violated, its corresponding multiplier grows, increasing penalty pressure in subsequent updates.

This adaptive balancing ensures fairness and operational safety even as the policy improves revenue.

---

## 9.6 Alternative Policy Formulations

Uber’s research explored several alternative policy formulations before converging on the spatial actor–critic:

| Policy Type | Description | Pros | Cons |
| --- | --- | --- | --- |
| Linear surge model | Parametric mapping \(m\_t = W s\_t\) | Interpretable, fast | Too rigid; cannot handle nonlinear cross-terms |
| GNN-based policy | Graph neural network actor | Natural spatial inductive bias | Higher latency (~2× UNet); less stable gradients |
| Transformer-based policy | Sequence model over zones | Captures long-range dependencies | Overparameterized; training instabilities |
| UNet + Attention (chosen) | Multiscale convolutional actor with spatial attention | Low latency, multiscale context, interpretable structure | Slightly larger memory footprint |

The chosen architecture achieves near-optimal tradeoffs for global coordination, local adaptivity, and serving latency within 60 ms p95 in production.

---

# 10. Environment Simulator and Counterfactual Replay

Direct online RL experimentation is unsafe in a live marketplace. Instead, Uber’s policy training occurs primarily in a **calibrated agent-based simulator**, as described in the “Reinforcement Learning for Modeling Marketplace Balance” blog.

This simulator provides a differentiable approximation of city-scale dynamics, enabling millions of policy iterations per day before any live A/B deployment.

---

## 10.1 Simulator Structure

The simulator models the full spatiotemporal feedback loop across riders, drivers, and matching logic.
Each simulation tick (e.g., one minute) executes the following pipeline:

1. **Rider Request Generation:**
   Requests are sampled from a Poisson process with rate parameter derived from the predictive demand model:
   \(\lambda\_{z,t} = \hat{D}\_\text{demand}(s\_t(z), m\_t(z)).\)
   Generated requests inherit rider attributes, destination distributions, and price sensitivity from historical distributions conditioned on context.
2. **Driver Behavior Modeling:**
   Each driver agent is modeled as a stateful decision-maker with two probabilistic modules:

   * Acceptance probability \(P\_\text{accept}(m, \text{ETA}, \text{earnings}\).
   * Reposition policy derived from the driver value network \(V(s^{(d)}\_t\).
3. **Matching Process:**
   Rider–driver matching is implemented as a **bipartite matching optimization**, minimizing expected pickup time under the surge multipliers. The matching algorithm’s stochastic behavior introduces variability into rewards and transitions.
4. **Trip Realization:**
   Accepted trips update driver locations and trip completion times, adjusting available supply for future timesteps.
5. **Metric Logging:**
   Simulator computes GMV, wait times, cancellations, and fairness metrics for policy evaluation.

The simulator state is thus updated according to empirically learned transition models, yielding an environment consistent with real marketplace feedback.

---

## 10.2 Calibration and Validation

To ensure simulator fidelity, Uber calibrates each component against real historical data:

* **Demand calibration:** predicted vs. observed trip counts across time and geography. Mean absolute error (MAE) must remain below 2%.
* **Supply calibration:** simulated driver distributions must match observed distributions via Wasserstein distance metrics.
* **Temporal fidelity:** cross-correlation between simulated and real wait times must exceed 0.9.

Only after passing these checks is a simulator version approved for policy training.

---

## 10.3 Simulation-Augmented Learning

Uber combines **offline replay learning** with **online simulation** in a two-phase loop:

1. **Offline Phase:** Initialize policy using logged historical data with *conservative Q-learning (CQL)* loss to avoid extrapolation error:
   \(\mathcal{L}\*{CQL} = \alpha (\log \sum\_a e^{Q(s,a)} - \mathbb{E}\*{(s,a)\sim D}[Q(s,a)]) + |Q - \mathcal{T}Q|^2.\)
2. **Simulation Phase:** Deploy the initialized policy into the calibrated simulator for policy-gradient fine-tuning using PPO.

This hybrid approach accelerates convergence and reduces unsafe exploration, enabling stable RL policies within realistic training cycles.

---

# 11. Constraint Projection and Safety at Inference Time

Once trained, the policy proposes an unconstrained surge field \(m^\*(z\). Before deployment, this field is projected into a feasible set defined by operational constraints.
This projection is implemented as a **quadratic programming (QP)** problem:

\[\begin{aligned}
\min\_{m} \quad & \frac{1}{2}|m - m^\*|^2 + \mu , m^\top L m, \
\text{s.t.} \quad & m\_{\min} \le m \le m\_{\max}, \
& |m - m\_{t-1}| \le \Delta\_{\max}.
\end{aligned}\]

The term \(m^\top L m\) enforces spatial smoothness, discouraging abrupt changes across adjacent zones.
Temporal stability is ensured by bounding the rate of change \(\Delta\_{\max}\).

The QP is convex and solved via a pre-factored KKT system in under 10 ms.
This ensures that even if the RL model outputs erratic multipliers, the final published surge field remains safe, fair, and regulation-compliant.

---

# 12. Policy Evaluation and Deployment within Michelangelo

### 12.1 Offline Evaluation

Before deployment, every policy undergoes **Offline Policy Evaluation (OPE)** using **Doubly Robust (DR) Estimation**:

\[\hat{V}\_{DR} = \frac{1}{n}\sum\_i \left[ \hat{m}(x\_i, a\_i^\*) + w\_i (Y\_i - \hat{m}(x\_i, a\_i)) \right],
\quad
w\_i = \frac{\pi(a\_i|x\_i)}{b(a\_i|x\_i)}.\]

The DR estimator combines model-based predictions with importance weighting to yield unbiased and low-variance value estimates.
Policies whose offline evaluations do not outperform the baseline with statistical confidence are not advanced to live testing.

### 12.2 Experimentation and Rollout

Validated policies are registered in Michelangelo’s **Model Registry**, versioned with reproducible configuration metadata.
Deployment follows hierarchical canary testing:

* Initial rollout in one sub-region of a city, monitored for constraint satisfaction.
* Escalation to full-city deployment if metrics remain within tolerance bounds.
* Gradual scaling across cities with adaptive retraining based on feedback data.

Michelangelo’s experiment orchestrator tracks key KPIs: GMV uplift, average wait time, fairness, and volatility.
If the policy causes degradation exceeding preset thresholds (e.g., wait time +10%), automated rollback triggers restore the last stable model.

---

# 13. Monitoring, Drift Detection, and Governance

Post-deployment, the system continuously monitors both performance and compliance.

1. **Drift Detection:**
   Feature distributions are compared between live data and training distributions using KL and PSI metrics. Violations trigger retraining workflows.
2. **Elasticity Residual Analysis:**
   Discrepancies between predicted and realized elasticities indicate environmental drift (e.g., sudden changes due to events or regulation).
3. **Safety Monitors:**
   Every surge update is logged with pre/post-projection deltas, constraint violations, and the policy version. Dashboards visualize these metrics per region.
4. **Governance Layer:**
   Michelangelo enforces reproducibility and auditability: each pricing decision can be traced to model weights, configuration, and input features. This satisfies both internal governance and external regulatory audits.

---

# 14. System Summary and End-to-End Flow

The complete price optimization loop functions as a closed feedback controller orchestrating millions of micro-markets:

1. **Data ingestion** pipelines continuously update the system’s state.
2. **Predictive models** infer short-term responses and elasticities.
3. **Hierarchical Bayesian regularization** ensures spatial coherence and uncertainty-aware estimates.
4. **RL actor–critic policy** optimizes long-term performance, balancing exploration, revenue, and fairness.
5. **Constraint projection** guarantees safe and smooth final prices.
6. **Michelangelo infrastructure** handles training orchestration, deployment, and monitoring at global scale.

Through this architecture, Uber’s marketplace evolves from a reactive surge mechanism into a **self-learning economic system** — continuously forecasting, optimizing, and adapting in real time across billions of transactions.

Excellent — we’re going full depth then.
Stage 3 will complete the architecture by expanding the **infrastructure, orchestration, monitoring, and governance layers**, including detailed system pipelines within **Michelangelo**, the **distributed training ecosystem**, **data lineage**, **experiment tracking**, and **reliability guarantees**.

This stage reads as an internal Uber systems design document — meant to be both **technically rigorous** and **architecturally descriptive** enough to serve as a foundation for actual implementation or internal architecture review.

---

# 15. Infrastructure and Computational Orchestration

A production-grade price optimization system at Uber’s scale must coordinate **continuous data ingestion**, **massive distributed training**, **safe deployment**, and **real-time serving** — all under stringent latency and reliability requirements.
Michelangelo, Uber’s in-house ML platform, is the backbone enabling this full lifecycle.

The system is thus a **closed-loop ML+RL control architecture** comprising four primary planes:

1. **Data Plane** — responsible for stream ingestion, feature computation, and storage consistency.
2. **Training Plane** — responsible for distributed training, simulation, and reinforcement learning orchestration.
3. **Serving Plane** — responsible for low-latency inference and decision application.
4. **Monitoring and Governance Plane** — responsible for reliability, compliance, and continuous evaluation.

Each plane communicates through versioned interfaces, allowing the entire system to evolve modularly without breaking operational integrity.

---

## 15.1 Data Plane: Streaming Feature Fabric

The data pipeline begins at Uber’s telemetry infrastructure, which emits **Kafka streams** containing trip requests, driver locations, pricing updates, ETAs, and other sensor events.

**Flink** and **Spark Structured Streaming** jobs aggregate these signals into temporally aligned feature windows, producing incremental updates every few seconds.
Each data record includes both instantaneous features (e.g., current ETA, surge multiplier) and exponentially weighted moving averages to encode temporal context.

The resulting feature sets are written to Uber’s **Feature Store**, an integrated Michelangelo service that maintains **online/offline consistency**.

Key principles of the data plane include:

* **Temporal determinism:** every feature has an associated timestamp and window definition, enabling exact reconstruction of the training state for offline replay.
* **Feature lineage:** each feature definition is version-controlled and tied to its transformation code, ensuring reproducibility and auditability.
* **Schema evolution:** backward-compatible updates allow incremental feature rollout without downtime.
* **Validation pipelines:** unit and statistical tests validate that new feature versions remain within empirical tolerances (mean, variance, correlation drift).

The data plane thus ensures that every model and simulator component operates on temporally aligned, version-consistent, and validated inputs — a nonnegotiable requirement for stability in reinforcement learning systems.

---

## 15.2 Training Plane: Distributed Reinforcement Learning and Simulation

The training plane integrates Uber’s distributed ML stack with **Ray/RLlib**, **Michelangelo’s orchestration layer**, and **containerized simulation clusters** that can execute millions of environment steps per second.

### Cluster Composition

Each training run is divided into three logical groups of machines:

* **Actor Nodes** simulate environments and generate trajectories in parallel.
* **Learner Nodes** aggregate gradients, compute policy updates, and broadcast new parameters.
* **Evaluator Nodes** perform periodic off-policy evaluations using doubly robust estimators.

All nodes are orchestrated via **Kubernetes on Michelangelo**, allowing elastic resource scaling based on queue load and batch throughput.

### Data Flow

1. Actors run the latest policy \(\pi\_\theta\) in the simulator and collect trajectories \(s\_t, a\_t, r\_t, s\_{t+1}\).
2. Collected samples are streamed into an intermediate **Replay Buffer Service**, sharded by region and timestamp.
3. Learners fetch mini-batches from this buffer to compute gradient updates using distributed SGD or Adam optimizers.
4. Updated parameters are pushed back to actors every few seconds, maintaining asynchronous but stable convergence.

The entire loop achieves throughput of several billion environment steps per day, enabling robust convergence even in high-dimensional continuous control spaces.

### Training Synchronization

Michelangelo enforces deterministic synchronization through:

* **Global random seeds** for reproducibility.
* **Data checkpoints** tied to feature store versions.
* **Configuration registries** capturing all hyperparameters (learning rate, PPO clip ratio, constraint weights).

Every training job thus becomes fully replayable: given a timestamp and configuration hash, the exact model weights and performance metrics can be reconstructed.

---

## 15.3 Simulation-as-a-Service

A major innovation of this architecture is **simulation-as-a-service (SaaS)**: instead of embedding simulators directly in training code, Uber deploys simulators as gRPC services accessible via Michelangelo’s internal network.

Each simulator instance exposes standardized APIs:

* `reset(city_id, seed)` initializes simulation state.
* `step(actions)` applies surge multipliers and returns transitions.
* `get_metrics()` returns aggregated KPIs for evaluation.

This separation allows:

* Multiple policies to train concurrently on the same calibrated simulation backend.
* Fine-grained monitoring of simulation health and divergence.
* Independent evolution of simulation logic (e.g., matching algorithms, driver dynamics) without altering RL code.

All simulation endpoints are containerized with versioned configurations, so training runs can be pinned to specific simulator builds — crucial for experiment reproducibility and causal attribution.

---

## 15.4 Model Registry and Versioning

Trained models, once validated, are serialized and registered in the **Michelangelo Model Registry**, which serves as a global artifact management system.
Each registry entry includes:

* Binary weights and architecture definition.
* Training metadata: simulator version, feature schema hash, hyperparameters, random seeds.
* Evaluation metrics: offline validation, simulation reward, constraint adherence.
* Governance metadata: experiment owner, approval state, rollout history.

The registry enforces immutability: once a model is versioned and marked as deployed, it cannot be altered, only superseded. This enables strict rollback capability and full lineage tracking for every deployed policy.

---

# 16. Serving Plane: Real-Time Inference and Control

The serving layer handles live decision-making — transforming incoming feature states into surge multipliers within a latency budget of approximately **60 milliseconds p95** per request.

---

## 16.1 System Topology

At runtime, each city operates a **pricing service cluster** consisting of:

* **Ingress Layer:** receives requests from marketplace services containing current state tensors and contextual data.
* **Inference Layer:** runs model computations on GPUs or high-performance CPUs using TensorRT or ONNX-optimized inference graphs.
* **Projection Layer:** applies the QP-based safety projection (see Section 11).
* **Publication Layer:** writes finalized surge multipliers to the pricing cache consumed by rider and driver apps.

These clusters are geographically distributed for low latency and redundancy. Load balancing is dynamic, based on real-time traffic and latency monitoring.

---

## 16.2 Feature Synchronization

A key challenge in serving RL models is maintaining **feature-time consistency** between online inference and training.
Uber achieves this through **feature materialization checkpoints**: each batch of features used in training is timestamped and synchronized to the online store via a commit log. The inference service only consumes feature definitions that have corresponding offline training versions.

This mechanism eliminates train/serve skew — one of the most common sources of instability in live RL deployments.

---

## 16.3 Latency and Resilience Engineering

To guarantee real-time responsiveness, several engineering optimizations are used:

* **Model quantization:** parameters are quantized to 8-bit representations without perceptible accuracy loss.
* **Asynchronous batching:** concurrent requests within a 5 ms window are batch-processed on shared GPU cores.
* **Circuit breakers:** if inference latency exceeds thresholds, the system temporarily reverts to a cached baseline policy.
* **Health probes and redundancy:** multiple instances per region ensure zero downtime in the event of node failure.

The serving infrastructure thus provides deterministic, low-variance response times — a requirement for smooth user experience and fairness.

---

# 17. Monitoring, Evaluation, and Feedback Loops

The monitoring layer transforms the live system into a **self-diagnosing and self-correcting organism**. It continuously evaluates model health, data drift, policy behavior, and business metrics.

---

## 17.1 Data and Feature Drift Monitoring

Every feature used by the model has an associated monitoring job that computes divergence metrics between live and training distributions:

* **Population Stability Index (PSI):** measures feature distribution drift; thresholds of 0.05 trigger retraining.
* **Kullback–Leibler Divergence:** tracks high-dimensional embeddings such as driver state encodings.
* **Temporal Autocorrelation Checks:** ensure temporal consistency, detecting anomalous spikes (e.g., sudden demand surges from external events).

Detected drifts automatically create *feature drift tickets* in the Michelangelo monitoring dashboard, prompting retraining or investigation.

---

## 17.2 Behavioral Metrics and Feedback

Beyond raw data drift, Uber monitors emergent system behavior through composite indicators:

* **Elasticity consistency:** compares realized demand responses to predicted elasticities; deviations indicate behavioral drift.
* **Spatial fairness index:** evaluates geographic equity of multipliers across regions.
* **Temporal volatility:** measures stability of prices over consecutive updates.
* **Driver satisfaction proxy:** inferred from driver earnings variance and session length distributions.

These indicators feed into continuous retraining cycles, ensuring that the learned policy remains adaptive to evolving conditions.

---

## 17.3 Model Governance and Compliance

Given that pricing directly impacts customer experience and earnings, the system includes strong governance mechanisms:

* **Audit Trails:** every surge decision can be traced back to model version, input features, and configuration parameters.
* **Explainability Interfaces:** Michelangelo provides Shapley-value-based attributions for each pricing decision, enabling explainable AI auditing.
* **Policy Approval Workflow:** new RL policies require sign-off from dedicated pricing committees, ensuring adherence to business and ethical standards.

All governance data is retained for compliance reviews, ensuring regulatory accountability.

---

# 18. Continuous Learning and Auto-Retraining

Uber’s architecture treats the entire reinforcement learning process as a **continuous production pipeline** rather than episodic projects.

### 18.1 Automated Retraining

When drift thresholds are breached or new feature schemas are registered, the pipeline automatically schedules:

1. Data backfill and feature generation for the recent period.
2. Recalibration of hierarchical Bayesian elasticity priors.
3. Reinitialization of RL training from the latest stable checkpoint.
4. Simulation fine-tuning and offline evaluation.
5. Canary rollout if performance surpasses baseline thresholds.

This automation keeps the RL policy continuously aligned with the current marketplace dynamics without requiring manual intervention.

### 18.2 Human-in-the-Loop Oversight

While automation handles the majority of operations, human experts remain in the oversight loop. Domain experts can:

* Adjust constraint weights (fairness, volatility tolerance).
* Freeze policies during extraordinary events (natural disasters, regulation changes).
* Manually inspect explainability dashboards for anomaly triage.

This balance between autonomy and oversight preserves reliability while allowing adaptive intelligence.

---

# 19. Computational and Economic Efficiency

Uber’s system must also be economically efficient at global scale.
The architecture therefore employs several optimization strategies:

* **Model distillation:** large RL policies are periodically distilled into smaller student networks for inference efficiency.
* **Elastic GPU allocation:** training clusters scale up during RL exploration phases and down during policy convergence.
* **Incremental simulator updates:** only changed regions are re-simulated when retraining, reducing computational cost by 60%.
* **Hierarchical caching:** frequently accessed features are cached in-memory within regional inference nodes, minimizing data transfer latency.

Together these optimizations yield near-linear scaling efficiency and sustainable cost structures for city-level and global operation.

---

# 20. End-to-End System Lifecycle

Bringing everything together, the **end-to-end price optimization system lifecycle** proceeds as follows:

1. **Ingestion:** live trip and driver telemetry streams feed the Feature Store via Flink and Kafka.
2. **Feature Preparation:** data is validated, timestamped, and versioned for consistency.
3. **Predictive Modeling:** short-term demand and supply response models are trained and updated continuously.
4. **Elasticity Estimation:** hierarchical Bayesian inference provides smoothed elasticity priors for all zones.
5. **Simulation:** the calibrated simulator reproduces marketplace dynamics with high fidelity.
6. **RL Training:** distributed actor–critic models learn long-term control policies through PPO within simulation.
7. **Projection:** proposed multipliers are projected into the feasible region via QP optimization.
8. **Serving:** Michelangelo-deployed inference clusters compute final prices in real time with low latency.
9. **Monitoring and Governance:** continuous drift analysis, constraint monitoring, and audit trails ensure compliance and reliability.
10. **Feedback Loop:** performance metrics and live data feed back into the training pipeline for continuous adaptation.

This cyclical flow transforms the pricing system into an *autonomous learning organism* — perpetually sensing, predicting, acting, and adapting.

---

# 21. Closing Perspective

Uber’s Price Optimization System exemplifies the frontier of real-world reinforcement learning — operating not as an academic curiosity, but as a **production-scale economic control system**.
By embedding hierarchical Bayesian reasoning, calibrated simulation, distributed actor–critic RL, and rigorous governance within the Michelangelo ecosystem, the platform achieves **continuous self-optimization** under uncertainty, while maintaining fairness, safety, and transparency.

In essence, the system converts the entire Uber marketplace into a **city-scale learning machine** — one that continuously harmonizes the stochastic symphony of human behavior, economic incentives, and real-world logistics.

---

# Uber ETA Optimization System Design

*A Fully Detailed and Mathematical Architecture for Real-Time Travel-Time Prediction*

---

## 1. Context and Motivation

ETA prediction is the backbone of Uber’s marketplace equilibrium:
it underlies pricing (time-dependent fare components), driver matching (pickup ETAs), routing, customer trust, and incentive computations.

Unlike deterministic routing in static graphs, Uber’s ETA system must continuously adapt to stochastic road dynamics, multi-agent interactions, and model-induced feedback loops.
Each predicted ETA becomes an *actionable decision input* in other systems — miscalibration propagates errors across the marketplace.

The global objective is thus not just to predict a mean travel time but to **model the full predictive distribution of arrival times**, in real time, with uncertainty awareness and spatial consistency.

Formally, for a trip requested at time \(t\) with origin \(o\) and destination \(d\):

\[p(T | o, d, t, \mathbf{c}) \quad \text{where } \mathbf{c} \text{ = contextual features (traffic, weather, events, routing policy)}\]

and minimize expected loss:

\[\min\_\theta E\_{(o,d,t)}[\ell(\hat{T}\*\theta(o,d,t), \1\_{\2}})]\]

subject to operational constraints on latency (<30 ms p95), calibration, and fairness across geographies.

---

## 2. ETA as a Hierarchical Spatio-Temporal Inference Problem

ETA prediction is a multi-scale probabilistic inference problem decomposable as:

\[T(o,d,t) = \sum\_{e \in r(o,d)} \tau\_e(t)\]

where each edge \(e\) in the route \(r(o,d\) has a stochastic travel-time distribution \(p(\tau\_e\).
However, since:

* the route \(r\) itself is not deterministic (drivers may deviate),
* road segments exhibit spatial correlation,
* and real-time interventions (pricing, rebalancing) affect traffic,

the system must jointly infer a *latent traffic field* \(\tau\_e(t\) across the road network.

This transforms the ETA problem into a **spatiotemporal graph inference** task with embedded uncertainty propagation.

---

## 3. System Overview

```
                    ┌──────────────────────────────────────────────┐
                    │               TELEMETRY LAYER                │
                    │  GPS traces, routing events, map updates     │
                    └──────────────────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────┐
                    │           DATA & FEATURE LAYER               │
                    │  - Map matching via HMM                      │
                    │  - Temporal aggregation (Flink/Spark)        │
                    │  - Weather/Event augmentation                │
                    └──────────────────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────┐
                    │        SEGMENT-LEVEL ESTIMATION MODEL        │
                    │  Graph + Temporal Encoder + Probabilistic    │
                    │  Head → LogNormal(μ,σ) for τ_e(t)            │
                    └──────────────────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────┐
                    │         ROUTE-LEVEL AGGREGATION ENGINE       │
                    │  Copula-based Monte Carlo or Covariance Prop │
                    │  → p(T_r) over candidate routes              │
                    └──────────────────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────┐
                    │      GLOBAL CALIBRATION & BIAS CORRECTION    │
                    │  Shallow bias network, isotonic adjustment   │
                    │  → final calibrated p(T)                     │
                    └──────────────────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────┐
                    │     INFERENCE + SERVING INFRASTRUCTURE       │
                    │  - ONNX Runtime, TensorRT                    │
                    │  - Cache-aware route DAG inference           │
                    └──────────────────────────────────────────────┘
                                         │
                                         ▼
                    ┌──────────────────────────────────────────────┐
                    │       MONITORING + RETRAINING LOOP           │
                    │  Drift detection, calibration audits,        │
                    │  automatic retraining triggers               │
                    └──────────────────────────────────────────────┘
```

This pipeline transforms raw GPS telemetry into calibrated, uncertainty-aware ETAs.

---

## 4. Data Plane: From Telemetry to Features

### 4.1 Map-Matching and Segmentization

Raw GPS pings are converted into segment-level trajectories via a **Hidden Markov Model (HMM)**:

\[p(s\_{1:T} | x\_{1:T}) \propto \prod\_t p(x\_t | s\_t) p(s\_t | s\_{t-1})\]

where \(x\_t\) are GPS observations and \(s\_t\) are latent segment IDs.
Emission probabilities depend on geodesic distance; transition probabilities on network connectivity.
Viterbi decoding yields the most likely segment sequence.

### 4.2 Feature Generation

For each segment \(e\):

* **Instantaneous velocity:** from recent GPS deltas.
* **Rolling congestion factor:** \(\frac{v\_{\text{short}}}{v\_{\text{long}}}\).
* **Temporal embeddings:** hour-of-day, day-of-week.
* **Spatial features:** neighbor segment mean speeds.
* **Context features:** rain, temperature, event embeddings.

### 4.3 Storage and Retrieval

All processed features enter **Michelangelo’s Feature Store**, enabling:

* consistent offline/online feature use,
* schema versioning,
* temporal point-in-time joins (avoid lookahead bias).

---

## 5. Segment-Level Model

### 5.1 Input/Output Formalism

Input: \(x\_e(t) \in \mathbb{R}^d\), features of segment e at time t.
Output: parameters \(\mu\_e(t), \sigma\_e(t)\) defining a LogNormal predictive distribution.

\(f\_\theta: x\_e(t) \mapsto [\mu\_e(t), \sigma\_e(t)]\)
\(\tau\_e(t) \sim \text{LogNormal}(\mu\_e(t), \sigma\_e(t))\)

### 5.2 Architecture

```
x_e(t) ─► Temporal LSTM Encoder ─► h_t
          ↑
Neighboring segments ─► Graph Convolution ─► h_spatial
                │
                └────► Concatenate(h_t, h_spatial) ─► MLP ─► μ, σ
```

* **Graph Convolution:** propagates speed context across adjacent segments:
  \(h\_e^{(l+1)} = \sigma\left(W\_1 h\_e^{(l)} + \sum\_{u \in \mathcal{N}(e)} W\_2 \frac{h\_u^{(l)}}{\sqrt{d\_e d\_u}}\right)\)
* **Temporal Encoder:** captures inertia and periodicity in traffic.
* **Output Head:** predicts \(\mu\_e, \sigma\_e\), regularized to avoid overconfidence.

### 5.3 Objective

Negative log-likelihood for LogNormal:

\(\mathcal{L}\_{\text{NLL}} = -\sum\_i \log \frac{1}{T\_i \sigma\_i \sqrt{2\pi}} e^{-\frac{(\log T\_i - \mu\_i)^2}{2\sigma\_i^2}}\)
with smoothness and KL regularizers.

### 5.4 Bayesian Hierarchy for Sparsity

To stabilize low-sample segments:

\[\mu\_e \sim \mathcal{N}(\mu\_{\text{type}(e)}, \sigma\_{\text{type}}^2), \quad
\mu\_{\text{type}} \sim \mathcal{N}(\mu\_0, \sigma\_0^2)\]

This ensures partial pooling: urban arterials share parameters, rural roads share another.

---

## 6. Route-Level Inference Engine

The route-level ETA engine fuses segment predictions into trip-level distributions.

### 6.1 Correlated Aggregation

Assuming joint Gaussian copula:

\(p(\tau\_1,...,\tau\_n) = C\_\Sigma(F\_1(\tau\_1),...,F\_n(\tau\_n)) \prod\_i f\_i(\tau\_i)\)
Monte Carlo samples approximate:
\(E[T\_r] = E[\sum\_i \tau\_i], \quad \text{Var}(T\_r) = \text{Var}(\sum\_i \tau\_i)\)

Covariance matrix \(\Sigma\) is low-rank factored via learned kernel:
\(\Sigma\_{ij} = \exp(-\alpha \cdot \text{dist}(e\_i,e\_j))\)

### 6.2 Risk-Aware Routing Objective

ETA is used within route optimization:
\(r^\* = \arg\min\_r E[T\_r] + \lambda \text{Var}(T\_r)\)

This penalizes uncertain (volatile) paths, improving reliability.

---

## 7. Calibration and Bias Correction

Residual biases from driver behavior or GPS noise are corrected by a post-hoc bias model:

\[\hat{T}\*{\text{final}} = g\_{\phi}(\hat{T}\*{\text{route}}, \1\_{\2}}, c\_t)\]

Trained on rolling historical logs using:
\(\mathcal{L}\_{\text{calib}} = \sum\_b\)\hat{p}\_b - p\_b^{\text{target}}\(^2\)
where \(\hat{p}\_b\) are predicted quantiles.

**Outputs:** calibrated mean and interval coverage (e.g., 90% CI matches 90% empirical coverage).

---

## 8. System Infrastructure and Training

### 8.1 Distributed Training Cluster

* **Data parallelism:** partition by city-region.
* **Model parallelism:** graph embeddings distributed across GPU clusters.
* **Trainer orchestration:** via Michelangelo’s Training Orchestrator (K8s + Airflow DAG).
* **Evaluation nodes:** run rolling backtests and calibration diagnostics.

### 8.2 Simulation-based Augmentation

Uber maintains **Traffic Simulators** (Digital Twins) for major cities.
Segment-level models can be stress-tested under simulated anomalies (road closures, heavy rain).
This provides synthetic but physically plausible training data to reduce domain shift.

### 8.3 Continuous Retraining

Triggers for retraining include:

* PSI > 0.1 for traffic features,
* ECE > 0.05 for calibration drift,
* road graph updates detected by Map Service.

Retraining DAG:

1. Backfill data from last 14 days.
2. Refit segment GCN+LSTM.
3. Update bias model.
4. Validate calibration.
5. Deploy to Canary cluster.
6. Auto-promote to production if metrics exceed baseline.

---

## 9. Serving Layer

### 9.1 Runtime Topology

```
Request (o,d,t)
   ↓
Feature Service (Feast/Redis)
   ↓
Segment Inference (TensorRT batch < 5ms)
   ↓
Route Aggregator (C++ engine, SIMD/GPU)
   ↓
Calibration Model (PyTorchServe)
   ↓
Response: p(T) (mean, std, quantiles)
```

### 9.2 Performance and Reliability

* SLA: 30 ms p95 end-to-end.
* Fault Tolerance: fallback to cached mean ETA if model unavailable.
* Streaming updates: short-term congestion features update every 2–3 minutes.
* Autoscaling via Michelangelo Serving Autoscaler.

---

## 10. Monitoring and Governance

### 10.1 Drift and Calibration Dashboards

Metrics monitored continuously:

* KS divergence between predicted and realized ETA distributions.
* PSI for feature drift.
* Calibration curves per city-hour.

### 10.2 Explainability

SHAP analysis identifies which factors (segment density, event signals) most influence ETA variance.
Segment attribution heatmaps help diagnose anomalies.

### 10.3 Governance

* Model lineage tracked via Michelangelo Model Registry.
* Version-controlled route aggregation code.
* Automatic rollback on calibration degradation.
* Retention of prediction logs for audit compliance.

---

## 11. Integration into Marketplace

ETA uncertainty feeds directly into:

* **Pricing Models:** expected fare = base fare + rate × E[ETA].
* **Dispatch Optimization:** driver assignment minimizes expected pickup ETA + variance penalty.
* |  |  |  |
  | --- | --- | --- |
  | **Reliability Scoring:** trip-level risk score = 1 – P( | error | < threshold). |

This integration ensures consistent marketplace behavior even under uncertainty.

---

## 12. End-to-End Feedback Cycle

1. Telemetry and trip outcomes stream into Feature Store.
2. Segment model retrained with updated data.
3. Route aggregator recalibrated using empirical joint variances.
4. Calibration model updated for bias correction.
5. Evaluation → Canary → Production pipeline ensures safety.

---

## 13. Evaluation Metrics

| Category | Metric | Description |
| --- | --- | --- |
| Accuracy | RMSE, MAE | Mean prediction error |
| Calibration | ECE, PICP | Probabilistic reliability |
| Coverage | % trips within ±x s | User-facing trust |
| System | Latency p95 | Real-time SLA |
| Fairness | Error variance across regions | Spatial equity |
| Robustness | Stability under weather/traffic shocks | Simulation validation |

---

## 14. ASCII Diagram – System Architecture with Michelangelo Integration

```
 ┌──────────────────────────────────────────────────────────────────────────────┐
 │                        UBER ETA SYSTEM (MICHELANGELO)                        │
 └──────────────────────────────────────────────────────────────────────────────┘
             ▲
             │
 ┌───────────┴────────────┐
 │      Data Plane        │
 │  - GPS Streams (Kafka) │
 │  - Flink aggregation   │
 │  - Map-Matching (HMM)  │
 │  - Feature Store       │
 └───────────┬────────────┘
             │
             ▼
 ┌───────────────────────────────────────────────────────────┐
 │    Segment-Level Model (GCN + LSTM + LogNormal Head)      │
 │  Input: x_e(t)                                            │
 │  Output: μ_e, σ_e                                         │
 └───────────┬───────────────────────────────────────────────┘
             │
             ▼
 ┌───────────────────────────────────────────────────────────┐
 │    Route Aggregator (Monte Carlo, Copula, Covariance)     │
 │  Combines segment τ_e → trip-level p(T)                   │
 └───────────┬───────────────────────────────────────────────┘
             │
             ▼
 ┌───────────────────────────────────────────────────────────┐
 │  Calibration + Bias Correction                            │
 │  - Shallow g_φ network                                    │
 │  - Ensures unbiased & calibrated predictions              │
 └───────────┬───────────────────────────────────────────────┘
             │
             ▼
 ┌───────────────────────────────────────────────────────────┐
 │  Serving Layer                                             │
 │  - Feature Service                                         │
 │  - Inference (TensorRT, ONNX)                              │
 │  - Route Aggregation Engine                                │
 │  - Latency <30 ms                                          │
 └───────────┬───────────────────────────────────────────────┘
             │
             ▼
 ┌───────────────────────────────────────────────────────────┐
 │  Monitoring & Governance                                   │
 │  - Drift, Calibration, SHAP                                │
 │  - Automated retraining via Michelangelo DAG               │
 │  - Canary & Rollback                                       │
 └───────────┬───────────────────────────────────────────────┘
             │
             ▼
 ┌───────────────────────────────────────────────────────────┐
 │  Feedback Loop                                             │
 │  - Telemetry → Retraining → Deployment                     │
 │  - Continuous calibration                                  │
 └───────────────────────────────────────────────────────────┘
```

---

## 15. Closing Summary

Uber’s ETA optimization system is a **multi-layer probabilistic inference architecture** built atop Michelangelo, blending deep spatiotemporal modeling, Bayesian smoothing, and real-time serving infrastructure.

It combines:

* GCN+LSTM segment models,
* correlated Monte Carlo route aggregation,
* dynamic calibration,
* and continuous feedback loops,
  to yield globally consistent, calibrated ETAs.

This system enables Uber to predict arrival times not just accurately, but **probabilistically faithfully and operationally safely**, forming the foundation for all marketplace control and user trust mechanisms.

---

---

# Unified Pricing–ETA Reinforcement Learning System

*A Joint Control and Forecasting Architecture for the Uber Mobility Marketplace*

---

## 1. Motivation and Problem Context

In isolation, pricing and ETA models optimize different targets:

* **Pricing RL** seeks to maximize revenue and balance the market via surge multipliers.
* **ETA forecasting** predicts travel and pickup durations.

In reality, they’re *causally coupled*:

* Higher surge → drivers relocate → ETA distributions change → rider acceptance changes → supply-demand equilibrium shifts → future surge re-optimizes.
* ETA errors → wrong perceived friction → distorted demand elasticity estimates → miscalibrated pricing.

Thus, to achieve stability and long-term equilibrium, **price** and **ETA** must form a *closed feedback loop*:

* Pricing must *account for ETA uncertainty* (delay risk as cost).
* ETA must *condition on surge-induced routing patterns* and *supply movements*.

This motivates a **joint learning and control framework** where the policy optimizes expected reward under uncertain dynamics parameterized by the ETA distributions.

---

## 2. Formalizing the Coupling

Let:

* \(s\_t\): state of the marketplace at time \(t\),
* \(a\_t = m\_t(z\): surge field chosen by policy \(\pi\_\theta\),
* \(\tau\_t(z\): random ETA from origin zone \(z\) given \(s\_t, a\_t\),
* \(r\_t\): immediate reward (e.g., GMV minus penalties),
* \(c\_t\): service-level costs (wait times, cancellations).

The transition model becomes:

\[s\_{t+1} \sim P(s\_{t+1} | s\_t, a\_t, \tau\_t), \quad \tau\_t \sim p\_\phi(\cdot | s\_t, a\_t)\]

Here \(p\_\phi\) is the ETA predictive model parameterized by its own parameters \(\phi\).
The policy optimization objective incorporates ETA uncertainty:

\[\max\_\theta E\_{\pi\_\theta, p\_\phi}\Big[\sum\_t \gamma^t (r\_t - \lambda\_1 c\_t - \lambda\_2 U(\tau\_t))\Big]\]

where \(U(\tau\_t\) is a *risk penalty functional* of the ETA distribution, such as variance or quantile deviation.

---

## 3. Why Uncertainty Matters

A deterministic ETA (mean-only) ignores variance.
But riders and drivers care about **risk**, not just expectation.
Late arrivals degrade trust disproportionately compared to early arrivals (asymmetric loss).

We define **risk-adjusted reward**:

\[R\_t = E[T\_t] + \beta \cdot \text{Var}[T\_t] + \gamma \cdot \max(0, T\_t - T\_{\text{promised}})^2\]

This transforms ETA variance into an implicit *cost of unreliability*.
Pricing policies trained with this term naturally learn to dampen surge in regions with volatile ETAs — trading some revenue for predictability.

---

## 4. Joint Architecture Overview

```
                    +-------------------------------+
                    |        Real-Time Data          |
                    +---------------+----------------+
                                    |
                                    v
                 +-------------------------------------------+
                 |   ETA Forecasting Model p(τ | s,a)        |
                 |  (GCN+LSTM, LogNormal output)             |
                 +-------------------------------------------+
                                    |
                   Uncertainty (μ, σ, Cov[τ])
                                    |
                                    v
+------------------------------------------------------------+
|               RL Marketplace Controller πθ                 |
|   Actor (UNet + Attention)                                 |
|   Critic (Value + ETA cost critics)                        |
|   Objective: E[r - λ₁c - λ₂U(τ)]                           |
+------------------------------------------------------------+
                                    |
                                    v
                 +-------------------------------------------+
                 |   Constraint Projection Layer (QP)        |
                 +-------------------------------------------+
                                    |
                                    v
                          Marketplace Serving
```

Conceptually:

* ETA model acts as a **stochastic dynamics generator**.
* RL policy acts as a **risk-sensitive controller**.
* They are trained in alternation or jointly via shared simulation.

---

## 5. Algorithmic Formulation

### 5.1 Joint Distribution Modeling

We treat the marketplace as a **partially observable stochastic system**:

\[p(s\_{t+1}, \tau\_t | s\_t, a\_t) = p(s\_{t+1} | s\_t, a\_t, \tau\_t) , p(\tau\_t | s\_t, a\_t)\]

|  |  |
| --- | --- |
| The ETA model provides $$p\_\phi(\tau\_t | s\_t, a\_t\(, while the RL policy optimizes over\)a\_t$$. |

### 5.2 Risk-Aware RL Objective

Define cumulative reward:

\[J(\theta) = E\_{\pi\_\theta,p\_\phi}\Big[\sum\_t \gamma^t (r\_t - \lambda\_1 c\_t - \lambda\_2 , \rho(\tau\_t))\Big]\]

where \(\rho(\tau\_t\) is a risk measure, such as:

* variance penalty: \(\rho(\tau\_t) = \text{Var}[\tau\_t]\),
* |  |  |
  | --- | --- |
  | CVaR (Conditional Value at Risk): $$\rho(\tau\_t) = E[\tau\_t | \tau\_t > q\_{0.9}]$$, |
* entropy penalty: encourages deterministic, reliable ETAs.

Gradient estimate via policy gradient theorem:

\[\nabla\_\theta J(\theta) = E[\nabla\_\theta \log \pi\_\theta(a\_t|s\_t) (R\_t - b\_t)]\]

but \(R\_t\) includes terms depending on ETA uncertainty, so we propagate stochastic ETA samples through reparameterization:
\(\tau\_t = \mu\_\phi(s\_t,a\_t) + \sigma\_\phi(s\_t,a\_t) \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0,I)\)

### 5.3 Actor–Critic Update

Critic learns *risk-augmented value*:

\[V\_\psi(s\_t) = E[r\_t - \lambda\_1 c\_t - \lambda\_2 \rho(\tau\_t) + \gamma V\_\psi(s\_{t+1})]\]

The ETA variance now directly enters the TD target — effectively teaching the critic to predict both economic and reliability impacts of surge.

### 5.4 Dual Optimization Loop

We can co-train \(\phi\) (ETA) and \(\theta\) (pricing) in alternating fashion:

1. **ETA Phase:**
   Fix \(\pi\_\theta\), update \(\phi\) to maximize ETA likelihood and calibration:
   \(\max\_\phi E[-\log p\_\phi(\tau|s,a)] + \alpha \cdot \text{calib\_loss}\)
2. **RL Phase:**
   Fix \(p\_\phi\), update \(\pi\_\theta\) with ETA uncertainty as part of reward.

Optionally, fine-tune both jointly with stochastic gradients.

---

## 6. Simulator Coupling

The simulator is extended to sample from ETA distributions rather than using static means.
Each simulation step:

1. Query ETA model for each (driver, route) pair.
   \(\mu,\sigma) = f\_\phi(s\_t,a\_t\)
2. Sample travel time \(\tau \sim \text{LogNormal}(\mu,\sigma\).
3. Advance environment time by \(\tau\).
4. Compute reward/cost from realized delays.

This stochasticity forces RL to experience uncertainty, teaching robustness against ETA variance — crucial for urban chaos (accidents, weather, protests).

---

## 7. Theoretical Perspective: Robust and Distributional RL

### 7.1 Distributional Value Function

Instead of a scalar value \(V(s\), we model a **value distribution** \(Z(s,a\), representing the full distribution of returns given stochastic ETAs.

\[Z(s,a) = r\_t - \lambda\_2 \rho(\tau\_t) + \gamma Z(s',a')\]

Learned via quantile regression (QR-DQN or IQN).
The critic thus estimates quantiles of long-term reward, capturing how ETA risk propagates temporally.

### 7.2 Robust Control Interpretation

We can interpret ETA uncertainty as environment noise.
The optimization problem becomes:

\[\max\_\pi \min\_{p\_\phi \in \mathcal{P}} E\_{p\_\phi,\pi}[r - \lambda c]\]

where \(\mathcal{P}\) is a set of plausible ETA distributions around empirical estimates.
This leads to *robust RL* behavior — policies that hedge against ETA estimation errors.

---

## 8. Engineering Implementation

### 8.1 Model Interfaces

ETA model runs as a service:

* Input: (state tensor, proposed surge field)
* Output: (mean, variance) per zone

RL policy consumes these outputs via gRPC with caching for spatial proximity.
At training time, both components run locally in TensorFlow/PyTorch simulation.

### 8.2 Training Loop

```
for epoch in range(E):
    for batch in replay_buffer:
        τ_samples = ETA_model.sample(batch.states, batch.actions)
        rewards = compute_rewards(batch, τ_samples)
        critic_loss = MSE(critic(batch.states), rewards)
        actor_loss = -mean(log_prob(actor(batch.states))*advantage)
        update(critic, critic_loss)
        update(actor, actor_loss)
    update(ETA_model, ETA_loss)
```

### 8.3 Serving-Time Integration

At inference:

1. Pricing policy proposes surge field.
2. ETA service predicts mean/variance.
3. Policy re-evaluates cost term \(U(\tau\) (simple variance penalty).
4. Final projected prices output to marketplace.

This creates a **feedback-corrected policy** — surge values adapt based not only on imbalance but also reliability of travel.

---

## 9. Metrics and Evaluation

Joint evaluation now includes both economic and reliability metrics:

* **GMV uplift** (economic objective)
* **Wait-time satisfaction score**
* **ETA calibration** (ECE, PICP)
* **Reliability-adjusted reward:**
  \(E[r] - \lambda\_2 , E[\rho(\tau)]\)
* **Temporal stability:**
  auto-correlation of surge over time (lower = smoother).
* **Safety metrics:**
  constraint violations in ETA fairness (urban vs. suburban bias).

Offline tests run via **doubly robust OPE** extended for stochastic dynamics; online A/B includes joint lag metrics (e.g., mean rider complaint latency).

---

## 10. Alternative Architectures and Tradeoffs

| Design Dimension | Alternative | Chosen | Rationale |
| --- | --- | --- | --- |
| ETA → RL interface | Mean-only ETA | Distributional ETA | Enables risk-aware pricing |
| Joint training | Sequential (ETA first) | Alternating updates | Stabilizes co-training |
| Uncertainty handling | Dropout uncertainty | Explicit parametric LogNormal | Calibrated, interpretable |
| RL formulation | Deterministic PPO | Distributional constrained PPO | Captures ETA-driven reward variance |
| Serving | Decoupled services | Cached interleaved inference | Balances latency vs. coherence |
| Risk penalty | None | CVaR / Variance | Explicitly trades risk vs. reward |

---

## 11. Intuitive Analogy

Imagine surge pricing as a **pilot** and ETA as the **weather radar**.
If the radar reports high turbulence (ETA variance), the pilot doesn’t fly the shortest path — she chooses the stable route that minimizes expected shock.
Similarly, risk-aware pricing reduces surge aggressiveness in volatile traffic conditions, improving reliability and user trust, even at a small cost in immediate revenue.

Over time, the coupled system learns equilibrium:
high congestion zones get stabilized, driver repositioning anticipates ETA patterns, and rider satisfaction metrics rise without explicit hardcoding.

---

## 12. Theoretical Summary

Combined system solves a **stochastic constrained optimization**:

\[\begin{aligned}
\max\_{\pi} \ & E\_{\pi,p\_\phi}\Big[\sum\_t \gamma^t (r\_t - \lambda\_1 c\_t - \lambda\_2 U(\tau\_t))\Big] \
\text{s.t.} \ & m\_{\min} \le m\_t \le m\_{\max}, \ |m\_t - m\_{t-1}| \le \Delta\_{\max}
\end{aligned}\]

Gradient of objective wrt. policy parameters \(\theta\):

\[\nabla\_\theta J = E\big[\nabla\_\theta \log \pi\_\theta(a\_t|s\_t) (r\_t - \lambda\_1 c\_t - \lambda\_2 U(\tau\_t) - V(s\_t))\big]\]

Gradient wrt. ETA parameters \(\phi\):

\[\nabla\_\phi J = -E\big[\lambda\_2 \nabla\_\phi U(\tau\_t) + \nabla\_\phi \log p\_\phi(\tau\_t|s\_t,a\_t)\big]\]

This is a **bi-level optimization** problem — inner level (ETA model) defines environment dynamics; outer level (policy) optimizes control under those dynamics.

---

## 13. Deployment and Monitoring

**Rollout:**

* Joint models versioned together (pricing-RL v\_k, ETA v\_k).
* Canary rollouts on a few cities to monitor feedback stability.

**Monitoring:**

* Cross-correlation of surge and ETA error.
* Divergence between predicted and observed ETA variance under new surge levels.
* GMV vs. reliability Pareto frontier visualization — helps product decide where to operate.

**Self-healing:**
If ETA model drifts (e.g., post-storm regime change), policy falls back to deterministic baseline via KL regularization to last safe policy.

---

## 14. Broader System Implications

This coupling enables **predictive control**:
pricing doesn’t just react to observed imbalance but *anticipates* imbalance propagation via ETA forecasts.
The system thus becomes **proactive**, not reactive — Uber starts moving drivers *before* ETAs degrade.

Economically, this stabilizes demand elasticity, reduces cancellation churn, and increases long-term retention by improving perceived reliability — a key competitive differentiator.

---

## 15. Closing Summary

* The **ETA model** supplies a distributional, uncertainty-aware forecast of travel time.
* The **RL policy** uses that uncertainty as a soft penalty within its reward function.
* Together they form a *robust, risk-sensitive, closed-loop controller* for the Uber marketplace.
* Mathematically, this is a constrained stochastic optimal control problem solved via alternating stochastic gradient descent.
* Practically, it manifests as a pair of online services exchanging predictions and corrections at sub-second latency to drive billions of pricing decisions per day.

The final result: a marketplace that *learns to price not just for efficiency, but for reliability*, intelligently balancing speed, earnings, and trust across a highly dynamic, global transportation graph.

---

# Marketplace Simulation and Joint Training Framework

*A Distributed, Stochastic, and Risk-Aware Learning Infrastructure for Uber Pricing + ETA Optimization*

---

## 1. Purpose and Design Philosophy

The marketplace is a **non-stationary, coupled dynamical system**:

* rider demand and driver supply co-evolve;
* ETA and surge influence each other;
* policy interventions have delayed, nonlinear effects.

It is *impossible* to train robust policies using only direct online A/B testing — that would risk real riders’ experience.
Therefore, Uber uses an **offline simulation and replay environment**, faithfully reproducing the physics and stochasticity of the real marketplace, to train and test policies before rollout.

This environment must:

1. Model stochastic transitions (ETA distributions, cancellations, relocations).
2. Reproduce causal dependencies between pricing, matching, and routing.
3. Support distributed rollouts for millions of simulated episodes per hour.
4. Provide unbiased off-policy evaluation and confidence bounds.
5. Support both **model-based RL** (using learned dynamics) and **model-free RL** (learning directly from simulation traces).

---

## 2. Hierarchical Simulation Overview

```
                           +-------------------------------------------+
                           |            Global Coordinator             |
                           |   (Policy manager, job scheduler)         |
                           +-------------------+-----------------------+
                                               |
               +-------------------------------+-------------------------------+
               |                                                               |
    +-------------------------+                                     +-------------------------+
    |   City Simulator (NYC)  |                                     |  City Simulator (Paris)  |
    |  - Demand generation    |                                     |  - ETA, weather, events  |
    |  - Driver agents        |                                     |  - Rider behavior model  |
    |  - Routing engine       |                                     |  - RL policy injection   |
    +-----------+-------------+                                     +-----------+-------------+
                |                                                               |
                v                                                               v
       +---------------------+                                         +---------------------+
       |  Micro-simulator    |                                         |  Micro-simulator    |
       |  (Zone-level envs)  |                                         |  (Zone-level envs)  |
       +---------------------+                                         +---------------------+
```

**Multi-level simulation design:**

* The **global coordinator** runs multiple city environments concurrently on distributed compute nodes.
* Each **city simulator** replicates macro phenomena (demand curve, supply pool evolution, event schedule).
* Each **micro-simulator** models individual trip requests, driver movements, and routing on the local road graph.

This architecture enables high-fidelity, stochastic rollouts at scale while preserving modularity — any component (ETA, demand model, routing policy) can be replaced independently.

---

## 3. Simulation State Representation

At time step \(t\), the simulator maintains a hierarchical state:

\[s\_t = { S\_t^{(macro)}, S\_t^{(meso)}, S\_t^{(micro)} }\]

where:

* \(S\_t^{(macro)}\): city-level aggregates (active riders/drivers per region, surge history, weather, events).
* \(S\_t^{(meso)}\): zone-level features (supply–demand ratio, average ETA mean/variance, local revenue).
* \(S\_t^{(micro)}\): agent-level states (driver positions, current trip progress, route path).

This state evolves via stochastic transitions conditioned on the RL policy’s surge actions \(a\_t = m\_t(z\).

---

## 4. Dynamics Model

|  |  |
| --- | --- |
| The transition probability $$P(s\_{t+1} | s\_t, a\_t$$ decomposes into causal submodels: |

\[P(s\_{t+1} | s\_t, a\_t) = P(D\_{t+1}|s\_t,a\_t) \cdot P(\text{Supply}\*{t+1}|s\_t,a\_t,\1\_{\2}) \cdot P(\text{ETA}\_{t+1}|s\_t,a\_t)\]

### Components:

* **Demand generator:**
  \(D\_{t+1}(z) \sim \text{Poisson}(\hat{\lambda}(z,t) \cdot g(m\_t(z))\),
  where \(g\) is elasticity function learned via hierarchical Bayes.
* **Supply updater:**
  drivers reposition stochastically according to observed relocation patterns.
* **ETA module:**
  draws \(\tau\_t(z) \sim p\_\phi(\cdot | s\_t, a\_t\) from the trained ETA model.

This probabilistic transition captures both *expected outcomes* and *variance propagation* — essential for risk-sensitive RL.

---

## 5. Agent-Based Simulation Loop

Each micro-simulator executes the following core loop:

```
for t in time_horizon:
    observe s_t
    a_t = πθ(s_t)                # surge policy action
    τ_t ~ ETA_model(s_t, a_t)    # sample ETA distribution
    D_t ~ Demand_model(s_t, a_t)
    drivers = match(D_t, Supply_t, τ_t)
    r_t, c_t = compute_rewards(drivers, riders)
    s_{t+1} = update_state(s_t, a_t, D_t, drivers, τ_t)
    store (s_t, a_t, r_t, c_t, τ_t, s_{t+1})
```

Each simulated time step represents ~1–2 minutes of real-world time.
Episodes last several hours to capture long-term equilibria (driver earnings stabilization, rider retention).

---

## 6. Distributed Rollout Infrastructure

### 6.1 Parallelism Model

* **Horizontal sharding:** Each simulator instance runs a separate city or random seed.
* **Vertical vectorization:** Within a city, 10³–10⁴ parallel zone rollouts via batched tensor ops (PyTorch JIT).
* **Coordinator node:** Gathers rollouts, computes policy gradients asynchronously (A3C or IMPALA architecture).

This allows millions of simulated “trip-minutes” per GPU-hour.

### 6.2 Replay Buffer and Experience Store

All transitions \(s,a,r,c,s'\) are stored in a distributed replay buffer (Redis or Ray object store) with priorities based on TD-error magnitude.

Supports **off-policy learning** and **doubly robust OPE**.

---

## 7. Model-Based vs. Model-Free Integration

### 7.1 Model-Based Branch

The ETA model \(p\_\phi\) and demand model \(q\_\psi\) serve as *learned environment models*.
A model-based planner computes policy improvements analytically:

\[a\_{t+1} = \arg\max\_a E\_{p\_\phi,q\_\psi}[r\_t - \lambda\_2 U(\tau\_t) + \gamma V\_\psi(s\_{t+1})]\]

Advantages:

* Sample efficiency (learn from synthetic rollouts).
* Analytical gradients via differentiable simulation.

Limitations:

* Model bias: imperfect ETA/demand models produce optimistic plans.

### 7.2 Model-Free Branch

In parallel, the RL policy learns directly from simulator rollouts (no explicit dynamics model).

Advantages:

* Robust to model bias.
* Captures nonlinear emergent effects.

Tradeoff: high variance, slower convergence.

### 7.3 Hybrid (Dyna-style)

Final system uses **Dyna architecture**:

* Real rollouts from simulator mixed with synthetic rollouts from learned models.
* Synthetic-to-real ratio adaptively tuned via model uncertainty.

---

## 8. Off-Policy Evaluation under Stochastic Dynamics

### 8.1 Problem

We must estimate how a new policy \(\pi'\) would perform under stochastic ETA transitions, given logged data from old policy \(\pi\).

### 8.2 Importance Sampling with ETA Uncertainty

For each trajectory:

\[w\_t = \prod\_{i=0}^t \frac{\pi'(a\_i|s\_i)}{\pi(a\_i|s\_i)} \cdot \frac{p\_\phi'(\tau\_i|s\_i,a\_i)}{p\_\phi(\tau\_i|s\_i,a\_i)}\]

and value estimate:

\[\hat{V}\_{OPE} = \sum\_t \gamma^t w\_t (r\_t - \lambda U(\tau\_t))\]

This accounts for both policy difference and ETA model uncertainty.

### 8.3 Doubly Robust Formulation

Combining model-based and model-free terms for variance reduction:

\(\hat{V}\_{DR} = E[\hat{m}(s,a) + w\_t (r\_t - \hat{m}(s,a))]\)
where \(\hat{m}\) is the reward model estimated from simulation.

This estimator remains unbiased if *either* the model or the importance weights are correct.

---

## 9. Safety-Constrained Training

A critical component is **safe policy learning** — ensuring that no learned surge pattern degrades key SLAs (wait time, fairness).

Implemented via **Constrained Policy Optimization (CPO)**:

\[\begin{aligned}
\max\_\theta \ & E[R\_t] \
\text{s.t.} \ & E[C\_k(s,a)] \le \bar{C}\_k, \quad \forall k
\end{aligned}\]

Solving via Lagrangian dual:

\[L(\theta, \lambda) = E[R\_t] - \sum\_k \lambda\_k(E[C\_k] - \bar{C}\_k)\]

with dual updates:
\(\lambda\_k \leftarrow [\lambda\_k + \eta (E[C\_k] - \bar{C}\*k)]\*+\)

Constraints typically include:

* p95 pickup time ≤ threshold
* surge variance ≤ target
* fairness index (Gini of earnings) ≤ limit

---

## 10. Calibration and Domain Randomization

### 10.1 Calibration

Simulator parameters are calibrated using real-world logs via Bayesian optimization:

\[\min\_\theta | f\_{\text{sim}}(\theta) - f\_{\text{real}} |^2\]

where \(f\) are metrics like trip duration distribution, cancellation rate, driver movement patterns.

### 10.2 Domain Randomization

To prevent the RL agent from overfitting to specific traffic or ETA distributions, we randomize simulator parameters each episode:

* demand elasticity ±10%,
* ETA variance ±20%,
* event frequency noise.

This yields **robust policies** that generalize across conditions.

---

## 11. Training Stability and Curriculum

* **Warm-start from behavior cloning:** Initialize policy by imitating historical pricing.
* **Progressive horizon extension:** start with 15-min rollouts, expand to 6h as variance stabilizes.
* **KL annealing:** gradually loosen divergence constraint from baseline.
* **Multi-objective scheduling:** alternate between maximizing GMV and minimizing ETA risk every N epochs.

---

## 12. System Implementation

### 12.1 Compute Topology

* Simulation pods: GPU-enabled Ray clusters.
* ETA and demand models served locally for low-latency sampling.
* RL policy updates done via distributed gradient aggregation (Horovod / TorchElastic).

### 12.2 Data Flow

```
Simulator --> Rollout logs --> Replay buffer --> Trainer
Trainer --> Updated policy weights --> Simulator
```

ETA and demand models are versioned in model registry; simulator automatically refreshes when new ones are published.

---

## 13. Validation Pipeline

Before deployment, every candidate policy undergoes:

1. **Offline simulation replay:** 10× real-world duration simulated under varied seeds.
2. **Counterfactual replay on logs:** DR-OPE comparison vs. production policy.
3. **Shadow deployment:** runs in parallel in production, logs surge decisions but doesn’t affect pricing.
4. **A/B Canary:** limited cities for 1 week; automatic rollback if:

   * pickup ETA worsens > 5%,
   * GMV volatility > 10%,
   * fairness deviation > 2%.

---

## 14. Monitoring and Diagnostics

* Drift detection on ETA distribution shift (PSI > 0.1 triggers retraining).
* Reward attribution dashboard: contribution of ETA cost term to total objective.
* Simulation–production gap metrics:
  \(|\text{GMV}\*{sim} - \text{GMV}\*{real}| < 3%\).

Logs include per-zone surge, ETA variance, driver acceptance rate, and constraint dual variables.

---

## 15. Theoretical Note: Stochastic Model Predictive Control (MPC) View

The entire system can be interpreted as a **stochastic MPC loop**:

* ETA and demand models define a learned world model \(f\_\phi\).
* RL policy acts as control law \(\pi\_\theta(s\).
* At runtime, we solve:
  \(a\_t^\* = \arg\max\_a E\_{f\_\phi}[r(s,a) - \lambda\_2 U(\tau)]\)
  over a short horizon with receding optimization.

This yields an interpretable, real-time control policy that continuously re-optimizes as new ETA forecasts arrive.

---

## 16. Design Tradeoffs

| Design Question | Option 1 | Option 2 | Chosen | Reason |
| --- | --- | --- | --- | --- |
| Simulator fidelity | Deterministic replay | Stochastic ETA/demand | ✓ | Captures real variance and risk |
| Training mode | Pure model-free RL | Hybrid (Dyna) | ✓ | Balances efficiency and realism |
| OPE method | IS only | Doubly Robust | ✓ | Stable under stochastic transitions |
| Safety | Post-hoc filters | Constrained RL | ✓ | Guarantees ex ante constraint satisfaction |
| Robustness | Fixed simulator | Domain randomization | ✓ | Generalizes to new cities/events |

---

## 17. Intuitive Analogy

Think of the system as a **virtual city lab** — thousands of digital twins of real cities running in parallel, each a sandbox where Uber can experiment safely.
Each simulation run is a “what-if” world:
What if it rains and ETA doubles? What if drivers cluster downtown?
The joint ETA–Pricing agent learns not a single rule, but a **policy distribution** robust to all these futures.

When it finally goes live, it already “knows” how to handle tomorrow’s congestion because it has experienced a thousand stochastic versions of it overnight.

---

## 18. Closing Summary

* The **simulation framework** is the backbone that connects prediction and control.
* It combines **probabilistic ETA modeling**, **agent-based simulation**, and **risk-sensitive reinforcement learning** into a coherent loop.
* It ensures **safety, robustness, and generalization** through domain randomization and constrained optimization.
* It scales globally via distributed rollout infrastructure and principled off-policy evaluation.
* It transforms Uber’s operational ML from reactive modeling into proactive, closed-loop decision-making.

---

# Uber Rider–Driver Matching Optimization System

*A Fully Detailed and Mathematical Architecture for Real-Time Marketplace Matching and Assignment Control*

---

## 1. Context and Objective

The **rider–driver matching problem** lies at the core of Uber’s real-time marketplace control.
At any given instant, there are:

* active drivers \(D = {d\_1, d\_2, ..., d\_m}\)
* active trip requests \(R = {r\_1, r\_2, ..., r\_n}\)

The system must pair a subset of them in real time, while minimizing **global cost** and maximizing **market health**.

Each potential assignment \(r\_i, d\_j\) has an associated **utility**:

\[U\_{ij} = \alpha\_1 \cdot (-\text{pickup\_ETA}\_{ij}) + \alpha\_2 \cdot \text{driver\_score}\*j + \alpha\_3 \cdot \text{rider\_priority}\*i - \alpha\_4 \cdot \text{idle\_distance}\*{ij} + \alpha\_5 \cdot \text{future\_value}\*{ij}\]

The goal is to find an assignment \(M^\* \subseteq R \times D\) maximizing total utility, subject to capacity constraints:

\(M^\* = \arg\max\_M \sum\_{(r\_i,d\_j) \in M} U\_{ij}\)
\(\text{s.t. } d\_j \text{ assigned to at most one rider}, \quad r\_i \text{ assigned to at most one driver.}\)

This is a **dynamic bipartite matching** problem — but the “edges” and utilities change every few seconds, driven by live location updates, ETA predictions, and stochastic future supply.

Hence the system blends:

* **Graph optimization** (assignment),
* **Reinforcement learning** (anticipatory control),
* **Probabilistic forecasting** (supply and demand dynamics),
* **Distributed systems** (low-latency serving).

---

## 2. Problem Formulation: Dynamic Matching as MDP

At each discrete decision epoch \(t\):

State:
\(s\_t = (\text{locations of drivers}, \text{outstanding requests}, \text{ETAs}, \text{historical features})\)
Action:
\(a\_t = \text{assignment matrix } A\_t \in {0,1}^{|R\_t| \times |D\_t|}\)
Transition:
\(s\_{t+1} = f(s\_t, a\_t, \text{new requests}, \text{driver movements})\)
Reward:
\(r\_t = \sum\_{(r\_i,d\_j) \in A\_t} \left(-\text{pickup\_ETA}\_{ij} - \lambda\_1 \cdot \text{rider\_wait\_penalty}\_i + \lambda\_2 \cdot \text{driver\_utilization}\_j \right)\)

We seek the optimal policy \(\pi^\*(s\_t\) that maximizes long-term expected reward:

\[\pi^\* = \arg\max\_\pi E\_\pi \left[ \sum\_t \gamma^t r\_t \right]\]

---

## 3. System Overview

```
 ┌──────────────────────────────────────────────────────────┐
 │                TELEMETRY + REQUEST FEEDS                 │
 │   (Driver GPS, Rider requests, cancellations)            │
 └──────────────────────────────────────────────────────────┘
                        │
                        ▼
 ┌──────────────────────────────────────────────────────────┐
 │         FEATURE AND FORECASTING LAYER                   │
 │   - Real-time ETAs (from ETA system)                    │
 │   - Demand/supply forecasts (ML models)                 │
 │   - Driver state embeddings                             │
 └──────────────────────────────────────────────────────────┘
                        │
                        ▼
 ┌──────────────────────────────────────────────────────────┐
 │        CANDIDATE GENERATION & SCORING ENGINE            │
 │   - Compute U_ij for feasible (r_i, d_j) pairs           │
 │   - Filter by radius, ETA, driver constraints            │
 └──────────────────────────────────────────────────────────┘
                        │
                        ▼
 ┌──────────────────────────────────────────────────────────┐
 │        MATCH OPTIMIZATION (RL + ASSIGNMENT)             │
 │   - Hungarian / Auction algorithm                       │
 │   - RL policy for dynamic tuning of scoring weights      │
 └──────────────────────────────────────────────────────────┘
                        │
                        ▼
 ┌──────────────────────────────────────────────────────────┐
 │      POST-MATCH VALIDATION + DISPATCH SERVICE           │
 │   - Driver ping, trip confirmation                      │
 │   - Retry logic for declines/cancellations              │
 └──────────────────────────────────────────────────────────┘
                        │
                        ▼
 ┌──────────────────────────────────────────────────────────┐
 │       MONITORING + FEEDBACK LOOP                        │
 │   - Matching efficiency, pickup ETA errors, fairness     │
 │   - Reinforcement updates via simulation                 │
 └──────────────────────────────────────────────────────────┘
```

---

## 4. Data Plane and Feature Space

### 4.1 Core Features

Each potential edge \(r\_i, d\_j\) is characterized by:

* Spatial: distance, ETA (from ETA system), shared route fraction.
* Temporal: request age, traffic level, time-of-day embeddings.
* Behavioral: driver acceptance rate, rider patience profile.
* Contextual: surge multiplier, weather, event embeddings.

### 4.2 Driver State Representation

For driver \(d\_j\):

\[z\_j = \text{Encoder}\_\phi(\text{history}\_j, \text{location}\_j, \text{context}\_t)\]

A small RNN embedding encodes session history (accepted/declined requests, idle time).

### 4.3 Demand Forecasting

Short-term demand density \(D(z, t+\Delta\) estimated via a spatio-temporal forecasting model:

\[\hat{D}(z, t+\Delta) = g\_\psi(f\_{\text{traffic}}(z,t), f\_{\text{events}}(z,t), ...)\]

This informs the RL controller about future scarcity — enabling anticipatory assignment rather than purely myopic matching.

---

## 5. Candidate Generation

Given a new rider request \(r\_i\) at location \(o\_i\):

* Identify candidate drivers within radius \(R\_{\text{max}}\) (≈ 5–10 km).
* Compute ETA between \(o\_i\) and each driver location via the **ETA system** (Section above).
* Filter out infeasible drivers (on trip, low battery, incompatible mode).
* Construct edge feature vectors \(x\_{ij}\).

This step runs on **Uber’s spatial index service (H3)** for efficient neighbor lookups.

---

## 6. Utility Scoring Function

Each feasible edge gets a composite utility score:

\[U\_{ij} = w^\top x\_{ij}\]

where \(w\) are tunable weights or outputs of a learned neural scorer.

Optionally, the system learns \(w\) dynamically via **contextual bandits** or **RL policy gradients** to optimize fleet-level performance.

To avoid overfitting, features are standardized and clipped, ensuring monotonic response with respect to ETA and idle distance.

---

## 7. Matching Optimization Layer

### 7.1 Deterministic Matching (Assignment Step)

Given the utility matrix \(U\_{ij}\), the immediate assignment problem is a **maximum-weight bipartite matching**.

For small batches:
\(M^\* = \text{HungarianAlgorithm}(U)\)
Complexity \(O(n^3\), suitable for local pools (<50 drivers).

For large-scale systems (city-wide), Uber uses **Auction Algorithms** or **Min-Cost Flow** formulations over the H3 grid.

---

### 7.2 Stochastic RL Controller (Dynamic Weight Tuning)

To incorporate long-term effects (e.g., preventing starvation of certain zones), an RL controller adjusts utility weights \(w\_t\) in real time:

State:
\(s\_t = (\text{supply distribution}, \text{demand forecast}, \text{recent wait times})\)
Action:
\(a\_t = w\_t \quad (\text{weight vector for U computation})\)
Reward:
\(r\_t = -E[\text{pickup ETA}] - \lambda\_1 \text{rider cancel rate} + \lambda\_2 \text{driver utilization}\)

Policy:
\(\pi\_\theta(s\_t) = w\_t\)
trained via Proximal Policy Optimization (PPO) or policy gradient methods on simulated city environments.

This RL layer **modulates** the deterministic assignment, effectively learning global control parameters (e.g., tradeoff between fairness and efficiency).

---

## 8. Simulation Environment

Like pricing and ETA systems, Uber maintains a **city-scale simulator** that replays trip logs and simulates stochastic request arrivals.

Simulator state includes:

* driver and rider distributions,
* ETA models for each segment,
* acceptance/cancellation probabilities.

Each episode simulates ~1 hour of city activity, generating trajectories \(s\_t, a\_t, r\_t, s\_{t+1}\) for RL updates.

This allows safe training of new matching policies without affecting live operations.

---

## 9. Losses and Learning Objectives

* **RL Objective:**
  \(J(\theta) = E\_\pi \left[ \sum\_t \gamma^t r\_t \right]\)

  with gradient updates via PPO:
  \(\nabla\_\theta J(\theta) \approx E\_t \left[ \frac{\pi\_\theta(a\_t|s\_t)}{\pi\_{\theta\_{\text{old}}}(a\_t|s\_t)} A\_t \right]\)
* **Supervised Calibration Loss:**
  Match model outputs to observed historical matches:
  \(\mathcal{L}\*{\text{sup}} = -\\1\_{\2}} \log \sigma(U\_{ij})\)
* **Fairness Regularizer:**
  Penalize geographic or demographic bias:
  \(\mathcal{L}\*{\text{fair}} = \lambda \cdot \text{Var}\*{z}(\text{match\_prob}(z))\)

Final loss:
\(\mathcal{L} = \mathcal{L}\*{\text{RL}} + \mathcal{L}\*{\text{sup}} + \mathcal{L}\_{\text{fair}}\)

---

## 10. Serving and Deployment

### 10.1 Real-Time Inference Path

```
Rider request arrives
    ↓
Nearby driver lookup via H3 index
    ↓
ETA computation (from ETA model)
    ↓
Feature vector x_ij computed
    ↓
Utility scoring (ML model or tuned weights)
    ↓
Assignment algorithm (Auction / Hungarian)
    ↓
Dispatch + driver app notification
```

Latency target: **<50 ms end-to-end**.

### 10.2 Michelangelo Deployment Stack

* Models registered in **Michelangelo Model Registry** (versioned by city and model type).
* Real-time scoring via **TensorRT** microservices.
* Assignment and dispatch logic implemented in **Go/C++** for sub-millisecond scheduling.
* State synchronization handled by **Redis** and **Kafka** event logs.

---

## 11. Monitoring and Feedback

Metrics:

* **Match rate** (% of requests successfully assigned).
* **Average pickup ETA**.
* **Rider wait time distribution**.
* **Driver idle time**.
* **Fairness index** (variance across zones).
* **RL policy drift** (KL divergence from baseline).

Feedback loop:

* Aggregated logs → training cluster.
* Simulation replay → policy re-evaluation.
* Continuous retraining DAG under Michelangelo orchestrator.

---

## 12. ASCII System Architecture Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                RIDER–DRIVER MATCHING SYSTEM                  │
│             (Michelangelo-Orchestrated ML/RL)                │
└──────────────────────────────────────────────────────────────┘
                   ▲
                   │
        ┌──────────┴───────────┐
        │   TELEMETRY & FEEDS  │
        │  - Rider requests    │
        │  - Driver GPS        │
        │  - Trip completions  │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────────────────────────────┐
        │  FEATURE + FORECAST LAYER                    │
        │  - ETAs from ETA system                      │
        │  - Demand/Supply forecasts                   │
        │  - Driver embeddings                         │
        └──────────┬───────────────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────────────┐
        │  CANDIDATE GENERATION ENGINE                 │
        │  - H3 spatial lookup                         │
        │  - Feasibility filtering                     │
        │  - Edge feature construction                 │
        └──────────┬───────────────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────────────┐
        │  MATCHING OPTIMIZATION                       │
        │  - Deterministic solver (Auction/Hungarian)  │
        │  - RL controller for weight tuning           │
        └──────────┬───────────────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────────────┐
        │  DISPATCH & CONFIRMATION                     │
        │  - Driver notification                       │
        │  - Cancellation handling                     │
        └──────────┬───────────────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────────────┐
        │  MONITORING + RL FEEDBACK                    │
        │  - Matching metrics                          │
        │  - Retraining triggers                       │
        │  - Simulation fine-tuning                    │
        └──────────────────────────────────────────────┘
```

---

## 13. Evaluation Metrics

| Category | Metric | Purpose |
| --- | --- | --- |
| Efficiency | Mean pickup ETA | Responsiveness |
| Coverage | Match rate | Supply-demand balance |
| Fairness | Gini index over wait times | Regional equity |
| Stability | Policy variance | RL safety |
| Throughput | QPS handled per shard | Scalability |
| Business | Trip acceptance, earnings/hour | Economic efficiency |

---

## 14. Governance and Safety

All RL policies undergo:

* Offline simulation replay (stress test with synthetic shocks),
* Canary rollout (small % live users),
* Multi-metric gating (efficiency, fairness, stability),
* Explainability logging (edge-level utility decompositions).

All match decisions are reproducible: every request’s assignment is traceable via:

* Model version,
* Input features,
* Utility vector,
* Policy weights.

---

## 15. Closing Summary

Uber’s Rider–Driver Matching System is a **hierarchical control and inference machine**:

* At the micro level, it solves combinatorial assignment in milliseconds.
* At the macro level, it learns global weight control policies via reinforcement learning.
* At the system level, it continuously retrains via simulation feedback.

Together with the ETA and Pricing systems, it completes Uber’s **triangular control loop**:

```
       ETA ↔ Matching ↔ Pricing
            ↖—— Feedback ——↙
```

forming an **adaptive, self-regulating economic network** operating at planetary scale.

---
