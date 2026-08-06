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
    python3 scripts/notion_pull_todo.py            # open items only
    python3 scripts/notion_pull_todo.py --all      # include done/archived
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "leo" / "notion.json"
NOTION_VERSION = "2022-06-28"  # stable version; databases/query unchanged since
DONE_STATUSES = {"done", "completed", "complete", "archived", "canceled", "cancelled"}

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


def query_database(token, database_id):
    """Yield all pages in the database, following pagination."""
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    cursor = None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode(),
            headers={
                "Authorization": f"Bearer {token}",
                "Notion-Version": NOTION_VERSION,
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.load(resp)
        except urllib.error.HTTPError as e:
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


def main():
    include_done = "--all" in sys.argv
    cfg = load_config()
    lines, skipped = [], 0
    for page in query_database(cfg["token"], cfg["database_id"]):
        title, status, due, checked = extract(page)
        if not title:
            continue
        is_done = checked is True or (status or "").strip().lower() in DONE_STATUSES
        if is_done and not include_done:
            skipped += 1
            continue
        box = "x" if is_done else " "
        meta = " · ".join(m for m in (status, f"due {due}" if due else None) if m)
        lines.append(f"- [{box}] {title}" + (f"  ({meta})" if meta else ""))
    print("# To-do (Notion pull)")
    print()
    if lines:
        print("\n".join(lines))
    else:
        print("(no open items returned)")
    if skipped and not include_done:
        print(f"\n_{skipped} done/archived item(s) hidden — rerun with --all to see._")


if __name__ == "__main__":
    main()
