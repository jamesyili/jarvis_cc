# 2024 Year in Review

**Source:** https://eugeneyan.com//writing/2024-review/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

2024 was a peaceful year of steady progress. With regard to my craft, the prototypes of 2023 were scaled and put into production, and I rediscovered the joy of building in public. On the personal side, I continued the prior year’s focus on health, further improving my diet and exercise habits, leading to measurable results.

Past years: [2020](/writing/retrospective-2020/), [2021](/writing/2021-year-in-review/), [2022](/writing/2022-in-review/), [2023](/writing/2023-review/)

## Reviewing my 2024 goals

✅ **Work:** Shipped ML/LLM systems that serve customers at scale. 2024 was the year of productionizing the prototypes of 2023. I learned how to deploy these systems reliably, at scale, and cost-effectively, for both customer-facing UXes and internal pipelines.

✅ **Writing:** Published 6 substantive pieces by writing the following:

* [How to Generate and Use Synthetic Data for Finetuning](/writing/synthetic/)
* [Task-Specific LLM Evals that Do & Don’t Work](/writing/evals/)
* [Prompting Fundamentals and How to Apply them Effectively](/writing/prompting/)
* [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](/writing/llm-evaluators/)
* [How to Interview and Hire ML/AI Engineers](/writing/how-to-interview/)

