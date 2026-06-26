---
name: Multi-page screenshot labeling
description: When the user shares screenshots that contain multiple pages, label captured content by what's actually visible — not by the page-indicator overlay
type: feedback
originSessionId: 8a82b336-94a0-40ca-b514-4a07a67cc9b8
---
When the user shares screenshots of multi-page documents (papers, slides, PDFs), each screenshot may show 2+ pages stacked vertically with the page-indicator overlay (e.g., "X of N") referring to one of the visible pages. Do not assume the indicator labels the entire screenshot.

**How to apply:**

- When extracting content from such screenshots, count the page-headers/footers visible in each image, not just the indicator.
- Label captured sections by the **range of pages they cover** (e.g., "Pages 1–2"), not by a single page number.
- If the user later says "I gave you those pages" and you have content gaps in your notes, the most likely cause is mis-labeling — re-examine the screenshots before asking for missing pages.

**Why:**

In session 2026-04-25b, I labeled extracted paper content as "Page 1, Page 3, Page 6, Page 7, Page 10, Page 11" based on the visible "X of 14" indicator. Each screenshot actually contained two stacked pages (1+2, 3+4, 5+6, 7+8, 9+10, 11+12). I then asked James to share "missing pages 2, 4, 5, 8, 9, 12" — pages he had already provided. He pushed back ("What do you mean pull pages? I gave you those as part of the screenshots"). The correction was simple but the original mislabeling created downstream confusion (editor + writing reviews ran on what I had labeled "pages 1–12" without realizing that was actually all 12 of those pages, not gaps).
