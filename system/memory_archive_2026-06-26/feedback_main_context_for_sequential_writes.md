---
name: Main context for sequential edit-between-step writes
description: Don't delegate work that requires Edit-after-each-step persistence to spawned agents — they don't reliably commit Edit calls to disk between steps. Use main context.
type: feedback
originSessionId: d6312f4c-5043-42ed-a478-1283dd16250f
---
When work involves sequential queries + edits where each step's output must be persisted before the next step (e.g., 15 NotebookLM queries with file edits between each), prefer main-context execution over agent dispatch — even when the agent has Edit tools and explicit instructions to save after each write.

**Why:** Observed failure 2026-04-25f. Spawned a consult-notebook agent with explicit instruction to (1) query NotebookLM, (2) Edit file with response, (3) move to next query. Agent reached Q7 internally but had not actually persisted any of Q1-Q7 to disk by the time it was killed. Result: 7 responses lost. The agent appears to hold Edit calls in memory and flush less frequently than expected, OR there's some other persistence-gap in the agent runtime that causes mid-flow Edits not to land. Same agent works fine for read-only research where output returns at the end as a single message.

**How to apply:**
- For 1–4 sequential write operations: agent dispatch is fine.
- For 5+ sequential writes that must each persist before next step (e.g., long-form fill-ins, structured iterations through a file): main-context execution. Cost is polluted context (~10-20K tokens for 15 verbose responses), but persistence is guaranteed.
- Especially applies to consult-notebook and Explore agents.
- Counterexample: bulk read-only research with single end-of-task output → still fine for agents.
- Failsafe: if dispatching such work to an agent is unavoidable, instruct the agent to verify file contents on disk after each edit (Read tool) before moving to next step — but this is heavy and slow; prefer main-context.
