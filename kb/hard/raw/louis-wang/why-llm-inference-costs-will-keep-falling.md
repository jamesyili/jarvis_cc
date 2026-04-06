# Why LLM Inference Costs Will Keep Falling

**Source:** https://louiswang524.github.io/blog/inference-cost-trends/
**Ingested:** 2026-04-05
**Tags:** llms, recsys, ai-agents, ml-systems, inference

---

[Home](/) › [Blog](/blog) › Why LLM Inference Costs Will Keep Falling  
Why LLM Inference Costs Will Keep Falling
 
 March 1, 2026 · 3 min read  · [LLM](/tags/LLM)[infrastructure](/tags/infrastructure)[economics](/tags/economics) 
  
The cost to run a large language model has dropped by roughly 100× over the past two years. This post explores why that trend is likely to continue — and what it means for how we build AI systems.

[The Three Drivers](#the-three-drivers)

LLM inference costs are shaped by three independent forces: hardware efficiency, algorithmic improvements, and market competition. All three are moving in the same direction.

[Hardware: Moore’s Law Is Not Dead (For This Workload)](#hardware-moores-law-is-not-dead-for-this-workload)

GPUs designed for inference are improving faster than general-purpose compute. The H100 delivers roughly 4× the throughput of an A100 on transformer workloads, not because of raw FLOPS, but because of architectural improvements purpose-built for matrix multiplications and attention.

The next generation of inference accelerators — from NVIDIA, Google (TPUs), Groq, and others — are designed from the ground up to maximize tokens-per-second per dollar. Custom memory architectures reduce the memory bandwidth bottleneck that has historically limited throughput.

[Algorithms: Doing More With Less](#algorithms-doing-more-with-less)

The algorithmic side has been equally impactful:

**Quantization**: Running models at INT4/INT8 precision instead of FP16 cuts memory and compute by 2-4×, with minimal quality loss on most tasks.

**Speculative decoding**: Using a small draft model to propose tokens that the large model validates in parallel can achieve near-2× speedups.

**KV cache compression**: Techniques like PagedAttention (used in vLLM) improve GPU utilization from ~20% to >50% on real workloads.

**Mixture of Experts (MoE)**: Models like Mixtral route tokens to specialized sub-networks, reducing compute per token while maintaining model capacity.

Each technique compounds with the others.

[Market Structure: The Commoditization Effect](#market-structure-the-commoditization-effect)

Open-source models have fundamentally changed the pricing dynamics. When Llama 3 70B can be self-hosted for ~$0.20 per million tokens, proprietary API providers face a ceiling on how much they can charge for equivalent capability.

This creates a ratchet: open-source models improve → API prices drop → more adoption → more investment in inference infrastructure → better open-source models.

[What This Means for System Design](#what-this-means-for-system-design)

If you’re building LLM-powered systems today, cheap inference changes the design space significantly:

**Sampling over caching**: When API calls are cheap, it’s often better to generate fresh responses than maintain complex prompt caches.

**Ensemble methods become viable**: Running the same query through multiple models and combining results is no longer prohibitively expensive.

**Iteration speed matters more than optimization**: Spending engineering time on prompt optimization returns less value when the underlying cost is already low.

[The Long-Term Trajectory](#the-long-term-trajectory)

Extrapolating current trends, running a GPT-4-class model will cost roughly the same as running a search query within 3-5 years. At that point, the economics of AI integration change fundamentally — not because models are smarter, but because the marginal cost of intelligence approaches zero.

The interesting question isn’t whether this will happen, but which applications become viable at what price points along the way.
   
  
 
 [ Next → From Vibe Coding to Harness Engineering: How to Actually Ship AI-Assisted Software ](/blog/vibe-coding-to-harness-engineering)
