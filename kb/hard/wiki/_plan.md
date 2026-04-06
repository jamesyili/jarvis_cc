# Wiki Compilation Plan — Hard Skills

> Generated: 2026-04-05 (fresh scan with real content)
> Raw articles scanned: 795 across 10 sources
> Concepts identified: 65 (merged from 121 raw candidates across 3 scan agents)
> Existing wiki articles: 10 (will be updated with additional sources)

Review this plan. Edit or remove concepts before compiling.
Mark concepts with `[x]` to approve, `[ ]` to skip.

---

## 1. ML Fundamentals (12 concepts)

- [x] **Neural Network Fundamentals** (`neural-network-fundamentals`) — EXISTING, update
  - Perceptron to MLP, activation functions (ReLU, GELU, SiLU), backpropagation, loss functions, weight initialization.
  - Sources: aman-ai (8+), lilian-weng/an-overview-of-deep-learning-for-curious-people.md
  - Related: neural-network-training, regularization, optimization-algorithms

- [x] **Neural Network Training & Optimization** (`neural-network-training`)
  - Karpathy's training recipe, optimizers (SGD→Adam→AdamW), LR schedules, debugging, overfitting paradox.
  - Sources: karpathy/a-recipe-for-training-neural-networks.md, lilian-weng (2), aman-ai (5+), cameron-wolfe/a-guide-for-debugging-llm-training-data.md
  - Related: neural-network-fundamentals, distributed-training, regularization

- [x] **Regularization & Overfitting** (`regularization`)
  - L1/L2, dropout, batch/layer norm, data augmentation, early stopping, bias-variance tradeoff.
  - Sources: aman-ai (6+)
  - Related: neural-network-fundamentals, neural-network-training

- [x] **Optimization Algorithms** (`optimization-algorithms`)
  - SGD variants, momentum, RMSProp, Adam, AdaGrad, second-order methods, convergence behavior.
  - Sources: aman-ai (4+)
  - Related: neural-network-training, learning-rate-scheduling

- [x] **Decision Trees & Ensemble Methods** (`decision-trees-ensembles`)
  - CART, random forests, gradient boosting (XGBoost, LightGBM), their role in ranking pipelines.
  - Sources: aman-ai (4+)
  - Related: learning-to-rank, feature-engineering

- [x] **Supervised Learning Algorithms** (`supervised-learning`)
  - Linear/logistic regression, SVMs, Naive Bayes — unified treatment before deep models.
  - Sources: aman-ai (7+)
  - Related: neural-network-fundamentals, decision-trees-ensembles

- [x] **Unsupervised Learning & Clustering** (`unsupervised-learning`)
  - K-means, hierarchical clustering, PCA, EM algorithm.
  - Sources: aman-ai (4+)
  - Related: embeddings-and-representation-learning

- [x] **Reinforcement Learning** (`reinforcement-learning`) — EXISTING, update
  - MDP, value-based (Q-learning, DQN), policy gradient (REINFORCE, PPO), actor-critic, exploration.
  - Sources: lilian-weng (5), aman-ai (4), karpathy/deep-reinforcement-learning-pong-from-pixels.md
  - Related: bandits-exploration-exploitation, rl-for-llms

- [x] **Distributed Training & Memory Optimization** (`distributed-training`)
  - Data/model/pipeline parallelism, ZeRO, gradient checkpointing, mixed precision, DeepSpeed.
  - Sources: aman-ai (3), lilian-weng/how-to-train-really-large-models-on-many-gpus.md, sebastian-raschka (1)
  - Related: large-language-models, scaling-laws

- [x] **Loss Functions** (`loss-functions`)
  - Cross-entropy, MSE, hinge, contrastive/triplet, ranking losses — task-appropriate selection.
  - Sources: aman-ai (4+)
  - Related: neural-network-training, learning-to-rank, embeddings-and-representation-learning

- [x] **Transfer Learning & Fine-Tuning** (`transfer-learning`)
  - Pretraining/fine-tuning paradigm, layer freezing, LoRA, adapters, prefix tuning, domain adaptation.
  - Sources: aman-ai (4+), cameron-wolfe (1), chip-huyen (1)
  - Related: large-language-models, rl-for-llms

- [x] **Self-Supervised & Contrastive Learning** (`self-supervised-contrastive`)
  - SimCLR, MoCo, BYOL, CLIP, contrastive loss — learning representations without labels.
  - Sources: lilian-weng (2), chip-huyen (1)
  - Related: embeddings-and-representation-learning, multimodal-models

---

## 2. NLP & Language Models (12 concepts)

- [x] **Transformer Architecture** (`transformer-architecture`) — EXISTING, update
  - Self-attention, multi-head attention, GQA/MQA/MLA, FlashAttention, KV cache, positional encoding (RoPE, ALiBi).
  - Sources: aman-ai (4+), lilian-weng (2), jay-alammar (1), sebastian-raschka (3), cameron-wolfe (1)
  - Related: large-language-models, embeddings-and-representation-learning

- [x] **Large Language Models** (`large-language-models`) — EXISTING, update
  - GPT, Claude, Gemini, LLaMA, DeepSeek, Qwen. Scaling laws, Chinchilla, context extension, post-benchmark era.
  - Sources: aman-ai (5+), sebastian-raschka (3), nathan-lambert (4), cameron-wolfe (1), lilian-weng (1)
  - Related: transformer-architecture, rl-for-llms, llm-evaluation

- [x] **LLM Post-Training & Alignment** (`llm-post-training`)
  - SFT, RLHF pipeline, reward modeling, DPO, KTO, preference optimization.
  - Sources: aman-ai (3), cameron-wolfe (4), nathan-lambert (2), lilian-weng (1), chip-huyen (1)
  - Related: rl-for-llms, large-language-models

- [x] **RL for LLMs** (`rl-for-llms`) — EXISTING, update
  - PPO for LLMs, REINFORCE/RLOO, GRPO, DeepSeek-R1 pipeline, reasoning models, RLVR.
  - Sources: cameron-wolfe (4), sebastian-raschka (3), aman-ai (1), nathan-lambert (1)
  - Related: reinforcement-learning, llm-post-training, large-language-models

- [x] **LLM Evaluation** (`llm-evaluation`) — EXISTING, update
  - LLM-as-judge, benchmarks, eval-driven development, statistical rigor, post-benchmark era.
  - Sources: eugene-yan (7), aman-ai (3), cameron-wolfe (2), sebastian-raschka (1), nathan-lambert (1)
  - Related: large-language-models, llm-hallucination

- [x] **Mixture of Experts (MoE)** (`mixture-of-experts`)
  - Sparse routing, load balancing, expert capacity. Switch Transformers → DeepSeek V3.
  - Sources: aman-ai (2), cameron-wolfe (2), sebastian-raschka (2), nathan-lambert (1)
  - Related: transformer-architecture, distributed-training

- [x] **Reasoning Models & Inference-Time Scaling** (`reasoning-models`)
  - o1, DeepSeek-R1, extended thinking, test-time compute, best-of-N, self-consistency.
  - Sources: cameron-wolfe (1), sebastian-raschka (3), aman-ai (2)
  - Related: rl-for-llms, large-language-models

- [x] **Prompt Engineering & In-Context Learning** (`prompt-engineering`)
  - Zero/few-shot, chain-of-thought, structured prompting, temperature/top-k/top-p.
  - Sources: aman-ai (2), lilian-weng (1), chip-huyen (1), sebastian-raschka (1)
  - Related: large-language-models, retrieval-augmented-generation

- [x] **Sequence Models (RNN/LSTM/SSM)** (`sequence-models`)
  - Vanilla RNN, LSTM gates, GRU, state space models (Mamba) — pre-transformer sequence modeling.
  - Sources: aman-ai (3+)
  - Related: transformer-architecture, attention-mechanism

- [x] **LLM Inference & Serving** (`llm-inference-serving`)
  - KV cache, speculative decoding, quantization, continuous batching, throughput/latency trade-offs.
  - Sources: aman-ai (5+), sebastian-raschka (1), lilian-weng (1), louis-wang (3)
  - Related: distributed-training, model-compression, mixture-of-experts

- [x] **Model Compression & Quantization** (`model-compression`)
  - INT8/INT4, pruning, knowledge distillation, on-device deployment.
  - Sources: aman-ai (3), louis-wang (1)
  - Related: llm-inference-serving, transfer-learning

- [x] **LLM Hallucination** (`llm-hallucination`)
  - Taxonomy, causes, measurement, mitigation (RAG, self-consistency, NLI checks).
  - Sources: lilian-weng (1), chip-huyen (1), eugene-yan (2)
  - Related: llm-evaluation, retrieval-augmented-generation

---

## 3. Recommendation Systems (14 concepts)

- [x] **Recommendation Systems** (`recommendation-systems`) — EXISTING, update
  - End-to-end funnel (retrieval → ranking → reranking), architecture patterns, production considerations.
  - Sources: aman-ai (10+), eugene-yan (4), louis-wang (2)
  - Related: two-tower-retrieval, learning-to-rank, reranking

- [x] **Two-Tower Retrieval** (`two-tower-retrieval`) — EXISTING, update
  - Dual encoder, training (in-batch/hard negatives), ANN serving, cross-tower limitation.
  - Sources: aman-ai (7), eugene-yan (3), louis-wang (1)
  - Related: recommendation-systems, embeddings-and-representation-learning, approximate-nearest-neighbor

- [x] **Learning to Rank** (`learning-to-rank`) — EXISTING, update
  - Pointwise/pairwise/listwise, deep ranking models (W&D, DCN, DeepFM, DHEN), calibration.
  - Sources: aman-ai (8), eugene-yan (2)
  - Related: recommendation-systems, feature-engineering, decision-trees-ensembles

- [x] **Reranking & Multi-Objective Optimization** (`reranking`)
  - Post-ranking for diversity, freshness, fairness. Pareto-optimal trade-offs, MOO vs MAB.
  - Sources: aman-ai (4+), eugene-yan (2)
  - Related: recommendation-systems, bandits-exploration-exploitation

- [x] **Bandits & Exploration-Exploitation** (`bandits-exploration-exploitation`) — EXISTING, update
  - MAB, UCB, Thompson Sampling, contextual bandits, explore-exploit in recsys.
  - Sources: lilian-weng (2), eugene-yan (3), aman-ai (2)
  - Related: reinforcement-learning, recommendation-systems

- [x] **RecSys Embeddings & Collaborative Filtering** (`recsys-embeddings`)
  - User/item embeddings, matrix factorization, NCF, GNNs (PinSage), cold start.
  - Sources: aman-ai (6+), eugene-yan (2), louis-wang (1)
  - Related: two-tower-retrieval, embeddings-and-representation-learning

- [x] **RecSys Evaluation & Bias** (`recsys-evaluation`)
  - NDCG, MAP, precision@K, position bias, exposure bias, calibration, offline vs online eval.
  - Sources: aman-ai (5+), eugene-yan (3)
  - Related: recommendation-systems, learning-to-rank, a-b-testing

- [x] **LLMs in Recommendation Systems** (`llm-recsys`)
  - Semantic retrieval, generative ranking, BERT4Rec, SASRec, semantic IDs, HSTU.
  - Sources: aman-ai (3), louis-wang (2), eugene-yan (2)
  - Related: recommendation-systems, large-language-models, generative-recommendation

- [x] **Generative Recommendation** (`generative-recommendation`)
  - Framing recs as generation — RQ-VAE semantic IDs, Meta HSTU, Google PLUM, fine-tuned LLMs.
  - Sources: louis-wang (2)
  - Related: llm-recsys, recommendation-systems

- [x] **Personalization Patterns** (`personalization-patterns`)
  - User signals, context-aware ranking, push notification targeting, when personalization helps vs hurts.
  - Sources: eugene-yan (3)
  - Related: recommendation-systems, feature-engineering

- [x] **RecSys Beyond Accuracy** (`recsys-beyond-accuracy`)
  - Diversity, novelty, serendipity, long-tail exposure, assortment health.
  - Sources: eugene-yan (3)
  - Related: reranking, bandits-exploration-exploitation

- [x] **Counterfactual & Offline Policy Evaluation** (`counterfactual-evaluation`)
  - IPS, doubly robust, off-policy evaluation from logged data.
  - Sources: eugene-yan (3)
  - Related: recsys-evaluation, bandits-exploration-exploitation

- [x] **Applied RecSys Case Studies** (`recsys-case-studies`)
  - YouTube, Airbnb, Snapchat, LinkedIn PYMK, Pinterest — real-world architecture choices.
  - Sources: aman-ai (8+), eugene-yan (2)
  - Related: recommendation-systems, two-tower-retrieval

- [x] **Feature Engineering** (`feature-engineering`) — EXISTING, update
  - Feature taxonomy, encoding, normalization, temporal features, feature stores, train/serve consistency.
  - Sources: aman-ai (8+), eugene-yan (3)
  - Related: recommendation-systems, learning-to-rank

