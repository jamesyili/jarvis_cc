# Datacast Podcast - Effective Data Science with Eugene Yan

**Source:** https://eugeneyan.com//speaking/datacast-eugeneyan/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

[James](https://twitter.com/le_james94) invited me for a casual chat on his podcast where we chatted about my transition from a Psychology degree into data science, my experience, leadership, and my writing on agile, machine learning in production, culture, writing, and more. James was an excellent host and helped me to sound almost coherent.

## Highlights from our chat

### Why did you join Lazada?

Back in 2012 (when Lazada was founded), e-commerce was almost non-existent in South-East Asia. To buy anything, customers had to go to a brick-and-mortar shop—this is inconvenient for customers who lived in rural areas. And even if there was e-commerce, getting access to credit, logistics, and trustworthy sellers was difficult. How would you buy a product and pay for it? How would you return the product if you were not satisfied? Those were the problems the Lazada was trying to solve.

(Podcast 9:03)

### How did you join Lazada?

I took part in a Kaggle competition on product classification (with my friend [Weimin](https://weiminwang.blog)) and we did decently well. I then had a chance to [share about this](/speaking/dssg-kaggle-top-3-percent-talk/) at a meetup group co-founded by my friend [Kai Xin](http://thiakx.com).

It so happened that Lazada (being new) had this problem as well. They reached out and invited me for a chat. It was only a very small team (3 people) back then. But it sounded super fun and the people I met were super awesome and I was looking forward to learning from them. More details [here](/writing/psych-grad-to-data-science-lead/#serendipity).

(Podcast 10:18)

### Could you share about your journey from Psychology into Data Science?

My path is idiosyncratic and I was very lucky.

When making the transition out of government, I was lucky that IBM gave me the opportunity for my first data role. Then while at IBM, I was very lucky that the hiring manager for the global workforce analytics team was looking for someone with a Psychology background, and I was the only one in my cohort.

Then, when I shared about my Kaggle effort at a meetup, again it was pure luck that Lazada had that same problem. And they took a chance on me. Then, while in Lazada, I had great teammates and great bosses who gave me lots of opportunity to do crazy things, build things fast, and run experiments (and fail). Of course, they would never say it’s a failure—they would always say it’s a lesson.

If I had to distill it, it would be: (i) try a lot and you’ll get lucky on 5% of the shots, and (ii) look for people who give you opportunity to do great work and work with them.

(Podcast 19:14)

Relevant writing: [My Journey: From Psych Grad to Leading Data Science at Lazada](/writing/psych-grad-to-data-science-lead/)

### You speak at conferences/meetups. Could you share some tips with listeners?

If you’re going to share, share about something you *really* care about. When you share, you’re being a lighthouse; this attracts like-minded people to discuss it with you. Don’t try to ride the trend and share about what’s fashionable—it comes across clearly to the audience and they won’t be interested. It won’t be authentic.

Once you have a topic you care about, share as much as you can about it. Imagine yourself in the audience. What details would you care about? Metrics? Results? How customers gained? Methodology? Code (or Github repo)? I’m interested in all of the above, especially *what didn’t work*. Thus, I always try to share what didn’t work so I can save my audience experimentation time—these lessons on what didn’t work are very precious.

When you’re sharing, don’t make it a lecture; people will zone out after 5 - 10 minutes. What you want to do is to entertain and provide the bigger picture and context. Then you can go deep. And even then, don’t go too deep as your audience will lose track—they don’t have your expertise and knowledge. Try to empathize with your audience and keep it light. If they want to learn more, they can always reach out to you.

(Podcast 25:29)

Relevant writing: [How to Give a Kick-Ass Data Science Talk](/writing/how-to-give-a-kick-ass-data-science-talk/)

### What are some lessons from your transition from IC into leadership?

To be honest, I had a lot of help with these lessons. When the transition happened, I had a chat with my boss as well as his boss and asked them what they needed me to do.

As an IC, I was always trying to give it my 100% to build a new system to improve the customer experience. When I transitioned, I was taught that I cannot continue to get into the details and to be building it myself—it’s not scalable with a team of 10+. Instead, my role was to help everyone on the team be 20% (or even 100%) better. This way, across 10 people, the whole team is 200% (or 1,000%) better. My role was to scale the team, increase the output, put in the right practices, mentor and help the team grow.

So this is why I write a lot about agile and scrum. And why I advocate practices such as writing a one-pager to get alignment with stakeholders, and making sure they’ll use what you build. The worst thing is to spend 3 man-months building something they won’t use. (The customer doesn’t benefit and your team doesn’t have anything to show for it.) These were some of the practices I found valuable to my team and I would like to share them.

I also learned to conduct 1-on-1s. I asked everyone where they wanted to be in three years, and how we could build them up for that (even if it was not with the team or or). Once I know their interests, I can align it with what the org needs. A lot of what I was trying to do was to find a fit between the individual’s motivation and what the organization needs.

Overall, I wasn’t trying to optimize or build my own project anymore. Instead, I was trying to optimize for the entire team’s contribution to the organization: to help them grow, to put in the right processes for increased productivity, to teach them good habits and how to communicate with stakeholders better.

This also made it hard to quantify my contribution. I didn’t build this, I didn’t build that—it was all done by the team. But in the end, it all works out as you’re assessed based on your team’s output, how they’ve grown, their satisfaction, their retention, etc.

(Podcast 39:01)

Relevant writing: [My first 100 days as Data Science Lead](/writing/my-first-100-days-as-data-science-lead/)

### What were the challenges faced during the Alibaba acquisition of Lazada?

Some context: Lazada was Alibaba’s first acquisition outside of China. Thus, it was as much a learning experience for them as it was for us.

One challenge was the very tight timeline. We were given nine months to fully migrate onto their platform. This means going from AWS to AliCloud. And using their data model and schemas so that how a customer, product, and review is represented in Lazada is exactly the same across Alibaba. We also had to integrate their tracker so the logs were consistent, and use their tools for building a search engine and recommendation system.

Another key challenge was the language gap. The Alibaba team was mostly comprised of Mandarin speakers and very few of them could speak English. And on my team, half of them couldn’t understand Mandarin. Thus, there were people left out when the discussions were in Mandarin and I had to figure out how to manage this. And all the documentation was in Mandarin. We had to do Google Translate, and as part of that, 50% of the content would be lost or corrupted.

The work was also brutal—it was [996](https://en.wikipedia.org/wiki/996_working_hour_system). Sometimes, when we went to Hangzhou, it was seven days a week. And trips were two weeks at a time, with a week of rest in between. We had to do this because this was really the best way to work—in person with your Chinese counterpart and sitting close to them. Even now, I think it was the only way that we could have made the nine-month deadline.

(Podcast 44:20)

### Could you share about the keynote you gave OLX?

First, a bit of context about OLX Group. OLX is a global online marketplace that’s in 40+ countries. They are a platform for buying and selling services and goods, including cars, electronics, real estate, and jobs. They were rapidly expanding in Europe, sometimes through acquisitions, and were wondering how to continue to scale.

The main question they had for me was this: What do we centralise, and what do we decentralise? How do Alibaba and other players in South-East Asia scale their platforms?

In Alibaba’s case, all the infra, data models, platforms, and tooling was mostly the same. These packages were used by many teams across Alibaba’s different properties, and Lazada used them too. We also had standard guidelines. Now, if someone from Alibaba looked at Lazada’s data, they would be able to understand it very quickly. The way we represent customers and products is the same. Thus, this makes it very easy for people to share knowledge across organizations and iterate fast.

What was decentralised then? The local teams would work on aspects such as product and app design to ensure that it fits the tastes of South-East Asian consumers. Our data science team would also work on local campaigns as well as fraud, which was slightly different from fraud in China.

We also discussed the SuperApp and how it was blossoming all over China and South-East Asia. It’s really interesting to see bundling in China and South-East Asia, and the reverse in the US, where unbundling is happening. More [here](/speaking/olx-group-keynote-asia-tech-giants-talk/).

(Podcast 47:51)

Relevant writing: [OLX Prod Tech 2019 (Amsterdam) Keynote - Asia’s Tech Giants](/speaking/olx-group-keynote-asia-tech-giants-talk/)

### You come across as a DS x Agile evangelist. Could you share more about it?

I didn’t know I was an evangelist for data science and agile. It’s interesting how this came about. When I chat with friends in the industry, they are surprised that my teams adopt Scrum, and would ask how it worked and if it worked. So many people were asking the same questions that I decided to just write about it and put it online.

When I first started applying Scrum, I thought it was a very strict process of prioritisation, stand-ups, demos, retrospective, etc. But as I apply it more, I found a few key things that are most important (to me).

First, you’ll want to think about how to iterate fast. This is where the concept of time-boxing helps. For example, building a recommender could take anywhere from two months to two years. For me, and for our customers, I rather build something quickly (in two months) and test it with customers. It might not work, but then we iterate. This is preferable to spending two years on it and then finding out that it also doesn’t work.

Second, you’ll want to do prioritisation with the business. For example, you might want to build sexy stuff but if the business doesn’t want or need it, then it should not be a priority. It’s important to figure out what customers and the business need, and then how to solve those problems with data science. We shouldn’t try to build something sexy and just hope that people will like it. Amazon does this very well through our [Working Backwards](/writing/what-i-do-before-a-data-science-project-to-ensure-success/#first-draw-the-map-to-the-destination-one-pager) process, where we work backwards from the customer problem or opportunity.

Then, there are two practices that teams really enjoy. First, demos. Demos are super fun, and once you build the cadence, people work fast and are eager to share (discoveries, results, hacks) and get feedback.

People also enjoy retrospectives. Retrospectives are a great way to get feedback from the team in a neutral and objective environment. As a leader, you should pay attention to the items in the “What didn’t go well” bucket (e.g., needing three days to get data permissions) and solve them. If you can solve these problems, then you would increase the productivity of the entire team. After 10 - 20 retrospectives, you’ll look back at where you started and realized that the team has improved by so much.

(Podcast 57:44)

Relevant writing:

* [GovTech Conference - Data Science and Agile—can or not?](/speaking/data-science-and-agile-can-or-not-talk/)
* [Data Science and Agile (What works, and what doesn’t)](/writing/data-science-and-agile-what-works-and-what-doesnt/)
* [Data Science and Agile (Frameworks for effectiveness)](/writing/data-science-and-agile-frameworks-for-effectiveness/)
* [What I Love about Scrum for Data Science](/writing/what-i-love-about-scrum-for-data-science/)

### Could you share about your talk on “How Lazada Ranks Products”?

Firstly, something I haven’t mentioned before was that my target audience for this talk was not the conference attendees; it was the sellers on our platform. I wanted to share how we were ranking products so they could try to figure it out and work within the system to give the customer the best experience.

To build this system, we first developed a ranking model that assigns a score for each product on category and search pages. There’s nothing special about this; we used historical data on clicks, add-to-carts, and purchases to optimize a target. The target could be conversion, revenue, or customer acquisition and can be blended based on your business objective. But the features remained the same.

Also, Lazada was rapidly scaling and adding a lot of new sellers and products daily. Thus, I wanted to show sellers that we were working on features to help new sellers and products. We broke this down into a demand and supply problem and approached it from the demand side. We tried to understand unmet demand via what customers were searching for but not finding. With this, we knew what customers want but couldn’t find—these were the new products that we should rank higher. The results of this were amazing, but it was also because the problem was so bad to begin with. In e-commerce, the rich get richer; top-ranking products continue to rank well due to the virtuous cycle.

We also shared about how product quality affects ranking. I wanted to show sellers that we cared about product quality and trying to cheat customers won’t get them very far. Sellers can try to cheat customers by selling products that are very low price and very low quality. Or sellers could claim to ship in one day, but the actual shipping time might be a week or more. Or sellers could sell counterfeit goods. But, this will show up very quickly in the reviews and we’ll penalise products on that. We tried to be very transparent with sellers on what we ranked on so they would know how to improve their rank.

(Podcast 01:03:18)

Relevant writing: [Strata x Hadoop 2016 - How Lazada Ranks Products](/speaking/shared-about-my-work-in-lazada-at-strata-hadoop-singapore-2016-talk/)

### You wrote about building a product classifier app—could you share more?

I think it’s useful to have some context on why I did that. Back then, I had two to three years of experience as a data scientist in industry, and had done a *lot* of courses. But it still felt like something was missing. Thus, I was looking for more experience and found some data on Amazon products.

Through that project, I learnt a lot. First, the data was not in csv and could not fit into memory. I had to learn how to parse and covert this json data into csv via an out-of-memory approach. Then, I had to do data cleaning, feature engineering, and building a machine learning model—this was familiar to me.

Next, when I had to deploy this model online and make it publicly accessible, I realized there was so much I didn’t know about cloud and AWS. I also had little experience with GPUs and deep learning frameworks; back then, I was using Theano. I certainly didn’t learn about image classification in online courses. I also picked up transfer learning which was very new to me back then. Then, I also had to develop an API and a basic front-end, and deploy it on an EC2 instance.

The process was super rewarding. I had to learn so much and it helped me at work when I had to deploy machine learning systems on my own.

(Podcast 01:19:04)

Relevant writing:

* [Product Classification API Part 1: Data Acquisition](/writing/product-categorization-api-part-1-data-acquisition-and-formatting/)
* [Product Classification API Part 2: Data Preparation](/writing/product-categorization-api-part-2-data-preparation/)
* [Product Categorization API Part 3: Creating an API](/writing/product-categorization-api-part-3-creating-an-api/)
* [Image classification API is now live!](/writing/image-categorization-is-now-live/)
* [Image search is now live!](/writing/image-search-is-now-live/)

### Three people in data science whose work you admire?

[Andrej Karpathy](https://twitter.com/karpathy), Director of AI at Tesla. I admire how he’s able to apply his research in the real world. He also shares amazing content. I learnt a lot about early sequence and text models from his blog post [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). He also shared very practical advice in [A Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/).

[Jeremy Howard](https://twitter.com/jeremyphoward), he’s founded several companies, and together with [Rachel Thomas](https://twitter.com/math_rachel), they co-founded [fast.ai](https://www.fast.ai). They made deep learning more accessible to coders and hackers. I love their pedagogical approach of starting with the problem, showing that it can be solved, before going into the details. I believe this approach works better for many learners. Unfortunately, teachers often start with the theory before going into the application, and the learner isn’t clear on how they would use it.

[Hamel Husain](https://twitter.com/HamelHusain), Staff ML engineer at GitHub. He’s created a lot of ML tooling and content around MLOps. I think this is important for data scientists and not enough people pay attention to it. Recently, together with a couple others, he also put up some resources on how to do [MLOps on GitHub actions](https://mlops-github.com). Together with Jeremy Howard, they developed [FastPages](https://github.com/fastai/fastpages) to make it easier for people to publish blog posts from Jupyter Notebooks.

(Podcast: 01:24:42)

### Can you recommend a book for data scientists?

It’s difficult to just recommend one book. But I can tell you about the two books that I give to junior data scientists that join my team.

The first book is [Introduction to Statistical Learning](http://faculty.marshall.usc.edu/gareth-james/ISL/) (ISL). I know a lot of people cite [Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/) (ESL). I have both books, and I’m looking at them right now, and ISL is about half the size of ESL. I think ISL is a lot more digestible and doesn’t scare people off. It’s possible that if you take a month or two to study it, you can fully understand it. And once you grok it, you would have a great perspective of machine learning from the statistical point of view. If you want something from the CS point of view, perhaps consider [Artificial Intelligence](http://aima.cs.berkeley.edu) by Peter Norvig.

The other book that I would highly recommend, and almost everyone I’ve given this book to loves it, is [The Pragmatic Programmer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer). This was the first amazing coding resource that made an impact on me. It talks about how to build systems incrementally, starting from the skeleton and getting it working end-to-end, before trying to fill it in. I’ve applied a lot about what I’ve learnt from this book to how I build machine learning systems.

(Podcast: 01:28:16)

### What’s the one thing that you would share with all data scientists?

I would share about this approach that works really well for me: When you’re building an ML application, first focus on how it will help people. Once you understand it, then work backwards from it. By doing it this way, what you build *will* be useful for customers and you’ll make a much bigger impact, likely 2 - 10x more. Start with the problem first, then work backwards from it.

(Podcast: 01:30:58)

> James was a great host and helped me to sound almost coherent 😂  
>   
> We discussed my transition from psychology into data science, work experience, leadership, agile, machine learning in production, culture, etc.  
>   
> If 90-min is too long, here's the highlights:<https://t.co/COUCGWd2zL> <https://t.co/RcEytgXek7>
>
> — Eugene Yan (@eugeneyan) [September 4, 2020](https://twitter.com/eugeneyan/status/1302030715744378881?ref_src=twsrc%5Etfw)

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Sep 2020). Datacast Podcast - Effective Data Science with Eugene Yan. eugeneyan.com.
> https://eugeneyan.com/speaking/datacast-eugeneyan/.

or

```
@article{yan2020datacast,
  title   = {Datacast Podcast - Effective Data Science with Eugene Yan},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Sep},
  url     = {https://eugeneyan.com/speaking/datacast-eugeneyan/}
}
```

  
Share on:
