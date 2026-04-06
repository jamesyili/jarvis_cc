# DataScience SG x ODSC Meetup - Applying ML to Healthcare

**Source:** https://eugeneyan.com//speaking/machine-learning-in-production-for-healthcare-talk/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

Having been in a healthtech startup for nearly a year and a half, it was long overdue for me to do a sharing at a meetup. I had previously shared on this at the DataX Conference in Singapore and wanted to share it at a meetup where anyone could attend.

## What’s the talk about?

The talk covers the architecture and end-to-end process that we took to build the machine learning system that is currently deployed in Southeast Asia’s largest hospital group (Parkway Pantai).

For this, I shared the case study of how uCare.ai helped develop a machine learning system for Parkway Pantai Group (Southeast Asia’s largest healthcare group) that estimates a patient’s total bill at the point of pre-admission.

Doing so provides greater transparency to patients, helping to reduce potential payment challenges at point of discharge. It also benefits providers where the improved transparency helps with patient experience and retention. Lastly, this is also a requirement by Singapore’s Ministry of Health.

## Intent of the talk

For the talk, I wanted to share about how we were able to improve on the existing system that Parkway had, reducing the prediction error by half. The talk went into the nitty gritty details that included the overall architecture, how the code is organized, as well as details steps that included:

* Data validation and ingestion
* Data preparation
* Feature engineering
* Model validation before deployment
* Machine learning
* Deployment

## Outcomes

Overall, the system reduced mean absolute error by 55% and root mean squared error by 60%. It also reduced the percentage of underestimates (a key intent was to bias towards overestimation to better manage patient expectations).

Rollout was easy and invisible to front-line users—the front-end remained the same while the backend was updated to call our API—who continued using an interface familiar to them.

Since the rollout, hospital administrators have indicated that there have been virtually zero complaints from staff and patients, a big improvement from the previous system.

## Key Takeaways

There were a couple of key takeaways that I emphasized to the audience.

Firstly, building useful data products is a team effort. Looking at the architecture diagram above, you can see that data science is only part of it. Data engineers helped with the data encryption, transportation, and ETL. DevOps helped with taking the packaged models (e.g., pickle files, docker images) and deploying it. Infra helped with setting up the necessary cloud requirements (e.g., storage, compute, networks).

Given the above, it should be clear that machine learning made up only a small percentage of the effort, approximately ~20%. This is the opposite from what many laymen, academics, or people getting started in data science think—that machine learning is 80%. I hoped that the talk showed that the methodology (i.e., how to frame the problem for machine learning) and proper engineering (i.e., for deployment and operational maintenance) is more important instead.

## Conclusion

From a technical perspective, a common failure I see in start-ups (and even some medium-sized enterprises) is to focus too much on applying machine learning on some batch data, usually CSVs, to achieve some (artificially) strong result that is likely overfitted and not replicable in production.

Kaggle is a great example of this, where winning solutions comprise of complex ensembles that take days to train. I’m not saying that Kaggle is bad—it’s a great place to explore different solutions with clean data sets on different problem areas. Nonetheless, it’s quite divorced from the reality of production machine learning systems.

I hope that the talk helped provide greater understanding on the process of developing production-grade machine learning systems, and that organizations in Southeast Asia will be more effective at it.

Here’s the slides for those who are interested.

 
  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Oct 2019). DataScience SG x ODSC Meetup - Applying ML to Healthcare. eugeneyan.com.
> https://eugeneyan.com/speaking/machine-learning-in-production-for-healthcare-talk/.

or

```
@article{yan2019healthtech,
  title   = {DataScience SG x ODSC Meetup - Applying ML to Healthcare},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2019},
  month   = {Oct},
  url     = {https://eugeneyan.com/speaking/machine-learning-in-production-for-healthcare-talk/}
}
```

  
Share on:
