# Mailbag: What's the Architecture for your Blog?

**Source:** https://eugeneyan.com//writing/mailbag-blog-architecture/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

M [writes](https://github.com/eugeneyan/ama/issues/2):

> As someone who wants to get started in writing and technical blogging, I was thinking about a custom app but then got overwhelmed. Your app looks very well put together, and I was wondering what the architecture was and how easy it was to set up. Maybe a blog post about it would be good.

My site doesn’t have much “architecture” per se. It’s just a combination of the following:

* [Jekyll](https://jekyllrb.com) to generate HTML from Markdown (the content is built on this)
* [GitHub Pages](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/setting-up-a-github-pages-site-with-jekyll) for hosting. (Jekyll has built-in support for GH Pages; can be hosted for free on a public repo.)
* HTML for navigation pages/snippets (e.g., homepage, navigation bar)
* CSS for styling
* JavaScript for some extra touchs (e.g., [adding anchor links on headers](https://www.the-art-of-web.com/javascript/remove-anchor-links/))

I don’t use a theme. Nonetheless, there are many free themes to get started on [here](https://jekyllthemes.io/free).

On setting it up, my friend YuXuan wrote about his process here: [Part 1](https://yxtay.github.io/blog/understanding-jekyll-and-github-pages/), [Part 2](https://yxtay.github.io/blog/setting-jekyll-themes-on-github-pages/). I think you’ll find it useful.

---

Have a question for me? Happy to answer concise questions via email on topics I know about.
More details in [How I Can Help](/how-i-can-help/).

  
Share on:
