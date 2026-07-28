# Org Planner Tool — build context for work-leo (2026-07-27)

**Purpose:** deliverable 3 of the 7/27 session — self-contained context for building an **interactive HTML org-planning tool** with work-leo. James drags people between teams; the tool shows live level distributions, seniority balance, MLE/SWE mix, and constraint warnings relevant to the July/August 2026 reorg. James will supply additional fields (geographic location, etc.) on the work side.

**Sensitivity:** work-confidential. Includes performance-process facts (marked `sensitive`) because they are real placement constraints. The tool must default to hiding sensitive annotations (screen-share safety) with an explicit toggle to reveal.

---

## 1. What the tool is for

James (Sr EM, M17) runs a 3-team org forming via a July/August 2026 reorg: his existing team, an inherited EM (Daniel Liu + 7 ICs), and a new EM (Alim Virani, started 7/27) whose pod is drawn from James's current reports. The org design has a locked **initial state** (minimal moves, announced Aug 5) and a **target state** that resolves through settle-point gates (~60 days). The open design work is *which people land where at settle* — and that's what the tool supports: scenario play with instant feedback on the shape each move produces.

**Org name (locked):** Personalization Retrieval and Anticipation. **Teams (locked):** Retrieval Foundations (James, direct pod) · Retrieval Modeling (Daniel) · Anticipation Modeling (Alim).

## 2. Roster data (authoritative as of 2026-07-27)

Drop-in JSON. `reports_to_current` = line before any reorg move; `initial` = day-1 assignment around the Aug 5 announcement; `target` = settle-state lean per the org doc (null = genuinely open). `family`: MLE/SWE. Levels L13–L16 (IC), M16–M17 (EM).

```json
{
  "meta": {
    "as_of": "2026-07-27",
    "org_name": "Personalization Retrieval and Anticipation",
    "teams": ["Retrieval Foundations (James)", "Retrieval Modeling (Daniel)", "Anticipation Modeling (Alim)"],
    "level_order": ["L13", "L14", "L15", "L16", "M16", "M17"]
  },
  "ems": [
    {"name": "James Li", "level": "M17", "family": "MLE", "role": "Org lead + Retrieval Foundations"},
    {"name": "Daniel Liu", "level": "M16", "family": "MLE", "role": "EM Retrieval Modeling", "notes": "Inherited via Dylan's reorg; team intact day 1"},
    {"name": "Alim Virani", "level": "M16", "family": "MLE", "role": "EM Anticipation Modeling", "notes": "Started 2026-07-27; pod drawn from James's reports"}
  ],
  "ics": [
    {"name": "Piyush Maheshwari", "level": "L16", "family": "MLE", "workstreams": ["UPP"], "reports_to_current": "James", "initial": "James", "target": "James", "notes": "UPP anchor; single point of failure (hedge: Zihao); standing direct"},
    {"name": "Bella Huang", "level": "L16", "family": "MLE", "workstreams": ["RecGPT", "Reflex"], "reports_to_current": "James", "initial": "James", "target": null, "sensitive": "Active perf-doc path (no PIP per Dylan); H1 doc with dated deliverables", "notes": "Staff anchor GenRet incubation; DECLINED moving under Alim — GenRet graduation destination unresolved"},
    {"name": "Balaji Rengarajan", "level": "L16", "family": "MLE", "workstreams": ["Intelligent Boards"], "reports_to_current": "Daniel", "initial": "Daniel", "target": null, "notes": "FORK (Dylan decision): platform TL under Daniel vs Staff anchor under Alim — the fix for Alim's no-senior pod"},
    {"name": "Devin Kreuzer", "level": "L15", "family": "MLE", "workstreams": ["CLR", "GULP"], "reports_to_current": "James", "initial": "James", "target": "with CLR → Alim at settle (TBC)", "notes": "CLR lead"},
    {"name": "Ryan Kam", "level": "L15", "family": "SWE", "workstreams": ["CLR", "LWS"], "reports_to_current": "James", "initial": "James", "target": null, "notes": "Joined ~May 2026; dev-velocity focus"},
    {"name": "J.J. Hu", "level": "L15", "family": "MLE", "workstreams": ["Reflex", "Foundations & Efficiency"], "reports_to_current": "James", "initial": "James", "target": "James", "notes": "~half Reflex Build / ~half F&E; IC16 package submitted; returns mid-Aug"},
    {"name": "Yali Bian", "level": "L15", "family": "MLE", "workstreams": ["LWS"], "reports_to_current": "James", "initial": "James", "target": "Daniel (with LWS)", "notes": "De facto LWS owner; SM/SL retrieval POC (announced 7/25)"},
    {"name": "Hedi Xia", "level": "L15", "family": "MLE", "workstreams": ["LWS"], "reports_to_current": "James", "initial": "James", "target": "Daniel (with LWS)"},
    {"name": "Yuke Yan", "level": "L15", "family": "MLE", "workstreams": ["RecGPT"], "reports_to_current": "James", "initial": "James", "target": "James through perf resolution", "sensitive": "Dated-deliverables expectations doc; end-Sept checkpoint; PIP starts Oct if missed", "notes": "Single RecGPT stream only; must NOT move to a new EM while process open"},
    {"name": "Zihao Chen", "level": "L15", "family": "MLE", "workstreams": ["UPP", "Content Exploration"], "reports_to_current": "James", "initial": "James", "target": "James", "notes": "UPP cross-surface training lead; Piyush succession hedge — moving him to Alim points him away from UPP"},
    {"name": "Roderick Gao", "level": "L15", "family": "SWE", "workstreams": ["Unified Explore Backend"], "reports_to_current": "Daniel", "initial": "Daniel", "target": "Alim (UEB consolidates at settle)", "notes": "High performer; drives UEB; Lionel's backend partnership option"},
    {"name": "Yang Liu", "level": "L15", "family": "MLE", "workstreams": [], "reports_to_current": "Daniel", "initial": "Daniel", "target": "Alim-lean at settle (anticipation history)", "notes": "PARENTAL LEAVE — return date/ramp open; pre-leave UIC work"},
    {"name": "Kim Toy", "level": "L15", "family": "MLE", "workstreams": ["UPP foundational (loaned to Dhruvil)", "CLR"], "reports_to_current": "Daniel", "initial": "Daniel", "target": null, "notes": "LOANED to Dhruvil's team — capacity ≠ headcount until wind-down (open Dylan ask)"},
    {"name": "Yongwoo Noh", "level": "L15", "family": "MLE", "workstreams": ["unknown"], "reports_to_current": "Daniel", "initial": "Daniel", "target": null, "notes": "Workstream map pending first substantive Daniel conversation"},
    {"name": "REQ-1 (open)", "level": "L15", "family": "MLE", "workstreams": [], "reports_to_current": "James", "initial": "unallocated", "target": null, "notes": "Open req; deliberately unallocated until settle gates resolve; closes Alim's '2 seniors' — do not upgrade to L16"},
    {"name": "Rui Wang", "level": "L14", "family": "SWE", "workstreams": ["Reflex", "L1/Real-Time"], "reports_to_current": "James", "initial": "James", "target": "James", "notes": "L1/RT operational owner under F&E; joined ~late June 2026"},
    {"name": "Alok Malik", "level": "L14", "family": "MLE", "workstreams": ["Retentive Recs (primary)", "Reflex"], "reports_to_current": "James", "initial": "Alim", "target": null, "notes": "In Alim's locked day-1 pod, but reporting line flagged unresolved: RR = Alim's charter, Reflex = James's. Load-bearing for RR pod"},
    {"name": "Zili Li", "level": "L14", "family": "MLE", "workstreams": ["LWS"], "reports_to_current": "James", "initial": "James", "target": null, "sensitive": "Formal PIP initiated 2026-07-22 (ER engaged); James retains perf mgmt regardless of charter moves", "notes": "Zili-PIP × LWS→Daniel sequencing decision OPEN"},
    {"name": "Hanlin Lu", "level": "L14", "family": "MLE", "workstreams": ["RecGPT"], "reports_to_current": "James", "initial": "James", "target": null, "notes": "GenRet delivery pair with Bella; follows GenRet graduation"},
    {"name": "Chuxi Wang", "level": "L14", "family": "MLE", "workstreams": ["Retentive Recs"], "reports_to_current": "James", "initial": "Alim", "target": "Alim", "notes": "TL ramp (supported, unannounced); runs both pUIC syncs; James = skip-level sponsor"},
    {"name": "Lionel Bewa", "level": "L14", "family": "SWE", "workstreams": ["RR serving"], "reports_to_current": "Alim", "initial": "Alim", "target": "Alim", "notes": "STARTED 7/27 (same day as Alim) — founding member; Toronto (remote); Charlie backfill; 30/60/90 James skip checks"},
    {"name": "Ling Lan", "level": "L14", "family": "MLE", "workstreams": ["Retentive Recs", "Intelligent Boards"], "reports_to_current": "Daniel", "initial": "Daniel", "target": "Alim-lean at settle (RR shed)", "notes": "Built LLM-pUIC inferencing pipeline; Chuxi's daily delivery partner; straddles Daniel's IB"},
    {"name": "Felix Yang", "level": "L14", "family": "SWE", "workstreams": ["unknown"], "reports_to_current": "Daniel", "initial": "Daniel", "target": null, "notes": "Workstream map pending first substantive Daniel conversation"},
    {"name": "Yichi Wang", "level": "L13", "family": "MLE", "workstreams": ["CLR"], "reports_to_current": "James", "initial": "James", "target": "with CLR → Alim at settle (TBC)"},
    {"name": "Yidi Wang", "level": "L13", "family": "MLE", "workstreams": ["Retentive Recs"], "reports_to_current": "James", "initial": "Alim", "target": "Alim", "notes": "Carries most of model-based pUIC"},
    {"name": "REQ-2 (open)", "level": "L13", "family": "MLE", "workstreams": [], "reports_to_current": "James", "initial": "unallocated", "target": null, "notes": "Open req; deliberately unallocated"}
  ],
  "excluded": [
    {"name": "Rita Lyu", "role": "Intern (Daniel's team)", "why": "~2 months left — ignore for org design; conversion question is separate"},
    {"name": "Daniel Dormer", "role": "Contractor", "why": "Not headcount; committed to Reflex + later oncall-alert-AI project"}
  ]
}
```

**Cross-check totals:** 26 ICs incl. 2 open reqs — L16 ×3 (12%) · L15 ×12 (46%) · L14 ×8 (31%) · L13 ×3 (12%). MLE 20 / SWE 6 (incl. reqs as MLE per plan).

## 3. Constraints to encode (warning rules, non-blocking)

Fire an inline warning (with the reason text) when a drag violates one; never hard-block — James overrides deliberately.

1. **Yuke → anyone but James** while perf process open (end-Sept checkpoint): "Open perf process — no incoming EM inherits it."
2. **Zili's team changes:** "PIP stays with James regardless of charter move — sequencing decision open (LWS→Daniel)."
3. **Bella → Alim:** "Declined this move; GenRet graduation destination unresolved."
4. **Zihao → Alim (or off UPP):** "UPP succession hedge — moving him un-hedges Piyush SPOF."
5. **Any pod with 0 seniors:** highlight pods with no L15+ (Alim's day-1 pod is deliberately in this state; Balaji fork or REQ-1 is the fix — show it, don't hide it).
6. **Oncall coverage:** each of {LWS, boards, L1/Real-Time, pUIC serving} must have an owning team in every scenario; warn if the owning workstream's people all leave a team. Zili carve-out: his pager can move; his perf case cannot.
7. **Daniel-fairness counter:** show "moved away from Daniel since day 1: N" — carving many of his people to Alim early is explicitly flagged as bad optics in the design docs.
8. **Kim capacity:** render as 0.2–0.5 effective capacity until loan wind-down (field editable).
9. **Yang:** parental leave — count headcount, exclude from capacity until return date set.
10. **Reqs:** unallocated by design; placing them is a scenario choice, tag it visibly ("REQ allocated — flexibility spent").
11. **Alok dual-line:** wherever he lands, badge "RR (Alim charter) + Reflex (James charter) — line unresolved."

## 4. Tool features (spec)

- **Layout:** four columns — Retrieval Foundations (James) / Anticipation Modeling (Alim) / Retrieval Modeling (Daniel) / Unallocated. Person cards drag between columns. Card face: name, level chip, family chip, workstream tags, badges (leave/loan/remote/req; sensitive badge only in sensitive mode).
- **Presets (buttons):** `Current` (reports_to_current) · `Initial / Day 1` (initial) · `Target lean` (target where non-null, else initial). Loading a preset never destroys the working scenario without confirm.
- **Live stats per column:** headcount; level histogram (L13→L16); MLE/SWE split; L15+ count ("senior anchors"); effective capacity (after leave/loan adjustments); warning count.
- **Org-wide bar:** side-by-side level distribution per team + % shape vs. the whole org.
- **Diff view:** vs. any preset — moved people highlighted, "N moves from Current, M from Initial."
- **Scenario management:** save/load named scenarios (localStorage) + JSON export/import (so scenarios round-trip between work-leo and personal-leo).
- **Sensitive mode:** OFF by default — hides `sensitive` fields and badges entirely (screen-share safe). Toggle reveals them with a visual reminder (border tint) that sensitive info is showing.
- **Extra fields:** schema is open — work-leo adds `location`, `timezone`, and anything else to person objects; unknown keys render as card chips + become filter facets automatically.
- **Implementation constraints:** single self-contained HTML file, no external network deps (inline CSS/JS), works from `file://`. No frameworks needed; vanilla JS is fine at this scale (29 cards).

## 5. Settle gates the scenarios should model (context, not code)

- **CLR → Alim at settle** (gate: both EMs landed) — moves Devin/Yichi (± Ryan).
- **GenRet graduates to Alim at settle** (gate: incubation criteria) — Hanlin follows; Bella unresolved (see constraint 3).
- **IB gains-origin read (~60 days):** modeling-driven → stays Daniel; surface-pairing-driven → Alim. Moves Balaji's context either way.
- **RR shed from Daniel:** Ling/Roderick/Yang lean Alim at settle.
- **LWS → Daniel** (day-1 charter move; people follow: Yali, Hedi; Zili per constraint 2).
- **Balaji fork** = Dylan decision ask #1. **Kim loan wind-down** = Dylan ask #2.

## 6. What work-leo should NOT need

No stakeholder history, no perf-case narratives beyond the one-line `sensitive` fields, no interview/hiring context. If a placement question needs more background than this file provides, the answer is "ask James," not "infer."
