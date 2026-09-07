---
concept: Self-Supervised & Contrastive Learning
tags: [self-supervised, contrastive-learning, simclr, moco, clip]
sources:
  - kb/hard/raw/lilian-weng/self-supervised-representation-learning.md
  - kb/hard/raw/lilian-weng/contrastive-representation-learning.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/embeddings-and-representation-learning|Embeddings & Representation Learning]]"
  - "[[hard/wiki/vision-language-models|Vision-Language Models]]"
  - "[[hard/wiki/loss-functions|Loss Functions]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Self-Supervised & Contrastive Learning

Self-supervised learning (SSL) trains representations without human-labeled data by constructing supervised tasks from the data itself. Contrastive learning is the dominant SSL paradigm: learn an encoder such that similar (positive) samples are close in embedding space and dissimilar (negative) samples are far apart.

This approach has produced some of the most transferable representations in vision and language — CLIP, BERT, SimCLR, and MoCo all draw from these ideas.

## The Core Idea

In supervised learning, we have labels. In self-supervised learning, we create "pseudo-labels" from the structure of the data:

- **Vision**: create two augmented views of the same image → they should have similar embeddings
- **Language**: mask tokens and predict them (BERT), or predict the next token (GPT)
- **Multimodal**: pair images with their captions → the matched pair should be similar, mismatched pairs dissimilar

The key insight: **data augmentation defines what "same" means**. If random cropping, color jitter, and flipping don't change the semantics, the model is forced to learn semantic content by making augmented views agree. Getting the augmentation strategy right is critical.

## Contrastive Training Objectives

### Contrastive Loss (Early Formulation)

The original pairwise contrastive loss (Chopra et al. 2005):

`L(x_i, x_j) = 1{y_i=y_j} · ||f(x_i) - f(x_j)||² + 1{y_i≠y_j} · max(0, ε - ||f(x_i) - f(x_j)||)²`

Similar pairs are pulled together; dissimilar pairs are pushed apart to at least distance ε. Works but requires explicit label pairs and only uses one negative per anchor.

### Triplet Loss

Triplet loss (FaceNet, Schroff et al. 2015) introduces a positive and negative alongside an anchor:

`L = max(0, ||f(x) - f(x⁺)||² - ||f(x) - f(x⁻)||² + ε)`

The margin ε enforces that positive pairs are closer than negative pairs by at least ε. Selecting **hard negatives** — samples with features close to the anchor but from a different class — is essential. Easy negatives (far-away points) produce near-zero loss and no learning signal. Mining hard negatives is an art: too hard (actual false negatives, mislabeled data) corrupts training; too easy adds no value.

### InfoNCE Loss

InfoNCE (Contrastive Predictive Coding, van den Oord et al. 2018) generalizes to multiple negatives:

`L_InfoNCE = -E[log(f(x, c) / Σ_{x'∈X} f(x', c))]`

This is a categorical cross-entropy: among N samples in the batch, identify which one is the positive (the sample from the same context). Maximizing this objective lower-bounds the mutual information between x and c. More negatives = tighter lower bound = better representations.

The scoring function `f(x, c) ∝ p(x|c)/p(x)` — it estimates the density ratio, not the density itself, which is tractable.

### NT-Xent (Normalized Temperature-Scaled Cross-Entropy)

The SimCLR loss. Given a batch of N images, create 2N views (2 augmentations per image):

`L(i,j) = -log[exp(sim(z_i, z_j)/τ) / Σ_{k≠i} exp(sim(z_i, z_k)/τ)]`

- sim(·,·) = cosine similarity
- τ = temperature (typically 0.1–0.5)
- The 2N-2 other views in the batch serve as negatives

**Temperature τ controls sharpness**: low τ concentrates the distribution, penalizing hard negatives more heavily. High τ is more uniform. τ ≈ 0.1–0.2 is typical.

## Key Methods

### SimCLR

**SimCLR** (Chen et al. 2020) is the simplest strong contrastive learning baseline for vision:

1. Sample a mini-batch of N images
2. Apply two independent augmentation operations (random crop, color jitter, Gaussian blur, horizontal flip) to each image → 2N views total
3. Encode all views with a shared encoder f (ResNet)
4. Project through a non-linear MLP head g: `z_i = g(f(x̃_i))`
5. Compute NT-Xent loss over the projected embeddings
6. **Crucially**: only the encoder f (not g) is used for downstream tasks

**Key findings:**
- The projection head g is important — computing loss in projected space (not encoder space) improves representations
- Composition of random crop + color distortion is the single most important augmentation combination
- Large batch size is necessary — 4096+ for good performance (more negatives per anchor)
- Stronger augmentation = better generalization

SimCLR requires very large batches (and thus large compute) to have enough in-batch negatives. MoCo solves this.

### MoCo (Momentum Contrast)

**MoCo** (He et al. 2019) decouples the number of negatives from the batch size via a **memory queue**:

- A query encoder processes the current batch
- A momentum encoder (updated as EMA of query encoder) encodes keys stored in a FIFO queue of size K (e.g., 65,536)
- Loss: InfoNCE over query vs. one positive key + K-1 negative keys from the queue

`θ_key ← m·θ_key + (1-m)·θ_query`

The momentum update (m ≈ 0.999) keeps key representations consistent — the queue can be large because it moves slowly. This decouples batch size from effective negative count, achieving SimCLR-level performance at much smaller batch sizes.

**MoCo V2** adds SimCLR's MLP projection head and stronger augmentation, closing the gap with SimCLR while maintaining memory efficiency.

### BYOL (Bootstrap Your Own Latent)

**BYOL** (Grill et al. 2020) eliminates negative pairs entirely — it only uses positive pairs:

- **Online network** (θ): encoder → projector → predictor
- **Target network** (ξ): same architecture, no predictor, updated as EMA of online network
- Loss: MSE between online predictor output and target projector output (L2-normalized)

`ξ ← τ·ξ + (1-τ)·θ`

BYOL avoids collapse (all representations going to zero) through the asymmetry between online and target networks and the non-updated target. But it turns out batch normalization in the encoder implicitly injects dependency on other batch members — effectively functioning as an implicit contrastive signal. Remove BN and BYOL collapses to random performance.

**Why BYOL matters**: it shows that explicit negatives may not be strictly necessary; architectural asymmetry + EMA target can prevent collapse.

### SimSiam

**SimSiam** (Chen & He 2021) pushes the idea further: same architecture as BYOL but without the EMA update. Stop-gradient is applied to one branch to prevent collapse:

`L = -cosine_similarity(p₁, sg(z₂)) / 2 - cosine_similarity(p₂, sg(z₁)) / 2`

where `sg(·)` is stop-gradient. The theoretical understanding is that SimSiam implicitly performs EM: the predictor and encoder alternate optimization steps. In practice, careful learning rate tuning is needed to prevent collapse.

### Barlow Twins

**Barlow Twins** (Zbontar et al. 2021) takes a different angle: learn representations where the cross-correlation matrix between two augmented views approaches the identity matrix.

`L_BT = Σ_i (1 - C_ii)² + λ Σ_i Σ_{j≠i} C_ij²`

The first term (invariance) forces diagonal entries to 1 — each feature should be invariant across augmentations. The second term (redundancy reduction) forces off-diagonal entries to 0 — features should be decorrelated. This is an information-theoretic perspective: maximize information content while minimizing redundancy.

Barlow Twins is competitive with SimCLR and MoCo and more robust to batch size variation.

## CLIP (Contrastive Language-Image Pre-Training)

**CLIP** (Radford et al. 2021) extends contrastive learning to multimodal (image-text) pairs. Given a batch of N (image, text) pairs:

- Encode images with an image encoder → image embeddings
- Encode texts with a text encoder → text embeddings
- Build N×N cosine similarity matrix
- **Optimize**: maximize similarity of N correct (image, text) pairs, minimize similarity of N(N-1) incorrect pairs via symmetric cross-entropy

CLIP is trained on 400M internet-scraped (image, text) pairs. The result: zero-shot transfer to virtually any visual recognition task by comparing image embeddings against text embeddings of class descriptions.

Key insight: natural language supervision is a more flexible training signal than discrete labels. "A photo of a dog" encodes richer semantics than a one-hot label for class 47.

**CLIP's impact**: directly enables zero-shot image classification, open-vocabulary object detection, image-text retrieval, and is a backbone for generative models (Stable Diffusion, DALL-E).

## Key Ingredients for Effective SSL

**1. Heavy data augmentation**: augmentation defines the invariances the model learns. For vision: random crop + resize, color jitter, Gaussian blur, horizontal flip. The combination matters — crop + color distortion is especially powerful.

**2. Large batch sizes or memory banks**: contrastive learning needs many negatives. SimCLR uses batch size 4096+; MoCo uses a 65,536 item queue.

**3. Hard negative mining**: random negatives are often trivially easy. Samples close in feature space but from different classes force the model to learn finer distinctions. Too many false negatives (actual positives mislabeled as negatives) degrade performance.

**4. Projection head**: use a non-linear MLP projection on top of the encoder for the contrastive loss, but use the encoder representation for downstream tasks. The projection head seems to absorb information about the specific augmentation strategy, leaving the encoder to learn more general features.

**5. Temperature tuning**: τ controls the hardness of the negatives in the softmax. Too low → training is dominated by a few hard negatives and is unstable. Too high → loss is too uniform, training is inefficient.

## Self-Supervised Pretraining Objectives Beyond Contrastive

**Masked prediction (BERT-style)**: mask 15% of tokens, train to predict them. The representation must encode context to reconstruct masked content.

**Next-token prediction (GPT-style)**: predict the next token autoregressively. The representation encodes a rich generative model of the data distribution.

**Masked autoencoders (MAE)**: mask 75% of image patches, reconstruct the masked pixels. Highly efficient — most of the compute processes only visible patches.

These objectives define what "agreement" means differently from contrastive learning, but all share the goal: learn representations that capture the structure of the data without human labels.

---

## Sources

- Lilian Weng, "Self-Supervised Representation Learning," lilianweng.github.io, 2019
- Lilian Weng, "Contrastive Representation Learning," lilianweng.github.io, 2021
