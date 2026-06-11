# Unified Cross Surface Retrieval (UBR) — Technical Design Reference

**Source document:** Internal Pinterest design doc, authors: **Piyush Maheshwari**, **Jiaxing Qu**. Last updated: **2026-04-05**.

**Captured into Leo:** 2026-04-11 (from screenshots James shared).

**Status:** Active design in co-development across UPP Retrieval + P2P Retrieval + ATG. Next-steps MVP markers suggest initial e2e workflow is the current P0 sprint.

---

## Overview

Unified Cross Surface Base Retrieval (UBR) is being developed as part of the **Unified P13N Platform (UPP)** project. The goal is to provide base models to drive engagement/retention **and relevance** across different recommendation surfaces at Pinterest.

By building a strong cross-surface unified model, UBR provides strong pretrained backbones to surface teams who can then fine-tune as needed to maximize model quality and increase dev velocity.

**This is the operational instantiation of the pretrain-finetune paradigm for retrieval at Pinterest** — the same paradigm blog post #1 will describe at a public-knowledge level, grounded in CLR (which is public) and broader recsys literature.

---

## Background and Design Principles

UBR is a **conditional learned retrieval (CLR)** model that generates user embeddings for a given user and condition. Different surfaces support different conditions:

| Surface | Condition |
|---|---|
| HF (Homefeed) CLR | interest, pin, board, text |
| P2P CLR | query pin |
| Search CLR | search query |
| Notification | interest (text) |
| BMI | query board |

### Why P2P and Search are natural CLR fits

P2P and Search are a natural fit for the CLR paradigm since query pin and search query can be treated as conditions. **Important note:** P2P and Search are more contextual (query pin / search query), which makes **semantic relevance more important** compared to surfaces like HF or Notifications.

Therefore, it is of high importance to improve the base model's generalization ability for **both relevance and personalization**.

**Evidence from existing models:**
- P2P current model uses ~20 features to describe query pin
- Search LR model also uses a similar number to describe search query
- HF CLR uses just omnisage embedding to describe pin/board condition

### Two core design principles

1. **P2P and Search condition encoders use all the existing features for their respective conditions.** No feature loss during the migration to the unified base model.
2. **Reserve dedicated model capacity to focus on relevance**, which is super important to P2P and Search.

> **Strategic note (Leo):** Principle 2 is the *operational answer* to Kurchi's March must-win concern about semantic relevance. The design doc explicitly names relevance as a first-class concern in the base model. When interacting with Kurchi or Jinfeng on UPP going forward, this is the citable answer to "how does UBR protect relevance?"

More details in initial SSJ TDD: [TDD] SSJ Learned Retrieval (linked in source doc).

---

## Base Model Architecture / Training

Overall architecture is the same as the **standard two-tower model** with a query tower and a pin tower.

### Query Tower

Consists of four components:

#### 1. Condition Tower (different for each surface)

**Features:**
- **HF:** All features describing input condition (pin/board/interest/text)
- **P2P:** All features describing query pin
- **Search:** All features describing search query
- **BMI:** All features describing board

**Processing:**
- Add feature cross layer
- Generate tokens from encoding all the features as output of feature cross layer
- Use these tokens as input to the user tower **and** to the final feature cross layer

#### 2. Surface Tower (different for each surface)

**Features:** All features describing surface-specific nuances.
- **HF:** n/a
- **P2P:** device type, top-level traffic source, traffic source, timestamp
- **Search:** TBD
- **BMI:** n/a

**Processing:**
- Generate tokens from encoding using surface-specific context features
- Add feature cross layer

#### 3. User Tower (SHARED across surfaces)

Model user history using either:

- **Conditioned User Sequence Transformer** — [LR] Unified CLR: Conditioned User Sequence Module
- **Use context tokens** (surface/conditions)
- **(Ablation) Model scaling:**
  - **CLR FM** — Integrating FM in CLR
  - **Transformer decoder** — P2P LR in OneTrans
  - **Sparse-MoE** — P2P LR in Rankmixer

#### 4. Final Feature Cross Layer

- DHEN etc.

### Design Ablations

- Potentially **combine Surface Tower and Condition Tower**
- Explore multiple ways to generate tokens from condition towers and surface towers
- Consider **removing the final crossing** and using a transformer backbone
- More details in linked discussion thread

### Parameter sharing assumption (initial)

All components marked `**` above are defined per-surface. **To start**, these components will **not share parameters** — so a P2P surface tower would only get gradient updates from P2P rows in the batch.

Components like **condition towers are more natural candidates for sharing parameters**, and this is something the team will explore.

### Pin Tower (much simpler)

- Encode all features and pass them to the final feature cross layer
- **Features:** Take intersection of candidate pin features from different surfaces datasets. For features outside the intersection, can be added to the pin tower during the **fine-tuning stage**.
- **Feature Cross:** DHEN

### Feature Set

See linked: UPP Retrieval Feature Audit.

---

## Evaluation

For CLR models, compute **recall@k** metric across different conditions. Because the model is trained on cross-surface data, the team needs to compute this metric **per surface** (not globally).

**Per-surface recall metrics** `<Surface_topk_condition_head_segment>`:

- `p2p_recall_k_query_pin_condition`
- `search_recall_k_query_condition`
- `hf_recall_k_interest_condition`
- `hf_recall_k_pin_condition`
- `hf_recall_k_board_condition`
- `notif_recall_k_interest_condition`
- `bmi_recall_k_board_condition`

---

## Training Data

### Sources

Use a **multi-source dataloader** (either Stacked or MultiSource DL) to assemble training data from different surfaces.

- **Batch size tuning on data distribution across surfaces.** This decides how much base model training compute to spend on each data source.
- **Current data sources:** HF, BMI, P2P, Search, Notif.

**Feature remapping:** To account for differences in names/data types of features across surfaces that are used in shared modules, the team will remap features either in dataloading or in model forward pass.

### Sampling

Experimenting with **different sampling strategies** for each surface is **out of scope for the initial version**. The team will use the sampling strategies each surface's current retrieval model uses.

**The only thing being experimented with is the % of total data per surface.**

### Loss Function

**Binary cross-entropy** + **in-batch negatives** + **(optional) relevance loss**.

One important design decision is how to construct in-batch negative loss. Two options:

1. Apply IBN loss **separately to each surface batch**
2. Apply IBN loss **together**, but treat other surface's data as easy negative

### Labels

Start with labels common across all surfaces — **repin, click, close up, etc.** Surface-specific labels will be added during fine-tuning.

---

## Relevance Modeling

Options the team will explore for adding relevance modeling in the base model:

### Labels (objective)

- **Content similarity distillation** as soft relevance label
  - **Label source:** PinCLIP embedding, GPT labeler, relevance teacher model
  - **Loss:** MSE, KL divergence

### Features (from P2P LR, currently missing in UPP base model)

P2P LR launches features that help content relevance, currently missing in UPP base model:

- **Search relevance:** Search Relevance Embeddings v1 Summary (LR)
- **SearchSage content only:** SearchSage v24a Summary (LR)

### Architecture

- **Hard negatives mining** — reduce false negative rate on high-relevance in-batch negatives
- **Pin-level:** Semantic ID co-occurrence contrastive learning (LR)

---

## Next Steps (initial MVP)

| Priority | Task |
|---|---|
| **P0** | Decide the minimal feature set & labels for each surface |
| **P0** | Prepare the surface training & eval data |
| — | Setup the initial e2e workable workflow |
| **P0** | Overall query-pin tower and training workflow setup |
| **P0** | Surface tower |
| **P1** | Feature crossing |
| **P1** | Scaling user sequence |
| **P1** | Data sampling |
| — | Fine-tuning |

---

## Fine-tuning: Model Adoption

There are a few ways a surface model can consume the base model, all boiling down to: **"How much of the base model do we want to use in the surface model fine-tuning?"**

In reality there is a wide spectrum of solutions. The team will experiment with different options through online A/B tests.

In the design doc diagrams, **everything in red is defined as the surface tower**; **everything in purple is loaded from the base model**.

The design doc lays out **three progressive approaches** for loading the base model into the surface FT model, representing increasing degrees of base model reuse. Diagrams use **red = surface tower (defined per surface)** and **purple = loaded from base model**.

#### Approach 1: Embedding Generation Module (FM adoption fashion)

Use the base query model for embedding generation, fed into the rest of the model.

- For the **query tower**: load the **user tower from the base model** into the surface FT model as a module.
- **All other logic/modules** are defined in the Surface model.

This is the minimal adoption path — the surface model reuses only user embeddings and retains full control over condition/context/feature-crossing logic.

#### Approach 2: User Tower Module

Use the base query model **as the user tower module**. Leave the rest of the module components to surface models.

Example: for **P2P**, the surface model keeps the query pin tower, context tower, and feature crossing as surface-defined.

