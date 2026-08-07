#!/usr/bin/env python3
"""Pull James's to-do list from Notion as markdown (input for /plan-week).

Runs on system python3 — stdlib only, like the other repo scripts.

Config: ~/.config/leo/notion.json (mode 600), created manually:
    {"token": "ntn_...", "database_id": "<32-hex database id>"}

Setup (one-time, personal Notion workspace):
  1. notion.so/profile/integrations -> New integration (internal) -> copy token
  2. To-do database page -> ... -> Connections -> add the integration
  3. Database ID = the 32-hex segment in the database URL (before any ?v=)

Usage:
    python3 scripts/notion_pull_todo.py            # open items + their in-page sub-lists
    python3 scripts/notion_pull_todo.py --flat     # top-level items only (no page bodies)
    python3 scripts/notion_pull_todo.py --all      # include done/archived items
"""

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "leo" / "notion.json"
NOTION_VERSION = "2022-06-28"  # stable version; databases/query unchanged since
DONE_STATUSES = {"done", "completed", "complete", "archived", "canceled", "cancelled"}
MAX_DEPTH = 3            # page body -> nested sub-items
MAX_DETAIL_LINES = 40    # per item, so one huge page can't flood the output

SETUP_MSG = """\
No Notion config found at ~/.config/leo/notion.json — falling back is fine
(/plan-week accepts a screenshot or paste). To wire up the pull:

  1. notion.so/profile/integrations -> New integration (internal) -> copy token
  2. Open the to-do database -> ... -> Connections -> add the integration
  3. Database ID = the 32-hex segment in the database URL (before any ?v=)
  4. printf '{"token": "ntn_...", "database_id": "..."}' > ~/.config/leo/notion.json
     chmod 600 ~/.config/leo/notion.json
"""


def load_config():
    if not CONFIG_PATH.exists():
        print(SETUP_MSG, file=sys.stderr)
        sys.exit(2)
    cfg = json.loads(CONFIG_PATH.read_text())
    missing = [k for k in ("token", "database_id") if not cfg.get(k)]
    if missing:
        print(f"Config {CONFIG_PATH} missing keys: {missing}", file=sys.stderr)
        sys.exit(2)
    return cfg


def api_request(token, url, body=None):
    """One Notion API call (POST if body else GET), with 429 retry."""
    for attempt in range(3):
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode() if body is not None else None,
            headers={
                "Authorization": f"Bearer {token}",
                "Notion-Version": NOTION_VERSION,
                "Content-Type": "application/json",
            },
            method="POST" if body is not None else "GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                time.sleep(float(e.headers.get("Retry-After", 1)))
                continue
            detail = e.read().decode(errors="replace")
            print(f"Notion API error {e.code}: {detail}", file=sys.stderr)
            if e.code in (401, 403):
                print(
                    "Hint: token invalid, or the database was never shared with "
                    "the integration (••• -> Connections).",
                    file=sys.stderr,
                )
            elif e.code == 404:
                print(
                    "Hint: database_id wrong, or the integration lacks access.",
                    file=sys.stderr,
                )
            sys.exit(1)


def query_database(token, database_id):
    """Yield all pages in the database, following pagination."""
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    cursor = None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        data = api_request(token, url, body)
        yield from data.get("results", [])
        if not data.get("has_more"):
            return
        cursor = data.get("next_cursor")


def plain_text(rich):
    return "".join(part.get("plain_text", "") for part in rich)


def extract(page):
    """Pull title / status / due date / done-checkbox from arbitrary props."""
    title, status, due, checked = "", None, None, None
    for prop in page.get("properties", {}).values():
        ptype = prop.get("type")
        if ptype == "title":
            title = plain_text(prop["title"])
        elif ptype in ("status", "select") and prop.get(ptype):
            status = prop[ptype].get("name")
        elif ptype == "date" and prop.get("date"):
            due = prop["date"].get("start")
        elif ptype == "checkbox":
            checked = prop["checkbox"]
    return title, status, due, checked


def block_children(token, block_id):
    """Yield all child blocks, following pagination."""
    base = f"https://api.notion.com/v1/blocks/{block_id}/children"
    cursor = None
    while True:
        qs = {"page_size": 100}
        if cursor:
            qs["start_cursor"] = cursor
        data = api_request(token, f"{base}?{urllib.parse.urlencode(qs)}")
        yield from data.get("results", [])
        if not data.get("has_more"):
            return
        cursor = data.get("next_cursor")


def render_blocks(token, block_id, depth=1):
    """Render a page/block's children as indented markdown lines."""
    lines = []
    for block in block_children(token, block_id):
        btype = block.get("type", "")
        payload = block.get(btype, {}) if isinstance(block.get(btype), dict) else {}
        text = plain_text(payload.get("rich_text", []))
        indent = "  " * depth
        if btype == "to_do":
            box = "x" if payload.get("checked") else " "
            lines.append(f"{indent}- [{box}] {text}")
        elif btype in ("bulleted_list_item", "numbered_list_item", "toggle"):
            lines.append(f"{indent}- {text}")
        elif btype.startswith("heading_") and text:
            lines.append(f"{indent}**{text}**")
        elif btype == "paragraph" and text.strip():
            lines.append(f"{indent}· {text}")
        elif btype in ("child_page", "child_database"):
            title = payload.get("title", "")
            lines.append(f"{indent}- ({btype.replace('_', ' ')}: {title})")
            continue  # never descend into child pages/databases
        if (
            block.get("has_children")
            and depth < MAX_DEPTH
            and btype not in ("child_page", "child_database")
        ):
            lines.extend(render_blocks(token, block["id"], depth + 1))
    return lines


def main():
    include_done = "--all" in sys.argv
    flat = "--flat" in sys.argv
    cfg = load_config()
    token = cfg["token"]
    items, skipped = [], 0
    for page in query_database(token, cfg["database_id"]):
        title, status, due, checked = extract(page)
        if not title:
            continue
        is_done = checked is True or (status or "").strip().lower() in DONE_STATUSES
        if is_done and not include_done:
            skipped += 1
            continue
        box = "x" if is_done else " "
        meta = " · ".join(m for m in (status, f"due {due}" if due else None) if m)
        items.append((f"- [{box}] {title}" + (f"  ({meta})" if meta else ""), page["id"]))

    print("# To-do (Notion pull)")
    print()
    if not items:
        print("(no open items returned)")
    for line, page_id in items:
        print(line)
        if flat:
            continue
        detail = render_blocks(token, page_id)
        if len(detail) > MAX_DETAIL_LINES:
            hidden = len(detail) - MAX_DETAIL_LINES
            detail = detail[:MAX_DETAIL_LINES] + [f"  … (+{hidden} more lines in Notion)"]
        for d in detail:
            print(d)
    if skipped and not include_done:
        print(f"\n_{skipped} done/archived item(s) hidden — rerun with --all to see._")


if __name__ == "__main__":
    main()
