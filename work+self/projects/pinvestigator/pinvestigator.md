# PINvestigator

LLM-powered metrics investigation tool for the Homefeed Relevance team.

## What It Does

Python Notebook launched during metric investigations. Built-in functions that:

1. **High-dimensional time-series analysis** — pulls all metrics (repins, closeups, etc.) with breakdowns (Discovery surface, fresh, shopping, etc.) and YoY/WoW/MoM patterns
2. **Metric similarity** — compares and finds closest metrics given a target metric of investigation
3. **Anomaly detection & visualization** — basic anomaly detection, cross-surface analysis
4. **Breakdowns** — by RTC, countries, platforms
5. **LLM digest** — digests all data points and suggests what to look for next
6. **Slack + internal systems integration** — checks relevant launch and/or incident timing
7. **Historical context** — loads past analyses, LLM digests all context and proposes next investigation steps

## Architecture: Thin Orchestrator + 3 Parallel Subagents

Built as a Claude Code skill (`agent-skills/pinvestigator/`).

```
SKILL.md (orchestrator, ~236 lines, auto-loaded)
  │
  ├── Phase 0:  Resolve TARGET_DATE + TARGET_METRIC
  ├── Phase 1:  Dispatch 3 subagents IN PARALLEL
  │   ├── Subagent A (engagement-analysis.md + data-tables.md) → 7 Presto tables
  │   ├── Subagent B (holdout-analysis.md + data-tables.md)    → 1 holdout table
  │   └── Subagent C (slack-search.md)                         → 4 Slack channels
  ├── Phase 1b: Validate subagent results (handle partial failures)
  ├── Phase 2:  Cross-correlate findings across A + B + C
  └── Phase 3:  Generate report (report-template.md)
```

## File Organization: 10 Files, 3 Categories

```
pinvestigator/
├── SKILL.md                    [AGENT PROMPT — auto-loaded]
├── ARCHITECTURE.md             [AGENT+HUMAN — read for dev context]
├── MCP_SETUP.md                [AGENT+HUMAN — read on MCP errors]
├── prompts/
│   ├── engagement-analysis.md  [AGENT PROMPT — Subagent A]
│   ├── holdout-analysis.md     [AGENT PROMPT — Subagent B]
│   └── slack-search.md         [AGENT PROMPT — Subagent C]
└── references/
    ├── data-tables.md          [AGENT REF — read by A and B]
    ├── principles.md           [HUMAN REF — not read at runtime]
    └── report-template.md      [AGENT REF — read in Phase 3]
```

Every file has an explicit role tag. At runtime, the agent reads only the files it needs for the current phase.

## Design Principles

1. **Minimal context loading** — SKILL.md (~236 lines) is the only file auto-loaded. Table schemas, SQL patterns, Slack channel lists load only when a subagent needs them. Each subagent loads ~290 lines total (its prompt + data-tables.md) vs. ~900 lines monolithic.

2. **Parallel subagents** — three independent data sources (engagement tables, holdout table, Slack) queried simultaneously. Wall-clock time drops from ~28 min sequential to ~20 min (bounded by engagement subagent). Orchestrator blocks until all three return.

3. **One subagent per data source** — clean ownership. Editing holdout-analysis.md can't regress engagement analysis. Each prompt testable in isolation. Failures contained (Slack MCP down → other two still produce valid results).

4. **Synthesis in orchestrator** — cross-correlation (holdout divergence + iOS isolation + Slack deploy on same date) requires all three outputs. Phase 2 runs after all subagents return. No subagent knows about the others.

5. **Shared reference files** — data-tables.md is single source of truth for table schemas, column names, valid values, query rules. Both Subagent A and B read it.

6. **Layered context loading** — developers modifying the skill read ARCHITECTURE.md. MCP errors trigger MCP_SETUP.md. Default context stays clean.

7. **Human reference files don't consume agent context** — principles.md (~400 lines, full examples) is for human investigators. Subagents use compact inline excerpts instead.

## Current Status (April 2026)

Last updated: 2026-04-11

### This week's milestones (week of 2026-04-07)

- **Eval harness landed.** 8 golden set examples generated (3 slow drift incidents + 5 cliff incidents). Evaluation harness built and code merged. Quality gate now exists — can A/B prompt/architecture changes against a fixed reference set instead of vibes.
- **Demoed to Jeff and his directs.** ~10-minute slot. Body language was strong — clear "moment of recognition" in the room. Jeff did not commit verbally to anything concrete (see Jeff demo dynamic below).
- **Dhruvil onboarded as a user.** Asked to play with the tool, James shared. Practitioner ally signal — Dhruvil is a peer Sr EM (Homefeed Ranking) and his hands-on engagement is a high-credibility internal endorsement.

### Jeff demo dynamic (and the Manu lane)

During the demo, **Manu (Sr Director, Data Science)** publicly interjected: "Your team should follow my team — we're building something similar." Jeff went silent — no commitment, no follow-up. Read of Jeff's silence (stress-tested against Wes Kao + Coaching Patterns notebooks):

- **Most likely cause:** time + Manu interjection. 10 minutes is below the threshold for an exec to switch context, absorb a tool, navigate a turf interjection, and commit publicly. Not a value miss.
- **Comparison trap to avoid:** Reading Jeff's silence as "demo lost steam" relative to Akaasha's earlier ralph-loop demo (which got more Jeff/Phil questions) is the *Status Sensor* firing. Akaasha's was research/exploration → invites curiosity. PINvestigator is a production tool → invites adoption decisions, not out-loud commitments. Different stage, not lower value.
- **Delivery lesson:** Did not preempt the **MOO (Most Obvious Objection)** — Manu's overlap. Wes Kao framework: when an adjacent team's work is in the room, address it head-on in the opening so you control the frame.
- **Load-bearing fact often under-weighted:** Dylan strongly supports PINvestigator. She brokers upward to Jeff. Asking Jeff for sign-off post-silence reads needy; asking Dylan for partnership reads strategic.

### Five committed next steps (2026-04-11)

1. **Send Dylan a written follow-up using OAV (Wes Kao framework).** Originally drafted for Jeff; swapped to Dylan to get her blessing and let her broker upward.
   - **Observe:** "Following up on yesterday's PINvestigator demo. Jeff's directs were engaged; Manu flagged that his team is exploring adjacent work."
   - **Assert:** "Proposing a 2-week pilot on the next 3 recsys incidents to capture hard metrics on time-to-resolution and engineering hours saved. In parallel, I'll sync with Kareem (Manu's team) offline to deconflict and find consolidation opportunities. JJ is going to drive the eval harness expansion; I'll own the stakeholder layer and adoption metrics."
   - **Validate:** "Want your blessing to proceed — and if the metrics land where I expect, your help framing this with Jeff for broader rollout. Sound right?"

2. **Drive adoption metrics — that's the only signal that matters now.** Success = runs + hours saved. Operationalize: lightweight telemetry on every PINvestigator invocation (timestamp, user, incident type, outcome). **Target: 20+ runs across 3+ teams in 2 weeks.** Weekly summary line for Dylan's 1:1 and Jeff's follow-up thread.

3. **Convert Manu's overlap into a Kareem partnership — not a competition.** Already in motion (James engaging Kareem). Accelerate it. Offer PINvestigator to Kareem's team as a co-pilot. The moment Manu's org is *using* the tool, the overlap dissolves and Jeff has nothing to referee. Related: Dylan shared a front-end DS tool from Manu's team for "integration possibilities." James's gut: not a front-end fit (PINvestigator is a Claude Code skill). Reframe back to Dylan as: "Not a front-end fit, but I see an analytics-agent integration path. I'll scope it with Kareem and JJ."

4. **Delegate features to JJ aggressively.** JJ contributing to PINvestigator while on PTO is the strongest possible signal he wants this. Hand him: eval harness expansion, new surface integrations, better harnessing strategies. **James keeps:** adoption + stakeholder layer (Manu, Kareem, Dhruvil, Dylan, Jeff follow-up). **Why partition:** JJ gets a clean promo artifact for end-of-June with James as visible sponsor; James gets velocity without building himself into a corner. If the work merges, JJ's promo case gets muddy.

5. **Stop benchmarking PINvestigator's reception against Akaasha's demo.** That comparison is the Roberto-line tournament re-asserting itself. Not a fair comp for James's Pinsight/PINvestigator track — Akaasha sits in the Kurchi-line dynamic, which is partly proxy for Dylan-vs-Kurchi director-level positioning. *Impact Over Approval audit:* James's scoreboard is **adoption volume**, not exec question count.

### Reflex Connection (updated 2026-04-11)

PINvestigator is the **"Detect" layer** of Andrew Yaroshevsky's Reflex vision (self-healing discovery stack). It surfaces metric anomalies; Pinsight (separate project) handles diagnosis.

Reflex has escalated significantly this week — Andrew built a working prototype and has committed to landing the code in git **before Tuesday 2026-04-14** for explicit co-development with James. PINvestigator's adoption story is now load-bearing for the broader Reflex narrative: every PINvestigator run is also a hypothesis source Reflex can consume. See `pinsight/pinsight.md` for the full Reflex × Anticipation Vision context.

### Ownership going forward

- **JJ:** primary code/feature owner. Eval harness expansion, new surfaces, harnessing strategies. Promo artifact for end-of-June.
- **James:** adoption + stakeholder layer. Manu, Kareem, Dhruvil, Dylan follow-up, Jeff follow-up via Dylan, telemetry/metrics narrative. Director-track signal: incubating a tool, sponsoring a contributor, and converting it into org-wide adoption.

---

## Interview Positioning (March 2026)

PINvestigator is James's hands-on agentic AI case study — he's acting as tech lead, building it himself with Claude Code. This is complementary to the UPP case study (Director-scale oversight):

- **UPP**: Shows James operates at Director scale (oversight, architecture, cross-org stakeholder management)
- **PINvestigator**: Shows James can go deep and build (hands-on, novel agentic architecture, eval-driven)

Key differentiators for interviews:
1. **Parallel subagent architecture** — most candidates can't talk about building agent systems from scratch
2. **Eval harness** (Q2 focus) — demonstrates the "hard part" of agent engineering that separates real systems from demos
3. **Three-level evaluation**: black-box (report quality), glass-box (trajectory), white-box (per-step)
4. **Failure handling as architecture** — one subagent per data source means failures are contained, partial results are useful
