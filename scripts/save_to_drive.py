#!/usr/bin/env python3
"""save_to_drive.py — Upload files to James's "Leo Outbox" in Drive.

.md files convert to Google Docs by default (override with --raw).
Other files upload as-is. Logs to system/outbound_log.md.

Usage:
    save_to_drive.py <path> [<path> ...] [--folder NAME] [--raw]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from leo_google.common import append_outbound_log  # noqa: E402
from leo_google.drive_upload import upload  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Upload files to James's 'Leo Outbox' folder in Drive."
    )
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--folder", default="Leo Outbox")
    ap.add_argument(
        "--raw",
        action="store_true",
        help="Upload .md as raw markdown (no Google Doc conversion).",
    )
    args = ap.parse_args()

    paths = [p.resolve() for p in args.paths]
    for p in paths:
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            return 2

    results: list[tuple[Path, str]] = []
    for p in paths:
        try:
            _file_id, link = upload(
                p, convert_md=not args.raw, folder_name=args.folder
            )
        except Exception as e:
            print(f"Drive upload failed for {p}: {e}", file=sys.stderr)
            return 1
        print(f"Uploaded. {p.name} → {link}")
        results.append((p, link))

    summary = f"Uploaded {len(results)} file(s) to {args.folder}"
    extra = "; ".join(link for _, link in results)
    append_outbound_log("drive", summary, [p for p, _ in results], extra=extra)
    return 0


if __name__ == "__main__":
    sys.exit(main())
