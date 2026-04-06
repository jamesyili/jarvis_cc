---
concept: Generative AI Platform Design
tags: [genai, llm-platform, guardrails, model-serving, orchestration, ai-strategy]
sources:
  - kb/hard/raw/chip-huyen/building-a-generative-ai-platform.md
  - kb/hard/raw/chip-huyen/common-pitfalls-when-building-generative-ai-applications.md
  - kb/hard/raw/chip-huyen/generative-ai-strategy.md
  - kb/hard/raw/chip-huyen/open-challenges-in-llm-research.md
  - kb/hard/raw/eugene-yan/what-weve-learned-from-a-year-of-building-with-llms.md
  - kb/hard/raw/eugene-yan/patterns-for-building-llm-based-systems-products.md
  - kb/hard/raw/jay-alammar/generative-ai-and-ai-product-moats.md
last_compiled: 2026-04-05
related:
  - hard/wiki/large-language-models
  - hard/wiki/retrieval-augmented-generation
  - hard/wiki/ai-agents-and-agentic-systems
  - hard/wiki/llm-evaluation
---

# Generative AI Platform Design

## What It Is

A generative AI platform is the infrastructure layer that sits between raw model APIs and production user-facing applications. It is not a single component but a progressively assembled stack: context construction, guardrails, model routing, caching, complex orchestration, and observability. The right approach is to start minimal and add layers only as real needs emerge — premature complexity is one of the most common failure modes.

---

## Platform Architecture: The Five-Layer Stack

### 1. Context Construction (RAG and Beyond)

The first expansion beyond a bare model call is giving the model access to external information. Context construction is to GenAI what feature engineering is to classical ML — it determines what the model knows at inference time.

**Retrieval-Augmented Generation ([[hard/wiki/retrieval-augmented-generation|RAG]])** is the dominant pattern. Documents are chunked, embedded, and stored in a vector index. At query time, the system retrieves the most relevant chunks and injects them into the prompt. Two core retrieval strategies:

- **Term-based retrieval** (BM25, Elasticsearch): fast, cheap, no GPU, good baseline.
- **Embedding-based retrieval** (ANN via FAISS, ScaNN, HNSW): semantically richer but compute-intensive. Key trade-offs: recall, QPS, build time, and index size.

Production systems typically combine both in **hybrid search**: term-based retrieval as a fast first-pass, embedding-based re-ranking as a precision filter. This mirrors the candidate generation → ranking pipeline familiar from [[hard/wiki/recommendation-systems|recommendation systems]].

For structured data, the pattern is **text-to-SQL**: model reads table schemas, generates a SQL query, executes it, then generates a final response. When context sources span multiple external systems (web search, databases, APIs), the architecture becomes **agentic RAG** — the model selects which retrieval action to take as part of its reasoning loop.

**Query rewriting** is a lightweight but high-leverage step: a small model rewrites the raw user query to make it self-contained and retrieval-friendly before it hits the retrieval layer.

**"Lost in the Middle"**: models process documents at the beginning and end of context better than in the middle. Retrieval ordering matters.

### 2. Guardrails

Guardrails protect both users and the platform operator. They sit at two points: input and output.

**Input guardrails:**
- **PII detection and masking**: intercept sensitive data before it leaves your org to a third-party API. Use a reversible placeholder dictionary to unmask in the returned response.
- **Jailbreak and topic filtering**: classify inputs against a set of restricted topics or anomaly patterns. Out-of-scope detection also saves API costs by deflecting low-value queries.

**Output guardrails:**
- **Format validation**: regex, JSON schema validators, constrained decoding (guidance, outlines, instructor).
- **Toxicity and brand-risk detection**: off-the-shelf classifiers or keyword monitors.
- **Hallucination detection**: active research area; tools like SelfCheckGPT offer signal. Primary mitigation is providing sufficient context (RAG) plus chain-of-thought prompting.
- **Sensitivity filters**: prevent retrieval-augmented systems from leaking retrieved private data into responses.

**Failure management policy:** for failures, use retry logic with parallel calls (send 2 requests simultaneously, return the better one) to contain latency. Fall back to human operators for edge cases or high-stakes interactions. Some teams route to humans when sentiment analysis detects user frustration.

**Core tradeoff:** guardrails add latency. Most teams find the risk reduction worth it. Streaming mode creates a specific tension — unsafe tokens may reach the user before output guardrails can evaluate the full response.

### 3. Model Router and Gateway

**Router:** an intent classifier that directs queries to the best-suited model or solution path. Benefits: specialized models can outperform general-purpose ones on narrow tasks; simpler queries can be routed to cheaper models. The router also handles context window management — if a retrieval action bloats context beyond the intended model's limit, route to a larger-context model.

**Gateway:** a unified API wrapper over all model endpoints (OpenAI, Anthropic, self-hosted). Core functions:
- **Access control**: centralized credentials, fine-grained per-application permissions.
- **Cost management**: usage monitoring, rate-limit enforcement.
- **Fallback policies**: if the primary API is unavailable, route to a backup model or retry after backoff.
- **Logging and analytics**: the gateway is already in the critical path, so it is a natural place to instrument.

The gateway and router models are typically small and fast (classification models rather than generation models) to avoid adding meaningful latency.

### 4. Caching

Cache is the most underrated cost and latency lever in a GenAI platform. Three distinct strategies:

| Cache Type | What It Does | When to Use |
|---|---|---|
| **Prompt cache** | Reuses computation for shared prefix text (e.g. system prompt) | Always — large system prompts, repeated long documents |
| **Exact cache** | Stores and returns results for identical queries | High-repeat query patterns (FAQs, common searches) |
| **Semantic cache** | Stores results and matches similar (not identical) queries via embedding similarity | Use cautiously — false similarity matches return wrong answers |

Prompt cache is the most reliable and impactful: a 1,000-token system prompt with 1M daily API calls means ~1B tokens of avoidable computation per day. Major providers (Gemini) now offer discounted pricing for cached input tokens.

Semantic cache is fragile. It depends on embedding quality, vector search correctness, and a well-calibrated similarity threshold. Only use it when cache hit rates are demonstrably high.

Cache eviction policies (LRU, LFU, FIFO) are necessary to manage cache size in exact caches. User-specific or time-sensitive queries should not be cached.

### 5. Complex Logic and Write Actions

Simple pipelines return model output directly. Complex pipelines add conditional branching, loops (feed model output back as input), and multi-step planning (model decides what action to take next, executes it, evaluates, continues).

**Write actions** — sending emails, updating databases, placing orders — make a system dramatically more capable but dramatically riskier. Prompt injection attacks (equivalent to social engineering aimed at the model) become a live threat when the model has write access to systems. Mitigation: require human approval for high-impact write operations; implement defense-in-depth at the application layer, not just in the model prompt.

---

## Observability: Logs, Traces, Metrics

Observability is not an afterthought — instrument from day one. Three pillars:

**Metrics:** track model performance (accuracy, toxicity, hallucination rate), system health (throughput, latency, memory), and cost drivers (input/output token volume, API call rate). For latency specifically: Time to First Token (TTFT) is the UX-critical signal; Total Latency covers the full response. For [[hard/wiki/retrieval-augmented-generation|RAG]] pipelines, track context relevance and precision separately from generation quality.

**Logs:** log everything — query, intermediate outputs, final response, component start/stop, failures. Tag logs with IDs that can be traced back to a specific pipeline component. Manual daily review of production data (even 15 minutes) consistently surfaces insights that automated analysis misses.

**Traces:** record the full execution path of a request — what actions were taken, what was retrieved, what prompt was assembled, how long each step took. Traces enable root-cause diagnosis when a response fails: was it bad retrieval, bad context construction, or bad generation?

---

## Orchestration

An orchestrator chains components — models, retrievers, databases, tools — into an end-to-end pipeline. It handles data passing between steps and schema validation across step boundaries.

**Key evaluation criteria for orchestration tools:**
1. **Integration breadth**: does it support your model providers and databases?
2. **Complex pipeline support**: branching, parallel execution, error handling.
3. **Performance**: no hidden API calls or added latency.

**The main risk of orchestrators:** they abstract away critical details. If a framework silently updates its default prompts, your system behavior changes without warning. Start without an orchestrator. Add one when the complexity demands it and you already understand the system deeply.

Parallelism is a first-class optimization: independent steps (PII filtering + intent routing, for example) should run concurrently to minimize wall-clock latency.

---

## Build vs. Buy

The gateway, scoring models, and many guardrail components are commodity. Open-source options (LangChain, LlamaIndex, Portkey, Kong AI Gateway) cover most needs. The real differentiation is not in the infrastructure — it is in data, fine-tuned behavior, and product design. Because everyone uses the same foundation models, the platform components increasingly converge. **Moat lives in proprietary data, user behavioral signals, and the quality of the product layer built on top.**

---

## AI Product Moats

When foundation models are accessible to everyone, the defensible advantages are:

1. **Proprietary data**: training data, fine-tuning data, user interaction logs that competitors cannot access.
2. **Behavioral signals**: user feedback loops that continuously improve model behavior for your specific use case.
3. **Distribution and workflow integration**: deep embedding in user workflows that creates switching costs independent of model quality.
4. **Evaluation infrastructure**: teams that build rigorous [[hard/wiki/llm-evaluation|evaluation]] pipelines move faster and improve more reliably than teams that don't. Evaluation is itself a moat.

---

## Common Pitfalls

These failures are well-documented across production teams:

**1. Using GenAI when you don't need it.** Many problems are better solved by simpler, cheaper methods (linear programming, rule-based systems, classical ML). GenAI should be chosen because it is the right tool, not because it is new.

**2. Confusing bad product with bad AI.** AI is often the easy part. UX is hard. Teams that fail with GenAI frequently fail at product — wrong interface design, poor workflow integration, missing human-in-the-loop. Intuit improved chatbot satisfaction not by changing the model but by adding suggested questions to reduce blank-page friction.

**3. Starting too complex.** Do not reach for agentic frameworks, vector databases, or fine-tuning before validating that simpler approaches are insufficient. Abstractions hide bugs and slow debugging. Term-based retrieval before embedding search. Direct API calls before orchestration frameworks.

**4. Over-indexing on early success.** The demo → production gap is severe. Getting from 0% to 80% takes roughly as long as getting from 80% to 95%. The last 5% can dominate the total engineering investment. Plan for it. Reliability (provider timeouts, silent model updates), compliance, and safety surface as the system scales.

**5. Forgoing human evaluation.** AI-as-a-judge is useful but not sufficient. Best-performing teams have daily human review of 30–1,000 output samples. Human evaluation catches distribution drift that automated judges miss, and it calibrates whether the AI judge itself has drifted.

**6. Crowdsourcing use cases without a strategy.** Individual contributors surface problems affecting their own workflows. Without executive strategy that filters for ROI, you end up with a portfolio of low-impact tools. Strategy precedes execution.

---

## Open Challenges

- **Hallucination**: still the #1 production blocker. RAG mitigates it but does not eliminate it. Detection (SelfCheckGPT, SAFE) is improving but remains imprecise.
- **Context efficiency**: longer context windows do not automatically improve performance. Context position matters ("Lost in the Middle"). Active research into better context construction and ordering.
- **Latency and cost**: quantization (4-bit, 8-bit), knowledge distillation, and pruning are mature techniques for self-hosted models. Prompt caching and model routing are the primary levers for API-based deployment.
- **Agent reliability**: [[hard/wiki/ai-agents-and-agentic-systems|Agentic systems]] that plan and act across multi-step tasks remain unreliable at production scale. Tool-calling accuracy, latency/accuracy tradeoffs, and safe write-action handling are open problems.
- **Human preference alignment**: RLHF is effective but labeler demographics create bias. Whose preferences are being learned? This is as much a policy problem as a technical one.

---

## Key Principles

- **Add components incrementally.** Start with the simplest working system. Measure. Add layers only when a real bottleneck justifies the complexity cost.
- **Instrument from day one.** Observability retrofitted later is always incomplete. Logs, traces, and metrics belong in the initial design.
- **Keep humans in the loop.** Daily manual review of production outputs is among the highest-leverage activities in GenAI product development.
- **The platform is not the moat.** Infrastructure converges to commodity. Differentiation comes from data, evaluation rigor, and product quality.
