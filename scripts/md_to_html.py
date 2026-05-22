#!/usr/bin/env python3
"""md_to_html.py — Render a Markdown file to phone-friendly HTML.

Used by the /send-me skill to ship rendered HTML instead of raw .md
(per Thariq Shihipar's argument: HTML wins for any artifact a human reads).

Usage:
    md_to_html.py <input.md>              # writes to stdout
    md_to_html.py <input.md> -o <out.html>  # writes to file

Template detection (cascading):
    1. YAML frontmatter `template:` override
    2. Filename / content heuristics
    3. Default: base

Templates available: base, option_memo, stakeholder_prep.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import markdown
from jinja2 import Template


SHARED_CSS = """
:root {
  --bg: #ffffff;
  --fg: #1a1a1a;
  --muted: #6b6b6b;
  --accent: #2c5cdd;
  --border: #e5e5e5;
  --row-alt: #fafafa;
  --code-bg: #f4f4f5;
  --callout-bg: #f5f8ff;
  --callout-border: #c7d4f7;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a1a;
    --fg: #e8e8e8;
    --muted: #999;
    --accent: #7a9cff;
    --border: #333;
    --row-alt: #232323;
    --code-bg: #262626;
    --callout-bg: #1d2438;
    --callout-border: #3a4a78;
  }
}
* { box-sizing: border-box; }
html, body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
}
.wrap {
  max-width: 760px;
  margin: 0 auto;
  padding: 24px 20px 64px;
}
.meta {
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}
.meta .kind {
  display: inline-block;
  padding: 2px 8px;
  background: var(--callout-bg);
  border: 1px solid var(--callout-border);
  border-radius: 4px;
  color: var(--accent);
  font-weight: 600;
  font-size: 11px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
h1 { font-size: 28px; line-height: 1.25; margin: 0 0 16px; font-weight: 700; }
h2 { font-size: 22px; line-height: 1.3; margin: 32px 0 12px; font-weight: 650; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
h3 { font-size: 18px; line-height: 1.35; margin: 24px 0 8px; font-weight: 600; }
h4 { font-size: 16px; margin: 20px 0 8px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }
p { margin: 0 0 14px; }
ul, ol { margin: 0 0 14px; padding-left: 24px; }
li { margin-bottom: 6px; }
li > ul, li > ol { margin-top: 6px; margin-bottom: 0; }
strong { font-weight: 650; }
em { font-style: italic; }
a { color: var(--accent); text-decoration: none; border-bottom: 1px solid transparent; }
a:hover { border-bottom-color: var(--accent); }
hr { border: 0; border-top: 1px solid var(--border); margin: 32px 0; }
blockquote {
  margin: 16px 0;
  padding: 8px 16px;
  border-left: 3px solid var(--accent);
  background: var(--callout-bg);
  color: var(--fg);
  border-radius: 0 4px 4px 0;
}
blockquote p:last-child { margin-bottom: 0; }
code {
  font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  font-size: 13.5px;
  background: var(--code-bg);
  padding: 1px 5px;
  border-radius: 3px;
}
pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 12px 14px;
  overflow-x: auto;
  font-size: 13.5px;
  line-height: 1.5;
  margin: 16px 0;
}
pre code { background: transparent; padding: 0; }
.table-wrap { overflow-x: auto; margin: 16px 0; -webkit-overflow-scrolling: touch; }
table { border-collapse: collapse; width: 100%; font-size: 14.5px; }
th, td { padding: 8px 12px; border: 1px solid var(--border); text-align: left; vertical-align: top; }
th { background: var(--row-alt); font-weight: 650; font-size: 13px; text-transform: uppercase; letter-spacing: 0.03em; color: var(--muted); }
tbody tr:nth-child(even) { background: var(--row-alt); }
@media (max-width: 600px) {
  .wrap { padding: 16px 14px 48px; }
  h1 { font-size: 24px; }
  h2 { font-size: 19px; }
  h3 { font-size: 16.5px; }
  body { font-size: 15.5px; }
  table { font-size: 13.5px; }
  th, td { padding: 6px 8px; }
}
"""

OPTION_MEMO_CSS = """
/* option_memo: card treatment for Option N sections + recommendation callout */
h3[id^="option-"] {
  background: var(--callout-bg);
  border-left: 4px solid var(--accent);
  padding: 10px 14px;
  border-radius: 4px;
  margin-top: 28px;
}
h2[id^="recommendation"] {
  color: var(--accent);
}
h2[id^="recommendation"]::before {
  content: "→ ";
  color: var(--accent);
}
h2[id^="open-questions"]::before,
h2[id^="open-variables"]::before {
  content: "? ";
  color: var(--muted);
}
"""

STAKEHOLDER_PREP_CSS = """
/* stakeholder_prep: phone-glanceable cards for talking points / watch-fors / asks */
h2[id^="talking-points"]::before,
h2[id^="watch-fors"]::before,
h2[id^="watch-outs"]::before,
h2[id^="asks"]::before,
h2[id^="framing"]::before,
h2[id^="before-you"]::before { content: "▸ "; color: var(--accent); }
ul li { margin-bottom: 8px; }
h2 + ul, h2 + ol { background: var(--callout-bg); padding: 12px 12px 12px 36px; border-radius: 6px; border: 1px solid var(--callout-border); }
"""

KIND_CSS = {
    "base": "",
    "option_memo": OPTION_MEMO_CSS,
    "stakeholder_prep": STAKEHOLDER_PREP_CSS,
}

LAYOUT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ title }}</title>
<style>{{ css }}</style>
</head>
<body>
<div class="wrap">
<div class="meta">
<span class="kind">{{ kind }}</span>
{%- if subtitle %} &nbsp;·&nbsp; {{ subtitle }}{% endif %}
</div>
{{ body | safe }}
</div>
</body>
</html>
"""


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Strip YAML-ish frontmatter. Returns (frontmatter dict, body)."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm_block, body = m.group(1), m.group(2)
    fm: dict[str, str] = {}
    for line in fm_block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def detect_template(path: Path, frontmatter: dict, body: str) -> str:
    """Cascading detection: frontmatter → filename → content → base."""
    if "template" in frontmatter and frontmatter["template"] in KIND_CSS:
        return frontmatter["template"]
    name = path.name.lower()
    parent = str(path.parent).lower()
    if "session-log" in parent or re.match(r"^\d{4}-\d{2}-\d{2}.*\.md$", name):
        return "base"
    if "prep" in name or "1on1" in name or "/prep" in parent:
        return "stakeholder_prep"
    if re.search(r"##+\s+Option\s+\d", body, re.IGNORECASE | re.MULTILINE):
        return "option_memo"
    if re.search(r"##+\s+Recommendation\b", body, re.IGNORECASE | re.MULTILINE) and \
       re.search(r"##+\s+(Open\s+questions?|Open\s+variables?)\b", body, re.IGNORECASE | re.MULTILINE):
        return "option_memo"
    return "base"


def extract_title(body: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return m.group(1).strip() if m else fallback


def render(md_path: Path) -> str:
    text = md_path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    kind = detect_template(md_path, frontmatter, body)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "toc"])
    html_body = md.convert(body)
    html_body = re.sub(r"<table>", '<div class="table-wrap"><table>', html_body)
    html_body = re.sub(r"</table>", "</table></div>", html_body)

    title = frontmatter.get("title") or extract_title(body, md_path.stem)
    subtitle = frontmatter.get("subtitle") or frontmatter.get("date") or ""

    css = SHARED_CSS + KIND_CSS.get(kind, "")
    template = Template(LAYOUT)
    return template.render(
        title=title,
        subtitle=subtitle,
        kind=kind.replace("_", " "),
        body=html_body,
        css=css,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Markdown to phone-friendly HTML.")
    parser.add_argument("input", type=Path, help="Markdown input file")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Output HTML file (default: stdout)")
    parser.add_argument("--show-kind", action="store_true", help="Print detected template kind to stderr and exit")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"File not found: {args.input}", file=sys.stderr)
        return 2

    if args.show_kind:
        text = args.input.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        print(detect_template(args.input, fm, body))
        return 0

    html = render(args.input)
    if args.output:
        args.output.write_text(html, encoding="utf-8")
        print(f"Wrote {args.output} ({len(html)} bytes)", file=sys.stderr)
    else:
        sys.stdout.write(html)
    return 0


if __name__ == "__main__":
    sys.exit(main())
