# Wes Kao Review — UPP Cross-Org Operational Model v2

**⚠️ NOT RAG-grounded.** The Wes Kao notebook consult **failed on authentication** (recurring issue logged 2026-04-21, still P0 in backlog). This review channels Wes Kao's frameworks from training knowledge — her Maven course material, her Substack, her LinkedIn essays, her public frameworks. Treat with the same skepticism as the Ethan Evans channeling. When the notebook auth lands, re-run this for grounded source quotations.

**Document reviewed:** `draft_v2.md` (UPP Base Retriever Release Cycle + Cross-Org Operational Model).

---

## The headline I'd give James

This doc is structurally complete. It has the right sections, the right scope, the right audience instinct. **The problem is sentence-level: it hedges where it should declare, narrates where it should land, and asks for permission where it should invite challenge.** Three Wes Kao moves fix 80% of the issues: lead with what changes, replace hedges with declarative bets, and pre-empt the most obvious objection before the reader can voice it.

---

## 1. Lead with "what changes" — not "what this is for"

### What's wrong

The opening callout reads: *"This is a working draft to align the UPP Base Retriever working group on (1) how we run the release cycle..."*

That's meta-talk. The reader is being told what the doc *is*, not what it *does*. Wes's "what changes" test fails: a busy reader skims this and walks away with no operational change in their head.

### Concrete rewrite

Replace with something like:

> **What changes when this doc lands.** Surface teams own their fine-tuning end-to-end. Base team owns the release cadence, base architecture, and platform infrastructure. Notif goes first: by end of May, Rui drives Notif FT decisions, James and Hongtao step out of the execution loop, and we publish a formal release cadence (1–2 base retrievers per quarter, 2 stable versions max). P2P and Search adapt the same template as their handoffs land in Q3 and H2.

Three sentences. Reader walks away knowing exactly what's different. The "what this doc is for" framing is then the second paragraph, not the first.

---

## 2. The Most Obvious Objection (MOO) is unanswered

### What's wrong

Wes's MOO framework: surface the strongest pushback the audience will raise, and answer it before they ask. The two MOOs the working group will have:

**MOO 1:** *"This is overengineered for a single handoff. We don't need a charter; we need a Notif transition plan."*

**MOO 2:** *"How is this materially different from how things already work? Surface teams already own their FT in practice."*

Neither is answered in the current doc. They lurk under the surface and will surface in the meeting if not pre-empted.

### Concrete addition

Add a §1.5 — **"Anticipating two objections."**

> *"Why a charter when we just need a Notif handoff plan?"* Because Notif is the first of three handoffs in 12 months. P2P adoption is in active co-design; Search adoption follows in H2. Treating Notif as one-off means re-litigating the operational model three times. Treating it as the first instance of a model means each subsequent handoff inherits the precedent.
>
> *"Doesn't this already work in practice?"* In practice, base team is still partly driving Notif FT (Hongtao on his ATG hat). Rui is stepping up but does not yet own launch decisions. Without the explicit handoff, base team will keep getting pulled into surface decisions, and surface team will not fully own the surface. The cost shows up next time we change architecture and discover surface team had not been making the FT decisions on its own.

Two paragraphs. Reader's biggest objections pre-empted. They can now read the rest of the doc constructively rather than skeptically.

---

## 3. Hedges to strip

### Wes Kao anti-hedge audit

Hedges weaken claims. They signal the writer is uncertain — even when the claim is sound. Strip every "may," "can," "should," "we believe," "largely," "typically," and rewrite as a declarative.

| Current | Rewrite |
|---------|---------|
| "Aim to release a new UPP Base Retriever 1–2 times per quarter" | "Base team releases a new UBR 1–2 times per quarter" |
| "We can target supporting at most 2 base retrievers at a time" | "We support at most 2 base retrievers at a time" |
| "A primary goal is to avoid maintaining multiple stable versions. We acknowledge this won't always be achievable" | "We avoid multiple stable versions. When we deviate, the deviation is time-boxed (§5)" |
| "If they're asking, they're not yet owning. Either coach them through it or accept the handoff isn't done." | "If they're asking, the handoff isn't done. Coach them through the decision; do not make it for them." |
| "Surface teams may have a legitimate 'we don't want to migrate just for migration's sake' position" | "Surface teams may decline migration when adoption cost outweighs the maintenance-cost benefit" |

The pattern: replace conditional/hedging modal verbs with present-tense declaratives. The doc reads ~20% sharper after this pass alone.

---

## 4. §9 — invitation in the wrong shape

### What's wrong (echo of Ethan's #3)

§9 reads as "is X right? Or should it be Y?" That's a plebiscite, not a working session. The reader can only vote up or down on each item. There's no surface for them to add nuance or propose alternatives that aren't in the framing.

### Wes-flavored rewrite

Each §9 item should follow the structure: **declarative bet → named alternative we considered → specific kind of pushback we want.**

**Example, §5 Scenario A:**

