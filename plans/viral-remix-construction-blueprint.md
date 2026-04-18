# Viral Remix — Construction Blueprint

**Objective:** Build a faceless short-form video pipeline that scrapes viral celebrity/news/entertainment clips, VLM-annotates them, and produces commentary-overlaid remix videos for a new sister channel to @rekko.ai. MVP exit = 3–5 videos posted end-to-end via the pipeline.

**Source plan:** `work+self/projects/viral_remix_plan.md`
**Date:** 2026-04-17
**Owners:** Daniel (primary, 10–15 hrs/wk), James (co-pilot, 5–10 hrs/wk)
**Target repo:** New repo, created in Step 1 (tentative: `jamesyili/viral-remix` or `jamesyili/<channel-name>`). This plan lives in `leo/plans/` until the target repo exists, then moves to `<target-repo>/plans/`.
**Pre-flight:** git ✓, gh ✓ (authenticated as jamesyili). Target repo will be created in Step 1. Full branch/PR/CI workflow mode enabled.

---

## Step Graph + Parallelism Summary

```
STEP 0 (gate)
   │
   ▼
STEP 1 (scaffold)
   │
   ▼
STEP 2 (scraper) ────────────┐
   │                         │
   ▼                         │
STEP 3 (clip extraction)     │
   │                         │
   ▼                         │
STEP 4 (VLM annotation) ────► STEP 5 (clip DB) ◄──┐
   │                         │                    │
   └─────────┬───────────────┘                    │
             ▼                                     │
         STEP 6 (retrieval) ◄──────────────────────┘
             │
             ├──► STEP 7 (script gen) ────┐
             ├──► STEP 8 (TTS) ───────────┤
             └──► STEP 9 (stitch/render)  │
                         │                │
                         ▼                │
                  STEP 10 (QC + publish) ◄┘
                         │
                         ▼
                  STEP 11 (first 3–5 videos)
```

**Parallel opportunities:**
- Steps 4 & 5 (VLM annotation interface + DB schema) — can proceed in parallel after Step 3 with interface contracts defined upfront
- Steps 7, 8, 9 (script / TTS / stitch) — can proceed in parallel after Step 6 stub interface is defined

**Serial-only:** Step 0 → Step 1 → Step 2 → Step 3. Step 10 depends on 7+8+9. Step 11 depends on 10.

**Total estimated effort:** ~80–120 hours of nominal build work across Daniel + James. **Realism buffer: assume 120–180 hrs / 10–14 weeks in practice** — adversarial review flagged estimates low by 30–50%, and James's Pinterest day-job load makes interrupts likely. Step 0 is ~8–12 hrs (non-code).

**"Full branch/PR/CI workflow mode" (preamble clarification):** Every code step gets its own branch (`step-<n>-<slug>`), a PR to `main` with CI required (ruff + mypy + pytest green), a description referencing this plan's step number, and squash-merge on approval. Each PR is one step. No direct commits to `main`.

---

## Step 0 — Pre-Build Gate (Research, Legal, Decisions)

**Dependencies:** None. Must complete before any code step.
**Parallel with:** None.
**Model tier:** N/A (non-code, human decision work).
**Owner:** Shared (James + Daniel).
**Estimated effort:** 8–12 hrs total.

### Context brief
Before any code is written, four pre-conditions must be satisfied. These close the operating-plan gap and retire the largest risks cheaply. The outputs of this step feed channel identity, voice design, and cost targets into later steps. If any output surfaces a kill-condition, rescope or abandon here.

### Tasks
1. **Daniel — Reverse-engineer 10 successful channels.** TikTok + YouTube Shorts, celebrity/news/entertainment niche. Spreadsheet at `research/competitor-analysis.xlsx` (or Google Sheets link committed to repo) with columns: channel name, platform, subscriber count, posts/day, posts/week, avg video length, hook format (first 2 seconds), commentary-to-clip ratio estimate, editorial POV, recurring video formats, intro/outro pattern, caption style, breaking-news lag time. **Budget: 4–6 hrs.**
2. **James — IP attorney consult.** Book + attend 1-hour consult. Brief attorney on BOTH sides: (a) **publish-side** — commentary-heavy faceless editorial, celebrity/news/entertainment niche, ≥2:1 commentary-to-footage ratio, short clip spans (3–5s), YouTube Shorts first; (b) **ingest-side** — scraping YouTube for raw video (yt-dlp fallback) violates YouTube ToS independent of publish-side fair use. Goals: stress-test fair-use posture, confirm right-of-publicity mitigations, get source-attribution recommendation, assess ingestion-ToS exposure + mitigation (API-only vs. yt-dlp-fallback). **Budget: $500–1K + 2 hrs prep+attend.**
3. **Both — Channel identity + sub-niche + voice decisions.** Working session (2 hrs). Output: `docs/brand.md` with (a) channel name, (b) 2–3 sub-niche focus formats (e.g., "celebrity relationship drama breaking news," "retrospective deep dives," "reaction-style commentary"), (c) voice/persona definition (cloned voice vs. off-the-shelf ElevenLabs; if cloned, whose?), (d) intro/outro concept.
4. **James — Cost spike on VLM annotation.** Manually annotate 10 keyframes via Gemini Flash API. Extrapolate to $/clip at MVP scale (10K clips). Document in `research/cost-model.md`. **Budget: 2 hrs.**
5. **James — Google Cloud + YouTube upload credentials setup.** Create GCP project. Enable YouTube Data API v3. Configure OAuth consent screen with `youtube.upload` scope (restricted scope — requires app verification for >100 users; MVP is under cap but still requires consent-screen completion). Generate OAuth 2.0 credentials. Test token-refresh flow with a dry-run upload to a throwaway channel. Commit `.env.example` with variable names only (no secrets). **Budget: 1–2 hrs.** Blocks Step 10.

