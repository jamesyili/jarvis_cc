# Mailbag: Qns on the Intersection of Data Science and Business

**Source:** https://eugeneyan.com//writing/mailbag-ds-requirements/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

V writes (in response to this [post](/writing/what-i-do-before-a-data-science-project-to-ensure-success/)):

> 1. Is there a Business Requirement sign off in DS ? At what stage does it come?
> 2. In real life DS , do the customers want more inference or ‘black box’ methods?
> 3. Do you need to do web scraping to get additional supporting data, in addition to the customer data? I mean, in actual business scenario, how much of web scraping is done?
> 4. In which scenarios would the business separate out Data Engineering and Data Modelling? I assume that it isn’t cost-effective to separate the two roles but I may be wrong.
> 5. How do I know I have done my best in creating meaningful features and the model can not be improved further?

Hey V, these are great questions that get into the intersection of data science and business! I’m happy that you’re thinking about them.

1. Yes, there’s often a set of requirements. I work with business to determine the benefit they would like to see (e.g., automating a process 95% of the time, improving revenue, etc) and the deliverables (e.g., an product categorisation API, a recommender system). This is done early so we don’t invest effort in deliverables that don’t get used.
2. This depends. Initially, customers might want something more understandable (e.g., regression, decision trees), though the level of comfort varies across people. As we earn their trust, we get more free rein, including using more black box approaches.
3. I seldom do web scrapping. I find that the effort required to clean up that data is usually not worth it. If I’m scraping it, I would probably use a combination of Selenium and Python libraries (e.g., beautiful soup, spacy).
4. This usually depends on the size of the overall data team. As teams get larger and more mature, there’s usually a tendency to specialise—that’s when the roles are separated. Nonetheless, some teams (such as in StitchFix) deliberately keep have the generalist data scientist role so they do [end-to-end](/writing/end-to-end-data-science/).
5. It’s hard to say how good is “good enough”. It’s an unbounded problem, almost like asking how much fraud caught is good enough. What I usually try to do though is to time-box it—how much does the additional model performance from better features cost? And then I work from there. Alternatively, you could try to brute force it and perform operations between each feature (e.g., add, subtract, multiple, divide) though this might lead to overfitting. Feature statistics help too.

---

Have a question for me? Happy to answer concise questions via email on topics I know about.
More details in [How I Can Help](/how-i-can-help/).

  
Share on:
