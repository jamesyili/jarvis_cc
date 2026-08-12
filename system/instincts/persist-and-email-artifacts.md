---
id: persist-and-email-artifacts
trigger: When work produces a substantive artifact (~50+ lines: memo / spec / template / long draft), when new substance belongs in an existing artifact, or when James changes an item's status (done / cut / defer / deprioritize)
behavior: Persist proactively, in the right place, immediately — but only what's durable. (1) Write substantive DURABLE drafts to files with a proposed path — show AND write, not either/or; scratch/short stays in chat. (1b) EPHEMERAL one-shot outbound content (Slack messages, short notes, anything consumed once) gets chat + email only, NEVER a repo file (2026-07-25 correction — compose in scratchpad if a file is needed for sending). (1c) A draft James will SEND LATER (not consume in-session) must reach a durable delivery channel in the same session it's composed — scratchpad file with the path stated, or email when he asks; chat-only composition is a silent loss (2026-08-11: transcript archaeology to recover the Shifu drafts). (2) Emailing is EXPLICIT-ASK ONLY (2026-07-25 correction — auto-/send-me retired): write the file, tell James the path, send only when he says send. (3) Edit the original artifact in-place rather than spawning a parallel companion doc (companion only on explicit ask / format change / coherence loss). (4) When James changes a status, update the source-of-truth file in the same response — don't defer to session end. (5) NEVER say "filed/updated" in prose before the Edit/Write has actually run — run the tool first or say "filing next"; a claimed-but-unwritten update is a silent record gap.
confidence: 0.85
evidence_count: 8
created: 2026-06-26
last_updated: 2026-08-11
status: active
---

## Why merged

Consolidated 2026-06-26 from four feedback memories on persisting artifacts/decisions in the right place at the right time: `write_artifacts_to_files`, `update_in_place_not_companion`, `email_md_files_by_default`, `persist_decisions_immediately`.

## Evidence (from migrated feedback memories)

- **write_artifacts_to_files** (4/xx) — substantive named artifacts get written to files proactively with a proposed path, not left in chat.
- **update_in_place_not_companion** (5/22) — new substance belonging in an existing artifact → edit the original, don't create a parallel companion doc.
- **email_md_files_by_default** (5/23) — new substantive `.md` under user-facing dirs → auto /send-me; carve-outs for memory/session-logs/KB.
- **persist_decisions_immediately** (4/04) — status changes get written to the source-of-truth file in the same response, not deferred.
- **2026-07-25 correction (auto-email retired):** Leo auto-/send-me'd the Bella H1 draft mid-session; James: "Don't send me things until I tell you." Emailing is now explicit-ask only — persist the file, state the path, wait. (Supersedes the 5/23 `email_md_files_by_default` clause.)
- **2026-07-25 correction (ephemeral ≠ repo file):** Leo saved a one-shot NLFU Slack-message draft as `work/projects/nlfu_slack_message_2026-07-27.md`; James: "Delete the slack message md file, don't keep these short term things in the future." One-shot outbound snippets are ephemeral — chat + email only; scratchpad if a file is mechanically needed for /send-me.
- **2026-07-27 (self-caught): claimed-before-written.** During the Yuke debrief Leo wrote "Plan as ratified is filed on Yuke's entry" in prose without having run the edit; caught and repaired next turn. New clause (5): the tool call precedes the claim, always.
- **2026-08-11 (implicit correction): chat-only drafts got lost.** The 8/10b session composed the three Shifu Slack drafts in-conversation only — no email, no scratchpad file (session log said "drafts written," but nothing was on disk). Next morning James: "did you send me the message to be sent to the Shifu people? If not, email me that" — recovery required parsing the raw session transcript, which only worked because it still existed locally. New clause (1c): send-later drafts reach a delivery channel same-session. (Note: recovery was filed to `work/projects/reflex/shifu_followup_slack_drafts_2026-08-10.md` — a judgment call against the 7/25 ephemeral-≠-repo-file letter, made because the email cites the path and the drafts are load-bearing in the Shifu record; James can veto the file.)
