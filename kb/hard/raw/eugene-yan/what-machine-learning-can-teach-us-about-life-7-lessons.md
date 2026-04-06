# What Machine Learning Can Teach Us About Life - 7 Lessons

**Source:** https://eugeneyan.com//writing/life-lessons-from-machine-learning/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

I think a lot about machine learning. And I think a lot about life. Sometimes, the channels mix and I find certain lessons from machine learning applicable to life.

Here are seven lessons. While I assume most readers are familiar with these machine learning concepts, I begin each lesson with a brief explanation.

## Data cleaning: Assess what you consume

We [clean data](https://en.wikipedia.org/wiki/Data_cleansing) so our downstream analysis or machine learning is correct. As Randy Au [shares](https://counting.substack.com/p/data-cleaning-is-analysis-not-grunt), data cleaning isn’t grunt work; it is *the* work.

We don’t use data without exploring and cleaning it. Similarly, we shouldn’t consume life’s inputs without assessing and filtering them.

Take food for example. How often do we reach for what’s widely available and easy to prepare? Until a few years ago, I was happily munching on a bowl of Sugary-Os cereal daily. Now that I’m more aware of my family’s history with diabetes, I’m more selective and pay greater attention to nutritional content. Also, as age catches up and my metabolism slows, I have to make a conscious effort to eat healthier and avoid junk food.

Sugar is *"good"* for you ([source](https://divinations.substack.com/p/oatly-the-new-coke))

It’s the same with content. News outlets and social media rank information based on virality and advertising dollars. “Empty calorie info-bites” that are easy to consume—but don’t enrich us—circulate faster. [Misinformation](https://twitter.com/realDonaldTrump/status/1328334945148952576) is rampant. Some content is in poor taste and downright toxic, and attempts to engage don’t end well. For sanity’s sake, just filter it out. Curate your news sources and who you follow on social media.

A final example, relationships. We all have people in our life that do more harm than good. They distract or discourage us from our productive habits. Some talk behind our backs and play manipulative games, despite our best efforts to make things work out. Letting go of them makes way for more productive relationships to blossom.

## Low vs. high signal data: Seek to disconfirm and update

In addition to filtering out the noise, we also want to deliberately find data that updates our decision boundary.

As we get disconfirming data, the decision boundary shifts (center) and becomes non-linear (right)

In the left image above, we start with two easily separable clusters and a linear decision boundary with a wide margin. (The circled points—one blue, two red—are the [support vectors](https://en.wikipedia.org/wiki/Support_vector_machine).) In the center image, with a single new data point, the decision boundary shifts greatly and the margin shrinks. On the right, as we get more data, we learn that a non-linear decision boundary (and a [soft margin](https://en.wikipedia.org/wiki/Support_vector_machine#Soft-margin)) works better.

In life, we should also consciously seek data that updates our assumptions, hypotheses, and decision boundaries. Kind of like the opposite of [confirmation bias](https://en.wikipedia.org/wiki/Confirmation_bias).

> True ignorance is not the absence of knowledge, but the refusal to acquire it. – Karl Popper

Take feedback for example. Getting positive feedback is akin to adding more data on the correct side of the decision boundary—it’s always appreciated but doesn’t help much with improvement. I’m more interested in receiving negative feedback so I can update my life algorithm and grow.

## Explore-Exploit: Balance for greater long-term reward

In reinforcement learning, we face the [exploration-exploitation](https://www.davidsilver.uk/wp-content/uploads/2020/03/XX.pdf) trade-off. We can either *explore* to get more information (e.g., transition probabilities, rewards) that might lead to better future decisions and rewards, or *exploit* and make the best decision—given current information—for maximum reward now.

We want to get the best solution as fast as possible. But committing to a solution too quickly, without sufficient exploration, is bad and can lead to local optima. On the other hand, indiscriminate exploration is pointless. Striking the right balance is difficult.

Life is the same. Half a year ago, I decided that the pork belly bento from an Asian supermarket was the cheapest (< $7 after 5pm) and tastiest dinner option within walking distance. However, I only sampled a handful of places, and have not tried other options recently—how do I know it’s *still* the highest utility? (BTW, [reach out](https://twitter.com/eugeneyan) if you know of cheap, fuss-free takeout in downtown Seattle).

On a more serious topic, let’s talk careers. If you’ve just graduated and haven’t figured out what you want to do, hey, that’s normal. Not all of us drop out (of college) to start multi-billion dollar companies—don’t be too hard on yourself. Take the time to explore various career paths and find what’s best for you. Don’t rush to pick a career because Dad/society/linkedin said so.

> "Your goal in life is to find out the people who need you the most, to find out the business that needs you the most, to find the project and the art that needs you the most. There is something out there just for you.” - [@naval](https://twitter.com/naval?ref_src=twsrc%5Etfw)
>
> — Naval Ravikant Bot (@NavalBot) [January 16, 2019](https://twitter.com/NavalBot/status/1085627786478407682?ref_src=twsrc%5Etfw)

And once you figure it out, double down on it. Matthew McConaughey wanted to switch from law school to film school and didn’t know how Dad would take it. Instead of disapproval, he got the three greatest words ever: “Don’t half-ass it”.

> The three most important words Matthew McConaughey's dad said to him.   
>   
> Listen to my full interview with [@McConaughey](https://twitter.com/McConaughey?ref_src=twsrc%5Etfw) here: <https://t.co/Lx15hHZzOJ> [pic.twitter.com/GxaayzN0Gr](https://t.co/GxaayzN0Gr)
>
> — Tim Ferriss (@tferriss) [October 19, 2020](https://twitter.com/tferriss/status/1318273508733034502?ref_src=twsrc%5Etfw)

The greatest words Matthew McConaughey ever got: "Don't half-ass it"

Once we shift from *exploration* to *exploitation*, commit and see it through. Spending too much energy exploring on the side is wasteful. Nonetheless, look up every now and then to see if there’s a better way. Like most things, finding the right balance is key.

(To qualify, not everything needs to be thoroughly explored. Most decisions are [two-way doors](https://www.inc.com/jeff-haden/amazon-founder-jeff-bezos-this-is-how-successful-people-make-such-smart-decisions.html). Also, given limited time and energy, it’s okay to pick “[good enough](https://www.wsj.com/articles/how-you-make-decisions-says-a-lot-about-how-happy-you-are-1412614997)”.)

## Transfer Learning: Books and papers are cheat codes

In deep learning, pre-training is the step of training our models on a different, usually larger, dataset before applying transfer learning (aka fine-tuning) to our specific problem and data.

For example, we use models pre-trained on ImageNet for computer vision tasks. For language, recent models include an [unsupervised pre-training](/writing/nlp-supervised-learning-survey/#fine-tuning-learned-embeddings-2017) step. To adapt pre-trained models for our specific problems, we apply transfer learning by adding our own final layers, providing task-specific inputs and labels, and fine-tune to update model weights.

Similarly, we can think of school as generalized pre-training. We’re pre-trained on general theory, method, and knowledge of a variety of subjects (math, science, humanities, etc). But once we graduate (or even before), we need to fine-tune ourselves for specific tasks, such as building software, starting businesses, or hiring teams. The point is, school’s really just pre-training—don’t treat graduation as the end of learning.

Transfer learning is a cheat code for machine learning. It works for life too; I’ve found books to be the best pre-trained models by far. Books are the weights and biases of the great thinkers before us. Books contain a lifetime of learning, condensed into a couple hundred pages in an easily consumable format. Papers are another high-quality source of learning. They contain years of research, experiments, and learning condensed into a single paper. I find those with [ablation studies](https://en.wikipedia.org/wiki/Ablation_(artificial_intelligence)) especially enlightening.

Is it any wonder that the most successful and learned are voracious readers?

> The man who doesn’t read has no advantage over the man who can’t read – Mark Twain

## Iterations: Find reps you can tolerate, and iterate fast

Many machine learning techniques involve iteration. [Gradient boosted trees](https://en.wikipedia.org/wiki/Gradient_boosting#Gradient_tree_boosting) iteratively grow new trees based on pseudo-residuals (i.e., remaining error) from the previous tree. Gradient descent is an iterative optimization algorithm to find the lowest error. Deep learning models are trained iteratively via epochs, where each epoch passes the entire data set through the network.

Life involves iteration too. We won’t fully understand a paper by reading it once. (I usually need [three passes](/writing/why-read-papers/#how-to-read-papers).) The first machine learning model we train likely won’t beat the baseline; we need to iterate and try different data, features, objective functions, params, etc. Our [first A/B test](/writing/psych-grad-to-data-science-lead/#how-i-lost-millions-on-my-first-ab-test) probably won’t go well (but 🤞). Don’t worry if you don’t get it right the first time—who does? As long as we keep iterating, we’ll grow and improve.

Along the same vein, don’t expect success to come overnight. The developers of Angry Birds [failed 51 times](https://www.theatlantic.com/technology/archive/2011/03/how-rovio-fought-off-bankruptcy-to-make-angry-birds/72250/) before finding a game that clicked. Sir James Dyson [failed 5,126 times over 15 years](https://www.entrepreneur.com/article/224855) before his vacuum cleaner worked. If you decide to pursue something, make sure you’re able to tolerate the iterations and failure.

> I start early, and I stay late, day after day after day. It took me 17 years and 114 days to be become an overnight success. – Lionel Messi.

Other than the number of iterations, how fast we iterate is also important. Automating our [machine learning experimentation workflow](/writing/experimentation-workflow-with-jupyter-papermill-mlflow/) helps us iterate faster. Launching—and getting feedback from customers—earlier helps us improve quicker. If we’re not embarrassed with version 1, we probably launched too late. Even perfectionist Apple launched the iPhone [without copy-paste](https://www.t3.com/us/features/remember-this-heres-everything-that-the-first-iphone-couldnt-do).

> The number one predictor of success for a very young startup: Rate of iteration. – Sam Altman

## Overfitting: Focus on intuition and keep learning

Overfitting happens when our machine learning models fit the training data too closely and can’t generalize to new data. As a result, though training error is low, validation error is high. We guard against overfitting by evaluating our models on an unseen [holdout](https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets#Test_dataset) set.

Similarly, when we’re learning, we can prevent overfitting by focusing on understanding and intuition. While memorizing problems and solutions can get us pretty far in school, it won’t help when faced with novel, real-life problems.

> I don’t know what’s the matter with people: they don’t learn by understanding, they learn by some other way — by rote or something. Their knowledge is so fragile! – Richard P. Feynman

If we train on stale data, our models can’t generalize to recent data. Similarly, if we stop learning, we can’t adapt as technology progresses. Imagine trying to perform machine learning in Excel; it’s doable (I think), but it’s far easier and more effective with Python.

In life, how do we prevent overfitting? Adopting a Beginner’s mind works well for me. It’s a concept from Zen Buddhism where we have an attitude of openness, eagerness, and no preconceptions. We think like a beginner, stay curious, and approach new ideas as a student, even if it doesn’t fit our paradigm. With beginner’s mind, we’re always learning and updating our algorithm, reducing the likelihood of overfitting in life.

> The illiterate of the 21st century will not be those who cannot read and write, but those who cannot learn, unlearn, and relearn. – Alvin Toffler

## Ensembling: Diversity is strength

In machine learning, [ensembling](https://en.wikipedia.org/wiki/Ensemble_learning) involves using different machine learning models to obtain better performance than any single model can achieve. We also see this in random forests, where many different trees are grown and their predictions combined. Essentially, each model make up for the others’ weaknesses.

Different classifiers make up for one another's weaknesses ([source](https://www2.slideshare.net/eugeneyan/kaggle-otto-challenge-how-we-achieved-85th-out-of-3845-and-what-we#30)).

Similarly in life, diversity is a strength. When building teams, I favor diverse demographics, educations, experiences, and skills; diverse perspectives help us relate to and serve customers better. To build machine learning systems, we need skills in data pipelines, machine learning, software engineering, devops, product, etc.—it’s not enough to excel in just one aspect. One person’s strength complements another person’s shortfalls.

> Strength lies in differences, not in similarities – Stephen R. Covey

Some of the best ideas happen when we overcome [groupthink](https://en.wikipedia.org/wiki/Groupthink) and combine various ideas. Or when we combine our understanding of various subjects to develop a new superpower. For example, Scott Adams combined his ability to draw, sense of humor, and business know-how to create Dilbert.

> Creativity is just connecting things. When you ask creative people how they did something, they feel a little guilty because they didn’t really do it, they just saw something. It seemed obvious to them after a while. That’s because they were able to connect experiences they’ve had and synthesize new things.
>
> And the reason they were able to do that was that they’ve had more experiences or they have thought more about their experiences than other people.
>
> Unfortunately, that’s too rare a commodity. A lot of people in our industry haven’t had very diverse experiences. So they don’t have enough dots to connect, and they end up with very linear solutions without a broad perspective on the problem. – Steve Jobs

• • •

What other parallels between machine learning and life do you see? Reply to this tweet or post in the comments below.

> I think a lot about machine learning. I think a lot about life. Sometimes, the signals cross.  
>   
> Here are 7 lessons from machine learning applied to life.   
>   
> A thread 👇
>
> — Eugene Yan (@eugeneyan) [November 24, 2020](https://twitter.com/eugeneyan/status/1331065176733360129?ref_src=twsrc%5Etfw)

**Thanks** to Yang Xinyi for reading drafts of this.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Nov 2020). What Machine Learning Can Teach Us About Life - 7 Lessons. eugeneyan.com.
> https://eugeneyan.com/writing/life-lessons-from-machine-learning/.

or

```
@article{yan2020life,
  title   = {What Machine Learning Can Teach Us About Life - 7 Lessons},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Nov},
  url     = {https://eugeneyan.com/writing/life-lessons-from-machine-learning/}
}
```

  
Share on:
