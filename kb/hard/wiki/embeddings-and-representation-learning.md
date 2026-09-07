---
concept: Embeddings & Representation Learning
tags: [embeddings, representation-learning, word2vec, contrastive]
sources:
  - kb/hard/raw/lilian-weng/learning-word-embedding.md
  - kb/hard/raw/aman-ai/word2vec.md
  - kb/hard/raw/aman-ai/recsys-embeddings.md
  - kb/hard/raw/aman-ai/primers-gemini-embedding.md
  - kb/hard/raw/aman-ai/coursera-nlp-word-embeddings-and-vector-spaces.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/two-tower-retrieval|Two-Tower Retrieval]]"
  - "[[hard/wiki/self-supervised-contrastive|Self-Supervised & Contrastive Learning]]"
  - "[[hard/wiki/transformer-architecture|Transformer Architecture]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# Embeddings & Representation Learning

Embeddings are dense, low-dimensional numerical representations of objects — words, sentences, items, users, images — that encode semantic meaning as geometric relationships in vector space. The fundamental insight: things that behave similarly in context should be nearby in the embedding space. This transforms discrete, symbolic objects into continuous vectors that support arithmetic, similarity search, and downstream learning.

John Firth captured the linguistic intuition in 1957: "You shall know a word by the company it keeps." Word2Vec operationalized this into a training objective. Gemini Embedding extends it to universal representations across 100+ languages and dozens of tasks. The core idea has not changed — context encodes meaning — but the machinery has grown dramatically more powerful.

## The Pre-Embedding World

Traditional text representations were sparse and semantic-blind:

- **TF-IDF:** Assigns weights based on term frequency vs. corpus rarity. Captures word importance, ignores semantic similarity. "Doctor" and "physician" are orthogonal.
- **BM25:** Probabilistic extension of TF-IDF with document length normalization. Still lexical, not semantic.
- **One-hot encoding:** A vector of zeros with a single 1 at the word's index. Dimensionality equals vocabulary size (hundreds of thousands); no semantic structure at all.

The failure mode is clear: systems built on these representations can't retrieve "cardiac arrest" when the query says "heart attack."

## Word2Vec: Learning Embeddings from Context

Word2Vec (Mikolov et al., 2013) introduced the paradigm shift — learn dense embeddings by training a shallow neural network to predict context. Two architectures:

**Skip-gram:** Given a target word, predict its surrounding context words. For "swing" in a sentence, predict "sentence," "should," "the," "sword." More data-efficient; better for infrequent words.

**CBOW (Continuous Bag of Words):** Given surrounding context words, predict the target word. Averages context embeddings into a fixed-length hidden representation. Faster, better for frequent words and small datasets.

Both share the same network structure: an input one-hot vector, a weight matrix W (V×N) that acts as the embedding lookup, and an output layer predicting context or target words. The hidden layer weights — the rows of W — become the word embeddings.

**Training efficiency:** Full softmax over the vocabulary (size V) is computationally prohibitive. Two solutions:
- **Hierarchical softmax:** Encodes the output layer as a binary tree. Reduces computation from O(V) to O(log V) per training step.
- **Negative sampling (NEG):** Instead of normalizing over all words, train a binary classifier that distinguishes true context words from k randomly sampled "noise" words. Practical default for large corpora.

**What emerges:** Linear algebraic structure in the embedding space. `v_king - v_man + v_woman ≈ v_queen`. Cosine similarity between vectors encodes semantic relatedness. This arithmetic works because the training objective aligns embeddings based on shared contextual co-occurrence patterns.

**Training tips:** Subsampling frequent stopwords (which carry little semantic signal), using a soft sliding window (weighting distant context words less), and learning phrase embeddings first ("New York" before "New" and "York" separately) all improve embedding quality.

## GloVe: Global Co-occurrence Statistics

GloVe (Pennington et al., 2014) bridges count-based and prediction-based approaches. Rather than learning from local context windows, GloVe factorizes a global word co-occurrence matrix.

The key insight: meaning is captured by ratios of co-occurrence probabilities, not the probabilities themselves. If "solid" co-occurs much more with "ice" than with "steam," the ratio `p(solid|ice) / p(solid|steam)` encodes that "solid" is related to ice states. GloVe trains embeddings so that `w_i · w_k = log C(w_i, w_k)` — the dot product of two word vectors approximates the log of their co-occurrence count. This produces embeddings that capture global statistics more efficiently than Word2Vec's sliding window.

## Modern Embedding Models

**FastText:** Extends Word2Vec by representing each word as a bag of character n-grams. "playing" decomposes into {pla, lay, ayi, yin, ing, <pl, ng>} plus the full word. This handles morphological variants and out-of-vocabulary words naturally — "unpredictable" can be embedded even if never seen in training.

