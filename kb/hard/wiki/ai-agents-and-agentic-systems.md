---
concept: AI Agents & Agentic Systems
tags: [agents, agentic-ai, tool-use, planning, mcp]
sources:
  - kb/hard/raw/aman-ai/primers-agents.md
  - kb/hard/raw/aman-ai/primers-agentic-design-patterns.md
  - kb/hard/raw/chip-huyen/agents.md
  - kb/hard/raw/lilian-weng/llm-powered-autonomous-agents.md
  - kb/hard/raw/cameron-wolfe/ai-agents-from-first-principles.md
last_compiled: 2026-04-05
related:
  - "[[hard/wiki/large-language-models|Large Language Models]]"
  - "[[hard/wiki/retrieval-augmented-generation|Retrieval-Augmented Generation]]"
  - "[[hard/wiki/llm-evaluation|LLM Evaluation]]"
understanding: 3  # proven depth (demonstrated in dialogue/practice, or authored)
relevance: 3  # very relevant
knowledge_updated: 2026-09-07
---

# AI Agents & Agentic Systems

An agent is anything that perceives its environment and acts upon it. In the AI context, an LLM-powered agent uses a language model as the reasoning core, augmented with tools, memory, and planning capabilities to accomplish multi-step tasks autonomously. The key upgrade over a static LLM: the system can iterate, observe outcomes, and adjust — rather than producing a single response and stopping.

The classic book *AI: A Modern Approach* (Russell & Norvig, 1995) defined the field of AI research as "the study and design of rational agents." Foundation models have finally made that goal tractable at a practical level.

## What Makes a System Agentic

A static LLM call: one prompt in, one response out. An agentic system:
- Can **perceive** the environment (read files, call APIs, search the web)
- Can **act** upon the environment (write code, send emails, update databases)
- **Loops** — produces intermediate outputs, observes results, decides what to do next
- Maintains **state** across steps

The clearest marker of agency is the loop: the model's output feeds back as input, driving continued action until a terminal condition is met.

A RAG system is a simple agent — its tools are a text retriever, an image retriever, and an SQL executor. ChatGPT with web search is an agent. SWE-agent (built on GPT-4) is a coding agent whose environment is a terminal and file system, with actions like navigate, search, view, and edit.

## Core Design Patterns

**ReAct (Reasoning + Acting):** The foundational framework for LLM agents. The model interleaves *Thought* and *Action* steps in its output. A thought is a special kind of action — it lets the model plan explicitly before acting. The pattern:
1. Observe current state
2. Think: "I need to find X. I'll search for Y first."
3. Act: call a tool
4. Observe: process tool output
5. Repeat until terminal action

ReAct enables language to serve as both the reasoning medium and the communication protocol. The agent explains its reasoning trace in natural language, making it interpretable.

**Reflection:** The agent critiques its own output and revises. Self-Refine, Reflexion, and CRITIC all implement variants. A reflection loop: generate → critique → revise → repeat. Multi-agent reflection uses a separate critic agent to evaluate the generator's output, avoiding self-serving evaluations.

**Tool Use:** Tools expand the agent's capability beyond text generation. Categories:
- *Knowledge augmentation:* text retriever, SQL executor, web search, internal APIs
- *Capability extension:* calculator, code interpreter, translator, calendar
- *Write actions:* email sender, database writer, form submitter

Tools can be integrated via fine-tuning (early approaches like Toolformer) or prompt-based function calling (modern standard). Modern function calling: describe available tools in the prompt; the LLM generates a structured tool call; the system executes it and returns results to the context.

**Planning:** Complex tasks require decomposing into subtasks. Planning involves generating a sequence of steps, validating the plan (via heuristics or an AI judge), and executing. Crucially: planning and execution should be decoupled. Generate a plan first, validate it, then execute — otherwise the agent can burn API credits on a flawed plan for hours. Key planning types: sequential (step by step), hierarchical (decompose into subtasks), reactive (plan incrementally based on observations).

**Multi-agent systems:** Architectures where multiple specialized agents collaborate:
- *Supervisor (centralized):* One orchestrator routes tasks to specialized sub-agents
- *Network (decentralized):* Agents communicate peer-to-peer
- *Hierarchical:* Supervisors oversee supervisors, enabling complex workflows

Multi-agent is not always better — single agents preserve context, are simpler to debug, and avoid coordination overhead. Use multi-agent when tasks naturally decompose into non-overlapping specializations.

## Agentic Workflow Patterns

**Prompt chaining:** Output of step N is input to step N+1. Enables complex pipelines where each LLM call focuses on one task. Failure compounds — errors early propagate through the chain.

**Routing:** An intent classifier directs queries to specialized handlers. Enables cost optimization (simple queries → cheap models) and specialization (billing queries → billing agent). Router models are typically small and fast.

**Parallelization:** Independent subtasks run concurrently; results are aggregated. Reduces wall-clock time for decomposable tasks.

**Orchestrator-Workers:** A central orchestrator breaks down the task and delegates to specialized workers. Workers return results; orchestrator synthesizes.

**Evaluator-Optimizer:** An evaluator scores the generator's output; if it fails quality thresholds, the optimizer generates a revised version. Loop until pass or max iterations.

## Memory Systems

Memory is what enables agents to maintain state across turns and sessions. Four types:

- **In-context (working) memory:** The current token window. Fast, but limited and ephemeral.
- **External short-term (episodic):** Conversation history, recent actions — stored externally and retrieved as needed.
- **Long-term semantic memory:** Persistent knowledge base, typically a vector store. Semantically similar past experiences retrieved by embedding similarity.
- **Long-term structured memory:** Database or file-based logs — precise, temporal, queryable. Less flexible than vector memory but fully verifiable.

Hybrid memory systems combine vector retrieval (for fuzzy semantic search) with structured logs (for precise episodic recall). The choice depends on whether retrieval needs to be semantic or exact.

## Failure Modes

Agents fail in characteristic ways that differ from single-call LLMs:

**Compound errors:** Multi-step accuracy degrades multiplicatively. At 95% accuracy per step, a 10-step task succeeds 60% of the time; at 100 steps, 0.6%. More steps = lower reliability. This pushes toward shorter plans with validation gates.

**Tool misuse:** Agents call the wrong tool, pass wrong parameters, or misinterpret tool outputs. Particularly bad when agents have access to many similar tools.

**Infinite loops:** Without a well-defined terminal condition, agents can loop indefinitely. Mitigation: step limits, explicit goal-checking, human checkpoints.

**Prompt injection:** Malicious content in retrieved documents or tool outputs that hijacks the agent's behavior. Especially dangerous when agents have write access.

**Hallucinated tool calls:** Agent invents a tool call to a non-existent function, or generates plausible-sounding but wrong parameters.

## Evaluation

Evaluating agents is harder than evaluating single LLM outputs because correctness is trajectory-dependent:

**Pass@k:** Run the task k times; success if at least one run completes correctly. Accounts for sampling variance.

**Trajectory evaluation:** Does the sequence of actions make sense? Were tool calls appropriate? Did the agent explore efficiently or wastefully?

**Outcome evaluation:** Did the agent accomplish the stated goal? For software tasks (SWE-bench): does the code pass the test suite?

**Human-in-the-loop benchmarks:** For open-ended tasks, human raters evaluate whether the final output meets the user's intent.

The Berkeley Function-Calling Leaderboard evaluates tool use specifically — assessing whether models generate correct, executable function calls across diverse APIs and programming languages.

## Model Context Protocol (MCP)

MCP (Anthropic, 2024) standardizes how external systems provide context to LLMs. Rather than each integration requiring custom code, MCP defines a universal format: tool schemas, resource descriptions, and prompt templates. Developers publish "MCP servers" — pre-built integrations for specific data sources (GitHub, Slack, databases) that any MCP-compatible LLM client can consume.

The practical value: dramatically reducing the integration tax for adding new tools to agent systems. Instead of N×M integrations (N models × M tools), MCP enables N+M (each model and tool implements the standard once).

## Production Considerations

**Write actions require trust:** Read-only tools are low-risk; write actions (database mutations, email sending, financial transactions) require explicit human approval gates. The principle of least privilege applies — agents should have the minimum write access required for their task.

**Latency-accuracy tradeoff:** More planning and self-correction steps improve accuracy but increase latency. Production systems tune the number of reflection cycles based on task stakes.

**Cost management:** Multi-step agents can consume disproportionate API credits. Routing simple queries to cheaper models, caching intermediate results, and strict step budgets are essential cost controls.

**Monitoring:** Log every action, observation, and intermediate LLM call. Agent behavior is much harder to debug without complete traces. LangSmith, Weave, and similar tools provide trace visualization for agentic workflows.

## Sources

- Aman Chadha. *Primers: Agents* — agent framework (core, memory, tools, planning), design patterns, MCP, A2A protocol, agentic RAG, responsible AI agents
- Aman Chadha. *Primers: Agentic Design Patterns* — what makes a system agentic, all major patterns with failure modes, state/adaptation/control, human-in-the-loop
- Chip Huyen. *Agents* — agent definition, tool categories, planning as search, multi-step accuracy degradation, evaluation approaches
- Lilian Weng. *LLM Powered Autonomous Agents* — planning/memory/tool-use framework, subgoal decomposition, reflection and refinement
- Cameron Wolfe. *AI Agents from First Principles* — tool use evolution (finetuning → prompting), ReAct framework, reasoning models, MCP standardization
