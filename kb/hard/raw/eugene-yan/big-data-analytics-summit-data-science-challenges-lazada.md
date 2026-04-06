# Big Data & Analytics Summit - Data Science Challenges @ Lazada

**Source:** https://eugeneyan.com//speaking/data-science-challenges-impact-lazada-talk/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I was recently invited to share at the Big Data & Analytics Innovation Summit on Data Science at Lazada. There were plenty of sessions sharing on potential use cases and case studies based on other companies, but none on the challenges of building and scaling a data science function. Thus, I decided to share about some of the challenges faced during Lazada-Data’s three-year journey, as we grew from 4 - 5 pioneers to a 40-ish man team.

In a nutshell, the three key challenges faced were:

* How much business input/overriding to allow?
* How fast is “too fast”?
* How to set priorities with the business?

## How much business input/overriding to allow?

How do we balance the trade-off between having business and people providing manual input, vs machine learning systems that perform decision making automatically? Business input is usually in the form of rules or manual processes, while machine learning—when in production—is usually via a black box algorithm.

Before the data science team came to be, processes were done via rules or manual labour. E.g., rules (usually regex) to (i) categorize products, (ii) determine fraudulent transactions, or (iii) redirect users to specific pages based on their search terms. However, this approach was not scalable in the long run.

With the data science team helping with their “black box” algorithms and machine learning systems, the business had to get used to having those task automated. While there were several stakeholders that embraced the automation and freeing up of manpower, some resisted. Those that resisted wanted to retain control over business processes, usually through manual input and rules, as they believed the automated systems were inferior in some aspect. There was also the fear of being made redundant.

Our experience has been that manual input to override algorithms and systems is necessary to some extent, but harmful if overdone (example coming up next). In addition, rules are difficult to maintain! When you have more than 1,000 rules in each domain, who will maintain and QA them daily to check if they still make sense, are applied correctly, and lead to the desired outcomes?

What’s an example of this challenge, and how did we overcome it?

When the Lazada data science team first put our product ranking system into production, category managers wanted to continue manually boosting products (i.e., manually determine product rank on category page and search results).

This was a valid requirement. It allowed category manages to incorporate domain expertise and respond quickly to the environment. E.g., when high-potential new products are released, our ranking system would not rank them highly due to the cold start problem. A seasoned category manager would know which new products (e.g., flagship phones, on-trend fashion items, etc.) would do well and manually boost them to the first page.

Nonetheless, too much manual boosting can reduce site performance (i.e., click-through rate, conversion rate). Imagine having a person rank hundreds of products daily—how likely is it that they would outperform a learning-to-rank ensemble?

To demonstrate the (negative) impact of excessive manual boosting, we conducted multiple AB tests and did some analysis. With this, we could demonstrate and quantify the impact of excessive manual boosting, and determine an ideal threshold of products to manually boost. (Hint: The number is much lower than 100.)

## How fast is “too fast”?

Another challenge we faced is going “too fast”—how could this be a challenge? In this case, the trade-off is between development speed and production stability.

It is not difficult to write code and build data products quickly. Who needs abstractions, utilities, code reviews, test cases, and documentation? Technical debt—what’s that? (Kidding btw).

Yes, we can hack and write code this way for quick POCs—however, be aware that this is not (software) development!

Imagine the hacked-together code (e.g., thousands of lines in a single script, no docstrings or comments) in production. You are not the original developer, but you have to modify it to fix some bugs, or add a new feature. Would your task be easier/faster if there were documentation and automated testing? Having documentation helps with understanding the code better, and automated testing provides assurance that code changes don’t break anything unintentionally. Without these, further development could be really slow, and you can find yourself fixing p0 bugs in production often.

Facebook initially had [“move fast and break things”](https://hackernoon.com/moving-fast-and-breaking-things-is-such-a-load-of-crap-f23ac50215b0) as their motto. However, as they scaled over time, they realized that having to slow down to fix bugs was not helping with their overall speed at all. Thus, their motto is now [“move fast with stable infra”](https://www.cnet.com/news/zuckerberg-move-fast-and-break-things-isnt-how-we-operate-anymore/)—in the long run, this actually helps with moving faster.

Development effort increases in the long run without automation

How did the Lazada data science team overcome this challenge in our journey?

A year after starting the team, we had about 8 people, and 20 problems. We picked 10 with the highest potential ROI and focused mainly on delivery, mostly in one-man teams. By the second year, we had several solutions in production, and had added a lot of value for the company.

However, as we matured in terms of solution complexity and scale, we had to maintain more production code and ops—moving at the same (breakneck) development speed was not helping with delivering better results faster.

Having one person per project is great—it ensures that person will always be employed. Of course not! It’s actually a big risk for the organization. For that person, it means if she’s on vacation, hiking up some mountain, and there’s a p0 bug, she’ll have to pull out her satellite wifi and laptop to fix it.

Thus, as we matured, we had to rethink how to allocate manpower to projects, as well as invest time in building tools and utility code that can be reused to improve on iteration speed. We also found time to pay off technical debt, refactor our code to further simplify, write proper documentation, and ensure code quality.

## How to set priorities with business?

Another challenge we faced was on how to set priorities with the business, the trade-off being between short-term and long-term impact.

The business understands best what is needed and can immediately make an impact on customers, sellers, and business outcomes. They often have good intuition on the overall approach and can provide guidance on initial hypotheses to explore. Nonetheless, they are usually very focused on the day-to-day, and on very near term goals.

On the other hand, the data science team is active in scanning and understanding the cutting edge technology advancements. They can adapt on research and innovate to develop technology or data products that are perhaps 10x better than previously. However, the data science team risks being detached from the business needs—they could spend a lot of time and effort innovating and building things that the business cannot use, wasting valuable time and resources.

How did Lazada navigate this challenge?

We found that timebox-ed skunkworks projects, with the target of delivering a working POC, to be a suitable approach. Often, someone will have an idea for a data product or machine learning system. Sometimes, it will be a solution that the business does not think they need, but we believe will add tremendous value. These ideas will be collated and raised to the leadership team for evaluation, and the best few are selected and sponsored. A clear plan on the innovation, deliverable, and timeline is made, and we work towards the deliverable within the timeline.

Sometimes, we might find that a working solution is out of our reach—this is fine. At the deadline, if this is the final assessment, we move on and not expend any more time and resources on the project.

The majority of the time, we manage to hack together a working POC and present it to the business. Of these, many POCs are accepted for AB testing and demonstrate positive results. The codebase is then refactored and polished, before putting into production.

The intent is to focus on research and innovation that can be directly applied to improve the online shopping experience for customers and sellers, and contribute to business outcomes—not research for research’s sake.

## Conclusion

Those are three key challenges Lazada faced while scaling our data science team, and examples of how we overcame them. There will be alternative approaches and solutions—which works better depends on the team’s context, stakeholders, and resources. I would love to hear more about other challenges you have faced, as well as how you resolved them in the comments below.

Here’s the deck shared at the conference–it includes additional content on how we built our (i) automated review classifier and (ii) product ranking system, and their respective impact.

 
  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jun 2018). Big Data & Analytics Summit - Data Science Challenges @ Lazada. eugeneyan.com.
> https://eugeneyan.com/speaking/data-science-challenges-impact-lazada-talk/.

or

```
@article{yan2018challenge,
  title   = {Big Data & Analytics Summit - Data Science Challenges @ Lazada},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2018},
  month   = {Jun},
  url     = {https://eugeneyan.com/speaking/data-science-challenges-impact-lazada-talk/}
}
```

  
Share on:
