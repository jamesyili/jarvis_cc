# Study Plan — LLM System Interview book, calibrated for OpenAI Integrity EM onsite

**Source:** `interview_prep/llm_system_interview.md` (27K lines, 31 chapters, 11 parts)
**Seat shape:** Sr EM on Integrity Foundations — ML classifier stack for behavioral harms. Not an IC / infra-IC seat.
**Total study budget:** ~50 hrs across 3–4 weeks (assumes onsite confirmed after May 27 recruiter call).

---

## Bottom line

**Read deeply (10 chapters):** Ch 1, 2, 22, 23, 24, 25, 26, 27, 28, 31
**Skim for vocabulary (5–6 chapters):** Ch 3, 15, 19, 20, 21, 29
**Skip / one-liner only (15 chapters):** Ch 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 30

The book's own "Path 3 — Applied / Product Engineering" matches the seat closely (Ch 1, 2, 15, 19, 20–22, 23–25, 26, 27, 31). I'm de-weighting 15 + 19 (inference infra — IC work, not EM work) and adding 28 (RL from verifiable rewards = constitutional AI substrate, load-bearing for Integrity).

---

## Tier 1 — Read deeply (10 chapters, ~30 hrs)

These are the chapters where an interviewer will probe and a generic answer will land you on the "good not great" pile.

| Ch | Topic | Why it matters for THIS seat |
|---|---|---|
| **1** | LLM Systems Interview (landscape, roles) | Sets the bar. Read in first session — calibrates everything else. |
| **2** | How to Approach an LLM System Design Question | Framework. Internalize the four-axis requirement template. Your failed Anthropic loop missed depth + adversarial resolution — this chapter is the fix. |
| **22** | Mid-Training and Post-Training Data | This is where safety classifiers get trained / fine-tuned. Direct seat content. |
| **23** | Designing an Evaluation | **Eval IS half of integrity work.** Most operational time on this team will be eval design / curation / contamination handling. |
| **24** | Benchmarks You Must Know | Vocabulary floor — be able to name and critique the standard safety / capability benchmarks. |
| **25** | Validity, Contamination, Real-World Use | The hardest part of eval — what makes safety evals actually predictive. Will absolutely come up. |
| **26** | Supervised Fine-Tuning | Foundational; you'll be expected to talk about SFT vs RLHF trade-offs with conviction. |
| **27** | Preference-Based Alignment (RLHF) | Load-bearing. Safety classifiers either consume RLHF outputs or generate the preference data. |
| **28** | RL from Verifiable Rewards | **Constitutional AI lives here.** Anthropic's constitutional classifier work is the public reference. OpenAI uses related approaches. Must internalize. |
| **31** | Designing a Fine-Tuning and Alignment Pipeline | **This is literally the seat's work.** Treat this as a mock-interview drill at end of Week 4. |

## Tier 2 — Skim for vocabulary (5–6 chapters, ~12 hrs)

You need to talk credibly about these but won't be asked to derive them as an EM.

| Ch | Topic | Skim target |
|---|---|---|
| **3** | Transformer Architecture Essentials | Vocabulary + the one-line "what is QKV / decoder-only / why this matters for classifiers." Don't derive flash attention. |
| **15** | Inference Workload | Understand prefill vs decode, TTFT vs throughput. Latency-relevant for input classifiers (your team would own inference budget conversations). |
| **19** | Compression for Deployment | Quantization / distillation vocab. Your fast classifiers will be small distilled models. |
| **20** | Pre-Training Data Pipelines | Where harm data gets filtered out upstream — directly upstream of what your team does. |
| **21** | Data Filtering and Deduplication | Same upstream relevance. Deduplication failures create training-data poisoning vectors. |
| **29** | Production LLM Serving Stack | One-pass read; understand where your classifiers sit in the request path. Don't memorize. |

## Tier 3 — Skip / one-liner only (15 chapters, ~8 hrs total for cursory awareness)

These are IC / infra-IC topics. Read each chapter's "The Take" paragraph and "Key Takeaways" bullets only. Total ~30 min per chapter.

- **Ch 4** Hyperparameters — know the names exist; don't derive.
- **Ch 5** Stability tricks — research / IC.
- **Ch 6–7** MoE — know what MoE is, don't go deep.
- **Ch 8–10** GPU architecture / single GPU fast / custom kernels — pure IC.
- **Ch 11–12** Multi-GPU / parallelism — pure infra-IC.
- **Ch 13–14** Scaling laws / Chinchilla — research vocab. Know "20 tokens per parameter" exists.
- **Ch 16** KV cache reduction — inference IC.
- **Ch 17** Beyond the transformer — research frontier.
- **Ch 18** Speculative decoding — inference IC.
- **Ch 30** Designing a pre-training run — out of scope (your team consumes, doesn't pre-train).

---

## 4-week schedule (if onsite confirmed)

**Pacing assumes ~2 hrs/day study + 1 mock-interview drill per week.**

### Week 1 — Framework + foundations (~8 hrs)
- Ch 1 (1 hr) — interview landscape
- Ch 2 (3 hrs) — framework, deeply. **Internalize the four-axis template + the timing breakdown** (the timing chart in the prep section).
- Ch 3 skim (2 hrs) — transformer essentials, vocabulary only
- **Drill:** time yourself on a 45-minute mock for "design a safety classifier for an LLM API." Compare against `interview_prep/system_design/05_defense_in_depth_full.md`.

### Week 2 — Data + evaluation (~10 hrs)
- Ch 22 deep (3 hrs) — mid/post-training data
- Ch 23 deep (3 hrs) — designing an evaluation
- Ch 20–21 skim (2 hrs) — data pipelines + filtering
- Ch 24 deep (2 hrs) — benchmarks
- **Drill:** "Design an evaluation framework for a multimodal harm classifier." Time-boxed 45 min.

### Week 3 — Alignment + RLHF (~10 hrs)
- Ch 25 deep (3 hrs) — validity, contamination
- Ch 26 deep (2 hrs) — SFT
- Ch 27 deep (3 hrs) — RLHF
- Ch 28 deep (2 hrs) — RL from verifiable rewards
- **Drill:** "Design an RLHF pipeline that produces calibrated harm classifiers without amplifying labeler bias." Time-boxed 45 min.

### Week 4 — Integration + seat drills (~10 hrs)
- Ch 31 deep (3 hrs) — fine-tuning + alignment pipeline (THE seat drill)
- Ch 29 skim (2 hrs) — production serving
- Ch 15 + 19 skim (2 hrs) — inference workload + compression vocab
- Mock loop (3 hrs): 45-min system design + 30-min cross-functional / stakeholder case + 30-min hiring case
- Review Appendix C checklist + reproduce verbally

### What to skip in week 4 even if anxious
- Don't go deep on Ch 4–14 — those won't be on the EM loop.
- Don't try to re-derive FLOP budgets from first principles. The book says "interview asks Sr EMs for judgment, not arithmetic." Trust that.

---

## Calibration

**You probably need 30 hrs minimum, 50 hrs ideal.** If the onsite lands in week 3 from now and you have other workstreams, drop Tier 2 skim chapters and just do Tier 1 deep. The seat's actual day-to-day is eval + alignment data + classifier design — not parallelism or kernel writing.

**Where this differs from a generic ML EM onsite:** the book is biased toward training/inference infra. Half of it (Ch 4–14, 16–18) is IC infrastructure work. Don't get sucked into that just because the chapters are interesting. The Integrity EM seat will probe leadership, eval, classifier judgment, and alignment data — in that order.

**Highest-ROI prep activity:** mock interviews on the four 45-minute drills above. Reading the book without drilling gets you to "informed candidate." Drilling gets you to "this person has actually answered these before."
