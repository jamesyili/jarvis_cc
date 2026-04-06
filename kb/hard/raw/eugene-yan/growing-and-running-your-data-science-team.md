# Growing and Running Your Data Science Team

**Source:** https://eugeneyan.com//writing/data-science-teams/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

An effective data science team is like the goose that lays the golden eggs. Sometimes, we focus too much on the eggs (i.e., results)—how can we get more, faster? As a result, the goose (i.e., team) can get neglected.

> Stage 3 manager:  
>   
> A manager who is all-business & primarily views people as "resources". May care about people. May even care a lot.  
>   
> But cares much more about short term results & targets. So when the two are in conflict, she will unabashedly prioritize short term results.
>
> — Shreyas Doshi (@shreyas) [January 30, 2021](https://twitter.com/shreyas/status/1355405171321262083?ref_src=twsrc%5Etfw)

Here, we’ll focus on the goose. I’ll share what I learned about growing ([hiring](#hiring-the-most-important-thing-you-can-do), [training](#training-similar-to-transfer-learning)) and running ([innovation](#innovation-encouraging-creativity-ideas-and-risks), [discipline](#discipline-bridging-ideas-and-results), [camaraderie](#camaraderie-gluing-the-team-together)) data science teams. This is based on [my experience](https://eugeneyan.com/about/) at Lazada (as an early DS who eventually led the team) and uCare (where we shipped an [ML system for Southeast Asia’s largest hospital chain](https://www.healthcareitnews.com/news/asia-pacific/parkway-pantai-offer-fixed-prices-certain-medical-procedures-using-ai-powered-tool)). I measured myself on team productivity, growth, and well-being. Here’s what made the biggest impact.

> This was requested on the [topic-poll](/topic-poll/). Please add your topics and vote! 🙏

## Hiring: The most important thing you can do

Hiring is the most important thing *everyone* on the team can do to contribute to our success. We should always try to raise the bar by finding people who will improve the talent pool. Here’s how I identify such people:

* What can this person (potentially) do better than everyone else on the team?
* What can our team learn from this person?
* Would I want to be part of a project led by this person?

This doesn’t mean that we *only* hire people who have better qualifications or are more senior. Recent grads and juniors contribute infectious energy, a fresh pair of eyes, new ideas, and knowledge of the latest research and technology. Mentoring them is also rewarding for everyone on the team. We don’t need new hires to be better than everyone on the team *now*, but we should believe that they will *surpass us in future*.

> If each of us hires people who are smaller than we are, we shall become a company of dwarfs. But if each of us hires people who are bigger than we are, we shall become a company of giants. — David Ogilvy

I had the chance to interview hundreds of candidates and work with those who made it through the process, including people I was *against* hiring (I wasn’t the final decision maker sometimes). This gave me a rare opportunity to observe a wide spectrum of candidates and follow their journey through several projects. There were three traits most great hires had.

First, they are **curious**. When stakeholders ask them to solve a problem, they’ll ask “Why? How does solving this problem create value?” (This can annoy stakeholders but is correct behavior IMHO). When given access to data, they’ll trace it upstream so they can clean and use it correctly, often building their own data pipelines. They’ll dig into issues that haven’t become full-blown problems yet, bring attention to them, and start solving them.

They also have **grit**. A big chunk of our work involves R&D and experimentation. Failure and negative results are to be expected. Having grit (and a touch of optimism) helps them push through the low points.

Finally, they are **humble**. They don’t let their egos get in the way and are less prone to the [“Not Invented Here”](https://learnosity.com/not-invented-here-syndrome-explained/) syndrome. They’re stay detached from their assumptions and hypotheses, especially when data and experimentation disagree. They’re also more willing to accept feedback on their designs and work, leading to improved outcomes for the team (also see [Crocker’s Law](/writing/how-to-apply-crockers-law-for-feedback-and-growth/)).

> Hire character, train skill. — Peter Schutz

Skills-wise, I noticed that great hires could deliver projects **mostly [end-to-end](/writing/end-to-end-data-science/)**. Thus, they start, and continue, delivering value faster than most. (Note: This observation is likely biased by my experience in start-ups and scale-ups). And if they lacked the skill or knowledge (e.g., Docker, CI/CD), they were enthusiastic to learn the ropes, helping them be more productive on their next project.

Here are some heuristics I use to assess the above (caveat emptor):

* The scope of previous work demonstrates the extent of their end-to-end skills.
* Personal projects show curiosity to learn on their own time. Similarly, the scope demonstrates their ability to work end-to-end and persistence in finishing it, especially if they had to learn something new (e.g., deploying on AWS).
* The ability to accept and act on feedback during design/coding interviews can reveal ego (and lack of humility). Being overly defensive or unwilling to accept alternatives might be a red flag.
* Participation in sports at a competitive level (e.g., marathons, e-sports) and having consistent habits demonstrates grit, and to a certain extent, dependability.

A valuable but rare trait: Hunger

One other valuable—but rare—trait is **hunger**. As I interact and work with some people, I sense that they are hungry to learn, hungry to get shit done, hungry for impact. Such people have a perpetual-motion engine in them and need lesser management. They also deliver disproportionally outsized results relative to the rest of the team.

> Great companies don’t hire skilled people and motivate them, they hire already motivated people and inspire them. — Simon Sinek

However, I think this trait depends on a person’s life stage. I see it mostly in younger folks, especially those just out of school, who have not started families of their own. They’re idealistic and ambitious, and have more time and energy to focus on learning and career. Hunger can also subside with time—a new mum will have less time to learn new tech or tinker on personal projects on the weekends. Thus, I don’t emphasize it when hiring.

It’s not easy to assess hunger over interviews. Some candidates appeared dispassionate and quiet during interviews but turned out to be hungry after getting to know them better, and vice versa. If you have a way to assess this, I would love to hear from you.

Referrals and meetups/conferences were our best channels for hiring—about 90% of hires came from them. At Lazada, our first data engineer brought in fellow rockstars in the big data space, one of whom eventually became our VP of data engineering. Referrals are a great source of quality candidates as we only tend to refer people we (i) enjoy working with and/or (ii) can learn from, especially if the referral is joining the same team.

Hiring via meetups is a hack to cheaply building/scaling a team. I observed this first-hand in Singapore’s meetup scene where companies would speak at meetups to hire. [AXA](https://www.meetup.com/DataScience-SG-Singapore/events/231463742/), [Twitter](https://www.meetup.com/DataScience-SG-Singapore/events/237365856/), and [Uber](https://www.meetup.com/DataScience-SG-Singapore/events/239842664/) hosted meetups as they were setting up tech hubs while [Go-Jek](https://www.meetup.com/DataScience-SG-Singapore/events/242352295/), [HonestBee](https://www.meetup.com/DataScience-SG-Singapore/events/234190669/), [Facebook](https://www.meetup.com/DataScience-SG-Singapore/events/216933342/), and [Shopee](https://www.meetup.com/DataScience-SG-Singapore/events/240723055/) actively shared at meetups to scale their teams. Similarly, Lazada’s sharing at [conferences](https://www.oreilly.com/library/view/strata-hadoop/9781491944561/video234452.html) and [meetups](https://www.meetup.com/DataScience-SG-Singapore/events/235703077/) helped with several great hires.

## Training: Similar to transfer learning

As we hire people who raise the bar, training almost takes care of itself. IMHO, the best way to develop the team is to surround them with superb teammates they can learn from, and give them ambitious problems to work on. For example, as the team collaborates with the newly joined NLP expert, they pick up some of her hard-won NLP tricks and best practices.

> Nothing we do is more important than hiring and developing people. At the end of the day, you bet on people, not on strategies. — Lawrence Bossidy

Demos are a great way to promote learning. (If you adopt scrum, [demos come as part of the process](/writing/what-i-love-about-scrum-for-data-science/#demos-boost-morale-and-promote-accountability).) Everyone loves demos. Demo-ers are excited to share their work and get feedback. Attendees love learning more about what everyone else on the team is working on. Demos provide a way for the team to sync, learn from each other, and learn from the questions others may ask.

Another favorite practice is paper-lunches (aka lunch-and-learn). Every two weeks, two people share a paper each. Ideally, something they’re excited about and applicable to their work. They focus on understanding the paper thoroughly—this happens as part of project research anyway—and giving a quick walkthrough of it. The rest of the team is expected to read the paper beforehand and come prepared with questions and discussion points. In a year, the team would have discussed 50 papers! (More on [why we should read papers](/writing/why-read-papers/).)

A final approach is conducting reviews (e.g, code, design reviews). Reviews are not just a process for seniors to vet design documents and code; it’s also a learning and development opportunity. Reviewing pull requests is a great way for new joiners to ramp up on the codebase and standards. It’s also an avenue to clarify doubts and provide feedback.

Sitting in design reviews helps team members learn how business stakeholders and senior engineers/scientists think, balance trade-offs, and make decisions. For example, stakeholders focus on business requirements (e.g., bottom-line metrics, user experience) and ROI, while engineers focus on technical requirements (e.g., scalability, latency, failover) and long-term ops costs. Scientists focus on data flows, methodology, experimental results, A/B testing, etc.

By participating in reviews, the team picks up best practices and learns how to balance the concerns of different stakeholders, helping them to improve their future designs and code.

## Innovation: Encouraging creativity, ideas, and risks

As the data science team achieves success and improves metrics, we’ll be expected to continue growing these metrics linearly (or even exponentially). For example, if revenue attributed to our ML systems (e.g., recommendations, push notifications) increased 10% last year, this year’s targets will be the same, if not more. Such demanding expectations can leave little room for riskier, longer-term, projects.

I find this akin to the [innovator’s dilemma](https://en.wikipedia.org/wiki/The_Innovator's_Dilemma). To keep delivering on increasing targets, we focus on safe, incremental gains. However, past a certain threshold, we hit the point of diminishing returns on the current paradigm (e.g., daily recommendations) and a shift (e.g., real-time recommendations) is necessary. However, such paradigm shifts can be risky, with the payoff in an uncertain future.

Nonetheless, such innovation is essential. Without continuous innovation and product improvement, we can get to a point where all we’re left with is a Hail Mary bet at the end.

> Companies that don’t continue to experiment or embrace failure eventually get in the position where the only thing they can do is make a Hail Mary bet at the end of their corporate existence. — Jeff Bezos

Innovator’s dilemma in the hard drive industry

In the ‘70s, hard drive producers focused on building hard drives for mainframe producers. These mainframe producers wanted more storage and faster transfer rates and the hard drive incumbents gave it to them.

However, some start-ups and smaller companies went in the opposite direction. They started producing hard drives that had *lesser* storage and *slower* transfer rates, but were half the size. These drives were mainly for the then-nascent minicomputer market.

Back then, minicomputers were a small fraction of the hard drive market and incumbents weren’t interested in serving them (i.e., small portion of overall revenue).

However, as we know, mini and personal computers flourished while mainframes declined. As a result, the underdogs who focused on disruptive, initially unpopular, technology (i.e., smaller hard drives) now had a lion’s share of the market.

This shows that disruptive tech (smaller computers, smaller drives) can initially underperform and thus not make sense financially. However, they may become fully competitive tomorrow, and not investing in them could be a company’s downfall.

One way to foster innovation is by sharing openly about failure. When team members confide their project and A/B testing anxieties, sharing about [my flop](/writing/psych-grad-to-data-science-lead/#how-i-lost-millions-on-my-first-ab-test) puts them at ease. I also openly share our team’s failures and negative experiments (if the people involved are 100% okay with it). By doing so, I hope to inculcate the mindset—especially among stakeholders—that experimentation and ~~failure~~ learning are a key part of our work. As my old boss, John used to say: “That’s not a mistake; it’s an opportunity to learn!”

> “Failure is an option here. If things are not failing, you’re not innovating enough” — Elon Musk

I’ve also found it helpful to be an accountability partner and cheerleader on [20% projects](https://en.wikipedia.org/wiki/20%25_Project). Though 20% projects start with passion, they can get pushed to the back burner to make way for more urgent work, or lose steam due to lack of accountability and visibility. After a year, there’s nothing to show for it—this is unfulfilling for both the people involved and the business.

Thus, when someone proposes a 20% project, I work with them to scope it out and check in now and then, making sure they have the space, time, and resources to work on it. This also signals that the 20% project is as important as regular work, if not more. And if the project is a success, it graduates out of “incubation” and becomes an MVP that we can put in front of customers and get their feedback.

## Discipline: Bridging ideas and results

With a team of creative, intelligent data scientists, we want to give them the freedom and autonomy to innovate and do great work. I’ve found having a culture of discipline helps.

Discipline starts as early as selecting the right problems to solve. The goal of a business is to create value for customers and the organization. Thus, when deciding on projects, we should start from our customers (e.g., [Working Backwards](https://www.inc.com/justin-bariso/amazon-uses-a-secret-process-for-launching-new-ideas-and-it-can-transform-way-you-work.html)) and business needs, or focus on capabilities that will allow us to meet those needs more effectively.

Operationalizing this via a [one-pager](/writing/what-i-do-before-a-data-science-project-to-ensure-success/#first-draw-the-map-to-the-destination-one-pager) is helpful. The one-pager defines the intent, desired outcome, deliverables, and constraints. It is then circulated to get alignment with stakeholders before any substantial work starts. Doing this upfront ensures we ask the *right* questions and solve the *right* problems, instead of unnecessarily going down rabbit holes or boiling the ocean.

Discipline also matters in execution. I view this as executing with a sense of urgency. Basecamp found [6-week cycles](https://basecamp.com/shapeup/2.2-chapter-08) to work best for them—it’s long enough to finish something meaningful yet short enough to feel urgent. IMHO, most data science projects should be run like a start-up. We want to ship early and ship often, so we can quickly get feedback from customers, iterate, and improve.

> The number one predictor of success for a very young startup: rate of iteration. — Sam Altman

This thinking explains my inclination towards scrum and [time-boxing](/writing/what-i-love-about-scrum-for-data-science/#time-boxed-iterations-speed-up-learning--limit-loss) for data science. Each sprint delivers milestones that we can bring to stakeholders and/or customers to get their feedback on. We want to be like stochastic gradient descent (i.e., incremental deliverables) rather than batch gradient descent (i.e., Big Bang integration).

We also foster discipline through the standards we uphold (or tolerate). For example, we should have objective standards for [linting, type checks, and functional tests](/writing/setting-up-python-project-for-automation-and-collaboration/). Another way is to actively share examples of great work (e.g., documents, deliverables) that meet and surpass our standards, so we have ideals to aspire towards.

While such standards can seem stifling, they provide more freedom in the medium-to-long term. Consistent processes and standards let us focus on the work that matters (instead of constantly reinventing processes or templates). And because everyone adopts the same standards, it’s much easier to understand and provide feedback on projects across the entire team, as well as fluidly move between projects as required.

## Camaraderie: Gluing the team together

One of my biggest contributions while leading teams was to build camaraderie. While at Lazada, together with the VP of data engineering, we would open and close the “bar” every Friday. (We started happy hour so the team could point to us and join in, and stay back to clean up). In my next role, happy hour didn’t work but Counterstrike did. Fragging each other (especially the QA and CTO) on Friday nights was great for team bonding.

Team bonding helps to build trust. With a high level of trust, there’s no more second-guessing. I know you’re critiquing my work because you objectively think there’s room for improvement, and not because you have something personal against me (i.e., [Crocker’s Law](/writing/how-to-apply-crockers-law-for-feedback-and-growth/)). This lets us disagree openly and figure out the best possible outcome. It also saves time and cognitive capacity. There’s no need to read between the lines or try to figure out what someone *really* meant.

> A team is not a group of people that work together. A team is a group of people that trust each other. — Simon Sinek

As trust builds, people share more too. I noticed a team member behaving slightly off and not joining for team lunch as much as she used to, and casually asked if she was alright. She shared that, with 6 months left on her work visa, she had difficulty renewing the lease on her apartment. Most landlords had a minimum lease of 1 year and few wanted to take the risk of renting to her. Knowing this, I worked with HR to renew her visa, indirectly helping her secure an apartment. With that worry off her mind, she could focus on her work better.

Having camaraderie also makes work more enjoyable. We’re going to be spending at least 8 hours a day, every weekday, with the team (though less now with WFH)—why not make it fun? Research shows that team camaraderie can translate into measurable outcomes. Gallup found that employees who have a best friend at work were [twice as likely to be engaged](https://www.gallup.com/workplace/236213/why-need-best-friends-work.aspx). They were also less likely to be looking for, or watching for job opportunities, thus helping to improve retention.

## Conclusion

It’s great to have a results-oriented team—they deliver! Nonetheless, do also make sure to take care of the goose, and not just focus on the golden eggs.

What other practices did you find useful for building and running effective data science teams? Would love to hear from you [@eugeneyan](https://twitter.com/eugeneyan) or in the comments below.

> How do we grow & run an effective data team?   
>   
> Here's what I learned about:  
> • Hiring: The most important thing  
> • Training: Knowledge transfer  
> • Innovation: Encouraging creativity  
> • Discipline: Bridging ideas & results  
> • Camaraderie: Gluing the team <https://t.co/NLZjFjvgg8>
>
> — Eugene Yan (@eugeneyan) [February 2, 2021](https://twitter.com/eugeneyan/status/1356411512844218368?ref_src=twsrc%5Etfw)

**Thanks** to Yang Xinyi for reading drafts of this.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Jan 2021). Growing and Running Your Data Science Team. eugeneyan.com.
> https://eugeneyan.com/writing/data-science-teams/.

or

```
@article{yan2021team,
  title   = {Growing and Running Your Data Science Team},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2021},
  month   = {Jan},
  url     = {https://eugeneyan.com/writing/data-science-teams/}
}
```

  
Share on:
