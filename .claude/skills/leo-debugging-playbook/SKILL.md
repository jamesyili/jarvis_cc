---
name: leo-debugging-playbook
description: Symptom-to-triage playbook for the Leo repo's real failure modes. Load this when something in Leo misbehaves — a hook didn't fire or its output is missing from context, git didn't sync at session start, /consult-notebook or NotebookLM fails, /send-me or /save-to-drive errors (ModuleNotFoundError, OAuth, crashes), a KB script fails or returns stale/wrong results, the search agent finds nothing, or a long run died partway. Keywords - hook not firing, no instincts in context, ModuleNotFoundError, Notebook not found, auth expired, stale search results, TypeError, rate limit, session limit, silent no-op, stash conflict.
---

# Leo Debugging Playbook

Triage by subsystem. Each row: symptom → first check → likely cause → fix. Incident SHAs and full stories live in [leo-failure-archaeology]; config details in [leo-config-and-flags]. Machine context matters: many failures are pc-leo/mac-leo/work-leo divergence — always establish which machine you're on first (`pwd` — `/home/james/src/leo` = pc-leo WSL2, `/Users/jamesli/code/leo` = mac-leo).

## Hooks

| Symptom | First check | Cause | Fix |
|---|---|---|---|
| No instincts/session-log block in session context | `cat .claude/settings.local.json \| grep -A3 SessionStart` | Hooks live in **repo `.claude/settings.local.json`**, NOT `~/.claude/settings.json` (global hooks block is empty — this was mis-documented until commit `9ca6865`) | Verify wiring + `bash scripts/hooks/session-start.sh` manually to see its output/errors |
| Compaction log not updating on mac/work-leo | `grep COMPACT_LOG scripts/hooks/pre-compact.sh` | `pre-compact.sh` hardcodes `/home/james/src/leo/system/compaction-log.md` — breaks off pc-leo. Known bug; `session-start.sh` had the same class and was fixed via `REPO_ROOT` derivation (see its header comment) | Apply the same `REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"` pattern |
| Corrections never detected off pc-leo | `grep 'home-james' scripts/hooks/detect-corrections.sh` | Hardcoded transcript dir `-home-james-src-leo` → **silent no-op** on any other machine (project-dir slug differs per path) | Derive the slug from `$PWD`; until then, know detection only works on pc-leo |
| /compact nudge fires at odd times | `ls /tmp/leo-toolcount-*` | `suggest-compact.sh` keys on `${SESSION_ID:-default}` but Claude Code doesn't export `SESSION_ID` → all sessions share `/tmp/leo-toolcount-default` | Cosmetic; ignore or fix the keying |

## Git sync

| Symptom | First check | Cause | Fix |
|---|---|---|---|
| "Working tree is dirty — skipped auto-pull" at session start | `git status` | By design: hook only fast-forwards a clean tree (`--ff-only`, `timeout 20`) | Commit or stash, then pull. /start-session handles via stash → pull → pop |
| Stash pop conflicts after sync | `git stash list`, `git status` | Two-machine editing collision — precedent: 2026-06-26, stashed deletion vs incoming edit | Resolve manually; prefer the incoming edit unless the local change is this session's work |
| Machines diverged / non-ff | `git log --oneline origin/main..HEAD` | A session ended without push (violates always-commit-and-push) | Rebase local on origin; never force-push |

## NotebookLM / consult-notebook

Triage in this order:

1. **Auth expired** (~3-week cookie cadence; failures logged 04-21, 04-25, 05-02, 07-02 in `system/notebooklm/query_log.md`): `get_health` → if unauthenticated, `setup_auth` (browser required — cannot fix headless).
2. **Wrong notebook id**: use **slug ids** (`wes-kao-frameworks`, `coaching-patterns`, `decisive-framework`, `ml-ai-system-design`, `ethan-evans-frameworks`). UUIDs caused "Notebook not found" on 2026-07-02. WARNING: `.claude/skills/consult-notebook/SKILL.md` is stale (4 notebooks, UUID ids) — trust `.claude/agents/consult-notebook.md` and `system/notebooklm/notebooks.md` instead.
3. **Answer looks fabricated**: the agent has a hard ERROR-string failsafe added after the 2026-04 hallucination bug (`b99c388` — wrong MCP tool name meant no call was ever made). If a "consult result" has no matching entry appended to `system/notebooklm/query_log.md`, treat it as fabricated.

## Google integration (/send-me, /save-to-drive)

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: markdown` / `jinja2` / `googleapiclient` | Wrong interpreter — these need the leo venv | Run with `~/.venvs/leo/bin/python scripts/send_me.py …` |
| `FileNotFoundError: Missing OAuth client secret` | `~/.config/leo/google_credentials.json` absent on this machine | Per-machine setup — see [leo-build-and-env] step 4; GCP project `leo-api` |
| Browser window opens / hangs headless | First auth or refresh failure runs `run_local_server` — browser mandatory | Auth once interactively per machine; there is no headless path |
| Crash in `append_outbound_log` | `Path` objects required, `str` passed (2026-07-10 incident, `04656a0`) | Pass `Path(...)`; documented in send-me SKILL.md |
| Exit 3 on send | File > 25 MB Gmail cap | Use `/save-to-drive` |

## KB scripts

| Symptom | Cause | Fix |
|---|---|---|
| `kb_search.py` misses recent articles | Index **never auto-invalidates**; last built 2026-04-05 (as of 2026-07-13) while corpus kept growing | `python3 scripts/kb_search.py --rebuild` first |
| `compile_wiki.py` / `build_graph.py build` / graph build fails immediately | Shells out to `claude` CLI — must be on PATH | `which claude` |
| `build_graph.py` exits 2 | graphify venv missing | `~/.venvs/graphify/bin/python scripts/build_graph.py <cmd>`; install per AGENTS.md §Graph backend |
| `yt_ingest.py` crashes after a successful ingest | Latent bug: calls `build_raw_index()` with no `domain` arg (required) → TypeError | Known; fix the call or run `python3 scripts/build_index.py` manually after |
| `extract_themes.py` fails on paths | **Orphaned** — points at `work/learning/`, which no longer exists | Do not run. Historical only |
| `migrate.py` does nothing useful | Dead one-shot (learning/ → kb/ migration, source gone) | Do not run |

**Remote/cloud container specifics (2026-09-07):** `export.arxiv.org` is blocked by the egress proxy (urllib `Tunnel connection failed: 403`) — `ingest_paper.py` exits with a plain message; pass a downloaded PDF/.md instead. `pip install pypdf` succeeds but the system `cryptography` package is broken there (`_cffi_backend` missing), so `import pypdf` fails; PDF extraction only works on James's machines (poppler `pdftotext` or a working `pypdf`).

## Local tooling

| Symptom | Cause | Fix |
|---|---|---|
| Read tool fails on a PDF with "pdftoppm is not installed" (large/multi-page PDFs) | poppler-utils absent on pc-leo (hit 2026-08-11 reading a 12-page upload) | Text extraction via `~/.venvs/leo/bin/python` + `pypdf` (installed): `PdfReader(path).pages[i].extract_text()`. Loses figures/tables' layout — fine for prose docs. Or install poppler-utils for full rendering |

## Agents

| Symptom | Cause | Fix |
|---|---|---|
| `search` agent returns nothing/garbage | `.claude/agents/search.md` carries stale `/Users/jamesli/...` macOS paths (+ one dead `articles/` dir) — known-broken on pc-leo as of 2026-07-13 | Fix its paths, or grep directly |
| `/weekly-review` reads missing files | Its SKILL.md still points at dead `AIContext/` paths (pre-2026-03-29 layout) | Known stale; update before relying on it |

## Long-running / multi-agent work

Session limits kill long runs mid-flight. Precedents: graphify Phase 1 lost 13 chunks (2026-04-08); a 17-agent skill-authoring workflow died wholesale (2026-07-12). Rules: forecast token cost before any LLM sweep (see [leo-proof-and-analysis-toolkit] Recipe 2), checkpoint incrementally, design for resume, and **never assume a long run completed — verify outputs on disk** (dirs can exist with no files inside).

## When NOT to use this skill

- Understanding *why* the system is designed this way → [leo-architecture-contract]
- Full incident stories with SHAs → [leo-failure-archaeology]
- Where a config value lives / how to add config → [leo-config-and-flags]
- Routine operation commands → [leo-run-and-operate]

## Provenance & maintenance

Authored 2026-07-13 from repo state + git archaeology (this playbook's rows were verified against script/source reads on 2026-07-11/12 discovery). Re-verify before trusting:
- Hook wiring: `python3 -c "import json;print(json.load(open('.claude/settings.local.json'))['hooks'].keys())"`
- Hardcode bugs still present: `grep -l '/home/james/src/leo' scripts/hooks/pre-compact.sh scripts/hooks/detect-corrections.sh`
- Search-index staleness: `stat -c '%y' kb/.kb/search_index.json`
- yt_ingest bug still present: `grep -n 'build_raw_index()' scripts/yt_ingest.py`
- Stale agent paths: `grep -n '/Users/jamesli' .claude/agents/*.md`
- Notebook slugs: `grep -i 'slug\|id' system/notebooklm/notebooks.md | head`
