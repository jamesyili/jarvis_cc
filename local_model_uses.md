# Local Model Uses

*Created 2026-08-16, from the Qwen3.8-27B session. Status: nothing built — this is the ranked menu for when the trial runs. Hardware facts in `system/leo-overview.md` §Machines; strategic frame in `.claude/skills/leo-research-frontier/` (Frontier 2) and `.claude/skills/leo-kb-automation-campaign/`.*

## The frame

Claude Code stays Leo's brain — all interactive, judgment, high-stakes work. A local model is hands for work that currently doesn't happen at all: jobs disabled for cost (the two cloud triggers), jobs too token-expensive to ever justify (nightly sweeps over everything), and jobs too private to send out (journals, finances). Never a Claude replacement; a zero-marginal-cost batch tier under it.

## Hardware reality (pc-leo: RTX 5070 12GB, 32GB DDR5, 9800X3D)

- **~27B class (Qwen3.8-27B Q4, ~18GB):** doesn't fit in VRAM → CPU/GPU split → ~5–9 tok/s. Batch-only. Run Ollama Windows-native (WSL2 RAM cap).
- **~14B class (Q4, ~9GB):** fits fully on-GPU → ~50–70 tok/s. The interactive-capable tier.
- Two-tier plan: 27B for quality-sensitive batch, 14B for anything time-sensitive. A/B the digest quality before assuming the 27B is worth the speed hit.

## Scheduling constraint (James, 2026-08-16)

**No overnight runs.** The PC lives in the bedroom; fan noise while sleeping is a hard no. Batch jobs schedule into **daytime idle windows instead — the machine sits alone in an empty room all workday.** The "night shift" is a day shift: cron fires mid-morning, everything is done before evening. Revisit if the PC ever moves rooms.

## Ranked uses

1. **Nightly→daily instinct-adherence eval (Frontier 1).** Local judge replays each day's transcript against the ~70 instincts, files violations. The semantic-judgment eval that's been unbuildable on Claude economics; doubles as eval-harness blog material. Milestone: an automated check catches a real violation before James does.
2. **The pre-briefed session.** Daily digest of scout output + arXiv recsys + Notion list written into the repo, so the first Claude session of the day opens oriented. Campaign Phase 2(a) is the vehicle; gate below.
3. **Longitudinal mining of the record.** 170+ session logs, journals, karen_observations — carried-item lifetimes, comparison-engine timing, Karen hit-rate. Too token-expensive for Claude, most privacy-sensitive corpus in the repo.
4. **Semantic search over the KB.** The already-fenced item (`system/kb-spec.md`); unfences when the trial succeeds. Needs only a small embedding model, not the 27B.
5. **Local Whisper debrief pipeline.** Voice-memo debriefs → local transcription into the repo → `/debrief` runs on a transcript. Same box, not Qwen.
6. **Multimodal drop-folder.** Photos/screenshots → local vision transcription to a staging file. Must be a new folder with explicitly opposite semantics to `inbox/` (never-read-contents instinct stands) — deliberate decision required before building.
7. **Family tier.** Offline kid-safe tutor / Evelyn speech-and-debate sparring partner. Fun, zero-risk, James's call.

## The gate (tool-builder-trap fence)

Trial = two commands next local session: `nvidia-smi` sanity check, then Windows-native `ollama run qwen3.8:27b` on one day's scout output. Success gate stays the campaign's: **7 consecutive unattended days + one digest James actually reads.** If the digest goes unread, stop — the 5070 is a gaming card and that's fine.
