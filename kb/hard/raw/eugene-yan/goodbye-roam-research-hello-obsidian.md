# Goodbye Roam Research, Hello Obsidian

**Source:** https://eugeneyan.com//writing/roam-to-obsidian/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I was bored over the weekend and migrated my notes from Roam Research to Obsidian. It was easier than expected and took under an hour. Here are the steps I took.

First, I selectively followed this [guide](https://notes.nicolevanderhoeven.com/Migrating+from+Roam+to+Obsidian) to download my notes as a zip file (steps 1) and create an Obsidian vault. Then, I [downloaded the images](https://github.com/nicolevanderhoeven/deroamify/blob/main/downloadfirebase.py) in my notes into `/assets` (step 11). A few notes were in folders because they had `/` in the title; I cleaned these up by hand.

As part of format conversion (step 4), I incorrectly enabled “Roam Research tag fixer”. As a result, my `#tag` and `#[[tag]]` were converted to `[[tag]]`. Fortunately, my tags always came after `tags:` and were on the first line of each file. Thus, I wrote some [basic regex](https://gist.github.com/eugeneyan/95d09eaeff0c99d468d8c459cfed5218) to fix it.

Next, I set up [obsidian-git](https://github.com/denolehov/obsidian-git) for syncing across devices. Installation on [Mac](https://github.com/denolehov/obsidian-git/wiki/Installation#plugin-installation) and [mobile](https://github.com/denolehov/obsidian-git/wiki/Installation#mobile) was straightforward. The first sync took seconds and subsequent syncs were under a second.

Syncing images was trickier as git doesn’t do well with large commits. For my 1k+ existing images (mostly screenshots of talks and papers), I [iteratively committed](https://gist.github.com/eugeneyan/c4da21af315b62fc3b88163541c816e3) those that were less than 1,024kb in size. Images greater than 1,024kb were shrunk—by converting image format from `png` to `jpg`—before committed. Syncing the images to GitHub took about 15 minutes. New images will be synced via obsidian-git.

A few community plug-ins I use:

* [obsidian-git](https://github.com/denolehov/obsidian-git): To sync notes across devices via git
* [obsidian-outliner](https://github.com/vslinko/obsidian-outliner): Easier working with bullets
* [obsidian-minimal](https://github.com/kepano/obsidian-minimal) and [obsidian-minimal-settings](https://github.com/kepano/obsidian-minimal-settings): Minimal display theme

Others have also recommended their favorite plug-ins on this [tweet](https://twitter.com/eugeneyan/status/1614847315914936321).

I’m loving Obsidian so far. It feels snappier than web-based Roam during startup and while using it. It’s also more customizable. I don’t foresee it hindering my [Zettelkasten workflow](/writing/note-taking-zettelkasten/). While I have a forever-free Roam graph (I was an early adopter) and there’s no push factor, I’m going to stick with Obsidian for a bit and see how it goes.

Are you an Obsidian user as well? What features or plug-ins do you recommend?

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jan 2023). Goodbye Roam Research, Hello Obsidian. eugeneyan.com.
> https://eugeneyan.com/writing/roam-to-obsidian/.

or

```
@article{yan2023obsidian,
  title   = {Goodbye Roam Research, Hello Obsidian},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2023},
  month   = {Jan},
  url     = {https://eugeneyan.com/writing/roam-to-obsidian/}
}
```

  
Share on:
