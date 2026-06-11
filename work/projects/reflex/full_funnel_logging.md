# Full Funnel Logging — Homefeed Pipeline

> Complete field inventory and process documentation for all pipeline stages.
> Stages 1–3 cover request entry, sizer, and resource fetching.
> Stages 4–9 cover candidate generation, LWS, L1 presort, pre-ranking filtering, and L1 utility merge.
> Stages 10–12 cover L2 ranking batching, ranking output, and post-ranking filtering.
> Stages 13–16 cover presorting/diversity, SSD/L3 reranking, and the final content chunk.
> The final section documents funnel latency stats instrumentation.

---

## Stage 1: AT_REQUEST_ENTRY

**Code location:** `HomefeedAllPlanner.getContentChunkNode()` — top of the method,
right after the method parameters are received.

**Objects available:** `ChunkRequest`, `RequestContext`, `SourceRequestContext`,
`UnityContext`

### Selected Fields

#### Request-level `[R]`

| Field                              | Source Object    | Type                      | Captured? | Notes                                                                    |
| ---------------------------------- | ---------------- | ------------------------- | --------- | ------------------------------------------------------------------------ |
| `userId`                           | `ChunkRequest`   | i64                       | ⚠️        | Not in request entry; captured as `UnityFunnelUser.id` (user-level)      |
| `chunkId`                          | `ChunkRequest`   | i64                       | ✅        | `entryLongMeta["CHUNK_ID"]`                                              |
| `targetingContext`                 | `ChunkRequest`   | TargetingContext          | ⚠️        | Only `targetingContextType` captured, not full object                    |
| `targetingContextType`             | derived          | TargetingContextType enum | ✅        | `entryStringMeta["TARGETING_CONTEXT_TYPE"]`                              |
| `startTime`                        | derived          | long                      | ✅        | `HomefeedUnityFunnelContext.startTimeMs`; used for latency stats         |
| `source`                           | `RequestContext` | string                    | ✅        | Split: `entryStringMeta["SOURCE_ENDPOINT"]` + `["SOURCE_SERVICE"]`       |
| `requestId`                        | `RequestContext` | string                    | ✅        | `UnityFunnelRequest.id` via `UnityUtils.getTraceIdDecimal()`             |
| `userSessionInfo.sessId`           | `RequestContext` | string                    | ⚠️        | Not in entry meta; in `UnityFunnelUser.sessionId` (user-level)           |
| `userSessionInfo.locale`           | `RequestContext` | string                    | ⚠️        | Not in entry meta; in `UnityFunnelUser.locale` (user-level)              |
| `userSessionInfo.country`          | `RequestContext` | string                    | ⚠️        | Not in entry meta; in `UnityFunnelUser.country` (user-level, UserInfo)   |
| `userSessionInfo.appType`          | `RequestContext` | string                    | ⚠️        | Not in entry meta; in `UnityFunnelUser.appType` (user-level)             |
| `userSessionInfo.appVersion`       | `RequestContext` | string                    | ✅        | `entryStringMeta["APP_VERSION"]`                                         |
| `userSessionInfo.device`           | `RequestContext` | i64                       | ✅        | `entryLongMeta["DEVICE"]`                                                |
| `userSessionInfo.userJoinDate`     | `RequestContext` | i64                       | ✅        | `entryLongMeta["USER_JOIN_DATE"]`                                        |
| `userSessionInfo.isBot`            | `RequestContext` | bool                      | ❌        | Not captured anywhere                                                    |
| `userSessionInfo.isEmployee`       | `RequestContext` | bool                      | ⚠️        | Not in entry meta; in `UnityFunnelUser.isEmployee` (user-level)          |
| `userSessionInfo.isPartner`        | `RequestContext` | bool                      | ❌        | Not captured anywhere                                                    |
| `userSessionInfo.forceExperiments` | `RequestContext` | map                       | ⚠️        | Activated experiments in `triggeredExperiments`, not forced specifically |

#### User-level `[U]`

| Field                                   | Source Object    | Type         | Captured? | Notes                     |
| --------------------------------------- | ---------------- | ------------ | --------- | ------------------------- |
| `viewingUser.userId`                    | `RequestContext` | i64          | ✅        | `UnityFunnelUser.id`      |
| `viewingUser.locale`                    | `RequestContext` | string       | ✅        | `UnityFunnelUser.locale`  |
| `viewingUser.country`                   | `RequestContext` | string       | ✅        | `UnityFunnelUser.country` |
| `viewingUser.gender`                    | `RequestContext` | string       | ✅        | `UnityFunnelUser.gender`  |
| `viewingUser.signupTimeInSec`           | `RequestContext` | i64          | ❌        |                           |
| `viewingUser.birthdayInSec`             | `RequestContext` | i64          | ❌        |                           |
| `viewingUser.isPartner`                 | `RequestContext` | bool         | ❌        |                           |
| `currentUserState.numUserFollows`       | `RequestContext` | i32          | ❌        |                           |
| `currentUserState.numBoardFollows`      | `RequestContext` | i32          | ❌        |                           |
| `currentUserState.numTopicFollows`      | `RequestContext` | i32          | ❌        |                           |
| `currentUserState.userStates`           | `RequestContext` | map<i32,i32> | ❌        | Engagement state map      |
| `currentUserState.firstLoadPostNux`     | `RequestContext` | bool         | ❌        |                           |
| `currentUserState.isRenuxUser`          | `RequestContext` | bool         | ❌        |                           |
| `currentUserState.visitationState`      | `RequestContext` | i32          | ❌        |                           |
| `currentUserState.hfBrowsingLevel`      | `RequestContext` | i32          | ❌        |                           |
| `currentUserState.landerDays`           | `RequestContext` | i16          | ❌        |                           |
| `currentUserState.browserDays`          | `RequestContext` | i16          | ❌        |                           |
| `currentUserState.deepBrowserDays`      | `RequestContext` | i16          | ❌        |                           |
| `currentUserState.pinsSeenOverDefault`  | `RequestContext` | i32          | ❌        |                           |
| `currentUserState.userActivityState`    | `RequestContext` | i32          | ❌        |                           |
| `currentUserState.resurrectedDays`      | `RequestContext` | i16          | ❌        |                           |
| `currentUserState.hasNuxUseCaseStarted` | `RequestContext` | bool         | ❌        |                           |

### Excluded Fields (always null/empty at runtime)

| Field                                 | Reason                                                   |
| ------------------------------------- | -------------------------------------------------------- |
| `sessionId` (ChunkRequest)            | Always null; real session ID is `userSessionInfo.sessId` |
| `sessionInfo` (RequestContext)        | All sub-fields null; redundant with `userSessionInfo`    |
| `currentUserState.experiences`        | Always null                                              |
| `currentUserState.userBrowsingLevels` | Always null                                              |

---

## Stage 2: AFTER_SIZER_CALCULATION

**Code location:** `Sizer.computeSizerParams()` in `Sizer.java` — right before the
return statement, after all experiment overrides, budget tuning, and emergency
reductions are applied. **Not** in `HomefeedAllPlanner.java`.

### Selected Fields

#### Request-level `[R]`

| Field                      | Source Object | Type                           | Captured? | Notes                                                                            |
| -------------------------- | ------------- | ------------------------------ | --------- | -------------------------------------------------------------------------------- |
| `perPullsarSourceMaxSizes` | `SizerParams` | map<FeedSourceIdentifier, i32> | ✅        | Stored as `sizerBudgets`; emitted as `SIZER_BUDGET_{source}` in request metadata |

Each key is a `FeedSourceIdentifier` with only `leafIdentifier` set (no
`poolIdentifier`). The leaf has `source` (FeedSourceType enum) and `name` (string).
The value is the max number of candidates to fetch from that source.

The set of feed sources varies per request (depends on user state, experiments,
targeting context, etc.).

### Example output (staging, targetingContextType=ALL)

| leafIdentifier (source:name)                        | Budget |
| --------------------------------------------------- | ------ |
| INTEREST:prod                                       | 1400   |
| FANTASIO:tt_conditional_pin_embedding_to_web_pins   | 1000   |
| FANTASIO:user_offsite_engagement_search_navboost    | 1000   |
| FANTASIO:one_day_recent_action_pins                 | 975    |
| FANTASIO:navboost_pfy                               | 985    |
| FANTASIO:tt_conditional_uic_medioid_emb_to_web_pins | 750    |
| FANTASIO:graphsage_product_pins                     | 500    |
| FANTASIO:offsite_ipfy                               | 500    |
| FANTASIO:prod                                       | 400    |
| INTEREST:first_load                                 | 400    |
| FANTASIO:tt_multi_embedding_to_web_pins             | 357    |
| FANTASIO:tt_conditional_board_embedding_to_web_pins | 351    |
| FANTASIO:fresh_from_regular_pfy                     | 340    |
| FANTASIO:landing_page_pixie                         | 300    |
| FANTASIO:recboost_shopping                          | 250    |
| FOLLOWING_FEED:prod                                 | 175    |
| FANTASIO:tt_embedding_to_tml_product_pins           | 100    |
| FANTASIO:landing_page_recboost                      | 100    |
| FANTASIO:user_to_creator_story_pins                 | 100    |
| FANTASIO:tt_embedding_to_product_pins               | 50     |
| FANTASIO:landing_page_pin                           | 10     |
| FANTASIO:tt_embedding_to_fresh_product_pins         | 10     |
| FANTASIO:organic_coengagement                       | 0      |
| FANTASIO:related_pins_pfy                           | 0      |
| FANTASIO:recgpt_v0_user_to_pins                     | 0      |

`chunkSize` was 200 in this example.

### Excluded Fields

| Field                        | Reason                                             |
| ---------------------------- | -------------------------------------------------- |
| `poolIdentifier`             | Always null — only `leafIdentifier` is set         |
| `perPullsarSourceExtraSizes` | Not populated by the homefeed sizer path           |
| `chunkSize`                  | Available but derivative; not selected for logging |

### Notes

- This is the **final** sizer output after all experiment overrides, shopping
  tuning, emergency reductions, and incident shutdowns.
- Staging verification: done

---

## Stage 3: AFTER_RESOURCE_FETCHING

**Code location:** `HomefeedAllPlanner.getContentChunkNode()` — after
`ResourceFetcher.fetchResourcesAll()` returns and the GSS override is applied
(line ~615). The complete `Map<ResourceType, Node<Resource>>` is available here.

**Recording approach:** Resources are fetched from multiple backend services (USS,
UFR, GSS, etc.) and assembled at different points — some pre-fetched as inputs in
`HomefeedAllPlanner`, others created inside `ResourceFetcher.fetchResourcesAll()`
via ~30 `addXxxResource()` calls. However, they all converge into a single
`resources` map at this location. Since the map contains lazy `Node<Resource>`
objects (graph construction, not evaluation), we will use `.peek()` on each node
to record resource parameters at evaluation time without blocking graph
construction. See the commented code block at the stage marker in
`HomefeedAllPlanner.java`.

### Selected Fields

#### User-level `[U]`

| Field                | Source Object        | Type | Captured? | Notes                                                                                                               |
| -------------------- | -------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| `userFeatureUfrNode` | `Node<UFR>` (merged) | UFR  | ⚠️        | UIC features metadata captured via `userUicFeaturesMetadata` → `UnityFunnelUser.userMetadata`, but not the full UFR |

#### Request-level `[R]`

| Field           | Source Object   | Type              | Captured? | Notes        |
| --------------- | --------------- | ----------------- | --------- | ------------ |
| `resourceTypes` | `resources` map | Set<ResourceType> | ❌        | Not captured |

### Notes

- The `resources` map keys vary per request (depends on user state, experiments,
  targeting context). Recording which keys are present is sufficient — the
  internal fields of each `Resource` are user-level signals whose effects are
  visible in downstream stages (e.g., Stage 10 AFTER_RANKING).
- `userFeatureUfrNode` is the merged UIC UFR containing user interest cluster
  features from `getUICUfrUserFeaturesNode()`. It combines the L2 ranking/blending
  UIC node (`uicUFRNode`) and the L1/CLR diversity UIC node (`clrUicUFRNode`).
  Log the entire UFR object to capture all user feature vectors.
- Staging verification: done

---

## Stage 4: AFTER_CANDIDATE_GENERATION

**Code location:** `CandidateFetcher.fetchContentWithL1Utility()` — inside the
per-feed-source loop, right after `fetchFeedSourcePins()` returns and before LWS
or any processing. One log line per active feed source.

**Objects available:** `FeedSourceIdentifier`, `List<InternalPinResult>`

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field                   | Source Object                   | Type                                          | Captured? | Notes                                                     |
| ----------------------- | ------------------------------- | --------------------------------------------- | --------- | --------------------------------------------------------- |
| `pinId`                 | `PinResult`                     | i64                                           | ✅        | Via `buildCandidateId`                                    |
| `source`                | `PinDetails`                    | FeedSourceType enum                           | ✅        | Via `extractPinResultMetadata` with `isSetSource()` guard |
| `reasonToChoose`        | `Reason` (via `fantasioReason`) | ReasonToChoose enum                           | ✅        | Via `extractReasonMetadata`                               |
| `interestItemIdStr`     | `Reason`                        | string                                        | ✅        | Via `extractReasonMetadata`                               |
| `throughProperties`     | `Reason`                        | map<ThroughPropertyType, list<ThroughObject>> | ❌        | Not extracted in `extractReasonMetadata`                  |
| `recSource`             | `RecommendationSourceDetails`   | RecSource enum                                | ✅        | Via `extractRecSourceDetailsMetadata`                     |
| `queryScore`            | `RecommendationSourceDetails`   | double                                        | ✅        | Via `extractRecSourceDetailsMetadata`                     |
| `queryBoardId`          | `RecommendationSourceDetails`   | i64                                           | ✅        | Via `extractRecSourceDetailsMetadata`                     |
| `queryActionTimestamp`  | `RecommendationSourceDetails`   | i32                                           | ✅        | Via `extractRecSourceDetailsMetadata`                     |
| `querySignature`        | `RecommendationSourceDetails`   | string                                        | ✅        | Via `extractRecSourceDetailsMetadata`                     |
| `queryNeardupSignature` | `RecommendationSourceDetails`   | string                                        | ✅        | Via `extractRecSourceDetailsMetadata`                     |
| `imageSignature`        | `PinDetails`                    | string                                        | ✅        | Via `buildCandidateId` / `buildFunnelCandidate`           |
| `chunkSeparator`        | `PinDetails`                    | bool                                          | ✅        | Via `extractPinResultMetadata`                            |

#### Request-level `[R]`

| Field        | Source Object          | Type           | Captured? | Notes                                                      |
| ------------ | ---------------------- | -------------- | --------- | ---------------------------------------------------------- |
| `feedSource` | `FeedSourceIdentifier` | LeafIdentifier | ✅        | Via `CANDIDATE_FEED_SOURCE_IDENTIFIER` on each candidate   |
| `numPins`    | derived                | int            | ✅        | Via `stageCandidateCounts` in `HomefeedUnityFunnelContext` |

### Excluded Fields

| Field                         | Reason                                                       |
| ----------------------------- | ------------------------------------------------------------ |
| `binarySignature`             | Redundant with `imageSignature` (same data, binary encoding) |
| `transientInternalPinDetails` | Empty at this stage — populated by downstream scoring        |

### Notes

- Different feed sources populate different subsets of these fields. For example,
  INTEREST-based sources may not have `recSourceDetails`, and FOLLOWING_FEED sources
  have different `Reason` structures.
- `transientInternalPinDetails` is empty here because LWS, L1, and L2 scoring
  have not yet run.
- Staging verification: done (`beef95b`)

---

## Stage 5: AFTER_LWS_BATCHING

**Deferred** — out of scope.

---

## Stage 6: AFTER_LWS

**Code location:** `ScorpionUtils.getUnifiedLwsScoredPinsNode()` — right after
`annotatorNode` is produced by either `splitAndScoreLws()` (GPU path) or
`getL1ScorpionNode()` (non-GPU path), before Pin Selection V2 merge and before
`HomefeedUnifiedLwsPostProcessingNode` (diversity/cutoff). One log line per
active feed source.

**Objects available:** `List<InternalPinResult>` (per feed source)

### Selected Fields

#### Candidate/Pin-level `[C]` — new fields first appearing at this stage

| Field                                  | Source Object                 | Type             | Captured? | Notes                                  |
| -------------------------------------- | ----------------------------- | ---------------- | --------- | -------------------------------------- |
| `unifiedLwsScore`                      | `TransientInternalPinDetails` | double           | ✅        | `CANDIDATE_LWS_SCORE`                  |
| `lwsScoreTimeNs`                       | `TransientInternalPinDetails` | i64              | ✅        | `CANDIDATE_LWS_SCORE_TIME_NS`          |
| `lwsHeadsScores`                       | `TransientInternalPinDetails` | map<i32, double> | ✅        | `CANDIDATE_LWS_HEAD_{key}` per head    |
| `scorpionReturnedFeatures`             | `TransientInternalPinDetails` | UFR              | ❌        | Complex UFR type; not captured         |
| `isProduct`                            | `TransientInternalPinDetails` | bool             | ✅        | `CANDIDATE_IS_PRODUCT`                 |
| `isProductPin`                         | `TransientInternalPinDetails` | bool             | ✅        | `CANDIDATE_IS_PRODUCT_PIN`             |
| `isTmplDistroPrioritized`              | `TransientInternalPinDetails` | bool             | ✅        | `CANDIDATE_IS_TMPL_DISTRO_PRIORITIZED` |
| `isTrustWorthyProductFromPinSelection` | `TransientInternalPinDetails` | bool             | ✅        | `CANDIDATE_IS_TRUSTWORTHY_PRODUCT`     |
| `productShotScore`                     | `TransientInternalPinDetails` | double           | ✅        | `CANDIDATE_PRODUCT_SHOT_SCORE`         |
| `stockPhotoScore`                      | `TransientInternalPinDetails` | double           | ✅        | `CANDIDATE_STOCK_PHOTO_SCORE`          |
| `selectedPinId`                        | `TransientInternalPinDetails` | i64              | ✅        | `CANDIDATE_SELECTED_PIN_ID`            |
| `itemId`                               | `TransientInternalPinDetails` | string           | ✅        | `CANDIDATE_ITEM_ID`                    |

#### Carried forward from Stage 4 `[C]`

All `PinResult`/`PinDetails` fields from Stage 4 are still present (`pinId`,
`source`, `reasonToChoose`, `interestItemIdStr`, `throughProperties`,
`recSourceDetails`, `imageSignature`, `chunkSeparator`).

#### Request-level `[R]`

| Field        | Source Object          | Type           | Captured? | Notes                                  |
| ------------ | ---------------------- | -------------- | --------- | -------------------------------------- |
| `feedSource` | `FeedSourceIdentifier` | LeafIdentifier | ✅        | Via `CANDIDATE_FEED_SOURCE_IDENTIFIER` |
| `numPins`    | derived                | int            | ✅        | Via `stageCandidateCounts`             |

### Notes

- Feed sources with LWS inference disabled (e.g. `recgpt_v0_user_to_pins`)
  will have null `unifiedLwsScore`, `lwsHeadsScores`, and `lwsScoreTimeNs`.
  Pin Selection outputs are still populated.
- No pin enrichment fields at this stage — `qualityScore`, coteries, pin perf,
  locale, dimensions, etc. are all still empty/null. Enrichment happens downstream.
- Staging verification: done (`beef627`)

---

## Stage 7: AFTER_L1_PRESORT

**Code location:** `CandidateFetcher.processLws()` — right after
`ScorpionUtils.getUnifiedLwsScoredPinsNode()` returns (which includes
`HomefeedUnifiedLwsPostProcessingNode`). One log line per active feed source.

**Objects available:** `Node<List<InternalPinResult>>` (per feed source)

### Selected Fields

#### Candidate/Pin-level `[C]` — new fields first appearing at this stage

| Field                 | Source Object                 | Type   | Captured? | Notes                             |
| --------------------- | ----------------------------- | ------ | --------- | --------------------------------- |
| `lwsRank`             | `TransientInternalPinDetails` | i32    | ✅        | `CANDIDATE_LWS_RANK`              |
| `diversifiedLWSScore` | `TransientInternalPinDetails` | double | ✅        | `CANDIDATE_DIVERSIFIED_LWS_SCORE` |
| `useCaseBucket`       | `TransientInternalPinDetails` | i32    | ✅        | `CANDIDATE_USE_CASE_BUCKET`       |
| `pinUserClusterL1`    | `TransientInternalPinDetails` | i32    | ✅        | `CANDIDATE_PIN_USER_CLUSTER_L1`   |

#### Request-level `[R]`

| Field        | Source Object          | Type           | Captured? | Notes                                  |
| ------------ | ---------------------- | -------------- | --------- | -------------------------------------- |
| `feedSource` | `FeedSourceIdentifier` | LeafIdentifier | ✅        | Via `CANDIDATE_FEED_SOURCE_IDENTIFIER` |
| `numPins`    | derived                | int            | ✅        | Via `stageCandidateCounts`             |

### Notes

- `HomefeedUnifiedLwsPostProcessingNode` sorts by LWS score, applies
  through-ID/signature diversity penalty, and cuts off to `numLimit`.
- Some feed sources skip diversity and/or cutoff (e.g. board CLR, shopping CGs,
  all-CGs-LWS experiment sources), making this a pass-through — same pins,
  same count as Stage 6.
- Pin enrichment fields are still empty at this stage.
- Staging verification: done (`beef627`)

---

## Stage 8: AFTER_PRERANKING_FILTERING

**Code location:** `CandidateFetcher` — `applyPreScoringFilters()` is called in
two different places depending on the path:

- **`useL1Utility() == true` (prod path, 100% of normal homefeed):**
  Inside `processL1UtilityAndMerge()`, after feed source merge (Stage 6),
  `postLwsProcessing()` / pin enrichment (Stage 7), and before L2 ranking.
  Filtering runs on merged batches with `FeedSourceConstants.EXP_MULTIPLE`.

- **`useL1Utility() == false` (non-ALL targeting, NUX, holdout):**
  Per feed source, right after `processFeedSourcePins()` returns.

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field            | Source Object                                                          | Type   | Captured? | Notes                      |
| ---------------- | ---------------------------------------------------------------------- | ------ | --------- | -------------------------- |
| `pinId`          | `PinResult` via `pin.getPinResult().getPinId()`                        | i64    | ✅        | Via `buildCandidateId`     |
| `imageSignature` | `PinDetails` via `pin.getPinResult().getDetails().getImageSignature()` | string | ✅        | Via `buildFunnelCandidate` |

### Notes

- At this stage we only need to record which pins survived the pre-scoring
  filters. Full pin details are already cataloged in Stage 4 (pre-filtering)
  and Stage 10 (post-ranking).

---

## Stage 9: AFTER_L1_UTILITY

**Code location:** `CandidateFetcher.fetchContentWithL1Utility()` — right after
`processL1UtilityAndMerge()` returns and before `splitAndScore()`. At this point
all feed sources have been merged into a single list sorted by L1 utility score.

**Objects available:** `Node<List<InternalPinResult>>` (merged across all sources)

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field   | Source Object | Type | Captured? | Notes                  |
| ------- | ------------- | ---- | --------- | ---------------------- |
| `pinId` | `PinResult`   | i64  | ✅        | Via `buildCandidateId` |

#### Candidate/Pin-level `[C]` — new fields first appearing at this stage

| Field                  | Source Object                 | Type                 | Captured? | Notes                              |
| ---------------------- | ----------------------------- | -------------------- | --------- | ---------------------------------- |
| `lwScore`              | `TransientInternalPinDetails` | double               | ✅        | `CANDIDATE_LW_SCORE`               |
| `feedSourceIdentifier` | `TransientInternalPinDetails` | FeedSourceIdentifier | ✅        | `CANDIDATE_FEED_SOURCE_IDENTIFIER` |

#### From `InternalPinDetails` `[C]` — newly populated at this stage

| Field     | Source Object        | Type   | Captured? | Notes                |
| --------- | -------------------- | ------ | --------- | -------------------- |
| `boardId` | `InternalPinDetails` | i64    | ✅        | `CANDIDATE_BOARD_ID` |
| `score`   | `InternalPinDetails` | double | ✅        | `CANDIDATE_SCORE`    |

#### Request-level `[R]`

| Field     | Source Object | Type | Captured? | Notes                      |
| --------- | ------------- | ---- | --------- | -------------------------- |
| `numPins` | derived       | int  | ✅        | Via `stageCandidateCounts` |

### Notes

- This is the first stage where pins from all feed sources are merged into a
  single list. No per-source breakdown — just a flat list sorted by L1 utility.
- All fields from Stages 4, 6, and 7 are carried forward (LWS scores, Pin
  Selection outputs, `PinDetails`, etc.).
- Pin enrichment fields (coteries, pin perf, locale, etc.) are still empty —
  enrichment happens in `postLwsProcessing()` which runs after this merge but
  before L2 ranking.
- Staging verification: done (`beefcc3`)

---

## Stage 10: AFTER_RANKING_BATCHING

**Code location:** `CandidateFetcher.splitAndScore()` — inside the `.map("batched_node_l1_utility", ...)`
lambda, right after `splitIntoBatches()` returns. At this point the merged L1-sorted
list has been divided into up to `maxBatches` batches of size `batchSize` for L2 ranking.

**Objects available:** `Map<Integer, List<InternalPinResult>>` (batch index → pins)

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field   | Source Object | Type | Captured? | Notes                  |
| ------- | ------------- | ---- | --------- | ---------------------- |
| `pinId` | `PinResult`   | i64  | ✅        | Via `buildCandidateId` |

#### Request-level `[R]`

| Field          | Source Object  | Type          | Captured? | Notes                                           |
| -------------- | -------------- | ------------- | --------- | ----------------------------------------------- |
| `chunkId`      | `ChunkRequest` | i64           | ✅        | Captured at Stage 1 `entryLongMeta["CHUNK_ID"]` |
| `numBatches`   | derived        | int           | ✅        | Via `stageCandidateCounts`                      |
| `pinsPerBatch` | derived        | map<int, int> | ✅        | Via `stageCandidateCounts`                      |

### Notes

- The code already emits Stats histograms for `num_batches`, `num_batches_non_empty`,
  and per-batch `batch_size` — the full funnel log mirrors this as a single dictionary.
- Trailing batches may be empty (0 pins) when the total candidate count is less
  than `maxBatches * batchSize`.
- Pin data is unchanged from Stage 9; `pinId` is recorded to track which pins
  are in which batch.

---

## Stage 11: AFTER_RANKING

**Code location:** `HomefeedAllPlanner.getContentChunkNode()` — right after
`CandidateFetcher.fetchContentFromFeedSources()` returns. At this point LWS,
L1 utility, and L2 ranking have all run inside `fetchContentWithL1Utility()`.

**Objects available:** `Map<FeedSourceIdentifier, List<InternalPinResult>>`

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field   | Source Object | Type | Captured? | Notes                  |
| ------- | ------------- | ---- | --------- | ---------------------- |
| `pinId` | `PinResult`   | i64  | ✅        | Via `buildCandidateId` |

Fields carried forward from earlier stages (Stages 4, 6, 7) are not repeated
here. See those stages for other `PinResult`/`PinDetails` fields and LWS scores.

#### From `PinResult.PinDetails` `[C]` — new at this stage

| Field                  | Source Object | Type                  | Captured? | Notes                                |
| ---------------------- | ------------- | --------------------- | --------- | ------------------------------------ |
| `feedSource`           | `PinDetails`  | FeedSourceIdentifier  | ✅        | `CANDIDATE_FEED_SOURCE_IDENTIFIER`   |
| `nativeFormatType`     | `PinDetails`  | NativeFormatType enum | ✅        | `CANDIDATE_NATIVE_FORMAT_TYPE`       |
| `isNonSingleImgNative` | `PinDetails`  | bool                  | ✅        | `CANDIDATE_IS_NON_SINGLE_IMG_NATIVE` |

#### From `InternalPinDetails` `[C]` — new at this stage

| Field          | Source Object        | Type | Captured? | Notes                     |
| -------------- | -------------------- | ---- | --------- | ------------------------- |
| `scoreVersion` | `InternalPinDetails` | i32  | ✅        | `CANDIDATE_SCORE_VERSION` |
| `ownerId`      | `InternalPinDetails` | i64  | ✅        | `CANDIDATE_OWNER_ID`      |

#### From `TransientInternalPinDetails` `[C]` — new at this stage (pin enrichment + L2 ranking)

