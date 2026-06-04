# UPP Retrieval: What's Built, What's Missing, and What Makes This Approach Distinctive

*Assessment based on codebase analysis (May 2026) + PR #252762 + PR #251610*

---

## What's Already Built (Codebase Reality)

### The Cross-Surface Training Stack Is Live

The core UPP Retrieval trainer exists and functions end-to-end:

| Component | Status | Key Evidence |
|-----------|--------|-------------|
| **5-surface StackLoader** | Shipped | HF, BMI, P2P, Search, Notif all wired with batch mixing ratios |
| **SurfaceMetadataManager** | Mature | ~1100 lines handling per-surface feature maps, aliases, transforms, filters |
| **5 condition towers** | Shipped | HF MultiSlot, BMI/Search/Notif Concat, P2P DHEN — all with uniform output contract |
| **Label aliasing + binarization** | Shipped | Cross-surface labels mapped to HF canonical schema; count-to-binary fix for P2P |
| **Multi-head IBN loss** | Shipped | With all_gather negatives, CountMinSketch frequency correction, uid dedup masking |
| **Offline eval pipeline** | Shipped | Per-surface recall@K evaluation with configurable eval corpus strategies |
| **TorchScript deploy** | Working (with patches) | Viewer tower GPU, Pin tower CPU; PR #252762 fixes condition-tower input gaps |
| **Snapshot-based checkpointing** | Shipped | UPPRetrievalSolver forces uniform torchsnapshot format for downstream consumers |
| **Cosine LR + warmup** | Shipped | Gradual warmup then cosine annealing (with PR fix to match CLR global iteration count) |
| **ID embedding support** | Shipped | Optional TorchRec DMP path via UPPRetrievalIDEmbSolver |

### The Fine-Tuning Path (Base → Surface CLR)

PR #251610 implements the full fine-tuning infrastructure:

| Component | Status | Key Evidence |
|-----------|--------|-------------|
| **Module embedding pattern** | Built | UPP base towers embedded as `nn.Module` children in CLR model |
| **4-mode integration ladder** | Built | `none`, `into_ft_dhen`, `late_fusion`, `both` — configurable per tower |
| **Snapshot pattern remapping** | Built | `get_snapshot_load_patterns()` maps UPP keys → embedded module paths |
| **Differential LR param groups** | Built | `base_module_log10_base_lr` controls base tower learning rate independently |
| **Decomposed forward interface** | Built | `forward_pre_cross_features()` / `forward_feature_cross()` boundary |
| **Batch routing (`_ft` suffix)** | Built | Key naming convention prevents collisions in shared batch dict |
| **HomeFeedConditionedViewerTower** | Built | `modules_v2.py`: dual-branch (CLR native + embedded base) architecture |
| **Design documentation** | Written | 732-line `hf_clr_finetune.md` design doc in `upp_retrieval/` |

### What the Architecture Demonstrates

1. **The metadata-driven surface abstraction works.** Adding a surface is a configuration problem: one block in `_build_surface_metadata()` + one condition tower class. The model code (`model.py`) never branches on surface names.

2. **The condition tower output contract is enforced.** All five towers — despite having radically different internal architectures (slot-routing, DHEN, concat+FC) — produce identical shapes: `[B, 256]` token + `[B, 512]` FC. The viewer tower treats them identically downstream.

3. **Cross-surface negative diversity is real.** A single training step's pin tower processes pins from all 5 surfaces (cat along dim=0). With `all_gather_negatives=True`, the IBN loss sees `B_total x world_size` unique candidates, naturally covering diverse content types that no single surface provides alone.

4. **The deploy path separates viewer (GPU) from pin (CPU).** Viewer tower runs on GPU at query time (user-conditioned, changes per request). Pin tower runs on CPU for offline index building (fixed per pin, changes only on reindex). This is architecturally load-bearing — it determines what goes into the HNSW index vs. what's computed online.

5. **The fine-tuning pipeline is end-to-end.** A surface team can now: take any UPP base checkpoint → construct CLR model with embedded base → load snapshot with pattern remap → train with differential LR → deploy surface-specific model. No manual weight surgery needed.

6. **The integration ladder enables controlled experimentation.** Teams can A/B test `none` vs `into_ft_dhen` vs `late_fusion` vs `both` to measure the incremental value of base tower knowledge transfer, without changing model architecture.

---

## What's Missing

### 1. LoRA / Adapter Injection (Parameter-Efficient Fine-Tuning)

**The gap:** The current fine-tuning approach trains ALL base tower parameters (at reduced LR) or freezes them entirely. There's no parameter-efficient middle ground.

**What's needed:**
- LoRA adapter injection at key layers (DHEN FC, sequence transformer attention)
- Adapter configuration: rank, alpha, target modules
- Comparison: full fine-tune vs. LoRA vs. frozen+late_fusion on offline recall + compute cost

**Why it matters:** Full fine-tuning of the base tower is expensive (2x parameters to train) and risks catastrophic forgetting of cross-surface knowledge. LoRA would let surface teams adapt with ~1-5% additional parameters while preserving the base's learned representations.

### 2. Surface-Specific Output Heads

**The gap:** All surfaces share the same multi-head output structure (same heads = repin, closeup, click, etc.). Surfaces with different engagement semantics (e.g., Notif cares about "open" not "repin") must map their labels into HF's head schema.

**What's needed:**
- Per-surface head configuration (which heads are active, head-specific loss weights)
- Surface-exclusive heads (e.g., Notif "open" head that doesn't affect HF training)
- Head importance weighting per surface in the loss computation

**Why it matters:** The current approach forces all surfaces into HF's engagement model. Surfaces where "success" means something different (Search = query satisfaction, Notif = open rate) lose signal precision by mapping to HF labels.

### 3. Serving/Indexing Integration

**The gap:** The code produces TorchScript artifacts (viewer GPU + pin CPU), but there's no documentation or automation for:
- How pin embeddings flow into the HNSW index builder
- How the viewer model gets deployed to GPU serving
- The index refresh cadence / staleness trade-off
- How condition-type routing works at serving time (N forward passes x M conditions = NxM ANN lookups)

**What's needed:**
- An indexing pipeline that takes the pin tower TorchScript + full pin corpus and produces HNSW index
- Serving documentation: which conditions are active, how many embeddings per user, what latency budget
- Model versioning story: how does a new base model safely roll into production without breaking downstream surfaces?

### 4. Offline-Online Correlation Validation

**The gap:** The eval pipeline computes recall@K, but there's no systematic validation that offline recall improvements translate to online engagement gains. The `eval_segment_fns` config exists but the calibration between "recall@100 improved by 2%" and "engagement improved by X%" is undocumented.

**What's needed:**
- Historical data linking offline recall delta to online experiment delta
- Evaluation by surface segment (fresh vs. core vs. product vs. shopping pins)
- Calibration methodology: when is an offline gain large enough to warrant an online experiment?

### 5. Cross-Surface Data Contamination Analysis

**The gap:** When all 5 surfaces contribute to the same batch and IBN loss, there's an implicit assumption that negative pins from surface A are valid negatives for queries from surface B. This isn't always true:
- A pin that's irrelevant to HF (bad for interest-based retrieval) might be highly relevant to P2P (good for pin-similarity retrieval)
- The `uid_ibn_mask` (PR #252762) addresses same-user contamination but not same-intent contamination

**What's needed:**
- Analysis of cross-surface false negative rate in the IBN pool
- Potentially: surface-aware negative weighting (downweight negatives from the same surface, or mask negatives that are known positives on other surfaces for the same user)

### 6. Scaling and Operational Guardrails

**The gap:**
- No automated batch mixing ratio tuning (currently hardcoded per-surface)
- No surface-specific gradient monitoring (is one surface dominating the loss?)
- No automated data quality checks (what if a surface's data pipeline breaks and sends garbage for 3 days?)
- No documentation of compute budget: training cost per iteration, total training time, GPU-hours

**What's needed:**
- Per-surface loss tracking in W&B with alerts
- Data quality gates (row count sanity, label distribution drift)
- Automated mixing ratio adjustment based on surface loss convergence rates

### 7. Condition Dropout / Augmentation Strategy

**The gap:** The original CLR has explicit condition dropout (10% of training steps mask the condition entirely). The UPP codebase doesn't have this — conditions are always present. This means:
- The model has never seen "no condition" at training time
- Serving a "fallback" retrieval (user without any specific condition) would produce undefined behavior

**What's needed:**
- Condition dropout configuration (per-surface or global)
- A "none" condition type that produces a generic user embedding
- Testing that the model degrades gracefully when condition features are missing

---

## What Makes This Approach Uniquely Important

### 1. The "Condition Tower as Surface Adapter" Pattern

**Why it's distinctive:** Most industry approaches to multi-task/multi-surface retrieval either:
- Train completely separate models per surface (Google: separate towers per use case)
- Use a single shared model with task heads (Meta: shared backbone + per-task MLP heads)

UPP Retrieval does **neither**. It uses a shared backbone but injects surface identity through a *structural* mechanism (the condition tower) rather than a *parametric* one (a task-ID embedding or separate head). The condition tower actively **transforms the input** (pops its features, writes new tokens/FC into the batch) rather than passively modulating the output.

**Consequences:**
- The sequence transformer sees condition-dependent tokens — the user history is *interpreted differently* depending on condition type
- The DHEN feature cross sees condition FC output as a first-class field — cross-surface feature interactions happen at the structural level
- At serving time, the condition tower is part of the TorchScript artifact — no separate "condition router" service needed

**Analogy:** If MLM fine-tuning is "change the head", UPP's condition tower is closer to "change the prompt" — it modifies what the model sees rather than what it predicts from.

### 2. Cross-Surface Contrastive Negatives (Natural Hard-Negative Mining)

**Why it's distinctive:** Standard two-tower training uses in-batch negatives from the same distribution. This creates a well-known failure mode: if all negatives are "kitchen pins" (because the user's HF is dominated by cooking), the model never learns to distinguish kitchen pins from travel pins — it just memorizes easy decision boundaries.

UPP's StackLoader **guarantees cross-surface diversity in every batch**. A single batch contains:
- HF pins (interest-driven engagement)
- P2P pins (visually similar pins)
- BMI pins (board-context pins)
- Search pins (query-relevant pins)
- Notif pins (notification-triggered engagement)

This means pin embeddings must encode content properties that generalize across retrieval intents. A pin that's only "good for notifications" but encodes no visual/semantic content will be a bad negative for HF and will receive correct gradient signal from the HF portion of the batch.

**The result:** Cross-surface training acts as an implicit hard-negative curriculum. No explicit hard-negative mining pipeline needed — the surface diversity provides it structurally.

### 3. The "Surface as Plugin" Development Velocity

**Why it's distinctive:** The metadata-driven architecture means a new surface team can onboard to UPP Retrieval by:
1. Writing a `SurfaceMetadata` config (feature map, labels, aliases, filters) — no Python model code
2. Writing a condition tower class (~100 lines for a `_ConcatConditionTower` subclass)
3. Setting a `batch_mixing_ratio` in the surface config

Compare this to the industry norm where adding a new retrieval surface means:
- Cloning an entire model repo
- Re-implementing dataloading
- Training from scratch
- Building separate serving infrastructure

UPP makes surface onboarding an **additive, non-breaking** operation. The base model keeps training; the new surface starts receiving gradient signal immediately; no other surface's performance is affected (batch mixing just redistributes budget).

**Evidence from codebase:** Search was added after the initial HF+P2P+BMI stack. The PR history shows it was a ~200-line metadata addition + one `SearchConditionTower` class (inherits `_ConcatConditionTower` with zero overrides). Notif followed the same pattern with slightly more complexity (virtual labels, shared interest_id embedding).

### 4. The Shared Interest-ID Embedding as Cross-Surface Transfer Signal

**Why it's distinctive:** HF and Notif both use `interest_id` as a condition feature. Rather than having separate embedding tables, UPP shares a single `BatchIdEmbeddingTable` by reference between the two condition towers.

This means:
- Gradient from HF interest-conditioned training updates the same parameters as Notif interest-conditioned training
- An interest that's well-represented in HF data (e.g., "recipes") automatically improves Notif retrieval for that interest, even if Notif has sparse data for it
- The embedding table sees ~55% of batch volume (HF 50% + Notif 5%) instead of being split into two 50%/5% tables with no cross-pollination

**This is the UPP value proposition in microcosm:** shared parameters that receive gradient from multiple surfaces, creating transfer effects that no single-surface model can achieve.

### 5. Multi-Head Retrieval with Shared Pin Embedding

**Why it's distinctive:** The model produces `[B, num_heads, D]` viewer embeddings but only `[B, D]` pin embeddings. This means:
- The **same pin embedding** is used by all retrieval heads (repin, closeup, click, etc.)
- At serving time, only one HNSW index is needed (over pin embeddings)
- Multiple retrieval intents (save-intent, browse-intent) can be served from a single index lookup

The multi-head structure exists purely for **training regularization**: auxiliary heads (closeup, click) provide gradient diversity that improves the primary head. This is cheaper than training separate models per intent and maintains a single serving infrastructure.

**Industry comparison:** Meta's approach often uses separate indices per retrieval intent. Google's approach often uses a single embedding but with multiple retrieval conditions (similar to CLR). UPP's approach is closest to Google's but with the cross-surface training dimension that neither company's published work describes in this form.

### 6. Module-Embedding Fine-Tuning (The "Improve Base, All Surfaces Benefit" Mechanism)

**Why it's distinctive:** The fine-tuning architecture (PR #251610) is the mechanism that closes the loop on UPP's cross-surface value proposition. Without it, "improve base" was aspirational. With it, the flow is concrete:

```
UPP Base (cross-surface training) → snapshot → Module embed into CLR →
Differential LR fine-tuning → Surface-specific model → Deploy
```

**What makes this approach unusual vs. industry norms:**

1. **Module embedding > weight copying.** Meta and Google fine-tuning typically copies/renames state_dict keys into a new architecture. UPP embeds the original module as a child — preserving the exact forward pass, enabling TorchScript of both standalone and embedded variants from the same code.

2. **The integration ladder is a research tool.** The 4-mode system (`none` / `into_ft_dhen` / `late_fusion` / `both`) isn't just config — it's a built-in ablation framework. Teams can measure the marginal value of base knowledge at each integration depth without separate model implementations.

3. **Decomposed forward as a stable API.** By splitting the tower into `forward_pre_cross_features()` and `forward_feature_cross()`, the architecture creates a versioned interface. Base tower internals can evolve (new layers, different attention) without breaking downstream CLR models — as long as the intermediate feature dict shape is preserved.

4. **The `_ft` suffix convention is a routing protocol.** Batch-level key namespacing via suffix means multiple models can coexist in the same training loop consuming the same dataloader output. This is unusual — most fine-tuning approaches use separate dataloaders or forward passes.

---

## Strategic Implications

### The Bet

UPP Retrieval is betting that:
1. **Cross-surface data provides better representations than any single surface can** — the model learns general "pin quality" signals that transfer
2. **Surface-specific condition towers are sufficient to specialize** — you don't need separate models
3. **A single pin embedding can serve all retrieval intents** — the pin tower doesn't need to specialize
4. **Module embedding fine-tuning preserves cross-surface knowledge while enabling surface specialization** — the integration ladder finds the right transfer-specialization balance

### The Risk

1. **Negative interference:** If surfaces have conflicting objectives (e.g., Notif wants "clickable" pins, HF wants "saveable" pins), the shared pin tower may compromise on both
2. **Batch mixing sensitivity:** The 50/20/15/10/5 split is arbitrary. If the optimal ratios change per-surface, the shared model might under-serve minority surfaces
3. **Deploy complexity:** All 5 surfaces coupled through one model means a training regression affects everyone simultaneously. No blast-radius isolation.
4. **Fine-tuning drift:** If CLR fine-tuning heavily modifies base tower parameters (even at reduced LR), the "improve base, all surfaces benefit" loop breaks — each surface's CLR diverges from the base, requiring re-fine-tuning on every base update
5. **Integration mode explosion:** With 4 viewer modes × 4 pin modes × N LR choices, the hyperparameter search space for fine-tuning is large. Without strong offline-online correlation, teams may over-fit to offline metrics.

### The Moat

If the approach works:
- Adding surface N+1 is near-zero marginal cost (config + small tower class)
- Every surface gets better as ANY surface's data improves
- Serving cost is O(1) pin index + O(surfaces) query evaluations, not O(surfaces) separate indices
- Engineering headcount needed per surface drops dramatically — one team maintains the base model
- Surface teams get a "free" starting point — embed the latest base, measure integration modes, ship the best one without training from scratch

---

*Written 2026-05-31, updated with PR #251610 fine-tuning architecture*
