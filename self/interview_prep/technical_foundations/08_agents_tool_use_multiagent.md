# 08 — Agents, Tool Use & Multi-Agent Systems

> **Bridge:** This is where you're genuinely *ahead of the curve*, not catching up. Reflex is a **production multi-agent system** with adversarial verification, blast-radius control, eval-against-ground-truth, and an RLHF-style human-correction loop — the exact patterns frontier labs are still formalizing. Most EM candidates have *used* agents; you *architected* a multi-agent system that ships code. Lead with Reflex when agents come up.
> **Book:** Ch 24 (agentic benchmarks) is the main touchpoint; the agent-design content is mostly frontier-current, not in the book.

---

## 1. The core idea

An **agent** is an LLM in a loop with **tools, memory, and the ability to act and observe** — it doesn't just answer, it *takes actions, sees the results, and decides what to do next* until a goal is met. The leap from a chat model to an agent is the **loop + tools + state**:

```
   goal ──► [perceive context] ──► [plan] ──► [act: call a tool] ──► [observe result]
              ▲                                                          │
              └──────────────────────── repeat until done ◄─────────────┘
                          (memory / state persists across steps)
```

The senior framing: *"An agent trades reliability for autonomy. The whole engineering discipline is buying back the reliability — through tool design, verification, guardrails, and evaluation — without giving up the autonomy that made it useful."*

---

## 2. The fundamentals

### The building blocks
- **Tool use / function calling:** the model emits a structured call (name + args); the harness executes it and returns the result. Tools are how the agent touches the world (search, code, APIs, MCP servers). *Tool design is the highest-leverage agent work* — a well-scoped tool with good errors makes a mediocre model competent.
- **The reasoning-acting loop (ReAct):** interleave reasoning ("what do I know, what's next") with acting (tool calls) and observing. Plan-then-execute and reflexion (self-critique between attempts) are variants.
- **Memory / state:** the context window is working memory; durable state lives outside (files, a DB, a scratchpad). *What persists across steps and how it's structured is an architecture decision*, not a given.
- **Planning & decomposition:** break a goal into steps; for hard goals, a planner agent emits subtasks for executor agents.
- **Interoperability protocols (MCP / A2A):** **MCP (Model Context Protocol)** is the emerging standard for connecting an agent to tools and data sources; **A2A (Agent-to-Agent)** is the standard for agents calling *other* agents. Naming these signals currency — and you ship both: Reflex's agents reach Presto / Slack / Asana over **MCP**, and Pinkerton is architected as a callable agent behind an **A2A-style façade** (Pattern A — data-API via MCP, reasoning in the consumer).

### Workflows vs. agents, and the four design patterns (current vocabulary — use it)
**Anthropic's distinction:** *workflows* orchestrate LLMs + tools through **predefined code paths**; *agents* let the LLM **dynamically direct its own process and tool use**. Most production "agents" are actually workflows — and that is usually the *correct reliability call*, because predefined paths are auditable and bounded. The four canonical **agentic design patterns**: **Reflection** (self-critique/refine), **Tool Use**, **Planning** (decompose), **Multi-agent Collaboration** (specialized roles).

*Reflex maps onto this exactly, and the mapping is your strongest answer:* it sits on the **workflow end** (deterministic phase orchestration, human-dispatched) — Skeptic = **Reflection**, playbooks = **Tool Use**, PM = **Planning**, the PM/DS/Skeptic/Curator roster = **Multi-agent Collaboration**. That it's a *workflow*, not a free-running agent, is precisely why it's reliable enough to modify production code.

### Multi-agent orchestration
Decompose a problem into **specialized roles** with **handoffs** and — critically — **verification**:
- **Role specialization** (a generator, a critic, a router) beats one do-everything prompt when the subtasks need different context or different stakes.
- **Adversarial verification:** a separate critic/skeptic whose job is to *refute* the generator. This is the single most important reliability pattern — independent verification catches plausible-but-wrong outputs a single agent rubber-stamps.
- **Orchestration shape:** pipeline (each stage feeds the next), parallel fan-out (independent subtasks, then merge), or loop-until-converged.

### The hard parts (name these — they're the senior signal)
- **Compounding errors:** a 90%-reliable step run 10 times is ~35% reliable end-to-end. Autonomy multiplies error rates — the argument *for* verification and short loops.
- **Agent evaluation is unsolved and trajectory-based:** you must grade the *path*, not just the final answer (did it use the right tool, avoid the destructive action, stay in budget). Output-only eval misses the dangerous failures. (Ties to guide 06.)
- **Guardrails / blast radius:** an acting agent can do harm. Bound what it can touch (allowlists), cap the magnitude (diff caps, rate limits), and gate the risky actions (human-in-the-loop).
- **Reward hacking in long horizons** (guide 05): the longer the loop, the more room to satisfy the metric while missing the intent.

---

## 3. Your anchor: Reflex (a real multi-agent system) + Pinkerton + RR reasoning

### Reflex — the architecture, in interview terms
- **"Claude Code sessions *are* the agents."** No custom framework — each agent is a prompt; the repo is the database; **git is the audit trail.** That's a sophisticated minimalist design choice you can defend: *the substrate already does orchestration, persistence, and audit, so don't rebuild it.*
- **Specialized roles with verification:** **PM** (generate hypotheses) → **DS** (enrich, size, score) → **Skeptic** (adversarial gate: PASS/FAIL/NEEDS_HUMAN) → **Feedback Curator** (turn human corrections into permanent structured patterns). The **Skeptic is the adversarial verifier** pattern in production; it even **self-calibrates** off its own verdict log (guide 06).
- **Blast-radius control:** the Build agent can only write to an **allowlist** of paths with **diff caps** — explicit, signed-off blast radius. This is *the* answer to "how do you let an agent modify production safely."
- **Eval against ground truth:** the **BuildValidator evaluates generated edits against real merged PRs** — agent output graded against reality, not a proxy.
- **RLHF-style compounding loop:** every human comment becomes a permanent analytical-check / dead-end, so the system's quality floor rises monotonically — agents that *learn from operators* (guide 05).

### Pinkerton & the RR reasoning layer
- **Pinkerton as a federated, callable agent** (Pattern A — data-API via MCP, reasoning lives in the consumer): the architecture decision that an agent should be a *callable capability with a clean interface*, not a monolith that subsumes everything. Good "how do you compose agents across teams" answer.
- **RR's LLM/VLM reasoning layer:** the UIC becomes a **dynamic prompt** — the VLM ingests a cluster's pins, deduces intent ("building a deck"), and generates a next-best-action ("needs staining"). An agent reasoning over structured user state to produce a *future timeline*, not a lookalike. This is "agent grounded on a real user representation," which is exactly the grounding problem frontier agents struggle with.

---

## 4. The frontier-lab connection

- **Agents are *the* frontier** — Claude Code, OpenAI's agentic products, computer use. This is the most current possible topic, and your Reflex experience is a differentiated, concrete, ahead-of-curve story while most candidates have only toy demos.
- **The patterns transfer one-to-one:** adversarial verification, decomposition into roles, guardrails/blast-radius, trajectory eval, grounding on real state — these are exactly the open problems at Anthropic/OpenAI. You can speak them from having *built* them.
- **The training frontier — agentic RL (ties to guide 05):** agents are increasingly *trained*, not just prompted — RL over multi-step tool-use trajectories where the reward is whether the task *verifiably* succeeded (RLVR/GRPO applied to agents; "tool-integrated reasoning"). This is the bleeding edge at both labs. Know it's happening and anchor it to the verifiable-reward + GRPO story from guide 05 — most candidates treat agents as a pure prompting problem and miss that the frontier is *RL on agents*.
- **For an Integrity seat:** the multi-layer defense system *is* a multi-agent/multi-stage pipeline with a verifier and a feedback loop (guide 05 §6). Frame safety as orchestration: input classifier → mid-generation → post-response → human review → red-team loop, each a stage with its own reliability profile.

---

## 5. Interview-portable (90 seconds)

> *"An agent is an LLM in a loop with tools, memory, and the ability to act and observe — and the whole engineering problem is that autonomy trades away reliability, so you spend your effort buying the reliability back. The distinction I lead with is Anthropic's — workflows orchestrate the model through predefined paths, agents let the model direct itself — and most reliable production 'agents' are really workflows; that's a feature, not a limitation. I've built this in production: Reflex is a multi-agent workflow where the agents continuously find, build, and validate improvements to our discovery stack. The design choices are the interesting part. There's a dedicated adversarial verifier — a Skeptic agent whose only job is to refute the proposer — because independent verification is the highest-leverage reliability pattern; a 90%-reliable step compounds badly over a long loop. Acting agents are bounded by an allowlist and diff caps, so the blast radius is explicit and signed off. And generated output is evaluated against real merged PRs — graded against reality, not a proxy. The thing I'd flag as still genuinely hard is agent evaluation: you have to grade the trajectory, not just the final answer, because the dangerous failures are in the path — the wrong tool, the unbounded action — not the output."*

**Likely probes:**
- "Single agent vs multi-agent?" → decompose when subtasks need different context/stakes or independent verification; otherwise one agent is simpler.
- "How do you make agents reliable?" → tool design, adversarial verification, short loops, guardrails, trajectory eval.
- "How do you evaluate an agent?" → trajectory + outcome; did it use the right tools, stay in budget, avoid harmful actions; not output-only.
- "Let an agent modify production — safely?" → allowlist + magnitude caps + human gate on risky actions (Reflex Build).
- "Why do long agent runs fail?" → compounding error + reward hacking over horizon; mitigate with verification and decomposition.
- "How do you ground an agent?" → real structured state (your UIC-as-dynamic-prompt) + tools that return ground truth, not the model's guesses.
- "Workflow vs agent?" → workflow = predefined code paths orchestrating LLM + tools; agent = the LLM directs its own process. Most reliable production systems are workflows; reach for full autonomy only when the task space is too open to script. Reflex is workflow-end on purpose.
- "MCP vs A2A?" → MCP = the agent↔tools/data standard; A2A = the agent↔agent standard. Reflex reaches its data tools over MCP; Pinkerton is an A2A-style callable agent.

---

## 6. Self-test (out loud, from memory)

1. What turns a chat model into an agent? Name the three additions.
2. Why is adversarial verification the highest-leverage reliability pattern? Use the compounding-error math.
3. When do you go multi-agent vs single-agent?
4. Why is agent eval different from model eval? What does "trajectory eval" mean?
5. How does Reflex bound blast radius, and how would you generalize that to any acting agent?
6. Explain Reflex's roles (PM/DS/Skeptic/Curator) and which of the four canonical patterns (Reflection/Tool-Use/Planning/Multi-agent) each is.
7. Define workflows vs. agents (Anthropic's distinction) and place Reflex. What do MCP and A2A each standardize?
8. Frame a multi-layer safety system as a multi-agent/multi-stage pipeline.

*This is your ahead-of-curve story — own it cold. Anchors: `reflex/system_design/codebase-guide.md`, `pinkerton/`, `retentive_recs.md` §4.*
