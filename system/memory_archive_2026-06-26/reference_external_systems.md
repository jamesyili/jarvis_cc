---
name: external-system-pointers
description: "NotebookLM notebook IDs/URLs, work-leo location, Rekko repo — where to find things outside the Leo repo"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6f6e1047-8616-4a6b-b5b7-36ae551d5655
---

**NotebookLM notebooks** (full registry: `notebooklm/notebooks.md`):
- Wes Kao Frameworks: slug `wes-kao-frameworks` / UUID `e2650916-178d-460d-bf27-fb25bd933dc9`
- Coaching Patterns: slug `coaching-patterns` / UUID `05132ad9-3803-472e-b917-42f8bf301782`
- Decisive Framework: slug `decisive-framework` / UUID `fb9a13f3-fb09-4109-a1c3-e2f28d3978d9`
- ML & AI System Design: slug `ml-ai-system-design` / UUID `bac25104-a8e4-4b19-957b-caea1ac4644d`

**NotebookLM MCP tool conventions:**
- `notebook_id` arg expects the **slug** (e.g. `coaching-patterns`), NOT the UUID.
- `notebook_url` arg expects the full URL (UUID embedded). Use when slug fails.
- **Always call `get_health` before write operations** (`add_source`, etc.) — auth expires periodically and write ops fail silently with vague "Could not open dialog" errors. `authenticated: false` → run `setup_auth` (browser one-time login).

**Work-Leo:** Separate Claude Code instance on Pinterest work laptop. Independent context, one-time copy from Leo. No persistent sync. Setup guide at `work-leo-setup/TRANSFER.md`.

**Rekko:** Side project with Daniel. Repo at `rekko.ai`. Has its own start/end session skills. Context at `sideprojects/rekko.md`.

**Leo repo:** `git@github.com:jamesyili/leo_cc.git` (remote: origin)

**Graphify (KB graph backend):**
- Python package: `~/.venvs/graphify/` — isolated venv, `graphifyy==0.3.15` installed
- Run the script via: `~/.venvs/graphify/bin/python scripts/build_graph.py <cmd>`
- Claude Code skill: `~/.claude/skills/graphify/SKILL.md` (installed by `graphify install`)
- Leo's wrapper skill: `~/.claude/skills/kb-graph/SKILL.md` (`/kb-graph` — query + refresh)
- Leo's wrapper script: `scripts/build_graph.py` (imports `graphify.*` modules, subprocess-calls the graphify skill for the build pipeline)
- Canonical artifact: `kb/.kb/graph/graph.json` (committed; graph.html + cache/ gitignored)
- Upstream repo: https://github.com/safishamsi/graphify
