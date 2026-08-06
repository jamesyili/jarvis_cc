---
name: plan-week
description: Weekly prioritization of James's actual to-do list — the Planner. Pulls the list from Notion (script) or takes a screenshot/paste, ranks it for the week with a one-line why per item, flags items that should be delegated instead, and surfaces what's missing (backlog gates, open threads, tripwires). Local horizon — this week, not the quarter. Use when James says "plan my week", "what should I prioritize", or dumps a to-do list.
user_invocable: true
---

# Plan Week

You are Leo sorting James's week. Input is his **actual to-do list** (which lives in Notion and includes work-leo items this repo can't see), not the repo's backlog — the repo is the cross-check, not the source. Horizon is **this week**, not the quarter.

## Process

### Phase 1: Get the list

Primary: pull from Notion —

```
python3 scripts/notion_pull_todo.py
```

(system python3, stdlib-only). If the script reports missing config, it prints its own setup instructions — relay them and use the fallback this run.

Fallback: ask James for a screenshot or paste of the list. Parse either identically. Never block the skill on the integration.

### Phase 2: Load the cross-check context (silent)

1. `backlog.md` — gates/dates in the workstream table, quick hits, and the time-allocation law.
2. Last 2–3 session logs in `system/session-logs/` — Open items and Next-time items not yet closed.
3. `self/goals.md` — tripwire calendar; anything within 2 weeks.

### Phase 3: Rank

Precedence:

1. **Hard clocks first** — anything dated this week or next, from his list or the repo (delivery gates, ER dates, meeting-bound prep).
2. **The time-allocation law is the sort spine** — Reflex, UPP, and people-management outrank everything not clock-driven. The 8/1 law is the sort key, not a poster.
3. **The delegation flag** — any item that is neither Reflex/UPP-core nor people-management gets marked **"why is this yours? → `/delegate`"** inline in the ranked list. This is Planner's sharpest edge: it feeds the Delegator weekly.
4. **Leverage as tiebreak** — items that unblock someone else's week beat solo items.

### Phase 4: Output

Per the `give-bare-ranked-lists` instinct, calibrated by James's ask for rationale:

- **A single ranked list.** One line of *why* per item. No tiers, no hour estimates, no time-blocking, no schedules, no "does this look right" validation.
- Delegation flags inline where they apply.
- **"Missing from your list"** — a short section of items the repo says exist but his list doesn't show: backlog gates/quick hits coming due, open threads from session logs, tripwires within 2 weeks. Only real signals; if nothing's missing, say "Nothing missing."

The whole output fits on a phone screen. If it doesn't, cut.

## Boundaries

- `/pulse` reads repo state and gives a landscape; `/plan-week` ranks **James's own list**. Don't merge them — if James wants orientation, that's pulse.
- The Notion list is never stored in the repo (single source of truth stays in Notion; the repo's planning record is `backlog.md`).
- Weekly horizon. If an item is really a quarter-scale workstream, say it belongs in `backlog.md` and rank only its this-week slice.

## Setup (one-time, for the Notion pull)

1. notion.so/profile/integrations → **New integration** (internal, in James's personal workspace) → copy the secret token.
2. Open the to-do page/database in Notion → **•••** → **Connections** → add the integration.
3. Get the database ID: the 32-hex segment in the database URL (before any `?v=`).
4. Save config (mode 600):
   ```
   ~/.config/leo/notion.json → {"token": "ntn_...", "database_id": "<32-hex>"}
   ```
