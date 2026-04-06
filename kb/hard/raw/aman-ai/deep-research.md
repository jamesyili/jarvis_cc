# Deep Research

**Source:** https://aman.ai/h/des/deep-research/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Clarifying requirements](#clarifying-requirements)
* [Input and output of the system](#input-and-output-of-the-system)
  + [Input](#input)
  + [Output](#output)
* [Background: What is an Agent?](#background-what-is-an-agent)
* [Agentic design](#agentic-design)
  + [Single agent vs. Multi-agent](#single-agent-vs-multi-agent)
    - [Single agent](#single-agent)
    - [Multi-agent](#multi-agent)
  + [Multi-agent design (end-to-end components and workflow)](#multi-agent-design-end-to-end-components-and-workflow)
    - [Content moderation and safety gating (pre-preprocessing stage)](#content-moderation-and-safety-gating-pre-preprocessing-stage)
    - [Metaplanner / Query rewriting and expansion (pre-processing stage)](#metaplanner--query-rewriting-and-expansion-pre-processing-stage)
    - [Planner / LeadResearcher / Orchestrator](#planner--leadresearcher--orchestrator)
    - [Research agents/Subagents (Evidence Collection)](#research-agentssubagents-evidence-collection)
    - [Memory (persistent run-state memory)](#memory-persistent-run-state-memory)
    - [Orchestration and control plane](#orchestration-and-control-plane)
    - [UI: Thinking panel](#ui-thinking-panel)
    - [Output format](#output-format)
  + [Prompts](#prompts)
    - [Planner / LeadResearcher / Orchestrator](#planner--leadresearcher--orchestrator-1)
    - [Subagents (Parallel Explorers)](#subagents-parallel-explorers)
* [Model fine-tuning strategies (SFT, RL)](#model-fine-tuning-strategies-sft-rl)
  + [When SFT Fails (and Why RL Is Required) for Agents](#when-sft-fails-and-why-rl-is-required-for-agents)
* [Reinforcement Learning with Verifiable Process-Based Rewards](#reinforcement-learning-with-verifiable-process-based-rewards)
  + [Purpose](#purpose)
  + [Definitions](#definitions)
    - [Charts](#charts)
    - [Unified objective](#unified-objective)
* [Evaluation](#evaluation)
  + [Simple/Factoid question answering](#simplefactoid-question-answering)
  + [Complex, multi-hop research evaluation](#complex-multi-hop-research-evaluation)
  + [Targeted Deep Research evaluation](#targeted-deep-research-evaluation)
* [Challenges and proposed solutions](#challenges-and-proposed-solutions)
  + [Hitting context window limits due to large volumes of content](#hitting-context-window-limits-due-to-large-volumes-of-content)
  + [Tool-call dependency graph management](#tool-call-dependency-graph-management)
  + [Implementing a parallel tool-calling framework](#implementing-a-parallel-tool-calling-framework)
  + [Balancing exploration quality with cost and latency](#balancing-exploration-quality-with-cost-and-latency)
* [Rainbow Deployment](#rainbow-deployment)
* [Post-deployment monitoring and continuous improvement](#post-deployment-monitoring-and-continuous-improvement)
  + [Continuous improvement loop](#continuous-improvement-loop)
  + [Monitoring, observability, and diagnostics](#monitoring-observability-and-diagnostics)
  + [Evaluation in the loop](#evaluation-in-the-loop)
  + [Safety, governance, and reliability](#safety-governance-and-reliability)
* [References](#references)

## Overview

* This system is engineered to enable scalable, high-quality scientific and technical research using state-of-the-art foundation models that support advanced reasoning (for example, [DeepSeek-R1](https://arxiv.org/abs/2501.12948), [Claude 3/4 family](https://www.anthropic.com/news/claude-3-family), [GPT-4](https://arxiv.org/abs/2303.08774), [GPT-4o](https://openai.com/index/hello-gpt-4o/), [GPT-4.1](https://www.reuters.com/technology/artificial-intelligence/openai-launches-new-gpt-41-models-with-improved-coding-long-context-2025-04-14/)). Instead of training models from scratch—which is compute-intensive, expensive, and risky in terms of generalization—the platform uses pretrained and fine-tuned APIs as the cognitive backend.
* The emphasis is on agentic orchestration, persistent semantic memory, automated evaluation, and real-time workflow serving. Together, these enable a production-grade, enterprise-ready agentic research platform aligned with Anthropic’s planner-plus-subagents approach, including a dedicated citation step for provenance (see Anthropic’s engineering write-up on multi-agent research [blog](https://www.anthropic.com/engineering/built-multi-agent-research-system), Claude’s [tool-use docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use), and [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)).
* The design avoids common pitfalls (reinventing foundational model training, fragile orchestration) and instead focuses on composability, observability, and governance—critical for large organizations deploying AI in research and regulated industries.
* The following figure shows the high-level multi-agent architecture in action: user queries flow through a lead researcher/orchestrator (i.e., lead agent) that creates specialized, parallel subagents to search for different aspects in parallel, along with a dedicated citation agent.

## Clarifying requirements

1. Which data sources must the system integrate with at runtime (public web, proprietary corpora, Workspace connectors like Drive/Gmail/Chat)?
2. To meet our latency budgets at p50 and p95, how much parallelism is desired in terms of maximum number of agents, tool calls per agent, tool retries? This constrains whether a multi-agent architecture is viable by default and how aggressive planning and early stopping should be.
3. To ensure transparency and reliability of factual claims, I’m assuming citations are necessary.
4. What forms of observability are required (for example, exposing intermediate plans, agent progress, or reasoning summaries to the UI)? Is a user-facing “thinking panel” necessary?
5. Google’s latest deep research outputs artifacts such as graphs and interactive visuals. We can output structured tables too. This will involve coming up with executable plotting code, relevant components in the RL reward function, and post-processing agents to render graphs.
6. Safety - to accommodate governance and safety constraints (for example, policy-violating content, restrictions on browsing domains, tool usage/API caps, or mandatory audit logs)?

## Input and output of the system

### Input

* User query expressed in natural language. Queries may be underspecified, ambiguous, or exploratory.
* Optional user-provided constraints such as desired depth, time horizon, regions, or output format.
* Optional context from connected sources (for example, Drive documents or prior conversations), retrieved via connectors when enabled.
* **Design implications:**

  + The system must include a query understanding and clarification stage inside the planner to resolve ambiguity without excessive back-and-forth.
  + Inputs are treated as soft constraints that can be refined into a concrete research plan rather than hard execution instructions.

### Output

* A synthesized research report with:

  + Structured sections (executive summary, methodology, findings, limitations).
  + Charts and interactive visualizations generated via executable Python code (matplotlib, seaborn, plotly, D3.js, etc.) embedded or attachable.
  + Tables summarizing key facts, comparisons, or datasets.
  + Inline citations mapped to specific factual claims, with URLs or DOIs.
* Optional alternate modalities:

  + Audio overview generated from the final report.
* **Design implications:**

  + Chart generation requires sandboxed code execution and schema validation to prevent runtime or security issues.
  + A strict output schema is needed so downstream systems (export, PDF generation, sharing) remain robust.

## Background: What is an Agent?

* The following figure shows a conceptual view of an AI agent’s ingredients (autonomy under human control, memory, tools such as APIs/web/code, and reactivity to the environment).

* For a detailed discourse on Agents, please refer to our [Agents](../../../primers/ai/agents) and [Agentic RL](../../../primers/ai/agentic-RL) primers.

## Agentic design

### Single agent vs. Multi-agent

#### Single agent

* **Pros**:

  + **Simpler system surface area:** one execution trace, and more predictable execution paths and evaluation, since the agent typically follows a mostly linear reasoning process. This leads to lower orchestration overhead and fewer coordination failure modes, and ultimately easier debugging.
* **Cons**:

  + **Context window pressure dominates deep research:** long documents, intermediate notes, and partial drafts displace earlier constraints and plans, causing silent objective drift or loss of strategy. Anthropic explicitly persists plans to external memory to mitigate truncation in long-horizon tasks, highlighting this as a core limitation of single-agent setups.
  + **Limited parallelism:** even with batched tool calls, a single policy must interleave planning, retrieval, evaluation, and synthesis sequentially, creating throughput bottlenecks for breadth-heavy tasks.
  + **Weak specialization:** orchestration, evidence gathering, evaluation, and synthesis compete in one prompt and policy, making it harder for the agent to excel simultaneously at decomposition, search strategy, and aggregation.
  + **Hard limits on scale:** once the task exceeds the agent’s effective token or reasoning budget, performance degrades sharply, regardless of prompt quality.

#### Multi-agent

* **Pros**:

  + **Breadth-first exploration at scale:** multiple research agents explore different facets of the problem in parallel, which is particularly effective for open-ended, ambiguous, or poorly specified research queries where the solution path is not known in advance.
  + **Empirical quality gains:** A significant performance improvement over a single-agent baseline when using a lead agent plus supporting subagents, validating the architectural lift of task decomposition and parallel search.
  + **Robustness to context limits:** plans and intermediate state are externalized to memory, while agents exchange compact summaries rather than raw content, effectively scaling usable reasoning capacity across multiple context windows.
  + **Natural specialization:** the planner focuses on decomposition, prioritization, and stopping criteria, while research agents focus on evidence discovery, source evaluation, and localized reasoning.
  + **Reduced path dependency:** independent subagents explore distinct trajectories, lowering the risk that early planning errors overly constrain the final result.
* **Cons**:

  + **Cost and latency trade-offs:** multi-agent breadth substantially increases token usage and tool calls, often by an order of magnitude relative to chat-style single-agent interactions.
  + **Coordination and orchestration complexity:** agent spawning, dependency tracking, deduplication, result merging, and error handling introduce non-trivial control-plane logic and additional failure modes.
  + **Harder evaluation and debugging:** non-deterministic execution paths mean agents may reach correct answers via different routes, requiring outcome-based or LLM-as-judge evaluation rather than step-by-step verification.
  + **Poor fit for tightly coupled tasks:** domains with strong interdependencies or shared context, such as many coding workflows, offer limited parallelism and therefore weaker returns from multi-agent architectures.
* [How Anthropic Built a Multi-Agent Research System](https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent) by ByteByteGo notes that a lead-agent (Claude Opus 4) plus supporting subagents (Claude Sonnet 4) outperformed a single-agent setup by more than \(90%\), with a coordination token cost overhead of roughly \(15\times\) compared to standard chat. This necessitates explicit budget controls, scaling rules, and adaptive parallelism driven by query complexity.
* **Design orientation and trade-offs**:

  + **Exploration vs. cost and latency**:

    - Breadth-first multi-agent exploration delivers substantial gains for open-ended research but must be balanced against spend and runtime. The system therefore needs policy-driven limits on agent count, tool concurrency, retries, and escalation, with early stopping when marginal value declines.
  + **Empirical lift vs. overhead**:

    - The observed quality improvements of lead-agent plus subagent architectures justify the added complexity, but only when paired with adaptive spawning, per-agent budgets, robust observability, and planner-controlled termination to prevent runaway behavior.

### Multi-agent design (end-to-end components and workflow)

* The following figure shows an end-to-end swimlane of the iterative research loop with user/system handoffs, planner and subagent cycles, memory interactions, and the final synthesis phase with embedded citations.

* Note that rather than using a dedicated citation agent similar to [Anthropic’s multi-agent research implementation](https://www.anthropic.com/engineering/built-multi-agent-research-system), this design incorporates citations as part of the research agents/subagents.

#### Content moderation and safety gating (pre-preprocessing stage)

* **Purpose**:

  + **Safety model application**: Apply an SLM-based safety classifier, for example [ShieldGemma](https://ai.google.dev/gemma/docs/shieldgemma) or [LlamaGuard](https://ai.meta.com/research/publications/llamaguard-open-and-robust-safety-classifier-for-llms), or a comparable lightweight moderation model, to screen queries before any rewriting or expansion.
  + **Harm prevention**: Prevent the system from researching or amplifying content that would promote hate speech, racism, violence, discrimination, or catastrophic harm.
* **Screening scope**:

  + **Input evaluation**: Evaluate the original user query and any immediately inferred intent prior to metaplanning.
  + **Implicit risk detection**: Detect both explicit harmful requests and implicitly dangerous objectives suggested by context.
* **Disallowed categories**:

  + **Hate and dehumanization**: Hate speech or dehumanization targeting protected classes.
  + **Violence facilitation**: Advocacy, justification, or facilitation of violence or physical harm.
  + **Discriminatory optimization**: Discriminatory recommendations or exclusionary optimization goals.
  + **Catastrophic enablement**: Research that materially lowers the barrier to large-scale or irreversible harm.
* **Decision logic**:

  + **Intent classification**: Distinguish descriptive or critical analysis from promotional or instructional intent.
  + **Conservative defaulting**: Default to conservative blocking when intent is ambiguous and potential harm is high.
* **Mitigation outputs**:

  + **Disposition outcome**: Allow, block, or conditionally allow the query with constraints.
  + **Query sanitization**: Produce a sanitized query when partial salvage is possible.
  + **Transparency signals**: Explicitly list removed or suppressed intents for transparency.
* **Design rationale**:

  + **Amplification control**: Early safety gating prevents harmful amplification during query expansion.
  + **Operational efficiency**: Using a small, fast model minimizes overhead while keeping downstream planners aligned with safety constraints.

#### Metaplanner / Query rewriting and expansion (pre-processing stage)

* **Role in the system:**: The planning-researching agentic loop begins with a MetaPlanner which performs query rewriting and expansion to address underspecified queries.
* **Purpose**:

  + **Query normalization and disambiguation**: Normalize and disambiguate underspecified or ambiguous user queries.
  + **Constraint and assumption surfacing**: Surface implicit constraints, assumptions, and missing dimensions that materially affect research quality.
  + **Intent expansion**: Expand the query into a small set of well-scoped research intents that the planner can reason over deterministically.
  + **Context enrichment**: Enrich queries with relevant temporal and spatial context when required for correctness or usefulness.
* **Key functions**:

  + **Disambiguation**: detect unclear entities, time ranges, geographies, metrics, or comparison axes and infer likely interpretations based on context, defaults, or user history.
  + **Location and time grounding**: automatically inject inferred or explicit location and time constraints into the query when relevant.

    - Example: “restaurants near me” or “buy a laptop near me” is rewritten to include the user’s inferred city or coordinates and the current date and time, enabling downstream agents to reason about factors such as whether a restaurant is currently open, same-day availability of an item, or local inventory at nearby retailers.
  + **Expansion**: generate structured sub-questions that cover breadth (the main facets of the topic) without prematurely decomposing into execution-level subtasks.
  + **Normalization**: rewrite the query into a canonical form that explicitly states objectives, scope boundaries, location, time horizon, and expected output type.
  + **Safety and harm-aware constraint setting**: detect sensitive or high-risk queries and apply explicit guardrails before planning. The MetaPlanner must avoid creating subagents to research or expand topics that could promote hate speech, racism, violence, discrimination, or catastrophic harm. When a query is sensitive but potentially valid, the MetaPlanner must rewrite it with clear, enforceable constraints that limit scope, frame the task in a non-harmful manner, and prevent downstream agents from producing or amplifying harmful content.
* **Outputs**:

  + **Rewritten primary query**: A rewritten primary query that:

    - **Explicit research dimensions**: Explicitly enumerates clarified intents or research dimensions that cover the breadth of the topic.

      * **Example:** “Compare leading AI safety startups” may be rewritten to include dimensions such as funding stage, core technology focus, customer segments, regulatory posture, and recent growth signals.
      * **Example:** “Best electric cars” may expand into price range, driving range, charging ecosystem, safety ratings, and availability.
    - **Location and time constraints**: Includes explicit location and time constraints when applicable.

      * **Example:** “best restaurants near me” becomes “best restaurants within 5 km of San Francisco, open as of today at 7 pm, ranked by reviews and cuisine type.”
      * **Example:** “buy a laptop near me” becomes “laptops available for in-store pickup within 10 miles of Seattle as of this week, filtered by price, performance, and brand.”
  + **Expanded intent set**: A small set of expanded clarifying intents or research dimensions.
  + **Explicit assumptions**: Makes all inferred assumptions explicit so they can be corrected later if needed.
* **Design rationale**:

  + **Planner simplification**: Separating query rewriting and expansion from planning reduces cognitive load on the planner and avoids conflating clarification with orchestration.
  + **Consistency through grounding**: Automatic location and time grounding prevents downstream agents from making inconsistent assumptions and improves relevance for queries with implicit “near me” or “current” intent.
  + **Improved allocation and coverage**: By explicitly enumerating research dimensions up front, the planner can more reliably allocate subagents, detect coverage gaps, and apply stopping criteria.
  + **Stability and reproducibility**: This stage improves planner stability, reproducibility, and stopping behavior by ensuring the planner operates on a well-formed objective rather than raw user input.

#### Planner / LeadResearcher / Orchestrator

* **Responsibilities**:

  + **Research plan construction:** Convert the input query into a structured, multi-point research plan with explicit subtasks, selection criteria for consideration, and defined output formats.
  + **Agent allocation and scaling:** Decide how many research agents to spawn based on difficulty signals such as breadth, ambiguity, depth, expected evidence diversity, and tolerance for uncertainty, following explicit scaling guidance encoded in the planner prompt:

    - **Very simple queries:** Well-scoped fact-finding tasks involving a single entity, single source type, and minimal ambiguity typically spawn **1 to 2 research agents**, primarily for redundancy checking and fast verification.
    - **Moderately complex queries:** Comparisons, multi-entity questions, or tasks with several clearly separable research dimensions typically spawn **4 to 8 research agents**, with each agent assigned to a distinct facet such as market landscape, technical details, recent developments, or regional variation.
    - **Broad or ambiguous queries:** Queries spanning many dimensions, requiring heterogeneous sources, or involving open-ended exploration typically spawn **10 to 20 research agents**, each with a narrowly scoped mandate to avoid overlap.
    - **Very deep or high-stakes research:** Exploratory or high-impact tasks such as policy analysis, frontier technology surveys, or multi-disciplinary reviews may spawn **20 to 40 research agents**, often executed in staged phases where early agents map the space and later agents fill identified gaps.
    - **Adaptive scaling rule:** The planner prompt explicitly instructs the Planner/LeadResearcher to start at the lower end of these ranges and increase agent count only when early returns indicate missing dimensions, conflicting evidence, or insufficient confidence.
  + **Parallel execution and orchestration:** For maximum efficiency, invoke multiple independent tool calls simultaneously rather than sequentially. Use parallel tool calls for creating multiple subagents, typically launching 3 subagents at the start of research unless the query is straightforward. For other queries, perform any necessary quick initial planning directly, then run subagents in parallel. Extensive tool usage is delegated to subagents, with the planner focusing on efficient parallelization.
  + **State persistence and resumability:** Persist the research plan and evolving execution state to memory early to defend against context truncation in long-horizon jobs and to enable resumability after crashes.
  + **Iterative synthesis and control:** Iteratively synthesize research agent outputs, assess coverage and gaps, and determine whether to continue research or transition to finalization.
  + **Avoid harm-causing subagents**: Avoid creating subagents to research topics that could cause harm. Specifically, you must not create subagents to research anything that would promote hate speech, racism, violence, discrimination, or catastrophic harm. If a query is sensitive, specify clear constraints for the subagent to avoid causing harm.
* **Key planner prompt aspects**:

  + **Explicit delegation:** Each subtask includes a clearly defined objective, scope boundaries, expected output shape, recommended tools or tool interfaces, and constraints designed to prevent duplication.
  + **Dynamic effort scaling:** Agent count and research depth are continuously adjusted during execution based on concrete signals from returned evidence, such as uncovered facets, low-confidence claims, contradictory sources, or excessive uncertainty.
* **Stopping criteria and termination policy**:

  + **Clear stopping criteria:** The planner must explicitly decide when to stop research and transition to synthesis, avoiding infinite search loops, uncontrolled agent fan-out, or unnecessary tool usage.
  + **Diminishing-returns assessment:** The planner must explicitly reason about diminishing returns and terminate research as soon as a high-confidence, good-enough answer can be produced.
    - **Indicators of diminishing returns:** Additional research is considered low value when:

      * New sources largely restate previously collected information.
      * Incremental evidence does not materially change rankings, conclusions, or confidence levels.
      * Additional agents converge on the same claims, sources, or summaries already captured in earlier searches.
    - **Mandatory termination actions:** When further research is unlikely to improve correctness, coverage, or insight, the planner must:

      * Stop spawning new research agents.
      * Stop issuing further tool calls.
      * Transition immediately to final synthesis and report generation.
  + **Budget-based termination:** Budget exhaustion is an explicit stopping condition:

    - If remaining tokens, tool calls, or wall-clock time fall below the minimum required for another meaningful research iteration, the planner must halt further research.
    - The planner must then synthesize the best possible report from existing evidence and clearly surface any remaining uncertainty.
  + **Preference for early completion:** The planner should favor early termination over exhaustive exploration when the task has a natural completeness boundary. For example, if the task is to identify the top 5 fastest-growing startups and a stable top 5 set has already been identified with high confidence from reliable sources, research must stop immediately.
  + **Anti-overreach safeguards:** This termination behavior is mandatory for efficiency and cost control and exists to prevent:

    - Unbounded search loops.
    - Over-retrieval that adds noise rather than signal.
    - Wasted tokens and tool calls after the answer is already sufficient or budgets are depleted.
  + **Answer-complete recognition:** The planner must explicitly recognize the answer-complete state and proceed directly to final report generation rather than continuing the research loop unnecessarily.

#### Research agents/Subagents (Evidence Collection)

* **Responsibilities**:

  + **Research planning and budgeting first**: Begin every task by thinking through the problem thoroughly. Review requirements, decompose the task into subtasks, identify relevant tools, and determine how they should be used optimally. Using this information, come up with a research plan and set a research budget that estimates the number of tool calls appropriate to the task’s complexity, using it as a strict efficiency guardrail.
  + **Independent subtask execution**: Execute scoped subtasks independently according to the plan and return distilled findings with embedded citations directly tied to specific claims.
  + **Iterative reasoning and control**: After each tool result, reason carefully about what was learned, update the plan if needed, and decide whether to refine queries, branch into parallel searches, execute dependent calls, or stop.
  + **Source quality scrutiny and epistemic care**: Critically evaluate results rather than taking them at face value. Identify speculation, future-tense projections, marketing language, unnamed or passive sourcing, aggregators rather than primary sources, and cherry-picked or misleading data. Clearly distinguish confirmed facts from predictions or uncertain claims and flag issues explicitly when reporting back.
  + **Citation discipline**: Provide citations that are directly tied to substantive claims, emphasizing key facts and conclusions that readers would plausibly want to verify. Avoid citing common knowledge, and ensure citation placement preserves readability and meaning.
  + **Efficiency discipline**: Avoid repeating identical tool queries. If an approach yields diminishing returns or information appears unavailable or low quality, pivot to alternative tools or queries or stop and report partial findings with uncertainty.
  + **Parallelization awareness**: When multiple independent subtasks can be specified without dependencies, execute them in parallel to reduce latency and improve coverage.
  + **Hard limits and stopping behavior**: Enforce global limits on tool calls and sources. When nearing the budget or absolute caps, or when new calls are unlikely to add value, stop gathering evidence and move to synthesis.
* **Tool-calling execution model**:

  + **Planning-first workflow**: Tool use is always preceded by an explicit plan that specifies subtasks, tool choices, expected dependencies, and a calibrated research budget.
  + **Budget calibration heuristic**: Align the research budget with task complexity: simple tasks typically require under 5 tool calls, medium tasks around 5, hard tasks about 10, and very difficult or multi-part tasks up to 15. Treat the budget as binding unless strong justification emerges.
  + **Fine-tuning requirements**: Reliable tool use depends on models trained with both supervised fine-tuning and reinforcement learning. SFT teaches correct syntax, schemas, and formatting, while RL teaches when to call tools, which tool to select, how to balance cost and latency, how to parallelize safely, and when to stop.
  + **Implicit dependency resolution**: Prefer parallel tool calls where possible. Decisions about parallel vs. serial execution are learned rather than encoded as an explicit dependency graph.

    - **Background on tool calls:**

      * **Parallelizable calls**: Calls whose arguments can be fully specified immediately, without relying on other tool outputs.
      * **Serial calls**: Calls whose arguments depend on the results of prior tool calls.
    - **Learned dependency checks**: Dependency assessment is based on agent’s output (and not computed via a formal algorithm).

      * **Concurrent emission of independent calls**: Independent subtasks yield multiple complete tool call objects emitted in a single model turn and executed concurrently by the runtime.
      * **Sequential chaining of dependent calls**: Dependent subtasks yield a call, incorporate its results into the prompt state, and then emit the next call, enforcing a serial chain.
    - **Runtime enforcement**: The orchestration layer executes concurrent calls within a step and carries results forward across steps to enable serial chaining.
    - **Training signal effects**: SFT enforces correct schemas and multi-tool formatting, while RL penalizes unnecessary calls and rewards correct sequencing, tool choice, low latency, and appropriate stopping.
    - **Common failure modes**: Over-serializing independent calls, parallelizing calls with hidden dependencies, skipping prerequisite calls, or hallucinating inputs.
  + **Stopping criteria as policy**: Stop calling tools once sufficient high-quality evidence is obtained, when further calls are unlikely to change conclusions, or when budget and system limits are approaching.
  + **Tool choice under uncertainty**: Prefer fresh verification when information may be time-sensitive. When results are redundant or low quality, change queries or tools rather than repeating the same calls.
* **Retry and failure handling**:

  + **Retry policy**: Each tool call supports up to \(M\) retries with argument repair and exponential backoff.
  + **Graceful degradation**: On repeated failure, substitute an alternative tool or return partial results with explicit uncertainty and failure metadata.
  + **Non-repetition constraint**: Retries must involve corrected arguments or different tools; identical repeated calls are treated as wasteful.
* **Execution pattern rationale**:

  + **Hybrid exploration and refinement**: Effective research alternates between wide parallel exploration to map the space and narrow serial refinement to deepen understanding.
* **Citation guidelines**:

  + **Guiding principle**:

    - **Cite to add verification and credibility**: Use citations to support key facts, conclusions, and substantive claims tied to sources, especially where a reader would reasonably want to verify the statement. Avoid citing common knowledge or purely background framing.
  + **Granularity and placement**:

    - **Cite meaningful semantic units**: Attach citations to complete thoughts, findings, or claims that stand on their own. Prefer placing citations at the end of sentences (after the period) rather than attaching them to individual words or short fragments that lose meaning out of context.
  + **Readability and flow**:

    - **Minimize sentence fragmentation**: Avoid peppering a sentence with many citations that interrupt readability. Only place citations mid-sentence when it is necessary to attribute distinct sub-claims to different sources.
  + **Redundancy control**:

    - **Avoid redundant citations in close proximity**: Do not cite the same source multiple times within the same sentence. If multiple claims in a sentence are supported by the same source, use a single citation at the end of the sentence.
* **MCP servers and tool access abstraction**:

  + The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is an open protocol designed to standardize how applications provide context to LLMs. Conceptually, MCP can be understood as the AI equivalent of a USB-C port: just as USB-C defines a single, standardized interface for connecting many different peripherals, MCP provides a uniform way for AI models to connect to heterogeneous tools, data sources, and services without bespoke adapters.
  + MCP follows a client–server architecture in which an MCP client connects to one or more MCP servers, and each server exposes its capabilities through a standardized protocol. These capabilities may include callable tools, retrievable resources, and reusable prompt templates.
  + The following figure illustrates MCP’s client–server architecture as a standardized bridge between AI applications and local or remote data sources, analogous to how a USB-C port enables seamless connectivity across peripherals without custom connectors.
  + In the Deep Research system, research agents can invoke tools either as raw APIs or via MCP servers. MCP is preferred when the system requires:

    - A single, standardized integration surface across many heterogeneous tools.
    - Dynamic discovery of available tools and capabilities at runtime, rather than hard-coded integrations.
    - Security controls such as centralized authentication, authorization, and policy enforcement across all tools.
    - Easier evolution and versioning of tools without retraining models or rewriting prompts.
    - Richer, two-way interaction patterns that go beyond simple request–response APIs.
  + **Implementation approach:**

    - Existing APIs, databases, search systems, internal services, or proprietary data sources are wrapped behind MCP servers that expose:

      * Tools: callable operations such as search, fetch, compute, or transact.
      * Resources: structured context such as documents, records, or snapshots.
      * Prompts: reusable prompt templates for common workflows.
    - MCP servers can be deployed locally (for example, via stdio transport) or remotely (via streamable HTTP-style transports), depending on latency, security, and deployment requirements.
    - Security controls such as authentication, authorization, and side-effect annotations (for example, read-only versus write operations) are enforced at the MCP server boundary, not inside the LLM.
  + From the agent’s perspective, calling a tool via an MCP server is equivalent to calling any other tool. The same SFT- and RL-trained tool-calling policies apply, allowing new tools to be added, swapped, or upgraded behind MCP servers without changing agent prompts or retraining from scratch.
  + For a detailed discourse on MCP, please refer to our [Agents](../../../primers/ai/agents/#model-context-protocol-mcp) primer.
* **Additional design aspects**:

  + Start-wide-then-narrow search strategy to map the information space before deep dives.
  + Source quality evaluation and deduplication before returning results to the planner.

#### Memory (persistent run-state memory)

* **Unified persistent memory**:

  + The system uses a memory layer that acts as the source of truth for both short-lived execution state and long-lived continuity, eliminating reliance on ephemeral in-context state.
  + This memory is designed to support long-running research tasks and crash recovery (to enable resumability without restarting from scratch).
* **What is stored**:

  + The canonical research plan, including clarified objectives, assumptions, and success criteria.
  + Current execution state of the plan, including:

    - Subtask registry with completion status, assigned agents, and dependency relationships.
    - Tool-call dependency graphs with execution status, retry counts, and failure metadata.
    - Source maps linking claims to evidence and citations gathered so far.
    - Intermediate summaries and partial syntheses produced at each stage.
    - Explicit next steps computed by the planner, such as pending subtasks, candidate agent spawns, or readiness for final synthesis.
  + Checkpoints for in-progress runs, enabling recovery after crashes, restarts, or budget-enforced pauses.
  + User-specific preferences relevant to execution, such as desired depth, formatting expectations, trusted sources, and cost or latency constraints.
* **How it is used**:

  + The planner and research agents read from and write to this memory continuously, treating it as the authoritative execution state rather than relying on the LLM context window.
  + On restart or resumption, the system rehydrates the planner from memory, restoring the plan, progress, and pending actions so execution can continue deterministically.
  + Large documents and evidence are referenced by identifiers or summaries in memory, with raw content stored externally and fetched only when needed.
* **Design principles**:

  + Treat the LLM context window as a transient working cache, not as durable state.
  + Externalize all information required for correctness, progress tracking, and recovery into structured, persistent memory.
  + Prefer compact summaries, references, and identifiers over raw text to minimize token usage and avoid context overflow.
  + Ensure that any long-running research task can be paused, resumed, or retried after failure without losing progress or duplicating work.

#### Orchestration and control plane

* **Scheduler**:

  + Manages agent lifecycle, concurrency limits, dependency-aware tool execution, timeouts, and cancellation.
* **Budget and policy manager**:

  + Enforces per-agent and global limits on tool calls, retries, and spend.
* **Observability**:

  + Logs planning decisions, tool dependency graphs, failures, and outcomes to diagnose systematic issues.

#### UI: Thinking panel

* Displays the current plan, completed actions, active tasks, websites researched, and intended next actions.
* A curated view of intermediate reasoning improves trust and controllability without exposing raw chain-of-thought.

#### Output format

* Comprehensive research reports synthesized by the Planner/LeadResearcher with embedded citations produced directly by research agents, along with tables and graphs/plots/interactive visualizations.
* Optional Audio Overview generated from the final structured report.

### Prompts

* This section refers Anthropic’s open-source prompts in their [cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/patterns/agents/prompts) for their Multi-Agent Research system.

#### Planner / LeadResearcher / Orchestrator

```
You are an expert research lead, focused on high-level research strategy, planning, efficient delegation to subagents, and final report writing. Your core goal is to be maximally helpful to the user by leading a process to research the user's query and then creating an excellent research report that answers this query very well. Take the current request from the user, plan out an effective research process to answer it as well as possible, and then execute this plan by delegating key tasks to appropriate subagents. The current date is .

<research_process> 
Follow this process to break down the user’s question and develop an excellent research plan. Think about the user's task thoroughly and in great detail to understand it well and determine what to do next. Analyze each aspect of the user's question and identify the most important aspects. Consider multiple approaches with complete, thorough reasoning. Explore several different methods of answering the question (at least 3) and then choose the best method you find. Follow this process closely:

Assessment and breakdown: Analyze and break down the user's prompt to make sure you fully understand it.
Identify the main concepts, key entities, and relationships in the task.
List specific facts or data points needed to answer the question well.
Note any temporal or contextual constraints on the question.
Analyze what features of the prompt are most important - what does the user likely care about most here? What are they expecting or desiring in the final result? What tools do they expect to be used and how do we know?
Determine what form the answer would need to be in to fully accomplish the user's task. Would it need to be a detailed report, a list of entities, an analysis of different perspectives, a visual report, or something else? What components will it need to have?
Query type determination: Explicitly state your reasoning on what type of query this question is from the categories below.
Depth-first query: When the problem requires multiple perspectives on the same issue, and calls for "going deep" by analyzing a single topic from many angles.
Benefits from parallel agents exploring different viewpoints, methodologies, or sources
The core question remains singular but benefits from diverse approaches
Example: "What are the most effective treatments for depression?" (benefits from parallel agents exploring different treatments and approaches to this question)
Example: "What really caused the 2008 financial crisis?" (benefits from economic, regulatory, behavioral, and historical perspectives, and analyzing or steelmanning different viewpoints on the question)
Example: "can you identify the best approach to building AI finance agents in 2025 and why?"
Breadth-first query: When the problem can be broken into distinct, independent sub-questions, and calls for "going wide" by gathering information about each sub-question.
Benefits from parallel agents each handling separate sub-topics.
The query naturally divides into multiple parallel research streams or distinct, independently researchable sub-topics
Example: "Compare the economic systems of three Nordic countries" (benefits from simultaneous independent research on each country)
Example: "What are the net worths and names of all the CEOs of all the fortune 500 companies?" (intractable to research in a single thread; most efficient to split up into many distinct research agents which each gathers some of the necessary information)
Example: "Compare all the major frontend frameworks based on performance, learning curve, ecosystem, and industry adoption" (best to identify all the frontend frameworks and then research all of these factors for each framework)
Straightforward query: When the problem is focused, well-defined, and can be effectively answered by a single focused investigation or fetching a single resource from the internet.
Can be handled effectively by a single subagent with clear instructions; does not benefit much from extensive research
Example: "What is the current population of Tokyo?" (simple fact-finding)
Example: "What are all the fortune 500 companies?" (just requires finding a single website with a full list, fetching that list, and then returning the results)
Example: "Tell me about bananas" (fairly basic, short question that likely does not expect an extensive answer)
Detailed research plan development: Based on the query type, develop a specific research plan with clear allocation of tasks across different research subagents. Ensure if this plan is executed, it would result in an excellent answer to the user's query.
For Depth-first queries:
Define 3-5 different methodological approaches or perspectives.
List specific expert viewpoints or sources of evidence that would enrich the analysis.
Plan how each perspective will contribute unique insights to the central question.
Specify how findings from different approaches will be synthesized.
Example: For "What causes obesity?", plan agents to investigate genetic factors, environmental influences, psychological aspects, socioeconomic patterns, and biomedical evidence, and outline how the information could be aggregated into a great answer.
For Breadth-first queries:
Enumerate all the distinct sub-questions or sub-tasks that can be researched independently to answer the query.
Identify the most critical sub-questions or perspectives needed to answer the query comprehensively. Only create additional subagents if the query has clearly distinct components that cannot be efficiently handled by fewer agents. Avoid creating subagents for every possible angle - focus on the essential ones.
Prioritize these sub-tasks based on their importance and expected research complexity.
Define extremely clear, crisp, and understandable boundaries between sub-topics to prevent overlap.
Plan how findings will be aggregated into a coherent whole.
Example: For "Compare EU country tax systems", first create a subagent to retrieve a list of all the countries in the EU today, then think about what metrics and factors would be relevant to compare each country's tax systems, then use the batch tool to run 4 subagents to research the metrics and factors for the key countries in Northern Europe, Western Europe, Eastern Europe, Southern Europe.
For Straightforward queries:
Identify the most direct, efficient path to the answer.
Determine whether basic fact-finding or minor analysis is needed.
Specify exact data points or information required to answer.
Determine what sources are likely most relevant to answer this query that the subagents should use, and whether multiple sources are needed for fact-checking.
Plan basic verification methods to ensure the accuracy of the answer.
Create an extremely clear task description that describes how a subagent should research this question.
For each element in your plan for answering any query, explicitly evaluate:
Can this step be broken into independent subtasks for a more efficient process?
Would multiple perspectives benefit this step?
What specific output is expected from this step?
Is this step strictly necessary to answer the user's query well?
Methodical plan execution: Execute the plan fully, using parallel subagents where possible. Determine how many subagents to use based on the complexity of the query, default to using 3 subagents for most queries.
For parallelizable steps:
Deploy appropriate subagents using the <delegation_instructions> below, making sure to provide extremely clear task descriptions to each subagent and ensuring that if these tasks are accomplished it would provide the information needed to answer the query.
Synthesize findings when the subtasks are complete.
For non-parallelizable/critical steps:
First, attempt to accomplish them yourself based on your existing knowledge and reasoning. If the steps require additional research or up-to-date information from the web, deploy a subagent.
If steps are very challenging, deploy independent subagents for additional perspectives or approaches.
Compare the subagent's results and synthesize them using an ensemble approach and by applying critical reasoning.
Throughout execution:
Continuously monitor progress toward answering the user's query.
Update the search plan and your subagent delegation strategy based on findings from tasks.
Adapt to new information well - analyze the results, use Bayesian reasoning to update your priors, and then think carefully about what to do next.
Adjust research depth based on time constraints and efficiency - if you are running out of time or a research process has already taken a very long time, avoid deploying further subagents and instead just start composing the output report immediately. 
</research_process>

<subagent_count_guidelines> 
When determining how many subagents to create, follow these guidelines:

Simple/Straightforward queries: create 1 subagent to collaborate with you directly -
Example: "What is the tax deadline this year?" or “Research bananas” → 1 subagent
Even for simple queries, always create at least 1 subagent to ensure proper source gathering
Standard complexity queries: 2-3 subagents
For queries requiring multiple perspectives or research approaches
Example: "Compare the top 3 cloud providers" → 3 subagents (one per provider)
Medium complexity queries: 3-5 subagents
For multi-faceted questions requiring different methodological approaches
Example: "Analyze the impact of AI on healthcare" → 4 subagents (regulatory, clinical, economic, technological aspects)
High complexity queries: 5-10 subagents (maximum 20)
For very broad, multi-part queries with many distinct components
Identify the most effective algorithms to efficiently answer these high-complexity queries with around 20 subagents.
Example: "Fortune 500 CEOs birthplaces and ages" → Divide the large info-gathering task into smaller segments (e.g., 10 subagents handling 50 CEOs each) IMPORTANT: Never create more than 20 subagents unless strictly necessary. If a task seems to require more than 20 subagents, it typically means you should restructure your approach to consolidate similar sub-tasks and be more efficient in your research process. Prefer fewer, more capable subagents over many overly narrow ones. More subagents = more overhead. Only add subagents when they provide distinct value. 
</subagent_count_guidelines>

<delegation_instructions> 
Use subagents as your primary research team - they should perform all major research tasks:

Deployment strategy:
Deploy subagents immediately after finalizing your research plan, so you can start the research process quickly.
Use the run_blocking_subagent tool to create a research subagent, with very clear and specific instructions in the prompt parameter of this tool to describe the subagent's task.
Each subagent is a fully capable researcher that can search the web and use the other search tools that are available.
Consider priority and dependency when ordering subagent tasks - deploy the most important subagents first. For instance, when other tasks will depend on results from one specific task, always create a subagent to address that blocking task first.
Ensure you have sufficient coverage for comprehensive research - ensure that you deploy subagents to complete every task.
All substantial information gathering should be delegated to subagents.
While waiting for a subagent to complete, use your time efficiently by analyzing previous results, updating your research plan, or reasoning about the user's query and how to answer it best.
Task allocation principles:
For depth-first queries: Deploy subagents in sequence to explore different methodologies or perspectives on the same core question. Start with the approach most likely to yield comprehensive and good results, the follow with alternative viewpoints to fill gaps or provide contrasting analysis.
For breadth-first queries: Order subagents by topic importance and research complexity. Begin with subagents that will establish key facts or framework information, then deploy subsequent subagents to explore more specific or dependent subtopics.
For straightforward queries: Deploy a single comprehensive subagent with clear instructions for fact-finding and verification. For these simple queries, treat the subagent as an equal collaborator - you can conduct some research yourself while delegating specific research tasks to the subagent. Give this subagent very clear instructions and try to ensure the subagent handles about half of the work, to efficiently distribute research work between yourself and the subagent.
Avoid deploying subagents for trivial tasks that you can complete yourself, such as simple calculations, basic formatting, small web searches, or tasks that don't require external research
But always deploy at least 1 subagent, even for simple tasks.
Avoid overlap between subagents - every subagent should have distinct, clearly separate tasks, to avoid replicating work unnecessarily and wasting resources.
Clear direction for subagents: Ensure that you provide every subagent with extremely detailed, specific, and clear instructions for what their task is and how to accomplish it. Put these instructions in the prompt parameter of the run_blocking_subagent tool.
All instructions for subagents should include the following as appropriate:
Specific research objectives, ideally just 1 core objective per subagent.
Expected output format - e.g. a list of entities, a report of the facts, an answer to a specific question, or other.
Relevant background context about the user's question and how the subagent should contribute to the research plan.
Key questions to answer as part of the research.
Suggested starting points and sources to use; define what constitutes reliable information or high-quality sources for this task, and list any unreliable sources to avoid.
Specific tools that the subagent should use - i.e. using web search and web fetch for gathering information from the web, or if the query requires non-public, company-specific, or user-specific information, use the available internal tools like google drive, gmail, gcal, slack, or any other internal tools that are available currently.
If needed, precise scope boundaries to prevent research drift.
Make sure that IF all the subagents followed their instructions very well, the results in aggregate would allow you to give an EXCELLENT answer to the user's question - complete, thorough, detailed, and accurate.
When giving instructions to subagents, also think about what sources might be high-quality for their tasks, and give them some guidelines on what sources to use and how they should evaluate source quality for each task.
Example of a good, clear, detailed task description for a subagent: "Research the semiconductor supply chain crisis and its current status as of 2025. Use the web_search and web_fetch tools to gather facts from the internet. Begin by examining recent quarterly reports from major chip manufacturers like TSMC, Samsung, and Intel, which can be found on their investor relations pages or through the SEC EDGAR database. Search for industry reports from SEMI, Gartner, and IDC that provide market analysis and forecasts. Investigate government responses by checking the US CHIPS Act implementation progress at commerce.gov, EU Chips Act at ec.europa.eu, and similar initiatives in Japan, South Korea, and Taiwan through their respective government portals. Prioritize original sources over news aggregators. Focus on identifying current bottlenecks, projected capacity increases from new fab construction, geopolitical factors affecting supply chains, and expert predictions for when supply will meet demand. When research is done, compile your findings into a dense report of the facts, covering the current situation, ongoing solutions, and future outlook, with specific timelines and quantitative data where available."
Synthesis responsibility: As the lead research agent, your primary role is to coordinate, guide, and synthesize - NOT to conduct primary research yourself. You only conduct direct research if a critical question remains unaddressed by subagents or it is best to accomplish it yourself. Instead, focus on planning, analyzing and integrating findings across subagents, determining what to do next, providing clear instructions for each subagent, or identifying gaps in the collective research and deploying new subagents to fill them. 
</delegation_instructions>

<answer_formatting> 
Before providing a final answer:
Review the most recent fact list compiled during the search process.
Reflect deeply on whether these facts can answer the given query sufficiently.
Only then, provide a final answer in the specific format that is best for the user's query and following the <writing_guidelines> below.
Output the final result in Markdown using the complete_task tool to submit your final research report.
Do not include ANY Markdown citations, a separate agent will be responsible for citations. Never include a list of references or sources or citations at the end of the report. 
</answer_formatting>

<use_available_internal_tools> 
You may have some additional tools available that are useful for exploring the user's integrations. For instance, you may have access to tools for searching in Asana, Slack, Github. Whenever extra tools are available beyond the Google Suite tools and the web_search or web_fetch tool, always use the relevant read-only tools once or twice to learn how they work and get some basic information from them. For instance, if they are available, use slack_search once to find some info relevant to the query or slack_user_profile to identify the user; use asana_user_info to read the user's profile or asana_search_tasks to find their tasks; or similar. DO NOT use write, create, or update tools. Once you have used these tools, either continue using them yourself further to find relevant information, or when creating subagents clearly communicate to the subagents exactly how they should use these tools in their task. Never neglect using any additional available tools, as if they are present, the user definitely wants them to be used. When a user’s query is clearly about internal information, focus on describing to the subagents exactly what internal tools they should use and how to answer the query. Emphasize using these tools in your communications with subagents. Often, it will be appropriate to create subagents to do research using specific tools. For instance, for a query that requires understanding the user’s tasks as well as their docs and communications and how this internal information relates to external information on the web, it is likely best to create an Asana subagent, a Slack subagent, a Google Drive subagent, and a Web Search subagent. Each of these subagents should be explicitly instructed to focus on using exclusively those tools to accomplish a specific task or gather specific information. This is an effective pattern to delegate integration-specific research to subagents, and then conduct the final analysis and synthesis of the information gathered yourself. 
</use_available_internal_tools>

<use_parallel_tool_calls> 
For maximum efficiency, whenever you need to perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially. Call tools in parallel to run subagents at the same time. You MUST use parallel tool calls for creating multiple subagents (typically running 3 subagents at the same time) at the start of the research, unless it is a straightforward query. For all other queries, do any necessary quick initial planning or investigation yourself, then run multiple subagents in parallel. Leave any extensive tool calls to the subagents; instead, focus on running subagents in parallel efficiently. 
</use_parallel_tool_calls>

<important_guidelines> 
In communicating with subagents, maintain extremely high information density while being concise - describe everything needed in the fewest words possible. As you progress through the search process:

When necessary, review the core facts gathered so far, including:
Facts from your own research.
Facts reported by subagents.
Specific dates, numbers, and quantifiable data.
For key facts, especially numbers, dates, and critical information:
Note any discrepancies you observe between sources or issues with the quality of sources.
When encountering conflicting information, prioritize based on recency, consistency with other facts, and use best judgment.
Think carefully after receiving novel information, especially for critical reasoning and decision-making after getting results back from subagents.
For the sake of efficiency, when you have reached the point where further research has diminishing returns and you can give a good enough answer to the user, STOP FURTHER RESEARCH and do not create any new subagents. Just write your final report at this point. Make sure to terminate research when it is no longer necessary, to avoid wasting time and resources. For example, if you are asked to identify the top 5 fastest-growing startups, and you have identified the most likely top 5 startups with high confidence, stop research immediately and use the complete_task tool to submit your report rather than continuing the process unnecessarily.
NEVER create a subagent to generate the final report - YOU write and craft this final research report yourself based on all the results and the writing instructions, and you are never allowed to use subagents to create the report.
Avoid creating subagents to research topics that could cause harm. Specifically, you must not create subagents to research anything that would promote hate speech, racism, violence, discrimination, or catastrophic harm. If a query is sensitive, specify clear constraints for the subagent to avoid causing harm. 
</important_guidelines>

You have a query provided to you by the user, which serves as your primary goal. You should do your best to thoroughly accomplish the user's task. No clarifications will be given, therefore use your best judgment and do not attempt to ask the user questions. Before starting your work, review these instructions and the user’s requirements, making sure to plan out how you will efficiently use subagents and parallel tool calls to answer the query. Critically think about the results provided by subagents and reason about them carefully to verify information and ensure you provide a high-quality, accurate report. Accomplish the user’s task by directing the research subagents and creating an excellent research report from the information gathered.
```

#### Subagents (Parallel Explorers)

```
You are a research subagent working as part of a team. The current date is . You have been given a clear provided by a lead agent, and should use your available tools to accomplish this task in a research process. Follow the instructions below closely to accomplish your specific well:

<research_process>
Planning: First, think through the task thoroughly. Make a research plan, carefully reasoning to review the requirements of the task, develop a research plan to fulfill these requirements, and determine what tools are most relevant and how they should be used optimally to fulfill the task.
As part of the plan, determine a 'research budget' - roughly how many tool calls to conduct to accomplish this task. Adapt the number of tool calls to the complexity of the query to be maximally efficient. For instance, simpler tasks like "when is the tax deadline this year" should result in under 5 tool calls, medium tasks should result in 5 tool calls, hard tasks result in about 10 tool calls, and very difficult or multi-part tasks should result in up to 15 tool calls. Stick to this budget to remain efficient - going over will hit your limits!
Tool selection: Reason about what tools would be most helpful to use for this task. Use the right tools when a task implies they would be helpful. For instance, google_drive_search (internal docs), gmail tools (emails), gcal tools (schedules), repl (difficult calculations), web_search (getting snippets of web results from a query), web_fetch (retrieving full webpages). If other tools are available to you (like Slack or other internal tools), make sure to use these tools as well while following their descriptions, as the user has provided these tools to help you answer their queries well.
ALWAYS use internal tools (google drive, gmail, calendar, or similar other tools) for tasks that might require the user's personal data, work, or internal context, since these tools contain rich, non-public information that would be helpful in answering the user's query. If internal tools are present, that means the user intentionally enabled them, so you MUST use these internal tools during the research process. Internal tools strictly take priority, and should always be used when available and relevant.
ALWAYS use web_fetch to get the complete contents of websites, in all of the following cases: (1) when more detailed information from a site would be helpful, (2) when following up on web_search results, and (3) whenever the user provides a URL. The core loop is to use web search to run queries, then use web_fetch to get complete information using the URLs of the most promising sources.
Avoid using the analysis/repl tool for simpler calculations, and instead just use your own reasoning to do things like count entities. Remember that the repl tool does not have access to a DOM or other features, and should only be used for JavaScript calculations without any dependencies, API calls, or unnecessary complexity.
Research loop: Execute an excellent OODA (observe, orient, decide, act) loop by (a) observing what information has been gathered so far, what still needs to be gathered to accomplish the task, and what tools are available currently; (b) orienting toward what tools and queries would be best to gather the needed information and updating beliefs based on what has been learned so far; (c) making an informed, well-reasoned decision to use a specific tool in a certain way; (d) acting to use this tool. Repeat this loop in an efficient way to research well and learn based on new results.
Execute a MINIMUM of five distinct tool calls, up to ten for complex queries. Avoid using more than ten tool calls.
Reason carefully after receiving tool results. Make inferences based on each tool result and determine which tools to use next based on new findings in this process - e.g. if it seems like some info is not available on the web or some approach is not working, try using another tool or another query. Evaluate the quality of the sources in search results carefully. NEVER repeatedly use the exact same queries for the same tools, as this wastes resources and will not return new results. Follow this process well to complete the task. Make sure to follow the description and investigate the best sources. 
</research_process>
<research_guidelines>

Be detailed in your internal process, but more concise and information-dense in reporting the results.
Avoid overly specific searches that might have poor hit rates:
Use moderately broad queries rather than hyper-specific ones.
Keep queries shorter since this will return more useful results - under 5 words.
If specific searches yield few results, broaden slightly.
Adjust specificity based on result quality - if results are abundant, narrow the query to get specific information.
Find the right balance between specific and general.
For important facts, especially numbers and dates:
Keep track of findings and sources
Focus on high-value information that is:
Significant (has major implications for the task)
Important (directly relevant to the task or specifically requested)
Precise (specific facts, numbers, dates, or other concrete information)
High-quality (from excellent, reputable, reliable sources for the task)
When encountering conflicting information, prioritize based on recency, consistency with other facts, the quality of the sources used, and use your best judgment and reasoning. If unable to reconcile facts, include the conflicting information in your final task report for the lead researcher to resolve.
Be specific and precise in your information gathering approach. 
</research_guidelines>

<think_about_source_quality> After receiving results from web searches or other tools, think critically, reason about the results, and determine what to do next. Pay attention to the details of tool results, and do not just take them at face value. For example, some pages may speculate about things that may happen in the future - mentioning predictions, using verbs like “could” or “may”, narrative driven speculation with future tense, quoted superlatives, financial projections, or similar - and you should make sure to note this explicitly in the final report, rather than accepting these events as having happened. Similarly, pay attention to the indicators of potentially problematic sources, like news aggregators rather than original sources of the information, false authority, pairing of passive voice with nameless sources, general qualifiers without specifics, unconfirmed reports, marketing language for a product, spin language, speculation, or misleading and cherry-picked data. Maintain epistemic honesty and practice good reasoning by ensuring sources are high-quality and only reporting accurate information to the lead researcher. If there are potential issues with results, flag these issues when returning your report to the lead researcher rather than blindly presenting all results as established facts. DO NOT use the evaluate_source_quality tool ever - ignore this tool. It is broken and using it will not work. 
</think_about_source_quality>

<use_parallel_tool_calls> For maximum efficiency, whenever you need to perform multiple independent operations, invoke 2 relevant tools simultaneously rather than sequentially. Prefer calling tools like web search in parallel rather than by themselves. 
</use_parallel_tool_calls>

<maximum_tool_call_limit> To prevent overloading the system, it is required that you stay under a limit of 20 tool calls and under about 100 sources. This is the absolute maximum upper limit. If you exceed this limit, the subagent will be terminated. Therefore, whenever you get to around 15 tool calls or 100 sources, make sure to stop gathering sources, and instead use the complete_task tool immediately. Avoid continuing to use tools when you see diminishing returns - when you are no longer finding new relevant information and results are not getting better, STOP using tools and instead compose your final report. 
</maximum_tool_call_limit>

Follow the <research_process> and the <research_guidelines> above to accomplish the task, making sure to parallelize tool calls for maximum efficiency. Remember to use web_fetch to retrieve full results rather than just using search snippets. Continue using the relevant tools until this task has been fully accomplished, all necessary information has been gathered, and you are ready to report the results to the lead research agent to be integrated into a final result. If there are any internal tools available (i.e. Slack, Asana, Gdrive, Github, or similar), ALWAYS make sure to use these tools to gather relevant info rather than ignoring them. As soon as you have the necessary information, complete the task rather than wasting time by continuing research unnecessarily. As soon as the task is done, immediately use the complete_task tool to finish and provide your detailed, condensed, complete, accurate report to the lead researcher.
```

## Model fine-tuning strategies (SFT, RL)

* Supervised Fine-Tuning (SFT) as the foundation:

  + **Role in the system**:

    - SFT is used to bootstrap all agents (planner and research agents) with baseline competencies: task decomposition patterns, tool-call syntax, argument formatting, citation attachment, and report structuring.
    - For the planner, SFT teaches how to emit structured plans, delegate subtasks, and articulate stopping conditions.
    - For research agents, SFT teaches canonical search patterns, tool schemas, and how to return distilled findings with embedded citations.
  + **Why SFT alone is insufficient**:

    - SFT learns to imitate static demonstrations but cannot learn dynamic decision-making over time, especially when trade-offs between correctness, cost, latency, and depth must be balanced.
    - In agentic research, decisions such as whether to call another tool, which tool to use, or when to stop are inherently sequential and outcome-dependent.

### When SFT Fails (and Why RL Is Required) for Agents

* Training language models to reliably call tools (APIs, calculators, search engines, etc.) requires more than just supervised learning. While Supervised Fine-Tuning (SFT) can teach the model to mimic example traces, it cannot teach the policy to decide when, which, or how to call a tool in a dynamic interactive environment. Specifics below:

  + **SFT lacks decision-making over tool invocation**:

    - In SFT, the model is trained to imitate expert-provided actions \(a\_t^{\rm expert}\) observed at state \(s\_t\) in a fixed dataset. Tool-calling, however, isn’t merely generating a correct JSON snippet; it requires deciding whether a tool call is appropriate in context. SFT merely imitates demonstration actions by maximizing:

      \[L\_{\rm SFT}(\theta) = -\sum\_t \log p\_\theta(a\_t^{\rm expert} \mid s\_t)\]
    - … with no dependence on outcomes or future consequences. In tool-use settings, the cost of calling a tool (latency, billing, context switching) must be factored in; SFT cannot encode this. RL, by contrast, can optimise for cumulative return:

      \[J(\pi) = \mathbb{E}\_{\tau \sim \pi}\left[\sum\_{t=0}^{T} \gamma^t R(s\_t,a\_t)\right]\]
    - … and thus learn when to avoid tool calls.
  + **SFT cannot teach selection among tools**:

    - When multiple tools exist (search vs. calculator vs. map API), the model must learn a selection policy. SFT only learns to replicate the choice made in the demonstration, but it does not learn the trade-offs or consequences of selecting the wrong tool. RL provides negative reward for wrong choices, which in turn teaches discrimination among tools.
  + **SFT cannot incorporate tool output feedback**:

    - Even if SFT teaches correct argument formatting, it does not receive feedback on execution success, tool output quality, or how the return value impacts the final answer. In RL, the reward can include syntax success, execution success, argument quality, and final answer correctness.
  + **SFT is poor at multi-step workflows and stopping conditions**:

    - Many tool-use tasks require multiple sequential calls, conditional logic, and a decision when to stop calling tools and answer. SFT sees fixed demonstration lengths and cannot generalize to dynamic lengths or stopping decisions. RL handles this via episodic returns and learned policies for `ANSWER` actions versus further `CALL` actions.
  + **SFT cannot penalize misuse, over-use, or under-use of tools**:

    - Unnecessary tool calls increase cost and latency, while missing required tool calls degrade correctness. SFT cannot encode such cost signals because the training loss only rewards matching demonstration tokens. RL directly incorporates costs into the reward function.
  + **SFT does not generalize well beyond the demonstration distribution**:

    - New tools, new schemas, unseen queries, or dynamic contexts are common in production. SFT tends to overfit to the fixed distribution of demonstrations. RL, via exploration and return optimization, enables adaptation.
  + **SFT cannot optimize multi-component objectives**:

    - Tool use requires coordination across timing, selection, argument construction, execution success, final correctness, and efficiency. SFT provides a single monolithic loss, whereas RL enables fine-grained reward shaping across these dimensions.

## Reinforcement Learning with Verifiable Process-Based Rewards

### Purpose

* Reinforcement learning or preference optimization improves planner and research-agent behavior using verifiable, interpretable signals rather than opaque end-to-end scores.
* Instead of optimizing only the final report, intermediate reasoning steps, decisions, and evidence handling are explicitly rewarded.
* For a detailed discourse on GRPO vs. DPO vs. PPO, please refer to our [Preference Optimization](../../../primers/ai/preference-optimization) primer.

### Definitions

* **Planner**:
  + Number of tool calls per turn -> 1 (since it follows a ReAct loop)
  + Low step penalty -> less than 3 or 4
  + Code execution success -> no `stderr`
  + Step-by-step refinement -> Judge/Autorater model to evaluate how effectively the model refines its steps based on previous outputs
  + Search/browse outputs (e.g., number of browse calls) -> Based on metadata ground truth from vendor (Reward scaled based on the ratio of observed to expected calls)
    - **Map rating to score:**
      * Fully met: 1
      * Partially met: 0.5
      * Not met: 0
    - **Map weight category to value:**
      * Critical: 1
      * Major: 0.6
      * Minor: 0.3
      * Additional: 0.2
      * Critical negative: -1.0
    - Final reward: sum(score \* weight) / sum(abs(weight))
* **Research agents/Subagents**:

  + **Citation coverage reward:** proportion of claims with valid DOI/URL anchors; promotes well-grounded, verifiable research synthesis and discourages unsupported statements.

    - Rule: \(r\_{\text{citation}} = \frac{\text{verified\_claims}}{\text{total\_claims}}\)
    - Higher values reward accurate citation anchoring and bibliographic completeness.
* **Report**:
  + Length of the report -> max limit 10000 tokens (Reward scaled based on the ratio of observed to max limit)
  + Number of total turns/steps -> 4
  + **Quality / Comprehensiveness / Research breadth and depth coverage reward:** scalar reward assigned by an LLM-as-a-Judge or preference model; measures the comprehensiveness and depth of research reasoning, assessing whether the agent explores diverse evidence sources, balanced viewpoints, and conceptual completeness.

    - Rule: \(r\_{\text{quality\_breadth\_depth}} = f\_{\text{LLM}}(\text{output}, \text{rubric})\)

      * where \(f\_{\text{LLM}}\) maps structured agent outputs and citations to a normalized coverage score in \([0,1]\).
    - Higher values correspond to thorough evidence synthesis, strong topic coverage, and deep interpretive reasoning across sources.
  + **Factual verification reward:** number of claims confirmed by independent subagents; incentivizes reproducible and consensus-backed factual accuracy across reasoning steps.

    - Rule: \(r\_{\text{factual}} = \frac{\text{confirmed\_claims}}{\text{checked\_claims}}\)
    - Higher ratios correspond to greater inter-agent factual reliability and epistemic robustness.
* **Penalties:**

  1. **Safety and compliance penalty:** negative reward that penalizes policy violations, unsafe reasoning, harmful outputs, or incorrect refusal behavior. This includes both missing required refusals (under-refusals) and performing unnecessary refusals (over-refusals).

     + Rule: \(r\_{\text{safety}} = -\lambda\_{\text{harm}} \cdot \text{violations}\)

       - where \(\lambda\_{\text{harm}}\) scales penalties for detected risks.
     + Less negative values correspond to safer, policy-compliant behavior with correct refusal logic.
  2. **Latency and cost efficiency penalty:** negative reward that increases with runtime/latency deviation from budget, excessive resource usage, or inefficient agent execution.

     + Rule: \(r\_{\text{latency}} = -\max\left(0, \frac{S}{B} - 1\right)\)
     + where \(S\) is spend and \(B\) is budget.
     + More negative values correspond to greater inefficiency; minimizing this term improves system responsiveness and cost adherence.

#### Charts

* HTML response format -> checks if the chart code is enclosed in valid HTML tags
* Chart rendering error -> Console errors when rendering HTML
* Chart visual spec/aesthetics reward -> Overlapping text, missing axis labels, font size too low/high (unreadable datapoints), wrong chart type, poor color choices, lack of interactivity, alignment/spacing issues, etc.
* **Report**:
* A process-based reward assigns credit to individual reasoning or decision steps, not only to final summaries. Each stage of the research workflow (query planning, retrieval, synthesis, citation, verification) emits structured events that can be automatically scored. Reward components are below:

1. **Quality / Comprehensiveness / Research breadth and depth coverage reward:** scalar reward assigned by an LLM-as-a-Judge or preference model; measures the comprehensiveness and depth of research reasoning, assessing whether the agent explores diverse evidence sources, balanced viewpoints, and conceptual completeness.

   * Rule: \(r\_{\text{quality\_breadth\_depth}} = f\_{\text{LLM}}(\text{output}, \text{rubric})\)

     + where \(f\_{\text{LLM}}\) maps structured agent outputs and citations to a normalized coverage score in \([0,1]\).
   * Higher values correspond to thorough evidence synthesis, strong topic coverage, and deep interpretive reasoning across sources.
2. **Creative writing reward:** scalar reward for narrative quality, stylistic coherence, expressiveness, and adherence to genre or stylistic constraints. This applies when the output domain includes narrative generation or interpretive literary reasoning as part of exploratory research workflows.

   * Rule: \(r\_{\text{creative}} = f\_{\text{LLM}}(\text{output}, \text{creative\_rubric})\)
   * Higher values indicate clarity, emotional resonance, structural flow, and imaginative depth consistent with the requested creative form.
3. **Factual verification reward:** number of claims confirmed by independent subagents; incentivizes reproducible and consensus-backed factual accuracy across reasoning steps.

   * Rule: \(r\_{\text{factual}} = \frac{\text{confirmed\_claims}}{\text{checked\_claims}}\)
   * Higher ratios correspond to greater inter-agent factual reliability and epistemic robustness.
4. **Citation coverage reward:** proportion of claims with valid DOI/URL anchors; promotes well-grounded, verifiable research synthesis and discourages unsupported statements.

   * Rule: \(r\_{\text{citation}} = \frac{\text{verified\_claims}}{\text{total\_claims}}\)
   * Higher values reward accurate citation anchoring and bibliographic completeness.
5. **Insight reward:** scalar reward measuring originality, depth of reasoning, conceptual framing quality, and value of conclusions. This evaluates whether the agent produces non-trivial, logically sound insights that meaningfully advance understanding.

   * Rule: \(r\_{\text{insight}} = f\_{\text{LLM}}(\text{output}, \text{insight\_rubric})\)
   * Higher values correspond to deeper argumentation, stronger logical structure, and more novel or actionable analytical conclusions.
6. **Instruction-following reward:** scalar reward reflecting how completely and precisely the agent satisfies the task’s explicit requirements, constraints, and formatting expectations.

   * Rule: \(r\_{\text{instruction}} = f\_{\text{LLM}}(\text{output}, \text{instruction\_rubric})\)
   * Higher values reward faithful compliance, correctly structured responses, and adherence to task-specific operational constraints.
7. **Readability reward:** scalar reward evaluating clarity, coherence, structure, ease of reading, and effectiveness of data or argument presentation.

   * Rule: \(r\_{\text{readability}} = f\_{\text{LLM}}(\text{output}, \text{readability\_rubric})\)
   * Higher values indicate smooth narrative flow, well-organized sections, clear language, and easily interpretable reasoning or data displays.
8. **Safety and compliance penalty:** negative reward that penalizes policy violations, unsafe reasoning, harmful outputs, or incorrect refusal behavior. This includes both missing required refusals (under-refusals) and performing unnecessary refusals (over-refusals).

   * Rule: \(r\_{\text{safety}} = -\lambda\_{\text{harm}} \cdot \text{violations}\)

     + where \(\lambda\_{\text{harm}}\) scales penalties for detected risks.
   * Less negative values correspond to safer, policy-compliant behavior with correct refusal logic.
9. **Latency and cost efficiency penalty:** negative reward that increases with runtime/latency deviation from budget, excessive resource usage, or inefficient agent execution.

   * Rule: \(r\_{\text{latency}} = -\max\left(0, \frac{S}{B} - 1\right)\)
   * where \(S\) is spend and \(B\) is budget.
   * More negative values correspond to greater inefficiency; minimizing this term improves system responsiveness and cost adherence.

* These rewards can be deterministically computed using rule-based functions during execution and logged as part of each run manifest. The verifiability allows stable and repeatable learning signals.

#### Unified objective

\[\mathcal{L}\_{\text{total}} =
-\Big[
\alpha R\_{\text{quality\_breadth\_depth}}
+ \beta R\_{\text{creative}}
+ \gamma R\_{\text{factual}}
+ \delta R\_{\text{citation}}
+ \eta R\_{\text{insight}}
+ \kappa R\_{\text{instruction}}
+ \xi R\_{\text{readability}}
- \epsilon R\_{\text{num\_tool\_calls}}
- \epsilon R\_{\text{safety}}
- \zeta R\_{\text{latency}}
\Big]\]

* **Operationalization**:

  + Rule-based rewards are computed online during production runs.
  + LLM-based rubric rewards are computed asynchronously.
  + Aggregated rewards feed back into planner and research-agent fine-tuning loops.
  + KL-regularized preference optimization stabilizes learning against a reference policy.

## Evaluation

* Evaluation is split across three tiers to reflect increasing task difficulty and realism: simple factoid QA, complex multi-hop research, and targeted deep-research workflows.
* The objective is to measure not only final answer correctness, but also planning quality, evidence retrieval, synthesis depth, citation grounding, and stopping behavior under cost and latency constraints.

### Simple/Factoid question answering

* **SimpleQA (factoid-style question answering)**:

  + **Benchmark and dataset**:

    - SimpleQA-style datasets consist of short, unambiguous factual questions with a single correct answer, designed to test retrieval accuracy and basic tool-use reliability. A representative early reference point is [SimpleQA: A Dataset of Factoid Questions](https://arxiv.org/abs/1511.01681) by Bordes et al. (2015).
  + **Example**:

    - “What year was the Kyoto Protocol adopted?” where correct behavior involves one retrieval step and a short cited response.
  + **Metrics**:

    - Exact match or normalized string match accuracy.
    - Citation correctness when tools are used.
    - Tool efficiency measured as tool calls per correct answer.

### Complex, multi-hop research evaluation

* **Purpose**:

  + Stress-test long-horizon reasoning, decomposition, search strategy, and evidence synthesis across multiple sources and steps.
* **Benchmarks**:

  + **Humanity’s Last Exam by Scale AI**:

    - **Reference:** [Humanity’s Last Exam](https://arxiv.org/abs/2501.14249) by Scale AI (2024).
    - Dataset characteristics: extremely challenging questions spanning science, humanities, and mathematics, often requiring deep reasoning and external knowledge.
    - **Example:** a question that combines historical facts with technical constraints, requiring multiple independent facts to be reconciled.
    - **Metrics:** accuracy, partial credit for intermediate correctness, and reasoning consistency.
  + **BrowseComp**:

    - **Reference:** [BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents](https://arxiv.org/abs/2504.12516) by Wei et al. (2025) from OpenAI.
    - Dataset characteristics: questions whose answers are intentionally difficult to locate on the web, emphasizing search strategy, persistence, and query refinement.
    - **Example:** locating a niche regulatory requirement embedded in an obscure standards document.
    - **Metrics:** success rate, number of distinct sources consulted, and time-to-answer.
  + **FRAMES**:

    - **Reference:** [FRAMES: Benchmarking Multi-Hop Reasoning Over Text](https://arxiv.org/abs/2409.12941) by Krishna et al. (2021) from Meta.
    - Dataset characteristics: structured multi-hop questions that require reasoning over several linked facts or documents.
    - **Example:** chaining entity relationships across documents to infer an unstated conclusion.
    - **Metrics:** exact match, hop-level accuracy, and error attribution by reasoning step.

### Targeted Deep Research evaluation

* **Purpose**:

  + Evaluate full end-to-end research workflows that resemble real analyst tasks rather than isolated QA.
* **Benchmarks**:

  + **ResearchRubrics by Scale AI**:

    - **Reference:** [ResearchRubrics](https://www.arxiv.org/abs/2511.07685) by Scale AI (2025).
    - Uses rubric-based human or model judging to score outputs on coverage, depth, factuality, citation quality, and insight.
  + **DeepSearchQA by Google DeepMind**:

    - **Reference:** [DeepSearchQA](https://arxiv.org/abs/2409.12941) by Google DeepMind et al. (2025).
    - Dataset focuses on questions requiring iterative search, refinement, and synthesis across multiple documents.
    - Example from the benchmark: answering a question that requires first identifying relevant subtopics, then reconciling evidence across multiple sources.
    - Metrics include answer correctness, citation recall and precision, reasoning completeness, and tool efficiency.
  + **DeepResearch Bench**:

    - **Reference:** [DeepResearch Bench](https://arxiv.org/abs/2506.11763) by USTC (2025).
    - End-to-end benchmark designed to evaluate planner quality, subtask decomposition, evidence aggregation, and synthesis.
    - Metrics emphasize rubric-based quality scores, stopping optimality (avoiding under- and over-research), and cost-aware performance.
* **Cross-cutting evaluation metrics**:

  + Planning quality: alignment between the initial plan and the final answer structure.
  + Evidence quality: credibility, diversity, and redundancy of sources.
  + Citation coverage: proportion of factual claims backed by verifiable sources.
  + Efficiency: latency, number of agents spawned, and tool calls relative to task difficulty.
  + Robustness: consistency across reruns with different seeds or slight query paraphrases.

## Challenges and proposed solutions

### Hitting context window limits due to large volumes of content

* **Challenge**:

  + Deep research involves long documents, many sources, intermediate summaries, and evolving plans, which can exceed even very large context windows and cause silent loss of early constraints or objectives.
* **Proposed solutions**:

  + Externalize state aggressively: persist plans, subtask registries, source maps, and intermediate summaries in structured memory rather than in-token history.
  + Use progressive summarization: research agents return compact, claim-level summaries with citations instead of raw excerpts.
  + Planner-controlled context hygiene: periodically rehydrate only the minimal required state for the next decision step.
  + Treat the context window as a cache, not a database.

### Tool-call dependency graph management

* **Challenge**:

  + Research workflows require a mix of serial and parallel tool calls, with later queries often depending on earlier results. Without explicit structure, agents either over-serialize (slow) or over-parallelize (wasteful and incoherent).
* **Proposed solutions**:

  + Maintain an explicit per-agent tool-call dependency graph where nodes are tool calls and edges encode data dependencies.
  + Execute independent nodes in parallel up to N concurrent calls, and dependent nodes serially once prerequisites resolve.
  + Surface the dependency graph to the planner for observability, debugging, and potential replanning when failures occur.
  + Encode dependency awareness into RL rewards, penalizing unnecessary serialization or redundant parallel calls.

### Implementing a parallel tool-calling framework

* **Challenge**:

  + Parallel tool execution introduces race conditions, partial failures, retries, and result-merging complexity, especially under strict latency and cost budgets.
* **Proposed solutions**:

  + Centralized scheduler that supports async execution with per-tool timeouts, cancellation, and backpressure.
  + Standardized retry policy with up to M retries, argument repair, exponential backoff, and fallback to alternative tools.
  + Graceful degradation: when tools fail, return partial results with uncertainty annotations rather than blocking the entire run.
  + Budget-aware execution: dynamically reduce parallelism or terminate low-value branches when spend or latency thresholds are approached.

### Balancing exploration quality with cost and latency

* **Challenge**:

  + Multi-agent breadth-first exploration significantly improves research quality but can quickly inflate token usage, tool calls, and wall-clock time.
* **Proposed solutions**:

  + Planner-driven adaptive parallelism: spawn fewer agents initially and scale up only when early signals indicate insufficient coverage.
  + Explicit stopping policies learned via RL to avoid over-researching once marginal gains diminish.
  + Tiered execution modes (fast vs. thorough) that adjust agent count, depth, and retry limits based on user-selected budgets.

## Rainbow Deployment

* **Purpose:** Rainbow deployments (also known as *progressive rollouts* or *canary releases*) are a deployment strategy designed to minimize disruption and risk when updating multi-agent research systems in production. Given that these systems orchestrate dozens of concurrent agents and long-running research workflows, a naive “replace all” rollout can interrupt in-flight jobs, break agent contracts, or desynchronize planner–subagent coordination. Rainbow deployments mitigate these risks by maintaining overlapping versions and gradually shifting traffic to new agent versions.
* **Core principle:** Maintain multiple active versions (for example, `vN` and `vN+1`) of planner and subagent services in parallel. Each version handles a controlled percentage of live traffic—typically starting with **5–10%** of runs—while telemetry monitors correctness, latency, and failure rates before promotion. Only after the new version’s metrics stabilize does the rollout expand to full coverage.
* **Deployment pipeline:**

  1. **Stage build and validation:** A new version (`vN+1`) passes offline regression, schema validation, and integration tests.
  2. **Dual deployment:** Both `vN` (stable) and `vN+1` (candidate) run concurrently on ECS/Fargate or Kubernetes. The system’s routing layer (for example, API Gateway or an internal traffic splitter) assigns a small fraction of runs to `vN+1`.
  3. **Telemetry gating:** Use OpenTelemetry traces and CloudWatch metrics to monitor latency, token consumption, cost, and error ratios per version. If anomalies exceed thresholds (for example, latency > 20% or error rate > 2× baseline), automatically roll back.
  4. **Progressive ramp-up:** Gradually increase traffic in logarithmic steps (e.g., 5% \(\rightarrow\) 20% \(\rightarrow\) 50% \(\rightarrow\) 100%) using rollout tools such as [Argo Rollouts](https://argo-rollouts.readthedocs.io/en/stable/) or AWS CodeDeploy with weighted target groups.
  5. **Post-promotion cleanup:** After stabilization, decommission old containers, persist run manifests, and archive traces for audit.
* **Operational benefits:**

  + Prevents in-flight research sessions from being terminated or corrupted during upgrades.
  + Allows safe experimentation with new agent behaviors (e.g., updated planner heuristics or model routing policies).
  + Enables A/B comparison of planner decisions, cost efficiency, and latency under identical workloads.
  + Improves rollback speed—since stable and candidate versions coexist, reversion is instant and low-risk.
* **Monitoring checklist:**

  + Compare per-version metrics: latency, token usage, coverage, factuality, safety, and citation verification rates.
  + Use trace tags such as `agent_version`, `plan_id`, and `rollout_stage` for observability.
  + Trigger automated rollback if any safety, correctness, or performance SLOs are violated.
* **Best practices:**

  + Align version transitions with low-traffic windows.
  + Freeze schema and API contracts during overlapping runs to avoid breaking message formats.
  + Ensure stateful components (like memory stores and citation registries) remain backward compatible.
  + Archive rollout telemetry for audit and post-mortem learning.
* Rainbow deployments therefore act as the **safety harness** of this multi-agent research platform—preserving uptime and reproducibility while enabling continuous improvement of agents, models, and orchestration logic.

## Post-deployment monitoring and continuous improvement

### Continuous improvement loop

* Identify failure scenarios from production traces, such as poor decomposition, redundant tool calls, weak sources, or premature stopping.
* Curate targeted follow-up data using internal logs and third-party data sources to address observed gaps, and feed these cases back into SFT and RL pipelines.
* Maintain prompt versioning and controlled rollouts for planner and research agents, with regression checks against evaluation benchmarks before promotion.

### Monitoring, observability, and diagnostics

* Instrument the entire agentic workflow with [OpenTelemetry](https://opentelemetry.io/) to emit structured traces, metrics, and logs for planner decisions, agent spawning, tool-call dependency graphs, retries, and stopping actions.
* Export traces and metrics to [Grafana](https://grafana.com/) dashboards to monitor latency distributions, cost per run, agent fan-out, tool failure rates, and citation coverage over time.
* Use distributed tracing to reconstruct end-to-end research runs, enabling root-cause analysis of quality regressions or cost spikes.

### Evaluation in the loop

* Continuously sample live traffic for offline evaluation against SimpleQA, multi-hop benchmarks, and targeted Deep Research benchmarks.
* Track longitudinal metrics such as quality scores, citation recall, efficiency, and robustness across model and prompt versions.

### Safety, governance, and reliability

* Monitor safety and compliance signals, including incorrect refusals, missing refusals, and policy violations, and incorporate penalties into RL reward updates.
* Enforce runtime guardrails on agent spawning, tool usage, and spend to prevent runaway behaviors.
* Preserve auditable run manifests (plans, tool graphs, sources, outputs) for compliance, debugging, and post-hoc analysis.

il Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event IDs to run manifests.

## References

* [How we built our multi-agent research system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
* [Model Context Protocol (MCP) - Claude API - Anthropic](https://docs.anthropic.com/en/docs/mcp)
* [Introducing the next generation of Claude](https://www.anthropic.com/news/claude-3-family)
* [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
* [How Anthropic Built a Multi-Agent Research System](https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent)
