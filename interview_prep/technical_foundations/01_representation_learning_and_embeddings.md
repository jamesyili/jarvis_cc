# 01 — Representation Learning & Embeddings

> **Bridge:** This is your deepest moat. OmniSage, UIC, the UPP Foundation Model, and CLR towers are all *representation learning* — the same primitive that produces token embeddings in an LLM. Master the framing here and you can answer "how would you build a representation?" with a system you shipped at billion-item scale.
> **Book:** recsys-native (the Hoang book under-covers this); pairs with Ch 3 (architecture) and Ch 20–22 (data).

---

## 1. The core idea

A **representation** (embedding) is a learned map from a raw object — a token, a pin, a user, an image — to a dense vector in $\mathbb{R}^d$, such that **geometry encodes meaning**: objects that should be treated similarly land close together; the axes capture latent factors no one hand-labeled.

Why this is the whole game: once you have a good embedding space, *every downstream task gets easy* — retrieval is nearest-neighbor, ranking is a dot product, clustering is k-means, prediction is a vector operation. The hard, expensive, differentiating work is **learning the space**. Everything else is cheap geometry on top. This is why frontier labs talk about "the base model" and you talk about "the foundation model / OmniSage" — same instinct: invest in the representation, reuse it everywhere.

**The senior framing:** *"Most of the value and most of the cost is in the representation. Downstream heads are cheap. So the architecture question is always: what's the shared representation, who owns it, and how do surfaces specialize on top of it?"* — that sentence is your UPP three-tier thesis **and** the modern foundation-model thesis, said once.

---

## 2. How you actually train one

### Objective families (know all four cold)

| Objective | Idea | Where it shows up |
|---|---|---|
| **Reconstruction** (autoencoder) | compress → decompress, minimize reconstruction error | classic, mostly historical |
| **Contrastive** (InfoNCE / triplet) | pull positives together, push negatives apart | two-tower retrieval, CLIP, SimCLR |
| **Self-supervised predictive** | predict a held-out part from the rest (next-token, masked-token) | LLM token embeddings, UPP FM |
| **Graph / co-occurrence** | embed so that connected/co-engaged nodes are close | OmniSage interaction + topology layers |

**Contrastive is the one to be fluent in** (it's the retrieval workhorse). The InfoNCE loss, in words: given an anchor $q$ and a positive $k^+$, maximize the similarity $q\cdot k^+$ relative to a set of negatives $\{k^-\}$:

$$\mathcal{L} = -\log \frac{e^{q\cdot k^+/\tau}}{e^{q\cdot k^+/\tau} + \sum_{k^-} e^{q\cdot k^-/\tau}}$$

This is just **softmax cross-entropy where the "classes" are items** and the temperature $\tau$ controls how hard you separate. Memorize three things about it:

1. **Negatives make or break it.** With only easy (random) negatives the model learns coarse structure; you need **hard negatives** (plausible-but-wrong) to learn fine distinctions. Hard-negative mining is where most retrieval quality lives.
2. **In-batch negatives** are the cheap trick: every other positive in the minibatch serves as a negative for this anchor — so batch size *is* a quality knob (more negatives per step). This is why retrieval training is batch-size-hungry.
3. **Popularity bias correction.** In-batch negatives oversample popular items → the model under-ranks them at serving. Fix with the **logQ / sampled-softmax correction** (subtract $\log(\text{sampling prob})$ from the logit). Naming this in an interview signals you've actually trained retrieval, not just read about it.

### Two-tower architecture (the retrieval primitive)

```
   query/user side                    item side
   ┌───────────────┐                ┌───────────────┐
   │  query tower  │                │   item tower  │
   │  (user feats, │                │ (content feats,│
   │   context,    │                │  pin embedding,│
   │   UIC vector) │                │  metadata)     │
   └───────┬───────┘                └───────┬───────┘
           │  q ∈ R^d                       │  v ∈ R^d
           └──────────►  score = q · v  ◄───┘
                         (cosine / dot product)
```

Trained with contrastive loss so that (user, engaged-item) pairs score high. **Why two towers and not one cross-attention model?** Because at serving the item tower is **precomputed and indexed** (millions–billions of vectors in an ANN index), and you only run the query tower live, then do approximate nearest-neighbor. One cross-encoder would be more accurate but you'd have to score every item per request — infeasible at retrieval scale. (Cross-encoders come *back* at the ranking stage, where the candidate set is small. → guide 04.)

### Evaluating an embedding

- **Recall@K / MRR / NDCG** against held-out positives — does the true next item land in the top-K of the ANN search?
- **Alignment & uniformity** (the contrastive-learning diagnostic): positives should be close (*alignment*) AND the space should be used evenly, not collapsed (*uniformity*). Collapse = everything maps to a few points = useless.
- **Probing** — train a cheap linear head on frozen embeddings for some labeled task; high accuracy = the embedding already encodes that factor.

---

## 3. Your anchor: OmniSage, UIC, UPP FM

### OmniSage — the multi-signal fused space (your single best representation story)

OmniSage fuses **three signal layers** into one space:
1. **Visual/Semantic (CLIP):** raw content meaning — a hiking boot looks like a shoe.
2. **Interaction graph:** co-engagement — items the same users engage with cluster together.
3. **Pin-board topology:** community curation — items pinned to the same boards cluster together.

**The punchline that makes this special:** in OmniSage, *closeness = functional utility, not visual similarity.* A **hiking boot and a granola bar are neighbors** because the board graph connects them via "camping trip" boards. That lets you represent unlabeled behavior ("minimalist apartment gardening") with no taxonomy. → In interview terms: *"We learned a space where distance is task-relevance, by fusing a content encoder with two graph signals — so the geometry does the work a taxonomy used to."* That is a sophisticated, non-generic answer to "how would you represent users/items?"

### UIC — clustering in the representation

A **User Interest Cluster** is a tuple $C_i = \{\vec{\mu}_i, \Sigma_i, T_i, A_i\}$: medioid (center), variance (focus/tightness), temporal distribution (velocity/decay), action vector (repins/closeups/clicks). Built by **complete-link hierarchical clustering over the user's L500 sequence** (last 500 actions) in OmniSage space, then **externalized to the GSS feature store** for low-latency reuse across CG, ranking, and diversity.

Two design choices worth being able to defend:
- **Cluster over only the user's engaged pins, not the global catalog** (Innovation 1) — smaller, easier, far more accurate per-user representation. The general principle: *personalize the representation, don't just personalize on top of a global one.*
- **Dynamic cluster count** — a user with broad interests gets more clusters; you don't force a fixed taxonomy.

### UPP Foundation Model — pretraining the user representation

The UPP FM is **pretrained via user-level next-token prediction** — exactly the LLM objective, but the "tokens" are user actions. The output is a reusable user representation that base retrieval (CLR) and base ranking (CFM) fine-tune from. **This is the cleanest possible bridge:** you are *literally* doing self-supervised sequence pretraining to learn a representation, then transferring it — the foundation-model paradigm, applied to users. (Pretrain→finetune mechanics → guide 03.)

---

## 4. The frontier-lab connection

Everything above is how an LLM works under the hood:

- **Token embeddings** are a learned lookup table — the input representation. The first thing a transformer does is *represent*.
- The **residual stream** (the vector at each position as it flows up the layers) is a *contextual* representation — the same object as a UIC, but recomputed per layer by attention (which is itself retrieval — guide 02).
- **CLIP** (your OmniSage visual layer) is the canonical contrastive multimodal representation — image-text pairs pulled together with InfoNCE. You already ship a system built on it; most candidates have only read the paper.
- **Embeddings as the product:** RAG, semantic search, vector DBs, dedup, classification — all are "train a good embedding, then do cheap geometry." When an interviewer asks about *any* of these, the substrate is this guide.

**The asymmetry to exploit:** LLM-native candidates know token embeddings but have rarely trained a billion-item contrastive retriever with hard-negative mining and popularity correction at serving scale. You have. Lead with that when representation comes up.

---

## 5. Interview-portable (say-it-in-90-seconds)

> *"Representation is where the value and the cost both sit — downstream heads are cheap. At Pinterest I've built this at two altitudes. OmniSage is a fused embedding space — CLIP visual signal plus a co-engagement graph plus pin-board curation topology — trained so that distance means *functional utility*, not visual similarity; a hiking boot and a granola bar are neighbors because the board graph links them through camping. On top of that we cluster each user's last 500 actions into interest clusters and externalize them as a reusable feature. And the foundation layer pretrains a user representation with user-level next-token prediction — the same self-supervised objective as an LLM, applied to user behavior — which surface models then fine-tune from. So when I think about representation learning, it's contrastive training with hard-negative mining, two-tower retrieval with popularity-corrected in-batch negatives, and a pretrain-then-specialize hierarchy — at billion-item scale."*

**Likely probes & where to go:**
- "How do you pick negatives?" → in-batch + hard-negative mining; logQ correction for popularity bias (guide 04 has the full treatment).
- "Why two towers?" → precompute + ANN the item side; cross-encoder only survives at the small-candidate ranking stage.
- "Cold start?" → synthetic profiling: match a low-signal user's fragment to a mature synthetic cluster aggregated from similar users (your RR Strategy D).
- "How do you know the embedding is good?" → recall@K offline, alignment/uniformity for collapse, linear-probe for specific factors, then online A/B (guide 06).
- "Isn't this just word2vec?" → same family (co-occurrence → geometry); the modern moves are the *fusion* of heterogeneous signals and the *self-supervised sequence* objective.

---

## 6. Self-test (do these out loud, from memory)

1. Write the InfoNCE loss and explain each term. What does temperature do?
2. Why are in-batch negatives biased, and what's the correction?
3. Why two-tower for retrieval but cross-encoder for ranking? What changes between the stages?
4. What are the three signals OmniSage fuses, and what does "closeness" mean in the resulting space?
5. The UPP FM pretrains with "user-level next-token prediction." Map every word of that phrase to its LLM equivalent.
6. A teammate says "our retrieval embeddings collapsed." What metric tells you that, and what causes it?

*Can't answer 1–2 cleanly? Read Hoang Ch 3 + any contrastive-learning primer. The rest are in your own `work+self/projects/upp/` and `retentive_recs/` docs.*