---

## 4. Retrieval & Search (4 concepts)

- [x] **Retrieval-Augmented Generation** (`retrieval-augmented-generation`) — EXISTING, update
  - Chunking, retrieval (dense/sparse/hybrid), advanced RAG, agentic RAG, evaluation.
  - Sources: aman-ai (2), chip-huyen (1), eugene-yan (2), lilian-weng (1), cameron-wolfe (3), jay-alammar (1)
  - Related: embeddings-and-representation-learning, large-language-models, ai-agents

- [x] **Approximate Nearest Neighbor Search** (`approximate-nearest-neighbor`)
  - FAISS, ScaNN, HNSW, LSH — accuracy/recall vs latency trade-offs, production indexing.
  - Sources: aman-ai (4), eugene-yan (2)
  - Related: two-tower-retrieval, embeddings-and-representation-learning

- [x] **Search Systems** (`search-systems`)
  - Query understanding, BM25, dense retrieval, hybrid search, multimodal search.
  - Sources: aman-ai (5+), eugene-yan (2)
  - Related: retrieval-augmented-generation, learning-to-rank, approximate-nearest-neighbor

- [x] **Embeddings & Representation Learning** (`embeddings-and-representation-learning`) — EXISTING, update
  - Word2Vec → contrastive learning → modern embedding models, ANN search, pretraining as representation learning.
  - Sources: aman-ai (6+), lilian-weng (3), eugene-yan (2)
  - Related: two-tower-retrieval, transformer-architecture, self-supervised-contrastive

---

## 5. AI Agents & GenAI Platforms (4 concepts)

- [x] **AI Agents & Agentic Systems** (`ai-agents-and-agentic-systems`) — EXISTING, update
  - Design patterns, tool use, MCP, multi-agent, memory, failure modes, evaluation.
  - Sources: aman-ai (7), chip-huyen (1), eugene-yan (1), lilian-weng (1), cameron-wolfe (1), nathan-lambert (1), louis-wang (2)
  - Related: large-language-models, retrieval-augmented-generation, llm-evaluation

- [x] **Generative AI Platform Design** (`genai-platform`) — EXISTING, update
  - Model gateway, orchestration, guardrails, caching, observability, build vs buy, common pitfalls.
  - Sources: chip-huyen (3), eugene-yan (3), jay-alammar (1)
  - Related: ai-agents-and-agentic-systems, retrieval-augmented-generation

- [x] **LLM Patterns for Products** (`llm-patterns`)
  - The 7 core patterns (evals, RAG, fine-tuning, caching, guardrails, defensive UX, feedback).
  - Sources: eugene-yan (5)
  - Related: genai-platform, llm-evaluation, retrieval-augmented-generation

- [x] **GenAI Product Strategy & Moats** (`genai-product-strategy`)
  - Data moats, workflow integration, open vs closed models, what 900+ OS tools reveal.
  - Sources: chip-huyen (2), jay-alammar (1), nathan-lambert (2)
  - Related: genai-platform, open-models-ecosystem

---

## 6. Computer Vision (5 concepts)

- [x] **Convolutional Neural Networks** (`convolutional-neural-networks`)
  - Conv layers, pooling, canonical architectures (AlexNet→ResNet→EfficientNet), skip connections.
  - Sources: aman-ai (5+)
  - Related: neural-network-fundamentals, transfer-learning

- [x] **Object Detection** (`object-detection`)
  - HOG/DPM → R-CNN family → YOLO, segmentation, applied vision systems.
  - Sources: aman-ai (2+), lilian-weng (3)
  - Related: convolutional-neural-networks

- [x] **Vision-Language Models** (`vision-language-models`)
  - CLIP, LLaVA, Flamingo, BLIP-2 — multimodal alignment, adapters, instruction following.
  - Sources: aman-ai (3), chip-huyen (1), cameron-wolfe (1), lilian-weng (1), sebastian-raschka (1)
  - Related: transformer-architecture, large-language-models

- [x] **Diffusion Models** (`diffusion-models`)
  - DDPM/DDIM, latent diffusion, Stable Diffusion, text-to-image, video generation.
  - Sources: aman-ai (3), lilian-weng (2), jay-alammar (1)
  - Related: generative-adversarial-networks, vision-language-models

