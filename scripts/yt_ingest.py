#!/usr/bin/env python3
"""
YouTube transcript extraction and KB ingestion pipeline.

Extracts transcripts from YouTube videos and ingests them as KB articles.
Supports batch processing from a video backlog file.

Usage:
    python scripts/yt_ingest.py                    # Process all unprocessed videos
    python scripts/yt_ingest.py --video VIDEO_ID   # Single video by ID
    python scripts/yt_ingest.py --status            # Show progress
    python scripts/yt_ingest.py --retry             # Retry rate-limited errors
    python scripts/yt_ingest.py --dry-run           # Preview without writing
"""

import json
import re
import sys
import time
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_index import build_raw_index

BASE_DIR = Path(__file__).parent.parent
KB_DIR = BASE_DIR / "kb"
BACKLOG_FILE = BASE_DIR / "scripts" / "yt_backlog.json"
MANIFEST_FILE = KB_DIR / ".yt_manifest.json"

# Rate limit handling
INITIAL_DELAY = 5        # seconds between requests
RATE_LIMIT_WAIT = 300    # 5 min backoff on rate limit
MAX_RETRIES = 3          # retries per video on rate limit


def load_backlog():
    if not BACKLOG_FILE.exists():
        print(f"ERROR: Backlog file not found: {BACKLOG_FILE}")
        sys.exit(1)
    with open(BACKLOG_FILE) as f:
        return json.load(f)


def load_manifest():
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE) as f:
            return json.load(f)
    return {}


def save_manifest(manifest):
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2, sort_keys=True)


def is_rate_limited(error_str):
    """Check if an error is a rate limit / IP block (retryable)."""
    return any(k in error_str.lower() for k in ["blocking requests", "ip", "too many requests"])


def is_permanent_error(error_str):
    """Check if an error is permanent (subtitles disabled, etc.)."""
    return any(k in error_str.lower() for k in ["subtitles are disabled", "no subtitles"])


def extract_transcript(video_id):
    """Extract transcript from a YouTube video. Returns (text, language) or raises."""
    from youtube_transcript_api import YouTubeTranscriptApi

    api = YouTubeTranscriptApi()

    try:
        transcript = api.fetch(video_id, languages=["en"])
    except Exception:
        try:
            transcript = api.fetch(video_id)
        except Exception as e:
            raise RuntimeError(str(e))

    snippets = list(transcript)
    if not snippets:
        raise RuntimeError(f"Empty transcript for {video_id}")

    # Join with paragraph breaks every ~60 seconds for readability
    paragraphs = []
    current_para = []
    last_break = 0

    for s in snippets:
        current_para.append(s.text)
        if s.start - last_break >= 60:
            paragraphs.append(" ".join(current_para))
            current_para = []
            last_break = s.start

    if current_para:
        paragraphs.append(" ".join(current_para))

    text = "\n\n".join(paragraphs)
    lang = transcript.language if hasattr(transcript, "language") else "en"
    return text, lang


def slugify(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


def format_article(video, transcript_text):
    url = f"https://www.youtube.com/watch?v={video['id']}"
    tags_str = ", ".join(video.get("tags", []))
    duration = video.get("duration", "unknown")

    return f"""# {video['title']}

**Source:** {url}
**Channel:** {video['channel']}
**Type:** YouTube transcript
**Duration:** {duration}
**Ingested:** {date.today().isoformat()}
**Tags:** {tags_str}

---

{transcript_text}
"""


def ingest_video(video, manifest, dry_run=False):
    """Extract transcript and write KB article. Returns 'ingested', 'rate_limited', 'error', or 'skip'."""
    vid = video["id"]
    title = video["title"]

    if vid in manifest and manifest[vid].get("status") == "ingested":
        return "skip"

    print(f"  Extracting: {title} ({vid})...")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            text, lang = extract_transcript(vid)
            break
        except RuntimeError as e:
            error_str = str(e)
            if is_permanent_error(error_str):
                print(f"  PERMANENT ERROR: {title} — subtitles disabled")
                manifest[vid] = {"status": "no_subtitles", "date": date.today().isoformat()}
                return "error"
            elif is_rate_limited(error_str):
                if attempt < MAX_RETRIES:
                    wait = RATE_LIMIT_WAIT * attempt
                    print(f"  Rate limited (attempt {attempt}/{MAX_RETRIES}). Waiting {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"  Rate limited after {MAX_RETRIES} retries. Stopping batch.")
                    manifest[vid] = {"status": "rate_limited", "date": date.today().isoformat()}
                    return "rate_limited"
            else:
                print(f"  ERROR: {error_str}")
                manifest[vid] = {"status": "error", "error": error_str, "date": date.today().isoformat()}
                return "error"

    # Route to correct KB domain/source dir
    domain = video.get("domain", "hard")
    source = video.get("source_dir", "youtube")
    out_dir = KB_DIR / domain / "raw" / source
    out_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(title)
    out_file = out_dir / f"{slug}.md"
    article = format_article(video, text)

    if dry_run:
        print(f"  WOULD WRITE: {out_file} ({len(text)} chars)")
        return "ingested"

    out_file.write_text(article)
    print(f"  WROTE: {out_file} ({len(text)} chars)")

    manifest[vid] = {
        "status": "ingested",
        "title": title,
        "file": str(out_file.relative_to(BASE_DIR)),
        "chars": len(text),
        "date": date.today().isoformat(),
    }
    return "ingested"


def process_all(dry_run=False, retry=False):
    """Process all videos in the backlog."""
    backlog = load_backlog()
    manifest = load_manifest()

    # If --retry, clear rate_limited entries so they get re-attempted
    if retry:
        cleared = 0
        for vid, info in list(manifest.items()):
            if info.get("status") in ("rate_limited", "error") and not is_permanent_error(info.get("error", "")):
                del manifest[vid]
                cleared += 1
        if cleared:
            print(f"Cleared {cleared} retryable errors from manifest.\n")
            save_manifest(manifest)

    total = len(backlog)
    done = sum(1 for v in backlog if v["id"] in manifest and manifest[v["id"]].get("status") == "ingested")
    perm_errors = sum(1 for v in backlog if v["id"] in manifest and manifest[v["id"]].get("status") == "no_subtitles")
    pending = total - done - perm_errors

    print(f"YouTube ingest: {done}/{total} done, {perm_errors} no-subtitles, {pending} pending\n")

    ingested = 0
    for video in backlog:
        vid = video["id"]
        status = manifest.get(vid, {}).get("status")
        if status in ("ingested", "no_subtitles"):
            continue

        result = ingest_video(video, manifest, dry_run=dry_run)
        save_manifest(manifest)

        if result == "ingested":
            ingested += 1
        elif result == "rate_limited":
            # Stop the whole batch — no point hammering a blocked IP
            print("\nStopping batch due to rate limiting. Run with --retry later.")
            break

        time.sleep(INITIAL_DELAY)

    print(f"\nDone. Ingested {ingested} new transcripts.")

    if not dry_run and ingested > 0:
        print("Rebuilding search index...")
        build_raw_index()

    return ingested


def show_status():
    backlog = load_backlog()
    manifest = load_manifest()

    total = len(backlog)
    done = sum(1 for v in backlog if v["id"] in manifest and manifest[v["id"]].get("status") == "ingested")
    errors = sum(1 for v in backlog if v["id"] in manifest and manifest[v["id"]].get("status") in ("error", "no_subtitles", "rate_limited"))

    print(f"YouTube ingest status: {done}/{total} ingested, {errors} errors\n")

    for video in backlog:
        vid = video["id"]
        info = manifest.get(vid, {})
        status = info.get("status", "pending")
        chars = info.get("chars", "")
        char_str = f" ({chars} chars)" if chars else ""
        icons = {"ingested": "OK", "error": "ERR", "no_subtitles": "N/A", "rate_limited": "WAIT", "pending": "..."}
        icon = icons.get(status, "?")
        print(f"  [{icon}] {video['title']}{char_str}")


def ingest_single(video_id, dry_run=False):
    backlog = load_backlog()
    manifest = load_manifest()

    video = next((v for v in backlog if v["id"] == video_id), None)
    if not video:
        print(f"ERROR: Video ID {video_id} not found in backlog")
        sys.exit(1)

    ingest_video(video, manifest, dry_run=dry_run)
    save_manifest(manifest)

    if not dry_run:
        print("Rebuilding search index...")
        build_raw_index()


if __name__ == "__main__":
    if "--status" in sys.argv:
        show_status()
    elif "--video" in sys.argv:
        idx = sys.argv.index("--video")
        vid = sys.argv[idx + 1]
        ingest_single(vid, dry_run="--dry-run" in sys.argv)
    else:
        process_all(
            dry_run="--dry-run" in sys.argv,
            retry="--retry" in sys.argv,
        )
