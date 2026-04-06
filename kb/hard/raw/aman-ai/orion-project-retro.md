# Orion: Project Retro

**Source:** https://aman.ai/h/orionRetro/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Rubric - Retro](#rubric---retro)
  + [Structure my thoughts](#structure-my-thoughts)
  + [Business + Product (Key value prop, Competition) / “Context around my team and the specific project we’ll be covering today” (2.5 mins)](#business--product-key-value-prop-competition--context-around-my-team-and-the-specific-project-well-be-covering-today-25-mins)
    - [What is your product and role?](#what-is-your-product-and-role)
  + [Vision + Strategy / “Top-Level Strategy” / 2.5 mins](#vision--strategy--top-level-strategy--25-mins)
    - [How did you figure out your part in that strategy?](#how-did-you-figure-out-your-part-in-that-strategy)
    - [Can you give me an example of being given a really ambiguous problem and coming up with a strategy for it?](#can-you-give-me-an-example-of-being-given-a-really-ambiguous-problem-and-coming-up-with-a-strategy-for-it)
  + [Metrics + Goals (cost metrics, feasibility of alternatives) / “Objective/Goal and Metrics: OKRs” / 10 mins](#metrics--goals-cost-metrics-feasibility-of-alternatives--objectivegoal-and-metrics-okrs--10-mins)
    - [What was the OKR you set for this project?](#what-was-the-okr-you-set-for-this-project)
    - [How do you define success for the team/product?](#how-do-you-define-success-for-the-teamproduct)
    - [For that definition of success, what is the team’s goal? Follow up: How was that goal identified?](#for-that-definition-of-success-what-is-the-teams-goal-follow-up-how-was-that-goal-identified)
  + [Roadmap (your contribution specifically) / “Roadmap” / 7 mins](#roadmap-your-contribution-specifically--roadmap--7-mins)
    - [V0/MVP - Summarizing Reviews](#v0mvp---summarizing-reviews)
      * [What kind of reviewer metadata would be essential here?](#what-kind-of-reviewer-metadata-would-be-essential-here)
    - [V1 - LLM + RAG, Pre-Rufus, No Guardrails](#v1---llm--rag-pre-rufus-no-guardrails)
    - [V2 - Rufus as you see it today, Multilingual + Guardrails + Continuous Monitoring and Learning](#v2---rufus-as-you-see-it-today-multilingual--guardrails--continuous-monitoring-and-learning)
      * [Explain the implementation details around guardrails.](#explain-the-implementation-details-around-guardrails)
    - [How did you identify the roadmap for the half? (What were your contributions)](#how-did-you-identify-the-roadmap-for-the-half-what-were-your-contributions)
    - [How do you identify and track dependencies?](#how-do-you-identify-and-track-dependencies)
  + [Put together cross-team effort / “XF Planning and Alignment” / 3 mins](#put-together-cross-team-effort--xf-planning-and-alignment--3-mins)
    - [How do you work with cross functional partners XFNs?](#how-do-you-work-with-cross-functional-partners-xfns)
    - [What are some of the ways you can have influence over other teams?](#what-are-some-of-the-ways-you-can-have-influence-over-other-teams)
    - [How do you work with non-technical stakeholders?](#how-do-you-work-with-non-technical-stakeholders)
  + [Delivery + Risks / “Delivery: Task Tracking + Risk Mitigation” / 10 mins](#delivery--risks--delivery-task-tracking--risk-mitigation--10-mins)
    - [How do you track progress on all projects? / Planning (OKRs) + Tracking (Sprint) Process](#how-do-you-track-progress-on-all-projects--planning-okrs--tracking-sprint-process)
    - [Why do teams fall behind schedule?](#why-do-teams-fall-behind-schedule)
    - [What were the risks to the project and how did you mitigate them? / “Risk Mitigation”](#what-were-the-risks-to-the-project-and-how-did-you-mitigate-them--risk-mitigation)
  + [Failures + Learning / Introspection / Reflection / 5 mins](#failures--learning--introspection--reflection--5-mins)
    - [What was the biggest challenge you faced during this project?](#what-was-the-biggest-challenge-you-faced-during-this-project)
    - [How did you recover from a failed delivery? / “Recovering from a Failed Delivery”](#how-did-you-recover-from-a-failed-delivery--recovering-from-a-failed-delivery)
    - [What was your biggest mistake / failure as part of this project and outside this project? What did you learn from it?](#what-was-your-biggest-mistake--failure-as-part-of-this-project-and-outside-this-project-what-did-you-learn-from-it)
      * [What is AWS Data Pipeline?](#what-is-aws-data-pipeline)
        + [Key Features of AWS Data Pipeline](#key-features-of-aws-data-pipeline)
    - [What are your areas of growth around execution? / Tell me about a growth area you’re currently working on.](#what-are-your-areas-of-growth-around-execution--tell-me-about-a-growth-area-youre-currently-working-on)
* [Additional Questions](#additional-questions)
  + [How do you work with other disciplines?](#how-do-you-work-with-other-disciplines)
  + [Tell me about your greatest success or a project that you didn’t think could work but it did. What did you learn?](#tell-me-about-your-greatest-success-or-a-project-that-you-didnt-think-could-work-but-it-did-what-did-you-learn)
    - [Tell me about a project that you were really passionate about and believed in with all your heart but failed. What did you learn?](#tell-me-about-a-project-that-you-were-really-passionate-about-and-believed-in-with-all-your-heart-but-failed-what-did-you-learn)
  + [How do you track progress on all projects? / Planning (OKRs) + Tracking (Sprint) Process](#how-do-you-track-progress-on-all-projects--planning-okrs--tracking-sprint-process-1)
    - [XF Collaboration](#xf-collaboration)
* [Recruiter - Retro](#recruiter---retro)

## Rubric - Retro

### Structure my thoughts

* “Context around my team and the specific project we’ll be covering today”
* “Top-level Vision/Strategy”
* “Objectives and Key Results/OKRs (Organizational OKRs)”
* “Roadmap: Phases”
* “XF Collaboration: Planning and Alignment (Timelines and Deliverables via Team-Level OKRs)”
* “Execution/Delivery: Task Tracking + Risk Mitigation”
* “Introspection: Failures + Learning”

### Business + Product (Key value prop, Competition) / “Context around my team and the specific project we’ll be covering today” (2.5 mins)

* My team is part of the **Generative AI** org within AWS. We’re a centralized org with the charter of building **GenAI models** in collaboration with other business units such as Amazon Shopping, Alexa, Amazon Prime Video, and Amazon Music. Our goal is the adoption of GenAI for projects and initiatives across Amazon.

* Now let’s setup some context before we get into the problem statement.
* One of the primary business metrics Amazon tracks for its **shopping business** is the **time from browse-to-buy**. This metric reflects how easily customers can access **relevant information** about products, which was known to be correlate with better customer experience and hence positively impacting **revenue**.
* An analysis of user interaction data for **Amazon Shopping** by the **customer analytics** team revealed that the **biggest obstacle for customers** in making a purchase was the **lack of easily accessible product information**. This information was often buried deep within **user reviews** leading to an increased time from browse-to-buy. This issue was **particularly evident** for some of our **most popular products**, which often had **hundreds of thousands of reviews**. Given that **retail accounts for approximately 80% of Amazon’s total revenue** (~$400 billion/yr), our hypothesis was that addressing this issue, even partially, could translate to a significant lift in our **north-star business metrics**. This was our top-level problem statement.

#### What is your product and role?

* **Product:** Led the development of **Rufus**, a conversational chatbot on Amazon.com, designed to **reduce “browse-to-buy” time** by surfacing relevant product information quickly using **Generative AI** and **RAG**. Rufus assists with both **product-specific** and **general queries**, providing users with summarized reviews and product suggestions.
* **My Role:**

  + **Lead strategy and execution** of Rufus, ensuring alignment with Amazon’s overarching **business growth objectives**.
  + **Ensuring XF alignment** with both technical and non-technical stakeholders (i.e., between our team, **Amazon.com product catalog**, **customer analytics**, and **legal/compliance**, **UI design** teams.)
  + Working closely with my **tech leads** to **oversee the technical implementation** including guardrails, driving the development of the **LLM-based solution** and **RAG system** to enable real-time retrieval of product information.
  + **Ensured safety protocols** by implementing guardrails for **safe user interactions** and ensuring full compliance with **data privacy regulations**.
  + **Handled Agile project management**, establishing clear **milestones**, tracking project progress, and addressing risks like **scope creep** and **integration delays**.

### Vision + Strategy / “Top-Level Strategy” / 2.5 mins

* Now, let’s talk about the top-level strategy and the role I played in charting out a realizable vision, working with the Product Manager (PM) and evaluating the technical feasibility of the project at hand.

* Working backwards from our ultimate goal of improving **business growth metrics**, our focus was on reducing the **deliberation period** of customers by surfacing relevant product information to expedite their **decision-making process**.

* Working with the PM, my role in this strategy was to **come up with a roadmap** and subsequently **work closely with our XFN to form an execution plan**, where our team was responsible for leveraging **Generative AI** to deliver on this vision. Specifically, this involved: (i) **defining the architecture and safety protocols** of the system and (ii) ensuring **alignment** with our XFN which included the **Amazon.com product catalog** team (which owned the **product data**), **customer analytics** team (responsible for data analytics and tracking the health of the business via metrics), **legal and compliance** team (oversaw **data privacy compliance**), and the **UI design** team (for app UI changes).
* This eventually led to the birth of **Rufus**, a versatile, conversational chatbot currently live on Amazon.com, which is capable of handling a range of **product-specific queries** and **open-ended product recommendations**. For instance, users could ask an open-ended question like “I need a gift for a 7-month-old,” and engage in a **multi-turn conversation** where Rufus refines the request to suggest specific items, such as “a baby walker.”

#### How did you figure out your part in that strategy?

* Working backwards from the **north-star business metrics** of Amazon’s e-commerce growth, I worked closely with **customer analytics** team to identify that **the browse-to-buy time** was a bottleneck in fostering business growth. Adopting Generative AI to trim down this metric thereby enhancing the customer experience in the process to eventually scale the business seemed to be a plausible direction based on the power of this technology and our expertise in the domain.
* Working with our XFN, I helped define **Rufus’s role** in optimizing the shopping experience and tying it into Amazon’s long-term growth.
* My role was to lead the **technical development of Rufus**, aligning it with strategic goals by driving the integration of **GenAI** technology, ensuring **infrastructure scalability**, and delivering a product that could support **global expansion**.

#### Can you give me an example of being given a really ambiguous problem and coming up with a strategy for it?

* When initially tasked with reducing the “browse-to-buy” time, the problem was highly ambiguous. There were **multiple potential solutions** but no clear path forward.
* I led a **brainstorming session** with my team and XF partners to identify core customer pain points. From this, we identified that the **main issue was information overload** from too many product reviews.
  + I proposed using **Generative AI** to build a **summarization system** to extract key product features from reviews, reducing the time customers spent searching for information.
  + We evolved this into a **conversational chatbot** that could not only summarize reviews but also engage with users in **multi-turn conversations** to help them find products faster.
* This approach led to the creation of **Rufus**, which significantly reduced the **browse-to-buy time** and became a critical feature for improving Amazon’s shopping experience.

### Metrics + Goals (cost metrics, feasibility of alternatives) / “Objective/Goal and Metrics: OKRs” / 10 mins

* Now, let’s talk about how we defined success for this project in terms of the goals and metrics. I’ll also touch upon the OKR framework we used for goal planning.
* Let’s begin with the objective. Success for the project was to **optimize the customer’s shopping experience** by surfacing the product information that **the customer was looking for**, rather than having the customer **manually seek it out**. This would eventually **decrease the average time from browse-to-buy**, aligning with Amazon’s top-line **business metric** of e-commerce growth.
* Working with the customer analytics team, I found that customers spent approximately **30% of their shopping time** analyzing reviews to find specific product attributes before making a purchase decision. As a result, the success metric for this project was set at a **25% reduction in browse-to-buy time**.
* For goal planning, I used the OKR (Objectives and Key Results) framework to ensure **strategic alignment** of our team’s goals with the overarching business growth goals.
  + The objective for the first quarter was set to **improve product review accessibility to enhance customer experience and drive e-commerce growth**, with 3 key results: (i) achieve a **25% reduction in browse-to-buy time**, (ii) **ensure at least 80% of customer feedback on summarized reviews was rated as helpful**, and (iii) contribute to a **1% lift in Amazon’s e-commerce growth**.
  + The objective for the second quarter was set to **build an internal conversational shopping experience for QA**, with 2 key results: (i) a RAG pipeline that could answer **70% of product-related questions and recommendations**, and (ii) acquire **samples across harmful input/output categories**.
  + The objective for the third quarter was set to **conversational shopping experience to enhance customer experience and drive e-commerce growth**, with 3 key results: (i) achieve a **30% reduction in browse-to-buy time**, (ii) **ensure at least 80% of customer feedback on chatbot responses was rated as helpful**, and (iii) contribute to a **0.1% lift in Amazon’s e-commerce growth**.

#### What was the OKR you set for this project?

* **Objective:** Improve the accessibility of product reviews to enhance customer experience and drive e-commerce growth.
* **Key Results:**

  1. Achieve a **25% reduction** in the average **browse-to-buy time** for customers by streamlining access to relevant product reviews.
  2. Ensure **at least 80% of product reviews** are automatically summarized and surfaced with minimal customer intervention.
  3. Increase **customer satisfaction scores** related to the product review experience by **15%** through improved review accessibility.
  4. Contribute to an overall **2% lift in Amazon’s e-commerce growth** by reducing customer decision-making time through review enhancements.

#### How do you define success for the team/product?

* Success for the product, **Rufus**, is defined by its impact on **reducing the “browse-to-buy” time** and increasing **customer satisfaction**. Specifically, achieving a **25% reduction** in the time it takes customers to find and purchase products is a key success metric, directly contributing to **e-commerce revenue growth**.
* Success means **improving the shopping experience** by making product information **more accessible and easier to navigate**, ultimately leading to higher customer confidence in purchase decisions. Positive customer feedback, measured through **user engagement** (e.g., likes/dislikes, feedback on chatbot responses), is a critical indicator.
* For the team, success is defined by **delivering milestones on time**, adhering to **sprint goals**, and ensuring **XF collaboration** flows smoothly. Clear, measurable results such as improving **RAG retrieval accuracy**, maintaining **low latency**, and **expanding features** like multilingual support also mark success.
* Success includes the team’s ability to **continuously improve the product**—iterating on features based on customer feedback, running successful **A/B tests**, and delivering **innovative solutions** that keep the product aligned with the broader business goals.
* Another key success factor is ensuring the chatbot operates with **robust safety guardrails** in place, adhering to **legal standards** such as **GDPR**. This ensures we build a product that is both **innovative and safe** for global deployment.

#### For that definition of success, what is the team’s goal? Follow up: How was that goal identified?

* **Team Goals:**

  + The primary goal for the team is to **reduce the time it takes customers to go from browsing to purchasing** by **25%**. This directly supports the business objective of **increasing e-commerce revenue** by making the shopping process faster and more user-friendly.
  + The team aims to **make product information more accessible** through **accurate and relevant review summarization** and **conversational assistance**. This involves improving the chatbot’s ability to surface key product details quickly and **boost customer confidence**.
  + A core technical goal is to optimize the **Retrieval-Augmented Generation (RAG) system** by improving **retrieval accuracy** and **reducing latency** in generating responses, ensuring a smooth and real-time customer experience.
  + Another goal is to make **Rufus multilingual** and deploy it in **more geographic regions**, ensuring it aligns with **local regulations** and **customer needs**, particularly around **safety guardrails** and **legal compliance** (e.g., GDPR).
  + The team also has a goal to **ensure scalability** of the underlying infrastructure to handle **increasing product and user data**. This involves optimizing the **OpenSearch vector database** and enhancing the chatbot’s ability to function effectively at scale.
* **How the Team’s Goals Were Identified:**

  + The goals were defined based on Amazon’s top-line business metrics, specifically **e-commerce growth**. By focusing on reducing **browse-to-buy time** and improving **customer satisfaction**, we ensured that the team’s goals directly contribute to these strategic priorities.
  + Through **data analysis** and **user feedback**, we identified that customers were spending too much time searching for product details in **reviews**. This insight drove the goal of **improving information accessibility** and minimizing customer effort.
  + The goals were also influenced by the **technical roadmap**. For example, the goal of improving **RAG system performance** and **scalability** was necessary to ensure that Rufus could handle increased **data load** and provide **accurate, real-time responses** as it scaled globally.
  + The goals were shaped by feedback from **XF teams**, such as product management, data science, legal, and compliance. This ensured that the goals were not only focused on innovation but also aligned with **safety**, **regulation compliance**, and **business feasibility**.
  + The broader vision of **improving the customer shopping experience** guided the specific goals related to **multilingual support**, **RAG system efficiency**, and **feature enhancements** that would make shopping on Amazon more intuitive and efficient.

### Roadmap (your contribution specifically) / “Roadmap” / 7 mins

* Working backwards from the goal and success metrics, I worked with the PM to devise a **multi-stage roadmap** based on inputs from **SMEs in my team** and **relevant external teams**, with **specific, measurable metrics associated with each step**.
* We visualized the project plan with a Gantt chart (shared on the project confluence), which offered a visual summary of timelines, dependencies, and milestones, providing a roadmap for effective scheduling and tracking.
* Now, let me walk you through each stage of our roadmap, going from **V0 to the final V2** (the “What”). After this, I’ll do a walk-through of how I put together a XF team effort to execute on this roadmap (the “How”).

#### V0/MVP - Summarizing Reviews

* V0 was the Minimum Viable Product (MVP) with an execution timeline of 3 months. The plan was to build an LLM to summarize product reviews, highlighting the **most salient features** associated with each product. For example, for an iPhone cover, the salient features within the summary could be quality, durability, and scratch resistance.
* **Evaluation and Metrics**:
  + **Offline Evaluation**:
    - **Lexical Metrics**: To measure the **lexical quality** of the reviews, we tracked BLEU and ROUGE scores – metrics that are commonly used for evaluating text generation.
    - **Semantic Metrics**: **Semantic performance** was measured using BERTScore and MoverScore – metrics that evaluate semantic textual similarity.
  + **Online Evaluation**:
    - **A/B Testing and Gradual Rollout**: After offline evaluation, early fishfooding, and dogfooding, we ran **A/B testing** with a **gradual rollout** starting with **5% of the US market** before expanding across **17 geos** worldwide.
    - **Online Customer Metrics**: The A/B tests tracked both the **key metrics** and **guardrail metrics**, with **conversion rate** (i.e., whether users **purchased the product**) as our **key metric**, and **latency** and **user reports** as our guardrail metrics.
* **Cost/Budget**: To ensure we stay within our cost constraints,
  I worked with the **Edge AI team** to create a pruned and knowledge-distilled version of the model (similar to Llama 3.2 1B).

##### What kind of reviewer metadata would be essential here?

* Essential metadata for a system that ranks product reviews by importance, relevance, and helpfulness for customers:

  1. **Reviewer Credibility**: This could be based on the reviewer’s past contributions, such as the number of reviews written, helpfulness ratings from other users, or verified purchase status.
  2. **Review Date**: Recent reviews are often more relevant, especially for products that undergo frequent updates or changes.
  3. **Product Usage Context**: Metadata indicating the specific model, version, or product variant the review pertains to, ensuring relevance to the item being viewed.
  4. **Review Length and Detail**: Longer, more detailed reviews might be given higher weight compared to brief or vague comments.
  5. **Reviewer Demographics**: If appropriate, factors like location or expertise could help contextualize the review (e.g., weather-specific products, technical equipment).
  6. **Sentiment Analysis Score**: Automatically generated sentiment ratings (e.g., positive, neutral, negative) based on the content of the review.
  7. **Engagement Metrics**: The number of upvotes, likes, or thumbs up/down given by other users can reflect how useful or trusted a review is perceived to be.

#### V1 - LLM + RAG, Pre-Rufus, No Guardrails

* The focus of V1 was to build an **internal Retrieval-Augmented Generation (RAG)-based LLM** to identify scenarios where the model could **produce unintended outputs** such as hallucinations or even **inappropriate outputs** such as hate speech. The end goal was a versatile conversational chatbot that would **bring down the browse-to-buy time significantly**.
* V1 spanned **3 months** going from building a RAG pipeline, offline evaluation, and dogfooding to collect safety data.

* **Evaluation and Metrics:**
  + **Offline RAG Eval**: To evaluate the performance of the newly introduced RAG system, we
    evaluated the retrieval and generation components of the system to measure how effectively the system retrieved relevant data and generated **coherent summaries** based on user queries and product attributes. In terms of metrics, we used **context precision, context recall** for the **retrieval portion** and **answer relevancy**, **faithfulness**, and **latency** for **output generation**. To measure the performance of the **end-to-end system**, we utilized similar **lexical and semantic match metrics** as V0.
  + **Dogfooding and Dataset Creation**: Post offline evaluation, the system went through **2 months of dogfooding**, as it was an internal system with **no guardrails**. This enabled us to create our **safety benchmarking** dataset for Rufus by leveraging feedback from internal users.
* **Cost:** The major cost v/s performance trade-off was **choosing the embedding model**, so we weighed various options such as BERT, ALBERT, DistilBERT based on where they landed on the cost v/s performance graph, and eventually opted for **DistilBERT**.

#### V2 - Rufus as you see it today, Multilingual + Guardrails + Continuous Monitoring and Learning

* The final stage V2, is now live on Amazon.com as Rufus, a fully-fledged **multilingual** chatbot with **guardrails both at the input and output**, deployed in **17 geos** around the world.
* V2 spanned **6 months**, going from dataset curation, fine-tuning, red-teaming, dogfooding, and A/B testing.
* **Evaluation and Metrics**:
  + **Red Teaming:** To ensure Rufus adhered to our safety standards, it underwent **red-teaming, both internally and with external vendors** to identify potential vulnerabilities, ensuring safety and reliability before going live.
  + **Offline Evaluation**: Similar to V0.
  + **A/B Testing and Gradual Rollout**: Similar to V0, we carried out offline eval, dogfooding and subsequently **A/B testing** with a **gradual rollout** starting with **5% of the US** before expanding across **17 geos** worldwide.
  + **Online Customer Metrics**: The A/B tests tracked both the **key metrics** such as the **conversion rate**, **user’s likes/dislikes of the chatbot responses** and **guardrail metrics** such as if the user re-asked the query with a **semantically different variation**, or **returned to read user reviews**.  
    <!– - **Fine-tuning the Model with Safety Datasets**: The process involved fine-tuning the model using **datasets that were curated as part of the V1 internal launch** to reflect Amazon’s safety policies. This dataset included examples of **safe and unsafe responses** to ensure the model understood the boundaries of acceptable interactions.
  + **Pre-defined Responses and Content Moderation**: We created **pre-defined responses for harmful user queries** and also added **content moderation filters** that automatically flagged and blocked harmful responses.
  + **UI Design**: We collaborated closely with the **UI designers** to create an intuitive interface that seamlessly integrated Rufus into the shopping experience, ensuring a **smooth** and **visually appealing** user interaction. –>
* **Cost**: Although **data annotation costs** for V2 were high, prioritizing both **quality and quantity** of annotated data was essential to ensure alignment with **safety protocols** and a **successful rollout**.

##### Explain the implementation details around guardrails.

* **Guardrails**:
  + Rule based: PII data leak, toxic language, financial advice, sensitive topics: politics and opinions
  + Input guardrails: flag content before it gets to LLM
  + Output guardrails: validate LLM response before it gets to user
* **Building Guardrails**:
  1. **Data Collection and Preparation**:
     + Based on data collected from V1, curate and annotate safety-critical scenarios with safe responses (e.g., inappropriate inputs/outputs, PII data leak, toxic language, financial advice, sensitive topics: politics and opinions, harmful requests)
     + Label escalation scenarios for human intervention.
  2. **Training Rufus**:
     + Fine-tune using instruction-tuned safety data.
  3. **Production Guardrails**:
     + Implement NLP-based filters for real-time monitoring (block harmful content).
     + Ensure safe default responses when unsure.
  4. **Continuous Monitoring and Learning**:
     + Monitor safety performance using dashboards by collecting user feedback.
     + Continuously update instruction-tuned data based on new scenarios.

#### How did you identify the roadmap for the half? (What were your contributions)

* I begin by working backwards from the key business metrics (“the north star metrics”) we aim to optimize and setting team goals that are strategically aligned with these broader business objectives. For goal planning, I use the OKR (Objectives and Key Results) framework to ensure this **strategic alignment** between our team’s goals with the overarching business growth goals.
* From there, we work backward from what success looks like—identifying the projects to pursue that would drive team metrics. Working backwards from the projects, together as a team, we identify the tasks needed to be done to hit our goal. I like to ensure that this process is highly inclusive and collaborative, by encouraging input from all relevant team members—especially SMEs and XF partners.
* Once we have a clear vision and aligned team goals, we identify the appropriate tasks to pursue over a six-month period to execute on the team’s goal based on resource availability, skillset in the team, etc. We prioritize tasks using the RICE framework, ensuring that we focus on the initiatives with the highest impact and feasibility.

#### How do you identify and track dependencies?

* To identify dependencies, I work backwards from the roadmap to **map out key milestones**, working backwards from the **milestones**, I determine the **deliverables** that rely on other teams’ contributions or resources based on their charter and scope.
* To promote transparency and coordination, the PM on my team establishes a shared Wiki page to track these dependencies and timelines, giving our XFN clear visibility into the project’s broader scope.
* Once dependencies are identified, I secure alignment with the corresponding teams to agree on the scope, specific deliverables, and timelines.
* We track progress on dependencies through **weekly sprints** (with **daily standups**), using **Jira** for task tracking, and **the shared Wiki** for the project roadmap and timelines. Each sprint was tied to specific **milestones**, which served as intermediate checkpoints toward the overall project goals.
* I coordinated with XF managers over **weekly syncs** to ensure **alignment across teams**, while the PMs handled **daily stand-ups** to ensure **day-to-day task tracking**.

### Put together cross-team effort / “XF Planning and Alignment” / 3 mins

* Now, let me touch upon about how I obtained XF alignment to execute on this roadmap. I started off by identifying **XF dependencies** and **arranged a series of syncs** with our XFN to get their **buy-in** and **secure the necessary resources**. As part of these discussions, I communicated the broader impact of the project, highlighting how their contributions would **mutually benefit** both their metrics and ours as well as ultimately drive Amazon’s business objectives.
* Using the **AIM framework** (Audience, Intent, Message), I tailored my narrative to align with the specific backgrounds of my technical and non-technical audience.
* Once we had XF alignment with agreed-upon deliverables and timelines, I setup a **shared Wiki page** to track these **dependencies and timelines**, giving all teams clear visibility into the **project’s broader scope**.

* **End Result**: The end result was a detailed **XF plan** established collaboratively, with **tasks** assigned to each XF partner, each with its defined **timelines and priorities**.
  <!– - **GenAI Team**: Focused on fine-tuning the LLM, integrating safety guardrails, and handling **real-time monitoring**.
  + **Product Catalog Team**: Responsible for providing **product data** in the right schema and maintaining the product **OpenSearch database**.
  + **Customer Analytics Team**: Tasked with **running A/B experiments**, owing metrics to track, analyzing experimental results.
  + **Legal Team**: Overseeing **data privacy compliance** tasks.
  + **PM Team**: Task-tracking by coordinating daily stand-ups. –>

#### How do you work with cross functional partners XFNs?

* **Early Stakeholder Engagement**: Identify and involve XF early, right after an initial roadmap, to secure resources and set clear expectations.
* **Align on Shared Objectives**: Establish mutual goals, aligning project outcomes with top-level business metrics.
* **AIM Framework for Communication**: Use AIM (Audience, Intent, Message) to tailor discussions, ensuring each partner understands the project’s impact on their own metrics and priorities.
* **Structured Communication**: Maintain consistent updates and tracking through dedicated channels (e.g., weekly syncs, Confluence) for transparency.
* **Mutual Accountability**: Define deliverables and dependencies, regularly reviewing progress to address blockers and maintain alignment.

#### What are some of the ways you can have influence over other teams?

1. **Align on Shared Goals:** I like to emphasize the **mutual benefits** and how each team’s work contributes to the **broader business objectives**, ensuring everyone is working toward a common purpose.
2. **Leverage Data and Metrics:** Use **data-driven insights** to show the impact of the project, making it easier to influence priorities and justify resource allocation.
3. **Build Strong Relationships:** Establish **trust and rapport** with key stakeholders through regular communication and **empathy for their challenges**, fostering a collaborative environment.
4. **Involve Leadership Early:** Secure **leadership buy-in** to reinforce the project’s importance, helping influence **priority shifts** and ensuring timely support from other teams.

#### How do you work with non-technical stakeholders?

* When working with **non-technical stakeholders**, it is crucial to focus on the big picture, business impact, and outcomes, ensuring the message is clear, concise, and aligned with their goals.

1. **Using the AIM Framework to Link Approach/Project to Business Impact:** The **AIM framework** (Audience, Intent, Message) lends itself well to ensure effective communication with non-technical stakeholders. I tailor my narrative based on the specific background of my audience (say **marketing, finance, or legal teams**), by framing my **Intent** as **seeking alignment and obtaining their buy-in**, and crafting my **Message** to focus on the **big picture impact** rather than the **low-level implementation details** by linking the project to **shared business objectives**. I emphasize how the project will enhance **key top-line business metrics** (say, **customer satisfaction**, **sales**, and **conversion rates**). For instance, using clear, relatable terms that align with the stakeholder’s business objectives to convey how **improving customer experience** through accurate and relevant product information would directly lead to higher **sales**, helps effectively drive the message.
2. **Distilling Concepts to their Core:** When discussing complex technical concepts, I focus on distilling them down to their **most essential elements** to make them understandable for non-technical stakeholders. In some cases, I’ve used a **contrapositive** to help illustrate the value of the proposal. For instance, explaining that **without** a specific feature (e.g., retrieval-augmented generation), the system would rely on outdated or generic information; but with it, we can dynamically retrieve the latest and most relevant reviews. This approach makes the value of the feature clear, emphasizing how it enhances the overall product experience.
3. **Anticipating and Proactively Addressing Concerns:** Lastly, as with all kinds of stakeholders and especially non-technical ones, it’s crucial to **anticipate potential concerns** and proactively address them by explaining how the chosen approach mitigates risks and improves performance. For example, if stakeholders are concerned about **latency** when introducing a new real-time recommendation system, I would detail how implementing **caching mechanisms** can significantly reduce response times, enhancing the user experience. I also link these improvements to **business outcomes**, such as faster load times improving **customer satisfaction** and directly impacting **conversion rates**. All in all, my philosophy is to secure stakeholder confidence in the proposed solution by demonstrating the connection between addressing technical challenges and measurable business metrics.

### Delivery + Risks / “Delivery: Task Tracking + Risk Mitigation” / 10 mins

* Let’s talk about project delivery, specifically task tracking and risk mitigation.

* For **day-to-day task tracking**, we used a **Scrum-based Agile framework** with **weekly sprints** and daily **stand-ups** to track progress and address any blockers. We used **Jira** for task tracking and setup a **shared Wiki with our XFN** that had details of the project roadmap and timelines. Each sprint was tied to specific **milestones**, which served as intermediate checkpoints toward the overall OKRs.

* We applied the **RICE framework** (Reach, Impact, Confidence, and Effort) for task prioritization, allowing us to systematically evaluate and prioritize tasks.
  This ensured that the most valuable tasks were prioritized in each sprint, aligning with our broader project objectives.

* I coordinated with XF managers over **weekly syncs** to ensure **alignment across teams**, while the PMs

  ran **sprint planning**, **sprint reviews**, and **daily stand-ups**, ensuring our priorities were clear and any issues were promptly addressed.
* **V0**:
  + V0 required building a rule-based system that could filter a dataset of reviews based on reviewer credibility (helpful/verified), recency, relevance, and other metadata. After human annotation on this curated dataset with the most salient features identified in each review, we **fine-tuned** the Titan LLM from Amazon to generate cohesive summaries.
  + **Result/Impact of V0**: The end result was an **8%** reduction in the **browse-to-buy time**, in line with our expectations.
* **V1:**
  + To execute on our vision for V1, I worked closely with a principal engineer on my team to define the technical requirements, breaking the work into **3 key pillars**: (i) building a RAG pipeline using **Amazon’s OpenSearch vector database** with embedded reviews and doing an ANN-search to retrieve the top-\(k\) summaries, (ii) setting up **API endpoints for the LLM**, and (iii) evaluation of the **end-to-end RAG pipeline**.
  + **Result/Impact of V1**: The end result of V1 was a **safety benchmarking** dataset by leveraging feedback from internal users, which in turn, powered V2.
* **V2**:
  + To build guardrails for Rufus, we got human annotations for **safety-critical data** gathered from the prior phase (e.g., toxic language, PII data, financial advice, other harmful inputs/outputs). The model was fine-tuned on this dataset with LoRA (a PEFT method), and implementing **rule-based guardrails** to block harmful content at both the **input and output**.
  + Lastly, we also built a **continuous monitoring and learning** pipeline by setting up a dashboard to track performance based on user feedback and updating the model based on new data from the field.
  + **Result/Impact of V1**: The end result of V2 was Rufus live on Amazon.com, rolled out to 17 geos.

#### How do you track progress on all projects? / Planning (OKRs) + Tracking (Sprint) Process

* To ensure that the **day-to-day execution** stayed in-line with the **broader vision**, we employed a **hybrid framework** of using **Agile project management** – specifically a Scrum and Kanban framework – for **iterative development and continuous delivery**, while ensuring broader strategic alignment with **OKRs (Objectives and Key Results)** with specific, measurable metrics.
* Progress was tracked through **weekly sprints**, using **Jira** for task tracking, and a **Wiki** shared with our XFN for the project roadmap and milestone dates. Each sprint was tied to specific **milestones**, indicating significant progress toward project goals.
* I coordinated with **XF managers** over **weekly syncs** to ensure alignment across teams, while the PMs ran **daily stand-ups** to ensure day-to-day task tracking and address any blockers.

#### Why do teams fall behind schedule?

* Teams often fall behind when the project’s requirements aren’t clearly defined from the start, leading to **misaligned expectations** or **scope creep**, where additional features or tasks are added mid-project without adjusting timelines. Poor communication between XF teams can also lead to **misunderstanding of priorities**, causing delays in key deliverables and missed deadlines.
* The team may not fully anticipate the **technical complexity** or **dependencies** involved in certain tasks, causing delays due to underestimated complexity.
* When working with multiple teams, delays in one team’s work (e.g., data or resource availability) can create a **ripple effect**, causing others to fall behind due to blocked tasks or misaligned timelines.
* Example: As part of building Rufus, my team was integrating a **Retrieval-Augmented Generation (RAG) system** with data from Amazon’s **product catalog team**. We fell behind schedule because the **product catalog team** delivered data in a schema that was different from what we expected. This misalignment delayed the integration process for our chatbot, and we had to rework parts of our system to accommodate the new data format. We mitigated this by using **mock data** as the product team fixed the schema to keep testing and coordinated more closely to **adjust future timelines**.

#### What were the risks to the project and how did you mitigate them? / “Risk Mitigation”

* Proactively identifying risks and tracking deadlines – especially for a high-stakes XF project of this scale – was critical to ensure **smooth delivery**. Weekly sprints, 1:1s, and milestone tracking allow for **early detection** of potential issues. When risks arose, I focused on identifying root causes and immediate mitigation strategies.
* In critical situations, daily stand-ups can help the team course-correct quickly. Keeping leadership informed early also ensures transparency and enables timely resolution of risks by getting their support.
* The following risks were identified, and mitigation strategies were employed to minimize their impact:
  1. **Scope Creep**:
     + As the project evolved, there was a risk of **scope expansion**, where additional features were requested mid-sprint. For example, after initial feedback on Rufus, the product team wanted to include **more complex features**, such as **integrating video product reviews** and **incorporating voice-activated queries**, which could have delayed delivery. To mitigate this, we implemented **strict change control processes**, where any new features were evaluated for feasibility in future releases rather than the current sprint.
  2. **Infrastructure Scaling Issues**:
     + As our **back-end Vector database** – powered by OpenSearch – grew with new product data, **performance degradation risks** multiplied, particularly during peak traffic and high QPS. To mitigate this, we conducted **load testing**, optimized the **database sharding strategy**, and employed **serverless services to scale on demand**. Additionally, **real-time monitoring tools** were implemented to track performance and address scaling issues proactively.
  3. **Technical Debt / Maintenance Challenges**:
     + The **rapid iteration cycle** increased the risk of accumulating **technical debt**. For example, **shortcuts taken to meet tight deadlines**, such as deferring necessary **code refactoring** or **skipping documentation**, could lead to long-term maintenance challenges. We mitigated this by scheduling **dedicated time in future sprints** to address and refactor technical debt, ensuring **long-term stability and scalability** of the codebase.
  4. **Data Privacy and Compliance Risks**:
     + Due to the **large volume of customer data**, there was a high risk of violating **data privacy regulations** (e.g., GDPR). To prevent exposing sensitive data, we collaborated with **legal teams** to ensure compliance and integrated **automatic redaction tools** to remove **PII before processing queries**.
  5. **Safety and Guardrail Failures**:
     + Given the **chatbot’s customer-facing nature**, there was a significant risk of generating **inappropriate or harmful content** without proper safeguards. To mitigate this, we implemented **robust safety guardrails**, including **rule-based filters**, and conducted ongoing **human-in-the-loop testing** to identify and prevent harmful outputs before release.
  6. **Integration Delays with Other Teams**:
     + Coordination with **XF teams**, like the product catalog and customer data teams, posed a risk of delays when timelines misaligned. For instance, **delays in receiving updated data schemas** from the product catalog team could hinder integration with the RAG system. To mitigate this, we scheduled **weekly syncs with stakeholders** and developed **contingency plans**, such as using **mock data**, to keep development ongoing while awaiting dependencies.

### Failures + Learning / Introspection / Reflection / 5 mins

* **Lessons in XF Alignment and Retrospective Improvements:** Throughout this journey, there have been several valuable lessons learned. While we made significant progress, looking back, there are a few key areas where I would approach things differently.

#### What was the biggest challenge you faced during this project?

* Given the project’s extensive XF scope, achieving alignment across teams took considerable time. The complexity of coordinating numerous moving pieces across 2 business units (AWS GenAI, Amazon Shopping) and 7 XF partners (**GenAI Science**, **product catalog team**, **customer analytics**, **legal/compliance**, **UI design**, **QA testing**, **infrastructure**) required alignment with stakeholders early on, as each team had their own quarterly priorities and specific metrics to optimize.
* In fact this oversight led to my biggest mistake in execution. I initially missed consulting the infrastructure team managing **AWS Data Pipeline**, a service we initially depended on for orchestrating ETL flows critical to Rufus’s LLM deployment.
* This service was essential for automating the movement and transformation of data across AWS services before feeding into our model. Given that AWS oversees over **200 evolving services**, some, like the **AWS Data Pipeline**, are occasionally **deprecated or sunset** as part of their lifecycle.
* As I was new to the role and hence the AWS ecosystem, I hadn’t anticipated this **service deprecation**, which required us to **migrate to AWS Step Functions**. This eventually led to us having to **re-design portions of the architecture** and **redo sprint planning** to accommodate the transition. To stay on track, we had to **de-prioritize some tasks to later sprints**, which ultimately led to a **2-week delay**.
* Had I engaged the relevant team from the start, we could have **avoided setbacks by anticipating roadmap changes** and proactively adjusting our plan. This early collaboration would have avoided delays and ensured smoother progress by aligning our approach with upcoming changes.
* Since this experience, I’ve made it a priority to **map dependencies** and **secure XF alignment** as early as possible in the project lifecycle. This approach has enabled me to **better anticipate risks**, **align resources efficiently**, and **ensure smoother project execution without unexpected disruptions**.

#### How did you recover from a failed delivery? / “Recovering from a Failed Delivery”

* In one instance, we missed a delivery due to the **unexpectedly complex integration** of our LLM with a XF system involving product catalog and customer data from Amazon Shopping. The delay was primarily caused by a **misalignment in the expected schema for the data** received from the product catalog team, which slowed the integration process for our RAG pipeline.
* Trying to resolve the issue by taking steps at our end, we **looked into adjusting our code to accept a different schema**, but this would have introduced **latency issues**—especially problematic given the **real-time performance requirements** of the chatbot—since it would have required additional processing to convert the data into the necessary format.
* To keep the ball rolling, we **implemented a contingency plan using mock data**, allowing us to continue testing the RAG system while awaiting the finalized schemas. This **proactive approach ensured the overall project stayed on track**, and we used the experience to **refine our coordination processes** with XF teams to mitigate future delays.
* Instead of assigning blame, I treated the **missed delivery as a learning opportunity**, incorporating the insights into our **future sprint planning** and ensuring **tighter alignment across XF teams**.

#### What was your biggest mistake / failure as part of this project and outside this project? What did you learn from it?

* **Story 1 (MISTAKE IN THIS PROJECT - XF ALIGNMENT)**:
  + Given the project’s extensive XF scope, achieving alignment across teams took considerable time. The complexity of coordinating numerous moving pieces across 2 business units (AWS GenAI, Amazon Shopping) and 7 XF partners (**GenAI Science**, **product catalog team**, **customer analytics**, **legal/compliance**, **UI design**, **QA testing**, **infrastructure**) required alignment with stakeholders early on, as each team had their own quarterly priorities and specific metrics to optimize.
  + This oversight led to a roadblock for the project since I failed to consult the infrastructure team managing **AWS Data Pipeline**, a service we initially depended on for orchestrating ETL flows critical to Rufus’s LLM deployment.
  + This service was essential for automating the movement and transformation of data across AWS services before feeding into our model. Given that AWS oversees over **200 evolving services**, some, like the **AWS Data Pipeline**, are occasionally **deprecated or sunset** as part of their lifecycle.
  + As I was new to the role and hence the AWS ecosystem, I hadn’t anticipated this **service deprecation**, which required us to **migrate to AWS Step Functions**. This eventually led to us having to **re-design portions of the architecture** and **redo sprint planning** to accommodate the transition. To stay on track, we had to **de-prioritize some tasks to later sprints**, which ultimately led to a **2-week delay**.
  + Had I engaged the relevant team from the start, we could have **avoided setbacks by anticipating roadmap changes** and proactively adjusting our plan. This early collaboration would have avoided delays and ensured smoother progress by aligning our approach with upcoming changes.
  + Since this experience, I’ve made it a priority to **map dependencies** and **secure XF alignment** as early as possible in the project lifecycle. This approach has enabled me to **better anticipate risks**, **align resources efficiently**, and **ensure smoother project execution without unexpected disruptions**.
* **Story 2 (MISTAKE - OUTSIDE THIS PROJECT - PROJECT)**:
  + Back in early 2023, I saw a unique opportunity to capitalize on the emergence of LLMs shortly after ChatGPT’s initial launch. At the time, I was new manager who ran Alexa’s Query Understanding and Personalization team, and I believed that integrating LLMs could be a game-changer for the product. Alexa was largely a combination of rule-based pipelines and shallow models and heavily constrained to narrow use-cases like music playback, reminders, and shopping. I envisioned a paradigm-shift from this rigid model to an intelligent, open-ended assistant that could engage in natural, flowing conversations.
  + Motivated by this potential, I charted a bold initiative to replace Alexa’s traditional shallow model pipeline with an LLM-driven architecture. I saw this not only as a technical upgrade, but as a way to reimagine the assistant experience entirely. However, in hindsight, the environment was still too early. LLMs were in their nascent stages—scaling laws were still being formalized, inference latency was poorly understood and hard to predict (projection models didn’t exist), and foundational tooling like synthetic data generation was still underdeveloped.
  + Despite these uncertainties, the potential upside felt large enough to justify a focused pivot. I made the call to redirect my team’s energy entirely toward this effort and successfully convinced senior leadership to deprioritize other ongoing initiatives in favor of this bet. This created a situation where we essentially put all our eggs in one basket, in the pursuit of wanting to be the first to market an LLM-powered voice assistant.
  + Unfortunately, as we began experimenting, it became clear that even with smaller models, the latency was unmanageable for real-time voice interactions. There were promising signs in terms of conversational quality and relevance, but the technical constraints ultimately blocked us from getting to production readiness. After several months of intense work, we had to abandon the project.
  + This decision had ripple effects. Other deliverables that had been put on pause suffered a six-month delay, and the team experienced the morale dip that often comes with a high-effort project being sunset prematurely. In many ways, we were ahead of our time—the vision was right, but the ecosystem hadn’t caught up yet. Amazon only recently announced Alexa+—an LLM-powered version of Alexa—in late March 2025. Had we successfully delivered on this back in 2023, we would have been the first voice assistant powered by LLMs, capable of engaging in much more natural, open-ended conversations with users with a .
  + The good news is that I had a lot of learnings through this experience. In retrospect, I should have structured the effort differently: I’ve since adopted a more measured approach to moonshots—keeping a portion of the team focused on forward-looking bets, while ensuring that core deliverables and shorter-term wins continue to move forward in parallel. More importantly, investing in earlier prototyping and gathering feedback from partner teams before fully committing. This experience deepened my understanding of how to manage innovation risk in a fast-moving space and how to build long-term vision without compromising near-term execution.
* **Story 3 (MISTAKE - OUTSIDE THIS PROJECT - MANAGEMENT)**:
  + One of the **biggest mistakes I’ve made as a people manager** was growing a high-performing IC into a manager role without fully aligning on their motivations or readiness for the shift, which ultimately resulted in team disruption. At the time, I was a new manager on the team and still getting to know the individual strengths, motivations, and “superpowers” of each person. We also had an urgent business need for additional management capacity, and this IC stood out due to their strong technical contributions and ownership. I saw their growth as an opportunity to address this gap while rewarding their performance.
  + We spent several months working on their development—delegating leadership responsibilities, having them shadow me in team planning, and slowly transitioning them into more strategic conversations. While their technical depth helped them lead projects effectively, there were early signs that skills like **cross-functional communication**, **stakeholder management**, and **prioritization under ambiguity** weren’t coming as naturally. I viewed these as coachable gaps and believed they’d ramp up with time and support.
  + However, once officially in the manager role, feedback from the team indicated growing misalignment. **Communication with non-technical stakeholders was often unclear**, and internal team conversations started to surface concerns about **lack of direction and shifting priorities**. Despite being technically strong, the new manager struggled to represent the team’s needs externally and to make crisp prioritization decisions that accounted for business trade-offs.
  + This led to decreased confidence in leadership from the team and ultimately contributed to the departure of a respected technical leader who had previously relied on clear technical direction and stable prioritization. In hindsight, I should have spent more time **understanding this IC’s true career motivations** before encouraging them into a role that may not have aligned with their strengths or aspirations. Their interests leaned more toward technical depth than people leadership, and by not clarifying that upfront—especially as someone still learning the unique capabilities of the team—I put them in a position that wasn’t set up for success, while inadvertently creating risk for the broader team.
  + The key lesson for me was the importance of **not assuming that high technical performance leads to great people leadership**, especially when business needs create pressure to fill management gaps quickly. Since then, I’ve become more deliberate about **checking for intrinsic motivation and leadership signals**—such as how someone thinks about coaching others, how they approach prioritization across multiple stakeholders, and whether they show natural ownership over team health and outcomes beyond their own work.
  + To smoothen this, I’ve put in place a structured **“IC2M” development plan** that spans 3 months and is designed to target the core competencies needed for successful transition into management. As part of this plan, candidates take on management of 3 direct reports while focusing on specific **leadership competencies** including **goal-setting**, **hiring and talent acquisition**, **cross-functional planning and communication**, **running effective 1:1s**, and **driving results through their team** rather than individual contribution. This approach allows us to assess their potential in real scenarios while giving them structured support and feedback to grow the necessary muscles before stepping into a formal manager role.
    <!– - My biggest mistake was that I underestimated the importance of identifying the **XF dependency graph** as early as possible in a highly XF project like this one. This early mapping is crucial for **socializing the project** and securing **early buy-in** from all relevant teams, preventing **potential delays and misalignment** and maximizing project success and impact. This led to me making the mistake of not consulting one of the infrastructure teams that managed **AWS Data Pipeline, which we initially relied upon to orchestrate ETL data flows necessary for Rufus’s LLM deployment**. This service was essential for automating the movement and transformation of data across AWS services before feeding into our model. Given that AWS oversees over **200 evolving services**, some, like the **AWS Data Pipeline**, are occasionally **deprecated or sunset** as part of their lifecycle. Being relatively new to AWS, I didn’t foresee this outcome, which led to unexpected rework, delays in our timeline, and additional coordination efforts with the infrastructure team to migrate to a replacement service, ultimately impacting both our resource allocation and overall project momentum.
  + As the project got into execution, the original infrastructure—designed before AWS deprecated key components—began to **jeopardize our timeline**. With the sunsetting of AWS Data Pipeline, we had to **migrate to AWS Step Functions**, which required us to **re-design portions of the architecture** and **revisit our sprint planning** to accommodate the transition. To stay on track, we had to **de-prioritize some tasks to later sprints**, which ultimately led to a **2-week delay**. Involving the AWS infrastructure team earlier would have allowed us to **anticipate service deprecations** and proactively adjust our designs. Engaging XF teams early also ensures they can incorporate the project into their own priorities and **track second-hop dependencies**, minimizing the risk of setbacks.
  + Since this experience, I’ve made it a priority to **map dependencies** and **secure XF alignment** as early as possible in the project lifecycle. This approach has enabled me to **better anticipate risks**, **align resources efficiently**, and **ensure smoother project execution without unexpected disruptions**. –>
* **Story 4 (GENERAL MISTAKE - OUTSIDE THIS PROJECT - DO NOT USE)**:
  + One of the **biggest mistakes I’ve made as a people manager** was failing to be **proactive in providing upward feedback** to my manager. To set context, my manager recently inherited our org of 80 people after my previous manager’s departure. He was unfamiliar with our team’s specific workflows and processes, and his approach to management was drastically different from what the team was used to. He had a vision of **revamping our processes** to increase operational efficiency, which was well-intentioned but didn’t account for the unique needs and workflows we had developed over time.
  + For instance, our **bi-weekly project updates** had been structured to allow for a balance between in-depth status reporting and maintaining the team’s autonomy. This process ensured that team members weren’t bogged down by excessive oversight, allowing them to focus on execution. Additionally, we had **streamlined our approval process** to prevent bottlenecks, allowing for **quicker decision-making during critical project phases**. This change was implemented after a previous project experienced **a two-week delay due to multiple layers of sign-offs**, which resulted in a missed deadline. By streamlining approvals, we avoided these delays on subsequent projects, which significantly improved our ability to move quickly during important phases.
  + Unfortunately, I failed to communicate these nuances to my new manager. I didn’t explain that these workflows had already been optimized based on specific challenges we had encountered and that sudden changes—such as doubling the cadence of our status meetings and additional approval layers—would likely **disrupt our momentum, delay decision-making, and diminish the team’s sense of ownership.**
  + When the changes were introduced, feedback from both **personal 1:1 discussions and anonymous polling of daily connection scores** revealed growing frustration over challenges in meeting project deadlines due to the increased focus on status reporting. This led to **increased frustration and lowered morale** in the team, outcomes that could have been mitigated had I **been more proactive in providing upward feedback**. Instead, I waited until it became a more significant issue, which resulted in **unnecessary friction** within the team.
  + Looking back, I learned the importance of being **proactive in providing upward feedback**, especially when changes could significantly impact team dynamics. Since that experience, I’ve made it a priority to **proactively advocate for my team’s needs** and ensure that leadership **has the relevant context** about how decisions may affect the team’s overall productivity and well-being.

##### What is AWS Data Pipeline?

* AWS Data Pipeline is a managed ETL (Extract, Transform, Load) service that helps automate the movement and transformation of data across AWS services and on-premises data sources. With Data Pipeline, users can create complex data workflows that handle data processing, transformation, and movement between different AWS services (like Amazon S3, Amazon RDS, Amazon DynamoDB) and external sources on a scheduled basis. The service enables data processing in intervals—whether hourly, daily, or monthly—by orchestrating tasks and ensuring they run in the correct sequence.

###### Key Features of AWS Data Pipeline

1. **Orchestration and Automation**: Automates data workflows, including dependency management, retries, and failure handling.
2. **Scalability and Reliability**: Manages data processing tasks over large datasets and can scale as needed.
3. **Data Transformation**: Supports data transformation through integration with AWS resources and custom shell scripts.
4. **Scheduling Flexibility**: Allows for setting up pipelines that trigger at specific times or intervals.
5. **Integrated with AWS Ecosystem**: Facilitates easy data movement and transformation between AWS services.

* AWS Data Pipeline has historically been popular for its ease of scheduling and workflow management within the AWS ecosystem. However, AWS has introduced newer tools like **AWS Glue** and **Step Functions**, which provide enhanced features, pushing AWS Data Pipeline toward gradual deprecation in favor of these more advanced solutions.

#### What are your areas of growth around execution? / Tell me about a growth area you’re currently working on.

* **Story 1 (Evolving from problem-solver to coach)**:

  + When I joined my current team, as part of the onboarding process, I proactively decided to own a key part of the codebase — specifically around model serving infrastructure. It felt like the right entry point: owning a critical component was a great way to get deeply onboarded to our infra, and there was also a clear business need at that point for someone to step in with strong technical ownership.
  + In the beginning, that ownership naturally involved a lot of direct problem-solving — debugging rollout issues, unblocking integration blockers, and firefighting system bottlenecks. But as I ramped up and the team started growing around me, I realized that continuing to lead through hands-on problem-solving wouldn’t scale. It was becoming clear that my impact now needed to come through enabling others to lead — not just delivering fixes myself.
  + So one growth area I’ve been focusing on over the last couple of years is evolving from being a hands-on problem-solver to more of a coach and enabler for the people around me.
  + Having a strong instinct to jump in and solve problems directly is useful in the short term, but I began to notice that it had some hidden downsides: engineers felt less ownership, and we weren’t building the next layer of technical leadership fast enough. Whether it was debugging a finicky model serving pipeline or unblocking a deployment issue at the eleventh hour, my goal as the team’s manager is to guide thinking rather than offer direct answers – as the old Chinese proverb goes “give a man a fish and you feed him for a day. Teach him how to fish and you feed him for a lifetime”. It’s slower in the moment, but it builds decision-making muscle within the team — and I’ve seen it pay off as engineers step up with greater clarity and confidence.
  + I’ve been very intentional about shifting that behavior. These days, when someone brings me a problem, I pause before suggesting anything. Instead, I’ll ask questions like, “What options have you explored?” or “What are the trade-offs you’re seeing?”
  + One example was with a mid-level engineer who was leading their first cross-team infra migration. Initially, they came to me frequently for direction — which libraries to use, how to manage timeline risks, how to communicate blockers. Rather than give them prescriptions, I helped them build a lightweight decision-making framework, and we established weekly coaching sessions that focused less on *what* to do and more on *how* to lead. Within a few months, they weren’t just managing the migration — they were running design reviews, negotiating cross-org priorities, and mentoring junior engineers through it.
  + I have learned to be more of a symphony conductor than a violinist. I’ve come to realize that being a great leader isn’t about solving problems at scale — it’s about creating the conditions where others can. Coaching isn’t passive — it’s one of the most high-leverage things I can do. It requires patience, trust, and the discipline to sometimes sit on an answer and let someone else find their way to it.
  + It’s still a growth area for me — especially when things are moving fast and the stakes are high. But the more I practice it, the more I see the long-term compounding value it brings — both to the individuals I support and to the technical depth and resilience of the team as a whole.
* **Story 2 (GENERAL GROWTH AREA - OUTSIDE THIS PROJECT - SAYING YES)**:

  + **Developmental Area:** Striking the right balance between delivering high-quality work on fewer, high-impact projects v/s spreading myself—and the team—too thin. Balancing my **enthusiasm** for new tasks with our focus on core priorities. My default answer to requests in gray areas—tasks that were borderline beyond our scope or those we might not have full bandwidth for—was often a “yes,” driven by my enthusiasm to contribute. In my mind, saying **“yes” unlocked a world of possibilities**, enabling the team to explore new opportunities, develop new XF relationships, expand our impact, and contribute to a wide range of initiatives. However, this resulted in the team struggling to strike a balance between addressing maintenance/backlog items and focusing only on new initiatives.
  + **How I Recognized the Growth Opportunity:** I recognized this growth opportunity through feedback shared during 1:1s with my team.
    My inclination to take on additional responsibilities was seen as positive and encouraging by stakeholders, but over time, the cumulative impact of these gray-area tasks was creating challenges in delivering against our core commitments. This feedback highlighted that while enthusiasm was valuable, it needed to be tempered with intentional prioritization.
  + **Steps to Improve:** Being **self-aware** of this gap, I have taken a couple of steps to make improvements.

    1. **Analyzing Requests Thoroughly:** I adopted a deliberate approach to evaluating new asks, taking into account their alignment with strategic goals, impact, and the team’s available bandwidth.
    2. **Prioritizing Transparency and Openness:** When declining tasks, I focused on being transparent about our current priorities. This helped stakeholders understand how we were allocating resources and why certain requests couldn’t be accommodated.
    3. **Collaborating with the Team:** I engaged the team in discussions about prioritization, ensuring they felt empowered to assess the feasibility of requests and say “no” when appropriate.
    4. **Ruthless prioritization**: I’ve ruthlessly prioritized is essential in cases of extreme load, especially when our team was swamped. Without clear prioritization, even the most enthusiastic efforts can dilute focus and hinder overall impact.

  + Over time, I realized that saying **“yes” to something means saying “no” to many other things.** While my initial philosophy of saying “yes” opened up a world of possibilities, this experience taught me that saying **“no” is not about shutting doors; it’s about choosing the right ones to walk through.** By focusing on priorities and communicating effectively, I’ve been able to drive better outcomes for my team and the overall business.
  + This self-awareness and adaptation have enabled me to balance ambition with sustainability, ensuring my enthusiasm contributes positively without overwhelming the team.
* **Story 3 (GENERAL GROWTH AREA - OUTSIDE THIS PROJECT)**:

  + **Developmental Area**: While I have successfully advocated for my team’s contributions to **parallel teams within our org and XF partners**, a key developmental area that I’m currently working on is the **ability to identify opportunities to champion my team’s work beyond our org to other business units within the company**. Specifically, I’d like to find opportunities to cross-pollinate our work in GenAI to other parts of the company such as Amazon Prime Video, Amazon Music, etc. where it can **drive significant business value**. By **proactively promoting our work for broader adoption**, I hope to increase our impact beyond our immediate org and across the company.
  + **How I Recognized the Growth Opportunity**: I recognized this growth opportunity through my **mentor**, who is a director in a parallel org. Observing her in meetings, I saw how she consistently **championed her team’s contributions** in cross-org meetings. I remember she spoke about one of the libraries her team had developed to automate large-scale distributed training of models, which was adopted company-wide and resulted in improved efficiency for training some of our large models.

  + **Steps to Improve**: Being **self-aware** of this gap, I have taken a couple of steps to make improvements.
    I began by identifying **key stakeholders** across different orgs, attending **technical deep dives** to familiarize myself with their **roadmaps at a high level**, and even **cold-messaging peers** to find collaboration opportunities. I’ve also worked on my **pitching skills** to better communicate our work’s **impact** and sought **feedback from my mentor** to learn how to more effectively connect my team’s work with cross-org priorities.
  + **Recent Progress Made**: Recently, my team led an initiative to build **infrastructure for data pre-processing, fine-tuning, and offline evaluation of LLMs**. I proactively **championed this initiative** in cross-org forums, including **technical deep dives and working groups**, highlighting how it streamlines the model development lifecycle. I also facilitated **knowledge-sharing workshops** to demonstrate its benefits, leading to **adoption by several teams** and positioning our team as a key contributor of foundational AI capabilities.

  + **Reflection with Impact on Team and Career**: With a growth mindset, I like to reflect on gaps and figure out ways to optimize for **win-win scenarios**. In this case, by advocating for broader cross-org adoption of our work, not only did the team gain more **recognition** and **influence**, but on a personal level, this offered me an opportunity to **develop into a more strategic leader**, with the ability to influence at a broader organizational level.

* **Story 1 (GROWTH AREA IN THIS PROJECT)**:

  + **Developmental Area:** In a highly XF project such as this one, **charting out the XF dependency graph** as early as possible is essential to **socializing the idea and securing early buy-in from all relevant teams**. This helps prevent **potential delays and misalignment** and maximizes project success and impact.
  + **How I Recognized the Growth Opportunity:**: During an extensively XF project, I observed delays and misalignments that stemmed from uncoordinated dependencies across teams. Each team, focused on its own projects and priorities, inadvertently became a potential blocker when dependencies were not clearly identified and communicated early on. This experience highlighted the need for a strategic approach to managing dependencies to minimize project risks.
  + **Steps to Improve:**: To address these challenges, I adopted a proactive approach to mapping out the XF dependency graph right at the project’s initial stages. This approach involved the following steps:
    1. **Identifying Key Dependencies:** I charted all XF dependencies, including both **direct and second-hop (indirect) dependencies**, to understand how various teams’ work intertwined with our goals.
    2. **Socializing and Securing Buy-In Early:** I scheduled kickoff meetings to present the XF dependency graph to all involved teams, facilitating alignment on priorities and timelines from the start. This ensured that each team understood how their contributions fit into the broader project and recognized potential second and third-hop dependencies.
    3. **Creating Clear Communication Channels:** To foster accountability, I established regular syncs and updates with teams impacted by dependencies, ensuring everyone was aware of upcoming tasks, potential shifts, and ways to mitigate delays.
  + **Recent Progress Made:**: Since implementing these steps, I’ve successfully led multiple complex XF projects with fewer delays and **more cohesive collaboration**. For instance, in a recent project, early identification and communication of XF dependencies allowed us to anticipate and resolve potential bottlenecks proactively, significantly improving our timeline adherence. Regular updates with dependent teams helped us stay on course and pivot when priorities shifted without impacting the overall project schedule.
  + **Reflection with Impact on Team and Career:**: This approach to managing XF dependencies has transformed my effectiveness in XF projects, enabling me to navigate complexities with confidence and resilience. By prioritizing dependency identification and team alignment, I’ve built stronger relationships with stakeholders across the organization, enhancing our collective accountability and trust. This proactive, structured approach has not only streamlined project delivery but also demonstrated my capability to lead complex initiatives, positively impacting my career trajectory as I continue to build a reputation for reliability and collaborative leadership within the organization.

## Additional Questions

### How do you work with other disciplines?

* I ensure regular interaction with product managers, designers, data scientists, and engineers to maintain alignment. This often involves setting up regular syncs, working sessions, and using tools like Wiki/Confluence for shared documentation, which promotes transparency and keeps everyone on the same page.
* I bring in stakeholders from other disciplines early in the process. Whether it’s product managers for understanding business goals, data scientists for insights, or designers for user experience input, I ensure each team’s perspective is considered when defining the roadmap or technical requirements.
* I prioritize clear and concise communication across teams. I adapt my communication style depending on the audience, whether I’m discussing technical details with engineers or focusing on business outcomes with PMs or leadership. This helps avoid misunderstandings and ensures everyone understands their role in achieving project goals.
* I work to ensure that all teams are aligned with the overarching business objectives and key metrics. This is essential to keep the project on track, as each discipline can approach the project from different angles, but with the same goal in mind.
* I emphasize accountability by ensuring each discipline understands its deliverables and how they contribute to the broader project success. Regular check-ins, sprint reviews, milestone tracking, OKRs for broader strategic alignment help keep everyone aligned and ensure that dependencies between teams are managed effectively.

### Tell me about your greatest success or a project that you didn’t think could work but it did. What did you learn?

* This current project, Rufus, seemed like a far-fetched dream: to have all our retail offerings available at our customers fingertips.
* Taking out the browsing time by showing them the exact product they came on the site to buy with their single query.
* They can also use vague queries, “A gift for a 7 month old girl” and through our system, we can capture top \(k\) exact best fitting products.

#### Tell me about a project that you were really passionate about and believed in with all your heart but failed. What did you learn?

* A project I deeply believed in was an **internal LLM** designed to act as a **subject matter expert** for AWS engineers. AWS has an extensive and complex range of internal documentation and resources, and it can be overwhelming for engineers to find the exact solution they need.
* The idea was to build an LLM solution that would be **trained on prior solutions and deployments** that had already been successfully implemented within AWS. This would allow engineers to quickly reference **past successful deployments**, configurations, and troubleshooting strategies to resolve their current issues more efficiently.
* I believed this tool could significantly improve productivity by acting as an **intelligent assistant**, helping engineers narrow down potential solutions without sifting through countless documents and manuals. The LLM would serve as a quick-access resource for resolving infrastructure-related issues.
* Unfortunately, the project faced significant hurdles from **legal teams**. While we had anonymized data for training, they were concerned that the **data still contained sensitive customer information**. Despite the anonymization, legal did not believe the risk of **potential re-identification** or **unintentional exposure** was worth taking, given the volume and sensitivity of the data. This concern ultimately led to the project being **halted**, as the compliance risks outweighed the potential benefits.

### How do you track progress on all projects? / Planning (OKRs) + Tracking (Sprint) Process

* Using Agile project management for project tracking, specifically within a Scrum or Kanban framework, while using elements of OKR (Objectives and Key Results) for strategic alignment/planning.

  + Tasks (or sub-tasks) are often broken down within user stories (put simply, user stories are often broken down into tasks or sub-tasks), and they should have clear acceptance criteria to ensure successful completion.
  + Track user stories in sprint planning/sprint review meetings. Sprint planning is where user stories are discussed, estimated, and assigned to a sprint.
  + Track multiple sprints aligned with a milestone in milestone review/project or release planning meetings. Milestones are typically higher-level checkpoints that span multiple sprints. Milestone tracking often happens at a broader level (e.g., a project or release level).
  + Track milestones in OKRs. OKRs are high-level goals with measurable results/outcomes to ensure broader progress and strategic alignment, typically tracked quarterly or annually. Milestones could feed into OKRs, but milestones are usually more operational or project-based. OKRs are broader and can encompass multiple milestones or even projects.

#### XF Collaboration

* We engaged SMEs from each relevant discipline, as identified through our dependency roadmap, to ensure comprehensive input and alignment across the board.

## Recruiter - Retro

* You’ll be sharing more about a project you’ve led walking us through the start to finish and key project highlights. Specifically, be prepared to discuss: The Business understanding, product/project planning. How did you negotiate with stakeholders and peers? Who was involved in the project? How did you go about driving success? How did you keep track of progress? Your understanding of design tradeoffs, business vs operations vs development considerations. How do you scale systems and business processes?
  + **Situational-Based Example:**
  + A product you led that changed halfway through
    - Year end retail, added music
  + Delivered with little to no direction from leadership
    - Integration of GenAI in music (Maestro)
  + **Project Details:**
  + Explain the transition from the initial goal to success metrics.
  + Discuss the roadblocks, challenges, and tradeoffs.
  + Describe why you chose option A vs. option B.
  + Could you have done something differently?
  + **Team and Task Management:**
  + How did you remain on task?
  + How did you keep the team on task?
  + How did you drive deliverables and execution?
  + **Project Impact:**
  + Why is it a meaningful project?
  + Highlight the tech impact and product impact.
  + How did it shape you as a leader?
  + **Reflection:**
  + Avoid discussing any project that failed.
  + Reflect on the project and what you learned.
