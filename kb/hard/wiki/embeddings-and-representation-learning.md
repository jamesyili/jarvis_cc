---
concept: Embeddings & Representation Learning
tags: [embeddings, representation-learning, word2vec, contrastive-learning, self-supervised]
sources:
  - kb/hard/raw/lilian-weng/learning-word-embedding.md
  - kb/hard/raw/lilian-weng/contrastive-representation-learning.md
  - kb/hard/raw/lilian-weng/self-supervised-representation-learning.md
  - kb/hard/raw/aman-ai/recsys-embeddings.md
  - kb/hard/raw/aman-ai/primers-gemini-embedding.md
  - kb/hard/raw/aman-ai/coursera-nlp-word-embeddings-and-vector-spaces.md
  - kb/hard/raw/aman-ai/cs224n-natural-language-processing-with-deep-learning.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]]"
  - "[[hard/wiki/recommendation-systems|Recommendation Systems]]"
---

# Embeddings & Representation Learning

An embedding is a dense, low-dimensional vector that encodes meaning. The core bet: semantically similar things should land near each other in vector space. That one idea underlies word2vec, matrix factorization, contrastive learning, and modern LLM pretraining — it's the same intuition applied at different scales.

---

## From One-Hot to Distributed Representations

The naive approach to representing words is one-hot encoding: each word gets a unique dimension, all zeros except a single 1. This breaks immediately — vocabulary sizes hit millions, vectors become unmanageably sparse, and there's no notion of similarity (every pair of words is equally orthogonal).

Distributed representations solve this. A word's meaning is spread across many dimensions; each dimension participates in many words. The result: a dense vector of floats, typically 50–300 dimensions, where geometric proximity encodes semantic similarity. This is the founding insight of the field: *you shall know a word by the company it keeps* (Firth, 1957).

Co-occurrence matrices operationalize this directly. In a **word-by-word** design, count how often two words appear within a window of size k across a corpus. In a **word-by-document** design, count how often a word appears in each document category. These raw counts become the basis for vector representations, though they require dimensionality reduction (PCA, SVD) before they're useful.

---

## Word Embedding Algorithms

**Word2Vec** (Mikolov et al., 2013) trains a shallow neural network on a predictive task rather than raw co-occurrence counts. Two architectures:

- **CBOW (Continuous Bag of Words):** predict the center word from surrounding context words. Faster to train; better for frequent words.
- **Skip-gram:** predict surrounding context words given the center word. Slower but better for rare words and larger datasets.

Both produce the same artifact: a learned embedding matrix where similar words cluster together. The classic demonstration — *king − man + woman ≈ queen* — shows that semantic relationships encode as linear vector arithmetic.

**GloVe** (Global Vectors) combines the coverage of co-occurrence matrices with the efficiency of Word2Vec. It trains on ratios of co-occurrence probabilities, explicitly factorizing the global co-occurrence matrix. Result: similar to Word2Vec but with more stable training and better capture of global statistics.

**FastText** extends Word2Vec by representing each word as a bag of character n-grams. This lets it generate embeddings for out-of-vocabulary words by composing subword pieces — critical for morphologically rich languages.

The training objective for all of these is fundamentally contrastive: make the embedding of a target word similar to its context, dissimilar to noise samples (negative sampling). This framing connects directly to modern contrastive learning.

---

## Embedding Space Properties

Useful embedding spaces have several measurable properties:

- **Nearest neighbors:** semantically related words cluster — *doctor, nurse, surgeon* near each other.
- **Analogy via arithmetic:** relationships encode as consistent vector offsets. Capital-country, gender pairs, verb tenses all manifest as roughly parallel vectors.
- **Cosine similarity:** the standard metric. Measures the angle between vectors, not their magnitude — important because corpus size differences inflate raw distances. `sim(a, b) = (a · b) / (‖a‖ ‖b‖)`, ranging [0, 1] when all values are non-negative.
- **Euclidean distance:** useful but biased by vector magnitude; cosine preferred when comparing across corpora of different sizes.

**Visualization:** PCA and t-SNE project embeddings to 2D. PCA finds the axes of maximum variance via SVD of the covariance matrix; t-SNE optimizes neighborhood structure non-linearly and is better for revealing clusters.

---

## Embeddings for Recommendation

In RecSys, the same machinery that encodes word meaning is applied to users and items.

**Matrix Factorization (MF)** decomposes the user-item interaction matrix into two low-rank matrices — a user embedding matrix and an item embedding matrix — such that their dot product approximates the observed interactions. Equivalent to learning embeddings via SVD or ALS. Simple and interpretable, but assumes linear interactions and struggles with high sparsity.

**Neural Collaborative Filtering (NCF)** replaces the dot product with a multi-layer perceptron, allowing the model to learn non-linear user-item relationships. User and item IDs are looked up in learned embedding tables, then passed through hidden layers to predict interaction probability. Empirically outperforms MF on sparse datasets.

**Factorization Machines (FM)** generalize MF to arbitrary feature vectors. They model all pairwise interactions via factorized parameters — efficient even when the feature space is high-dimensional and sparse. **DeepFM** extends this by running an FM component (low-order interactions) and a DNN component (high-order interactions) in parallel, combining their outputs.

**Graph Neural Networks (GNNs)** treat the user-item interaction graph directly, propagating embeddings through neighbor aggregation. They capture indirect interactions (friends-of-friends) and graph structure that pairwise models miss.

**Implementation details that matter in production:**
- Embedding tables for billions of IDs require the **hashing trick**: hash each ID to a fixed number of buckets via modulo, MurmurHash, or consistent hashing, reducing memory at the cost of collisions. Concatenating multiple hash functions mitigates collision impact.
- **New ID handling:** options include dynamic matrix expansion, reserving a pool of embeddings for unseen IDs, or defaulting to a shared zero/learnable vector. Incremental retraining on fresh data keeps embeddings current.
- **Dimensionality reduction post-hoc:** PCA or autoencoders can compress large embeddings for cheaper ANN indexing.

See [[hard/wiki/recommendation-systems|Recommendation Systems]] for the full retrieval stack these embeddings feed into.

---

## Contrastive Learning

Contrastive learning is the paradigm: **pull similar pairs together, push dissimilar pairs apart** in embedding space. It's the dominant approach for learning representations from unlabeled data.

**SimCLR** (Chen et al., 2020): take an image, apply two random augmentations to get a positive pair. All other images in the batch are negatives. Train a projection head to maximize cosine similarity for the positive pair and minimize it for negatives. Loss: NT-Xent (normalized temperature-scaled cross-entropy), equivalent to InfoNCE.

**MoCo** (He et al., 2020): maintains a momentum-updated encoder and a large queue of negative keys. Decouples batch size from negative count — you can have 65K negatives without needing a massive batch. The momentum encoder updates slowly (`m=0.999`), keeping the key queue consistent.

**CLIP** (Radford et al., 2021): applies contrastive learning across modalities. Match images to their text captions; in-batch negatives are all other image-text pairs. This produces a shared embedding space where images and text describing the same concept land near each other — the foundation of multimodal retrieval.

**Key implementation details:**
- **Temperature (τ):** smaller τ sharpens the softmax, making the model focus harder on near-negatives. Typical values: 0.07–0.1.
- **In-batch negatives:** every other sample in the batch serves as a negative, giving O(N²) signal from N samples.
- **Hard negatives:** explicitly mine near-misses (examples superficially similar to the positive but semantically different). Improves fine-grained discrimination but adding too many causes overfitting.

---

## Self-Supervised Representation Learning

Self-supervised learning creates supervision signals from the data itself, without human labels. Contrastive methods (above) are one family. Others:

- **Predictive/generative:** predict masked tokens (BERT's MLM), predict the next token (GPT), predict image patches. The model must learn rich representations to succeed at the task.
- **Contrastive Predictive Coding (CPC):** encode context with an autoregressive model, then use contrastive loss to predict future representations. Connects sequential structure to the contrastive framework.
- **BYOL / SimSiam:** bootstrap without negatives — the model learns by making one view's representation match another view's, using a stop-gradient on one branch to prevent collapse.

The key insight is that the pretext task forces general-purpose representation learning. A model that predicts masked words must understand grammar, syntax, and semantics to do it well — which is exactly what makes pretrained LLM representations useful downstream.

---

## Modern Embedding Models

**Gemini Embedding** exemplifies the current state of the art. Architecture:

1. **Encoder:** bidirectional transformer initialized from Gemini (not trained from scratch).
2. **Pooling:** mean pooling over all token positions — averages contextualized token vectors into one sentence-level representation. Chosen for stability over CLS pooling or max pooling.
3. **Projection:** linear map `f: R^{d_m} → R^d` for dimensional control (768 / 1536 / 3072), decoupling encoder hidden space from task-aligned output space.
4. **Loss:** contrastive NCE with in-batch negatives and optional hard negatives. Temperature-controlled softmax.

**Matryoshka Representation Learning (MRL):** a single model supports multiple output sizes. Training adds contrastive losses at each prefix slice (768, 1536, 3072 dims), forcing the model to distribute semantic information hierarchically. At inference, truncate to the desired size without retraining.

**Training recipe:** two-stage — broad pre-finetuning on large noisy data to shape the embedding space, then fine-tuning on curated task-diverse data. Multiple checkpoint runs are averaged (model soup) for better generalization.

**text-embedding-ada / OpenAI embeddings** follow similar principles: transformer encoder + pooling + contrastive training, optimized for asymmetric retrieval (query vs. document).

---

## ANN Search Over Embedding Spaces

Dense embeddings are only useful if you can retrieve nearest neighbors at scale. Exact k-NN search is O(N·d) — too slow for millions of items.

Approximate Nearest Neighbor (ANN) indexes trade a small accuracy loss for orders-of-magnitude speedup:
- **HNSW (Hierarchical Navigable Small Worlds):** graph-based, very fast query, high recall.
- **IVF (Inverted File Index):** cluster the space, search only nearby clusters.
- **Product Quantization (PQ):** compress vectors into compact codes, reducing memory and compute.

This is the bridge between representation learning and retrieval systems. See [[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]] for how embedding models are deployed inside a candidate generation pipeline.

---

## Pretraining as Representation Learning

The connection to LLMs: pretraining a language model on next-token prediction is representation learning at scale. The model learns to compress the statistical structure of language into its internal activations. Those internal representations can be extracted (via pooling or finetuning) and used as general-purpose embeddings.

BERT/encoder models are optimized for bidirectional context — good for sentence-level embeddings. GPT/decoder models are optimized for generation — representations are usable but require adaptation. The Gemini Embedding approach of re-initializing a generative model as a bidirectional encoder is a convergence of these two lineages.

In RecSys, this maps to the idea of **Universal People Profiles (UPP)**: pretrain on broad behavioral signals to learn general user representations, then adapt to specific downstream tasks. The pretraining-as-embedding framing extends naturally from NLP to user modeling.

---

## Interview Cheat Sheet

| Question | Key point |
|---|---|
| Why not one-hot? | Sparse, high-dim, no similarity signal |
| Word2Vec CBOW vs. Skip-gram | CBOW: context → center (faster); Skip-gram: center → context (better rare words) |
| How does negative sampling work? | Sample k "wrong" words as negatives, train to distinguish positive from noise |
| Matrix factorization = embeddings? | Yes — UV^T ≈ R is equivalent to learned user/item embedding tables |
| Why cosine over Euclidean? | Scale-invariant; corpus size doesn't inflate distance |
| What is hard negative mining? | Explicitly include near-misses in the contrastive loss denominator; improves fine-grained discrimination |
| How does MRL work? | Add contrastive losses at multiple prefix sizes; embeds a hierarchy of representations in one vector |
| Hashing trick trade-off | Smaller embedding matrix vs. hash collisions (mitigate by concatenating multiple hashes) |

---

## Sources

- Lilian Weng — [Learning Word Embedding](https://lilianweng.github.io/posts/2017-10-15-word-embedding/)
- Lilian Weng — [Contrastive Representation Learning](https://lilianweng.github.io/posts/2021-05-31-contrastive/)
- Lilian Weng — [Self-Supervised Representation Learning](https://lilianweng.github.io/posts/2019-11-10-self-supervised/)
- Aman.ai — [RecSys Embeddings](https://aman.ai/recsys/embeddings/)
- Aman.ai — [Gemini Embedding Primer](https://aman.ai/primers/ai/GeminiEmbedding/)
- Aman.ai — [Coursera NLP: Word Embeddings and Vector Spaces](https://aman.ai/coursera-nlp/vector-spaces/)
- Aman.ai — [CS224n: NLP with Deep Learning](https://aman.ai/cs224n/)
