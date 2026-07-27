#!/usr/bin/env python3
"""doc_viewer.py — Render repo .md files to HTML and open them in the local browser.

Local sibling of /send-me's rendering: reuses md_to_html.render() (same templates,
same CSS), but instead of emailing, writes HTML to system/doc_viewer/ (gitignored,
regenerable) and opens the default browser. Makes repo docs comfortable to read
while editing the .md source.

Interpreter: ~/.venvs/leo/bin/python  (needs markdown + jinja2 — same as md_to_html;
system python3 raises ModuleNotFoundError).

Usage:
    ~/.venvs/leo/bin/python scripts/doc_viewer.py <file.md> [more.md ...]
    ... --watch      # keep running; re-render on save, page auto-refreshes every 2s
    ... --no-open    # render only, print output path(s)

Browser open: WSL → wslview, else explorer.exe (via wslpath -w); macOS → open;
other Linux → xdg-open.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from md_to_html import render  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "system" / "doc_viewer"
AUTO_REFRESH = '<meta http-equiv="refresh" content="2">'


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


def open_in_browser(path: Path) -> None:
    if sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)
    elif is_wsl():
        if shutil.which("wslview"):
            subprocess.run(["wslview", str(path)], check=False)
        else:
            win_path = subprocess.run(
                ["wslpath", "-w", str(path)], capture_output=True, text=True
            ).stdout.strip()
            # explorer.exe exits nonzero even on success — don't check
            subprocess.run(["explorer.exe", win_path], check=False)
    elif shutil.which("xdg-open"):
        subprocess.run(["xdg-open", str(path)], check=False)
    else:
        print(f"No browser opener found — open manually: {path}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render repo .md to HTML and open locally.")
    parser.add_argument("inputs", nargs="+", type=Path, help="Markdown file(s)")
    parser.add_argument("--watch", action="store_true",
                        help="re-render on save; page auto-refreshes every 2s")
    parser.add_argument("--no-open", action="store_true", help="render only, don't open browser")
    args = parser.parse_args()

    files = []
    for p in args.inputs:
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            return 2
        if p.suffix.lower() not in (".md", ".markdown"):
            print(f"Not a markdown file: {p}", file=sys.stderr)
            return 2
        files.append(p.resolve())

    outs = {}
    for p in files:
        outs[p] = render_one(p, watch=args.watch)
        print(f"Rendered {p.name} → {outs[p]}")
        if not args.no_open:
            open_in_browser(outs[p])

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
