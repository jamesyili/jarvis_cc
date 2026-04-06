# How to Update a GitHub Profile README Automatically

**Source:** https://eugeneyan.com//writing/how-to-update-github-profile-readme-automatically/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

Today I learnt how to set up my GitHub profile `README` to automatically update with the latest writing from this site. It’s now set to run every day at midnight.

It’s nothing too complex. Simon Willison [shared](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/) how to do this with GitHub Actions and it seemed like a fun afternoon project (and it was). And I thought an hour or two of work would save hours of future manual updates.

## First, Pull From Your Site’s Feed

This site is set up with an [Atom feed](https://eugeneyan.com/feed) that RSS readers (e.g., [Feedly](https://feedly.com)) can aggregate with. Getting the latest writing with Python’s `feedparser` is simple. Based on how your dates are formatted, you might need to update the regular expression.

```
import feedparser

def fetch_writing():
    entries = feedparser.parse('https://eugeneyan.com/feed')['entries'][:5]
    return [
        {
            'title': entry['title'],
            'url': entry['link'].split('#')[0],
            'published': re.findall(r'(.*?)\s00:00', entry['published'])[0]
        }
        for entry in entries
    ]
```

## Next, Update The README Sections

My `README` has a section for “📝 Recent Writing” which I update with the results from `fetch_writing()`. This is done by searching for comment blocks for “writing” (e.g., `<!-- writing starts -->`) and replacing everything between them.

```
import re

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '\n{}\n'.format(chunk)
    chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
    return r.sub(chunk, content)
```

So far, running both methods will update the README file.

## Finally, Set Up GitHub Actions

We’ll want to set up GitHub Actions to run this workflow automatically. Currently, it runs with each push and at midnight daily. There’s also the ability for one-click build (which is pretty cool).

```
name: Build README
on:
  push:
  workflow_dispatch:
  schedule:
    - cron:  '0 0 * * *'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Check out repo
      uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
        architecture: x64
    - name: Install dependencies
      run: python -m pip install -r requirements.txt
    - name: Update README
      run: |-
        python build_readme.py
        cat README.md
    - name: Commit and push if changed
      run: |-
        git diff
        git config --global user.email "[email protected]"
        git config --global user.name "README-bot"
        git add -A
        git commit -m "Updated content" || exit 0
        git push
```

## Chill and Let Automation Take Over

Now that it’s set up, no more manual updating of the `README` with each new post. Here’s how it looks like now, *without* this current post.

My profile now; if it's the same when you visit it, my effort in this post failed.

By the time you visit [my GitHub profile](https://github.com/eugeneyan/), the “📝 Recent Writing” section will be updated to include this post, or (if you’re visiting it more than a month from now) be updated with a new set of recent posts.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jul 2020). How to Update a GitHub Profile README Automatically. eugeneyan.com.
> https://eugeneyan.com/writing/how-to-update-github-profile-readme-automatically/.

or

```
@article{yan2020github,
  title   = {How to Update a GitHub Profile README Automatically},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Jul},
  url     = {https://eugeneyan.com/writing/how-to-update-github-profile-readme-automatically/}
}
```

  
Share on:
