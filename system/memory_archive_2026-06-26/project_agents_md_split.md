---
name: agents-md-split
description: "Repo restructured 2026-05-23 — AGENTS.md is tool-neutral base, CLAUDE.md is Claude-Code-specific extensions, GEMINI.md → AGENTS.md symlink, prompts/ holds flattened workflows for Codex/Gemini/Cursor/Aider"
metadata: 
  node_type: memory
  type: project
  originSessionId: c023450d-34a1-41ac-9eb4-6db4e5a95ac2
---

# AGENTS.md / prompts/ split for multi-tool agent friendliness

Restructured 2026-05-23 to make the repo readable by Codex, Gemini, Cursor, Aider, and other agentic tools beyond Claude Code.

**Layout:**
- `AGENTS.md` (repo root) — tool-neutral base: who James is, modes, operating principles, folder structure, context-loading guide, NotebookLM via MCP, KB layout, conventions. This is what Codex / Cursor read by convention.
- `CLAUDE.md` — thin wrapper that points to `AGENTS.md` for the base, then adds Claude-Code-specific extensions: slash-command skill registry, custom sub-agents (Karen / Code Planner / Search / Consult-Notebook), settings.json hooks, file-based memory system.
- `GEMINI.md` — symlink → `AGENTS.md` (what Gemini CLI reads).
- `prompts/` — flattened tool-neutral prose versions of the 5 most-used workflow skills: `start-session.md`, `end-session.md`, `prep.md`, `draft-email.md`, `debrief.md`, plus a `README.md` index.

**Why:** James wants the codebase agent-friendly across tools. Skills/agents/hooks/memory are Claude Code primitives that don't port — those stay in CLAUDE.md. Context substrate (work+self/, kb/, etc.) is already tool-agnostic markdown; AGENTS.md just makes that discoverable.

**How to apply:**
- For Claude Code, `.claude/skills/<name>/SKILL.md` remains source of truth — the `prompts/*.md` files are derivative. Keep both in sync if a workflow changes. Most-used 5 are flattened; other skills (`/coach-check`, `/grill-me`, `/thinking-partner`, `/pulse`, `/weekly-review`, etc.) are Claude-only for now.
- When James asks for further coverage (more skills flattened, AGENTS.md tweaks), update `prompts/` and `prompts/README.md`.
- AGENTS.md is the canonical statement of operating principles — if a principle changes, update AGENTS.md, not CLAUDE.md.
- Slash-command references in AGENTS.md were softened to tool-neutral phrasings (e.g. "Want me to run cross-cutting KB reflection?" not "Want me to run /kb-reflect?"). Preserve that pattern in future edits.
