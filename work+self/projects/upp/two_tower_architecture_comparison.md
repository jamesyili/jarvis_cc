# Two-Tower Architecture Comparison: Homefeed CLR vs. Closeup Learned Retrieval

## Table of Contents
- [1. Problem Statement](#1-problem-statement)
- [2. High-Level Architecture](#2-high-level-architecture)
- [3. Query Tower Design](#3-query-tower-design)
- [4. Candidate Tower Design](#4-candidate-tower-design)
- [5. Feature Crossing / DHEN](#5-feature-crossing--dhen)
- [6. User Sequence Transformer](#6-user-sequence-transformer)
- [7. Condition / Context System](#7-condition--context-system)
- [8. Loss Functions](#8-loss-functions)
- [9. Label Extraction and Heads](#9-label-extraction-and-heads)
- [10. Training Pipeline](#10-training-pipeline)
- [11. Inference and Deployment](#11-inference-and-deployment)
- [12. Feature Summary Table](#12-feature-summary-table)
- [13. Shared Infrastructure](#13-shared-infrastructure)
- [14. Key File Reference](#14-key-file-reference)

---

## 1. Problem Statement

Both systems solve retrieval using the two-tower paradigm (encode query and candidate independently, score by dot product), but for fundamentally different surfaces:

| | Homefeed CLR | Closeup LR |
|---|---|---|
| **Surface** | Homefeed (main feed) | Related Pins (closeup page) |
| **Query** | "What should this user see next?" | "What pins are related to this pin for this user?" |
| **Query signal** | User + retrieval condition (interest/board/pin) | User + specific query pin |
| **Candidate** | Any pin in the corpus | Pins related to the source pin |
| **Retrieval key** | User intent (varies by condition) | Query pin content + user preference |

The core architectural difference follows from this: CLR must produce **multiple embeddings per user** (one per condition type), while Closeup LR produces **one embedding per (user, query_pin) pair** (possibly multi-head).

---

## 2. High-Level Architecture

### Homefeed CLR

```
                    ┌─────────────────────────────────────┐
                    │         Viewer Tower                 │
                    │                                     │
  User Features ──> │  ┌──────────────────────┐           │
                    │  │  UserConditionTower   │           │
  Condition ──────> │  │  (routing + tokens)   │──> DHEN ──> viewer_emb [B, H, D]
                    │  │  + Seq Transformer    │           │
  User Sequence ──> │  └──────────────────────┘           │
                    └─────────────────────────────────────┘

  Pin Features ──>  ┌──────────────┐
                    │  Pin Tower   │──────────────────────> pin_emb [B, D]
                    └──────────────┘

  Score = dot(viewer_emb, pin_emb)

  At inference: N forward passes (1 per condition) -> N embeddings -> N ANN lookups
```

### Closeup LR

```
                    ┌──────────────────────────────────────────────┐
                    │           Viewer Tower                        │
                    │                                              │
  User Features ──> │  ┌──────────┐  ┌──────────┐  ┌───────────┐ │
                    │  │ User DHEN│  │ Pin DHEN │  │Context MLP│ │
  Query Pin ──────> │  └────┬─────┘  └────┬─────┘  └─────┬─────┘ │
                    │       └──────┬──────┘──────────────┘        │
  User Sequence ──> │         Final DHEN + MLP                     │──> viewer_emb [B, H*D]
                    └──────────────────────────────────────────────┘

  Cand Pin ──────>  ┌──────────────────┐
                    │  Pin Tower (DHEN) │───────────────────────────> pin_emb [B, D]
                    └──────────────────┘

  Score = dot(viewer_emb, pin_emb)

  At inference: 1 forward pass -> 1 embedding per head -> 1 ANN lookup
```

---

## 3. Query Tower Design

### CLR: ConditionedViewerTower

The viewer tower is split into two sub-paths that are processed independently and merged:

```
split_batch()
    │
    ├── Unconditioned features ──> format -> embed -> UOE/language/coterie modules
    │
    └── Condition features + sequence ──> UserConditionTower:
            ├── create_routing_masks()       (priority: interest > board > pin)
            ├── condition dropout (10%)
            ├── interest/text dropout (25%)
            ├── format -> embed
            ├── TextEmbeddingModule (SearchSage, PinCLIP)
            ├── ConditionRouter -> condition_tokens [B, 64]
            └── ConditionedUserSequenceTransformer
                    (appends condition tokens to sequence)
                    -> proj_user_seq, proj_cond_seq, all_cond_feature_combined
    │
    └── Merge outputs ──> DHEN feature crossing (feature_mix_dict weighted)
```

**Key design:** Condition features flow through a dedicated `UserConditionTower` module. The condition token is injected into the transformer as an additional sequence position that attends to the user's action history.

### Closeup LR: DHENViewerTower

The viewer tower sees both user and query pin features, which are split by name prefix and processed in parallel sub-towers:

```
format -> embed -> (optional sequence transformer)
    │
    ├── user_features (k contains "user") ──> DimUnifier -> LayerNorm -> DHEN_user
    ├── pin_features  (k contains "pin")  ──> DimUnifier -> LayerNorm -> DHEN_pin
    └── context_features (k contains "context") ──> context_MLP
    │
    └── Combine: DimUnifier(user, pin, context) -> LayerNorm -> Final DHEN -> MLP
```

**Key design:** The query pin is not a "condition" that modifies the user representation - it's a first-class feature group with its own DHEN sub-tower. User and pin representations are fused at the final crossing layer. Parallel processing uses `torch.jit.fork/wait`.

### Side-by-Side: Query Tower

| Aspect | CLR | Closeup LR |
|--------|-----|------------|
| **Input features** | User only (conditions separated) | User + query pin (split internally) |
| **Feature group source** | `PASSED_IN_DATA` | `PASSED_IN_DATA` |
| **Sub-tower split** | Conditioned vs unconditioned | User vs pin vs context (by name prefix) |
| **Condition/query pin handling** | Routed through ConditionRouter -> token -> transformer | Processed as a parallel DHEN sub-tower |
| **Number of sub-towers** | 2 (condition tower + main tower) | 3 (user DHEN + pin DHEN + context MLP) |
| **Representation layers** | Shared dense normalization | Separate user and pin normalization pipelines |
| **Text embeddings** | SearchSage + PinCLIP (projected) | Not used |
| **Output shape** | `[B, H, D]` | `[B, H*D]` (reshaped to `[B, H, D]`) |

---

## 4. Candidate Tower Design

### CLR: PinTower

Standard pin tower inherited from the base `TwoTowerModel`. Features from `PINNABILITY_PIN_FEATURES`.

```
features -> format -> representation_layers -> embed -> DHEN -> pin_emb [B, D]
```

No special modifications for CLR - the pin tower is condition-agnostic.

### Closeup LR: DHENPinTower / PinTowerOrganic

Features from `RELATED_PINS_UFR_CAND_PIN_FEATURES`. Optionally integrates semantic IDs.

```
features -> nan_to_num -> group -> (dropout) -> format -> representation
    -> embed OR sid_embedding_layer (RQ-VAE encode + cascading fusion)
    -> DHEN (DimUnifier -> LayerNorm -> DHEN -> Linear)
    -> pin_emb [B, D]
```

### Side-by-Side: Candidate Tower

| Aspect | CLR | Closeup LR |
|--------|-----|------------|
| **Feature source** | `PINNABILITY_PIN_FEATURES` | `RELATED_PINS_UFR_CAND_PIN_FEATURES` |
| **Semantic IDs** | Not used | RQ-VAE tokenizer (8 codebooks x 2048 codes) + cascading MLP fusion |
| **Feature dropout** | Not used | Optional `FeatureDropOutInput` |
| **NaN handling** | `_fill_na(batch)` | `torch.nan_to_num(0.0)` |
| **Feature crossing** | DHEN (via base TwoTowerModel) | DHEN with DimensionUnifier |
| **Normalization** | Optional L2 norm | Optional L2 norm |
| **Embedding table** | Shared with viewer tower | Optionally separate (`separate_embedding_layers`) |

---

## 5. Feature Crossing / DHEN

Both models use DHEN (Deep Hierarchical Embedding Network) for feature interaction, but with different architectures.

### CLR DHEN

Uses `feature_mix_dict` to control feature group weights in a flat DHEN:

```python
feature_mix_dict = {
    "continuous": 1,
    "proj_user_seq": 2,
    "all_cond_feature_combined": 8,   # condition features dominate
    "proj_cond_seq": 2,
    "pinnersage_v3e_static_realtime": 1,
    "pinnersage_v3e_static": 1,
}
```

All features are mixed in a single DHEN layer. The weight of 8 on condition features ensures the embedding is heavily condition-dependent.

### Closeup LR DHEN

Uses a **hierarchical multi-tower DHEN** with three levels:

1. **User DHEN**: Processes user features independently
2. **Pin DHEN**: Processes query pin features independently
3. **Final DHEN**: Crosses the outputs of user, pin, and context sub-towers

Each level has its own config (`dhen_user_config`, `dhen_pin_config`, `dhen_final_crossing_config`) with independent:
- `per_field_dim`, `transformer_heads`, `transformer_num_layers`
- `dhen_interaction_list` (which interaction types: transformer, DCNv2, MLP, MaskNet)
- `dhen_ensemble_mode` (how interactions are combined)

### DimensionUnifier (Closeup LR only)

Before DHEN, all feature groups are projected to a uniform dimension via `LazyDimensionUnifier`:

```python
class LazyDimensionUnifier(nn.Module):
    # Special: continuous features are replicated N times (default 4)
    # with separate linear projections, giving DHEN multiple "views"
    # of the same continuous features
    for key in batch:
        if key in {"user_continuous", "pin_continuous", "continuous"}:
            for i in range(4):
                output.append(linear_i(tensor))  # 4 projections
        else:
            output.append(linear(tensor))  # 1 projection
    return torch.stack(output, dim=1)  # [B, num_fields, per_field_dim]
```

CLR doesn't use DimensionUnifier - features go through `BatchMLPSummarization` instead.

---

## 6. User Sequence Transformer

Both models encode user action history with a Transformer, but the implementations differ significantly.

### CLR: ConditionedUserSequenceTransformer

```
Inputs:
  action_types [B, 500] -> embed [B, seq_len, 32]
  seq_embeddings (OmniSage int8) [B, 500, 32] -> dequantize
  condition_tokens [B, num_cond_tokens, 64]

Token: [action_emb(32) | omnisage_emb(32)] = 64D
  + condition tokens appended at end of sequence

Transformer: d_model=64, d_ffn=32, 8 heads, 2 layers, pre-layer-norm

Output:
  proj_user_seq: last N positions projected
  proj_cond_seq: condition token positions projected + residual
```

### Closeup LR: UserSequenceTransformerEncoder

```
Inputs:
  action_types [B, 200] -> vocab lookup -> embed [B, seq_len, 16]
  seq_embeddings [B, 200, 32]
  surface_types [B, 200] -> vocab lookup -> embed [B, seq_len, 8]
  timestamps [B, 200] -> log-bucket -> embed [B, seq_len, 16]

Token: [action_emb(16) | seq_emb(32) | surface_emb(8) | timestamp_emb(16)] = 72D

Transformer: configurable d_model/d_ffn/heads/layers

Output:
  max_pool(linear(tfmr_out)) + flatten(latest_n_emb)
```

### Side-by-Side: Sequence Transformer

| Aspect | CLR | Closeup LR |
|--------|-----|------------|
| **Sequence length** | 500 (trimmed to 100) | 200 (trimmed to configurable seq_len) |
| **Sequence embeddings** | OmniSage v1 32D int8 sparse | OmniSage 32D |
| **Action embedding dim** | 32 | 16 |
| **Token composition** | action(32) + omnisage(32) = 64D | action(16) + omnisage(32) + surface(8) + timestamp(16) = 72D |
| **Surface embedding** | Not used | 8D, vocab of 24 surface types |
| **Timestamp embedding** | Not used (only for filtering) | 16D, 50 log-spaced buckets (0 to 1 year) |
| **Condition tokens** | Appended to sequence, attend via self-attention | Not used (query pin is in a separate tower) |
| **Context features as tokens** | Not used | Optional: GSV5 mini + PinnerSage mini prepended |
| **Time window masking** | Optional date filtering (zero out old actions) | Random time window masking during training |
| **Output extraction** | Separate user seq projection + condition projection | Max pool + latest N flatten |
| **Residual connection** | Raw condition tokens added back to output | Not used |
| **Transformer config** | d=64, ffn=32, 8 heads, 2 layers, pre-norm | Configurable, JIT-scripted |

---

## 7. Condition / Context System

This is the most fundamental architectural difference between the two models.

### CLR: Explicit Condition Routing

CLR has a formal condition system with three types:

| Type | Feature | Signal |
|------|---------|--------|
| Interest | `common_pin_source_interest_id` + SearchSage + PinCLIP | Topical category |
| Board | `common_omnisage_v1_board_256d_fp16` | Board context |
| Pin | `common_omnisage_v1_pin_256d_fp16` | More-like-this |

**Routing:** Priority-based assignment (interest > board > pin). Each sample gets exactly one condition. Routing is done by checking for non-default feature values.

**Token generation:** Condition features -> `ConditionTokenGenerator` (pad or MLP) -> 64D token -> appended to transformer sequence.

**Multi-output inference:** At serving time, produces one embedding per condition type (via dummy features and multiple forward passes). Each embedding does a separate ANN lookup, yielding different candidate sets per retrieval context.

### Closeup LR: Implicit Query Context

Closeup LR has no explicit condition system. The query pin IS the context:

- Query pin features (OmniSage embedding, content type, annotations) flow through `PASSED_IN_DATA`
- They enter the viewer tower alongside user features
- The DHEN sub-tower architecture (user DHEN vs pin DHEN) provides structured interaction
- A single embedding is produced per (user, query_pin) pair

**There is no multi-output inference** - each query produces exactly one viewer embedding (per head). Different query pins naturally produce different embeddings.

### Why the Difference?

On homefeed, the system needs to retrieve pins for a user across multiple possible intents *simultaneously* (what interests them, what boards they're building, what pins they want more of). These are all active at once, requiring multiple parallel ANN lookups.

On closeup, the context is already determined - the user clicked on a specific pin. There's only one retrieval context per request.

---

## 8. Loss Functions

### Shared

Both use `InBatchNegativeLoss` as the primary loss with learnable temperature and optional sample probability correction via Count-Min Sketch.

| Loss | CLR | Closeup LR |
|------|-----|------------|
| **In-batch negative** | `InBatchNegativeLossMultihead` | `InBatchNegativeLossMultihead` |
| **Temperature** | Learnable, clamped to log(100) | Learnable, clamped to log(100) |
| **Sample prob correction** | CpuBasedCounter or CountMinSketch | CpuBasedCounter or CountMinSketch |
| **UID masking** | `uid_ibn_mask=True` (mask same-user negatives) | Not used (P2P uses candidate sigs, not UIDs) |
| **Logistic loss** | BCE with `global_bias` per head | BCE with `global_bias` AND `global_temp` per head |
| **Relevance loss** | `\|\|PinCLIP_sim - TT_sim\|\|^2 * 200000` | Not used |
| **Distillation** | Not used | MSE from teacher model with separate `global_bias_distill` and `global_temp_distill` |
| **SID contrastive** | Not used | Symmetric InfoNCE per codebook level |
| **C2C contrastive** | Not used | Co-occurrence loss (same-query candidates closer) |
| **Q2Q contrastive** | Not used | Co-occurrence loss (same-candidate queries closer) |
| **Random negatives** | Not used | Separate dataloader stream merged with in-batch |
| **Dedup negatives** | Configurable | Configurable |
| **AllGather negatives** | Optional (multi-GPU) | Optional (multi-GPU) with `max_rndneg` cap |

### CLR Total Loss
```
L = ibn_weight * L_ibn + logistic_weight * L_log + L_relevance
```

### Closeup LR Total Loss
```
L = ibn_weight * L_ibn
  + logistic_weight * mean(L_log_per_head)
  + distill_weight * L_distill
  + sid_weight * L_sid_contrastive
  + c2c_weight * L_c2c
  + q2q_weight * L_q2q
```

---

## 9. Label Extraction and Heads

### CLR

Uses the homefeed two-tower label extractor. Heads are defined by engagement signals in the training data (e.g., repin, closeup). Labels come from `LABEL/` features in the batch. The label extractor is inherited from the base `TwoTowerModel`.

### Closeup LR: P2PLearnedRetrievalLabelExtractor

A dedicated label extractor with P2P-specific logic:

**Action types tracked:**
- Closeup, clickthrough, long_clickthrough, repin, screenshot, save_to_device, react, revisitation_7d

**Three head modes:**

| Mode | Config | Heads |
|------|--------|-------|
| Multi-head | `multi_head=True` | One per action type (8 heads) |
| Combined single | `use_combined_head=True` | 1 head: label=1 if ANY action positive |
| Combined multi | `enable_combined_multi_head=True` | 3 heads: close_up, combined_clicks, combined_srsd |

**Hard negatives (Closeup LR only):**
```python
HARD_NEGATIVE_ACTIONS = [SHORT_CLICKTHROUGH, HIDE]
NEGATIVE_ACTION_WEIGHTS = {SHORT_CLICKTHROUGH: 3.0, HIDE: 3.0}
```
If a sample has a positive label (e.g., closeup) AND a hard negative (e.g., hide), the label flips to 0 with weight 3.0. CLR does not use hard negatives.

**Content boosting (Closeup LR only):**
- `tw_product_boost`: Multiplies weight for product pins (content_type == 4)
- `fresh_boost`: Multiplies weight for fresh pins

---

## 10. Training Pipeline

| Aspect | CLR | Closeup LR |
|--------|-----|------------|
| **Trainer class** | Inherited from `two_tower/trainer_v2.py` | `P2PLearnedRetrievalTrainer` (extends `CloseupBaseRunner`) |
| **Config** | `BaseConditionalTrainerConfigBundle` | `P2PLearnedRetrievalConfigBundle` |
| **Data format** | Proprietary (via MLEnv feature registry) | Tabular ML (parquet, via `TabularMLDataset`) |
| **Data loading** | Single dataloader | `StatefulStackLoader` (train + index for random negatives) |
| **Feature stats** | Pre-computed from S3 | `load_or_calc_feature_stats()` (auto-calculates if missing) |
| **Optimizer** | Configurable | `FusedAdam(lr, betas=(0.9, 0.999))` |
| **LR schedule** | Warmup (5000 steps) | Constant (no warmup, no decay) |
| **Batch size** | 6000 | Configurable (halved if random negatives enabled) |
| **Solver** | `TwoTowerFaultTolerantSolver` | `TwoTowerFaultTolerantSolver` |
| **Checkpointing** | Standard | `WandbCheckPointManager` + stateful dataloader snapshots |
| **Warm start** | Snapshot loading with `reset_parameter_pattern` / `allowed_mismatched_pattern` | `load_pretrain_weights()` |
| **Tower freezing** | Not standard | `freeze_viewer_tower`, `freeze_pin_tower` options |
| **Teacher model** | Not used | Optional TorchScript teacher for distillation |
| **Tokenizer** | Not used | Optional RQ-VAE tokenizer (frozen) |
| **Feature attribution** | Not standard | Optional `run_attribution` at final eval |
| **HPT objective** | Various recall metrics | `eval_w_repin/ALL_10` (repin recall@10) |

### Training-Time Regularization

| Technique | CLR | Closeup LR |
|-----------|-----|------------|
| **Condition feature dropout** | 10% per condition | N/A |
| **Interest/text dropout** | 25% each (mutually exclusive) | N/A |
| **Pin feature dropout** | N/A | Configurable prob + column list |
| **Random time window** | N/A | Random masking of recent actions |
| **Hard negative relabeling** | N/A | Short clicks + hides flip labels |

---

## 11. Inference and Deployment

### CLR Multi-Condition Inference

```
User request arrives with interest/board/pin conditions
    │
    ├── Create dummy features for all condition types
    ├── For each condition variant:
    │     └── forward(unconditioned_batch + condition_batch)
    │         -> viewer_emb_for_condition [B, D]
    │
    ├── Stack: [B, num_conditions, D]
    ├── int8 quantize
    │
    └── Each condition embedding -> separate HNSW lookup -> different candidate sets
        -> merge & rank downstream
```

Options: sequential with `jit.fork/wait` or batched GPU mode (batch_size * num_conditions).

### Closeup LR Single-Pass Inference

```
User + query pin request arrives
    │
    ├── viewer_tower(features) -> viewer_emb [B, H*D]
    ├── pin_tower(features)    -> pin_emb [B, D]
    │
    ├── Normalize both
    ├── Dot product score (summed across heads, or per-head for multi-head)
    │
    └── Single ANN lookup with viewer_emb
```

### Side-by-Side: Deployment

| Aspect | CLR | Closeup LR |
|--------|-----|------------|
| **Export format** | TorchScript (separate viewer + pin) | TorchScript (separate viewer + pin) |
| **Quantization** | int8 output embeddings | Not standard (float32) |
| **CUDA graphs** | Static shape optimization | Not used |
| **MLflow logging** | Yes | Yes (with `auto_promote_stage`) |
| **Model naming** | `{name}_pin_scorpion`, `{name}_viewer_scorpion` | `{name}_pin_scorpion`, `{name}_viewer_scorpion` |
| **Multi-condition output** | Yes (N embeddings per user) | No (1 embedding per query) |
| **Inference parallelism** | `jit.fork` across conditions | `jit.fork` across DHEN sub-towers |

---

## 12. Feature Summary Table

| Feature | CLR | Closeup LR |
|---------|-----|------------|
| Surface | Homefeed | Related Pins (Closeup) |
| Query type | User + condition | User + query pin |
| Candidate source | `PINNABILITY_PIN_FEATURES` | `RELATED_PINS_UFR_CAND_PIN_FEATURES` |
| Condition system | 3 types (interest/board/pin) with routing | None (query pin is implicit context) |
| Multi-output | Yes (1 per condition) | No (1 per query) |
| Codebase | Extends `mlenv/two_tower/` | Standalone in `closeup/` |
| DHEN architecture | Flat (feature_mix_dict weighted) | Hierarchical (user/pin/context sub-towers) |
| Semantic IDs | No | RQ-VAE (8 codebooks x 2048) |
| Text embeddings | SearchSage + PinCLIP (256D each) | No |
| Sequence token dim | 64D (action + OmniSage) | 72D (action + OmniSage + surface + timestamp) |
| Condition tokens in transformer | Yes (appended, with residual) | No |
| Embedding tables | Shared | Optionally separate per tower |
| Hard negatives | No | Short click + hide (3x weight) |
| Random negatives | No | Separate dataloader |
| Distillation | No (relevance loss from PinCLIP) | MSE from teacher model |
| Auxiliary losses | Relevance loss only | SID contrastive, C2C, Q2Q |
| Gradient analysis | No | Per-head cosine similarity tracking |
| Content/fresh boosting | No | `tw_product_boost`, `fresh_boost` |
| Warm start strategy | Pattern-based reset/mismatch | Direct weight loading |
| LR schedule | Warmup then constant | Constant (no warmup) |

---

## 13. Shared Infrastructure

Despite being separate codebases, both models share several foundational components:

| Component | Location | Used By |
|-----------|----------|---------|
| `InBatchNegativeLossMultihead` | `modules/metric_learning.py` | Both |
| `CountMinSketch` / `CpuBasedCounter` | `modules/approx.py` | Both |
| `AllGatherWithGrad` | `modules/negatives.py` | Both |
| `BinnedAUC` | `modules/metrics.py` | Both |
| `FormatFeatureRegistryInput` | `common/modules/input.py` | Both |
| `BatchMergedIdEmbeddingTable` | `common/packageable_modules/id_embedding_table.py` | Both |
| `FullyConnectedLayers` | `common/packageable_modules/fully_connected_layers.py` | Both |
| `LazyLayerNorm` | `common/packageable_modules/lazy_layernorm.py` | Both |
| `LazyConcatInput` | `common/packageable_modules/input.py` | Both |
| `BatchMLPSummarization` | `common/packageable_modules/summarization.py` | Both |
| `LazyMergedTransformerMixer` | `common/modules/feature_cross.py` | Both (optional) |
| `EnsembleInteractionLayers` (DHEN) | `ads/l2/common/modules/ensemble_interactions.py` | Both |
| `TwoTowerFaultTolerantSolver` | `two_tower/solver.py` | Both |
| `generate_embedding_vocabs` | `common/automl_utils.py` | Both |
| `maybe_dedup_negatives` | `two_tower/utils.py` | Both |
| `TorchScriptDeployInfo` | `utils/torchscript_converter.py` | Both |
| `build_torchscript_convert_fn` | `common/utils.py` | Both |

---

## 14. Key File Reference

### Homefeed CLR

| File | Purpose |
|------|---------|
| `two_tower/conditional_learned_retrieval/model.py` | `ConditionalTwoTowerModel`, `ConditionalDHENTwoTowerModel` |
| `two_tower/conditional_learned_retrieval/modules.py` | `ConditionRouter`, `ConditionTokenGenerator`, `ConditionedUserSequenceTransformer`, `UserConditionTower`, `ConditionedViewerTower` |
| `ml_resources/.../configs/features/feature_names.py` | Feature IDs, `create_routing_masks()`, `is_default_value()` |
| `ml_resources/.../configs/base_conditional_lr_config_bundles.py` | Training configs |
| `ml_resources/.../configs/config_bundle_defs.py` | `ConditionalRetrievalConfig`, `ConditionTagConfig` |
| `two_tower/model.py` | Base `TwoTowerModel`, `ViewerTower`, `PinTower` |
| `two_tower/model_zoo/dhen_model.py` | `DHENTwoTowerModel` |

### Closeup LR

| File | Purpose |
|------|---------|
| `closeup/p2p_learned_retrieval/model.py` | Production `TwoTowerModel` with all loss functions |
| `closeup/p2p_learned_retrieval/modules.py` | `PinTowerOrganic`, `ViewerTowerOrganic`, `DHENPinTower`, `DHENViewerTower`, `DimensionUnifier`, contrastive losses |
| `closeup/p2p_learned_retrieval/label_extractor.py` | `P2PLearnedRetrievalLabelExtractor` |
| `closeup/p2p_learned_retrieval/train.py` | `P2PLearnedRetrievalTrainer` |
| `closeup/p2p_learned_retrieval/filters.py` | Data filtering functions |
| `closeup/p2p_learned_retrieval/eval_utils.py` | Inference functions |
| `closeup/p2p_lws/two_tower/model.py` | Base `TwoTowerModel` for LWS |
| `closeup/p2p_lws/two_tower/modules.py` | Base towers and sequence transformer |
| `ml_resources/mlenv/p2p/configs/learned_retrieval_train_config.py` | `P2PLearnedRetrievalAppConfig` |

All paths relative to `machine-learning/trainer/ppytorch/mlenv/`.
