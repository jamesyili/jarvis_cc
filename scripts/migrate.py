#!/usr/bin/env python3
"""
One-time migration: learning/ → kb/

Usage:
    python scripts/migrate.py              # Execute migration
    python scripts/migrate.py --dry-run    # Preview only
    python scripts/migrate.py --verify     # Post-migration verification
"""
import json
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent
LEARNING = BASE / "learning"
KB = BASE / "kb"

HARD_SLUGS = [
    "aman-ai", "chip-huyen", "eugene-yan", "lilian-weng", "karpathy",
    "cameron-wolfe", "sebastian-raschka", "nathan-lambert", "simon-willison", "jay-alammar",
]
SOFT_SLUGS = ["wes-kao", "jefferson-fisher"]


def copy_file(src, dst, dry_run):
    if dry_run:
        print(f"  {src} → {dst}")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def copy_dir(src, dst, pattern, dry_run):
    """Copy all files matching pattern from src to dst. Returns count."""
    if not src.exists():
        return 0
    count = 0
    for f in sorted(src.glob(pattern)):
        if f.is_file():
            copy_file(f, dst / f.name, dry_run)
            count += 1
    return count


def migrate(dry_run=False):
    stats = {}
    label = "[DRY RUN] " if dry_run else ""
    print(f"{label}Migrating learning/ → kb/\n")

    # 1. Hard skills sources
    print("=== Hard Skills ===")
    for slug in HARD_SLUGS:
        src = LEARNING / "articles" / slug
        dst = KB / "hard" / "raw" / slug
        count = copy_dir(src, dst, "*", dry_run)
        stats[f"hard/raw/{slug}"] = count
        print(f"  {slug}: {count} files")

    # 2. Soft skills: wes-kao, jefferson-fisher
    print("\n=== Soft Skills ===")
    for slug in SOFT_SLUGS:
        src = LEARNING / "articles" / slug
        dst = KB / "soft" / "raw" / slug
        count = copy_dir(src, dst, "*", dry_run)
        stats[f"soft/raw/{slug}"] = count
        print(f"  {slug}: {count} files")

    # 3. Ethan Evans: .md → raw/ethan-evans/, .txt → raw/do_not_index_sources/ethan-evans/
    ee_src = LEARNING / "articles" / "ethan-evans"
    md_count = 0
    txt_count = 0
    if ee_src.exists():
        for f in sorted(ee_src.iterdir()):
            if not f.is_file():
                continue
            if f.suffix == ".md":
                copy_file(f, KB / "soft" / "raw" / "ethan-evans" / f.name, dry_run)
                md_count += 1
            elif f.suffix == ".txt":
                copy_file(f, KB / "soft" / "raw" / "do_not_index_sources" / "ethan-evans" / f.name, dry_run)
                txt_count += 1
    stats["soft/raw/ethan-evans"] = md_count
    stats["soft/raw/do_not_index_sources/ethan-evans"] = txt_count
    print(f"  ethan-evans: {md_count} articles, {txt_count} source files")

    # 4. Lenny full transcripts → do_not_index_sources/
    print("\n=== Lenny Transcripts → do_not_index_sources/ ===")
    lenny_src = LEARNING / "articles" / "lennys-podcast"
    lenny_dst = KB / "soft" / "raw" / "do_not_index_sources" / "lennys-podcast"
    count = copy_dir(lenny_src, lenny_dst, "*.md", dry_run)
    stats["soft/raw/do_not_index_sources/lennys-podcast"] = count
    print(f"  transcripts: {count} files")

    # 5. Theme extractions → kb/soft/raw/lennys-podcast/
    print("\n=== Theme Extractions → lennys-podcast/ ===")
    themes_src = LEARNING / "themes"
    lenny_raw_dst = KB / "soft" / "raw" / "lennys-podcast"
    theme_count = 0
    if themes_src.exists():
        for theme_dir in sorted(themes_src.iterdir()):
            if not theme_dir.is_dir() or theme_dir.name.startswith("_"):
                continue
            for f in sorted(theme_dir.glob("*.md")):
                dst_name = f"{theme_dir.name}--{f.name}"
                copy_file(f, lenny_raw_dst / dst_name, dry_run)
                theme_count += 1
    stats["soft/raw/lennys-podcast (themes)"] = theme_count
    print(f"  theme extractions: {theme_count} files")

    # 6. Copy and update manifests
    print("\n=== Manifests ===")
    manifest_src = LEARNING / ".ingested_manifest.json"
    if manifest_src.exists():
        if dry_run:
            print(f"  Would copy manifest to kb/.ingested_manifest.json")
        else:
            shutil.copy2(manifest_src, KB / ".ingested_manifest.json")
            print(f"  Copied ingested manifest")

    themes_manifest = LEARNING / ".themes_manifest.json"
    if themes_manifest.exists():
        if dry_run:
            print(f"  Would copy themes manifest to kb/.themes_manifest.json")
        else:
            shutil.copy2(themes_manifest, KB / ".themes_manifest.json")
            print(f"  Copied themes manifest")

    # Summary
    total = sum(stats.values())
    print(f"\n{'=' * 40}")
    print(f"{'[DRY RUN] ' if dry_run else ''}Total: {total} files")
    for location, count in stats.items():
        if count > 0:
            print(f"  {location}: {count}")


def verify():
    """Post-migration verification: check all source files have targets."""
    print("Verifying migration...\n")
    issues = []

    # Check hard skills
    for slug in HARD_SLUGS:
        src = LEARNING / "articles" / slug
        dst = KB / "hard" / "raw" / slug
        if src.exists():
            for f in src.glob("*"):
                if f.is_file() and not (dst / f.name).exists():
                    issues.append(f"MISSING: {f} → {dst / f.name}")

    # Check soft skills
    for slug in SOFT_SLUGS:
        src = LEARNING / "articles" / slug
        dst = KB / "soft" / "raw" / slug
        if src.exists():
            for f in src.glob("*"):
                if f.is_file() and not (dst / f.name).exists():
                    issues.append(f"MISSING: {f} → {dst / f.name}")

    # Check ethan-evans
    ee_src = LEARNING / "articles" / "ethan-evans"
    if ee_src.exists():
        for f in ee_src.iterdir():
            if not f.is_file():
                continue
            if f.suffix == ".md":
                target = KB / "soft" / "raw" / "ethan-evans" / f.name
            elif f.suffix == ".txt":
                target = KB / "soft" / "raw" / "do_not_index_sources" / "ethan-evans" / f.name
            else:
                continue
            if not target.exists():
                issues.append(f"MISSING: {f} → {target}")

    # Check lenny transcripts
    lenny_src = LEARNING / "articles" / "lennys-podcast"
    lenny_dst = KB / "soft" / "raw" / "do_not_index_sources" / "lennys-podcast"
    if lenny_src.exists():
        for f in lenny_src.glob("*.md"):
            if not (lenny_dst / f.name).exists():
                issues.append(f"MISSING: {f} → {lenny_dst / f.name}")

    # Check theme extractions
    themes_src = LEARNING / "themes"
    lenny_raw_dst = KB / "soft" / "raw" / "lennys-podcast"
    if themes_src.exists():
        for theme_dir in themes_src.iterdir():
            if not theme_dir.is_dir() or theme_dir.name.startswith("_"):
                continue
            for f in theme_dir.glob("*.md"):
                dst_name = f"{theme_dir.name}--{f.name}"
                if not (lenny_raw_dst / dst_name).exists():
                    issues.append(f"MISSING: {f} → {lenny_raw_dst / dst_name}")

    if issues:
        print(f"FAILED: {len(issues)} missing files")
        for issue in issues[:20]:
            print(f"  {issue}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more")
        return False
    else:
        # Count totals
        hard_count = sum(1 for _ in (KB / "hard" / "raw").rglob("*.md") if "do_not_index_sources" not in str(_) and _.name != "_index.md")
        soft_count = sum(1 for _ in (KB / "soft" / "raw").rglob("*.md") if "do_not_index_sources" not in str(_) and _.name != "_index.md")
        sources_count = sum(1 for _ in (KB / "hard" / "raw" / "do_not_index_sources").rglob("*") if _.is_file()) + \
                        sum(1 for _ in (KB / "soft" / "raw" / "do_not_index_sources").rglob("*") if _.is_file())
        print(f"OK: All files migrated successfully")
        print(f"  Hard skills raw: {hard_count} articles")
        print(f"  Soft skills raw: {soft_count} articles")
        print(f"  Sources (archive): {sources_count} files")
        return True


def main():
    if "--dry-run" in sys.argv:
        migrate(dry_run=True)
    elif "--verify" in sys.argv:
        verify()
    else:
        migrate(dry_run=False)


if __name__ == "__main__":
    main()
