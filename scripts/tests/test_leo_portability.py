"""Run with python -m unittest discover -s scripts/tests -p test_leo_portability.py."""

import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import leo_runtime
import leo_setup


class PortabilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="leo portability ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "relocated repo with spaces"
        self.root.mkdir()
        skill = self.root / ".claude/skills/start-session/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("---\nname: start-session\ndescription: >\n  Start Leo\n  from any folder.\n---\n\nCanonical workflow.\n", encoding="utf-8")
        self.destination = Path(self.temp.name) / "user home/.agents/skills"

    def test_user_install_is_idempotent_and_preserves_unrelated_skills(self):
        other = self.destination / "other/SKILL.md"
        other.parent.mkdir(parents=True)
        other.write_text("User-authored content", encoding="utf-8")
        count, changed = leo_setup.install(self.root, self.destination, user=True)
        self.assertEqual((count, len(changed)), (1, 1))
        installed = self.destination / "start-session/SKILL.md"
        self.assertIn(self.root.as_posix(), installed.read_text(encoding="utf-8"))
        self.assertEqual(leo_setup.skill_metadata(installed)["description"], "Start Leo from any folder.")
        self.assertEqual(leo_setup.install(self.root, self.destination, user=True)[1], [])
        self.assertEqual(other.read_text(encoding="utf-8"), "User-authored content")

    def test_conflicting_skill_prevents_all_writes(self):
        conflict = self.destination / "start-session/SKILL.md"
        conflict.parent.mkdir(parents=True)
        conflict.write_text("My own start-session", encoding="utf-8")
        earlier = self.root / ".claude/skills/aaa/SKILL.md"
        earlier.parent.mkdir()
        earlier.write_text("---\nname: aaa\ndescription: Earlier skill.\n---\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "preserved"):
            leo_setup.install(self.root, self.destination, user=True)
        self.assertFalse((self.destination / "aaa").exists())
        self.assertEqual(conflict.read_text(), "My own start-session")

    def test_check_never_writes(self):
        self.assertEqual(len(leo_setup.install(self.root, self.destination, user=True, check=True)[1]), 1)
        self.assertFalse(self.destination.exists())

    def test_discovery_description_is_bounded_without_editing_canonical(self):
        canonical = self.root / ".claude/skills/start-session/SKILL.md"
        content = "---\nname: start-session\ndescription: " + "Long description. " * 100 + "\n---\n"
        canonical.write_text(content, encoding="utf-8")
        leo_setup.install(self.root, self.destination, user=True)
        metadata = leo_setup.skill_metadata(self.destination / "start-session/SKILL.md")
        self.assertLessEqual(len(metadata["description"]), 1024)
        self.assertEqual(canonical.read_text(encoding="utf-8"), content)

    def test_windows_git_symlink_stub_is_replaced_without_copying_body(self):
        destination = self.root / ".agents/skills"
        destination.parent.mkdir()
        destination.write_text("../.claude/skills", encoding="utf-8")
        leo_setup.install(self.root, destination)
        content = (destination / "start-session/SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("Canonical workflow.", content)
        self.assertTrue((self.root / ".claude/skills/start-session/SKILL.md").is_file())
        self.assertEqual(leo_setup.install(self.root, destination, check=True)[1], [])

    @unittest.skipIf(os.name == "nt", "Windows symlink privileges are not needed by this installer")
    def test_linux_symlink_is_replaced_without_following_it_for_writes(self):
        destination = self.root / ".agents/skills"
        destination.parent.mkdir()
        destination.symlink_to("../.claude/skills", target_is_directory=True)
        leo_setup.install(self.root, destination)
        self.assertFalse(destination.is_symlink())
        self.assertIn("Canonical workflow.", (self.root / ".claude/skills/start-session/SKILL.md").read_text())

    def test_legacy_lowercase_without_metadata_is_skipped(self):
        directory = self.root / ".claude/skills/legacy"
        directory.mkdir()
        (directory / "skill.md").write_text("# Legacy workflow", encoding="utf-8")
        self.assertEqual(len(list(leo_setup.canonical_skills(self.root))), 1)

    def test_no_sync_reads_latest_two_logs_from_relocated_root(self):
        logs = self.root / "system/session-logs"
        logs.mkdir(parents=True)
        for name in ("2026-09-04", "2026-09-05", "2026-09-05b"):
            (logs / f"{name}.md").write_text(f"LOG {name}", encoding="utf-8")
        output = io.StringIO()
        with contextlib.redirect_stdout(output), patch.object(leo_runtime, "git") as git:
            leo_runtime.session_start(self.root, sync=False)
        git.assert_not_called()
        self.assertIn("LOG 2026-09-05b", output.getvalue())
        self.assertIn("LOG 2026-09-05", output.getvalue())
        self.assertNotIn("LOG 2026-09-04", output.getvalue())

    def test_dirty_git_repository_is_never_pulled(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        output = io.StringIO()
        with contextlib.redirect_stdout(output), patch.object(leo_runtime, "git", wraps=leo_runtime.git) as git:
            leo_runtime.session_start(self.root)
        self.assertIn("dirty", output.getvalue())
        self.assertEqual(git.call_count, 1)

    def test_clean_pull_keeps_ff_only_and_timeout(self):
        status = subprocess.CompletedProcess([], 0, "", "")
        with contextlib.redirect_stdout(io.StringIO()), patch.object(leo_runtime, "git", side_effect=[status, status]) as git:
            leo_runtime.session_start(self.root)
        self.assertEqual(git.call_args.args, (self.root, "pull", "--ff-only", "--no-edit"))
        with patch.object(subprocess, "run", return_value=status) as run:
            leo_runtime.git(self.root, "pull", "--ff-only", "--no-edit")
        self.assertEqual(run.call_args.kwargs["timeout"], 20)

    def test_git_failure_still_loads_context(self):
        index = self.root / "system/instincts/INDEX.md"
        index.parent.mkdir(parents=True)
        index.write_text("MEMORY STILL LOADS", encoding="utf-8")
        output = io.StringIO()
        with contextlib.redirect_stdout(output), patch.object(leo_runtime, "git", side_effect=subprocess.TimeoutExpired("git", 20)):
            leo_runtime.session_start(self.root)
        self.assertIn("MEMORY STILL LOADS", output.getvalue())

    def test_precompact_uses_explicit_root_and_appends(self):
        with contextlib.redirect_stdout(io.StringIO()):
            leo_runtime.pre_compact(self.root)
            leo_runtime.pre_compact(self.root)
        content = (self.root / "system/compaction-log.md").read_text(encoding="utf-8")
        self.assertEqual(content.count("# Compaction Log"), 1)
        self.assertEqual(content.count("compaction triggered"), 2)

    def test_actual_script_from_unrelated_directory_and_moved_checkout(self):
        scripts = self.root / "scripts"
        scripts.mkdir()
        for name in ("leo_runtime.py", "leo_setup.py"):
            shutil.copy2(Path(leo_runtime.__file__).parent / name, scripts / name)
        unrelated = Path(self.temp.name) / "unrelated"
        unrelated.mkdir()
        result = subprocess.run([sys.executable, str(scripts / "leo_runtime.py"), "session-start", "--no-sync"],
                                cwd=unrelated, capture_output=True, text=True, encoding="utf-8", check=True)
        self.assertIn(str(self.root), result.stdout)
        self.assertFalse((unrelated / "system").exists())

    def test_codex_startup_delivers_briefing_and_full_memory_in_json(self):
        scripts = self.root / "scripts"
        scripts.mkdir()
        shutil.copy2(Path(leo_runtime.__file__), scripts / "leo_runtime.py")
        briefing = self.root / ".codex/LEO.md"
        briefing.parent.mkdir()
        briefing.write_text("LEO BRIEFING", encoding="utf-8")
        index = self.root / "system/instincts/INDEX.md"
        index.parent.mkdir(parents=True)
        memory = "Known campaign before questions.\n" * 1000 + "FINAL INSTINCT"
        index.write_text(memory, encoding="utf-8")
        result = subprocess.run([sys.executable, str(scripts / "leo_runtime.py"),
                                 "session-start", "--codex", "--no-sync"],
                                capture_output=True, text=True, encoding="utf-8", check=True)
        payload = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(payload["hookEventName"], "SessionStart")
        self.assertIn("LEO BRIEFING", payload["additionalContext"])
        self.assertIn(memory, payload["additionalContext"])
        self.assertIn("Skipped (--no-sync)", payload["additionalContext"])

    def test_postcompact_hook_has_no_sync_on_both_platforms(self):
        root = Path(leo_runtime.__file__).resolve().parents[1]
        hooks = json.loads((root / ".codex/hooks.json").read_text(encoding="utf-8"))
        compact = next(item for item in hooks["hooks"]["SessionStart"] if item["matcher"] == "compact")
        for key in ("command", "commandWindows"):
            self.assertIn("--no-sync", compact["hooks"][0][key])
            self.assertIn("--codex", compact["hooks"][0][key])

    def test_launcher_preserves_spaces_and_sets_explicit_root(self):
        with patch.object(sys, "argv", ["leo_runtime.py", "launch", "--", "--no-alt-screen"]), \
                patch.object(leo_runtime.shutil, "which", return_value="codex"), \
                patch.object(leo_runtime, "ROOT", self.root), \
                patch.object(subprocess, "call", return_value=0) as call:
            self.assertEqual(leo_runtime.main(), 0)
        self.assertEqual(call.call_args.args[0], ["codex", "-C", str(self.root), "--no-alt-screen", "$start-session"])


if __name__ == "__main__":
    unittest.main()
