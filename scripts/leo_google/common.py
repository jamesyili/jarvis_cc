"""Shared helpers: subject derivation, outbound-log append, MIME detection."""
from __future__ import annotations

import datetime as dt
import mimetypes
import re
from pathlib import Path

LEO_ROOT = Path(__file__).resolve().parents[2]  # leo/
OUTBOUND_LOG = LEO_ROOT / "system" / "outbound_log.md"

_LOG_HEADER = (
    "# Outbound Log\n\n"
    "| Timestamp | Kind | Summary | Files | Extra |\n"
    "|---|---|---|---|---|\n"
)

_MIME_OVERRIDES = {
    ".md": "text/markdown",
    ".yml": "text/yaml",
    ".yaml": "text/yaml",
}


def derive_subject(path: Path) -> str:
    """First H1 of the file, else Title-Cased filename. Prefixed with [Leo]."""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        title = m.group(1).strip()
    else:
        stem = path.stem.replace("_", " ").replace("-", " ")
        title = " ".join(w.capitalize() for w in stem.split())
    title = title[:80].rstrip()
    return f"[Leo] {title}"


def append_outbound_log(kind: str, summary: str, paths: list[Path], extra: str = "") -> None:
    """Append one row to system/outbound_log.md."""
    OUTBOUND_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not OUTBOUND_LOG.exists():
        OUTBOUND_LOG.write_text(_LOG_HEADER)
    ts = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    file_list = ", ".join(
        str(p.relative_to(LEO_ROOT)) if p.is_absolute() and LEO_ROOT in p.parents else str(p)
        for p in paths
    )
    row = f"| {ts} | {kind} | {summary} | {file_list} | {extra} |\n"
    with OUTBOUND_LOG.open("a", encoding="utf-8") as f:
        f.write(row)


def guess_mime(path: Path) -> str:
    if path.suffix.lower() in _MIME_OVERRIDES:
        return _MIME_OVERRIDES[path.suffix.lower()]
    mt, _ = mimetypes.guess_type(str(path))
    return mt or "application/octet-stream"


def human_size(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"
