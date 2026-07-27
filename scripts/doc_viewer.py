#!/usr/bin/env python3
"""doc_viewer.py — Render repo .md files to HTML locally: view, watch, or edit.

Local sibling of /send-me's rendering: reuses md_to_html's templates/CSS, but
nothing leaves the machine.

Modes:
  view (default)  render to system/doc_viewer/ (gitignored) and open the browser
  --watch         keep running; re-render on save, page auto-refreshes every 2s
  --edit          localhost edit server: markdown source pane + live rendered
                  preview; Save (button or Ctrl/Cmd+S) writes back to the .md.
                  Source of truth stays markdown — no HTML→md round-trip.

Interpreter: ~/.venvs/leo/bin/python  (needs markdown + jinja2 — same as
md_to_html; system python3 raises ModuleNotFoundError).

Usage:
    ~/.venvs/leo/bin/python scripts/doc_viewer.py <file.md> [more.md ...]
    ~/.venvs/leo/bin/python scripts/doc_viewer.py --edit <file.md> [--port N]
    ... --no-open    # render/serve only, don't open browser

Browser open: WSL → wslview, else explorer.exe (via wslpath -w); macOS → open;
other Linux → xdg-open. Edit server binds 127.0.0.1 only and can read/write
ONLY the file given on the command line.
"""
from __future__ import annotations

import argparse
import hashlib
import html as html_mod
import json
import re
import shutil
import subprocess
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md_to_html import render  # noqa: E402
from md_to_html import (  # noqa: E402
    KIND_CSS,
    LAYOUT,
    SHARED_CSS,
    detect_template,
    extract_title,
    parse_frontmatter,
)
from jinja2 import Template  # noqa: E402
import markdown as markdown_mod  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "system" / "doc_viewer"
AUTO_REFRESH = '<meta http-equiv="refresh" content="2">'


# ---------- static view / watch mode ----------

def out_path_for(md_path: Path) -> Path:
    """Deterministic output path: flattened repo-relative path, or stem+hash outside the repo."""
    md_path = md_path.resolve()
    try:
        rel = md_path.relative_to(REPO_ROOT)
        name = "__".join(rel.with_suffix("").parts)
    except ValueError:
        digest = hashlib.sha256(str(md_path).encode()).hexdigest()[:8]
        name = f"{md_path.stem}-{digest}"
    return OUT_DIR / f"{name}.html"


def render_one(md_path: Path, watch: bool) -> Path:
    html = render(md_path)
    if watch:
        html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + AUTO_REFRESH, 1)
    out = out_path_for(md_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


def is_wsl() -> bool:
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except OSError:
        return False


def open_in_browser(target: str) -> None:
    if sys.platform == "darwin":
        subprocess.run(["open", target], check=False)
    elif is_wsl():
        if shutil.which("wslview"):
            subprocess.run(["wslview", target], check=False)
        elif target.startswith("http"):
            # explorer.exe/cmd start handle URLs; exit code unreliable — don't check
            subprocess.run(["cmd.exe", "/c", "start", target], check=False,
                           cwd="/mnt/c", stderr=subprocess.DEVNULL)
        else:
            win_path = subprocess.run(
                ["wslpath", "-w", target], capture_output=True, text=True
            ).stdout.strip()
            subprocess.run(["explorer.exe", win_path], check=False)
    elif shutil.which("xdg-open"):
        subprocess.run(["xdg-open", target], check=False)
    else:
        print(f"No browser opener found — open manually: {target}", file=sys.stderr)


# ---------- edit mode ----------

def render_markdown_text(text: str, md_path: Path) -> str:
    """render() but from a string (unsaved editor content) instead of the file."""
    frontmatter, body = parse_frontmatter(text)
    kind = detect_template(md_path, frontmatter, body)
    md = markdown_mod.Markdown(extensions=["tables", "fenced_code", "attr_list", "toc"])
    html_body = md.convert(body)
    html_body = re.sub(r"<table>", '<div class="table-wrap"><table>', html_body)
    html_body = re.sub(r"</table>", "</table></div>", html_body)
    title = frontmatter.get("title") or extract_title(body, md_path.stem)
    subtitle = frontmatter.get("subtitle") or frontmatter.get("date") or ""
    css = SHARED_CSS + KIND_CSS.get(kind, "")
    return Template(LAYOUT).render(
        title=title, subtitle=subtitle, kind=kind.replace("_", " "),
        body=html_body, css=css,
    )


EDITOR_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>edit · __FILENAME__</title>
<style>
:root { --bg:#fff; --fg:#1a1a1a; --muted:#6b6b6b; --accent:#2c5cdd; --border:#e5e5e5; --bar:#fafafa; --code-bg:#f4f4f5; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#1a1a1a; --fg:#e8e8e8; --muted:#999; --accent:#7a9cff; --border:#333; --bar:#232323; --code-bg:#262626; }
}
* { box-sizing:border-box; }
html,body { margin:0; height:100%; background:var(--bg); color:var(--fg);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif; }
#bar { display:flex; align-items:center; gap:12px; padding:8px 14px; background:var(--bar);
  border-bottom:1px solid var(--border); font-size:13px; }
#bar .name { font-weight:600; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
#bar .dirty { color:var(--accent); font-weight:700; visibility:hidden; }
#bar button { font-size:13px; padding:5px 14px; border:1px solid var(--border); border-radius:5px;
  background:var(--bg); color:var(--fg); cursor:pointer; }
#bar button.primary { background:var(--accent); border-color:var(--accent); color:#fff; font-weight:600; }
#bar button:disabled { opacity:.5; cursor:default; }
#bar .status { color:var(--muted); margin-left:auto; }
#bar .mode { display:flex; gap:0; }
#bar .mode button { border-radius:0; border-right-width:0; }
#bar .mode button:first-child { border-radius:5px 0 0 5px; }
#bar .mode button:last-child { border-radius:0 5px 5px 0; border-right-width:1px; }
#bar .mode button.on { background:var(--accent); color:#fff; border-color:var(--accent); }
#main { display:flex; height:calc(100% - 42px); }
#src { flex:1; min-width:0; resize:none; border:0; outline:none; padding:16px 18px;
  background:var(--bg); color:var(--fg); border-right:1px solid var(--border);
  font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace; font-size:13.5px; line-height:1.55;
  white-space:pre; overflow-wrap:normal; overflow-x:auto; }
#pv { flex:1; min-width:0; border:0; height:100%; background:var(--bg); }
.hidden { display:none !important; }
</style>
</head>
<body>
<div id="bar">
  <span class="name">__FILENAME__</span>
  <span class="dirty" id="dirty">●</span>
  <span class="mode">
    <button id="m-split" class="on">Split</button>
    <button id="m-edit">Edit</button>
    <button id="m-view">View</button>
  </span>
  <button class="primary" id="save">Save</button>
  <span class="status" id="status">loaded</span>
</div>
<div id="main">
  <textarea id="src" spellcheck="false"></textarea>
  <iframe id="pv"></iframe>
</div>
<script>
const src = document.getElementById('src');
const pv = document.getElementById('pv');
const dirtyDot = document.getElementById('dirty');
const statusEl = document.getElementById('status');
const saveBtn = document.getElementById('save');
let baseMtime = 0;
let dirty = false;
let previewTimer = null;

function setDirty(d) { dirty = d; dirtyDot.style.visibility = d ? 'visible' : 'hidden'; }
function setStatus(s) { statusEl.textContent = s; }

async function loadDoc() {
  const r = await fetch('/raw');
  baseMtime = parseFloat(r.headers.get('X-Mtime'));
  src.value = await r.text();
  setDirty(false);
  await preview();
  setStatus('loaded');
}

async function preview() {
  const r = await fetch('/preview', {method:'POST', body: src.value});
  pv.srcdoc = await r.text();
}

src.addEventListener('input', () => {
  setDirty(true);
  clearTimeout(previewTimer);
  previewTimer = setTimeout(preview, 400);
});

// Tab inserts two spaces instead of leaving the textarea
src.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    e.preventDefault();
    const s = src.selectionStart, epos = src.selectionEnd;
    src.setRangeText('  ', s, epos, 'end');
    src.dispatchEvent(new Event('input'));
  }
});

async function save(force=false) {
  saveBtn.disabled = true;
  setStatus('saving…');
  try {
    const r = await fetch('/save', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({text: src.value, base_mtime: baseMtime, force})
    });
    const j = await r.json();
    if (r.status === 409) {
      if (confirm('File changed on disk since you loaded it (another editor or Leo). Overwrite with your version?')) {
        return save(true);
      }
      setStatus('save cancelled — reload to pick up disk version');
      return;
    }
    if (!j.ok) { setStatus('save failed: ' + (j.error || r.status)); return; }
    baseMtime = j.mtime;
    setDirty(false);
    setStatus('saved ' + new Date().toLocaleTimeString());
  } catch (err) {
    setStatus('save failed: ' + err);
  } finally {
    saveBtn.disabled = false;
  }
}

saveBtn.addEventListener('click', () => save());
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 's') { e.preventDefault(); save(); }
});
window.addEventListener('beforeunload', (e) => { if (dirty) { e.preventDefault(); e.returnValue=''; } });

const modes = {'m-split':[false,false], 'm-edit':[false,true], 'm-view':[true,false]};
for (const id of Object.keys(modes)) {
  document.getElementById(id).addEventListener('click', () => {
    const [hideSrc, hidePv] = modes[id];
    src.classList.toggle('hidden', hideSrc);
    pv.classList.toggle('hidden', hidePv);
    for (const other of Object.keys(modes))
      document.getElementById(other).classList.toggle('on', other === id);
  });
}

loadDoc();
</script>
</body>
</html>
"""


def make_handler(md_path: Path):
    class EditHandler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):  # quiet
            pass

        def _send(self, code: int, body: bytes, ctype: str, extra: dict | None = None):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(body)

        def _body(self) -> bytes:
            length = int(self.headers.get("Content-Length", 0))
            return self.rfile.read(length)

        def do_GET(self):
            if self.path in ("/", "/index.html"):
                page = EDITOR_PAGE.replace("__FILENAME__", html_mod.escape(md_path.name))
                self._send(200, page.encode(), "text/html; charset=utf-8")
            elif self.path == "/raw":
                text = md_path.read_text(encoding="utf-8")
                self._send(200, text.encode(), "text/plain; charset=utf-8",
                           {"X-Mtime": str(md_path.stat().st_mtime)})
            else:
                self._send(404, b"not found", "text/plain")

        def do_POST(self):
            if self.path == "/preview":
                try:
                    html = render_markdown_text(self._body().decode("utf-8"), md_path)
                    self._send(200, html.encode(), "text/html; charset=utf-8")
                except Exception as e:  # render errors must not kill the preview loop
                    msg = f"<pre>preview error: {html_mod.escape(str(e))}</pre>"
                    self._send(200, msg.encode(), "text/html; charset=utf-8")
            elif self.path == "/save":
                try:
                    payload = json.loads(self._body().decode("utf-8"))
                    text = payload["text"]
                    base_mtime = float(payload.get("base_mtime", 0))
                    force = bool(payload.get("force", False))
                    disk_mtime = md_path.stat().st_mtime
                    if not force and abs(disk_mtime - base_mtime) > 1e-6:
                        self._send(409, json.dumps({"ok": False, "error": "disk changed"}).encode(),
                                   "application/json")
                        return
                    md_path.write_text(text, encoding="utf-8")
                    self._send(200, json.dumps({"ok": True, "mtime": md_path.stat().st_mtime}).encode(),
                               "application/json")
                except Exception as e:
                    self._send(500, json.dumps({"ok": False, "error": str(e)}).encode(),
                               "application/json")
            else:
                self._send(404, b"not found", "text/plain")

    return EditHandler


def serve_edit(md_path: Path, port: int, no_open: bool) -> int:
    server = ThreadingHTTPServer(("127.0.0.1", port), make_handler(md_path))
    url = f"http://127.0.0.1:{server.server_address[1]}/"
    print(f"Editing {md_path}")
    print(f"Serving {url}  (Ctrl-C to stop)")
    if not no_open:
        open_in_browser(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    return 0


# ---------- CLI ----------

def main() -> int:
    parser = argparse.ArgumentParser(description="Render repo .md to HTML locally: view, watch, or edit.")
    parser.add_argument("inputs", nargs="+", type=Path, help="Markdown file(s)")
    parser.add_argument("--watch", action="store_true",
                        help="re-render on save; page auto-refreshes every 2s")
    parser.add_argument("--edit", action="store_true",
                        help="serve a localhost editor (source + live preview, Save writes the .md)")
    parser.add_argument("--port", type=int, default=0, help="edit-server port (default: auto)")
    parser.add_argument("--no-open", action="store_true", help="don't open the browser")
    args = parser.parse_args()

    if args.edit and args.watch:
        print("--edit and --watch are exclusive (the editor previews live already).", file=sys.stderr)
        return 2

    files = []
    for p in args.inputs:
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            return 2
        if p.suffix.lower() not in (".md", ".markdown"):
            print(f"Not a markdown file: {p}", file=sys.stderr)
            return 2
        files.append(p.resolve())

    if args.edit:
        if len(files) > 1:
            print("--edit takes exactly one file.", file=sys.stderr)
            return 2
        return serve_edit(files[0], args.port, args.no_open)

    outs = {}
    for p in files:
        outs[p] = render_one(p, watch=args.watch)
        print(f"Rendered {p.name} → {outs[p]}")
        if not args.no_open:
            open_in_browser(str(outs[p]))

    if not args.watch:
        return 0

    print("Watching for changes (Ctrl-C to stop)...")
    mtimes = {p: p.stat().st_mtime for p in files}
    try:
        while True:
            time.sleep(1)
            for p in files:
                try:
                    mt = p.stat().st_mtime
                except FileNotFoundError:
                    continue  # editor save-in-progress; retry next tick
                if mt != mtimes[p]:
                    mtimes[p] = mt
                    render_one(p, watch=True)
                    print(f"Re-rendered {p.name} ({time.strftime('%H:%M:%S')})")
    except KeyboardInterrupt:
        print("\nStopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