**Contextual embeddings (ELMo, BERT):** Static embeddings assign a single vector per word regardless of context. "Bank" in "river bank" and "bank loan" get the same vector. Contextual models run the full sequence through deep Transformers, producing position- and context-dependent representations. BERT's bidirectional self-attention means each token embedding integrates information from the entire sequence.

**Gemini Embedding — production-scale contrastive training:**
The architecture: a bidirectional Transformer encoder, mean pooling across token embeddings (averaging all token vectors to get a sentence-level representation), followed by a linear projection to the target embedding dimension. Mean pooling is preferred over CLS pooling (BERT-style) because it is more robust across languages and tasks without overfitting to classification-specific signals.

Training uses contrastive NCE loss with in-batch negatives. For a batch of B examples, each query-positive pair is trained against B-1 other positives as negatives — providing B² comparisons per batch. Hard negatives (superficially similar but incorrect passages) are added to force the model to learn fine-grained distinctions. Temperature τ controls the sharpness of the similarity distribution.

Multi-resolution training (MRL) trains the model to produce useful embeddings at multiple dimensionalities simultaneously — a single model can output 768, 1536, or 3072-dimensional embeddings, trading off quality for computational cost downstream.

## Embeddings in Recommender Systems

In recsys, embeddings represent users and items in a shared latent space. The embedding approach generalizes across methods:

**Matrix Factorization:** Decomposes the user-item interaction matrix into low-rank user and item embedding matrices via SVD or ALS. Simple and interpretable; struggles with sparse data and non-linear patterns.

**Neural Collaborative Filtering (NCF):** Jointly learns user and item embeddings via a neural network combining matrix factorization with an MLP. Captures non-linear interactions; requires more training data.

**Factorization Machines (FM):** Models interactions between all feature pairs through factorized embedding matrices. Generalizes MF to arbitrary features — user demographics, item metadata, context. Handles high-dimensional sparse features well.

**Graph Neural Networks (GNNs):** Propagates embeddings across the user-item interaction graph via neighborhood aggregation. Captures higher-order relational structure — "users who liked X also liked Y" propagates through the graph.

**Embedding ID scalability:** When item/user catalogs number in the billions, embedding lookup tables become memory-intensive. Solutions include the hashing trick (map IDs to a fixed hash space, trading off collision rate for memory), embedding compression, and pooling strategies for variable-length ID sequences.

## Embedding Space Properties

Several properties emerge from well-trained embedding spaces that practitioners rely on:

- **Cosine similarity:** Measures directional alignment, not magnitude. Standard for semantic similarity because embedding norms don't reliably encode meaning.
- **Linear relationships:** Analogies are linear offsets. `v_Paris - v_France + v_Italy ≈ v_Rome`. This enables embedding arithmetic for recommendation ("user embedding + 'adventure genre' direction = adjusted preference vector").
- **Euclidean distance vs. cosine similarity:** Euclidean distance is misleading when vectors have different norms — a large corpus will have longer vectors for frequent words not because they're more similar to other words, but because they co-occur more. Cosine similarity normalizes this out.
- **Clustering:** Semantically similar items cluster geometrically. This enables efficient nearest-neighbor retrieval — the foundation of vector-based search (see [[hard/wiki/retrieval-augmented-generation|Retrieval-Augmented Generation]]).

## ANN Search Over Embeddings

Once embeddings are trained, retrieval at scale requires Approximate Nearest Neighbor (ANN) search. See [[hard/wiki/approximate-nearest-neighbor|Approximate Nearest Neighbor]] for full treatment. Key libraries: FAISS (Meta), ScaNN (Google), ANNOY (Spotify), hnswlib. All trade recall for speed by avoiding exhaustive scan.

## Pretraining as Representation Learning

Modern large models are fundamentally representation learning engines. BERT's masked language modeling pretraining objective forces the model to build rich contextual representations in order to predict masked tokens — the downstream embeddings are the byproduct of this self-supervised task. This framing unifies word embeddings, contrastive vision-language models (CLIP), and modern embedding APIs: all are learning to map objects into spaces where semantic similarity is preserved.

## Sources

- Lilian Weng. *Learning Word Embedding* — Skip-gram, CBOW, GloVe, NCE, negative sampling, hierarchical softmax
- Aman Chadha. *Word2Vec* — distributional hypothesis, semantic arithmetic, comparison to TF-IDF/BM25, probabilistic interpretation
- Aman Chadha. *RecSys Embeddings* — MF, NCF, FM, GNN, embedding lookup, hashing trick, sparsity handling
- Aman Chadha. *Primers: Gemini Embedding* — bidirectional encoder, mean pooling, contrastive NCE, in-batch negatives, hard negatives, MRL, two-stage training
- Aman Chadha / Coursera NLP. *Word Embeddings and Vector Spaces* — co-occurrence matrices, cosine similarity vs. Euclidean distance, vector space models
