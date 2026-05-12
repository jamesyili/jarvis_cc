# Reflex Next Steps — Critical Codebase Observations + Iteration Plan

Owner: James Li | Last updated: 2026-04-18 | Based on: PR #236032 (`ayaroshevsky/reflex` branch, Cycle 66)

---

## 1. What Was Done This Session

Created two new agent files in `services/reflex/detect/agents/`:

1. **`feedback_curator.md`** — Custodian of `quality_patterns.md`. Shapes expert feedback into well-formed patterns, detects conflicts, flags decay. Human approves every write. Adapted from pre-code-read draft to match actual codebase conventions (organic pattern format, REST API curl for Asana, real GIDs).

2. **`skeptic.md`** — Adversarial pre-review gate between DS Agent and human expert. Runs 5 checks (pattern, context, evidence, internal consistency, novelty). PASS/FAIL/NEEDS-HUMAN verdict. 2-revision cap before human escalation. Adapted to reference actual Known Dead Ends table, real pattern names, and concrete column-name pitfalls from quality_patterns.md.

**Key adaptation decisions:**
- Used the EXISTING pattern format (prose with Discovered/Applied/Verdict) instead of the draft's P-### numbered schema. Introducing a new schema breaks convention continuity and would require migrating 1564 lines.
- Skeptic reads quality_patterns.md directly (no Curator retrieval API yet). The file is large but structured by section, so targeted reads work.
- All Asana operations use REST API curl (not MCP) per detect/CLAUDE.md convention.
- Conflict reports and proposals write to `quality/proposed/` directory (new).

---

## 2. Critical Codebase Observations

### 2a. quality_patterns.md is approaching a scalability wall

**Current state:** 1564 lines. Sections: Analytical Approaches (~30 patterns), Presentation Patterns (~10 patterns), Known Dead Ends (34 entries), Task Quality Ranking (47 Opportunities + 12 Hypotheses), Cycle Learnings (66 cycles of reflections).

**Problem:** Both PM and DS agents read the FULL file every cycle. At current growth rate (~20 lines/cycle from learnings alone), the file hits 3000+ lines within 70 more cycles. Context window pressure becomes real — agents already deal with ~2000+ lines of prompt context before adding quality_patterns.md.

**The Cycle Learnings section is the biggest growth driver.** It's append-only, one entry per agent run. Cycles 39-66 alone account for ~500 lines. Most of these are consumed once (the next cycle) and then become historical.

**Recommendation for Andrew:**
- Split Cycle Learnings into a separate `cycle_learnings.md` (archive). Agents read only the most recent 3 cycles + the compiled patterns.
- Or: Feedback Curator compacts learnings into patterns every 6 cycles (audit cadence), then truncates.
- Task Quality Ranking could also move to a separate file — it's a board state snapshot, not a permanent pattern.

### 2b. The 10-hypothesis pipeline bottleneck

**Current state:** 10 hypotheses sit in the queue, all analytically complete with experiment cross-refs and codebase evidence, all blocked on VLM pin stories and inline charts because Presto MCP has been unavailable for 4+ consecutive cycles.

**Why this matters for Skeptic:** The Skeptic will correctly FAIL every card that lacks VLM and charts. If Presto remains unavailable, the Skeptic creates a formal bottleneck that makes the existing informal one visible. This is arguably a feature — it enforces the quality bar — but it means the first Skeptic cycles will produce many FAILs until Presto comes back.

**Recommendation:** When Presto returns, prioritize bulk promotion of the top 3 hypotheses (HF L2 RL CORE: 3.6, P2P exploration: 3.7, AMB ceiling: 3.7). The Skeptic should run on these first as a validation exercise.

### 2c. detect/CLAUDE.md says "no separate review agent"

**Line 70:** "There is no separate review agent. Instead, both PM Agent and DS Agent self-improve through a shared learning loop."

This directly conflicts with the Skeptic and Feedback Curator additions. The CLAUDE.md needs updating before a PR to add:
- Skeptic as a gate between DS Agent and human review
- Feedback Curator as an async agent triggered by expert comments
- Updated handoff sequence diagram

**Recommendation:** Update `detect/CLAUDE.md` when opening the PR. The sentence should become something like: "Quality compounding happens through four mechanisms: (1) PM and DS agents self-improve via quality_patterns.md, (2) the Skeptic gates cards before human review, (3) the Feedback Curator shapes expert corrections into patterns, and (4) human experts provide RLHF feedback via Asana comments."

### 2d. Two retired playbooks still in the rotation

`external_feedback.md` and `research_frontier.md` are both marked RETIRED in `detect/CLAUDE.md` (lines 43-44) but still exist as files in `detect/playbooks/`. The PM Agent's rotation tracker should skip them (and does, based on the learnings). But the detect/CLAUDE.md listing creates confusion — a new agent reader would think there are 18 active playbooks when there are actually 16.

**Recommendation:** Either delete the retired files or add `## Status: Retired` headers to them. Update the "18 playbooks" count to "16 active + 2 retired."

### 2e. Asana MCP ban is not documented where the Skeptic/Curator will look

`board_setup.md` line 10-12 documents the ban: "Asana MCP server (mcp__asana__*) has persistent DNS failures — never use it." But the detect/CLAUDE.md mentions it only briefly (line 110). Both new agents reference `board_setup.md` for curl patterns, which is correct — but if Andrew restructures the file loading order, the ban could be missed.

**Recommendation:** Both new agent files already contain the warning. No action needed unless Andrew moves them.

### 2f. The Anticipation vision doc is 7 months old

`docs/anticipation-p13n-vision-2026.md` is dated Nov 17, 2025. It outlines 4 pillars with workstreams. The PM Agent ties every hypothesis to a specific workstream. But some workstreams may have shipped, been deprioritized, or pivoted in 5 months. The Feedback Curator's decay detection should eventually cover vision doc drift too — flagging when a pattern references a workstream that's no longer active.

### 2g. MCP proxy pattern (localhost:19193)

The `.mcp.json` in `services/reflex/` configures Presto and experiments via `localhost:19193`. This is the same proxy pattern as Pinsight (see MEMORY.md). The Known Dead Ends entry about "never use curl to localhost:19193" (returns 403) is critical — agents must use native MCP tool calls. Quality_patterns.md documents a 6-cycle self-reinforcing failure loop where agents saw "Presto blocked" in the patterns file and repeated the mistake.

---

## 3. Open Design Questions (for Andrew + Dylan)

These are from the design doc §5, now informed by code-read:

### Q1: Does Skeptic FAIL block human review?
**Current proposal:** Blocks for up to 2 DS revision rounds, then unblocks.
**Code-read insight:** Given the 10-hypothesis bottleneck (all blocked on Presto), adding a blocking Skeptic creates a formal two-layer gate. When both Presto and Skeptic are active, cards must pass both. This is correct behavior but means the first Skeptic cycles will surface the backlog problem.
**Recommendation:** Keep blocking. The quality bar is the right call. But document the 2-round cap prominently so it doesn't create an infinite loop.

### Q2: Where do Curator proposals live?
**Current proposal (design doc):** Separate staging file or proposed section.
**Adaptation:** `quality/proposed/` directory with individual markdown files. This avoids polluting quality_patterns.md with unreviewed content and gives humans clean files to review.

### Q3: Skeptic MCP access?
**Current proposal:** Rely on DS Agent's query traces (cheaper).
**Code-read insight:** Presto is frequently unavailable. Giving Skeptic its own MCP access would let it re-verify evidence independently, but doubles the MCP cost per card and doesn't help when Presto is down.
**Recommendation:** Start without. Add if evidence-check drift is observed.

### Q4: File placement — flat or subdir?
**Current proposal:** Flat under `agents/`.
**Code-read insight:** `agents/` now has 4 files (pm_agent.md, ds_agent.md, feedback_curator.md, skeptic.md). Still manageable. A `quality/` subdir makes sense if/when more quality-layer agents emerge (e.g., Attribution agent for Prove→Detect).
**Recommendation:** Keep flat for now. The `quality/proposed/` directory is the only new subdir needed.

### Q5: Pattern numbering migration (P-### IDs)?
**Not in the original design questions, but surfaced by code-read.** The design doc's pattern entry format uses P-### numbered IDs with `applies_when` predicates. The actual quality_patterns.md uses named prose sections.
**Recommendation:** Defer migration. The named format works. Numbering adds overhead and requires migrating 30+ existing patterns. If the Curator ever needs programmatic pattern retrieval, do it then.

---

## 4. Remaining TODO Before PR

### 4a. Must-do
- [ ] Update `services/reflex/detect/CLAUDE.md` to reference the two new agents and reconcile the "no separate review agent" statement
- [ ] Create `services/reflex/detect/quality/proposed/.gitkeep` (empty dir for Curator proposals)
- [ ] Dry-run Skeptic against 2-3 historical cards where James caught issues (Following CG cycle 4, INTEREST.prod deprecation, VLM gap cycle 9) — does it catch what James caught?
- [ ] Dry-run Curator against 2-3 past Asana expert feedback threads — does it produce well-formed proposals?

### 4b. Should-do
- [ ] Update `services/reflex/CLAUDE.md` top-level to mention the two new agents in the project structure
- [ ] Write a short README in `services/reflex/detect/agents/` explaining the four agents and the handoff sequence
- [ ] Add the Skeptic review step to the DS Agent's Phase 3 (before moving to Opportunities)

### 4c. Nice-to-have
- [ ] Propose the quality_patterns.md split (Cycle Learnings → separate file) to Andrew
- [ ] Update retired playbook files with `## Status: Retired` headers
- [ ] Add a "Skeptic Review" tag to Asana for cards that have passed/failed review

---

## 5. Handoff Sequence (updated from design doc §3)

```
PM Agent (playbook cycle) → hypothesis card
    ↓
DS Agent (enrichment) → opportunity card draft
    ↓
Skeptic → annotated card
    ├─ PASS → card moves to Opportunities, flagged for human review
    ├─ FAIL (≤ 2 revisions) → back to DS Agent with critique
    └─ NEEDS-HUMAN → card moves to Opportunities with low-confidence flag
    ↓
Human Expert → review, comment, approve / reject
    ↓
Feedback Curator (async)
    ├─ Shapes Asana comments into proposed patterns
    ├─ Detects conflicts with existing patterns
    └─ Proposes updates to quality_patterns.md
    ↓
Human merges approved proposals into quality_patterns.md
    ↓
(feeds back to Skeptic and PM/DS agents next cycle)
```

---

## 6. Success Criteria (from design doc, adjusted for current state)

- Skeptic catches ≥ 80% of cases where James would have flagged deprecated-CG, holdout, or unverified-VLM issues on historical cards (measure against cycles 1-13 archive + recent cycles)
- Curator produces well-formed proposals for 100% of James's Asana feedback in cycles 67+. Human merge rate ≥ 50% without major edits.
- Expert review time per card drops by ≥ 30% within 5 cycles of Skeptic activation
- Zero autonomous pattern retirements or modifications in quality_patterns.md
- Andrew's verdict: extends the compounding loop rather than complicating it

---

## 7. Codebase Deep Dive: quality_patterns.md Structure

The file (1564 lines) is the single most important artifact in the Reflex system. It's the institutional memory that compounds across cycles. Understanding its structure is essential for iteration.

### Section Map

| Section | Lines (approx) | Purpose | Growth rate |
|---------|-------|---------|-------------|
| Critical Directive | 1-5 | "Always generate new hypotheses" mandate | Static |
| Analytical Approaches | 6-235 | ~30 named patterns with Discovered/Applied/Verdict | Slow (~1 new pattern every 3-5 cycles) |
| Presentation Patterns | 243-302 | ~10 formatting/evidence requirements | Slow |
| Known Dead Ends | 305-334 | 34 entries of table/column/approach failures | Medium (~1-2 per Presto cycle) |
| Task Quality Ranking | 337-410 | 47 Opportunities + 12 Hypotheses with ★ ratings | Every DS cycle |
| Playbook Library Audits | 600-800 | 2 full-rotation audit tables + coverage gap analysis | Every 6th cycle |
| Cycle Learnings | 800-1564 | Per-agent-run reflections (66+ entries) | ~20 lines/cycle (BIGGEST driver) |
| Playbook Rotation Tracker | Bottom | Current rotation position, next playbooks | Every PM cycle |

### Key Analytical Patterns (the ones the Skeptic checks against)

**Mandatory (every card):**
1. **VLM verification** — query `galaxy_pin_features_iceberg.common_pin_vlm_image_description_v1` by `signature`. No exceptions. Discovered Cycle 9.
2. **Topline impact sizing** — bridge to SSv2 % at minimum, DAU/WAU/MAU when possible. Discovered Cycle 9.
3. **Contradiction testing** — design a disproving query, run it, report honestly. Discovered Cycle 2.
4. **Experiment/holdout status check** — before citing any CG engagement data. Discovered Cycle 4 (James's catch on Following CG).
5. **Cross-validate signal availability** — verify features via codebase before claiming absence. Discovered Cycle 54.

**High value (apply when applicable):**
6. **CG source decomposition** — slice by `reason_to_choose`. Discovered Cycle 2.
7. **User state decomposition** — check if uniform or concentrated. Discovered Cycle 2.
8. **Compound dimensional cuts** — cross two dimensions (e.g., CG × user_state). Discovered Cycle 2.
9. **Feed position analysis** — for any CG-related task. Discovered Cycle 2.
10. **Market × CG decomposition** — reframes "market problem" into "specific CG problem." Discovered Cycle 3.
11. **Three-layer architecture gap** — model vs evaluation vs serving. Discovered Cycle 18.
12. **Ranking-vs-utility architecture** — per-state belongs in utility, not ranking. Discovered Cycle 49 (Dylan Wang feedback).
13. **Fresh-vs-stale reversal check** — fresher signals worse for CORE users. Discovered Cycle 37.
14. **Signal lifecycle audit** — pipeline user_state gating vs serving user_state gating mismatch. Discovered Cycle 44.
15. **Experiment status re-verification** — re-check every 2-3 cycles. Features deploy silently. Discovered Cycle 31-32.

### Known Dead Ends (critical for Skeptic context checks)

**Table/column errors (most common agent mistakes):**
- `datestr` → correct: `date` (northstar) or `dt` (sessions/survey)
- `country` → case varies: lowercase in `bi.core_daily_search_feedview_stats`, UPPERCASE in `bi.core_daily_feedview_pin_stats`
- `reason_to_choose` → only in survey tables; `home_feed_reason_to_choose` in feedview tables
- `irrelevance_reason` → doesn't exist; use individual boolean columns (`interest_match`, `old_interest`, etc.)
- `num_closeups` → doesn't exist; use `num_pin_clicks`
- `corequantuxr.hf_relevance_survey_responses` (no suffix) → only through Nov 2025; use `_2025` suffix for current data
- `dt = '2025-04-14'` → table has 2026 data despite `_2025` name

**HTML/Asana errors:**
- `<br />` → rejected by Asana API (use `<hr />`)
- `<code>` → rejected by Asana API (use `<strong>`)
- `<table>` → rejected by REST API (only works via UI/MCP)
- Named HTML entities (`&rarr;`, `&middot;`) → double-escaped; use Unicode directly
- Cross-task `<img>` attachment references → 500 error; must be same task

**Approach errors:**
- Calling MCP via curl/bash → 403 (6-cycle self-reinforcing failure loop)
- Composite score on /10 scale → parsed as /5, causing rank errors
- VLM iceberg returns empty for low-volume CG pins
- Experiment search shows "Running" for shut-down experiments → always call `get_experiment_summary`

---

## 8. Codebase Deep Dive: Playbook Library

### Overview

18 playbooks (16 active + 2 retired), ~2200 total prompt lines across all files. Each playbook is a structured detection routine with query patterns, thresholds, and interpretation logic.

### Playbook Performance (from 2 full rotation audits)

**Tier 1 — Consistently high-yield:**

| Playbook | Conversion | Avg Quality | Key strength |
|----------|-----------|-------------|-------------|
| `relevance_gaps.md` | 6/6 (100%) | 4.7 | Most productive playbook. CG × market × surface grids. |
| `market_cg_performance.md` | 4/4 (100%) | 4.5 | Every market card promoted. Delta-vs-US framing. |
| `experiment_review.md` | 2/2 (100%) | 4.5 | Small count, high hit rate. Shipped experiment analysis. |
| `surface_transfer.md` | 2/2 (100%) | 4.9 | Three-layer gap discovery. Feature × surface matrix. |

**Tier 2 — Solid contributors:**

| Playbook | Notes |
|----------|-------|
| `metric_anomaly.md` | 3/3 promoted first rotation. Pyramid walkdown effective. |
| `ranking_feature_performance.md` | Metamodel binary split discovery. Three-layer analysis. |
| `filter_bubble.md` | Diversity processor blind spots. Code-level evidence. |
| `retention_decomposition.md` | Strongest first-cycle (Cycle 21). Resurrection 2.16%. |
| `engagement_decomposition.md` | SSv2 action decomposition. Casual users card. |
| `explicit_signals.md` | Cross-surface hide isolation. Signal utilization check. |

**Tier 3 — Cross-validators (not standalone generators):**

| Playbook | Notes |
|----------|-------|
| `codebase_analysis.md` | Highest value strengthening other cards, not standalone. |
| `follow_graph_health.md` | Findings fold into board staleness, notification cards. |
| `team_roadmap_gaps.md` | Needs internal docs MCP. Limited without it. |

**Tier 4 — Tool-dependent / Retired:**

| Playbook | Notes |
|----------|-------|
| `experiment_doubledown.md` | Needs Experiments MCP for metric results. |
| `supply_gaps.md` | Needs Presto for gap quantification. |
| `internal_feedback.md` | Needs Slack MCP. |
| `external_feedback.md` | RETIRED — no Reddit/App Store access. |
| `research_frontier.md` | RETIRED — no academic paper access. |

### Key Tables Referenced Across Playbooks

| Table | Used by | Key columns |
|-------|---------|-------------|
| `corequantuxr.hf_relevance_survey_responses_2025` | relevance_gaps, market_cg, explicit_signals, follow_graph | `reason_to_choose`, `user_state`, `user_country`, `relevance`, `interest_match`, `old_interest` (booleans) |
| `bi.core_daily_feedview_pin_stats` | metric_anomaly, engagement_decomp, follow_graph | `feedview_type`, `home_feed_reason_to_choose`, `user_state`, `country` (UPPERCASE) |
| `bi.core_daily_search_feedview_stats` | ranking_feature, relevance_gaps | `user_country` (lowercase), `image_signature` |
| `finops.northstar_user_ge_metrics` | retention_decomp, metric_anomaly | `date` (not `datestr`), no `user_state` column |
| `galaxy_pin_features_iceberg.common_pin_vlm_image_description_v1` | All DS Agent enrichment | `signature`, `epoch`, `common__pin__vlm_image_description_text_v1.string_data[1]` |
| `gcoanalytics.engagement_stats` | engagement_decomp | `pin_upload_method`, `acquisition_channel_l1`, `dt` |

### Placeholder Tables (need discovery via `mcp__presto__search_tables`)

Several playbooks reference tables as `[placeholder]`:
- `filter_bubble.md`: `[exploration_metrics_table]`, `[segments_table]`
- `metric_anomaly.md`: `[table]`, `[quality_score_table]`
- `supply_gaps.md`: query-level supply/demand tables not yet discovered

These placeholders mean these playbooks can't run without first discovering the actual table names via Presto table search.

### Hardcoded Thresholds Across Playbooks

| Playbook | Threshold | Value | Notes |
|----------|-----------|-------|-------|
| relevance_gaps | pRelevance danger zone | < 2.5 with > 10M searches (P1) | |
| relevance_gaps | Supply gap indicator | < 40% coverage (P2) | |
| market_cg_performance | CG delta actionable | > 5pp worse than US | |
| market_cg_performance | Sample minimum | ≥ 50 ratings per cell | |
| metric_anomaly | DAU/MAU decline | > 0.02 (P1) | |
| metric_anomaly | SSv2 flatline | < 0.1% growth 4+ weeks (P1) | |
| filter_bubble | Exploration rate low | < 5% (P1) | |
| filter_bubble | Interest/SSv2 conversion | +2.1% SSv2 per additional interest | From Anticipation doc |
| retention_decomp | Churn crisis | > 25% monthly (P1) | |
| retention_decomp | US baseline churn | ~18% | Historical benchmark |
| explicit_signals | CG net-negative | hide-to-save ratio > 1 | |
| supply_gaps | Critical supply gap | < 30% AND > 50M searches (P1) | |

### Total Prompt Budget

The full agent context for a single cycle includes:

| Component | Lines | Loaded by |
|-----------|-------|-----------|
| Agent prompt (PM or DS) | ~330 | Always |
| detect/CLAUDE.md | ~154 | Always |
| quality_patterns.md | ~1564 | Always |
| board_setup.md | ~320 | Always |
| schemas/opportunity_card.md | ~140 | DS Agent |
| schemas/hypothesis_card.md | ~60 | PM Agent |
| 3 playbook files per cycle | ~100-240 each | PM Agent |
| **Total per PM cycle** | **~2700-3100** | |
| **Total per DS cycle** | **~2500** | |

Adding Skeptic (~350 lines) and Curator (~250 lines) to the load order increases the per-card cost but they run less frequently than PM/DS.

---

## 9. Codebase Deep Dive: Board State (Cycle 66)

### Current Board Composition

**Opportunities (47 cards):**

| Tier | Composite | Count | Top cards |
|------|-----------|-------|-----------|
| Tier 1 (★★★★★, 4.7-5.0) | 4.7-5.0 | 12 | Per-state utility, Shopping CGs, European dormant, Search intl, Casual users, Resurrection-to-habit |
| Tier 2 (★★★★½, 4.3-4.6) | 4.3-4.6 | 8 | Relevance survey, Homefeed diversity, Notification CRP, LATAM, MAU proxy |
| Tier 3 (★★★★, 3.7-4.2) | 3.7-4.2 | 15 | Resurrected CG mix, Product pin CG, GB market, RecGPT transfer, GenAI measurement, Board staleness |
| Tier 4 (★★★-★★★½, 2.5-3.6) | 2.5-3.6 | 12 | BMI landing, RP quality void, OFFSITE_INTEREST, Content quality slop |

**Hypotheses (12 cards, all blocked on Presto for promotion):**
- HF L2 RL CORE reward downweight (4.0)
- P2P/HF exploration per-state gap (3.8/4.0)
- AMB tab content quality ceiling (3.7)
- Visual Tabs traffic redistribution (4.4 — highest-composite hypothesis)
- PinnerSpark CORE quality reversal (3.5)
- Search pre-blending calibration (3.4 — monitor-only)
- Others at 2.4-3.5

**ARCHIVED cards:** 12 cards merged or retired (FOLLOWING_FEED, Pin selection, Ads time decay, GenAI signals duplicates, etc.)

### Surface Coverage

| Surface | Opportunity count | Notes |
|---------|------------------|-------|
| Homefeed | 25+ | Dominant. CG decomposition, per-state, diversity, staleness |
| Search | 5 | Intl relevance, per-state ranking, pre-blending |
| Notifications | 4 | CRP expansion, journey-aware, Pin Ranker, HFDP |
| Related Pins | 3 | RP fresh, RP quality void, per-state (from surface_transfer) |
| Landing Pages | 3 | BMI, AMB ceiling, Visual Tabs |

### Anticipation Workstream Coverage (cumulative, 2 rotations)

| Pillar | Covered | Gap |
|--------|---------|-----|
| 1.1 Downstream Rewards | Yes (3 cards) | |
| 1.2 Explore/Exploit | Yes (2 cards) | |
| 1.3 Responsiveness | Yes (2 cards) | |
| 1.4 Board Recs | Partial (1 card) | Needs dedicated intelligent boards card |
| 2.1 Ground Truth | Yes (1 promoted) | |
| 2.2 Optimize | Yes (5+ cards) | |
| 2.3 Reduce Low-Relevant | Yes (3 cards) | |
| 2.4 Low-Signal Users | Yes (2 cards) | |
| 2.5 Signals | Partial (2 cards) | |
| 3.0-3.3 Measurements | Partial | 3.2 pRelevance proxy weakest |
| 4.1 UPP | Yes (1 card) | |
| 4.2 GULP | Partial | GULP experiment bypass documented but no dedicated card |

---

## 10. Codebase Deep Dive: Operational Patterns

### The 6-Cycle MCP Failure Loop (Cycles 15-20)

The most instructive operational failure in Reflex's history:
1. An agent called Presto via `curl` to `localhost:19193` → got 403 (curl lacks MCP client auth)
2. Agent wrote "Presto blocked" to quality_patterns.md
3. Next agent read "Presto blocked" from quality_patterns.md → didn't even try native MCP calls
4. Pattern repeated for 6 cycles, each cycle reinforcing the "blocked" belief
5. Fixed in Cycle 20-21: native `mcp__presto__*` tool calls work fine

**Lesson for new agents:** quality_patterns.md is authoritative for domain patterns but CAN propagate operational misconceptions. The Skeptic and Curator should never write operational status ("tool X is blocked") into quality_patterns.md — only domain patterns.

### Presto Query Conventions

From `board_setup.md` and quality_patterns.md:
- Always use native MCP tool calls, never curl
- Presto on `presto-adhoc-003-graviton`
- For multi-partition queries: `SET SESSION pinterest_query_category='expensive'`
- Survey table: `corequantuxr.hf_relevance_survey_responses_2025` (has 2026 data despite name)
- Always check latest partition: `SELECT dt FROM ... ORDER BY dt DESC LIMIT 1`
- VLM table: query by `signature` with latest `epoch`

### Asana HTML Gotchas (from board_setup.md + Known Dead Ends)

The Asana REST API has XML validation that silently rejects invalid HTML:
- **Reliable pattern:** Create task first (name + project only), then update html_notes separately
- **Banned elements:** `<br />`, `<code>`, `<table>` (via REST API), `<p>` (unnecessary)
- **Banned entities:** All named entities except `&amp;`, `&lt;`, `&gt;`, `&quot;` → use Unicode
- **Cover image:** Last uploaded attachment becomes cover. Upload key chart LAST.
- **Cross-task img refs:** 500 error. Attachment must belong to same task.

### Rotation Tracker State (as of Cycle 66)

- Currently in **Rotation 9/10** (positions vary; Rotation 9 completed through position 15 of 16)
- Next playbooks in queue depend on which positions are next in the tracker
- `codebase_analysis` (position 16) was deferred as overused
- 2 retired playbooks (`external_feedback`, `research_frontier`) are skipped in rotation
- Full rotation = 16 active playbooks × 3 per cycle = ~5.3 cycles per rotation

---

## 11. Architectural Observations for Future Iterations

### 11a. The quality_patterns.md split is the highest-leverage structural change

Splitting quality_patterns.md into:
1. **`quality_patterns.md`** — Analytical Approaches + Presentation Patterns + Known Dead Ends (~340 lines, stable)
2. **`board_state.md`** — Task Quality Ranking (~100 lines, every cycle)
3. **`cycle_learnings.md`** — Archive of per-cycle reflections (~800 lines, append-only, agents read last 3 only)
4. **`playbook_audits.md`** — Full rotation audit tables (~200 lines, every 6th cycle)

This reduces the per-cycle context load from ~1564 to ~440 lines (patterns + last 3 learnings) — a 72% reduction.

### 11b. The Skeptic's primary value is catching Known Dead Ends

Based on the 34 Known Dead Ends entries, the most common agent mistakes are:
1. Wrong table/column names (12 entries)
2. Banned HTML elements (5 entries)
3. MCP usage errors (2 entries, but caused 6 cycles of damage)
4. Stale experiment status (3 entries)
5. Scale/scoring errors (2 entries)

The Skeptic's context check (§2 in its prompt) maps directly to these. If it catches even 50% of table/column errors before cards reach human review, it saves significant expert cycles.

### 11c. Playbook placeholder tables need a discovery pass

`filter_bubble.md`, `metric_anomaly.md`, and `supply_gaps.md` all have `[placeholder]` table references. These playbooks can't run their prescribed queries until someone does a `mcp__presto__search_tables` discovery pass and fills in the actual table names. This is a one-time investment that would unblock 3 playbooks.

### 11d. The "infrastructure hypothesis" quality bar debate

quality_patterns.md Cycle 19 raised a genuine design question: should infrastructure/measurement hypotheses (Relevance survey contamination, Content quality slop signals) require VLM pin stories? These cards are about measurement pipelines, not pin-level content. Cycle 20 DS Agent resolved this pragmatically — codebase evidence suffices for architectural cards — but the policy isn't formalized. The Skeptic currently treats VLM as mandatory for all cards. If James and Andrew agree that infrastructure cards have a different quality bar, the Skeptic's evidence check needs a card-type conditional.

### 11e. Cost tracking doesn't exist

`detect/CLAUDE.md` line 102: "Cost: Untracked." The total prompt budget per cycle is ~2700-3100 lines for PM Agent, ~2500 for DS Agent, plus whatever Presto queries and experiments MCP calls cost. As agents scale (4 agents now, potentially more), cost per cycle becomes a real concern. Neither Andrew nor the system tracks API cost.

### 11f. Portability is still local-only

`detect/CLAUDE.md` references `~/code/pinboard/` for codebase analysis. The `.mcp.json` uses `localhost:19193`. Both are Andrew's machine. Running Reflex on devapp (mentioned in the context instructions) requires resolving these local paths and the MCP proxy. The new agents (Skeptic, Curator) inherit this constraint — they reference `../quality_patterns.md` and `../board_setup.md` relative to the detect/ directory.
