---
name: leo-build-and-env
description: Recreate the Leo environment from scratch on a new machine - clone, the three Python runtimes, claude CLI, Google OAuth (GCP leo-api), NotebookLM MCP auth, inbox symlink, hook caveats, and smoke tests. Load this when bootstrapping Leo on a new or rebuilt machine, when an environment is half-working after a move, when deciding what can run headless, or when onboarding work-leo (which has its own separate flow). Keywords - new machine, bootstrap, setup, install, venv, pip, OAuth consent, credentials, headless, smoke test, environment.
---

# Leo Build & Environment

From-scratch bootstrap, in order. Day-to-day operation → [leo-run-and-operate]; where each config value lives → [leo-config-and-flags].

## 0. Know which Leo you're building

- **Personal Leo** (this flow): pc-leo `/home/james/src/leo` (WSL2 Ubuntu) and mac-leo `/Users/jamesli/code/leo` share one git remote.
- **work-leo is a DIFFERENT flow**: separate repo, own source of truth, excludes personal content. Follow `system/export/work-leo-setup/SETUP.md` instead of this skill.

## 1. Clone + verify hooks

```
git clone <remote> ~/src/leo && cd ~/src/leo   # check remote with: git remote -v on an existing machine
```
Hooks need no install — they're wired in the repo's `.claude/settings.local.json` with scripts in `scripts/hooks/`. `session-start.sh` is machine-portable (derives REPO_ROOT from BASH_SOURCE). **Caveat as of 2026-07-13:** `pre-compact.sh` and `detect-corrections.sh` hardcode pc-leo paths and silently degrade elsewhere — see [leo-debugging-playbook] §Hooks before trusting them on a new machine.

## 2. Python runtimes (the #1 new-machine failure)

Three runtimes; binding a script to the wrong one = ModuleNotFoundError:

| Runtime | Create/install | Serves |
|---|---|---|
| system `python3` | `pip3 install --user requests beautifulsoup4 markdownify youtube-transcript-api` | all stdlib KB scripts (ingest, scout, kb_search, kb_lint, build_index, compile_wiki) + rescrape_* + yt_ingest |
| `~/.venvs/leo` | `python3 -m venv ~/.venvs/leo && ~/.venvs/leo/bin/pip install google-api-python-client google-auth-oauthlib markdown jinja2` | send_me.py, save_to_drive.py, md_to_html.py, leo_google/* |
| `~/.venvs/graphify` | `python3 -m venv ~/.venvs/graphify && ~/.venvs/graphify/bin/pip install graphifyy networkx` | build_graph.py (per AGENTS.md §Graph backend) |

(Package set derived from actual imports; versions seen working 2026-07: google-api-python-client 2.196, google-auth-oauthlib 1.4.)

## 3. claude CLI

Must be on PATH — Leo itself, plus `compile_wiki.py` and `build_graph.py build` shell out to it. `which claude` is the check.

## 4. Google OAuth (/send-me, /save-to-drive)

GCP project **leo-api** already exists (Desktop OAuth client "Leo CLI", scopes `gmail.send` + `drive.file`, test user jamesyili@gmail.com — details in `system/leo-overview.md` §Google Integration).

1. Put the client secret at `~/.config/leo/google_credentials.json`, `chmod 600`.
2. First run of `~/.venvs/leo/bin/python scripts/send_me.py <some.md>` opens a **browser consent** (`run_local_server`, port=0) → token saved to `~/.config/leo/google_token.json` (per-machine, gitignored).
3. **There is no headless path** for first auth or a failed refresh. Plan accordingly.

## 5. NotebookLM MCP

Server `notebooklm-mcp`. `get_health` → if unauthenticated, `setup_auth` (browser login; cookies persist ~3 weeks, then re-auth — recurring, see [leo-failure-archaeology] C). Registry is already in the repo (`system/notebooklm/notebooks.md`, slug ids).

## 6. inbox symlink (optional, machine-specific)

pc-leo pattern: `ln -s "/mnt/g/My Drive/Leo Inbox" inbox` (requires Google Drive for Desktop on the Windows side). Mac target differs. Symlink is gitignored; dangles harmlessly if absent. **Never read file bodies under inbox/** (ls only — instinct).

## 7. Smoke tests

```
bash scripts/hooks/session-start.sh | head -20          # git sync + instincts injection
python3 scripts/kb_search.py --stats                    # search index loads
python3 scripts/scout.py --status                       # RSS registry intact
~/.venvs/graphify/bin/python scripts/build_graph.py stats   # graph loads
~/.venvs/leo/bin/python -c "import googleapiclient, markdown, jinja2; print('leo venv OK')"
```
Then run the doctor: `bash .claude/skills/leo-validation-and-diagnostics/scripts/leo_doctor.sh`.

## Headless capability matrix

| Works headless | Needs a browser once per machine |
|---|---|
| git sync, all KB scraping/search/lint/index, graph queries | Google OAuth (send-me/save-to-drive), NotebookLM auth |

## Known traps

- WSL `Zone.Identifier` junk files appear beside Windows-downloaded files — harmless, gitignored.
- The three-runtime split is documented centrally ONLY in this library — older docs assume you know it.
- After bootstrap, the first session on a new machine should check for machine-local absolute paths (the recurring bug class — [leo-failure-archaeology] B/H/K).

## When NOT to use this skill

- Machine already works, something broke → [leo-debugging-playbook]
- Adding config (sources/skills/hooks) → [leo-config-and-flags]
- work-leo → `system/export/work-leo-setup/SETUP.md`

## Provenance & maintenance

Authored 2026-07-13; package sets verified against script imports 2026-07-12. Re-verify:
- Imports still match: `grep -h '^import\|^from' scripts/*.py scripts/leo_google/*.py | sort -u`
- Venvs exist: `ls ~/.venvs/leo/bin/python ~/.venvs/graphify/bin/python`
- Creds present: `ls -l ~/.config/leo/`
- Hook portability caveat still true: `grep -l '/home/james/src/leo' scripts/hooks/*.sh`
