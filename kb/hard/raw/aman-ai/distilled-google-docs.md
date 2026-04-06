# Distilled • Google Docs

**Source:** https://aman.ai/sysdes/google-docs/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** system-design

---

* [Design](#design)
* [Further Reading](#further-reading)

## Design

1. Clients send document editing operations to the WebSocket Server.
2. The real-time communication is handled by the WebSocket Server.
3. Documents operations are persisted in the Message Queue.
4. The File Operation Server consumes operations produced by clients and generates transformed operations using collaboration algorithms.
5. Three types of data are stored: file metadata, file content, and operations.

* One of the biggest challenges is real-time conflict resolution. Common algorithms include:

  + Operational transformation (OT)
  + Differential Synchronization (DS)
  + Conflict-free replicated data type (CRDT)
* Google Doc uses OT according to its Wikipedia page and CRDT is an active area of research for real-time concurrent editing.

## Further Reading

* [Powered by AI: Instagram’s Explore recommender system](https://ai.facebook.com/blog/powered-by-ai-instagrams-explore-recommender-system/).
* [How to design Google Docs (Episode 4)](https://blog.bytebytego.com/p/how-to-design-google-docs-episode?s=r)
