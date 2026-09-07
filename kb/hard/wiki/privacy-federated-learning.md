---
concept: Privacy & Federated Learning
tags: [privacy, federated-learning, differential-privacy, on-device]
sources:
  - kb/hard/raw/aman-ai/concepts-privacy.md
  - kb/hard/raw/aman-ai/primers-federated-learning.md
  - kb/hard/raw/aman-ai/primers-differential-privacy.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/mlops-monitoring|MLOps & Monitoring]]"
  - "[[hard/wiki/model-compression|Model Compression]]"
understanding: 1  # very little exposure / unknown (default)
relevance: 0  # not obviously relevant
knowledge_updated: 2026-09-07
---

# Privacy & Federated Learning

Privacy-preserving ML sits at the intersection of regulatory pressure, user trust, and technical constraint. Three complementary techniques form the modern stack: **on-device processing** (data never leaves the device), **differential privacy** (formal mathematical guarantees on information leakage), and **federated learning** (collaborative training without centralizing raw data). Together they define how AI systems can learn from sensitive data — medical records, financial transactions, personal conversations — without compromising the individuals who generated it.

## On-Device Privacy (Edge Computing)

On-device processing runs model inference and training entirely on the user's device rather than sending data to a central server. The privacy benefit is fundamental: data that never travels cannot be intercepted in transit or exfiltrated from a breached server.

For NLP and conversational AI, this matters most because private conversations are the primary use case. On-device processing also reduces latency — no network round trip — and enables offline operation.

The deployment challenge is resource constraints. Modern LLMs are GPU-hungry; smartphones are not. Model compression techniques — pruning (removing low-importance weights), quantization (reducing numeric precision from FP32 to INT8 or INT4), and knowledge distillation — make it increasingly viable to run effective models on-device. The trend toward smaller, highly capable models (Phi family, Qwen small variants) is directly motivated by on-device deployment requirements.

Apple's on-device inference for Siri and on-device keyboard prediction are production examples. The on-device model never uploads raw user data; only aggregate statistics (privacy-protected via DP) are reported.

## Differential Privacy (DP)

**The core problem**: ML models trained on sensitive data can memorize and inadvertently reveal individual data points. A language model trained on private emails might reproduce those emails verbatim when prompted. Membership inference attacks can determine whether a specific individual's data was in the training set. Differential privacy provides a rigorous mathematical defense.

### Formal Definition

A randomized algorithm M satisfies **(ε, δ)-differential privacy** if, for any two adjacent datasets D and D' differing by exactly one record, and for all subsets S of possible outputs:

```
Pr[M(D) ∈ S] ≤ e^ε · Pr[M(D') ∈ S] + δ
```

**ε (epsilon)**: The privacy loss parameter. Smaller = stronger privacy. Typical range: 0.01–10. Apple uses ε=4 for emoji suggestions, ε=8 for QuickType, ε=2 for Health Type Usage.

**δ**: Probability that the DP guarantee fails. Should be < 1/n where n is dataset size. When δ=0, this is "pure DP"; δ>0 gives "approximate DP," which is more practical for deep learning.

**Adjacent datasets**: Two datasets differing in exactly one individual's record. DP ensures that no adversary can reliably distinguish which of two adjacent datasets was used — i.e., whether any particular person was in the training data.

The intuition: the algorithm adds enough randomness that the presence or absence of any single individual changes the output distribution by at most a factor of e^ε. A powerful adversary sees the output but cannot confidently infer individual membership.

### Noise Mechanisms

**Laplace mechanism**: Adds Laplace-distributed noise calibrated to the query's *sensitivity* (maximum change in output from adding/removing one record). Provides pure DP (δ=0). Used for real-valued queries.

**Gaussian mechanism**: Adds Gaussian noise. Provides approximate DP (δ>0). More practical for high-dimensional queries like gradient updates in deep learning.

### DP-SGD: Training Neural Networks with Privacy

Differentially Private Stochastic Gradient Descent (DP-SGD) is the standard approach for training models with formal DP guarantees:

1. **Per-sample gradient computation**: Compute gradients separately for each training example (not averaged over a minibatch).
2. **Gradient clipping**: Clip each per-sample gradient to maximum norm C: g_i ← g_i · min(1, C / ‖g_i‖₂). This bounds the sensitivity of the update.
3. **Noise addition**: After averaging clipped gradients, add Gaussian noise: ḡ = (1/n) Σ g_i + N(0, σ²C²I), where σ is the noise multiplier.
4. **Privacy accounting**: A privacy accountant (Rényi or Moments Accountant) tracks cumulative ε across all training steps. Training consumes privacy budget; more epochs = higher ε.

**PyTorch implementation via Opacus** (Facebook):
```python
from opacus import PrivacyEngine
privacy_engine = PrivacyEngine(
    model, batch_size=256, sample_size=len(dataset),
    noise_multiplier=1.2, max_grad_norm=1.0
)
privacy_engine.attach(optimizer)
```
Opacus handles per-sample gradients, clipping, noise injection, and privacy budget tracking automatically.

**DP-Weights** (post-training alternative): Add noise to trained model weights after training rather than during. Lower overhead but weaker guarantees than full DP-SGD.

### Applying DP to LLMs

Fine-tuning LLMs on private datasets (clinical notes, enterprise emails, legal documents) with DP-SGD is the primary production use case. Standard pipeline:

1. Select ε and δ based on risk tolerance.
2. Calibrate noise multiplier σ and clipping norm C on a non-sensitive validation set.
3. Train with DP-SGD via Opacus, tracking cumulative ε.
4. Evaluate utility trade-off: DP typically increases perplexity and reduces task-specific metrics. The cost improves with larger public pretraining followed by private fine-tuning.

**DP is especially valuable against membership inference**: LLMs can memorize rare sequences (uncommon names, specific numbers) that membership inference attacks exploit. DP-trained models memorize less, reducing attack success.

**Recent strategies**:
- Pre-train with DP on private corpus, then fine-tune on public data to recover utility.
- Use LoRA adapters for private fine-tuning — only the adapter parameters require DP, greatly reducing the per-sample gradient computation cost.

### Local Differential Privacy (LDP) and Apple's Implementation

LDP applies randomization at the device before data leaves, rather than on the server side. Apple's implementation uses **Count Mean Sketch (CMS)**:

1. Hash user input to a vector space.
2. Flip each coordinate with probability 1/(1+e^(ε/2)) — introducing controlled uncertainty.
3. Transmit only one random row of the sketch matrix (further limiting leakage).
4. Server aggregates noisy vectors from millions of users to estimate population statistics (top emojis, frequent words).

**Hadamard Count Mean Sketch (HCMS)** refines CMS by applying a Hadamard transform before privatization, reducing transmission to a single bit per user per record. Ideal for bandwidth-constrained mobile telemetry.

## Federated Learning (FL)

Federated learning enables collaborative model training across distributed clients while raw data never leaves its source. The server never sees individual user data — only model updates.

### Architecture and Training Loop

The canonical **FedAvg** algorithm (centralized FL):

1. **Initialization**: Server broadcasts global model w^(t) to selected clients.
2. **Client selection**: Random fraction of clients participates per round.
3. **Local training**: Each client performs E epochs of SGD on its private dataset D_k.
4. **Reporting**: Clients send back updated weights w_k^(t+1) or deltas Δw_k.
5. **Aggregation**: Server computes weighted average: w^(t+1) = Σ_k (n_k/n) · w_k^(t+1)
6. **Repeat** until convergence criteria met.

This objective minimizes the global empirical risk: min_w Σ_k (n_k/n) · F_k(w), where F_k is the local loss on client k's private data.

### Types of Federated Learning

**Cross-device FL**: Millions of edge devices (smartphones, IoT). Characteristics: sparse participation (<10% active per round), highly diverse hardware and data distributions, intermittent connectivity. Primary use cases: on-device keyboard prediction (Google Gboard), private assistant models.

**Cross-silo FL**: Small number (2–100) of reliable institutions — hospitals, banks, data centers. High bandwidth, stable participation, institutional data heterogeneity. Use cases: medical AI across hospital networks, fraud detection across banks without sharing customer records.

### Addressing Non-IID Data

A fundamental challenge: in real FL deployments, data is **not identically distributed** (non-IID) across clients. Hospital A may have predominantly elderly patients; hospital B may serve a different demographic. Problems this causes:

- **Covariate shift**: Features from different distributions.
- **Prior probability shift**: Label distributions differ.
- **Concept drift**: Same labels, different feature distributions.

Standard FedAvg struggles with non-IID data because local models diverge significantly before aggregation. Solutions:

- **FedProx**: Adds a proximal term to the local objective that constrains how far local models can drift from the global model. More stable convergence on non-IID data.
- **SCAFFOLD**: Uses control variates to correct for client drift in gradient directions.
- **FedDyn**: Dynamic regularization that adapts to each client's data distribution.

### Federated LoRA for LLMs

Fine-tuning large LLMs across distributed devices is expensive. **Federated LoRA** applies low-rank adapters in the FL context:

- Only the LoRA adapter parameters (a small fraction of total model parameters) are trained locally and shared.
- Reduces communication cost dramatically — adapter deltas are small.
- Reduces per-device computation cost.
- Preserves the base model weights, which can be public.

Challenge: LoRA adapter spaces may not aggregate cleanly across clients with heterogeneous data distributions. Active research area.

### Security Extensions

**Secure Aggregation**: Cryptographic protocols (e.g., secure multiparty computation) ensure the server cannot see individual client updates, only their aggregate. Prevents the server from reverse-engineering individual gradients to reconstruct training data.

**Homomorphic encryption**: Allows computation on encrypted data — clients encrypt their gradients before sending; server aggregates in ciphertext space and returns encrypted global model. High computational overhead, but provides stronger privacy than DP alone.

**Differential Privacy + Federated Learning**: The two techniques complement each other. FL prevents raw data from leaving the client; DP protects against inference attacks on aggregated model updates. Apple and Google Gboard combine both in production. The combined guarantee: raw data stays local (FL) and aggregate model updates cannot reveal individual contributions (DP).

### FL Limitations

- **Communication bottleneck**: Each round requires all selected clients to download and upload model weights. Gradient compression, quantization, and top-k sparsification reduce this cost.
- **System heterogeneity**: Device capability varies enormously. HeteroFL allows varying model sizes across clients. Asynchronous variants handle variable update latency.
- **Data poisoning / adversarial clients**: Malicious clients can submit manipulated updates. Robust aggregation rules (Byzantine-fault-tolerant aggregation, anomaly detection on client updates) are necessary in adversarial settings.
- **Privacy-utility trade-off**: Stronger DP guarantees require more noise, degrading model quality. Larger participating populations reduce noise requirements at fixed ε.

### Production Use Cases

- **Google Gboard**: Next-word prediction on Android keyboards. Cross-device FL with DP. The canonical production example.
- **Apple iOS**: Keyboard prediction, emoji suggestions, Safari AutoPlay detection — LDP for telemetry, on-device for inference.
- **Healthcare**: Federated training of clinical NLP models across hospital systems without sharing patient records. Cross-silo FL.
- **Finance**: Fraud detection models trained across banks without sharing customer transaction data.

## Sources

- Aman Chadha, "Concepts • Privacy" — `kb/hard/raw/aman-ai/concepts-privacy.md`
- Aman Chadha, "Primers • Federated Learning" — `kb/hard/raw/aman-ai/primers-federated-learning.md`
- Aman Chadha, "Primers • Differential Privacy" — `kb/hard/raw/aman-ai/primers-differential-privacy.md`