This is a middle path — surface models give up the user tower to the base model but keep all surface-specific condition/query/crossing logic.

#### Approach 3: Full Model (User Tower Module + Condition Tower + Feature Cross)

In the surface query model, **add a feature adaption module** for extra surface features. Keep **user tower, surface tower, condition tower, and final feature crossing layer** all loaded from the base model.

This is the maximum adoption path — the surface model is essentially a thin adapter on top of the base model, with only a feature adaption module handling surface-specific features that weren't in pretraining.

**Adapter layer design:** For feature adapter modules, the team proposes using something similar to the **FiLMAdapter layer** described in [LR] GULP ranker: Pinnability with Context Adapter.

### Surface Pin Tower options

Parallel to the query tower adoption choices, the surface pin tower has **two options** for base-model reuse:

1. **Embedding Generation Module** — pin embedding only is loaded from base.
2. **Embedding Generation Module + Feature Cross** — pin embedding and feature cross both loaded from base; surface models define the rest.

### Fine-tuning training data

Fine-tune **with surface-only training data**. Use data from the window **after** the pre-training window. This prevents information leakage from pre-training data into the fine-tuning phase.

### Fine-tuning features

- **Candidate tower:** Since UBR only takes **intersections** of candidate pin features from different surfaces datasets during pre-training, the rest of the features can be added during the **fine-tuning stage** (surface-specific features).
- **Viewer tower:** Add surface-specific features into surface-designed modules.

### Fine-tuning labels

Surface retrieval models can add **additional labels beneficial for business requirements** — e.g., download, screenshot, revisitation, etc. The base model labels (repin, click, close up) remain the shared backbone; surface-specific labels are layered on top for finetuning.

---

## Alternative Design Choices

### Query pin tower — Ablation study

**Thesis:** Since surface tokens and condition tokens are already included in the user sequence module in the user tower, the team can consider **removing the final feature crossing layer** and relying on the **attention mechanism for global crossing**.

This is a simpler, more transformer-native architecture — letting attention do the cross-feature interaction work rather than an explicit DHEN-style crossing layer.

#### Unified tokenization scaling

Combine feature crossing and user sequence module into a **single backbone**. Explorations in this direction from P2P:

- **Transformer:** OneTRANS (26" — TikTok reference) — P2P LR in OneTrans
- **Sparse-MoE:** RankMixer (25" — TikTok reference) — P2P LR in Rankmixer
- **Using FM as backbone**

#### Benefits of unified backbone

- **Pre-training scalability:** transformer scales well with larger parameter size — the path to CLR-FM integration.
- **More industrial learnings on training & serving optimizations** — leveraging existing TikTok/industry precedent (OneTRANS, RankMixer) reduces research risk.

### Architecture diagram (unified backbone variant)

The user tower with unified backbone structure:

```
                    User Tower
                        │
              Multi-task layer (MMoE, PLE)
                        │
           Unified Backbone (Transformer, RankMixer)
                        │
                     Input MLP
              (Pos emb + Token type embedding)
                        │
    ┌──────────┬─────────┬──────────┬──────────┐
    │          │         │          │          │
User Seq   User Context  Surface tokens  Cond tokens
(IDs + IDs)    │              │              │
              MLP            MLP            MLP
               │              │              │
       User-Context Tower  Surface Tower  Condition Tower
       - Feature Cross    - Feature Cross - Feature Cross
       - Emb Layer        - Emb Layer     - Emb Layer
               │              │              │
          User Features  Surface Context  Condition Features
                             Features
```

Key structural insight: **three parallel towers (User Context, Surface, Condition)** each with their own feature cross + embedding layer, feeding tokens into a unified transformer backbone with a multi-task output layer. This is the strong-transformer variant that sits at the scalable end of the ablation space.

### Popularity bias note (sidebar)

**"In addition, as we know, negative sampling [is effective at] mitigating popularity bias in in-batch negatives..."** — team member sidebar comment flagging popularity bias as a known concern addressed via negative sampling strategy.

---

## Scratch / Open Design Questions

### Q1: AppConfigs — Two-layer config design

**Current state:**
- **CLR** uses a **flat single-surface config**: `LearnedRetrievalTrainerAppConfig > P2FLearnedRetrievalAppConfig`
- **CFM** uses a **two-layer pattern**: `LongSeqAppConfig` (pretrain) > `ConditionAllFMAppConfig` (fine-tune with per-surface allocation and weight loading)

**Proposal:** Combine both into a two-layer config:
- **Pretrain config:** base query/pin tower configs *(details cut off in captured screenshot — flesh out when full doc is accessible)*

This is the config-layer reflection of the overall pretrain-finetune architectural choice: infrastructure catching up to the architecture.

---

## Active review engagement (as of 2026-04-03 to 2026-04-05)

Sidebar comments in the design doc show active cross-team review:

- **Jinfeng Rao** (Apr 3, 10:31 AM) — "How do we aggregate pretraining?"
- **Piyush Maheshwari** (Apr 3, 11:54 AM) — "Each surface can define condition tower module..."
- **Hongtao Lin** (Mar 31) — "How do we decide if a [surface needs a dedicated] condition tower? e.g. ..."
- **Jiaxing Qu** (Mar 31, 8:42 PM) — Responding on condition towers, features like device type, important context features for P2P, query pin features
- **Piyush Maheshwari** (Apr 1, 7:14 AM) — "sorry @qu@pinterest.com [on] condition tower right? nomenclature..."
- **Jiaxing Qu** (Apr 1, 8:17 PM) — "synced offline. Confusion [about] different surface. We will c[larify] query pin/search query tower..."
- **Dafang He** (Apr 7) — "why device type..." (nomenclature question)
- **Hongtao Lin** — follow-up on condition tower design
- **Sai X.** (Apr 8, 8:49 AM) — "Can we also [consider] infra and efficiency..."
- **Jaewon Yang** (May 10) — "Discussed suggestion: OneTrans is..."
- **Jiaxing Qu** (Apr 7, 10:22 AM) — "P2P side, we [are] exploring for workstream..."
- **Olafur Gudmundsson** (Apr 3, 10:10 AM) — **"can we outline or reference how this will be for different use cases where applicable?"**

**Leo note on Olafur:** Olafur is both the **KDD paper Federation subsection co-author** (per Retentive Recs KDD paper plan) AND an **active reviewer on the UBR design doc**. His role is coupled across both artifacts — he is not just a KDD co-author; he is engaged on the platform architecture that Retentive Recs runs on. Upgrade his stakeholder entry from "limited information, light touch" to "active cross-project collaborator." His comment ("outline how this will be for different use cases") is the classic senior-engineer "make the abstraction concrete" ask — worth taking seriously in the design doc revision.

---

## Discussion Threads (from sidebar comments in source doc)

Active discussion threads visible in the source document include:

- **Jinfeng Rao** — "How do we aggregate pretraining?"
- **Piyush** — "Each surface can define condition tower module..."
- **Hongtao Lin** — "How do we decide if a [surface needs a dedicated] condition tower?"
- **Jiaxing Qu** — Responding on condition towers, features like device type, important context features for p2p, query pin features
- **Dafang He** — "why device type..." (nomenclature question)
- **Sai (X.)** — "Can we also [consider] infra and efficiency..."
- **Jiaewon Yang** — Referenced OneTrans as a potential direction
- **Jiaxing Qu** — "P2P side, we [are] exploring for workstream..."

**Leo note:** The comment density shows active cross-team engagement from Piyush, Hongtao, Jaewon, Jinfeng, Dafang, Sai, and Jiaxing — this is the same cross-org collaboration signal Jeff valued at the March must-win. "Team dynamic" as Jeff named it is visibly operating in the design doc itself.

---

## Connection to UPP five-prong strategy

This UBR design doc is the **technical instantiation of UPP Prongs 1-3**:

- **Prong 1 (Cross-surface training)** — provided by the multi-source dataloader + per-surface training data + shared user tower
- **Prong 2 (Scale up Base/HF CLR)** — the base model itself + FM in CLR ablation + Search CLR extension
- **Prong 3 (P2P architectural discussions + socialization)** — the Condition Tower + Surface Tower design for P2P, plus the "reserve dedicated model capacity for relevance" principle

Prongs 4 (Notifications) and 5 (HF/BMI fine-tuning) come later via the fine-tuning stage of this architecture.

---

## Open questions Leo is tracking

1. **Is "Jiaxing Qu" the same person as "Jiaqing" mentioned verbally in earlier UPP updates?** Same person, transliteration/spelling variation? Needs confirmation from James.
2. **Full technical UPP context update (James's explicit deferred item):** When James does the full technical refresh, this UBR design doc should be cross-referenced with updates to surface-specific fine-tuning details, the final CLR architecture choices, and the resolved ablation outcomes.
3. **Sophia on Search CLR** — UU team member unnamed in the Dylan update. Need identification for stakeholder map.
