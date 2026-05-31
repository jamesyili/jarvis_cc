# 07 — Inference & Serving Economics

> **Bridge:** Your study plan correctly de-weights this as *IC-infra depth* — but an EM owns the *budget conversation*, and you have real anchors: UPP GPU serving (shipped, adopted by Notif/P2P), the two-tower "precompute the item side" trick (recsys's original KV-cache), distillation (which *is* your preranking alignment loss), and concrete training/serving cost numbers. Know the economics and the levers; don't write kernels.
> **Book:** Ch 6–7 (MoE), Ch 15 (inference workload), Ch 16 (KV cache), Ch 18 (speculative decoding), Ch 19 (compression), Ch 29 (serving stack) — skim per your plan.

---

## 1. The core idea

Training is a one-time capital cost; **inference is a recurring cost that dominates at scale** — you pay it on every request, forever. So the economics of serving *drive the architecture*: model size, quantization, batching, caching, and whether you can afford the model you trained. The EM job here is to *price the trade-offs*, not implement them.

The framing: *"Every serving decision is a point on a latency / throughput / cost / quality surface. My job is to know which knob moves which axis and what it costs in quality."*

---

## 2. The two-phase workload (the one mental model for LLM inference)

LLM generation has two phases with *opposite* bottlenecks — this is the single most useful thing to know:

| Phase | What it does | Bottleneck | Metric |
|---|---|---|---|
| **Prefill** | process the whole prompt at once | **compute-bound** (big matmuls, parallel) | **TTFT** (time to first token) |
| **Decode** | generate tokens one at a time | **memory-bandwidth-bound** (load weights + KV per token) | **throughput** (tokens/sec) |

- Decode is slow not because of FLOPs but because each token must stream the weights and the growing KV cache from memory — *memory-bound*. This is why batching helps decode (amortize the weight load across many sequences) and why the KV cache matters so much.
- **TTFT vs throughput vs cost** is the trade triangle. Interactive chat optimizes TTFT; bulk/offline optimizes throughput; both fight cost.

### The KV cache (the one detail worth knowing)
Autoregressive decoding would recompute attention over all prior tokens every step; the **KV cache** stores past keys/values so each new token is $O(n)$ not $O(n^2)$. The catch: **KV cache memory grows with batch × sequence length** and often becomes the binding constraint on how many requests you can serve. Hence the shrink-the-KV-cache toolbox: **GQA / MQA** (share keys/values across heads), local/sliding-window attention, MLA. Know *why* they exist (KV memory), not the math.

---

## 3. The cost levers (what an EM actually decides)

| Lever | What it trades | One-liner |
|---|---|---|
| **Quantization** | precision → memory/speed | serve in int8/fp8/int4; small quality hit for big memory/throughput win; the default first move |
| **Distillation (KD)** | a big teacher → a small fast student | *you already do this* — LWS is a distilled student of the L2 ranker; "fast classifiers are small distilled models" (your Integrity-seat note) |
| **Pruning** | sparsity → speed | drop weights/structure; usually less bang than quant/distill |
| **MoE** | params ↑, active-FLOPs flat | sparse experts: route each token to a few experts → dense-model quality at a fraction of the per-token compute. *Why frontier models are MoE.* |
| **Batching** | latency ↔ throughput | **continuous/in-flight batching** packs requests to keep the GPU busy; the core serving-stack win (vLLM-style) |
| **Caching** | recompute → memory | prefix/KV-cache reuse for shared prompts; **semantic caching** for repeated queries |
| **Speculative decoding** | a draft model proposes, the big model verifies | more tokens per big-model pass; faster decode, same outputs (one-liner) |

**MoE, one level deeper (still EM-altitude — name the facts, skip the routing math):** MoE replaces the dense FFN with $N$ expert FFNs + a router that sends each token to its **top-$k$** experts, so per-token compute scales with *active* experts while total capacity scales with *total* experts — **sparsity = $E_\text{total}/E_\text{active}$**. The hard part is **load balancing**: without it you get "rich-get-richer" expert collapse (a few experts hog the tokens). Classic fix = an **auxiliary load-balancing loss** (Switch Transformer); modern fix = **auxiliary-loss-free balancing via dynamic per-expert biases** (DeepSeek-V3), which avoids competing with the language-modeling objective. Most designs keep **1 shared expert always-on + N routed experts**. Frontier scale is *ultra-sparse*: **Mixtral** (8 experts, top-2), **DeepSeek-V3** (671B total / 37B active, sparsity 32), **Kimi K2** (1.04T / 32B active, sparsity 48). The EM takeaway: **MoE buys more parameters without more per-token FLOPs — paid for in routing complexity, load-balancing, and all-to-all communication.**

---

## 4. Your anchor: recsys serving + real numbers

- **Two-tower = recsys's KV cache.** The whole reason retrieval is a *two*-tower is to **precompute and index the item side** so you only run the query tower live (guide 01/04). That's the same instinct as caching K/V: don't recompute the static part per request. You've been doing inference-economics-driven architecture for years.
- **UPP GPU serving** shipped and was adopted by Notif and P2P — a concrete "we moved the base model to GPU serving with strong offline results" story about *serving*, not just modeling.
- **Latency budgets are the recsys native constraint:** **overfetch** ratios, **ANN caps**, and the LWS existing *at all* are pure latency-economics — LWS is the cheap stage so you don't run the expensive ranker on thousands of items. The preranking funnel **is** an inference-cost-optimization structure.
- **Real compute econ you can cite:** the dual-distribution preranking trainer costs **~$200 and 16.5 hrs/run** vs **$110 and 9 hrs** for the single-distribution baseline (≈40% of batches zeroed to balance two data streams). You can talk concrete training $/run and the engineering trade behind it — rare for an EM candidate.
- **Feature store (GSS):** UICs are externalized to GSS for **low-latency online feature serving** — the recsys analogue of caching computed state so serving doesn't recompute it. Online/offline feature parity (compute the same features in training and serving) is the classic production trap; name it.

---

## 5. The frontier-lab connection

- **You won't be asked to write a kernel** as an EM — you'll be asked "where do the classifiers sit in the request path, what's the latency budget, and what's the cost." Prefill/decode, KV cache, quantization, distillation, MoE-at-a-sentence: that's the EM floor, and your plan says skim, not derive.
- **Distillation is the through-line to the Integrity seat:** fast input classifiers are distilled students of bigger models — exactly your LWS-from-L2 structure. When they ask "how do you make this cheap enough to run on every request," you say "distill a small student, quantize it, and put it first in the cascade so the expensive model only sees what survives" — and that's *your funnel*.

---

## 6. Interview-portable (90 seconds)

> *"The thing I keep central is that inference is the recurring cost, so the economics drive the architecture. For LLMs the one model I'd lead with is the two-phase workload: prefill is compute-bound and sets time-to-first-token, decode is memory-bandwidth-bound and sets throughput — and decode is slow because every token streams the weights and a growing KV cache, which is why batching and KV-cache reduction like GQA matter and why MoE is attractive, since it grows parameters without growing per-token compute. I've lived the recsys version of all of this: a two-tower retriever is literally caching the item side so you only compute the query side live, the whole preranking cascade exists so you don't run the expensive ranker on thousands of candidates, and the cheap stage is a distilled student of the heavy ranker — which is the same move as a fast distilled safety classifier sitting first in the request path. I can also talk real numbers — our dual-distribution trainer runs about $200 a run versus $110 for the baseline, and the engineering reason for the gap."*

**Likely probes:**
- "Why is decoding slow?" → memory-bound autoregression + growing KV cache; batching/GQA amortize.
- "Make this cheap to serve." → quantize → distill a smaller student → batch → cache → put it first in a cascade.
- "What's MoE and why?" → sparse experts, dense-ish quality at lower active FLOPs (sparsity = total/active); load-balancing is the hard part (aux-loss or DeepSeek's aux-loss-free biases); frontier models (DeepSeek-V3, Kimi K2, Mixtral) are all MoE.
- "TTFT too high." → prefill cost; smaller model / prompt, prefix-cache shared context, more compute.
- "Online/offline feature skew?" → compute the same features both paths or you train on a distribution you can't serve.

---

## 7. Self-test (out loud, from memory)

1. Prefill vs decode — which is compute-bound, which memory-bound, and which metric each sets?
2. What is the KV cache, why does it exist, and what does it constrain? Name one way to shrink it.
3. List the cost levers and what each trades. Which is your first move and why?
4. Why is a retrieval model two-tower? Frame it as an inference-economics decision.
5. What is MoE and why are frontier models adopting it?
6. Explain how LWS/distillation = a fast safety classifier in front of an expensive model.
7. What's online/offline feature skew and why does it bite in production?

*Skim-tier per your study plan. Hoang Ch 15–16, 19, 29 for the LLM side; the anchors are UPP serving + your preranking paper Appendix B.*
