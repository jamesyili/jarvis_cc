# Hedi Xia — H1 2026 Performance Feedback (James's draft, verbatim, 2026-08-02)

> **Status:** James's own draft, logged verbatim 2026-08-02. **Supersedes Leo's inferred DRAFT v1 (2026-07-31)** and retires its verify-before-delivery block. Non-case. **First review period at IC15.**
>
> **⚠️ This doc corrects the repo — two facts to propagate.** Hedi's entry in `team_members_scope.md` was the thinnest of any tenured IC (level and workstream only); nearly everything below is net-new record.
> - **The RecSys preranking paper is ACCEPTED**, with a 15-minute oral — fourteen pages, thirteen co-authors. Leo's v1 draft flagged the venue/status as unverified; it is now confirmed. **`backlog.md` still carries "Preranking paper: confirm the RecSys 2026 deadline" as an open quick hit — that item is stale and should be closed.**
> - **Hedi is the lead author.** `team_members_scope.md` and the H2 analysis both treat the preranking paper as a team artifact without naming its author.
>
> **Pre-ER fix list (Leo flags, 2026-08-02):**
> 1. **No explicit verdict sentence.** Every other doc in the cycle states the bar plainly ("trending above IC15," "fell short of IC15 expectations," "on par with"). This one opens with "a solid first half" and never says where he lands. For a **first review period at a new level**, that absence will itself be read as an answer — decide whether it is the answer you want.
> 2. **Goal 1 asks one L15 to follow another L15's lead:** *"following Yali's overall project leadership where appropriate."* Hedi and Yali are the same level. That is a real signal about relative standing on LWS and it will land as one. If intended, say why in the conversation; if it is shorthand for "Yali owns the roadmap," phrase it that way instead.
> 3. **Departed-colleague reference:** "You partnered with **David** on dataset logging" — David is recorded as **departed**. Historically accurate so fine to keep, but confirm it reads right at delivery.
> 4. **"Leo on dataset generation"** — a colleague named Leo. Flagged only so future repo sessions do not misparse it as the assistant; no change to the text.
> 5. **Acronym drift across the cycle:** "SSv2 proxy" here, "SSv2 Proxy" in Chuxi's, "ssv2proxy" in Yali's. Normalize.
> 6. **No assignment-change clause** — Yuke's final closes with "…remain applicable regardless of project assignment." LWS is Daniel's charter and Hedi's line may move at T2.

---

## Key Accomplishments

Congratulations, Hedi, on a solid first half of 2026 and your first review period at IC15. You continued to demonstrate differentiated technical depth, particularly in first-principles ML reasoning, and translated that strength into an externally recognized paper, novel modeling work, and several positive production outcomes across LWS.

Your clearest accomplishment in H1 was lead-authoring the RecSys preranking paper, which establishes alignment and accuracy as the defining principles for the L1 layer. You carried a fourteen-page industry paper with thirteen co-authors from draft through submission, resulting in its acceptance at RecSys with a 15-minute oral presentation. This work reflects real technical depth: it required synthesizing the team's LWS practices into a coherent first-principles framework, coordinating input across many contributors, and holding a high quality bar for the writing and evidence. On the workstream itself, you contributed model iterations and experimental support across the LWS preranking stack, supported the serving and operational aspects of the system, and provided a steady senior presence on a workstream involving several junior contributors.

You were also a key technical contributor to the unimpressed track. You designed model requirements, the pairwise distillation loss, and the blocking and optimization algorithms needed to make the approach computationally practical. You partnered with David on dataset logging and Leo on dataset generation, helped Yali resolve training infrastructure issues, and helped Zili understand the loss structure and tuning options. These contributions supported launches across training-serving alignment, multi-embedding funnel efficiency, rank distillation, and early-funnel distribution improvements, with repeated SSv2 and SSv2 proxy gains. You also worked with Yidi to launch LWS unified tower/transact, delivering +0.10% total SSv2, and ramped Yali up on incorporating shopping CGS into LWS L1 utility, delivering +0.03% total SSv2 and +0.11% SSv2 proxy.

Iterative diversity was another strong example of your first-principles thinking. You reframed diversity from a deterministic post-ranking layer into an optimization problem over L1 utility and drove the approach through implementation and launch, delivering +0.17% SSv2 proxy and +0.16% impression diversity. This established a useful foundation for connecting L1 utility optimization with the broader L1 and L3 diversity strategy. Peers consistently recognized the strengths underlying this work, describing you as having "strong technical depth with a quantitative lens" and being "careful, rigorous, and dependable." They also observed that you identify risks early, improve technical decisions, and "consistently turn discussions into deliverable outcomes."

## Improvement Areas

### Translate Technical Depth into Sustained Production Impact

Your rigor and ability to reason from first principles are among your greatest strengths. The opportunity is to translate those strengths into an even more consistent cadence of experiments, decisions, and production gains. This continues part of the feedback from 2025, although you made meaningful progress through the launches completed in H1. One peer described the opportunity well: to "lean a bit more into an engineering mindset as distinct from a research one."

This does not mean lowering the technical bar. It means distinguishing between questions that require deep theoretical certainty and those where a workable solution can be tested, launched, and improved through iteration. Spending too long resolving every uncertainty before validating the central hypothesis can delay learning and reduce the impact generated by your technical ideas. In H2, time-box exploration, identify the smallest experiment that can answer the key question, and use offline and online evidence to iterate toward a stronger solution.

### Broaden Your First-Principles Influence Across Homefeed

At IC15, technical leadership does not always require being the overall lead for a large program. You can create significant leverage by proactively identifying where your modeling insights apply beyond your immediate workstream and helping teams make better technical decisions across system boundaries.

Diversity is a promising opportunity to do this. Your iterative diversity work created a useful L1 foundation; the next step is to engage proactively with the L3 diversity direction, understand which ideas transfer across layers, and bring the relevant concepts back into L1 utility and diversity modeling. This would allow your thinking to influence the broader Homefeed stack rather than remaining concentrated in retrieval and lightweight scoring.

This also requires giving collaborators sufficient context to apply your ideas independently. In your work with Zili, you provided enough implementation detail to build on earlier PRs, but not enough background on the motivation and tradeoffs, which created avoidable confusion. When working with Yali, Zili, and other partners in H2, continue being a strong technical collaborator while explaining the "why," making your recommendations clear, and ending discussions with concrete decisions and next steps. You do not need to lead every program, but I expect you to contribute proactively and take clear responsibility for converting your technical insights into outcomes.

## Goals for H2

1. **Collaborate closely with Yali to deliver additional LWS gains.** Contribute as a senior technical partner while following Yali's overall project leadership where appropriate. Own well-defined modeling problems—potentially involving training data, objectives, distillation, or offline-online validation—and convert the strongest ideas into measurable production improvements or clear technical decisions.
2. **Proactively contribute to diversity across the Homefeed stack.** Engage with Dafang and the L3 diversity work, develop a deep understanding of the approaches being explored there, and identify concepts that can improve L1 utility and diversity modeling. Bring promising cross-layer ideas through concrete design, evaluation, and iteration.
3. **Advance foundational improvements in lightweight scoring.** Apply your first-principles strength to important LWS modeling or systems problems, which could include unimpressed data, teacher distillation, foundation models, or another high-leverage direction. Own or co-own clearly scoped technical work and carry it through experimentation to a production outcome or decision-quality evidence.
4. **Increase iteration speed and strengthen technical alignment.** Time-box exploratory work, define crisp hypotheses and evaluation criteria, and use staged experiments rather than waiting for a fully optimized first solution. Give collaborators the broader motivation and tradeoffs behind your recommendations, communicate decisions and next steps explicitly, and continue helping junior contributors build confidence and independence.
