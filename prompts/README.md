# prompts/

Tool-neutral workflow recipes. Each file is a self-contained set of instructions any agentic tool can follow when James asks for that workflow by name.

## When to use

When James says "let's start a session", "end session", "prep me for X", "draft an email to Y", or "let's debrief" — read the matching file and follow it.

These are the source of truth for **Codex, Gemini, Cursor, Aider, and any tool without a registered-command system**.

For **Claude Code**, the canonical source is `.claude/skills/<name>/SKILL.md` and these files are derivative — kept in sync but the slash-command versions are richer (they integrate with the Claude Code agent / hook / memory systems).

## Files

| Workflow | Trigger phrases |
|----------|-----------------|
| [`start-session.md`](./start-session.md) | "start session", "let's begin", "hi" / "hello" at start of a conversation |
| [`end-session.md`](./end-session.md) | "wrap up", "goodbye", "end session", "let's commit" |
| [`prep.md`](./prep.md) | "prep me for X", "prep for the Dylan 1:1", "I have a meeting with Y" |
| [`draft-email.md`](./draft-email.md) | "draft an email to X", "draft a slack to Y", "write a message for Z" |
| [`debrief.md`](./debrief.md) | "let's debrief", "here's what happened today", end-of-day capture |

Read [`../AGENTS.md`](../AGENTS.md) first for the base context (who James is, principles, folder layout) before running any of these workflows.
