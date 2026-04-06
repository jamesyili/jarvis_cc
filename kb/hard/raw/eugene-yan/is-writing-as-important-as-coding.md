# Is Writing as Important as Coding?

**Source:** https://eugeneyan.com//writing/writing-and-coding/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

Does writing become more important (relative to coding) as we transition to senior roles? How is writing beneficial in technical positions? How can we help the team write better?

As a data scientist, I find myself straddling between building and deploying ML systems (*coding*), and communicating proposals and explaining results (*writing*). What’s the optimal balance between writing code and writing documents?

Here, we’ll discuss these questions and more. I’m also happy to have several friends who will chime in with their lessons and advice:

* [David Said](https://www.linkedin.com/in/david-said-martinez-3836a72b/), Principal Engineer @ Amazon
* [Alexey Grigorev](https://twitter.com/Al_Grigor), Lead Data Scientist @ OLX Group
* [Pratik Bhavsar](https://twitter.com/nlpguy_), NLP Engineer @ Jina AI
* [Grace Tang](https://www.linkedin.com/in/tsmgrace/), Senior Data Scientist @ Netflix

## As we grow, how we can contribute *most* shifts

**At the start of our careers, it’s all about delivery**. We contribute by implementing and delivering systems (via *writing code*). David describes this aptly:

> “[At the start,] you need to focus on getting your fangs [akin to earning your stripes] on real-world problems. Then, as you get your fangs and grow your career, it becomes more important to share what you know.” – David Said

So as we gain experience and grow our fangs, the way in which we create impact changes. Instead of implementing systems ourselves, it becomes more valuable to **guide and serve the team**. A great way to do this is via *writing documents*.

One way (to guide the team) is **providing the context and the why**. As we rise in seniority, we gain context—business goals, organization roadmap, budget—that junior members may lack. A straightforward way to increase team effectiveness is sharing this context and helping the team to understand it. With the context, **they can solve the problem better**.

As lead data scientist, Alexey’s role is to connect the different parts of the organization and have a big picture view of the entire system. While he codes less now, he contributes by conveying the big picture and why to the team. He does this through writing documents such as product roadmaps, requirements, API specs, etc. He advises that seeing the context and communicating it becomes more important as our careers progress:

> “When you grow from middle to senior level, having context matters. Communicating with other teams matters. Understanding if the customer really wants to use what you’re building matters. This is when writing becomes *especially* important, through scoping the context and sharing the message.” – Alexey Grigorev

Focus on sharing the “why”, not the “what” and “how”

Assume that we’re part of an e-commerce platform. Popular products get traffic and continue to stay popular; newer long-tail products don’t get traffic and stay obscure (even though they might be good). Instead of communicating the **what** (increase visibility of new products) and the **how** (randomly pick the latest product to rank high), we should communicate the **why**:

* Customers get bored seeing the same products and leave the platform
* It’s risky to have a disproportionately large amount of sales concentrated on a small number of sellers and products (i.e., poor seller & assortment health)
* New sellers who don’t get traffic and sales get discouraged and leave

By sharing the context and the why—and giving space to figure out the what and the how—we empower the team to creatively solve the customer’s problem. In my experience, this almost always leads to a far better outcome than expected.

(In this case, we fixed it with a combination of [understanding customers unmet demands](https://www.slideshare.net/eugeneyan/how-lazada-ranks-products-to-improve-customer-experience-and-conversion#30) and providing the ability for sellers to place ads.)

Also, with the lessons we’ve learned (read: failures), we can contribute by **helping to look around corners**. We do this by [foreseeing potential pitfalls](/writing/what-i-do-before-a-data-science-project-to-ensure-success/#break-it-down-to-spot-rabbit-holes-and-dead-ends) the team should prioritize early. Or we can suggest (or decide) on problem statements, methodology, and technology. This could involve reviewing design docs and leaving feedback, or writing the design doc and [setting boundaries](/writing/what-i-do-before-a-data-science-project-to-ensure-success/#constraints-how-not). Thus, our contribution transitions from day-to-day execution to longer-term strategic thinking:

> “As you become a tech leader, you need to think about the future. The experienced are those who know what the corners are and how to look around them. They have to parse the business problems, do the (design and code) reviews, and minimize the errors that the team commits.” – David Said

A well-timed insight can save weeks, if not months, of going down the rabbit hole. Unfortunately, the reverse can also happen if recommendations of tech leads are ignored.

In addition, we’ll need to **learn how to scale our impact**. The number of systems we can build ourselves is limited. To increase our impact, we’ll need to gain leverage by working with other people, by working across multiple teams and projects.

Here’s where writing helps. It scales well—once written, an API spec can be easily distributed without additional effort. It clarifies—the same spec can help achieve alignment and unblock multiple teams at once. Also, by writing about the lessons we’ve learned and the how-tos, we pave the way for those who follow our footsteps:

> “As soon as you get into a senior role (maybe not title-wise, but having increased scope), you’ll have to work with others. A great mechanism for this is via documentation. If you’ve always been a coder, you might find this boring. But writing documentation, such as how to deploy [CloudFormation](https://aws.amazon.com/cloudformation/), is tremendously helpful both for yourself and the team.” – Pratik Bhavsar

All in all, this suggests that (as we grow in our careers) we’ll find ourselves **writing more and coding less**. Grace observed that in general, individual contributors (ICs) tend to write more code, while tech leads and managers tend to write more docs. Nonetheless, writing documents is important *even* if you’re an IC:

> “Both writing docs and writing code are important: Write good code and perform quality analysis, then write good docs to maximize its impact. You need to help stakeholders be aware of and understand your work so it can make an impact. Not sharing your work means no one knows about it and no one can use it.” – Grace Tang

If you’re mostly writing docs, how can you write more code?

If you're a senior member, the team counts on you to provide the strategic long-term vision and roadmap. To do this well, it’s essential to stay grounded on, and understand, the existing systems and codebase.

Consciously think about how to find time to code, perhaps by jumping into a sprint and picking up a task. Choose an area of the design and implementation that you can dig deep into. Focus on tasks with longer-term goals and a lengthier lead time. This way, your work will not become an immediate blocker for the team (when you get waylaid with higher-level tasks that demand your attention).

## Writing has several benefits, especially in tech roles

> “Writing is nature’s way of letting you know how sloppy your thinking is.” – Dick Guindon, via Leslie Lamport

Without writing, we might believe our designs are sound, our methodology clear, and our understanding complete. Well, trying to write about it will sort that out. Writing is a hack to **gaining clarity**. Here’s Jeff Bezos on why he banned powerpoint (as a medium at meetings) and enforced six-page narratives instead:

The fateful email that changed Amazon.

Yes, the audience benefits from reading well-structured narrative. **But the main benefit goes to the writer.** By writing long-form prose instead of bullet points, by adding data and connecting ideas, we’re forced to *think deeply and resolve inconsistencies*. We have to *focus on the single thread* that ties everything together. We need to *remove redundant details* (to fit the page limits). There is no way to write a six-page narrative and not come away with clear(er) thinking.

And even if the document is lost, the research and thinking has already been done. The process and outcomes of the thinking are often more important than the document.

> “Reports are more a medium of self-discipline than a way to communicate information. Writing the report is important; reading it often is not.” – Andy Grove

I fully agree with this and advocate the practice of writing [one-pagers](/writing/what-i-do-before-a-data-science-project-to-ensure-success/#first-draw-the-map-to-the-destination-one-pager). (In my previous teams, it was a must before starting on a project.) The process helps to clarify the intent, desired outcome, deliverable, and constraints. Such practices are also common in Amazon, such as the [working backwards](https://www.quora.com/What-is-Amazons-approach-to-product-development-and-product-management/) process and the [press release](https://www.businessinsider.com/heres-the-surprising-way-amazon-decides-what-new-enterprise-products-to-work-on-next-2015-3) document.

Also, writing is a short cut to **socializing ideas and getting feedback**. Before starting on (costly) implementation, we can (cheaply) share written proposals to gather feedback. With feedback, our initial designs can be refactored at zero development cost. Sharing our designs—in written form—also ensures our eventual implementation meets the intent:

> “When you write your proposal, you have a way to understand if it’s interesting and useful for others. In contrast, you can write code for a very long time and still not know if it’s useful. Thus, writing the proposal is important to helping yourself and others understand if what you’re building is actually solving the problem.“ – Alexey Grigorev

The same documents we write to gain clarity can also be used to socialize our ideas. In Amazon, when asked about a project, it’s common to share the press release document (and the six-pager if it’s available). In other organizations, this could be in the form of a requirements doc, confluence page, or API specifications.

In addition, writing helps with **knowledge retention and transfer**. Our memory is leaky—we forget [as much as 90% of what we read within 7 days](/writing/reading-note-taking-writing/#note-taking). Writing is like saving knowledge to a database. And now, instead of asking us, people can access our knowledge via that database (i.e., writing)—this helps us save time:

> “When you have project documentation, it’s easy to onboard someone onto the project. Instead of having to sit with them to explain it, you can just direct them to the docs. Also, as the organization grows larger, it becomes difficult to transfer knowledge; this can lead to miscommunication. An effective way to prevent this is via writing good documentation” – Pratik Bhavsar

Alexey strongly advocates this too. By investing time in documenting the process, decisions, and outcomes, it’s much easier to revisit the project when we need to (a year later). He does this through a *project journal*:

> “I have a single document for everything about the project. How it started, what the goal is, every decision made. This allows you to go back in time and step through the problems and understand the decisions we made (especially if things didn’t go well). Eventually, it becomes very valuable and contains a lot of knowledge, though it also becomes lengthy. … If someone asks me about the project, well, here you go *< shares project journal >*” – Alexey Grigorev

I also suggest documenting outcomes of experiments that may have consumed hundreds, if not thousands, of compute hours. Here’s a simple automated approach via [`Jupyter`, `Papermill`, and `MLflow`](/writing/experimentation-workflow-with-jupyter-papermill-mlflow/).

## How can we help the team write better?

One way to improve writing quality by **raising the bar**. For example, David wrote a document on how to write design documents (very meta) that devs in Amazon refer. Pratik suggests that a great way to write well is to imitate good writing. Thus, we can point the team to examples of good documents that they can emulate. Or we can provide the team with templates, such as Amazon’s [press release outline](https://www.linkedin.com/pulse/working-backwards-press-release-template-example-ian-mcallister/).

Balancing between templates and autonomy

Templates are a great way to standardize how the team documents and shares knowledge. They streamline the writing process and ensure the resulting document is familiar to (internal) readers and thus easy to understand.

However, it can be difficult to balance between adhering to templates and allowing autonomy in structure and format. What works for one team may not necessarily work for another. For example, an engineering proposal will likely include sections for security, privacy, and infrastructure. On the other hand, a data science proposal will include sections for machine learning, experimentation plan, and model refresh procedure.

[Stripe balances standardization and autonomy](https://slab.com/blog/stripe-writing-culture/#know-when-to-standardize-and-when-to-give-autonomy) by having templates for high-level documents that would have a broader audience (i.e., organization-wide, multiple teams) or significant implications (e.g., quarterly reports). Amazon does the same with a suggested format for [working backwards and press releases](https://www.quora.com/What-is-Amazons-approach-to-product-development-and-product-management/answer/Ian-McAllister) but [no template for six-pagers](https://www.quora.com/What-is-the-template-for-the-6-page-memo-required-by-Jeff-Bezos-at-Amazon). This ensures widely circulated documents and standardized as easily parsed while giving teams autonomy over their internal documents.

In addition, we need to **provide sufficient time** to write.

> “The great memos are written and rewritten, shared with colleagues who are asked to improve the work, set aside for a couple of days, and then edited again with a fresh mind.” – Jeff Bezos

You just can’t churn out a great memo in a day. Jeff suggested that some memos might take a week to get right. Taking enough time can be more important than actual writing skills when it comes to such documents.

How do we write good technical documents? Here are some **great resources to start with**:

* [The process of writing documents at Amazon](https://blog.usejournal.com/writing-docs-at-amazon-e025808616bd), including having the right people in the room, checking your ego at the door, etc.
* [The why, what, and how of design documents](https://www.freecodecamp.org/news/how-to-write-a-good-software-design-document-66fcf019569c/), and the process around it.
* [A practical guide to writing technical specs](https://stackoverflow.blog/2020/04/06/a-practical-guide-to-writing-technical-specs/) with a very detailed template.

> Learning to write is much more important than learning to code.
>
> — Sahil (@shl) [May 3, 2020](https://twitter.com/shl/status/1256988523455893510?ref_src=twsrc%5Etfw)

## Deciding between writing & coding—a useful question

As we progress in our careers, it seems inevitable that we’ll write more documents than code. But as we’ve seen, writing documents is *also* high impact work. Given our limited time and energy, how do we choose between both?

Here’s a good question to ask ourselves: **“Which would have greater impact *right now*?”** If we need to understand and clarify the intent and context so we can start implementing, then writing a design doc will help most. If we’re struggling to meet an delivery deadline, then writing (and reviewing) code will help more.

> Writing documents is like writing code. Code is for machines; documents are for people.

Writing documents is hard. For some, harder than writing code. And relative to writing code, the impact of writing documents is not as immediately measurable. **But if it helps provide clarity, or save the team time, then it’s well worth the effort.** (If you know of ways to measure the impact of writing, I would love to [hear from you!](https://twitter.com/eugeneyan))

What advice do you have for tech professionals starting to write more? Share in the comments below.

> Why does writing become more important (than coding) as we gain seniority? How do we balance between both? How can we help the team write better?  
>   
> Here, I explore answers to these question with the help of some friends, including [@Al\_Grigor](https://twitter.com/Al_Grigor?ref_src=twsrc%5Etfw) & [@nlpguy\_](https://twitter.com/nlpguy_?ref_src=twsrc%5Etfw).<https://t.co/foqhU5A9Rx>
>
> — Eugene Yan (@eugeneyan) [October 7, 2020](https://twitter.com/eugeneyan/status/1313634645272002562?ref_src=twsrc%5Etfw)

**Thanks** to Yang Xinyi and [Drew Stegmaier](https://stegdrew.com/) for reading drafts of this. **Thanks** to [David Said](https://www.linkedin.com/in/david-said-martinez-3836a72b/), [Alexey Grigorev](https://twitter.com/Al_Grigor), [Pratik Bhavsar](https://twitter.com/nlpguy_), and [Grace Tang](https://www.linkedin.com/in/tsmgrace/) for making time to discuss on this topic.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Oct 2020). Is Writing as Important as Coding?. eugeneyan.com.
> https://eugeneyan.com/writing/writing-and-coding/.

or

```
@article{yan2020coding,
  title   = {Is Writing as Important as Coding?},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Oct},
  url     = {https://eugeneyan.com/writing/writing-and-coding/}
}
```

  
Share on:
