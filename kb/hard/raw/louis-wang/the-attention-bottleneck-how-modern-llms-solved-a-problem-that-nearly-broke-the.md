# The Attention Bottleneck: How Modern LLMs Solved a Problem That Nearly Broke the Transformer

**Source:** https://louiswang524.github.io/blog/attention-variants/
**Ingested:** 2026-04-05
**Tags:** llms, recsys, ai-agents, ml-systems, attention, transformers

---

[Home](/) › [Blog](/blog) › The Attention Bottleneck: How Modern LLMs Solved a Problem That Nearly Broke the Transformer  
The Attention Bottleneck: How Modern LLMs Solved a Problem That Nearly Broke the Transformer
 
 March 28, 2026 · 16 min read  · [transformers](/tags/transformers)[attention](/tags/attention)[LLM](/tags/LLM)[deep learning](/tags/deep learning)[GQA](/tags/GQA)[flash attention](/tags/flash attention)[linear attention](/tags/linear attention) 
  
Every modern large language model — GPT-4, Llama 3, Gemini, Mistral — is a transformer. Every transformer is built around attention. But the original mechanism from “Attention Is All You Need” (Vaswani et al., 2017) cannot scale to those lengths. No GPU that exists today can run it at 128K tokens.

The math makes the problem concrete. The attention matrix for a single layer has n2n^2n2 entries, where nnn is sequence length. At n=32,768n = 32{,}768n=32,768 tokens in FP16, that matrix occupies roughly 2 GB of GPU memory — for one layer. With 32 layers, attention matrices alone require 64 GB. The H100, the most powerful production GPU available, has 80 GB of HBM in total.

This post traces how the field solved that problem — not once, but four separate times, each addressing a different bottleneck. The variants covered here are not academic curiosities. They are prerequisites for every LLM running at scale today.

[The Baseline: Scaled Dot-Product Attention](#the-baseline-scaled-dot-product-attention)

Before examining the variants, we need a precise definition of what they are varying from. Scaled dot-product attention takes three matrices as input — queries Q∈Rn×dkQ \in \mathbb{R}^{n \times d_k}Q∈Rn×dk​, keys K∈Rn×dkK \in \mathbb{R}^{n \times d_k}K∈Rn×dk​, and values V∈Rn×dvV \in \mathbb{R}^{n \times d_v}V∈Rn×dv​ — and produces a weighted sum of values:

Attention(Q,K,V)=softmax ⁣(QK⊤dk)V\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) VAttention(Q,K,V)=softmax(dk​

​QK⊤​)V

The dk\sqrt{d_k}dk​

​ scaling prevents dot products from growing large in magnitude, which would push softmax into regions with near-zero gradients.

**Multi-head attention (MHA)** runs HHH independent attention computations in parallel, each projecting into a lower-dimensional subspace:

MultiHead(Q,K,V)=Concat(head1,…,headH) WO\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_H)\, W^OMultiHead(Q,K,V)=Concat(head1​,…,headH​)WO
headi=Attention(QWiQ,  KWiK,  VWiV)\text{head}_i = \text{Attention}(Q W^Q_i,\; K W^K_i,\; V W^V_i)headi​=Attention(QWiQ​,KWiK​,VWiV​)

where WiQ,WiK∈Rdmodel×dkW^Q_i, W^K_i \in \mathbb{R}^{d_{\text{model}} \times d_k}WiQ​,WiK​∈Rdmodel​×dk​, WiV∈Rdmodel×dvW^V_i \in \mathbb{R}^{d_{\text{model}} \times d_v}WiV​∈Rdmodel​×dv​, and dk=dv=dmodel/Hd_k = d_v = d_{\text{model}} / Hdk​=dv​=dmodel​/H.

[Complexity](#complexity)

Computing QK⊤QK^\topQK⊤ produces an n×nn \times nn×n matrix. Time complexity is O(n2d)O(n^2 d)O(n2d); memory to store the attention matrix is O(n2)O(n^2)O(n2). This quadratic dependence on nnn is the root cause of every problem in the sections that follow.

[The KV Cache](#the-kv-cache)

During autoregressive inference — generating one token at a time — the model must recompute keys and values for every previous token at each step unless they are cached. In practice, they are always cached: after computing KKK and VVV for position iii, they are stored and reused for all future positions.

The cache size per transformer layer is:

Cache=2×nseq×H×dhead×bytes per value\text{Cache} = 2 \times n_{\text{seq}} \times H \times d_{\text{head}} \times \text{bytes per value}Cache=2×nseq​×H×dhead​×bytes per value

For a 70B-parameter model with H=64H = 64H=64 heads, dhead=128d_{\text{head}} = 128dhead​=128, FP16 (2 bytes), and nseq=32,768n_{\text{seq}} = 32{,}768nseq​=32,768:

Cache per layer=2×32768×64×128×2≈1 GB\text{Cache per layer} = 2 \times 32768 \times 64 \times 128 \times 2 \approx 1\text{ GB}Cache per layer=2×32768×64×128×2≈1 GB

With 80 layers: 80 GB — the entire memory of an H100, before weights, activations, or any other state. The KV cache is the first wall.

[Problem 1: The KV Cache Explodes](#problem-1-the-kv-cache-explodes)

The KV cache grows with every attention head — and standard MHA has a lot of heads. The fix is to ask: do all those heads actually need their own keys and values?

[Multi-Query Attention](#multi-query-attention)

**Multi-Query Attention (MQA)** (Shazeer, 2019) answers no. It keeps HHH query heads but collapses keys and values to a single shared head:

headi=Attention(QWiQ,  KWK,  VWV)\text{head}_i = \text{Attention}(Q W^Q_i,\; K W^K,\; V W^V)headi​=Attention(QWiQ​,KWK,VWV)

A single WKW^KWK and WVW^VWV replaces the HHH separate projections. The KV cache shrinks by H×H\timesH×. For H=64H = 64H=64, that is a 64× memory reduction at inference time.

The quality cost is real but small. Shazeer found perplexity increases of roughly 1–2% on language modeling tasks — acceptable for most applications, especially when the alternative is running out of memory.

[Group Query Attention](#group-query-attention)

**Group Query Attention (GQA)** (Ainslie et al., 2023) generalizes MQA. Rather than collapsing to one K/V head, it creates GGG groups. Each group of H/GH/GH/G query heads shares one K/V head:

headi=Attention(QWiQ,  KWg(i)K,  VWg(i)V)\text{head}_i = \text{Attention}(Q W^Q_i,\; K W^K_{g(i)},\; V W^V_{g(i)})headi​=Attention(QWiQ​,KWg(i)K​,VWg(i)V​)

where g(i)=⌊i⋅G/H⌋g(i) = \lfloor i \cdot G / H \rfloorg(i)=⌊i⋅G/H⌋ maps each query head to its group.

MHA is GQA with G=HG = HG=H. MQA is GQA with G=1G = 1G=1. GQA interpolates between them:

VariantK/V headsCache vs. MHAQuality vs. MHA

MHAHHH1×1\times1×Baseline

GQA (GGG groups)GGGH/G×H/G\timesH/G× smallerNear-identical

MQA111H×H\timesH× smallerSmall degradation

   Multi-Head Attention  

      1× cache (baseline)   Multi-Query Attention  

      8× smaller cache   Group Query Attention  

      4× smaller cache  

*Figure 2: How MHA, MQA, and GQA differ in their key/value head structure. Circles = query heads, rectangles = K/V head pairs.*

**Uptraining from MHA:** To convert an existing MHA checkpoint to GQA, Ainslie et al. propose mean-pooling the H/GH/GH/G K/V head projections within each group to initialize the shared GQA head, then continuing training for a short period. This avoids training GQA models from scratch.

GQA is now the default in most production LLMs: Llama 2 70B, Llama 3, Mistral 7B, and Gemma all use it.

[Problem 2: The Sequence Length Wall](#problem-2-the-sequence-length-wall)

GQA and MQA reduce the KV cache. They do not reduce the cost of computing attention itself. The QK⊤QK^\topQK⊤ matrix is still n×nn \times nn×n. At n=100,000n = 100{,}000n=100,000 tokens, that is 101010^{10}1010 entries — approximately 20 GB at FP16, per layer, before any K/V cache optimizations apply.

The question becomes: does every token need to attend to every other token?

[Sparse Attention](#sparse-attention)

**Sparse Transformer** (Child et al., 2019) applies a binary mask M∈{0,1}n×nM \in \{0,1\}^{n \times n}M∈{0,1}n×n to restrict which positions attend to each other:

Attentionsparse(Q,K,V)=softmax ⁣(QK⊤dk+log⁡M)V\text{Attention}_{\text{sparse}}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + \log M\right) VAttentionsparse​(Q,K,V)=softmax(dk​

​QK⊤​+logM)V

where log⁡M\log MlogM is zero at allowed positions and −∞-\infty−∞ at masked positions (which become zero after softmax). Three patterns proved most useful:

**Local window:** Mij=1M_{ij} = 1Mij​=1 iff ∣i−j∣≤w|i - j| \leq w∣i−j∣≤w. Each token attends to its 2w2w2w nearest neighbors.

**Strided:** Mij=1M_{ij} = 1Mij​=1 iff (i−j) mod k=0(i - j) \bmod k = 0(i−j)modk=0. Every kkk-th token is globally visible.

**Combined:** local + strided, covering O(nn)O(n\sqrt{n})O(nn

​) pairs instead of O(n2)O(n^2)O(n2).

[Sliding Window Attention](#sliding-window-attention)

**Sliding Window Attention**, used in Longformer (Beltagy et al., 2020) and Mistral 7B (Jiang et al., 2023), is the causal special case of local windowing: each token attends only to the WWW most recent positions:

Mij=1[i−W≤j≤i]M_{ij} = \mathbf{1}[i - W \leq j \leq i]Mij​=1[i−W≤j≤i]

Complexity drops from O(n2)O(n^2)O(n2) to O(n⋅W)O(n \cdot W)O(n⋅W).

**Effective receptive field across layers:** Although each layer sees only a window of size WWW, information propagates across layers. A token at position iii can receive information from position jjj in ⌈(i−j)/W⌉\lceil (i - j) / W \rceil⌈(i−j)/W⌉ layers. With LLL layers stacked, the effective receptive field is W×LW \times LW×L.

Mistral 7B uses W=4,096W = 4{,}096W=4,096 with L=32L = 32L=32 transformer layers:

Effective context=4,096×32=131,072 tokens\text{Effective context} = 4{,}096 \times 32 = 131{,}072 \text{ tokens}Effective context=4,096×32=131,072 tokens

This is why Mistral achieves strong long-context performance despite attending to a small local window per layer.

  Query token ↑  Full Attention   

  

  ← Key tokens →  Sparse Attention   

  

  ← Key tokens →  Sliding Window (causal)   

  

  ← Key tokens →  

*Figure 1: Attention patterns for an 8-token sequence. Dark cells indicate attended positions.*

[Problem 3: Even O(n⋅W)O(n \cdot W)O(n⋅W) Has Limits](#problem-3-even-on-cdot-w-has-limits)

Sparse and sliding window patterns reduce the constant but do not change the complexity class. For very long sequences — or tasks where important context is globally distributed — fixed sparsity patterns miss signal. The deeper question is: can we reduce the complexity of attention from O(n2)O(n^2)O(n2) to O(n)O(n)O(n)?

[The Kernel Decomposition](#the-kernel-decomposition)

The obstacle is the softmax. Written out explicitly, the iii-th output of attention is:

Attention(Q,K,V)i=∑jexp⁡(qi⊤kj/d) vj∑jexp⁡(qi⊤kj/d)\text{Attention}(Q, K, V)_i = \frac{\sum_j \exp(q_i^\top k_j / \sqrt{d})\, v_j}{\sum_j \exp(q_i^\top k_j / \sqrt{d})}Attention(Q,K,V)i​=∑j​exp(qi⊤​kj​/d

​)∑j​exp(qi⊤​kj​/d

​)vj​​

The denominator sums over all jjj — the positions are coupled. You cannot compute the outputs independently.

Linear attention replaces the exponential kernel with a decomposable kernel κ(q,k)=ϕ(q)⊤ϕ(k)\kappa(q, k) = \phi(q)^\top \phi(k)κ(q,k)=ϕ(q)⊤ϕ(k) for some feature map ϕ:Rd→Rr\phi : \mathbb{R}^d \to \mathbb{R}^rϕ:Rd→Rr:

Attentionlinear(Q,K,V)i=ϕ(qi)⊤∑jϕ(kj) vj⊤ϕ(qi)⊤∑jϕ(kj)\text{Attention}_{\text{linear}}(Q, K, V)_i = \frac{\phi(q_i)^\top \sum_j \phi(k_j)\, v_j^\top}{\phi(q_i)^\top \sum_j \phi(k_j)}Attentionlinear​(Q,K,V)i​=ϕ(qi​)⊤∑j​ϕ(kj​)ϕ(qi​)⊤∑j​ϕ(kj​)vj⊤​​

Now factor the computation. Define:

S=∑jϕ(kj) vj⊤∈Rr×d,z=∑jϕ(kj)∈RrS = \sum_j \phi(k_j)\, v_j^\top \in \mathbb{R}^{r \times d}, \qquad z = \sum_j \phi(k_j) \in \mathbb{R}^rS=∑j​ϕ(kj​)vj⊤​∈Rr×d,z=∑j​ϕ(kj​)∈Rr

Compute SSS and zzz once in O(nr)O(nr)O(nr) time. Then each query is: ϕ(qi)⊤S  /  ϕ(qi)⊤z\phi(q_i)^\top S \;/\; \phi(q_i)^\top zϕ(qi​)⊤S/ϕ(qi​)⊤z in O(r)O(r)O(r) time. Total: O(nr)O(nr)O(nr) — linear in sequence length.

[Linear Transformer](#linear-transformer)

**Linear Transformer** (Katharopoulos et al., 2020) uses ϕ(x)=elu(x)+1\phi(x) = \text{elu}(x) + 1ϕ(x)=elu(x)+1, which ensures positivity (required for the kernel interpretation). The causal variant accumulates SSS and zzz as prefix sums, making it equivalent to an RNN — enabling O(1)O(1)O(1) per-step inference once the recurrence is unrolled.

[Performer (FAVOR+)](#performer-favor)

Rather than replacing softmax with an arbitrary kernel, **Performer** (Choromanski et al., 2020) approximates the softmax kernel itself using random features (FAVOR+: Fast Attention Via positive Orthogonal Random features):

exp⁡(q⊤k/d)≈Eω ⁣[ϕω(q)⊤ϕω(k)]\exp(q^\top k / \sqrt{d}) \approx \mathbb{E}_\omega\!\left[\phi_\omega(q)^\top \phi_\omega(k)\right]exp(q⊤k/d

​)≈Eω​[ϕω​(q)⊤ϕω​(k)]

where ϕω(x)=1mexp⁡ ⁣(ωr⊤x−∥x∥22)\phi_\omega(x) = \frac{1}{\sqrt{m}}\exp\!\left(\omega_r^\top x - \tfrac{\|x\|^2}{2}\right)ϕω​(x)=m

​1​exp(ωr⊤​x−2∥x∥2​) for random directions ωr∼N(0,Id)\omega_r \sim \mathcal{N}(0, I_d)ωr​∼N(0,Id​) drawn as orthogonal vectors. Orthogonality reduces estimator variance by approximately d×d\timesd× compared to i.i.d. sampling.

[Quality Trade-off](#quality-trade-off)

Linear attention approximates softmax — it loses the sharp, peaked attention distributions that standard attention learns. For tasks requiring precise token recall (e.g. copying a specific value from earlier in the context), the approximation gap is measurable. For tasks that aggregate information over long spans, linear attention is often competitive with standard attention at a fraction of the compute.

[Problem 4: The GPU I/O Wall](#problem-4-the-gpu-io-wall)

By 2022, practitioners had sparse and linear attention. Yet profiling showed standard attention was still slow. The GPU’s tensor cores were sitting idle. The bottleneck was not arithmetic — it was memory bandwidth. Moving data between memory tiers dominated runtime.

[The GPU Memory Hierarchy](#the-gpu-memory-hierarchy)

Modern GPUs have two relevant memory tiers:

**SRAM (shared memory, on-chip):** ~20 MB on an A100, bandwidth ~19 TB/s

**HBM (high-bandwidth memory, off-chip):** 40–80 GB on an A100, bandwidth ~2 TB/s

SRAM is roughly 10× faster than HBM but 2,000× smaller. Standard attention reads QQQ, KKK, VVV from HBM and computes QK⊤QK^\topQK⊤. It writes the n×nn \times nn×n result to HBM, reads it back for softmax, then reads it again for the VVV multiplication. That is three round-trips over O(n2)O(n^2)O(n2) data — dominated by HBM bandwidth, not arithmetic.

[Flash Attention](#flash-attention)

**Flash Attention** (Dao et al., 2022) achieves the same mathematical output as standard attention while never materializing the full n×nn \times nn×n matrix in HBM. It does this with three ideas:

**1. Tiling.** Partition QQQ, KKK, VVV into blocks of size Br×BcB_r \times B_cBr​×Bc​ that fit in SRAM. Process one block at a time, keeping all intermediate values on-chip.

**2. Online softmax.** Softmax over a full row requires seeing all scores first. The online softmax algorithm computes a numerically stable result using running statistics. For each new block of key-value pairs, update:

mnew=max⁡(mold,  rowmax(Sblock))m^{\text{new}} = \max(m^{\text{old}},\; \text{rowmax}(S_{\text{block}}))mnew=max(mold,rowmax(Sblock​))
ℓnew=emold−mnew⋅ℓold+rowsum ⁣(eSblock−mnew)\ell^{\text{new}} = e^{m^{\text{old}} - m^{\text{new}}} \cdot \ell^{\text{old}} + \text{rowsum}\!\left(e^{S_{\text{block}} - m^{\text{new}}}\right)ℓnew=emold−mnew⋅ℓold+rowsum(eSblock​−mnew)
Onew=diag ⁣(emold−mnew)Oold+eSblock−mnewVblockO^{\text{new}} = \text{diag}\!\left(e^{m^{\text{old}} - m^{\text{new}}}\right) O^{\text{old}} + e^{S_{\text{block}} - m^{\text{new}}} V_{\text{block}}Onew=diag(emold−mnew)Oold+eSblock​−mnewVblock​

After all blocks: Ofinal=diag(1/ℓnew)⋅OnewO_{\text{final}} = \text{diag}(1/\ell^{\text{new}}) \cdot O^{\text{new}}Ofinal​=diag(1/ℓnew)⋅Onew.

This produces the exact same result as computing softmax over all scores at once.

**3. Recomputation.** The backward pass normally needs the n×nn \times nn×n attention matrix to compute gradients. Flash Attention discards it and recomputes from the saved output OOO and softmax statistics (ℓ,m)(\ell, m)(ℓ,m) during backprop. This trades extra FLOPs for drastically less HBM traffic.

**Result:** IO complexity drops from O(n2)O(n^2)O(n2) to O(n2/M)O(n^2 / M)O(n2/M) where MMM is SRAM size. On an A100:

**2–4×** wall-clock speedup over PyTorch standard attention

**5–20×** reduction in GPU memory usage for the attention operation

The mathematical output is bit-for-bit identical to standard attention.

 Memory access comparison: Standard Attention vs Flash Attention   

   

      Standard Attention   GPU   SRAM (fast, small)  

    3 round-trips   HBM (slow, large)   n×n matrix     Flash Attention   GPU   SRAM (fast, small)    tiles   

  output O only   HBM (slow, large)  

*Figure 3: Standard attention makes 3 round-trips over the n×n matrix. Flash Attention keeps tiles in SRAM and writes only the output to HBM.*

[Subsequent Versions](#subsequent-versions)

**Flash Attention 2** (Dao, 2023): restructures work partitioning across GPU warps to reduce non-matmul FLOPs and improve parallelism. Roughly 2× faster than FA1.

**Flash Attention 3** (Shah et al., 2024): targets the H100’s Hopper architecture specifically — uses warp-specialized pipelines, asynchronous memory copies, and FP8 precision. Achieves up to 75% of the H100’s theoretical FP8 peak FLOPS.

[How Modern LLMs Combine These](#how-modern-llms-combine-these)

No single variant won. Production models stack them because the bottlenecks they address are independent:

ModelKV ReductionLong ContextIO Efficiency

GPT-3 (2020)MHA — none—Standard

PaLM (2022)MQA—Standard

Llama 2 70B (2023)GQA—Flash Attention 2

Mistral 7B (2023)GQASliding Window (W=4096W = 4096W=4096)Flash Attention 2

Llama 3 8B/70B (2024)GQA—Flash Attention 2

Gemma 7B (2024)GQA—Flash Attention 2

Qwen2 7B/72B (2024)GQA—Flash Attention 2

Qwen2.5 72B (2024)GQA128K (YaRN)Flash Attention 2

DeepSeek-V2 (2024)MLA128KFlash Attention 2

DeepSeek-V3 (2024)MLA128KFlash Attention 2

Kimi k1.5 (2025)MHA128KFlash Attention 2

Kimi K2 (2025)MLA128KFlash Attention 2

The combinations are not arbitrary. Each technique addresses a different bottleneck:

**GQA** attacks the KV cache — the memory cost per sequence during inference.

**Sliding Window Attention** attacks the per-layer compute cost for long inputs.

**Flash Attention** attacks GPU memory bandwidth — it applies regardless of which attention variant you use.

**MLA** attacks the KV cache more aggressively than GQA, using low-rank compression instead of head-sharing.

[A New Direction: Multi-head Latent Attention (MLA)](#a-new-direction-multi-head-latent-attention-mla)

GQA reduces the KV cache by sharing key/value heads across query groups — but the cache still grows linearly with sequence length. DeepSeek-V2 (Liu et al., 2024) introduced a different approach: compress the KV cache into a low-dimensional latent vector and store that instead.

The core idea: instead of caching full KKK and VVV matrices, compute a compressed latent cKV∈Rdcc^{KV} \in \mathbb{R}^{d_c}cKV∈Rdc​ where dc≪nh⋅dhd_c \ll n_h \cdot d_hdc​≪nh​⋅dh​:

cKV=WDKVhc^{KV} = W^{DKV} hcKV=WDKVh

At inference, decompress on the fly:

K=WUKcKV,V=WUVcKVK = W^{UK} c^{KV}, \quad V = W^{UV} c^{KV}K=WUKcKV,V=WUVcKV

Only cKVc^{KV}cKV is cached. For DeepSeek-V2, this reduces the KV cache per token by 93.3% compared to standard MHA. GQA with G=8G = 8G=8 groups achieves roughly an 8× reduction; MLA achieves roughly a 57–93× reduction depending on configuration.

One complication: Rotary Position Embeddings (RoPE) cannot be applied to compressed keys — position information is entangled with the compression. DeepSeek-V2 solves this with **decoupled RoPE**: a separate set of query and key vectors carries position, applied independently before the attention dot product. The compressed KV path handles content; the RoPE path handles position.

MLA is compatible with Flash Attention and can be used alongside sliding window patterns. DeepSeek-V3 and Kimi K2 both adopted MLA directly, making it the dominant KV cache strategy for frontier MoE models as of 2025.

[Qwen2 and Long-Context Extrapolation](#qwen2-and-long-context-extrapolation)

Qwen2 uses GQA across all model sizes and adds **Dual Chunk Attention (DCA)** for long-context inference. DCA splits the sequence into fixed-size chunks and uses three query types per token: one for attending within the same chunk, one for attending to the preceding chunk, and one for attending to all other chunks with relative position clamped. This allows Qwen2 to extrapolate from a 32K training context to 128K at inference without retraining, using position interpolation (YaRN) alongside DCA. Qwen2.5 extends the same approach to 1M tokens in the Turbo variant, adding sparse attention patterns based on MInference.

[Decision Framework](#decision-framework)

If you are building or fine-tuning a model:

Hitting **KV cache limits** during inference → add GQA (simpler, widely supported) or MLA (higher compression, more implementation complexity)

Hitting **sequence length limits** → add sliding window or linear attention

Hitting **training throughput** → enable Flash Attention (always do this regardless of attention variant)

Need **ultra-long context** without retraining → combine YaRN position scaling with DCA or sparse attention patterns

**What this post does not cover:** state-space models (Mamba, S4) and hybrid architectures (Jamba, Zamba) represent a different branch of the scaling tree — replacing attention with selective state transitions rather than approximating it. That is a separate post.

[References](#references)

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). [Attention Is All You Need](https://arxiv.org/abs/1706.03762). *NeurIPS 2017*.

Shazeer, N. (2019). [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150). *arXiv:1911.02150*.

Ainslie, J., Lee-Thorp, J., de Jong, M., Zemlyanskiy, Y., Lebrón, F., & Sanghai, S. (2023). [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245). *EMNLP 2023*.

Child, R., Gray, S., Radford, A., & Sutskever, I. (2019). [Generating Long Sequences with Sparse Transformers](https://arxiv.org/abs/1904.10509). *arXiv:1904.10509*.

Beltagy, I., Peters, M. E., & Cohan, A. (2020). [Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150). *arXiv:2004.05150*.

Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., de las Casas, D., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., Lavaud, L. R., Lachaux, M.-A., Stock, P., Le Scao, T., Lavril, T., Wang, T., Lacroix, T., & El Sayed, W. (2023). [Mistral 7B](https://arxiv.org/abs/2310.06825). *arXiv:2310.06825*.

Katharopoulos, A., Vyas, A., Pappas, N., & Fleuret, F. (2020). [Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention](https://arxiv.org/abs/2006.16236). *ICML 2020*.

Choromanski, K., Likhosherstov, V., Dohan, D., Song, X., Gane, A., Sarlos, T., Hawkins, P., Davis, J., Mohiuddin, A., Kaiser, Ł., Belanger, D., Colwell, L., & Weller, A. (2020). [Rethinking Attention with Performers](https://arxiv.org/abs/2009.14794). *ICLR 2021*.

Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022). [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135). *NeurIPS 2022*.

Dao, T. (2023). [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691). *ICLR 2024*.

Shah, J., Bikshandi, G., Zhang, Y., Thakkar, V., Ramani, P., & Dao, T. (2024). [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](https://arxiv.org/abs/2407.08608). *arXiv:2407.08608*.

DeepSeek-AI, Liu, A., Feng, B., et al. (2024). [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434). *arXiv:2405.04434*.

DeepSeek-AI, Liu, A., Feng, B., et al. (2024). [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437). *arXiv:2412.19437*.

Qwen Team, Alibaba Group. (2024). [Qwen2 Technical Report](https://arxiv.org/abs/2407.10671). *arXiv:2407.10671*.

Qwen Team, Alibaba Group. (2024). [Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115). *arXiv:2412.15115*.

Kimi Team, Moonshot AI. (2025). [Kimi k1.5: Scaling Reinforcement Learning with LLMs](https://arxiv.org/abs/2501.12599). *arXiv:2501.12599*.

   
 [ ← Previous The Harness Is the Moat: Why Autonomous AI Agents Live or Die by Their Architecture ](/blog/harness-is-the-moat) 
 
 [ Next → Two Bets on Generative Recommendation: Semantic IDs vs. Fine-Tuned LLMs ](/blog/genrec-paradigm-comparison)
