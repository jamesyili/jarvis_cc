# Learning progress

Updated: 2026-09-06 15:55, Pacific time.

## Active course and cursor

- Course: LLM×RecSys + Reflex, `learning_agenda.md` (current 14-week program).
- Lesson: W01 — the generative-recommendation map.
- Source: `lessons/w01_generative_rec_map.html`, map in §2; use the correction
  notice before teaching the old classification or numerical claims.
- Block: `W01-articulation-01`, explain and defend a semantic-ID retrieval design.
- Current activity: skill refinement; practice is paused. Infer learning versus
  practice from James's next substantive message, without requiring a mode label.
- Status: first architecture prompt delivered; no answer or critique yet. James
  requested a clear separation of learning/help from coached practice.
- Paused practice prompt: "We currently use a two-tower model and ANN retrieval. You're
  proposing a TIGER-style alternative. Walk me through the architecture, what
  each model learns and from which loss, and how a request becomes a set of
  recommended items. What would you need to demonstrate before choosing it
  over the existing system?"
- Active learning question: none; this turn is about the skill's behavior.
- Next action: follow his intent. If he asks to learn or for help, explain without
  grading or articulation critique and keep the practice prompt paused. If he
  returns to answering, give room for his explanation, then critique technical
  correctness, design reasoning, exact words/referents, and organization. Track
  supported rehearsal separately from independent evidence without penalties.
  W1 remains incomplete. Search-01 is deferred; its full
  numerical explanation and diagnostic question were prepared but not delivered
  before the user clarified his preferred format.

## Session constraints

- James is on his phone for about 90 minutes, waiting at Ethan's soccer practice.
- Current request: test lesson 1 display, build a continuation skill, and begin
  learning. Clarifying questions are welcome as needed, in plain text.
- Research-arm leadership analysis is being handled with Claude Fable; not part
  of this learning session.
- Visual preference (James, 09:10–09:15): "I do want you to try to visualize since
  that's a lot more effective for learning." Keep trying a compatible visual;
  text-only was Leo's fallback decision, not James's preference. A static PNG was
  the second display attempt and also FAILED: James's second screenshot shows a
  gray image placeholder with a reload icon, no diagram. This is an observed load
  failure, not evidence of the same color bug. Third attempt SUCCEEDED: native
  Mermaid directly in the conversation. James: "Yes this image works now!"
  Prefer small native Mermaid diagrams on this phone; no repeat display question.
- Earlier inline HTML display: FAILED on James's phone in the dark appearance, 2026-09-06.
  James: "I just see black." Screenshot observation: TIGER/OneRec buttons visible,
  central diagram labels and selected HSTU control unreadable against black;
  faint connector lines remain. Cause unverified. Ordinary surrounding chat is
  readable. Host browser tests at 320/360/736px in light/dark had passed, which
  did not predict the actual phone result. Essential explanations stay in chat;
  try direct text-based diagrams next. Do not repeat local image links as if the
  phone has already demonstrated access to those files.

## Evidence and source cautions

- 2026-09-06 15:55 mode boundary, explicit from James: learning concepts and
  coached open-ended practice are different activities. Asking for explanation
  or help, including being stumped mid-practice or consulting side sources, must
  receive teaching rather than critique. Infer intent naturally; a pending prompt
  does not make subsequent questions graded answers. Preserve useful terminology
  clarification while withholding performance/communication assessment in learning.
  This correction supersedes any earlier wording that made critique the default
  for every learning turn. No practice performance is evidenced by this request.

- 2026-09-06 15:51 explicit teaching contract: ask open-ended questions about
  architecture, loss functions, and system design for future frontier-AI-lab
  interviews; get James to say more, then critique both accuracy and articulation.
  Track exact terminology, whether descriptions identify the right operations,
  and whether an interviewer can follow the explanation. This refines the format
  beyond merely increasing quiz difficulty. Align with existing senior ML
  engineering leadership context; no active recruiting campaign or recurring
  mock schedule was requested. Preserve clarity, visuals, and learning depth.
  Original request: "Get me to say more, and then you critique me on how I said
  it, not just on the accuracy of my answer, but also on the type of words I'm
  using and whether or not I'm describing it correctly."

- Foundations-02 answer, verbatim: "Of course not. The parameters didn't change.
  This might be too easy for me." Correct: computed gradients do not update
  parameters without an optimizer update. Explicit difficulty correction: skip
  elementary training-loop recall, retain plain explanation, increase mechanism
  and diagnostic depth. This establishes the specific distinction, not broad
  hands-on optimization or teacher-forcing mastery.
- Search-01 prepared: for a toy two-token SID, ordinary unsmoothed summed token
  cross-entropy equals negative log full-sequence probability. Do not teach the
  false dichotomy that token likelihood and full-SID likelihood are different
  objectives. Ranking metrics and finite-beam approximation are separate issues.
  Constructed example (not paper data): target first-token probability .40→.25;
  correct second-token probability conditional on that prefix .40→.90; complete
  target probability .16→.225; first-token rank 2→3 under beam width 2. Its
  likelihood improves while its prefix becomes unsearchable at serving time.
  The example establishes prefix loss; without other leaf scores it does not
  establish the target's exact global item rank or baseline final recall.
  Related primary evidence: Understanding Semantic IDs, §§4–5,
  https://arxiv.org/html/2607.24995v1 (July 2026 preprint; three Amazon domains).

- Foundations-01 answer, 2026-09-06, verbatim: "Yes. The RQ-VAE decoder is only
  used to ensure the SIDs encode the original semantic meaning from the input
  vectors, not used during SID generation or in the transformer prediction phase."
  Assessment: correct training/serving boundary and reason for reconstruction.
  Narrow correction: reconstruction encourages preservation of the input
  representation; it does not guarantee complete semantics or recommendation
  relevance. No evidence yet of gradient, beam-search, or collaborative-loss mastery.
- James supplied a preferred explanatory example: foundation first, systems
  separated by role, explicitly named inputs/outputs, then a data-flow summary.
  Original preserved in `archive/2026-09-06-encoder-decoder-explanation-supplied.md`.
  Adopt the structure while correcting encoder=mandatory compression/single
  vector, literal genre meanings for codes, and fixed-during-learning codebooks.
- Foundations-02 prepared example: observed next-item SID [14,82,101,0]; decoder
  uses correct preceding target tokens during teacher forcing. Token cross-entropy
  measures probability of the correct token; backward computes gradients and an
  optimizer updates recommendation encoder/decoder weights and token embeddings.
  SID assignments/codebooks stay fixed in original TIGER's second-stage training.
  Sources: TIGER §3.2, original Transformer §3.1 (shifted targets and causal mask),
  https://arxiv.org/html/1706.03762v7 and
  https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html

- Foundations-01 request, 2026-09-06: James identified two gaps: beam search
  (SID generation and LLMs), and RQ-VAE plus engagement/CF signals. He reported
  using "encode" and "decode" interchangeably and being misunderstood in
  technical interviews. This is a specific self-reported terminology concern,
  not evidence that his established attention/recsys knowledge is weak.
- Prepared distinction: content encoder maps item text to an embedding; RQ-VAE
  encoder maps that embedding to a latent vector; residual quantization selects
  code indices; RQ-VAE decoder reconstructs the original content embedding from
  summed code vectors. The separate recommendation Transformer encodes historical
  SID tokens and predicts next-item SID tokens. Beam search selects sequence
  hypotheses from its probabilities. Full SID to item ID is a table lookup.
- Foundations sources inspected live:
  - RQ-VAE residual mechanism and reconstruction training:
    https://arxiv.org/html/2203.01941v2 (image paper; TIGER adapts the input/target).
  - Beam search, greedy and sampling distinction:
    https://huggingface.co/docs/transformers/generation_strategies
  - LETTER (CIKM 2024): tokenizer uses content reconstruction plus contrastive
    alignment of quantized item vectors with pretrained collaborative embeddings,
    and a diversity objective. Collaborative signal can shape SID assignments
    through the loss; it need not be raw per-user history input to the tokenizer.
    https://arxiv.org/html/2405.07314v2
  - LC-Rec: collaborative alignment during recommendation-model training is a
    different intervention from LETTER's collaborative SID-assignment objective.
    https://arxiv.org/html/2311.09049v3
- Team-reading backlog: James requested Understanding Semantic IDs and the
  original SID paper (interpreted as TIGER from the current discussion).
  Created Notion parent "Team reading recommendations - Semantic IDs" in
  2Backlog with both paper links as subtasks. Notion is the live task record:
  https://www.notion.so/3d313be907ce81ab95b1c4d642ac6e74

- Map-02 follow-up, 2026-09-06: James: "it depends on how granular of SID we
  decide to decode at"; asked whether TIGER ablates stopping prefixes or item
  selection within prefixes and what later SID literature does. Correct as a
  broader design axis, but original TIGER uses complete unique IDs. Do not treat
  his proposed design as an observed implementation of TIGER.
- Map-03 research (primary papers inspected live, 2026-09-06):
  - TIGER v3 §4.5 leaves prefix matching after invalid IDs as future work. Appendix
    E qualitatively reports trying longer IDs (6 codes × 64 vs 4 × 256), not a
    per-prefix stopping-depth/item-selector sweep. https://arxiv.org/html/2305.05065v3
  - COBRA §3.4: beam-search coarse IDs; condition a dense query on each ID; ANN
    within that ID's associated items; BeamFusion mixes ID beam and dense scores.
    Its industrial ablation changes from 2-level 32×32 IDs plus dense to 3-level
    256×256×256 IDs without dense, so it is not a clean stopping-depth ablation.
    https://arxiv.org/html/2503.02453v1
  - GRID §4.2/Table 7 compares an extra collision token with random item selection
    from colliding SIDs. Extra token wins slightly on its public benchmarks;
    Beauty Recall@10 0.0597 vs 0.0591. This is a collision bucket, not a broad
    arbitrary prefix. Table 3 varies learned codebook depth/width, not inference
    truncation of a fixed SID. https://arxiv.org/html/2507.22224v1
  - Understanding Semantic IDs (July 2026 preprint), ISD: uses an independent
    user-specific item ranking to support prefixes before beam pruning and order
    generated items afterward. Evaluated on three Amazon domains; do not present
    as production validation or optimal early-stop depth. Its costly diagnostic
    and its actual efficient ISD method differ; don't conflate their formulas.
    https://arxiv.org/html/2607.24995v1
  - LIGER's author code reports varying number of generated candidates before
    dense reranking; this is candidate-budget, not stopping-prefix evidence.
    https://github.com/facebookresearch/liger/blob/main/README.md

- Map-01 answer, 2026-09-06: James correctly inferred that pure generative
  retrieval removes serving-time ANN lookup and proposed SID→Pin-ID key-value
  resolution. He asked how pins are selected when one SID matches several pins.
  His phrase "KV cache" may mean an ordinary key-value store; clarify terminology
  without scoring that as an attention-mechanics misconception. His inference
  "and therefore an indexing step" needs narrowing: ANN-index building goes,
  but code assignment and catalog-map maintenance remain.
- Prepared correction: TIGER §3.1 appends a token to disambiguate code collisions;
  full IDs uniquely identify items. The model predicts that token as part of the
  target sequence. Beam search generates several candidate sequences. §4.5 filters
  invalid IDs; do not claim original TIGER used a constrained-decoding trie.
  Appendix E explicitly names both lookup hash tables. Verified against
  https://arxiv.org/html/2305.05065v3 on 2026-09-06. These corrections have not
  yet been demonstrated by James.

- Prior record LR-0001: strong transformer forward-pass and recsys architecture
  knowledge; training mechanics were the recorded gap. RoPE/ALiBi exposure was
  explicitly distinguished from demonstrated mastery. Do not infer new mastery.
- The newer agenda sets W1 as the generative-recommendation map; the June
  transformer's NOTES cursor belongs to the older course and must not override it.
- W1's three categories overlap: semantic IDs concern representation/retrieval;
  HSTU concerns sequence modeling; cascade integration concerns system scope.
  The old "share almost no machinery"/mutually exclusive classifier is misleading.
- OneRec's current technical-report abstract (v4, arXiv:2506.13695, checked
  2026-09-06) reports +0.54%/+1.24% App Stay Time on different apps and 25% QPS.
  The old lesson's blanket sub-1% quiz and full-cascade-at-400M framing need
  version/surface/traffic checks before use. Do not teach those old figures as current.
- HSTU's abstract reports a 12.4% improvement in online metrics without naming
  them there; do not compare it directly to OneRec's App Stay Time.
- RecGPT classification remains unverified; consult its actual current design
  before assigning it a category.

## History

- 2026-09-06: current agenda and prior-knowledge record loaded; W1 opening map
  prepared. No learner answers recorded. Display test is the first pending step.
- 2026-09-06 09:06: James reported the black diagram and supplied a screenshot;
  observed rendering failure transcribed above. Switched to chat and prepared
  `W01-map-01`. This is a delivery correction, not learner assessment evidence.
- 2026-09-06 09:15: map-01 answer assessed; substantive follow-up about SID
  collisions supersedes the original plan to go straight to RQ-VAE. Prepared
  map-02 and `sid-to-pin.png` in this task's visualization directory. Updated
  `$learn` to retain the explicit preference for visuals after a rendering failure.
- 2026-09-06 09:25: static image load failure transcribed; third display route
  prepared (Mermaid). Researched original TIGER and later prefix/item-selection
  work for James's question; key evidence and limitations retained above.
- 2026-09-06 09:57: James confirmed Mermaid works; updated learn's device default
  and terminology teaching guidance. Added two requested team-reading papers to
  Notion via the existing WSL connection. Prepared foundations-01, replacing the
  resolved display prompt with the RQ-VAE-decoder removal transfer question.
- 2026-09-06 11:28: foundations-01 answer assessed; recorded explanation-style
  preference and retained the supplied example with technical caveats. Prepared
  foundations-02 on teacher forcing, loss, backward, and optimizer updates.
- 2026-09-06 15:48: James rejected elementary optimizer-step question as too easy;
  updated learn's difficulty calibration. Prepared search-01 counterexample and
  a diagnostic question connecting sequence likelihood to finite-beam retrieval.
- 2026-09-06 15:51: James clarified open-ended technical articulation practice as
  the desired format. Updated learn and agenda; superseded the undelivered search
  quiz with articulation-01. No interview-readiness or communication mastery claimed.
- 2026-09-06 15:55: refined learn into inferred learning/practice modes with help
  interrupting critique. Preserved articulation-01 as a paused prompt rather than
  treating skill-design questions as an answer or forcing immediate rehearsal.
