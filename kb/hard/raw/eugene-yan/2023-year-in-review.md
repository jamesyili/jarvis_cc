# 2023 Year in Review

**Source:** https://eugeneyan.com//writing/2023-review/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

2023 was a peaceful year of small, steady steps. There were no major lifestyle changes and I had the time and energy to explore new interests and focus on learning. Here’s my 2023 year in review, including goals, highlights, and statistics.

Past years: [2020](/writing/retrospective-2020/), [2021](/writing/2021-year-in-review/), [2022](/writing/2022-in-review/)

## Goals

First, checking in on the [goals I had set for myself](/writing/2022-in-review/#goals-for-2023) last year:

* **Write 26 posts 💪:** I wrote 20 posts, hacked on five prototypes, and gave two talks. My writing covered topics such as [project mechanisms](/writing/mechanisms-for-projects/), [content moderation](/writing/content-moderation/), [ML patterns](/writing/more-patterns/), [experiments with LLMs](/writing/llm-experiments/), and [LLM patterns](/writing/llm-patterns/). The last two were well received and gained the [🔥 tag](/tag/🔥/) (>20k views).
* **Learn something new ✅:** Though I learned a lot about [Search](/writing/search-query-matching/) on the job, I lacked the fundamentals. Grant Ingersoll and Dan Tunkelang’s excellent [Search track](https://uplimit.com/track/search) helped to fill this gap. I also dove deep into content moderation and [labeling queues](/writing/labeling-guidelines/) for work, and spent many nights and weekends tinkering with LLMs.
* **Work with a career coach 💪:** GPT-4 has been effective at helping me reflect and consider various perspectives, and suggesting next steps. That said, I wonder if I should still get a human career coach, and am open to recommendations!
* **Advance the industry ✅:** I think [my writing on LLMs](/tag/llm/) has helped here. That said, I haven’t convinced enough people that [lexical search should be part of RAG](https://x.com/eugeneyan/status/1738097398273163375).
* **Learn to snowboard ✅:** My wife and I started on the blue slopes this week!
* **Read fiction ❌:** I was mostly occupied with the firehose of GenAI papers and advancements. Nonetheless, I was able to make time for some fiction, mostly sci-fi (Pandemic, Genome) and short stories (Ted Chiang, Cixin Liu).
* **Meditate 60 minutes daily ❌:** I didn’t do the full 60 minutes and funneled some time towards exercise and journaling instead.

I wished I could have found more time to meditate and read fiction but it’s been tough this year with all the learning I’ve had to do. Nonetheless, I’m happy with the progress on the other goals. Beyond the goals, I also had a few other highlights.

## Exploring LLMs

With the step-change improvement from gpt-3.5-turbo, I started paying more attention to language modeling (LM) at the start of 2023. Thankfully, I had some familiarity with the subject, having previously applied [LM models](/writing/nlp-supervised-learning-survey/) to recommender systems and experimented with gpt-3 for simple summarizations. To catch up, I did some experimentation and prototyping to learn the strengths and limits of autoregressive LMs. These prototypes included [Discord bots](/writing/llm-experiments/), [UIs for interacting with LLMs](/writing/llm-ux/), [Obsidian copilot](/writing/obsidian-copilot/) based on lexical and embedding-based RAG, and [finetuning a hallucination classifier](/writing/finetuning/) on out-of-domain data.

This self-learning set me up for success at internal hackathons. Our first prototype, codenamed Dewey, did well (shout out to my awesome partner-in-crime Kelly N!) This gave me the courage to ask if I could start working on GenAI at least one day per week, and perhaps eventually transition to half-time. This request went better than expected…

## Transitioning to a new role

Since then, my Charter has expanded to include working on GenAI initiatives across the org. This includes educating the working level and senior leadership, as well as figuring out [how to deploy GenAI reliably and cost-effectively at scale](/writing/llm-patterns/). We’ve organized two fruitful hackathons: Two prototypes have been launched while two more are in progress.

## Writing and speaking

Although I didn’t hit my goal of 26 posts, I’m proud of the writing I’ve done this year. Some pieces that have been impactful include:

* [Patterns for Building LLM-based Systems & Products](/writing/llm-patterns/)
* [More Design Patterns For Machine Learning Systems](/writing/more-patterns/)
* [Content Moderation & Fraud Detection - Patterns in Industry](/writing/content-moderation/)
* [Evaluation & Hallucination Detection for Abstractive Summaries](/writing/abstractive/)

Much of my writing is a byproduct of my work building ML systems, and in return it contributes to me being more effective at the work. Writing helps identify and fill my knowledge gaps, refine my thinking, and scale my sharing. (I learned that my leadership reads my writing and tweets 😱)

As usual, I found writing easier when I write with a specific person in mind (instead of a vague general audience). Some example pieces and their audience-of-one include:

* [Dependency teams](/writing/getting-help/) and [Matching LLM patterns](/writing/llm-problems/) was written for mentees
* [Labeling guides](/writing/labeling-guidelines/) and [Attention & Transformers](/writing/attention/) was written for PMs
* [Project mechanisms](/writing/mechanisms-for-projects/) and [Team mechanisms](/writing/mechanisms-for-teams/) was written for tech managers
* [LLM patterns](/writing/llm-patterns/) and [Summarization evals](/writing/abstractive/) was written for senior leaders

I also had the opportunity to [speak at the inaugural AI Engineer Summit](/speaking/ai-eng-summit/). The energy was inspiring (my recap [here](/writing/aieng-reflections/)) and I got the chance to connect and stay in touch with several practitioners as we figure out how to use this new technology in production.

In addition, I gave an invited keynote at the Amazon Machine Learning Conference. I took the chance to share the awesome work our team had done on session-based retrieval, contextual ranking, and cost-effective, just-in-time infrastructure. (I previously presented a public version at [RecSys 2022 as a keynote](/speaking/recsys2022-keynote/) too.)

## Paper club

Together with a few friends, we started a [paper club](https://lu.ma/llm-paper-club) to read and discuss fundamental papers in the LM space. I believe we’ve learned more as a group than we could have individually, by pooling together our shared knowledge, experience, and questions. Here are [one-sentence summaries for the earlier papers](/writing/llm-reading-list/).

## Angel investments

I made three angel investments in ML and tooling startups. This will likely be the volume of investments going forward. I’ve also become more selective, focusing on startups where I can provide the most value, mostly in the field of data and ML.

## Health

I had a minor health scare (that involved bruising easily) that prompted me to reexamine my diet and exercise. My wife and I paid more scrutiny to our nutrition, such as reducing saturated fat and alcohol. We continued to keep sugar and processed food to a minimum.

Also, while I’ve been consistent with weight training, I’ve been neglecting cardio. Thus, I started forcing myself to jog at least twice a week. On challenging weeks, I make do with 45-minute brisk walks. This has improved my resting heart rate and VO2 max.

## Goals for 2024

* **Work:** Continue shipping ML systems that serve customers at scale. Prototype on the side to test new tech (e.g., vision). Teach what I’ve learned.
* **Writing:** Write 6 good pieces. I previously focused on quantity ([writing once a week](/writing/retrospective-2020/#my-sole-2020-resolution-writing-weekly)) to build the habit. Now that it’s stable, I’ll invest more time into each piece, especially writes-ups that require more research or prototyping.
* **Health:** Minimize sugar, saturated fat, alcohol, and processed food in my diet. Exercise five days a week, with at least two days of cardio. 30 minutes of gratitude journaling and meditation first thing in the morning.
* **Travel:** Make time for two vacations (likely Las Vegas and Alaska).
* **Snowboarding:** Aiming to start hitting the black slopes by the end of the year.
* **Learn something new:** Tentatively synthetic data for finetuning, model distilation to reduce serving costs, and cold-start/ad-based recsys.

### Mission statement (v5)

I wrote my first mission statement in 2013 and have been revising it every year or so. Here’s the latest iteration, written while on the flight back from SF after a particularly inspiring and energizing week. Fun fact: It started as a tweet and fits in 280 chars.

```
• Work hard
• Keep learning
• Cherish loved ones
• Find people who inspire you
• Be kind & egoless
• Eat healthy, exercise, sleep well
• Read & write
• Practice gratitude & meditate
• Be present
• Enjoy food & nature
• Don’t sweat the small stuff
• Smile
```

## Statistics for 2023

Here’s a word cloud of my writing in 2023. The top themes (user, data, model) have been consistent though the focus on LLMs is new. (Word cloud from a previous year [here](/writing/2021-year-in-review/#statistics-and-charts-for-2021).)

Word cloud of my writing in 2023

This site saw 259k unique visitors in 2023, an increase of 21% from 2022.

Number of unique visitors in 2023

The incoming channels were mostly direct, organic search, and organic social. The US is the largest source by far (and it looks like my audience in Singapore is tapering 😢).

Channel and geography of readers in 2023

The top pages in 2023 were mostly broader pieces on patterns and system design. Old but gold pieces continue to be in the top 10, including: (i) [recsys system design](/writing/system-design-for-discovery/), (ii) [writing why what how](/writing/writing-docs-why-what-how/), and (iii) [real-time retrieval](/writing/real-time-recommendations/).

Top 10 most visited pages in 2023

Clicks via Google search was mostly flat at 77.6k, though impressions increased from 2.14M to 2.71M (+27%). As a result, average CTR dropped from 3.6% to 2.9% (-19%).

Google search traffic in 2023

Miscellaneous social metrics

* Email: Subscriber count grew from 4.2k to 6.2k; 55.7% open rate, 6.8% click rate.
* Twitter: Follower count grew from 9.5k to 15.8k
* LinkedIn: Follower count grew from 27.1k to 32.7k

Email subscriber growth in 2023

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Dec 2023). 2023 Year in Review. eugeneyan.com.
> https://eugeneyan.com/writing/2023-review/.

or

```
@article{yan20232023-review,
  title   = {2023 Year in Review},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2023},
  month   = {Dec},
  url     = {https://eugeneyan.com/writing/2023-review/}
}
```

  
Share on:
