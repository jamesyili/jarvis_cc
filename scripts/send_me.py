#!/usr/bin/env python3
"""send_me.py — Email a file (or files) to jamesyili@gmail.com via Gmail API.

Renders .md → HTML via md_to_html.py, builds MIME with real attachments,
sends through the local Gmail integration. Logs to system/outbound_log.md.

Usage:
    send_me.py <path> [<path> ...] [--to addr]
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

# Allow `from leo_google...` and `from md_to_html...` when run as a script.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from leo_google.common import append_outbound_log, derive_subject, human_size  # noqa: E402
from leo_google.gmail_send import send  # noqa: E402
from md_to_html import render as md_render  # noqa: E402

DEFAULT_TO = "jamesyili@gmail.com"


def _render_md(path: Path) -> tuple[str, Path]:
    """Render .md to HTML; write tmp .html for attachment. Return (body, html_path)."""
    html = md_render(path)
    tmp = Path(tempfile.gettempdir()) / f"{path.stem}.html"
    tmp.write_text(html, encoding="utf-8")
    return html, tmp


def _build_body_and_attachments(paths: list[Path]) -> tuple[str, list[Path]]:
    if len(paths) == 1:
        p = paths[0]
        ext = p.suffix.lower()
        if ext == ".md":
            html, html_path = _render_md(p)
            return html, [html_path]
        if ext == ".html":
            return p.read_text(encoding="utf-8"), [p]
        if ext == ".txt":
            content = p.read_text(encoding="utf-8")
            return f"<pre>{content}</pre>", []
        size = human_size(p.stat().st_size)
        return f"<p>Attached: <b>{p.name}</b> ({size}).</p>", [p]

    # Multi-file
    items = "\n".join(
        f"<li>{p.name} ({human_size(p.stat().st_size)})</li>" for p in paths
    )
    body = f"<p>Multiple files attached:</p><ul>{items}</ul>"
    attachments: list[Path] = []
    for p in paths:
        if p.suffix.lower() == ".md":
            _, html_path = _render_md(p)
            attachments.append(html_path)
        else:
            attachments.append(p)
    return body, attachments


def main() -> int:
    ap = argparse.ArgumentParser(description="Send files to James's inbox.")
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--to", default=DEFAULT_TO)
    args = ap.parse_args()

    paths = [p.resolve() for p in args.paths]
    for p in paths:
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            return 2

    subject = derive_subject(paths[0])
    body, attachments = _build_body_and_attachments(paths)

    try:
        msg_id = send(to=args.to, subject=subject, html_body=body, attachments=attachments)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        print("Too large for email. Try /save-to-drive.", file=sys.stderr)
        return 3
    except Exception as e:
        print(f"Gmail send failed: {e}", file=sys.stderr)
        return 1

    append_outbound_log("gmail", subject, paths, extra=f"to={args.to} id={msg_id}")
    print(f"Sent. {subject} → {args.to}. (msg_id={msg_id})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
