---
name: leo-run-and-operate
description: Day-to-day operating runbook for the Leo repo - the session lifecycle (hooks, start-session, end-session, session logs), the full KB operations command set with the correct interpreter for each script, outbound email/Drive commands, and where every kind of output lands. Load this when running any Leo operation - starting or ending a session properly, scouting/ingesting/searching/linting the KB, compiling wiki articles, querying the graph, sending files to James, or figuring out where an artifact/draft/log belongs. Keywords - runbook, session lifecycle, end-session, session log, scout, ingest, search, lint, compile, graph query, send-me, save-to-drive, outbound log, artifacts, where does X go.
---

# Leo Run & Operate

The operating runbook. Interpreter matters — wrong python = ModuleNotFoundError ([leo-config-and-flags] has the full runtime map). Failures → [leo-debugging-playbook].

## Session lifecycle

1. **SessionStart hook fires automatically**: git sync (clean tree only, ff-only, 20s timeout) → injects `system/instincts/INDEX.md` → injects last 2 session logs. If that block is missing from context, the hook failed — triage before proceeding.
2. **/start-session**: read the latest 2 logs, load task-relevant context, then act on James's request; no alignment questions by default. Non-Claude tools: follow `prompts/start-session.md`.
3. **Work**, honoring instincts (INDEX is in context; read the full instinct file when one applies).
4. **/end-session** (or `prompts/end-session.md`): capture without confirmation questions → check local/remote same-day log collisions → write the log → context update → self-improvement → instinct extraction → review ownership, stage explicit session files, **commit AND push LAST**. Verify the push landed, even when the log is skipped. Preserve existing logs; no automatic retention deletion.

**Session log spec** (`system/session-logs/YYYY-MM-DD.md`; multi-segment days append `b`, `c`):

```markdown
## YYYY-MM-DD (time-of-day) — one-line summary
**Done:** 2-5 concrete bullets
**Decisions:** if any
**Open:** if any
**Next time:** specific and actionable
```

Skip the log for trivial sessions. `backlog.md` is retired; Notion is the live task list. End-session does not automatically sync it: apply list changes only when the session changed items and James asked for list updates. Bump `system/file_index.md` timestamps on context-file edits and add an INDEX line for any new instinct.

## KB operations

| Task | Command (copy-paste) | Notes |
|---|---|---|
| RSS scout | `python3 scripts/scout.py [--source slug] [--status]` | 13 sources; writes articles + rebuilds affected indexes |
| Ingest modes | `python3 scripts/ingest.py {daily\|status\|check-rss\|backfill-aman\|backfill-lenny\|backfill-substack}` | `daily` also writes `kb/.digests/` (idle as of 2026-07-13) |
| Search | `python3 scripts/kb_search.py "query" [--top N]` | **`--rebuild` first if index is older than newest article** — it never auto-invalidates (stale since 2026-04-05) |
| Rebuild index | `python3 scripts/kb_search.py --rebuild` then `--stats` | |
| Catalogs | `python3 scripts/build_index.py [--domain hard\|soft]` | regenerates `_index.md` files |
| Ingest a paper James passes | `python3 scripts/ingest_paper.py <arXiv id\|URL\|.pdf\|.md> --tags ... [--evidence authored\|discussed]` | → `kb/hard/raw/arxiv/`, rebuilds search, reports inherited U/R (skill: `ingest`, 2026-09-07) |
| Learner model | `python3 scripts/kb_knowledge_state.py {queue\|get\|set\|list\|article\|render\|export\|check}` | James's per-concept understanding/relevance; `set` only on evidence (skill: `knowledge-state`) |
| Lint | `python3 scripts/kb_lint.py [--domain d] [--json]` | thin articles, broken wikilinks, near-dup slugs |
| Wiki compile | `python3 scripts/compile_wiki.py {scan\|plan\|compile\|incremental} --domain d [--all\|--concept X]` | shells `claude` CLI; scan batches 150 articles/call; long + token-spending — forecast first |
| Graph query | `~/.venvs/graphify/bin/python scripts/build_graph.py {stats\|show\|neighbors\|god-nodes\|orphans\|communities\|surprising}` | instant, free |
| Graph rebuild | `... build_graph.py {build\|refresh\|postprocess}` | **1–3 hrs, token-heavy, rate-limit precedent** — treat as a James-gated spend decision |
| YouTube | `python3 scripts/yt_ingest.py {--status\|--retry\|--video ID\|--dry-run}` | 16 queued; known TypeError after successful ingest — run `build_index.py` manually after |

**Do not run:** `extract_themes.py` (orphaned — dead paths), `migrate.py` (dead one-shot).

## Outbound (human-gated beyond James himself)

| Task | Command |
|---|---|
| Email file(s) to James | `~/.venvs/leo/bin/python scripts/send_me.py <file>... [--to addr]` — md→HTML, 25 MB cap (exit 3 → use Drive) |
| Upload to Drive "Leo Outbox" | `~/.venvs/leo/bin/python scripts/save_to_drive.py <file>... [--raw]` — .md converts to Google Doc unless `--raw` |

Both append an audit line to `system/outbound_log.md`. Anything outbound to someone other than James requires his explicit per-item approval — no exceptions.

## Where outputs land

| Output | Home |
|---|---|
| Display artifacts (HTML, viz) | `system/artifacts/` |
| Drafts staged for sending | `system/outbound_drafts/` (+ audit in `system/outbound_log.md`) |
| Tool-transfer bundles | `system/export/` |
| NLM consult audit | `system/notebooklm/query_log.md` (append-only; a consult with no entry here didn't happen) |
| Session logs | `system/session-logs/` |
| Compaction events | `system/compaction-log.md` |
| Month rollups | `system/monthly-summaries/` |
| New behavioral rules | `system/instincts/` + INDEX line |

## When NOT to use this skill

- Something errored → [leo-debugging-playbook]
- What the KB data means / graph concepts → [leo-kb-reference]
- Bootstrapping a machine → [leo-build-and-env]
- Scheduling recurring jobs → [leo-kb-automation-campaign]
- Session-log/backlog *format* details and doc duties → [leo-docs-and-writing]

## Provenance & maintenance

Authored 2026-07-13; every command verified against script argparse/main during 2026-07-11/12 discovery. Re-verify:
- Any script's real interface: `python3 scripts/<name>.py --help` (or read its argparse block)
- Log spec: `sed -n '1,40p' .claude/skills/session-log/SKILL.md`
- Digest idleness: `ls kb/.digests/ 2>/dev/null | wc -l`
- Outbound audit works: `tail -3 system/outbound_log.md`