A major highlight was collaborating with several friends to write [What We’ve Learned From a Year of Building with LLMs](https://applied-llms.org/). This was also published on O’Reilly as a [book](https://www.oreilly.com/library/view/what-we-learned/9781098176716/) and technical series (parts [I](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-i/), [II](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-ii/), [III](https://www.oreilly.com/radar/what-we-learned-from-a-year-of-building-with-llms-part-iii-strategy/)).

I also had fun writing a few shorter, snappier pieces:

* [Don’t Mock Machine Learning Models In Unit Tests](/writing/unit-testing-ml/)
* [39 Lessons on Building ML Systems, Scaling, Execution, and More](/writing/conf-lessons/)
* [How to Run a Weekly Paper Club](/writing/paper-club/)
* [My Minimal MacBook Pro Setup Guide](/writing/mac-setup/)
* [Seemingly Paradoxical Rules of Writing](/writing/paradox/)

On public speaking, while it isn’t an explicit goal, I try to speak once a year for the sake of practice. In 2024, I was invited to speak at [Netflix’s internal RecSys conference](/speaking/netflix-prs/), deliver the [closing keynote](/speaking/aie-2024/) at the AI Engineer World’s Fair with my fellow authors, and judge the [Weights & Biases LLM-Judge hackathon](/speaking/hackathon-judge/). Also, I got to [present my paper](https://x.com/eugeneyalt/status/1846238823333662880) on detecting factual inconsistencies at the Amazon Machine Learning Conference.

✅ **Health:** Further improved my diet and exercise habits. After avoiding jogging in the first half of 2024, I restarted in June. I also bought a [body fat scale](https://www.amazon.com/dp/B01N1UX8RW) on Prime Day in July, and inspired by this [tweet](https://x.com/chrisalbon/status/1832946165446553716), I began intermittent fasting by skipping breakfast. Overall, I’m now exercising daily with a slight calorie deficit.

Here’s my weekly routine:

* At least two sessions of weight training
* At least one session of jogging
* The rest being Zone 2 - 3 cardio on the stair stepper or treadmill

🟠 **Travel:** One of two planned trips completed. We traveled to Alaska to catch the Northern Lights ([November 2024 - March 2026](https://abcnews.go.com/US/peak-northern-lights-activity-occur/story?id=113839425) is the the peak of the 11-year Solar Cycle). Next we have a snowboarding trip to Hakuba Valley in Febuary 2025.

Northern Lights in Alaska

❌ **Snowboarding:** Did not do a black run in 2024. In hindsight, this was a stretch given our limited time on the slopes (~5 times a year). We ended 2024 with a lesson to get more comfortable on the blue runs. With our upcoming Hakuba Valley trip and a few more sessions on Crystal, we’re hoping to get comfortable enough to attempt a black run in 2025.

✅ **Learn something new:** Beyond diving into [synthetic data for finetuning](/writing/synthetic/), [application-specific evals](/writing/evals/), [LLM-evaluators](/writing/llm-evaluators/), and [various web frameworks](/writing/web-frameworks/), I also improved my product thinking via Shreya Doshi’s [Product Sense](https://maven.com/shreyas-doshi/product-sense) course.

## Building AI Coach & AlignEval

Inspired by this [tweet](https://x.com/swyx/status/1765995892107317407), I explored voice as a modality by building [Tara, an AI Coach](/writing/ai-coach/) you can talk to on the go. Since launching, Tara has helped hundreds of people. A few of them have reached out to share positive, constructive feedback. My favorite story is how Tara convinced someone’s spouse to quit their horrible role after reminding them, in a gentle yet tough-love tone, that it was a “soul-sucking job”.

While researching and writing about [LLM-evaluators](/writing/llm-evaluators/), I started developing an idiosyncratic take on how we should build LLMs as judges. To test these ideas, I built [AlignEval](https://aligneval.com/).

AlignEval: Label -> Evaluate -> Optimize

The response and usage has been more positive than I expected. So far, users have:

* Uploaded 538 dataset files
* Labeled ≥ 1 sample for 454 files
* Labeled ≥ 20 samples for 289 files and ran an LLM-evaluator
* Labeled ≥ 50 samples for 84 files and optimized their LLM-evaluator

Building AI Coach and AlignEval was a blast, and the feedback from users has been valuable. I already have ideas for AlignEval v2.

## Doubling Down on Health

In 2023, I started to watch my sugar, saturated fat, and alcohol intake, and exercised 3 - 4 times a week. 2024 is more of the same, with:

* Limiting alcohol/snacks to three servings per week
* Intermittent fasting by skipping breakfast (since September)
* Tracking body fat percentage (since September)
* Increasing protein intake (since September; [David bars](https://davidprotein.com/) are great)
* Doing intervals for more heart-pumping exercise (since June)
* At least 30 minutes of exercise every day (since June)

These changes have helped lower my resting heart rate and body fat percentage.

Resting heart rate and body fat percentage decreased since the middle of 2024

## Statistics for 2024

Google Search traffic took a hit in 2024, with impressions falling from 2.71M to 1.97M (-27.3%) and clicks dropping proportionately from 77.6k to 56.5k (-27.2%). While this data is from a single site, it might hint at the scale of the decline in Google’s traffic. Also, despite my average position improving from 31.5 to 24.6, CTR held steady at 2.9%.

Impressions and clicks from Google Search fell in 2024

Given the dip in search metrics, it’s surprising that eugeneyan.com saw a 10.5% increase in unique visitors, reaching 285k in 2024. The graph suggests this was driven by outlier traffic, likely from HackerNews.

Despite the hit on Search traffic, users and views continued growing from 2023

The distribution of incoming channels and geography remained similar to 2023.

Incoming channels and geography remained similar to 2023

Seven of the top 10 pages were published in 2024 though three older pieces continued to resonate: (i) [Patterns for Building LLM Systems](/writing/llm-patterns/) with 62.4k views, (ii) [Simplicity](/writing/simplicity/) with 23.4k views, and (iii) [System Design for RecSys](/writing/system-design-for-discovery/) with 18k views.

Top 10 most popular write-ups in 2024

Social metrics continued growing

* Email subscribers from 6.2k to 9.5k (+34.7%); 54.9% open rate and 6% click rate
* Twitter followers from 15.8k to 21.3k (+25.8%)
* LinkedIn followers from 32.7k to 37.7k (+13.3%)

Subscriber growth continued in 2024, with the increase since June due to recommendations

Side note: Compiling these engagement metrics felt less insightful this year. I might skip them in the next annual review.

## Goals for 2025

* **Write 6 substantive pieces**
* (New) **Prototype 4 apps in public**: Building AI Coach and AlignEval in public was educational, lots of fun, and yielded valuable feedback. Will do more in 2025.
* **Health**: Stay consistent with diet and exercise until they become ingrained habits
* **Snowboarding**: Try a black run by the end of the year

Several goals from previous years, like meditating, learning, and traveling, have become so habitual that restating them annually feels unnecessary. On the other hand, some of my newer goals feel too personal to share publicly right now—perhaps in a future review!

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Dec 2024). 2024 Year in Review. eugeneyan.com.
> https://eugeneyan.com/writing/2024-review/.

or

```
@article{yan20242024-review,
  title   = {2024 Year in Review},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2024},
  month   = {Dec},
  url     = {https://eugeneyan.com/writing/2024-review/}
}
```

  
Share on:
