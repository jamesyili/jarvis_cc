# Reflex Context Instructions (for work-leo)

> Paste the block below into a fresh work-leo conversation. work-leo has Pinterest code + internal doc access that main-Leo does not. The output is a `context.md` that Andrew Yaroshevsky's Reflex agent will load as grounding context for autonomous HF recsys hypothesis generation.

Last updated: 2026-04-15

---

## Background (for James — don't paste this part)

This is the artifact James promised Andrew during the 2026-04-09 escalation: *"point Claude Code at the HF CG codepaths + share the table of HF CG engagement rates so Reflex can join survey labels (relevance) with engagement results."*

Andrew's bias going forward: **engagement data over relevance signals.** The survey × engagement join is the specific unlock that lets Reflex reason about both axes together.

Output: `~/reflex-context/context.md` on the work laptop. James reviews before anything reaches Andrew.

---

## What We Know About Reflex (from PR #234422, reviewed 2026-04-15)

### Architecture

PR adds `services/reflex/` to Pinboard. 4,143 lines across 32 files — all markdown/JSON, no Python code. This is a prompt library + accumulated operational memory, not a deployable service.

```
services/reflex/
├── .mcp.json              Presto + experiments MCP via localhost:19193
├── CLAUDE.md              Top-level: Reflex vision + Anticipation context
├── detect/
│   ├── CLAUDE.md          Detect-specific instructions (154 lines)
│   ├── agents/
│   │   ├── pm_agent.md    Hypothesis generation (315 lines)
│   │   └── ds_agent.md    Opportunity enrichment (218 lines)
│   ├── playbooks/         18 playbooks across 4 categories
│   ├── schemas/
│   │   ├── hypothesis_card.md   Lightweight card template
│   │   └── opportunity_card.md  Detailed 10-section writing guide (139 lines)
│   ├── board_setup.md     Asana Kanban GIDs + API patterns (295 lines)
│   ├── quality_patterns.md Self-improving shared memory (341 lines, growing)
│   └── queries/README.md  SQL query patterns
└── docs/
    ├── reflex-vision-two-pager.md     Andrew's vision doc
    └── anticipation-p13n-vision-2026.md  P13N 2026+ vision (7 co-authors)
```

### How the Agents Work

- **PM Agent** runs 3 playbooks per cycle (rotating through 18). Generates hypothesis cards on the Asana Kanban board. Full library audit every 6th cycle — evaluates which playbooks produce signal, retires stale ones, drafts new ones.
- **DS Agent** takes each hypothesis and enriches it into a quantified opportunity card. The opportunity card schema is extremely detailed: 4-6 deep qualitative pin examples (each a mini root-cause investigation with user history traces, stale signal identification, system failure diagnosis), SSv2 bridging estimates, contradiction tests, experiment cross-references, inline charts, and VLM-verified pin images.
- Both agents share **quality_patterns.md** — accumulated learning from 13 cycles. Key patterns discovered: VLM verification (cycle 9), holdout status checks (cycle 4, from James's feedback on Following CG card), engagement-first framing, CG source decomposition, compound dimensional cuts.
- Agents upgrade weak existing cards before creating new ones. Upgrades often more valuable than new work.

### The 18 Playbooks

**Data-driven (10):**
1. `metric_anomaly.md` — scan for declining metrics
2. `relevance_gaps.md` — find pRelevance gaps
3. `market_cg_performance.md` — decompose market engagement decline by CG source
4. `engagement_decomposition.md` — decompose SSv2 actions, user engagement anomalies, session patterns
5. `explicit_signals.md` — analyze hides, reports, "see more/less", search refinements, unfollows
6. `ranking_feature_performance.md` — analyze ranking features, utility weights, pinnability calibration
7. `filter_bubble.md` — detect explore/exploit imbalances
8. `supply_gaps.md` — find content supply gaps
9. `follow_graph_health.md` — detect stale follows, boards, interests, taste signals
10. `retention_decomposition.md` — markets/segments with good relevance but poor retention

**Experiment-driven (3):**
11. `experiment_review.md` — mine recent experiment completions
12. `experiment_doubledown.md` — deep-read top experiments, trace idea sources, find expansion vectors
13. `surface_transfer.md` — find cross-surface transfer debt

**Qualitative/research (3):**
14. `internal_feedback.md` — scan Slack feedback channels
15. `external_feedback.md` — scan Reddit, App Store, social media
16. `research_frontier.md` — review RecSys/IR literature

**Strategic (2):**
17. `team_roadmap_gaps.md` — review team plans, PRDs, architecture docs for gaps
18. `codebase_analysis.md` — analyze source code for config issues, cross-validate hypotheses

### What Andrew Values Most (from 4/14 Slack thread with Dylan)

- The **self-improving loop** is what he's proudest of — not the playbooks themselves (he called those "bootstrapping"). The quality_patterns.md compounding across cycles is the real innovation.
- The **quality of the output cards** — "there is a new level of sick" — the opportunity cards with VLM verification, inline charts, deep qualitative analysis.
- **James's role is RLHF expert-in-loop.** Andrew explicitly told Dylan: "this is the RLHF thing that we need to be providing feedback as experts." Expert feedback on the CARDS (domain accuracy), not the agentic architecture.
- Andrew is **running Reflex agents on devapp** as of 4/14 evening — moving from manual Claude Code execution toward automation.

### What the DS Agent Needs That context.md Should Provide

Based on reading the opportunity_card.md schema, the DS Agent needs:
1. **CG source → codepath mapping** — to trace which CG served a pin and diagnose the system failure
2. **Engagement rate tables with join keys to survey data** — the core unlock for reasoning about relevance + engagement together
3. **User engagement history tables** — the DS Agent traces individual users' engagement timelines to build pin-level root-cause investigations
4. **Signal source tables** — what input signals (follows, boards, interests) drove a recommendation, and how to check staleness
5. **Known failure modes** — so the system doesn't rediscover things James already caught (Following CG holdout, INTEREST.prod deprecation, etc.)

### Operational Details

- **Execution:** Currently manual (open Claude Code in `services/reflex/detect/`, follow agent instructions). Moving to devapp.
- **MCP:** Presto and experiments via `localhost:19193` proxy. Same proxy pattern as Pinkerton.
- **Asana:** Hardcoded project/section/tag GIDs in board_setup.md. Board has columns: Hypotheses → Opportunities → Ready to Build.
- **Cost:** Untracked. Each cycle loads ~2000+ lines of prompt context before any queries.
- **Portability:** Local paths (`~/code/pinboard/`) and localhost MCP mean it only runs on Andrew's machine currently.

### James's Review Approach (decided 4/15)

- **PR review:** Stamp with appreciation + practical nits (portability, local paths, Anticipation doc location). Do NOT redesign the agentic architecture in the review.
- **Where heavy feedback goes:** On the Asana board. When Reflex generates a card about HF CG and gets domain details wrong — holdout status, retrieval architecture, deprecated CGs — that's James's superpower. That feedback compounds into quality_patterns.md permanently.
- **Written review:** `~/work-leo/andrew_reflex_pr_review.md` (two versions: objective + diplomatic)

---

## Prompt to paste into work-leo

```
Task: Produce a context.md document that Andrew Yaroshevsky's Reflex agent will
load as grounding context for autonomous HF recsys hypothesis generation.

This is the artifact I promised Andrew when co-dev starts — "point Claude Code
at the HF CG codepaths + share the engagement rate table so Reflex can join
survey labels with engagement." This document IS that artifact.

Audience:
  (a) The Reflex DS Agent at runtime — loads this when enriching hypothesis
      cards into opportunity cards. The DS Agent traces individual pin examples
      back to CG sources, user engagement history, and stale signals. It needs
      exact table names, join keys, and codepaths — not descriptions.
  (b) The Reflex PM Agent uses this for playbooks like codebase_analysis.md,
      engagement_decomposition.md, and market_cg_performance.md.
  (c) Andrew reviews before ingestion.

Output file: ~/reflex-context/context.md (create directory if needed)

Strict rules:
  - Tables > prose. Reflex is an agent, not a reader.
  - Every codepath reference must be a REAL file path. No hallucinations.
  - Every table reference must be a REAL warehouse location.
  - If you don't know something, mark it [GAP: need X] — do NOT invent.
  - No section longer than 40 lines.
  - No TODO/TBD text reaches Andrew. Fill or flag.

Context on how Reflex agents work (DO NOT include this in the output — this is
so you understand what the agents need):
  - PR #234422 landed the full Detect stage. Two agents (PM + DS) run against
    real Pinterest infrastructure via Presto MCP and experiments MCP.
  - The DS Agent's opportunity card schema requires: 4-6 deep qualitative pin
    examples, each a mini root-cause investigation. For each pin, it needs to:
    (a) identify the CG source (reason_to_choose), (b) trace the user's
    engagement history with that content type, (c) identify the stale signal
    that drove the rec, (d) diagnose which pipeline stage failed (retrieval vs.
    ranking vs. signal decay). This means the DS Agent needs exact table names
    for user engagement history, signal sources, and CG metadata.
  - The PM Agent's playbooks reference specific dimensions: CG source
    decomposition, user state (dormant/casual/core), market, feed position,
    SSv2 action type. The context.md should make these dimensions queryable.
  - quality_patterns.md (the agents' shared memory) already encodes: VLM
    verification, holdout status checks, engagement-first framing, compound
    dimensional cuts. Don't duplicate these — complement them with data access.

Required structure (follow exactly):

# Reflex Context: HF Candidate Generation
Version: v0.1 | Owner: James Li | Co-dev: Andrew Yaroshevsky
Last updated: [date]

## 1. HF CG Codepath Map
Table per active CG: name | CG ID (reason_to_choose) | one-line purpose |
retrieval architecture (Pixie P2P / Pixie P2B→Polaris / ANN-Embedding /
KV Store / Following) | codepath | input signals | output shape |
known failure modes | owner.
Pull from: HF CG codebase, cg_quota_analysis.md registry, recent design docs.
Include deprecated CGs with deprecation note (INTEREST.prod → Interest CLR,
Organic Coengagement → Pin CLR, Followed Interest → RTC 5).

## 2. Engagement Rate Table
- Table name + warehouse location
- Full schema: column | type | meaning | grain
- Join keys (specifically: what joins to survey labels AND to reason_to_choose)
- 3-5 canonical queries with SQL
- Caveats: sampling, staleness, missing segments
- Include user engagement history tables the DS Agent needs for tracing
  individual user timelines (saves, clicks, follows by user_id + timestamp)

## 3. Survey × Engagement Join (Reflex's core unlock)
- Specific table paths enabling relevance-label × engagement join
- The key table: corequantuxr.hf_relevance_survey_responses_2025 (the DS Agent
  already references this in the opportunity_card schema)
- Join path: survey response → reason_to_choose → CG source → engagement data
- Worked example: "for candidate X from CG Y, survey rating + engagement rate"
- Include the user signal tables: bi.pnr_signature_top_interests_flat_all_latest,
  follow/board tables, data.pins_d — the DS Agent uses these for deep qualitative
  pin investigations

## 4. Known Failure Mode Library (seed — don't let Reflex rediscover)
Critical: The DS Agent encodes reviewer corrections into quality_patterns.md so
the same mistake never recurs. Seed this library with known issues so the agents
don't waste cycles rediscovering them.
- Following CG (19): holdout-only, low volume ≠ small feature (caught cycle 4)
- INTEREST.prod: DEPRECATED, replaced by Interest CLR. Do not recommend
  improvements to INTEREST.prod.
- Organic Coengagement: DEPRECATED, replaced by Pin CLR.
- Followed Interest: DEPRECATED (RTC 5).
- UIC CLR (237) ANN cap: hardcoded at 200/actualConds — changing sizer alone
  does NOT increase retrieval. Sizer and ANN cap are decoupled.
- Pred UIC CLR (238): disabled by default, requires experiment params to enable.
- 14-condition cap: PIN(9) + UIC(5) share 14 slots in
  PIN_LATE_FUSION_CONDITIONS. PUIC steals from PIN via pcond_N.
- Non-English CTR gap (CJK 83%): 9.5B impressions scope, MoE I18N at 0%
- DS Agent CG signal decay: what happened, reframe after James+Dylan feedback
- [Any others from Pinkerton M0 logs, PINvestigator runs, postmortems]

## 5. RLHF Feedback Protocol (how James corrects Reflex)
- Where feedback lands: Asana task comments on the Kanban board. The owning
  agent picks up comments, investigates, rewrites the card, and encodes the
  lesson into quality_patterns.md as a permanent system pattern.
- James reviews cards in the Opportunities column. Feedback focuses on domain
  accuracy: CG holdout status, retrieval architecture, deprecated CGs, signal
  source accuracy, stale engagement data.
- Worked examples: cycle 4 Following CG holdout catch → permanent pattern;
  cycle 9 VLM verification gap → "Never claim pin content without VLM check"

## 6. Glossary (HF-specific)
Terms Reflex must use correctly: CG, pUIC, SSD, MoE, UPP, BMI, UIC, OmniSage,
RecGPT, I18N MoE, Retentive Recs, CLR, Pixie, Polaris, ANN, reason_to_choose,
SSv2, pRelevance, pinnability. One-line def + system location per term.

## 7. Boundaries & Constraints
- PII: never surface raw user IDs, raw queries, raw content in cards
- Cost caps: max $X per hypothesis card; sample size ceilings
- Scope: HF CG only until extended — do NOT hypothesize on ads, moderation,
  P2P ranking, or Search until flagged
- Do NOT recommend changes to the agentic architecture (playbooks, agent
  prompts, quality_patterns structure) — that's Andrew's domain

Process:
  1. Read Pinterest code + internal docs to fill each section
  2. Cross-reference cg_quota_analysis.md for CG registry data
  3. Flag gaps explicitly (do not paper over)
  4. Show me the draft before anything reaches Andrew
  5. Prefer terse: Reflex is loading this, not reading it

Quality gate before you hand it to me:
  - Every file path exists (verify)
  - Every table name resolves (verify)
  - Section lengths within budget
  - No invented field names anywhere
  - Failure mode library includes all known deprecated CGs and architecture
    constraints from cg_quota_analysis.md
```