| Field                         | Source Object                 | Type                        | Captured? | Notes                                                            |
| ----------------------------- | ----------------------------- | --------------------------- | --------- | ---------------------------------------------------------------- |
| `qualityScore`                | `TransientInternalPinDetails` | double                      | ✅        | `CANDIDATE_QUALITY_SCORE`                                        |
| `unadjustedQualityScore`      | `TransientInternalPinDetails` | double                      | ✅        | `CANDIDATE_UNADJUSTED_QUALITY_SCORE`                             |
| `isVideo`                     | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_IS_VIDEO`                                             |
| `isNative`                    | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_IS_NATIVE`                                            |
| `isRepin`                     | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_IS_REPIN`                                             |
| `height`                      | `TransientInternalPinDetails` | i32                         | ✅        | `CANDIDATE_HEIGHT`                                               |
| `width`                       | `TransientInternalPinDetails` | i32                         | ✅        | `CANDIDATE_WIDTH`                                                |
| `pinnabilityMultiScores`      | `TransientInternalPinDetails` | map<i32, double>            | ✅        | `CANDIDATE_PINNABILITY_MULTI_SCORES` (intDoubleMap feature type) |
| `pinJoinHfPerfSignal`         | `TransientInternalPinDetails` | PinJoinHfPerfSignal         | ❌        | Complex nested struct; not captured                              |
| `scoreTimeNs`                 | `TransientInternalPinDetails` | i64                         | ✅        | `CANDIDATE_SCORE_TIME_NS`                                        |
| `realtimePinPerf`             | `TransientInternalPinDetails` | RealtimePinPerf             | ❌        | Complex struct; not captured                                     |
| `pinCreationTimeMs`           | `TransientInternalPinDetails` | i64                         | ✅        | `CANDIDATE_PIN_CREATION_TIME_MS`                                 |
| `rootUserId`                  | `TransientInternalPinDetails` | i64                         | ✅        | `CANDIDATE_ROOT_USER_ID`                                         |
| `objectStartActivationTimeMs` | `TransientInternalPinDetails` | i64                         | ✅        | `CANDIDATE_OBJECT_START_ACTIVATION_TIME_MS`                      |
| `annotationsToCoteries`       | `TransientInternalPinDetails` | map<i64, InternalCoterie>   | ❌        | Complex nested map; not captured                                 |
| `coteriesByLevel`             | `TransientInternalPinDetails` | list<list<InternalCoterie>> | ❌        | Complex nested list; not captured                                |
| `coteriesL1`                  | `TransientInternalPinDetails` | list<InternalCoterie>       | ❌        | Complex nested list; not captured                                |
| `isActive`                    | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_IS_ACTIVE`                                            |
| `isHidden`                    | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_IS_HIDDEN`                                            |
| `pinDescriptionLanguage`      | `TransientInternalPinDetails` | i32                         | ✅        | `CANDIDATE_PIN_DESCRIPTION_LANGUAGE`                             |
| `variantMetaData`             | `TransientInternalPinDetails` | VariantMetadata             | ❌        | Complex struct; not captured                                     |
| `trustSafetyDecision`         | `TransientInternalPinDetails` | TrustSafetyDecision         | ❌        | Complex struct; not captured                                     |
| `neardupSignature`            | `TransientInternalPinDetails` | string                      | ✅        | `CANDIDATE_NEARDUP_SIGNATURE`                                    |
| `rootUserCountry`             | `TransientInternalPinDetails` | string                      | ✅        | `CANDIDATE_ROOT_USER_COUNTRY`                                    |
| `textLocale`                  | `TransientInternalPinDetails` | LocaleResult                | ❌        | Complex struct (language, country, sources); not captured        |
| `rootUserLocale`              | `TransientInternalPinDetails` | string                      | ✅        | `CANDIDATE_ROOT_USER_LOCALE`                                     |
| `contentNeardupSignature`     | `TransientInternalPinDetails` | string                      | ✅        | `CANDIDATE_CONTENT_NEARDUP_SIGNATURE`                            |
| `rootUserVisibleToPublic`     | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_ROOT_USER_VISIBLE_TO_PUBLIC`                          |
| `isProductTaggedIdeaPin`      | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_IS_PRODUCT_TAGGED_IDEA_PIN`                           |
| `pinLocale`                   | `TransientInternalPinDetails` | PinLevelLocale              | ❌        | Complex struct (language weights, neutral scores); not captured  |
| `skinToneBucketV3`            | `TransientInternalPinDetails` | enum                        | ✅        | `CANDIDATE_SKIN_TONE_BUCKET_V3`                                  |
| `rootUserVisibleToPublicV2`   | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_ROOT_USER_VISIBLE_TO_PUBLIC_V2`                       |
| `bodySizeV1`                  | `TransientInternalPinDetails` | enum                        | ✅        | `CANDIDATE_BODY_SIZE_V1`                                         |
| `rootUserOptInPrivateAccount` | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_ROOT_USER_OPT_IN_PRIVATE_ACCOUNT`                     |
| `commonRealtimePinPerf`       | `TransientInternalPinDetails` | UFR                         | ❌        | UFR type; not captured                                           |
| `feedSourceIdentifier`        | `TransientInternalPinDetails` | FeedSourceIdentifier        | ✅        | `CANDIDATE_FEED_SOURCE_IDENTIFIER`                               |
| `method`                      | `TransientInternalPinDetails` | string                      | ✅        | `CANDIDATE_METHOD`                                               |
| `boardIsPrivate`              | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_BOARD_IS_PRIVATE`                                     |
| `boardHiddenFromFeeds`        | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_BOARD_HIDDEN_FROM_FEEDS`                              |
| `boardExists`                 | `TransientInternalPinDetails` | bool                        | ✅        | `CANDIDATE_BOARD_EXISTS`                                         |
| `boardCollaborators`          | `TransientInternalPinDetails` | list                        | ❌        | Complex list type; not captured                                  |
| `pinLevelSmsOutputsToLog`     | `TransientInternalPinDetails` | UFR                         | ❌        | UFR type (~30 tensor features); not captured                     |
| `commonRealtimePinClip`       | `TransientInternalPinDetails` | UFR                         | ❌        | UFR type; not captured                                           |

#### From `TransientInternalPinDetails` `[C]` — updated from earlier stages

| Field                      | Source Object                 | Type | Captured? | Notes                          |
| -------------------------- | ----------------------------- | ---- | --------- | ------------------------------ |
| `scorpionReturnedFeatures` | `TransientInternalPinDetails` | UFR  | ❌        | Complex UFR type; not captured |

#### Request-level `[R]`

| Field        | Source Object          | Type           | Captured? | Notes                                  |
| ------------ | ---------------------- | -------------- | --------- | -------------------------------------- |
| `feedSource` | `FeedSourceIdentifier` | LeafIdentifier | ✅        | Via `CANDIDATE_FEED_SOURCE_IDENTIFIER` |
| `numPins`    | derived                | int            | ✅        | Via `stageCandidateCounts`             |

### Excluded Fields

| Field                  | Reason                                |
| ---------------------- | ------------------------------------- |
| `binarySignature`      | Redundant with `imageSignature`       |
| `queryActionTimestamp` | Not needed for debugging              |
| `auxData`              | Pin aux data not needed at this stage |

### Notes

- This is the output of `fetchContentFromFeedSources()` which includes candidate
  fetching, LWS, L1 utility, and L2 ranking (Scorpion). The `transientInternalPinDetails`
  is now fully populated with scores, features, and metadata.
- `internalDetails.score` is 0 at this stage — the final blender score is applied later.
- LWS-related fields (`unifiedLwsScore`, `lwsHeadsScores`, `lwsScoreTimeNs`,
  `diversifiedLWSScore`, `lwsRank`) first appear at Stages 6/7 and are carried forward.
- Pin Selection fields (`isProduct`, `isProductPin`, `isTmplDistroPrioritized`,
  `isTrustWorthyProductFromPinSelection`, `productShotScore`, `stockPhotoScore`,
  `selectedPinId`, `itemId`) first appear at Stage 6 and are carried forward.
- Staging verification: done (`beef95b`)

---

## Stage 12: AFTER_POST_RANKING_FILTERING

**Code location:** `HomefeedAllPlanner.getContentChunkNode()` — right after
`applyPostScoringFilters()` returns, before blending begins.

**Objects available:** `Node<Map<FeedSourceIdentifier, List<InternalPinResult>>>`

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field            | Source Object | Type   | Captured? | Notes                      |
| ---------------- | ------------- | ------ | --------- | -------------------------- |
| `pinId`          | `PinResult`   | i64    | ✅        | Via `buildCandidateId`     |
| `imageSignature` | `PinDetails`  | string | ✅        | Via `buildFunnelCandidate` |

#### Request-level `[R]`

| Field            | Source Object  | Type             | Captured? | Notes                                           |
| ---------------- | -------------- | ---------------- | --------- | ----------------------------------------------- |
| `chunkId`        | `ChunkRequest` | i64              | ✅        | Captured at Stage 1 `entryLongMeta["CHUNK_ID"]` |
| `totalPins`      | derived        | int              | ✅        | Via `stageCandidateCounts`                      |
| `perSourceCount` | derived        | map<string, int> | ✅        | Via `stageCandidateCounts`                      |

### Notes

- At this stage we record which pins survived the post-scoring filters, mirroring
  Stage 8 (AFTER_PRERANKING_FILTERING). Full pin details are already cataloged
  in Stage 11 (AFTER_RANKING).
- Comparing `totalPins` here against Stage 11 shows how many candidates were
  dropped by post-ranking filters.
- `perSourceCount` keys use `HomefeedCommonUtils.getFeedSourceIdentifierString()`.
- Staging verification: skipped (straightforward filter output)

---

## Stage 13: AFTER_PRESORT

**Code location:** `ScoreSortedUnionBlenderNode.blend()` — after pinner utility
scoring, sort by pinner utility score, and deduplication. Right before the output
candidate list is assembled.

**Objects available:** `List<InternalPinResult>` (sorted by pinner utility score)

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field                          | Source Object                 | Type   | Captured? | Notes                                        |
| ------------------------------ | ----------------------------- | ------ | --------- | -------------------------------------------- |
| `pinId`                        | `PinResult`                   | i64    | ✅        | Via `buildCandidateId`                       |
| `presortPinnerUtilityScore`    | `TransientInternalPinDetails` | double | ✅        | `CANDIDATE_PRESORT_UTILITY_SCORE`            |
| `l3SamplingPinnerUtilityScore` | `TransientInternalPinDetails` | double | ✅        | `CANDIDATE_L3_SAMPLING_PINNER_UTILITY_SCORE` |

#### Request-level `[R]`

| Field           | Source Object | Type | Captured? | Notes                      |
| --------------- | ------------- | ---- | --------- | -------------------------- |
| `numCandidates` | derived       | int  | ✅        | Via `stageCandidateCounts` |

### Notes

- `ScoreSortedUnionBlenderNode` merges prod and experimental candidates from
  `ProdFeedSourceBlenderNode` and `ExpFeedSourceBlenderNode`, computes pinner
  utility scores, and sorts by those scores.
- This stage captures the ordering purely based on pinner utility — before any
  diversity penalties are applied. Compare with Stage 14 to see the diversity effect.

---

## Stage 14: AFTER_PRESORT_DIVERSITY

**Code location:** `DiversifyingBlenderNode.blend()` — after coterie-based diversity
penalty, intent diversification, final sort by presort pinner utility score, and
merchant proportionality reordering. Right before stats tracking.

**Objects available:** `List<HomefeedUnityCandidate>` (reordered candidates)

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field                          | Source Object                 | Type   | Captured? | Notes                                        |
| ------------------------------ | ----------------------------- | ------ | --------- | -------------------------------------------- |
| `pinId`                        | `PinResult`                   | i64    | ✅        | Via `buildCandidateId`                       |
| `presortPinnerUtilityScore`    | `TransientInternalPinDetails` | double | ✅        | `CANDIDATE_PRESORT_UTILITY_SCORE`            |
| `preDiversityRank`             | `TransientInternalPinDetails` | i32    | ✅        | `CANDIDATE_PRE_DIVERSITY_RANK`               |
| `l3SamplingPinnerUtilityScore` | `TransientInternalPinDetails` | double | ✅        | `CANDIDATE_L3_SAMPLING_PINNER_UTILITY_SCORE` |
| `pinTags`                      | `TransientInternalPinDetails` | list   | ✅        | `CANDIDATE_PIN_TAGS` (intSet feature type)   |
| `rootPinId`                    | `TransientInternalPinDetails` | i64    | ✅        | `CANDIDATE_ROOT_PIN_ID`                      |
| `pinUserCluster`               | `TransientInternalPinDetails` | i32    | ✅        | `CANDIDATE_PIN_USER_CLUSTER`                 |

#### Request-level `[R]`

| Field           | Source Object | Type | Captured? | Notes                      |
| --------------- | ------------- | ---- | --------- | -------------------------- |
| `numCandidates` | derived       | int  | ✅        | Via `stageCandidateCounts` |

### Notes

- `DiversifyingBlenderNode` runs inside the `BlenderChain`, not in `HomefeedAllPlanner`.
- The presort utility score is the penalized pinner utility after coterie-based
  diversity and optional intent (UIC cluster) diversification.
- Merchant proportionality reordering may further change the order after scoring.
- Staging verification: done (`beef779`)

---

## Stage 15: AFTER_SSD

**Code location:** `HomefeedSsdServingNode.blend()` — after L3/SSD model scoring
and reordering, right before the `BlenderLogEntry` is created and results returned.

**Objects available:** `List<InternalPinResult>` (reordered by SSD scores)

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field                     | Source Object       | Type   | Captured? | Notes                                                        |
| ------------------------- | ------------------- | ------ | --------- | ------------------------------------------------------------ |
| `pinId`                   | `PinResult`         | i64    | ✅        | Via `buildCandidateId`                                       |
| `ssdRank`                 | derived             | i32    | ✅        | Implicitly captured as candidate position at AFTER_SSD stage |
| `ssdRewardScore`          | `allReturnedScores` | double | ✅        | `SSD_REWARD_SCORE` via `enrichWithSsdScores`                 |
| `ssdMultiHeadScore`       | `allReturnedScores` | double | ✅        | `SSD_MULTIHEAD_SCORE` via `enrichWithSsdScores`              |
| `softSpacingPenaltyScore` | `allReturnedScores` | double | ✅        | `SSD_SOFT_SPACING_PENALTY` via `enrichWithSsdScores`         |
| `pinnerUtilityScore`      | `allReturnedScores` | double | ✅        | Via `DEBUGGING_COLUMNS` loop in `HomefeedSsdServingNode`     |
| `pinclipImgDiversity`     | `allReturnedScores` | double | ✅        | Via `DEBUGGING_COLUMNS` loop in `HomefeedSsdServingNode`     |
| `textDiversity`           | `allReturnedScores` | double | ✅        | Via `DEBUGGING_COLUMNS` loop in `HomefeedSsdServingNode`     |
| `gsDiversity`             | `allReturnedScores` | double | ✅        | Via `DEBUGGING_COLUMNS` loop in `HomefeedSsdServingNode`     |

#### Request-level `[R]`

| Field           | Source Object | Type | Captured? | Notes                      |
| --------------- | ------------- | ---- | --------- | -------------------------- |
| `numCandidates` | derived       | int  | ✅        | Via `stageCandidateCounts` |

### Excluded Fields

| Field                            | Reason                                                |
| -------------------------------- | ----------------------------------------------------- |
| `output_l3_repin/closeup/p2pimp` | All -1.0 at runtime — not populated in current model  |
| `*_empty_embedding` columns      | Diagnostic flags (0.0 = has embedding), not needed    |
| Duplicate diversity columns      | Old vs new model ordering — only one set is populated |

### Notes

- SSD (L3) reranks the top `numPinsToScore` candidates using multi-head L3 model
  scores. Pins outside that window keep their presort order.
- If the input list has fewer than `numPinsToScore` pins, or L3 scores are missing,
  SSD is a no-op and returns the input unchanged.
- All SSD scores are **ephemeral** — they exist only inside `HomefeedSsdServingNode.blend()`
  and are never written to `InternalPinResult`. The only persistent effect is the
  reordered rank.
- `ssdRewardScore` clearly drives ranking (98, 97, 96 for ranks 1, 2, 3 in sample).
- Staging verification: done (`beeffb5`)

---

## Stage 16: FINAL_CHUNK

**Code location:** `HomefeedAllPlanner.getContentChunkNode()` — right before the
final `return` statement, after all blending, caching, DSA, and subchunk processing.

**Objects available:** `Node<ContentChunk>`

### Selected Fields

#### Candidate/Pin-level `[C]`

| Field   | Source Object | Type | Captured? | Notes                       |
| ------- | ------------- | ---- | --------- | --------------------------- |
| `pinId` | `FeedObject`  | i64  | ✅        | Via `buildFromContentChunk` |

#### Request-level `[R]`

| Field     | Source Object  | Type | Captured? | Notes                                                |
| --------- | -------------- | ---- | --------- | ---------------------------------------------------- |
| `chunkId` | `ChunkRequest` | i64  | ✅        | Captured at Stage 1 `entryLongMeta["CHUNK_ID"]`      |
| `numPins` | derived        | int  | ✅        | `finalChunkNumPins` → `NUM_PINS` in request metadata |

### Notes

- The `ContentChunk` contains `FeedObject` (external-facing), not
  `InternalPinResult`. All internal details (scores, features, transient data)
  are stripped at this point — only `pinId` and external pin metadata remain.
- This is the final stage — comparing pin IDs here against Stage 15 shows which
  pins were dropped or added by post-SSD processing (caching, DSA opt-out, etc.).
- Staging verification: done — `FeedObject` contains `objectId` (pinId), `objectType`,
  `feedSource`, `fantasioReason`, `pinnabilityMultiScores`, image signatures, `nativeFormatType`.
  All internal scores/transient data are stripped at this point.

---

## Funnel Output Data (Thrift → DTBX / Hive)

Every sampled request produces a `UnityFunnel` Thrift object containing three
top-level sections. This is what appears in Discovery Toolbox (DTBX) and the
`default.unity_funnel_log_dev_hr_v2` Hive table.

### `unityFunnelRequest`

| Field                  | Type                | Source                                                  |
| ---------------------- | ------------------- | ------------------------------------------------------- |
| `id`                   | string              | Trace ID (decimal) via `UnityUtils.getTraceIdDecimal()` |
| `triggeredExperiments` | map<string, string> | All activated experiments from `ExperimentManager`      |
| `requestMetadata`      | `FunnelMetadata`    | See subsections below                                   |

#### `requestMetadata.intFunnelMetadata` (map<string, i32>)

| Key pattern                   | Source                     | Notes                                                                                                          |
| ----------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `NUM_CANDIDATES_{STAGE_NAME}` | `stageCandidateCounts` map | One entry per stage that evaluates; recorded in `evaluatePostProcess` via `.merge(stage, count, Integer::sum)` |
| `SIZER_BUDGET_{feedSourceId}` | `sizerBudgets` map         | Per-source sizer budget from Stage 2                                                                           |

Stages that produce `NUM_CANDIDATES_*` entries (all 12 stages with loggers):
`AFTER_CANDIDATE_GENERATION`, `AFTER_LWS`, `AFTER_L1_PRESORT`,
`AFTER_PRERANKING_FILTERING`, `AFTER_L1_UTILITY`, `AFTER_RANKING_BATCHING`,
`AFTER_RANKING`, `AFTER_POST_RANKING_FILTERING`, `AFTER_PRESORT`,
`AFTER_PRESORT_DIVERSITY`, `AFTER_SSD`, `FINAL_CHUNK`.

Per-feed-source stages (4, 6, 7, 8) accumulate via `Integer::sum` across all
feed sources into a single count per stage type.

#### `requestMetadata.longFunnelMetadata` (map<string, i64>)

| Key pattern            | Source               | Notes                                                                                   |
| ---------------------- | -------------------- | --------------------------------------------------------------------------------------- |
| `LATENCY_{STAGE_NAME}` | `stageLatencies` map | Wall-clock ms from `startTimeMs` to stage evaluation; recorded in `evaluatePostProcess` |
| `NUM_PINS`             | `finalChunkNumPins`  | Number of pins in the final content chunk (only if > 0)                                 |
| `CHUNK_ID`             | `entryLongMeta`      | From Stage 1 request entry metadata                                                     |
| `DEVICE`               | `entryLongMeta`      | From Stage 1 request entry metadata                                                     |
| `USER_JOIN_DATE`       | `entryLongMeta`      | From Stage 1 request entry metadata                                                     |

Stages that produce `LATENCY_*` entries: same 12 stages as candidate counts.
These measure cumulative wall-clock latency from request entry, NOT
per-stage duration. To get per-stage duration, subtract consecutive stage
latencies.

#### `requestMetadata.stringFunnelMetadata` (map<string, string>)

| Key                      | Source            | Notes        |
| ------------------------ | ----------------- | ------------ |
| `TARGETING_CONTEXT_TYPE` | `entryStringMeta` | From Stage 1 |
| `SOURCE_ENDPOINT`        | `entryStringMeta` | From Stage 1 |
| `SOURCE_SERVICE`         | `entryStringMeta` | From Stage 1 |
| `APP_VERSION`            | `entryStringMeta` | From Stage 1 |

### `unityFunnelUser`

| Field          | Type           | Source                                                                 |
| -------------- | -------------- | ---------------------------------------------------------------------- |
| `id`           | i64            | `UserInfo.id` from `StructuredFeedRequest`                             |
| `country`      | Country        | `UserInfo.country`                                                     |
| `gender`       | Gender         | `UserInfo.gender`                                                      |
| `isEmployee`   | bool           | `UserInfo.isEmployee`                                                  |
| `locale`       | string         | `UserInfo.locale`                                                      |
| `appType`      | AppType        | `SessionInfo.appType`                                                  |
| `sessionId`    | string         | `SessionInfo.sessionId`                                                |
| `userMetadata` | FunnelMetadata | UIC features from `HomefeedUnityFunnelContext.userUicFeaturesMetadata` |

### `unityFunnelCandidates`

map<i64, `UnityFunnelCandidate`> — keyed by `candidateId` (pinId or
UUID-from-imgSig). Each candidate records the furthest stage it reached
(`furthestStage`) and per-stage metadata. See individual stage sections
above for which fields are captured at each stage.

### Recording mechanism

`HomefeedUnityFunnelLoggerNode.evaluatePostProcess()` fires for each stage
during Apex graph evaluation. It records two things to the
`HomefeedUnityFunnelContext`:

1. **Stage latency**: `stageLatencies.put(stage, System.currentTimeMillis() - startTimeMs)`
2. **Candidate count**: `stageCandidateCounts.merge(stage, candidateCount, Integer::sum)`

After graph evaluation completes, `HomefeedUnityFunnelLoggerMergerNode`
(for Hive logging) or `UnityBackend.setUnity2ContextDebugInfo()` (for DTBX)
reads these maps and writes them into the `FunnelMetadata` Thrift struct.

---

## Open Items

- ~~**Pin tags / content-type flags:**~~ **Resolved.** All items now recorded:
  - `isVideo` — Stage 11. `isProduct`, `isProductPin` — Stage 7.
  - `isTrustWorthyProductFromPinSelection`, `isTmplDistroPrioritized` — Stage 7.
  - `isFresh` — derived from `objectStartActivationTimeMs` (Stage 11). No stored field.
  - `isOffsite` — derived from `feedSourceIdentifier` (Stages 9, 11). No stored field.
  - `pinTags` (full PinTag enum) — Stage 14 (AFTER_PRESORT_DIVERSITY, blender phase).
- ~~**UIC UFR user features (`getUICUfrUserFeaturesNode` output):**~~ **Resolved.**
  Added `userFeatureUfrNode` (full merged UFR) as a user-level `[U]` field in
  Stage 3 (AFTER_RESOURCE_FETCHING).

---

# Funnel Latency Stats

Measures wall-clock latency from `startTime` (captured at the top of
`HomefeedAllPlanner.getContentChunkNode()`) to each pipeline stage.
All measurements are recorded at **node evaluation time** (inside `.map()`
callbacks), not during graph construction.

## How it works

1. `startTime` is captured via `HomefeedDependencies.getDependencies().getClock().millis()`
   at the entry of `getContentChunkNode()`.
2. A `funnelLatencyTags` string is built using `StatsTagsCreator` with:
   - `targeting_context_type` (e.g. `all`, `board_more_ideas`)
3. Both values are threaded as parameters through the call chain.
4. At each stage, a `.map()` is attached to the output node. When the node
   evaluates, it records `Stats.histogram(statName + tags, clock.millis() - startTime)`
   and returns the result unchanged.
5. For per-feed-source stages, a `feed_source_identifier` tag is appended.
6. Paths that don't originate from the homefeed planner (e.g. discover stream)
   pass `startTimeMs=0` to skip measurement.

## Pipeline structure

```
Per feed source (parallel):
  Stage 4 (candidate generation)
    → Stage 6 (LWS scoring)
      → Stage 7 (L1 presort)
        → Stage 8 non-ALL path (preranking filtering, per feed source)

All feed sources merge via processL1UtilityAndMerge:
  Stage 9 (L1 utility) — mergedFeedsourceNode
    → Stage 10 (ranking batching) — splitAndScore batches merged pins
      → Stage 8 ALL path (preranking filtering, post-merge batches)
        → L2 scoring

Back in HomefeedAllPlanner:
  Stage 11 (after ranking) — feedSourceNode returned from fetchContentFromFeedSources
    → Stage 12 (post-ranking filtering)
      → Stage 13 (presort blending)
        → Stage 14 (presort diversity)
          → Stage 15 (SSD)
            → Stage 16 (final chunk)
```

## Stat name format

```
{statsPrefix}.funnel_latency.{stage_name} targeting_context_type={ctx}
```

Per-feed-source stages (4, 6, 7, 8-non-ALL) additionally include:

```
feed_source_identifier={feedSourceId}
```

Post-merge stages (8-ALL, 9, 10, 11, 12, 13–16) do NOT include
`feed_source_identifier` since all sources are merged at that point.

## Exact stat names

### Tags

All stats include: `targeting_context_type`

Per-feed-source stages additionally include: `feed_source_identifier`

### Per-feed-source stages

| Stage | Stat name                                                                    |
| ----- | ---------------------------------------------------------------------------- |
| 4     | `unity-homefeed.candidate_fetcher.funnel_latency.after_candidate_generation` |
| 6     | `unity-homefeed.candidate_fetcher.unified_lws_node.funnel_latency.after_lws` |
| 7     | `unity-homefeed.candidate_fetcher.funnel_latency.after_l1_presort`           |
| 8     | `unity-homefeed.candidate_fetcher.funnel_latency.after_preranking_filtering` |

### Post-merge stages

| Stage | Stat name                                                                    |
| ----- | ---------------------------------------------------------------------------- |
| 8     | `unity-homefeed.candidate_fetcher.funnel_latency.after_preranking_filtering` |
| 9     | `unity-homefeed.candidate_fetcher.funnel_latency.after_l1_utility`           |
| 10    | `unity-homefeed.candidate_fetcher.funnel_latency.after_ranking_batching`     |
| 11    | `unity-homefeed.funnel_latency.after_ranking`                                |
| 12    | `unity-homefeed.funnel_latency.after_post_ranking_filtering`                 |
| 13    | `unity-homefeed.funnel_latency.after_presort`                                |
| 14    | `unity-homefeed.funnel_latency.after_presort_diversity`                      |
| 15    | `unity-homefeed.funnel_latency.after_ssd`                                    |
| 16    | `unity-homefeed.funnel_latency.final_chunk`                                  |

## Parameter threading

```
HomefeedAllPlanner.getContentChunkNode()            (defines startTime, funnelLatencyTags)
  └─ CandidateFetcher.fetchContentFromFeedSources   (startTimeMs, funnelLatencyTags)
       └─ CandidateFetcher.fetchContentWithL1Utility (startTimeMs, funnelLatencyTags)
            ├─ Stage 4: .map() on pinListNode                          [per feed source]
            ├─ processLws                            (startTimeMs, funnelLatencyTags)
            │    ├─ ScorpionUtils.getUnifiedLwsScoredPinsNode
            │    │    └─ Stage 6: .map() on annotatorNode              [per feed source]
            │    └─ Stage 7: .map() on feedSourcePinsNode              [per feed source]
            ├─ processFeedSourcePins → processLws (same as above)
            ├─ Stage 8 (non-ALL): .map() on pinListNode               [per feed source]
            ├─ processL1UtilityAndMerge              ── feed sources merge here ──
            │    └─ Stage 9: .map() on mergedFeedsourceNode            [merged]
            └─ splitAndScore                         (startTimeMs, funnelLatencyTags)
                 ├─ Stage 10: inside .map() on batchedFeedsourceNode   [merged]
                 └─ Stage 8 (ALL): .map() on pinsToScore               [merged]
  └─ BlenderChain                                  (funnelStartTimeMs, funnelLatencyTags)
       ├─ Stage 13: .map() on scoreSortedUnionBlenderNode              [merged]
       ├─ Stage 14: .map() on diversifyBlenderNode                     [merged]
       └─ Stage 15: .map() on homefeedL3RerankingNode (in createL3ServingNode) [merged]
```

## Completed stages

| Stage | Name                         | Stat suffix                    | File                      | Node                                       | Feed source tag?         |
| ----- | ---------------------------- | ------------------------------ | ------------------------- | ------------------------------------------ | ------------------------ |
| 4     | AFTER_CANDIDATE_GENERATION   | `after_candidate_generation`   | `CandidateFetcher.java`   | `pinListNode`                              | Yes                      |
| 6     | AFTER_LWS                    | `after_lws`                    | `ScorpionUtils.java`      | `annotatorNode`                            | Yes                      |
| 7     | AFTER_L1_PRESORT             | `after_l1_presort`             | `CandidateFetcher.java`   | `feedSourcePinsNode`                       | Yes                      |
| 8     | AFTER_PRERANKING_FILTERING   | `after_preranking_filtering`   | `CandidateFetcher.java`   | `pinListNode` / `pinsToScore`              | Yes (non-ALL) / No (ALL) |
| 9     | AFTER_L1_UTILITY             | `after_l1_utility`             | `CandidateFetcher.java`   | `mergedFeedsourceNode`                     | No                       |
| 10    | AFTER_RANKING_BATCHING       | `after_ranking_batching`       | `CandidateFetcher.java`   | inside `.map()` on `batchedFeedsourceNode` | No                       |
| 11    | AFTER_RANKING                | `after_ranking`                | `HomefeedAllPlanner.java` | `feedSourceNode`                           | No                       |
| 12    | AFTER_POST_RANKING_FILTERING | `after_post_ranking_filtering` | `HomefeedAllPlanner.java` | `feedSourceNode`                           | No                       |
| 13    | AFTER_PRESORT                | `after_presort`                | `BlenderChain.java`       | `.map()` on `scoreSortedUnionBlenderNode`  | No                       |
| 14    | AFTER_PRESORT_DIVERSITY      | `after_presort_diversity`      | `BlenderChain.java`       | `.map()` on `diversifyBlenderNode`         | No                       |
| 15    | AFTER_SSD                    | `after_ssd`                    | `BlenderChain.java`       | `.map()` on `homefeedL3RerankingNode`      | No                       |
| 16    | FINAL_CHUNK                  | `final_chunk`                  | `HomefeedAllPlanner.java` | `blendedContentChunkNode`                  | No                       |

## Remaining stages (TODO)

Each of these has a `// FULL FUNNEL LOGGING` comment marker in the code.
The approach is the same: thread `startTimeMs` + `funnelLatencyTags` to the
method, then attach `.map()` on the output node at the marker location.

| Stage | Name                    | File                                            | Notes                           |
| ----- | ----------------------- | ----------------------------------------------- | ------------------------------- |
| 1     | AT_REQUEST_ENTRY        | `HomefeedAllPlanner.java:199`                   | Skipped — always ~0ms           |
| 2     | AFTER_SIZER_CALCULATION | `HomefeedAllPlanner.java:388`, `Sizer.java:290` | Synchronous; low value          |
| 3     | AFTER_RESOURCE_FETCHING | `HomefeedAllPlanner.java:624`                   | No single output node           |
| 5     | AFTER_LWS_BATCHING      | —                                               | Deferred / no marker exists yet |

### How to add a remaining stage

1. Find the `// FULL FUNNEL LOGGING` comment for the stage.
2. Identify the output node at that point (the node whose evaluation means the
   stage's work is done).
3. Thread `long startTimeMs` and `String funnelLatencyTags` as parameters
   through the call chain from the nearest caller that already has them.
4. Add:
   ```java
   if (startTimeMs > 0) {
     outputNode = outputNode.map(
         "funnel_latency.{stage_name}",
         result -> {
           Stats.histogram(
               statsPrefix + ".funnel_latency.{stage_name}" + funnelLatencyTags,
               HomefeedDependencies.getDependencies().getClock().millis() - startTimeMs);
           return result;
         });
   }
   ```
5. For per-feed-source stages, append the feed source tag to `funnelLatencyTags`:
   ```java
   final String tagsWithSource =
       funnelLatencyTags
           + " " + StatsTagsCreator.FEED_SOURCE_IDENTIFIER_TAG_NAME
           + "=" + feedSourceIdStr;
   ```
6. For call sites that don't originate from the homefeed planner, pass
   `0L` and `""` to skip measurement.
