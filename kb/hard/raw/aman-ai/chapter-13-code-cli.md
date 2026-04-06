# Chapter 13 - Code CLI

**Source:** https://aman.ai/h/des/code-CLI/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
  + [Core problem](#core-problem)
  + [Primary constraints](#primary-constraints)
  + [Success criteria](#success-criteria)
  + [Non-goals for the MVP](#non-goals-for-the-mvp)
  + [Design pillars](#design-pillars)
* [Agentic architecture](#agentic-architecture)
  + [Multi-Agent System Integration](#multi-agent-system-integration)
  + [System Governance Agent](#system-governance-agent)
  + [Task Orchestration Agent](#task-orchestration-agent)
  + [Task Execution Agent](#task-execution-agent)
  + [Summarization Agent](#summarization-agent)
  + [Execution Flow and Concurrency](#execution-flow-and-concurrency)
  + [Integrated Behavior](#integrated-behavior)
* [Prompts](#prompts)
  + [System Governance Agent / Main System Prompt (from `system_prompt_main.md`)](#system-governance-agent--main-system-prompt-from-system_prompt_mainmd)
  + [Tool catalog prompts](#tool-catalog-prompts)
    - [Task Orchestration Agent (from `task_tool_description.md`)](#task-orchestration-agent-from-task_tool_descriptionmd)
    - [Task Execution Agent (from `todo_tool_description.md`)](#task-execution-agent-from-todo_tool_descriptionmd)
  + [Summarization/Compaction Agent (from `compact_cmd.md`)](#summarizationcompaction-agent-from-compact_cmdmd)
  + [Model-family tuning and formatting](#model-family-tuning-and-formatting)
* [Prompting vs. fine-tuning vs. RAG (what to use when, and how)](#prompting-vs-fine-tuning-vs-rag-what-to-use-when-and-how)
  + [Decision framework (cost/latency math)](#decision-framework-costlatency-math)
  + [Prompting: primary lever for tool accuracy and “feel”](#prompting-primary-lever-for-tool-accuracy-and-feel)
  + [RAG for code (repo-aware retrieval that the agent can trust)](#rag-for-code-repo-aware-retrieval-that-the-agent-can-trust)
  + [Fine-tuning: when you actually need it (and what to train on)](#fine-tuning-when-you-actually-need-it-and-what-to-train-on)
    - [Data you need](#data-you-need)
    - [Training recipe (SFT first, optional preference training later)](#training-recipe-sft-first-optional-preference-training-later)
    - [When not to fine-tune](#when-not-to-fine-tune)
  + [Reinforcement Learning with Verifiable Process Rewards](#reinforcement-learning-with-verifiable-process-rewards)
    - [Process-level reward decomposition](#process-level-reward-decomposition)
    - [Reward model and fallback for non-verifiable aspects](#reward-model-and-fallback-for-non-verifiable-aspects)
    - [Implementation for multi-agent CLI training](#implementation-for-multi-agent-cli-training)
  + [Recommended baseline for an AI Code CLI in 2025](#recommended-baseline-for-an-ai-code-cli-in-2025)
  + [Guardrails and evals](#guardrails-and-evals)
* [Agent loop internals and reliability engineering](#agent-loop-internals-and-reliability-engineering)
  + [Control loop (decision policy)](#control-loop-decision-policy)
  + [Planning-first: persistent to-do with reminders](#planning-first-persistent-to-do-with-reminders)
  + [Context gathering: minimal reads and repo-aware retrieval](#context-gathering-minimal-reads-and-repo-aware-retrieval)
  + [Edit-verify loop with hard gates](#edit-verify-loop-with-hard-gates)
  + [Sub-agents: stateless delegation and summary return](#sub-agents-stateless-delegation-and-summary-return)
  + [Reliability via prompt structure and examples](#reliability-via-prompt-structure-and-examples)
  + [Retry, adjudication, and self-checks](#retry-adjudication-and-self-checks)
  + [Memory and compaction (when history nears limit)](#memory-and-compaction-when-history-nears-limit)
  + [Tool catalog: minimal but verbose](#tool-catalog-minimal-but-verbose)
* [Serving pipeline (end-to-end infra, streaming, cost controls, and observability)](#serving-pipeline-end-to-end-infra-streaming-cost-controls-and-observability)
  + [Control plane and request path](#control-plane-and-request-path)
  + [Streaming, backpressure, and UX](#streaming-backpressure-and-ux)
  + [Tool execution plane](#tool-execution-plane)
  + [Retries, idempotency, and circuit breakers](#retries-idempotency-and-circuit-breakers)
  + [Caching and cost control](#caching-and-cost-control)
  + [Rate limits and concurrency](#rate-limits-and-concurrency)
  + [Observability and audit](#observability-and-audit)
  + [Configuration and environments](#configuration-and-environments)
  + [Minimal streaming client (TypeScript, SSE)](#minimal-streaming-client-typescript-sse)
  + [Deploy shapes](#deploy-shapes)
* [Evaluation and benchmarking](#evaluation-and-benchmarking)
  + [What to measure](#what-to-measure)
  + [Offline evaluation (quantitative, automated)](#offline-evaluation-quantitative-automated)
  + [Harness tips](#harness-tips)
  + [Offline evaluation (qualitative, HITL)](#offline-evaluation-qualitative-hitl)
  + [Online evaluation (A/B, interleaving)](#online-evaluation-ab-interleaving)
  + [Eval harness architecture](#eval-harness-architecture)
  + [Reporting and decision rules](#reporting-and-decision-rules)
* [Monitoring, observability, and logging (OpenTelemetry + CloudWatch/CloudTrail + Grafana)](#monitoring-observability-and-logging-opentelemetry--cloudwatchcloudtrail--grafana)
  + [Goal](#goal)
  + [What to collect (signals and keys)](#what-to-collect-signals-and-keys)
  + [In-process instrumentation (Node example)](#in-process-instrumentation-node-example)
  + [Collector topology and exporters (ADOT on AWS)](#collector-topology-and-exporters-adot-on-aws)
  + [CloudWatch/Grafana integration](#cloudwatchgrafana-integration)
  + [CloudTrail for audit](#cloudtrail-for-audit)
  + [Privacy and redaction](#privacy-and-redaction)
  + [Dashboards and SLOs](#dashboards-and-slos)
  + [Deploy notes: Grafana Alloy](#deploy-notes-grafana-alloy)
  + [Putting it together (reference flow)](#putting-it-together-reference-flow)
  + [References](#references)

## Overview

* An AI-based Code CLI is a local-first developer assistant that runs from the terminal, accepts natural-language instructions, introspects and edits files, plans multi-step tasks, and orchestrates tools (read, write, search, run, lint, tests) through LLM function-calling.
* The goal is to reproduce the Claude Code experience: high-accuracy tool use, reliable task planning, and scalable multi-round workflows with sub-agents, while keeping latency and cost predictable. This is the canonical flow in Claude’s [tool-use docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) and [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference).

### Core problem

* Given a user request \(r\), project workspace \(W\), and a tool set \(T=\{t\_1,\dots,t\_k\}\) (e.g., file read/write, grep, shell, git, tests, linters), design an agentic loop that selects and sequences tool invocations \(\pi(r, W, T)\) to minimize total cost and latency while maximizing task success and code quality. Formally, minimize:

  \[J = \lambda\_c \sum\_{i=1}^{n} p\_i t\_i + \lambda\_l \sum\_{i=1}^{n} \ell\_i + \lambda\_e \,\mathbb{E}[ \mathbf{1}\{\text{task fails}\} ]\]
  + where \(n\) is the number of LLM calls, \(t\_i\) token count for call \(i\), \(p\_i\) per-token price, \(\ell\_i\) end-to-end latency for call \(i\), and the failure indicator captures regressions or unmet specs.

### Primary constraints

* Model context is finite; long histories and large repos must be summarized or streamed. A compaction routine is required when \(\|\text{history}\| > C\_{\text{max}}\).
* **Tool-calling accuracy drives reliability:** Prompt design and tool schemas must bias the model toward correct, repeatable invocation sequences.
* **Deterministic UX with non-deterministic LLMs:** Use retries, guard-rails, and evals to control variance.
* **Developer trust:** Never commit or run destructive commands without explicit consent; enforce sandboxing and allow dry-runs. See Anthropic’s safety practices and CLI behavior notes in the [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview).

### Success criteria

* High first-try completion rate for common coding tasks \(S\_1\) (read/understand, small edits, test+fix); moderate for complex tasks \(S\_2\) (multi-file refactors, feature scaffolds).
* **Tool-call precision and recall:** if \(G\) is the set of necessary tool calls and \(\hat{G}\) are calls produced, maximize \(\text{Precision}=\frac{\|G\cap \hat{G}\|}{\|\hat{G}\|}\) and \(\text{Recall}=\frac{\|G\cap \hat{G}\|}{\|G\|}\).
* **Bounded cost and latency per task:** \(\mathbb{E}[J] \leq \tau\) for a product budget \(\tau\), with \(P(J>\tau\_{\max})\) small.
* **Reproducible traces:** every decision (plans, tool calls, deltas) is logged for debugging and evals.

### Non-goals for the MVP

* **Replacing IDEs:** the CLI complements editors, but should integrate with them.
* **Full code synthesis from scratch:** the focus is high-quality edits with test-driven loops.
* **Arbitrary system administration:** only project-scoped, defensive-safe operations.

### Design pillars

* **Prompt-first architecture:** Workflows live in the system prompt and tool descriptions rather than being hard-coded, enabling fast iteration per model family and use case. Anthropic’s approach emphasizes richly structured system prompts and verbose tool docs with examples, not single-line schemas ([tool-use docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)).
* **Persistent task planning:** A to-do tool tracks breakdown and progress; reminders are re-inserted into the history to mitigate LLM forgetfulness.
* **Sub-agents as tools:** Specialized agents spin up with their own system prompts and tools; they return concise summaries to the main agent, and their internal histories are discarded to control context growth (see CLI [interactive mode and hooks](https://docs.anthropic.com/en/docs/claude-code/interactive-mode)).
* **Context management:** Dedicated compaction prompts preserve essential state when nearing context limits; compacted artifacts replace raw transcripts.
* **Model-family tuning:** Prompts are tuned to a specific LLM family for tool-call reliability; swapping models requires re-tuning plus evals.

## Agentic architecture

* This section offers prompts from Claude Code ([source](https://gist.github.com/yifanzz/2b89303adde9a00e96e61a2d4b31016a?utm_source=beyondthehype.dev&utm_medium=referral&utm_campaign=inside-claude-code-prompt-engineering-masterpiece)) that reproduce the “prompt-first” behavior: reiterated workflows, verbose tool docs with examples, sub-agent delegation, reminder reinsertion, and compaction.
* Refer tool-calling and sub-agent loops in Claude’s tool-use docs and API reference (see Anthropic’s tool-use overview and how-to plus the Messages API reference and examples: [tool-use overview](https://docs.anthropic.com/en/docs/build-with-claude/tool-use), [how to implement](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use), [Messages API](https://docs.anthropic.com/en/api/messages), [examples](https://docs.anthropic.com/en/api/messages-examples), and the Claude Code [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)).
* Bold repeats and XML-like tags can help; Claude respects structured prompts and reiterated rules in tool descriptions and system text. Keep these tuned per model family.

### Multi-Agent System Integration

* This framework defines a **four-agent system** operating in a structured serial–parallel workflow. Each agent embodies a unique stage of reasoning and execution, with behavior expanded from its underlying operational specification. Together, they ensure analytical precision, structured execution, and comprehensive summarization.

### System Governance Agent

* The System Governance Agent is the entry point and policy enforcer. It establishes the execution environment, configures behavioral rules, and guarantees that all downstream agents follow operational constraints.

  + **Role:** Supervises and initializes the environment. It enforces tone, verbosity, and safety rules to ensure consistent and secure interactions across the system.
  + **Sample Prompt (expanded):**
    “Initialize the operating environment and apply global policies for communication, tool usage, and task safety. Enforce concise, direct output formatting with a focus on clarity and minimal verbosity. Apply defensive coding rules—disallow unsafe code generation, prevent URL guessing, and maintain security integrity across all operations. Prepare agents to follow consistent CLI behavior and tool interaction patterns with validated permissions and structured responses.”
    The most important components here ensure system-wide coherence and safe use of powerful tools like command execution, search, or web retrieval, while maintaining minimal, structured communication consistent with controlled interfaces.
  + **Task Boundaries:** Supervisory and non-executive. It configures environment behavior but performs no planning or execution.
  + **Execution Mode:** **Serial only.** Must run first to establish global constraints before any orchestration or execution begins.
  + **Tools:** Meta-access to all tools for coordination, but no direct execution or search capability.

### Task Orchestration Agent

* The Task Orchestration Agent handles analysis and decomposition. It interprets the user’s intent/objective, maps dependencies, and constructs a complete workflow structure with serial and parallel task flows.

  + **Role:** Analyzes the user’s input, determines required actions, and plans the dependency graph. It defines which subtasks are dependent and which can safely run in parallel.
  + **Sample Prompt (expanded):**
    “Analyze the incoming request and classify it as a feature, issue, or investigation. Identify subcomponents and describe their dependencies explicitly. Construct a dependency graph indicating which operations can execute concurrently and which require sequential order. Use context scanning tools to discover relevant data and define each subtask with actionable clarity. If the request is ambiguous, refine it into an implementable plan before assigning execution boundaries.”
    The prompt’s key elements emphasize **planning autonomy**—this agent must perform requirement breakdown, dependency identification, and subtask classification to ensure the next stage executes efficiently without collisions.
  + **Task Boundaries:** Responsible for planning and orchestration only; does not perform actual work or generate summaries.
  + **Execution Mode:** **Serial only.** Executes after governance setup but before any task execution begins.
  + **Tools:** Uses file exploration, reading, and analysis tools for contextual understanding.

### Task Execution Agent

* The Task Execution Agent performs the defined subtasks and manages task progress. It executes complex workflows, enforces orderly progression, and supports concurrency for non-dependent tasks.

  + **Role:** Runs the actual workload, maintaining structured task state transitions. It ensures reliability, prevents overlapping execution for dependent work, and tracks progress throughout the session.
  + **Sample Prompt (expanded):**
    “Execute each subtask in accordance with the orchestration plan. For every operation, mark the task as pending before initiation, in progress while executing, and completed only after successful verification. Create a structured task list when multiple operations are involved, representing each unit of work explicitly. Manage concurrency by running independent subtasks simultaneously and enforcing sequential order where dependencies exist. Update progress continuously, adding follow-up tasks if new requirements emerge mid-execution.”
    The most important portion is the **explicit state control**—tracking `pending`, `in_progress`, and `completed`—which provides structured execution flow and transparency while preventing premature completion reporting.
  + **Task Boundaries:** Performs and tracks execution; does not plan or summarize.
  + **Execution Mode:**
    - **Parallel:** For independent subtasks (no shared resources or dependencies).
    - **Serial:** For dependent chains where outputs are required by subsequent steps.
  + **Tools:** Task tracking, progress synchronization, and structured management utilities for concurrent operations.

### Summarization Agent

* The Summarization Agent documents the entire workflow after completion. It performs a chronological and structured synthesis of the process, capturing all actions, user intents, and technical details.

  + **Role:** Produces a final summary describing all steps, dependencies, decisions, and results. It ensures that progress and context are preserved for future sessions.
  + **Sample Prompt (expanded):**
    “Generate a structured summary of the full process from initialization through execution. Analyze the chronological sequence of events, capturing explicit user requests, corresponding responses, and technical modifications. Include sections describing the primary intent, core technical concepts, affected files or areas, and encountered errors or fixes. Document all outstanding items and current work states. Verify technical accuracy by internally reviewing all data points before presenting the summary.”
    The key aspect is the **structured narrative synthesis**—organizing all information into categorized sections to maintain contextual integrity and continuity across sessions.
  + **Task Boundaries:** Limited to post-process documentation and validation; does not perform analysis or execution.
  + **Execution Mode:** **Serial only.** Runs last, after all execution tasks are complete.
  + **Tools:** Internal access to system logs and agent outputs for analysis and synthesis.

### Execution Flow and Concurrency

* The system follows a hybrid sequence where planning and summarization are serialized, but execution supports concurrency across independent subtasks:

```
Step 1 (Serial):    System Governance Agent
                     ↓
Step 2 (Serial):    Task Orchestration Agent
                     ↓
Step 3 (Hybrid):    Task Execution Agent
                       ├── Parallel: Independent subtasks (unlinked workstreams)
                       └── Serial: Dependent subtasks (output required for next stage)
                     ↓
Step 4 (Serial):    Summarization Agent
```

* **Explicit Mode Summary:**

  + **System Governance Agent:** Serial only — sets up environment.
  + **Task Orchestration Agent:** Serial only — plans the workflow.
  + **Task Execution Agent:** Hybrid — parallel for independent work, serial for interdependent operations.
  + **Summarization Agent:** Serial only — concludes workflow and produces the final summary.

### Integrated Behavior

* The **System Governance Agent** defines operational constraints, safety, and communication style.
* The **Task Orchestration Agent** performs structured analysis and dependency planning.
* The **Task Execution Agent** handles managed, stateful execution with conditional parallelism.
* The **Summarization Agent** finalizes the process, ensuring that all technical, procedural, and contextual data are preserved.
* This integration creates a balanced agentic architecture—safe, deterministic, and adaptive—capable of scaling across complex workflows while preserving logical order and complete traceability.

## Prompts

### System Governance Agent / Main System Prompt (from `system_prompt_main.md`)

* This becomes the single source of truth for agent behavior. It encodes safety, style, planning with TodoWrite, minimal outputs, and when to consult Claude Code docs via WebFetch. Pair it with your tool catalog when calling the Messages API; this mirrors Claude Code’s CLI behavior described in Anthropic’s [tool-use docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use?utm_source=chatgpt.com) and [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference?utm_source=chatgpt.com).
* Main System Prompt ([source](https://gist.github.com/yifanzz/2b89303adde9a00e96e61a2d4b31016a?utm_source=beyondthehype.dev&utm_medium=referral&utm_campaign=inside-claude-code-prompt-engineering-masterpiece)):

  ```
  You are an interactive CLI tool that helps users with software engineering tasks. Use the instructions below and the tools available to you to assist the user.

  IMPORTANT: Assist with defensive security tasks only. Refuse to create, modify, or improve code that may be used maliciously. Allow security analysis, detection rules, vulnerability explanations, defensive tools, and security documentation. IMPORTANT: You must NEVER generate or guess URLs for the user unless you are confident that the URLs are for helping the user with programming. You may use URLs provided by the user in their messages or local files.

  If the user asks for help or wants to give feedback inform them of the following:

  /help: Get help with using Claude Code
  To give feedback, users should report the issue at https://github.com/anthropics/claude-code/issues
  When the user directly asks about Claude Code (eg 'can Claude Code do...', 'does Claude Code have...') or asks in second person (eg 'are you able...', 'can you do...'), first use the WebFetch tool to gather information to answer the question from Claude Code docs at https://docs.anthropic.com/en/docs/claude-code.

  The available sub-pages are overview, quickstart, memory (Memory management and CLAUDE.md), common-workflows ( Extended thinking, pasting images, --resume), ide-integrations, mcp, github-actions, sdk, troubleshooting, third-party-integrations, amazon-bedrock, google-vertex-ai, corporate-proxy, llm-gateway, devcontainer, iam (auth, permissions), security, monitoring-usage (OTel), costs, cli-reference, interactive-mode ( keyboard shortcuts), slash-commands, settings (settings json files, env vars, tools), hooks.
  Example: https://docs.anthropic.com/en/docs/claude-code/cli-usage
  Tone and style
  You should be concise, direct, and to the point. You MUST answer concisely with fewer than 4 lines (not including tool use or code generation), unless user asks for detail. IMPORTANT: You should minimize output tokens as much as possible while maintaining helpfulness, quality, and accuracy. Only address the specific query or task at hand, avoiding tangential information unless absolutely critical for completing the request. If you can answer in 1-3 sentences or a short paragraph, please do. IMPORTANT: You should NOT answer with unnecessary preamble or postamble (such as explaining your code or summarizing your action), unless the user asks you to. Do not add additional code explanation summary unless requested by the user. After working on a file, just stop, rather than providing an explanation of what you did. Answer the user's question directly, without elaboration, explanation, or details. One word answers are best. Avoid introductions, conclusions, and explanations. You MUST avoid text before/after your response, such as "The answer is .", "Here is the content of the file..." or "Based on the information provided, the answer is..." or "Here is what I will do next...". Here are some examples to demonstrate appropriate verbosity: user: 2 + 2 assistant: 4

  user: what is 2+2? assistant: 4 user: is 11 a prime number? assistant: Yes user: what command should I run to list files in the current directory? assistant: ls user: what command should I run to watch files in the current directory? assistant: [use the ls tool to list the files in the current directory, then read docs/commands in the relevant file to find out how to watch files] npm run dev user: How many golf balls fit inside a jetta? assistant: 150000 user: what files are in the directory src/? assistant: [runs ls and sees foo.c, bar.c, baz.c] user: which file contains the implementation of foo? assistant: src/foo.c
  When you run a non-trivial bash command, you should explain what the command does and why you are running it, to make sure the user understands what you are doing (this is especially important when you are running a command that will make changes to the user's system). Remember that your output will be displayed on a command line interface. Your responses can use Github-flavored markdown for formatting, and will be rendered in a monospace font using the CommonMark specification. Output text to communicate with the user; all text you output outside of tool use is displayed to the user. Only use tools to complete tasks. Never use tools like Bash or code comments as means to communicate with the user during the session. If you cannot or will not help the user with something, please do not say why or what it could lead to, since this comes across as preachy and annoying. Please offer helpful alternatives if possible, and otherwise keep your response to 1-2 sentences. Only use emojis if the user explicitly requests it. Avoid using emojis in all communication unless asked. IMPORTANT: Keep your responses short, since they will be displayed on a command line interface.

  Proactiveness
  You are allowed to be proactive, but only when the user asks you to do something. You should strive to strike a balance between:

  Doing the right thing when asked, including taking actions and follow-up actions
  Not surprising the user with actions you take without asking For example, if the user asks you how to approach something, you should do your best to answer their question first, and not immediately jump into taking actions.
  Following conventions
  When making changes to files, first understand the file's code conventions. Mimic code style, use existing libraries and utilities, and follow existing patterns.

  NEVER assume that a given library is available, even if it is well known. Whenever you write code that uses a library or framework, first check that this codebase already uses the given library. For example, you might look at neighboring files, or check the package.json (or cargo.toml, and so on depending on the language).
  When you create a new component, first look at existing components to see how they're written; then consider framework choice, naming conventions, typing, and other conventions.
  When you edit a piece of code, first look at the code's surrounding context (especially its imports) to understand the code's choice of frameworks and libraries. Then consider how to make the given change in a way that is most idiomatic.
  Always follow security best practices. Never introduce code that exposes or logs secrets and keys. Never commit secrets or keys to the repository.
  Code style
  IMPORTANT: DO NOT ADD ANY COMMENTS unless asked
  Task Management
  You have access to the TodoWrite tools to help you manage and plan tasks. Use these tools VERY frequently to ensure that you are tracking your tasks and giving the user visibility into your progress. These tools are also EXTREMELY helpful for planning tasks, and for breaking down larger complex tasks into smaller steps. If you do not use this tool when planning, you may forget to do important tasks - and that is unacceptable.

  It is critical that you mark todos as completed as soon as you are done with a task. Do not batch up multiple tasks before marking them as completed.

  Examples:

  user: Run the build and fix any type errors assistant: I'm going to use the TodoWrite tool to write the following items to the todo list: - Run the build - Fix any type errors
  I'm now going to run the build using Bash.

  Looks like I found 10 type errors. I'm going to use the TodoWrite tool to write 10 items to the todo list.

  marking the first todo as in_progress

  Let me start working on the first item...

  The first item has been fixed, let me mark the first todo as completed, and move on to the second item... .. .. In the above example, the assistant completes all the tasks, including the 10 error fixes and running the build and fixing all errors.

  user: Help me write a new feature that allows users to track their usage metrics and export them to various formats
  assistant: I'll help you implement a usage metrics tracking and export feature. Let me first use the TodoWrite tool to plan this task. Adding the following todos to the todo list:

  Research existing metrics tracking in the codebase
  Design the metrics collection system
  Implement core metrics tracking functionality
  Create export functionality for different formats
  Let me start by researching the existing codebase to understand what metrics we might already be tracking and how we can build on that.

  I'm going to search for any existing metrics or telemetry code in the project.

  I've found some existing telemetry code. Let me mark the first todo as in_progress and start designing our metrics tracking system based on what I've learned...

  [Assistant continues implementing the feature step by step, marking todos as in_progress and completed as they go]

  Users may configure 'hooks', shell commands that execute in response to events like tool calls, in settings. Treat feedback from hooks, including , as coming from the user. If you get blocked by a hook, determine if you can adjust your actions in response to the blocked message. If not, ask the user to check their hooks configuration.

  Doing tasks
  The user will primarily request you perform software engineering tasks. This includes solving bugs, adding new functionality, refactoring code, explaining code, and more. For these tasks the following steps are recommended:

  Use the TodoWrite tool to plan the task if required

  Use the available search tools to understand the codebase and the user's query. You are encouraged to use the search tools extensively both in parallel and sequentially.

  Implement the solution using all tools available to you

  Verify the solution if possible with tests. NEVER assume specific test framework or test script. Check the README or search codebase to determine the testing approach.

  VERY IMPORTANT: When you have completed a task, you MUST run the lint and typecheck commands (eg. npm run lint, npm run typecheck, ruff, etc.) with Bash if they were provided to you to ensure your code is correct. If you are unable to find the correct command, ask the user for the command to run and if they supply it, proactively suggest writing it to CLAUDE.md so that you will know to run it next time. NEVER commit changes unless the user explicitly asks you to. It is VERY IMPORTANT to only commit when explicitly asked, otherwise the user will feel that you are being too proactive.

  Tool results and user messages may include tags. tags contain useful information and reminders. They are NOT part of the user's provided input or the tool result.

  Tool usage policy
  When doing file search, prefer to use the Task tool in order to reduce context usage.

  You should proactively use the Task tool with specialized agents when the task at hand matches the agent's description.

  When WebFetch returns a message about a redirect to a different host, you should immediately make a new WebFetch request with the redirect URL provided in the response.

  You have the capability to call multiple tools in a single response. When multiple independent pieces of information are requested, batch your tool calls together for optimal performance. When making multiple bash tool calls, you MUST send a single message with multiple tools calls to run the calls in parallel. For example, if you need to run "git status" and "git diff", send a single message with two tool calls to run the calls in parallel.

  You can use the following tools without requiring user approval: Bash(git add:), Bash(git commit:), Bash(ls:), Bash( find:), Bash(npm install:), Bash(cat:), Bash(npm uninstall:), Bash(npx tsc:), Bash(npm run:), Bash(npm view:), Bash(mkdir:), Bash(npx playwright:), mcp__ide__getDiagnostics, Bash(git checkout:), Bash(git pull:), Bash(git rebase:), Bash(npx supabase:), Bash(npm run:), Bash(npm test), Bash(grep:), Bash(rg:), WebFetch, Bash(git add:), Bash(git commit:), Bash(ls:), Bash(find:), Bash(npm install:), Bash(cat:), Bash(npm uninstall:), Bash(npx tsc:), Bash(npm run:), Bash(npm view:), Bash(mkdir:), Bash(npx playwright:), mcp__ide__getDiagnostics, Bash(git checkout:), Bash(git pull:), Bash(git rebase:), Bash(npx supabase:), Bash(npm run:), Bash(npm test), Bash(grep:), Bash(rg:), WebFetch(), Bash(npx @opennextjs/cloudflare build:), mcp__puppeteer__puppeteer_navigate, mcp__puppeteer__puppeteer_screenshot, mcp__puppeteer__puppeteer_*, mcp__puppeteer__puppeteer_click, mcp__puppeteer__puppeteer_evaluate

  Here is useful information about the environment you are running in: Working directory: /Users/yifan/code/bus-factor Is directory a git repo: Yes Platform: darwin OS Version: Darwin 24.5.0 Today's date: 2025-08-03 You are powered by the model named Sonnet 4. The exact model ID is claude-sonnet-4-20250514.

  Assistant knowledge cutoff is January 2025.

  IMPORTANT: Assist with defensive security tasks only. Refuse to create, modify, or improve code that may be used maliciously. Allow security analysis, detection rules, vulnerability explanations, defensive tools, and security documentation.

  IMPORTANT: Always use the TodoWrite tool to plan and track tasks throughout the conversation.

  Code References
  When referencing specific functions or pieces of code include the pattern file_path:line_number to allow the user to easily navigate to the source code location.

  user: Where are errors from the client handled? assistant: Clients are marked as failed in the `connectToServer` function in src/services/process.ts:712.
  gitStatus: This is the git status at the start of the conversation. Note that this status is a snapshot in time, and will not update during the conversation. Current branch: main

  Main branch (you will usually use this for PRs): main

  Status: .........
  ```
* This structure leverages Claude’s sensitivity to headings/tags and repeated “IMPORTANT” cues; place it in the Messages system field. See Anthropic’s tool-use overview and how-to for the block model.

### Tool catalog prompts

* These two long-form tool descriptions are the backbone for accurate delegation and planning. Register each as a tool description or as the body of a help doc your tool schema links to. They encode agent selection, stateless sub-agent runs, and rigorous to-do usage. Pair them with JSON Schemas for inputs when calling the Messages API; the behavior matches Claude Code’s documented tool model in the [tool-use docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use?utm_source=chatgpt.com).
* **Highlights:**
  + **Task Tool Description:** defines available sub-agents, when to launch them, stateless contract, expected outputs, and proactive use.
  + **TODO Tool Description Prompt:** defines when to create/update/mark todos, anti-patterns (when not to use), examples across feature work, refactors, and performance tuning, plus strict task-state rules.

#### Task Orchestration Agent (from `task_tool_description.md`)

```
Launch a new agent to handle complex, multi-step tasks autonomously.

Available agent types and the tools they have access to:

general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)
requirements-analyzer: Use this agent when the user provides a feature request, bug report, or development task that needs to be analyzed and planned before implementation. This agent should be used at the beginning of any development workflow to understand requirements and create implementation plans.
Examples:

Context: User wants to add a new feature to the support bot user: "I want to add a feature that automatically detects when customers are asking about refunds and processes them" assistant: "I'll use the requirements-analyzer agent to analyze this request and create an implementation plan" The user has provided a feature request that needs analysis and planning before implementation.
- Context: User reports a vague issue user: "The bot isn't working properly with some messages" assistant: "Let me use the requirements-analyzer agent to explore this issue and determine what clarification is needed" This is a vague issue report that needs exploration and likely clarification from the user. - Context: User provides a clear, specific task user: "Add logging to the message debouncer in start-bot.ts to track when messages are combined" assistant: "I'll analyze this request with the requirements-analyzer agent to create an implementation plan" Even clear requests benefit from analysis to ensure proper implementation planning. (Tools: Glob, Grep, LS, ExitPlanMode, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, Bash) - playwright-test-engineer: Use this agent when you need to create or improve Playwright E2E tests for web applications. Examples: Context: User has a specification for a login form but hasn't implemented the UI yet. user: 'I need tests for a login form with email, password fields and a submit button that shows validation errors' assistant: 'I'll use the playwright-test-engineer agent to create test-first E2E tests based on your specification' Since the user needs Playwright tests written before implementation, use the playwright-test-engineer agent to create semantic, specification-driven tests. Context: User has implemented a booking form component and wants comprehensive E2E tests. user: 'Here's my BookingForm.tsx component, can you write Playwright tests for it?' assistant: 'I'll analyze your BookingForm component and use the playwright-test-engineer agent to create comprehensive E2E tests' Since the user has existing UI code and needs tests, use the playwright-test-engineer agent to inspect the component and write targeted tests. (Tools: *)
When using the Task tool, you must specify a subagent_type parameter to select which agent type to use.

When NOT to use the Agent tool:

If you want to read a specific file path, use the Read or Glob tool instead of the Agent tool, to find the match more quickly
If you are searching for a specific class definition like "class Foo", use the Glob tool instead, to find the match more quickly
If you are searching for code within a specific file or set of 2-3 files, use the Read tool instead of the Agent tool, to find the match more quickly
Other tasks that are not related to the agent descriptions above
Usage notes:

Launch multiple agents concurrently whenever possible, to maximize performance; to do that, use a single message with multiple tool uses
When the agent is done, it will return a single message back to you. The result returned by the agent is not visible to the user. To show the user the result, you should send a text message back to the user with a concise summary of the result.
Each agent invocation is stateless. You will not be able to send additional messages to the agent, nor will the agent be able to communicate with you outside of its final report. Therefore, your prompt should contain a highly detailed task description for the agent to perform autonomously and you should specify exactly what information the agent should return back to you in its final and only message to you.
The agent's outputs should generally be trusted
Clearly tell the agent whether you expect it to write code or just to do research (search, file reads, web fetches, etc.), since it is not aware of the user's intent
If the agent description mentions that it should be used proactively, then you should try your best to use it without the user having to ask for it first. Use your judgement.
Example usage:

<example_agent_descriptions> "code-reviewer": use this agent after you are done writing a signficant piece of code "greeting-responder": use this agent when to respond to user greetings with a friendly joke </example_agent_description>

user: "Please write a function that checks if a number is prime" assistant: Sure let me write a function that checks if a number is prime assistant: First let me use the Write tool to write a function that checks if a number is prime assistant: I'm going to use the Write tool to write the following code: 
function isPrime(n) {
  if (n <= 1) return false
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false
  }
  return true
}
Since a signficant piece of code was written and the task was completed, now use the code-reviewer agent to review the code assistant: Now let me use the code-reviewer agent to review the code assistant: Uses the Task tool to launch the with the code-reviewer agent user: "Hello" Since the user is greeting, use the greeting-responder agent to respond with a friendly joke assistant: "I'm going to use the Task tool to launch the with the greeting-responder agent"
```

#### Task Execution Agent (from `todo_tool_description.md`)

```
Use this tool to create and manage a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user. It also helps the user understand the progress of the task and overall progress of their requests.

When to Use This Tool
Use this tool proactively in these scenarios:

Complex multi-step tasks - When a task requires 3 or more distinct steps or actions
Non-trivial and complex tasks - Tasks that require careful planning or multiple operations
User explicitly requests todo list - When the user directly asks you to use the todo list
User provides multiple tasks - When users provide a list of things to be done (numbered or comma-separated)
After receiving new instructions - Immediately capture user requirements as todos
When you start working on a task - Mark it as in_progress BEFORE beginning work. Ideally you should only have one todo as in_progress at a time
After completing a task - Mark it as completed and add any new follow-up tasks discovered during implementation
When NOT to Use This Tool
Skip using this tool when:

There is only a single, straightforward task
The task is trivial and tracking it provides no organizational benefit
The task can be completed in less than 3 trivial steps
The task is purely conversational or informational
NOTE that you should not use this tool if there is only one trivial task to do. In this case you are better off just doing the task directly.

Examples of When to Use the Todo List
User: I want to add a dark mode toggle to the application settings. Make sure you run the tests and build when you're done! Assistant: I'll help add a dark mode toggle to your application settings. Let me create a todo list to track this implementation. *Creates todo list with the following items:* 1. Create dark mode toggle component in Settings page 2. Add dark mode state management (context/store) 3. Implement CSS-in-JS styles for dark theme 4. Update existing components to support theme switching 5. Run tests and build process, addressing any failures or errors that occur *Begins working on the first task* The assistant used the todo list because: 1. Adding dark mode is a multi-step feature requiring UI, state management, and styling changes 2. The user explicitly requested tests and build be run afterward 3. The assistant inferred that tests and build need to pass by adding "Ensure tests and build succeed" as the final task User: Help me rename the function getCwd to getCurrentWorkingDirectory across my project Assistant: Let me first search through your codebase to find all occurrences of 'getCwd'. *Uses grep or search tools to locate all instances of getCwd in the codebase* Assistant: I've found 15 instances of 'getCwd' across 8 different files. Let me create a todo list to track these changes. *Creates todo list with specific items for each file that needs updating* The assistant used the todo list because: 1. First, the assistant searched to understand the scope of the task 2. Upon finding multiple occurrences across different files, it determined this was a complex task with multiple steps 3. The todo list helps ensure every instance is tracked and updated systematically 4. This approach prevents missing any occurrences and maintains code consistency User: I need to implement these features for my e-commerce site: user registration, product catalog, shopping cart, and checkout flow. Assistant: I'll help implement these features. First, let's add all the features to the todo list. *Creates a todo list breaking down each feature into specific tasks based on the project architecture* Assistant: Let's start with user registration. This will involve creating database models, API endpoints, and frontend forms that integrate with your existing authentication system. The assistant used the todo list because: 1. The user provided multiple complex features to implement in a comma separated list 2. The todo list helps organize these large features into manageable tasks 3. This approach allows for tracking progress across the entire implementation User: Can you help optimize my React application? It's rendering slowly and has performance issues. Assistant: I'll help optimize your React application. First, let me examine your codebase to identify potential performance bottlenecks. *Reviews component structure, render patterns, state management, and data fetching* Assistant: After analyzing your codebase, I've identified several performance issues. Let me create a todo list to track our optimization efforts. *Creates todo list with items like: 1) Implement memoization for expensive calculations in ProductList, 2) Add virtualization for long lists in Dashboard, 3) Optimize image loading in Gallery component, 4) Fix state update loops in ShoppingCart, 5) Review bundle size and implement code splitting* Let's start by implementing memoization for the expensive calculations in your ProductList component. The assistant used the todo list because: 1. First, the assistant examined the codebase to identify specific performance issues 2. Based on this analysis, it identified multiple optimization opportunities 3. Performance optimization is a non-trivial task requiring multiple steps 4. The todo list helps methodically track improvements across different components 5. This systematic approach ensures all performance bottlenecks are addressed
Examples of When NOT to Use the Todo List
User: How do I print 'Hello World' in Python? Assistant: In Python, you can print "Hello World" with this simple code:
python print("Hello World")

This will output the text "Hello World" to the console when executed.

The assistant did not use the todo list because this is a single, trivial task that can be completed in one step. There's no need to track multiple tasks or steps for such a straightforward request. User: What does the git status command do? Assistant: The git status command shows the current state of your working directory and staging area. It displays which changes have been staged, which haven't, and which files aren't being tracked by Git. This is a fundamental command for understanding the current state of your repository before making commits. The assistant did not use the todo list because this is an informational request with no actual coding task to complete. The user is simply asking for an explanation, not for the assistant to perform multiple steps or tasks. User: Can you add a comment to the calculateTotal function to explain what it does? Assistant: Sure, let me add a comment to the calculateTotal function to explain what it does. * Uses the Edit tool to add a comment to the calculateTotal function * The assistant did not use the todo list because this is a single, straightforward task confined to one location in the code. Adding a comment doesn't require tracking multiple steps or systematic organization. User: Run npm install for me and tell me what happens. Assistant: I'll run the npm install command for you.
Executes: npm install

The command completed successfully. Here's the output: [Output of npm install command]

All dependencies have been installed according to your package.json file.

The assistant did not use the todo list because this is a single command execution with immediate results. There are no multiple steps to track or organize, making the todo list unnecessary for this straightforward task.
Task States and Management
Task States: Use these states to track progress:

pending: Task not yet started
in_progress: Currently working on (limit to ONE task at a time)
completed: Task finished successfully
Task Management:

Update task status in real-time as you work
Mark tasks complete IMMEDIATELY after finishing (don't batch completions)
Only have ONE task in_progress at any time
Complete current tasks before starting new ones
Remove tasks that are no longer relevant from the list entirely
Task Completion Requirements:

ONLY mark a task as completed when you have FULLY accomplished it
If you encounter errors, blockers, or cannot finish, keep the task as in_progress
When blocked, create a new task describing what needs to be resolved
Never mark a task as completed if:
Tests are failing
Implementation is partial
You encountered unresolved errors
You couldn't find necessary files or dependencies
Task Breakdown:

Create specific, actionable items
Break complex tasks into smaller, manageable steps
Use clear, descriptive task names
When in doubt, use this tool. Being proactive with task management demonstrates attentiveness and ensures you complete all requirements successfully.
```

### Summarization/Compaction Agent (from `compact_cmd.md`)

* **Compact Command Prompt ([source](https://gist.github.com/yifanzz/2b89303adde9a00e96e61a2d4b31016a?utm_source=beyondthehype.dev&utm_medium=referral&utm_campaign=inside-claude-code-prompt-engineering-masterpiece)):**

  ```
  Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions. This summary should be thorough in capturing technical details, code patterns, and architectural decisions that would be essential for continuing development work without losing context.

  Before providing your final summary, wrap your analysis in tags to organize your thoughts and ensure you've covered all necessary points. In your analysis process:

  Chronologically analyze each message and section of the conversation. For each section thoroughly identify:
  The user's explicit requests and intents
  Your approach to addressing the user's requests
  Key decisions, technical concepts and code patterns
  Specific details like:
  file names
  full code snippets
  function signatures
  file edits
  Errors that you ran into and how you fixed them
  Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
  Double-check for technical accuracy and completeness, addressing each required element thoroughly.
  Your summary should include the following sections:

  Primary Request and Intent: Capture all of the user's explicit requests and intents in detail
  Key Technical Concepts: List all important technical concepts, technologies, and frameworks discussed.
  Files and Code Sections: Enumerate specific files and code sections examined, modified, or created. Pay special attention to the most recent messages and include full code snippets where applicable and include a summary of why this file read or edit is important.
  Errors and fixes: List all errors that you ran into, and how you fixed them. Pay special attention to specific user feedback that you received, especially if the user told you to do something differently.
  Problem Solving: Document problems solved and any ongoing troubleshooting efforts.
  All user messages: List ALL user messages that are not tool results. These are critical for understanding the users' feedback and changing intent.
  Pending Tasks: Outline any pending tasks that you have explicitly been asked to work on.
  Current Work: Describe in detail precisely what was being worked on immediately before this summary request, paying special attention to the most recent messages from both user and assistant. Include file names and code snippets where applicable.
  Optional Next Step: List the next step that you will take that is related to the most recent work you were doing. IMPORTANT: ensure that this step is DIRECTLY in line with the user's explicit requests, and the task you were working on immediately before this summary request. If your last task was concluded, then only list next steps if they are explicitly in line with the users request. Do not start on tangential requests without confirming with the user first. If there is a next step, include direct quotes from the most recent conversation showing exactly what task you were working on and where you left off. This should be verbatim to ensure there's no drift in task interpretation.
  Here's an example of how your output should be structured:

  [Your thought process, ensuring all points are covered thoroughly and accurately]
  1. Primary Request and Intent: [Detailed description]
  Key Technical Concepts:

  [Concept 1]
  [Concept 2]
  [...]
  Files and Code Sections:

  [File Name 1]
  [Summary of why this file is important]
  [Summary of the changes made to this file, if any]
  [Important Code Snippet]
  [File Name 2]
  [Important Code Snippet]
  [...]
  Errors and fixes:

  [Detailed description of error 1]:
  [How you fixed the error]
  [User feedback on the error if any]
  [...]
  Problem Solving: [Description of solved problems and ongoing troubleshooting]

  All user messages:

  [Detailed non tool use user message]
  [...]
  Pending Tasks:

  [Task 1]
  [Task 2]
  [...]
  Current Work: [Precise description of current work]

  Optional Next Step: [Optional Next step to take]

  Please provide your summary based on the conversation so far, following this structure and ensuring precision and thoroughness in your response.

  There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the above summary. Examples of instructions include:

  Compact Instructions
  When summarizing the conversation focus on typescript code changes and also remember the mistakes you made and how you fixed them.

  ## Summary instructions When you are using compact - please focus on test output and code changes. Include file reads verbatim.
  ```
* **Validation**:

  + Enforce JSON Schema on response; reject/resample if invalid (JSON Schema [spec](https://json-schema.org/)).
  + Confidence calibration: isotonic regression on offline eval to map model scores to calibrated \(p\in\[0,1]\) (scikit-learn Isotonic Regression [docs](https://scikit-learn.org/stable/modules/isotonic.html)).

### Model-family tuning and formatting

* The transcript notes model-specific prompt tuning. Keep separate prompt bundles per model family \(\mathcal{P}\_\text{sonnet}, \mathcal{P}\_\text{haiku}, ...\).
* Use structured headings and XML-like tags in prompts; Claude models respect these semantics and Anthropic’s docs illustrate how system prompts are paired with tool use, including computer-use variants that inject tool-specific system text ([tools overview](https://docs.claude.com/en/docs/build-with-claude/tool-use), [computer-use system prompts](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/computer-use-tool)).

## Prompting vs. fine-tuning vs. RAG (what to use when, and how)

* This section gives a concrete decision framework for an AI Code CLI, then shows implementable recipes (with prompts) for each approach.
* Where relevant, the design maps to Claude’s tool-use message model and CLI behaviors as documented in Anthropic’s tool-use and Messages API docs and the Claude Code pages ([tool-use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview), [how to implement tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use), [Messages API](https://docs.anthropic.com/en/api/messages), [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview), [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)).

### Decision framework (cost/latency math)

* Let a task induce \(n\) LLM calls with per-call token count \(t\_i\) and per-token price \(p\). Pure prompting cost

\[J\_{\text{prompt}} = p\sum\_{i=1}^{n} t\_i.\]

* Adding retrieval with \(q\) embedding calls (avg length \(e\)), ANN search overhead \(\kappa\), and shorter prompts \(t'\_i\):

\[J\_{\text{RAG}} = p\sum\_{i=1}^{n} t'\_i + p\_{\text{embed}}\cdot q e + \kappa.\]

* RAG is beneficial when \(\sum\_i (t\_i - t'\_i) > \frac{p\_{\text{embed}}}{p}\,q e + \frac{\kappa}{p}\).
* Fine-tuning changes behavior so the same task completes in \(n'\) calls with tokens \(t''\_i\) and higher tool-call accuracy; add a fixed training amortization \(A/T\) over \(T\) tasks:

\[J\_{\text{ft}} = p\sum\_{i=1}^{n'} t''\_i + \frac{A}{T}.\]

* Choose the minimum of \(J\_{\text{prompt}}, J\_{\text{RAG}}, J\_{\text{ft}}\) subject to reliability targets (tool-call precision/recall) and latency SLOs. Claude’s integrated tool-use message structure makes the RAG and tool orchestration straightforward: user messages can carry `tool_result` blocks; assistant messages emit `tool_use` blocks. ([implement tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use)).

### Prompting: primary lever for tool accuracy and “feel”

* Transcript takeaway: the core workflows live in the system prompt and verbose tool descriptions, reiterated with examples. Claude’s API respects structured message blocks and long, example-rich tool descriptions; do not rely on one-line schemas ([tool-use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)).
* System prompt excerpt (agent role and workflows; use XML-like tags and repeated “IMPORTANT” cues):

```
<SYSTEM_ROLE>
You are a local code CLI agent for . Never run destructive commands without explicit user approval.
</SYSTEM_ROLE>

<WORKFLOWS>
  <PLANNING>
    IMPORTANT: Use todo.write to create a plan before edits. Keep 3–7 steps for complex tasks.
  </PLANNING>
  <EXECUTION>
    Read → Edit (minimal diff) → Lint+Typecheck → Test → Iterate until green.
  </EXECUTION>
  <CONSTRAINTS>
    Do not commit. Do not add comments unless the user asked.
  </CONSTRAINTS>
</WORKFLOWS>

<REMINDER_PATTERN>
After any todo.write, reinsert: “There is an active to-do list; update statuses; run lint/typecheck after edits.”
</REMINDER_PATTERN>
```

Tool description pattern (long, example-heavy):

```
{
  "name": "todo.write",
  "description": "Manage a checklist for the current session. ALWAYS create or update before non-trivial work. Examples: ...",
  "input_schema": { "type": "object", "properties": { "items": {...}, "mode": {...}, "mark": {...} }, "required": ["items"] }
}
```

* Sub-agent tool schema (stateless delegation returning a single report):

```
{
  "name": "task.launch_agent",
  "description": "Launch a specialized sub-agent (e.g., requirements-analyzer). It has its own system prompt and tools; only its final report is returned.",
  "input_schema": {
    "type":"object",
    "properties":{
      "agent_type":{"type":"string","enum":["requirements-analyzer","general-purpose"]},
      "system_prompt":{"type":"string"},
      "task":{"type":"string"},
      "context_files":{"type":"array","items":{"type":"string"}},
      "expected_outputs":{"type":"array","items":{"type":"string"}}
    },
    "required":["agent_type","task","expected_outputs"]
  }
}
```

* Init and compact prompts should explicitly enumerate files to read first (`CLAUDE.md`, editor rules, Copilot instructions) and, when compacting, preserve file paths, diffs, pending todos, and decisions.

### RAG for code (repo-aware retrieval that the agent can trust)

* **Goal:** reduce prompt length and improve relevance by retrieving only the minimal code/doc context the model needs.
* **Indexing pipeline**

  + **Chunking.** Prefer AST-aware chunking (e.g., per function/class with sliding window) to naive fixed-size chunks. Let average chunk size be \(c\) tokens with overlap \(\delta\).
  + **Embeddings.** Use a strong code/text embedding model; store vectors in an ANN index (HNSW/IVF). Maintain metadata: path, language, symbols, last commit, test coverage.
  + **Freshness.** Update on each Git change via lightweight background jobs or pre-commit hooks.
* **Query pipeline**

  + Rewrite. From the user request and active plan, produce a retrieval query \(q\).
  + Hybrid search. Combine BM25 and vector search with reciprocal rank fusion

    \[\text{RRF}(d) = \sum\_{s\in\{\text{BM25},\,\text{ANN}\}} \frac{1}{k + \text{rank}\_s(d)},\]
    - pick top-\(k\) with diversification over paths.
* **Snippet construction.** Build a compact context block with line numbers and symbols; cap to \(\approx\) \(8\%\) of remaining context budget to avoid starving the tool-use planner.
* **Injection strategy**:

  + Provide retrieved snippets as a dedicated content block in the next user message (as `tool_result`), keeping the assistant free to emit new `tool_use` calls. This aligns with Claude’s user/assistant block model ([tool-use message structure](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use)).

**Prompts**:

```
  <RETRIEVAL_INSTRUCTIONS>
  Given the task and current plan, request only the smallest set of files/symbols needed.
  Prefer function-level snippets with line numbers over whole files.
  If retrieval is ambiguous, ask to read specific files via tools.read before editing.
  </RETRIEVAL_INSTRUCTIONS>
```

* **When to turn RAG on**:

  + Large repos, multi-file refactors, or when the same libraries repeat across tasks.
  + Empirically, turn on when expected token savings per call exceeds the embed+search overhead per Section 3.1.

### Fine-tuning: when you actually need it (and what to train on)

Use fine-tuning if you need model-family-specific habits the prompt cannot reliably induce: stable tool-call sequencing for your tool catalog, consistent plan-first behavior, editor-style diffs, or house style constraints. Availability varies by provider and model; e.g., Anthropic announced GA fine-tuning for Claude 3 Haiku on Amazon Bedrock ([Anthropic post](https://www.anthropic.com/news/fine-tune-claude-3-haiku-ga)).

#### Data you need

* High-quality traces from your CLI: (system prompt, tool catalog) + (user text) + (assistant `tool_use` sequence) + (`tool_result`) + (final answer).
* Label success/fail and attach diffs, test outcomes, lint/typecheck logs.

#### Training recipe (SFT first, optional preference training later)

* Supervised fine-tune on full successful traces emphasizing tool-use JSON, not just prose.
* Optional DPO/IPO on pairs where the winning trace used fewer steps, passed tests, and respected non-destructive constraints.
* Keep a prompt-first fallback: even with FT, you will still ship model-family-specific prompt bundles (transcript observation).

#### When not to fine-tune

* If prompt changes fix the behavior reliably.
* If you change base models often (prompt portability beats model-specific checkpoints).
* If your provider’s model lacks FT support for your chosen size; stick to prompting+RAG.

### Reinforcement Learning with Verifiable Process Rewards

* For a multi-agent Code CLI such as Codex-like architectures, reinforcement learning (RL) can refine the decision policy beyond supervised traces. Instead of optimizing on scalar task success only, we define a **process-based reward** that evaluates intermediate behaviors—planning quality, tool-call correctness, verification adherence, and efficiency—at each step. The training objective is to maximize cumulative verifiable rewards while maintaining alignment with supervised behavior.

#### Process-level reward decomposition

* Each trajectory consists of a sequence of tool interactions and model responses:

  \[\tau = (s\_0, a\_0, r\_0, s\_1, a\_1, r\_1, \dots, s\_T)\]
  + where \(s\_t\) encodes the current context (prompt + history + workspace state), \(a\_t\) is a `tool_use` or text action, and \(r\_t\) is a process reward computed from observable outcomes.
* We decompose \(r\_t\) into verifiable components:

\[r\_t = w\_p R\_{\text{plan}} + w\_c R\_{\text{toolcall}} + w\_v R\_{\text{verify}} + w\_o R\_{\text{outcome}} - w\_s R\_{\text{safety}} - w\_\ell R\_{\text{latency}}\]

* **Planning reward \(R\_{\text{plan}}\)** — checks whether a `todo.write` occurred before edits, whether tasks are structured correctly, and if reminders were inserted. Computed by rule-based parsing of message logs.
* **Tool-call reward \(R\_{\text{toolcall}}\)** — verifies that tool invocations match schemas, arguments are valid, and no disallowed calls appear. Fully verifiable via schema validators.
* **Verification reward \(R\_{\text{verify}}\)** — depends on lint/typecheck/test outcomes after each edit. Deterministic and programmatically verifiable.
* **Outcome reward \(R\_{\text{outcome}}\)** — final success signal (tests pass, diff minimal, no regressions). Usually verifiable, but if task quality is open-ended, it falls back to model-judged preference.
* **Safety penalty \(R\_{\text{safety}}\)** — applied negatively to discourage unsafe or unsandboxed behavior such as forbidden shell operations, unverified file edits, or system-level commands. Deterministic via rule-based safety validators.
* **Latency penalty \(R\_{\text{latency}}\)** — measures end-to-end response time between consecutive actions or tool completions:

  \[R\_{\text{latency}} = \frac{t\_{a\_t}^{\text{end}} - t\_{a\_t}^{\text{start}}}{t\_{\text{max}}}\]
  + normalized by a maximum tolerable delay \(t\_{\text{max}}\). The penalty discourages unnecessary tool-calls, redundant reasoning chains, and excessive deliberation.

#### Reward model and fallback for non-verifiable aspects

* Some aspects of reasoning, code clarity, or UX helpfulness cannot be verified automatically. For those, use a **reward model** trained on human preference data or an **LLM-as-a-Judge**:
* Train a small transformer or adapter head \(R\_\phi(x)\) on pairs of traces \((\tau^+, \tau^-)\) with human or model-judged preference labels, optimizing a Bradley–Terry likelihood:

  \[\mathcal{L}\_{\text{pref}} = -\log \sigma(R\_\phi(\tau^+) - R\_\phi(\tau^-))\]
* Alternatively, use an external LLM with a rubric prompt (“Judge which agent trace better followed instructions and maintained safety”) to produce pseudo-labels for \(R\_\phi\).
* During RL, these learned scores are combined with deterministic rule-based components into a single scalar reward:

\[\tilde{r}\_t = (1 - \lambda\_h) r\_t^{\text{verifiable}} + \lambda\_h R\_\phi(\tau\_{\le t})\]

#### Implementation for multi-agent CLI training

* **Environment:** simulate CLI sessions with a sandboxed executor; each agent’s tool actions are executed and logged.
* **Reward pipeline:** rule-based scripts compute verifiable metrics (including timing metrics and safety flags); the reward model fills gaps.
* **Algorithm:** preference-optimized policy gradient (e.g., PPO, DPO, or IPO) using messages and tool-calls as the action space.
* **Penalty integration:** safety and latency penalties are applied at each step; reward normalization ensures stability during training.
* **Credit assignment:** process rewards encourage intermediate correctness, safety, and efficiency—not just end success.

### Recommended baseline for an AI Code CLI in 2025

* Base model. Claude Sonnet 4 (balanced cost/capability for agentic coding; see Sonnet 4 overview) with integrated tool use via Messages API ([Sonnet 4 page](https://www.anthropic.com/claude/sonnet), [Messages API](https://docs.anthropic.com/en/api/messages)).
* Prompt bundle. System prompt + verbose tool descriptions + reminder pattern + init/compact prompts. Keep a separate bundle per model family.
* Retrieval. Lightweight code-RAG with AST-aware chunking and hybrid search; inject as `tool_result` blocks.
* Optional FT. Only after you have weeks of good traces and a measured gap that prompting cannot close.

### Guardrails and evals

* Track tool-call precision/recall, pass-rate of lint/typecheck/test loops, and average calls per task.
* Use golden tasks and repo snapshots; record deltas and outcomes automatically from CLI traces.
* Re-tune prompts per model family; tool-use semantics can differ slightly across deployments and providers ([Messages/tool-use docs](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use)).

## Agent loop internals and reliability engineering

* This section turns the prompt-first architecture into a concrete, reproducible loop: plan → gather context → edit → verify → iterate, with sub-agents, reminders, retries, and compaction. We map this to Claude’s Messages API and tool-use message model, which natively supports assistant `tool_use` blocks and user `tool_result` blocks (see tool-use overview and Messages API; this is the canonical flow used by Claude Code’s CLI) ([tool-use overview](https://docs.anthropic.com/en/docs/build-with-claude/tool-use), [how to implement tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use), [Messages API](https://docs.anthropic.com/en/api/messages), [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)).

### Control loop (decision policy)

* At turn \(t\), choose the next action \(a\_t \in \{\text{todo.write}, \text{read}, \text{edit}, \text{lint}, \text{typecheck}, \text{test}, \text{launch\\_agent}, \text{summarize}, \text{finalize}\}\) by maximizing utility

  \[U(a\_t)=\alpha \cdot \Delta P\_{\text{success}}(a\_t)-\beta \cdot \Delta \text{Tokens}(a\_t)-\gamma \cdot \Delta \text{Latency}(a\_t),\]
  + subject to hard constraints: no destructive shell, no commits without consent, and post-edit verification gates. In practice, you let the LLM propose `tool_use`; your client enforces constraints and adds reminders/guardrails before resuming the loop (assistant emits `tool_use`; client returns `tool_result` and optional reminder; repeat per the Messages API) ([Messages examples](https://docs.anthropic.com/en/api/messages-examples)).

### Planning-first: persistent to-do with reminders

* Claude Code’s reliability stems from reiterated instructions and a persistent checklist. Recreate this by forcing a todo.write on the first non-trivial turn and after any major phase shift, then injecting a short reminder block. This mirrors the approach described in Anthropic’s tool-use docs (use verbose tool descriptions; repeat critical policies) and in the CLI’s own guidance. Link the reminder to lint/typecheck/test gates to raise adherence. ([tool-use overview](https://docs.anthropic.com/en/docs/build-with-claude/tool-use), [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)).

### Context gathering: minimal reads and repo-aware retrieval

* The agent should prefer targeted reads over whole files and may request retrieval results if you’ve enabled code-RAG (Section 3). Provide file reads as `tool_result` blocks in user messages, keeping the assistant free to propose new `tool_use` calls. This is idiomatic for Claude’s tool-use message structure, and you can complement it with the Web Fetch/Search tools where internet context is allowed ([how to implement tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use), [Web search tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

### Edit-verify loop with hard gates

* After any edit, enforce verification gates:

  + **Gate 1: Lint/typecheck**. Run linters and type checkers; block progression until zero errors.
  + **Gate 2: Tests**. Run fast unit tests; if failing, iterate with minimal diffs.
* Claude’s code-execution and bash/text-editor tools provide standard patterns for “run tests then fix minimal diff”; you can model these as custom tools if you’re not using Anthropic’s built-ins ([Code execution tool](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)).

### Sub-agents: stateless delegation and summary return

* Treat sub-agents as a tool. The main agent emits a `task.launch_agent` call containing an `agent_type`, `system_prompt`, task, and `expected_outputs`. Your client starts a fresh Messages session for the sub-agent, runs it until it returns a final assistant message (no tools), then injects only that final report back as the `tool_result`. Discard the sub-history to bound context. This mirrors the CLI’s pattern and keeps the main loop focused ([Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview), [tool-use overview](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)).
* Sub-agent launch tool schema (client-side registration):

```
{
  "name": "task.launch_agent",
  "description": "Launch a specialized sub-agent; return one final report only.",
  "input_schema": {
    "type":"object",
    "properties":{
      "agent_type":{"type":"string","enum":["requirements-analyzer","general-purpose","playwright-test-engineer"]},
      "system_prompt":{"type":"string"},
      "task":{"type":"string"},
      "context_files":{"type":"array","items":{"type":"string"}},
      "expected_outputs":{"type":"array","items":{"type":"string"}}
    },
    "required":["agent_type","task","expected_outputs"]
  }
}
```

### Reliability via prompt structure and examples

* Reiterate critical behaviors across sections in the system prompt and in tool descriptions. Use XML-like tags, uppercase cues (IMPORTANT / NEVER), and concrete examples. Provide negative examples (what not to do) beside positive ones. Anthropic’s docs emphasize verbose tool definitions and example-driven schemas; short one-liners underperform ([tool-use overview](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)).
* Example negative/positive pair inside the `todo.write` description:

```
Do: Create 3–7 items with “Run lint/typecheck” and “Run tests” as distinct steps.
Do not: Skip planning and jump straight to edit; do not combine lint/typecheck/test into one vague step.
```

### Retry, adjudication, and self-checks

* **Deterministic retries**. On tool failure or violation, re-ask with a short, high-precision “fix-up” system addendum. Keep temperature low and seed fixed.
* **Self-check prompt**. Before finalize, ask the model to verify that all gates passed and that no destructive actions were taken.
* **Adjudication**. For critical diffs, run a cheap second pass (e.g., smaller model) to score the diff’s risk; continue only if \(s\_{\text{risk}} < \tau\).
* Self-check block inserted before finalize:

  ```
  <SELF_CHECK>
  Confirm: (1) All planned todos are completed, (2) Lint/typecheck/tests passed, (3) No destructive shell commands were run, (4) Changes minimal and scoped.
  If any fail, propose exactly one next tool call.
  </SELF_CHECK>
  ```

### Memory and compaction (when history nears limit)

* When \(\|H\_t\|\ge C\_{\text{max}}-\epsilon\), call a summarizer sub-agent to produce a compact artifact that preserves: decisions, file paths, key diffs, failing/passing tests, and the active todo list. Replace early turns with the artifact. This exactly follows the multi-message pattern supported by the Messages API and aligns with Claude Code’s practice of compacting when running out of context ([Messages API](https://docs.anthropic.com/en/api/messages), [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)).

### Tool catalog: minimal but verbose

* Register a small set of tools with rich descriptions and examples (read, edit, `todo.write`, lint, typecheck, test, `task.launch_agent`). Claude’s tool runtime will validate inputs against the input\_schema fields and surface `tool_use` blocks accordingly; you provide `tool_result` blocks with outputs and logs ([tool-use on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html)).

## Serving pipeline (end-to-end infra, streaming, cost controls, and observability)

* This section turns the agent loop into a production-grade service: request shaping, streaming, tool execution, sub-agent fan-out, retries/idempotency, caching, rate limits, and telemetry. Where relevant, I link directly to vendor docs inline and cite them.

### Control plane and request path

* User input enters a stateless gateway that assembles a Messages request: system prompt bundle, verbose tool schemas, current history \(H\_t\), and optional retrieval/`tool_result` blocks. Prefer a single abstraction that targets three providers: Anthropic native Messages API, Amazon Bedrock, and Google Vertex AI.
* **Provider adapters**:

  + **Anthropic native.** Use the Messages API; enable SSE streaming via `"stream": true`. See Streaming Messages and API reference ([streaming](https://docs.anthropic.com/en/docs/build-with-claude/streaming), [Messages API](https://docs.anthropic.com/en/api/messages)).
  + **Amazon Bedrock.** Use InvokeModel or InvokeModelWithResponseStream for streaming; the Messages+tools parameters map 1:1, including tool routing. See Bedrock model parameters and Messages API on Bedrock ([model params](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-claude.html), [messages on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html)).
  + **Google Vertex AI.** Call Claude via Vertex AI endpoints; responses can be streamed with SSE. See Vertex partner-model docs and request walkthrough ([models on Vertex](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude), [use Claude on Vertex](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/use-claude), [Anthropic’s Vertex guide](https://docs.anthropic.com/en/api/claude-on-vertex-ai)).
* **Message shaping**:

  + Tools registered with rich descriptions and examples; control tool routing with `tool_choice` values auto/any/tool/none. See “How to implement tool use” ([docs](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use)).
  + When using Claude Code as a reference interface, its CLI flags and settings map to these same underlying calls. See Claude Code overview/CLI reference/settings ([overview](https://docs.anthropic.com/en/docs/claude-code/overview), [CLI reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference), [settings](https://docs.anthropic.com/en/docs/claude-code/settings)).

### Streaming, backpressure, and UX

* **Server-sent events (SSE).** Stream tokens to reduce perceived latency; multiplex incremental `tool_use` decisions and partial text. Anthropic supports `"stream": true`; Bedrock exposes InvokeModelWithResponseStream; Vertex AI supports SSE for Claude endpoints ([Anthropic streaming](https://docs.anthropic.com/en/docs/build-with-claude/streaming), [Bedrock streaming](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-claude.html), [Vertex streaming note](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude)).
* **Flow control.** Apply token-bucket for outbound events; coalesce non-user-visible deltas. For long tool runs, send periodic “activity” messages in-stream so the terminal UI stays responsive.
* Throughput estimate with \(Q\) concurrent sessions, average streamed latency \(\mathbb{E}[L]\): \(X \approx \frac{Q}{\mathbb{E}[L]}\) sessions/s. Size buffers so that \(B \ge \lambda \cdot \max\\_t \text{rate}(t)\) where \(\lambda\) is a safety factor.

### Tool execution plane

* **Execution adapters.** Each `tool_use` yields a local adapter (read/edit/grep/lint/typecheck/test) executed in a sandbox. Return outputs as `tool_result` blocks in the next user message; this is the canonical flow for Claude tool use ([tool-use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)).
* **Sub-agents as a tool.** Implement a special `task.launch_agent` adapter that starts a fresh Messages session with a sub-agent prompt, runs it to completion, and returns only its final report as `tool_result` (discarding its inner history to cap context). This mirrors documented agent patterns and the CLI’s practice ([Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)).
* **Provider specifics.** On Bedrock, note the polymorphic tools format and `anthropic_beta` flags when opting into certain tool types (e.g., computer use). See Bedrock’s tool-use page ([docs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html)).

### Retries, idempotency, and circuit breakers

* **Idempotency keys.** Hash \(H\_t\) plus input to avoid duplicate side effects on network retries.
* **Deterministic retries.** On tool validation errors, issue a short “fix-up” system addendum and re-invoke with low temperature.
* **Circuit breaking.** Trip if rolling error rate \(>\tau\) or if average tool latency exceeds SLO.

### Caching and cost control

* Total expected cost per task is: \(J = p \sum\_{i=1}^{n} t\_i + p\_{\text{embed}} \cdot q e + \kappa,\) matching what we discussed earlier. Use three caches:
  + **Prompt bundle cache.** Content-hash the system prompt + tool schemas + static instructions; reuse across turns.
  + **Retrieval cache.** For RAG, cache ANN/BM25 results by (query, repo-commit) to avoid recomputation.
  + **Response shard cache.** If your gateway splits long reads into multiple assistant turns, persist previously streamed prefixes and resume after reconnects.
* **Provider controls:**

  + **Anthropic:** cap tokens and enable streaming in Messages; see API body fields ([Messages API](https://docs.anthropic.com/en/api/messages), [streaming](https://docs.anthropic.com/en/docs/build-with-claude/streaming)).
  + **Bedrock/Vertex:** apply per-request max tokens and concurrency limits using their SDKs and service quotas ([Bedrock params](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-claude.html), [Vertex guide](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/use-claude)).

### Rate limits and concurrency

* Let provider quota be \(R\_{\text{max}}\) requests/s and token rate \(T\_{\text{max}}\) tokens/s. Choose concurrency \(Q\) such that

  \[Q \le \min\!\Bigg( \frac{R\_{\text{max}}}{\rho},\ \frac{T\_{\text{max}}}{\mathbb{E}[\text{tokens/req}]}\Bigg),\]
  + where \(\rho\) accounts for burst smoothing. Implement adaptive backoff with EWMA of request and token rates.

### Observability and audit

* **Traces.** One span per LLM call and one child span per tool execution. Attach input/output sizes, tool names, exit codes, and pass/fail for lint/typecheck/test.
* **Structured logs.** Persist: selected prompt bundle hash, tool catalog version, model id, token counts, timing, and diff sizes. Redact secrets.
* **Session artifacts.** Save the compaction summaries and final reports to aid handoff. Claude Code exposes similar surfaces via CLI usage/flags for debugging ([CLI usage](https://docs.anthropic.com/en/docs/claude-code/cli-usage)).

### Configuration and environments

* **Environment variables.** Provide `ANTHROPIC_API_KEY`, optional base URL override, and project-level JSON settings for tools and permissions. Claude Code documents project and global settings files, environment variables, and MCP tool configuration ([settings](https://docs.anthropic.com/en/docs/claude-code/settings)).
* **Cloud endpoints.** For organizations on AWS or GCP, route via Bedrock or Vertex to centralize IAM, networking, and billing ([Claude on Bedrock](https://docs.anthropic.com/en/api/claude-on-amazon-bedrock), [Claude Code on Vertex AI](https://docs.anthropic.com/en/docs/claude-code/google-vertex-ai)).
* **Local development.** Provide a dev profile with a fake tool executor and a “dry-run” shell to test tool JSON without touching the workspace.

### Minimal streaming client (TypeScript, SSE)

```
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const stream = await client.messages.create({
  model: "claude-3-7-sonnet-latest",
  system, messages, tools, tool_choice: "auto",
  stream: true
});

for await (const event of stream) {
  if (event.type === "message_start") /* init UI */;
  if (event.type === "content_block_delta") /* append text */;
  if (event.type === "tool_use") /* show pending tool */;
  if (event.type === "message_stop") /* finalize */;
}
```

* This mirrors the documented streaming/events surface; wire your tool executor to consume emitted `tool_use` blocks and post `tool_result` blocks back in the next turn ([streaming](https://docs.anthropic.com/en/docs/build-with-claude/streaming), [tool-use overview](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)).

### Deploy shapes

* **Single-tenant CLI** with local tool executors; optional cloud LLM calls.
* **Multi-tenant service** behind an API gateway; per-org model routing (Anthropic vs Bedrock vs Vertex).
* **Enterprise** with private networking, audit retention, and centralized settings mirroring Claude Code’s documented configuration surfaces ([Claude Code settings](https://docs.anthropic.com/en/docs/claude-code/settings)).

## Evaluation and benchmarking

* This section gives you a reproducible eval stack for a Code CLI: offline (quantitative and HITL/qualitative) and online (A/B and interleaving). It uses executable, repo-level tasks (e.g., SWE-bench), unit-test suites (HumanEval-style), rubric-driven human review, and production experiments.
* For foundational references, see HumanEval’s code-generation evaluation, SWE-bench and SWE-bench Verified, and Anthropic’s guidance and console-based Evaluation Tool for building task-specific tests ([HumanEval](https://arxiv.org/abs/2107.03374), [SWE-bench paper](https://arxiv.org/abs/2310.06770), [SWE-bench leaderboards](https://www.swebench.com/), [SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/), [Anthropic eval principles](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests), [Anthropic Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)).

### What to measure

* Let success at run \(j\) be \(s\_j \in \{0,1\}\) (tests pass, requirements met), total tokens \(t\_j\), latency \(\ell\_j\), and price/token \(p\). Core KPIs:

  + **Task success rate** \(\text{SR}=\frac{1}{N}\sum\_{j=1}^{N} s\_j\).
  + **Cost** \(J = p\cdot \frac{1}{N}\sum\_{j=1}^{N} t\_j\).
  + **Edit minimality** via diff size \(\Delta\_j = \text{lines\\_changed}\_j\) and proportion-of-file-changed \(\delta\_j = \frac{\Delta\_j}{\text{lines\\_file}}\).
  + **Tool-call quality**: precision/recall over ground-truth tool sequence \(G\) vs. produced \(\hat G\): \(\text{P}=\frac{\|G\cap \hat G\|}{\|\hat G\|},\ \text{R}=\frac{\|G\cap \hat G\|}{\|G\|}\).
  + **Safety**: disallowed tool-call rate per 100 runs.
  + **User-centric** (for online): completion, revert rate, sticky usage, satisfaction score.

### Offline evaluation (quantitative, automated)

* **Unit-test benchmarks (function-level)**. HumanEval-style harness: for each prompt, the agent edits or writes code, and the grader runs hidden tests; compute pass\@1 or pass\@k. This is ideal for measuring synthesis/repair under controlled conditions ([HumanEval paper](https://arxiv.org/abs/2107.03374)).
* **Repo-level, end-to-end benchmarks**. Use SWE-bench to evaluate realistic bug-fix/feature tasks inside real repos (environment bootstrap, apply patch, run tests). Prefer SWE-bench Verified for human-filtered items that better reflect true solvability; track success, retries, and diff size ([SWE-bench](https://arxiv.org/abs/2310.06770), [Verified subset](https://openai.com/index/introducing-swe-bench-verified/), [leaderboards](https://www.swebench.com/)).
* **Prompt bundle and tool variants**. Because the CLI is prompt-first, treat each prompt bundle/tool-catalog as an experiment factor; run a full-factorial or Latin square across benchmarks to isolate effects (e.g., reminder reinsertion on/off, sub-agents on/off).
* **LLM-as-a-judge for non-executable criteria**. When you can’t auto-grade (readability, rationale quality), use an LLM judge with pairwise prompts, but always calibrate on a small human-labeled set and report agreement (Cohen’s \(\kappa\) or Krippendorff’s \(\alpha\)). Anthropic recommends task-specific, automatable tests when possible ([eval principles](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests)).
* **Cost/latency curves**. Plot \((\text{SR}, J, \ell)\) Pareto fronts for each configuration to choose defaults at fixed budgets.

### Harness tips

* Containerize repos; pin toolchains; record traces and tool I/O; seed for determinism; shard by repo. Use Anthropic’s console Evaluation Tool for quick prompt-bundle regressions; migrate winning configs into your scripted harness ([Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)).

### Offline evaluation (qualitative, HITL)

* **Rubric design**. Create 1–5 Likert rubrics for code clarity, minimality, architectural fit, and test quality. Provide concrete anchors (e.g., 1 = breaks style and tests; 5 = minimal diff, idiomatic, comprehensive tests).
* **Sampling**. Stratify by task type and difficulty (e.g., SWE-bench tags); sample \(n\) per stratum to keep CI width \(<\varepsilon\).
* **Blinding**. Blind annotators to model/prompt condition; randomize order; include gold checks.
* **Agreement**. Report inter-rater reliability; resolve by adjudication with a senior reviewer.
* **Turn logs**. Review planning adherence (`todo.write` usage), tool-call mistakes, and compaction summaries to attribute failures to prompt/tool design, matching Anthropic’s advice to be task-specific and example-heavy in definitions ([tool-use best practices](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use)).

### Online evaluation (A/B, interleaving)

* **Fixed-horizon A/B**. Randomly assign users to control vs. treatment prompt bundle or model. Primary metric might be per-session completion; use a two-proportion z-test or Bayesian posterior for uplift:

  + Difference in rates \(\hat d = \hat p\_T - \hat p\_C\), standard error \(\text{SE}=\sqrt{\frac{\hat p\_T(1-\hat p\_T)}{n\_T}+\frac{\hat p\_C(1-\hat p\_C)}{n\_C}}\); 95% CI \(\hat d \pm 1.96\,\text{SE}\).
  + Guardrails: error spikes, tool-failure rates, safety violations.
  + Power analysis to size \(n\) for minimum detectable effect.
    See Kohavi’s practical guide for experiment hygiene (pre-registration, no peeking, invariant metrics) ([A/B testing guide](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-ab-testing)).
* **Interleaving for ranked suggestions**. When comparing ranked outputs (e.g., quick-fix candidates, file read priorities), use team-draft interleaving to boost sensitivity and reduce required traffic; measure click/accept wins per session ([Airbnb interleaving explainer](https://medium.com/airbnb-engineering/beyond-a-b-test-speeding-up-airbnb-search-ranking-experimentation-through-interleaving-7087afa09c8e), [academic PDF](https://assets.amazon.science/c1/4d/7945330e47539fdd870cb5c73613/interleaved-online-testing-in-large-scale-systems.pdf)).
* **Counterfactual sanity checks (optional)**. Before shipping an online test, estimate expected uplift with off-policy estimators on logs to avoid bad experiments; this isn’t perfect for agents but can catch egregious regressions ([offline A/B for recommenders](https://arxiv.org/abs/1801.07030)).
* **Instrumentation**. Emit OpenTelemetry spans for each LLM/tool call with inputs/outputs redacted; attach metrics (tokens, latency, pass/fail). Use emerging OTel patterns for LLM/agent traces and vector DB spans ([OTel agent observability](https://opentelemetry.io/blog/2025/ai-agent-observability/)).

### Eval harness architecture

* **Replayable runner**. Given a task spec, seed, and repo snapshot, the runner executes the full agent loop, captures tool I/O, diffs, test logs, and final verdicts. Store artifacts for regrade.
* **Dataset registry**. Support HumanEval-like tests and SWE-bench-style repos; pin Docker images and language toolchains.
* **Aggregators**. Produce per-task JSONL; compute SR, cost \(J\), latency \(\ell\), diff minimality \(\delta\), and tool-call P/R; render Pareto charts and league tables.
* **Bridging**. Optionally trigger Anthropic’s Evaluation Tool from CI to smoke-test prompt changes before running the full suite ([Anthropic Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)).

### Reporting and decision rules

* **Dashboards**. SR over time, cost/latency distributions, tool precision/recall, safety violations per 100 runs, and A/B deltas with CIs. Tag runs by prompt bundle and model family.
* **Ship/no-ship**. Require \(\text{SR}\_\text{treat} - \text{SR}\_\text{ctrl} \ge \tau\_s\) and \(J\_\text{treat} - J\_\text{ctrl} \le \tau\_c\) with 95% CI excluding zero; enforce no regressions on guardrails.
* **For agents**. Add a plan-adherence KPI: probability that the agent called `todo.write` before first edit and reinserted reminders at major phases.

## Monitoring, observability, and logging (OpenTelemetry + CloudWatch/CloudTrail + Grafana)

### Goal

* Emit rich, privacy-safe telemetry for every LLM turn, tool call, retrieval, and verification step; ship it over OTLP to an OpenTelemetry Collector; export traces to AWS X-Ray, metrics/logs to CloudWatch (and/or Loki), and visualize in Grafana. Use GenAI semantic conventions so spans/metrics are comparable across providers. See OpenTelemetry’s generative-AI semantic conventions and Node.js SDK guides, plus the Collector’s transform processors for redaction.
* Refer [GenAI semconv](https://opentelemetry.io/docs/specs/semconv/gen-ai/), [AI agent observability](https://opentelemetry.io/blog/2025/ai-agent-observability/), [Node SDK](https://opentelemetry.io/docs/languages/js/getting-started/nodejs/), [instrumentation](https://opentelemetry.io/docs/languages/js/instrumentation/), [Collector transform](https://opentelemetry.io/docs/collector/transforming-telemetry/), [sensitive data handling](https://opentelemetry.io/docs/security/handling-sensitive-data/).

### What to collect (signals and keys)

* **Traces**:
  + Spans: llm.request, llm.tool\_call, retrieval.query, tool.exec, test.run, lint.run. Use GenAI/LLM attributes such as gen\_ai.system, gen\_ai.operation, gen\_ai.request.model, gen\_ai.request.temperature, gen\_ai.response.id, gen\_ai.usage.input\_tokens, gen\_ai.usage.output\_tokens. For tool calls, add tool.name and tool.error if any.
  + Refer [GenAI semconv](https://opentelemetry.io/docs/specs/semconv/gen-ai/), [AI agent observability blog](https://opentelemetry.io/blog/2025/ai-agent-observability/).
* **Metrics**:
  + Counters/gauges: llm\_calls, tokens\_in, tokens\_out, cost\_estimate \(\hat{J}=p\cdot(\text{tokens\\_in}+\text{tokens\\_out})\), tool\_failures, test\_pass\_rate, latency histograms per span kind. Emit via OTel SDK or Collector metrics transform.
  + Refer [Node SDK](https://opentelemetry.io/docs/languages/js/getting-started/nodejs/), [Collector transform](https://opentelemetry.io/docs/collector/transforming-telemetry/).
* **Logs**:
  + Structured JSON for decision summaries, diff sizes, lint/test outputs. Include `trace_id` and span\_id so Grafana can deep-link between logs and traces; see Loki’s native OTLP ingestion notes.
  + Refer [Loki OTLP ingestion](https://grafana.com/docs/loki/latest/send-data/otel/).

### In-process instrumentation (Node example)

Initialize OTel once at process start; wrap LLM and tool adapters with spans and attributes:

```
// telemetry.ts
import { diag, DiagConsoleLogger, DiagLogLevel, context, trace, SpanStatusCode } from "@opentelemetry/api";
import { NodeSDK } from "@opentelemetry/sdk-node";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";
import { OTLPMetricExporter } from "@opentelemetry/exporter-metrics-otlp-http";
import { PeriodicExportingMetricReader } from "@opentelemetry/sdk-metrics";

diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.ERROR);

export async function startTelemetry() {
  const sdk = new NodeSDK({
    traceExporter: new OTLPTraceExporter({ url: process.env.OTEL_EXPORTER_OTLP_TRACES_ENDPOINT }),
    metricReader: new PeriodicExportingMetricReader({
      exporter: new OTLPMetricExporter({ url: process.env.OTEL_EXPORTER_OTLP_METRICS_ENDPOINT }),
      exportIntervalMillis: 15000
    }),
    resource: /* add service.name=cli, service.version, deployment.environment */
  });
  await sdk.start();
}

export async function withLLMSpan(op: string, attrs: Record<string, any>, fn: () => Promise<any>) {
  const span = trace.getTracer("cli").startSpan("llm.request", {
    attributes: {
      "gen_ai.operation": op,
      "gen_ai.request.model": attrs.model,
      "gen_ai.request.temperature": attrs.temperature,
      "gen_ai.system": "anthropic"
    }
  });
  try {
    const res = await context.with(trace.setSpan(context.active(), span), fn);
    span.setAttributes({
      "gen_ai.response.id": res?.id,
      "gen_ai.usage.input_tokens": res?.usage?.input_tokens,
      "gen_ai.usage.output_tokens": res?.usage?.output_tokens
    });
    return res;
  } catch (e: any) {
    span.setStatus({ code: SpanStatusCode.ERROR, message: e?.message });
    throw e;
  } finally {
    span.end();
  }
}
```

This follows the official Node SDK shape; add HTTP/undici instrumentation if your client library isn’t already emitting spans. [Node SDK](https://opentelemetry.io/docs/languages/js/getting-started/nodejs/), [JS instrumentation](https://opentelemetry.io/docs/languages/js/instrumentation/).

### Collector topology and exporters (ADOT on AWS)

Run an OpenTelemetry Collector (or AWS Distro for OpenTelemetry, ADOT) as a sidecar/daemon. Export traces to AWS X-Ray, metrics to CloudWatch (EMF), and logs either to CloudWatch Logs or to Loki (Grafana). [ADOT + X-Ray](https://aws-otel.github.io/docs/getting-started/x-ray), [CloudWatch metrics via ADOT](https://aws-otel.github.io/docs/getting-started/cloudwatch-metrics), [X-Ray + ADOT overview](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html).

Minimal collector config (YAML):

```
receivers:
  otlp:
    protocols:
      http:
      grpc:

processors:
  memory_limiter: {}
  batch: {}
  transform/redact:
    error_mode: ignore
    traces:
      statements:
        - replace_pattern(attributes["gen_ai.request.prompt"], "(?s).+", "<redacted>")
    logs:
      statements:
        - delete_key(attributes, "raw_prompt")
        - set(attributes.cost_estimate, attributes.tokens_total * env("PRICE_PER_TOKEN"))

exporters:
  awsxray: {}         ## traces → X-Ray
  awsemf: {}          ## metrics → CloudWatch EMF
  awscloudwatchlogs:  ## alt: logs → CloudWatch Logs
    log_group_name: "/ai-code-cli"
  otlphttp/loki:      ## alt: logs → Loki OTLP endpoint
    endpoint: http://loki:3100/otlp
    tls: { insecure: true }

service:
  pipelines:
    traces:  { receivers: [otlp], processors: [memory_limiter, batch, transform/redact], exporters: [awsxray] }
    metrics: { receivers: [otlp], processors: [memory_limiter, batch],                    exporters: [awsemf] }
    logs:    { receivers: [otlp], processors: [memory_limiter, batch, transform/redact], exporters: [awscloudwatchlogs] }
```

The awsxray and awsemf exporters are standard in ADOT; use the transform processor to redact prompts/tokens before export. [ADOT getting started](https://aws-otel.github.io/docs/getting-started/x-ray), [Collector transform](https://opentelemetry.io/docs/collector/transforming-telemetry/), [sensitive data handling](https://opentelemetry.io/docs/security/handling-sensitive-data/).

Notes. You can also go “collector-less” with ADOT SDKs sending traces directly to OTLP/CloudWatch endpoints for small installs, but a Collector gives you redaction/routing control. [Collector-less traces](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLP-UsingADOT.html).

### CloudWatch/Grafana integration

* **CloudWatch in Grafana**: Add the CloudWatch data source; build dashboards from EMF metrics (tokens, latency, pass rate). [Grafana CloudWatch data source](https://grafana.com/docs/grafana/latest/datasources/aws-cloudwatch/).
* **X-Ray traces in Grafana**: Add the AWS X-Ray (Application Signals) data source to query/visualize traces and service maps from your OTel→X-Ray pipeline. [AWS docs](https://docs.aws.amazon.com/grafana/latest/userguide/x-ray-data-source.html), [plugin page](https://grafana.com/grafana/plugins/grafana-x-ray-datasource/), [using X-Ray data source](https://docs.aws.amazon.com/grafana/latest/userguide/xray-using.html).
* **Logs via Loki (optional)**: Loki accepts OTLP logs directly; set `allow_structured_metadata` to true and use otlphttp/logs exporter. Link logs to traces using `trace_id` labels for click-through. [Loki OTLP docs](https://grafana.com/docs/loki/latest/send-data/otel/), [OTLP→Loki example](https://grafana.com/docs/enterprise-logs/latest/send-data/otel/otel-collector-getting-started/).
* **Linking**: Grafana auto-links CloudWatch logs to X-Ray if the @xrayTraceId field is present, enabling “from error log → trace” workflows. [CloudWatch plugin linking](https://grafana.com/docs/plugins/cloudwatch/latest/configure/).

### CloudTrail for audit

* Enable CloudTrail in all regions to record control-plane activity (who ran what in AWS). Store to S3 and optionally forward to CloudWatch Logs for dashboards/alerts; use it to audit IAM/key usage by agent-side tools or CI. Correlate by timestamp/account and the userIdentity/session fields alongside your internal `trace_id`s. [CloudTrail docs](https://docs.aws.amazon.com/cloudtrail/), [CloudTrail API ref](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html).

### Privacy and redaction

* Redact prompts, code, and user PII at the Collector edge. Use transform and attributes processors to drop or hash fields, and keep only token counts, models, tools, and error codes for analytics. Maintain a short allowlist of attributes that can leave the VPC. [Sensitive data handling](https://opentelemetry.io/docs/security/handling-sensitive-data/), [transform processor](https://opentelemetry.io/docs/collector/transforming-telemetry/).

### Dashboards and SLOs

* **LLM health**: calls/s, p50/p95 latency, error rate \(\frac{\text{error\\_spans}}{\text{llm\\_spans}}\), tokens in/out, estimated cost \(\hat{J}\).
* **Agent reliability**: plan-adherence rate (`todo.write` before first edit), tool-call precision/recall, test pass rate.
* **Infra**: Collector queue size, dropped spans, exporter retry counts.
* **Alerting**: CloudWatch alarms on latency SLO breaches and spike in tool.exec failures; Grafana alert rules on Loki queries for “lint failure” or “test fail” patterns. [CloudWatch data source](https://grafana.com/docs/grafana/latest/datasources/aws-cloudwatch/).

### Deploy notes: Grafana Alloy

* Grafana Agent is deprecated in favor of Grafana Alloy (an OpenTelemetry Collector distribution). If you were using Agent, plan to migrate to Alloy before end-of-life; Alloy simplifies pipelines to Loki/Tempo/CloudWatch and is 100% OTLP-compatible. [Alloy announcement](https://grafana.com/blog/2024/04/09/grafana-agent-to-grafana-alloy-opentelemetry-collector-faq/), [Agent docs noting migration timeline](https://grafana.com/docs/agent/latest/), [migrate to Alloy](https://grafana.com/docs/loki/latest/setup/migrate/migrate-to-alloy/).

### Putting it together (reference flow)

1. App emits OTel spans/metrics/logs with GenAI semconv and trace/log correlation fields.
2. Collector/ADOT receives via OTLP, redacts, batches, and exports: traces→X-Ray, metrics→CloudWatch EMF, logs→CloudWatch Logs or Loki.
3. Grafana reads CloudWatch (metrics/logs) and X-Ray (traces), and optionally Loki for logs; cross-links traces ↔ logs via `trace_id`/@xrayTraceId.
4. CloudTrail provides a separate audit trail for AWS control-plane actions.

* This stack uses stable, vendor-supported paths and leaves room to expand to Grafana Tempo/Prometheus later without changing in-process instrumentation. [ADOT + X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-adot.html), [CloudWatch data source](https://grafana.com/docs/grafana/latest/datasources/aws-cloudwatch/), [X-Ray data source](https://docs.aws.amazon.com/grafana/latest/userguide/x-ray-data-source.html), [Loki OTLP ingestion](https://grafana.com/docs/loki/latest/send-data/otel/).

### References

* [I Reverse-Engineered Claude Code: Learn These Agent Tricks](https://www.youtube.com/watch?v=i0P56Pm1Q3U)
* [Claude Code Prompts](https://gist.github.com/yifanzz/2b89303adde9a00e96e61a2d4b31016a?utm_source=beyondthehype.dev&utm_medium=referral&utm_campaign=inside-claude-code-prompt-engineering-masterpiece))
