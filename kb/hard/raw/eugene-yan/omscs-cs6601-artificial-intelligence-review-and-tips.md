# OMSCS CS6601 (Artificial Intelligence) Review and Tips

**Source:** https://eugeneyan.com//writing/omscs-cs6601-artificial-intelligence/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

> You might also be interested in this [OMSCS FAQ](/writing/georgia-tech-omscs-faq/) I wrote after graduation. Or view all OMSCS related writing here: [`omscs`](/tag/omscs).

Happy holidays! Have just completed the exceptionally difficult and rewarding course on artificial intelligence, just as my new role involved putting a healthcare data product into production (press release [here](https://sbr.com.sg/healthcare/more-news/parkway-pantai-and-ucareai-unveils-ai-powered-predictive-hospital-bill-estimati)). The timing could not have been better. The combination of both led to late nights (due to work) and weekends completely at home (due to study).

## Why take this course?

I was curious about how artificial intelligence would be defined in a formal education syllabus. In my line of work, the term “Artificial Intelligence” is greatly overhyped, with snake oil salesmen painting pictures of machines that learn on their own, even without any new data, sometimes, without data at all. There are also plenty of online courses on “How to do AI in 3 hours” (okay maybe I’m exaggerating a bit, it’s How to do AI in 5 hours).

Against this context, I was interested to know how a top CS and Engineering college taught AI. To my surprise, it included topics such as adversarial search (i.e., game playing), search, constraint satisfaction, logic, optimzation, Bayes networks, just to name a few. This increased my excitement in learning about the fundamentals of using math and logic to solve difficult problems.

In addition, the course had a very good reviews (4.2 / 5, one of the highest), with a difficulty of 4.3 / 5, and average workload of 23 hours a week. Based on these three metrics, AI was rated better, more difficult, and requiring more time than [Machine Learning](/writing/omscs-cs7641-machine-learning/), [Reinforcement Learning](/writing/omscs-cs7642-reinforcement-learning/), and [Computer Vision](/writing/omscs-cs6476-computer-vision/)—challenge accepted! It was one hell of a ride, and I learnt a lot. However, if I had to go back in time, I’m not sure if I would want to put myself through it again.

What’s the course like?
The course is pretty close to the real deal on AI education. Readings are based on the quintessential AI textbook [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), co-authored by Stuart Russell and [Peter Norvig](http://norvig.com/). The latter is a former Google Search Director who also guest lectures on Search and Bayes Nets. Another guest lecturer is [Sebastian Thrun](https://en.wikipedia.org/wiki/Sebastian_Thrun), founder of Udacity and Google X’s self-driving car program. The main lecturer, [Thad Starner](https://en.wikipedia.org/wiki/Thad_Starner), is an entrance examiner for the AI PhD program and draws from his industry experience at Google (where he led the Google Glass development) when structuring assignments.

With regard to lectures, I found them to be somewhat superficial and lacking. Topics were introduced at a very high level. Students are expected to follow up with the textbook for more details—this was absolutely required for both the assignments and the exams. There was a lot of self-learning, and learning from peers and TAs on both the Slack channel and Piazza.

On assignments, there were six assignments that were each two - three weeks long. The best five contributed a total of 60% to the total grade. These involved implementing some popular and fundamental AI algorithms from scratch, including:

* Adversarial search / game playing (i.e., minimax, alpha-beta, iterative deepening, killer move (detection), etc)
* Search (i.e., uniform cost search (UCS), A-star search (A*), bi-directional UCS/A*, tri-directional UCS/A\*)
* Bayesian networks (i.e., probabilistic modelling, Gibbs sampling, Metropolis-Hastings sampling)
* Decision Trees (i.e., splitting, random forests, boosting, validation, etc.)
* Expectation maximisation (i.e., k-means, gaussian mixture models)
* Hidden Markov Models (i.e., Viterbi trellis, adjusting for noise)

These assignments also included opportunities for extra credit. I found some of these assignments a lot of fun, and went beyond the class material to implement better algorithms (i.e., various evaluation functions for adversarial search, more efficient splitting techniques for decision trees, etc.)

Grading the assignments involved automated testing via Bonnie (Udacity’s code testing server) which provides quick feedback on your algorithm and code submitted. However, some of the error messages were vague with little reason provided for the failures. Also, there were some assignments which allowed limited submissions (e.g., 6 submissions in total) which made everyone somewhat nervous.

With regard to the exams—they were killer. The midterm and finals were 34 and 47 pages respectively, with seven days to complete them. Students were only allowed to refer to the lectures, book, and Piazza. I felt that these were structured with the intent of getting students to learn the material better while doing the exam, and less of a strict evaluation—indeed, I learnt a lot of extra material from doing the exams.

However, there were a few downsides. A new exam seem to be developed every term, and thus they were less polished than expected. There were numerous clarifications for each exam, even up till the last few days of the exam. Some of these clarifications were “breaking”, with students having to revisit and re-do some questions.

The exams mostly involved (somewhat tedious) calculation (by hand), through which you learn how the algorithms work and gain practice, as well as demonstrate your understanding and ability to apply and implement. There were questions where you spent three-four hours working on a two point sub-question (out of 100), while an entire question (10-12 points) would take half a day. However, small mistakes can cost you greatly, though they do provide partial credit (pro-tip: attach all methodology for a chance of getting partial credit).

I had to take a day’s vacation for the mid-term and finals each. Coupled with the weekend, this gave me about 30-40 hours for each exam, and I was throughly burnt out after each one. I thought I prepared throughly for each exam, but there were always a few questions out of left field that required me to pore over an obscure section of the textbook and learn on the fly. Overall, the midterms and final had a weightage of 15% and 20% respectively. There was a separate plagiarism quiz that had a weightage of 5%.

The forums and TAs were excellent. The TAs responded very quickly on forums with regard to clarifications on assignments and exams. In addition, the office hours held by the TAs were immensely helpful for the assignments and lectures—I highly recommend attending them. Thad also held office hours to go through the mid-terms and finals solutions, and it was fun watching him trying to do the paper live.

## Tips on how to manage the workload

Due to my heavy workload (in my startup), I could only start on assignments / exams about three - five days after they were released. On hindsight, this was helpful as it allowed the “bugs” to be worked out and the initial discussion to be seeded on Piazza and Slack. I gained from these and stood on the shoulders of giants before me.

Nonetheless, I still struggled significantly, especially for the first two assignment which took anywhere between 20 - 40 hours for most people. You have two weekends for each assignment—you should definitely start on the first weekend! Many are right that the first and second assignments were the hardest. If you manage to get past them, you’re halfway there. I found the assignments on decision trees and expectation maximisation to be somewhat easier, though HMMs were unfamiliar and required more time.

## What did I learnt?

The course provided a good overview of the fundamental AI techniques such as search, Bayes networks, HMMs, etc. These are seldom covered in other online courses available which tend to mostly focus on machine learning. There were also other interesting topics covered such as constraint satisfaction, logic and planning, and optimisation which I found interesting and useful in expanding my knowledge in algorithms.

In addition, the assignments taught a lot about translating algorithms from equations into working code. This seemed to be a recurring theme throughout a few other courses (i.e., [ML](/writing/omscs-cs7641-machine-learning/), [RL](/writing/omscs-cs7642-reinforcement-learning/), [CV](/writing/omscs-cs6476-computer-vision/)) and I was glad to have the additional practice.

## Kaggle challenge on decision trees

One assignment I particularly enjoyed was decision trees. I’m a big fan of decision trees for machine learning, given their effectiveness, speed, and robustness to overfitting and outliers. Thus, when the opportunity came to implement decision trees from scratch using only Numpy, I relished it.

This particular assignment also involved the opportunity for extra credit via a Kaggle competition on our self-implemented decision trees. In working through the assignment and extra credit, I took the time to go through the [XGBoost](https://arxiv.org/pdf/1603.02754.pdf) and [LightGBM](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf) papers, and adopted some of their techniques on my classifier.

As a result, I managed to clinch second place on the Kaggle challenge, something I’m especially proud of.

Went up 2 spots on the private leaderboard =)

## What’s next?

Next term, I plan to have a “break” (somewhat). Will be taking two of the more fun courses. [Machine Learning for Trading](https://omscs.gatech.edu/cs-7646-machine-learning-trading) involves learning about machine learning on sequential data, with lot of Numpy vectorization goodness. [Intro to Health Informatics](https://omscs.gatech.edu/cs-6440-intro-health-informatics) will hopefully provide more knowledge on the healthcare industry, as well as provide more practice on Java and Docker, which is also useful in my work.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Dec 2018). OMSCS CS6601 (Artificial Intelligence) Review and Tips. eugeneyan.com.
> https://eugeneyan.com/writing/omscs-cs6601-artificial-intelligence/.

or

```
@article{yan2018ai,
  title   = {OMSCS CS6601 (Artificial Intelligence) Review and Tips},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2018},
  month   = {Dec},
  url     = {https://eugeneyan.com/writing/omscs-cs6601-artificial-intelligence/}
}
```

  
Share on:
