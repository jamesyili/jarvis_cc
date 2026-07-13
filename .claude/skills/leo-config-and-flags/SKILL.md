---
name: leo-config-and-flags
description: >
  Catalog of every configuration axis in the Leo repo: hook wiring in
  .claude/settings.local.json, permission allowlists (repo vs global), the
  three-Python-interpreter runtime map, model pins buried in scripts,
  credentials/registries in ~/.config/leo/ and system/notebooklm/, machine
  symlinks, .gitignore classes, and how-to-add checklists (new KB source, new
  skill, new instinct, new hook). Load this when: a hook isn't firing or fires
  on the wrong machine; a script throws ModuleNotFoundError; you need to know
  which python runs which script; you're adding a KB source / skill / instinct
  / hook; you're auditing permissions or model pins; Google/NotebookLM auth is
  failing; or you're asking "where is X configured?". Keywords: settings.local.json,
  hooks, SessionStart, PreCompact, Stop, permissions, venv, ~/.venvs/leo,
  ~/.venvs/graphify, model pin, claude-sonnet-4-6, bypassPermissions,
  google_token.json, drive_folders.json, HARD_SLUGS, SOFT_SLUGS, RSS_SOURCES,
  instinct schema, gitignore.
---

# Leo — Config & Flags Catalog

Every configuration axis in the Leo repo, with defaults, guards, known bugs, and
re-verification commands. All facts verified against repo state on **2026-07-12**
unless marked otherwise. Config drifts — run the re-verify line at the end of each
section before trusting it.

**Machine context:** absolute paths like `/home/james/...` are **pc-leo** (WSL2,
repo at `/home/james/src/leo`). The Mac clone lives at `/Users/jamesli/code/leo`
(mac-leo; path attested in the comment at `scripts/hooks/session-start.sh:7`).
work-leo is a **separate repo** with its own source of truth — nothing here
configures it. Several configs below are pc-leo-only; each is flagged.

---

## 1. Hooks wiring

**Authoritative location: the repo's `.claude/settings.local.json`.** The global
`~/.claude/settings.json` contains **no `hooks` key at all** (as of 2026-07-12) —
if you're debugging a hook, editing the global file does nothing. Scripts live in
`scripts/hooks/` (all four executable, `-rwxr-xr-x`).

| Event | Script (in firing order) | What it does |
|---|---|---|
| SessionStart | `scripts/hooks/session-start.sh` | (1) If tree is **clean**: `timeout 20 git pull --ff-only --no-edit`; dirty tree → skip pull, print instruction to use `/start-session` stash flow. (2) `cat system/instincts/INDEX.md` (behavioral memory injection). (3) `cat` the **2** most recent `system/session-logs/*.md` (sorted by filename, which is date-based). All stdout is injected as a session-start system message. |
| PreCompact | `scripts/hooks/pre-compact.sh` | Appends `- <timestamp> — compaction triggered` to the compaction log, then emits a recovery-instructions block that survives compaction. |
| Stop (1st) | `scripts/hooks/suggest-compact.sh` | Increments a counter file `/tmp/leo-toolcount-${SESSION_ID:-default}` on every Stop; prints a "/compact?" nudge when the counter is **exactly 50 or exactly 100** — despite the comment claiming "every 50", there is no nudge at 150+. |
| Stop (2nd) | `scripts/hooks/detect-corrections.sh` | Scans only-new lines of the latest transcript `*.jsonl` for **13** correction regexes (`\bwrong\b`, `\bi told you`, `\bstop (doing|adding|saying)`, etc.) over user text messages; on hit, prints a prompt to create/enrich an instinct in `system/instincts/`. Marker file `/tmp/leo-correction-marker` tracks the last-scanned line count. |

Hook entry format in `settings.local.json` (each event maps to a list of
`{"matcher": "", "hooks": [{"type": "command", "command": "<abs path>"}]}`
objects; Stop has two command entries under one matcher).

### Known bugs / guards (all verified by reading the scripts, 2026-07-12)

- **`session-start.sh` is the portable exemplar.** It derives
  `REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"` (line 8) —
  the comment records it *was* hardcoded and broke on the Mac. Copy this pattern
  into every new hook.
- **`pre-compact.sh` is the counterexample:** line 6 hardcodes
  `COMPACT_LOG="/home/james/src/leo/system/compaction-log.md"` — **pc-leo-only
  bug**; on mac-leo the append silently targets a nonexistent path's parent
  (mkdir is never called; the write fails). Known, not yet fixed.
- **`suggest-compact.sh` shared-counter bug:** `SESSION_ID` is not set by the
  harness, so every session shares `/tmp/leo-toolcount-default` (file exists on
  this machine now, confirming the fallback fires). Concurrent sessions inflate
  each other's counts; counts also survive across sessions until `/tmp` clears.
- **`detect-corrections.sh` is pc-leo-only:** line 6 pins
  `PROJECT_DIR="$HOME/.claude/projects/-home-james-src-leo"` — the project-dir
  slug encodes the repo path, so on mac-leo (slug would be
  `-Users-jamesli-code-leo`) it finds no transcript and exits 0 silently. Its
  `MEMORY_DIR` variable (line 8) is defined but **never used** (vestige of the
  retired auto-memory store). The `/tmp/leo-correction-marker` file is also
  global-not-per-session, same class of bug as the tool counter.
- Also note the fifth settings.local.json permissions entry
  `Bash(/home/james/src/leo/scripts/hooks/session-start.sh)` — the hook script
  itself is allowlisted so manual re-runs don't prompt.

**Hooks wiring also documented in** `CLAUDE.md` §Hooks (must stay consistent —
`CLAUDE.md` is law; this skill just adds the bug detail).

Re-verify: `jq .hooks /home/james/src/leo/.claude/settings.local.json && grep -c "r'" /home/james/src/leo/scripts/hooks/detect-corrections.sh && grep -n "COMPACT_LOG=\|PROJECT_DIR=\|REPO_ROOT=\|SESSION_ID" /home/james/src/leo/scripts/hooks/*.sh`

---

## 2. Permissions

Two layers. Repo layer = narrow, incident-shaped; global layer = broad daily-driver.

### Repo: `.claude/settings.local.json` → `permissions.allow` (21 entries as of 2026-07-12)

Character of the list — do not "clean it up," each entry is a deliberate grant:

- **Narrow one-off Bash grants** accreted from past sessions: five `curl`
  variants probing the interconnects.ai feed URL (RSS debugging), two `cp -r`
  lines that copied the `ingest`/`search` skills from global into the repo, the
  three-line humanizer-skill bootstrap (`mkdir` + two `curl -sL ...
  blader/humanizer ...`), `mkdir -p export/claude-ai/...`, `Bash(exit:*)`.
- **Read broadening:** `Read(//home/james/**)` and `Read(//tmp/**)` — lets Leo
  read outside the repo (global skills, venvs, tmp scratch) without prompts.
- **Skill grants:** `Skill(schedule)` and `Skill(schedule:*)` — the scheduled-
  agents skill is pre-approved.
- **Hook self-grant:** the session-start.sh line noted in §1.

No `deny` or `ask` list at the repo layer.

### Global: `~/.claude/settings.json` (NOT repo-tracked; per-machine)

As of 2026-07-12 on pc-leo:

- `permissions.allow`: ~55 entries — broad tool grants (`Read`, `Edit`, `Write`,
  `Glob`, `Grep`, `WebSearch`, `WebFetch`) plus wildcard Bash for the daily
  toolbelt: `git *`, `gh *`, `uv run/sync/lock/build *`, `python *`, `python3 *`,
  `node/npm run/npx`, `pytest/ruff/mypy`, and the coreutils set (`ls cat head
  tail grep find sed awk sort uniq wc diff echo printf mkdir cp mv chmod ps
  kill killall env export which type sqlite3 jq cd touch tee xargs true false`).
- `permissions.ask` (destructive-op gate): `rm -rf *`, `rm -r *`, `rm -fr *`,
  `shred *`, `dd if=*`. Note plain `rm <file>` is neither allowed nor asked —
  it falls through to the default prompt.
- **Model pin:** `"model": "claude-fable-5[1m]"` (1M-context variant),
  `"effortLevel": "xhigh"`.
