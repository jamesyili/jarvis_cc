# Multi Agent Ads Customer Support

**Source:** https://aman.ai/h/adsChatbot/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Q & A](#q--a)
  + [**1. System Architecture**](#1-system-architecture)
  + [**2. LLM Engineering**](#2-llm-engineering)
  + [**3. Retrieval & Grounding**](#3-retrieval--grounding)
  + [**4. Evaluation & Metrics**](#4-evaluation--metrics)
  + [**5. Scalability and Failure Modes**](#5-scalability-and-failure-modes)
  + [**6. Prompt Engineering**](#6-prompt-engineering)
  + [**7. Explainability & Trust**](#7-explainability--trust)
  + [**8. Data Engineering & Logging**](#8-data-engineering--logging)
  + [**9. Security & Compliance**](#9-security--compliance)
  + [**10. Tradeoffs & Alternatives**](#10-tradeoffs--alternatives)
* [Break down the multi-agent LLM system **component by component**,](#break-down-the-multi-agent-llm-system-component-by-component)
  + [**1. Planner (Orchestrator) Agent**](#1-planner-orchestrator-agent)
  + [**2. Intent Classification Agent**](#2-intent-classification-agent)
  + [**3. Campaign Context Retrieval Agent**](#3-campaign-context-retrieval-agent)
  + [**4. Auction Diagnostics Agent**](#4-auction-diagnostics-agent)
  + [**5. Policy & Compliance Agent**](#5-policy--compliance-agent)
  + [**6. Response Synthesis Agent**](#6-response-synthesis-agent)
  + [**7. Memory Agent**](#7-memory-agent)
  + [**8. System Monitoring & Observability**](#8-system-monitoring--observability)

**Vision for a Multi-Agent LLM-Based Ads Support System**

**Overview**

This system is designed to provide 24/7 automated support for ad customers. It performs root-cause analysis, handles campaign and billing issues, and escalates unresolved problems to human agents when necessary.

**Primary Capabilities**

* Campaign operations: create, modify, pause, delete
* Auction diagnostics: budget checks, bid strategy analysis
* Performance analysis: impressions, CTR, ROAS
* Billing and policy support
* Root-cause troubleshooting and proactive suggestions

**Why Multi-Agent?**

Using a modular multi-agent architecture allows specialized agents to handle distinct tasks with focused logic and tools. This improves accuracy, modularity, and scalability.

**Core Agents**

* **Campaign Agent**: Manages campaign creation, updates, and lifecycle actions.
* **Auction Agent**: Handles bidding strategy diagnostics and auction insights.
* **Performance Agent**: Answers metric-related queries.
* **Billing & Policy Agent**: Resolves issues related to payments, invoices, and compliance.
* **Orchestrator (Planner) Agent**: Classifies user intent and routes tasks to the right agent.
* **Memory Agent**: Maintains context across sessions (campaign state, user history).

---

**LLM Architecture**

The system is powered by a decoder-only LLM with:

* Multi-turn memory support
* Function-calling capability
* Retrieval-Augmented Generation (RAG) for grounding in campaign data

**Training LLM for Function Calling**

To fine-tune the model (e.g., via LoRA), the training dataset must include clear mappings between user queries and function call invocations.

**Datasets**

1. **Hermes Function Calling**

   * User-query and function-call pairs in JSON or markdown format
   * OpenAI-compatible schema
2. **NousResearch Function Calling**

   * Thousands of structured examples
   * Multi-function prompts with defined tools
3. **Synthetic Data**

   * Programmatically generated with function schemas and prompt templates
   * Custom data fills domain-specific gaps

---

**Function Calling: Input/Output Format**

**Input**

```
{
  "system": "You are an ad support assistant. You help users manage ad campaigns using structured tools.",
  "user": "Why is my campaign not spending money?"
}
```

**Output**

```
{
  "function_call": {
    "name": "diagnose_campaign_budget",
    "arguments": {
      "campaign_id": "camp001"
    }
  }
}
```

Alternate format (OpenAI-style):

```
Thought: The user is asking why their campaign is not spending.
Action: diagnose_campaign_budget
Action Input: {"campaign_id": "camp001"}
```

---

**Dataset Construction**

* **Size**: 5,000–20,000 examples per domain
* **Negative Examples (30%)**:

  + Teach the model when *not* to call functions
* **Multi-Turn Dialogues (20%)**:

  + Show stateful conversations with chained function calls
* **Ambiguous Queries (10%)**:

  + Train clarifying question behavior

**Contrastive Example Pair**

*Positive*:

```
User: Create a campaign with a $100 daily budget in San Francisco.
→ Output: function_call: create_campaign(...)
```

*Negative*:

```
User: Is $100 a good budget for San Francisco?
→ Output: Natural language response, no function call.
```

---

**LoRA Fine-Tuning Tools**

* QLoRA via PEFT + Transformers
* Axolotl, FastChat
* Compatible base models: Mistral 7B, LLaMA 3, GPT-J variants
* Use `bf16` or `fp16`, 8–16 bit models for efficient training

---

**Evaluation Methodology**

To evaluate function-calling models, use **AST (Abstract Syntax Tree)** parsing for semantic correctness.

**Evaluation Dimensions**

1. **Simple Calls**: Match name + args
2. **Sequential Calls**: Ordered matching across dependent calls
3. **Parallel Calls**: Set-wise comparison, order-independent
4. **Parallel Groups**: Match grouped logical chains (e.g., per campaign)

**Metrics**

* Exact Match Accuracy
* Argument-Level F1
* Sequence Accuracy
* Jaccard Index for sets

**Tools**

* `ast.literal_eval`, Pydantic for parsing
* `zss` or DFS tree matching
* `scikit-learn`/`evaluate` for metric calculation

**Error Types**

| Component | False Positive Type |
| --- | --- |
| Intent Classifier | Incorrect intent label |
| Function Calling | Unneeded/wrong function |
| Escalation Logic | Escalates unnecessarily |
| Context Retrieval | Fetches incorrect campaign data |
| Guardrail Filter | Flags valid queries as unsafe |

---

**System Flow**

1. **User Query**: e.g., “Why is my campaign not spending?”
2. **Planner Agent**: Decomposes task
3. **Intent Classifier**: Detects query type (e.g., budget\_diagnosis)
4. **Context Retrieval Agent**: Fetches campaign metadata
5. **Auction Agent**: Analyzes auction logs
6. **Policy Agent**: Checks for holds/violations
7. **Response Agent**: Synthesizes final message

Each agent is stateless, uses JSON for communication, and is orchestrated centrally.

---

**Agent Optimization Strategies**

**Planner Agent**

* Use CoT examples and graph-based reasoning
* Add execution memory and task deduplication
* Reward model training with downstream success labels

**Intent Classifier**

* Fine-tune on labeled query-intent pairs
* Apply multi-label prediction and ensemble voting
* Add hard negatives to reduce false classifications

**Campaign Context Agent**

* Pre-fetch and cache active campaigns
* Resolve ambiguous names with disambiguation prompts
* Align schemas with model vocabulary

**Auction Agent**

* Add diagnostics like market CPM gaps, bid loss reasons
* Use functions like `analyze_pacing_issues()`
* Rule-engine integration for critical spend issues

**Policy Agent**

* Retrieve and embed match latest policies
* Explain violations in plain language
* Connect to live moderation alerts

**Response Agent**

* Tune on style/tone examples
* Combine templates + LLM for consistency
* Auto-ask clarifying questions
* Run A/B tests for quality improvements

---

**System-Wide Enhancements**

* End-to-end feedback collection for supervised fine-tuning
* Unified memory system for persistent context
* Self-diagnosis loops with prompts like “Did I fully resolve this?”
* HITL dashboards for human review + model retraining

---

**Scaling & Performance Planning**

**Query Load (Meta Example)**

* Daily active advertisers: 10M
* Support-seeking daily users: ~200k
* Average user session: 3 queries
* Total: 600k queries/day → 7 QPS avg, 17 QPS peak

**Agent Load Distribution**

If planner routes to 2–3 downstream agents:

* Planner: 10 QPS
* Campaign Retrieval: 7 QPS
* Auction Diagnostics: 6 QPS
* Synthesizer: 10 QPS

Each agent should scale to 10–15 QPS.

---

**Latency Targets**

| Agent | Max Latency |
| --- | --- |
| Planner | <100ms |
| Context Retrieval | <200ms |
| LLM Call | ~500–1000ms |
| Total Roundtrip | <2 seconds |

---

**Serving Infrastructure**

* **LLM Serving**: vLLM + FastAPI with quantized models
* **Autoscaling**: K8s or ECS clusters with zonal distribution
* **Caching**: Redis or memcached for recent queries/context
* **Async Queues**: Kafka/SQS for multi-agent pipelines

---

**Retrieval System**

**Purpose**

Fetch campaign-level, account-level, and policy context:

* Campaign status, budgets, targeting
* Auction diagnostics and pacing
* Performance metrics
* Policy docs and account-level holds

**Architecture**

* **Structured Retrieval**: APIs and DBs (e.g., Presto, Redshift)
* **Unstructured Retrieval**: Vector DB (e.g., FAISS, Pinecone) + semantic embeddings
* **Hybrid Flow**: Structured retrieval first, fallback to semantic RAG

**Example Retrieval Flow**

User: “Why did my NY Holiday Sale campaign stop spending?”

Agents:

1. **Planner** decomposes tasks
2. **Context Agent** gets campaign metadata
3. **Auction Agent** finds low delivery due to tight geo-targeting
4. **Policy Agent** confirms no violations
5. **Response Agent** summarizes findings

**Performance Optimizations**

* Use per-session Redis cache
* Batch requests for high-scale clients
* Disambiguate fuzzy campaign names
* Log all retrieval attempts for traceability

**LLM-Based Ads Support System: Architecture & Implementation**

**1. Visual Architecture Diagram**

A simplified block diagram of the multi-agent LLM system:

```
+----------------------+             +------------------------+
|     User Query       | ----> ---> |    Planner / Router    |
+----------------------+             +------------------------+
                                              |
                                              v
      +-------------+   +-------------------+   +-------------------+
      | Campaign    |   | Auction Diagnostics|   | Policy & Billing |
      | Retrieval   |   | Agent              |   | Agent            |
      +-------------+   +-------------------+   +-------------------+
              |                     |                    |
              v                     v                    v
     [ Structured Retrieval ]   [ Auction Logs ]    [ Policy DB / RAG ]
              |                     |                    |
              +----------+  +-------+---------+----------+
                         |  |                 |
                         v  v                 v
                   +-------------------------------+
                   |  Response Synthesis (LLM)     |
                   +-------------------------------+
                                   |
                                   v
                          +------------------+
                          | Final User Reply |
                          +------------------+
```

**2. Prompt Formats per Agent**

Each agent should be designed around robust prompting + tool-use logic. Examples:

**Campaign Retrieval Agent**

```
Prompt:
"Given the campaign name 'NY Holiday Sale', retrieve campaign_id, targeting, budget, and status."

Tool Call:
fetch_campaign_metadata(name='NY Holiday Sale')
```

**Auction Diagnostics Agent**

```
Prompt:
"Given campaign_id='camp042', identify reasons for delivery drop."

Tool Call:
get_auction_logs(campaign_id='camp042') → analyze_pacing_issues()
```

**Policy Agent (RAG)**

```
Prompt:
"The campaign stopped delivering. Is there a policy violation involved?"

RAG Query:
"Disapproved ad causes for holiday-themed campaigns"
```

**Response Synthesizer Agent**

```
Prompt:
"Based on campaign status, auction logs, and policy check, synthesize a concise explanation for the user."
```

**3. Retrieval Prompt Format for RAG**

Use this unified structure:

```
SYSTEM:
"You are a retrieval agent that queries policy or help center documents to resolve ad account issues."

USER:
"Why is my alcohol ad disapproved?"

RAG QUERY:
"alcohol advertising policy meta ad disapproval"

RAG RETURN:
[doc snippet: "Alcohol ads are restricted to licensed sellers in permitted regions..."]
```

**4. Deployment: Inference Stack Example**

* **LLM Serving**: vLLM or TGI, optimized with QLoRA (4-bit)
* **API Gateway**: FastAPI or ExpressJS
* **Orchestration**: Celery or Dagster for chaining agent calls
* **Caching**: Redis, memcached for user session storage
* **Async Queue**: Kafka or SQS

Example Docker Compose:

```
services:
  llm:
    image: vllm/vllm:latest
    command: --model /models/ads-llm --quantization qlora

  api:
    image: fastapi-app
    ports:
      - "8000:8000"
    depends_on:
      - llm

  redis:
    image: redis:alpine

  orchestrator:
    image: python-agent-pipeline
    environment:
      - QUEUE=kafka
      - CACHE=redis
```

**5. Real-Time Scaling Example on Kubernetes**

Use HPA (Horizontal Pod Autoscaler) config:

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: llm-inference-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: llm-inference
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 60
```

**6. Sample Prompt Tuning Pairs**

**Before**:
“Why isn’t my ad running?”
→ LLM generic reply

**After**:
Few-shot prompt:

```
Q: Why isn’t my ad running?
A:
Thought: The campaign may be paused or restricted.
Action: fetch_campaign_status
Action Input: {"campaign_id": "camp001"}

Q: Why is my CPC increasing suddenly?
A:
Thought: This may be due to auction pressure.
Action: analyze_bid_strategy
Action Input: {"campaign_id": "camp049"}
```

## Q & A

### **1. System Architecture**

**Q1: How would you ensure low-latency and high availability across this multi-agent system under heavy load (e.g., 100 QPS)?**

**A:**

* Use an **async-first architecture**: agents communicate via Kafka/SQS queues to allow non-blocking coordination.
* Each agent is **horizontally scalable** with autoscaling pods in Kubernetes.
* LLM inference is optimized using **quantized models** (e.g., QLoRA, 4-bit) served via vLLM or TGI.
* Add **Redis caching layers** for hot campaign metadata and previous agent results within a session.
* Introduce a **fallback mode**: when LLM response time degrades, agents switch to rule-based templates to maintain uptime.

---

### **2. LLM Engineering**

**Q2: How do you prevent over-triggering of function calls (false positives)?**

**A:**

* Fine-tune with **negative and contrastive examples** where function calling is *not* appropriate.
* Introduce **intent confidence thresholds**: only trigger function calls above a confidence cutoff.
* Use a **classifier + LLM ensemble**: a lightweight model (e.g., DistilBERT) filters calls before invoking the LLM.
* Log and periodically audit **false positives** by comparing AST output to expected outputs.

---

### **3. Retrieval & Grounding**

**Q3: How would you ground the model’s answers in dynamic campaign data while ensuring relevance and freshness?**

**A:**

* Split retrieval into:

  + **Structured** (via internal APIs, SQL queries)
  + **Unstructured** (via RAG over policy and help docs)
* Add **real-time freshness checks** on retrieved structured data.
* Use **semantic matchers** to disambiguate fuzzy user references (e.g., “my Christmas ad” → exact campaign name).
* For RAG: fine-tune the embedding model (e.g., BGE, E5) on domain-specific docs to increase recall precision.

---

### **4. Evaluation & Metrics**

**Q4: How would you evaluate the performance of the system’s function-calling ability?**

**A:**

* Parse model output into an **AST representation**.
* Compare predicted ASTs to gold ASTs using:

  + **Exact Match Accuracy** (function name + full args)
  + **Argument-Level F1** (for partial credit)
  + **Jaccard Index** (for parallel or unordered calls)
* Group errors into taxonomies (wrong function, missing arg, overcall) and track their frequency.

---

### **5. Scalability and Failure Modes**

**Q5: What failure modes do you expect as query volume scales to 100+ QPS, and how would you mitigate them?**

**A:**

* **LLM bottlenecks** → Use quantized models, MoE architectures, and GPU load balancing
* **Cold start latency in agents** → Warm pools with minimum pod replicas per agent
* **Cache thrashing** → Shard Redis cache by user ID or campaign ID
* **Cross-agent race conditions** → Enforce TTL on agent messages and idempotent request processing
* Use **circuit breakers**: fallback to static rules if LLM or retriever is unavailable

---

### **6. Prompt Engineering**

**Q6: How would you design prompts to make agents composable and resistant to hallucination?**

**A:**

* Use a **task description + few-shot examples** per agent:

  + E.g., for the Auction Agent: “Your job is to diagnose under-delivery using auction logs…”
* Standardize **function call schemas** in every example
* Insert **guardrails inside prompts**: e.g., “Only call a function if a specific campaign is referenced.”
* Modularize prompt parts using **LangChain or Jinja templates**

---

### **7. Explainability & Trust**

**Q7: How would you make the system’s responses explainable to users and auditable by engineers?**

**A:**

* Attach a **trace log** to every response with:

  + Invoked agents
  + Function calls made
  + Data sources used
* Show users a simplified explanation: “We checked campaign XYZ and found a low bid issue.”
* Use OpenTelemetry or Datadog to **trace each sub-agent call**
* Build internal dashboards that display AST diffs and hallucination heatmaps

---

### **8. Data Engineering & Logging**

**Q8: What logs or telemetry would you collect to monitor system performance over time?**

**A:**

* **Agent-level logs**: request/response per agent with timestamps and status
* **Function call metadata**: predicted vs. expected ASTs, confidence scores
* **RAG source trace**: document ID, embedding match score, retrieval latency
* **Session logs**: query history, clarifications, escalations
* Use this data to retrain agents on edge cases and detect drift

---

### **9. Security & Compliance**

**Q9: How would you handle PII and security when agents access campaign data?**

**A:**

* Enforce **strict access scopes** per agent; use OAuth tokens per session
* Encrypt all inter-agent payloads (e.g., JSON messages) in transit
* Redact PII before logging or sharing with external systems
* Set up **data lineage** tracking so engineers know what data was used in each LLM output

---

### **10. Tradeoffs & Alternatives**

**Q10: Why use an agentic LLM system instead of a monolithic chatbot? What are the tradeoffs?**

**A:**
**Pros**:

* Easier to reason about and debug per task
* Scalable (each agent can evolve independently)
* Better latency tuning per component
* Lower risk of model overreach or hallucination

**Cons**:

* Higher system complexity and orchestration overhead
* More challenging observability and testing
* Requires robust inter-agent protocol (e.g., consistent JSON message formats)

## Break down the multi-agent LLM system **component by component**,

* For each one, define a set of **deep technical questions** that probe practical understanding of **design, implementation, scaling, observability**, and **failure handling**. For each, I’ll include how a strong answer might be framed.

### **1. Planner (Orchestrator) Agent**

**Role**: Interprets user queries, decomposes tasks, and routes to appropriate agents.

**Interview Questions**:

**Q1: How do you implement task decomposition in the planner?**
*A*: Use prompt-chained reasoning. Provide few-shot examples of complex queries broken into subtasks and routed accordingly. You can encode these as a task DAG (Directed Acyclic Graph) and execute downstream agents asynchronously.

**Q2: How is the planner agent stateless while preserving the ability to coordinate multi-turn workflows?**
*A*: Session state is managed by the Memory Agent. The planner accepts a session token and retrieves context from there. Internally, use a shared state object (e.g., Redis or a context DB) to track delegated tasks and agent completions.

**Q3: How do you prevent redundant delegation (e.g., re-calling the same agent)?**
*A*: Maintain a history log in session state with hashes of agent inputs and responses. The planner checks this before re-issuing a subtask.

---

### **2. Intent Classification Agent**

**Role**: Detects the primary task type from user input.

**Interview Questions**:

**Q1: How do you structure the multi-label classification problem for overlapping intents?**
*A*: Convert intent space into a multi-hot label vector. Use a BERT-style encoder fine-tuned on labeled queries. Output softmax or sigmoid-based multi-label predictions with confidence thresholds.

**Q2: How do you handle intent ambiguity?**
*A*: Train the classifier to return top-`k` candidates. The planner can issue clarification prompts based on overlap or low confidence.

**Q3: How do you incorporate LLMs into the intent pipeline without causing overdependence?**
*A*: Use LLMs for fallback only when intent classifier has confidence < threshold. Otherwise, use fast pre-trained classifiers (e.g., BERT + SVM).

---

### **3. Campaign Context Retrieval Agent**

**Role**: Fetches structured campaign metadata.

**Interview Questions**:

**Q1: What database schema would you use to store campaign metadata for low-latency access?**
*A*: Denormalized schema in a columnar store like BigQuery or Redshift for batch analytics. For low-latency needs, cache hot campaign entries in Redis with TTL based on campaign activity.

**Q2: How would you resolve vague campaign references like “my last holiday sale”?**
*A*: Use a semantic matcher. Precompute embeddings for campaign names/titles and compare with the query vector using cosine similarity via FAISS or a vector DB.

**Q3: How do you cache campaign state effectively in a high-QPS environment?**
*A*: Use a Redis cache with composite keys (`user_id:campaign_id`) and eviction policies like LFU. Invalidate entries when the user makes state-changing updates (pause/edit campaign).

---

### **4. Auction Diagnostics Agent**

**Role**: Performs root-cause analysis using auction logs and bid data.

**Interview Questions**:

**Q1: What kinds of features would you extract from auction logs to diagnose under-delivery?**
*A*: Features like:

* `win_rate`
* `bid_amount vs. market_cpm`
* `audience_overlap`
* `pacing_diff`
* `disapproval flags`

These are analyzed over time windows to detect patterns.

**Q2: How do you safely expose diagnostics to the LLM without leaking sensitive backend mechanics?**
*A*: Use an abstraction layer: LLM invokes `get_auction_diagnostics(campaign_id)`, which internally maps to backend queries and returns sanitized summaries or high-level signals.

**Q3: What rule-based fallbacks would you define?**
*A*: Rules like:

* If `pacing=0` and `bid < market`, suggest “increase bid”
* If `audience overlap = low`, suggest “broaden targeting”

These kick in when LLM or auction logs are unavailable.

---

### **5. Policy & Compliance Agent**

**Role**: Identifies restrictions or violations based on policy databases and documents.

**Interview Questions**:

**Q1: How would you design the retrieval system for dynamic policy docs (e.g., constantly changing ad rules)?**
*A*: Store documents in a vector DB (Pinecone/FAISS) and index with fine-tuned BGE embeddings. Set up daily sync with CMS/policy source-of-truth to update documents.

**Q2: How do you contextualize policy retrieval with specific account/campaign info?**
*A*: Include user-specific metadata (e.g., region, campaign type) as filters in the RAG prompt or as structured constraints in the retrieval phase.

**Q3: How do you explain a policy violation clearly to a non-technical advertiser?**
*A*: Post-process RAG result using a response template:
“Your ad was disapproved because *{policy\_reason}*, which violates *{section}*. You can resolve this by *{fix\_suggestion}*.”

---

### **6. Response Synthesis Agent**

**Role**: Generates the final user-facing message from all agent outputs.

**Interview Questions**:

**Q1: How do you structure prompt inputs to make sure synthesis is grounded and not hallucinated?**
*A*: Pass a JSON payload with the outputs from each agent (`{"campaign_info":..., "diagnostics":..., "policy":...}`) into the LLM. Use a fixed template:
“Based on these inputs, generate a coherent explanation under 300 words.”

**Q2: How do you enable clarification handling if information is missing?**
*A*: The LLM checks for null or missing fields and is prompted to ask for clarification.
Example: “Could you confirm which campaign you’re referring to?”

**Q3: How do you prevent over-explaining or overwhelming users?**
*A*: Use a summarization step with a “max reasoning depth” constraint, and run A/B tests on message length vs. satisfaction scores.

---

### **7. Memory Agent**

**Role**: Maintains session history, previous queries, and state.

**Interview Questions**:

**Q1: How do you store and retrieve contextual memory efficiently for multi-turn dialogs?**
*A*: Use Redis or DynamoDB with session-scoped keys. Store memory as key-value pairs (campaign context, last user intent, agent responses). TTL is session-length or customizable.

**Q2: How do you serialize and persist nested memory objects (like agent traces)?**
*A*: Use structured formats like JSON Schema or Protobuf. Include versioning to support schema migration.

**Q3: How do you handle memory expiration or drift in long-running sessions?**
*A*: Implement memory checkpoints. Periodically summarize and compress long interactions into a reduced state blob (e.g., “user is troubleshooting campaign X, has already seen budget diagnostics”).

---

### **8. System Monitoring & Observability**

**Role**: Ensure system health, traceability, and debugging.

**Interview Questions**:

**Q1: What would you log for each query and agent call?**
*A*: Log:

* Query ID
* Timestamps per agent
* Input/output payloads (redacted)
* AST function calls
* Cache hits/misses
* RAG retrieval metadata
  Use OpenTelemetry or Datadog to trace entire multi-agent call chains.

**Q2: How do you detect function-calling drift over time?**
*A*: Store gold-standard ASTs and compare predictions daily. Calculate drift metrics: AST token overlap, argument mismatches, etc. Use them to retrain on misclassified queries.
