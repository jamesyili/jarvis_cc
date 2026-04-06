# OMSCS CS7646 (Machine Learning for Trading) Review and Tips

**Source:** https://eugeneyan.com//writing/omscs-cs7646-machine-learning-for-trading/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

> You might also be interested in this [OMSCS FAQ](/writing/georgia-tech-omscs-faq/) I wrote after graduation. Or view all OMSCS related writing here: [`omscs`](/tag/omscs).

The 2019 spring term ended a week ago and I’ve been procrastinating on how ML4T (and IHI) went. I’ve known all along that writing is DIFFICULT, but recently it seems significantly more so.

Perhaps its because I’ve noticed this site has been getting a lot more traffic recently. This includes having Prof Thad Starner commenting on my post for his course on [Artificial Intelligence](/writing/omscs-cs6601-artificial-intelligence/). This has increased my own expectations of my writing, making it harder for me to start putting pen to paper.

To tackle this, I looked to the stoicism techniques (i) to decide if something is within my locus of control, and (ii) to internalise my goals. Is it within my control how much traffic my writing receives? No. Is it within my control how much feedback I get on my writing? No.

Instead, what is within my control is writing in a simple and concise to share my views on the classes, so others can learn from them and be better prepared when they take their own classes. This has been the goal from the start—I guess I lost track or forgot about it over time, and got distracted by other metrics.

With that preamble, lets dive into how the ML4T course went.

## Why take the course?

My personal interest in data science and machine learning is sequential data, especially on people and behaviour. I believe sequential data will help us understand people better as it includes the time dimension.

In my past roles in human resource and e-commerce, I worked with sequential data to identify the best notifications to send a person. For example, you would suggest a phone case after a person buys a phone, but not a phone after a person buys a phone case. Similarly, in my current role in healthcare, a great way to model a patient’s medical journey and health is via sequential models (e.g., RNNs, GRUs, transformers, etc). I’ve found that this achieves superior results in predicting hospital admissions and/or disease diagnosis with minimal feature engineering.

Thus, when I heard about the ML4t course, I was excited to take it to learn more about sequential modelling—stock market data is full of sequences, especially when technical analysis was concerned. In addition, framing the problem and data from machine and reinforcement learning should provide useful lessons that can be applied in other datasets as well (e.g., healthcare).

I also wanted to learn more about the financial markets, as well as improve my general knowledge on trading and investment (though mostly the latter). I have some basic understanding, mostly self-learnt through books and have applied it with some success. Nonetheless, I felt that some fundamental, technical knowledge was missing, and I was looking to this course to supplement it. Learning how to invest is a life skill, as essential as learning how to use a computer, and is one of the key pillars to retiring comfortably.

Lastly, I’ve heard good reviews about the course from others who have taken it. On OMSCentral, it has an average rating of 4.3 / 5 and an average difficulty of 2.5 / 5. The average number of hours a week is about 10 - 11. This makes it great for pairing with another course (IHI, which will be covered in another post).

## What’s the class like?

Much of the learning comes from the eight assignments—an average of one assignment every two weeks. These assignments required some amount of coding in Python, with the code to be submitted and (auto) graded. Some of the bigger assignments also involved writing a report on the results from the experiments, often involving visualisations and tables. A basic understanding of object-oriented programming is useful, especially for bigger projects that involved multiple classes.

Grading scripts were provided for most of these assignments. These functioned as test cases, providing immediate feedback as the code was developed. Nonetheless, some grading / test cases were kept aside, for use in the actual grading, though this was usually less that 10 - 20% of the total points for the coding portion.

In terms of effort, some assignments took less than a few hours, while a few took 10 - 20 hours, especially the later projects which involved framing the market trade data into a machine learning problem. This includes development time, creating visualisations, and writing the report (usually 2-3 pages long).

Here are the eight projects we had in Spring 2019:

* Project 1, Martingale: Analyze the “Martingale” roulette betting approach for unlimited vs. limited loss
* Project 2, Optimize Something: Use optimization to find the allocations for an optimal portfolio
* Project 3, Assess Learners: Implement decision tree learner, random tree learner, and bag learner (i.e., ensemble)
* Project 4, Defeat Learners: Create data sets better suited for Linear Regression vs. Decision Trees, and vice versa
* Project 5, Marketsim: Implement code to take data of trades and return portfolio values and metrics given a start value, commission and impact
* Project 6, Manual Strategy: Create a simple manual strategy with higher returns than benchmark (to be compared with a machine learner in final assignment)
* Project 7, Q Learning Robot: Implement a Q-Learner with Dyna Q framed by a simple robot navigation problem
* Project 8, Strategy Learner: Frame the trading problem using a learning approach from one of the prior assignments (Random Tree, Q-Learner or Optimization).

There were also two exams, one mid-term and one final. The final was not cumulative and did not cover topics already covered in the mid-term. Each exam had 30 multiple choice questions, to be completed in 35 min. Revise the lectures and you’ll be fine.

Someone compiled transcripts of all the lectures together with essential screen shots, available [here](https://drive.google.com/drive/folders/1n8ostcGENIVTxbxf-ZNThRcM2keM3nAz). I found revising this to be much faster, as reading is faster than listening to video. Make sure you’ve at least viewed the videos once though, or you might be lost on some of the more technical aspects, especially in the later half of the course.

In addition, you can also revise past year exam questions. Here are two comprehensive questions banks that should help tremendously. You’ll probably not need to go through all of the questions—they number in the hundreds—and still be fine. Nonetheless, being the “A-sian” I am, I went through all of them. On hindsight, it was probably overkill.

* Question bank for midterm [here](https://kirkbrunson.github.io/ml4t-guide/)
* Question bank for finals [here](https://quizlet.com/348217964/ml4t-questions-4-rating-3-votes-flash-cards/)

With regard to lectures, I found them to be generally engaging and well done, with high production quality. The class is organised into three mini courses: (i) General Python, Numpy, Pandas, (ii) Finance, (iii) Machine Learning (in Finance).

For those who already have some python background, the first mini-course will be a breeze and a good revision for Numpy. Some material in the finance mini-course was new to me, though not much. I was hoping to go into more detail on fundamental analysis. The mini-course mainly focused on technical analysis—as this is what machine learning is applied on—though in lesser detailed that I hoped. The last mini-course on machine learning was fairly basic, covering decision trees and Q-learning, and how to apply machine learning to a problem. For those who’ve already taken [Artificial Intelligence](/writing/omscs-cs6601-artificial-intelligence/) and [Reinforcement Learning](/writing/omscs-cs7642-reinforcement-learning/), the learning from those course will help.

On the logistics, the Piazza forum and Slack channels were well supported by TAs, largely thanks to TA Tala. Prof David Joyner took over the class in Spring 2019 after [JP Morgan poached Prof Tucker Balch](https://news.efinancialcareers.com/uk-en/3000034/jp-morgan-poaches-machine-learning-guru-tucker-balch)—so we know that what is taught can really be applied. You’ll receive Piazza notifications on what to look out for each week, helping you keep on top of the multiple course materials, canvas notifications, piazza notifications, and slack notifications—make sure you read the weekly updates carefully.

With regard to assignment and exam grading, it was done relatively quickly, significantly faster than some of the other classes I’ve taken. Most of the grading appears to be automated, and (part of) the grading scripts are shared with students as well. The grading pipeline is largely as follows:

* Test if your code can run properly on the provided testing (buffet) servers
* Upload completed code to canvas
* A few days after the deadline, a batch job is run to pull the code and run them using the automated grading scripts on the servers
* Results are automatically reflected on canvas, include the automated feedback and error logs

For more details, head over to the course website [here](http://quantsoftware.gatech.edu/Machine_Learning_for_Trading_Course).

## What did I learn in this course?

I learnt a lot about how the stock market functions and about stock market data, as well as both perspectives of profiting from it (i.e., technical and fundamental analysis). The class also covered the different financial instruments, such as options and how you can buy and write them, and the associated risks (i.e., unlimited loss). I had some basic understanding about various financial instruments from my own learning, but less about how they transact on the exchange—the class helped to supplement my knowledge.

Specific to technical analysis, I learnt how people try to distill stock market movements (in price and volume) into technical indicators that can be traded upon automatically (e.g., Bollinger Bands, Moving Average Convergence Divergence, etc.). I’m still not fully convinced it works, but ¯(ツ)/¯. It was especially fun trying to frame stock market trading into a supervised learning problem for machine learning. What should the target be? Next day’s price (regression)? Whether or not to buy or sell (classification)? These are the key questions in machine learning that are seldom covered in most machine learning classes.

## What’s next?

Well, I’m definitely NOT going to put my money on my self-developed trading algorithms, especially after seeing how they perform on the out-of-sample testing set. Nevertheless, the class was a good refresher on what I previously self-learnt on fundamental analysis and portfolio allocation—I will try to apply this to my own investment portfolio.

In addition, some of the techniques covered in sequential modelling are useful, and I will try applying them to the sequential healthcare data at work. Hope to share some positive results soon.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (May 2019). OMSCS CS7646 (Machine Learning for Trading) Review and Tips. eugeneyan.com.
> https://eugeneyan.com/writing/omscs-cs7646-machine-learning-for-trading/.

or

```
@article{yan2019trading,
  title   = {OMSCS CS7646 (Machine Learning for Trading) Review and Tips},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2019},
  month   = {May},
  url     = {https://eugeneyan.com/writing/omscs-cs7646-machine-learning-for-trading/}
}
```

  
Share on:
