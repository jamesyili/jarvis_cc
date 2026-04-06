# How to Win a Data Hackathon (Hacklytics 2021)

**Source:** https://eugeneyan.com//writing/how-to-win-data-hackathon/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

Last week, I was a mentor and judge at [Hacklytics 2021](https://hacklytics.io), Georgia Tech’s 36-hour datathon. As I interacted with teams during the hacking and evaluation sessions, I noticed patterns among the top teams that help them win. Here’s what I learned about how to do well at a data hackathon under time constraints.

Evaluation criteria for Hacklytics 2021

In case you're interested, here's the predefined criteria that judges were given to evaluate projects.

### Technical complexity — 20 points

What technologies were used or explored? We want to reward projects that demonstrate understanding as well as the desire to delve into and learn about unknown skills. This checks if the project has engaged with data science concepts and understands what it means to work with datasets (statistics, insights, exploration, modeling, etc.)

### Innovation — 10 points

Is the project something new or rarely seen before? Does it bring a new spin or angle to a known area or topic? What gives this project a “wow” factor?

### Completeness — 10 points

How much have they achieved of what they set out to achieve? Is the project deployed or ready to be deployed? How much further effort would be needed to make the project into a full-fledged application or solution?

### Design and Visualization - 20 points

Does the project look visually pleasing? Is it something that could potentially be seen and used on a public platform? Most importantly, if it is a visualization project, does the project justify their decisions from the visualizations made, and do they provide any valuable information that was sought?

### Presentation - 10 points

How well has the project been presented? Is the purpose and motivation clear? Whats next for the project? Do they have a working demo or prototype?

## Minimize data collection; use available datasets & APIs

While hacking, some teams asked how to scrape data from websites. For example, one team wanted to scrape IMDb for data on movie titles, cast, director, ratings, etc.

I advised against it. Scraping data is time-consuming and can be tricky when it comes to dynamically generated content (e.g., via JavaScript). Accurately parsing and extracting fields from raw HTML is a time sink. Instead, I pointed them to publicly available datasets, such as the data [provided by IMDb](https://www.imdb.com/interfaces/) or this [Kaggle dataset](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset) which has more than 80k titles.

In contrast, most of the winning teams saved time by using readily available, clean data. For example, the team building a [fake news detector](https://devpost.com/software/fake-news) used a Kaggle dataset of [40k real and fake news articles](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset). Similarly, the [overall winner](https://devpost.com/software/voices-of-the-vaccine) used a Kaggle dataset on [COVID Vaccine tweets](https://www.kaggle.com/kaushiksuresh147/covidvaccine-tweets). The organizers also shared a [list of publicly available datasets](https://hacklytics.io/participant.html#Data-sets) hackers could use.

What if teams needed recent data for which there’s no dataset? If so, they used APIs. The winning team (finance category) [used the Reddit API](https://github.com/yuktmitash21/Crawler/blob/main/crawl.py) to get data on r/wallstreetbets posts, including view counts, comments, title, body, etc. The overall winner used the [Twitter API](https://developer.twitter.com/en/docs/labs/tweets-and-users/quick-start/get-tweets) to get recent tweets on COVID vaccines. Using these APIs allowed them to focus on other aspects such as sentiment analysis and building user interfaces (UIs).

## Use libraries / pre-trained models to speed up ML

Though it was a data hackathon, relatively few teams trained machine learning models.

Many teams used [`Vader`](https://pypi.org/project/vaderSentiment/) for sentiment analysis. Its simple API and [great examples](https://github.com/cjhutto/vaderSentiment#python-demo-and-code-examples) made it easy for beginners to pick up—three of the winning teams applied `Vader` on tweets and Reddit posts. Another winning team used a combination of [`afinn`](https://pypi.org/project/afinn/) and [`text2emotion`](https://pypi.org/project/text2emotion/).

Some teams used pre-trained models. The team building a fake news detector started with pre-trained BERT and [fine-tuned](https://github.com/naisargidave/fakenewshacklytics/blob/main/Fake_News_Detection.py) it on their fake news dataset for three epochs. The winning team of the athletics (track & field) category started with pre-trained [3D human pose estimation models](https://github.com/xingyizhou/pytorch-pose-hg-3d) to detect when athletes jump over hurdles.

## Familiarity with front-end is useful

Most of the winning teams built simple UIs that made their ideas more concrete.

The winner of the healthcare category built [Clinical Model Tuner](https://devpost.com/software/clinical-model-tuner) to let physicians upload existing models and fine-tune them on additional data (i.e., inverse federated learning). They built a React app that demonstrated this well. Users could upload pre-trained models, datasets, and labels to fine-tune models. After fine-tuning, users could also see the improvements to model evaluation metrics.

User interface of Clinical Model Tuner (thanks to the team)

Another [team](https://devpost.com/software/wolf-of-wallstreetbets) performed sentiment analysis on r/wallstreetbets posts and visualize the correlation between a stock’s sentiment and its price movements. They also built a [React app](https://yuktmitash21.github.io//WolfofWallStreetBets-Frontend/) that allowed users to see Reddit posts on each stock and their associated sentiment, as well as price movements.

User interface of [Wolf of WallStreetBets](https://yuktmitash21.github.io//WolfofWallStreetBets-Frontend/)

Some teams also used python libraries to quickly build interactive UIs. The [winner](https://devpost.com/software/predicting-potentiail-yellow-jackets) of the athletics (football) track used [Streamlit](https://www.streamlit.io) to build a dashboard to show the football and social media statistics of potential recruits to help teams make better decisions. The overall winner built an interactive Plotly dashboard to visualize public sentiment towards COVID vaccines based on tweets.

User interface for Voices of the Vaccine ([source](https://devpost.com/software/voices-of-the-vaccine))

That said, it was not absolutely necessary to use React or libraries. The [TickerTrakr team](https://devpost.com/software/tickertrakr) won the best visuals award with a simple combination of Flask, HTML, CSS, and JavaScript.

## Knowing how to deploy is useful

Many of the winning teams had prototypes deployed. This made the difference between offline experimentation and a live demo that felt much closer to reality.

The [RealityCheck](https://devpost.com/software/fake-news) wrapped a [`Flask`](https://flask.palletsprojects.com/en/1.1.x/) app around their fine-tuned BERT model and deployed it on [Google Cloud Platform](https://cloud.google.com). This let them demo their Chrome extension which allowed users to enter news snippets and get the probability of it being fake news.

Some teams even made their prototypes publicly available so other participants and judges could interact with them. Some of these demos are still only (as of 2021-02-14):

* [The Wolf of WallStreetBets](https://yuktmitash21.github.io//WolfofWallStreetBets-Frontend/): Price and sentiment trends (based on r/wallstreetbets)
* [Hurdle Tracker](https://www.hurdl.us): Hurdle jumping performance (e.g., distance, speed) from videos

User interface of [Hurdle Tracker](https://www.hurdl.us/)

## Conclusion

Training bespoke machine learning models wasn’t a differentiating factor at this hackathon. Instead, what made a difference was:

* Using readily available data via public datasets or APIs
* Using libraries / pre-trained models to speed up ML iteration
* Building UIs to make machine learning and insights easy to consume
* Deploying models and UIs so people can use them

Similar to building machine learning systems in industry, no?

> How do you win a data hackathon?  
>   
> I saw how top teams did it at Hacklytics 2021 by:  
> • Using available datasets & APIs  
> • Using ML libraries & pre-trained models  
> • Building simple UIs for demos  
> • Deploying prototypes for judges to try  
>   
> More details 👇<https://t.co/f7vvuRCHCH>
>
> — Eugene Yan (@eugeneyan) [February 17, 2021](https://twitter.com/eugeneyan/status/1361847330811506691?ref_src=twsrc%5Etfw)

**Thanks** to Yang Xinyi for reading drafts of this.

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Feb 2021). How to Win a Data Hackathon (Hacklytics 2021). eugeneyan.com.
> https://eugeneyan.com/writing/how-to-win-data-hackathon/.

or

```
@article{yan2021hacklytics,
  title   = {How to Win a Data Hackathon (Hacklytics 2021)},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2021},
  month   = {Feb},
  url     = {https://eugeneyan.com/writing/how-to-win-data-hackathon/}
}
```

  
Share on:
