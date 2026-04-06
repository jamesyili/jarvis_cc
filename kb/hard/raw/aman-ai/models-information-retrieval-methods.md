# Models • Information Retrieval Methods

**Source:** https://aman.ai/primers/ai/info-retrieval-methods/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals, retrieval, evaluation

---

* [TF-IDF](#tf-idf)
* [TF-IDF vs. BM25](#tf-idf-vs-bm25)

## TF-IDF

* TF (Term Frequency) helps capture the importance of a term within a specific document. It indicates how frequently a term appears in the document’s content and helps identify the prominent themes or topics within the description. High TF values for certain terms suggest their significance in describing the document.
* However, TF alone may not be sufficient to differentiate between common terms and those that are truly informative or distinctive. This is where IDF (Inverse Document Frequency) comes into play. IDF measures the **rarity or uniqueness** of a term across the entire corpus. It helps identify terms that are less common across documents but hold more discriminative power.
* By combining TF and IDF through the TF-IDF approach, the resulting scores reflect both the local importance of terms within a document’s description (TF) and the global distinctiveness of those terms across the document collection (IDF). This allows the recommendation system to highlight terms that are both prominent within a document and unique compared to other documents, enabling more accurate content-based filtering.

## TF-IDF vs. BM25

* While both BM25 and TF-IDF are term weighting schemes used in information retrieval and text mining, they have some fundamental differences in how they calculate the importance or relevance of terms in a document.
  + **Calculation:**
    - TF-IDF (Term Frequency-Inverse Document Frequency) calculates the weight of a term based on its frequency within a document (TF) and its rarity across the entire document collection (IDF).
    - BM25 (Best Match 25) also takes into account the term frequency within a document but uses a more sophisticated scoring function that considers factors like document length, average document length, and term frequency in the entire collection.
  + **Document Length:**
    - TF-IDF treats all documents as having equal length and does not explicitly account for differences in document length.
    - BM25 incorporates the document length by penalizing the weight of terms based on the document length. Longer documents tend to have higher term frequencies, so BM25 compensates for this effect.
  + **Term Frequency Saturation:**
    - TF-IDF can suffer from term frequency saturation, where the importance of a term plateaus after a certain frequency threshold.
    - BM25 addresses this issue by using a term frequency saturation function that prevents excessive term weight for high frequencies.
