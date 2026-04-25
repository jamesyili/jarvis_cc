# Wes Kao Notebook Review — Cupcake Lookback Draft v2

Wes Kao Frameworks notebook consult on the v2 draft. Notebook ID: `wes-kao-frameworks` (UUID `e2650916-178d-460d-bf27-fb25bd933dc9`). Session ID: `c8ff2b56`. Run via direct MCP after the consult-notebook agent stalled (subagent tool-exposure issue still open per backlog).

---

## Raw notebook output

### 1. Top 3 Strengths to Keep

**"System gap, not people gap" framing**
- Framework: *Comment on the behavior, not the person.*
- By depersonalizing the friction, you prevent defensiveness and keep the cross-functional team focused on process improvement rather than pointing fingers.

**"Rather than let separate narratives form, we wanted to write one doc together"**
- Framework: *Playing Defense (Control the narrative).*
- You are proactively shaping the story of Q1's friction instead of letting the vacuum be filled by gossip or misalignment across the three teams.

**Inviting PM/Design/TPM input ("It's incomplete by design")**
- Framework: *Observe, Assert, Validate (OAV).*
- You are asserting the engineering perspective, but explicitly validating it with your cross-functional partners. Creates psychological safety and gives them a reason to enthusiastically say "yes" to co-authoring rather than feeling dictated to.

### 2. Top 3 Weaknesses to Fix

**Weakness 1: The opening is chronological and buries the punchline.**
- Frameworks: *Start right before you get eaten by the bear* + *Bottom Line Up Front (BLUF).*
- Executives and busy partners don't need the chronological backstory of how you decided to write the doc.
- **Concrete rewrite:** "BLUF: Q1 cross-team work drove strong UX/backend wins, but exposed 5 system-level integration gaps. This draft asserts Engineering's proposed Q2 ownership principles to resolve them. We are seeking PM/Design/TPM input to finalize a unified operating model."

**Weakness 2: Leaving "Tim and Yan TBD" on leadership commitments.**
- Frameworks: *Act like an owner / This is a relay race (Do you have the baton?).*
- Shipping a "joint" document where 2 of the 3 authors haven't actually committed to their action items signals misalignment and passes the burden to the reader.
- **Concrete rewrite:** Secure their alignment before sending. "Where we're leaning as leads: James commits to X, Tim commits to Y, Yan commits to Z."

**Weakness 3: Mentions of a "recurring quarterly practice" in the opening paragraph.**
- Framework: *Sales, Not Logistics.*
- Establishing a recurring operational cadence is a logistical detail. It dilutes the "sales" pitch of why the EPD team needs to align right now.
- **Concrete rewrite:** Move this detail entirely out of the Opening and drop it into the "Forward practices" bulleted list.

### 3. Single Most Important Edit Before Manager Review

**Fix the "Tim and Yan TBD" gap.**

Sending a draft to your Sr. Director that claims to be from "engineering leadership" but clearly lacks commitment from your two peer EMs projects *Insecure Vibes* and highlights poor cross-team alignment.

Do not send this to your manager until you have forced the alignment conversation with Tim and Yan to fill in those blanks.

> *Your manager wants to know you have herded the cats, not that you are asking them to herd your peers for you.*

### 4. Framing Question to Answer Before Sending

**"What is the Question Behind the Question (QBQ) my Sr. Director will have when reading this?"**

If you just send the draft as an FYI, you are making them guess what to do. You must be explicit about the type of feedback you are looking for.

Your Sr. Director's QBQ is likely: *"Will opening this doc up to the whole EPD org create alignment, or will it trigger a massive, unstructured complain-fest?"*

You must preface your review request by explicitly stating how you plan to control the feedback loop. Example:

> "I'm sending this for your directional feedback before we share it with EPD. We are gating the comments to focus strictly on forward-looking solutions, not past grievances."

---

## Leo synthesis + sequencing correction

### The sequencing correction I owe James

Earlier in the conversation I told James to leave Tim and Yan commitment placeholders blank and let them write their own — and warned against drafting their commitments. **That is correct for the broader EPD release.**

It is **not** correct for the Dylan pre-review. Wes is sharp: a "joint" leadership doc with TBD placeholders for two of three authors signals misalignment. Dylan reads that as "James can't herd his peers."

The correct sequence:
1. Send draft to Tim and Yan (separately from Dylan). Lock their commitments.
2. Send v3 (with all three commitments visible) to Dylan for pre-review.
3. After Dylan's pass, open to broader EPD.

Not: send v2-with-TBDs to Dylan, ask Dylan to validate before peers commit.

### Top-line edits to apply to v2 before next iteration

1. **BLUF opener.** Lead with a 2-3 sentence punchline: wins, gap diagnosis, ask. Keep the rapport-building chronological paragraph below as paragraph 2 for the broader audience. Best of both.
2. **Move "recurring quarterly practice" line out of the opener** into Forward Practices.
3. **Lock Tim and Yan commitments before Dylan pre-review.** Send them the draft with the Tim/Yan ask cover note (see `sequencing_and_cover_notes.md`).
4. **Add the QBQ-controlling preface to the Dylan cover note.** Explicitly state how the EPD comment loop will be controlled.

### What Wes endorsed that should be protected through iterations

- The "system gap, not people gap" framing across friction sections. Don't let later edits weaken this.
- The "rather than let separate narratives form" framing in the why-this-exists section. Don't let later edits remove this — it's the narrative-control move.
- The function-specific input prompts at the end of each major section. They are doing OAV work.

### What Wes did NOT flag but worth tracking

- The PM-engineering subsection wording ("Both sides acted reasonably given the inputs they had"). Wes didn't comment on it but James and Leo previously identified it as the section closest to thin-veil for Akshanta/Lili. Hold the current version unless something better surfaces.
- The Yan ownership-transition encoding via forward principles. Wes didn't comment on this layer specifically. The "soft publication, not ratified policy" calibration is judged correctly per the briefing's strategic backdrop.
- The James commitment ("first point of contact for cross-team asks"). Wes didn't single this out but the *Owner mindset* framing he applied to weakness #2 implicitly endorses it — James's commitment IS a clear baton-pickup, not a TBD.

### Open question

Wes's framing question — "What is Dylan's QBQ?" — is worth answering explicitly before sending. The current best answer:

> Dylan's QBQ is *"Will this doc create alignment in EPD, or trigger a complain-fest?"* The cover note must preempt this by naming the feedback-loop control mechanism (e.g., gating comments to forward-only solutions, time-boxed retro session as the venue for past grievances, named EM owner per comment thread).
