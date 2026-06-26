---
name: send-me-html-default
description: /send-me defaults to HTML-rendered body + .html attachment. Raw markdown is opt-in only.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6d10c65e-48cc-44a1-b554-02c45a633d95
---

When using `/send-me`, render `.md` files to HTML via `scripts/md_to_html.py` and ship the rendered HTML as both the email body and the attachment. Do NOT attach the raw `.md`. James should never have to specify "use the html structures" — that's the default. Raw markdown is opt-in only if he explicitly asks.

**Why:** Phone reading is the primary `/send-me` use case. Raw markdown renders as ugly source code on Gmail mobile (per Thariq Shihipar's HTML-vs-Markdown argument, May 2026). HTML rendered with the structured CSS in `md_to_html.py` reads like a real document on phone, which is the whole point.

**How to apply:** Any time `/send-me` is invoked with a `.md` file, render first and send the HTML. Never ask "should I render to HTML?" — just do it. If James wants raw `.md`, he'll say so explicitly.