- Other toggles: `tui: fullscreen`, `skipDangerousModePermissionPrompt: true`,
  `theme: dark-ansi`, `remoteControlAtStartup: false`,
  `agentPushNotifEnabled: true`.

**Guard:** outbound actions (email via `send_me.py`, Drive upload) are
human-gated by convention, not by permission config — no allowlist entry makes
them auto-fire, and no skill may route around that gate (see leo-change-control).

Re-verify: `jq '.permissions.allow | length' /home/james/src/leo/.claude/settings.local.json && jq '{model, effortLevel, ask: .permissions.ask}' ~/.claude/settings.json`

---

## 3. Python runtime map (THE machine-specific fact)

Three interpreters. Wrong interpreter = `ModuleNotFoundError`. All scripts have
`#!/usr/bin/env python3` shebangs, which is misleading for the venv scripts —
**the shebang does not encode the required interpreter; this table does.**

| Interpreter | Scripts | Why (imports verified 2026-07-12) |
|---|---|---|
| **system `python3`** (`/usr/bin/python3`, 3.12.3) — stdlib-only scripts | `ingest.py`, `scout.py`, `kb_search.py`, `kb_lint.py`, `build_index.py`, `compile_wiki.py`, `build_graph.py`*, `migrate.py`, `extract_themes.py` | Pure stdlib (`urllib`, `json`, `re`, `subprocess`, ...). `compile_wiki.py` and `extract_themes.py` shell out to the `claude` CLI rather than importing an SDK. |
| **system `python3`** — scripts needing site-packages installed system-wide | `rescrape_aman.py`, `rescrape_stubs.py` (import `requests`, `bs4`, `markdownify`); `yt_ingest.py` (deferred import of `youtube_transcript_api` at line 69) | `requests`/`bs4`/`markdownify`/`youtube_transcript_api` are importable from system python3 on pc-leo (verified). On a rebuilt machine these must be pip-installed system-side — see leo-build-and-env. |
| **`~/.venvs/leo/bin/python`** (3.12.3) | `send_me.py`, `save_to_drive.py`, `md_to_html.py`, `scripts/leo_google/*` | `google-api-python-client` + `google-auth-oauthlib` (Gmail/Drive), `Markdown`, `Jinja2`, `pypdf`. System python3 lacks `googleapiclient` (verified: ModuleNotFoundError). The send-me and save-to-drive SKILL.md files document the exact invocation: `~/.venvs/leo/bin/python scripts/send_me.py <path>` / `... scripts/save_to_drive.py <path>`. |
| **`~/.venvs/graphify/bin/python`** (3.12.3) | `build_graph.py`* — for `stats/show/neighbors/god-nodes/orphans/communities/surprising/postprocess` subcommands and the `build` path | `graphifyy` 0.3.15 + `networkx` 3.6.1 + tree-sitter grammars. The script's own docstring (line 20): "Requires: graphifyy installed. Intended python: `~/.venvs/graphify/bin/python`." Its `_ensure_graphify()` fails loud with the exact bootstrap commands (lines 59–69). |

\* `build_graph.py` imports only stdlib at module top, so *some* subcommands run
under system python3 by accident — but `build` calls `_ensure_graphify()` and
the intended interpreter per its docstring is the graphify venv. Use the venv
unconditionally to avoid surprises.

Both venvs live **outside the repo** at `~/.venvs/` (pc-leo path;
machine-specific). Recreation recipe → leo-build-and-env.

Re-verify: `ls ~/.venvs/ && python3 -c "import requests,bs4,markdownify,youtube_transcript_api; print('sys-py OK')" && ~/.venvs/leo/bin/python -c "import googleapiclient,markdown,jinja2; print('leo venv OK')" && ~/.venvs/graphify/bin/python -c "import graphify,networkx; print('graphify venv OK')"`

---

## 4. Model pins in scripts (all as of 2026-07-12)

Model choices are **scattered in script constants**, not centralized. Inventory:

| File:line | Pin | Status |
|---|---|---|
| `scripts/compile_wiki.py:25` | `MODEL = "claude-sonnet-4-6"` → used at line 35: `["claude", "-p", prompt, "--model", MODEL]`, `capture_output=True`, default `timeout=300` | **Production** (wiki compile path). |
| `scripts/build_graph.py:39` | `MODEL = "claude-sonnet-4-6"` | **Dead constant** — defined, never referenced anywhere else in the file (verified by grep). The real model choice is in the subprocess below. |
| `scripts/build_graph.py:107–115` | `claude -p "/graphify <target> --mode <mode>[ --update]" --append-system-prompt <see below> --permission-mode bypassPermissions --add-dir <target> --model sonnet --fallback-model haiku --output-format text`, run from a scratch CWD `/tmp/graphify-leo-<domain>` | **Production** (graph build). ⚠️ **Guard bypass, deliberate:** `bypassPermissions` plus an appended system prompt that orders the child session to skip graphify's ">200 files / >2,000,000 words" interactive subfolder gate and run the full corpus. This is the one place in Leo where a permission gate is auto-approved by design. Do not copy this pattern elsewhere without explicit sign-off (see leo-change-control). Aliases `sonnet`/`haiku` float with CLI resolution rather than pinning a dated snapshot. |
| `scripts/extract_themes.py:29` | `CLAUDE_MODEL = "claude-sonnet-4-6"` | **Idle** — the Lenny's-Podcast theme-extraction campaign finished 272/272 episodes on 2026-04-05 (`system/lennys_podcast_pipeline.md`); script retained for `--concat`/`--status`. ⚠️ **Stale docstring:** line 5 still says "claude-opus-4-6" — the constant is the truth. |
| `~/.claude/settings.json` | `"model": "claude-fable-5[1m]"`, `"effortLevel": "xhigh"` | **Production** — the interactive daily-driver session model (global, per-machine). |

Sub-agent model pins (Karen = Opus 4.6, Consult-Notebook = Sonnet) live in
`.claude/agents/*` frontmatter and are cataloged in `CLAUDE.md` §Agents — that
table is their home; not duplicated here.

Re-verify: `grep -n 'MODEL = \|CLAUDE_MODEL = \|--model' /home/james/src/leo/scripts/compile_wiki.py /home/james/src/leo/scripts/build_graph.py /home/james/src/leo/scripts/extract_themes.py && jq .model ~/.claude/settings.json`

---

## 5. Credentials & registries

### `~/.config/leo/` (outside repo, per-machine, pc-leo inventory verified 2026-07-12)

| File | Mode | What |
|---|---|---|
| `google_credentials.json` | `600` | OAuth **client secret** (GCP desktop client). Machine-portable — copy to a new machine. |
| `google_token.json` | `600` | Per-machine refresh token. **Not portable in practice** — regenerate via browser flow: first run of any `leo_google` script launches `InstalledAppFlow.run_local_server(port=0, prompt="consent")` when the token is missing/expired (see `scripts/leo_google/auth.py`). |
| `drive_folders.json` | `644` | Folder-name → Drive-folder-ID cache; current keys: `"Leo Outbox"`, `"Technical Foundations"`. Safe to delete — regenerated on next upload. |
| `client_secret_leo.json:Zone.Identifier` | — | Windows-download junk artifact; harmless, ignorable. |

Paths are pinned in `scripts/leo_google/auth.py`: `CONFIG_DIR = ~/.config/leo`,
and `SCOPES = ["https://www.googleapis.com/auth/gmail.send",
"https://www.googleapis.com/auth/drive.file"]` — one token covers both send and
upload. Changing scopes forces re-auth.

### NotebookLM

- Registry of record: **`system/notebooklm/notebooks.md`** — **5 notebooks**,
  each with an `ID` field that is a **human-readable slug, not a UUID**:
  `wes-kao-frameworks`, `coaching-patterns`, `decisive-framework`,
  `ml-ai-system-design`, `ethan-evans-frameworks`. (The notebook **URLs** in the
  same file contain Google's UUIDs; the slug is Leo's handle.) Registry last
  updated 2026-04-03 per its own header.
- `notebooklm_cookies.txt` is gitignored (`.gitignore:10`) as defense in depth;
  **no such file exists anywhere in the repo as of 2026-07-12** — the NotebookLM
  MCP server manages its own cookie persistence outside the repo.
- Query audit trail: `system/notebooklm/query_log.md` (append-only, written by
  the Consult-Notebook agent per `CLAUDE.md`).

Re-verify: `ls -la ~/.config/leo/ && grep -n '"scopes"\|SCOPES' /home/james/src/leo/scripts/leo_google/auth.py && grep -c '^\- \*\*ID:\*\*' /home/james/src/leo/system/notebooklm/notebooks.md`

---

## 6. Machine symlinks (repo root)

| Link | Target | Scope |
|---|---|---|
| `inbox` | `/mnt/g/My Drive/Leo Inbox` | **pc-leo only** (WSL2 mount of Google Drive for Desktop). On mac-leo/work-leo this symlink dangles or must point at that machine's Drive mount — do not "fix" it into a real directory. The link itself is **gitignored** (`.gitignore:38`), so each machine sets its own. Do not read file bodies under `inbox/` without James's ask (see the gitignore comment referencing the old `feedback_inbox_no_read` rule). |
| `GEMINI.md` | `AGENTS.md` | All machines (repo-tracked symlink) — gives Gemini CLI the same base context without duplicating the file. If you edit AGENTS.md you have edited GEMINI.md; never break the link by writing a real GEMINI.md file. |

Re-verify: `ls -la /home/james/src/leo/ | grep '\->'`

---

## 7. `.gitignore` classes

Three intent classes (file: `.gitignore`, 45 lines as of 2026-07-12). Know the
class before adding an entry — privacy entries are load-bearing.

1. **Privacy / credentials:** `inbox` (Drive-synced personal drop),
   `notebooklm_cookies.txt`, `google_credentials.json`, `google_token.json`,
   `drive_folders.json` (the Google three are defense-in-depth — real copies
   live in `~/.config/leo/`, never in the repo).
