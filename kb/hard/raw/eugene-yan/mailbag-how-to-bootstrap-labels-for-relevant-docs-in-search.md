# Mailbag: How to Bootstrap Labels for Relevant Docs in Search

**Source:** https://eugeneyan.com//writing/mailbag-bootstrap-relevant-docs/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

A writes:

> Recently I’m trying to build a semantic search system with my own data and I came across your [blog post](/writing/search-query-matching/). I found quite a few papers using “Recall@K” as an evaluation metric (e.g. Semantic Product Search by Amazon, Embedding-based Retrieval in Facebook Search by Facebook, Embedding-based Product Retrieval in Taobao Search), but it is unclear how they obtain the total number of relevant documents (or items) for their query-document pairs.
>
> While it is totally possible to hire a lot of annotators to figure out which documents are relevant to a search query, I don’t think that is economically feasible at all. Do you have any idea how engineers in industry figure out the total number of relevant documents (or items) for their query-document pairs? Many thanks!

If I had to build a search engine from scratch, I would:

* Start with lexical matching such [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) or what’s available in Elasticsearch or Solr
* Deploy this in production and collect data on what users click on (i.e., labels)
* Then, use these labels for semantic search

I think using human annotators can work, but probably only for defects or edge cases, given how costly it is.

---

Have a question for me? Happy to answer concise questions via email on topics I know about.
More details in [How I Can Help](/how-i-can-help/).

  
Share on:
