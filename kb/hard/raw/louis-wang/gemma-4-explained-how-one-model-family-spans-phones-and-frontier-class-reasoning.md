# Gemma 4 Explained: How One Model Family Spans Phones and Frontier-Class Reasoning

**Source:** https://louiswang524.github.io/blog/gemma-family/
**Ingested:** 2026-04-05
**Tags:** llms, recsys, ai-agents, ml-systems

---

[Home](/) › [Blog](/blog) › Gemma 4 Explained: How One Model Family Spans Phones and Frontier-Class Reasoning  
Gemma 4 Explained: How One Model Family Spans Phones and Frontier-Class Reasoning
 
 April 2, 2026 · 13 min read  · [Gemma](/tags/Gemma)[LLM](/tags/LLM)[Google DeepMind](/tags/Google DeepMind)[mixture of experts](/tags/mixture of experts)[on-device AI](/tags/on-device AI)[multimodal](/tags/multimodal)[open models](/tags/open models) 
  
[1. The Intelligence-per-Parameter Problem](#1-the-intelligence-per-parameter-problem)

Gemma 4 matters because it compresses an unusually wide deployment range into one architecture family: small enough for edge devices, large enough to stay competitive on serious reasoning and coding benchmarks.

On April 2, 2026, Google DeepMind released Gemma 4, an open model family whose largest variant scores 89.2% on AIME 2026, the same mathematics benchmark used to evaluate leading frontier models. At the other end of the lineup, the smallest variant, Effective 2B (E2B), is designed for edge devices such as phones and Raspberry Pi-class hardware. [[8]](#references)

Those two facts are the point. Gemma 4 is not claiming that a 2B-class model now matches a frontier system on hard reasoning benchmarks; the smaller models clearly do not. The novelty is that one family spans both ends of the deployment spectrum, and it does so by changing what parameter count means for memory use, latency, and capability.

This post unpacks the four decisions behind that span: a Matryoshka-nested model structure with per-layer embeddings (MatFormer + PLE), a hybrid local/global attention mechanism with proportional rotary position encoding (p-RoPE), a parallel dense-plus-mixture-of-experts feed-forward design, and native agentic tooling in the default interaction stack. We start with the three Gemma generations that defined the problem Gemma 4 is solving.

**At a glance.** Gemma 4’s story is not “one tiny model beats frontier labs.” It is “one architecture family stretches unusually far,” from E2B/E4B edge deployment to 26B A4B / 31B models that stay competitive on hard benchmarks.

[2. The Gemma Lineage: Three Generations, Three Problems Solved](#2-the-gemma-lineage-three-generations-three-problems-solved)

**Gemma 1 (February 2024)** established Google’s open-model baseline by applying Gemini architecture research to publicly releasable weights. The 2B and 7B models are decoder-only transformers with GeGLU activations (a gated variant of the standard feed-forward non-linearity), RoPE positional encodings, and RMSNorm at each sub-layer. The 2B model uses multi-query attention (MQA) — one key/value head shared across all query heads — while the 7B uses full multi-head attention (MHA). Training data totaled 3 trillion tokens for the 2B model and 6 trillion for the 7B, with an 8,192-token context window. [[1]](#references)

**Gemma 2 (June 2024)** addressed quality-at-smaller-size through knowledge distillation. The 2B and 9B models were trained with a 27B teacher: rather than predicting the next token from one-hot targets, smaller models minimize a combination of cross-entropy loss and KL divergence from the teacher’s output distribution. Architecturally, Gemma 2 added two further innovations: sliding-window attention (alternating between local and full-quadratic attention layers per the interleaved design) and logit soft-capping (scaling logits to a bounded range before softmax to stabilize training). [[2]](#references)

**Gemma 3 (March 2025)** made the first multimodal leap. A frozen 400-million-parameter SigLIP vision encoder processes images at 896×896 pixels and compresses them into 256 visual token vectors, which are concatenated into the text token sequence at the transformer input. Context length expanded to 128K tokens, enabled by a higher ratio of local (sliding-window) to global (full) attention layers — which limits KV-cache growth with sequence length. Gemma 3 also introduced multilingual training across 140+ languages, a model family spanning 270M to 27B parameters, and continued distillation across all sizes. [[3]](#references)

Gemma 1Gemma 2Gemma 3Gemma 4

**Sizes**2B, 7B2B, 9B, 27B270M–27BE2B, E4B, 26B A4B, 31B

**Context**8K8K128K128K / 256K

**Modality**TextTextText + ImageText + Image across all models; audio on E2B/E4B; video handled as frames

**Key innovation**Gemini-derived baselineDistillation + sliding attentionSigLIP multimodalMatFormer + parallel MoE

**License**Gemma ToSGemma ToSGemma ToSApache 2.0

[3. Gemma 4: Four Architectural Decisions](#3-gemma-4-four-architectural-decisions)

[3.1 MatFormer + Per-Layer Embeddings](#31-matformer--per-layer-embeddings)

[The problem: a phone has 8 GB of RAM](#the-problem-a-phone-has-8-gb-of-ram)

Traditional transformer models store a single embedding matrix at the input layer: one row per vocabulary token. For a model with a 256K-token vocabulary and 4,096-dimensional embeddings in BF16, that matrix occupies 2 GB. On a phone with 8 GB of total RAM, this leaves little headroom for the rest of the model.

Gemma 4 addresses this with two linked mechanisms: MatFormer and Per-Layer Embeddings (PLE).

[MatFormer: nesting smaller models inside larger ones](#matformer-nesting-smaller-models-inside-larger-ones)

MatFormer (Matryoshka Transformer) extends Matryoshka Representation Learning to the full transformer. A single checkpoint trains nested sub-models at multiple scales simultaneously. The 2B model’s weights are a strict subset of the 4B’s, which are a subset of the 26B’s, and so on:

θE2B⊂θE4B⊂θ26B⊂θ31B\theta_\text{E2B} \subset \theta_\text{E4B} \subset \theta_\text{26B} \subset \theta_\text{31B}θE2B​⊂θE4B​⊂θ26B​⊂θ31B​

This means a single training run can produce nested sub-models at different scales. Conceptually, inference can select a smaller sub-model by taking a prefix of the larger parameter family. The important point is that the smaller models are structurally contained in the larger one rather than produced by a separate post-hoc distillation step.

 MatFormer nested model architecture — Gemma 4 
MatFormer: Nested Weight Subsets
   31B Dense 31B params · 31B active at inference   26B MoE 26B params · 3.8B active at inference   Effective 4B ~4B active params   Effective 2B ~2B active params  
θ_E2B ⊂ θ_E4B ⊂ θ_26B ⊂ θ_31B — one checkpoint serves all four model sizes
 

Figure 1. Gemma 4 model sizes as nested weight subsets. The important idea is that smaller variants are structurally contained inside larger ones rather than trained as entirely separate checkpoints.

[Per-Layer Embeddings: move more parameters into lookup-heavy storage](#per-layer-embeddings-move-more-parameters-into-lookup-heavy-storage)

Standard token embeddings are computed once at the input: a single lookup mapping token IDs to embedding vectors. Per-Layer Embeddings (PLE) distribute token-specific embedding tables across decoder layers instead of concentrating all of that capacity in one large input embedding matrix.

Google’s public Gemma 4 documentation does not fully specify the exact residual-path implementation details, but it does make the deployment consequence clear: E2B and E4B have materially more *total* parameters than their *effective* parameter counts because many parameters sit in these embedding tables and behave more like lightweight lookups than always-on dense compute. [[8]](#references)

That is why Google reports the small models as 2.3B effective / 5.1B total and 4.5B effective / 8B total instead of giving a single headline parameter number. PLE is less about making the model smaller in absolute terms than about shifting more of the parameter budget into a form that is friendlier to on-device deployment.

[3.2 Hybrid Attention + p-RoPE](#32-hybrid-attention--p-rope)

[The KV-cache problem at 256K context](#the-kv-cache-problem-at-256k-context)

Full self-attention computes QK⊤∈Rn×nQK^\top \in \mathbb{R}^{n \times n}QK⊤∈Rn×n and caches K,V∈Rn×dK, V \in \mathbb{R}^{n \times d}K,V∈Rn×d for every position. For a 31B model with 64 layers, d=4096d = 4096d=4096, and n=256,000n = 256{,}000n=256,000 tokens in BF16:

KV cache=2×L×n×d×2 bytes=2×64×256,000×4096×2≈536 GB\text{KV cache} = 2 \times L \times n \times d \times 2\,\text{bytes} = 2 \times 64 \times 256{,}000 \times 4096 \times 2 \approx 536\,\text{GB}KV cache=2×L×n×d×2bytes=2×64×256,000×4096×2≈536GB

No single GPU can hold this. Gemma 4 addresses the problem with a hybrid attention stack that interleaves local sliding-window layers with full global layers, while also using unified keys/values in the global layers and proportional rotary position encoding (p-RoPE). [[8]](#references)

[Local sliding-window attention](#local-sliding-window-attention)

A sliding-window attention (SWA) layer with window www restricts each query position iii to attend only to positions [i−w, i][i-w,\, i][i−w,i]:

SWA(Q,K,V)i=softmax ⁣(Qi K[i−w:i]⊤dk)V[i−w:i]\text{SWA}(Q, K, V)_i = \text{softmax}\!\left(\frac{Q_i\, K_{[i-w:i]}^\top}{\sqrt{d_k}}\right) V_{[i-w:i]}SWA(Q,K,V)i​=softmax(dk​

​Qi​K[i−w:i]⊤​​)V[i−w:i]​

The KV cache for a single SWA layer holds www key-value pairs — constant regardless of total sequence length nnn. Five consecutive SWA layers contribute 5×w×d×2 bytes5 \times w \times d \times 2\,\text{bytes}5×w×d×2bytes to the cache. Local layers handle fine-grained dependencies within the window but cannot propagate information across the full document.

[Global full-attention layers](#global-full-attention-layers)

Periodically, a standard full-attention layer computes the full n×nn \times nn×n matrix and integrates the local context built up by the sliding-window layers into a sequence-level representation. These layers are the expensive part of the stack, and their KV cache still grows with nnn, but only the global layers pay that full long-context cost:

KV cache (Gemma 4)≈klocal×w×d⏟SWA layers (constant)+kglobal×n×d⏟global layers (linear in n)\text{KV cache (Gemma 4)} \approx \underbrace{k_\text{local} \times w \times d}_\text{SWA layers (constant)} + \underbrace{k_\text{global} \times n \times d}_\text{global layers (linear in } n\text{)}KV cache (Gemma 4)≈SWA layers (constant)

klocal​×w×d​​+global layers (linear in 

kglobal​×n×d​​n)

 Hybrid attention pattern in Gemma 4 — local and global layers  
Hybrid Attention: 5 Local → 1 Global (per cycle)
   
Local (sliding window) — KV cache: O(w)
  
Global (full attention) — KV cache: O(n)
   
Layer 0    Local — sliding window   O(w)   
Layer 1    Local — sliding window   O(w)   
Layer 2    Local — sliding window   O(w)   
Layer 3    Local — sliding window   O(w)   
Layer 4    Local — sliding window   O(w)   
Layer 5    Global — full self-attention   O(n)   
Layer 6    Local — sliding window   O(w)   
Layer 7    Local — sliding window   O(w)   
Layer 8    Local — sliding window   O(w)   
Layer 9    Local — sliding window   O(w)   
Layer 10    Local — sliding window   O(w)   
Layer 11    Global — full self-attention   O(n)    
w = fixed window size (constant with n). n = full sequence length (grows with context).
 

Figure 2. Illustrative local and global attention interleaving. Most layers operate on bounded windows, while periodic global layers reintegrate document-scale context.

[p-RoPE for long-context extrapolation](#p-rope-for-long-context-extrapolation)

Standard RoPE (Rotary Position Embedding) encodes position mmm using rotation frequencies θi=10000−2i/d\theta_i = 10000^{-2i/d}θi​=10000−2i/d. When the model is queried at context lengths beyond its training length LtrainL_\text{train}Ltrain​, positions see rotation angles outside the trained distribution, causing instability.

Proportional RoPE (p-RoPE) rescales frequencies proportionally to the target context length LtargetL_\text{target}Ltarget​:

θip-RoPE=θi⋅LtrainLtarget\theta_i^{\text{p-RoPE}} = \theta_i \cdot \frac{L_\text{train}}{L_\text{target}}θip-RoPE​=θi​⋅Ltarget​Ltrain​​

Conceptually, this compresses the positional signal so that the model’s trained angular range covers a longer target context. In Gemma 4, Google combines p-RoPE with hybrid local/global attention to support 128K context on E2B/E4B and 256K on 26B A4B / 31B. [[8]](#references)

[3.3 Parallel Dense + MoE FFN](#33-parallel-dense--moe-ffn)

[Why standard Mixture of Experts isn’t enough](#why-standard-mixture-of-experts-isnt-enough)

In a standard Mixture of Experts (MoE) transformer, the feed-forward network (FFN) is replaced entirely by a router and a bank of experts:

FFNMoE(x)=∑i∈TopK(r(x), k)gi(x)⋅Ei(x)\text{FFN}_\text{MoE}(x) = \sum_{i \in \text{TopK}(r(x),\, k)} g_i(x) \cdot E_i(x)FFNMoE​(x)=∑i∈TopK(r(x),k)​gi​(x)⋅Ei​(x)

where r(x)=softmax(Wrx)∈RNr(x) = \text{softmax}(W_r x) \in \mathbb{R}^Nr(x)=softmax(Wr​x)∈RN is the router over NNN experts, gi(x)=r(x)ig_i(x) = r(x)_igi​(x)=r(x)i​ is the routing weight, and TopK selects the kkk highest-weighted experts. At inference, only kkk of NNN experts activate per token — compute scales as O(k)O(k)O(k) rather than O(N)O(N)O(N).

The issue: routing is all-or-nothing. If the router assigns a token to sub-optimal experts — a failure mode called routing collapse — there is no fallback. The FFN’s entire representational capacity depends on getting the routing decision right.

[Gemma 4’s parallel design](#gemma-4s-parallel-design)

Gemma 4 keeps a dense GeGLU FFN running in every layer *alongside* the MoE experts, summing both outputs:

FFNGemma4(x)=GeGLUdense(x)⏟always active+shared(x)⏟always active shared expert+∑i∈TopK(r(x), 8)gi(x)⋅Ei(x)⏟sparse: top-8 of 128 experts\text{FFN}_\text{Gemma4}(x) = \underbrace{\text{GeGLU}_\text{dense}(x)}_{\text{always active}} + \underbrace{\text{shared}(x)}_{\text{always active shared expert}} + \underbrace{\sum_{i \in \text{TopK}(r(x),\, 8)} g_i(x) \cdot E_i(x)}_{\text{sparse: top-8 of 128 experts}}FFNGemma4​(x)=always active

GeGLUdense​(x)​​+always active shared expert

shared(x)​​+sparse: top-8 of 128 experts

i∈TopK(r(x),8)∑​gi​(x)⋅Ei​(x)​​

where GeGLU is defined as:

GeGLU(x)=GELU(xW1)⊙(xW2)\text{GeGLU}(x) = \text{GELU}(xW_1) \odot (xW_2)GeGLU(x)=GELU(xW1​)⊙(xW2​)

The dense FFN provides stable, always-on representational capacity. The sparse branch adds specialization through 128 routed experts with 8 active per token, plus one shared expert that is always on. The 26B A4B model has 25.2B total parameters but only 3.8B active parameters per token at inference. [[8]](#references)

   

   

    
Standard MoE
 
Gemma 4 (parallel)
  

    Input x  

 replaces FFN entirely   Router + Top-8 Experts  

   Σ  

   Output    Input x  

  

 

  

 

   Dense GeGLU always active   Router + Experts top-8 of 128  

 

 

  

 

 

   ⊕  

   Output  
Standard MoE: FFN replaced by experts. Gemma 4: dense FFN runs in parallel with experts — outputs summed.
 

Figure 3. Standard MoE replaces the FFN with experts. Gemma 4 keeps dense capacity in parallel with sparse expert routing, reducing how much the layer depends on any single routing decision.

[Why the parallel design helps](#why-the-parallel-design-helps)

The most plausible benefit of this design is robustness. In a pure MoE block, representational quality depends heavily on the router choosing the right experts. In Gemma 4, some dense capacity remains available even when the sparse route is imperfect. That does not by itself prove why the benchmark gains happen, but it is a coherent explanation for how Google gets close to 31B-dense quality while keeping active parameters much lower.

[3.4 Native Agentic I/O](#34-native-agentic-io)

Previous Gemma generations did not expose this level of native chat, thinking, and function-calling support in the default prompting stack. Gemma 4 moves these capabilities into the official interaction format and tooling docs. [[8]](#references)

**Function calling** uses the chat template to declare tools and emit tool-call tokens, which your application then parses and executes:

<|turn>system
You are a helpful assistant.<|tool>declaration:get_current_weather{...}<tool|><turn|>
<|turn>user
Hey, what's the weather in Tokyo right now?<turn|>
<|turn>model
<|tool_call>call:get_current_weather{location:<|"|>Tokyo, JP<|"|>}<tool_call|><|tool_response>

The model does not execute tools itself. The supported flow is: the model emits a tool call, the application validates and executes it, then the application appends `tool_calls` and `tool_responses` back into the conversation before asking for the final answer. [[9]](#references)

**Thinking mode** is enabled through the official chat template rather than ad hoc prompt engineering. In the Hugging Face flow, `enable_thinking=True` inserts the `<|think|>` control token, and the processor can parse the model’s output into thought content, tool calls, and final answer. [[10]](#references)

**Native system role** support enables structured conversation control and persistent persona instructions without overloading the user/assistant turn format.

[4. Benchmarks and Practitioner Takeaways](#4-benchmarks-and-practitioner-takeaways)

[Benchmark results](#benchmark-results)

Before the table, it helps to separate the family into two stories: E2B/E4B are the edge models, while 26B A4B and 31B are the benchmark-chasing models. Reading all four rows as if they answer the same deployment question makes the lineup feel more confusing than it is.

ModelAIME 2026LiveCodeBench v6MMLU ProMMMU ProMATH-VisionArena AI

Gemma 4 E2B37.5%44.0%————

Gemma 4 E4B42.5%52.0%————

Gemma 4 26B A4B88.3%77.1%82.6%73.8%82.4%#6 open

Gemma 4 31B89.2%80.0%85.2%76.9%85.6%#3 open

The headline result is how close the 26B A4B model gets to the 31B dense model while activating only 3.8B parameters per token. That is strong evidence that the architecture is buying real efficiency rather than just moving parameters around on paper. The 31B dense model still leads the family on raw quality, but the 26B A4B result is what makes the lineup strategically interesting. [[8]](#references)

[Which model for which use case?](#which-model-for-which-use-case)

Use caseRecommended model

Mobile app, on-device assistant, Raspberry Pi, Jetson NanoE2B

On-device with more headroom, T4 GPU inferenceE4B

Developer machine, consumer GPU (RTX 4090 / 5090)26B A4B — much closer to 31B quality than its active parameter count suggests

Offline server, fine-tuning, research31B Dense

[The license change may matter more than the benchmarks](#the-license-change-may-matter-more-than-the-benchmarks)

Gemma 1, 2, and 3 shipped under custom Gemma terms rather than a standard permissive open-source license. Gemma 4 ships under Apache 2.0, which is a materially simpler legal position for teams that care about redistribution, internal compliance review, and long-term deployment optionality. For many practitioners, that license change matters nearly as much as the benchmark jump. [[11]](#references)

[References](#references)

Gemma Team, Google DeepMind. “Gemma: Open Models Based on Gemini Research and Technology.” *arXiv:2403.08295*, February 2024. [https://arxiv.org/abs/2403.08295](https://arxiv.org/abs/2403.08295)

Gemma Team, Google DeepMind. “Gemma 2: Improving Open Language Models at a Practical Size.” *arXiv:2408.00118*, June 2024. [https://arxiv.org/abs/2408.00118](https://arxiv.org/abs/2408.00118)

Gemma Team, Google DeepMind. “Gemma 3 Technical Report.” *arXiv:2503.19786*, March 2025. [https://arxiv.org/abs/2503.19786](https://arxiv.org/abs/2503.19786)

Google Blog. “Gemma 4: Byte for byte, the most capable open models.” April 2, 2026. [https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)

Google Developers Blog. “Bring state-of-the-art agentic skills to the edge with Gemma 4.” April 2, 2026. [https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/](https://developers.googleblog.com/bring-state-of-the-art-agentic-skills-to-the-edge-with-gemma-4/)

Google DeepMind. “Gemma 4.” April 2, 2026. [https://deepmind.google/models/gemma/gemma-4/](https://deepmind.google/models/gemma/gemma-4/)

HuggingFace Blog. “Welcome Gemma 4: Frontier multimodal intelligence on device.” April 2, 2026. [https://huggingface.co/blog/gemma4](https://huggingface.co/blog/gemma4)

Google AI for Developers. “Gemma 4 model card.” April 2, 2026. [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)

Google AI for Developers. “Function calling with Gemma 4.” April 2, 2026. [https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4](https://ai.google.dev/gemma/docs/capabilities/text/function-calling-gemma4)

Google AI for Developers. “Thinking mode in Gemma.” April 2, 2026. [https://ai.google.dev/gemma/docs/capabilities/thinking](https://ai.google.dev/gemma/docs/capabilities/thinking)

Google AI for Developers. “Gemma 4 license.” April 2, 2026. [https://ai.google.dev/gemma/docs/core/model_card_4#license](https://ai.google.dev/gemma/docs/core/model_card_4#license)

NVIDIA Technical Blog. “Bringing AI Closer to the Edge and On-Device with Gemma 4.” April 2, 2026. [https://developer.nvidia.com/blog/bringing-ai-closer-to-the-edge-and-on-device-with-gemma-4/](https://developer.nvidia.com/blog/bringing-ai-closer-to-the-edge-and-on-device-with-gemma-4/)

   
 [ ← Previous TurboQuant Explained: How Google Compresses KV Caches to 3 Bits Without Losing the Plot ](/blog/turboquant-explained) 
 
 [ Next → Building a Self-Improving Personal Knowledge Base Powered by LLM ](/blog/llm-knowledge-base)
