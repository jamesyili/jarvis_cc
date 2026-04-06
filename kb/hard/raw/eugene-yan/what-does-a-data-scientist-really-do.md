# What does a Data Scientist really do?

**Source:** https://eugeneyan.com//writing/what-does-a-data-scientist-really-do/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

As a data scientist, I sometimes get approached by others on questions related to data science. This could be while at work, or at the meetups I organise and attend, or questions on my site or linkedIn. Through these interactions, I realised there is significant misunderstanding about data science. Misunderstandings arise around the skills needed to practice data science, as well as what data scientists actually do.

## Perception of what is needed and done

Many people are of the perception that deep technical and programming abilities, olympiad level math skills, and a PhD are the minimum requirements, and that having such skills and education qualifications will guarantee success in the field. This is slightly unrealistic and misleading, and does not help to mitigate the issue of scarce data science talent, such as those listed in [The New York Times](https://www.nytimes.com/2017/10/22/technology/artificial-intelligence-experts-salaries.html) and [Bloomberg](https://www.bloomberg.com/news/articles/2018-02-07/just-how-shallow-is-the-artificial-intelligence-talent-pool).

Similarly, based on my interactions with people, as well as comments online, many perceive that a data scientist’s main job is machine learning, or researching the latest neural network architectures—essentially, Kaggle as a full time job. However, machine learning is just a slice of what data scientists actually do (personally, I find it constitutes < 20% of my day to day work).

## How do these perceptions come about?

One hypothesis is the statical fallacy of availability. For the average population, they would probably know about data scientists based on what they’ve seen/heard on the news and articles, or perhaps a course or two on Coursera.

What’s likely to be the background of these data scientists? If it’s from this [Forbes article](https://www.forbes.com/sites/nicolemartin1/2019/03/27/turing-award-and-1-million-given-to-3-ai-pioneers/#66295b2a4784) on the recent Turing Award for contributions in AI, you’ll find three very distinguished gentlemen who have amazing publishing records and introduced the world to neural networks, backpropogation, CNNs, and RNNs.

Or perhaps you read the recent [Deepmind post](https://deepmind.com/blog/article/alphastar-mastering-real-time-strategy-game-starcraft-ii) about how neural networks and reinforcement learning achieved human expert level performance, and found that the team was largely comprised of PhDs. If it’s from a course, the person is likely to have a PhD, and went through deep mathematical proofs on machine learning techniques. Thus, based on what you can think of, or what is available in memory, many people tend to have a skewed perception on what background a data scientist should have.

The same goes for what data scientists actually do. Most of the sexy headlines on data science involve using machine learning to solve (currently) unsolvable problems, everything from research-based (computer games) to very much applied (self-driving cars). In addition, given that the majority of data science courses are on machine learning, its no wonder that the statistical fallacy of availability would skew people towards thinking that machine learning is the be all end all.

## Such perceptions are (mostly) incorrect

Firstly, yes, there are researchers in labs who spend 80% of their time training tens of the same neural network architecture and hope for convergence on some of them, publish breakthrough research papers, and build cool applications that involve the latest and greatest. Nonetheless, they probably constitute < 1% of the overall data science community.

For most data scientists, while machine learning is a critical aspect of their work, it is only part of it. In addition, the perceived requirement for deep technical and math skills, as well as a PhD, to be effective in data science, is naive.

In my years of experience, first as a data scientist, then as a data science lead, I’ve had the opportunity to hire and assess many data scientists, and observed first hand what is needed for effective data science. In addition, I’ve also reached out and interviewed many experts, people who are Chief Data Officers, Chief Data Scientists, CTOs, and Heads of Data Science—they too, disagree with the flawed public perception.

## So what do Data Scientists actually do?

To provide some context, I’ll reference the [commonly used distinction](https://www.quora.com/What-is-data-science/answer/Michael-Hochster) between Type A and Type B data scientists.

* Type A: The A stands for Analysis. Such data scientists are primarily concerned with making sense of data, or working with it in a fairly static way. They are very similar to a statistician.
* Type B: The B stands for Building. They share some statistical background with Type A, but are also strong programmers and may be trained software engineers. They are mostly interested in serving data “in production”.

The following is tilted towards Type B Data Scientists, due to my personal background, the teams I’ve built, and the objectives I’ve had to achieve. For Type B, the desired outcomes of most data science efforts is a data product that delivers value, either via providing insight for decisions, or automated decision making.

The journey towards putting a data product into production may involve many steps, which include:

**Understanding the problem and context, and framing problem statement (framing)**

* Understanding the problem to solve, and the available data
* Framing the task and scope
* Identifying constraints (data refresh rate, data security, etc.)
* Identifying desired outcomes (including optimisation metrics)
* Identifying ethical risks (e.g., how would predictions be misused, either deliberately or accidentally)

**Data acquisition, exploration, and preparation (infra)**

* Laying the foundation for robust analytics
* Understanding how to collect more data if needed
* Understanding the data, including errors in the data and how to fix them
* Preparing the data, including filling nulls, handling outliers, formatting, etc.
* Figuring out how to join data across multiple different sources, ensuring that the process is valid and correct
* Visualizing the data and understanding underlying signals in the data

**Building frameworks (e.g., validation) and pipelines (e.g., data preparation and ML experiments)**

* Building a proper validation framework (e.g., can we use random shuffle k-fold, or should a time-based split be used)
* Building data processing pipelines to prepare data, sometimes involving big data
* Performing statistical analysis to understand the relationships between variables in the data
* Building feature processing pipelines to convert prepared data into ML ready format (e.g., all features should be numerics)
* Building ML pipelines to allow you to run parallel experiments, record results, visualise them, etc.
* Pipelines should be built such that they allow for easily change in data prep or feature engineering approaches via config files, instead of being hardcoded
* The same goes for ML experiment pipelines—they should work for all model types, params, etc.

**Running experiments, monitoring, and analysing (testing)**

* Assessing multiple broad approaches before deciding on a model to use (e.g., trees, regression, svms, neural networks)
* Deciding how to model the data (e.g., for forecasting, should it be in batch, with hand crafted features, or take in sequential data)
* Running experiments with numerous hyperparams to understand how model learns on the data
* Running experiments with other “tricks” (e.g., data augmentation, data weighting, different objective functions, etc)
* Analyse the model performance (e.g., learning curves, error analysis)
* Assess for underfitting/overfitting
* Running online experiments, etc.

**Putting the data product into production (data products)**

* Ensuring data and machine learning pipelines are scalable and robust
* Building personalised data products
* Creating APIs for machine learning models
* Determining how to schedule your pipelines
* Monitoring and maintaining data product and models over time
* Monitoring input data, and model validation results
* Communicating results to the organization
* Convincing decision makers of their results
* Rollback planning for incorrect models
* Ethics of how the data is being use

As you may have noticed, machine learning makes up a (small) portion of what data scientists actually do. While not every step is necessary in every project, and not every data scientists will do every step, most aspects will be de facto in many data science projects/products.

## So what abilities do Data Scientists need?

Given the above, we get a sense that a strong understanding of machine learning alone is insufficient in the data science process. Having additional deep technical, math, and programming skills are useful, but don’t encompass the full picture.

What exactly is needed then? In my quest to understand this, I interviewed many data science experts and leaders, with questions such as:

* “What do you think makes a rockstar data scientist?”
* “What do the best data scientists on your team do? What are they like?”
* “How do you measure success in data science?

The overall answer to the questions was this—the best data scientists work with data to “deliver measurable value”.

For me, this was completely out of the left field. I had imagined the answer to be based on math, research, programming, cutting edge techniques, and developing new algorithms. While the answers from the experts/mentors were simple, it was not something that could be replicated in a straightforward manner. If it were programming and technical abilities, I could just practise more and get better at it. If it were math and algorithms, I would study more and practise. However, this was not the case.

How does one practise “using data to deliver measurable value”?

Thus, I began on my next journey to understand what was required. I’ll share what I’ve found in a later post.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Apr 2019). What does a Data Scientist really do?. eugeneyan.com.
> https://eugeneyan.com/writing/what-does-a-data-scientist-really-do/.

or

```
@article{yan2019scientist,
  title   = {What does a Data Scientist really do?},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2019},
  month   = {Apr},
  url     = {https://eugeneyan.com/writing/what-does-a-data-scientist-really-do/}
}
```

  
Share on:
