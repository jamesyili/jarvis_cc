---
name: leo-docs-and-writing
description: Maintaining the Leo repo's documents of record - which docs are live vs historical (and the never-repoint-historical rule), the real templates (session log, backlog row, instinct file, file_index row), sync duties (SKILL.md to prompts/, CLAUDE.md registry, file_index timestamps), house style for James-facing prose, and what may leave the repo. Load this when writing or updating any doc of record, filing a session log or backlog row, refreshing the stale leo-overview.md, flattening a skill to prompts/, or checking whether content is shareable outside the repo. Keywords - docs of record, session log format, backlog format, instinct schema, file_index, prompts sync, house style, AI prose tells, leo-overview refresh, shareable, historical record.
---

# Leo Docs & Writing

## Docs of record: live vs historical

| Class | Files | Rule |
|---|---|---|
| **LIVE** — must stay current, re-pointed on moves | AGENTS.md (§Folder Structure is the canonical layout), CLAUDE.md (skill/agent/hook registry), backlog.md, system/file_index.md, system/instincts/* + INDEX.md, work/ + self/ context files, system/notebooklm/notebooks.md, prompts/* | Drift here is a defect — doctor check 5 |
| **HISTORICAL — never re-pointed, by stated rule** | system/session-logs/, system/memory_archive_2026-06-26/, system/export/ snapshots, work/people/archive/ | Old paths inside are historical record, not bugs (rule stated in 2026-07-11c log) |
| **Self-description** | system/leo-overview.md — the portable, outward-shareable system description | **~3 months stale as of 2026-07-13** (dated 2026-04-05: claims live auto-memory, 4 notebooks, "24 skills", "25 sessions"). Refreshing it is the standing first exercise for any maintainer — re-derive from CLAUDE.md (skills/agents/hooks), system/notebooklm/notebooks.md (5 notebooks), `ls system/session-logs \| wc -l`, and AGENTS.md structure |

## Templates (quoted from the real specs)

**Session log** (`system/session-logs/YYYY-MM-DD.md`, suffix `b`/`c` for multi-segment days — spec in `.claude/skills/session-log/SKILL.md`):
```markdown
## YYYY-MM-DD (time-of-day) — one-line summary
**Done:** 2-5 concrete bullets, specific enough to pick up without the conversation
**Decisions:** / **Open:** / **Next time:** actionable ("finish X and validate against Y", not "continue X")
```

**Backlog row** (`backlog.md`): `| Item | Why / Goal | Description / Subtasks | Rough Time | Progress | Priority |` — priority P0–P4; demotions/promotions logged inside the Progress cell with dates (the backlog doubles as lab notebook); the file header carries a dated changelog paragraph per session.

**Instinct file** (`system/instincts/<id>.md`): YAML frontmatter `id / trigger / behavior / confidence (start 0.3) / evidence_count / created / last_updated / status`, then `## Evidence` entries dated, each with quote, context, and `Signal: correction|confirmation`. Plus one `- **id** — trigger → behavior` line in INDEX.md. Lifecycle rules → [leo-research-methodology].

**file_index row** (`system/file_index.md`): `| File | Description | Last updated |` — one-line descriptions; bump the timestamp on every context-file edit; add a row for every new context file.

## Sync duties

1. **SKILL.md → prompts/**: 8 workflows are flattened (start-session, end-session, prep, draft-email, debrief, coach-check, grill-me, thinking-partner — prompts/README.md is the authority; note CLAUDE.md/AGENTS.md still say "five", a known undercount). SKILL.md is source of truth; edit it first, then re-flatten. Flattening = strip Claude-Code-only machinery (hooks, sub-agents, skill chaining), keep the instincts system (portable).
2. **CLAUDE.md registry**: every added/removed skill or agent updates its tables. As of 2026-07-13 the leo-* library itself is **not yet registered** — a pending change-control item.
3. **file_index timestamps**: every context edit, same commit.

## House style

**James-facing prose** (drafts in his voice, journal-adjacent writing — from the instincts, read them before big drafts): no em-dash overuse, no rule-of-three cadence, no epigram verdict sentences, no vague grandiosity (`avoid-ai-prose-tells`); evidence the reader can check; first person "I" when writing as James; plain prose, no framework names, on emotional topics (`plain-language-on-emotional-topics`); ranked lists arrive bare — no tiers/hours/validation (`give-bare-ranked-lists`); during live iteration, synthesize in chat — don't auto-write a doc unless a durable artifact is requested (`prefer-chat-synthesis-during-iteration`).

**This skill library**: imperative runbook voice, tables over prose, copy-pasteable commands with interpreter, date-stamped volatile facts, Provenance & maintenance with runnable re-verify commands, one home per fact + cross-references to siblings.

## What may leave the repo

- `system/leo-overview.md` — the only doc written to be shared outside.
- `kb/` — potentially indexable/shareable, hence the hard rule: no Pinterest internals, ever (instinct `pinterest-internals-not-in-kb`).
- Everything under `work/` and `self/` — private, never leaves. Blog writing about Leo/work must be grounded on public material only (e.g., no UPP by name — constraint recorded in backlog.md Write section).
- Outbound of any kind beyond /send-me to James → per-item human approval.

## When NOT to use this skill

- Executing moves/commits/migrations → [leo-change-control]
- Instinct lifecycle decisions (create/enrich/promote) → [leo-research-methodology]
- Where outputs land at runtime → [leo-run-and-operate]

## Provenance & maintenance

Authored 2026-07-13. Re-verify:
- Flattened set: `ls prompts/*.md` vs prompts/README.md table
- leo-overview staleness: `head -6 system/leo-overview.md`
- Registry completeness: `ls .claude/skills | wc -l` vs CLAUDE.md tables
- Template specs: `sed -n '1,40p' .claude/skills/session-log/SKILL.md`; any instinct file's frontmatter
