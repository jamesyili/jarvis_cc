# Airbnb

**Source:** https://aman.ai/h/airbnb/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Data Science - Quality](#data-science---quality)
* [Data Quality crucial two links](#data-quality-crucial-two-links)
* [Youtube talk](#youtube-talk)
* [Causal Inference at Abnb](#causal-inference-at-abnb)
* [Minerva - Abnb Metrics tool](#minerva---abnb-metrics-tool)
  + [**What is Minerva?**](#what-is-minerva)
  + [**Key Technical Features of Minerva:**](#key-technical-features-of-minerva)
  + [**Why it Matters for Data Science Quality**:](#why-it-matters-for-data-science-quality)
* [Understanding Airbnb’s Data Quality Rebuild: Key Insights](#understanding-airbnbs-data-quality-rebuild-key-insights)
  + [**1. Data Challenges During Growth**](#1-data-challenges-during-growth)
  + [**2. Airbnb’s Data Quality Initiative**](#2-airbnbs-data-quality-initiative)
  + [**3. Organizational Changes**](#3-organizational-changes)
  + [**4. Architectural Improvements**](#4-architectural-improvements)
  + [**5. Technology Stack & Best Practices**](#5-technology-stack--best-practices)
  + [**6. Governance and Accountability**](#6-governance-and-accountability)
  + [**How This Relates to a Data Science Role**](#how-this-relates-to-a-data-science-role)
* [End Data Science - Quality](#end-data-science---quality)
* [answer](#answer)
  + [Situation:](#situation)
  + [Task:](#task)
  + [Action:](#action)
  + [Result:](#result)
* [Values](#values)
* [Coding](#coding)
* [Team specs](#team-specs)
  + [Intent Discovery (Phase 1)](#intent-discovery-phase-1)
  + [Intent Classification (Phase 2)](#intent-classification-phase-2)
  + [Production Implementation](#production-implementation)
  + [Benefits in Production](#benefits-in-production)
  + [Ongoing Improvements](#ongoing-improvements)
  + [Figure 3: Single-choice Q&A Model Setup](#figure-3-single-choice-qa-model-setup)
  + [Figure 4: Multi-choice Q&A Setup](#figure-4-multi-choice-qa-setup)
  + [Single-choice Q&A Model Setup (Figure 3):](#single-choice-qa-model-setup-figure-3)
  + [Multi-choice Q&A Model Setup (Figure 4):](#multi-choice-qa-model-setup-figure-4)
  + [Single-choice Q&A Setup:](#single-choice-qa-setup)
  + [Multi-choice Q&A Setup:](#multi-choice-qa-setup)
  + [Handling Multi-turn Conversations:](#handling-multi-turn-conversations)
* [Overview interview 2](#overview-interview-2)
* [General coding 1 45mins](#general-coding-1-45mins)
* [Practical Machine Learning 2 - 45 mins](#practical-machine-learning-2---45-mins)
* [ML Experience 1 60 mins](#ml-experience-1-60-mins)
  + [ML Experience 1: Multi-turn Conversation in a Speech-based Music App](#ml-experience-1-multi-turn-conversation-in-a-speech-based-music-app)
    - [Data](#data)
    - [Features](#features)
    - [Model](#model)
    - [Eval/Train](#evaltrain)
    - [Business Impact](#business-impact)
    - [Learnings](#learnings)
    - [Feed Forward Loop](#feed-forward-loop)
  + [Additional Project Details](#additional-project-details)
  + [ML Experience 2: Intent recognition Alexa + Music](#ml-experience-2-intent-recognition-alexa--music)
* [Overview interview 1- Jon](#overview-interview-1--jon)
* [Software Engineering](#software-engineering)
  + [Technical Topics Explained](#technical-topics-explained)
    - [Python, Java, and C/C++](#python-java-and-cc)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Software Engineering Principles](#software-engineering-principles)
    - [Machine Learning Research and Engineering](#machine-learning-research-and-engineering)
    - [Domains of Machine Learning](#domains-of-machine-learning)
  + [Design Principles](#design-principles)
  + [Architectural Patterns](#architectural-patterns)
  + [1. **Start with the User in Mind**](#1-start-with-the-user-in-mind)
  + [2. **Use RESTful Principles (When Appropriate)**](#2-use-restful-principles-when-appropriate)
  + [3. **Consistency is Key**](#3-consistency-is-key)
  + [4. **Versioning**](#4-versioning)
  + [5. **Security**](#5-security)
  + [6. **Documentation**](#6-documentation)
  + [7. **Pagination, Filtering, and Sorting**](#7-pagination-filtering-and-sorting)
  + [8. **Rate Limiting**](#8-rate-limiting)
  + [9. **Use Meaningful HTTP Status Codes**](#9-use-meaningful-http-status-codes)
  + [10. **Feedback Loop**](#10-feedback-loop)
* [Neural Networks](#neural-networks)

## Data Science - Quality

## Data Quality crucial two links

-[link one](https://medium.com/airbnb-engineering/data-quality-score-the-next-chapter-of-data-quality-at-airbnb-851dccda19c3)
-[link two-Midas](https://medium.com/airbnb-engineering/data-quality-at-airbnb-870d03080469)

## Youtube talk

* [link here](https://www.youtube.com/watch?v=Lv-bFDSzrqw)

## Causal Inference at Abnb

* [link here, search causal](https://medium.com/airbnb-engineering/airbnb-at-kdd-2023-9084ad244d8c)
* The article from Airbnb’s Tech Blog describes how the company is utilizing causal inference techniques in various aspects of its business, particularly in marketing and user journey optimization. Here are the key takeaways on how Airbnb is leveraging causal methods:

1. **Marketing Attribution**: In marketing, Airbnb seeks to determine how much value each marketing channel contributes to incremental conversions. This is reframed as a causal inference problem, aiming to isolate the effect of each marketing channel, which is challenging due to multicollinearity (correlated channels). Airbnb’s solution is to hierarchically cluster marketing areas to reduce cross-channel correlation by up to 43%. This helps maintain the interpretability of causal models while isolating the individual effect of each channel.
2. **Customer Journey Optimization**: Airbnb applies causal inference to optimize user journeys, especially in search queries where there is a low number of results. By using causal inference, they can measure the incremental effect of additional search results on a user’s likelihood to book. This helps Airbnb improve supply management and the overall user experience by understanding how additional results impact customer decisions.
3. **TV Campaign Effectiveness**: For national TV advertising, Airbnb uses causal methods, such as propensity score matching, to estimate the effect of campaigns on user behavior. They combine TV exposure data with user demographic data to model how effective TV campaigns are in increasing bookings. This helps Airbnb understand which demographic groups respond best to TV campaigns and how long these effects last.

* In summary, Airbnb is employing causal inference to improve marketing efficiency, optimize user experiences, and better understand the impact of their advertising campaigns. These approaches help them make more informed, data-driven decisions that align closely with business outcomes.

## Minerva - Abnb Metrics tool

* [link here](https://medium.com/airbnb-engineering/how-airbnb-achieved-metric-consistency-at-scale-f23cc53dea70)

### **What is Minerva?**

* Minerva is Airbnb’s metric platform designed to ensure consistent and reliable data for analytics, reporting, and experimentation across the company. It acts as a “single source of truth,” centralizing all key business metrics and dimensions, ensuring consistency, and helping Airbnb manage the entire lifecycle of a metric—from creation to consumption.

### **Key Technical Features of Minerva:**

1. **Data Standardization**:
   * Minerva centralizes metrics and dimensions in a **GitHub repository**, ensuring everyone at the company uses the same definitions for metrics, which prevents discrepancies in reports and analytics.
2. **Validated Development Flow**:
   * It enforces best practices through **code reviews, static validation, and test runs** before metrics are finalized, reducing errors and improving data quality.
3. **DAG Orchestration**:
   * Minerva handles **data denormalization efficiently**, reusing intermediate results to avoid redundancy, which optimizes data processes and saves computing resources.
4. **Self-healing Computation**:
   * The platform has **self-healing capabilities** for job failures and ensures **built-in checks** for data quality, ensuring reliable metrics delivery.
5. **Unified API for Data Access**:
   * Minerva’s API makes metrics accessible across multiple tools such as **Apache Superset** (for visualization), Airbnb’s A/B testing platform, and **Python/R clients** for deeper data analysis.
6. **Flexible Backfilling**:
   * When business logic changes, Minerva can automatically track and backfill data, ensuring **historical data is updated** and consistent with current business definitions.

### **Why it Matters for Data Science Quality**:

* As part of Airbnb’s Data Science Quality efforts, understanding how Minerva ensures consistency, reliability, and accuracy in data is critical. The platform addresses common challenges like data duplication, differing metrics definitions, and debugging discrepancies, all of which are crucial to maintaining high standards of data quality.
* Highlight these points when speaking with the recruiter to show your understanding of how Airbnb’s data infrastructure supports its analytics and experimentation efforts through robust quality controls, which are likely key to the role you’re pursuing.

## Understanding Airbnb’s Data Quality Rebuild: Key Insights

* [link here](https://medium.com/airbnb-engineering/data-quality-at-airbnb-e582465f3ef7)

The article “Data Quality at Airbnb, Part 1—Rebuilding at Scale” describes Airbnb’s large-scale initiative to improve its data quality, particularly as the company scaled rapidly. Here’s a breakdown of the key technical details to help you make a strong impression when speaking to a recruiter for a data science role at Airbnb.

### **1. Data Challenges During Growth**

As Airbnb grew, it faced typical challenges with its data warehouse, including:

* **Ownership issues**: Data ownership was not clearly defined across teams, creating bottlenecks when issues arose.
* **Data architecture limitations**: Many pipelines were built organically without a clear overarching architecture, resulting in bloated data models.
* **Lack of governance**: There was no centralized governance to enforce quality standards across teams.

### **2. Airbnb’s Data Quality Initiative**

In 2019, Airbnb launched a comprehensive initiative to overhaul its data warehouse. The initiative focused on the following goals:

* **Clear ownership**: Ensuring that all important datasets had clearly defined owners.
* **Service-level agreements (SLAs)**: Ensuring important data consistently met timeliness and quality expectations.
* **High-quality pipelines**: Enforcing best practices for pipeline development.
* **Data validation**: Ensuring important data was routinely validated and trustworthy.
* **Data discoverability**: Making data well-documented and easily accessible for teams across the organization.

### **3. Organizational Changes**

To support the initiative, Airbnb made several structural changes:

* **Creation of a Data Engineering role**: The company formalized the Data Engineering role to ensure it had specialized personnel for tasks like data modeling and pipeline development.
* **Decentralized team structure**: Data engineering pods were aligned with product teams to ensure engineers were closer to the data’s consumers, but a centralized team was also created to handle global datasets and establish engineering standards.

### **4. Architectural Improvements**

Airbnb’s data architecture was revamped with the following principles:

* **Normalized data models**: Tables were designed to be as normalized as possible with fewer dependencies.
* **Subject area-based models**: Datasets were grouped into logical subject areas, with clear ownership and accountability for each.

### **5. Technology Stack & Best Practices**

* **Transition to Spark & Scala**: Airbnb moved away from SQL and Hive, adopting Spark with the Scala API to leverage benefits like type safety, code reuse, and modularity.
* **Enhanced testing**: Integration tests became mandatory to ensure code stability and quality in pipeline development.
* **Data quality checks**: New tools for anomaly detection and quality checks were introduced, particularly to prevent issues in new pipelines.

### **6. Governance and Accountability**

* **Midas Certification**: A new certification process was introduced to ensure data pipelines adhered to agreed-upon standards. Data flagged as certified is prioritized in discoverability tools.
* **Bug reporting and resolution**: A formal process for reporting and reviewing data quality bugs was established, including regular meetings to ensure accountability and resolution.

### **How This Relates to a Data Science Role**

For a data science role, understanding these core aspects of Airbnb’s approach to data quality will be critical. The emphasis on ownership, standardized processes, high-quality pipelines, and governance highlights how the company ensures data accuracy, timeliness, and reliability—key to any data-driven decision-making process. You can showcase your understanding of how these elements impact the broader goals of data science and product development.

This technical understanding will help you demonstrate to the recruiter that you’re familiar with Airbnb’s current data landscape, and that you are ready to contribute to enhancing data quality and reliability in a fast-paced, scalable environment.

## End Data Science - Quality

## answer

### Situation:

As a Team Lead at Amazon Music, I was tasked with leading a high-risk, cross-functional project to integrate item-to-item recommendations between Amazon Prime Video and Amazon Music. This integration aimed to enhance user experience by providing seamless content discovery across both platforms. However, the project presented significant challenges, including data discrepancies, potential disruption to user experience, and system compatibility issues.

### Task:

My primary responsibility was to ensure the successful integration of the recommendation systems while maintaining a high standard of user experience and system performance. This involved coordinating between multiple teams, developing robust models, and managing the rollout process carefully.

### Action:

To handle this high-stakes project, I took the following steps, aligning with key Airbnb values:

**1. \*\*Connection and Belonging:**

* I prioritized building a sense of connection and belonging within the team. I fostered open communication and collaboration between Amazon Prime Video and Amazon Music teams, ensuring everyone felt valued and heard. This helped create a cohesive team environment, crucial for tackling the complex integration challenges.

**2. \*\*Creatively-led Approach:**

* Embracing Airbnb’s creatively-led spirit, we developed a hybrid recommendation model that could merge video and music consumption data. This required innovative feature engineering to ensure the model could process the nuances of both media types effectively. We leveraged curiosity and imagination to explore unconventional solutions, ensuring our model was both accurate and efficient.

**3. \*\*Responsibility to Stakeholders:**

* I maintained a strong focus on our responsibility to stakeholders, including users and internal teams. We conducted extensive offline evaluations and simulations using historical data, ensuring the model’s reliability before deployment. This careful testing phase was critical in minimizing risks and maintaining trust with our user base.

**4. \*\*Phased Rollout:**

* In line with Airbnb’s principle of prioritizing long-term impact, we adopted a phased rollout strategy. We initially introduced the integrated recommendations to a small user group, closely monitoring performance and gathering feedback. This approach allowed us to make data-driven adjustments, ensuring a smooth and successful rollout to a broader audience.

**5. \*\*Continuous Monitoring and Feedback Loop:**

* Post-deployment, we implemented a robust monitoring system to track key performance metrics and established a feedback loop with customer support teams. This allowed us to address any issues promptly and continuously improve the system based on user feedback.

### Result:

The outcome was highly successful. The integrated recommender system enhanced user engagement on both platforms, leading to a 20% increase in cross-platform content discovery and a 15% increase in user retention. The phased rollout and continuous monitoring ensured a smooth transition with minimal disruption to users.

The project not only improved the user experience but also demonstrated the value of cross-functional collaboration in achieving complex integration goals. This experience reinforced the importance of thorough risk assessment, collaborative planning, and iterative development in managing high-stakes projects. It also highlighted the power of leveraging diverse datasets to create innovative solutions that enhance user satisfaction across multiple domains.

By embracing Airbnb’s values of connection and belonging, being creatively-led, and maintaining a strong responsibility to stakeholders, we successfully navigated the risks and delivered a project that significantly improved user experience and engagement.

## Values

* Youre interviewing for Staff Machine Learning engineer role in Airbnb. In the values interview, you’re asked the following question. Use your creativity to give a great answer that would get you a great job offer.
* The basic routine of these two rounds of interviews relies on core values, regardless of the specific questions asked.
* The interviewer is not an engineer and follows a list of questions, asking them one by one.
* These questions are essentially the same as those given by HR before.
* Examples of questions asked include:
  + What is the most challenging thing you have ever done?
  + Have you ever spoken up to your colleagues/friends?
  + Is there anyone or anything that has changed your outlook?
  + What can reflect your attitude?
  + Hospitality: what would you do if you were hypothetically capable of something?
* Prepare (edit) a few stories in advance.
* Apply the questions to the stories and align the stories with the core values.
* Avoid bringing up sensitive topics like politics or religion.
* It seems that as long as there are no red flags, it’s fine.
* You must give a good reason why you chose Airbnb.
  + It is best to combine this reason with your own experience, especially travel experiences.
* In the last round, my mind really stopped spinning.
  + The Chinese interviewer I met was a very good person.
  + I felt like he didn’t fully agree with what I was talking about.
  + It seemed like he was just trying to do what I wanted.
  + 11)amongallthefeaturesofairbnbwhatdoyouwanttoimprove?
* The core value page asks some incomprehensible things such as “Where do you want to travel?”
* Of course, one thing to note is that many of the advantages of Airbnb are that it is cheap!
* It’s about being able to better understand local culture.
* Whether you agree with it or not, you have to say this.
* + What brings you to Airbnb?
* What can you teach your co-workers after you get in?
* Describe a person whom you admire most.
* Describe your experience with Airbnb.
* Where have you been to?
* What will you do if you win a lottery such as Powerball?
* What is the biggest fear in your life?
* How would you describe Airbnb to people back in 2003?
* If you have a book that writes about your whole life, will you read it? Why?
* If you have a time machine and you can either go back or go forth, will you choose to go back or to go forth?
* Among all the features of Airbnb, what do you want to improve?
* + Describe a time when you thought something was very risky, how you handled it, and what the outcome was.
* how to demonstrate your resourcefulness. When preparing, align your answers with their “Cereal Entrepreneur” principle. A few days later, I was notified that I had passed and now the offer negotiations are starting.

  ## Coding

```
Introduction
Because there is a ton of code in our app, developers are experiencing very long build times. The way this build system works is, when you make any code change in a module, all modules that depend on that module (either directly or transitively) must be rebuilt. The goal of this challenge is to calculate a metric that represents the cost of making a change to a module in development. We refer to this metric as the cost of the module and it equals the number of modules that need to be rebuilt as the result of a code change.

For Example
The application has the following modules:

A: App (the application entry-point)
S: Stays
H: Homes
E: Experiences
N: Networking
And the dependency graph looks like this:

      A______
  ____|____  |
  ↓       ↓  |
  S       E  |  
↙  ↘    ↙   |
H     N  ←---
Dependencies:

The Application (A) module depends on Stays (S), Experiences (E), and Networking (N)
The Stays (S) module depends on Homes (H) and Networking (N)
The Experiences (E) module depends on Networking (N)
Cost of each module:

The cost of N is 4

Because making a code change to N requires rebuilding N, S, E, and A
The cost of H is 3

Because making a code change to H requires rebuilding H, S, and A
The cost of S is 2

Because making a code change to S requires rebuilding S and A
The cost of E is 2

Because making a code change to E requires rebuilding E and A
The cost of A is 1

Because making a code change to A required rebuilding just A
Input
The first line is a number indicating how many lines follow. On each following line of input, the first item represents a module in our dependency graph, then a comma, followed by all of it's children also separated by commas. There is no circles in the dependency graph. For the example, the input looks like this:

5
A,E,N,S
S,H,N
E,N
H
N
The first line says that E, N, and S, are children of A. The second line says that H and N are children of S. The third line says the N is the only child of E. The fourth line says that H has no children.

Output
Given the input as described above, your costOfNodes function should output a line for each module with the module name following by it's cost. The Lines should be sorted by module name. For the example, the output should be:

A,1
E,2
H,3
N,4
S,2
IMPORTANT! Your solution should return an array (or list, vector, etc depending on language) of strings. Ie., the first element of the array for the example above should be the string "A,1".

Hint
Reverse the directions of the arrows, then calculate cost.
```

```
def costOfNodes(input_data):
    import collections
    
    def parse_input(input_data):
        graph = collections.defaultdict(set)
        all_nodes = set()
        
        for line in input_data[1:]:
            parts = line.split(',')
            node = parts[0]
            children = parts[1:]
            all_nodes.add(node)
            all_nodes.update(children)
            for child in children:
                graph[child].add(node)
        
        return graph, all_nodes

    def calculate_costs(graph, all_nodes):
        def dfs(node, visited):
            count = 1  # Include this node itself
            for dependent in graph[node]:
                if dependent not in visited:
                    visited.add(dependent)
                    count += dfs(dependent, visited)
            return count

        costs = {}
        for node in all_nodes:
            visited = set()
            visited.add(node)
            costs[node] = dfs(node, visited)
        
        return costs

    # Parsing the input data
    graph, all_nodes = parse_input(input_data)

    # Calculating costs for each node
    costs = calculate_costs(graph, all_nodes)

    # Sorting the output and formatting it
    result = [f"{node},{costs
```

## Team specs

* In the Airbnb case study, multi-turn interactions and intent detection for their messaging platform were addressed using a combination of machine learning techniques, focusing primarily on two phases of development: intent discovery using unsupervised learning and intent classification using supervised learning. Here’s how each phase contributed and how it’s operationalized in production:

### Intent Discovery (Phase 1)

* **Methodology**: Used Latent Dirichlet Allocation (LDA), an unsupervised learning technique, to analyze the large corpus of guest-host messages. This method helped in identifying potential topics or intents without predefined labels by examining the statistical relationships between words in the messages.
* **Challenges**: Given that a single message could contain multiple intents, the typical challenge was to isolate the primary intent from auxiliary information. The LDA model helped in probabilistically determining the dominant topics within each message.

### Intent Classification (Phase 2)

* **Transition to Supervised Learning**: Using the topics identified in Phase 1 as labels, a supervised learning approach was adopted to refine the accuracy of intent detection. A Convolutional Neural Network (CNN) was specifically chosen for this purpose due to its effectiveness in handling text data, its speed, and its ability to pick out key phrases that signify intent.
* **Model Training and Accuracy**: The model training was performed using Airbnb’s internally developed tools and infrastructure. Text preprocessing was an important step, where normalizing data like dates, times, and URLs helped reduce noise and improve the relevance of the training data.

### Production Implementation

* **Infrastructure**: The models are hosted and served using Bighead, Airbnb’s machine learning infrastructure, and Deep Thought, the online inference component. This setup allows for real-time intent classification as guests interact with hosts through the platform.
* **Real-time Processing**: When a guest sends a message, the system immediately classifies its intent using the trained CNN model. This classification helps in determining the type of response or action required, potentially triggering automated responses or flagging the message for urgent human intervention if needed.

### Benefits in Production

* **Reduced Response Times**: By automatically classifying message intents, hosts can provide quicker responses to specific guest inquiries, improving the overall communication experience.
* **Efficient Message Handling**: The intent detection system helps in prioritizing messages based on their urgency and relevance, thus managing the hosts’ workload more effectively.

### Ongoing Improvements

* The Airbnb team continues to refine these models by exploring more advanced NLP techniques and by incorporating feedback from production use to improve both the accuracy and efficiency of the system. They also plan to extend these capabilities to accommodate multiple languages and include host intents, enhancing the platform’s usability and inclusiveness globally.
* [chat medium](https://medium.com/airbnb-engineering/task-oriented-conversational-ai-in-airbnb-customer-support-5ebf49169eaa)
* [second one](https://medium.com/airbnb-engineering/discovering-and-classifying-in-app-message-intent-at-airbnb-6a55f5400a0c)

The images you’ve shared depict two model setups for question and answer (Q&A) systems, with Figure 3 showing a Single-choice Q&A model setup and Figure 4 showing a Multi-choice Q&A setup. Here’s a breakdown of each:

### Figure 3: Single-choice Q&A Model Setup

* This model setup deals with scenarios where each question has only one correct answer.
* **Passage (P)**: The context or passage that the question is based on.
* **Question (Q)**: A question that relates to the passage provided.
* **Answers (A)**: Potential answers to the question. Each answer is evaluated to determine whether it’s correct, with only one possible correct answer.
* **Auto-encoder Transformer**: The model likely uses an auto-encoder transformer architecture for processing the passage and question, and to predict the correct answer.
* **Binary Cross-Entropy (BCE) Loss**: Each answer is treated as a binary classification problem, where the model predicts if each answer is correct (1) or not (0), and BCE Loss is used to train the model, penalizing it for incorrect classifications.

### Figure 4: Multi-choice Q&A Setup

* This model setup is for scenarios where there can be multiple correct answers for a given question.
* **Passage (P)**, **Question (Q)**, and **Answers (A)**: The same as in the single-choice setup.
* **Auto-encoder Transformer**: Similar architecture as above, but likely adapted for multi-choice scenarios.
* **Softmax CE Loss**: The Softmax function is used to predict a probability distribution over the answer choices, and Cross-Entropy Loss is used to compare the predicted probability distribution with the actual distribution (where the correct answers are marked with a 1). The model is trained to minimize this loss, effectively learning to increase the probability of correct answers.

In both the single-choice and multi-choice Q&A setups depicted in the figures, the auto-encoder transformer serves as the central processing unit, and the inputs and outputs are tailored for the respective tasks:

### Single-choice Q&A Model Setup (Figure 3):

**Input:**

* The input to the auto-encoder transformer typically consists of a combination of the passage (P) and the question (Q). This combined input is encoded by the transformer to understand the context provided by the passage and the specifics of the question being asked.

**Output:**

* The output is a binary classification for each potential answer (A), indicating whether it is correct or incorrect. This is represented by a vector of 0s and 1s, where 1 indicates the model predicts the answer is correct, and 0 indicates an incorrect answer.

### Multi-choice Q&A Model Setup (Figure 4):

**Input:**

* Similar to the single-choice setup, the input here also consists of the passage (P) and the question (Q). However, given that multiple answers can be correct, the model may be processing each answer choice in relation to the passage and question to determine the probability of each being correct.

**Output:**

* The output in this case is a probability distribution across all potential answers (A). Each answer is assigned a probability score reflecting how likely the model thinks it is to be correct. The Softmax function is applied to ensure that these probabilities sum up to 1.

The difference between the single-choice and multi-choice Q&A setups lies primarily in how the potential answers are treated and evaluated:

### Single-choice Q&A Setup:

* **Only one correct answer**: This setup assumes there’s only one correct response for each question.
* **Binary Classification**: Each answer is independently classified as either correct or incorrect, with a binary cross-entropy loss applied to each potential answer.

### Multi-choice Q&A Setup:

* **Multiple correct answers possible**: More than one answer can be correct for a given question.
* **Probabilistic Classification**: Instead of simply classifying answers as correct or incorrect, the model assigns a probability to each answer, indicating its likelihood of being correct. The softmax cross-entropy loss function is used to handle the probability distribution across all answer choices.

### Handling Multi-turn Conversations:

Multi-turn conversations pose additional complexities not directly addressed by these architectures. In a multi-turn setup, the model must maintain context over several rounds of interaction, remembering past exchanges and using that information to inform future responses. Here’s how the architecture might handle it:

1. **Context Management**: The model needs to encode not just a single passage and question but an entire conversation history. This could include several alternating passages (P) and questions (Q), along with their respective answers (A).
2. **Stateful Memory**: Multi-turn conversations require a stateful component that can remember the conversation’s context across turns. This could involve recurrent structures or attention mechanisms that allow the model to refer back to earlier parts of the conversation.
3. **Dynamic Output Adjustment**: Depending on the progression of the conversation, the model might dynamically change its output. For example, it might refine its predictions based on new information obtained in subsequent turns or re-evaluate earlier answers in light of recent interactions.
4. **Continual Learning**: As the conversation unfolds, the model might update its internal representations to better reflect the nuances of the ongoing interaction. This could involve adjustments to embeddings or weights in a way that mimics continual learning.

In practice, handling multi-turn conversations typically requires additional architecture components such as memory networks or transformer models with extended context windows that can keep track of the conversation state over time. Each new turn would be an input to the model, concatenated with the relevant conversation history, and the model would generate responses that are contextually relevant to all previous turns.

## Overview interview 2

* 1 General Coding Interview (45 minutes)
* 2 Practical Machine Learning Interviews (45 minutes)
* 1 Machine Learning Experience Interview (60 minutes)

## General coding 1 45mins

* **Coding #1:** 787 (Return Itinerary) - Use HackRanker for implementation.
* **Coding #2:** 269 Follow-up: Return all possible solutions (just describe the idea).
* “The elevator has n buttons and m people. As long as the button is pressed, it will stay on and will not go out if pressed multiple times. It is required to calculate the expected number of lit keys.”
* “LC39 Combination Sum variant. It should be noted that the number is of float type (the price of the dishes on the menu kept to two decimal places), so when judging whether it is 0, you need to use < 0.01 to judge.
* LC336 Palindrome Pairs. LC251 But one more API needs to be implemented: remove(). Reference post: <https://www1point3acres.com/bbs/read&tid=524974> csv Parser. I am too poor and I have seen this topic mentioned many times but I still don’t know what the topic looks like because I don’t have enough rice. Reference post: <https://www1point3acres.com/bbs/read&tid=511265> How to implement a queue using an array of length five (the number of arrays is not limited). In fact, I don’t fully understand the needs. Please refer to this post: <https://www1point3acres.com/bbs/read>”

## Practical Machine Learning 2 - 45 mins

* “Airbnb search ranking with personalization for maximum advertise booking.”
* **Service Chatbot**
* **System Design:** Design an autocomplete search for Airbnb using Zoom whiteboard.
* **Practical ML:** Discuss the first ML round Airbnb search ranking with personalization for maximum booking. It seems like a classic question. Complaint about lack of personalization in their search; it often doesn’t seem personalized.
* **Interview Experience:** The first interviewer asked about linear regression and various optimizers. Only memorized the differences between various optimizers before the exam and then never looked at them again. During the second round, worked with the interviewer to solve an ML problem, mentioning whether image features could be added to the existing model. Mentioned that adding image embedding did not improve the effect much based on previous experience with a similar multi-modality model (structured feature + free text + image).
* **Design Considerations:** Could be a mix of rapid back and forth and design. Design will likely derive from their blog. Topics may include search, recommendation systems, image processing, or perhaps a multi-turn conversation system since it’s team-relevant. Adding a multimodal component, such as an image of a broken sink with text for a multi-turn conversation, was seen as a hindrance in previous discussions.
* We’ll discuss an ML problem that is motivated by a particular product need in Airbnb’s marketplace.
* Be sure to explore our ML Blog and familiarize yourself with our marketplace and how we apply machine learning to it.
* You’ll be expected to propose options, analyze their strengths and weaknesses, and refine the solution during the interview.
* We’ll be covering choices like what data you would use, how you might use particular signals through feature engineering, what modeling techniques you might use, and how you would evaluate the model’s performance.
* We’ll be assessing the suitability of your approach to the task at hand, the depth of your knowledge of that approach, and how well you understand how all the pieces of a solution fit together.
* Interview tip #1: The questions will cover general ML concepts.
* Interview tip #2: Focus on business metrics/impact, problem formulation, risk evaluation, ML knowledge in breadth and depth, end to end experience in delivering ML products on production.
* The key competencies you will be measured on:
  + Communication: Ask clarifying questions, confirm assumptions, effectively reason through your approach and be receptive to hints or suggestions from your interviewer.
  + Problem Application: How well can you apply your existing ML experience and knowledge to a new, open-ended problem? e.g., can you think outside of the traditional ML box? How to get labels and understand their quality?
  + Logical Reasoning: Can reason through the problem, understand how to break it down, make the right assumptions, define the appropriate invariants, etc. Can grasp concepts quickly.
  + Depth of Knowledge: How well do you know the terms you’re throwing around? (e.g., Why is AUC good for unbalanced datasets? Why is L1 vs L2 norm? Why is ML good for feature selection?)solution
  + Trade-Offs: Ability and openness to explore different paths. Flexibility to talk about different things. Able to list the trade-offs for each path, pros/cons. Apply approaches that make sense for the particular problem as opposed to piecing together techniques without any proper validation as to why you’re choosing them.
* Resources to help you prepare:
  ● [Airbnb ML Blog](https://medium.com/airbnb-engineering/ai/home)

## ML Experience 1 60 mins

* You’ll have one interview focused on a project deep dive where you will have the opportunity to showcase a specific project you are working on now, or have worked on in the past. This project should represent a challenging and interesting problem that showcases your technical ability. Make sure to include the business need or problem, key technical decisions you made, architecture trade-offs you considered, the outcome/what you learned, and the impact of your work. This is also a good interview to show your passion for Airbnb - come prepared with questions for your interviewer to answer about what it’s like to work as an ML engineer at Airbnb.
* The key competencies you will be measured on:
* Trade-Offs: Are you open to exploring different paths and alternatives, talk about different things, do you list trade-offs, and make a pros-cons list, etc for complex problems and decisions?
* Technical Curiosity: Are you curious? Do you look beyond the surface-level and have a deep understanding of the system you’re working with? Do you understand decisions that were made not just for your part, but for your partners on this project?
* Impact: Do you understand how your work contributed to the business - what are the metrics and the factors you used to determine success for this project?
* Communication: Can you explain things well to an engineer who is not necessarily in the same domain by being explicit and avoiding buzzwords/being high-level? Do you share assumptions?
* Passion: Are you passionate about your project and your team?
* What is your project about?
* What milestones do you have?
* What role do you play in the project?
* Have you encountered any difficulties in each milestone, and how did you solve them?
* Are there any conflicts when cooperating and communicating with friends in other groups, and how to solve them?
* Finally, what are your life insights after completing this project?”
* Key decision
* Concieved ML problem formulated
* labels, eval, what learned
* business impact
* successful, what does success look like
* KPIs
* what to build at Airbnb
* Deep dive, specifics

Sure! Given that the project is a speech-to-text-to-speech music application using a large language model (LLM) for handling conversations, let’s redefine the structure to fit this more specific use case.

### ML Experience 1: Multi-turn Conversation in a Speech-based Music App

Sure, I can provide an ASCII art diagram of the system architecture for a speech-to-text-to-speech music app using AWS services:

```
                                      +-----------------+
                                      |   Amazon Lex    |
                                      | (Speech to Text)|
                                      +--------+--------+
                                               |
                                               v
                                    +----------+----------+
                                    |    AWS Lambda       |
                                    | (Processing & Logic)|
                                    +----------+----------+
                                               |
+----------------+                             |                                +-----------------+
| Amazon S3      | <--------------------------+------------------------------> |  Amazon Polly   |
| (Data Storage) |                            |                                | (Text to Speech)|
+----------------+                            |                                +---------+-------+
                                               |                                          |
                                               |                                          |
                                      +--------+--------+                        +---------+---------+
                                      |  Amazon RDS     |                        |  User's Device    |
                                      | (User Database) |                        |  (Output Speech)  |
                                      +--------+--------+                        +-------------------+
                                               ^
                                               |
                                     +---------+---------+
                                     | AWS Comprehend    |
                                     | (Text Analysis)   |
                                     +---------+---------+
                                               |
                                               |
                                     +---------+---------+
                                     | Amazon SageMaker  |
                                     | (Train LLM Model) |
                                     +-------------------+
```

This diagram illustrates how different AWS services are integrated to create a speech-to-text-to-speech music app. Here’s a brief overview of the flow:

* **Amazon Lex** handles the speech recognition part, converting user’s spoken input into text.
* **AWS Lambda** processes this text, executing business logic and interacting with other services.
* **AWS Comprehend** can be used to perform sentiment analysis or advanced text analysis on the conversation.
* **Amazon RDS** manages user data and preferences, which can influence the Lambda processing.
* **Amazon S3** serves as storage for all interaction logs and possibly user data and preferences if not fully contained within RDS.
* **Amazon SageMaker** is involved in training and fine-tuning the language model (LLM) that Lambda will use to generate appropriate responses based on user inputs and context.
* **Amazon Polly** converts the text output from Lambda into speech, which is then sent back to the user’s device.

This setup allows for a robust, scalable system capable of handling complex multi-turn conversations in a music app context.

**Project Overview:**
An interactive music application integrating speech recognition and synthesis with a powerful language model to facilitate multi-turn conversations. The app assists users by recommending music, answering queries, and demonstrating various app functionalities through voice interactions.

#### Data

* **Source**: User voice commands, interaction logs, music streaming data, and user feedback.
* **Type**: Audio data for speech recognition, text data for LLM training, and user behavioral data.
* **Usage**: Train the speech recognition system to accurately convert speech to text and use interaction data to train the LLM for generating appropriate text responses.

#### Features

* **Acoustic Features for Speech Recognition**: These include Mel-frequency cepstral coefficients (MFCCs), spectral roll-off, pitch, and zero-crossing rate. These features help the model capture the characteristics of human speech which facilitates accurate speech-to-text conversion.
* **Textual Features for LLM**:
  + **N-grams**: Sequences of words used to predict the next item in text. This helps in maintaining conversational context.
  + **Part-of-Speech Tags**: Used by the model to understand grammatical structure, which improves the quality of generated responses.
  + **Sentiment Scores**: Understanding the emotional tone of the user’s input can help tailor responses, making the interaction more engaging and personalized.
* **Contextual Features**:
  + **Session Duration**: The length of the current interaction session, which can help the model adapt its responses based on user engagement.
  + **Interaction History**: Historical data of past interactions, which the model can use to personalize responses and music recommendations.
* **User Profile Features**:
  + **Preferences and Listening History**: Information like favorite genres, artists, and previously enjoyed tracks, allowing for more tailored music recommendations.
  + **Demographics**: Age, location, and other demographics can influence music recommendations and conversational style.
* **Behavioral Features**:
  + **Click-through Rates**: How often a user follows through on a recommendation, providing feedback on the relevance of the model’s suggestions.
  + **Engagement Metrics**: Measures of how users interact with the app’s features, like time spent on the app, frequency of use, and active versus passive listening times.
* **Prosodic Features for Speech Synthesis**:
  + **Intonation, Stress, and Rhythm**: Key aspects that make synthesized speech sound natural and engaging.
  + **Speech Rate and Volume**: Adjustments in these areas can help mimic natural speech patterns, enhancing the clarity and effectiveness of communication.

These features are integral to training the respective components of the speech-based music app, from speech recognition through to the conversational model and speech synthesis. Each set of features helps the corresponding model understand and process user interactions more effectively, thereby enhancing the overall performance and user experience of the app.

#### Model

* **Speech Recognition Model**: Deep learning models trained on a wide variety of speech data.
* **LLM for Conversations**: Transformer-based models that are fine-tuned for conversational AI, capable of understanding and maintaining context over multiple turns.
* **Speech Synthesis Model**: Text-to-speech (TTS) models that produce clear, natural-sounding voice outputs.

#### Eval/Train

* **Training**: Separate training phases for speech recognition, LLM, and speech synthesis, using relevant datasets and feedback loops.
* **Evaluation**: Performance metrics for speech recognition (e.g., word error rate), LLM effectiveness (e.g., accuracy, relevance), and speech synthesis quality (e.g., naturalness, intelligibility).

#### Business Impact

* **User Engagement**: Providing a hands-free, conversational interface increases accessibility and user engagement.
* **Brand Innovation**: Enhances the brand’s image as a technology leader in music streaming services.
* **Customer Satisfaction**: Improved user experience through accurate, responsive, and natural interactions.

#### Learnings

* Effectiveness of integrating speech technologies with a conversational AI in a music context.
* User preferences and behavior when interacting via voice commands.

#### Feed Forward Loop

* **Data Collection**: Continuous collection of new user interactions for further training and refinement.
* **Model Updates**: Regular updates to models based on new data, user feedback, and emerging best practices in AI and speech processing.

### Additional Project Details

* **Milestones**:
  + Development of individual components (speech recognition, LLM, speech synthesis).
  + Integration of components into the music app.
  + Beta testing with real users and iteration based on feedback.
  + Launch and post-launch enhancements.
* **Role**:
  + Your specific contribution to the project, whether technical, managerial, or creative.
* **Difficulties and Solutions**:
  + Example: Dealing with noisy input data for speech recognition and refining models to improve accuracy.
* **Inter-group Cooperation**:
  + Collaboration dynamics between AI teams, software development teams, and user experience designers.
* **Life Insights**:
  + Personal and professional growth insights gained from working on a cutting-edge AI-driven project.
* **Key Decisions**:
  + Such as opting for a specific LLM or speech synthesis technology based on testing and research outcomes.
* **Success and KPIs**:
  + Defining success through specific key performance indicators like user retention rates, number of daily interactions, and satisfaction ratings.
* **Deep Dive into Specifics**:
  + Detailed exploration of challenges and solutions in speech recognition or LLM fine-tuning for the music context.

This redesign focuses on integrating speech technologies with a language model to enhance user interaction within a music app, aiming for a seamless and engaging user experience.

### ML Experience 2: Intent recognition Alexa + Music

---

## Overview interview 1- Jon

* The interview will contain three sections:
  + Algorithms and programming: The candidate will be asked to describe a solution or write code for specific problems. When an English description is rigorous enough, code will not be necessary; but when it is not specified rigorously, code may be needed. We will use codeshare.io to share code. Code is not expected to compile or run, just to demonstrate the solution. Any language among Python, C/C++, C#, or Java is acceptable.
  + Software engineering: We will discuss software engineering issues, system design and organization, and related principles, often using examples.
  + Neural networks: We will discuss the state-of-the-art in the field as well as principles and guidelines for the design and development of complex neural systems.
* It is also helpful if the candidate can list their level of expertise in the following: Pytorch, Python, Hive, pyhive/pyspark, Anyscale Ray, C/C++, Java, Jax, CUDA, and pytorch lightning. Can you please email me this list so I can share it with John in advance?

## Software Engineering

* ### Technical Topics Explained

#### Python, Java, and C/C++

* **Python**: An interpreted, high-level, general-purpose programming language known for its simplicity and readability, making it particularly popular for web development, data analysis, artificial intelligence, and scientific computing.
* **Java**: A class-based, object-oriented programming language designed to have as few implementation dependencies as possible. It’s widely used for building enterprise-scale applications, Android apps, and web applications.
* **C/C++**: C is a procedural programming language supporting structured programming, while C++ is an extension supporting object-oriented programming. Both are known for their speed and efficiency and are commonly used in system/software development, game programming, and applications requiring high-performance computation.

#### Frameworks and Libraries

* **PyTorch, TensorFlow, and Keras**:
  + **PyTorch** and **TensorFlow** are open-source machine learning libraries for research and production, offering robust tools for deep learning. PyTorch is known for its dynamic computation graph and user-friendly interface, while TensorFlow offers comprehensive services for a broad set of ML applications.
  + **Keras** is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It focuses on enabling fast experimentation.
* **Jax**: An open-source library for high-performance numerical computing in Python, offering automatic differentiation for high-speed machine learning research.
* **Cuda/Cudnn**: CUDA is a parallel computing platform and API model created by Nvidia allowing software developers to use a CUDA-enabled graphics processing unit (GPU) for general purpose processing, while CuDNN is NVIDIA’s library of primitives for deep learning networks.
* **Kubernetes**: An open-source system for automating deployment, scaling, and management of containerized applications, helping in managing application processes efficiently across a cluster of machines.
* **Spark**: Apache Spark is a unified analytics engine for large-scale data processing, offering libraries for SQL, streaming, machine learning, and graph processing.
* **Airflow**: Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows, allowing for scheduling and orchestration of complex data pipelines.
* **Kafka**: Apache Kafka is a distributed event store and stream-processing platform, designed for high-throughput, fault-tolerant handling of real-time data feeds.
* **Data Warehouse (e.g., Hive)**: Hive is a data warehousing solution over Hadoop, providing data summarization, query, and analysis. Data warehouses are centralized systems for storing, reporting, and analyzing data from various sources.

#### Software Engineering Principles

* **Quality Software Engineering and APIs**: Emphasizes creating reliable, maintainable, and testable code, developing APIs (Application Programming Interfaces) that allow different software applications to communicate with each other efficiently.

#### Machine Learning Research and Engineering

* Involves understanding and implementing the lifecycle of ML models including training, serving predictions, conducting A/B tests, and managing datasets. It also covers the importance of feature engineering, selection, and the validation processes to ensure models are robust and perform well on unseen data.

#### Domains of Machine Learning

* **Natural Language Processing (NLP)**: Focuses on the interaction between computers and humans through natural language, aiming to read, decipher, understand, and make sense of human languages in a valuable way.
* **Computer Vision**: Deals with how computers can gain high-level understanding from digital images or videos with the goal of automating tasks that the human visual system can do.
* **Personalization and Recommendation**: Involves tailoring services or products to individual users’ preferences using algorithms and machine learning techniques to predict what a particular user may prefer among a set of items or content.
* **Sequence Prediction**: Involves predicting subsequent elements of a sequence, important in various applications like time-series prediction, speech recognition, and language modeling.
* **Anomaly Detection**: The identification of items, events, or observations which do not conform to an expected pattern or other items in a dataset, crucial for fraud detection, network security, and fault detection.

### Design Principles

1. **DRY (Don’t Repeat Yourself)**: This principle advocates for reducing repetition of software patterns. It encourages the abstraction of functionality to prevent code duplication, leading to easier maintenance and updates.
2. **YAGNI (You Aren’t Gonna Need It)**: Emphasizes avoiding adding functionality until it is necessary. This principle helps in preventing over-engineering and focusing on what’s truly required at the moment.
3. **KISS (Keep It Simple, Stupid)**: A principle that promotes simplicity in design over complexity. Simple designs are easier to maintain, understand, and extend, reducing the overall cost of development.
4. **Loose Coupling**: This principle involves designing systems where each component has, or makes use of, little or no knowledge of the definitions of other separate components. Loose coupling increases the modularity of the system, making it easier to refactor, change, and understand.
5. **High Cohesion**: Encourages designing components that are self-contained, with a single, well-defined purpose. High cohesion increases the robustness, reliability, and reusability of components.

* Modularity: Breaking down the software into smaller, independent, and reusable components or modules. This makes the software easier to understand, test, and maintain.
* Abstraction: Hiding the implementation details of a module or component and exposing only the necessary information. This makes the software more flexible and easier to change.
* Encapsulation: Wrapping the data and functions of a module or component into a single unit, and providing controlled access to that unit. This helps to protect the data and functions from unauthorized access and modification.
* DRY principle (Don’t Repeat Yourself): Avoiding duplication of code and data in the software. This makes the software more maintainable and less error-prone.
* KISS principle (Keep It Simple, Stupid): Keeping the software design and implementation as simple as possible. This makes the software more understandable, testable, and maintainable.
* YAGNI (You Ain’t Gonna Need It): Avoiding adding unnecessary features or functionality to the software. This helps to keep the software focused on the essential requirements and makes it more maintainable.
* SOLID principles: A set of principles that guide the design of software to make it more maintainable, reusable, and extensible. This includes the Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.
* Test-driven development: Writing automated tests before writing the code, and ensuring that the code passes all tests before it is considered complete. This helps to ensure that the software meets the requirements and specifications.

### Architectural Patterns

1. **Event-Driven Architecture (EDA)**: An architecture that orchestrates behavior around the production, detection, and consumption of events. This pattern is excellent for systems that are highly responsive and adaptable to changes in real-time.
2. **CQRS (Command Query Responsibility Segregation)**: Separates read and write operations for a data store into distinct interfaces. This pattern can help in scaling applications by allowing reads and writes to be optimized independently.
3. **Domain-Driven Design (DDD)**: Focuses on the core domain logic of the application and its complexities. DDD advocates modeling software based on the real-world business domain, which can improve communication between technical and non-technical team members and lead to more effective software solutions.
4. **Serverless Architecture**: Allows developers to build and run applications and services without managing infrastructure. The cloud provider automatically provisions, scales, and manages the infrastructure required to run the code. This architecture is beneficial for reducing operational costs and complexity.
5. **Microfrontend Architecture**: An architectural style where independently deliverable frontend applications compose into a greater whole. It extends the microservices pattern to front-end development, allowing for multiple teams to work independently on different features of the front-end, using different frameworks or technologies.

* API (Application Programming Interface) design is a crucial aspect of software development, impacting how easily systems can interact with each other. Good API design facilitates easy integration, ensures stability and security, and provides a clear and intuitive way for developers to work with the service. Here are some key principles and best practices for effective API design:

### 1. **Start with the User in Mind**

* Design your API from the consumer’s perspective. It should be intuitive, with clear naming conventions and a logical structure that reflects how developers think about the domain.

### 2. **Use RESTful Principles (When Appropriate)**

* REST (Representational State Transfer) is a popular architectural style for designing networked applications. It uses HTTP requests to access and manipulate web resources using a stateless protocol and standard operations, making it a flexible and widely adopted standard for APIs.
* Employ HTTP methods explicitly (GET for fetching data, POST for creating data, PUT/PATCH for updates, DELETE for removal).

### 3. **Consistency is Key**

* Ensure consistency in naming conventions, request and response structures, and error handling across the entire API to reduce learning curve and potential confusion.

### 4. **Versioning**

* APIs evolve over time, and versioning helps manage changes without breaking existing integrations. Use a clear and straightforward versioning strategy (e.g., via the URL path, custom request header, or query parameters).

### 5. **Security**

* Implement authentication and authorization protocols like OAuth to protect access to resources. Consider security at every step of the API design to protect sensitive data and ensure privacy.

### 6. **Documentation**

* Comprehensive and clear documentation is crucial for a successful API. It should include detailed descriptions of endpoints, parameters, expected request and response structures, and examples. Tools like Swagger or OpenAPI can automate part of the documentation process and ensure it stays up-to-date.

### 7. **Pagination, Filtering, and Sorting**

* For APIs returning lists of resources, provide options for pagination, filtering, and sorting to allow consumers to easily query the data they need.

### 8. **Rate Limiting**

* Implement rate limiting to prevent abuse and ensure that the API can serve all consumers fairly without being overwhelmed by requests.

### 9. **Use Meaningful HTTP Status Codes**

* Utilize HTTP status codes to communicate the outcome of API requests clearly. For example, use 200 for successful requests, 400 for bad requests, 401 for unauthorized requests, and 500 for internal server errors.

### 10. **Feedback Loop**

* Maintain a feedback loop with your API consumers. Their experiences can provide valuable insights into how your API can be improved.

## Neural Networks

* Upon the user’s query. Searching for San Francisco doesn’t mean you want to stay anywhere in San Francisco, let alone the Bay Area more broadly.
* Therefore, a great listing in Berkeley shouldn’t come up as the first result for someone looking to stay in San Francisco. Conversely, if a user is specifically looking to stay in the East Bay, their search result page shouldn’t be overwhelmed by San Francisco listings, even if they are some of the highest quality ones in the Bay Area.
* Build a location relevance signal into our search model that would endeavor to return the best listings possible, confined to the location a searcher wants to stay. One heuristic that seems reasonable on the surface is that listings closer to the center of the search area are more relevant to the query. Given that intuition, we introduced an exponential demotion function based upon the distance between the center of the search and the listing location, which we applied on top of the listing’s quality score.
* This got us past the issue of random locations, but the signal overemphasized centrality, returning listings predominantly in the city center as opposed to other neighborhoods where people might prefer to stay.
* To deal with this, we tried shifting from an exponential to a sigmoid demotion curve. This had the benefit of an inflection point, which we could use to tune the demotion function in a more flexible manner. In an A/B test, we found this to generate a positive lift, but it still wasn’t ideal — every city required individual tweaking to accommodate its size and layout. And the city center still benefited from distance-demotion. There are, of course, simple solutions to a problem like this. For example, we could expand the radius for search results and diminish the algorithm’s distance weight relative to weights for other factors. But most locations aren’t symmetrical or axis-aligned, so by widening our radius a search for New York could — gasp — return listings in New Jersey. It quickly became clear that predetermining and hardcoding the perfect logic is too tricky when thinking about every city in the world all at once.
* So we decided to let our community solve the problem for us. Using a rich dataset comprised of guest and host interactions, we built a model that estimated a conditional probability of booking in a location, given where the person searched. A search for San Francisco would thus skew towards neighborhoods where people who also search for San Francisco typically wind up booking, for example the Mission District or Lower Haight.
* However, it didn’t take long to realize the biases we had introduced. We were pulling every search to where we had the most bookings, creating a gravitational force toward big cities. A search for a smaller location, such as the nearby surf town Pacifica, would return some listings in Pacifica and then many more in San Francisco. But the urban experience San Francisco offers doesn’t match the surf trip most Pacifica searchers are planning. To fix this, we tried normalizing by the number of listings in the search area. In the case of Pacifica, we now returned other small beach towns over SF. Victory!
* However by tightening up our search results for Santa Cruz to be great listings in Santa Cruz, the mushroom dome vanished. Thus, we decided to layer in another conditional probability encoding the relationship between the city people booked in and the cities they searched to get there
