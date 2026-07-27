---
name: doc-viewer
description: Open a repo .md file rendered as HTML in the local browser (same rendering as /send-me, no email). Use when James says "open that", "show me that doc", "view X", "/doc-viewer", or wants to read/review a written artifact comfortably while editing the source. --watch gives live re-render on save.
---

# Doc Viewer

Render one or more repo `.md` files to HTML and open them in the local default
browser. Local sibling of `/send-me`: identical rendering pipeline
(`scripts/md_to_html.py` — same templates: base / option_memo / stakeholder_prep,
same auto-detection), but nothing leaves the machine.

## Invocation

```bash
~/.venvs/leo/bin/python scripts/doc_viewer.py <file.md> [more.md ...]
```

**Interpreter matters:** `~/.venvs/leo/bin/python` (needs `markdown` + `jinja2`).
System `python3` fails with ModuleNotFoundError.

Flags:
- `--edit` — **edit directly in the browser.** Serves a localhost editor
  (127.0.0.1 only): markdown source pane left, live rendered preview right
  (debounced), Save button / Ctrl+S writes straight back to the .md. Split /
  Edit / View toggle. Source of truth stays markdown — no HTML→md round-trip.
  One file per server; `--port N` for a stable URL (default: auto). Run it in
  the background (`run_in_background`) and give James the URL; stop it when done
  (`pkill -f "doc_viewer.py --edit"`). Conflict-safe: if the file changed on
  disk after load (e.g. Leo edited it), Save returns 409 and the browser asks
  before overwriting — so avoid editing a file Leo is also mid-edit on.
- `--watch` — keep running; re-renders on every save of the source .md, and the
  page auto-refreshes every 2s (external-editor loop). Exclusive with `--edit`.
  Background it the same way.
- `--no-open` — render/serve only, print the path/URL.

## Defaults & conventions

- **No file named?** Default to the most recently written .md artifact of the
  current session (same convention as /send-me).
- Output lands in `system/doc_viewer/` (gitignored, regenerable — safe to delete
  anytime). Filenames are flattened repo-relative paths, so re-rendering the same
  doc overwrites its previous HTML at a stable path/URL.
- Browser open is platform-aware: WSL (pc-leo) → `wslview`, falling back to
  `explorer.exe` via `wslpath -w`; macOS (mac-leo) → `open`; other Linux →
  `xdg-open`. Note: `explorer.exe` exits nonzero even on success — the script
  ignores its exit code; don't diagnose a failure from it.
- Multiple files → each opens in its own tab.

## When NOT to use

- James wants it on his phone / in email → `/send-me`.
- James wants it in Google Drive / as a GDoc → `/save-to-drive`.
- This skill never sends anything anywhere — it is local-view only.
