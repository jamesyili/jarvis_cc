---
concept: Open Model Ecosystem
tags: [open-models, llm-ecosystem, governance, deepseek, qwen]
sources:
  - kb/hard/raw/nathan-lambert/8-plots-that-explain-the-state-of-open-models.md
  - kb/hard/raw/nathan-lambert/what-comes-next-with-open-models.md
  - kb/hard/raw/nathan-lambert/open-models-in-perpetual-catch-up.md
  - kb/hard/raw/sebastian-raschka/the-state-of-llms-2025-progress-problems-and-predictions.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/genai-product-strategy|GenAI Product Strategy]]"
  - "[[hard/wiki/large-language-models|Large Language Models]]"
understanding: 1  # very little exposure / unknown (default)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Open Model Ecosystem

The open-weight LLM ecosystem entered 2026 in a paradoxical state: technically impressive, adoption-concentrated, geopolitically contested, and strategically confused. Chinese labs — primarily Alibaba's Qwen and ByteDance's DeepSeek — dominate by every adoption metric. Western open models are failing to keep pace. And the fundamental question of why companies should build open models remains largely unanswered by most participants.

## The State of Adoption: China's Dominant Lead

The adoption data from Nathan Lambert's ATOM Project tracking (1,152+ models, post-ChatGPT releases) is unambiguous. As of late 2025/early 2026:

**Qwen has effectively won the open-weight ecosystem.** In December 2025, Qwen got more downloads than every other tracked organization combined — including DeepSeek, Meta (Llama), Mistral, Google, OpenAI, and all others. The top 5 Qwen3 models in a single month outperformed the combined downloads of OpenAI, Mistral, Nvidia, Z.ai, Moonshot AI, and MiniMax. This is a gap that will "take year(s) to unwind."

**DeepSeek's large models are its one area of strength over Qwen.** DeepSeek V3, R1, and their variants dominate large MoE model adoption — these 4 models outperform all of Qwen's large models. This is strategically significant because large models are the foundation for the startups building fine-tuned applications (Cursor's Composer is fine-tuned from a large Chinese MoE).

**Llama is still the most downloaded Western model** despite Meta not releasing updates. This is the state of Western open-model production: the most-used model is an unmaintained legacy release. OpenAI's GPT-OSS models are the only new Western entrant showing meaningful download momentum — roughly equal to all of DeepSeek or all of Mistral per month.

**New entrants (Z.ai, MiniMax, Kimi Moonshot) barely register.** Despite substantial press coverage, their adoption looks like a rounding error compared to Qwen and DeepSeek. These models matter for developing local ecosystems and pushing the frontier technically, but they do not compete with Qwen as the open model default.

**Fine-tune concentration**: Qwen's dominance extends to derivative models. The share of HuggingFace fine-tunes based on Qwen has grown throughout 2025. Only five organizations account for the vast majority of base models being fine-tuned: Qwen, Llama, Mistral, Google (Gemma), and DeepSeek.

## The Perpetual Catch-Up Dynamic

The open-closed gap has held remarkably stable at **6–18 months** behind frontier closed models for years. This is both a testament to open labs (operating on far smaller budgets) and a ceiling that they consistently cannot break through.

Several factors maintain this gap:

**Distillation is becoming less effective**: Previously, open labs could copy performance from closed models by distilling their completions. With the rise of RL-based post-training (RLVR/GRPO), the most important components — RL environments, complex prompts, and reward signals — are much easier to hide than text completions. You can't distill a reasoning trace if you can't observe the training environment that produced it.

**Benchmarking inflation ("benchmaxxing")**: Open models face pressure to perform on public benchmarks, which can be optimized for directly (intentionally or via data contamination). Qwen's flagship v3.5 model was repeatedly flagged for "benchmaxxing." Raschka observes that benchmark scores are now necessary thresholds but no longer sufficient signals: above-threshold performance no longer indicates relative superiority. The frontier of capability increasingly lives in domains that public benchmarks cannot capture.

**Compute constraints**: Chinese labs with the best open models constantly cite computational restrictions. The top American labs have vast compute advantages, and the gap in training FLOPs is not reflected in the 6-month capability gap only because open labs are extremely efficient with what they have.

**Domain specialization**: As frontier models move into legal, medical, and enterprise domains where data is not publicly available, open labs cannot replicate the training data. The performance gap is likely to grow for these specialized, high-value capabilities even while general benchmarks remain close.

**The scaling log-linear relationship**: The fact that the gap isn't larger may simply reflect diminishing returns on raw compute — a log-linear relationship between compute and performance means that large compute advantages translate into smaller capability gaps than intuition suggests.

## What Drives Open Model Success

The factors that determined whether any specific open model achieved meaningful adoption:

**Quality at time of release is necessary but not sufficient.** Many high-quality models achieved minimal adoption. The ecosystem is winner-take-most: only the top few models get any adoption, and "the likelihood for most models to even get tried once goes down month over month."

**Model stickiness**: Once a model achieves adoption, it's sticky — many deployments are set up once and never changed if performance is adequate. This creates a flywheel advantage for early leaders (Qwen) that is very hard to disrupt.

**Ecosystem depth**: Qwen's advantage isn't just the models — it's the ecosystem. Extensive documentation, tooling, downstream community, and fine-tune recipes compound over time. A new model with better raw benchmarks cannot displace an embedded ecosystem quickly.

**Size range coverage**: Qwen's dominance spans from 0.6B to large MoE models. For different deployment contexts (edge device → local server → cloud), having the best model at multiple size points is far more valuable than a single flagship.

**DeepSeek's open-source strategy**: DeepSeek's willingness to publish detailed technical papers (V3, R1) alongside model weights was a strategic choice that built enormous credibility and community engagement. The R1 paper's RLVR recipe was arguably as influential as the model weights themselves.

## Business Strategies for Open Models

Nathan Lambert's analysis of the business landscape for open models is frank: "Very few businesses have a real monetary reason to build open models."

**The Google Android analogy**: Google open-sourced Android not for altruism but to eliminate a layer between users and Google Search. Open-source was a defensive moat — "scorching the earth for 250 miles" around the search business. AI hasn't produced a clear analog: no company has a profit center so dominant that it can afford to commoditize the model layer as a defensive play.

**Nvidia's case**: The one clear business reason to build open models — selling more GPUs. Nvidia benefits when developers adopt open models and need GPU infrastructure to run them. Understanding what developers need helps Nvidia build the right hardware.

**The "model as product" assumption is softening**: As coding interfaces (Claude Code, OpenAI Codex, Cursor) become the dominant way to use frontier AI, the model weights themselves matter less than the integrated product. This could create incentives for more openness at the model layer while closing the product layer.

**Chinese labs**: Operate under different incentive structures — national strategic goals, academic institution ties, and an ecosystem of companies building on each other's work. The "intentional sharing" dynamic among Chinese labs, including public technical papers and coordinated experimentation, enables faster convergence on new standards.

## Three Classes of Open Models (Forward View)

Lambert's taxonomy of where open models are headed:

**True closed frontier models**: Will handle the most demanding knowledge work and coding agents. Closed labs have vertical integration advantages (chips → inference → weights → tools → UI) that open models cannot replicate.

**Open frontier models**: Best open-weight large models competing on similar directions. Will be "close enough" for a large portion of valuable use cases. The models around GPT-OSS 120B and MiniMax M2.5 represent this tier.

**Small, specialized open models as distributed intelligence**: The most underexplored and arguably highest-ROI opportunity. Specific models deployed with multiple LoRA adapters for specific enterprise tasks — "almost brain-numbingly boring and specific." These should handle repetitive sub-tasks in agentic systems at 10x speed and 100x lower cost than frontier models. Current open small models are "marketed on general-task benchmarks" rather than optimized for this use case. Qwen small variants are the current best option, but purpose-built specialized models barely exist.

Raschka's framing aligns: private, domain-specific data (medical records, legal documents, financial transactions) is the frontier that neither scaling nor public-web fine-tuning can reach. Domain specialization + privacy = the case for small, specialized open models deployed on-premises.

## Governance and Licensing

The governance landscape for open models is contested:

**"Open-weight" is not the same as "open-source"**: Most "open" models release weights but not training data, code, or recipes. True open source (OLMo, the Ai2 family) is rare and resource-constrained.

**License restrictions**: Many models labeled "open" have licensing restrictions on commercial use, fine-tuning, or redistribution. Meta's Llama license, for example, prohibits use by companies above a certain scale without a commercial license.

**Sovereign AI**: Nations are turning to open models as the only feasible path to sovereign AI infrastructure. A country cannot build a fully proprietary AI stack from scratch; open models give local AI communities a starting point. Lambert sees sovereign AI as "the real deal" — an increasingly important driver of open model adoption globally.

**Geopolitical concentration**: The shift from US-dominated open models (early Llama era) to Chinese-dominated models (Qwen era) has strategic implications. U.S. export controls and compute restrictions create asymmetries that may accelerate divergence in open model ecosystems between geopolitical blocs.

## The Research Ecosystem Role

Open models have a distinct role in scientific research and global technology diffusion that is separate from the frontier capability race:

**Anchoring scientific work**: When Llama was open SOTA, the global ML community ran experiments on Llama; when Qwen displaced it, Qwen became the research default. Scientific progress built on an open model propagates back to subsequent models in that family. This makes the choice of open SOTA model strategically significant for lab influence.

**Global diffusion**: In nations without access to expensive frontier APIs, open models are the default path to AI adoption. This "melting pot for innovation" operates below the visibility of the US AI discourse, but on a decade timescale it may be more consequential than frontier capability races.

**The 2025 trajectory**: DeepSeek R1's open-source release of the RLVR/GRPO recipe was the single most significant open research contribution of the year. It enabled hundreds of research groups and companies to replicate and extend reasoning-model training. This scientific diffusion effect — not adoption metrics — may be the lasting legacy of DeepSeek R1.

## Sources

- Nathan Lambert, "8 Plots That Explain the State of Open Models" (2026) — `kb/hard/raw/nathan-lambert/8-plots-that-explain-the-state-of-open-models.md`
- Nathan Lambert, "What Comes Next with Open Models" (2025) — `kb/hard/raw/nathan-lambert/what-comes-next-with-open-models.md`
- Nathan Lambert, "Open Models in Perpetual Catch-Up" (2025) — `kb/hard/raw/nathan-lambert/open-models-in-perpetual-catch-up.md`
- Sebastian Raschka, "The State of LLMs 2025: Progress, Problems, and Predictions" (Dec 2025) — `kb/hard/raw/sebastian-raschka/the-state-of-llms-2025-progress-problems-and-predictions.md`