> **Bet.** When surface FT-on-new-base shows engagement-negative, surface stays on old base; base team treats new release as blocked; multi-version maintained ≤1 quarter.
>
> **Alternative considered.** Block surface from upgrading until base is fixed (more conservative for platform; creates surface friction).
>
> **Pushback we want.** Production case studies where time-box should be tighter / looser. Specific cases where blocking-the-surface-upgrade is the right call.

This reads as a bet, not a question. The working group can argue with the bet's specifics or replace the bet with a sharper one. The reader knows what kind of input is useful.

---

## 5. Mechanism over outcome — §6 Notif Handoff

### What's missing

§6 lists six clean-handoff criteria. Each is a *result*, not a *mechanism*. The reader knows what "clean" looks like, but not how the team gets there.

### Concrete addition

After the criteria list, add: **"How we get there."**

> 1. **Week 1 (May 5):** James + Dimitra meet to align on the criteria above and the role split. James drafts the 1-pager (criterion 5).
> 2. **Week 2:** Rui leads first weekly sync agenda end-to-end. Hongtao supports but does not drive.
> 3. **Week 3:** Surface Tower v2 result lands. Notif team owns the analysis writeup. James + Piyush review only if asked.
> 4. **Week 4:** Notif team updates shared doc independently. James does not write in the doc this week.
> 5. **End of May:** Dimitra names the next FT initiative without prompting; James stops attending the weekly sync.

Five steps. Reader knows the mechanism. Without this, the criteria are scoreboards without a play-by-play.

---

## 6. Sentence density audit

### The "one beat per sentence" violation

§3 has paragraphs that pack 3–4 ideas into single sentences. Example:

> *"Lengthen if surface adoption lags; shorten if pinner-first urgency is clear and adoption is healthy."*

Two distinct mechanisms in one sentence. Reader has to parse both. Split:

> Lengthen the cycle if surface adoption is lagging — slow down to give surfaces time to absorb each release. Shorten the cycle if pinners are waiting on capability the next release ships and surface adoption is keeping pace.

Twice as many words, half the cognitive load. Run this audit across §3 (release cycle), §5 (scenarios), §7 (coordination mechanisms).

---

## 7. The "you" test

### What the doc currently does

Most sentences are framed in the third person or first-person plural: "we," "the base team," "surface teams." The reader feels described, not addressed.

### Targeted "you" rewrites for each audience

For the Notif team specifically, add a sidebar or callout:

> **For the Notif team (Rui, Hongtao, Dimitra, Zhenyu):** You own Notif FT end-to-end after May. That means: you decide what features to add at FT, you choose your A/B configurations, you own the launch call. We're not approving your launches; you are. Base team is on call for platform-level issues — we're not on call for your surface debugging. You can ping us on Slack with one business day SLA; expect that we will be hands-off unless you ask.

Same content as the body of the doc, but in second person. The reader feels addressed, not described. Apply selectively — too much "you" makes the doc feel like a memo to subordinates, not a partnership doc.

---

## 8. Implication chain — every claim should land a "so what"

### Wes's "so what" audit

Every paragraph should have a clear consequence. The reader should walk away knowing: "and therefore X." Several paragraphs in v2 land technical claims without a "so what."

### Specific examples

§3 *"Cadence: Aim to release a new UPP Base Retriever 1–2 times per quarter to start. Calibrate based on the first 2–3 cycles..."* — what's the so-what for the reader? Add: *"This means surface teams can plan their FT iteration cycles around a known release cadence rather than waiting on ad-hoc base updates. Base team can plan deprecations rather than reacting."*

§4 V0 *"Notif and HF currently share codebase. V0 will split surface teams into separate FT codepaths so each surface can independently add features without coupling."* — so-what: *"This unblocks surface teams from each other — Notif's feature additions no longer affect HF's, and vice versa."*

Audit every paragraph for the so-what. If it's not there, add it.

---

## Summary — top 4 highest-leverage Wes-flavored changes

1. **Open with "what changes when this doc lands."** Replace the meta-opener with a 3-sentence declarative future state.
2. **Add a §1.5 anticipating the two MOOs** ("why a charter for one handoff?" and "doesn't this already work?"). Pre-empt them in writing.
3. **Strip hedges system-wide.** "Aim to," "can," "may," "we believe" — rewrite as present-tense declaratives.
4. **Reframe §9 from questions to bet → alternative → kind-of-pushback-wanted.** Same concrete instinct as Ethan's #3.

If only one change happens: **#3 (hedge audit).** It's the highest signal-to-effort ratio. The doc reads materially sharper after one editing pass.

---

## What I'd say at the end of a Maven session

> "Your structure is right. Your judgment on what to include is right. Your altitude is right. The fix is at the sentence level: tell me what changes, anticipate my pushback, and stop hedging on bets you've actually made. Three passes through the doc with those three lenses and you have a charter your working group can actually use."

— Wes Kao (channeled, NOT notebook-grounded)
