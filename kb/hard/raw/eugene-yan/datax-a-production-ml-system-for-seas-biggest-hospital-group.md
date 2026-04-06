# DATAx - A Production ML system for SEA's Biggest Hospital Group

**Source:** https://eugeneyan.com//speaking/machine-learning-largest-hospital-group-talk/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I was humbled to be invited by [DATAx](https://www.theinnovationenterprise.com/summits/datax-singapore-2019/overview) to share at their conference. They were looking for a hands-on Applied Scientist to share about how data science and machine learning could be applied in healthcare and I was happy to help.

For this, I shared the case study of how uCare.ai helped develop a machine learning system for Parkway Pantai Group (Southeast Asia’s largest healthcare group) that estimates a patient’s total bill at the point of pre-admission.

Doing so provides greater transparency to patients, helping to reduce potential payment challenges at point of discharge. It also benefits providers where the improved transparency helps with patient experience and retention. Lastly, this is also a requirement by Singapore’s Ministry of Health.

## From the event [page](https://www.theinnovationenterprise.com/summits/datax-singapore-2019/agenda):

Healthcare expenditure is set to rise over the coming years. Cost will undoubtedly influence patients’ decision-making when it comes to diagnosis and treatment.

For healthcare providers, providing up-front cost estimates improves patient experience, making patients more willing to return (if required) in the future. For patients, having accurate pre-admission estimates allow for informed decisions and adequate preparation, reducing payment challenges after treatment. Ultimately, this case is a first step towards (i) standardization of healthcare cost estimation and (ii) price transparency to build trust between healthcare providers, payers, and patients.

In this talk, UCARE.AI will share about how we developed an automated and scalable system to predict hospitalization costs at pre-admission (e.g., without rich data, like measurements, final outcomes, etc.) We’ll go through our (i) methodology, (ii) useful features, (iii) tech stack, (iv) challenges and how we resolved them.

Prerequisite knowledge

* Basic understanding of hospitals and processes (i.e., visited one before)
* Basic understanding of DS projects end-to-end, from planning to delivery
* Basic understanding of cloud, architecture, and deployment models

What you’ll learn

* How to use data to understand patient conditions and predict costs
* How we collaborated with Parkway to plan, develop, and deploy a production-grade machine learning system
* How we overcame challenges, plus tips and tricks

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

## Slides

   

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Mar 2019). DATAx - A Production ML system for SEA's Biggest Hospital Group. eugeneyan.com.
> https://eugeneyan.com/speaking/machine-learning-largest-hospital-group-talk/.

or

```
@article{yan2019hospital,
  title   = {DATAx - A Production ML system for SEA's Biggest Hospital Group},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2019},
  month   = {Mar},
  url     = {https://eugeneyan.com/speaking/machine-learning-largest-hospital-group-talk/}
}
```

  
Share on:
