# NotebookLM Query Log

> Rolling log of queries sent to NotebookLM notebooks and their outcomes. Helps James see what Leo is consulting, evaluate response quality, and improve query patterns over time.

---

## 2026-04-06 — Wes Kao Frameworks + Dynamic Triggering Slack Delegation

**Notebook:** Wes Kao Frameworks
**Context:** James drafting cross-org Slack thread for Dynamic Triggering ELT follow-up (Sumanth/Mehdi/Sai). Strategic constraint: Dylan has told James to "let Mehdi drive" — needs to convene without inheriting ownership.

**Query 1:** Apply Wes Kao to actual draft. Where is James betraying the facilitator framing? Is the lead buried? Is there a "convening without owning" pattern?
- **Key insights extracted:**
  - Holding the baton vs. passing it — James was structurally claiming ownership (4-point agenda, scheduled sync, "I want us to align") while verbally disclaiming it. Wes Kao relay-race frame: passed baton requires acknowledgment.
  - "Insecure vibes" words — *"I'm just trying to..."* and *"happy for him to drive"* are weak modifiers that diminish authority and sound like apology.
  - Sales then logistics violation — assigning work via 4-point plan before selling Mehdi on why this matters for HIM.
  - **No-surprises rule** — public delegation in a group thread risks the named person getting put on the spot, defensive, or dropping the baton.
- **Action:** Restructured into 2-step move — private DM to Mehdi first to pass baton with acknowledgment, then tight 5-sentence public group thread that hands the mic and steps out. The 4-point agenda saved as private input to the Mehdi DM, not as the public thread structure. Created instinct file `no-surprises-public-delegation.md` for future delegation drafts.

---

## 2026-04-04 — Wes Kao Frameworks + Karen Agent Design

**Notebook:** Wes Kao Frameworks (How to Speak)
**Context:** Building adversarial advisor agent "Karen" — needed frameworks for reading intent, challenging blind spots, accountability, and proposing alternatives

**Query 1:** Frameworks for Karen's system prompt — reading intent (QBQ), challenging without being dismissed (OARB), accountability (Rigorous Thinking), proposing alternatives (OAV)
- **Key frameworks extracted:** QBQ, OARB, "Even More" Technique, Rigorous Thinking / "Bad Things Good Things", OAV, BLUF + Sales Not Logistics
- **Action:** Embedded all 6 frameworks directly into Karen agent's system prompt as operating principles

---

## 2026-03-29 — How to Speak + ELT Presentation

**Notebook:** How to Speak
**Context:** ELT presentation talk tracks (slides 3-5) for CTO + VPs, March 31

**Query 1:** Review talk tracks for "project management narration" vs "visionary leader framing" — apply signposting and strategic framing principles
- **Key insight:** Slide 3 funnel walkthrough is "backstory scope creep." Compress to 1 sentence, let diagram work.
- **Action:** Rewrote slide 3 opening to BLUF the $938K savings in the first 30 seconds

**Query 2:** Apply Robot Voice Method — where is James burying the lead or over-explaining?
- **Key insight:** $6.5M figure buried in slide 5. Leading with logistics instead of selling.
- **Action:** Moved $6.5M to slide 4, restructured slide 5 to open with conclusion

**Query 3:** How should James structure exec Q&A answers? Senior engineer vs executive framing.
- **Key insight:** 3A Pyramid (Answer → Arguments → Add-ons). "I've observed" > "I think" (40% more credible). Don't validate negative frames.
- **Action:** Added Q&A structure to speaking reminders, integrated into communication.md

---

## 2026-03-29 — Improving Leo + System Design

**Notebook:** Improving Leo
**Context:** Evaluating Leo system architecture for improvements

**Query 1:** Highest-leverage improvements for Leo given current structure
- **Key insights:** Context indexing (CLAUDE.md as index), escape hatches, automate context updates in end-session, reverse elicitation pattern
- **Action:** Added escape hatches to CLAUDE.md + skills, enhanced end-session with Phase 4

**Query 2:** What would a practical eval system look like for a personal AI?
- **Key insights:** SOPs/rubrics per task type, test suite of edge cases, human baseline, track escape hatch usage
- **Action:** Added to leo_backlog.md for future implementation

**Query 3:** Meta-prompting workflow for improving CLAUDE.md and skills
- **Key insights:** Prompt folding (feed failures back), end-of-session "what did you learn" debrief, interview technique for building new skills
- **Action:** Added to leo_backlog.md for future implementation
