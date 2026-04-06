# Internal Resource-System Design

**Source:** https://aman.ai/h/sysDesign/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [Google Search - by Damien Benveniste, PHD](#google-search---by-damien-benveniste-phd)

## Overview

* The content below is a work in progress and is a collection of content from [Damien Benveniste’s linkedIn posts that can be found here](https://www.linkedin.com/in/damienbenveniste/recent-activity/shares/) and [Prithivi Da](https://www.linkedin.com/search/results/content/?fromMember=%5B%22ACoAAANONyEBI75vYtjMK4f9hcDMhgneli34DsA%22%5D&heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAANONyEBI75vYtjMK4f9hcDMhgneli34DsA&keywords=prithivi%20da&origin=FACETED_SEARCH&position=1&searchId=db1fd6da-b7b0-4e5c-ae97-bb8b90a36918&sid=aGE&sortBy=%22date_posted%22).
* Content is also from [Sebastian Raschka](https://www.linkedin.com/feed/update/urn:li:activity:7019488884581384192/)

## Google Search - by Damien Benveniste, PHD

* [link to post](https://www.linkedin.com/posts/damienbenveniste_machinelearning-datascience-systemdesign-activity-7020785986410336256-kKo5/?utm_source=share&utm_medium=member_desktop)

How would you ARCHITECT a search engine like Google Search? That is a very common Machine Learning System Design interview question. There are more than 50B indexed websites and ~40K searches per second. The system needs to be fast, scalable and needs to adapt to the latest news!

When a query is created, it goes through a spell check and it is expanded with additional terms such as synonyms to cover as well as possible the user’s query. We know Google uses RankBrain (https://lnkd.in/g4FvNeAT) and it is used only 10% of the time. It is using a word vector representation to find semantically similar words.

The query is then matched against a database, very likely by keyword matching for very fast retrieval. A large set of documents are then selected. The small subset of those documents is selected using simple (fast) heuristic such as PageRank and other contextual information.

The ranking process happens in stages. The results go through a set of Recommender engines. There is most likely a simple Recommender Engine first ranking a large amount of documents (maybe 100,000 or 10,000 documents) and a complex one refining the ranking of the top ranked documents (maybe 100 or 1000). At this point, there might be tens of thousands of features created from the different entities at play: the user, the pages, the query, and the context. Google captures the user history, the pages interaction with other users, the pages natural language semantic, the query semantic, … The context relates to the time of the day, day of the week, … but also the current news of the day.

We will most likely need different model types for different languages, regions, platforms (website, mobile apps, …), document types, … There might be models that specialize in the pure search but I expect there are models that specialize in further filtering such as age appropriate websites or websites containing hate speech.

A typical server can handle 10,000 HTTP requests per second, but the limiting latency factor is mostly coming from the machine learning models. For example, if ranking 10,000 documents takes ~200 ms, that means we need ~8000 ML servers up at all times to handle the 40K/s requests.

Because Google is a search engine for multiple types of documents, we have a Universal Search Aggregation system to merge the search results. After the user is served with the results, we can use the user engagement to assess the models in online experiments and aggregate the training data for following model developments and recurrent training processes.

I guess we could use a tool like ChatGPT to extract a natural language representation of the resulting search results? Let’s see how Bing will handle that pairing!

---

Subscribe to my Newsletter to learn something new every week: TheAiEdge.io
#machinelearning #datascience #systemdesign
