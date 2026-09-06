# Retrieval and Pre-Ranking in Large-Scale Recommenders, 2021–2026
## A unified synthesis of two deep-research reports

**Compiled:** September 5, 2026
**Inputs:**
- **Report A** — "Step-Function Innovations in Retrieval and Pre-Ranking for Large-Scale Recommenders (2021–2026)." Systems-and-strategy narrative; primary-sourced (arXiv IDs, production A/B numbers); includes recommendations and caveats.
- **Report B** — "Groundbreaking Innovations in Retrieval and Pre-Ranking for Large-Scale Recommendation Systems (2021–2026)." Mechanisms narrative; survey-sourced; strong on *why* individual methods work.
- **Verification searches** run during synthesis (UxSID, Pinterest multi-embedding retrieval, 2025–26 semantic-ID literature).

**How to read this document**
- Part 0 is the executive summary.
- Part I merges the substantive content of both reports into one landscape, organized by theme rather than by source. Where a claim comes from only one report it is tagged [A] or [B]; verified additions from this synthesis are tagged [S].
- Part II is the synthesis proper: what each report contributes and seven synergies visible only when both are read together.
- Part III lists what is missing from both.
- Parts IV–VII: recommendations, caveats and factual flags, timeline, reading list.

---

## 0. Executive summary

**Three step-functions define the period.**
1. **The generative / sequence-scaling paradigm.** Reformulating retrieval (and increasingly ranking) as autoregressive generation over semantic-ID tokens gave recommenders LLM-style scaling laws for the first time. Flagship proofs: Meta HSTU (1.5T parameters, +12.4% online A/B), Kuaishou OneRec (end-to-end generative model serving 25% of QPS, OPEX ~10.6% of the legacy pipeline), Google PLUM (LLM-based generative retrieval in production at YouTube).
2. **Cross-stage consistency in pre-ranking.** COLD reframed L1 as algorithm–system co-design; the 2021–25 wave (RankFlow, logit distillation, COPR, CIT, RankTower, SDCL, ECM) turned L1 from a "shrunken ranker" into a funnel component jointly optimized with L2 and trained on the space it actually serves.
3. **Infrastructure and data unlocks preceded the modeling shifts.** Collisionless/streaming embedding systems (Monolith), trillion-parameter embedding training (Neo/ZionEX, TorchRec), accelerator co-design (MTIA, TPU SparseCore, cuVS/CAGRA), efficient generative inference (M-FALCON, FP8), and multimodal content foundation models used as features (QARM, OmniSearchSage).

**The two reports are complementary.** Report A supplies the causal chain (infra → long sequences → scaling laws → generative models), production evidence, and epistemic hygiene. Report B supplies mechanism-level explanations, the multi-interest retrieval lineage, cold-start and hallucination failure modes, interaction-enhanced two-towers, and the quantization ladder. Report B has no OneRec, no scaling-law thread, no ANN/embedding-system infrastructure, no case studies, and weak provenance.

**Seven synergies emerge only from reading both** (Part II §12):
1. Consistency is the unifying design principle of the era — across funnel stages, sequence-search stages, and index stages. Generative retrieval is the limiting case.
2. Sample-selection bias and ranking inconsistency are one disease with a data-side cure (full-space sampling), a model-side cure (ECM), and a supervision-side cure (distillation); all three need candidate logging that neither report names.
3. Semantic IDs are becoming a universal primitive (retrieval, ranking generalization, cold-start, long-sequence routing), which makes tokenizer quality and stability a platform concern.
4. There are three ways to ground generation; evidence favors the generate-embedding-then-ANN hybrid for anyone with existing ANN infrastructure.
5. Embedding collapse and interest collapse are the same lesson: capacity without a coordination mechanism is wasted.
6. Report A explains *why to invest*; Report B supplies the mechanistic *why it works* arguments needed to justify each rung.
7. The serving-cost picture is only complete when A's MFU/OPEX/M-FALCON numbers are combined with B's quantization ladder.

**Biggest gaps across both** (Part III): graph/I2I retrieval and multi-source ensembling; search-specific retrieval (query towers, hybrid lexical+dense, filtered ANN); cross-surface retrieval; the 2025–26 semantic-ID tokenizer literature (drift, collisions, expressiveness limits, GR+dense hybrids); differentiable cascade training; retrieval evaluation methodology; candidate-logging infrastructure. Pinterest's own 2025 multi-embedding retrieval paper is cited by neither.

**Reliability.** Report A is primary-sourced with explicit caveats. Report B recycles the same six or seven survey citations on every paragraph; one method it describes (SetMIR) could not be verified, one (UxSID) is real but is a ranking paper, and two attributions are wrong (Part V).

---

# PART I — THE UNIFIED LANDSCAPE

## 1. Why the cascade exists

Industrial recommenders score billions of items for hundreds of millions of users; scoring every user–item pair with a heavy model is physically intractable. The universal answer is a multi-stage cascade: **retrieval** (thousands of candidates from the full corpus under strict latency), **pre-ranking / L1** (hundreds), **ranking / L2** (tens), **re-ranking**. [B]

The retrieval and L1 stages have historically been dominated by the **two-tower (dual-encoder) model**: independent user and item towers produce embeddings in a shared space, item embeddings are precomputed, and serving is an approximate-nearest-neighbor (ANN) query by inner product or cosine. The decoupling makes serving cheap but creates a **semantic gap** — no early, fine-grained interaction between user and item features, which are the strongest CTR signals. [B]

Report B also notes the persistent academia/industry divergence: academic work optimizes methodological novelty, industrial work optimizes profit, hardware utilization, data throughput, and millisecond latency. The innovations below are the points where the two converged.

## 2. Generative retrieval

### 2.1 The TIGER recipe (Google DeepMind, NeurIPS 2023, arXiv 2305.05065) [A][B]
- **Semantic IDs (SIDs):** a Residual-Quantized VAE (RQ-VAE) compresses continuous content embeddings (Sentence-T5 in the paper) into a short hierarchical tuple of codewords. Early levels capture coarse category, later levels fine distinctions.
- **Model:** a T5-style encoder-decoder consumes the user's history as a sequence of SIDs and autoregressively generates the SID of the next item.
- **Decoding:** beam search constrained by a prefix trie of valid item SIDs.
- **Consequences:** the item embedding table no longer grows linearly with corpus size; there is no separate ANN index to build and serve; cold/unseen items generalize through shared token prefixes; decoding temperature gives explicit control over diversity.

### 2.2 Identifier taxonomy [B]

| Identifier type | Mechanism | Advantage | Limitation |
|---|---|---|---|
| Atomic IDs | Random/sequential integers | Compact, simple | No semantics; no generalization to unseen items |
| Textual IDs (TID) | Titles, descriptions, generated summaries | Uses pre-trained LLM knowledge directly | Token overlap, synonym ambiguity, hallucination, long prompts |
| Semantic IDs (RQ-VAE etc.) | Hierarchical quantization of content embeddings | Embeds semantic + collaborative structure; replaces ANN | Needs periodic re-tokenization; cold-start drops; collisions |

### 2.3 HSTU — Hierarchical Sequential Transduction Units (Meta, ICML 2024, arXiv 2402.17152) [A][B]
- **Why not standard attention:** softmax normalization is ill-suited to non-stationary streaming vocabularies (the denominator is sensitive to distribution shift) and cannot express the *absolute intensity* of a preference (dwell, depth). HSTU uses **pointwise aggregated attention** with element-wise products, functioning as a gating mechanism akin to MoE, and maps heterogeneous categorical/numerical/text features into a single time-series format. [B]
- **Stochastic Length (SL) sampling:** user histories are highly redundant, so training on stochastically sampled sub-sequences cuts cost without hurting quality. [B] (See Part V on the complexity formula B gives.)
- **Kernels:** grouped-GEMM restructuring; 5.3×–15.2× faster than FlashAttention2-based Transformers at sequence length 8,192. [B]
- **Production result:** 1.5T-parameter deployment, +12.4% online A/B, up to +65.8% offline NDCG; power-law scaling in compute. [A]
- **Serving — M-FALCON:** micro-batched attention leveraging cacheable operations amortizes the attention cost across thousands of ranking candidates, enabling ~285× more complex models within the same inference budget at 1.50–2.99× higher QPS than DLRMs; the repo frames overall train+inference acceleration at 10×–1000×. [A][B]
- **Sequence-length scaling:** jagged-tensor context parallelism sharded across GPUs (arXiv 2508.04711, RecSys 2025), because sequence-length scaling is activation-heavy. [A]

### 2.4 Production lineage [A]
- **Kuaishou OneRec (arXiv 2506.13695):** encoder–decoder + sparse MoE + Iterative Preference Alignment (DPO) + session-wise list generation; explicitly replaces the retrieval → L1 → L2 cascade. Serves 25% of total QPS; +0.54% app stay time (main app), +1.24% (Kuaishou Lite); Model FLOPs Utilization rose from ~11% (fragmented cascade) to 23.7% training / 28.8% inference (5.2× / 2.6× over the prior ranking model); OPEX ~10.6% of the traditional pipeline.
- **OneRec-V2 (arXiv 2508.20900):** "Lazy Decoder-Only" architecture, 94% compute reduction (V1's encoder had consumed 97.66% of compute), scaled to 8B parameters; +0.467% / +0.741% app stay time, +0.069% 7-day retention; FP8 inference cut latency ~49% and nearly doubled throughput.
- **Google PLUM (WWW 2026, arXiv 2510.07784):** adapts a pre-trained LLM via SID tokenization + continued pre-training (CPT) + task-specific fine-tuning; beats a heavily optimized large-embedding-table production model at YouTube scale; ablations show CPT and LLM initialization both materially improve Recall@10; includes a retrieval scaling study. A 2026 Gemini-based YouTube generative retriever runs on TPU v6e over a 100M–1B item corpus.
- **Pinterest PinRec (arXiv 2504.10507):** outcome-conditioned, multi-token generation; served on NVIDIA L40S with CUDA graphs and KV caching; the generated representation is retrieved through a FAISS IVF-HNSW index — a hybrid of generative embedding generation and classic ANN.
- **LinkedIn causal-LM feed retrieval (arXiv 2510.14223):** global-batch in-batch negatives plus per-member hard-negative mining.

### 2.5 Semantic-ID construction and multimodal features [A]
- **Tokenizers:** RQ-VAE (TIGER); LETTER (collaborative signal added); Kuaishou RQ-Kmeans (collaborative signal + codebook-utilization maximization); RVQ/OPQ variants. SID collision handling is an active area — QARM-V2's Res-KmeansFSQ cut collision rate from 77.92% to 32.39%.
- **QARM / QARM-V2 (Kuaishou, arXiv 2411.11739):** multimodal-LLM features made *trainable* SIDs rather than static cached vectors; QARM-V2 reports +4.873% ad revenue and +5.612% shopping GMV online.
- **OmniSearchSage (Pinterest, WWW 2024, arXiv 2404.16260):** unified query/pin/product embeddings enriched with GenAI captions, board titles, engaged queries; >8% relevance, >7% engagement, >5% ads-CTR gains; 300k requests/sec at 3 ms median / 20 ms p90.
- **Google "Better Generalization with Semantic IDs" (RecSys 2024):** SIDs as ranking features improve generalization — SIDs are useful before any generative retrieval is deployed.

### 2.6 Failure modes of generative retrieval [B]
- **Cold-start collapse.** New items and new users trigger generation of high-probability, previously seen ID patterns; accuracy on novel items falls to near zero, starving new content of the exposure needed to gather feedback. Severity depends on identifier design: textual IDs help item cold-start but hurt warm-start and user cold-start through semantic instability. Mitigation: **next-user retrieval** (lookalike-style — find users similar to a seed user and recommend the cold item to them). (A reproducibility study: arXiv 2603.29845.)
- **Hallucination.** The model can emit token sequences that map to no valid item. Report B cites an empirical ceiling: confidence-based abstention removes at most ~1.65 percentage points of hallucinations because ungrounded recommenders are equally confident in their surviving errors. Countermeasures: Context-aware Term Generation (CTG) during training to enforce distinctiveness among similar items, and bi-step constrained decoding through a verified inventory trie at inference.

### 2.7 Status assessment [A]
Generative retrieval "replacing two-tower at scale" is true in production only at Kuaishou. Everywhere else it is being added as an additional nominator/source alongside bias-corrected two-tower EBR, which remains the workhorse for most retrieval sources.

## 3. Long user-behavior sequences

**Motivation.** More history reliably improves CTR/conversion. Short windows are vulnerable to **session hopping** — interests are stable within a session but shift sharply across sessions — so the industry moved from hundreds of recent actions to lifelong histories exceeding 10^6 events. [B]

**The two-stage search paradigm.** Target attention (DIN-style) over 10^4–10^6 items is infeasible, so SIM introduced a cascade *within* sequence modeling: a cheap **General Search Unit (GSU)** filters the long history to a candidate-relevant subsequence; an **Exact Search Unit (ESU)** applies full multi-head target attention to the subset. [B]

| Model | Length | Search / compression mechanism | Defining contribution |
|---|---|---|---|
| SIM (Alibaba) | ~5×10^4 | Category hard-filtering GSU | Pioneered the GSU/ESU cascade; ~54k-event histories in display ads with large RPM lifts [B] |
| ETA | ~10^5 | Locality-sensitive hashing + Hamming distance | End-to-end GSU via bit-wise ops instead of category tags [A][B] |
| SDIM ("Sampling Is All You Need," arXiv 2205.10249) | ~10^5 | SimHash random projections; aggregate behaviors that collide with the target | Hash-collision probability ≈ softmax attention weight; parity with full target attention at 11.4× speed, ~1 ms added latency at length 2,000 [A][B] |
| TWIN (Kuaishou, KDD 2023, arXiv 2302.02352) | ~10^5 | Consistency-Preserved GSU using the *same* target-attention metric as the ESU | Removes the GSU/ESU objective mismatch that limited ETA and SDIM [A][B] |
| TWIN-V2 (Kuaishou, CIKM 2024, arXiv 2407.16357) | >10^6 | Offline recursive K-means over collaborative item embeddings → cluster tokens (mean-pooled); online cluster-aware target attention with weights scaled by cluster size | Lifelong sequences; offline AUC 0.7975 vs TWIN 0.7962 on Kuaishou data, with consistency the decisive factor [A][B] |
| UxSID (arXiv 2605.09040, May 2026) | >10^6 | Item-Agnostic Interest Compression (orthogonality-constrained per-token FFNs → learnable interest anchors) + Hierarchical Semantic Probing gated by target SID | "Third path": semantic-group shared interest memory routed by SIDs; constant-time inference; +0.337% ad revenue in a large-scale A/B [B][S] — **note: this is an ads-CTR (ranking) paper, not retrieval** |
| HSTU + context parallelism (Meta, arXiv 2508.04711) | 8,192+ tokens | Jagged-tensor context parallelism across GPUs | Sequence-length scaling for generative recommenders [A] |
| LONGER (ByteDance, 2025) | ~10^4 | GPU-efficient transformer for long sequences | Ranking-side; listed for completeness [S] |

**Cross-report reading.** Report A frames this lineage as the middle rung of the causal chain (infra → long sequences → scaling laws → generative models). Report B supplies the mechanism that makes cheap approximations legitimate (collision probability ≈ attention weight) and the failure mode that consistency fixes (separately trained GSU/ESU hand off suboptimal candidates).

## 4. Embedding-based retrieval: two-tower refinement and multi-interest

### 4.1 Training objectives and negatives [A]
- **Sampling-bias-corrected two-tower (Yi et al., Google, RecSys 2019):** a streaming frequency-estimation algorithm corrects the bias of in-batch negatives (popular items are over-sampled as negatives). +0.37% engagement in YouTube A/B; powers YouTube Neural Deep Retrieval over tens of millions of videos.
- **Mixed Negative Sampling (MNS, Google Play):** blend in-batch negatives with uniformly sampled corpus negatives to reduce selection bias.
- **Cross-Batch Negative Sampling (CBNS):** reuse encoded items across mini-batches to break the batch-size bound on the number of negatives.
- **logQ refinements:** Yandex, "Correcting the LogQ Correction" (arXiv 2507.09331).
- **Hard negatives:** per-member hard-negative mining alongside global in-batch negatives (LinkedIn feed retrieval).

### 4.2 Injecting interaction into the two-tower [B]
- **IntTower (CIKM 2022):** a Light-SE module scores feature importance inside each tower; a Fine-grained-and-Early (FE) block captures explicit cross-tower signals before the final inner product; Contrastive Interaction Regularization (CIR) forces the two towers' representations to share latent collaborative structure. Interaction without breaking the offline-item-embedding serving model.
- **InteractRank (Pinterest search pre-ranking, WWW 2025):** augments the two-tower dot product with **precomputed cross-interaction features** derived from historical query–item engagement, materially improving L1 quality at negligible serving cost.

### 4.3 Multi-interest retrieval [B, with A and S additions]
**The problem.** A single user vector averages disjoint intents (tools, classical music, baby clothes) toward the centroid of unrelated clusters and retrieves generic near-misses rather than specific matches. [B]

**First-generation methods.**
- **MIND:** capsule-network dynamic routing clusters behaviors into K interest capsules.
- **ComiRec-DR:** improved routing plus a controllable aggregation factor to trade accuracy against diversity.
- **PIMI:** adds periodicity and interactivity of interests over time.
- Serving pattern: K user embeddings → K independent ANN queries → pooled candidate set.
- **PinnerFormer (Pinterest)** and Report A's multi-embedding retrieval line belong to the same family. [A]

**Two structural failures.** [B]
- **Interest collapse:** assigning each target to its argmax interest vector during training means colliding targets update one vector while the other K−1 get no gradient; the model converges to one or two functional interests.
- **Static dispatch:** issuing all K ANN queries every request burns a fixed retrieval budget even when the user has two live interests, flooding the pool with redundant or low-quality candidates.

**SetMIR (as described in Report B — see Part V; not independently verified).** Reframes multi-interest generation as set prediction over K learnable queries; a Hungarian matcher (borrowed from DETR-style object detection) assigns engaged targets to queries one-to-one, with an explicit "absence" penalty for unmatched queries; at serving time a presence-gating head plus query-level non-maximum suppression activates only the live queries (adaptive retrieval).

**IMSR — Incremental Multi-interest Sequential Recommendation.** [B] Continual learning for shifting interests: an Existing-Interests Retainer (knowledge distillation against forgetting), a New-Interests Detector, and a Projection-based Interests Trimmer that decides when to spawn a new interest vector from streaming behavior.

**Pinterest multi-embedding retrieval framework (arXiv 2506.23060, 2025).** [S] Combines implicit (learned) and explicit user interests in a multi-embedding retrieval framework; deployed at Pinterest with large online engagement gains. Neither report cites it.

**Embedding collapse (arXiv 2310.04400, ICML 2024).** [A] Naively widening embeddings in DLRMs yields low-rank, collapsed representations; multi-embedding designs recover the lost dimensionality. (Report A attributes this to Meta; the paper is academic — see Part V.)

**kNN-Embed (Twitter, arXiv 2205.06205).** [S] Represents a user as a smoothed mixture over learned item clusters and queries each component in proportion to its weight; a turnkey diversity improvement on top of any existing ANN system, no retraining required.

## 5. Tree-based and learnable indices [A]
- **TDM / JTM (Alibaba):** tree indices with beam search give logarithmic complexity and allow arbitrary (non-dot-product) scorers at retrieval. "Learning Optimal Tree Models under Beam Search" (Zhuo et al., 2020) fixed the training/testing discrepancy introduced by beam search.
- **Deep Retrieval (ByteDance, arXiv 2007.07203):** replaces the tree with a learnable D×K discrete latent structure trained end-to-end with EM-style path assignment; near-brute-force accuracy in sub-linear time (~4× faster than brute force on Amazon Books).
- **Assessment:** influential, but superseded in mindshare by generative retrieval, which generalizes "learn a discrete structure and beam-search over it" while adding content semantics and compute scaling. Hybrids persist (MISS multimodal tree indexing, CIKM 2025).

## 6. Pre-ranking (L1)

### 6.1 Computation-aware design
- **Pre-2020 progression:** LR → vector-product two-tower → COLD. Quality plateaued because architecture was restricted to save compute. [A]
- **COLD (Alibaba, arXiv 2007.16122):** jointly optimize model *and* computing cost. Squeeze-and-excitation feature selection, column-based computation, FP16 + CUDA MPS inference (FP16 alone ~+21% usable QPS; FP16+MPS roughly 2× vs FP32). Deployed across Alibaba display-advertising pre-ranking since 2019. [A][B]
- **FSCD (Alibaba, 2021):** learnable feature selection via variational dropout to induce input sparsity in a full-ranker-like network. [B]
- **IntTower / InteractRank:** the interaction-injection alternative (§4.2). [B]

### 6.2 Ranking consistency (RC) — the real step change
**Failure mode.** L1 and L2 are trained independently with very different capacity, so their score distributions diverge. A **Matthew effect** results: items L2 would rank highly get low L1 scores and are filtered before L2 ever sees them. [B]

**Methods.**
- **RankFlow (SIGIR 2022):** joint optimization of cascade stages as flows. [A]
- **Ranking distillation / "On Ranking Consistency of Pre-ranking Stage" (arXiv 2205.01289):** distill L2 logits into L1 on the *pre-ranking candidate set* via MSE on logits. [A]
- **COPR (CIKM 2023):** consistency-oriented pre-ranking. [A]
- **JRC — Jointly Ranked Calibration (2022):** ranking consistency with calibration. [A]
- **CIT — Contrastive Information Transfer:** treats pre-ranking as representation distillation; the L2 ranker's representation is the positive, and a contrastive loss maximizes a mutual-information lower bound to align L1's latent space geometrically with L2's. [B]
- **RankTower (arXiv 2407.12385):** two-tower pre-ranker with full-stage sampling (impression + candidate + random) plus distillation. [A]
- **SDCL (AAAI 2025):** joint framework for SSB and RC — a Multi-Task Distillation module continuously transfers knowledge from a jointly trained heavy ranker, paired with adaptive negative sampling, so L1's top-K maximally overlaps the top-K the full ranker would have produced. [A][B]

### 6.3 Sample selection bias (SSB)
**Failure mode.** L1 is trained on ranker output (impressions and clicks plus uniform negatives) but serves the far wider, noisier retrieval output. Report B adds the optimization mechanism: the loss is dominated by "hard" samples resembling clicked items while "easy" irrelevant retrieval candidates are under-utilized — gradient conflict. [A][B]

**Cures.**
- **Full-space / full-stage sampling (data-side):** train on impressions + pre-ranking candidates + random corpus samples, treating unexposed items as negatives (with acknowledged cost and label-noise caveats). [A]
- **ECM — Entire-chain Cross-domain Model (arXiv 2310.08039; model-side):** a cross-domain multi-tower network with L0-regularized sub-network routing estimates every stage's probability — exposure-through rate given retrieval, CTR given exposure, joint post-exposure metrics — and evaluates the loss over the matching domain rather than the exposure domain, removing the distribution shift. [B]
- **Meta ads (arXiv 2502.06834):** cross-stage co-training and on-the-fly L2→L1 distillation on "consideration" traffic; without it, pre-ranking models over-predict on that traffic. [A]

### 6.4 Does a separate L1 survive? [A]
OneRec's claim is that an end-to-end generative model replaces the cascade, with MFU rising from ~11% to 28.8% inference / 23.7% training and OPEX at ~10.6% of the legacy pipeline. This is real in Kuaishou production but not industry consensus. Assessment: L1 persists at most companies through 2026 as a cost-control mechanism, but the justification for a *separately trained* L1 is eroding; the field is moving toward consistency-constrained or jointly optimized funnels, and toward collapse for those with short-video-scale GPU budgets.

## 7. Data investments [A]
- **Full-funnel data:** impression/exposure vs click labels across stages; full-space sampling to fix SSB.
- **Ultra-long histories:** tens of thousands of events (TWIN-V2 lifelong sequences; HSTU 8,192+ tokens).
- **Real-time / streaming training:** Monolith and Kuaishou online learning capture fresh interests within minutes and correct non-stationarity (Monolith applies log-odds correction after negative sampling).
- **Label engineering:** watch time, dwell, multi-task labels, OneRec's Duration-Aware Reward Shaping, unified pre-ranking labels.
- **Semantic-ID pipelines:** RQ-VAE / RQ-Kmeans / RVQ / OPQ tokenizers as a distinct data-engineering discipline; collision handling.
- **Multimodal content features:** QARM (trainable MLLM features), OmniSearchSage (GenAI captions, board titles, engaged queries), Netflix's learnable item-ID + metadata embeddings for cold-start.

## 8. Infrastructure [A][B]

### 8.1 Embedding and training systems
- **Monolith (ByteDance, RecSys 2022 ORSUM, arXiv 2209.07663):** Cuckoo-hash collisionless embedding table with expirable embeddings and frequency filtering; production real-time training/serving; powers TikTok/BytePlus Recommend. Collisions matter because distinct items overwrite each other's representations under the hashing trick. [A][B]
- **Neo / ZionEX (Meta, arXiv 2104.05158, ISCA 2022):** on 128 A100s across 16 ZionEX nodes, up to 1.7M queries/sec training DLRMs with 12T parameters — a 40× speedup — using 4D parallelism (table/row/column/data) over a dedicated RoCE network. [A]
- **TorchRec (RecSys 2022):** sharding strategies + FBGEMM kernels; 2D sparse parallelism to thousands of GPUs; embedding offloading (RecSys 2024) scaled to 104 TB with ~26% throughput regression. [A]

### 8.2 Accelerators [A]
- **Meta MTIA v1 (2023):** inference; 102.4 TOPS INT8 / 51.2 TFLOPS FP16; up to 128 GB LPDDR5; TSMC 7nm. **MTIA v2 (2024):** 354 TOPS INT8 dense (~708 with sparsity); 256 MB on-chip SRAM at 2.7 TB/s; TSMC 5nm; in production for ranking/recommendation.
- **Google TPU v4 SparseCore:** dedicated embedding hardware. DLRMs are ~25% of Google's ML workload; production ads models serve >100k requests/sec over billions of weights trained on >1T examples.

### 8.3 ANN infrastructure [A]
- FAISS / HNSW / ScaNN / DiskANN plus GPU ANN.
- **ScaNN anisotropic vector quantization (arXiv 1908.10396):** aligns the quantization objective to MIPS; ~2× QPS at a given accuracy versus the next-fastest library on ann-benchmarks.
- **SOAR (arXiv 2404.00774):** orthogonality-amplified spilling; a further ~2–3× speedup at ~6% index-size overhead.
- **NVIDIA cuVS / CAGRA:** GPU graph ANN; roughly 7–15× search throughput over CPU HNSW at 90–99% recall (indicative, vendor/Milvus benchmark); integrated into FAISS, Milvus, OpenSearch.

### 8.4 Efficient generative inference and quantization [A][B]
- **M-FALCON** (§2.3) and **OneRec MFU** figures (§2.4, §6.4).
- **Quantization ladder [B]:** FP32/FP16 → FP8-dynamic or INT8-dynamic (fractional quality loss, ~2× throughput) → INT4-AWQ / INT4-GPTQ (fits large generative models into accelerator SRAM, avoiding DRAM fetches). OneRec-V2 FP8 inference: ~49% latency reduction, ~2× throughput. [A]

### 8.5 Summary table (adapted from Report B, attribution corrected)

| Optimization | Mechanism | Metric improved |
|---|---|---|
| Monolith collisionless embeddings | Dynamic memory allocation per ID; expiry; frequency filter | Removes hash-collision interference; enables online training fidelity |
| FP8 / INT8 / INT4 quantization | Compress activations and weights | VRAM footprint; ~2× inference throughput |
| Stochastic Length (HSTU, training) | Sample subsets of redundant sequences | Training cost at long sequence lengths (see Part V on the exact complexity claim) |
| Rowwise AdamW (HSTU, training) | Row-wise optimizer state for embeddings | Optimizer memory during training (Report B lists this under M-FALCON; it is a training detail) |
| M-FALCON (inference) | Micro-batched attention over cacheable ops | Amortizes attention across thousands of candidates; ~285× model complexity at equal budget |
| Mixed / cross-batch negative sampling | Blend in-batch with uniform/hard negatives | Corrects implicit-feedback selection bias; better gradients |
| Context parallelism (HSTU) | Jagged-tensor sharding of sequence across GPUs | Activation memory at long sequence lengths |

## 9. Scaling laws — the intellectual through-line [A]
- **Wukong (Meta, ICML 2024, arXiv 2403.02545), HSTU, OneRec, and Netflix's foundation model** independently show power-law quality-vs-compute for recommendation — the property DLRMs had conspicuously lacked and the one that justifies capital investment.
- **Caveats:** HSTU's headline numbers are Meta-internal and not independently reproduced; public-dataset studies (e.g., UNGER, arXiv 2502.06269) show HSTU stagnating past ~8 layers on some datasets. Scaling laws are architecture- and data-dependent (the embedding-collapse lesson: if curves flatten early, the architecture — not the data — is the likely bottleneck).

## 10. Company snapshots [A, with S additions]
- **Kuaishou:** most aggressive adopter — OneRec / OneRec-V2 (cascade replacement), OneRec-Think (in-text reasoning, arXiv 2510.11639 [S]), QARM / QARM-V2, KuaiFormer (transformer multi-interest retrieval), TWIN / TWIN-V2.
- **Meta:** HSTU / Generative Recommenders, M-FALCON, Wukong, multi-embedding retrieval, Neo/ZionEX, TorchRec, MTIA, ads cross-stage L1 work (2502.06834), and work unifying generative and dense retrieval (LIGER, arXiv 2411.18814 [S]).
- **Google / YouTube:** sampling-bias-corrected two-tower → TIGER → SIDs for ranking generalization → PLUM → Gemini-based generative retrieval on TPU v6e; ScaNN / SOAR; TPU SparseCore.
- **Netflix:** unified transformer foundation model (March 2025) consolidating hundreds of specialized models; hundreds of billions of interactions from 300M+ users; scaled from millions to billions of parameters over ~2.5 years; embeddings feed home and search surfaces; multi-task "Hydra" head.
- **LinkedIn:** 360Brew (~150B-parameter decoder-only model on Mixtral 8x22B; 30+ ranking/recommendation tasks via a text interface with zero-shot generalization — paper later withdrawn over licensing; treat production claims cautiously), LiRank, causal-LM feed retrieval.
- **Pinterest (assembled across both reports plus verification):** PinnerFormer (multi-interest user representation) [A]; OmniSearchSage (search embeddings) [A]; PinRec (generative retrieval hybrid) [A]; InteractRank (search pre-ranking with cross-interaction features) [B]; multi-embedding retrieval framework combining implicit and explicit interests (arXiv 2506.23060) [S]. Neither report assembles this picture.
- **ByteDance:** Deep Retrieval, Monolith, LONGER [S].
- **Alibaba:** SIM / ETA lineage, COLD, FSCD, TDM/JTM, CIT, ECM lineage.

---

# PART II — SYNTHESIS

## 11. What each report contributes

| Dimension | Report A | Report B |
|---|---|---|
| Frame | Causal chain (infra → sequences → scaling laws → generative) and step-function thesis | Method-by-method taxonomy with mechanism explanations |
| Evidence base | Primary papers, production A/B numbers, arXiv IDs | Surveys (2407.21022, 2510.27157, 2509.06002 etc.) cited as blocks on every paragraph |
| Unique coverage | OneRec / V2, PLUM, PinRec, Netflix FM, 360Brew, Wukong and scaling laws, TDM/JTM/Deep Retrieval, ANN infra (ScaNN/SOAR/CAGRA), trillion-parameter embedding systems, accelerators, data investments, timeline, recommendations, caveats | HSTU internals (pointwise attention rationale, stochastic length, kernel speedups), identifier taxonomy, cold-start collapse, hallucination/constrained decoding, controllable diversity, multi-interest lineage (MIND → ComiRec → PIMI → SetMIR → IMSR), IntTower / InteractRank, FSCD, ECM, CIT, quantization ladder, UxSID |
| Blind spots | Multi-interest in one sentence; cold-start and hallucination only as open problems; no interaction-enhanced two-tower | No OneRec; no scaling laws; no ANN or embedding-system infra; no case studies; no timeline; no assessment of hype vs reality; scope drift into ranking-side papers |
| Best use | Strategy, sequencing of investments, "what is real in production" | Justifying *why* each method works; design detail for implementers |

## 12. Seven synergies

### 12.1 Consistency is the unifying design principle
Report A calls L1↔L2 consistency the pre-ranking step change, and separately notes TWIN's consistency-preserved GSU and the training/testing discrepancy fix for tree indices under beam search. Report B independently supplies the failure modes: the Matthew effect (good items starved by a divergent L1), gradient conflict under SSB, and GSU/ESU objective misalignment. Read together, every cheap-stage breakthrough of 2021–25 came from one move — **make the cheap stage optimize the metric of the expensive stage it feeds** — applied to funnel stages, sequence-search stages, and index stages alike. Generative retrieval is the limiting case: collapse the cascade and there is nothing left to be inconsistent. This reframes A's open question: **a separate L1 survives exactly as long as enforcing consistency is cheaper than collapsing the stage.** OneRec is the case where it was not.

### 12.2 SSB and ranking consistency are one disease
Report B separates SSB (train on ranker output, serve on retrieval output) from RC (score divergence). Report A separates full-space sampling from distillation. They are the same train/serve distribution mismatch across the funnel, with three cures that differ only in where the correction is applied:
- **Data-side:** full-space / full-stage sampling (A, RankTower).
- **Model-side:** ECM — explicitly model P(exposure | retrieved) and P(click | exposure) (B).
- **Supervision-side:** L2→L1 logit or representation distillation on the L1 candidate space (A: 2205.01289, Meta ads; B: CIT).
All three require **logging what retrieval and L1 saw but never showed**. Neither report lists candidate logging as an investment; it gates Report A's recommendation #2 and is a data-infrastructure project, not a modeling one.

### 12.3 Semantic IDs are becoming a platform primitive
Report A shows SIDs eliminating the ANN index (TIGER), improving ranking generalization (Google RecSys 2024), being trained end-to-end from multimodal models (QARM), and suffering collisions that need engineering (Res-KmeansFSQ). Report B shows that identifier design determines cold-start behavior and that constrained decoding is needed to ground generation. New in 2026, UxSID uses SIDs as **routers** so compressed interest memories are shared among items with the same semantic ID, avoiding per-candidate search. SIDs now touch retrieval, ranking generalization, cold-start, and long-sequence compression. **Tokenizer quality and stability is therefore a shared dependency across the stack**, and the 2025–26 tokenizer literature (Part III §13c) is the most consequential omission in both reports.

### 12.4 Three ways to ground generation
- **Trie-constrained decoding** over valid SIDs (TIGER; both reports).
- **Distinctiveness training** (CTG) plus bi-step constrained decoding (B).
- **Generate an embedding, then ANN** (PinRec's FAISS IVF-HNSW hybrid; A) — formalized in Meta's LIGER (unifying generative and dense retrieval, arXiv 2411.18814) and Baidu's COBRA (cascaded sparse-dense representations, arXiv 2503.02453) [S].
Report B's finding that confidence-based abstention removes at most ~1.65pp of hallucinations argues that the dense-fallback hybrid is the lower-risk production path for anyone with existing ANN infrastructure — which is exactly Report A's recommendation #3 (pilot GR as an additional nominator).

### 12.5 Two kinds of collapse, one lesson
Report A's Wukong / embedding-collapse lesson: if quality-vs-compute does not follow a power law, the architecture is the bottleneck — added width yields low-rank embeddings. Report B's interest-collapse lesson: argmax routing starves K−1 of K interest vectors. Same principle at different granularities: **capacity is wasted without a mechanism that forces it to be used.** Two corollaries: (i) any multi-embedding retrieval needs a coordination mechanism (Hungarian matching, presence gating, contrastive diversity regularization); (ii) a beam-search generative retriever with temperature control is itself a multi-interest retriever, so "K ANN queries vs one beam" is a design choice to A/B on the same corpus rather than two separate research areas.

### 12.6 A's "why invest" plus B's "why it works"
Report A's causal chain asserts that long sequences pay off. Report B supplies the mechanistic justifications one would cite in a funding document: session hopping motivates lifelong history; collision probability approximating softmax weights justifies SDIM-style cheap search; softmax's sensitivity to non-stationary vocabularies justifies HSTU's pointwise attention; sequence redundancy justifies stochastic-length training. Together they turn A's recommendations #1 and #4 from assertions into arguments.

### 12.7 The serving-cost picture requires both
Report A has MFU (11% → 28.8%), OPEX (10.6%), M-FALCON's amortization, and OneRec-V2's FP8 latency cut. Report B has the quantization ladder (FP8/INT8-dynamic → INT4-AWQ/GPTQ into SRAM). Neither alone lets you build a cost model for generative inference; together they roughly do:

> cost per request ≈ parameters × generated tokens × candidates ÷ (MFU × quantization throughput gain × micro-batching amortization)

This is the number that decides whether generative retrieval is an additional nominator or a cascade replacement at a given company.

---

# PART III — WHAT IS MISSING FROM BOTH

## 13. Gaps

### 13a. Retrieval families and the real production problem
- **Graph-based and item-to-item retrieval** (PinSage / Pixie lineage, GNN nominators, Swing-style co-occurrence, item-CF). Still the bulk of nominator volume at most companies; absent from both reports.
- **Multi-source ensembling:** quota allocation, dedup and merging, learned blending across dozens of nominators. Both reports write as if retrieval were a single model. In practice "retrieval quality" is an ensemble property.
- **Search-specific retrieval:** query-tower design, hybrid lexical + dense, late interaction (ColBERT-style), learned sparse retrieval (SPLADE-style), relevance-vs-engagement objectives, multilingual queries, **filtered ANN** with attribute constraints. Both reports are feed-centric; OmniSearchSage is the only search entry.
- **Cross-surface / multi-scenario retrieval:** one retrieval model or foundation model serving several surfaces (home, search, notifications, related items). Netflix's consolidation and 360Brew's 30 tasks are the nearest examples but are ranking-centric; the retrieval-specific design (shared item space, surface-conditioned user tower, per-surface calibration) is not treated.
- **Exposure / popularity bias in retrieval** (IPS-style correction), **exploration nominators**, and **creator-side distribution objectives**. Report B's cold-start collapse is the only adjacent discussion.
- **Real-time session retrieval** and serving-time user-embedding refresh. Report A covers online *training*; neither covers online *inference-side* freshness.
- **Pinterest's multi-embedding retrieval framework** (arXiv 2506.23060) — cited by neither.

### 13b. Cascade and L1
- **Differentiable / learned cascade training** (ARF-style adaptive ranking frameworks, learned top-K per stage) and **adaptive per-request candidate budgets**. RankFlow is the only joint-cascade entry in either report.
- **Multi-objective and ads-specific L1** (bid / eCPM-aware pre-ranking), and **calibration** beyond JRC.
- **Generative models as the pre-ranker** — MTGR (Meituan, CIKM 2025) and OneRec's ranking role are the concrete form "cascade collapse" takes; neither report treats GR-as-L1 as a distinct option.

### 13c. The 2025–26 semantic-ID tokenizer ecosystem (most consequential omission, given §12.3)
- **GR + dense hybrids:** LIGER (Meta, arXiv 2411.18814), COBRA (Baidu, arXiv 2503.02453).
- **Practitioner guidance:** "Generative Recommendation with Semantic IDs: A Practitioner's Handbook" (CIKM 2025, arXiv 2507.22224).
- **Tokenizer robustness:** drift-aware continual tokenization (arXiv 2603.29705); qualification-aware collision handling at industrial scale (arXiv 2603.00632); differentiable semantic IDs (SIGIR 2026, arXiv 2601.19711); end-to-end learnable item tokenization (ETEGRec, SIGIR 2025).
- **Theory:** expressiveness limits of autoregressive SID generation (arXiv 2605.06331).
- **Deployment reports:** Semantic IDs at Snapchat — use cases, challenges, design choices (arXiv 2026); a 2026 deployment report on SID-based generative retrieval building on PLUM (arXiv 2603.17540).
- **Lineage extension:** OneRec-Think (arXiv 2510.11639).

### 13d. Data and serving infrastructure
- **Candidate logging at retrieval / L1** — the prerequisite for every SSB/RC cure (§12.2).
- **Item-side real-time indexing**, embedding-version skew between user and item towers, index-rebuild cadence versus SID re-tokenization cadence.
- **Filtered ANN** and vector-database tradeoffs; feature stores and freshness SLAs.

### 13e. Evaluation and economics
- **Retrieval evaluation methodology:** recall@K versus downstream acceptance by L2, counterfactual / off-policy evaluation, the offline→online transfer gap. Report A lists it as an open problem; neither proposes a method.
- **Unit economics:** cost per incremental engagement for GPU retrieval versus CPU ANN — the number that actually decides Report A's recommendation #4.
- **Independent replication** of internally reported A/B lifts (A flags this; neither proposes how).

### 13f. Scope drift
Report B's long-sequence section (TWIN-V2, UxSID) and ByteDance's LONGER are CTR / ranking work, not retrieval or pre-ranking. If this synthesis feeds a retrieval strategy, keep that boundary explicit.

---

# PART IV — RECOMMENDATIONS

## 14. Report A's five, retained
1. **Build the infra rung you are missing before chasing generative models.** Without online/streaming training and dynamic (ideally collisionless) embedding tables, build those first (Monolith-style). Benchmark: refresh embeddings for fresh items within minutes; train on impression + candidate + random samples.
2. **For pre-ranking, adopt consistency + full-space sampling now.** Low-risk, high-return, validated at Alibaba / Tencent / Meta. Implement L2→L1 logit distillation on the L1 candidate set and add random/candidate negatives. Escalation threshold: if L1↔L2 rank correlation on consideration traffic is low, prioritize this over any new architecture.
3. **Pilot generative retrieval as an additional nominator, not a cascade replacement**, unless you operate at short-video scale with the GPU budget to attempt OneRec-style unification. Build the SID pipeline as reusable infrastructure — it pays off in cold-start and ranking generalization before any generative retrieval ships.
4. **Provision GPU inference and GPU/quantized ANN (cuVS/CAGRA or ScaNN/SOAR) before scaling sequence length or model FLOPs.** Sequence-length scaling needs context parallelism; generative serving needs micro-batching and usually FP8.
5. **Adopt scaling-law discipline.** Measure quality-vs-compute on your own data before committing capital. No power law → the architecture, not the data, is the likely bottleneck. Re-plan if curves flatten early.

## 15. Additions from the synthesis
6. **Fund candidate logging as a first-class project.** Log retrieval and L1 outputs (not just impressions) with stage tags; it is the shared prerequisite for full-space sampling, ECM-style modeling, and on-the-fly distillation (§12.2).
7. **Treat the SID tokenizer as a platform service with SLAs** — collision rate, drift between re-tokenizations, cold-item coverage, and downstream ranking-generalization lift — and track the 2025–26 robustness literature (§13c) before standardizing on RQ-VAE.
8. **Prefer the dense-fallback hybrid for the first GR nominator** (PinRec / LIGER / COBRA pattern) rather than pure trie-constrained generation; it reuses ANN infrastructure and sidesteps the hallucination ceiling (§12.4).
9. **Run the multi-interest A/B that neither report suggests:** K coordinated embeddings with adaptive dispatch versus one beam-search GR nominator with temperature-controlled diversity, on the same corpus, measured on downstream L2 acceptance rather than recall@K (§12.5).
10. **Write down the L1 exit criterion.** State explicitly the cost at which enforcing L1↔L2 consistency exceeds the cost of collapsing the stage (§12.1); revisit annually against GPU pricing and MFU achieved.

---

# PART V — CAVEATS AND FACTUAL FLAGS

## 16. Caveats carried from Report A
- **Hype vs reality.** Generative retrieval replacing two-tower at scale is true in production only at Kuaishou; elsewhere it is additive. HSTU's 1.5T-parameter, +12.4% result is Meta-internal and not independently reproduced; public-dataset HSTU results are far smaller-scale, and some studies (UNGER, arXiv 2502.06269) show stagnation past ~8 layers. Recommendation scaling laws are architecture- and data-dependent, not universal.
- **Third-party numbers.** GPU cluster counts, MTIA rack density, and CAGRA index-build speedups come from secondary sources; treat as indicative.
- **360Brew** is described in a pre-production paper later withdrawn from arXiv over a licensing issue; treat production claims cautiously. Public "LinkedIn algorithm" commentary about it is largely SEO/marketing.
- **Open problems (2026):** serving cost of generative models at scale; cold-start and corpus churn under SIDs; whether one foundation model should span retrieval + L1 + L2; evaluation beyond next-item accuracy (list/session quality, diversity, long-term value); independent replication of A/B lifts.

## 17. Factual flags raised in this synthesis

### Report B
- **SetMIR** — could not be located under that name in verification searches. Treat the Hungarian-matcher / presence-gating / NMS description as unverified until a primary source is found. The *problems* it addresses (interest collapse, static dispatch) are real and well documented.
- **UxSID** — real (arXiv 2605.09040, May 2026; ~0.337% ad-revenue lift), but it is an ads-CTR (ranking) paper, not a retrieval or pre-ranking method.
- **Stochastic Length complexity** — Report B's table states a reduction from O(N³d) to O(N²d). That does not match the author's recollection of HSTU §4 (which frames the saving in terms of a sub-linear effective sequence length). Verify against the primary before quoting.
- **Rowwise AdamW** — an HSTU *training* optimizer detail, listed by B under M-FALCON (an *inference* technique). Misattribution.
- **Hallucination "≤1.65pp" ceiling and "CTG"** — no traceable source in B's reference list. Verify before reuse.
- **Provenance generally** — B cites the same six or seven surveys as a block on nearly every paragraph, so most specific claims are at best second-hand. Numbers that match the primaries from memory: SIM ~54k events; SDIM 11.4× / ~1 ms at length 2,000; HSTU 5.3–15.2× vs FlashAttention2 at 8,192; TWIN-V2 to ~10^6.

### Report A
- **Embedding collapse (arXiv 2310.04400)** is, to the author's knowledge, an academic (Tsinghua) paper, not Meta's; Report A conflates it with Meta's separate multi-embedding line.
- **Reading-list IDs** — spot-check before citing; "Mixed / Cross-Batch Negative Sampling — arXiv 2110.15154" looks off (MNS is a WWW 2020 industry paper; CBNS is SIGIR 2021).
- **Self-reported lifts** — HSTU +12.4%, OneRec stay-time and retention, QARM-V2 revenue/GMV, OmniSearchSage gains are all first-party numbers. Report A flags this correctly; it bears repeating.

---

# PART VI — TIMELINE (2021–2026)

- **2021:** ZionEX/Neo (12T-parameter DLRM training); ETA long-sequence retrieval; ByteDance Deep Retrieval; COLD in wide Alibaba deployment; FSCD; CBNS (SIGIR).
- **2022:** SDIM; Monolith (real-time collisionless training); TorchRec; RankFlow (SIGIR); ranking-consistency distillation (2205.01289); CIT; IntTower (CIKM); JRC; kNN-Embed; ScaNN maturing.
- **2023:** TIGER (NeurIPS); TWIN (KDD); COPR (CIKM); ECM (2310.08039); MTIA v1; embedding-collapse / multi-embedding line begins.
- **2024:** HSTU + M-FALCON + first production scaling law (ICML); Wukong (ICML); TWIN-V2 (CIKM); SOAR; OmniSearchSage (WWW); QARM; RankTower; MTIA v2; Google "SIDs improve ranking generalization" (RecSys); LIGER (Meta GR+dense).
- **2025:** OneRec / OneRec-V2 (end-to-end generative in production); Netflix foundation model (March); LinkedIn 360Brew and causal-LM retrieval; PinRec; PLUM at YouTube; HSTU context parallelism (RecSys); SDCL (AAAI); InteractRank (WWW); Pinterest multi-embedding retrieval; COBRA; MTGR (CIKM); SID practitioner's handbook (CIKM); ETEGRec (SIGIR); OneRec-Think; LONGER; UNGER scaling critique.
- **2026:** PLUM (WWW); Gemini-based YouTube generative retrieval on TPU v6e over a 100M–1B corpus; UxSID (SID-routed ultra-long sequences); tokenizer-robustness wave (drift-aware continual tokenization, qualification-aware collisions, differentiable SIDs at SIGIR, expressiveness limits); Snapchat SID deployment report; cold-start reproducibility study (2603.29845); KDD 2026 scaling-bottleneck studies.

---

# PART VII — READING LIST

## Generative retrieval and scaling
- TIGER — arXiv 2305.05065 (NeurIPS 2023)
- HSTU / Generative Recommenders — arXiv 2402.17152 (ICML 2024); github.com/meta-recsys/generative-recommenders
- HSTU context parallelism — arXiv 2508.04711 (RecSys 2025)
- Wukong scaling law — arXiv 2403.02545 (ICML 2024)
- OneRec — arXiv 2506.13695; OneRec-V2 — arXiv 2508.20900; OneRec-Think — arXiv 2510.11639
- PLUM (YouTube) — arXiv 2510.07784 (WWW 2026)
- PinRec (Pinterest) — arXiv 2504.10507
- LinkedIn causal-LM feed retrieval — arXiv 2510.14223
- LIGER: Unifying Generative and Dense Retrieval — arXiv 2411.18814
- COBRA: cascaded sparse-dense representations — arXiv 2503.02453
- SID practitioner's handbook — arXiv 2507.22224 (CIKM 2025)
- Better Generalization with Semantic IDs — Google, RecSys 2024
- Cold-start reproducibility study — arXiv 2603.29845
- UNGER (scaling critique) — arXiv 2502.06269

## Semantic-ID tokenizers (2025–26)
- Drift-Aware Continual Tokenization — arXiv 2603.29705
- Qualification-Aware SID Learning (collisions) — arXiv 2603.00632
- Differentiable Semantic ID — arXiv 2601.19711 (SIGIR 2026)
- Expressiveness Limits of Autoregressive SID Generation — arXiv 2605.06331
- End-to-end learnable item tokenization (ETEGRec) — SIGIR 2025
- Semantic IDs at Snapchat — arXiv 2026
- QARM (Kuaishou multimodal SIDs) — arXiv 2411.11739

## Two-tower, negatives, multi-interest
- Sampling-bias-corrected two-tower — Yi et al., RecSys 2019
- Mixed Negative Sampling — Yang et al., WWW 2020; Cross-Batch Negative Sampling — Wang et al., SIGIR 2021 (verify arXiv IDs)
- Correcting the LogQ Correction — Yandex, arXiv 2507.09331
- Embedding collapse / multi-embedding — arXiv 2310.04400 (ICML 2024)
- Pinterest multi-embedding retrieval — arXiv 2506.23060
- kNN-Embed — arXiv 2205.06205
- MIND, ComiRec, PIMI, IMSR — see Report B §5 and the retrieval survey arXiv 2407.21022
- IntTower — CIKM 2022; InteractRank (Pinterest) — WWW 2025
- OmniSearchSage (Pinterest) — arXiv 2404.16260 (WWW 2024)

## Long sequences
- SIM (Alibaba, 2020); ETA (2021)
- SDIM — arXiv 2205.10249
- TWIN — arXiv 2302.02352 (KDD 2023); TWIN-V2 — arXiv 2407.16357 (CIKM 2024)
- UxSID — arXiv 2605.09040 (2026; ranking-side)
- LONGER (ByteDance, 2025; ranking-side)

## Learnable indices
- Deep Retrieval (ByteDance) — arXiv 2007.07203
- TDM / JTM; Learning Optimal Tree Models under Beam Search — Zhuo et al., 2020

## Pre-ranking
- COLD — arXiv 2007.16122
- FSCD — Alibaba, 2021
- RankFlow — SIGIR 2022
- On Ranking Consistency of Pre-ranking Stage — arXiv 2205.01289
- COPR — CIKM 2023; JRC — 2022
- CIT (Contrastive Information Transfer) — 2022
- RankTower — arXiv 2407.12385
- SDCL — AAAI 2025
- ECM (Entire-chain Cross-domain Model) — arXiv 2310.08039
- Hybrid Cross-Stage Coordination Pre-ranking — arXiv 2502.10284
- Meta ads cross-stage L1 — arXiv 2502.06834
- MTGR (Meituan generative ranking) — CIKM 2025

## Infrastructure
- Monolith — arXiv 2209.07663
- ZionEX / Neo — arXiv 2104.05158 (ISCA 2022)
- TorchRec — RecSys 2022 (dl.acm.org 3523227.3547387)
- ScaNN anisotropic VQ — arXiv 1908.10396; SOAR — arXiv 2404.00774
- NVIDIA cuVS / CAGRA — vendor docs and Milvus benchmarks (indicative)
- MTIA v1/v2 — Meta engineering blog; TPU v4 SparseCore — Google

## Surveys referenced by Report B
- A Comprehensive Survey on Retrieval Methods in Recommender Systems — arXiv 2407.21022
- A Survey on Generative Recommendation: Data, Model, and Tasks — arXiv 2510.27157
- A Survey of Real-World Recommender Systems — arXiv 2509.06002
- Neural Re-ranking for Multi-stage Recommenders — RecSys 2022 tutorial slides

## Company sources
- Netflix foundation model — Netflix Tech Blog, March 2025
- 360Brew (LinkedIn) — arXiv 2501.16450 (withdrawn; cite cautiously)
