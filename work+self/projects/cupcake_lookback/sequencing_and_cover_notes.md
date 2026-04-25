# Sequencing + Cover Notes

How to actually move this doc from v2 → broader EPD release. The Wes Kao review surfaced a sequencing correction that materially changes the order: Tim and Yan commitments must be locked **before** the Dylan pre-review, not after.

---

## The corrected sequence

| Step | Action | Audience | Cover note |
|---|---|---|---|
| 1 | Apply Wes Kao edits to v2 → produce v3 | Self | — |
| 2 | Send v3 to Tim and Yan; lock their commitment bullets | Tim, Yan | See §A below |
| 3 | Apply their commitments + any peer edits → produce v4 | Self | — |
| 4 | Send v4 to Dylan as pre-review | Dylan | See §B below |
| 5 | Apply Dylan's directional feedback → produce v5 | Self | — |
| 6 | Open v5 to broader EPD with controlled comment loop | Engineers, PMs, designers, TPMs across three teams | See §C below |
| 7 | Live retro session converts written input into resolution | All | — |
| 8 | Final v6 published as the artifact of record | All | — |

---

## §A — Cover note to Tim and Yan (locking their commitments before Dylan)

This goes in a 3-person DM with Tim and Yan, with the v3 draft attached.

> Tim, Yan —
>
> Iterated on our seed draft. Attached as v3.
>
> Before we run this by Dylan, want both of you to take a pass and lock the "Where we're leaning as leads" section. Mine is in. Yours are placeholders.
>
> The framing for your commitment bullet: one concrete forward commitment, action-flavored, system-shaped. Something an IC reading the doc would point to in three months and say "Tim/Yan said they'd do this and it's actually happening."
>
> Push back on anything in mine if it doesn't match what you expect from CG. Edit any other section freely — this is a draft, your fingerprints are welcome.
>
> Two-day turn would be great so we can run it by Dylan this week. If you need longer, say so and we'll re-time.
>
> — James

**Why this framing:**
- Direct ask, framed as locking-in not requesting permission.
- "Action-flavored, system-shaped" gives them a clear bar without writing it for them.
- "Two-day turn" sets a default cadence without imposing a deadline that reads as pressure.
- Invites edits anywhere in the doc — signals genuine co-authorship.

---

## §B — Cover note to Dylan (pre-review)

This goes 1:1 to Dylan after Tim and Yan have locked their commitments. Either DM or short email. The Wes Kao review surfaced this as the highest-leverage edit: preempt Dylan's QBQ before she has to ask.

> Dylan —
>
> Tim, Yan, and I co-authored a Q1/Cupcake lookback + look-forward doc for our combined EPD group. Attached as v4 — Tim's and Yan's commitments are locked.
>
> Before we open it to the broader EPD audience for input, wanted your eyes on three things specifically:
>
> 1. **Does the ownership section get ahead of the 1-pager, or is the altitude right?** The doc treats ownership direction as principles, not ratified policy — keeping the 1-pager as the formal artifact. Want to make sure I've calibrated that correctly.
>
> 2. **Does the friction framing feel balanced across functions?** Specifically don't want this to read as eng pointing at PMs. Both sides acted reasonably given the inputs they had — that's the framing — but want your read on whether it lands.
>
> 3. **Anything you'd want softened or sharpened before PMs and designers see it?**
>
> One thing I want to be deliberate about: when this opens to EPD, I'm gating the comment loop to focus on forward-looking solutions, not past grievances. The retro session is the venue for the harder conversations. The doc is the seed.
>
> No urgency on your timing — happy to adjust on your read.
>
> — James

**Why this framing:**
- Three explicit questions narrows Dylan's review surface area. Wes's *OAV* framework: assert your direction, validate with three pointed asks.
- The preempted-QBQ paragraph at the end ("gating the comment loop to focus on forward-looking solutions") is the load-bearing move per Wes Kao. It tells Dylan she doesn't need to worry about the doc triggering a complain-fest because James has thought about feedback-loop control.
- "No urgency on your timing" gives Dylan room without abdicating direction.
- Director-altitude framing throughout: outcomes, principles, audience-aware, not seeking validation.

---

## §C — Cover message to broader EPD (final release)

This goes after Dylan's directional feedback is incorporated, in the shared cross-team Slack channel(s) with the v5 doc attached.

> Hey EPD —
>
> Tim, Yan, and I put together a Q1/Cupcake lookback + look-forward doc for our combined group. Attached.
>
> What it is: our read on what worked, what produced friction, and the principles + practices we're proposing for stronger Q2 collaboration. The engineering leads' perspective. We know it's one lens.
>
> What we want from you: your perspective. PMs, designers, TPMs, ICs across all three teams — please add inline comments. Specifically interested in friction patterns we missed, practices that would actually help your work (or that would just add overhead), and anything in Q1 worth protecting that we underweighted.
>
> Joint EPD retro session: [date]. The doc is the seed. The session is where the harder things get talked through live.
>
> One ask: please keep comments focused on forward-looking solutions. The retro session is the venue for retrospective grievances. Helps us land somewhere actionable.
>
> — James, Tim, Yan

**Why this framing:**
- Replicates Wes's *OAV* at the broader-audience scale: assert the engineering perspective, validate with explicit input invitations.
- Function-specific prompts in the middle paragraph let each role know what to look for.
- The "one ask" closes the comment-loop control without sounding restrictive.
- "Tim, Yan, and I" signature reinforces the leadership-unity signal.

---

## Decisions James needs to make before sending §A

- **Title format.** Default proposal: `Q1 / Cupcake Lookback + Look-Forward — HF CG × P13N-Experiences × Frontend`. Decide before sending.
- **Retro session date.** Pick a date 2-3 weeks out (allows v3→v4→v5→EPD-input window). Send calendar invite alongside the §C message.
- **The "third tension" the v1-LLM referenced** in its open items list. Ignore unless James actually had a third item in mind from the original LLM session — likely hallucinated.
- **Cupcake content fill-ins.** UX wins, backend wins, exec visibility, cross-EPD collaboration moments. Highest-leverage remaining content gap (per Wes Kao review — friction + principles dominate the doc unless wins are filled in vividly).

---

## Risk register

| Risk | Mitigation |
|---|---|
| Tim or Yan pushes back on a forward principle | Welcome the pushback in §A. If material, iterate v3→v3.5 before sending Dylan. |
| Dylan flags the ownership section as too forward | Soften surface-ownership line further to "we're aligned on direction; operational details continue to be worked through." Defer specifics to the 1-pager. |
| AJ or Devin comments aggressively in EPD release | Architectural-disagreements-resolve-at-TL+EM-altitude principle in the doc gives a clean redirect: "let's take this offline at the TL+EM level." |
| PMs (Akshanta, Lili) flag the routing principle as gatekeeping | The "not gatekeeping — routing" language inside the principle preempts. If they push, James responds in-thread offering to be the routing point of contact himself. Lives with his commitment. |
| Raymond's name gets surfaced by an IC commenter | The "system gap, not people gap" framing gives clean redirect: "the principle is about ownership clarity at the role level. Specific people questions go through TLs+EMs." |
| Dylan flags the Q1 wins as thinly written | Wes Kao review already flagged this. Fill in the Cupcake wins before sending §B. |
