---
concept: AI Agents and Agentic Systems
tags: [agents, agentic-ai, tool-use, planning, multi-agent, mcp, react, reinforcement-learning]
sources:
  - kb/hard/raw/aman-ai/primers-agents.md
  - kb/hard/raw/aman-ai/primers-agentic-design-patterns.md
  - kb/hard/raw/aman-ai/primers-agentic-reinforcement-learning.md
  - kb/hard/raw/aman-ai/models-toolformer.md
  - kb/hard/raw/aman-ai/primers-computer-control.md
  - kb/hard/raw/chip-huyen/agents.md
  - kb/hard/raw/eugene-yan/building-news-agents-for-daily-news-recaps-with-mcp-q-and-tmux.md
  - kb/hard/raw/simon-willison/highlights-from-my-conversation-about-agentic-engineering-on-lennys-podcast.md
last_compiled: 2026-04-05
related: [large-language-models, retrieval-augmented-generation, llm-evaluation]
---

# AI Agents and Agentic Systems

An agent is anything that can perceive its environment and act upon it. In AI systems, the LLM is the *brain* — reasoning about tasks, planning action sequences, and deciding when goals have been met. The *environment* defines what tools are available and what the agent can affect. This distinction is central: a simple chatbot responds; an agent acts.

## What Makes a System "Agentic"

The boundary between a pipeline and an agent is autonomy. Anthropic's framework distinguishes two architectures:

- **Workflows**: LLMs and tools orchestrated through predefined code paths. Deterministic, auditable.
- **Agents**: LLMs that dynamically direct their own processes — choosing tools, managing subtasks, revising plans based on feedback.

The key enabling conditions for agentic behavior are (1) tool access, (2) planning ability, (3) a memory system that persists context across steps, and (4) a feedback loop so the agent can revise its behavior. Without all four, you have a sophisticated pipeline, not an agent.

Single-shot LLM calls produce text. Agents produce *outcomes* by chaining actions over time. This creates the compound-mistake problem: at 95% per-step accuracy, a 10-step task hits ~60% success; a 100-step task drops to 0.6%. More capable models — or tighter loops with reflection — are required as task complexity grows.

## Core Architecture: The Agent Loop

A typical agent operates in a cycle:

1. **Perceive** — receive a task or new environmental signal
2. **Plan** — decompose the task into manageable steps; select tools
3. **Execute** — invoke tools via function calling; take actions
4. **Observe** — receive tool outputs; update internal state
5. **Reflect** — evaluate progress; revise the plan or terminate

This loop maps cleanly to **ReAct** (Yao et al., 2022), the foundational pattern that interleaves Thought → Action → Observation at each step. ReAct let agents update plans based on observations rather than committing to an upfront plan, significantly improving multi-step task accuracy.

### Planning and Execution Decoupling

A critical design principle: separate plan generation from execution. Generate a plan first, validate it (check for invalid tools, unreasonable step counts, constraint violations), then execute. Without this, an agent can run 100 steps toward a bad plan before anyone notices. Plans can be validated via heuristics or an AI judge.

Planning granularity is a tradeoff: specific function-level plans are easier to execute but brittle to API changes; natural-language plans are more robust but need a translation layer. Hierarchical planning — high-level plan → per-subtask plans — is common for complex tasks.

Control flows extend beyond sequential: **parallel** execution (fetch multiple data sources simultaneously), **if/else routing** (Anthropic calls this "routing"), and **for loops** (repeat until a stopping condition). Parallel execution is a key latency lever for production agents.

## The Four Core Design Patterns

From Andrew Ng's widely-cited framing (echoed across sources):

1. **Reflection** — the agent evaluates its own output, identifies errors, and produces revised outputs. Reflexion (Shinn et al., 2023) formalizes this with an evaluator (scores outcomes) and a self-reflection module (diagnoses what went wrong). Can be done with a single agent via self-critique prompts, or as a two-agent setup (generator + critic). Low implementation cost, high ROI.

2. **Tool Use** — agents invoke external functions: web search, code execution, SQL queries, calculators, APIs. Introduced systematically by **Toolformer** (Schick et al., 2023), which trained GPT-J to self-supervise tool call insertion: sample candidate API calls, execute them, filter by whether they reduce prediction loss, finetune on the augmented dataset. Toolformer showed LLMs can decide *when* and *how* to use tools without heavy annotation. Core limitation: tool calls are independent (no chaining), and models are sensitive to exact input wording.

3. **Planning** — structured task decomposition before execution. Tree of Thoughts and similar approaches treat planning as search: enumerate paths, predict outcomes, prune bad branches. The key open question (Yann LeCun's position) is whether autoregressive LLMs can truly plan or only approximate it. Empirically: better models + better prompting + reflection get you far enough for most production tasks.

4. **Multi-Agent** — specialized agents collaborate, each handling a subproblem. Common patterns: orchestrator + worker agents (orchestrator decomposes, workers execute), generator + critic (one produces, one evaluates), or peer specialists (coding agent, QA agent, etc.). Frameworks: AutoGen, CrewAI, LangGraph, MetaGPT.

## Tool Use, Function Calling, and MCP

Tools divide into three categories: **knowledge augmentation** (retrieval, web search, SQL, email readers), **capability extension** (calculators, code interpreters, translators), and **write actions** (database writes, email senders, banking APIs). Write actions require careful trust calibration — automate read-only freely, gate writes behind approval.

Function calling APIs follow a standard flow: declare tools with names, parameter schemas, and documentation; receive structured `tool_calls` responses; execute and feed results back. Inspect parameter values — models frequently hallucinate parameter contents even when they select the right function. More tools ≠ better agents: each tool adds selection difficulty and hallucination surface.

**MCP (Model Context Protocol)** is Anthropic's open standard for LLM-to-tool connectivity — "the USB-C of AI integration." MCP standardizes the client-server layer between host apps (Claude Desktop, IDEs), protocol clients, and MCP servers (lightweight processes exposing capabilities). Why it became the de facto standard: AI-native design (unlike OpenAPI/GraphQL), major lab backing, built on the proven Language Server Protocol, and launched with complete first-party tooling.

## Memory Systems

Three timescales: **short-term** (in-context window — volatile, bounded by context length), **long-term** (vector databases like Pinecone/Weaviate — persistent across sessions, retrieved by semantic similarity weighted by recency), and **episodic** (prior task trajectories, used to avoid repeating mistakes). In-context reasoning + external retrieval is what enables tasks that exceed the context window. See [[hard/wiki/retrieval-augmented-generation|Retrieval-Augmented Generation]].

## Failure Modes

Agents fail in distinct ways: **invalid tool calls** (hallucinated function names), **valid tool / wrong parameters**, **goal failure** (steps complete but objective missed, or constraints ignored), **reflection failure** (agent incorrectly believes task is done), **efficiency failure** (correct outcome via wasteful path), **infinite loops** (no stopping condition fires), and **prompt injection** (malicious content in tool outputs hijacks subsequent actions — the "lethal trifecta": capable agent + write access + unsanitized inputs).

Willison's framing: "97% effectiveness is a failing grade" for high-stakes agents. Tail failures are severe — unauthorized transactions, deleted data, wrong emails at scale.

## Evaluation

Agent evaluation is two-dimensional: **outcome-wise** (did the goal get achieved?) and **process-wise** (did the agent take an efficient, correct path?). A right answer via a bad trajectory is a reliability risk.

For planning evaluation, measure over a (task, tool inventory) dataset: % valid plans generated, plans needed before a valid one, % tool calls with correct parameters. Ablate by task type and tool to isolate weaknesses.

**Key metrics**: success rate, action accuracy (% correct tool calls), trajectory efficiency (steps to completion), robustness under distribution shift.

**Benchmarks**: SWE-Bench (code), OSWorld (computer use), WebArena (browser), GAIA (general multi-domain), Mind2Web.

**pass@k**: generate k completions; score if ≥1 passes. Measures possibility of success, not reliability — useful for coding tasks, misleading for production agents where every call must succeed.

## Agentic Reinforcement Learning

SFT alone is insufficient for production agents — it teaches imitation but cannot encode when to call a tool, which tool to pick, or the cost of unnecessary calls. RL optimizes for cumulative return over full episode trajectories.

Key components:

- **Reward decomposition**: separate signals for (1) when to call a tool, (2) which tool, (3) argument quality, (4) execution success, (5) final task success
- **Asymmetric rewards**: penalize incorrect calls more than missed calls — asymmetry stabilizes PPO/GRPO training
- **Curriculum**: SFT bootstrapping → binary tool-invocation → tool selection → argument construction → multi-step pipelines
- **Process-wise vs. outcome-based**: outcome rewards ensure goal fidelity but are sparse; process rewards provide dense signal

PPO is standard. GRPO samples groups of completions and uses relative advantage, avoiding a separate value model.

## Computer Use and Browser Agents

Agents that control computer interfaces directly. Three paradigms:

- **Anthropic Computer Use** (Claude): full desktop control — cursor, clicks, multi-app workflows. Runs locally; user must cede control during execution.
- **OpenAI Operator**: browser-only, cloud-based. More constrained but safe.
- **Manus**: independent virtual environment with browser, terminal, and code execution. SOTA on GAIA.

Core challenge: visual grounding (identifying correct UI elements). **OmniParser v2** converts UI screenshots into structured elements, lifting GPT-4o from 0.8% to 39.6% accuracy on ScreenSpot Pro.

Key benchmarks: OSWorld (open-ended OS tasks), WebArena (browser), WebVoyager (autonomous web exploration), GAIA (general multi-domain).

## Production Considerations

**Cost and latency**: token burn scales with reasoning depth, reflection cycles, and tool roundtrips. Parallel tool execution is the primary latency lever. Monitor cost-per-task, not just per-call.

**Human-in-the-loop (HITL)**: practical pattern — automate read-only actions fully; require approval for write actions above a risk threshold. Define risk levels per action type explicitly before deployment.

**Testing bottleneck** (Willison): as code generation collapses from weeks to hours, the bottleneck shifts to verification. AI can generate credible artifacts (code, reports) faster than humans can validate them. The signal: "I built this but haven't used it yet."

**Dark factory pattern**: fully automated code pipelines with no human writing or reading the code. Practical today in narrow domains, but requires trusted test suites as the safety net.

**Prompt injection**: malicious content in tool outputs (web pages, documents) can hijack subsequent agent actions. High-stakes agents with write access and unsanitized inputs are the risk surface. Mitigate with output validation and sandboxed execution.

## Connection to PINvestigator Architecture

PINvestigator's parallel subagent design directly applies the multi-agent pattern: independent subagents handle separate retrieval/analysis tasks simultaneously, then an orchestrator synthesizes results. Parallel execution matters here for latency — subagents that don't depend on each other's outputs should run concurrently, not sequentially. Independent failure domains mean one subagent's hallucination or tool failure doesn't cascade. Each subagent should be scoped narrowly (single tool category or data source), with the orchestrator responsible for plan validation and final synthesis.

## Sources

- `kb/hard/raw/chip-huyen/agents.md` — primary reference: agent definition, tools taxonomy, planning patterns, failure modes, evaluation framework (from *AI Engineering*, Chip Huyen 2025)
- `kb/hard/raw/aman-ai/primers-agents.md` — agent framework components, design patterns, MCP protocol, agentic RAG, multi-agent frameworks
- `kb/hard/raw/aman-ai/primers-agentic-design-patterns.md` — pattern catalog: reflection, tool use, planning, multi-agent, HITL, guardrails, MCP integration
- `kb/hard/raw/aman-ai/primers-agentic-reinforcement-learning.md` — RL for tool-calling agents: MDP formulation, reward decomposition, curriculum, PPO/GRPO, evaluation metrics
- `kb/hard/raw/aman-ai/models-toolformer.md` — Toolformer: self-supervised tool call learning, filtering mechanism, limitations
- `kb/hard/raw/aman-ai/primers-computer-control.md` — computer use agents: Anthropic, Operator, Manus, OmniParser, benchmarks
- `kb/hard/raw/eugene-yan/building-news-agents-for-daily-news-recaps-with-mcp-q-and-tmux.md` — practical MCP + agentic workflow implementation
- `kb/hard/raw/simon-willison/highlights-from-my-conversation-about-agentic-engineering-on-lennys-podcast.md` — practitioner perspective: agent reliability, testing bottleneck, dark factory pattern, prompt injection risks
