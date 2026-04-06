# Internal • Netflix

**Source:** https://aman.ai/h/netflix/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Keywords](#keywords)
* [Key Stats](#key-stats)
* [Why did you interview with Netflix? / Why do you want to switch jobs? / What excites you most about potentially joining the Netflix team?](#why-did-you-interview-with-netflix--why-do-you-want-to-switch-jobs--what-excites-you-most-about-potentially-joining-the-netflix-team)
* [How do you provide context for your team?](#how-do-you-provide-context-for-your-team)
* [Desired qualities in your team](#desired-qualities-in-your-team)
* [Recommendations](#recommendations)
  + [Artwork Personalization](#artwork-personalization)
  + [“No Dead Ends”](#no-dead-ends)
* [Causal Inference](#causal-inference)
* [Future Works / Improvement](#future-works--improvement)
* [Cold Start](#cold-start)
* [Search](#search)
* [Content Decision Making](#content-decision-making)
* [Media ML](#media-ml)
* [Evidence Innovation](#evidence-innovation)
  + [What do you think of feedback?](#what-do-you-think-of-feedback)
  + [Aim to Assist](#aim-to-assist)
  + [Actionable](#actionable)
  + [Appreciate](#appreciate)
  + [Accept or Discard](#accept-or-discard)
* [The Keeper Test / High Talent Density](#the-keeper-test--high-talent-density)
* [Leading with Context](#leading-with-context)
  + [Loosely coupled but tightly aligned](#loosely-coupled-but-tightly-aligned)
  + [(Symphonic orchestras with Synchronicity + perfect coordination) Manufacturing v/s (Freedom and Responsibility to ensure Innovation) Creative Economy](#symphonic-orchestras-with-synchronicity--perfect-coordination-manufacturing-vs-freedom-and-responsibility-to-ensure-innovation-creative-economy)
* [No decision-making approvals needed](#no-decision-making-approvals-needed)
* [Dream team of stunning colleagues](#dream-team-of-stunning-colleagues)
* [Going Global](#going-global)
  + [Things on the culture memo: You must read them carefully + your own opinions + your own examples.](#things-on-the-culture-memo-you-must-read-them-carefully--your-own-opinions--your-own-examples)
  + [Why do you think you are a good match for this group?](#why-do-you-think-you-are-a-good-match-for-this-group)
  + [Establish Clear Roles and Responsibilities](#establish-clear-roles-and-responsibilities)
  + [Align on Shared Goals](#align-on-shared-goals)
  + [Regular and Transparent Communication](#regular-and-transparent-communication)
  + [Balance Short-Term and Long-Term Priorities](#balance-short-term-and-long-term-priorities)
  + [Use Data to Drive Decisions](#use-data-to-drive-decisions)
  + [Build Trust and Empathy](#build-trust-and-empathy)
  + [Collaborate on Roadmaps and Timelines](#collaborate-on-roadmaps-and-timelines)
  + [Escalate and Resolve Conflicts Promptly](#escalate-and-resolve-conflicts-promptly)
  + [Leverage Company Culture](#leverage-company-culture)
  + [Continuous Learning and Retrospectives](#continuous-learning-and-retrospectives)
  + [Conclusion](#conclusion)
* [HM](#hm)
  + [Expectations from your next job?](#expectations-from-your-next-job)
  + [What aspects of the Culture Memo do you agree with? / hat aspects of the Culture Memo are your favorites and why?](#what-aspects-of-the-culture-memo-do-you-agree-with--hat-aspects-of-the-culture-memo-are-your-favorites-and-why)
  + [What aspects of the Culture Memo do you disagree with?](#what-aspects-of-the-culture-memo-do-you-disagree-with)
  + [What was the most challenging project you have worked on?](#what-was-the-most-challenging-project-you-have-worked-on)
* [Increase experimentation velocity via configurable, modular flows. Amazon Music personalization, North - South Carousels](#increase-experimentation-velocity-via-configurable-modular-flows-amazon-music-personalization-north---south-carousels)
  + [When did you question the status quo?](#when-did-you-question-the-status-quo)
  + [How do you communicate with stakeholders?](#how-do-you-communicate-with-stakeholders)
  + [Unique Culture](#unique-culture)
* [Netflix Rows](#netflix-rows)
* [Netflix Games](#netflix-games)
  + [Feedback](#feedback)
  + [Netflix as a game publisher-developer hybrid](#netflix-as-a-game-publisher-developer-hybrid)
    - [Game Publisher](#game-publisher)
    - [Game Developer](#game-developer)
    - [Strategy](#strategy)
    - [Summary](#summary)
* [Business Models: (i) Digital on-demand streaming service and (ii) DVD-by-mail rental service](#business-models-i-digital-on-demand-streaming-service-and-ii-dvd-by-mail-rental-service)
* [Netflix Title Distribution](#netflix-title-distribution)
* [Memberships](#memberships)
* [Plans and Pricing](#plans-and-pricing)
* [Netflix Culture Memo/Deck](#netflix-culture-memodeck)
* [Netflix Originals / Original Programming / Only on Netflix](#netflix-originals--original-programming--only-on-netflix)
* [Diverse Audience](#diverse-audience)
* [Netflix Ratings](#netflix-ratings)
* [Netflix Deep-learning Toolboxes/Libraries](#netflix-deep-learning-toolboxeslibraries)
* [Netflix’s Long Term View/Investor Relations Memo](#netflixs-long-term-viewinvestor-relations-memo)
* [Netflix (Personalized) Search](#netflix-personalized-search)
* [Meetings](#meetings)
* [Netflix RecSys Talks](#netflix-recsys-talks)
* [Deep learning for recommender systems: A Netflix case study](#deep-learning-for-recommender-systems-a-netflix-case-study)
  + [Challenges in the data for building real-world recommender-systems compared to literature](#challenges-in-the-data-for-building-real-world-recommender-systems-compared-to-literature)
  + [Breaking (or at least dampening) Feedback Loops: Contextual Bandits and Search Data](#breaking-or-at-least-dampening-feedback-loops-contextual-bandits-and-search-data)
* [Design a recommendation system that can recommend movies, TV shows, and games. Note that games are only about 10-20 in number while there are thousands of movies and TV shows.](#design-a-recommendation-system-that-can-recommend-movies-tv-shows-and-games-note-that-games-are-only-about-10-20-in-number-while-there-are-thousands-of-movies-and-tv-shows)
  + [Core Objectives](#core-objectives)
  + [Architecture Design](#architecture-design)
    - [Data Collection and Processing](#data-collection-and-processing)
    - [Data Representation](#data-representation)
    - [Model Architecture](#model-architecture)
      * [Collaborative Filtering (CF) Layer](#collaborative-filtering-cf-layer)
      * [Content-Based Filtering](#content-based-filtering)
      * [Neural Models](#neural-models)
      * [Boosting Game Relevance in Rankings](#boosting-game-relevance-in-rankings)
      * [Game-Specific Handling](#game-specific-handling)
    - [Recommendation Process](#recommendation-process)
      * [Step 1: Candidate Generation](#step-1-candidate-generation)
      * [Step 2: Ranking](#step-2-ranking)
      * [Step 3: Post-Processing](#step-3-post-processing)
    - [Feedback Loop](#feedback-loop)
  + [Handling Challenges](#handling-challenges)
    - [Cold Start for Games](#cold-start-for-games)
    - [Overemphasis on Movies/TV Shows](#overemphasis-on-moviestv-shows)
    - [Boosting Game Representation](#boosting-game-representation)
  + [Tech Stack](#tech-stack)
  + [Summary of Enhancements](#summary-of-enhancements)
* [ML](#ml)
  + [1. **Intuition of ROC (Receiver Operating Characteristic) Curve**:](#1-intuition-of-roc-receiver-operating-characteristic-curve)
  + [2. **Why Do We Need Penalization?**](#2-why-do-we-need-penalization)
  + [3. **What Are the Corresponding Methods in Neural Networks?**](#3-what-are-the-corresponding-methods-in-neural-networks)
  + [4. **Which One Do You Like Best?**](#4-which-one-do-you-like-best)
  + [2. **Asked me to describe in detail a model I am most familiar with. I went back to GBDT and then was asked what are the parameters of GBDT and how to adjust them**:](#2-asked-me-to-describe-in-detail-a-model-i-am-most-familiar-with-i-went-back-to-gbdt-and-then-was-asked-what-are-the-parameters-of-gbdt-and-how-to-adjust-them)
  + [3. **Classic ML question: when the number of features is much larger than the number of data (p » n), how to handle this situation**:](#3-classic-ml-question-when-the-number-of-features-is-much-larger-than-the-number-of-data-p-n-how-to-handle-this-situation)
  + [1. How to serialize and deserialize the parameters of an ML model?](#1-how-to-serialize-and-deserialize-the-parameters-of-an-ml-model)
  + [2. How to use the context information, such as the query searched by the user, etc.?](#2-how-to-use-the-context-information-such-as-the-query-searched-by-the-user-etc)
* [System Design](#system-design)
* [Music + MAB](#music--mab)
  + [End-to-End Architecture for Personalized Music with Contextual MAB](#end-to-end-architecture-for-personalized-music-with-contextual-mab)
    - [1. **Query Understanding and Contextual Features Extraction**](#1-query-understanding-and-contextual-features-extraction)
    - [2. **Candidate Generation (Action Set)**](#2-candidate-generation-action-set)
    - [3. **Contextual Multi-Armed Bandit (MAB) Algorithm**](#3-contextual-multi-armed-bandit-mab-algorithm)
      * [Models:](#models)
    - [4. **Reward Signal**](#4-reward-signal)
    - [5. **Delayed Feedback Handling**](#5-delayed-feedback-handling)
    - [6. **Action Selection and Execution**](#6-action-selection-and-execution)
    - [7. **Latency Considerations**](#7-latency-considerations)
  + [End-to-End Flow for “Play Music” Query with Contextual MAB](#end-to-end-flow-for-play-music-query-with-contextual-mab)
  + [Conclusion](#conclusion-1)
* [Data Quality](#data-quality)
* [End Data Quality](#end-data-quality)
* [Data Platform](#data-platform)
* [Evan Cox/ Faisal Siddique - MetaFlow](#evan-cox-faisal-siddique---metaflow)
* [Tools](#tools)
  + [Python ML Infrastructure](#python-ml-infrastructure)
  + [Ray.io](#rayio)
  + [Horovod](#horovod)
  + [Kubernetes](#kubernetes)
  + [XGBoost](#xgboost)
  + [Other](#other)
  + [Google AutoML](#google-automl)
  + [Amazon SageMaker Autopilot](#amazon-sagemaker-autopilot)
  + [Metaflow](#metaflow)
  + [Summary](#summary-1)
* [Metaflow specs](#metaflow-specs)
* [comparision](#comparision)
* [Ville tutorial](#ville-tutorial)
* [Compute types](#compute-types)
* [Infrastructure](#infrastructure)
* [Below are the areas of focus:](#below-are-the-areas-of-focus)
* [Q’s](#qs)
* [Increase experimentation velocity via configurable, modular flows. Amazon Music personalization, North - South Carousels](#increase-experimentation-velocity-via-configurable-modular-flows-amazon-music-personalization-north---south-carousels-1)
  + [The motivation](#the-motivation)
  + [Competitors](#competitors)
  + [Problems](#problems)
  + [What is Metaflow?](#what-is-metaflow)
  + [Metaflow observability](#metaflow-observability)
  + [Metaflow achieves its functionality through a combination of a well-designed Python library, a set of conventions and best practices for workflow design, and integration with underlying infrastructure, particularly cloud services. Here’s a closer look at how Metaflow accomplishes its objectives:](#metaflow-achieves-its-functionality-through-a-combination-of-a-well-designed-python-library-a-set-of-conventions-and-best-practices-for-workflow-design-and-integration-with-underlying-infrastructure-particularly-cloud-services-heres-a-closer-look-at-how-metaflow-accomplishes-its-objectives)
    - [Python Library and API](#python-library-and-api)
    - [Data Versioning and Logging](#data-versioning-and-logging)
    - [Execution on Various Platforms](#execution-on-various-platforms)
    - [Resource Management](#resource-management)
    - [Experiment Tracking and Debugging](#experiment-tracking-and-debugging)
    - [Integration with Cloud Services](#integration-with-cloud-services)
    - [Plugin Architecture](#plugin-architecture)
  + [Sample Metaflow Workflow](#sample-metaflow-workflow)
  + [Running the Flow](#running-the-flow)
  + [Explanation](#explanation)
  + [Integration with AWS](#integration-with-aws)
  + [Metaflow](#metaflow-1)
  + [Outerbounds](#outerbounds)
* [Metaflow job descrip](#metaflow-job-descrip)
  + [AWS Stack Services (e.g., AWS Step Functions, SageMaker, AWS Glue)](#aws-stack-services-eg-aws-step-functions-sagemaker-aws-glue)
* [Fairness among New Items in Cold Start Recommender Systems](#fairness-among-new-items-in-cold-start-recommender-systems)
* [Data drift](#data-drift)
* [Causal Ranker](#causal-ranker)
* [Question bank](#question-bank)
* [your projects](#your-projects)
* [ooooo](#ooooo)
* [Syllabus](#syllabus)
  + [Week 1-2: Introduction to Econometrics](#week-1-2-introduction-to-econometrics)
  + [Week 3-4: Time-Series Analysis & Forecasting](#week-3-4-time-series-analysis--forecasting)
  + [Week 5-6: Causal Inference - Basics](#week-5-6-causal-inference---basics)
  + [Week 7-8: Experimental Design & A/B Testing](#week-7-8-experimental-design--ab-testing)
  + [Week 9-10: Advanced Causal Inference & Machine Learning Integration](#week-9-10-advanced-causal-inference--machine-learning-integration)
  + [Week 11-12: Reinforcement Learning](#week-11-12-reinforcement-learning)
  + [Week 13-14: Application to Real-World Problems](#week-13-14-application-to-real-world-problems)
  + [Ongoing: Networking & Keeping Up-to-Date](#ongoing-networking--keeping-up-to-date)
* [Further Reading](#further-reading)
* [References](#references)

## Keywords

* Netflix is one of the world’s leading entertainment platforms, with 283 million paid memberships in over 190 countries enjoying TV series, films and games across a wide variety of genres and languages. Members can play, pause and resume watching as much as they want, anytime, anywhere, and can change their plans at any time.
* At Netflix, we want to entertain the world and constantly innovate how entertainment is imagined, created, and delivered to a global audience.
* We stream content in over 30 languages across 190 countries, topping over 283 million paid subscribers. We launched a new ad-supported tier in November 2022 and are building an in-house world-class ad tech ecosystem to offer our members more choices in consuming their content. Our new tier allows us to attract new members at a lower price point while also creating a compelling path for advertisers to reach deeply engaged audiences.
* Netflix is global - roughly 60% of Netflix’s members are outside US and and a significant minority do not consume content in English at all.
* The engineering team’s mission is to develop advanced technology that ensures exceptional experiences for our members.
* We deliver thoughtful member viewing experiences. Our team is faced with the enormous ambitions of building highly performant, large scale, low-latency distributed systems and delivering an incredible slate of content.
* We seek to build unique value propositions that help us differentiate us and become a market leader in record time. Our roles come with expectations of delivering in a rapid clip, comfort with lofty goals (BHAG) and big ambitions, the visibility that comes with strategic initiatives, and responsibility and an appetite to operate like a startup within an established company.
* Join us on this journey, to lead some exciting initiatives, and the talented engineers who work on realizing our ambitious vision. As a stunning colleague, you will be responsible for building and leading a team of world-class engineers and researchers doing cutting-edge applied machine learning. You will foster/cultivate a vision and strategy for the team aligned with our mission and guide innovation projects from end-to-end: research ideas to production A/B tests.
* As an engineering manager you will:
  + Drive success in a fast paced, flat organization with minimal process and a heavy sense/emphasis on ownership and accountability.
  + Support your team by contextualizing the larger vision, enabling prioritization and fostering high focus and executional excellence.
  + Ability to lead in alignment with our unique culture. Operate as an ambassador of the Netflix Culture.
  + Create a dream team by hiring, retaining, and growing high performing talent.
* Netflix live: NFL Christmas Gameday Live – an audience of nearly 65 million US viewers. In the US, both games became the most-streamed NFL games in history, marking Netflix’s most-watched Christmas day ever.
  + Netflix live seeks to tap into massive fandoms across comedy, reality TV, sports, etc.
* Squid Game Season 2 enthralled fans all over the world as it skyrocketed to the top of the Netflix Global Top 10 (weekly), amassing an astounding 68 million views in its debut, ranking as the week’s most-watched title and breaking into the Most Popular List (all time) in a record three days.

## Key Stats

* Recommender – primary means of driving revenue, 80% of views on Netflix were from the service’s recommendations – drives member joy, satisfaction, and retention.
* ~30% of US internet traffic
* Netflix streams in more than 30 languages and 190 countries, because great stories can come from anywhere and be loved everywhere. Great, high-quality storytelling has universal appeal that transcends borders.
* According to Netflix, the average paid subscriber spends around two hours per day on the platform.
* As of 2023, Netflix employs approximately 13,000 full-time workers.
* Netflix is programming for well over half a billion people globally — something no other entertainment company has ever done before.
* Did you know that over 70% of all viewing on Netflix involves subtitles or dubs, and about 13% of hours viewed in the US are non-English titles? At the heart of this is building a product and technology that ensures Netflix feels immersive and meaningful, no matter what language you speak.
* Context, not control, guides the work for data scientists and algorithm engineers at Netflix. Contributors enjoy a tremendous amount of latitude to come up with experiments and new approaches, rapidly test them in production contexts, and scale the impact of their work.

## Why did you interview with Netflix? / Why do you want to switch jobs? / What excites you most about potentially joining the Netflix team?

* **Culture:** We’re at the cusp of a revolution in technology, thanks to the transformational power of AI. Netflix, with it’s unique culture that emphasizes people over process, context not control, extraordinary candor, the concept of a dream team with stunning colleagues, etc. – all of this ensures it’s uniquely positioned to succeed since the fast-paced nature of AI requires a culture that offers the nimbleness and agility to experiment. Reed Hasting’s No Rules Rules was the first book I read as I built my managerial chops back in 2017 at Apple, adopting some of it for my own teams at Apple and Amazon, etc. – its been crazy! The amount of influence Netflix has had on my life is phenomenal.
* **Technical Prowess in RecSys:** Coming to the area of recommendations and search – I’ve built search and recommender applications for music streaming on Alexa, search for Siri, etc. and Netflix stands out due to its culture of innovation which has lead to it being a frontrunner in the recommendations space for the past couple of decades. I’ve spent a ton of time on the Netflix blog over the past decade – especially going through articles from Justin’s team. As an area, Recommender and Search are critical to the business – they are the primary discovery channels that drive revenue, 80% of views on Netflix were from the service’s recommendations. RecSys is an area that carries significant impact.
* **Personal Level:** Lastly, on a more personal level, I am thrilled about the possibility of blending my passion for AI with my love for storytelling. I write AI primers and blogs (you can say its technical storytelling) and the prospect of contributing to a platform that reaches millions of people around the world, enhancing their entertainment experience, is truly exciting and fulfilling. Netfix has the world stage – the opportunity to delight over 283M members spanning over 190 countries representing hugely diverse cultures and tastes with Netflix’s content slate. The better the recommendations, the easier it is for Netflix members to find they’d love and resonate with and thereby bring about a lift in member joy, satisfaction, and retention is exciting.

## How do you provide context for your team?

* I’ve been wildly fortunate to hire and work with some of the most gifted SWEs I’ve ever known.
* I thinking bringing in a mix of perspectives and having people play to their strengths is a good recipe.
* Recognizing where the team has the deeper context needed to solve some of these problems. As an EM, providing that connective tissue and giving everyone the context they need to make the best decisions at every step to move forward.
* One of Netflix’s core values is FNR, people-over-process – you can do literally anything but the responsibility part kicks in which leads you to think about the implications/repercussions/first-second order effects of what you’re working on. Is this going to help other groups? Can we spend a little more time in the beginning to make it more resilient, say, make it less prone to error with flaky input? Not only making it more useful for the person using it but also more thoughtful for the person maintaining it.
* I prize a combination of pragmatism and empathy. This combination essentially makes for someone who can solve any problem that is presented to them.
* [Source](https://youtu.be/leTwsSw_QrI?t=906)

## Desired qualities in your team

* Culture of Extraordinary Candor: “Adapting” it as much as possible for my own team at Apple and Amazon
* Candid and Continuous Feedback: Open feedback can be considered an attack at face value
* Dream team: Worst morale, sourced, hired,
* Lead with empathy:

## Recommendations

* Figuring out how to bring unique joy to each member.
* Personalization enables us to find an audience even for relatively niche videos that would not make sense for broadcast TV models because their audiences would be too small to support significant advertising revenue, or to occupy a broadcast or cable channel time slot. A benefit of Internet TV is that it can carry videos from a broader catalog appealing to a wide range of demographics and tastes, and including niche titles of interest only to relatively small groups of users.
* We also believe that recommender systems can democratize access to long-tail products, services, and information, because machines have a much better ability to learn from vastly bigger data pools than expert humans, thus can make useful predictions for areas in which human capacity simply is not adequate to have enough experience to generalize usefully at the tail.

### Artwork Personalization

* To train our model, we leveraged existing logged data from a previous system that chose images in an unpersonalized manner. We will present results comparing the contextual bandit personalization algorithms using offline policy evaluation metrics, such as inverse propensity scoring and doubly robust estimators.
* We are far from done when it comes to improving artwork selection. We have several dimensions along which we continue to experiment. Can we move beyond artwork and optimize across all asset types (artwork, motion billboards, trailers, montages, etc.) and choose between the best asset types for a title on a single canvas?
* Images that have expressive facial emotion that conveys the tone of the title do particularly well.

### “No Dead Ends”

* If, on Netflix, the video Sonic the Hedgehog is in fact unavailable (as depicted, only Sonic X is available), we can still produce recommendations for similar available videos that are relevant to the query “sonic t”, and thus help avoid “dead ends” that users may otherwise experience.
  + From [Raveesh Bhalla’s Substack](https://raveesh.substack.com/p/no-dead-ends):
    - “No dead ends” is a commonly stated product/design “principle” for Search and Recommendation products. Unfortunately, it’s also wrong more often than not.
    - “No dead ends” is a commonly stated product/design “principle” for Search and Recommendation products. The thought behind it amongst every team is that users should never run out of choice: if we keep giving them some more, including in the form of “pivots” or “guided search suggestions”, users will ultimately be more successful and satisfied.
    - Unfortunately, for most products, this principle is wrong.
    - As an example from earlier in my career, I was working on introducing infinite scroll to a search product. Enough past tests had shown that if we increased recall and made it easier for people to see more options, they’d act more often. Some users would find the first thing to take action on, while others would find more to take action on.
    - A far more experienced Search PM warned me about the test, saying he’d run similar versions several times and they’d all failed. I didn’t believe him and went ahead.
    - Turns out, he was right. Users did consider more options (I.e. scroll and click on more), but they actually acted on fewer. This is because we effectively put them in a state of decision paralysis: “should I act on this item or scroll and see more?”
    - The exception to the rule would be passive consumption products - think shortform video feeds - where there is no action to take but to browse. In this world, infinite feeds will lead to greater success.

## Causal Inference

* “Testing your way into a better product” by letting members make the decisions. Test out every area of the product — where we relentlessly test our way to a better member experience with an increasingly complex set of hypotheses using the insights we have gained along the way.
* For more than 20 years, Netflix has utilized A/B testing to inform product decisions, allowing our users to “vote”—via their actions—for what they prefer. The platform that enables this decision-making encompasses UIs, backend services, and libraries, and is used by product managers, engineers, data scientists, and other roles internal to Netflix.
* Netflix consistently employs a simple but powerful approach to product innovation: we ask our members, through online experiments, which of several possible experiences resonate with them.
* We use controlled A/B experiments to test nearly all proposed changes to our product, including new recommendation algorithms, user interface (UI) features, content promotion tactics, title launch and scheduling strategies, streaming algorithms, new member signup process, and payment method
* Over the course of this series of tests, we have found many interesting trends among the winning images as detailed in this blog post. Images that have expressive facial emotion that conveys the tone of the title do particularly well. Our framework needs to account for the fact that winning images might be quite different in various parts of the world. Artwork featuring recognizable or polarizing characters from the title tend to do well. Selecting the best artwork has improved the Netflix product experience in material ways. We were able to help our members find and enjoy titles faster.
* We are far from done when it comes to improving artwork selection. We have several dimensions along which we continue to experiment. Can we move beyond artwork and optimize across all asset types (artwork, motion billboards, trailers, montages, etc.) and choose between the best asset types for a title on a single canvas?\
* Metrics:
  + There are many other possible metrics that we could use, such as time to first play, sessions without a play, days with a play, number of abandoned plays, and more. Each of these changes, perhaps quite sensitively, with variations in algorithms, but we are unable to judge which changes are for the better. For example, reducing time to first play could be associated with presenting better choices to members; however, presenting more representative supporting evidence might cause members to skip choices that they might otherwise have played, resulting in a better eventual choice and more satisfaction, but associated with a longer time to first play.
  + A related challenge with engagement metrics is to determine the proper way to balance long- and short-form content. Since we carry both movies (typically 90–120 minutes of viewing) and multiseason TV shows (sometimes 60 hour-long episodes), a single discovery event might engage a customer for one night or for several weeks of viewing. Simply counting hours of streaming gives far too much credit to multiseason shows; counting “novel plays” (distinct titles discovered) perhaps overcorrects in favor of one-session movies.

## Future Works / Improvement

* AR/VR for games – connecting people
* Auto-dubbing
* We are also interested in models that take into account how the languages available for the audio and subtitles of each video match the languages that each member across the world is likely to be comfortable with when generating the recommendations, for example, if a member is only comfortable (based on explicit and implicit data) with Thai and we think would love to watch “House of Cards,” but we do not have Thai audio or subtitles for it, then perhaps we should not recommend “House of Cards” to that member, or if we do have “House of Cards” in Thai, we should highlight this language option to the member when recommending “House of Cards.”
* Part of our mission is to commission original content across the world, license local content from all over the world, and bring this global content to the rest of the world. We would like to showcase the best French drama in Asia, the best Japanese anime in Europe, and so on. It will be too laborious and expensive to cross-translate every title into every other language, thus we need to learn what languages each member understands and reads from the pattern of content that they have watched, and how they have watched it (original audio vs. dub, with or without subtitles), so that we can suggest the proper subset of titles to members based on what they will enjoy.
* We have lots of research and exploration left to understand how to automatically credit viewing to the proper profile, to share viewing data when more than one person is viewing in a session, and to provide simple tools to create recommendations for the intersection of two or more individuals’ tastes instead of the union, as we do today.

## Cold Start

* Today, our member cold start approach has evolved into a survey given during the sign-up process, during which we ask new members to select videos from an algorithmically populated set that we use as input into all of our algorithms.

## Search

* Historically, Search and Recommendations have been treated as two separate problems; search being mainly focused on the query, recommendations on the user. Personalized Search brings them together because both the query and user information can be taken into account to effectively respond to the user’s needs. Search
  particularly can benefit from personalization as in many cases queries are broad enough to require different results for different users.
* Recognizing the variety of our customer’s needs, our advanced search features are designed to empower members to efficiently navigate our catalog, allowing them to find the right videos and games. This includes addressing the challenges associated with accommodating numerous languages and handling diverse input mechanisms from various devices, such as TV remotes and voice controls. We also extend our work beyond the title selection layer by looking for new ways we can present recommendations, explain them, and have members interact with our systems. Our goal is to minimize the time browsing and searching while maximizing enjoyment.
* Similar to other (video) search engines, when users search on Netflix they have a particular intent, i.e., an immediate reason, purpose or goal in mind. From qualitative and quantitative data we observe that search intents fall on a spectrum between Fetching a specific video from the catalog (“I know what I want, I need you to get it for me”) to extensively Exploring the catalog (“I don’t know what I want, let’s understand what you have”). We also observe that users express their intents using different query facets: (available and unavailable) videos to stream on Netflix, talent (e.g., actors), and collections (e.g,. genres). To illustrate the difference between intents and facets: a user searching for a specific video (i.e., the query facet), may have an intent to either play that video (Fetch) or to explore content that is similar to that video (Explore). By understanding the query facet, we can optimize for both intents.
* We define a search match as a video retrieved by the search engine by keyword-matching the query with the indexed videos (or by applying techniques such as query expansion). A search recommendation, on the other hand, is a video selected by the search engine by relaxing the match constraints, i.e., a video retrieved via traditional recommender systems approaches (e.g., collaborative filtering) in the query context. We use the term search results to refer to the union of search matches and search recommendations, i.e., all videos returned in response to a user query.
* A unique characteristic of search, and specifically Instant Search on TV where queries are very short. This presents a great opportunity for personalization as rich knowledge about the user can complement the limited query context. Users’ historical preferences can help the system to better predict users’ intent and in turn return a unique set of tailored results.
* The two typical search use cases for Netflix are fetch and explore. The fetch use case is most common, where users have a clear intent to search for a specific title (“I know what I want, I need you to get it for me”). Personalization can help users get to their results faster (less typing) if the title they are looking for has high affinity with their taste profile, which is often the case. A subset of this intent is for out-of-catalog videos, where the title the user is looking for is not available. Given that search results are the union of search matches and search recommendations, in the event of no search matches (out-of-catalog videos), this use-case degenerates to a purely recommendations-based use-case and the system should return titles which are related to the unavailable one. Also in this scenario personalization may provide additional value to the recommended results as the set of related titles can be broad and the notion of related titles can be different for different users. The explore use case (“I don’t know what I want, let’s understand what you have”) consists of broad queries, such as genres. Given the broad nature of the results, personalization can help optimize for the correct relevant titles for each user.
* One important aspect to highlight is that different search intents have different relevance personalization trade-offs. For example, query relevance is of primary importance for the fetch intent, since too much personalization could hurt the user experience if high affinity but lexically irrelevant results are ranked high in the list. On the other hand, for a genre query, titles belonging to the requested genre with high user affinity but low lexical query similarity are preferable. In other words, there is a delicate balance between relevance and personalization which is also intent specific.
* Re. Netflix search query testing framework for pre-launch and post launch regression analysis: In the pre-launch phase, we try to predict the types of failures the search system can have by creating a variety of test queries including exact matches, prefix matching, transliteration, and misspelling. Our query testing framework is a library which allows us to test a dataset of queries against a search engine. The focus is on the handling of tokens specific to different languages (word delimiters, special characters, morphemes, etc.)

## Content Decision Making

* Netflix creates content at an unprecedented scale. From movies to series: they release thousands of hours of content across hundreds of titles each year under “Netflix Originals”. But creating something great is expensive! Each project competes for budget and talented people.
* The big question? Greenlight or axe the project? Choosing wrong could mean missing out on the next “Squid Game” or “Stranger Things”. That’s a huge bummer not only for the producers but also for us viewers!
* To make well-informed decisions, Netflix uses data and machine learning to predict a project’s success before they film it. This helps them make informed decisions and hopefully avoid ditching the next big hit. Content decision making (CDM) is the question of what content Netflix should bring to the service.
* Content, marketing, and studio production executives make the key decisions that aspire to maximize each series’ or film’s potential to bring joy to our subscribers as it progresses from pitch-to-play on our service.
* We identified two ways to support content decision makers: surfacing similar titles and predicting audience size (“audience sizing”), drawing from various areas such as transfer learning, embedding representations, natural language processing, and supervised learning.
* Another crucial input for content decision makers is an estimate of how large the potential audience will be (and ideally, how that audience breaks down geographically). For example, knowing that a title will likely drive a primary audience in Spain along with sizable audiences in Mexico, Brazil, and Argentina would aid in deciding how best to promote it and what localized assets (subtitles, dubbings) to create ahead of time.
* By offering multiple views into how a given title is situated within the broader content universe, these similarity maps offer a valuable tool for ideation and exploration for our creative decision makers.
* Machine Learning goes way beyond the obvious. It analyzes data to discover non-obvious patterns. This is then used to answer key questions [3] and make the decision about a potential project:
  + Similar Movies and Shows: What are similar movies or series to the candidate project? Is this the next Stranger Things or a forgotten B-movie?
  + Regional Appeal: Predicting audience sizes across demographics and geographic locations. Will teens in Tokyo love it as much as families in France?
* This helps Netflix avoid duds and greenlight shows you’ll love.

## Media ML

* ML in Media use-cases:
  + Match Cutting: Finding Cuts with Smooth Visual Transitions Using Machine Learning
  + Discovering Creative Insights in Promotional Artwork
  + Video Understanding
  + Detecting Scene Changes in Audiovisual Content
  + AVA Discovery View: Surfacing Authentic Moments
  + Building In-Video Search
  + Detecting Speech and Music in Audio Content

## Evidence Innovation

* Gone in 90 seconds: Broadly, we know that if you don’t capture a member’s attention within 90 seconds, that member will likely lose interest and move onto another activity. Such failed sessions could at times be because we did not show the right content or because we did show the right content but did not provide sufficient evidence as to why our member should watch it. How can we make it easy for our members to evaluate if a piece of content is of interest to them quickly?
* Evidence includes everything we use to communicate to members what a movie, show, or game is and why it might be for them: critical for the discovery experience.
* Evidence is the information we present about movies, shows, and games - in the form of images, videos, and text - that help a member understand what a movie, show, or game is and why Netflix is recommending it. In success, evidence reflects a deep understanding of our titles and members’ taste.
* Leveraging available data, you will craft and communicate a strategic roadmap for the evidence product area and see to its execution leading cross-functional teams of the industry’s best data scientists, consumer insights researchers, designers, machine learning and software engineers. As a high-leverage thought leader, you will have the ability to shape our thinking on how to evolve our product, and have a massive impact on how members enjoy our service.
* Overall, putting these aspects together has helped us significantly reduce issues, increased trust with our stakeholders, and allowed us to focus on innovation.
* Excellent written communication skills and ability to present technical content to non-technical audiences.
* Ability to partner with different functions to ensure that your solutions drive real business impact. Strategic thinking and ability to incorporate larger business context into algorithm and product development.
* You combine a technical background with a strong product sense and excellent communication skills to define, explain and execute your vision. You naturally gravitate towards experimentation as a way to validate your hypotheses while having a healthy skepticism/cautiously optimistic when interpreting experimental results. In order to be successful in this position, you need to be able to work with world-class engineers, have the statistical acumen to collaborate with top-notch data scientists, the design sense to partner with a stellar experience design team, and the business sense to drive product goals and strategies. Demonstrated ability to build successful consumer-facing applications and algorithms, and a strong feel for the entertainment business are big pluses.

### What do you think of feedback?

* 4As
* At Netflix, it is tantamount to being disloyal to the company if you fail to speak up when you disagree with a colleague or have feedback that could be helpful.
* In the book “No Rules Rules” by Reed Hastings and Erin Meyer, the 4As of feedback serve as a guideline for giving and receiving constructive criticism effectively within a culture that emphasizes candor. Here’s a breakdown:

### Aim to Assist

* **Purpose**: Feedback should always be given with the intent to help the recipient improve, not to vent frustrations or assert dominance.
* **How**: Consider whether your feedback will genuinely benefit the person and improve the situation. Frame it as an act of support.

### Actionable

* **Purpose**: Feedback should be specific and include clear suggestions or examples so the recipient knows how to address the issue.
* **How**: Avoid vague statements like “Do better.” Instead, provide details, e.g., “You could improve this report by organizing the data into clear sections.”

### Appreciate

* **Purpose**: When receiving feedback, focus on the value it brings, even if it stings at first. Assume positive intent and be grateful for the opportunity to improve.
* **How**: Instead of becoming defensive, thank the person for taking the time to share their perspective and insights.

### Accept or Discard

* **Purpose**: The recipient of feedback has the autonomy to decide what to do with it. Not all feedback is equally relevant or accurate.
* **How**: Reflect on the feedback and determine if it aligns with your goals or values. You can choose to act on it or respectfully set it aside.
* These principles are part of Netflix’s culture of radical candor and are designed to foster openness and growth while minimizing the potential for feedback to feel personal or unhelpful.
* **From No Rules Rules:**
  + Say what you really think with positive intent.
  + Openly voice opinions and feedback instead of whispering behind one another’s backs, reducing backstabbing and politics, and enabling faster decision-making.
  + Coin the term “Only say about someone what you will say to their face.”
  + Frequent feedback encourages learning and enhances workplace effectiveness.
  + High Performance + Selfless Candor = Extremely High Performance.
  + At Netflix, failing to speak up when you disagree or have helpful feedback is seen as disloyal to the company.
  + Netflix promotes both candid and frequent feedback, even if it risks being hurtful.
  + Receiving bad news about your work can trigger feelings of self-doubt, frustration, and vulnerability, as the brain responds to negative feedback with fight-or-flight reactions.
  + A feedback loop is one of the most effective tools for improving performance, reducing misunderstandings, fostering co-accountability, and minimizing the need for hierarchy and rules.
  + To build a culture of candor, bosses must give copious feedback and also encourage employees to provide candid feedback to them.
  + Encouraging honest feedback can be facilitated by including it as an agenda item in meetings.
  + Netflix dedicates significant time to teaching employees the right and wrong ways to give feedback.
  + **4A Feedback Guidelines**:
    - **Giving Feedback**:
      * *Aim to Assist*: Feedback must have positive intent, clearly explaining how a specific behavior change benefits the individual or company.
      * *Actionable*: Feedback must focus on what the recipient can do differently.
    - **Receiving Feedback**:
      * *Appreciate*: Show appreciation for the feedback by listening carefully, considering it with an open mind, and avoiding defensiveness or anger.
      * *Accept or Discard*: You must listen and consider all feedback but are not required to act on it. Always respond with sincere thanks.
  + Feedback can be provided anywhere and anytime, including in private behind closed doors.
  + A culture of candor requires consideration of how feedback impacts others and adherence to the 4A guidelines.
* There is one Netflix guideline that if practiced religiously would force everyone to be either radically candid or radically quiet – “Only say about someone what you will say on their face”
* Netflix established regular mechanisms so that critical feedback is given at the right time.
* Reed came up with a Live 360 feedback, which was more like a Speed feedback – each pair gave one another feedback using the “Start, Stop, Continue” method. Once all the members were covered, they had a group discussion on what they learnt during the feedback.

## The Keeper Test / High Talent Density

* Netflix did not want people to see their jobs as a life time arrangement. A job is something you do for that magical period of time when you the best person for the job and that job is the best position for you.
* Once you stop learning or stop excelling, that is the moment for you to pass on that spot to some one else who is better fitted for it and to move on to a better role for you.
* They found a professional sports team as a good metaphor for high talent density since athletes:
  + Demand/expect excellence – making sure every position is filled by the best person at any given time
  + Train to win – expect to receive candid and continuous feedback about how to up their game from the coach and from one another
  + Know effort isn’t enough and putting in a B performance despite an A for effort – they will be thanked and swapped for another player.

## Leading with Context

* The benefit is that the person builds the decision-making muscle and makes better independent decisions.
* However, Leading with Context requires that you have a high talent density.
* A great example differentiating the Leading with Control and Leading with Context is how you treat your teenage son going out to party on Saturday nights – monitor him every half hour till he comes home or explain to him the dangers of drinking and driving and once he understands, let him go without any process or oversight.
* A second key question to consider to lead with context or with control is whether the goal is error prevention or innovation. If the focus is on eliminating mistakes, control is best. If the focus is on innovation, it is best to lead with context, encourage original thinking and not telling employees what to do
* A third criteria to consider is whether the system is loosely or tightly coupled. In a tightly coupled system, the various components are intricately intertwined and making changes to one of the systems may impact the entire system. In a loosely coupled system, there are few interdependencies between the component parts making the entire system flexible.
* Maintaining an unusually high level of transparency within a company can drive a more informed and engaged workforce.
  + Netflix shares sensitive information with employees, including financial data and strategies, underscoring its trust in them.
  + By providing employees with more information, they can make better, more informed decisions that align with the company’s overarching goals.
  + When employees have a broader understanding of the company’s performance and goals, they feel more empowered and invested in its success. This empowerment increases their sense of accountability.
  + Sharing information is a testament to the trust Netflix places in its employees, and in turn, this openness fosters a deeper trust between the company and its workforce.
* Many employees will respond to their new freedom by spending less than they would in a system with rules. When you tell people you trust them, they will show you how trustworthy they are.
* As companies grow, bureaucracy often increases. Netflix’s approach ensures that even as it scales, it remains nimble and avoids becoming bogged down by excessive processes.
* Removing layers of approvals accelerates decision-making, allowing the company to respond quickly to challenges and opportunities. The speed and agility gained allow for better flexibility.
  + Instead of imposing control, leaders provide employees with the context they need to make informed decisions that align with the company’s goals.
  + While this approach can lead to occasional mistakes, Netflix believes that the benefits of faster decision-making and employee empowerment outweigh the drawbacks.
  + When errors occur, they’re viewed as learning opportunities. The focus is on understanding what went wrong and how to prevent it in the future, rather than placing blame.
  + As companies grow, bureaucracy often increases. Netflix’s approach ensures that even as it scales, it remains nimble and avoids becoming bogged down by excessive processes.
* By providing employees with the necessary context and freedom, they can be more innovative, agile, and proactive, leading to better outcomes for the company as a whole.
  + Instead of micromanaging, leaders provide their teams with the necessary context to make informed decisions on their own.
  + When you have the freedom to make decisions, it leads to ownership and greater investment in results.
  + As a team or unit grows, there’s often a tendency to implement more rules. By leading with context, you can avoid this trap, ensuring that the team remains agile.
  + By providing clear context, leaders set expectations for high performance and empower employees to meet these standards without being bogged down by excessive rules.
  + Leaders are encouraged to be transparent about their decisions, ensuring that their teams understand the ‘why’ behind strategies and actions.
  + When employees understand the broader context, they can anticipate needs and challenges, becoming proactive rather than just reactive.
* We believe that our culture is key to our success and so we want to ensure that anyone applying for a job here knows what motivates Netflix — and all employees are working from a shared understanding of what we value most.
* Our emphasis on individual autonomy has created a very successful business. This is because in our industry, the biggest threats are a lack of creativity and innovation. And we’ve found that giving people the freedom to use their judgment is the best way to succeed long term.

### Loosely coupled but tightly aligned

* Yes, **Reed Hastings** and **Erin Meyer** discuss the idea of being “loosely coupled but tightly aligned” in *[No Rules Rules: Netflix and the Culture of Reinvention]*. This principle plays a significant role in Netflix’s organizational philosophy, emphasizing how autonomy and alignment coexist in their corporate culture.
* Here’s a breakdown of the concept as discussed in the book:

1. **Loosely Coupled**:  
   Netflix encourages autonomy at all levels of the organization. Teams and individuals are given significant freedom to make decisions, innovate, and act without needing layers of approval or micromanagement. This reduces bottlenecks, enables faster decision-making, and fosters creativity.
2. **Tightly Aligned**:  
   Despite the high level of autonomy, everyone at Netflix is expected to align around the company’s overarching goals and strategy. This ensures that while teams operate independently, their work supports the company’s shared objectives. Alignment is achieved through clear communication, transparency, and a deep understanding of the organization’s priorities.
3. **Why It’s Important**:  
   The balance of autonomy (looseness) with alignment (tightness) prevents chaos while avoiding the stifling effects of bureaucracy. Employees are trusted to do what they think is best while being mindful of how their actions contribute to the bigger picture.

* Hastings uses the example of a sports team to explain the concept: each player (team/department) focuses on their role but understands the game plan and works toward a common goal.
* This principle underpins Netflix’s broader cultural framework, which emphasizes freedom, responsibility, and innovation.

### (Symphonic orchestras with Synchronicity + perfect coordination) Manufacturing v/s (Freedom and Responsibility to ensure Innovation) Creative Economy

* Netflix believes that when you lead or manage a company, you have a clear choice – either working to control the movements of your employees through rules and process or implement a culture of freedom and responsibility, choosing speed and flexibility and offering more freedom to employees
* It is important to differentiate the different ways of working – in a manufacturing environment, you are trying to eliminate variation and most management approaches have been designed with this in mind. So, companies operated as symphonic orchestras with synchronicity, and perfect coordination as a goal.
* If you are leading an emergency room, testing airplanes or managing coal mines or delivering just in time medication to senior citizens, rules is the way to go. However, for those who are operating in the creative economy, where innovation, speed and flexibility are the keys to success, those which operate in closer to edge of chaos – the symphonic orchestra may not be the right type of musical score – it is more like a jazz and when it comes altogether, the music is beautiful.
* The insights into building a cohesive organizational culture ensure smoother and more effective partnerships. Empowering your team while maintaining accountability as well as decentralizing decisions and trusting team members result in a loosely coupled but tightly aligned team which raises the bar on excellence.
* Cutting down on bureaucratic approvals ensures faster decision-making and reduces administrative burdens, leading to greater efficiency.
* With great freedom comes great responsibility. Team members are expected to be judicious and prudent with their expenses and time off.

## No decision-making approvals needed

* People thrive in jobs that give them control over their own decisions. The more people are given control over their own projects, the more ownership they feel, and the more motivated they are to do their life’s best work.
* If your employees are excellent and you give them the freedom to implement the bright ideas they believe in, innovation will happen.
* Netflix believes that since they are in a creative market, their big threat in the long run is not making a mistake, it is lack of innovation.
* The Netflix Innovation Cycle talks of four steps:
  + “Farm for dissent” or “socialize” the idea
  + For a big idea, test it out
  + As the informed captain, make your bet.
  + If it succeeds, celebrate. If it fails, sunshine it
* It is disloyal to Netflix when you disagree with an idea and do not express the disagreement. By withholding your opinion, you are implicitly choosing not to help the company.
* Farming for dissent is about actively seeking out different perspectives before making any major decision. Different opinions could be through comments on a document or rating the idea on a scale -10 to +10 on a spreadsheet.
* At Netflix, getting it perfect does not matter, what matters is moving quickly and learning from what you are doing
* Netflix believed in celebrating it – if an idea blooms, and sunshine it, if it fails. For projects/ideas that don’t succeed, they had a three-part response
  + Ask what learning came from the project – be candid about your failed bets and talk about the learning
  + Don’t make a big deal about it – When a bet fails, the manager must be careful to express interest in the takeaways, but no condemnation – nobody will scream, and nobody will lose his job
  + Sunshine the failures/mistakes - They believe that when you sunshine your failed bets, everyone wins – it is about learning, and taking responsibility for your actions.
* The bigger the mistake, the more you lean into the sunshine. Talk openly about it – you will be forgiven. But if you brush your mistakes under the rug and keep making mistakes, the end result will be much more serious.

## Dream team of stunning colleagues

* Assemble a dream team of stunning colleagues

## Going Global

* Expanding this unique corporate culture to the global stage was not without difficulties.
  + As Netflix expanded globally, it faced the challenge of applying its distinctive culture across various countries and regions with different norms and practices.
  + Allow local teams to make decisions tailored to their regions, ensuring that content and strategies resonate with local audiences.
  + Despite regional autonomy, there’s an emphasis on maintaining a unified culture. The core values of freedom and responsibility are consistent, even if applied differently in various locations.
  + Expansion brings about challenges like understanding diverse cultural norms and working practices. See these as opportunities for growth and adaptation.
  + Rely on seasoned employees, familiar with its culture, to act as ambassadors when entering new regions. They would help new teams integrate and understand the company’s values.
  + When the culture of candid feedback is maintained globally, it involves respecting and understanding cultural differences in communication but ensuring the essence of open dialogue remains.
  + By applying its culture globally, Netflix aims to harness innovation and creativity from all corners of the world, making it a truly global entertainment provider ### What harsh feedback have you received?

### Things on the culture memo: You must read them carefully + your own opinions + your own examples.

* Innovate in the recommender space and strive to win more of our members’ “moments of truth”. Those decision points are, say, at 7:15 pm when a member wants to relax, enjoy a shared experience with friends and family, or is bored. The member could choose Netflix, or a multitude of other options.

### Why do you think you are a good match for this group?

* Effective collaboration between an Engineering Manager (EM) and a Product Manager (PM) at a large company like Netflix, or similar organizations, hinges on clear communication, aligned goals, and a shared understanding of priorities. Here are key principles and practices for fostering such collaboration:

### Establish Clear Roles and Responsibilities

* + **Product Manager’s Role**:
  + Owns the product vision, roadmap, and prioritization.
  + Focuses on user needs, business goals, and defining “what” to build.
* **Engineering Manager’s Role**:
  + Responsible for the technical execution, team development, and defining “how” to build.
  + Ensures scalable, reliable, and efficient technical solutions.
* By defining boundaries, they can prevent overlaps and focus on complementary strengths.

### Align on Shared Goals

* Both the EM and PM must work toward shared objectives, such as:
* Delivering value to customers.
* Achieving product and business outcomes.
* Ensuring long-term scalability and technical health.
* At Netflix, with its culture of high performance and ownership, this means regularly revisiting goals and ensuring alignment between product priorities and technical feasibility.

### Regular and Transparent Communication

* **Weekly Syncs**: Hold regular one-on-one meetings to discuss priorities, challenges, and updates.
* **Real-Time Problem Solving**: Stay in close contact via Slack, email, or quick in-person chats to resolve issues promptly.
* **Document Collaboration**: Use shared documentation tools (e.g., Confluence, Notion) to co-create and track product requirements and technical designs.

### Balance Short-Term and Long-Term Priorities

* PMs often prioritize delivering features to meet immediate market needs.
* EMs need to advocate for technical investments, such as refactoring or infrastructure improvements, to avoid long-term debt.
* Collaborate to create a balance, using frameworks like **RICE (Reach, Impact, Confidence, Effort)** for prioritization or agreeing on time-boxing for tech debt work.

### Use Data to Drive Decisions

* Netflix values a data-driven culture. Both PMs and EMs should:
  + Leverage A/B testing to evaluate the impact of features.
  + Analyze user feedback, operational metrics, and system performance data.
  + Align on KPIs (Key Performance Indicators) to measure success.

### Build Trust and Empathy

* **EMs** should understand user-centric perspectives brought by the PM.
* **PMs** should appreciate the complexities of engineering challenges.
* Foster mutual respect by listening actively and considering each other’s constraints and motivations.

### Collaborate on Roadmaps and Timelines

* **Joint Planning**: Collaborate on quarterly or sprint roadmaps to ensure priorities and technical feasibility are aligned.
  + **Trade-offs**: Discuss trade-offs openly. For example, if a feature has a tight deadline, negotiate scope reduction rather than overburdening the team.
  + **Resource Allocation**: Work together to balance feature development with engineering capacity.

### Escalate and Resolve Conflicts Promptly

* Disagreements are natural. Address them by:
  + Seeking data and objective criteria.
  + Involving stakeholders or leadership when necessary.
  + Prioritizing customer and business value over personal preferences.

### Leverage Company Culture

* Netflix’s **“Freedom and Responsibility”** culture encourages ownership and transparency. Both EMs and PMs should:
  + Be direct and candid in feedback.
  + Take ownership of outcomes rather than just deliverables.
  + Empower their teams to contribute ideas and solutions.

### Continuous Learning and Retrospectives

* Conduct regular retrospectives to assess what’s working and what isn’t in their collaboration.
* Adapt based on feedback from the team and each other.

### Conclusion

* By adhering to these principles, an Engineering Manager and a Product Manager can forge a strong partnership that aligns technical execution with product strategy, driving meaningful results for both the company and its users.

## HM

### Expectations from your next job?

* Best Work of My Life (Netflix style: thanks to its unique culture)
* Innovate and solve challenging problems that are herculean tasks not just technically but also non-technical (highly cross-functional, etc.)
* Bring people joy and satisfaction

### What aspects of the Culture Memo do you agree with? / hat aspects of the Culture Memo are your favorites and why?

* Keeper’s Test: Stunning colleagues
* People over Process
* Context not Control
* Drum up the wood quote
* FNR (x)

### What aspects of the Culture Memo do you disagree with?

### What was the most challenging project you have worked on?

* ## Increase experimentation velocity via configurable, modular flows. Amazon Music personalization, North - South Carousels
* Flows: allows swapping out models with ease w/in the config file
* Implement data from S3 via DataSource
* SageMaker inference toolkit
* Ideation -> productionization time reduce
* Repetitve manual effort due to complex, fragmented code process
  + One of the most challenging projects I’ve had to work on is creating a unified infrastructure for Amazon Music.
  + S: So the Amazon entertainment suite, Music, Prime Video, Audible, Wondery Podcast, we cross collaborate often. There’s a lot of cross-functional, item-to-item recommendation systems we run that help both products.
  + In this case, we wanted to collaborate with Prime Video, Taylor Swift is a big artist on our platform and she’s recently done a tour which she’s made into a movie and whenever the user pauses, they basically should have a link back to Music to listen to that song/ playlist. For many artists, as well as original shows that have playlists on our app.
  + T: Our task was to collaborate, in the past, to get from research to production for us would be a fairly long process, just to get from research to productionization takes months.
    - Every single team has their own approach to go to prod from research. Own pipelines/ tooling platform for common tasks
    - Lack of standardized metrics and analysis tools: calculating position
    - Lack of established component APIs: Each model would have it’s own APIs so to switch out the model, would require a lot of work to adapt the model to the existing interface
    - Feature engineering inside the model, makes the model not transferrable
    - Metrics: not measuring
    - Research - python tooling, prod: Scala/ Java code -> ONNX. Checking in code, setting in pipelines, periodic flows needed in prod, monitoring steps. Was model in research same as in prod, are we measuring it the same
    - Two different pipelines, environment variables in different files, dynamo db has configs everywhere, different clusters, EMR jobs, hard to test change isn’t breaking anything. Time to onboard was too long, too many tooling. New processes.
    - Bottom line was, we were not able to get from prototype to production with high velocity which was stifling our need for increased experimentation.
  + A: This was our current norm, we would make snowflake/ unique but repetitive fixes for each collaboration we did. We would have different env variables, clusters, components that we would have to rebuild just for this project. Time to onboard was long, too much tooling here. Outside of this, we also needed to configure regular jobs, retries, monitoring, cost analysis needed to be set up, data drift checks.
  + Our original methodology included creating a new pipeline for each project, we were maintaining as you can imagine, quite a few pipelines in quite a few environments.
  + This was inefficient, I wanted to create a solution that would be less problem specific and more easy to be reusable. I wanted to change the way we do things. This overhead was neither good for our customers, it stifles experimentation, nor was it good for our data scientists, to be working on repetitive non creative tasks. Thats not why we hired them.
  + As part of this collaboration, I wanted to fix this bottleneck of course, along with our cross collaborators and team members.
  + Researched a few options out in the market as well as custom solutions. Airflow, Metaflow
  + R: Our eventual goal is to have a unified platform that the entire entertainment suite at Amazon can leverage
  + R:

### When did you question the status quo?

* Daily update meetings / project
* The issue is when you have a daily meeting, it’s hard to come into the meeting with a proper agenda and make sure everyone’s time is respected. There are nominal movements within projects on an everyday basis.
* Work with Program Managers, create excel sheets categorizing tasks, as well as Jira tickets, and sync up on a less frequent cadence. There should be a point/agenda to a meeting

### How do you communicate with stakeholders?

* How to gear the message towards the audience, audience intended messaging

### Unique Culture

* Not every employee is worth keeping.
* What Netflix knows about pay that the rest of us are too scared to implement:
* Netflix has a radical approach to paying people.
* They eliminated performance bonuses and replaced them with this 3-part comp plan:
  1. Pay top of the market on salaries.
  2. Offer equity for long-term incentives.
  3. Use the “Keeper Test” to quickly exit underperformers.
* **Element 1: Top-of-Market Salary**
  + Netflix Co-founder Reed Hastings shares: “People are most creative when they have a big enough salary to remove some of the stress from home. But people are less creative when they don’t know whether or not they’ll get paid extra. Big salaries, not merit bonuses, are good for innovation.”
* **Element 2: Equity**
  + Netflix lets employees choose to include equity (and how much) in their compensation package with no vesting period.
  + So the employee can choose to cash out at any point. From day one they are owners. The message - think long term, like an owner.
* **Element 3: The Keeper’s Test**
  + These two elements ONLY work when paired with Netflix’s infamous Keeper Test:
    - Managers have to always ask: Which of my people, if they told me they were leaving for a similar job at a peer company, would I fight hard to keep at Netflix?
    - Anyone else gets a generous severance now so they can open that role up for a star.
    - Uniquely, all Netflix employees know that if they are not performing, the culture expects them to be exited from the company.
  + Thus, while they do pay top of market, but they also are very quick to let someone go. They are acutely aware that their culture is not for everyone and it’s very much a you didn’t work out, no hard feelings, here is your severance package.
* **Takeaways:**
  + Many business owners and CEOs like the IDEA of the keeper test. But rarely ask themselves: how often am I proactively exiting people I wouldn’t fight to keep?
  + The reality is that most companies don’t eliminate mediocre employees.
  + The Keeper Test, fully lived out, is the CRITICAL element that makes all this work.
  + It’s an incentive protecting against poor performance that is an ESSENTIAL complement to the elimination of bonuses.
  + This ultimately saves the company and the team a tremendous amount of heartache and money.

## Netflix Rows

* From 10,000 rows, there are typically up to 40 rows shown on each homepage (depending on the capabilities of the device), and up to 75 videos per row.
* Thematically coherent rows:
  + Top 10 TV Shows/Movies
  + Continue Watching
  + Only on Netflix
  + Watch It Again
  + My List
  + New on Netflix
  + Genres: Action / Comedy / Sci-Fi / Horror / Documentaries / Dramas
  + Games
  + Gems for you / Top Picks for You
  + Watch In One Weekend
  + Feel-Good Romantic Movies
  + 30 Minute Laughs
  + Because You Watched/Liked
  + Watch Together for Older Kids

> The most strongly recommended titles start on the left of each row and go right – unless you have selected Arabic or Hebrew as your language in our systems, in which case these will go right to left.

* 10-40 rows per personalized load.
* Top-left: most likely to see; bottom-right: least likely to see
* Row lifecycle:
  + Select candidates
  + Select evidence (personalized/ad-hoc genres / based on tag combinations)
  + Rank
  + Filter (titles previously watched, de-dup)
  + Format UI based on device
  + Choose
* Row Features:
  + Quality of items
  + Features of items
  + Quality of evidence
  + User-row interactions
  + Item/row metadata
  + Recency
  + Item-row affinity
  + Row length
  + Position on page
  + Context
  + Title
  + Diversity
  + Freshness
* Location: most important (i) licensing model/content is only licensed for certain regions (apart from Netflix originals); (ii) user preferences are different (Japan: people watch more anime).
* Time: recommendations for the same user at 9AM would have more child content; evening is more of adult content (inferred signal: Companion).
* Device: On the phone app, more binge-watching; not as much discovery. On the TV, more discovery and/or binge-watching.
* Language: Dutch in Belgium v/s French in Belgium (even though content is the same since it is licensed at a country resolution)
* 2D versions of ranking quality metrics:
  + Example: Recall @ row-by-column
* User Modes of Watching:
  + Continuation
  + Discovery
  + Play from My List
  + Rewatch
  + Search
* Certain rows may be static/always be required:
  + Examples: Continue Watching and My List
* Netflix is dipping into more types of content, like the live fight between Jake Paul and Mike Tyson, the NFL games coming later this year, and the WWE’s Monday Night Raw.
* **Page-Level Optimization**:
  + A more sophisticated approach involves a **full-page scoring function** that aims to optimize the entire layout (rows and videos) rather than ranking rows in isolation. The ranking function evaluates the quality of each row or page. It is driven by machine learning and incorporates:
    - **Content relevance**: How well the videos in the row match the member’s preferences.
    - **Diversity**: Ensuring variety in themes, genres, or other aspects across rows.
    - **Navigation modeling**: Anticipating how users interact with the page (e.g., vertical scanning, visibility of content in the top-left corner).
    - **Evidence quality**: How strong the contextual or behavioral evidence is for recommending a particular row.
    - **Page constraints**: Considering device-specific limitations and avoiding duplicate content.
  + This full-page optimization may use machine learning and learning-to-rank models trained on user interaction data.

## Netflix Games

* Can do a multi-objective recommender system to suggest games with the objective of increasing the play time.
* Hades, Dead Cells, Into the Breach, Arcanium, Into the Dead 2, and TMNT are some of the best ones on that service and of course there is the GTA series. Hades is a massive win for Netflix.
* They don’t have ads or in app purchases.
* Much better than Apple Arcade.
* These are native iOS games just require subscription to access. Very very similar to Apple Arcade.
* A series of streamable games are available in select regions alongside the more well known downloadable games
* If they figure out a way to stream those games to your TV/device and let you use your phone as a controller (or any Bluetooth controller) that would be ideal.
* Games features/characteristics:
  + Category/Genre: Action, Adventure, Arcade, Card Game, Interactive Story, Puzzle, Sports, Simulation
  + Maturity/Age/Parental Rating: 9+ or 12+ or 17+ (mild/realistic violence, horror/fear themes, suggestive themes, profanity, crude humor)
  + Mode: Single Player, Local Multiplayer, Online Co-op
  + Language(s)
  + Requires Internet
  + Game controller supported?
  + Developer?
  + Release year
  + Platform (not all games are on all platforms)
  + Depending on the device/surface, games’ titles change. Modes change (single player v/s double player).

### Feedback

* At the end of the game: “How was your experience playing ?" "What could we improve? Video quality; Audio quality; Delayed input; Gameplay quality; Other "

### Netflix as a game publisher-developer hybrid

* Netflix is primarily a **game publisher**, not a developer, although it has made steps toward developing its own games. Here’s the distinction and where Netflix fits:

#### Game Publisher

* A publisher funds, markets, and distributes games but doesn’t necessarily develop them in-house.
* Netflix’s Role as a Publisher:
  + Netflix collaborates with external game developers to publish games that align with its brand and content.
  + Examples: Netflix has worked with established studios to create games inspired by its popular franchises, like *Stranger Things: 1984* and *Stranger Things 3: The Game*.

#### Game Developer

* A developer is responsible for creating and coding the games.
* Netflix’s Development Efforts:
  + Netflix has acquired game studios, such as **Night School Studio** (known for *Oxenfree*) and **Boss Fight Entertainment**, signaling its intent to develop games in-house.
  + These acquisitions suggest Netflix is transitioning into a **developer-publisher hybrid**, focusing on creating original games while still publishing games from third-party developers.

#### Strategy

* Netflix’s entry into gaming is part of its strategy to enhance user engagement and diversify its offerings beyond streaming movies and TV shows. Its game catalog is accessible via its app for subscribers, aligning its gaming efforts with its core subscription model rather than standalone sales.

#### Summary

* Currently, Netflix is primarily a **game publisher** but is moving toward becoming a **hybrid developer-publisher** as it builds in-house capabilities and develops original content in gaming.

## Business Models: (i) Digital on-demand streaming service and (ii) DVD-by-mail rental service

* In 2007, the year the company introduced its digital on-demand streaming option alongside its DVD-by-mail rental service.

## Netflix Title Distribution

* As of July 2023, Netflix had 6,621 movies, series, and specials available in the US, not including over 60 video games. Of those titles, 3,657 were Netflix Originals, making up 55% of the US library.
* As of November 2024, Netflix has over 7-8k films/movies, TV shows and 100 mobile games available on its platform.

## Memberships

* As of November 2024, Netflix has approximately 283M global paid memberships, and remains the largest premium video on-demand service in the world.
* Netflix accounts for 17 percent of all worldwide online video subscriptions.

## Plans and Pricing

* Standard with ads: $6.99 / month
* Standard: $15.49 / month (extra member slots can be added for $7.99 each / month)
* Premium: $22.99 / month (extra member slots can be added for $7.99 each / month)

## Netflix Culture Memo/Deck

* [Netflix Culture — The Best Work of Our Lives](https://jobs.netflix.com/culture)
* [Netflix Culture Deck](https://www.slideshare.net/slideshow/culture-1798664/1798664) from 2009

## Netflix Originals / Original Programming / Only on Netflix

* Stranger Things
* The Crown
* 3 Body Problem
* Emily in Paris
* Wednesday
* The company’s first true original show was award-winning House of Cards.
* Categories:
  + Scripted series
  + Unscripted series/Special
  + Documentary film
  + Kids series
  + Foreign-language series
  + Film
* The company is actively pursuing awards as part of its Netflix’s original programming has received over 800 award nominations and 250 awards given. The Crown holds 129 of those awards.

## Diverse Audience

* Netflix is one of the world’s leading entertainment services with over 200 million members in over 190 countries. Our library of TV shows and movies varies by country and changes periodically.
* Netflix is not available in:
  1. China
  2. Crimea
  3. North Korea
  4. Russia
  5. Syria

## Netflix Ratings

* Netflix does NOT allow users to rate shows or movies using a star or numerical rating system. However, users can provide feedback through a **thumbs up** or **thumbs down** system:

  + **Thumbs Up**: Indicates you liked the content, helping Netflix recommend similar shows or movies.
  + **Thumbs Down**: Indicates you did not enjoy the content, so Netflix avoids recommending similar content.
* This simple system replaced the older star rating system in 2017 to streamline user feedback and enhance personalization.
* “Not for me”, Thumbs Up/”I like this”, Double Thumbs Up/”Love this!”

## Netflix Deep-learning Toolboxes/Libraries

* Netflix deploys a fairly large number of AWS EC2 instances that host their web services and applications. They collectively emit more than 1.5 million events per second during peak hours, or around 80 billion events per day. The events could be log messages, user activity records, system operational data, or any arbitrary data that our systems need to collect for business, product, and operational analysis.
* Experimentation Platform: the service which makes it possible for every Netflix engineering team to implement their A/B tests with the support of a specialized engineering team
  + ABlaze: View test allocations in real-time across dimensions of interest. To help test owners track down potentially conflicting tests, we provide them with a test schedule view in ABlaze, the front end to our Experimentation Platform.
  + Ignite: Netflix’s internal A/B Testing visualization and analysis tool. It is within Ignite that test owners analyze metrics of interest and evaluate the results of a test.
* DeLorean is our internal project to build the system that takes an experiment plan, travels back in time to collect all the necessary data from the snapshots, and generates a dataset of features and labels for that time in the past to train machine learning models. One of the primary motivations for building DeLorean is to share the same feature encoders between offline experiments and online scoring systems to ensure that there are no discrepancies between the features generated for training and those computed online in production. Note that the feature encoders are shared between online and offline to guarantee the consistency of feature generation.
* To validate reliability, we have Chaos Monkey which tests our instances for random failures, along with the Simian Army.
* The Hive metadata store is a central repository that stores metadata about the tables, partitions, schemas, and data locations in a Hive data warehouse. It enables Hive to manage and query structured data efficiently by maintaining information about the structure and storage of the underlying datasets.
* Presto is an interactive querying engine which is an open source project that could handle our scale of data & processing needs, had great momentum, was well integrated with the Hive metastore, and was easy for us to integrate with our DW on S3. We were delighted when Facebook open sourced Presto.
* Netflix uses a standardized schema for passing the Spark DataFrames of training features to machine learning algorithms, as well as computing predictions and metrics for trained models on the validation and test feature DataFrames.
* Meson is a general purpose workflow orchestration and scheduling framework that we built to manage ML pipelines that execute workloads across heterogeneous systems. Meson offers a simple ‘for-loop’ construct that allows data scientists and researchers to express parameter sweeps allowing them to run tens of thousands of docker containers across the parameter values.
* Metaflow is an open source machine learning infrastructure framework. Since its inception, Metaflow has been designed to provide a human-friendly API for building data and ML (and today AI) applications and deploying them in our production infrastructure frictionlessly. Modeling, Deployment, Versioning, Orchestration, Compute, Data.

## Netflix’s Long Term View/Investor Relations Memo

* Great, high-quality storytelling has universal appeal that transcends borders
* Netflix increasingly licenses and produces content all across the globe and Netflix members everywhere in the world can increasingly enjoy the same movies and TV series at the same time, free of legacy business models and outdated restrictions.
* With our global distribution, Netflix is well positioned to bring engaging stories from many cultures to people all across the globe.

## Netflix (Personalized) Search

* Ranking entities for partial queries
* Optimizing for the minimum number of interactions needed to find something
* Different languages involve very different interaction patterns
* How to automatically detect and adapt to such patterns in newly introduced languages?

## Meetings

* Gary Tang
  + Multi-objective (MOO) recommender systems
  + Reward innovation for long-term member satisfaction by predicting delayed rewards
* Raveesh Bhalla
  + “Your models are only as good as your data”
  + Cytation: “Find YouTube videos that cite an arXiv paper”
  + Decision-making frameworks
* Erik Schmidt
* Linas Baltrunas
  + ICLR 2016 paper: Session-based Recommendations with Recurrent Neural Networks
  + Contextual Multi-Armed Bandit for Email Layout Recommendation

## Netflix RecSys Talks

* 2021: Trends in Recommendation & Personalization at Netflix
* Oct 2024: Raising a Recommender System

## Deep learning for recommender systems: A Netflix case study

### Challenges in the data for building real-world recommender-systems compared to literature

* Even though several common properties of the data have been discussed in the literature of recommender systems, it is worth reviewing them briefly before we outline additional challenges in the data for building real-world recommender-systems. The key differences to the data-sets used in other domains are as follows: first and foremost, the observed/collected data are missing not at random (Hernández-Lobato, Houlsby, and Ghahramani 2014; Liang et al. 2016; Marlin, Zemel, and Roweis 2005; Marlin et al. 2007; Marlin and Zemel 2009; Steck 2010), that is, the entries with observed positives (e.g., played videos, clicked items, given ratings or thumbs, etc.) are not randomly distributed in the user-item interaction-matrix. This is a crucial difference to fields like compressive sensing or matrix completion, where the entries in the matrix are typically assumed to be missing at random. Second, the unobserved entries in a user-item interaction matrix may either be (true) negatives (i.e., the user is truly not interested in this item), or positives that were not observed (yet). Third, the observed data are typically extremely sparse, and the observed positives are very noisy as they originate from a stochastic process. Fourth, there is a large popularity-skew present in the data, that is, the popularities of the various items follow approximately a power-law distribution, resulting in many orders of magnitude in differences in the popularities of the various items. Regarding the users, there is a similar (approximate) power-law distribution, with a small number of very active users and a large number of less active users. This power-law distribution can cause modeling challenges due to distribution mismatch. It also poses a challenge in making fair and accurate recommendations regarding unpopular items or for users with low activity.

### Breaking (or at least dampening) Feedback Loops: Contextual Bandits and Search Data

* In a real-world recommender system, the various biases in the user-item interaction-data, like presentation or position biases, can possibly be amplified due to a feedback loop, where the recommender system is trained on the observed user-actions from a previous time-step, which may be biased due to the recommendations shown to the users at that time (Chaney, Stewart, and Engelhardt 2018). This is due to presentation bias, where users are more likely to interact with items shown more prominently by the system. Breaking (or at least dampening) the feedback loop is a key challenge in real-world recommender-systems. This poses not only a challenge for training recommender systems on the data that have been collected, but also results in a notable mismatch between offline and online metrics, as outlined later in this article.
* Contextual bandit techniques in particular are able to break the feedback loop and remove various biases (e.g., Wang et al. 2020) in the data by introducing some amount of randomness into the recommendations. With bandit algorithms, we can continuously gather cleaner training-data by keeping track of the propensities for the shown recommendations. Even though the user-experience may be occasionally slightly degraded in the short-term due to this randomization, it helps improve the quality of recommendations in the long-term. We found these approaches very effective in our online tests where the careful design of the exploration approach meant the initial impact of some randomness can be within the noise-floor of the algorithm.
* A complementary approach to exploration is to use the fact that there are different ways of discovering videos on the Netflix service. For instance, if a video gets recommended to a member, there is no need for the member to search for it. In contrast, if a video or category of videos is not recommended to a member, it may trigger the member to search for it. Hence, the feedback loop can be partially broken by training the recommender system not only on the videos that were discovered from pages of recommendations, but also on the videos found via search (and analogously for a search algorithm). The advantage of this approach is that it does not require any randomization of the displayed videos, and hence does not result in any short-term degradation of the recommendations shown to the user. The disadvantage of this approach obviously is that it is difficult to quantify to what degree the feedback loop was broken, and the importance of the different data sources has to be carefully tuned in the training data. Nevertheless, we found this approach to be an effective component for (partially) breaking the feedback loop, as it comes at no cost/degradation of the user-experience. Of course, this approach is only applicable in recommendation tasks where there are several ways for a user to discover items.

## Design a recommendation system that can recommend movies, TV shows, and games. Note that games are only about 10-20 in number while there are thousands of movies and TV shows.

* Designing a robust recommendation system for Netflix that includes movies, TV shows, and a limited number of games (10-20) requires careful consideration of data representation, scalability, and diversity by **boosting the relevance/ranking scores to ensure the representation of games**.

### Core Objectives

1. **Personalization:** Tailor recommendations to individual user preferences.
2. **Cross-category Relevance:** Recommend across movies, TV shows, and games, accounting for differing item quantities.
3. **Cold-Start Problem:** Handle scenarios where games (being fewer in number) have limited user interaction data.
4. **Diversity:** Ensure recommendations span all three categories, with specific emphasis on games due to their limited catalog size.

### Architecture Design

#### Data Collection and Processing

* **User Interaction Data:**
  + Movies/TV Shows: View history, ratings, time spent, search queries.
  + Games: Plays, durations, reviews, and specific in-game metrics (if available).
* **Metadata:**
  + Movies/TV Shows: Genre, director, cast, language, release year, etc.
  + Games: Genre, platform, developer, age rating, etc.
* **Implicit Feedback:** Clicks, browsing time, hovers over items, abandonment rates.

#### Data Representation

* **Unified Embedding Space:**
  + Represent movies, TV shows, and games in a shared vector space using embeddings.
  + Use techniques like word2vec or transformers to capture semantic similarity in metadata.
* **Contextual Features:**
  + Incorporate temporal features (e.g., recent interactions carry higher weight).
  + Include user profile data: preferences, age group, location, and history length.
* **Multi-hot Encoding for Genres:** Allow overlap in genre preferences across categories.

#### Model Architecture

##### Collaborative Filtering (CF) Layer

* **User-Item Matrix:**
  + Traditional CF models (e.g., Matrix Factorization or Alternating Least Squares) for movies and TV shows.
  + Sparse interactions for games integrated using a hybrid approach (CF + metadata-based similarity).

##### Content-Based Filtering

* Metadata-driven similarity for games due to their limited interaction data.
* Example: A user who enjoys action movies and TV shows may find action-adventure games relevant.

##### Neural Models

* Use a deep learning model like a **Multi-Modal Deep Neural Network (DNN):**
  + Inputs: User embeddings, item embeddings (movies, TV shows, games), and contextual features.
  + Outputs: Predicted relevance score for each item.

##### Boosting Game Relevance in Rankings

* Add **category-specific bias** in the ranking stage to ensure sufficient representation of games:
  + Apply a multiplicative boost to the game relevance scores during ranking:
    [
    S\_{game-boosted} = S\_{raw} \cdot (1 + B\_g)
    ]
    where ( B\_g ) is the game-specific boost factor, dynamically calculated based on:
    - The proportion of games already in the recommendation list.
    - A baseline boost factor to counteract their inherently lower interaction data.
    - Example: ( B\_g = 0.5 ) if games are underrepresented in the top N recommendations.
* Implement **boosting weights** using engagement trends:
  + If a user shows past engagement with games (e.g., has played 1 or more games), increase ( B\_g ).
  + Conversely, reduce ( B\_g ) for users with no gaming history to avoid irrelevant recommendations.

##### Game-Specific Handling

* Assign games higher weight in diversity-focused ranking since they’re fewer.
* Use game metadata (e.g., genre, platform) to align games with the user’s broader preferences.

#### Recommendation Process

##### Step 1: Candidate Generation

* Generate an initial pool of recommendations using:
  + CF for high-probability interactions.
  + Metadata similarity for games and new items.
  + Recently added content for novelty.

##### Step 2: Ranking

* **Rank candidates based on a combination of the following factors:**

1. **Relevance Score:**
   * Predicted by the DNN or hybrid model.
2. **Boosted Game Representation:**
   * Apply a boost to the relevance scores for games as detailed above.
   * Dynamically adjust ( B\_g ) based on:
     + The current proportion of games in the recommendation list.
     + User engagement signals for games.
   * Example:
     + If the initial top 10 recommendations contain 0 games, apply a boost ( B\_g = 0.75 ).
     + If 1 game is already present, reduce ( B\_g = 0.5 ).
3. **Diversity Score:**
   * Introduce a diversity penalty or bonus for over-represented categories in the ranked list.
   * Implement the diversity weight ( W\_d ) as a function of the current category distribution.
4. **Fine-Tune Ranking Using Weighted Hybrid Approach:**
   * Combine relevance, diversity, and game-focus scores into a final weighted score:
     [
     S\_{final} = w\_1 \cdot S\_{CF} + w\_2 \cdot S\_{content} + w\_3 \cdot S\_{game-boosted}
     ]
     + ( w\_3 ): Emphasize games in the scoring process, dynamically adjusted based on the user’s gaming engagement level.
     + For example, set ( w\_3 = 1.5 ), ( w\_1 = 1.0 ), ( w\_2 = 1.0 ).

##### Step 3: Post-Processing

* Apply **Diversity Constraints:**
  + Ensure a minimum quota for games in the top N recommendations:
    - Example: At least 1 game in the top 10, and at least 10% representation overall.
  + Use greedy algorithms to reorder items, preserving relevance while meeting quotas.
* Ensure relevance by re-ranking within each category to maintain high user satisfaction.

#### Feedback Loop

* Use A/B testing to validate recommendation performance.
* Update embeddings and model weights dynamically as new data is collected.
* Leverage reinforcement learning to reward models for engagement success.

### Handling Challenges

#### Cold Start for Games

* Use content-based recommendations leveraging game metadata.
* Cross-reference game genres with popular TV/movie genres.

#### Overemphasis on Movies/TV Shows

* Normalize category scores using logarithmic scaling to reduce the dominance of large item categories.
* Diversify the recommendation list using both proportional penalties and quotas for underrepresented categories like games.

#### Boosting Game Representation

* Dynamically calculate game-boost factors based on current recommendation list composition.
* Align boost factors with user gaming behavior for relevance.

### Tech Stack

1. **Data Processing:** Apache Kafka (streaming), Apache Spark (batch processing).
2. **Model Training:** TensorFlow, PyTorch, Scikit-learn.
3. **Recommendation Serving:** AWS Lambda/Fargate, Redis (for caching).
4. **Database:** Snowflake or AWS Redshift for storing user/item data.

### Summary of Enhancements

* **Introduced game-specific boosting mechanisms** to dynamically adjust the relevance scores for games, ensuring their fair representation in recommendations.
* **Detailed the implementation of game relevance boosts**, including proportional adjustments based on list composition and user engagement trends.
* **Refined the weighted hybrid ranking approach** to balance game representation with overall personalization goals.
* This refined recommendation system ensures fair and engaging recommendations across movies, TV shows, and games, while maintaining personalization and diversity.

## ML

### 1. **Intuition of ROC (Receiver Operating Characteristic) Curve**:

The ROC curve is a graphical plot that helps you understand how well your binary classification model is performing across different thresholds.

* **True Positive Rate (TPR)** (Sensitivity or Recall) is on the y-axis: This is the proportion of actual positives that the model correctly identifies.
* **False Positive Rate (FPR)** is on the x-axis: This is the proportion of actual negatives that the model incorrectly identifies as positives.

**Intuitive Explanation**:
Imagine you’re a doctor trying to detect a disease:

* **True Positives (TP)**: You correctly diagnose someone with the disease.
* **False Positives (FP)**: You mistakenly tell a healthy person they have the disease.
* **True Negatives (TN)**: You correctly tell a healthy person they don’t have the disease.
* **False Negatives (FN)**: You mistakenly tell someone with the disease that they are healthy.

The ROC curve helps visualize the trade-off between **sensitivity** and **specificity** at various decision thresholds. As you adjust the threshold (the point at which you classify someone as “having the disease” or “not”), you change both your true positive rate and false positive rate.

* A **perfect classifier** would have a curve that hugs the top left corner, indicating high TPR with low FPR.
* The **closer the ROC curve is to this upper left corner**, the better your classifier is performing.

The **AUC (Area Under the ROC Curve)** is a single number summarizing the ROC curve’s performance, where 1.0 represents a perfect model and 0.5 represents a model making random guesses.

### 2. **Why Do We Need Penalization?**

Penalization is a technique used in machine learning to **control model complexity** and prevent **overfitting**. In overfitting, the model learns not only the signal in the data but also the noise, which leads to poor generalization on new data.

**Why is penalization important?**

* **Prevent Overfitting**: Without penalization, a complex model (e.g., a neural network with too many parameters or a decision tree with many branches) could fit the training data too well, learning irrelevant patterns and noise. Penalization constrains the model to avoid this.
* **Simplicity and Generalization**: Penalized models tend to be simpler, focusing on the most important patterns in the data, which leads to better generalization to new, unseen data.

### 3. **What Are the Corresponding Methods in Neural Networks?**

In neural networks, several regularization techniques correspond to penalization in traditional machine learning:

* **L2 Regularization (Ridge Regularization)**: This technique adds a penalty to the sum of the squared weights in the loss function. It encourages smaller weights, reducing the model’s sensitivity to the training data and preventing overfitting. It corresponds to adding a penalty term that looks like (\lambda \sum w^2) in the loss function.
* **L1 Regularization (Lasso Regularization)**: This adds a penalty to the sum of the absolute values of the weights. It encourages sparsity, meaning it can reduce the influence of irrelevant features by driving their weights to zero.
* **Dropout**: A neural network-specific method where, during training, random neurons are “dropped out” (set to zero). This forces the network to learn more robust features and prevents co-dependency among neurons, which helps prevent overfitting.
* **Early Stopping**: Stop the training process when performance on a validation set starts to degrade, preventing the model from overfitting to the training data.
* **Batch Normalization**: Normalizes the input of each layer to reduce internal covariate shift, allowing the network to train faster and helping avoid overfitting.

### 4. **Which One Do You Like Best?**

This depends on the context, but **Dropout** is particularly appealing in deep neural networks because:

* It is simple to implement and widely used.
* It encourages the model to learn redundant and diverse representations, improving generalization.
* It works well in practice, especially for large, deep models.

However, for simpler models or when computational efficiency is a concern, **L2 Regularization** is often my go-to choice because:

* It’s mathematically elegant and works well across many models.
* It introduces less variance into the model than L1 regularization.

I like **Dropout** for neural networks due to its simplicity and effectiveness, but I also find **L2 Regularization** highly useful for a wide range of models.

### 2. **Asked me to describe in detail a model I am most familiar with. I went back to GBDT and then was asked what are the parameters of GBDT and how to adjust them**:

* **Description of GBDT (Gradient Boosted Decision Trees)**:
  + **GBDT** is an ensemble learning method that builds decision trees sequentially. Each tree tries to correct the errors of the previous ones by focusing more on the misclassified or under-predicted examples.
  + It works by combining weak learners (decision trees) into a strong model by optimizing a loss function using gradient descent.
* **Key Parameters of GBDT**:
  1. **n\_estimators**: The number of trees to be built. Increasing this value generally improves model performance but can lead to overfitting.
     + **Adjustment**: Start with a moderate number, such as 100-200, and increase it if underfitting is observed.
  2. **learning\_rate**: Controls how much each tree contributes to the overall model. A smaller learning rate requires more trees to reach the same accuracy, but can result in better generalization.
     + **Adjustment**: Use a grid search or cross-validation to find a balance between `n_estimators` and `learning_rate`.
  3. **max\_depth**: The maximum depth of each tree. It controls the complexity of the model. Deeper trees can capture more information, but risk overfitting.
     + **Adjustment**: Tune this parameter by checking model performance on the validation set. Typical values range from 3 to 8.
  4. **min\_samples\_split**: The minimum number of samples required to split an internal node. Increasing this value can prevent overfitting.
     + **Adjustment**: Higher values reduce model complexity, lower values can lead to more splits and potential overfitting.
  5. **subsample**: The fraction of samples to be used for fitting each tree. Using a value less than 1.0 can reduce overfitting.
     + **Adjustment**: Typically set between 0.5 and 0.9. Lower values add stochasticity, which can help with generalization.
  6. **min\_samples\_leaf**: The minimum number of samples required to be in a leaf node. Increasing this value prevents creating nodes with few samples, reducing overfitting.
  7. **max\_features**: The number of features to consider when looking for the best split. This can reduce overfitting by limiting the model’s capacity.
     + **Adjustment**: Typically a value between 0.3 and 1.0. Use cross-validation to tune this parameter.

### 3. **Classic ML question: when the number of features is much larger than the number of data (p » n), how to handle this situation**:

This is a common challenge in machine learning when you have high-dimensional data but a small number of samples. Here are some ways to handle it:

* **Dimensionality Reduction Techniques**:
  1. **Principal Component Analysis (PCA)**: A linear transformation method to reduce the dimensionality of the feature space while preserving as much variance as possible.
  2. **t-SNE or UMAP**: Non-linear dimensionality reduction techniques that can be useful for visualization and feature reduction.
* **Regularization Methods**:
  1. **Lasso Regression (L1 Regularization)**: L1 regularization adds a penalty equal to the absolute value of the coefficients, which tends to shrink some coefficients to zero, effectively performing feature selection.
  2. **Ridge Regression (L2 Regularization)**: L2 regularization adds a penalty proportional to the square of the coefficients, reducing their magnitude without eliminating them entirely.
  3. **Elastic Net**: A combination of L1 and L2 regularization, balancing between feature selection and regularization.
* **Feature Selection Techniques**:
  1. **Embedded Methods**: Use models like Random Forest or Gradient Boosted Decision Trees to rank and select the most important features.
  2. **Filter Methods**: Statistical methods like mutual information, correlation, or chi-square tests can be used to select the most relevant features.
  3. **Wrapper Methods**: Use techniques like Recursive Feature Elimination (RFE) to iteratively remove the least important features based on a model’s performance.
* **Model Choices**:
  1. **Sparse Models**: Use algorithms that handle high-dimensional data well, such as **Support Vector Machines (SVM)** or **Lasso Regression**.
  2. **Penalized Models**: Models that include built-in regularization, such as **Logistic Regression with L1/L2** penalties, can help handle p » n scenarios.
* **Increase Data Size**: If possible, collect more data to match the dimensionality of the feature space, or use data augmentation techniques.

These methods will help manage overfitting and improve the model’s performance in scenarios where the feature space is much larger than the sample size.

### 1. How to serialize and deserialize the parameters of an ML model?

Serialization is the process of converting the parameters of an ML model into a format that can be stored (like in a file) and later deserialized to restore the model. In Python, using libraries like **Pickle** or **Joblib** can help with this.

* **Serialization**: Use serialization to save the model’s state (including its parameters) to a file.

  ```
   import pickle
     
   # Assuming 'model' is your trained model
   with open('model.pkl', 'wb') as file:
       pickle.dump(model, file)
  ```
* **Deserialization**: Load the saved model back.

  ```
   with open('model.pkl', 'rb') as file:
       model = pickle.load(file)
  ```

Alternatively, **Joblib** is another option, especially for larger models, as it is more efficient with NumPy arrays.

```
   import joblib
   
   # Save the model
   joblib.dump(model, 'model.joblib')
   
   # Load the model
   model = joblib.load('model.joblib')
```

### 2. How to use the context information, such as the query searched by the user, etc.?

Yes, using the features of the query itself (e.g., **n-grams**, **keywords**, **entities**) can enhance search recommendations. Here’s how to approach it:

* **Query Feature Extraction**: Extract useful features from the user’s search query. For instance:
  + **N-grams**: Break the query into sequences of words (e.g., 1-gram for each word, 2-gram for pairs).
  + **Keywords**: Identify important terms or keywords.
  + **Entity Recognition**: Use NLP to detect entities like product names, locations, etc.
* **Use in Recommendations**:
  + **Search-based Recommendations**: Match these extracted query features with similar items in your dataset to generate recommendations.
  + **Context-Aware Recommendations**: Combine query features with other user data (e.g., previous interactions) to personalize results.

Example of using n-grams:

```
from sklearn.feature_extraction.text import CountVectorizer

query = ["find action movies with strong female leads"]
vectorizer = CountVectorizer(ngram_range=(1, 2))  # unigram and bigram
ngrams = vectorizer.fit_transform(query)

# Use 'ngrams' to search for relevant recommendations in the dataset
```

## System Design

* “An Indian sister mainly asked a lot of questions about recommendation systems and search, which were very detailed. She asked me how to solve various situations that Faye Wong encountered. For example, if the movie the user searched for was not available, what would you do? How to use the recommendation algorithm to solve it? How to use the context information such as the user’s search query, etc.? Finally, there was coding — how to serialize and deserialize the parameters of an ML model. I feel that this Indian sister is not as friendly as that Indian brother.”

## Music + MAB

In the context of **Amazon Alexa’s Generative AI**, a query like “Play Music” involves an ambiguous and generic request where personalization is crucial. A **contextual multi-armed bandit (MAB)** model can help in providing a highly personalized experience for the user by learning from user interactions over time. Below is an end-to-end architecture for implementing a **contextual multi-armed bandit** system for handling this type of query.

### End-to-End Architecture for Personalized Music with Contextual MAB

#### 1. **Query Understanding and Contextual Features Extraction**

When a user says “Play Music,” the system first needs to understand the context of the request. Although the user doesn’t provide specific details (e.g., genre, artist), the system can gather contextual information to make the recommendation more personalized. Key contextual features include:

* **User Profile Data**: Past interactions, listening history, preferences (e.g., favorite artists, genres).
* **Time of Day**: Morning, afternoon, evening (e.g., relaxing music in the evening vs. upbeat music in the morning).
* **Day of the Week**: Weekdays vs. weekends (weekends might call for more relaxed or party music).
* **Device Type**: Whether the user is interacting via an **Echo Dot**, **Echo Show** (with a screen), or another Alexa-enabled device. This helps determine if additional visual content should be considered, such as showing album art or music videos on **Echo Show**.

These features serve as the **context** in the **contextual MAB** framework.

#### 2. **Candidate Generation (Action Set)**

Once the context is established, the system generates a set of candidate actions, which in this case are the **songs, playlists, or stations** that could be played. The actions may include:

* **Songs**: Popular songs, personalized based on past listening behavior.
* **Playlists**: Genre-specific or mood-based playlists that align with the user’s preferences or recent trends.
* **Stations**: Personalized or curated radio stations.

Each action (song, playlist, station) is associated with its own expected reward (success likelihood based on past behavior and contextual information).

#### 3. **Contextual Multi-Armed Bandit (MAB) Algorithm**

For each user query, the **contextual MAB** algorithm selects the best action to present to the user based on:

* **Context**: Features like time of day, day of the week, genre preferences, user profile.
* **Arms**: In this case, the arms are the songs, playlists, or stations.

The bandit algorithm balances **exploration** (trying new or less common songs to learn more about user preferences) and **exploitation** (playing songs with a high probability of user engagement based on previous data).

##### Models:

* **LinUCB (Linear Upper Confidence Bound)** or **Thompson Sampling** with contextual features can be used to make real-time decisions based on the context.
* Each song, playlist, or station has a reward model based on past user interactions, adjusted for user context.

#### 4. **Reward Signal**

The **reward signal** is critical for training the contextual MAB. It defines what success looks like for a given action (song or playlist played).

* **Primary Reward**: The user listens to **more than 50% of the song** or playlist. This indicates strong engagement and satisfaction.
* **Secondary Reward** (Optional):
  + Skips (negative feedback).
  + Explicit positive feedback such as “liking” the song.
  + **Echo Show** interactions: If the device is an Echo Show, additional rewards could include whether the user interacted with the screen (e.g., looked at the lyrics, skipped to another song using the touch interface).

#### 5. **Delayed Feedback Handling**

In real-world scenarios, rewards may not be immediate. For instance, if a user listens to a playlist, the system may not know if they enjoyed it until they listen to a few songs or interact with the playlist over time. The system needs to handle **delayed feedback** by:

* **Deferring updates** to the model until meaningful feedback is collected (e.g., after the user listens to a significant portion of a playlist).
* Using **off-policy learning** or **reinforcement learning techniques** to update the model as feedback trickles in over time.

#### 6. **Action Selection and Execution**

Once the contextual bandit selects the action (song, playlist, or station), the system proceeds to:

* **Play the selected music**.
* If the device is an **Echo Show**, additional visual content like album covers, artist information, or even lyrics could be shown to enhance the experience. This adds a layer of multimodal engagement, and interactions with the screen (e.g., skipping songs) can also be fed back into the model as part of the reward signal.

#### 7. **Latency Considerations**

Given that Alexa must respond to user requests quickly, the entire process—from extracting context, selecting an action, to playing the music—must be highly efficient. Some latency considerations include:

* **Model Inference Latency**: The bandit model must make decisions in real time, so lightweight algorithms (like **LinUCB** or **Thompson Sampling**) are preferred for fast inference.
* **Caching Results**: Frequently played songs or playlists can be cached, reducing the time to action.
* **Pre-Computing Embeddings**: Precompute **content embeddings** and **user embeddings** (via models like **BERT** or **Word2Vec**) for rapid comparison during action selection.
* **Streaming Optimization**: Ensure the system can buffer or start streaming music immediately after an action is selected to minimize the wait time.

---

### End-to-End Flow for “Play Music” Query with Contextual MAB

1. **User Query**: A user issues a generic query like “Play Music.”
2. **Context Gathering**: The system gathers contextual information:
   * User’s historical preferences (e.g., genres, favorite artists).
   * Time of day, day of the week.
   * Device type (e.g., Echo Show).
3. **Candidate Generation**: The system generates a set of candidate actions (songs, playlists, or stations).
4. **Contextual MAB Decision**: The contextual MAB algorithm selects the action with the highest expected reward (e.g., a playlist of relaxing songs in the evening).
5. **Play Music**: The selected music is played on the user’s Alexa device.
   * If on **Echo Show**, album art, lyrics, or other visual content is shown.
6. **Collect Feedback**: The system monitors the user’s behavior:
   * If the user listens to **more than 50% of the song or playlist**, it’s considered a success.
   * If the user skips or interacts negatively, the reward is updated accordingly.
7. **Update Model**: The model updates its understanding of the user’s preferences based on feedback. If the feedback is delayed (e.g., the user listens to the playlist over several sessions), the system adjusts once sufficient feedback is gathered.

---

### Conclusion

Using a **contextual multi-armed bandit** system in the “Play Music” scenario allows Alexa to provide highly personalized music recommendations by learning from user preferences in real-time. The system is optimized to make quick decisions while balancing exploration and exploitation, and it adapts to user feedback. By considering key contextual factors like **time of day**, **user history**, and **device type**, the bandit system helps improve user satisfaction, leading to a more engaging and personalized Alexa experience.

## Data Quality

-[links video series 1](https://www.google.com/search?q=grace+huang+netflix+youtube&sca_esv=a132f53bdbf2e8af&sca_upv=1&sxsrf=ADLYWIIGAvjI58yzLmE7UUgH5BhuDcRn6A%3A1727120105115&ei=6cLxZsLcBu_L0PEP5rDZoAU&ved=0ahUKEwiC9eXi59mIAxXvJTQIHWZYFlQQ4dUDCBA&uact=5&oq=grace+huang+netflix+youtube&gs_lp=Egxnd3Mtd2l6LXNlcnAiG2dyYWNlIGh1YW5nIG5ldGZsaXggeW91dHViZTIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBDIIEAAYogQYiQUyCBAAGKIEGIkFSPULUIgGWP0KcAF4AJABAJgBcaABkwaqAQM1LjO4AQPIAQD4AQGYAgWgAo8DwgILEAAYsAMYogQYiQXCAgsQABiABBiwAxiiBMICBBAhGArCAgoQIRigARjDBBgKmAMAiAYBkAYFkgcDNC4xoAeYFQ&sclient=gws-wiz-serp)

-[Job role](https://explore.jobs.netflix.net/careers/job/790298797320-engineering-manager-machine-learning-and-interactive-discovery-los-gatos-united-states-of-america?domain=netflix.com)

```
Netflix is one of the world’s leading entertainment services with 278 million paid memberships in over 190 countries enjoying TV series, films and games across a wide variety of genres and languages. Members can play, pause and resume watching as much as they want, anytime, anywhere, and can change their plans at any time.

The Role

Fast-paced innovation in Generative AI and large language models (LLMs) is now advancing numerous fronts of the Search and Recommendations experiences on the Netflix product, including content discovery and personalization for members. We are looking for a seasoned engineering leader to help pave the future of Search and interactive discovery experiences at Netflix.

Your team will be at the forefront of research and application of LLM innovation, NLP, and Machine Learning. You will lead a team of experts and engineers to drive the development of machine learning models and algorithms that power our search and interactive discovery features, ensuring they provide personalized and contextually relevant recommendations to our members. In this role, you will be responsible for scaling and leading the team. Your team will be responsible for operating, as well as innovating on, these algorithms in production. You will help select and guide projects from end-to-end: idea to production. You will partner with people from many disciplines, including behavioral scientists, user experience designers, editors, machine learning researchers, application engineers, and product managers. 

To be successful in this role, you need to have rich machine learning and engineering experience driving ML applications on a consumer scale, and domain expertise  in the Search space. You are data-driven, curious with a healthy dose of skepticism, and have the proven ability to lead multi-disciplinary, cross-functional, teams. As owners of the systems, you are obsessed with engineering quality and operational excellence. You also need to be great at giving and receiving feedback, championing new ideas, empowering others, and balancing the needs of both research and engineering.

Minimum Job Qualifications
Experience building and leading a team of ML researchers and engineers

Proven track record of leading applications of ML to solve real-world problems

Broad knowledge of practical machine learning with a strong mathematical foundation

Experience driving cross-functional projects with diverse sets of stakeholders

Obsession with engineering and operational excellence and a relentless pursuit of great product experience

Excellent speaking, writing, and presentation skills to communicate with technical- and non-technical audiences

Strong interpersonal, analytical, problem-solving, and conflict-resolution skills. 

Advanced degrees in Computer Science, Computer Engineering, or a related quantitative field

Preferred Qualifications
10+ years of total experience including 5+ years of engineering management

Experience working on high-scale consumer problems and building ML-powered real-time interactive products  

Expertise in HCI, Information Retrieval and natural language processing (NLP) techniques 

Familiarity with Large Language Models (LLMs) 

Netflix's culture is an integral part of our success, and we approach diversity and inclusion seriously and thoughtfully. We are an equal opportunity employer and celebrate diversity, recognizing that bringing together different perspectives and backgrounds helps build stronger teams. We do not discriminate on the basis of race, religion, color, national origin, gender, sexual orientation, age, marital status, veteran status, or disability status.

Our compensation structure consists solely of an annual salary; we do not have bonuses. You choose each year how much of your compensation you want in salary versus stock options. To determine your personal top-of-market compensation, we rely on market indicators and consider your specific job family, background, skills, and experience to determine your compensation in the market range. The range for this role is $190,000 - $920,000.

Netflix provides comprehensive benefits including Health Plans, Mental Health support, a 401(k) Retirement Plan with employer match, Stock Option Program, Disability Programs, Health Savings and Flexible Spending Accounts, Family-forming benefits, and Life and Serious Injury Benefits. We also offer paid leave of absence programs.  Full-time hourly employees accrue 35 days annually for paid time off to be used for vacation, holidays, and sick paid time off. Full-time salaried employees are immediately entitled to flexible time off. See more details about our Benefits here.

Netflix has a unique culture and environment.  Learn more here.  

We are an equal-opportunity employer and celebrate diversity, recognizing that diversity of thought and background builds stronger teams. We approach diversity and inclusion seriously and thoughtfully. We do not discriminate on the basis of race, religion, color, ancestry, national origin, caste, sex, sexual orientation, gender, gender identity or expression, age, disability, medical condition, pregnancy, genetic makeup, marital status, or military service.

Job is open for no less than 7 days and will be removed when the position is filled.
```

* [Job listing](https://explore.jobs.netflix.net/careers/job/790298014065?&eventID=wy0mNaQWa)

```
Engineering Manager - Machine Learning for Content Personalization
Los Gatos, California, United States of America

Remote

1 item added
Job Requisition ID
AJRT43691
Job Posting Date
07-23-2024
Teams
Data Science & Analytics
Work Type
Onsite
Netflix is one of the world’s leading entertainment services with 278 million paid memberships in over 190 countries enjoying TV series, films and games across a wide variety of genres and languages. Members can play, pause and resume watching as much as they want, anytime, anywhere, and can change their plans at any time.

The Role

As Netflix continues to grow, we are venturing into exciting new frontiers of personalization to help our members find the content they will most enjoy. In particular, we’re seeking to expand the breadth of entertainment we can provide our members beyond movies and series to include games and live-streaming events. To do this, we need to enable our algorithms to recommend a broader range of content both by extending our existing approaches and taking on the unique challenges of different types of entertainment.

We are looking for a Manager to lead the Content Personalization Algorithms Engineering team. You will lead the way for a team of machine learning engineers and researchers to develop the next generation of algorithms that are capable of recommending from a wider selection of content. This includes being able to respond quickly to trending live events and using bootstrapping or transfer learning to personalize new entities within our system. It also involves enhancing our system’s understanding of the unique aspects of the content that we recommend.

In this role, you will be responsible for building and leading a team of world-class engineers and researchers doing cutting-edge applied machine learning. You will cultivate a vision and strategy for the team aligned with our mission and guide innovation projects from end-to-end: idea to production A/B tests. Your team will be responsible for improving our core recommendation algorithms as well as developing new ones, working in conjunction with many other teams spanning personalization, serving, product management, machine learning platforms, data engineering, data science, different content areas, and more. To be successful in this role, you need to have a strong machine learning and engineering background, be data-driven, have a passion for personalization, have an execution focus, a love of learning, and have the ability to partner well with multi-disciplinary, cross-functional teams and stakeholders. You also need to be great at giving and receiving feedback, championing new ideas, fostering an inclusive team culture, mentoring, empowering others, and balancing the needs of both engineering and research.

What we are looking for:

Experience building and leading a team of machine learning engineers and researchers.
A track record of leading successful real-world applications of machine learning.
Ability to lead in alignment with our unique culture.
Broad knowledge of machine learning with a strong mathematical foundation.
Strong understanding of software engineering and large-scale distributed systems.
Great interpersonal skills.
MS or PhD in Computer Science, Statistics, or a related field.
You will ideally have experience with:

10+ years of total experience including 5+ years of machine learning management.
Leading teams focused on Personalization, Search, or Recommender Systems.
Deep Learning, Ranking, LLMs, or Bandits/Reinforcement Learning.
Experience working on large-scale, consumer-facing machine-learning applications.
Our compensation structure consists solely of an annual salary; we do not have bonuses. You choose each year how much of your compensation you want in salary versus stock options. To determine your personal top of market compensation, we rely on market indicators and consider your specific job family, background, skills, and experience to determine your compensation in the market range. The range for this role is $190,000 - $920,000.

 

Netflix provides comprehensive benefits including Health Plans, Mental Health support, a 401(k) Retirement Plan with employer match, Stock Option Program, Disability Programs, Health Savings and Flexible Spending Accounts, Family-forming benefits, and Life and Serious Injury Benefits. We also offer paid leave of absence programs. Full-time hourly employees accrue 35 days annually for paid time off to be used for vacation, holidays, and sick paid time off. Full-time salaried employees are immediately entitled to flexible time off. See more detail about our Benefits here.

 

Netflix is a unique culture and environment. Learn more here. 

We are an equal-opportunity employer and celebrate diversity, recognizing that diversity of thought and background builds stronger teams. We approach diversity and inclusion seriously and thoughtfully. We do not discriminate on the basis of race, religion, color, ancestry, national origin, caste, sex, sexual orientation, gender, gender identity or expression, age, disability, medical condition, pregnancy, genetic makeup, marital status, or military service.
```

## End Data Quality

## Data Platform

## Evan Cox/ Faisal Siddique - MetaFlow

* [His 100 days](https://www.linkedin.com/pulse/netflix-going-places-faisal-zakaria-siddiqi/)
* 30 min call 3-3:30
  1) Metaflow
  2) Amazon Music , Oracle
  3) FNR, culture, book stories, Reed Hastings
  4) Faisal specifics

* Here’s a quick overview of the covered frameworks:
* Apache Airflow is a popular open source workflow management system that was released by Airbnb in 2015. It is implemented in Python and uses Python to define workflows. Multiple commercial vendors, including AWS and GCP, provide managed Airflow as a service.
* Luigi is another well-known Python-based framework that was open sourced by Spotify in 2012. It is based on the idea of dynamic DAGs, defined through data dependencies.
* Kubeflow Pipelines is a workflow system embedded in the open source Kubeflow framework for data science applications running on Kubernetes. The framework was published by Google in 2018. Under the hood, the workflows are scheduled by an open source scheduler called Argo that is popular in the Kubernetes ecosystem.
* AWS Step Functions is a managed, not open source, service that AWS released in 2016. DAGs are defined in the JSON format using Amazon States Language. A unique feature of Step Functions is that workflows can run for a very long time, up to a year, relying on the guarantees of high availability provided by AWS.
* Metaflow is a full-stack framework for data science applications, originally started by the author of this book and open sourced by Netflix in 2019. Metaflow focuses on boosting the productivity of data scientists holistically, treating workflows as a first-class construct. To achieve scalability and high availability, Metaflow integrates with schedulers like AWS Step Functions.

## Tools

* Michaelangelo - Uber

### Python ML Infrastructure

### Ray.io

* Scale a single component of an existing ML pipeline
* Build an end to end ML application
* Build an ML platform
* Each of Ray’s five native libraries distributes a specific ML task:
  + Data: Scalable, framework-agnostic data loading and transformation across training, tuning, and prediction.
  + Train: Distributed multi-node and multi-core model training with fault tolerance that integrates with popular training libraries.
  + Tune: Scalable hyperparameter tuning to optimize model performance.
  + Serve: Scalable and programmable serving to deploy models for online inference, with optional microbatching to improve performance.
  + RLlib: Scalable distributed reinforcement learning workloads.

### Horovod

* Distribute model training: servers, networking, containers, hardware
* Horovod is a distributed deep learning framework developed by Uber Technologies. It’s designed to efficiently scale out the training of deep neural networks across multiple GPUs or multiple machines.

1. **Distributed Training**: Horovod enables distributed training of deep learning models by leveraging techniques like distributed gradient averaging and message passing interface (MPI). This allows the workload to be spread across multiple GPUs or multiple machines, significantly reducing the training time for large models.
2. **Single-Ring Allreduce**: One of the key components of Horovod is its use of the single-ring allreduce algorithm. Allreduce is a collective communication operation commonly used in distributed computing to synchronize data across multiple processes. In the context of deep learning, allreduce is used to aggregate gradients computed on different workers during training. The single-ring allreduce algorithm used by Horovod is highly optimized for performance and efficiency.
3. **Integration with Deep Learning Frameworks**: Horovod seamlessly integrates with popular deep learning frameworks like TensorFlow, PyTorch, and MXNet. This integration allows users to leverage the distributed training capabilities of Horovod without having to make significant changes to their existing codebase.
4. **Ease of Use**: Horovod is designed to be easy to use, with a simple API that abstracts away much of the complexity of distributed training. Users can typically convert their single-GPU training scripts to distributed training scripts with just a few lines of additional code.
5. **Scalability**: Horovod is highly scalable and can efficiently distribute training workloads across hundreds or even thousands of GPUs. This makes it well-suited for training large-scale deep learning models on massive datasets.

In summary, Horovod is a powerful distributed deep learning framework that enables efficient scaling of training workloads across multiple GPUs or machines. It’s widely used in both industry and academia for training state-of-the-art deep learning models.

### Kubernetes

* Kubernetes can facilitate the deployment and management of infrastructure
* Kubeflow for making deployment of ML workflows on K8 simple

### XGBoost

* Robust ML algorithm that can help you understand your data and is based off of gradient boosting decision trees
* Also helps with classification and regression models training

### Other

* ETL:
  + Mage
  + Prefect
  + Dagster
  + Fivetran
  + Airbyte
  + Astronomer
* Streaming pipelines:
  + Voltron Data
  + Confluent
* Analytics:
  + Starburst
  + Preset
* Data Quality:
  + Gable
  + dbt Labs
  + Great Expectations
  + Streamdal
* Data Lake and Data Warehouse
  + Tabular
  + Firebolt

### Google AutoML

* **Model Development**: Google AutoML shines in automating the model development process. It provides a user-friendly interface and process for selecting the best ML model and tuning its hyperparameters without requiring deep ML expertise. It’s particularly effective for users who need quick results in domains like vision, language, and structured data without delving into the complexities of model architecture and optimization.
* **Training and Evaluation**: AutoML handles the training and evaluation process, automatically managing resources and scaling as needed. It also provides easy access to performance metrics to assess the model’s quality.
* **Deployment**: It simplifies the deployment of models for predictions, offering seamless integration with other Google Cloud services for hosting and serving the model.

### Amazon SageMaker Autopilot

* **Data Preprocessing and Feature Engineering**: Autopilot automatically preprocesses tabular data and performs feature engineering, making it easier to prepare data for model training.
* **Model Development**: Similar to Google AutoML, SageMaker Autopilot automates model selection and hyperparameter tuning. It goes a step further by providing an explainable AI feature, offering insights into the automated decisions made during the model creation process.
* **Training and Evaluation**: Autopilot manages the training and evaluation, automatically optimizing compute resources. It also allows users to dive into the automatically generated Jupyter notebooks to understand and modify the training process.
* **Deployment**: SageMaker Autopilot facilitates the deployment of models into production environments within AWS, including setting up endpoints for real-time predictions or batch processing.

### Metaflow

```
# pip install metaflow
```

* **Workflow Management**: Metaflow is designed to manage the entire ML workflow, from data ingestion and preprocessing to model training and deployment. It provides tools for building, orchestrating, and monitoring ML workflows, with a focus on making the process reproducible and scalable.
* **Experiment Tracking**: Metaflow automatically versions your experiments and data, making it easy to track, reproduce, and rollback changes across the ML workflow.
* **Resource Management**: It abstracts away the complexities of infrastructure management, allowing data scientists to easily run their workflows on various compute backends (local, cloud, or hybrid) without worrying about the underlying resources.
* **Deployment**: While Metaflow doesn’t directly handle model deployment in the same way as AutoML services, it integrates with AWS services to facilitate deploying models to production. It provides a robust foundation for building custom deployment pipelines.
* In the engineering point of view, Metaflow acts as a substrate for integrations rather than as an attempt to reinvent individual layers of the stack. Companies have built or bought great solutions for data warehousing, data engineering, compute platforms, and job scheduling, not to mention the vibrant ecosystem of open source machine learning libraries. It would be unnecessary and unproductive to try to replace the existing established systems to accommodate the needs of data scientists. We should want to integrate data science applications into the surrounding business systems, not isolate them on an island.
* Metaflow is based on a plugin architecture that allows different backends to be used for different layers of the stack, as long as the layers can support a set of basic operations. In particular, Metaflow is designed to be a cloud-native framework, relying on basic compute and storage abstractions provided by all major cloud providers.
* Metaflow has a gentle adoption curve. You can get started with the “single-player mode” on a laptop and gradually scale the infrastructure out to the cloud as your needs grow. In the remaining sections of this chapter, we will introduce the basics of Metaflow. In the chapters to follow, we will expand its footprint and show how to address increasingly complex data science applications, spanning all the layers of the stack, and enhance collaboration among multiple data scientists.
* If you want to build your infrastructure using other frameworks instead of Metaflow, you can read the next sections for inspiration—the concepts are applicable to many other frameworks, too—or you can jump straight in to chapter 4, which focuses on a foundational layer of the stack: compute resources.

### Summary

* **Google AutoML** and **Amazon SageMaker Autopilot** primarily assist in the model development phase, including data preprocessing, model selection, training, evaluation, and deployment, with a strong emphasis on automating these processes to minimize the need for ML expertise.
* **Metaflow** provides comprehensive support across the entire ML workflow, focusing on workflow management, experiment tracking, and resource management. It’s more about enabling data scientists to structure and scale their ML processes rather than automating the model development process.

The choice between these tools depends on whether the priority is on automating model development (AutoML and Autopilot) or managing and scaling ML workflows (Metaflow).

* To define a workflow in Metaflow, you must follow these six simple rules:

1. A flow is defined as a Python class that is derived from the FlowSpec class. You can name your flows freely. In this book, by convention the flow class names end with a Flow suffix, as in HelloWorldFlow. You can include any methods (functions) in this class, but methods annotated with @step are treated specially.
2. A step (node) of the flow is a method of the class, annotated with the @step decorator. You can write arbitrary Python in the method body, but the last line is special, as described next. You can include an optional docstring in the method, explaining the purpose of the step. After the first example, we will omit docstrings to keep listings concise in the book, but it is advisable to use them in real-life code.
3. Metaflow executes the method bodies as an atomic unit of computation called a task. In a simple flow like this, there is a one-to-one correspondence between a step and a task, but that’s not always the case, as we will see later in section 3.2.3.
4. The first step must be called start, so the flow has an unambiguous starting point.
5. The edges (arrows) between steps are defined by calling self.next (step\_name) on the last line of the method, where step\_name is the name of the next step to be executed.
6. The last step must be called end. Because the end step finishes the flow, it doesn’t need a self.next transition on the last line.
7. One Python file (module) must contain only a single flow. You should instantiate the flow class at the bottom of the file inside an if **name** == ‘**main**’ conditional, which causes the class to be evaluated only if the file is called as a script.

* Timestamp denotes when the line was output. You can take a look at consecutive timestamps to get a rough idea of how long different segments of the code take to execute. A short delay may occur between a line being output and the minting of a timestamp, so don’t rely on the timestamps for anything that requires accurate timekeeping.
* The following information inside the square brackets identifies a task:
  + Every Metaflow run gets a unique ID, a run ID.
  + A run executes the steps in order. The step that is currently being executed is denoted by step name.
  + A step may spawn multiple tasks using the foreach construct (see section 3.2.3), which are identified by a task ID.
  + The combination of a flow name, run ID, step name, and a task ID uniquely identifies a task in your Metaflow environment, among all runs of any flow. Here, the flow name is omitted because it is the same for all lines. We call this globally unique identifier a pathspec.
  + Each task is executed by a separate process in your operating system, identified by a process ID, aka pid. You can use any operating system-level monitoring tools, such as top, to monitor resource consumption of a task based on its process ID.
  + After the square bracket comes a log message, which may be a message output by Metaflow itself, like “Task is starting” in this example, or a line output by your code.
* What’s the big deal about the IDs? Running a countless number of quick experiments is a core activity in data science—remember the prototyping loop we discussed earlier. Imagine hacking many different variations of the code, running them, and seeing slightly different results every time. After a while, it is easy to lose track of results: was it the third version that produced promising results or the sixth one?
* In the old days, a diligent scientist might have recorded all their experiments and their results in a lab notebook. A decade ago, a spreadsheet might have served the same role, but keeping track of experiments was still a manual, error-prone process. Today, a modern data science infrastructure keeps track of experiments automatically through an experiment tracking system.
* An effective experiment tracking system allows a data science team to inspect what has been run, identify each run or experiment unambiguously, access any past results, visualize them, and compare experiments against each other. Moreover, it is desirable to be able to rerun a past experiment and reproduce their results. Doing this accurately is much harder than it sounds, so we have dedicated many pages for the topic of reproducibility in chapter 6.
* Standalone experiment tracking products can work with any piece of code, as long as the code is instrumented appropriately to send metadata to the tracking system. If you use Metaflow to build data science applications, you get experiment tracking for free—Metaflow tracks all executions automatically. The IDs shown earlier are a part of this system. They allow you to identify and access results immediately after a task has completed.
* We will talk more about accessing past results in section 3.3.2, but you can get a taste by using the logs command, which allows you to inspect the output of any past run. Use the logs command with a pathspec corresponding to the task you want to inspect. For instance, you can copy and paste a pathspec from the output your run produces and execute the next command:

## Metaflow specs

* Metaflow automatically persists all instance variables, that is, anything assigned to self in the step code. We call these persisted instance variables artifacts. Artifacts can be any data: scalar variables, models, data frames, or any other Python object that can be serialized using Python’s pickle library. Artifacts are stored in a common data repository called a datastore, which is a layer of persisted state managed by Metaflow. You can learn more about the datastore later in this chapter in the sidebar box, “How Metaflow’s datastore works.”
* Each task is executed as a separate process, possibly on a separate physical computer. We must concretely move state across processes and instances.
* Runs may fail. We want to understand why they failed, which requires understanding of the state of the flow prior to the failure. Also, we may want to restart failed steps without having to restart the whole flow from the beginning. All these features require us to persist state.
* Volume—We want to support a large number of data science applications.
* Velocity—We want to make it easy and quick to prototype and productionize data science applications.
* Validity—We want to make sure that the results are valid and consistent.
* Variety—We want to support many different kinds of data science models and applications.
* Batch processing vs. stream processing
  + An alternative to batch processing, which deals with discrete units of computation, is stream processing, which deals with a continuous stream of data. Historically, the vast majority of ML systems and applications requiring high-performance computing have been based on batch processing: data goes in, some processing is done, and results come out.
  + During the past decade, increased sophistication of applications has driven demand for stream processing, because it allows results to update with a much lower delay, say, in a matter of seconds or minutes, in contrast to batch jobs, which are typically run at most once an hour. Today, popular frameworks for stream processing include Kafka, Apache Flink, or Apache Beam. In addition, all major public cloud providers offer stream-processing-as-a-service, such as Amazon Kinesis or Google Dataflow.
  + Fortunately, the choice is not either/or. You can have an application use the two paradigms side by side. Many large-scale ML systems today, such as the recommendation system at Netflix, are mostly based on batch processing with some stream processing included for components that need to update frequently.
* PRODUCTIVITY TIP Containers boost productivity by granting users the freedom to experiment without having to fear that they can break something by accident or interfere with their colleagues’ work. Without containers, a rogue process can hog an arbitrary amount of CPU or memory or fill the disk, which can cause failures in neighboring but unrelated processes on the same instance. Compute- and data-intense machine learning processes are particularly prone to these issues.

```
helloworld.py logs 1609557277904772/start/1
```

* You should see a line of output that corresponds to the print statement in the step you inspected. The logs subcommand has a few options, which you can see by executing logs –help.
* Finally, notice how Metaflow turns a single Python file into a command-line application without any boilerplate code. You don’t have to worry about parsing command-line arguments or capturing logs manually. Every step is executed as a separate operating system-level subprocess, so they can be monitored independently. This is also a key feature enabling fault tolerance and scalability, as we will learn in chapter 4.

## comparision

Creating a highly detailed and technical table comparing the systems you’ve mentioned would exceed the text limitations here. Instead, I can provide a concise comparison touching on the creators, best use cases, and key technical details for each system.

1. **Metaflow**:
   * **Creator**: Netflix
   * **Best Used For**: Simplifying the building and managing of data science projects from prototype to production.
   * **Key Details**: Provides easy scaling, integrates with AWS, version control for data science experiments, Python and R API support.
2. **Apache Airflow**:
   * **Creator**: Airbnb
   * **Best Used For**: Scheduling and orchestrating complex, multi-step data pipelines.
   * **Key Details**: Supports DAGs for workflow orchestration, has a rich UI for monitoring, extensible with custom operators, supports numerous integrations.
3. **Luigi**:
   * **Creator**: Spotify
   * **Best Used For**: Batch job orchestration with dependency resolution.
   * **Key Details**: Python-based, handles dependency resolution, task visualization, failure recovery, and command line integration.
4. **MLflow**:
   * **Creator**: Databricks
   * **Best Used For**: Managing the machine learning lifecycle, including experimentation, reproducibility, and deployment.
   * **Key Details**: Offers tracking of experiments, packaging code into reproducible runs, and model sharing and collaboration.
5. **Kubeflow**:
   * **Creator**: Google
   * **Best Used For**: Deploying and orchestrating machine learning workflows in Kubernetes.
   * **Key Details**: Kubernetes-native, supports a variety of ML tools, serves models at scale, and facilitates end-to-end ML workflows.
6. **AWS Step Functions**:
   * **Creator**: Amazon Web Services
   * **Best Used For**: Serverless orchestration for AWS services to automate processes and workflows.
   * **Key Details**: Manages state transitions at scale, integrates with AWS ecosystem, visually manage workflows, supports error handling and retries.
7. **Ray.io**:
   * **Creator**: UC Berkeley’s RISELab
   * **Best Used For**: High-performance distributed computing for machine learning and other intensive workloads.
   * **Key Details**: Offers simple APIs for building and running distributed applications, supports dynamic task graphs, and provides scalability.
8. **Uber’s Michelangelo**:
   * **Creator**: Uber
   * **Best Used For**: Deploying and operating machine learning models at scale.
   * **Key Details**: End-to-end ML platform, supports training, deployment, and managing of ML models, integrates with Uber’s data and infrastructure.
9. **Horovod**:
   * **Creator**: Uber
   * **Best Used For**: Distributed training of deep learning models.
   * **Key Details**: Open-source, works with TensorFlow, Keras, and PyTorch, supports GPU training, and integrates with Kubernetes and Spark.
10. **AutoML**:
    * **Creator**: Varied, as AutoML is a category of tools rather than a single system (e.g., Google’s AutoML).
    * **Best Used For**: Automating the process of applying machine learning to real-world problems.
    * **Key Details**: Provides a suite of tools to automatically train and tune models, requiring minimal human intervention.

* **Apache Airflow**
* **Pros**:
  + Extensive scheduling capabilities.
  + Rich set of integrations with various data sources and services.
  + Strong community support, with a large number of contributors.
* **Cons**:
  + Complexity in setup and management, steep learning curve.
  + No built-in support for machine learning workflows.
* **Metaflow**
* **Pros**:
  + Designed with data scientists in mind, focuses on ease of use.
  + Integrates seamlessly with AWS for scaling and deployment.
  + Built-in data versioning and experiment tracking.
* **Cons**:
  + Less suitable for non-ML batch workflows.
  + Mainly tailored for AWS, which might not fit all cloud strategies.
* **Luigi**
* **Pros**:
  + Simplicity in defining workflows, with a focus on dependency resolution.
  + Good for Python-centric teams due to its integration with Python’s ecosystem.
* **Cons**:
  + Not as feature-rich as Airflow for complex task orchestration.
  + Limited capabilities for real-time processing.
* **MLflow**
* **Pros**:
  + Comprehensive platform for the entire ML lifecycle management.
  + Language agnostic with APIs for Python, R, Java, and REST.
* **Cons**:
  + Primarily an ML lifecycle tool, not a general workflow orchestrator.
  + Might require additional tools for complete end-to-end automation.
* **Kubeflow**
* **Pros**:
  + Kubernetes-native, leveraging container orchestration for ML workflows.
  + Supports a wide range of ML tools and frameworks.
* **Cons**:
  + Can be complex to set up and manage, requiring Kubernetes expertise.
  + Overhead might be too high for smaller projects or teams.
* **AWS Step Functions**
* **Pros**:
  + Serverless orchestration service, highly scalable and reliable.
  + Direct integration with many AWS services.
* **Cons**:
  + Locked into the AWS ecosystem, less ideal for hybrid or multi-cloud environments.
  + Pricing can become significant at scale.
* **Ray.io**
* **Pros**:
  + Excellent for distributed computing, offering easy scaling.
  + Supports a variety of machine learning and AI libraries.
* **Cons**:
  + More suitable for teams with distributed computing needs.
  + Might be too complex for simple, localized tasks.
* **Michelangelo**
* **Pros**:
  + Provides a full-stack solution for ML model building and deployment.
  + Suitable for large-scale, enterprise-grade ML deployments.
* **Cons**:
  + Details about Michelangelo are less publicly documented as it’s an internal Uber tool.
  + May not be accessible for smaller teams or organizations.
* **Horovod**
* **Pros**:
  + Efficient distributed training, especially with GPU support.
  + Works with popular deep learning frameworks like TensorFlow and PyTorch.
* **Cons**:
  + Primarily focused on model training, not a full workflow management tool.
  + Requires additional infrastructure for large-scale training.
* **AutoML (e.g., Google Cloud AutoML)**
* **Pros**:
  + Great for automating the development of ML models.
  + Accessible to non-experts and provides fast results.
* **Cons**:
  + Less control over the modeling process, which might not suit all advanced use cases.
  + Can be costly depending on the provider and usage.

For large-scale teams, it’s crucial to consider factors like the complexity of workflows, the team’s technical expertise, integration with existing tech stacks, scalability requirements, and the specific nature of data processing or ML tasks when choosing between these tools.

## Ville tutorial

* Here are the main technical points from Ville Tuulos’s talk on “Effective Data Science Infrastructure”:
* **Motivation from Netflix Experience**: Ville’s motivation for writing the book came from his experience leading the machine learning infrastructure team at Netflix, where the diverse use cases for machine learning across the company highlighted the need for a common infrastructure to support various ML applications.
* **Need for Common Infrastructure**: The talk emphasizes the importance of building a common machine learning and data science infrastructure that can handle a wide range of use cases, from natural language processing to computer vision and business analytics.
* **Data Handling and Compute at Scale**: Central to effective data science infrastructure is the efficient management of data and the ability to run computations at scale, leveraging cloud resources when necessary.
* **Workflow Management**: Ville discusses the concept of workflows or Directed Acyclic Graphs (DAGs) for orchestrating complex machine learning processes, including data preprocessing, model training, and evaluation.
* **Versioning and Collaboration**: The ability to manage multiple versions of machine learning models and workflows, track experiments, and facilitate collaboration among data scientists and engineers is highlighted as a critical component of effective infrastructure.
* **Dependency Management**: The talk touches on the challenge of managing external dependencies in machine learning projects, ensuring reproducibility and stable execution environments despite the fast evolution of ML libraries and frameworks.
* **Prototyping to Production Continuum**: Ville proposes a continuum approach for moving machine learning projects from prototyping to production, emphasizing the importance of scalability, robustness, and automation in production-ready ML systems.
* **Cloud-based Workstations and Development Environments**: The use of cloud-based workstations for development is advocated to bridge the gap between prototyping and production environments, making the use of IDEs like Visual Studio Code for remote development.
* **Metaflow as a Reference Implementation**: The open-source framework Metaflow, developed at Netflix, is presented as a reference implementation for managing data, compute resources, workflows, versioning, and dependencies in machine learning projects.
* **Scheduled Execution and Production Readiness**: Ville concludes with the concept of scheduled execution for production workflows, leveraging AWS Step Functions for automated, robust, and scalable ML model deployment and monitoring.
* The talk provides a comprehensive overview of the essential elements required for setting up an effective data science infrastructure, drawing on Ville Tuulos’s extensive experience and the Metaflow framework.

## Compute types

* The figure depicts the following three projects, each with a workflow of their own:
* Project 1 is a large, advanced project. It needs to process a large amount of data, say a text corpus of 100 GB, and train a massive deep neural network model based on it. First, large-scale data processing is performed with Spark, which is optimized for the job. Additional data preparation is performed on a large instance managed by AWS Batch. Training a large-scale neural network requires a compute layer optimized for the job. We can use Amazon SageMaker to train the model on a cluster of GPU instances. Finally, we can send a notification that the model is ready using a lightweight task launched on AWS Lambda.
* Project 2 trains a decision tree using a medium-scale, say, 50 GB, dataset. We can process data of this scale, train a model, and publish results, on standard CPU instances with, say, 128 GB of RAM. A general-purpose compute layer like AWS Batch can handle the job easily.
* Project 3 represents an experiment conducted by a data scientist. The project involves training a small model for each country in the world. Instead of training 200 models sequentially on their laptop, they can parallelize model training using AWS Lambda, speeding up their prototyping loop.
* As figure 4.9 illustrates, the choice of compute layers depends on the type of projects you will need to support. It is a good idea to start with a single, general-purpose system like AWS Batch and add more options as the variety of use cases increases.

## Infrastructure

* AutoML: Amazon SageMaker Autopilot
* Software consideration:

  + Realtime or Batch
  + Cloud vs Edge/Browser
  + Compute resources (CPU/ GPU/ memory)
  + Latency, throughput (QPS)
  + Logging
  + Security and privacy
  + Experiment tracking: Sagemaker Studio, Weights and Biases

* Common Deployment case: Gradual ramp up with monitoring / Rollback
  + New product/ capability:
    - Shadow mode: ML system shadows the human and runs in parallel but output is not used for any decision
  + Automate/assist with manual task:
    - Canary deployment: run only on small fraction of traffic initially. Monitor system and ramp up traffic gradually
  + Replace previous ML system:
    - Blue / Green deployment: Blue old version, Green new version, have router go from blue to green w/ easy way to rollback. Can also use with gradual dial up.

* **Success Criteria**: Enable our Scientists and Engineers to try out and test, offline experiments as fast as possible, from ideation to productionization. The infrastructure should support rapid iteration, high-performance computing, and efficient data management.
* **Model Selection**:
  + **Ray**: An open-source framework that provides a simple, universal API for building and running distributed applications. It’s used for parallel and distributed computing, making it suitable for training and serving ML models at scale. Ray supports model selection by enabling parallel experiments and hyperparameter tuning.
  + **Amazon SageMaker**: Provides a comprehensive environment for building, training, and deploying machine learning models at scale. It supports direct integration with Ray for distributed computing.
* **Data**:
  + **Fact Store**: Immutable data at Netflix
  + **Cassandra**: A distributed NoSQL database known for its scalability and high availability without compromising performance. Suitable for managing the Fact Store where read and write throughput is critical.
  + **S3**: Amazon Simple Storage Service (S3) is a scalable, high-speed, web-based cloud storage service. It’s used for storing and retrieving any amount of data at any time, ideal for large datasets used in ML.
  + **Parquet Files**: A columnar storage file format optimized for use with big data processing frameworks like Hadoop and Spark. It’s efficient for both storage and computation, making it ideal for storing large datasets that need to be processed for ML.
  + **Fact Store**: Immutable data at Netflix
  + **Amazon DynamoDB**: A fast and flexible NoSQL database service for any scale. It can complement Cassandra for managing immutable data, offering seamless scalability and integration with other AWS services.
  + **Amazon S3**: Already mentioned, it’s the backbone for storing vast amounts of data in a durable, accessible, and scalable way.
  + **Amazon FSx for Lustre**: A high-performance file system optimized for fast processing of large datasets, which can be used alongside or as an alternative to HDFS in some contexts. It integrates well with S3 for storing and processing large-scale datasets.
* **Train/ ML Pipeline automation**:
  + **Apache Spark**: A unified analytics engine for large-scale data processing. It’s used for data preparation, feature extraction, and ML model training, especially when dealing with large datasets.
  + **TensorFlow**: An open-source framework for numerical computation and machine learning. TensorFlow can be used within pipelines for model training and inference, leveraging its comprehensive ecosystem for deep learning.
  + **Workflow Scheduling**: Tools like Apache Airflow or Prefect can be used to automate and manage the ML pipeline workflows, ensuring that data processing, model training, and other tasks are executed in a reliable and scalable manner.
  + **Training Pipeline**: This refers to the entire process of data preparation, model training, validation, and testing. Tools like TensorFlow Extended (TFX) could be integrated here for end-to-end machine learning pipeline capabilities.
  + **AWS Step Functions**: Can orchestrate AWS services, automate workflows, and hence, manage ML pipelines efficiently. It provides a reliable way to coordinate components of the training pipeline.
  + **AWS Glue**: A fully managed extract, transform, and load (ETL) service that makes it easy for preparing and loading data for analytics. It can be used for data preparation stages in ML pipelines.
  + **Amazon SageMaker (for Training Pipeline)**: Facilitates the creation, training, and tuning of machine learning models. Provides a fully managed service that covers the entire machine learning workflow.
* **Serve**:
  + **Ray** or **Flink**: For serving models, especially in real-time applications. Flink provides high-throughput, low-latency streaming data processing and can be used for real-time model inference.
  + **EV Cache**: An in-memory caching solution that can be used to store pre-computed model predictions or feature vectors for fast retrieval during model inference, enhancing performance.
  + **Amazon SageMaker (for Serving)**: Enables developers to easily deploy trained models to production so they can start generating predictions (also known as inference).
  + **Amazon ElastiCache**: Similar to EV Cache, ElastiCache supports in-memory caching to enhance the performance of model inference by caching results or frequently accessed data.
* **Maintain**:
  + **Hadoop**: A framework that allows for the distributed processing of large data sets across clusters of computers. It’s useful for data storage and processing, supporting the infrastructure’s maintenance, especially for large-scale data.
  + **Presto** and **Hive**: Both are query engines but serve different purposes. Presto is used for interactive querying, while Hive is more suited for batch processing jobs. They can be used for data analysis and maintenance tasks, such as monitoring data quality and performance.
  + **Amazon CloudWatch**: Offers monitoring and observability of AWS cloud resources and applications, crucial for maintaining the health and performance of ML infrastructure.
  + **AWS Lake Formation**: Builds, secures, and manages data lakes. It simplifies data ingestion, cataloging, and cleaning, supporting the maintenance of a clean, well-organized data repository.
* **Model A/B Testing**:
  + **Ablaze A/B Testing**: A tool specifically designed for conducting A/B testing in machine learning models. It helps in evaluating the performance of different model versions in a production environment, facilitating data-driven decision-making.
  + **Amazon SageMaker (A/B Testing)**: Supports A/B testing natively, allowing users to easily compare different model versions directly within the service.
* **Deployment**:
  + **ONNX (Open Neural Network Exchange)**: Facilitates model deployment by providing an open standard for representing ML models. This allows models to be shared between different ML frameworks, easing deployment processes.
  + **AWS Lambda**: For running inference code without managing servers. It can be triggered by events, making it suitable for lightweight, real-time inference needs.
  + **Amazon EKS (Elastic Kubernetes Service) or Amazon ECS (Elastic Container Service)**: For deploying containerized applications, including machine learning models, at scale.
* **Inference**:
  + **Real-Time Stream**: Technologies like Apache Kafka can be used to handle real-time data streams for model inference, enabling applications to process data and make predictions in real-time.
  + **Amazon Kinesis**: For real-time data streaming and processing, enabling real-time analytics and inference on data in motion.
  + **Amazon SQS and SNS**: For message queuing and notifications, facilitating asynchronous communication between different parts of the ML infrastructure, especially useful in decoupling ingestion and processing.
* **Data Drift**:
  + **Marken**: Although not a widely recognized tool in the public domain (as of my last update), in the context of ML infrastructure, tools designed to monitor data drift are critical. They evaluate how the model’s input data distribution changes over time, potentially impacting model performance.
  + **Amazon CloudWatch** and **Amazon SageMaker Model Monitor**: For monitoring the performance of machine learning models and detecting data drift, ensuring models remain accurate over time.

## Below are the areas of focus:

* Technical Screen: You’ll be asked to participate in a system design exercise and discussion.
* Culture Alignment: The value of people over process is integrated into all aspects of our roles. We’ll be assessing your ability to thrive in this type of environment and the overall Netflix culture.
* Team Partnership: You’ll meet with a team member to discuss how you collaborate as a leader on a broad scale.
* Metaflow Partnership: You’ll meet with internal customers of Metaflow and will evaluate your ability to partner with them.

## Q’s

* What was the most challenging project you have worked on?
* ## Increase experimentation velocity via configurable, modular flows. Amazon Music personalization, North - South Carousels
* Flows: allows swapping out models with ease w/in the config file
* Implement data from S3 via DataSource
* SageMaker inference toolkit
* Ideation -> productionization time reduce
* Repetitve manual effort due to complex, fragmented code process
  + One of the most challenging projects I’ve had to work on is creating a unified infrastructure for Amazon Music.
  + S: So the Amazon entertainment suite, Music, Prime Video, Audible, Wondery Podcast, we cross collaborate often. There’s a lot of cross-functional, item-to-item recommendation systems we run that help both products.
  + In this case, we wanted to collaborate with Prime Video, Taylor Swift is a big artist on our platform and she’s recently done a tour which she’s made into a movie and whenever the user pauses, they basically should have a link back to Music to listen to that song/ playlist. For many artists, as well as original shows that have playlists on our app.
  + T: Our task was to collaborate, in the past, to get from research to production for us would be a fairly long process, just to get from research to productionization takes months.
    - Every single team has their own approach to go to prod from research. Own pipelines/ tooling platform for common tasks
    - Lack of standardized metrics and analysis tools: calculating position
    - Lack of established component APIs: Each model would have it’s own APIs so to switch out the model, would require a lot of work to adapt the model to the existing interface
    - Feature engineering inside the model, makes the model not transferrable
    - Metrics: not measuring
    - Research - python tooling, prod: Scala/ Java code -> ONNX. Checking in code, setting in pipelines, periodic flows needed in prod, monitoring steps. Was model in research same as in prod, are we measuring it the same
    - Two different pipelines, environment variables in different files, dynamo db has configs everywhere, different clusters, EMR jobs, hard to test change isn’t breaking anything. Time to onboard was too long, too many tooling. New processes.
    - Bottom line was, we were not able to get from prototype to production with high velocity which was stifling our need for increased experimentation.
  + A: This was our current norm, we would make snowflake/ unique but repetitive fixes for each collaboration we did. We would have different env variables, clusters, components that we would have to rebuild just for this project. Time to onboard was long, too much tooling here. Outside of this, we also needed to configure regular jobs, retries, monitoring, cost analysis needed to be set up, data drift checks.
  + Our original methodology included creating a new pipeline for each project, we were maintaining as you can imagine, quite a few pipelines in quite a few environments.
  + This was inefficient, I wanted to create a solution that would be less problem specific and more easy to be reusable. I wanted to change the way we do things. This overhead was neither good for our customers, it stifles experimentation, nor was it good for our data scientists, to be working on repetitive non creative tasks. Thats not why we hired them.
  + As part of this collaboration, I wanted to fix this bottleneck of course, along with our cross collaborators and team members.
  + Researched a few options out in the market as well as custom solutions. Airflow, Metaflow
  + R: Our eventual goal is to have a unified platform that the entire entertainment suite at Amazon can leverage
  + R:
* When did you question the status quo?
  + Daily update meetings / project
    - The issue is when you have a daily meeting, it’s hard to come into the meeting with a proper agenda and make sure everyone’s time is respected. There are nominal movements within projects on an everyday basis.
    - Work with Program Managers, create excel sheets categorizing tasks, as well as Jira tickets, and sync up on a less frequent cadence. There should be a point/agenda to a meeting
* Can you share your experience working with distributed systems?
* Why do you want to switch jobs?
  + It’s not so much that I want to leave, it’s more so that I want to join Netflix and let me explain.
  + There are two pillars that I see are important for a manger, the culture and the technology and this role has both.
  + The FnR culture, the culture of candor and frequent constructive feedback, having people over processes. As a leader, I’m always striving to grow and seek how to improve
  + No rules, rules Reed Hastings. Ville Tuulos Effective Data Science Infrastructure
  + metaflow, glorious product
* How do you communicate with stakeholders?
  + how to gear the message towards the audience, audience intended messaging
* Which culture memo is your favorite and why?
  + FnR, Keepers Test, People over Process,
* Why do you like working in the internal tools team? (Noted that this was mentioned to fit in with their team)
* The assignment was to be an API aggregator
* HR specifically reminded me that you should focus on saying “I” more and “we” less when answering questions in the future. They emphasized that he’s a pretty good person.
  1. What aspects do you agree with in the Culture memo?
  2. What aspects do you disagree with, or what are the problems in the Culture memo?
  3. How do your teammates describe you?
  4. Could you elaborate on the constructive feedback (co) that you received?
  5. The first round can’t exactly be labeled as technical; it was more about HR behavioral aspects. Traditional behavioral issues are typically seen as HR matters.
  6. In the second round, a person asked a question about Java ConcurrentHashMap. The question wasn’t difficult, but since the interviewee had been using Go before, he was only somewhat familiar with ConcurrentHashMap, leading to an average performance in this round.
  7. After dinner, the interviewer from India asked me to design a database that stores time series data to support queries with specific conditions, such as finding the maximum value within a certain time period. This is a classic time series database design question, and there should be a lot of information on the Internet about it.
  8. A second interviewer from India discussed designing something similar to Netflix. (Note: The rest of the message seems to refer to a content access system based on points, which is unrelated to the interview context.)
* The overall interview was very good. The questions were all quite realistic, and there were no tricky brain-teasers. However, due to my lack of preparation or experience in certain areas, I didn’t perform as well as I hoped. It’s clear that Netflix sets a high bar for its engineers.
* The interview was with a group from Infra for a senior software engineer position:
* **First Round of Coding:**
* Task: Implement a rate limiter, which is a very common exercise. The goal might be to write a function that, for example, rejects calls if it is invoked more than 10 times in one second. Then, the question extended to how to implement a per-caller rate limiter in Java, involving multi-threading and locks.
* Another question involved merging two sorted arrays, which was not difficult.
* **Second Round of Coding:**
* Scenario: There are n students (0 to n-1) in the classroom, and each student has a best friend (one-way relationship; if A is B’s best friend, B is not necessarily A’s best friend).
* **Input:** A size n integer array M where M[i] is student i’s best friend.
* **Constraint:** Every student needs to sit next to his best friend.
* **Output:** The number of groups (students sitting together form a group) and how many students are in the largest group.
* **Example:** Given M: [1,0,3,4,5,2], 0 and 1 sit together, 2, 3, 4, 5 form a circle. Thus, there are 2 groups, with the largest group having 4 students.
* Few interviews on Netflix in Dili, with minimal experience on engineering management roles.
* Contributed one interview but often struggled with insufficient points, leading to a request for support.
* Received a referral from a previous colleague; the recruiter contacted swiftly the next day.
* First interview: a half-hour phone call with the recruiter focusing on behavioral issues. Essential to review the culture deck beforehand.
* Second interview: a half-hour call with the hiring manager, centered around management issues, not technical.
* Two rounds of on-site interviews followed:
  + The first on-site round involved meetings with the engineering group.
  + The second on-site round involved meetings with cross-functional and higher-level leaders.
* Three interviews were conducted in the first on-site round, with an initial expectation of system design discussions, which ultimately focused solely on behavioral aspects.
* Answers to questions were very general; regretted forgetting important points from the culture deck.
* No news yet from the first round of on-site interviews; hopeful for a positive outcome, otherwise considering a move to Facebook to start anew.
* Designing a counter system, like a view count or metrics tracker, involves several stages, starting from a single server on bare metal infrastructure and eventually scaling up to a cloud-based solution. This process is iterative and can vary significantly based on specific requirements, traffic expectations, and technological preferences. Here’s a structured approach to designing and scaling such a system:
* Initial Design on a Single Server (Bare Metal)

  + **Counter Storage**: Implement the counter using an in-memory data structure for fast read/write operations, such as a hash map where keys are resource identifiers (e.g., video IDs for view counts) and values are the counts.
  + **Persistence**: Periodically write the in-memory counts to a disk-based database to ensure durability. SQLite or a simple file-based storage could work at this scale.
  + **Concurrency Handling**: Use locks or atomic operations to manage concurrent accesses to the counter to ensure accuracy.
  + **Caching Strategy**: Implement caching to reduce read load, especially for frequently accessed counters.
* Scaling Up: Multi-Server Environment

  + **Data Partitioning (Sharding)**: As traffic grows, partition the data across multiple servers to distribute the load. This can be based on resource IDs or hash-based sharding.
  + **Load Balancing**: Introduce a load balancer to distribute incoming requests evenly across servers.
  + **Replication**: Implement replication for each shard to improve availability and fault tolerance.
  + **Consistency and Synchronization**: Employ consistency mechanisms like eventual consistency or stronger consistency models, depending on the requirement. This might involve distributed locks or consensus protocols in complex scenarios.
* Moving to the Cloud

  + **Leverage Managed Services**: Utilize cloud-native services for databases, caching, and load balancing to reduce management overhead. Services like Amazon RDS for databases, ElastiCache for caching, and Elastic Load Balancer can be beneficial.
  + **Auto-Scaling**: Implement auto-scaling for the application servers and databases based on load, ensuring that the system can handle spikes in traffic without manual intervention.
  + **Global Distribution**: If the audience is global, consider using a Content Delivery Network (CDN) for caching views at edge locations to reduce latency.
  + **Monitoring and Metrics**: Use cloud monitoring tools to track system performance, usage patterns, and potential bottlenecks. This data is crucial for making informed scaling decisions.
* Conversation-Driven Design Considerations

  + **Deep Dive on Assumptions**: Be prepared to discuss and justify every assumption, such as why a particular database or caching strategy was chosen.
  + **Component Justification**: For each component proposed, explain its role, how it fits into the overall architecture, and why it’s the best choice.
  + **Handling Failures**: Discuss strategies for dealing with component failures, data inconsistencies, and other potential issues that could arise during scaling.
  + **Security and Compliance**: Ensure that the design incorporates necessary security measures and complies with relevant data protection regulations, especially when moving to the cloud.
* This approach not only helps in tackling the technical challenges of scaling but also prepares you for a detailed discussion with an interviewer, demonstrating your ability to think critically about system design and scalability.
* Your description outlines a comprehensive interview process for a machine learning engineering position, starting from the initial resume submission to the onsite interview rounds. Here’s a structured summary:
* **Initial Steps:**
* **Resume Submission:** You submitted your resume online in mid-September.
* **Initial Appointment:** The recruiter scheduled a meeting at the hiring manager’s (HM) store within 3 days to assess if your work projects align with the job requirements.
* **Technical Screen:** One week after the initial appointment, a technical screening was arranged.
* **Technical Screening:**
* **Interviewer Background:** The interviewer, an Indian male ML engineer, recently graduated from Faye Wong University and has over 4 years of experience. He is described as very nice and specializes in causal inference.
* **Interview Focus:** The main part of the interview involved introducing an ML project followed by a discussion on statistics and ML through eight-part essays. Shortly after the interview, the recruiter contacted you for the onsite interview.
* **Onsite Interview:**
* **Overview:** The HM outlined a five-round onsite interview process, warning of a potential “sudden death” round in the middle.
* **Round 1 (Indian Uncle):** You were given two lists of movies/shows with various details from Faye Wong and a third party. The task involved writing code to find the closest matches and discussing how ML could solve real-world problems, deploy monitoring indicators, and design statistical tests.
* **Round 2 (Indian Lady):** Focused on recommendation systems and search functionalities, with detailed questions about handling scenarios encountered by Faye Wong. For instance, what to do if a searched movie is unavailable and how to leverage the recommendation algorithm and context information. The round concluded with coding questions on serializing and deserializing ML model parameters. You noted a contrast in friendliness compared to the male interviewer.
* **Round 3: Brother Xiaobai**
* **Interviewer Description:** Brother Xiaobai is described as looking very cool and cute. It’s unclear if this person is also from Faye Wong or another entity.
* **Interview Focus:** This round seems to involve Faye Wong’s dataset of movie/show pairs (title1, title2), representing the number of viewers of similar movies in different regions. Unfortunately, the description of the task or questions for this round was not completed.
* To provide a useful continuation or answer, I’d need more details about what Brother Xiaobai’s round involved. Was it a coding challenge, a discussion on handling large datasets, or perhaps a machine learning model design question related to viewer prediction or regional preferences analysis?
* **Additional Interview Focus with Brother Xiaobai or Subsequent Rounds:**
  + **Behavioral Questions (BQ):** The interviewer asked about your views on their company culture along with some general questions, indicating an interest in assessing cultural fit and personal values.
  + **Design Questions:** Surprisingly, the interview also included technical design questions, such as:
    - **A/B Testing:** Discussing approaches to conduct A/B tests, which are critical for evaluating new features or changes in a controlled manner.
    - **ML Deployment Issues:** Questions on machine learning deployment challenges, including best practices for deploying models into production.
  + **Data Monitoring:** A specific focus on how to monitor data drift, especially when true labels cannot be obtained in a timely manner, using tools like Metaflow or similar technologies. This implies a deep dive into managing model performance and reliability over time in real-world scenarios.
* **Closing Thoughts:**
* The interviewer conveyed a technically strong impression, reflecting a comprehensive assessment covering technical skills, cultural fit, and practical challenges in ML deployment and maintenance.
* The message ends with well-wishes for the New Year, hoping that the shared experiences will be beneficial to others and expressing optimism for receiving attractive job offers in the future.
* Design a distributed database that syncs across 3 regions and 3 zones within the regions.
  + Requirement: eventually consistent system
* Netflix/youtube offers multiple services. I am trying to design a system that counts how minutes watched on particular video, number of video watched completely and Category of videos most watched.
  + I am new to system design when it comes to complex designs. If you have any links or documents that would be helpful. I would appreciate your help in advance.

### The motivation

* Real-life production ML systems operate autonomously, reacting to new data and events automatically. Besides indvidual workflows, Metaflow allows you to build advanced reactive ML systems. For instance, you can trigger a workflow whenever new data is available:
* We’re spending way too much time on infrastructure and tooling
  + Parallelization/ orchestration is an issue
* Software engineers have great hygiene with git, but what about ML engineers?
  + Model Development
  + Feature Engineering
  + Model Operations in production
  + Versioning the data, the features, the models
  + Job schedulers
  + Compute resources
  + Data warehouse
* Ville Tuulos -> architect for MetaFlow / founder of Outerbounds

* Metaflow only cares about the bottom of the stack
* Metaflow UI, support for the other clouds, tagging (add a label to each run this run corresponds to production, git message)
* It provides a Python-based interface that simplifies the entire lifecycle of data science workflows, from data processing and experimentation to model deployment.
* With features like automatic versioning of experiments, easy scalability from a laptop to the cloud, and integration with existing data science tools, Metaflow focuses on enhancing the productivity of data scientists by abstracting away the complexities of infrastructure and pipeline management.
* This allows data scientists to concentrate more on data analysis and model building, rather than on the technical details of implementation and deployment.

### Competitors

* Luigi by Spotify (cant test locally)
* Airflow (how do I do compute, does not do versioning)

### Problems

* Which version of Tensorflow do we need

### What is Metaflow?

* Metaflow helps you access data, run compute at scale, and orchestrate complex sets of ML and AI workflows while keeping track of all results automatically. In other words, it helps you build real-life data, ML, and AI systems.

It is one thing to build systems and another to operate them reliably. Operations are hard because systems can misbehave or fail in innumerable ways; we need to quickly understand why and proceed to resolve the issue. The challenge is especially pronounced in data, ML, and AI systems, which can exhibit a cornucopia of failure patterns - some related to models, some to code, some to infrastructure, and many related to data.

* Workflow Orchestration : Metaflow helps structure data science projects by organizing the code into easily manageable, logical steps. It provides a way to define workflows, which are sequences of steps, each performing a specific task (e.g., data preprocessing, training a model).
* Code Execution on Various Platforms : While Metaflow itself doesn’t provide computational resources, it simplifies the process of running code on different platforms. It allows seamless switching from running code on a local machine to executing it on larger-scale cloud platforms like AWS.
* Automatic Data Versioning and Logging : Metaflow automatically versions and logs all data used and produced at each step of a workflow. This feature makes it easy to track experiments, reproduce results, and understand the flow of data through the various steps.
* Built-in Scaling and Resource Management : Metaflow can automatically scale workflows, handling resource allocation and parallelization. This means it can execute tasks on larger datasets and compute clusters without requiring significant changes to the code.
* Experiment Tracking and Debugging : With its built-in tracking and logging, Metaflow simplifies debugging and tracking the progress of experiments. Data scientists can easily access previous runs, inspect results, or compare different iterations of their models.
* Integration with Existing Data Tools : Metaflow is designed to work well with commonly used data science tools and libraries (like Jupyter, pandas, scikit-learn), allowing data scientists to continue using familiar tools while benefiting from the additional capabilities Metaflow provides.
* Simplified Deployment : Metaflow can package and deploy models, taking care of dependencies and environment configurations, which simplifies the process of moving a model from development to production.
* Plugin Architecture : Metaflow offers a plugin architecture, allowing for customization and extension. For example, while it doesn’t provide its own storage, it can be configured to interface with different storage solutions.
* In summary, Metaflow acts as a facilitator and orchestrator for data science projects. It provides the framework and tools to efficiently manage, execute, and track data science workflows, leveraging existing infrastructure (like AWS) for storage, computation, and other needs. Its primary aim is to make the life of a data scientist easier by abstracting away many of the complexities involved in running data science projects at scale.

### Metaflow observability

* [linked here](https://outerbounds.com/blog/metaflow-dynamic-cards/)

### Metaflow achieves its functionality through a combination of a well-designed Python library, a set of conventions and best practices for workflow design, and integration with underlying infrastructure, particularly cloud services. Here’s a closer look at how Metaflow accomplishes its objectives:

#### Python Library and API

* **Workflow Definition**: Metaflow provides a Python library that allows data scientists to define workflows as Python scripts. Each script can be broken down into steps, with each step representing a part of the data science process (like data loading, preprocessing, training models, etc.).
* **Decorators**: It uses decorators extensively to add additional functionalities to steps in the workflow. These decorators handle things like specifying resources required (CPU, memory), managing dependencies, and branching logic in the workflow.

#### Data Versioning and Logging

* **Automatic Versioning**: Metaflow automatically versions the data at each step of the workflow. This means every time a step is executed, the data inputs and outputs are logged and versioned.
* **Artifact Tracking**: It tracks all data used and produced in the workflow, known as “artifacts,” which can include datasets, models, or even intermediate variables.

#### Execution on Various Platforms

* **Local and Cloud Execution**: While you can run Metaflow on a local machine, it also integrates with cloud platforms (AWS in particular). Metaflow can execute workflows on AWS, managing tasks such as spinning up necessary compute instances and scaling resources as needed.
* **Containerization**: Metaflow can package workflows into containers, allowing for consistent execution environments, both locally and in the cloud.

#### Resource Management

* **Resource Allocation**: Metaflow allows you to specify the resources needed for each step (like CPU and memory). It manages the allocation of these resources, whether on a local machine or in the cloud.
* **Parallelization and Scaling**: For steps that can be executed in parallel (like training models with different hyperparameters), Metaflow can manage the parallel execution and scaling.

#### Experiment Tracking and Debugging

* **Metadata Service**: Metaflow maintains a metadata service to keep track of all runs and their corresponding data. This service enables easy tracking and comparison of different runs.
* **Debugging Support**: The framework provides tools to inspect previous runs, which is particularly useful for debugging and understanding the workflow’s behavior.

#### Integration with Cloud Services

* **AWS Integration**: Metaflow offers deep integration with AWS services. This includes using S3 for data storage, AWS Batch for compute tasks, and AWS Step Functions for orchestrating complex workflows.

#### Plugin Architecture

* **Customization**: The plugin architecture of Metaflow allows it to be extended and customized to fit specific needs. This could include integrating with different storage solutions, compute environments, or data processing tools.
* In essence, Metaflow automates and simplifies many of the routine but complex tasks associated with running data science projects. Its design is focused on making these tasks as seamless and straightforward as possible, allowing data scientists to focus on the actual science rather than the underlying infrastructure and operational details.

Certainly! Here’s a simple example to illustrate how Metaflow is used in a data science workflow. This example will demonstrate defining a workflow, using decorators for resource allocation, versioning, and running steps, and integrating with AWS for cloud execution.

Please note, this is a basic illustration. In real-world scenarios, workflows can be much more complex and involve advanced features of Metaflow.

### Sample Metaflow Workflow

First, make sure you have Metaflow installed. You can install it using pip:

```
pip install metaflow
```

Now, let’s create a simple workflow with Metaflow:

```
from metaflow import FlowSpec, step, card

class MyDataScienceProject(FlowSpec):
    
    @step
    def start(self):
        """
        The 'start' step is the entry point of the flow.
        """
        print("Starting data science workflow...")
        # Initialize some data
        self.my_data = [1, 2, 3, 4, 5]
        self.next(self.process_data)

    @step
    def process_data(self):
        """
        A step to process data.
        """
        print("Processing data...")
        # Perform some data processing
        self.processed_data = [x * 2 for x in self.my_data]
        self.next(self.end)

    @step
    def end(self):
        """
        The 'end' step concludes the flow.
        """
        print("Processed data:", self.processed_data)
        print("Workflow is complete.")

# Run the flow
if __name__ == '__main__':
    MyDataScienceProject()
```

### Running the Flow

To run this Metaflow script, save it as a Python file (e.g., `my_data_science_project.py`) and execute it from the command line:

```
python my_data_science_project.py run
```

### Explanation

* **@step Decorator**: Each method in the class decorated with `@step` represents a step in the workflow. Metaflow automatically manages the transition from one step to the next.
* **Data Passing**: Metaflow automatically handles the passing of data (`self.my_data` and `self.processed_data`) between steps.
* **Workflow Definition**: The workflow is defined as a Python class (`MyDataScienceProject`), making it intuitive for Python programmers.
* **Execution**: Running the script with `python my_data_science_project.py run` executes the workflow from start to end.

### Integration with AWS

Metaflow can seamlessly scale this workflow to AWS. By using decorators like `@batch` or `@step`, you can specify resources and configure AWS execution. However, running workflows on AWS requires setup and configuration of your AWS environment, and the appropriate AWS-related decorators in your script.

This example is a basic demonstration. Metaflow supports much more sophisticated functionalities, including conditional branching, parallelization, complex data manipulations, integration with external data sources, and model deployment. For more advanced use cases, you would typically leverage these additional features of Metaflow.

### Metaflow

**Pros:**

1. **User-Friendly for Data Scientists**: Metaflow is designed with a focus on the data scientist’s workflow, making it easy to prototype, build, and deploy models without deep expertise in infrastructure management.
2. **Integrated Workflow Management**: It provides a seamless experience from data extraction to model deployment, with automatic versioning, easy access to past runs, and experiment tracking.
3. **Abstraction from Infrastructure**: Metaflow abstracts away many infrastructure details, allowing data scientists to focus on model development and experimentation.
4. **Scalability and Flexibility**: It easily scales from a single machine to cloud-based resources, handling resource allocation and parallelization effectively.
5. **Integration with Common Tools**: Metaflow integrates well with popular data science tools and libraries.

**Cons:**

1. **Limited to Python**: As of now, Metaflow is primarily Python-based, which might be a limitation if your workflow requires other programming languages.
2. **Less Control Over Infrastructure**: While abstraction is beneficial for simplicity, it can limit control over the underlying infrastructure, which might be a drawback for complex, customized workflows.
3. **Dependence on Metaflow’s Design Choices**: Users are somewhat at the mercy of the design and architectural decisions made by the Metaflow team.

### Outerbounds

* Model training platform that helps gets from prototype to production faster than any platform
* @Resource: decorator for GPU compute
* Amazon prime uses it
* daily cost keeps track, dashboard
* who ran what training
* monitoring
* requesting this much memory but only using this much during training
* Cost reporting with metaflow
* Support
* Data agnostic
* create an IAM role -> dev opsy
* very standard cloud formation
* easy ramp up
* desktop VS code
* docker image
* Role based access control
* Cost monitoring
* Data drift handling: https://arize.com/model-drift/

## Metaflow job descrip

* Engineering Manager, Metaflow, Machine Learning Platform
* Netflix · Los Gatos, CA · Reposted 1 week ago · Over 100 applicants
* $180,000/yr - $900,000/yr Full-timeMatches your job preferences, job type is Full-time.
* 10,001+ employees · Entertainment Providers
* Skills: Engineering Management, Computer Science, +8 more
* Netflix is the world’s leading streaming entertainment service with 238M paid memberships in over 190 countries enjoying TV series, documentaries, and feature films across a wide variety of genres and languages. Machine Learning drives innovation across all product functions and decision-support needs. Building highly scalable and differentiated ML infrastructure is key to accelerating this innovation.
* We are looking for an experienced engineering leader to lead the Metaflow team in the Machine Learning Platform org. The ML Platform org is chartered to maximize the business impact of all ML practice at Netflix and innovate on ML infrastructure to support key product functions like personalized recommendations, studio innovations, virtual productions, growth intelligence, and content demand modeling among others.
* Metaflow is an OSS ML platform developed here at Netflix, and now leveraged by several companies around the world. The Metaflow team within Netflix continues to develop our internal version and ecosystem of Metaflow, the most advanced in the world, to drive even higher levels of ML productivity for our customers. Our internal ecosystem includes fast data processing, ML serving capabilities, and other extensions not available elsewhere.
* In this role you will be responsible for a high visibility, widely adopted product that 100+ ML projects within Netflix, spanning consumer scale personalization, growth, studio algorithms, and content understanding models. We are looking for a leader who has prior experience building ML infrastructure, has a strong product sense, and technical vision to help take Metaflow to the next level of impact. Metaflow has the opportunity to grow in many ways such as higher level ML abstractions to reduce the boiler plate for common use cases, improving Metaflow core in collaboration with OSS to make the existing capabilities more flexible and powerful, and deepening our integration with other internal platform offerings.
* Expectations
  + Vision: Understanding the media business and how technology is changing the landscape will allow you to lead your team by providing clear technical and business context.
  + Partnership & Culture: Establishing positive partnerships with both business and technical leaders across Netflix will be critical. We want you to regularly demonstrate the Netflix culture values like selflessness, curiosity, context over control, and freedom & responsibility in all your engagements with colleagues.
  + Judgment: Netflix teams tend to be leaner compared to our peer companies, so you will rely on your judgment to prioritize projects, working closely with your partners - the personalization research leaders.
  + Technical acumen: We expect leaders at Netflix to be well-versed in their technical domain and be a user of the products we are building, so they can provide guidance for the team when necessary. Proficiency in understanding the needs of research teams and how to bring efficient ML infrastructure to meet those needs will be crucial.
  + Recruiting: Building and growing a team of outstanding engineers will be your primary responsibility. You will strive to make the team as excellent as it can be, hiring and retaining the best, and providing meaningful timely feedback to those who need it.
* Minimum Job Qualifications
  + Experience leading a team responsible for large-scale ML Infrastructure
  + Strong product sense – you take pride in building well designed products that users love.
  + Outstanding people skills with high emotional intelligence
  + Excellent at communicating context, giving and receiving feedback, fostering new ideas, and empowering others without micromanagement
  + Willing to take action, without being stubborn - the ability to recognize your own mistakes
  + Your team and partners see your humility all the time and diverse high-caliber talent wants to work with you
* Preferred Qualifications
  + 10+ years of total experience including 3+ years of engineering management
  + Experience with modern OSS ML frameworks such as Tensorflow, PyTorch, Ray.
  + Prior experience building and scaling Python ML infrastructure
  + Prior experience in personalization or media ML domains.
  + Exposure to Kubernetes or other container orchestration systems
  + BS/MS in Computer Science, Applied Math, Engineering or a related field
  + ML practitioner leader or individual contributor experience owning end-to-end ML functions for a product domain
* Our compensation structure consists solely of an annual salary; we do not have bonuses. You choose each year how much of your compensation you want in salary versus stock options. To determine your personal top of market compensation, we rely on market indicators and consider your specific job family, background, skills, and experience to determine your compensation in the market range. The range for this role is $180,000 - $900,000.
* Netflix provides comprehensive benefits including Health Plans, Mental Health support, a 401(k) Retirement Plan with employer match, Stock Option Program, Disability Programs, Health Savings and Flexible Spending Accounts, Family-forming benefits, and Life and Serious Injury Benefits. We also offer paid leave of absence programs. Full-time hourly employees accrue 35 days annually for paid time off to be used for vacation, holidays, and sick paid time off. Full-time salaried employees are immediately entitled to flexible time off. See more detail about our Benefits here.
* Netflix is a unique culture and environment. Learn more here.
* We are an equal-opportunity employer and celebrate diversity, recognizing that diversity of thought and background builds stronger teams. We approach diversity and inclusion seriously and thoughtfully. We do not discriminate on the basis of race, religion, color, ancestry, national origin, caste, sex, sexual orientation, gender, gender identity or expression, age, disability, medical condition, pregnancy, genetic makeup, marital status, or military service.

### AWS Stack Services (e.g., AWS Step Functions, SageMaker, AWS Glue)

**Pros:**

1. **Highly Customizable**: AWS services offer granular control over every aspect of the infrastructure and workflow, allowing for highly tailored solutions.
2. **Tight Integration with AWS Ecosystem**: They provide seamless integration with a wide range of AWS services, which is beneficial for projects heavily reliant on the AWS ecosystem.
3. **Scalability and Reliability**: AWS services are known for their scalability and reliability, capable of handling very large-scale data processing needs.
4. **Support for Diverse Workflows**: AWS offers a diverse set of tools that can support various types of data workflows, including batch processing, real-time analytics, and machine learning.

**Cons:**

1. **Complexity and Learning Curve**: The use of AWS services typically requires a good understanding of cloud infrastructure, which can have a steep learning curve.
2. **Management Overhead**: There is more overhead in terms of setting up, configuring, and managing different services and ensuring they work together seamlessly.
3. **Cost Management**: While AWS offers pay-as-you-go pricing, managing costs can be complex, especially with multiple integrated services.
4. **Potentially More Fragmented Workflow**: Using multiple AWS services might lead to a more fragmented workflow compared to an integrated solution like Metaflow.

In summary, Metaflow offers an easier, more integrated experience for data scientists, focusing on simplicity and ease of use, while AWS services offer more control, customization, and tight integration with the AWS ecosystem, albeit with a higher complexity and management overhead. The choice between them will depend on the specific needs of the project, the technical expertise of the team, and the desired level of control over infrastructure and workflow management.

## Fairness among New Items in Cold Start Recommender Systems

* Heater, DropoutNet, DeepMusic, and KNN
* Investigated fairness among new items in cold start recommenders.
* Identified prevalent unfairness in these systems.
* Proposed a novel learnable post-processing framework to enhance fairness.
* Developed two specific models, Scale and Gen, following the framework.
* Conducted extensive experiments, showing effectiveness in enhancing fairness and preserving utility.
* Future research planned to explore recommendation fairness between cold and warm items in a unified scenario.
* This work examines the fairness among new items in cold start recommendation systems, highlighting the widespread presence of unfairness.
* To address this issue, a novel learnable post-processing framework is introduced, with two specific models – Scale and Gen – designed following this approach.
* Extensive experiments demonstrate the effectiveness of these models in enhancing fairness while maintaining recommendation utility.
* Future research aims to explore fairness between cold and warm items in a unified recommendation context.
* Mean Discounted Gain

## Data drift

Data drift refers to the change in the statistical properties of the data that a model is processing over time. This can lead to decreased model performance if the model was trained on data with different statistical properties. Detecting data drift without access to labels can be more challenging, but it is still possible through various techniques.

1. **Statistical Tests**: You can conduct statistical tests on the features in your data to check for changes in distribution. Kolmogorov-Smirnov or Chi-squared tests are often used to compare the distribution of the current data with the distribution of the data on which the model was trained. If the test indicates a significant difference, it could be a sign of data drift.
2. **Monitoring Feature Statistics**: Continuously monitor summary statistics (e.g., mean, median, standard deviation, etc.) of your input features. If there are significant changes in these statistics over time, it may indicate data drift. You can set threshold levels to trigger alerts if the statistics deviate beyond acceptable bounds.
3. **Using Unsupervised Learning**: Techniques like clustering or dimensionality reduction (e.g., PCA) can be used to represent the data in a way that makes it easier to spot changes. By regularly fitting these techniques to the incoming data and comparing the results with the original training data, you might identify shifts in the data structure.
4. **Comparing Prediction Distributions**: Even without labels, you can compare the distribution of predictions made on the current data to the distribution of predictions made on the training or validation data. A significant shift might indicate a change in the underlying data distribution.
5. **Residual Analysis**: If you can obtain a small subset of labeled data, you can analyze the residuals (the difference between the predictions and the true labels). A change in the distribution of residuals over time might be indicative of data drift.
6. **Creating a Proxy for Labels**: If your production environment involves users interacting with the predictions (e.g., clicking on recommended items), you might create a proxy for true labels based on user behavior and use this to detect changes.
7. **Human-in-the-Loop**: Depending on the application, it might be feasible to introduce a human review process to periodically evaluate a subset of the predictions. While not fully automated, this can be a powerful way to detect issues that automated methods might miss.
8. **Use of Drift Detection Libraries**: There are libraries and tools designed specifically for drift detection, like the Python library Alibi-Detect, that can be implemented to monitor for data drift.

Remember, detecting data drift is not always straightforward, especially without access to true labels. The appropriate approach may depend on the specifics of your data, model, and application. It’s often useful to combine multiple methods to create a more robust detection system. Regularly reviewing and updating your model with new training data reflecting the current data distribution is an essential part of maintaining model performance.

## Causal Ranker

Certainly! Here’s a bullet-point summary of the information you provided about the Causal Ranker Framework by Netflix:

* **Overview**:
  + **Authors**: Jeong-Yoon Lee, Sudeep Das.
  + **Purpose**: To enhance recommendation systems by incorporating causal inference into machine learning.
  + **Concept**: Moving beyond mere correlations to understand causal mechanisms between actions and outcomes.
* **Machine Learning vs Causal Inference**:
  + **Machine Learning**: Focuses on associative relationships, learning correlations between features and targets.
  + **Causal Inference**: Provides a robust framework that controls for confounders to estimate true incremental impacts. This adds understanding of the causal relationship between actions and results.
* **Application at Netflix**:
  + **Current Systems**: Netflix uses recommendation models for personalizing content on user homepages.
  + **Need**: Netflix identified the potential benefit of adding algorithms that focus on making recommendations more useful in real-time, rather than merely predicting engagement.
* **Causal Ranker Framework**:
  + **Introduction**: A new model applied as a causal adaptive layer on top of existing recommendation systems.
  + **Components**: Includes impression (treatment) to play (outcome) attribution, true negative label collection, causal estimation, offline evaluation, and model serving.
  + **Goal**: To find the exact titles members are looking to stream at any given moment, improving recommendations.
  + **Reusability**: Designed with generic and reusable components to allow adoption by various teams within Netflix, promoting universal improvement in recommendations.
* **Implications**:
  + **Scalability**: By combining machine learning with causal inference, the framework offers a powerful tool that can be leveraged at scale.
  + **Potential Impact**: Enhancing personalization, meeting user needs more effectively, and aligning recommendations with users’ immediate preferences.
* The Causal Ranker Framework symbolizes an innovative step in recommendation systems, emphasizing the importance of understanding causal relationships and catering to real-time user needs. Its flexibility and comprehensive design have positioned it as a potential game-changer within Netflix’s personalization efforts and possibly beyond.

## Question bank

* Behavior interview with hiring manager
  1. Past projects - most challenging part, your role
* The most challenging thing about being a manager is also the most rewarding. As the team’s manager, I’m responsible for not just my own success but that of my team as well. In that sense, my charter typically involves a much bigger scope than as my prior role as an individual contributor. However, navigating a big ship comes with its own set of unique responsibilities. You are responsible not only for yourself, but for your team. So you must continually measure their performance, set clear expectations/goals/priorities, make sure the communication is crisp and clear, motivate them, and keep them focused. At the end of the day, it is a great feeling to be able to accomplish this.
* Also, another important aspect of this position would be to build the relationship with my employees because that will take time. However, I also feel it is one of the most rewarding part of this position. I enjoy relationship-building and helping others to achieve their success.

1. Tell me a time when you disagree with the team
   * I can tell you a time where I disagreed with my leadership.
   * At the time, we were working on content to content recommendations, books to podcast with cross collaborations with Amazon retail, audible and wondery (podcast platform).
   * There were a lot of novel insights and a unique architecture we approached to solve this and thus, we decided to get a publication out of this.
   * The process to start this off at Amazon, requires Director level approval to kick off the writing process, however, my managers manager, who sits under the Director, wanted to set up a meeting to discuss this before we presented it to the Director to approve.
   * This went against Amazon’s policies and would hinder time to submit to the conference. I respectfully,
2. Tell me a time when you inherited a system in bad shape
3. How do you prioritize
   * Name five devices you can watch Netflix on – Systems engineer candidate
   * What would you do if you were the CEO? – Partner product group candidate
   * Describe how you would deal with a very opinionated coworker.
     + I think netflix coins this term as “brilliant jerks.” Engin. Complaints about everyone on the team.
     + They were

* Tell me about a previous time you screwed up at your previous job.
* What has been the biggest challenge while you work?
* How do you improve Netflix’s service? – Financial analyst candidate
* Who do you think are Netflix’s competitors and why? – Creative coordinator candidate
* How do you test the performance of your service? – Software engineer candidate
* Because Netflix is focused on maintaining a strong company culture—the majority of questions that the hiring manager will ask will be situational, cultural, and behavioral-style questions. Like the example questions above.
* When asked these questions it is very easy to get nervous and mix up all of our responses. In this situation, the best way to stay structured is by using the STAR Methodology, which stands for Situation, Task, Action, and Result
* Let’s dive into an example so that you can better understand this method:
* Example question:
* How did you handle a task where you had a deadline that you couldn’t meet?
* Situation:
* Don’t generalize the information that you are conveying*\*\**. Be as specific as possible when describing the situation, so that the person asking the question understands the context.
* Example: Because the last company I was working at was growing so quickly, we did not have enough staff to cover all of the projects. Most people like me had more projects than we could handle, and that did cause stress and tension.
* Task:
* Describe your responsibility and the goal you were working towards.
* Example: I was a project manager that was in charge of application releases. I had to make sure that the applications were launched in the right order and on the right date.
* Action:
* You must provide what specific actions you took towards solving the problem. Also, make sure that you do not focus on talking about any other team member. Try using the word “I” and not “we”.
* Example: To make sure that I wasn’t too overwhelmed, I created a project timeline. I then organized all of the app launches in order of priority. If an application was not going to be launched on time or if it had low priority—I made sure to bring this up to my superiors and explain what my plan was.
* Result:
* This is your time to shine. Describe the outcome of the situation in detail, and show how you were able to solve the problem.
* Example: Because I created a timeline and took charge of prioritizing the launch, we were able to be much more efficient. Once the big launches were done, I was able to create much more time for the team. This led us to complete more projects than we thought was possible and generate more revenue for the company.
* hm screening team lead, they asked about the current system in very, very detailed terms.
* You must be very clear about your project and failure point. There are still a lot of bq, and the previous experience still has scenario based problems.
* cross functional
* Then I introduced myself. After talking about the background, I said that I want to go through all the projects on the resume for you? He said you tell me your favorite, so I will tell you one. After he finished speaking, he began to ask questions. If you want causal to be based on what assumptions, how did you rule out some possible reasons, are you confident that you ruled out other things that may affect causality? I said what I controlled, what fixed effects I added, so I was comparing with whom, and what robustness checks I did..
* under what circumstance is the power the highest for A/B test
* Suppose you want to do an experiment, that is, whether to use static pictures or dynamic videos on the netflix homepage, so that more people can sign up for subscription.
* I said, first of all, I need to determine my population, ah, do you want to be global or just the United States. He said global.
* Then I said that I want to determine my sample, it is best that a certain percentage of people from each country come in as a sample.
* Then I need to determine my time. Then I have to take into account that the audiences who come in at different times in the morning, noon and evening are different. The audience who come in on weekdays and weekends are different. Holidays may also be a problem, but you can’t do this experiment. Years, so it must be at least a week? (Then my brother praised me! He said I thought well!)
* Then I want to determine the outcome variable, that is whether to sign up.
* Wow, a lot of details, I said just do a t test, if there is no problem with the randomization (for example, I check the balance)
* What is the common misunderstanding of P value?
* Ans: The hypothesis can only reject or not reject, but not accept.

## your projects

## ooooo

* A director, Uncle Bai, mainly asked BQ, what he thinks of their culture, and some general questions.
* Surprisingly, I was even asked some questions about design, a/b test and Ml deployment, how to monitor data drift if the true label cannot be obtained in time on metaflow, etc.
* It feels technically strong.
* [Kolmogorov](https://www.google.com/search?q=kolmogorov+smirnov+test+data+drift&sca_esv=558292613&sxsrf=AB5stBhjXEvRVTc9q91HlUI91LiHR4-OQg%3A1692410983955&ei=ZyTgZL3gOdrbkPIPi-SW-AU&ved=0ahUKEwj9r4yc0ueAAxXaLUQIHQuyBV8Q4dUDCBA&uact=5&oq=kolmogorov+smirnov+test+data+drift&gs_lp=Egxnd3Mtd2l6LXNlcnAiImtvbG1vZ29yb3Ygc21pcm5vdiB0ZXN0IGRhdGEgZHJpZnQyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABSMsVUABY2xRwAHgBkAEAmAGXAaAB2gyqAQQwLjEyuAEDyAEA-AEBwgIHECMYigUYJ8ICCBAAGIoFGJECwgIHEAAYigUYQ8ICBhAAGAcYHsICBRAAGIAEwgIGEAAYFhgewgIIEAAYigUYhgPCAgUQIRirAsICCBAhGBYYHhgd4gMEGAAgQYgGAQ&sclient=gws-wiz-serp)

## Syllabus

* Since the goal is to prepare for the specific role at Netflix, focusing on applied aspects of econometrics and causal inference that relate to personalization, satisfaction estimation, and working with large-scale data, the study plan would be as follows:

### Week 1-2: Introduction to Econometrics

* **Reading**: “Introductory Econometrics: A Modern Approach” by Jeffrey M. Wooldridge - Focus on introductory chapters.
* **Online Course**: Coursera’s “Econometrics: Methods and Applications” - Focus on the basic methods and applications.
* **Hands-on Practice**: Work with simple datasets to apply linear regression and understand the assumptions behind it.

### Week 3-4: Time-Series Analysis & Forecasting

* **Reading**: “Applied Econometric Time Series” by Walter Enders.
* **Online Tutorial**: “Time Series Analysis in Python” on DataCamp or similar platforms.
* **Project**: Forecasting a time series data like stock prices or user activity trends.

### Week 5-6: Causal Inference - Basics

* **Reading**: “Causal Inference in Statistics: A Primer” by Judea Pearl.
* **Online Course**: “Causal Inference” on Coursera by Columbia University.
* **Hands-on Practice**: Implementing propensity score matching and other techniques on observational data.

### Week 7-8: Experimental Design & A/B Testing

* **Reading**: “Field Experiments: Design, Analysis, and Interpretation” by Alan S. Gerber and Donald P. Green.
* **Online Tutorial**: A/B Testing tutorials on platforms like Udacity.
* **Project**: Design a hypothetical A/B test for a feature that could enhance user satisfaction.

### Week 9-10: Advanced Causal Inference & Machine Learning Integration

* **Reading**: “Causal Inference for Statistics, Social, and Biomedical Sciences” by Guido W. Imbens and Donald B. Rubin.
* **Online Course**: “Causal Machine Learning” on Coursera by University of Pennsylvania.
* **Hands-on Practice**: Apply causal machine learning techniques to a complex dataset.

### Week 11-12: Reinforcement Learning

* **Reading**: “Reinforcement Learning: An Introduction” by Richard S. Sutton and Andrew G. Barto.
* **Online Course**: “Reinforcement Learning Specialization” on Coursera by the University of Alberta.
* **Project**: Build a simple recommendation system using reinforcement learning.

### Week 13-14: Application to Real-World Problems

* **Case Studies**: Research and analyze Netflix’s research papers or blogs related to personalization, satisfaction estimation.
* **Project**: Work on a complex project that integrates econometrics, causal inference, and machine learning to solve a real-world problem similar to what Netflix is facing.

### Ongoing: Networking & Keeping Up-to-Date

* **Conferences & Workshops**: Attend industry conferences related to data science, econometrics, and machine learning.
* **Blogs & Podcasts**: Follow related blogs and podcasts like “Not So Standard Deviations” to keep up with the latest in the field.

## Further Reading

* [Netflix Culture — The Best Work of Our Lives](https://jobs.netflix.com/culture)
* [Netflix Long-Term View](https://ir.netflix.net/ir-overview/long-term-view/default.aspx)
* [How Netflix’s Recommendations System Works](https://help.netflix.com/en/node/100639)
* [What We Watched: A Netflix Engagement Report](https://about.netflix.com/en/news/what-we-watched-a-netflix-engagement-report)
* [BayLearn2019-07 Ehsan Saberian](https://www.youtube.com/watch?v=ijzj6A4pkaY)
* [Recommender Systems Summit 2022](https://www.youtube.com/watch?v=9rouLchcC0k&t=9106s)
* [Sharing Our Latest Culture Memo](https://about.netflix.com/en/news/sharing-our-latest-culture-memo)
* [Netflix Updates Its Famous Culture Memo: ‘Netflix Sucks Today Compared to Where We Can Be Tomorrow’](https://variety.com/2024/digital/news/netflix-updates-culture-memo-freedom-responsbility-people-process-1236046696/)
* Blogs:
  + [Brief Summary of No Rules Rules](https://srinathramakrishnan.wordpress.com/wp-content/uploads/2020/10/brief-summary-of-rules-no-rules.pdf)
  + [DODReads Executive Summary: No Rules Rules](https://www.dodreads.com/wp-content/uploads/2024/02/No-Rules-Rules-Adam-Smith-1-2.pdf)
* Papers:
  + [Challenges in Search on Streaming Services: Netflix Case Study](https://arxiv.org/abs/1903.04638)
  + [Recommendations and Results Organization in Netflix Search](https://arxiv.org/abs/1903.04638)
  + [Augmenting Netflix Search with In-Session Adapted Recommendations](https://arxiv.org/abs/2206.02254)
  + [Synergistic Signals: Exploiting Co-Engagement and Semantic Links via Graph Neural Networks](https://arxiv.org/abs/2312.04071)
  + [IntentRec: Predicting User Session Intent with Hierarchical Multi-Task Learning](https://arxiv.org/abs/2408.05353)
  + [Joint Modeling of Search and Recommendations Via an Unified Contextual Recommender (UniCoRn)](https://arxiv.org/abs/2408.10394)
  + [Sliding Window Training – Utilizing Historical Recommender Systems Data for Foundation Models](https://arxiv.org/abs/2409.14517)
  + [The Netflix Recommender System: Algorithms, Business Value, and Innovation](https://dl.acm.org/doi/pdf/10.1145/2843948)
  + [From Hypothesis to Member Satisfaction: A Scientific Approach to Product ML Innovation](https://wamlm-kdd.github.io/wamlm/papers/wamlm_kdd24_abstract_swanand_joshi.pdf)
  + [Artwork Personalization at Netflix](https://dl.acm.org/doi/pdf/10.1145/3240323.3241729?casa_token=DwdMcCvrUCIAAAAA:H6626GhKYt1GNylkgtluX9xTj5bMA0_vd049FPF3KUy5u21R_cVthxEv8fEsaxL0gL_cPK_QnHTh)
  + [Recommendations and Results Organization in Netflix Search](https://dl.acm.org/doi/pdf/10.1145/3460231.3474602?casa_token=lBAiWY2te1EAAAAA:sbrPhNe5QE0zRUs_Kt-Kz_EbYOOxQ6gSBWSvtUl7P0PXGMBj8ijGTQMsM3T4oJOS0sllxWl7_Ovx)
  + [Search Personalization at Netflix](https://dl.acm.org/doi/pdf/10.1145/3543873.3587675?casa_token=JpXI6BRXLFsAAAAA:mifE-jPQBfTX2vU7AvikhIlu0xGVIXMvybi4yKrlT8-KrEo6nkJpwfltd1aAC5HAbDz41PAIogDb)
  + [Navigating the Feedback Loop in Recommender Systems: Insights and Strategies from Industry Practice](https://dl.acm.org/doi/abs/10.1145/3604915.3610246?casa_token=YgsLDSNvGzwAAAAA:FVksZ98OaxtUjjyBWJbmH__0zf-mGQUJ80l3H1YnawL4IKrEiW_a6yW-K1KdQ002ArFOGlDJagYp)
* Presentations:
  + [Context Aware Recommendations at Netflix](https://www.slideshare.net/slideshow/context-aware-recommendations-at-netflix/97526888#23)
  + [Time, Context and Causality in Recommender Systems](https://www.slideshare.net/slideshow/time-context-and-causality-in-recommender-systems/119760944)
  + [Deeper Things: How Netflix Leverages Deep Learning in Recommendations and Search](https://www.slideshare.net/slideshow/deeper-things-how-netflix-leverages-deep-learning-in-recommendations-and-search/131390360)
  + [Deep Learning for Recommender Systems](https://www.slideshare.net/slideshow/deep-learning-for-recommender-systems-86752234/86752234)
  + [Personalizing “The Netflix Experience” with Deep Learning](https://www.slideshare.net/slideshow/personalizing-the-netflix-experience-with-deep-learning/151983724#1)
  + [Tutorial on Deep Learning in Recommender System, Lars summer school 2019](https://www.slideshare.net/slideshow/tutorial-on-deep-learning-in-recommender-system-lars-summer-school-2019/190444877)
  + [Déjà Vu: The Importance of Time and Causality in Recommender Systems](https://www.slideshare.net/slideshow/deja-vu-the-importance-of-time-and-causality-in-recommender-systems/79252001)
  + [Artwork Personalization at Netflix](https://www.slideshare.net/slideshow/artwork-personalization-at-netflix/121997305)
  + [Past, Present & Future of Recommender Systems: An Industry Perspective](https://www.slideshare.net/slideshow/past-present-future-of-recommender-systems-an-industry-perspective/66170875)
  + [Learning a Personalized Homepage](https://www.slideshare.net/slideshow/learning-a-personalized-homepage/33397216)
  + [Personalized Page Generation for Browsing Recommendations](https://www.slideshare.net/justinbasilico/personalized-page-generation-for-browsing-recommendations)
  + [Shallow and Deep Latent Models for Recommender System](https://www.slideshare.net/slideshow/shallow-and-deep-latent-models-for-recommender-system/102255337)
  + [Calibrated Recommendations](https://www.slideshare.net/slideshow/calibrated-recommendations/118205343)
  + [Recommending for the World](https://www.slideshare.net/slideshow/recommending-for-the-world/61118114#7)
* Blogs:
  + [Netflix Recommendations: Beyond the 5 stars (Part 1)](https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429)
  + [Netflix Recommendations: Beyond the 5 stars (Part 2)](https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-2-d9b96aa399f5)
  + [How We Determine Product Success](https://netflixtechblog.com/how-we-determine-product-success-980f81f0047e)
  + [Lessons Learnt From Consolidating ML Models in a Large Scale Recommendation System](https://netflixtechblog.medium.com/lessons-learnt-from-consolidating-ml-models-in-a-large-scale-recommendation-system-870c5ea5eb4a)
  + [RecSysOps: Best Practices for Operating a Large-Scale Recommender System](https://netflixtechblog.medium.com/recsysops-best-practices-for-operating-a-large-scale-recommender-system-95bbe195a841)
  + [Supporting Diverse ML Systems at Netflix](https://netflixtechblog.com/supporting-diverse-ml-systems-at-netflix-2d2e6b6d205d)
  + [Supporting content decision makers with machine learning](https://netflixtechblog.com/supporting-content-decision-makers-with-machine-learning-995b7b76006f)
  + [New Series: Creating Media with Machine Learning](https://netflixtechblog.com/new-series-creating-media-with-machine-learning-5067ac110bcd)
  + [Scaling Media Machine Learning at Netflix](https://netflixtechblog.com/scaling-media-machine-learning-at-netflix-f19b400243)
  + [Match Cutting: Finding Cuts with Smooth Visual Transitions Using Machine Learning](https://netflixtechblog.com/match-cutting-at-netflix-finding-cuts-with-smooth-visual-transitions-31c3fc14ae59)
  + [Meson: Workflow Orchestration for Netflix Recommendations](https://netflixtechblog.com/meson-workflow-orchestration-for-netflix-recommendations-fc932625c1d9)
  + [AVA Discovery View: Surfacing Authentic Moments](https://netflixtechblog.com/ava-discovery-view-surfacing-authentic-moments-b8cd145491cc)
  + [Selecting the best artwork for videos through A/B testing](https://netflixtechblog.com/selecting-the-best-artwork-for-videos-through-a-b-testing-f6155c4595f6)
  + [Discovering Creative Insights in Promotional Artwork](https://netflixtechblog.com/discovering-creative-insights-in-promotional-artwork-295e4d788db5)
  + [Causal Machine Learning for Creative Insights](https://netflixtechblog.com/causal-machine-learning-for-creative-insights-4b0ce22a8a96)
  + [Round 2: A Survey of Causal Inference Applications at Netflix](https://netflixtechblog.com/round-2-a-survey-of-causal-inference-applications-at-netflix-fd78328ee0bb)
  + [Quasi Experimentation at Netflix](https://netflixtechblog.com/quasi-experimentation-at-netflix-566b57d2e362)
  + [Decision Making at Netflix](https://netflixtechblog.com/decision-making-at-netflix-33065fa06481)
  + [Global Languages Support at Netflix](https://netflixtechblog.com/global-languages-support-at-netflix-testing-search-queries-ede40f7d93d3)
* Infra:
  + [Netflix Open Source Software Center](https://netflix.github.io/)
  + [Announcing Suro: Backbone of Netflix’s Data Pipeline](https://netflixtechblog.com/announcing-suro-backbone-of-netflixs-data-pipeline-5c660ca917b6)
  + [Using Presto in our Big Data Platform on AWS](https://netflixtechblog.com/using-presto-in-our-big-data-platform-on-aws-938035909fd4)
  + [Distributed Time Travel for Feature Generation](https://netflixtechblog.com/distributed-time-travel-for-feature-generation-389cccdd3907)
  + [Hadoop Platform as a Service in the Cloud](https://netflixtechblog.com/hadoop-platform-as-a-service-in-the-cloud-c23f35f965e7)
* Articles:
  + [A look under the hood of the most successful streaming service on the planet](https://www.theverge.com/22787426/netflix-cdn-open-connect)
  + [The high tech behind Netflix’s old-school DVD service](https://www.theverge.com/23883662/netflix-dvd-shutdown-complex-tech-packaging-mail)

## References

* [Netflix Culture — The Best Work of Our Lives](https://jobs.netflix.com/culture)
* [You should check out Netflix Games, if you haven’t already.](https://www.reddit.com/r/iosgaming/comments/1ckky7t/you_should_check_out_netflix_games_if_you_havent/)
* [Brief Summary of No Rules Rules](https://srinathramakrishnan.wordpress.com/wp-content/uploads/2020/10/brief-summary-of-rules-no-rules.pdf)
* [Executive Summary: No Rules Rules](https://www.dodreads.com/wp-content/uploads/2024/02/No-Rules-Rules-Adam-Smith-1-2.pdf)
* [No Rules Rules: Netflix and the Culture of Reinvention / Reed Hastings and Erin Meyer](https://teachmint.storage.googleapis.com/public/680271877/StudyMaterial/6897612b-fe45-477c-93ca-72b285c6ce85.pdf)
* [How Netflix’s Recommendations System Works](https://help.netflix.com/en/node/100639)
* [The Netflix Recommender System: Algorithms, Business Value, and Innovation](https://github.com/manjunath5496/DL-Recommender-System-Papers/blob/master/%5BNetflix%5D%20The%20Netflix%20Recommender%20System-%20Algorithms%2C%20Business%20Value%2C%20and%20Innovation%20(Netflix%202015.pdf)
* [Netflix statistics: How many movies and TV shows do they have? 2024](https://www.comparitech.com/blog/vpn-privacy/netflix-statistics-facts-figures/)
* [Deep learning for recommender systems: A Netflix case study](https://onlinelibrary.wiley.com/doi/10.1609/aimag.v42i3.18140)
* [RecSysOps: Best Practices for Operating a Large-Scale Recommender System](https://netflixtechblog.medium.com/recsysops-best-practices-for-operating-a-large-scale-recommender-system-95bbe195a841)
* [Learning a Personalized Homepage](https://netflixtechblog.com/learning-a-personalized-homepage-aa8ec670359a)
* [Netflix ML Interview Prep: Insights and Recommendations](https://www.interviewnode.com/post/netflix-ml-interview-prep-insights-and-recommendations)
* [40 Netflix Interview Questions](https://mentorcruise.com/questions/netflix/)
