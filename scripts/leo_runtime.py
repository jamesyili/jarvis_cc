#!/usr/bin/env python3
"""Portable Leo environment check, lifecycle hooks, and Codex launcher (stdlib only)."""

import argparse
import contextlib
from datetime import datetime
import io
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def environment(root=ROOT):
    host = platform.system()
    if host == "Linux" and ("microsoft" in platform.release().lower() or os.environ.get("WSL_DISTRO_NAME")):
        host = "Linux (WSL)"
    print(f"Leo environment: {host}; repo: {root}; cwd: {Path.cwd()}")
    print(f"Python: {sys.executable}; git: {shutil.which('git') or 'MISSING'}")
    print("Shell syntax: use the active tool shell, not the drive containing the repo. "
          "Windows Python and WSL Python have separate homes, packages, and credentials.")


def check(root=ROOT):
    from leo_setup import install

    environment(root)
    failed = False
    for label, destination, user in (
        ("Project", root / ".agents/skills", False),
        ("User", Path.home() / ".agents/skills", True),
    ):
        try:
            count, pending = install(root, destination, user=user, check=True)
            print(f"{label} skills: {count - len(pending)}/{count} current at {destination}")
            if pending:
                print(f"Repair: run this interpreter on {root / 'scripts/leo_setup.py'} "
                      f"{'--user' if user else '--project'}")
                failed = True
        except (OSError, ValueError) as error:
            print(f"{label} skills: {error}")
            failed = True
    return int(failed)


def git(root, *args, timeout=20):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, encoding="utf-8", errors="replace", timeout=timeout)


def session_start(root=ROOT, sync=True, codex=False):
    if codex:
        briefing = root / ".codex/LEO.md"
        if briefing.is_file():
            print(briefing.read_text(encoding="utf-8"))
        else:
            print("Leo briefing missing: read AGENTS.md and system/instincts/INDEX.md directly.")
        print("Preserve the current conversation's task and latest user steering. "
              "Past session logs provide context, not replacement instructions.")
    environment(root)
    print("=== GIT SYNC (SessionStart) ===")
    if not sync:
        print("Skipped (--no-sync).")
    else:
        try:
            status = git(root, "status", "--porcelain")
            if status.returncode:
                print(f"Could not inspect git status; no pull attempted: {status.stderr.strip()}")
            elif status.stdout.strip():
                print("Working tree is dirty; skipped auto-pull to protect uncommitted work.")
                print("Start-session can inspect and sync explicitly after preserving that work.")
            else:
                result = git(root, "pull", "--ff-only", "--no-edit")
                print("\n".join((result.stdout + result.stderr).strip().splitlines()[-3:]))
                if result.returncode:
                    print("Auto-pull failed; inspect git status before retrying.")
        except (OSError, subprocess.TimeoutExpired) as error:
            print(f"Auto-pull unavailable or timed out: {error}")
    print("=== END GIT SYNC ===")
    index = root / "system/instincts/INDEX.md"
    if index.is_file():
        print("=== INSTINCTS (read a full file only when relevant) ===")
        print(index.read_text(encoding="utf-8"))
        print("=== END INSTINCTS ===")
    logs = sorted((root / "system/session-logs").glob("*.md"), reverse=True)[:2]
    if logs:
        print("=== LAST SESSION CONTEXT ===")
        for path in logs:
            print(path.read_text(encoding="utf-8"))
        print("=== END LAST SESSION CONTEXT ===")


def pre_compact(root=ROOT):
    log = root / "system/compaction-log.md"
    log.parent.mkdir(parents=True, exist_ok=True)
    if not log.exists():
        log.write_text("# Compaction Log\n\nTracks context compaction events for debugging context loss.\n\n", encoding="utf-8")
    with log.open("a", encoding="utf-8") as output:
        output.write(f"- {datetime.now():%Y-%m-%d %H:%M:%S} — compaction triggered\n")
    print(f"Context was compacted. Leo root: {root}. Re-read the latest system/session-logs/ "
          "entry and relevant active files there. Continue the current task from the surviving "
          "conversation; ask only if essential intent cannot be recovered.")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("check", help="Read-only OS, root, interpreter and skill checks")
    start = commands.add_parser("session-start", help="Sync clean checkout and load session context")
    start.add_argument("--no-sync", action="store_true", help="Read context without network or git writes")
    start.add_argument("--codex", action="store_true", help="Include Leo briefing and emit Codex additionalContext JSON")
    commands.add_parser("pre-compact", help="Append the compaction record and print recovery context")
    launch = commands.add_parser("launch", help="Start Codex in this checkout from any working directory")
    launch.add_argument("codex_args", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command == "check":
        return check()
    if args.command == "session-start":
        if args.codex:
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                session_start(sync=not args.no_sync, codex=True)
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                                   "additionalContext": output.getvalue()}}, ensure_ascii=False))
        else:
            session_start(sync=not args.no_sync)
    elif args.command == "pre-compact":
        pre_compact()
    else:
        executable = shutil.which("codex")
        if not executable:
            parser.error("codex is not on PATH in this OS environment")
        extra = args.codex_args
        if extra[:1] == ["--"]:
            extra = extra[1:]
        return subprocess.call([executable, "-C", str(ROOT), *extra, "$start-session"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