- [x] **Generative Adversarial Networks** (`generative-adversarial-networks`)
  - GAN training, mode collapse, StyleGAN/BigGAN, face/image generation.
  - Sources: aman-ai (3)
  - Related: diffusion-models

---

## 7. ML Engineering & Production (14 concepts)

- [x] **ML System Design Framework** (`ml-system-design-framework`)
  - Structured interview approach — scoping, data/model/eval/serving phases.
  - Sources: aman-ai (4+), eugene-yan (4)
  - Related: recommendation-systems, feature-engineering

- [x] **MLOps & Model Monitoring** (`mlops-monitoring`)
  - CD4ML, data/concept drift, model versioning, observability, production ML lifecycle.
  - Sources: aman-ai (4+), eugene-yan (3)
  - Related: model-deployment, a-b-testing

- [x] **A/B Testing & Experimentation** (`a-b-testing`)
  - Experiment design, statistical significance, novelty effects, causal inference.
  - Sources: aman-ai (4+), eugene-yan (1)
  - Related: recsys-evaluation, mlops-monitoring

- [x] **ML Testing Strategies** (`ml-testing`)
  - Pre-train/post-train testing, behavioral invariance, pipeline integration, don't mock models.
  - Sources: eugene-yan (3)
  - Related: mlops-monitoring, ml-production-maintenance

- [x] **ML Production Maintenance** (`ml-production-maintenance`)
  - Monitoring data quality, feedback loops, upstream schema changes, operational burden.
  - Sources: eugene-yan (3)
  - Related: mlops-monitoring, feature-stores, train-serve-skew

- [x] **Feature Stores** (`feature-stores`)
  - Hierarchy of needs, real-time vs batch, train-serve consistency, industry implementations.
  - Sources: eugene-yan (3)
  - Related: feature-engineering, ml-production-maintenance

- [x] **Data Flywheel & Feedback Loops** (`data-flywheel`)
  - Compounding data advantages, closing prediction-outcome loops, flywheel as moat.
  - Sources: eugene-yan (3)
  - Related: ml-production-maintenance, recommendation-systems

- [x] **ML Simplicity & Starting Without ML** (`ml-simplicity`)
  - Heuristics first, prove value before ML, resist complexity — Eugene Yan's first rule.
  - Sources: eugene-yan (3)
  - Related: ml-system-design-framework

- [x] **Synthetic Data for Fine-Tuning** (`synthetic-data`)
  - Distillation from stronger models, Self-Instruct, data augmentation for SFT/preference tuning.
  - Sources: eugene-yan (2), lilian-weng (1)
  - Related: llm-post-training, data-quality

- [x] **Data Quality & Curation** (`data-quality`)
  - What makes training data high quality, semi-supervised learning, active learning for data-scarce settings.
  - Sources: lilian-weng (3), cameron-wolfe (1), karpathy (1)
  - Related: synthetic-data, neural-network-training

- [x] **Ad Systems Design** (`ad-systems`)
  - Ad auction, CTR prediction, pCTR calibration, budget pacing, full ad serving stack.
  - Sources: aman-ai (6)
  - Related: recommendation-systems, learning-to-rank

- [x] **Distributed Systems Fundamentals** (`distributed-systems`)
  - Horizontal scaling, load balancing, consistent hashing, CAP theorem, message queues.
  - Sources: aman-ai (7+)
  - Related: database-storage, ad-systems

- [x] **Privacy & Federated Learning** (`privacy-federated-learning`)
  - Differential privacy, federated learning, on-device training.
  - Sources: aman-ai (3)
  - Related: mlops-monitoring

- [x] **Open Model Ecosystem** (`open-models-ecosystem`)
  - Open-weight LLMs, release dynamics, governance, capability gaps vs frontier.
  - Sources: nathan-lambert (4), sebastian-raschka (1)
  - Related: genai-product-strategy, large-language-models

---

## Summary

| Category | Concepts | Existing (update) | New |
|----------|----------|-------------------|-----|
| ML Fundamentals | 12 | 1 | 11 |
| NLP & Language Models | 12 | 5 | 7 |
| Recommendation Systems | 14 | 4 | 10 |
| Retrieval & Search | 4 | 2 | 2 |
| AI Agents & GenAI | 4 | 2 | 2 |
| Computer Vision | 5 | 0 | 5 |
| ML Engineering | 14 | 0 | 14 |
| **Total** | **65** | **14** | **51** |
