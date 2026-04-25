# Ethan Evans Review — UPP Cross-Org Operational Model v2

**Source:** Channeled from Ethan Evans's published frameworks (Substack, LinkedIn, "The Crow's Nest" archive). NO notebook exists for Ethan Evans in Leo's registry — this review is from training knowledge, not RAG-grounded sources, and should be treated accordingly.
**Reviewer voice:** Ex-Amazon VP, 15 years inside Big Tech leadership. Writes about promotion mechanics, scope, sponsorship, "Magical Thinking" (writing the future as if it's already true), "Bridges of Trust," reducing uncertainty for one's manager, working-at-the-level-above.
**Document reviewed:** `draft_v2.md` (UPP Base Retriever Release Cycle + Cross-Org Operational Model).

---

## The headline I'd give James

This doc is operating at Director altitude. The act of writing a cross-org operational charter that spans base team + multiple surface teams + multiple release cycles is a Director-level act. **You should not need to label it that way for anyone — let the artifact speak.** What matters is that the working group, the leads, and (eventually) Dylan all walk away thinking: *"this is the kind of thing a platform owner produces."*

But the draft, as written, occasionally drops back to Sr. EM altitude — most visibly in §9 (Working Group Input). That section reads like an IC asking for permission. **Director-altitude voice asks for sharpening, not approval.** Below: where to fix.

---

## 1. Lead with the future state — Magical Thinking

### What's missing

The doc opens with §1 Background — what's happening, why now. That's a Sr. EM opener: contextual, careful, defensible.

A Director opens with **the future state described as if it were already true**. The reader should walk away from paragraph 1 with a mental picture of how UPP operates 6 months from now.

### Concrete rewrite for §1

Replace the current §1 opening with something like:

> **By Q4 2026, UPP runs on a quarterly release cadence with 2–4 surface teams operating their own fine-tuning loops. Notifications goes first this quarter; P2P and Search follow as their co-design work matures.** This document defines how that operating model works: how releases ship, how surfaces adopt them, and where ownership splits between the platform team and the surface teams. It's the retriever counterpart to Matt Chun's ranking-side release cycle TDD, and it adds the partnership-shape layer that ranking is also going to need.

The shift: from "we need this because the handoff is approaching" (reactive) to "this is how UPP runs at platform maturity" (declarative future). **The handoff is the first instance of the model, not the reason for the model.** Tiny reframe, big altitude shift.

---

## 2. Reduce uncertainty for the manager — what Dylan extracts

### What's missing

The doc is written for the working group, but it will graduate to Dylan and other leads. Right now, a lead reading it has to construct her own headline. **Don't make Dylan do that work.**

Add — at the very top, after the doc header — a 3-bullet **"For leads"** callout:

> **For leads (Dylan, Dimitra, Sai, Matt Chun):**
> - **The model:** base team owns the platform (release cycle, architecture, infra). Surface teams own their fine-tuning, launches, and on-call. Co-design at architecture changes; hands-off at steady-state.
> - **The cadence:** 1–2 base retriever releases per quarter, 2 stable versions max, 2-week SLA for surface adoption start.
> - **The first test:** Notif handoff lands clean by end of May 2026. If it does, P2P and Search use the same template.

Three lines. Lead extracts the entire doc in 15 seconds. **Reduces uncertainty.** That's the manager-utility play.

---

## 3. Working-at-the-level-above — the §9 problem

### What's wrong with §9 currently

§9 (Working Group Input — places I most want pushback) is where this doc most clearly drops altitude. Eight numbered questions, each phrased as "is X right? Or should it be Y?"

That's an IC asking for permission. **A Director-altitude version of §9 is not a list of questions — it's a list of bets.** Each bet has a default answer. You're asking the working group to either (a) agree with the bet, (b) propose a sharper bet, or (c) push back with rationale. You are not asking for binary up-or-down votes.

### Concrete rewrite

Replace each §9 question of the form *"Is X right?"* with a structure of the form:

> **Bet 1 (§5 Scenario A — engagement-negative):** *Surface stays on old base; multi-version maintained for ≤1 quarter; rollback required if the new base can't catch up.* The alternative (block surface from upgrading until base is fixed) is more conservative for the platform but creates surface-team friction. **Push back if you've seen Scenario A play out differently in production, or if you think the time-box should be tighter / looser.**

This phrasing:
- Names the bet (declarative).
- Names the alternative (shows you considered it).
- Invites specific kinds of pushback (production experience, time-box calibration), not generic "what do you think."

Apply to all 8 §9 items. The doc gets *more* collaborative this way, not less — because the invitation is sharp, not vague.

---

## 4. Bridges of Trust — what surface teams get

### What's underweighted

The doc says "credit propagates outward" and "surface team's wins are surface team's." Good. But the surface-team-side value is mostly stated negatively (what the base team won't do — won't approve launches, won't claim wins, won't retune for them) rather than positively (what they get).

### Concrete addition

Add a §2.5 or sidebar: **"Surface team value proposition."**

> **Why surface teams choose UPP:**
> 1. **Pretrained capability they couldn't build alone.** Cross-surface data, foundation model integration, scale — surface team gets these for free, with a 2-week SLA to start FT.
> 2. **Surface team owns the product.** Features, FT recipe, labels, launch decisions — all yours. Base team is platform, not gatekeeper.
> 3. **Quarterly upgrades.** New base retrievers ship 1–2x per quarter. Surface teams get fresh capability without doing the platform work.
> 4. **Co-design seat at architecture changes.** When the base architecture changes, you have a named POC and decision rights on how it lands for your surface.

This is the **Bridges of Trust** opener with cross-org partners. Lead with what they get; the operational model is then the *infrastructure that makes the value durable*, not the constraint that limits them.

---

## 5. OAR — Ownership, Accountability, Results

### Where the doc loses sharpness on accountability

§6 Notif Handoff is the right shape but soft on accountability. "Hongtao currently driving FT" is a status. "Rui stepping up on FT iterations" is a status. **Status is not accountability.**

A Director-altitude version names accountability explicitly, with a date, owner, and result definition.

### Concrete rewrite for §6 "Current state"

> **Accountability state, end of April 2026:**
> - **Notif FT execution lead:** Rui Liu (Notif ML team). Accountable for FT recipe selection, A/B test setup, launch decision on Notif. Date assumed: end of April 2026.
> - **Cross-team execution support:** Hongtao Lin. Accountable for ATG-side support, no longer accountable for driving Notif FT decisions.
> - **Notif platform-engineering owner:** Dimitra. Accountable for surface-team capacity and the broader Notif strategy.
> - **Base-team execution support:** Piyush Maheshwari (TL), James Li (EM). Accountable for platform tooling and base model release cadence; NOT accountable for Notif FT execution.

The change: from "X is doing Y" to "**X is accountable for Y, by date Z, with result R.**" That's the OAR pattern. It also makes it possible for the working group to push back on the wrong owner — which is impossible under the current "status" framing.

---

## 6. Visibility for the right people — the doc as artifact

### What this doc lets Dylan do

Dylan can lift §1 and §2 of this doc verbatim into her own messaging to Rajat, Jeff, or peer Directors. **Make sure she can.**

Right now, §1 is too internal-process-focused to lift cleanly. After the rewrite in (1) above (Magical Thinking opener), it becomes a sentence Dylan can drop into any cross-org conversation: *"By Q4 2026, UPP runs on a quarterly release cadence with 2–4 surface teams operating their own fine-tuning loops..."*

That's a sentence she can use to brief Jeff. That's the **sponsor-utility** play. Don't write for the working group only — write so the artifact is useful to your sponsor without modification.

---

## 7. The "weekly snapshot" pattern

### What's missing structurally

This is a one-time alignment doc. After it lands, the operational model becomes invisible. **A Director-altitude version creates the cadence by which the model stays visible.**

### Concrete addition

Add a §7.5 or end-of-doc: **"Operational rhythm."**

> **Once the model is in steady state, base team will publish a monthly snapshot covering:**
> - Stable + nightly version status (which surface is on which version).
> - Active release cycle progress (V0 → V1 → V2 timeline).
> - Surface partnership health (last sync date per surface, last shared-doc update date, any tripwire signals).
> - Cost of multi-version maintenance (when applicable).
>
> **Audience:** working group + leads. **Distribution:** the same Slack channel and shared doc. **Owner:** base team TL.

A monthly snapshot is the Ethan Evans "weekly snapshot" pattern adapted for platform-team cadence. **It's the mechanism that prevents the doc from becoming shelfware.** Without it, the operational model lives in the doc but not in the operating reality.

---

## 8. The line you should not cross

### What this doc must NOT do

The doc is a charter, not a contract. It must not read as "if surface teams don't do X, base team won't do Y." That kind of conditional language reads as transactional and erodes trust.

The line I'd watch in v2: §3 "Consumer team handling" + §5 (Matt's scenarios) are at risk of reading transactional. Specifically, "*surface stays on old base*" in Scenario A could land as punitive if the surface team reads it as "you don't get the new base because you couldn't FT it well." That's not the intent, but the wording could land that way.

**Reframe:** "*Surface stays on old base while base team works the next release. The surface team has not failed; the release has.*" Make it explicit that the platform owns release-quality, not the surface.

---

## Summary — the four highest-leverage changes

1. **Rewrite §1 opener as Magical Thinking** (future-state declarative, not reactive context). 30 minutes.
2. **Add the "For leads" 3-bullet callout at the top** (sponsor-utility, reduces Dylan's work). 15 minutes.
3. **Reframe §9 from questions to bets-with-alternatives** (working-at-the-level-above). 1 hour.
4. **Add the §6 OAR-style accountability table** (sharper than status). 30 minutes.

If only one change happens: it's #3. The §9 reframe is what most clearly elevates the doc's altitude.

---

## What I'd say if I were James's sponsor reading this doc cold

> "This is the kind of artifact I'd expect from a Director-track Sr. EM. It's at the right altitude for cross-org alignment, it doesn't apologize for itself, and it sets up a real partnership model rather than asking permission. The four changes above sharpen it from 'good working draft' to 'production-grade platform charter.' Ship it after the rewrites — and use it as the lead artifact in your next career conversation with Dylan."

— Ethan Evans (channeled)
