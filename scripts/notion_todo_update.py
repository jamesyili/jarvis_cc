#!/usr/bin/env python3
"""Write operations on James's Notion to-do database (the /todo skill's pen).

Companion to notion_pull_todo.py (which reads). Runs on system python3 —
stdlib only. Config: ~/.config/leo/notion.json {"token", "database_id"}.

Usage:
    python3 scripts/notion_todo_update.py find TITLE
    python3 scripts/notion_todo_update.py add TITLE [--status STATUS] [--sub TEXT ...]
    python3 scripts/notion_todo_update.py add-sub PAGE TEXT [TEXT ...]
    python3 scripts/notion_todo_update.py check PAGE TEXT
    python3 scripts/notion_todo_update.py uncheck PAGE TEXT
    python3 scripts/notion_todo_update.py set-status PAGE STATUS
    python3 scripts/notion_todo_update.py archive PAGE

PAGE/TITLE args match case-insensitively on substring (a raw 32-hex/UUID page
id also works). STATUS matches the database's own options the same way, so
"this week" resolves to "0This Week". Ambiguous matches list candidates and
exit 1 instead of guessing. `archive` moves the page to Notion's trash
(recoverable in-app for 30 days).
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "leo" / "notion.json"
NOTION_VERSION = "2022-06-28"
MAX_DEPTH = 3  # match notion_pull_todo.py's sub-item depth

UUID_RE = re.compile(r"^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$", re.I)


def load_config():
    if not CONFIG_PATH.exists():
        sys.exit(f"No Notion config at {CONFIG_PATH} — see notion_pull_todo.py header.")
    cfg = json.loads(CONFIG_PATH.read_text())
    missing = [k for k in ("token", "database_id") if not cfg.get(k)]
    if missing:
        sys.exit(f"Config {CONFIG_PATH} missing keys: {missing}")
    return cfg


def api(token, path, method="GET", body=None):
    """One Notion API call with 429 retry."""
    for attempt in range(3):
        req = urllib.request.Request(
            f"https://api.notion.com/v1/{path}",
            data=json.dumps(body).encode() if body is not None else None,
            headers={
                "Authorization": f"Bearer {token}",
                "Notion-Version": NOTION_VERSION,
                "Content-Type": "application/json",
            },
            method=method,
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                time.sleep(float(e.headers.get("Retry-After", 1)))
                continue
            sys.exit(f"Notion API error {e.code}: {e.read().decode(errors='replace')}")


def plain_text(rich):
    return "".join(part.get("plain_text", "") for part in rich)


def db_schema(token, database_id):
    """Return (title_prop_name, status_prop_name, status_type, [option names])."""
    db = api(token, f"databases/{database_id}")
    title_prop, status_prop, status_type, options = None, None, None, []
    for name, prop in db.get("properties", {}).items():
        if prop["type"] == "title":
            title_prop = name
        elif prop["type"] in ("status", "select"):
            status_prop, status_type = name, prop["type"]
            options = [o["name"] for o in prop[prop["type"]].get("options", [])]
    return title_prop, status_prop, status_type, options


def resolve_status(token, database_id, wanted):
    _, prop, ptype, options = db_schema(token, database_id)
    if not prop:
        sys.exit("Database has no status/select property.")
    exact = [o for o in options if o.lower() == wanted.lower()]
    fuzzy = [o for o in options if wanted.lower() in o.lower()]
    hits = exact or fuzzy
    if len(hits) != 1:
        sys.exit(f"Status {wanted!r} matched {hits or options} — be more specific.")
    return prop, ptype, hits[0]


def all_pages(token, database_id):
    cursor = None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        data = api(token, f"databases/{database_id}/query", "POST", body)
        yield from data.get("results", [])
        if not data.get("has_more"):
            return
        cursor = data.get("next_cursor")


def page_title(page):
    for prop in page.get("properties", {}).values():
        if prop["type"] == "title":
            return plain_text(prop["title"])
    return ""


def resolve_page(token, database_id, ref, include_archived=False):
    """Match a page by id or case-insensitive (sub)string; exit on ambiguity."""
    if UUID_RE.match(ref.replace("-", "")) and len(ref.replace("-", "")) == 32:
        return ref, "(by id)"
    matches = []
    for page in all_pages(token, database_id):
        if page.get("archived") and not include_archived:
            continue
        title = page_title(page)
        if ref.lower() in title.lower():
            matches.append((page["id"], title))
    exact = [m for m in matches if m[1].lower() == ref.lower()]
    if len(exact) == 1:
        return exact[0]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        sys.exit(f"No open item matches {ref!r}.")
    listing = "\n".join(f"  {i} | {t}" for i, t in matches)
    sys.exit(f"{ref!r} is ambiguous — {len(matches)} matches:\n{listing}")


def find_todo_blocks(token, block_id, needle, depth=1):
    """Yield (block_id, text, checked) for to_do blocks matching needle."""
    cursor = None
    while True:
        qs = f"?page_size=100" + (f"&start_cursor={cursor}" if cursor else "")
        data = api(token, f"blocks/{block_id}/children{qs}")
        for block in data.get("results", []):
            btype = block.get("type", "")
            payload = block.get(btype, {}) if isinstance(block.get(btype), dict) else {}
            if btype == "to_do":
                text = plain_text(payload.get("rich_text", []))
                if needle.lower() in text.lower():
                    yield block["id"], text, payload.get("checked", False)
            if block.get("has_children") and depth < MAX_DEPTH and btype not in ("child_page", "child_database"):
                yield from find_todo_blocks(token, block["id"], needle, depth + 1)
        if not data.get("has_more"):
            return
        cursor = data.get("next_cursor")


def todo_block(text):
    return {"object": "block", "type": "to_do",
            "to_do": {"rich_text": [{"type": "text", "text": {"content": text}}], "checked": False}}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("find").add_argument("title")

    p_add = sub.add_parser("add")
    p_add.add_argument("title")
    p_add.add_argument("--status", default="2Backlog")
    p_add.add_argument("--sub", action="append", default=[])

    p_addsub = sub.add_parser("add-sub")
    p_addsub.add_argument("page")
    p_addsub.add_argument("texts", nargs="+")

    for name in ("check", "uncheck"):
        p = sub.add_parser(name)
        p.add_argument("page")
        p.add_argument("text")

    p_status = sub.add_parser("set-status")
    p_status.add_argument("page")
    p_status.add_argument("status")

    sub.add_parser("archive").add_argument("page")

    args = ap.parse_args()
    cfg = load_config()
    token, db = cfg["token"], cfg["database_id"]

    if args.cmd == "find":
        pid, title = resolve_page(token, db, args.title)
        print(f"{pid} | {title}")

    elif args.cmd == "add":
        title_prop, _, _, _ = db_schema(token, db)
        sprop, stype, sname = resolve_status(token, db, args.status)
        body = {
            "parent": {"database_id": db},
            "properties": {
                title_prop: {"title": [{"type": "text", "text": {"content": args.title}}]},
                sprop: {stype: {"name": sname}},
            },
        }
        if args.sub:
            body["children"] = [
                {"object": "block", "type": "heading_1",
                 "heading_1": {"rich_text": [{"type": "text", "text": {"content": "To Do"}}]}},
                *[todo_block(t) for t in args.sub],
            ]
        page = api(token, "pages", "POST", body)
        print(f"added: {args.title!r} ({sname}) — {page['id']}")

    elif args.cmd == "add-sub":
        pid, title = resolve_page(token, db, args.page)
        api(token, f"blocks/{pid}/children", "PATCH",
            {"children": [todo_block(t) for t in args.texts]})
        print(f"added {len(args.texts)} sub-item(s) to {title!r}: " + "; ".join(args.texts))

    elif args.cmd in ("check", "uncheck"):
        pid, title = resolve_page(token, db, args.page)
        hits = list(find_todo_blocks(token, pid, args.text))
        if len(hits) != 1:
            listing = "\n".join(f"  [{'x' if c else ' '}] {t}" for _, t, c in hits)
            sys.exit(f"{args.text!r} matched {len(hits)} to-dos in {title!r}:\n{listing}" if hits
                     else f"No to-do matching {args.text!r} in {title!r}.")
        bid, text, _ = hits[0]
        api(token, f"blocks/{bid}", "PATCH", {"to_do": {"checked": args.cmd == "check"}})
        print(f"{args.cmd}ed in {title!r}: {text!r}")

    elif args.cmd == "set-status":
        pid, title = resolve_page(token, db, args.page)
        sprop, stype, sname = resolve_status(token, db, args.status)
        api(token, f"pages/{pid}", "PATCH", {"properties": {sprop: {stype: {"name": sname}}}})
        print(f"{title!r} -> {sname}")

    elif args.cmd == "archive":
        pid, title = resolve_page(token, db, args.page)
        api(token, f"pages/{pid}", "PATCH", {"archived": True})
        print(f"archived: {title!r} (recoverable in Notion trash)")


if __name__ == "__main__":
    main()