### Exit criteria
- [ ] Competitor spreadsheet delivered; synthesis summary identifying 2–3 channel-brand anchors (cadence, hook pattern, voice) to emulate
- [ ] Attorney consult complete; written summary + any material constraints captured in `docs/legal.md` (covers BOTH publish-side fair use AND ingest-side ToS exposure)
- [ ] `docs/brand.md` filed with channel name, sub-niches, voice decision
- [ ] `research/cost-model.md` shows projected $/month for VLM annotation at 1K and 10K clip scale
- [ ] GCP project + OAuth consent + `youtube.upload` scope configured; throwaway-channel upload test succeeds
- [ ] **Go/no-go decision made and documented.** If any output surfaces a kill condition (attorney flags structural risk on either publish or ingest, cost model shows >$500/mo at MVP scale, voice decision can't converge, OAuth verification blocked), rescope or abandon before Step 1.

### Rollback strategy
N/A — no code written. Abandon = delete `docs/` and `research/` files; write a short post-mortem in `/home/james/src/leo/system/session-logs/` capturing why.

---

## Step 1 — Repo Bootstrap + Scaffold

**Dependencies:** Step 0 complete with go decision.
**Parallel with:** None.
**Model tier:** Default (Sonnet).
**Owner:** James (has git/gh setup).
**Estimated effort:** 2–3 hrs.

### Context brief
Create the new private repo on GitHub under `jamesyili/<repo-name>` (name decided in Step 0). Bootstrap a Python project with modern tooling, CI, and Claude Code integration. Port the `work+self/projects/viral_remix_plan.md` + `Step 0` outputs (`docs/brand.md`, `docs/legal.md`, `research/*`) into the new repo's `docs/` and `research/` directories. This plan file moves from `leo/plans/` into `<new-repo>/plans/`.

The repo stack should mirror Rekko's proven choices so porting is cheap: Python 3.12, `uv` for package management, Pydantic v2, pytest + ruff + mypy, GitHub Actions CI.

### Tasks
1. Create private repo `gh repo create jamesyili/<name> --private --description "Viral remix pipeline"`
2. Initial commit with `.gitignore` (Python + media files), `LICENSE`, `README.md` (placeholder — to be expanded in Step 11), `CONTRIBUTING.md`
3. Project skeleton:
   - `pyproject.toml` (uv-compatible, Python 3.12+)
   - `src/viral_remix/__init__.py`
   - `tests/` with pytest scaffolding
   - `.ruff.toml`, `mypy.ini` or inline config
4. GitHub Actions CI (`.github/workflows/ci.yml`): ruff, mypy, pytest on every PR
5. `CLAUDE.md` at repo root describing architecture + invoking skills (`videodb`, `video-editing`, `fal-ai-media`, `brand-voice`, `data-scraper-agent`, `eval-harness`, `tdd-workflow`)
6. `.claude/settings.json` (repo-scoped) with sensible permissions (allow pytest, ruff, uv, gh). `.claude/settings.local.json` reserved for operator-personal overrides, gitignored.
7. Directory structure stubs: `src/viral_remix/{scrapers,extraction,annotation,db,retrieval,generation,stitch,publish}/__init__.py`
8. Port `docs/brand.md`, `docs/legal.md`, `research/*`, and this `plans/` file from Leo
9. Initial protected-branch rules on `main` (require PR, require CI pass)
10. **Secrets management:** `.env.example` committed with all var names (no values) — `GEMINI_API_KEY`, `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`, `YOUTUBE_OAUTH_CLIENT_ID`, `YOUTUBE_OAUTH_CLIENT_SECRET`, `YOUTUBE_OAUTH_REFRESH_TOKEN`, `POSTGRES_URL`. `.env` gitignored. GitHub Actions secrets configured for CI (`gh secret set ...`). Pre-commit hook (`detect-secrets` or `gitleaks`) scans staged files.
11. **Reproducibility:** commit `.python-version` (pin to 3.12.x), commit `uv.lock` for exact dependency resolution, add a `CONTRIBUTING.md` section on local-machine setup steps.

### Verification commands
```bash
uv sync
uv run pytest   # should pass (empty test suite ok)
uv run ruff check .
uv run mypy src/
gh repo view jamesyili/<name>
```

### Exit criteria
- [ ] Repo exists on GitHub, private, `main` protected
- [ ] `uv sync` succeeds from clean clone
- [ ] CI green on initial commit
- [ ] `CLAUDE.md` references the skills to be used per subsystem
- [ ] `plans/viral-remix-construction-blueprint.md` lives in new repo
- [ ] `docs/brand.md`, `docs/legal.md`, `research/*` ported

### Rollback strategy
`git revert` the initial commits OR `gh repo delete` if scaffold is broken. No dependencies yet on this state.

---

## Step 2 — YouTube Shorts Scraper (Port + Extend)

**Dependencies:** Step 1.
**Parallel with:** None (Step 3 depends on its output).
**Model tier:** Default (Sonnet). Invoke `/data-scraper-agent` skill for scraper patterns.
**Owner:** Shared (Daniel leads).
**Estimated effort:** 6–10 hrs.

### Context brief
Port Rekko's viral discovery scrapers and specialize for YouTube Shorts ingestion. The source code lives at:
- `/home/james/src/rekko.ai/src/rekko_server/scrapers/viral_discovery.py` (155 lines) — discovery logic
- `/home/james/src/rekko.ai/src/rekko_server/scrapers/viral_broll.py` (1,011 lines) — main scraper
- `/home/james/src/rekko.ai/src/rekko_server/scrapers/viral_broll_downloader.py` (72 lines) — download
- `/home/james/src/rekko.ai/src/rekko_server/scrapers/viral_mapper.py` (294 lines) — mapping layer

License check: Rekko is James's own repo — no license barrier. Refactor during port: the Rekko code is prediction-market-biased. Strip prediction-market-specific code paths; retain the generic viral-discovery + YouTube Shorts ingestion spine.

MVP scope: YouTube Shorts only (no TikTok in Step 2 — that's Phase 2 per the plan). Sort by view count / engagement velocity, rolling 30-day window for MVP. Store raw videos to local filesystem or S3 with a manifest file (`manifest.jsonl`) tracking `{video_id, source_url, title, channel, views, duration, ingested_at, local_path, sha256}`.

### Tasks
1. Port the 4 files into `src/viral_remix/scrapers/`. Keep module-level APIs but strip Rekko-specific imports and paths.
2. Add YouTube Shorts-specific ingestion: filter by `shortFormVideo=true` or duration <60s. Use YouTube Data API v3 (quota: 10K units/day free). Fallback: `yt-dlp` for metadata + download if API quota exhausted.
3. Dedupe: compute SHA-256 of video file on ingest; skip if already in manifest.
4. Storage: `data/raw/{yyyy-mm-dd}/{video_id}.mp4` + `data/raw/manifest.jsonl`.
5. CLI: `uv run python -m viral_remix.scrapers.youtube --limit 100 --sort-by views --window-days 30`.
6. Tests: mock YouTube API + test dedupe, storage path construction, manifest append.
7. Rate limiting + retry with exponential backoff; capture ToS-violating behaviors in a `docs/scraping-posture.md` doc (transparency for attorney + ops).

### Verification commands
```bash
uv run pytest tests/scrapers/
uv run python -m viral_remix.scrapers.youtube --limit 5 --dry-run
uv run python -m viral_remix.scrapers.youtube --limit 5   # actually ingest 5 videos
ls data/raw/$(date +%Y-%m-%d)/   # should contain 5 mp4 files
wc -l data/raw/manifest.jsonl   # should show 5 entries
```

### Exit criteria
- [ ] 100 YouTube Shorts ingested cleanly in <30 min
- [ ] Dedupe verified (re-run ingest → no new files)
- [ ] Manifest well-formed JSONL
- [ ] Unit tests ≥80% line coverage on scraper module
- [ ] `docs/scraping-posture.md` filed

### Rollback strategy
Revert PR. Clear `data/raw/` if corrupted. Rekko's scrapers remain untouched — no risk to the source system.

---

## Step 3 — Clip Extraction (Shot Boundary Detection)

**Dependencies:** Step 2.
**Parallel with:** None (Steps 4 and 5 depend on this).
**Model tier:** Default (Sonnet).
**Owner:** Daniel.
**Estimated effort:** 4–6 hrs.

### Context brief
Split ingested videos into 3–5 second clips via shot-boundary detection. Use PySceneDetect as the default algorithm (battle-tested, free). Each clip gets extracted as its own `.mp4` + 3 keyframes (first, middle, last) as `.jpg` for downstream VLM annotation. Store clips at `data/clips/{source_video_id}/{clip_idx}.mp4` and keyframes at `data/keyframes/{source_video_id}/{clip_idx}/{frame_idx}.jpg`.

Constraint: if a shot is >5s, split into overlapping 4-second sub-clips with 0.5s overlap. If a shot is <3s, merge with adjacent until ≥3s. This enforces the fair-use clip-length guardrail from `docs/legal.md`.

### Tasks
1. Add `scenedetect` + `opencv-python` to `pyproject.toml`.
2. `src/viral_remix/extraction/segment.py`: function `segment_video(path) -> list[Clip]` using `ContentDetector` + `AdaptiveDetector`.
3. Clip object: `{clip_id, source_video_id, start_ts, end_ts, duration, clip_path, keyframe_paths}`.
4. Keyframe extraction: ffmpeg at (start, middle, end) of each clip.
5. CLI: `uv run python -m viral_remix.extraction.segment --input data/raw/manifest.jsonl --output data/clips/manifest.jsonl`.
6. Enforce 3–5s length guardrail with merge/split logic; test edge cases (<3s, >5s, video with no scene changes).
7. Tests: golden-output test on a fixed small video; assertion on output clip count + duration ranges.

### Verification commands
```bash
uv run pytest tests/extraction/
uv run python -m viral_remix.extraction.segment --input data/raw/manifest.jsonl
ls data/clips/ | wc -l   # should be > 100 (avg ~10–20 clips per source video)
python -c "import json; from pathlib import Path; entries = [json.loads(l) for l in open('data/clips/manifest.jsonl')]; assert all(3 <= e['duration'] <= 5 for e in entries), 'guardrail violated'"
```

### Exit criteria
- [ ] 100 source videos segmented into ~1,000–2,000 clips
- [ ] All clips satisfy 3–5s duration guardrail
- [ ] 3 keyframes extracted per clip
- [ ] Clip manifest well-formed; unit tests ≥80% coverage

### Rollback strategy
Revert PR. Delete `data/clips/` + `data/keyframes/` if corrupted. Scraper output (`data/raw/`) unaffected.

---

## Step 4 — VLM Annotation Pipeline

**Dependencies:** Step 3 + a 1-hr schema-contract session with Step 5's owner (see below).
**Parallel with:** Step 5 — only after a joint 1-hr **schema freeze session** at the start where both owners co-write `src/viral_remix/schemas/clip.py` containing final `ClipAnnotation` + embedding dimensions. After schema is committed on a shared branch, Steps 4 and 5 proceed in parallel without `models.py` conflicts.
**Model tier:** Strongest (Opus) for prompt design + annotation schema. Default for plumbing.
**Owner:** Daniel leads; James reviews prompts.
**Estimated effort:** 8–12 hrs.

### Context brief
For each clip's 3 keyframes, call a VLM to produce structured annotations: scene description, celebrity recognition (if any), emotion, setting, objects/brands, and a short semantic caption. Default model: Gemini Flash (cheapest, confirmed in Step 0 cost spike). Store annotations in a JSONL alongside clip manifest and in Postgres (Step 5).

Schema (Pydantic model):
```python
class ClipAnnotation(BaseModel):
    clip_id: str
    scene_description: str  # 1–2 sentence description of what's happening
    celebrities: list[str]  # named entities recognized
    emotion: Literal["happy", "sad", "angry", "surprised", "neutral", "dramatic", "intense", "calm"]
    setting: str  # "red carpet", "interview", "street", etc.
    objects: list[str]
    brands: list[str]
    semantic_caption: str  # one-line search-optimized summary
    confidence: float
    annotator_model: str
    annotated_at: datetime
```

Critical: the prompt must encourage the VLM to NOT fabricate celebrity names. Unknown faces → empty list. Use few-shot examples in the prompt to anchor correct behavior.

Retry strategy: 3 retries with backoff on 5xx; on persistent failure, log and skip (don't block the batch).

### Tasks
1. Add `google-generativeai` (or `anthropic` / `openai` depending on Step 0 cost spike) to deps.
2. `src/viral_remix/annotation/vlm.py`: async function `annotate_clip(clip: Clip) -> ClipAnnotation`.
3. Prompt templates at `prompts/annotate_clip.md` — loaded at runtime. Include 3–5 few-shot examples.
4. Async batch runner: process clips with `asyncio.gather` + semaphore (bounded concurrency; start at 10).
5. Cost tracking: log tokens + $ per batch to `data/cost.log`. Invoke `/cost-aware-llm-pipeline` skill patterns for budget controls.
6. CLI: `uv run python -m viral_remix.annotation.batch --input data/clips/manifest.jsonl --output data/annotations/manifest.jsonl`.
7. Tests: golden-output test on 3 fixed clips; schema validation tests; prompt regression test (small eval harness — invoke `/eval-harness` skill).
8. **Hand-label 20 clips** as the accuracy gold set. Daniel watches 20 clips from Step 3 output, writes ground-truth annotations in `evals/annotation-gold.jsonl`. Budget 1.5–2 hrs.
9. Produce `evals/annotation-quality.md` capturing: accuracy vs. gold set (scene description + celebrity ID), cost-per-clip actuals, p95 latency.

### Verification commands
```bash
uv run pytest tests/annotation/
uv run python -m viral_remix.annotation.batch --input data/clips/manifest.jsonl --limit 50
cat data/annotations/manifest.jsonl | wc -l   # == 50
cat data/cost.log | tail -5   # cost visible
uv run python scripts/run-annotation-evals.py   # eval harness output
```

### Exit criteria
- [ ] 1,000–2,000 clips annotated; cost under projected ceiling from Step 0
- [ ] Hand-labeled eval shows ≥80% accuracy on scene description + celebrity ID
- [ ] Zero fabricated celebrity names on the "unknown faces" test set
- [ ] Cost + latency tracked in `data/cost.log`
- [ ] Eval harness in place (reusable for future annotator swaps)

### Rollback strategy
Revert PR. Annotations in `data/annotations/` can be safely deleted — idempotent re-run. If VLM model changes later, re-annotate.

---

## Step 5 — Clip Database (Postgres + pgvector)

**Dependencies:** Step 3 (needs clip schema).
**Parallel with:** Step 4 — can start in parallel once annotation schema is defined.
**Model tier:** Strongest (Opus) for schema + query patterns. Default for plumbing.
**Owner:** Daniel.
**Estimated effort:** 6–8 hrs.

### Context brief
Set up Postgres with pgvector for clip storage + semantic retrieval. Tables: `videos`, `clips`, `annotations`, `embeddings`. Use SQLAlchemy 2.x with Alembic migrations. Embed `semantic_caption` from annotations using OpenAI `text-embedding-3-small` (1536 dim, cheap) — this is the retrieval key for Step 6.

Run Postgres locally via Docker for MVP. Production consideration (deferred to Phase 2): managed Postgres (Supabase, Neon) with pgvector extension.

### Tasks
1. `docker-compose.yml` with Postgres 16 + pgvector image.
2. `src/viral_remix/db/models.py`: SQLAlchemy models for videos, clips, annotations, embeddings.
3. Alembic scaffolding + initial migration creating all tables + pgvector index (ivfflat or hnsw).
4. `src/viral_remix/db/ingest.py`: function `ingest_manifests(videos, clips, annotations)` — idempotent bulk insert.
5. Embedding generator: batch-embed `semantic_caption` via OpenAI; store in `embeddings` table with FK to `clip_id`.
6. CLI: `uv run python -m viral_remix.db.ingest --from-manifests`.
7. Tests: docker-compose spin-up in CI (use `testcontainers-python`); round-trip test ingest + query.
8. Schema version check in CI.

### Verification commands
```bash
docker compose up -d postgres
uv run alembic upgrade head
uv run python -m viral_remix.db.ingest --from-manifests
psql -h localhost -U viral_remix -c "SELECT count(*) FROM clips;"   # should match Step 3 count
psql -h localhost -U viral_remix -c "SELECT count(*) FROM annotations;"
psql -h localhost -U viral_remix -c "SELECT count(*) FROM embeddings;"
uv run pytest tests/db/
```

### Exit criteria
- [ ] Migrations apply cleanly on empty + populated DB
- [ ] Clip count in DB matches Step 3 output; annotation count matches Step 4 output
- [ ] Vector index exists; `EXPLAIN` confirms index use on cosine similarity query
- [ ] Round-trip test green in CI

### Rollback strategy
**For empty DB:** Alembic down migration to drop all tables.
**For populated DB:** `pg_dump` before any migration (runbook: `scripts/db-backup.sh` invoked as pre-migration hook). Down migrations on populated DB require explicit dump restore if embeddings are dropped — embeddings cost real $ to regenerate.
Forward-only migrations with explicit downs for all schema changes.

---

## Step 6 — Retrieval (Text → Ranked Clips)

**Dependencies:** Step 5.
**Parallel with:** None directly, but gates Steps 7, 8, 9 (they need retrieval interface for integration).
**Model tier:** Default (Sonnet).
**Owner:** Daniel.
**Estimated effort:** 4–6 hrs.

### Context brief
Given a text query (e.g., "Taylor Swift red carpet emotional"), return the top-k most relevant clips. MVP ranking: cosine similarity on embedding. Phase-2 extension (not in this step): hybrid with BM25 + recency + engagement — placeholder hook left in code.

Also expose a minimal CLI + web UI (Streamlit or FastHTML) to interactively query and preview clips. This is the Path C (storyboard assistant) capability from the plan — used internally for QC and manual stitching in Step 11.

### Tasks
1. `src/viral_remix/retrieval/search.py`: function `search(query: str, top_k: int = 20) -> list[ClipResult]` returning clip + score + annotation snippet.
2. Embedding: embed query via same OpenAI model used in Step 5.
3. SQL: cosine similarity query against `embeddings` table with pgvector operators.
4. CLI: `uv run python -m viral_remix.retrieval.search "Taylor Swift red carpet"`.
5. Streamlit UI at `src/viral_remix/ui/search_app.py`: search box + video preview grid. (Streamlit chosen over FastHTML — lower setup cost, Rekko already uses Streamlit patterns. Lock in now, no bikeshed mid-build.)
6. Tests: fixture DB with 10 known clips; assert expected clip is in top-3 for target query.
7. Document query patterns + common failure modes in `docs/retrieval.md`.

### Verification commands
```bash
uv run python -m viral_remix.retrieval.search "celebrity award show reaction"
uv run streamlit run src/viral_remix/ui/search_app.py   # manual preview
uv run pytest tests/retrieval/
```

### Exit criteria
- [ ] Text query returns ranked clip list with scores
- [ ] Streamlit UI displays + plays top-k clips
- [ ] Fixture test green (known clip in top-3 on target query)
- [ ] `docs/retrieval.md` filed

### Rollback strategy
Revert PR. DB untouched.

---

## Step 7 — Script Generation (Editorial Voice)

**Dependencies:** Step 6 (interface stub sufficient; full impl not needed at step start).
**Parallel with:** Steps 8, 9.
**Model tier:** Strongest (Opus) for prompt engineering + editorial voice encoding.
**Owner:** James leads (prompt design is his domain); Daniel integrates.
**Estimated effort:** 6–10 hrs.

### Context brief
Given a topic (e.g., "Taylor Swift and Travis Kelce breakup rumors"), produce a scene-by-scene script with TTS narration embodying the channel's editorial voice (locked in `docs/brand.md` from Step 0). Use `/brand-voice` skill to extract and enforce the voice from reference content.

Output schema:
```python
class VideoScript(BaseModel):
    topic: str
    total_duration_s: float  # target 30–60
    beats: list[ScriptBeat]

class ScriptBeat(BaseModel):
    beat_idx: int
    narration: str  # what the TTS speaks
    narration_duration_s: float
    clip_query: str  # semantic query for Step 6 retrieval
    clip_duration_s: float  # how long the clip plays under this narration
    overlay_text: str | None  # optional burned-in caption
```

**Hard constraint (fair-use guardrail):** `sum(narration_duration) / sum(clip_duration) >= 2.0`. **Enforce with ≥2.2 safety margin at script-gen time** — Step 8 TTS renders have ±10% duration drift from estimates, so a script passing at 2.01 pre-TTS can fail post-render. Reject scripts at Step 7 if estimated ratio <2.2. Step 9 also re-validates on final render; if post-render ratio is 2.0–2.2 (inside safety band but above floor), Step 9 auto-extends inter-clip gaps (black-frame spacer or extended held frame) to restore margin rather than reject a rendered video.

The prompt must:
- Encode the channel's editorial POV (from `docs/brand.md`)
- Use one of the four proven hook formats (avoidance, best-advice, comparison, demographic)
- Keep narration punchy + spoken-word pacing (see `docs/james/tab1.md` 2026 Master Prompt Formula)
- Avoid AI slop vocabulary ("delve", "unleash", "tapestry", "revolutionize")
- Add transformative commentary — not just narration of footage

### Tasks
1. Run `/brand-voice` skill on the channel's intended editorial reference set (chosen in Step 0) → produce `prompts/voice_profile.md`.
2. `src/viral_remix/generation/script.py`: function `generate_script(topic, voice_profile, constraints) -> VideoScript` using Claude Sonnet 4.6 or Opus 4.7 (prompt caching enabled — invoke `/claude-api` skill).
3. Prompt templates at `prompts/generate_script.md` + `prompts/voice_profile.md`.
4. Commentary-ratio validator: reject + regenerate if ratio < 2.0 (max 2 retries; escalate to human if still failing).
5. Defamation guardrail: post-generation pass that checks for unsupported factual claims about named persons — invoke a small critique LLM.
6. CLI: `uv run python -m viral_remix.generation.script --topic "Taylor Swift breakup rumors" --duration 45`.
7. Tests: voice-profile adherence test; ratio guardrail test; defamation check test on known-problematic input.
8. Eval harness: 10 topics → inspect outputs; score for (a) hook strength, (b) voice adherence, (c) ratio compliance, (d) factual grounding.

### Verification commands
```bash
uv run python -m viral_remix.generation.script --topic "celebrity award moment" --duration 30
uv run pytest tests/generation/
uv run python scripts/run-script-evals.py   # human review of 10 outputs
```

### Exit criteria
- [ ] 10 scripts generated on diverse topics; all pass ratio + defamation guardrails
- [ ] Human review score ≥7/10 on voice adherence + hook quality
- [ ] Prompt caching measurably active (cache-hit rate logged)
- [ ] `prompts/voice_profile.md` committed

### Rollback strategy
Revert PR. Re-run with tuned prompts. No durable state (scripts are regenerated per request).

---

## Step 8 — TTS Integration

**Dependencies:** Step 6 stub (not required at start; Step 7 interface sufficient).
**Parallel with:** Steps 7, 9.
**Model tier:** Default (Sonnet).
**Owner:** Daniel.
**Estimated effort:** 3–5 hrs.

### Context brief
Render narration from `VideoScript.beats[*].narration` into audio files. Use ElevenLabs (realism) as default; support Kokoro (local, free) as fallback. Voice identity is locked from Step 0 `docs/brand.md`.

Rekko already integrates Kokoro — the `rekko.ai` codebase at `src/rekko_server/video/tts/` is referenceable but not a direct port (Rekko bundles TTS with video generation; here we want it separable).

### Tasks
1. `src/viral_remix/generation/tts.py`: function `synthesize(script: VideoScript, voice_id: str) -> list[AudioClip]` where each `AudioClip` has the path and duration of the rendered narration for one beat.
2. ElevenLabs integration (env: `ELEVENLABS_API_KEY`). Voice cloning path: if brand.md specifies cloned voice, upload reference audio + store voice_id at first run.
3. Kokoro fallback: invoke local model if ElevenLabs unavailable or budget-capped.
4. SSML support for pacing/emphasis (optional; add if ElevenLabs supports).
5. Caching: SHA-256 on `(text, voice_id, model)` → skip re-synthesis. Invoke `/content-hash-cache-pattern` skill.
6. CLI: `uv run python -m viral_remix.generation.tts --script path/to/script.json`.
7. Tests: fixture script → assert WAV files produced with expected durations (±10%).

### Verification commands
```bash
uv run python -m viral_remix.generation.tts --script tests/fixtures/script.json
ls data/tts/   # should contain .wav files per beat
ffprobe -i data/tts/beat_0.wav 2>&1 | grep Duration
uv run pytest tests/tts/
```

### Exit criteria
- [ ] TTS audio files produced for a fixture script
- [ ] Voice identity matches brand.md specification
- [ ] Duration of each audio ≈ target narration duration (±10%)
- [ ] Cache hit skips re-synthesis
- [ ] **Voice-swap escape hatch:** `voice_id` is read from `config/brand.yaml` at runtime. No voice_id hardcoded in Python. Swapping voice = edit one line + re-synthesize affected cache keys. (Mitigation for: Step 11 may reveal the voice is wrong; re-voicing must not require code changes or re-renders of all prior videos.)

### Rollback strategy
Revert PR. Audio outputs are regeneratable + cached.

---

## Step 9 — Stitch + Render

**Dependencies:** Step 6 (retrieval for clips), Step 8 (TTS audio). Can design in parallel with 7 + 8 using stub interfaces.
**Parallel with:** Steps 7, 8.
**Model tier:** Default (Sonnet). Invoke `/video-editing` + `/videodb` skills.
**Owner:** Daniel leads.
**Estimated effort:** 8–12 hrs.

### Context brief
Given a `VideoScript` with resolved clips (Step 6 result per beat) + TTS audio (Step 8 per beat), produce a finished 9:16 MP4 with:
- Intro (fixed asset, ~2s, branded)
- Stitched clips beat-by-beat, synced to TTS
- Burned-in captions (Whisper-transcribed from TTS or passed through from script)
- Outro (fixed asset, ~3s, branded)
- Watermark (persistent, upper-left, per brand.md)

Default renderer: Remotion (React/TypeScript) — Rekko uses this and the engineering is proven. FFmpeg fallback for minimal assembly. Reuse Rekko's Remotion scaffolding where license-compatible (James's own code; no barrier).

**Hard constraint:** re-validate commentary-ratio on the final render. Reject if violated.

### Tasks
1. Source intro/outro assets from Step 0 brand work (commit to `assets/brand/intro.mp4`, `assets/brand/outro.mp4`).
2. `src/viral_remix/stitch/renderer.py`: function `render_video(script, resolved_clips, audio_clips, output_path) -> RenderResult`.
3. Remotion project at `remotion/` — composition that takes beats + clips + audio as props and renders 9:16 @ 30fps. Reuse Rekko's composition patterns (at `/home/james/src/rekko.ai/remotion-video/`).
4. Caption generation: Whisper-transcribe TTS audio (or pass through script text) → burn-in via Remotion text component with brand styling from `docs/brand.md`.
5. Watermark overlay: configurable via `config/brand.yaml`.
6. Post-render validation: re-compute commentary-ratio on final MP4 (using ffprobe for durations).
7. CLI: `uv run python -m viral_remix.stitch --script path/to/script.json --output data/renders/video.mp4`.
8. Tests: fixture render test; duration assertion; ratio guardrail assertion.

### Verification commands
```bash
uv run python -m viral_remix.stitch --script tests/fixtures/script.json --output /tmp/test.mp4
ffprobe -i /tmp/test.mp4 2>&1 | grep -E "Duration|resolution"
# Should be 9:16, 30fps, duration in 30–60s range
uv run pytest tests/stitch/
```

### Exit criteria
- [ ] Fixture script → finished 9:16 MP4 rendered
- [ ] Resolution 1080x1920 (or equivalent), 30fps, H.264
- [ ] Watermark + intro + outro present (visual inspection)
- [ ] Post-render commentary-ratio guardrail passes

### Rollback strategy
Revert PR. Rendered outputs regeneratable from inputs.

---

## Step 10 — QC Gate + Publish Pipeline

**Dependencies:** Steps 7, 8, 9 all merged.
**Parallel with:** None.
**Model tier:** Default (Sonnet).
**Owner:** Daniel leads.
**Estimated effort:** 5–8 hrs.

### Context brief
Before any video is published, it passes through:
1. **Automated QC** — ratio check, clip-length check, defamation scan, banned-words check (from `docs/legal.md`)
2. **Human review** — operator (Daniel) watches the full video + approves via CLI or simple web UI
3. **Publish** — upload to YouTube via Data API v3 with AIGC label (required per YouTube's AI-content-disclosure policy), title + description + tags per brand.md conventions
4. **Track** — record upload metadata, view/engagement over time, takedown/demonetization notices

Also: a **dispute queue** for Content ID strikes. When a strike arrives, log to `data/disputes/queue.jsonl` and surface via CLI for operator action.

### Tasks
1. `src/viral_remix/publish/qc.py`: `run_qc(video_path) -> QCReport` combining all automated checks.
2. `src/viral_remix/publish/review.py`: CLI or Streamlit UI that plays video + shows QC report + approve/reject.
3. YouTube upload: `src/viral_remix/publish/youtube.py` using `google-api-python-client`. Set `publishStatus=private` on upload; flip to `public` only after final operator OK.
4. AIGC label: set correctly in upload metadata.
5. Metadata generator: title, description (with source attribution line from `docs/legal.md`), hashtags. Prompt-driven; operator edits before upload.
6. Dispute queue: `src/viral_remix/publish/disputes.py` — ingest notifications from YouTube Studio (manual for MVP; webhook later).
7. Analytics (MVP scope = manual check, not dashboard): simple CLI `uv run python -m viral_remix.publish.analytics --video-id X` pulls current view/engagement from YouTube Data API. No auto-polling, no dashboard, no retention curves in MVP — that's Phase 2. Just enough to fill the Step 11 exit criterion "7-day analytics captured."
8. **Observability for cost + errors:** `scripts/daily-digest.sh` cron candidate — tails `data/cost.log` + Content ID dispute queue, prints a 10-line summary. For MVP: run by hand daily. For Phase 2: wire to a Slack webhook. Add an alert threshold: if daily spend > (Step 0 budget / 30 days) * 1.5, surface a warning in the digest.
9. Tests: QC report generation test; mock YouTube upload test; dispute queue round-trip test.

### Verification commands
```bash
uv run python -m viral_remix.publish.qc --video /tmp/test.mp4
uv run python -m viral_remix.publish.review --video /tmp/test.mp4   # manual approval
uv run python -m viral_remix.publish.youtube --video /tmp/test.mp4 --title "..." --dry-run
uv run pytest tests/publish/
```

### Exit criteria
- [ ] QC automatically rejects videos violating ratio / clip-length / banned-words rules
- [ ] Operator review UI functional
- [ ] YouTube upload works end-to-end (dry-run and real)
- [ ] AIGC label visible on uploaded video (manual verification in YouTube Studio)
- [ ] Dispute queue captures a test Content ID notification
- [ ] Analytics pull works

### Rollback strategy
Revert PR. Set `publishStatus=private` on any test uploads; delete from channel if accidentally public.

---

## Step 11 — First 3–5 Videos (End-to-End Manual Operation)

**Dependencies:** Step 10.
**Parallel with:** None.
**Model tier:** Strongest (Opus) for quality review.
**Owner:** Shared (Daniel operates, James reviews).
**Estimated effort:** 10–15 hrs.

### Context brief
Operate the full pipeline manually, end-to-end, for 3–5 videos. Each video:
1. Pick a topic (from trending celebrity/news — cross-reference to `research/competitor-analysis.xlsx`)
2. Run script generation → human review
3. Retrieve clips → human curate
4. TTS → human listen-check
5. Stitch + render → human watch
6. QC → operator approve
7. Publish to YouTube Shorts

Capture pain points at each stage in `docs/operator-journal.md`. This is the learning deliverable — what automates cleanly, what needs more human-in-loop, what doesn't work.

This step also produces the **exit artifact for the craft bet** (the MVP): a working pipeline + 3–5 posted videos + a blog post outline.

### Tasks
1. Produce 3–5 videos end-to-end. Topic diversity: 1 breaking-news reaction, 1 retrospective, 1 relationship/drama, + 1–2 at operator's discretion.
2. Log pain points at each pipeline stage in `docs/operator-journal.md` after each video.
3. Fix any P0 bugs surfaced during operation (hotfix PRs).
4. Capture channel baseline: post all 3–5 videos over 2–3 days (not all at once); measure 7-day view + engagement curve.
5. Write the first draft of a blog post at `blog/post-draft.md` — this is the portfolio artifact. Topic: "Building a VLM-annotated viral-clip remix pipeline: what worked, what didn't." **MVP exit = full first draft, not just outline** (source plan §3 defines craft success as a full blog post). If full-draft effort exceeds Step 11's hours, outline ships as MVP and full draft moves to Phase 2 explicitly — do not silently downgrade.
6. Retro session (James + Daniel, 1 hr): review `operator-journal.md`, decide Phase 2 priorities.

### Exit criteria
- [ ] 3–5 videos successfully posted (public on YouTube)
- [ ] 7-day analytics captured for each
- [ ] `operator-journal.md` filed with specific pain points
- [ ] Blog post full draft committed to `blog/post-draft.md` (or explicit downgrade to outline + Phase 2 task filed)
- [ ] Retro complete; Phase 2 backlog in `backlog.md`
- [ ] **Voice-retention decision point:** if average view retention across the 3–5 videos is below median for the niche (benchmark from Step 0 competitor spreadsheet), run a voice-revision spike (swap voice via `config/brand.yaml`, re-render 1 video, compare) before committing to Phase 2
- [ ] **Dispute queue note for Phase 2:** if observed Content ID takedown rate ≥20% on the 3–5 videos, dispute-queue webhook + SLA becomes a Phase 2 blocker (not an afterthought)
- [ ] Decision made: continue to Phase 2 (posting cadence + automation) OR rescope OR abandon (per pre-mortem criteria in `work+self/projects/viral_remix_plan.md`)

### Rollback strategy
Remove posted videos from YouTube if quality/legal issues surface. No infra rollback — the pipeline stays even if the channel doesn't continue.

---

## Cross-Cutting Invariants (Verify After Every Step)

1. **CI green on `main`** — `uv run pytest && uv run ruff check . && uv run mypy src/` passes
2. **No Rekko imports** — `grep -r "from rekko_server" src/` returns empty (ensures clean separation)
3. **Legal guardrails active** — commentary-ratio check + clip-length check enforced at every stage they apply (generation ≥2.2 margin, pre-render, post-render)
4. **Cost tracked + surfaced** — `data/cost.log` updated per run; `scripts/daily-digest.sh` summarizes spend; alert fires if daily spend >1.5× projection
5. **No secrets in git** — `.env` gitignored; `.env.example` committed; pre-commit hook scans for leaked secrets; CI uses GitHub Actions secrets
6. **SKILL invocations logged** — which skills were used in each PR (documented in PR description)
7. **Voice identity not hardcoded** — `voice_id` read from `config/brand.yaml`; can be swapped without code change

---

## Anti-Pattern Catalog (Things We Will Not Do)

1. **Full 10-year crawl.** Cap catalog at 10K clips for MVP. No exceptions.
2. **Generative video (Veo/Runway/Sora) in MVP.** Real-clip remix is the bet; revisit only after Phase 2 retention data supports it.
3. **Autonomous posting without human review in MVP.** Every video gets Daniel's eyeballs before publish.
4. **TikTok ingestion in MVP.** YouTube first. Phase 2 only.
5. **Skip legal consult.** Non-negotiable in Step 0.
6. **Build-your-own VLM.** Use off-the-shelf (Gemini Flash / GPT-4o-mini / Claude Haiku). Cost optimization is fine; model research is out of scope.
7. **Skip dedupe or attribution.** Both are non-negotiable for legal posture.
8. **Over-index on infra polish pre-Step 11.** Step 11's operator journal is ground truth for what needs polishing. (Exception: MVP-minimum analytics in Step 10 — CLI-only, no dashboard — is not "polish.")
9. **Build for external creators.** Internal-only. No multi-tenant, no auth, no billing.
10. **Ignore the commentary-ratio guardrail.** Bake it into code paths at every stage (generation + pre-render + post-render).

---

## Plan Mutation Protocol

Steps may be split, inserted, skipped, reordered, or abandoned during execution. Any mutation requires:

1. A PR to this plan file documenting: (a) which step is mutated, (b) why, (c) what the new structure is, (d) what risk the change introduces
2. James's approval (for strategic shifts) or Daniel's approval (for tactical shifts within a step's scope)
3. Updated dependency graph + parallelism summary if edges change
4. Audit-trail line in a new `## Plan Mutations` appendix

---

## Registration

**Plan location:** `/home/james/src/leo/plans/viral-remix-construction-blueprint.md` until Step 1 moves it to `<new-repo>/plans/`.

**Source plan:** `/home/james/src/leo/work+self/projects/viral_remix_plan.md`.

**Backlog integration:** Once committed to Leo, add an entry to `backlog.md` → Build section tracking this blueprint.

**Session log:** Record blueprint generation in the next session log for `2026-04-17`.

---

## Review Findings Log (Adversarial Review 2026-04-17)

The initial draft of this blueprint underwent an adversarial review pass. Findings resolved in-place:

**Critical (all fixed):**
- Voice decision lock-in with no revision loop → voice-swap escape hatch added (Step 8 exit criterion + Step 11 retention decision point + invariant 7)
- Step 4/5 parallelism incorrectly declared → schema-contract freeze session required before parallel work (Step 4 header)
- Secrets management absent → `.env.example`, gitleaks pre-commit, GitHub Actions secrets added (Step 1 tasks 10–11)
- YouTube upload OAuth/GCP setup missing → added as Step 0 Task 5; blocks Step 10
- Commentary-ratio guardrail brittleness at Step 7 boundary → ≥2.2 safety margin + Step 9 auto-extend fallback
- Step 4 eval hand-labeled gold set unbuilt → explicit 1.5–2 hr sub-task (Step 4 Task 8)

**Important (all fixed):**
- Hour estimates under-forecast → realism buffer (120–180 hrs / 10–14 weeks) flagged in preamble
- No observability → daily digest + cost alert added (Step 10 Task 8 + invariant 4)
- Step 5 rollback weak on populated DB → pg_dump runbook added
- Attorney brief missing ingest-side ToS → Step 0 Task 2 updated to cover both sides
- Step 11 craft bet exit ambiguous → clarified: full draft is the target, explicit downgrade path documented
- Dispute queue Phase 2 blocker → flagged in Step 11 exit criteria

**Minor (addressed):**
- `.claude/settings.json` scope clarified (Step 1 task 6)
- Streamlit locked in over FastHTML (Step 6 task 5)
- Anti-pattern 8 reconciled with Step 10 analytics scope
- "Full branch/PR/CI workflow mode" defined in preamble
- `.python-version` + `uv.lock` added (Step 1 task 11)
