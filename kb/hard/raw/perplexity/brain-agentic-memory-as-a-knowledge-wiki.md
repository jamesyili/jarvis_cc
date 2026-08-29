# Brain: Agentic Memory as a Knowledge Wiki (Perplexity)

**Source:** https://www.perplexity.ai/hub/blog/brain-agentic-memory-as-a-knowledge-wiki
**Ingested:** 2026-08-28
**Tags:** agent-memory, knowledge-wiki, self-improving-agents, llm-agents, product-launch

---

> **Ingest note (2026-08-28):** the first-party post is behind a Cloudflare challenge that blocked every fetch path from this network (direct curl, browser-header curl, WebFetch 403, r.jina.ai 401, Wayback 429). This article is a **reconstruction from three secondary reports** published 2026-06-19 — AI Weekly (aiweekly.co/alerts/perplexity-brain-adds-self-improving-work-memory-to-its-agent), FourWeekMBA (fourweekmba.com/perplexity-brain-self-improving-agent-memory/), Quantum Zeitgeist (quantumzeitgeist.com/perplexity-brain-teach-agents-work/). Replace with the verbatim post when it can be fetched. Treat every number below as first-party, announced at launch, with no independent benchmark.

## What it is

Brain is a self-improving memory system for **Perplexity Computer** (the agentic product). It draws a distinction the coverage keeps returning to: most agent memory is *user* memory — preferences, name, style. Brain is *work* memory — "Brain remembers what it did, and learns from it." It is a performance log, not a personalization store.

## Architecture (as reported)

1. **Context graph.** Every completed agent task is logged into a "context graph of the work Computer performs": actions, sessions, connectors used, sources validated (which sources proved useful), user corrections, and failed attempts. Described as "a living context graph that allows the AI to understand a user's world."
2. **Overnight synthesis.** At set intervals — "typically overnight" — a synthesis process reviews the accumulated context graph, extracts patterns, and "converts those logs into reusable lessons."
3. **LLM wiki.** The lessons are stored in an LLM wiki ("personal knowledge base"). Direct quote carried by AI Weekly: "Overnight, a synthesis process converts those logs into reusable lessons, stored in an LLM wiki that automatically loads into the agent sandbox on each new run."
4. **Runtime loading.** The updated wiki loads into the agent's execution environment at the start of each new run, so the agent can "apply past learnings to future tasks" and is positioned to "proactively identify opportunities and flag potential problems."

**Page-level detail (Kalinga.ai guide, kalinga.ai/perplexity-brain-ai-memory-guide/, paraphrasing the post):**
- The wiki is organized as **pages per entity** — "a project, a data source, a key contact, a workflow step." Pages "update incrementally after each session and during overnight synthesis passes," so there are two write cadences, not one.
- What's tracked: "projects, connectors, artifacts, people, and ideas." **Every entry in the context graph links back to the session, file, or connector result that produced it** — provenance is per-entry, not per-page.
- Synthesis pulls from four inputs: completed sessions, connector results, source-document changes, and **user corrections** — "explicit feedback that a result was wrong, a source was a dead end, or a different approach was needed." Corrections are encoded as lessons of the form *avoid this route in this context*.
- At task start Computer "loads the **relevant** pages and uses them as a starting map" — scoped retrieval, not a full wiki load.
- Worked example: support-ticket triage — "Brain remembers which source documents resolved past tickets, routing future tickets to the right resource with fewer intermediate steps."

Beyond that, none of the coverage describes page-level mechanics — how wiki pages are created, merged, versioned, or deprecated; how conflicts between sessions are resolved; how retrieval is scoped at run time; or how records are removed. Those are exactly the questions a curation design needs answered, and the post (as reported) does not answer them.

## Reported metrics

| Metric | Claim | Measured on |
|---|---|---|
| Answer correctness | **+25%** | tasks Computer has seen before (repeated tasks) |
| Recall | **+16%** | history-dependent workflows |
| Cost | **−13%** | tasks requiring historical context |

Quote via Quantum Zeitgeist: "Early measurement results show that Brain increases answer correctness by 25% on tasks Computer has seen before." AI Weekly's caveat: "first-party, announced at launch, with no independent benchmark validation published."

## Limitations noted in coverage

- **Batch latency.** Overnight synthesis means "errors from today's run don't feed back until tomorrow's synthesis cycle."
- **Governance silence.** Nothing on data ownership in Enterprise deployments or how a record is removed from the graph/wiki.
- **Repeated-task framing.** The headline number is on tasks the agent has already seen; nothing is reported on transfer to novel tasks.

## Availability

Research Preview for Perplexity Max and Enterprise Max subscribers, announced 2026-06-18 (coverage dated 2026-06-19). Max is $200/month.
