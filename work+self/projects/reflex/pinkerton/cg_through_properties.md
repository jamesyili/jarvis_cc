# CG Through Entity Properties — Full Reference

*Created 2026-04-14. Code-verified against Optimus `unity/server/src/main/java/com/pinterest/unity/server/homefeed/`.*

---

## What Is the "Through Entity"?

The **through entity** is the provenance trail for a homefeed candidate — it answers **"what user signal triggered this candidate's retrieval?"** For example, if a user repinned a pin with image signature `abc123` and that action seeded a Pixie P2P retrieval that returned candidate pin `XYZ`, then `abc123` is the through entity.

### Three Fields Carry This Information

All three live on the `Reason` object (`fantasioReason`) attached to each candidate's `PinDetails`:

| Field | Thrift Type | FVL Column | Purpose |
|---|---|---|---|
| `interestItemId` | `i64` | `throughId` | Numeric through entity: pin ID, board ID, interest ID, annotation ID |
| `interestItemIdStr` | `string` | `throughStr` | String through entity: image signature (hex), base64 embedding, interest display name |
| `throughProperties` | `map<ThroughObjectType, list<ThroughObject>>` | N/A (internal) | Structured version of the same info, used for **denylist filtering** (hide/report propagation) |

`interestItemId` and `interestItemIdStr` are NOT mutually exclusive — a single candidate can have both set (e.g., IPFY sets pin ID as `interestItemId` and image sig as `interestItemIdStr`). Which one is populated depends on whether the seed entity is inherently numeric or string-based.

### How They Flow to FVL

1. **At retrieval time**: each converter/generator sets `interestItemId`, `interestItemIdStr`, and `throughProperties` on the `Reason` object
2. **At L2 scoring**: `ScorpionPinnabilityLogger` uses `interestItemIdStr` as the `DataPointer` ID for `THROUGH_ENTITY_FEATURES` — this is how the through entity's features (e.g., pin perf of the seed pin) get joined into the pinnability model input
3. **At impression logging**: `interestItemId` → FVL `throughId`, `interestItemIdStr` → FVL `throughStr`
4. **At denylist filtering**: `throughProperties` is used by `FilterUtils.getPossibleThroughObjectStrings()` and `ThroughObjectDenylistProperties` to propagate hide/report actions — if a user hides a pin, the through entity's other recommendations can also be suppressed

### Relationship Between the Three Fields

From `FilterUtils.getPossibleThroughObjectStrings()` (`FilterUtils.java:59-72`):

```java
public static List<String> getPossibleThroughObjectStrings(InternalPinResult pin) {
    List<String> throughStrings = new ArrayList<>();
    if (shouldGetThroughObjectId(pin)) {
      Reason fantasioReason = pin.getPinResult().getDetails().getFantasioReason();
      if (fantasioReason.isSetInterestItemId() && fantasioReason.getInterestItemId() > 0) {
        throughStrings.add(String.valueOf(fantasioReason.getInterestItemId()));
      }
      if (fantasioReason.isSetInterestItemIdStr()
          && !Strings.isNullOrEmpty(fantasioReason.getInterestItemIdStr())) {
        throughStrings.add(fantasioReason.getInterestItemIdStr());
      }
    }
    return throughStrings;
}
```

Both `interestItemId` (converted to string) and `interestItemIdStr` are extracted as possible through strings. The `throughProperties` map contains the same information in typed/structured form — its `ThroughObject` entries have either `throughObjectId` (Long) or `throughObjectStr` (String) matching the corresponding `interestItemId`/`interestItemIdStr` values.

For full funnel logging, either `interestItemId`/`interestItemIdStr` or `throughProperties` can be used — they carry the same entity identity. A quick stats comparison can confirm parity.

---

## Through Entity by CG/RTC — Detailed Table

### Pixie P2P CGs

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| IPFY | 36 | Query pin ID (Long) | Query image sig (hex) | `{PIN_ID: pinId, IMAGE_SIGNATURE: sig}` | throughId = pin ID |
| Offsite IPFY | 224 | Query pin ID (Long) | Query image sig (hex) | `{PIN_ID: pinId, IMAGE_SIGNATURE: sig}` | throughId = pin ID |

**Code path**: `XPixieHomefeedNodeUtils.createReason()` at `XPixieHomefeedNodeUtils.java:102-143`

```java
private static Reason createReason(long queryPinId, String queryImageSig, ...) {
    Reason reason = new Reason();
    Map<ThroughObjectType, List<ThroughObject>> throughProperties = new HashMap<>();

    if (queryPinId <= 0L) {
      // Invalid pin — set padding ID (999999) that gets filtered by denylist
      final long interestItemId = CandidateGeneratorUtils.padIntAsValidObjectTypeId(999999);
      reason.setInterestItemId(interestItemId);
      throughProperties.put(ThroughObjectType.PIN_ID,
          Arrays.asList(new ThroughObject().setThroughObjectId(interestItemId)));
    } else {
      reason.setInterestItemId(queryPinId);                          // ← throughId = seed pin ID
      throughProperties.put(ThroughObjectType.PIN_ID,
          Arrays.asList(new ThroughObject().setThroughObjectId(queryPinId)));
    }

    if (!Strings.isNullOrEmpty(queryImageSig)) {
      reason.setInterestItemIdStr(queryImageSig);                    // ← throughStr = seed image sig
      throughProperties.put(ThroughObjectType.IMAGE_SIGNATURE,
          Arrays.asList(new ThroughObject().setThroughObjectStr(queryImageSig)));
    }

    reason.setThroughProperties(throughProperties);
    return reason;
}
```

**What `queryPinId` and `queryImageSig` are**: The PinnerSage V2 user profile is decomposed into engagement signals, and each recently-engaged pin becomes a query. `queryPinId` is that seed pin's ID, `queryImageSig` is its image signature. Pixie does a random walk on the pin-pin graph starting from that seed.

---

### Offsite Search NavBoost (RTC 223)

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| Offsite Search NB | 223 | Not set | **The actual search query string** (e.g. "living room decor ideas") | `{SEARCH_QUERY: queryStr}` | **Yes** — human-readable search query |

**Code path**: `HomefeedGssQueryJoinMultiConverterNode.java:102-111`

```java
new Reason()
    .setInterestItemIdStr(query)                         // ← throughStr = the search query text
    .setThroughProperties(
        ImmutableMap.of(
            ThroughObjectType.SEARCH_QUERY,              // ← SEARCH_QUERY, not IMAGE_SIGNATURE
            ImmutableList.of(
                new ThroughObject().setThroughObjectStr(query))))
    .setReasonToChoose(ReasonToChoose.USER_OFFSITE_SEARCH_QUERIES)
```

**How this CG works**: Unlike the other Pixie P2P CGs, Offsite Search NB does NOT use pin-based Pixie retrieval. Instead:

1. The user's offsite search queries are extracted from UFR tensor features (`OFFSITE_SEARCH_QUERY_FEATURE_KEY`) in `SearchNavboostGeneratorsUtils.getOffsiteQueriesFromResource()` (line 586-630)
2. Queries go through denylist filtering against `ThroughObjectType.SEARCH_QUERY` entries (line 651-668)
3. Queries are sent to a Galaxy GSS QueryJoin service which returns NavBoost-style pin candidates
4. `HomefeedGssQueryJoinMultiConverterNode` wraps results into FeedObjects with the search query as the through entity

**What `query` is**: A literal search query string the user performed offsite (outside Pinterest) — e.g., "living room decor ideas", "wedding bouquet". This is the only CG where `throughStr` is a human-readable natural language string rather than a hex signature or encoded blob.

**Denylist**: Uses `ThroughObjectType.SEARCH_QUERY` (not `IMAGE_SIGNATURE` or `PIN_ID`), so hide/report actions propagate at the query level — hiding a pin from a query suppresses other pins from that same query.

---

### Pixie P2B → Polaris CGs

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| Repin Board | 1 | Not set | Image sig from PFY response | `{IMAGE_SIGNATURE: sig}` | No — hex sig |
| User Activity | 4 | Not set | Image sig from PFY response | `{IMAGE_SIGNATURE: sig}` | No — hex sig |
| Clickthrough | 9 | Not set | Image sig from PFY response | `{IMAGE_SIGNATURE: sig}` | No — hex sig |
| Fresh Repin Board | 47 | Not set | Image sig from PFY response | `{IMAGE_SIGNATURE: sig}` | No — hex sig |
| Fresh User Activity | 49 | Not set | Image sig from PFY response | `{IMAGE_SIGNATURE: sig}` | No — hex sig |
| Fresh Clickthrough | 48 | Not set | Image sig from PFY response | `{IMAGE_SIGNATURE: sig}` | No — hex sig |

**Code path**: `UserEmbeddingsToPinsPfyBuilderUtils.java:1028-1046`

```java
final Reason reason = new Reason().setReasonToChoose(reasonToChoose);
final Map<ThroughObjectType, List<ThroughObject>> throughProperties = new HashMap<>();

if (responseObject.isSetThroughObjectIdString()) {
  final String throughStr = responseObject.getThroughObjectIdString();
  reason.setInterestItemIdStr(throughStr);                           // ← throughStr = image sig
  throughProperties.put(ThroughObjectType.IMAGE_SIGNATURE,
      Arrays.asList(new ThroughObject().setThroughObjectStr(throughStr)));
}

if (!throughProperties.isEmpty()) {
  reason.setThroughProperties(throughProperties);
}
```

**What `throughObjectIdString` is**: The PFY builder sends engagement clusters (Through Rewards) to Pixie P2B, which walks the pin-to-board graph. Polaris then converts boards to pins. The `throughObjectIdString` in the response is the **image signature of the pin that seeded the engagement cluster** — e.g., the pin the user repinned (for Repin Board) or clicked (for Clickthrough).

**Note**: `interestItemId` is NOT set for these CGs — only `interestItemIdStr`. This means FVL `throughId` will be null; only `throughStr` carries provenance.

---

### CLR Variants — Multi-Conditional Path (Pin CLR, Board CLR, UIC CLR, Pred UIC, Multi-Emb)

These CGs go through `HomefeedMultiConditionalEmbeddingRetrievalManasConverterNode`, which calls `MuseUtilsCommon.createFeedObjectFromMuseDoc()`.

**Code path**: `MuseUtilsCommon.java:176-206` (the critical branch at lines 181-187)

```java
public static FeedObject createFeedObjectFromMuseDoc(
    GenericSearchDoc doc, ReasonToChoose reasonToChoose, String interestId) {

  Reason reason = new Reason().setReasonToChoose(reasonToChoose);
  if (interestId != null) {
    if (reasonToChoose.equals(ReasonToChoose.PINNABILITY_CONDITIONAL_PIN_EMBEDDINGS)      // Pin CLR
        || reasonToChoose.equals(ReasonToChoose.PINNABILITY_CONDITIONAL_UIC_PIN_EMBEDDINGS) // UIC CLR
        || reasonToChoose.equals(ReasonToChoose.PINNABILITY_CONDITIONAL_PRED_UIC_EMBEDDINGS)) { // Pred UIC
      reason.setInterestItemIdStr(interestId);       // ← throughStr = condition key (image sig)
    } else {
      reason.setInterestItemId(Long.parseLong(interestId));  // ← throughId = condition key (numeric)
    }
  }

  // If perDocData has a top_annotation column, also set annotation ID
  if (doc.isSetPerDocData() && ...) {
    for (PerDocField f : docFields) {
      if (f.fieldName.equals(TOP_ANNOTATION_COLUMN)) {
        long annotationId = Long.parseLong(...);
        reason.setInterestItemId(annotationId);              // ← throughId = annotation ID (overrides)
        reason.setThroughProperties(ImmutableMap.of(
            ThroughObjectType.ANNOTATION_ID,
            ImmutableList.of(new ThroughObject().setThroughObjectId(annotationId))));
      }
    }
  }
  ...
}
```

The `interestId` parameter is the **condition key** from the multi-conditional ANN request — each condition retrieves candidates from a different part of the embedding space.

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | What the condition key IS | Human-readable? |
|---|---|---|---|---|---|
| Pin CLR | 232 | Annotation ID (Long, from perDocData) | **Image sig of seed pin** (the condition) | Image signature of user's recently-engaged pin | No — hex sig |
| UIC CLR | 237 | Annotation ID (Long, from perDocData) | **Image sig of UIC medioid** (the condition) | Image signature of the user interest cluster centroid | No — hex sig |
| Pred UIC CLR | 238 | Annotation ID (Long, from perDocData) | **Image sig of predicted UIC medioid** | Image signature of a predicted interest cluster centroid | No — hex sig |
| Board CLR | 220 | **Condition key parsed as Long** (board-related ID) | Not set | Board embedding condition key (numeric) | throughId = numeric ID |
| Multi-Emb | 210 | **Annotation ID** (Long, from condition key or perDocData) | Not set | Annotation/interest condition key (numeric) | throughId = annotation ID |

**Why Board CLR and Multi-Emb don't get `throughStr`**: The branch at `MuseUtilsCommon:181-183` only routes to `setInterestItemIdStr` for three specific RTCs (`PINNABILITY_CONDITIONAL_PIN_EMBEDDINGS`, `PINNABILITY_CONDITIONAL_UIC_PIN_EMBEDDINGS`, `PINNABILITY_CONDITIONAL_PRED_UIC_EMBEDDINGS`). Board CLR (`PINNABILITY_CONDITIONAL_BOARD_EMBEDDINGS`) and Multi-Emb (`PINNABILITY_MULTI_EMBEDDINGS`) fall to the `else` branch: `setInterestItemId(Long.parseLong(interestId))`. This works because their condition keys are numeric (board IDs, annotation IDs).

**Caller**: `HomefeedMultiConditionalEmbeddingRetrievalManasConverterNode.java:204-205`:
```java
FeedObject feedObject =
    MuseUtilsCommon.createFeedObjectFromMuseDoc(doc, reasonToChoose, key);
```
Where `key` is the condition key from the multi-conditional Manas response map.

---

### Interest CLR Path (Rec Topics, PinnerSpark, Followed Interest, Offsite Interest)

These are Interest-based conditions routed through the CLR conditional retrieval system.

**Code path**: `HomefeedConditionalRetrievalManasConverterNode.java:325-467`

```java
for (String key : multiResponse.keySet()) {
  Long pinInterestId = Long.valueOf(key);        // ← condition key is an interest ID
  String throughStr = "";

  // Determine RTC based on which interest list this ID belongs to
  if (seeMoreExp && seeMoreInterests.contains(pinInterestId)) {
    reasonToChoose = ReasonToChoose.FOLLOWED_INTEREST;
    throughStr = translatedSeeMoreInterestsWithSigs.getOrDefault(pinInterestId, "see_more");
  } else if (followedInterests.contains(pinInterestId)) {
    reasonToChoose = ReasonToChoose.FOLLOWED_INTEREST;
  } else if (recommendedTopics.contains(pinInterestId)) {
    reasonToChoose = ReasonToChoose.RECOMMENDED_TOPICS;
  } else if (pinnerSparkInterests.contains(pinInterestId)) {
    reasonToChoose = ReasonToChoose.PINNERSPARK_INTEREST;
  } else if (offsiteInterests.contains(pinInterestId)) {
    reasonToChoose = ReasonToChoose.OFFSITE_INTEREST;
  } else {
    reasonToChoose = ReasonToChoose.RECOMMENDED_TOPICS;  // fallback
  }

  Reason reason = new Reason()
      .setInterestItemId(pinInterestId)                  // ← throughId = interest ID
      .setReasonToChoose(reasonToChoose);

  if (seeMoreExp && !Strings.isNullOrEmpty(throughStr)) {
    reason.setInterestItemIdStr(throughStr);              // ← throughStr = image sig (see_more only)
  }

  // Explore page experiment: overwrite throughStr with human-readable interest name
  if (HomefeedExperimentUtils.isInExplorePageExp(hfpExpPair)) {
    String interestName = translatedInterestTextDisplayName.get(pinInterestId);
    reason.setInterestItemIdStr(interestName);            // ← throughStr = e.g. "DIY Home Decor"
  }
  ...
}
```

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | Human-readable? |
|---|---|---|---|---|
| Rec Topics (via Interest CLR) | 65 | Interest ID (Long) | Conditionally: interest display name (explore exp) or image sig (see_more exp) or not set | throughId = interest ID; throughStr = human name when explore exp is on |
| PinnerSpark (via Interest CLR) | 231 | Interest ID (Long) | Same conditional logic | Same |
| Followed Interest | (varies) | Interest ID (Long) | Image sig (see_more exp) or interest name (explore exp) or not set | Same |
| Offsite Interest | 234 | Interest ID (Long) | Same conditional logic | Same |

**Note**: `throughProperties` is NOT explicitly set in this converter — only `interestItemId` and conditionally `interestItemIdStr`.

---

### Learned Embedding Retrieval CGs (RecGPT, Low-Signal, PLP, Shopping Embeddings)

These CGs go through `HomefeedEmbeddingRetrievalManasConverterNode`.

**Code path**: `HomefeedEmbeddingRetrievalManasConverterNode.java:80-158`

Two-step process:

**Step 1** — `MuseUtilsCommon.createFeedObjectFromMuseDoc(result, reasonToChoose, null)` (line 113)
- Called with `null` interestId → **neither `interestItemId` nor `interestItemIdStr` is set** from this call

**Step 2** — Conditionally, `setLearnedRetrievalThroughStr()` (line 122), gated by `LOG_EMBEDDING_DECIDER`:

```java
private static void setLearnedRetrievalThroughStr(
    ModelId modelId, EmbeddingVector vector, Double score, FeedObject obj) {
  ...
  Reason reason = obj.getObjectDetails().getPinDetails().getFantasioReason();
  // Through string format:
  // <model_id>:<model_version>:<emb_entry1>,<emb_entry2>,...,<emb_entryN>:<score>
  // E.g., 523469eb_074b_48a0_8612_5d01d073aa12:1:0.333,0.222,0.111,...,0.999:0.8
  StringBuilder throughStr =
      new StringBuilder(modelId.getModelName() + ":" + modelId.getMlflowModelVersion() + ":");
  float[] embeddingArray = Utils.convertByteArrayToFloatArray(vector.getBinaryValues());
  for (int idx = 0; idx + 1 < embeddingArray.length; idx += 1) {
    throughStr.append(embeddingArray[idx]).append(",");
  }
  throughStr.append(embeddingArray[embeddingArray.length - 1]).append(":").append(score);
  byte[] compressed = Base64.getEncoder().encode(throughStr.toString().getBytes());
  reason.setInterestItemIdStr(new String(compressed));   // ← throughStr = base64(model:ver:emb:score)
}
```

This is only called when `converterType == MUSE_EMBEDDING_TO_WEB_PINS` AND the user is in the `LOG_EMBEDDING_DECIDER`. Otherwise, these CGs have **no through entity at all**.

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| RecGPT | 206 | Not set | Base64 of `modelId:ver:emb1,emb2,...:score` (decider-gated) | Not set | No — opaque base64 blob |
| Low-Signal User Emb | 229 | Not set | Base64 (same, decider-gated) | Not set | No |
| PLP Embeddings | 218 | Not set | Base64 (same, decider-gated) | Not set | No |
| Product Pin Emb | 195 | Not set | Base64 (same, decider-gated) | Not set | No |
| TML Product Pin Emb | 213 | Not set | Base64 (same, decider-gated) | Not set | No |
| Fresh Product Pin Emb | 209 | Not set | Base64 (same, decider-gated) | Not set | No |

**Callers**:
- `MuseEmbeddingToWebPinsUtils.java:359-390` — wires up `HomefeedEmbeddingRetrievalManasConverterNode` for RecGPT, Low-Signal, PLP, and shopping embedding CGs
- `MuseEmbeddingToCreatorStoryPinsUtils.java:374-402` — same converter for creator story pins

**Key caveat**: If the `LOG_EMBEDDING_DECIDER` is off, these CGs have NO `throughId` and NO `throughStr` in FVL. This is a logging gap worth confirming.

---

### KV Store / Recboost CGs (NavBoost PFY, Recboost Shopping, Organic Coengagement)

All three share the same code path through `RecboostCandidateGeneratorUtils`.

**Important**: NavBoost PFY is a Recboost variant — `MagicBoxConstants.java:201` maps `RECBOOST_MODEL_IDENTIFIER` → `ReasonToChoose.NAVBOOST_PFY`. The `P2PNavboostManasConverterNode` only converts raw Manas responses to `ResultActivity` objects; actual FeedObject construction (including through fields) happens in the Recboost utils.

**Code path**: `RecboostCandidateGeneratorUtils.java:326-345`

```java
private static FeedObject constructFeedObject(
    RecboostObject recboostObject,
    String source,                              // ← this is keyImg (query image sig from KV lookup)
    RecommendationSourceDetails srcDetails,
    String modelIdentifier) {
  long objectId = recboostObject.getObjectId();
  RecommendationSource recSource = srcDetails.getRecSource();
  Reason reason =
      new Reason()
          .setInterestItemIdStr(source)          // ← throughStr = query image sig
          .setReasonToChoose(RECBOOST_IDENTIFIER_TO_RTC_MAP.get(modelIdentifier))
          .setThroughProperties(getThroughProperties(srcDetails));
  if (RecommendationSource.PIN_SEE_MORE.equals(recSource)) {
    reason.setInterestItemId(                    // ← throughId only for PIN_SEE_MORE
        CandidateGeneratorUtils.padIntAsValidObjectTypeId(
            RecommendationSource.PIN_SEE_MORE.getValue()));
  }
  ...
}
```

**`getThroughProperties()`** at `RecboostCandidateGeneratorUtils.java:796-812`:

```java
private static Map<ThroughObjectType, List<ThroughObject>> getThroughProperties(
    RecommendationSourceDetails srcDetails) {
  Map<ThroughObjectType, List<ThroughObject>> throughProperties = Maps.newHashMap();
  if (!Strings.isNullOrEmpty(srcDetails.getQueryNeardupSignature())) {
    throughProperties.put(ThroughObjectType.NEARDUP_SIGNATURE,
        Arrays.asList(new ThroughObject().setThroughObjectStr(srcDetails.getQueryNeardupSignature())));
  }
  if (!Strings.isNullOrEmpty(srcDetails.getQuerySignature())) {
    throughProperties.put(ThroughObjectType.IMAGE_SIGNATURE,
        Arrays.asList(new ThroughObject().setThroughObjectStr(srcDetails.getQuerySignature())));
  }
  return throughProperties;
}
```

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| NavBoost PFY | 89 | Not set (unless PIN_SEE_MORE) | Query image sig (`keyImg` from KV lookup) | `{NEARDUP_SIGNATURE: neardupSig, IMAGE_SIGNATURE: querySig}` | No — hex sig |
| Recboost Shopping | 214 | Not set (unless PIN_SEE_MORE) | Query image sig (`keyImg`) | Same | No — hex sig |
| Organic Coengagement | 211 | Not set (unless PIN_SEE_MORE) | Query image sig (`keyImg`) | Same | No — hex sig |

**Caller**: `RecboostCandidateGeneratorUtils.java:234-235`:
```java
FeedObject feedObject = constructFeedObject(recboostObject, keyImg, srcDetails, modelIdentifier);
```
Where `keyImg` is the image signature key from the Recboost KV store response — i.e., the image signature of the pin the user previously engaged with.

---

### Following Feed

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| Following Feed | 19 | Board ID (Long) | Not set | `{BOARD_ID: boardId}` | throughId = board ID |

**Code path**: `HomefeedApiaryManasResponseConverterNode.java:137-144`

```java
Reason reason =
    new Reason()
        .setReasonToChoose(ReasonToChoose.FOLLOWING_FEED)
        .setInterestItemId(boardId)                      // ← throughId = board ID
        .setThroughProperties(
            ImmutableMap.of(
                ThroughObjectType.BOARD_ID,
                ImmutableList.of(new ThroughObject().setThroughObjectId(boardId))));
```

**What `boardId` is**: The board from which the followed creator's pin was fetched.

---

### Graphsage Product

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| Graphsage Product | 97 | Not set | Image sig from response (`throughObjectIdString`) | `{IMAGE_SIGNATURE: sig}` | No — hex sig |

**Code path**: `HomefeedGraphSageP2PUnityResponseConverterNode.java:104`

This CG uses the GraphSage pin-to-product retrieval. The through string is the image signature of the seed pin used in the P2P graph walk.

---

### Landing Page CGs

| CG | RTC | `interestItemId` (throughId) | `interestItemIdStr` (throughStr) | `throughProperties` | Human-readable? |
|---|---|---|---|---|---|
| Landing Page Pins | 18 | Interest ID (Long) | Interest ID as string, or concat of up to 3 matched interest IDs | `{INTEREST_ID: interestId}` | throughId = interest ID; throughStr = comma-separated interest IDs |
| Landing Page Recs | 188 | Interest ID (Long) | Same | `{INTEREST_ID}` | Same |

**Code path**: `HomefeedTapestryGetPinsResponseConverterNode.java:305-330`

```java
Reason reason = new Reason().setInterestItemId(pinInterestId).setReasonToChoose(rtc);
if (rtc == ReasonToChoose.FOLLOWED_INTEREST) {
  reason.setInterestItemIdStr(pinInterestId.toString());
}

// If matched interests exist, overwrite throughStr with concat of up to 3 interest IDs
if (pin.isSetInterestIds() && !pin.getInterestIds().isEmpty()) {
  List<Long> matchedInterestIds = pin.getInterestIds();
  String concatInterestIdsStr =
      matchedInterestIds.subList(0, Math.min(3, matchedInterestIds.size()))
          .toString().replace("[", "").replace("]", "");
  reason.setInterestItemIdStr(concatInterestIdsStr);     // ← e.g. "12345, 67890, 11111"
}

throughProperties.put(ThroughObjectType.INTEREST_ID,
    ImmutableList.of(new ThroughObject().setThroughObjectId(pinInterestId)));
reason.setThroughProperties(throughProperties);
```

---

## Summary by Pattern

| Pattern | CGs (RTCs) | `throughId` | `throughStr` | `throughProperties` |
|---|---|---|---|---|
| **Pin-seeded (Pixie P2P)** | IPFY (36), Offsite IPFY (224) | Seed pin ID | Seed image sig (hex) | PIN_ID + IMAGE_SIGNATURE |
| **Search-query-seeded** | Offsite Search NB (223) | Not set | **Search query text** (human-readable) | SEARCH_QUERY |
| **Engagement-seeded (P2B → Polaris)** | Repin Board (1), User Activity (4), Clickthrough (9), Fresh variants (47, 49, 48) | Not set | Seed image sig (hex) | IMAGE_SIGNATURE |
| **CLR condition = image sig** | Pin CLR (232), UIC CLR (237), Pred UIC CLR (238) | Annotation ID | Image sig of condition pin/medioid | ANNOTATION_ID |
| **CLR condition = numeric** | Board CLR (220), Multi-Emb (210) | Condition key or annotation ID | Not set | ANNOTATION_ID |
| **Interest CLR** | Rec Topics (65), PinnerSpark (231), Offsite Interest (234) | Interest ID | Experiment-gated: interest name or image sig or not set | Not explicitly set |
| **Learned embedding** | RecGPT (206), Low-Signal (229), PLP (218), Product (195), TML (213), Fresh Product (209) | Not set | Base64 of `model:ver:embedding:score` (decider-gated) | Not set |
| **KV Store (Recboost)** | NavBoost PFY (89), Recboost Shopping (214), Organic Coengagement (211) | Not set (usually) | Query image sig from KV lookup | NEARDUP_SIGNATURE + IMAGE_SIGNATURE |
| **Board-seeded** | Following Feed (19) | Board ID | Not set | BOARD_ID |
| **P2P graph walk** | Graphsage Product (97) | Not set | Image sig from response | IMAGE_SIGNATURE |
| **Interest-seeded (Tapestry)** | Landing Page Pins (18), Landing Page Recs (188) | Interest ID | Concat interest IDs (comma-separated) | INTEREST_ID |

---

## Logging Implications for Full Funnel Log

### Which field to log?

For the full funnel log (Stage 4: AFTER_CANDIDATE_GENERATION), the FULL_FUNNEL_LOGGING.md doc lists `interestItemIdStr` as the primary through entity field. However:

1. **Some CGs only set `interestItemId` (not `interestItemIdStr`)**: Board CLR (220), Multi-Emb (210), Following Feed (19), legacy INTEREST.prod (231 via Interest Manas redesign)
2. **Some CGs only set `interestItemIdStr` (not `interestItemId`)**: Pixie P2B/Polaris (1, 4, 9, 47, 49, 48), Recboost variants (89, 214, 211), Graphsage (97)
3. **Some CGs set both**: Pixie P2P (36, 224), Pin CLR (232), UIC CLR (237), Pred UIC CLR (238), Landing Page (18, 188), Interest CLR (65, 231) when experiment is active
4. **Some CGs set neither** (decider-gated): RecGPT (206), Low-Signal (229), PLP (218), shopping embedding CGs — when `LOG_EMBEDDING_DECIDER` is off

**Recommendation**: Log BOTH `interestItemId` and `interestItemIdStr` to capture all CGs. Additionally log `throughProperties` if structured provenance is needed for downstream analysis.

### Decider gap for embedding CGs

The `LOG_EMBEDDING_DECIDER` gates whether RecGPT, PLP, Low-Signal, and shopping embedding CGs get any throughStr at all. If this decider is off (or covers only a fraction of traffic), these CGs will have empty through fields in FVL. Worth confirming the decider's current rollout percentage.

---

## Source File Index

| File | What it handles |
|---|---|
| `XPixieHomefeedNodeUtils.java:102-143` | IPFY, Offsite IPFY, Offsite Search NB (Pixie P2P) |
| `UserEmbeddingsToPinsPfyBuilderUtils.java:1028-1046` | Repin Board, User Activity, Clickthrough, Fresh variants (P2B → Polaris) |
| `MuseUtilsCommon.java:176-258` | Pin CLR, Board CLR, UIC CLR, Pred UIC CLR, Multi-Emb (via createFeedObjectFromMuseDoc) |
| `HomefeedConditionalRetrievalManasConverterNode.java:325-467` | Rec Topics, PinnerSpark, Followed Interest, Offsite Interest (Interest CLR) |
| `HomefeedEmbeddingRetrievalManasConverterNode.java:80-158` | RecGPT, Low-Signal, PLP, shopping embeddings (learned retrieval) |
| `RecboostCandidateGeneratorUtils.java:326-345, 796-812` | NavBoost PFY, Recboost Shopping, Organic Coengagement (KV store) |
| `HomefeedApiaryManasResponseConverterNode.java:137-144` | Following Feed |
| `HomefeedGssQueryJoinMultiConverterNode.java:102-111` | Offsite Search NB — FeedObject construction with search query as throughStr |
| `SearchNavboostGeneratorsUtils.java:586-668` | Offsite Search NB — query extraction from UFR + denylist filtering |
| `HomefeedGraphSageP2PUnityResponseConverterNode.java:104` | Graphsage Product |
| `HomefeedTapestryGetPinsResponseConverterNode.java:305-330` | Landing Page Pins, Landing Page Recs |
| `HomefeedInterestManasRedesignConverterNode.java:85` | Legacy INTEREST.prod (Interest Manas redesign) |
| `MagicBoxConstants.java:196-206` | RTC-to-model-identifier mapping (confirms NavBoost PFY = Recboost) |
| `FilterUtils.java:59-92` | Through string extraction for denylist filtering |
| `ScorpionPinnabilityLogger.java:524-544` | Through entity → pinnability model feature pointer |