2. **Size / regenerable:** `kb/.kb/graph/graph.html` (~4MB viz, rebuilt by
   `build_graph.py`), `kb/.kb/graph/cache/` (SHA256 extraction cache; directory
   does not currently exist locally), `kb/.kb/graph/raw_chunks/` (7MB
   pre-consolidation chunks — ⚠️ **single-copy risk**: gitignored but required
   to regenerate `surprising.json` via `compute-surprising`; exists only on
   machines that ran a build). Large PDFs: `self/interview_prep/aman_*.pdf`,
   `self/interview_prep/llm_eval/*.pdf` (~227MB, re-downloadable; searchable
   .md conversions are the committed form). Committed graph artifacts (per the
   gitignore's own comment): `graph.json`, `communities.json`,
   `GRAPH_REPORT.md`, `manifest.json`, `surprising.json`.
3. **Junk:** `*Zone.Identifier` (Windows/WSL download artifacts), `.DS_Store`,
   `Thumbs.db`, `__pycache__/`, `*.pyc`, `.antigravitycli/`, Obsidian workspace
   files.

Re-verify: `cat /home/james/src/leo/.gitignore && ls /home/james/src/leo/kb/.kb/graph/`

---

## 8. How-to-add checklists

### 8a. New KB RSS source

The domain routing default is **soft**: `ingest.py:42` computes
`domain = "hard" if source_slug in HARD_SLUGS else "soft"` — a slug you forget
to classify lands in `kb/soft/`.

1. Add the slug to `HARD_SLUGS` (line 32; currently 10 slugs) **or** rely on
   the soft default / add to `SOFT_SLUGS` (line 37; currently 4:
   `wes-kao`, `jefferson-fisher`, `ethan-evans`, `lennys-podcast`) in
   `scripts/ingest.py`.
2. ⚠️ **Drift trap:** `scripts/scout.py` does **not** import those sets — it has
   its own hardcoded inline copies of both slug lists (in the
   `hard_touched`/`soft_touched` blocks of `main()`). Update **both files** or
   scout will silently skip the `_index.md` rebuild for your new source's
   domain after depositing articles.
3. Add the `(slug, feed_url, [tags])` tuple to `RSS_SOURCES` in
   `scripts/ingest.py` (line 50; currently 12 entries). `scout.py` imports this
   registry, so one edit covers both.
4. Test single-source: `python3 scripts/scout.py --source <slug>` (unknown slug
   prints the available list). Check deposit under `kb/{hard|soft}/raw/<slug>/`
   and the dedup manifest `kb/.ingested_manifest.json`.
5. Rebuild catalogs + search index:
   `python3 scripts/build_index.py --domain <hard|soft>` and
   `python3 scripts/kb_search.py --rebuild`.
6. KB data-model details (article frontmatter, domain semantics) → leo-kb-reference.
   Privacy invariant: **Pinterest-internal content never goes in `kb/`**.

Re-verify: `grep -n "HARD_SLUGS\|SOFT_SLUGS" /home/james/src/leo/scripts/ingest.py /home/james/src/leo/scripts/scout.py && python3 /home/james/src/leo/scripts/scout.py --status`

### 8b. New skill

1. Decide the layer. **Project skills** (repo-tracked, portable via git):
   `.claude/skills/<name>/` — 17 dirs as of 2026-07-12. **Global skills**
   (`~/.claude/skills/`, per-machine, NOT repo-tracked): where `graphify` and
   all eight `kb-*` skills live — a rebuilt machine loses these unless
   re-installed (portability gap; see leo-research-frontier). Default new Leo
   skills to the repo layer.
2. Create `<dir>/SKILL.md` — **uppercase filename**, YAML frontmatter with
   `name:` (matching the dir) and a trigger-rich `description:`.
3. Register a row in the `CLAUDE.md` skill table (dispatch logic lives there;
   an unregistered skill is invisible to Leo's routing conventions).
4. If it's a core workflow that non-Claude tools must run, flatten it to
   `prompts/<name>.md` as tool-neutral prose. Note a known doc drift:
   `CLAUDE.md` says "five most-used" are flattened, but `prompts/` holds **8**
   workflows as of 2026-07-12 (coach-check, debrief, draft-email, end-session,
   grill-me, prep, start-session, thinking-partner) + README.md.
5. Adding a skill = structural change to the registry → follow leo-change-control
   conventions for the commit; no skill may route around outbound human-gating.

Re-verify: `ls /home/james/src/leo/.claude/skills/ | wc -l && ls /home/james/src/leo/prompts/ && grep -c '^| `/' /home/james/src/leo/CLAUDE.md`

### 8c. New instinct

Schema (verified from `system/instincts/always-commit-and-push.md` and the
prompt text inside `detect-corrections.sh` — they agree):

```yaml
---
id: <kebab-slug, matches filename>
trigger: <when it fires>
behavior: <what Leo does>
confidence: <0.0–1.0>
evidence_count: <int>
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
status: active
---
```

Body: dated `## Evidence` entries. Then **add a one-liner to
`system/instincts/INDEX.md`** under the right section
(`**<id>** — <trigger> → <behavior>` format) — the SessionStart hook injects
only INDEX.md, so an instinct absent from the index is invisible at session
start. 41 instinct files + INDEX.md as of 2026-07-12. Enrich-before-create:
check INDEX.md for an existing match first (the detect-corrections prompt says
exactly this). Lifecycle/demotion discipline → leo-research-methodology. Never
write to the retired `~/.claude/.../memory/` store.

Re-verify: `ls /home/james/src/leo/system/instincts/ | wc -l && head -10 $(ls /home/james/src/leo/system/instincts/*.md | grep -v INDEX | head -1)`

### 8d. New hook

1. Script goes in `scripts/hooks/`, `chmod +x`.
2. **Derive the repo root — never hardcode:** copy from `session-start.sh:8`:
   `REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"`.
   Counterexamples to not repeat: `pre-compact.sh:6` (hardcoded
   `/home/james/src/leo/...`) and `detect-corrections.sh:6` (hardcoded project
   slug `-home-james-src-leo`) — both silently pc-leo-only.
3. Avoid global `/tmp` state files; if you must persist per-session state,
   don't assume `SESSION_ID` is set (it isn't — see the suggest-compact bug).
4. Wire it in **`.claude/settings.local.json`** (repo file, NOT
   `~/.claude/settings.json`) under the event key, using the
   matcher/hooks/type/command shape shown in §1. Multiple hooks on one event go
   as multiple command entries in order.
5. Remember: hook stdout on SessionStart/PreCompact is injected into context —
   keep it terse; it costs tokens every session.
6. Register the new row in the `CLAUDE.md` §Hooks table.

Re-verify: `ls -la /home/james/src/leo/scripts/hooks/ && jq '.hooks | keys' /home/james/src/leo/.claude/settings.local.json`

---

## 9. Full drift check (run all)

```bash
cd /home/james/src/leo
jq '.hooks | keys' .claude/settings.local.json
jq '{model, effortLevel}' ~/.claude/settings.json
ls ~/.venvs/
grep -n 'MODEL = \|CLAUDE_MODEL = ' scripts/compile_wiki.py scripts/build_graph.py scripts/extract_themes.py
ls -la ~/.config/leo/
ls -la . | grep '\->'
grep -n "HARD_SLUGS\|SOFT_SLUGS" scripts/ingest.py scripts/scout.py
ls system/instincts/ | wc -l          # 42 (41 instincts + INDEX.md) as of 2026-07-12
ls .claude/skills/ | wc -l
```

---

## When NOT to use this skill

- **Why the config is shaped this way** (design invariants, weak points) →
  **leo-architecture-contract**.
- **Changing anything structural** (moves, renames, repoints, commit style) →
  **leo-change-control** — this skill catalogs config; it does not authorize edits.
- **A hook/script is misbehaving right now** (symptom → triage) →
  **leo-debugging-playbook**; the incident history behind each bug →
  **leo-failure-archaeology**.
- **Rebuilding venvs / a fresh machine from zero** → **leo-build-and-env**
  (this skill tells you *which* interpreter; that one tells you how to recreate it).
- **Day-to-day operation** (session lifecycle, KB ops sequences) →
  **leo-run-and-operate**.
- **KB data model / counts / graph concepts** → **leo-kb-reference**;
  scheduled-job campaign details → **leo-kb-automation-campaign**.
- **Verifying a change worked** (evidence standards, leo_doctor) →
  **leo-validation-and-diagnostics**.

---

## Provenance & maintenance

Authored **2026-07-12** by direct read of repo state (no facts copied from
memory or discovery notes without file-level verification): both settings files,
all four hook scripts in full, imports/shebangs of every `scripts/*.py` and
`scripts/leo_google/*.py`, both venv `pip list`s, system-python import probes,
`.gitignore`, `~/.config/leo/` listing with modes, `system/notebooklm/notebooks.md`,
`scripts/ingest.py` slug sets + `RSS_SOURCES`, full `scripts/scout.py`, one
instinct file + `INDEX.md`, skill/prompt directory listings, and root symlinks.
`inbox/` contents were never read (listing only). No git history was needed for
this catalog; incident SHAs live in leo-failure-archaeology.

**Explicitly inferred (not directly observed):** behavior of pc-leo-only paths
*on other machines* (mac-leo dangling `inbox`, detect-corrections finding no
transcript) is deduced from the hardcoded paths, not tested on those machines.
Whether the NotebookLM MCP cookie store lives outside the repo was confirmed
only negatively (no cookie file found in-repo).

Volatile fact classes and their one-line re-checks (each section above also
ends with one):

| Fact class | Re-verify |
|---|---|
| Hook wiring + scripts | `jq .hooks .claude/settings.local.json; ls scripts/hooks/` |
| Permission lists | `jq .permissions .claude/settings.local.json; jq .permissions ~/.claude/settings.json` |
| Global model/effort | `jq '{model, effortLevel}' ~/.claude/settings.json` |
| Runtime map | §3 one-liner (three import probes) |
| Model pins | §4 grep one-liner |
| Credentials inventory | `ls -la ~/.config/leo/` |
| NLM registry | `grep -n '^\- \*\*ID:' system/notebooklm/notebooks.md` |
| Symlinks | `ls -la . \| grep '\->'` |
| Slug sets / RSS registry | §8a grep one-liner |
| Skill/instinct/prompt counts | §8b/§8c `wc -l` one-liners |

If any re-check disagrees with this file, **the repo wins** — update this skill
via the normal change flow (leo-change-control), and if the drift was silent,
consider whether it belongs in leo-failure-archaeology.
