# Migrating Site Comments to Utterances

**Source:** https://eugeneyan.com//writing/migrating-to-utterances/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

Today I learnt how to migrate comments on this site to [Utterances](https://utteranc.es/). The comments functionality on this site has migrated from Discus to Commento and most recently, utterances. You can see the history in the comments [here](/writing/first-post/).

Here are the steps I took:

* Create a [repo](https://github.com/eugeneyan/eugeneyan-comments) just for comments.
* Set up [utteranc.es](https://utteranc.es) with the repo.
* Add the `html` below to my layout template.

```
<script src="https://utteranc.es/client.js"
        repo="eugeneyan/eugeneyan-comments"
        issue-term="url"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
```

* Download site comments from Commento. The download is in `json` format.
* Figure out the [GitHub API for importing issues](https://gist.github.com/jonmagic/5282384165e0f86ef105); expected payload below.

```
{
  "issue": {
    "title": "Imported from some other system",
    "body": "..."
  },
  "comments": [
    {
      "body": "comment",
      "create_at": "timestamp"
    }
  ]
}
```

* Read the `json` comments, clean them up, and upload via the GitHub API ([code](https://github.com/eugeneyan/json-to-utterances/blob/master/json-to-utterances.ipynb)).

Now all comments are GitHub [issues](https://github.com/eugeneyan/eugeneyan-comments/issues). Here’s an example of how it looks like in a [post](/writing/end-to-end-data-science/). One downside is that readers will need to login via GitHub to be able to comment; hope this isn’t too big of a barrier.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Sep 2020). Migrating Site Comments to Utterances. eugeneyan.com.
> https://eugeneyan.com/writing/migrating-to-utterances/.

or

```
@article{yan2020utterance,
  title   = {Migrating Site Comments to Utterances},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Sep},
  url     = {https://eugeneyan.com/writing/migrating-to-utterances/}
}
```

  
Share on:
