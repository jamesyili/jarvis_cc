---
concept: Generative AI Platform Design
tags: [genai, llm-platform, guardrails, orchestration]
sources:
  - kb/hard/raw/chip-huyen/building-a-generative-ai-platform.md
  - kb/hard/raw/chip-huyen/common-pitfalls-when-building-generative-ai-applications.md
  - kb/hard/raw/chip-huyen/open-challenges-in-llm-research.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/large-language-models|Large Language Models]]"
  - "[[hard/wiki/retrieval-augmented-generation|Retrieval-Augmented Generation]]"
  - "[[hard/wiki/llm-patterns|LLM Patterns]]"
understanding: 2  # basic understanding (assumed where James's background applies)
relevance: 2  # somewhat / potentially relevant
knowledge_updated: 2026-09-07
---

# Generative AI Platform Design

A generative AI platform is the infrastructure layer that turns a raw model API call into a production-grade application. The simplest form: receive query, send to model, return response. The production form: context construction, guardrails, model routing, caching, complex logic, write actions, observability, and orchestration — all layered progressively as application needs grow.

Platform design is additive. Start minimal, add components as failure modes emerge. A component can be skipped if the system works without it. But evaluation is necessary at every step.

## Step 1: Enhance Context (Context Construction)

The most common first expansion. Many queries need additional information to answer correctly — product specs, user history, internal documentation, real-time data. Providing this context dramatically reduces hallucination and improves specificity.

Context construction for foundation models is analogous to feature engineering for classical ML — giving the model the information it needs to process an input correctly.

**RAG (Retrieval-Augmented Generation):** The dominant pattern. A retriever fetches relevant chunks from external sources; these chunks augment the prompt. Term-based retrieval (BM25, Elasticsearch) is fast and cheap, works well out of the box. Embedding-based retrieval (vector search, ANN) handles semantic similarity but requires embedding infrastructure. Hybrid search combines both — term-based for initial candidates, vector search for semantic re-ranking. See [[hard/wiki/retrieval-augmented-generation|Retrieval-Augmented Generation]] for full treatment.

**RAG with structured data:** External data can be tabular. Text-to-SQL converts natural language queries to SQL, executes against the database, and uses results as context. Requires an intermediate step to identify relevant tables when many schemas are available.

**Query rewriting:** User queries are often ambiguous or context-dependent. A preprocessing step rewrites queries — resolving coreference, adding context — before retrieval. Critical for multi-turn conversations where the most recent message only makes sense in prior context.

**Agentic context construction:** Web search, internal API calls, SQL execution, and other retrieval actions become tool calls in an agentic workflow. The model decides dynamically what information it needs. Each tool is a read-only action that augments context. See [[hard/wiki/ai-agents-and-agentic-systems|AI Agents & Agentic Systems]].

## Step 2: Guardrails

Guardrails protect users and developers from AI failures. Add them wherever potential failures exist. Two categories:

**Input guardrails:**
- *PII/sensitive data detection:* Prevent employees from inadvertently sending proprietary information to external APIs (the Samsung ChatGPT incident is the canonical example). Detect and mask — or block — sensitive content. A reversible PII dictionary allows masking at input and unmasking at output.
- *Jailbreak/prompt injection prevention:* Filter inputs containing restricted topics, anomalous patterns, or phrases associated with adversarial behavior. Intent classifiers can identify out-of-scope requests.

**Output guardrails:**
- *Format validation:* Detect and retry on malformed JSON, invalid code, or missing required fields. Constrained sampling (outlines, guidance, instructor) prevents format failures at generation time.
- *Toxicity detection:* Identify racist, sexist, or otherwise harmful outputs.
- *Hallucination detection:* Check whether claims in the response are grounded in the provided context. SelfCheckGPT (sampling-based consistency check) and SAFE (search-engine factuality evaluation) are active approaches.
- *Sensitive information in outputs:* Even correctly formatted responses can leak sensitive data retrieved from internal sources.
- *Brand safety:* Monitor for responses that mischaracterize the company or competitors.
- *Quality scoring (AI judges):* General-purpose LLMs or specialized scorers evaluate response quality. Should be validated against human judgments.

**Failure management:** AI models are probabilistic — a bad response on retry may succeed. Basic retry logic addresses many failure modes. Parallel requests (send the same query twice simultaneously, return the better response) reduce latency at the cost of double API calls. Streaming mode conflicts with output guardrails — you can't evaluate a partial response.

**Tradeoffs:** Guardrails add latency and cost. Some teams skip them when latency is paramount. Most find that the risk cost outweighs the latency cost. Self-hosting eliminates the need for input PII guardrails (no data leaves the organization) but requires implementing all output guardrails internally.

## Step 3: Model Router and Gateway

**Router:** Routes queries to different models or handlers based on predicted intent. Benefits:
- *Specialization:* Route billing queries to a billing-specialized model, technical queries to a technical model.
- *Cost optimization:* Route simple queries to cheap models; reserve expensive models for complex ones.
- *Out-of-scope handling:* Classify irrelevant queries and return stock responses without wasting an API call.

An intent classifier powers routing. It can be a general-purpose LLM or a specialized small classification model — the latter is much faster and cheaper, adding minimal latency. A next-action predictor can also help agents decide what to do next (ask for clarification vs. execute).

**Gateway:** A centralized layer that abstracts access to multiple model APIs (OpenAI, Google, Anthropic, self-hosted) behind a unified interface. Core functions:
- *Unified interface:* Application code calls one endpoint regardless of underlying model.
- *Access control:* Single point for API key management, preventing token leakage.
- *Cost management:* Monitor and limit API call volumes by user or application.
- *Fallback policies:* Route to backup models on rate limit or API failure.
- *Logging and analytics:* Centralize request/response logging.

Off-the-shelf gateways: Portkey, MLflow AI Gateway, Kong AI Gateway, Cloudflare AI Gateway.

## Step 4: Caching

Caching reduces latency and cost. Three techniques:

**Prompt cache:** Cache processed prefixes (especially system prompts shared across queries). Without caching, the system prompt is processed with every query. With caching, only the first query pays that cost. For 1000-token system prompts at 1M daily API calls, prompt caching saves ~1 billion redundant input tokens per day. Gemini offers context caching at 75% token discount.

**Exact cache:** Cache generated responses for processed items (summaries, SQL query results, retrieved chunks). Implement with Redis or in-memory storage. Requires an eviction policy (LRU, LFU, FIFO). Only makes sense for queries likely to be repeated — user-specific or time-sensitive queries should not be cached.

**Semantic cache:** Cache responses and retrieve them for semantically similar (not identical) queries. "What's the capital of Vietnam?" and "What's the capital city of Vietnam?" should return the same cached answer. Implementation: embed each query, store with its response; for new queries, find closest cached embedding; return cached result if similarity exceeds threshold. Critical caveat: semantic cache is prone to failure — bad embeddings, wrong similarity thresholds, or mistaken matches all cause incorrect responses to be returned. Evaluate carefully before deploying.

## Step 5: Complex Logic and Write Actions

**Complex logic:** Model outputs can conditionally feed into other models, trigger different workflows, or loop back as inputs. Planning and self-correction patterns create these iterative flows. The output is returned to context construction, which feeds back to the model gateway.

**Write actions:** Actions that modify external state — send email, insert database record, execute API call, merge code. Write actions make agents vastly more capable. They also make failures vastly more consequential. Mitigations:
- Require explicit human approval before irreversible write actions
- Apply principle of least privilege — minimum write access required
- Guard against prompt injection (malicious content hijacking write actions)
- Define and enforce which actions can execute automatically vs. which require human confirmation

## Observability

Observability must be built in from the start, not added later. Three pillars:

**Metrics:** System metrics (throughput, memory, hardware utilization, uptime) plus model metrics (accuracy, toxicity, hallucination rate). Latency metrics matter most for user experience:
- Time to First Token (TTFT)
- Time Between Tokens (TBT)
- Tokens Per Second (TPS)
- Total Latency

Track cost metrics: query volume, input/output token counts, cost per query. Break down all metrics by user, release, prompt version, and query type.

**Logs:** Log everything — configurations, queries, outputs, intermediate states, component timing, failures. Structured logs with tags and IDs enabling attribution to specific pipeline stages. Manual inspection of production data (even 15 minutes/day) consistently reveals insights that automated analysis misses.

**Traces:** End-to-end recording of a request's path through system components — which documents were retrieved, what prompt was assembled, how long each step took, what the final response was. LangSmith, Weave, and similar tools provide trace visualization.

## Common Pitfalls

**Use GenAI when you don't need it:** Not every problem needs an LLM. Before building a GenAI solution, ask whether a simpler approach (linear programming, rule-based logic, a standard ML model) achieves the same goal more reliably.

**Confuse bad product with bad AI:** Poor user experience is often a product design problem, not a model problem. Users may want action items from meeting transcripts, not summaries. They may want helpful (not just correct) responses. They may need suggested prompts rather than a blank text box.

**Start too complex:** Don't use an agentic framework when direct API calls work. Don't insist on fine-tuning when prompting works. Don't implement semantic caching before proving it's needed. Abstractions obscure bugs; frameworks update their default prompts without warning. Start minimal.

**Over-index on early success:** The 0→80% journey is typically fast. The 80→95% journey takes as long again. Hallucination at the margins, tool-calling reliability, tonal consistency, edge case handling — these dominate production engineering time. LinkedIn: 1 month to 80%, 4 additional months to 95%.

**Forgo human evaluation:** AI judges are useful but must be validated against human judgments. Daily human review of 30–1000 examples provides ground truth, catches judge drift, and surfaces user behavior patterns that automated systems miss.

**Crowdsource use cases without strategy:** Individual contributors suggest use cases relevant to their day-to-day work, not highest-ROI applications. Without an overarching strategy, teams end up with a proliferation of low-impact apps that together produce no meaningful return.

## Open Challenges

The hardest unsolved problems in production LLM systems:

**Hallucination:** The #1 barrier to enterprise adoption. Measurement remains unsolved — there is no definitive hallucination metric. Mitigation via RAG, chain-of-thought, self-consistency helps but doesn't eliminate.

**Context optimization:** "Lost in the Middle" shows models attend poorly to content in the middle of long contexts. More context is not always better. Efficient context construction — including only what's needed, ordering it well — is as important as context length.

**Latency/accuracy tradeoff:** More planning, self-correction, and parallel execution improves accuracy but increases latency and cost. Production systems must tune this tradeoff per application.

**Reliability of API providers:** 10% timeout rates are reported in production. Model behavior changes when providers update underlying models. Building robust retry, fallback, and version-pinning strategies is essential but tedious.

## Sources

- Chip Huyen. *Building a Generative AI Platform* — complete platform architecture, context construction, guardrail types, router/gateway, caching, write actions, observability
- Chip Huyen. *Common Pitfalls When Building Generative AI Applications* — use case selection, complexity, human evaluation, the 0→80→95% curve
- Chip Huyen. *Open Challenges in LLM Research* — hallucination, context optimization, multimodality, cost/latency trends
