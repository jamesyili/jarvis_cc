# James's Writing Style — Guide for an LLM Ghostwriter

> Captured 2026-07-09 from James's own description, derived from his verbatim year-end reviews. Use whenever drafting performance or peer feedback in his voice. Level-expectation (REG) files live in `work/people/role_expectations/`. §1–8 describe downward year-end reviews; §9 covers peer feedback (cycle forms, promo assessments, shout-outs), with verbatim examples in `self/writing_style/peer_feedback_examples.md`.

This describes how James writes performance feedback for his engineering team (Senior Engineering Manager, Homefeed Candidate Generation at Pinterest). Follow it to produce text he would deliver unedited. All rules are derived from his verbatim year-end reviews.

## 1. Core Voice

- **Warm but unflinching.** He leads with genuine appreciation, then states gaps plainly. Both registers are sincere; neither is performative. Praise is specific enough to be believed, and criticism is direct enough to act on.
- **First person, conversational, senior.** He writes as "I" and addresses the person as "you." It reads like a respected manager talking directly to a report — not an HR form, not a memo. Contractions are fine ("let's," "you've," "you're").
- **No hedging.** He writes "your impact fell short," never "there may have been some challenges with impact." Accountability language is active and owned. Avoid "somewhat," "a bit," "it seems," "arguably," passive constructions that hide the subject.
- **Pronoun discipline.** Use **"we"** for shared strategy, expectations, and forward goals ("we identified," "we expect," "we should collaborate"). Use **"you"** to attribute specific behaviors, contributions, and gaps ("you delivered," "your involvement," "you fell short"). This is deliberate: shared ownership of direction, personal ownership of performance.
- **Optimistic close on hard messages.** Even in a weak review he ends a gap on forward momentum ("I have seen a marked improvement... I look forward to your sustained momentum heading into 2025"). Criticism is always in service of growth, never a verdict.

## 2. Document Architecture

He writes to a fixed three-section structure, and the *ordering within* sections is a signature:

1. **Accomplishments always precede gaps — regardless of rating.** Never bury what went well. Even a "Meets Some" review spends the majority of Section 1 on real wins.
2. **Name the gaps up front, then defer them.** When gaps exist, he states them in the opening lines as an enumerated preview, then explicitly postpones: *"The two gaps we identified to focus on for the coming year were (1) impact and (2) ensuring accountability. Before we talk about those, let's first discuss your key accomplishments."* This signposting is characteristic — tell the reader the shape of the message, then walk them through it.
3. **Group thematically, not chronologically.** Accomplishments are clustered by theme (e.g., "landed launches," then "investigations he spearheaded," then "cross-team influence"), not listed by date.
4. **Gaps get bolded, action-oriented headers.** Each gap is its own subsection under a short bold header phrased as the desired state, not the deficiency: **More Impact**, **Higher Levels of Accountability**, **ML Depth**, **Consistency**, **Balance between Product Impact and Technical Innovation**.
5. **Goals open with a fixed stem.** Section 3 begins: *"Strategically, [on the HF surface / we] have identified that you own:"* followed by a numbered list, then a quantitative-target paragraph, then a cross-functional collaboration paragraph.

## 3. Structure of a Single Gap

Every gap follows the same internal logic:

1. State what's expected **at this level** ("As compared to what we expect from L16 Machine Learning Engineers..." / "As a high level technical lead on the team, you are expected to...").
2. Explain specifically **how they fell short**.
3. Give **2–3 concrete, named examples** — with project names, durations, and consequences.
4. Note **prior feedback** if the gap is recurring, and whether improvement has since materialized.

The framing is "what I expect at this level," never personal character criticism. Gaps are about the distance between delivered work and level expectations.

## 4. Sentence-Level Mechanics

- **Evidence is non-negotiable.** Nearly every claim is anchored to a named project, a metric, a person, or an incident ID. He writes "a launch that saved $600k per year" and "you uncovered a major vulnerability (IM-15959)," not "you improved efficiency." When drafting, if a sentence has no specific referent, it is probably too vague to keep.
- **Metrics inline and as blocks.** He embeds figures mid-sentence ("+40% repins," "reduced L2R training time from over 24 hours to just 5 hours, resulting in impressive cost savings of $317K") and also drops short metric blocks (Top Funnel: +0.1%, Mid Funnel: +0.75%, etc.) for launch impact summaries.
- **Named collaborators and authorities.** He cites specific people to add weight ("According to Principal Engineer Nilesh Gohel, who oversees all dev-prod separation efforts, you established an outstanding playbook..."). Names lend credibility and show he's paying attention.
- **Signpost words for high-signal examples:** "Notably," "Specifically," "For example," "True to form."
- **Transition scaffolding:** "In addition to that," "Finally," "Another important contribution," "Beyond individual technical feats," "Overall."
- **Trailing participial clauses** that state the takeaway: "...showcasing your versatility and ability to collaborate well," "...illustrating your role as a model of engineering quality." He states what an accomplishment *demonstrates*, not just that it happened.
- **Enumeration inside prose:** gaps and grouped items are numbered "(1)... (2)..." even within a sentence.
- **Occasional formal flourish:** "from yourself" instead of "from you"; "Let us first highlight." Used sparingly, mostly in openings.
- **Narrative mode for standout work.** For major accomplishments (especially high performers), he tells a short story with tension and resolution: the setup, the obstacle ("the initial attempts led to no feed in the dev environment"), the effort, the outcome. Ordinary contributions get a crisp sentence; landmark ones get a paragraph-long arc.
- **Socratic questions in gaps for strong performers.** For high performers whose gap is "aim higher," he poses open questions rather than criticisms: "How can we experiment with different conditions and model architectures to effectively improve topline impact? How can we extend it into a more generic framework...?"

## 5. Signature Phrases

Openings (calibrated to rating — see §6):
- "Thank you [Name] for a [solid / strong / characterization] year!"
- "Congratulations [Name] on a strong year!"
- "In [year], you [met some of / completely met all / consistently greatly exceeded] the expectations for [level] [role]."

Gap preview: "The [N] gaps we identified to focus on for the coming year were (1) X and (2) Y. Before we talk about those, let's first discuss your key accomplishments."

Forward-looking: "heading into [year]," "as you continue to grow towards [next level]," "I look forward to..."

Goals stem: "Strategically, [on the HF surface / we] have identified that you own:"

Goals target paragraph: "While aiming for these strategic goals, we would also like to aim for >= [N] LRs in H1, leading to > [X]% SSv2 impact..."

Collaboration close: "In addition, we should continue to collaborate closely with [teams] to [outcome] and influence their roadmaps."

## 6. Calibration by Rating

The opening line must match the rating exactly, and the *emotional register* of the whole document scales with it:

| Rating | Opening language | Register |
|---|---|---|
| Greatly Exceeds | "you consistently greatly exceeded expectations on several dimensions of a [role]" + "This is a rating reserved for only the select few engineers per year..." | Effusive, rich adjectives ("transformative," "with finesse," "marked a new chapter"), story-driven, gaps reframed as next-level development |
| Exceeds / Meet All | "you completely met all expectations for a [role]" / "you exceeded the expectations for [role]" | Strong and appreciative; one focused stretch gap |
| Meets | "you met the expectations for [role]" | Balanced |
| Meets Some | "you met some of the expectations for [role]" | Warm opener, honest gaps, still ends each gap on momentum |
| Does Not Meet | "you did not meet the expectations for [role]" | Direct, still respectful |

Higher ratings earn more ornate, celebratory prose and narrative detail. Lower ratings keep the warmth in the opening and the accomplishments section, but the gap sections are plainer and more direct. **Never let praise in Section 1 contradict the rating.**

## 7. Evidence Sourcing (how he weights inputs)

- **Brain dump = primary truth.** His raw priorities drive narrative weight and emphasis.
- **Self-review = mine for names/metrics, but stay skeptical** of self-assessed impact level.
- **Peer feedback = supplementary only, positively skewed.** Read between the lines: if several peers gently raise the same thing, treat it as a confirming signal, not a headline. Never surface generic peer praise.
- **Mid-year feedback = continuity anchor.** Explicitly link prior commitments to current outcomes.
- **REG (level expectations) = the calibration ruler — paraphrased in his voice, never quoted, in downward reviews.** (Peer feedback inverts this — see §9.)

## 8. Things to Avoid

- Generic praise with no referent ("you're a great team player").
- Passive voice or softened accountability ("mistakes were made," "there were some challenges").
- Repeating one point in reworded forms to pad length.
- Praise in Section 1 that undercuts the rating.
- Quoting level-expectation (REG) language verbatim in downward reviews — always paraphrase there (peer feedback is the exception; see §9).
- Over-indexing on peer feedback.
- The words "genuinely," "honestly," "straightforward."
- Manufactured criticism for a strong review — if there are no real gaps, keep Section 2 short and focused on stretch opportunities.

## 9. Peer Feedback — the other three forms

Verbatim examples in `self/writing_style/peer_feedback_examples.md`: Hongbo, Claire, Andrew (cycle peer feedback), Kent (promo assessment), Alcida (free-form shout-out). Everything above still applies — evidence discipline, warmth plus directness, named people and projects — with these deltas:

### Voice shifts vs. downward reviews

- **Third person about the peer; first person for the observation.** The audience is the peer's manager or the promo committee, not the person. "Hongbo elevates the technical discourse of every room he enters"; "I encourage Claire to..." — never "you."
- **"I" carries the evidence.** Claims are framed as direct observation: "One strength I have observed from Kent...", "One thing I really appreciate about Claire is..."
- **Quote the REG here — the inverse of the downward-review rule.** In peer feedback James quotes rubric language verbatim inside quotation marks and names the level explicitly, so the reader can map behavior to level: "This aligns perfectly with the M16 expectation to 'identify and resolve misalignment... across teams'"; "While the IC14 rubric requires engineers to execute 'with some support'... Andrew operates with high independence." Strengths are often framed as operating above the current level ("operating well beyond the IC14 baseline, frequently demonstrating IC15 behaviors").
- **Coined epithets in quotes.** He names a behavior pattern with a compact quoted phrase, then unpacks it: "power-with-softness," the primary "technical voice," "air traffic control," "dissect to the heart of the issue," "acted as an owner," "customer-minded" ownership. One or two per document. ("Strategic bridge" recurs across his examples — fine to reuse across people, avoid twice in one cycle.)
- **Register runs shorter and slightly looser** than year-end reviews — conversational constructions and quick-form imperfections survive. Match that: polished enough, not lapidary.

### Cycle peer feedback (strength / adjust form)

- **"Worked together on":** bare comma-separated list of project names, no prose.
- **Strength answer = two paragraphs, one trait each.** Each paragraph runs trait statement → mechanism (how it works) → one named example with project and people → what it unlocked. First trait is typically technical or decision quality; second is collaboration posture.
- **Adjust answer = one paragraph, framed as the next-level unlock, never a deficiency.** Formula: current positive state → the structural bottleneck or missed leverage it creates → one concrete suggestion → what it frees them to do. ("Hongbo is the primary 'technical voice'... which bottlenecks Hongbo's ability to focus on organizational building... recruit a strong Staff/Principal engineer... which would free him up to drive the new UU vision he is well-positioned to lead.")
- For at-level managers, the adjust area opens with growth past level: "To continue growing beyond the M16 level, I encourage..."

### Promo assessment form

- **Unambiguous endorsement in the first sentence:** "I would absolutely endorse Kent's readiness to be at the Senior Engineering Manager level." No throat-clearing.
- **Calibrated superlative with a scope qualifier:** "one of the strongest engineering managers I have seen in a central, operationally heavy, and mission critical role."
- Performance highlight = 2–3 short paragraphs, each one strength grounded in a shared collaboration.
- Technical quality = one dense paragraph anchored to a concrete artifact (he links the actual doc).
- **Honest N/A beats manufactured evidence:** "Not that I'm aware of, but I believe Kent's team acts as great a shepherd of unity health and operations."
- Development area = the same growth formula as cycle feedback.

### Promo package — manager-authored (Workday Q1/Q2/Q3)

Derived 2026-07-10 from James's final edit of the JJ IC16 package against Leo's draft (final preserved verbatim in `self/writing_style/jj_ic16_promo_package_2026-07.md`). The governing insight: **a promo package is a case file assembled by the manager, not an essay written by one.** The manager's credibility is the asset being spent; every inflated, duplicated, or decorative claim taxes it. Rules, each anchored to a real edit:

1. **Provenance exactness — never upgrade someone's role for narrative punch.** Leo: "JJ *shaped* the cross Discovery 'More Real-Time Pinterest' vision." James: "*Following* the 'More Real-Time Pinterest' vision *from Infra and PJ technical leads*, JJ *connected the vision with practical applications*." The committee includes people who know who originated what; one inflated credit poisons every accurate claim around it. The precise contribution (connected, extended, executed, landed) is both safer and more credible.
2. **Quotes carry the case; the author's prose frames it.** James gathered full written assessments (Dafang, Nilesh, Olafur, Vikram) and let third-party voices deliver the superlatives, topline numbers, and adoption claims; his own prose sets up, connects, and maps behavior to REG. Claims Leo had asserted in James's voice ("engagement gains propagated through the funnel") moved inside quotes. Corollary: **a strong new quote can reverse a structural call** — PSv2 went from a compressed closing nod (7/9 decision) back to a full sub-block once Vikram's assessment arrived, because a firsthand Ownership/Resilience testimony is a higher evidence class than the author's summary.
3. **Evidence bullets beat aphorisms.** Leo's epigram "L1 Utility is not a project; it is a platform that compounds" became a plain bullet listing the actual new use-cases (shopping supply controls, UIC feedback loop, T&S filters) closing with "demonstrating the durability of JJ's work." "This is precisely the work of the level" was cut too. Verdict sentences the reader is meant to admire get deleted; sentences that add a checkable fact stay. (Values-weave phrases James plants himself — Win or Learn, Act As One, "treated infrastructure cost as a product" — are not aphorisms; they survive.)
4. **Business needs are concrete technical transitions with named artifacts and money.** Q1 final replaces category abstractions ("agentic engineering productivity... ML-adjacent systems") with named systems (Reflex Build Agents, Pinvestigator, Pinkerton) and states the transition mechanically ("from many heuristics CG and a simple L1 model to few ML-based CG and a more sophisticated L1 model + unified utility layer"), then closes the loop with aggregate money that funds the ML work (>$3M/yr). Bulleted lists for scope enumerations, not prose. Grand unverifiable framing ("one of the largest infra footprints in Discovery," "highest traffic surface") gets cut.
5. **Evidence lives once, in the strongest carrier.** The Content Success engineer onboarding left James's bullet because Olafur's quote names it better (Dan Sedra, autonomy). Secondary metrics that don't earn their space (head importance framework's 4-days-to-2) get dropped entirely rather than kept for completeness.
6. **Within a cross-org pillar: influence story first, craft story second**, joined by an explicit signpost ("It's important to call out that a key part of this cross-org initiative is not just technical leadership, but also careful craftsmanship.").
7. **Outcomes in final form:** "the experiment shipped with significant SSv2 and DAU/WAU gains," not "is showing significant gains."
8. **Development answer (Q3): short, positive-state, de-personalized.** 3-4 short paragraphs, not one block. "Routes the final call *to others*," never "to me" (don't center the manager in a committee-facing doc). Frame the expectation as the positive state ("have a strong technical point of view, and can bring others around a decision point"), not as a rhetorical inversion. No manager commitments ("my commitment in return...") and no prescriptive practice-stage plan — those belong in the 1:1, not the form. Pair the core gap with the adjacent skill needed to land it (decision ownership + the communication to land decisions well). End on the REG mapping.
9. **Committee-facing precision:** exact org names (P13N CG; HF and BMI surfaces), levels attached to named people (Yujiao Guo IC16), last-initial format where the full name isn't needed in James's prose (Heath V, Olafur G) with full names inside quotes. Verbatim quotes keep their punctuation and even their factual conflicts (Dafang's "ML Symposium 2025" stands next to James's "2026"); accuracy fixes happen in the author's prose only.
10. **Register confirmation:** quick-form imperfections survive in his final ("there two strong business needs") — velocity over lapidary polish, same as cycle feedback. Match it: polished enough, never gleaming.

### Free-form shout-out (shared feedback)

- Opens with one context line: "Context: Alcida and I partnered closely to lead the preparations of ML Day, and I would love to share some feedback in case it's helpful."
- One or two evidence paragraphs in the same trait → mechanism → example → outcome shape.
- Warm one-line close: "It was a pleasure working with Alcida and I look forward to opportunities to collaborate with her again in the future!"

## 10. One-Line Summary

Write like a senior engineering manager who respects the reader: open with earned, specific praise; state hard truths plainly and always tied to level expectations with named examples and metrics; use "we" for direction and "you" for performance; and close every difficult message on a path forward. For peers: same evidence bar in third person, quote the rubric to place them against level, and frame every growth area as the unlock for their next level.
