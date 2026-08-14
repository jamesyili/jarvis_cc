# Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents

**Source:** https://arxiv.org/pdf/2602.10226
**Ingested:** 2026-08-14
**Tags:** agent-evolution, recsys, llm-agents, ml-systems, automation

---

Self-Evolving Recommendation System: End-To-End Autonomous
Model Optimization With LLM Agents
Haochen Wang∗
Google Inc
Mountain View, California, USA
haochenww@google.com
Yi Wu∗
Google Inc
Mountain View, California, USA
wuyish@google.com
Daryl Chang∗
Google Inc
Mountain View, California, USA
dlchang@google.com
Li Wei
Google Inc
Mountain View, California, USA
liwei@google.com
Lukasz Heldt
Google Inc
Mountain View, California, USA
heldt@google.com
Abstract
Optimizing large-scale machine learning systems, such as recom-
mendation models for global video platforms, requires navigating
a massive hyperparameter search space and, more critically, de-
signing sophisticated optimizers, architectures, and reward func-
tions to capture nuanced user behaviors. Achieving substantial
improvements in these areas is a non-trivial task, traditionally re-
lying on extensive manual iterations to test new hypotheses. We
propose a self-evolving system that leverages Large Language Mod-
els (LLMs), specifically those from Google’s Gemini family, to au-
tonomously generate, train, and deploy high-performing, complex
model changes within an end-to-end automated workflow. The
self-evolving system consists of an Offline Agent (Fast Loop) that
performs high-throughput hypothesis generation to optimize for
proxy metrics, and an Online Agent (Slow Loop) that validates
candidates against delayed north star business metrics in live pro-
duction. Our agents act as specialized Machine Learning Engineers
(MLEs): they exhibit deep reasoning capabilities, discovering novel
improvements in optimization algorithms and model architecture,
and formulating innovative reward functions that target long-term
user engagement. The effectiveness of this approach is demon-
strated through several successful production launches at YouTube,
confirming that autonomous, LLM-driven evolution can surpass
traditional engineering workflows in both development velocity
and model performance.
CCS Concepts
• Information systems →Recommender systems; Language
models.
Keywords
Large Language Model, Autonomous Agent, Recommendation Sys-
tem
∗Equal contribution to the work.
This work is licensed under a Creative Commons Attribution 4.0 International License.
RecSys ’26, Minneapolis, MN, USA
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2284-4/2026/09
https://doi.org/10.1145/3773078.3831919
ACM Reference Format:
Haochen Wang, Yi Wu, Daryl Chang, Li Wei, and Lukasz Heldt. 2026. Self-
Evolving Recommendation System: End-To-End Autonomous Model Op-
timization With LLM Agents. In 20th ACM Conference on Recommender
Systems (RecSys ’26), September 27-October 02, 2026, Minneapolis, MN, USA.
ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/3773078.3831919
1
Introduction
Global video platforms like YouTube serve billions of users by curat-
ing personalized feeds from vast corpora of content. At the core of
delivering relevant experiences is the recommendation system, an
ensemble of algorithms and models designed to help users discover
content they love. Increasingly, modern recommendation systems
are being formulated as Reinforcement Learning (RL) problems
[4, 28], where the system acts as an agent interacting with a user
environment to maximize cumulative utility over time. As surveyed
in [1], this paradigm shifts the focus from simple Click-Through
Rate (CTR) prediction to optimizing long-term user satisfaction,
requiring models to balance immediate gratification with delayed
rewards like retention and diverse content exploration.
However, a critical bottleneck in this paradigm is the alignment
gap between training proxies and long-term user satisfaction. While
models are trained on differentiable loss functions, the actual goal
is user satisfaction, which is non-differentiable, delayed, sparse, and
often semantically complex. Recent approaches like the Learned
Ranking Function [25] attempt to bridge this gap by parameterizing
the reward function itself, allowing the system to learn the optimal
trade-off between conflicting objectives. Similarly, work on diversi-
fying by intent [22] highlights that modern reward functions must
now encode nuanced psychological concepts – such as user intent
and exploration – rather than simple binary labels.
Optimizing these increasingly semantic and structural compo-
nents exceeds the capabilities of traditional Automated Machine
Learning (AutoML) [29]. Standard AutoML methods [6, 20] excel
at tuning numerical hyperparameters within fixed search spaces.
Yet, they lack the reasoning capabilities to invent new reward logic
or architect novel interaction layers from scratch. They cannot
interpret past experiment results, hypothesize that a specific user
slice is under-served, and write the logic to fix it.
This limitation has catalyzed a shift in the broader machine learn-
ing community from "automated tuning" to "autonomous scientific
discovery." Recent works such as [12, 15] introduce the concept
arXiv:2602.10226v3  [cs.LG]  2 Aug 2026

RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
Haochen Wang, Yi Wu, Daryl Chang, Li Wei, and Lukasz Heldt
of AI agents capable of orchestrating the full scientific lifecycle:
generating hypotheses, writing code, and refining theories based
on empirical results. Unlike rigid AutoML pipelines, these agents
utilize Large Language Models (LLMs) to reason over unstructured
context. This capability offers a potential solution to the limitation
of traditional methods, promising a transition from mere parameter
tuning and selection, to automated discovery of complex, novel
model changes.
Despite these parallel advancements, a significant gap remains
at their intersection. Optimizing industrial-scale recommendation
models proves exceptionally difficult and remains a manual, human-
intensive endeavor. To bridge the gap, we introduce a Self-Evolving
Recommendation System deployed at YouTube. By integrating
recent advancements in LLMs with a production recommendation
system, we demonstrate the effectiveness of building a rigorous
framework where agents act as expert Machine Learning Engineers
(MLEs) to solve global-scale open-ended recommendation model-
ing problems. These agents do not just tune parameters; they read
production code, propose structural changes to neural topologies,
and formulate complex logic for reward functions within an end-to-
end autonomous pipeline. While our primary deployment utilizes
Gemini 2.5 Pro [8], our ablation studies (Section 5.4.1) also evaluate
a lightweight Gemini variant to quantify the relationship between
model reasoning power and discovery performance.
Our contributions are summarized as follows:
• Autonomous MLE Framework for Industrial-Scale Sys-
tems We introduce a hierarchical agentic system where
specialized LLM agents act as expert MLEs to evolve recom-
mendation models. We detail the system design that enables
agents to safely manage the full lifecycle of industrial model
development – from hypothesis generation and code imple-
mentation to A/B testing.
• Semantic Discovery We demonstrate that LLM-based agents
can move beyond simple parameter tuning to discover novel
architectural components and multi-objective reward func-
tions that align better with long-term user satisfaction, areas
previously accessible only to human experts in the recom-
mendation domain.
• Acceleration of Experimental Velocity We confirm the
success of an autonomous LLM-based evolutionary recom-
mendation system in accelerating the velocity of experimen-
tation and delivery of notable metric gains. With extensive
offline and online experiments and production deployments,
we validate that agentic systems can surpass hand-tuned
baselines and effectively evolve the state-of-the-art in rec-
ommendation systems at YouTube.
2
Related Work
Our work sits at the intersection of automated machine learning,
autonomous agents, and RL for recommendation. We distinguish
our contributions by contrasting them with existing paradigms in
these areas.
2.1
Automated Model Optimization
Industry standard practices for automated model optimization in
recommendation rely heavily on Hyperparameter Optimization
(HPO) [2]. Frameworks like Google Vizier [9] and Auto-Sklearn
[7] utilize iterative search methods (e.g., Bayesian optimization
[20], Gaussian processes [16]) to tune continuous hyperparame-
ters. However, these methods are confined to defined parameter
ranges and lack the semantic depth to interpret why a configuration
succeeds or fails.
Similarly, techniques like optimizer search [5] and Neural Ar-
chitecture Search (NAS) [6] (e.g., DARTS [11], evolutionary search
[17]) apply these principles to make structural improvements. Yet,
they remain fundamentally restricted by the constraints of their
search spaces, as they can only select or remix from a predefined
menu of operations. Consequently, they lack the creative capacity
to invent novel modules, refactor code to fix bottlenecks, or intro-
duce complex logic that was not explicitly programmed into the
search space.
2.2
LLMs and Autonomous Agents for Scientific
Discovery
The emergence of LLMs has enabled a shift from selection to gen-
eration. Optimization by PROmpting (OPRO) [26] demonstrates
that LLMs can serve as evolutionary operators, iteratively refining
solutions based on natural language descriptions. This capability is
amplified by models such as Gemini 2.5 [8] with advanced reason-
ing capabilities, building on the foundations of Chain-of-Thought
[24] and long-context understanding and thinking.
Beyond optimization, the field of AI agents has exploded with
frameworks like ReAct (Reasoning + Acting) [27] and Toolformer
[18], which demonstrate that LLMs can solve complex tasks by
interleaving reasoning traces with external tool execution. Build-
ing on this, recent "scientist" agents have attempted to automate
open-ended workflows. Voyager [21] and MetaGPT [10] introduce
agents that write executable code to solve open-ended problems,
maintaining a persistent repository of reusable functions to accel-
erate future tasks. AlphaEvolve [15], The AI Scientist [12], and
MLE-STAR [14] extend this to algorithmic discovery, where agents
perform direct edits on source code to improve performance on
academic benchmarks. Our work adapts this "scientist" paradigm to
the industrial recommendation system setting. Unlike prior works
that optimize for static datasets and academic benchmarks (e.g.,
ImageNet, Kaggle), our framework addresses the unique challenges
of a live production ecosystem: noisy feedback loops, strict safety
guardrails, complex user-system interactions, and the need for rig-
orous A/B testing protocols.
2.3
Reward Engineering for Reinforcement
Learning
In RL, designing the reward function is often the hardest part of
the problem. Eureka [13] pioneers the use of LLMs for evolutionary
reward design in robotics, while LEARN-Opt [3] optimizes rewards
without predefined metrics by using LLMs as analysts to evaluate
candidates. However, critical distinctions remain: the availability
of a clear oracle for success, and the latency of the feedback loop.
While prior approaches are evaluated on robotics or simulations
that offer immediate feedback, recommendation systems lack a clear
oracle for user satisfaction. The true objective is a latent variable
observable only through the delayed, noisy, and sparse real-world

Self-Evolving Recommendation System
RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
interactions on the order of Θ(𝑑𝑎𝑦𝑠) or Θ(𝑤𝑒𝑒𝑘𝑠). Consequently,
when designing a reward, we cannot simply optimize for a simu-
lation score; we must instead reason about alignment with offline
proxy signals analyzed over petabytes of interaction logs, and ulti-
mately validate our designs through real-world deployment.
3
Problem Formulation
We begin by introducing the components of an RL-based recommen-
dation model, specifically for the task of ranking videos to maximize
the total expected long-term user satisfaction. We formulate this
task as a bi-level optimization problem.
Our ultimate goal is to maximize a non-differentiable, long-term
user satisfaction metric, which is observable only through online in-
teraction. However, directly optimizing online metrics is intractable
because feedback is sparse, delayed, and noisy. Therefore, the prob-
lem is bi-level: in the lower level, a ranking model is trained to
optimize an engineered proxy objective (the cumulative reward). In
the upper level, we find the optimal system configuration (e.g., opti-
mizer, architecture, reward) such that the ranking model’s induced
policy maximizes the online metrics upon deployment.
3.1
The Lower Level: Model Training
We consider a standard recommendation setting where a ranking
model, parameterized by weights 𝜃, ranks a list of candidate items
to generate an action 𝑎(the ranking order) given state 𝑠, which com-
prises the user state and candidate videos, to maximize a cumulative
reward.
While the methodology proposed in this paper is model-agnostic,
our deployment environment utilizes a value-based RL approach
[25, 28]. Specifically, the model optimizes a state-action value func-
tion 𝑄𝜃(𝑠,𝑎) that estimates the long-term value of a ranking action,
defined by a proxy reward constructed from session-level user-item
interactions. The model is trained via Stochastic Gradient Descent
(SGD) to minimize a differentiable proxy loss function Lproxy:
𝜃∗(Φ) = arg min
𝜃
Lproxy(D;𝜃, Φ)
where D represents the training data logs and Φ represents the
meta-configuration of the system, such as the model optimizer,
architecture, and reward definition. This lower-level optimization
is performed by the model trainer.
3.2
The Upper Level: Optimizing North Star
Metrics
While the ranking model optimizes the proxy reward, industrial
recommendation systems ultimately care about the true north star
metrics M. The mapping between the proxy reward and the true
online metrics is not guaranteed; a model might improve offline
loss on a poorly defined reward function to the detriment of user
satisfaction.
Thus, we formulate the problem of finding the optimal configu-
ration Φ as:
Φ∗= arg max
Φ M(𝜃∗(Φ))
s.t.
G(Φ) ≤𝐶
Here, 𝜃∗(Φ) represents the model weights trained under config-
uration Φ, and G represents system-level constraints (e.g., training
cost).
This formulation highlights the challenge: we must optimize Φ
using expensive, noisy feedback from M to ensure the ranking
model, which efficiently optimizes reward, is actually solving the
business problem. Traditionally, optimizing Φ has been undertaken
by human researchers. Our goal is to automate the role of a human
researcher via an MLE agent that iteratively refines the components
of Φ. Concrete examples of Φ include:
• Optimizer (𝜂∈Φ) The learning rate and update rules (e.g.,
AdaGrad) used to train the model weights 𝜃.
• Architecture (𝜙∈Φ) The structure (e.g., DCN) of the rank-
ing network.
• Reward Definition (𝑟∈Φ) The logic determining the train-
ing labels, combining various engagement and user signals
to balance competing objectives.
4
The Self-Evolving System
We propose a system that automates the discovery of an optimal
model configuration Φ∗by decoupling the discovery process into
two distinct, synchronized reasoning loops. The system is designed
around the Experiment Journal – a shared, persistent knowledge
base containing the history of all configurations, their offline scores,
and any available online metrics – which informs two primary
agents (Figure 1):
(1) The Offline Agent (Fast Loop): Operates as a high-frequency
candidate generator, running once every day but waking up
every 5 minutes, tasked with nominating potential model
improvements. Each wakeup performs one or more of: nom-
inating new candidates, scheduling new training jobs or
analysis queries based on the latest day’s user data, and
scoring candidates. Its goal is to identify configurations that
minimize the offline metric (e.g., loss, inverted correlation)
within regions of the configuration space that have histori-
cally yielded promising online metrics (see the agent-specific
prompt in Figure 2). The agent uses available live signals to
steer away from dead-end trajectories that appear promis-
ing in offline proxies but have historically failed to improve
online metrics.
(2) The Online Agent (Slow Loop): Operates as a low-frequency
experiment strategist, running once every day, tasked with
ranking candidates produced by the Fast Loop. Its goal is to
identify candidates that maximize the north star metrics M
(see the agent-specific prompt in Figure 3). This agent uses
the rank to decide which configurations merit promotion to
live experiments and when to terminate unpromising exper-
iments, ensuring that expensive online traffic is reserved for
candidates with the highest demonstrated potential.
Both agents utilize a shared prompt template, with the specifics
of each agent injected into it (Figure 4). The prompt structure inte-
grates the agent’s goals with the Experiment Journal, enabling each
agent to reason over historical successes and failures. Addition-
ally, we use few-shot prompting by including example proposals to
guide the LLM’s output format.

RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
Haochen Wang, Yi Wu, Daryl Chang, Li Wei, and Lukasz Heldt
Figure 1: The Self-Evolving System Architecture. The framework operates as a dual-loop, self-evolving system centered around
a shared Experiment Journal containing a persistent knowledge base, historical trials and their resulting metrics. The Offline
Agent (Fast Loop) serves as the high-frequency nomination engine, where LLMs are invoked to instantiate specialized reasoning
personas that generate and refine hypotheses into executable code. Tool calls are made to assign offline scores to candidates.
The Online Agent (Slow Loop) is the low-frequency ranking engine, selecting high-potential candidates and promoting them to
online experiment. It manages the entire experiment lifecycle including fetching online north star metrics.
# GOAL
Propose changes to the model, with the following goals:
- Balance exploration, exploitation, and innovation: You should
make X, Y, and Z proposals, respectively, in the three categories.
- Minimize the offline metric: {AGENT_OFFLINE_METRIC}, while
maximizing the following online metrics in order of importance:
Metric#1, Metric#2, ..
# OUTPUT FORMAT
Think step-by-step and double-check syntax. Output each pro-
posal with exactly two fields:
- "explanation", briefly describing what change this is and why it
is potentially useful
- "delta", the change against the model’s current configuration
Figure 2: Offline Agent Task. This text is injected into the
shared prompt template in Figure 4 as the {AGENT_TASK}.
4.1
The Offline Agent: A Fast Loop
The Offline Agent serves as the rapid nomination engine of the
framework, responsible for generating high-potential candidates
for experimentation by the Online Agent. It utilizes specialized
reasoning personas to traverse the semantic configuration space
guided by historical metrics. Furthermore, the agent leverages a
suite of tools to assign offline scores to the generated candidates.
4.1.1
Specialized Reasoning Personas and Tool Calls. We decom-
pose the multifaceted task of recommendation system design into
specialized agent personas, each optimized for a distinct model
component. A monolithic persona exposed to the full breadth of the
codebase quickly becomes overwhelmed by irrelevant schema defi-
nitions and knowledge, leading to hallucinations that we observed
starting at ~400k tokens. We thus instantiate specialized personas,
each equipped with specific tools and objectives and focusing on
# GOAL
Propose a rank of the top 𝐾configurations in the history that
are expected to maximize the online performance.
- The offline metric is {AGENT_OFFLINE_METRIC}, with a smaller
value indicating better offline performance.
- The online metrics in order of importance are: Metric#1,
Metric#2, ..
# GUARDRAILS
Maintain system safety by enforcing: Keep Metric#3 ≤+1%, ..
# OUTPUT FORMAT
Output an ordered list of 𝐾configurations, starting with the
most promising configuration. Each item in the list must have
exactly two fields:
- "name", an identifier for the configuration
- "delta", the change from the history
Figure 3: Online Agent Task. This text is injected into the
shared prompt template in Figure 4 as the {AGENT_TASK}.
improving Θ(10) lines of a component’s code within Θ(1000)-line
model definition – typical of the size of a human-engineered change.
A. The Optimizer Persona (Tool: compute_loss) This per-
sona searches the space of optimization algorithms. It iteratively
proposes changes to the optimizer class (e.g., Adagrad, RMSprop)
and its internal hyperparameters (e.g., momentum, batch size).
For such changes, the definition of the loss function Lproxy re-
mains invariant. While the model changes, the yardstick measuring
its performance does not. Consequently, the resulting validation
loss values are comparable. A lower loss implies a better approxi-
mation of the ground truth labels.
• Objective Minimize offline loss Lproxy.

Self-Evolving Recommendation System
RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
# PERSONA
You are a brilliant and innovative machine learning scien-
tist with excellent programming and analytical skills. You
want to improve the model and you have deep expertise in
{AGENT_SPECIALIZATION}.
{AGENT_TASK}
# CONTEXT
The model currently has the following configuration: [BASELINE
CONFIGURATION]
(Optional) The output (hypotheses and data) from past data
analyses are: {SQL_QUERY_OUTPUT}
Below is the history of past offline and (if available) online
results, sorted by the offline score where the best offline
configuration is shown first: [EXPERIMENT JOURNAL]
# EXAMPLE PROPOSAL
{AGENT_EXAMPLE}
Figure 4: Shared LLM Prompt Template. {..} are populated
based on the agent’s task, and [..] are populated from shared
context.
• Tooling The persona utilizes the compute_loss tool. This
enables a direct sorting of candidates: Φ𝐴≻Φ𝐵
⇐⇒
Lproxy(Φ𝐴) < Lproxy(Φ𝐵).
• Process The persona generates multiple configurations (e.g.,
replacing optimizers, changing learning rates) and launches
asynchronous training jobs.
• Scoring The persona computes the loss for each configura-
tion.
B. The Architecture Persona (Tool: compute_loss) This per-
sona specializes in the neural topology of the model, parsing the
architecture definition and proposing structural mutations. Un-
like standard NAS, which selects from a fixed menu of layers, this
persona can write novel code – for example, replacing standard
embedding lookups with a custom "Gated Path" mechanism or intro-
ducing layer normalization in specific sub-towers (discussed in Sec-
tion 5.2.3). Like the Optimizer persona, it relies on the compute_loss
tool to score the configuration, where lower scores indicate a topol-
ogy that is more learnable and expressive than the baseline.
C. The Reward Persona (Tool: run_sql_query, compute_eval)
This persona performs reward engineering by editing the logic that
defines the training label for the ranking model. It utilizes a multi-
step reasoning process to discover and validate new rewards.
First, it performs open-ended and massive-scale data analyses us-
ing the run_sql_query tool, finding hypotheses and relationships
in the user logs. An example finding is the hypothesis that "videos
that are shared yield higher watch time", backed by data comparing
the average watch time of videos that are shared vs not shared.
Second, it generates configurations based on these findings (in-
jected into the prompt via {SQL_QUERY_OUTPUT} in Figure 4), and
computes loss-independent proxy metrics for them. Because modi-
fying the reward fundamentally alters the optimization landscape,
comparing Lproxy across different reward definitions is ill-defined.
A model trained on a "click-only" reward will naturally have a
lower loss than one trained on a complex "click + satisfaction"
reward, simply because the latter task is harder to learn. There-
fore, this persona cannot use compute_loss. Instead, it relies on
the compute_eval tool to calculate a proxy metric that is highly
predictive of desirable user behavior using the evaluation data. An
example is the long-watch correlation, which represents how well
the model’s prediction aligns with the actual occurrence of long
watches, with a higher score indicating that the model is success-
fully prioritizing content that users find engaging enough to watch
above a duration. More examples (e.g., correlation with retention
and repeat consumption) can be found in [23].
• Objective Identify promising signals that are highly predic-
tive of user engagement.
• Tooling The persona utilizes the run_sql_query tool to do
open-ended data analyses, and the compute_eval tool to
validate the quality of the new reward.
• Process The agent executes batches of analytical queries
over user logs, and launches training jobs for the proposed
configurations.
• Scoring The persona scores each configuration by comput-
ing a surrogate proxy.
4.2
The Online Agent: A Slow Loop
The Online Agent prioritizes the accuracy and safety required for
production deployment by selecting the top candidates produced
by the Offline Agent and validating them against delayed north
star metrics M. It manages the experiment lifecycle of the top
candidates through five phases, beginning with a reasoning phase
to determine the trajectory of each candidate:
(1) Selection: The Online Agent begins by evaluating the entire
candidate pool stored in the Experiment Journal. Its task
is to rank the candidates to identify the top 𝐾for online
experimentation. Importantly, while the Experiment Journal
is ordered by offline metrics, the Online Agent must also
consider the online metrics to produce a refined ranking.
The resulting LLM output categorizes the candidates into
three distinct paths:
• Candidates newly in the top 𝐾are routed through phases
(2) and (3) to begin their training and experimentation.
• Candidates that are already in active experiments and
remain in the top 𝐾are routed to phase (4) for continued
metric collection.
• Candidates that have fallen out of the top 𝐾are routed to
phase (5) for resource reclamation.
(2) Model Training: The agent trains new configurations and
monitors convergence to ensure weights are successfully
versioned and exported.
(3) Live Experimentation: The agent assigns production traffic
to the newly trained models to begin online experimentation.
(4) Metric Synthesis: The agent fetches online metrics and
writes them into the Experiment Journal. This data is critical
for the next iteration’s reasoning.
(5) Cleanup: For candidates no longer in the top 𝐾, the agent
reclaims resources by cleaning up their trainers and experi-
ments. This closes the loop for unpromising directions.

RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
Haochen Wang, Yi Wu, Daryl Chang, Li Wei, and Lukasz Heldt
By employing a dual-agent system instead of a monolithic agent,
we establish a rigorous filtration funnel that distinguishes high-
velocity candidate nomination from strategic experimentation. In
this new methodology, human engineers are only required to per-
form the high-level step of presenting the initial research idea to the
Offline Agent and the final step of reviewing experiment metrics
collected by the Online Agent.
5
Deployment and Results
The self-evolving recommendation system has been deployed across
several critical surfaces on YouTube. We present a comprehensive
evaluation comparing our autonomous dual-agent system against
human-engineered baselines.
5.1
Experimental Setup
We evaluate the efficacy of our framework in two stages, aligning
with the dual-agent methodology we established. The first stage
is offline validation via the Fast Loop, showing that LLM agents
are capable of finding candidates that minimize loss or exhibit high
correlation with key signals. The second stage is online A/B exper-
imentation via the Slow Loop, showing that candidates reaching
this stage significantly improve north star metrics. The underlying
production model is an RL model based on a deep neural network
to optimize video ranking on YouTube’s video watch page, with
training typically requiring Θ(ℎ𝑜𝑢𝑟𝑠). Final performance is judged
against a hierarchy of north star business metrics M.
A summary of the impact achieved by our autonomous agents
is presented in Table 1, with detailed discussion provided in Sec-
tion 5.2 and Section 5.3. To contextualize these gains, we analyzed
all launches on our surface from the past 6 months. On average,
the improvements generated by the agentic system outperformed
64% of launches generated using the traditional, manual approach
for the YouTube-level metric and 73% for the surface-level metric.
5.2
Evaluation of the Optimizer and
Architecture Components: Loss
Optimization
The first phase of deployment focused on improving the optimizer
and architecture, which both seek to minimize offline loss Lproxy.
The Offline Agent proposed the below refinements, which yielded
significant improvements when promoted to the live environment.
5.2.1
Algorithmic Discovery: Evolving the Optimizer. Traditionally,
optimizer configurations remained static due to the cost of tun-
ing. The agent autonomously identified that switching from the
legacy Adagrad optimizer to RMSprop (see Optimizer component
in Table 3) – with a specific learning rate, decay rate, momentum,
etc. – resulted in a statistically significant drop in offline loss and
improvement in live traffic. Notably, the benefit of an LLM is we can
simply ask it to find the "best Keras optimizer" without specifying
what’s available, as keywords are not the same for each optimizer.
5.2.2
System Optimization: Training Efficiency. Beyond model qual-
ity, the agent also learned to optimize for system efficiency. By
iteratively adjusting batch sizes, training epochs, and optimizer
hyperparameters, the agent achieved reductions – first by 4× then
by 2× – in training latency without degrading convergence. In total,
training time improved by 8× without sacrificing business metrics.
5.2.3
Structural Discovery: Gated Path Architectures and Activa-
tion Refinement. After exploring hundreds of potential solutions
to optimize the topology, the agent proposed a Gated Path archi-
tecture (see Architecture component in Table 3) similar to Gated
Linear Units (GLU) [19], which introduced a multiplicative gate to
the inputs. This innovation yielded some of the most robust gains
in our deployment. In a follow-up deployment, the agent further
refined this architecture by moving from standard sigmoid gates to
GELU activations combined with layer normalization, showing that
the agent is capable of both exploring innovative structures and
exploiting and fine-tuning structures that it believes to be superior.
5.3
Evaluation of the Reward Component:
Semantic Alignment via Signal Correlation
Unlike the Optimizer and Architecture improvements, which min-
imize the loss, the Reward improvement must interpret a loss-
independent proxy to find a reward that balances conflicting busi-
ness objectives while capturing nuanced user behaviors.
5.3.1
Semantic Discovery: Multi-Objective Reward Synthesis. Lever-
aging iterative analysis of user interaction patterns, the agent syn-
thesized a reward function that incorporates a novel signal in-
dicating whether the user is actively engaging with content on
the site (see Reward component in Table 3). This synthesis signifi-
cantly outperformed the human-engineered baseline – a remarkable
feat given the historical difficulty of manual reward engineering.
There are Θ(100) signals and combinations – watch time, survey
responses, retention metrics, and more – to consider to approximate
long-term user satisfaction. Human researchers often struggle to
pinpoint critical semantic bottlenecks within this massive search
space, frequently resulting in months of iteration in suboptimal
regions of the potential solution space. This discovery underscores
the agent’s unique ability to perform high-level semantic reasoning,
allowing it to redefine the business logic of success in ways that
traditional optimization processes cannot achieve.
5.3.2
Reward Hyperparameter Tuning. Beyond discovering novel
reward structures, the agent demonstrated the ability to tune exist-
ing reward hyperparameters. This tuning was performed without
offline metrics, relying exclusively on the Online Agent’s slow loop
to explore the parameter space. This is significant because previous
manual attempts over several months to tune these hyperparam-
eters failed to find a configuration that simultaneously improved
both YouTube-level and surface-level metrics. The agent, however,
identified a solution tuning four hyperparameters in two weeks.
5.4
LLM Performance and Ablation Studies
To understand the drivers of the system’s performance, we con-
ducted a series of ablation studies focusing on model selection,
persona framing, and context management. These benchmarks
highlight the sensitivity of the discovery process to the underlying
LLM’s reasoning capabilities and the quality of prompt grounding.
We consider the task of improving the offline loss of the optimizer
and its hyperparameters, using the following variants:

Self-Evolving Recommendation System
RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
Table 1: Agent Components vs Discovered Improvements vs Online Metrics (for a primary YouTube surface)
Component
Discovery
YouTube-level metric
Surface-level metric
Optimizer
Transition to RMSprop
+0.06% [+0.03%, +0.09%]
+0.12% [+0.05%, +0.19%]
Optimizer
Training Efficiency (4× Improvement)
−0.01%[−0.05%, +0.03%]
+0.06%[−0.02%, +0.13%]
Optimizer
Training Efficiency (2× Improvement)
+0.01%[−0.03%, +0.05%]
+0.09% [+0.04%, +0.15%]
Architecture
Gated Path (GLU)
+0.06% [+0.02%, +0.11%]
+0.14% [+0.08%, +0.21%]
Architecture
Activation Refinement
−0.02%[−0.05%, +0.01%]
+0.12% [+0.05%, +0.19%]
Reward
Multi-Objective Synthesis
+0.05% [+0.02%, +0.08%]
+0.17% [+0.13%, +0.22%]
Reward
Hyperparameter Tuning
+0.05% [+0.01%, +0.08%]
+0.21% [+0.13%, +0.29%]
Results that are statistically significant at the 95% confidence level are shown in bold.
Table 2: Agent Components vs Discovered Improvements vs Online Metrics (for a different YouTube surface)
Component
Discovery
YouTube-level metric
Surface-level metric
Optimizer
Transition to FTRL
+0.03% [+0.01%, +0.05%]
+0.16% [+0.06%, +0.26%]
Architecture
Wide & Deep Model
+0.08% [+0.04%, +0.13%]
+1.10% [+0.98%, +1.22%]
Results that are statistically significant at the 95% confidence level are shown in bold.
Table 3: Agentic Discovery Highlights: Evolution of Model Components
Component
Discovery
Initial Configuration
Evolved Configuration
Optimizer
Transition to RMSprop
Adagrad(learning_rate=0.1)
RMSprop(learning_rate=0.005,rho=0.95,...)
Architecture
Gated Path (GLU)
layer_norm(relu(dense(relu(dense(
inputs,128,’linear’),128,’linear’)))
value_path*gate_path, where:
value_path=dense(shared,32,’linear’),
gate_path=dense(shared,32,’sigmoid’),
shared=relu(dense(inputs,128,’linear’))
Reward
Multi-Objective Synthesis
(factorA+factorB)*exprC
factor_new*(factorA+factorB)*exprC, where:
factor_new=GREATEST(...,1.0-GREATEST(0.0,
CAST(IFNULL(...,0) AS FLOAT)-...)/...)
(1) opt_2p5 (Baseline) Uses Gemini 2.5 Pro with an expert MLE
persona framing, and the full history of past configurations
and metrics sorted by offline loss.
(2) opt_flash Uses Gemini 2.5 Flash instead of Pro.
(3) opt_no_role Ablates the expert MLE persona framing.
(4) opt_no_sort Provides the full history of past metrics but
ordered by timestamp instead of loss.
(5) opt_top_1 / opt_top_5 Limits the history to only the top 1
and 5, respectively, sorted by offline loss.
(6) opt_no_context Provides no history of past configurations
or metrics.
Results are averaged over 6 independent runs exploring 70 ideas
each, reported as normalized z-scores of the loss where lower (more
negative) values indicate superior performance (Table 4).
5.4.1
Impact of Model Size and Reasoning. We evaluated the effec-
tiveness of different model choices within the Gemini family. As
shown in Table 4, a larger model with advanced reasoning capabili-
ties significantly outperforms a smaller variant. Specifically, Gemini
2.5 Pro consistently achieves lower loss compared to Gemini 2.5
Table 4: Agent Performance (Normalized Lproxy) for the Op-
timizer Component
Agent Configuration
Normalized Loss
opt_2p5
−0.84 [−1.70, −0.01]
opt_top_5
−0.72 [−1.49, 0.05]
opt_no_role
−0.52 [−1.43, 0.38]
opt_no_sort
0.06 [−0.93, 1.05]
opt_top_1
0.11 [−0.76, 0.98]
opt_flash
0.85 [0.66, 1.05]
opt_no_context
1.05 [0.94, 1.16]
Flash. This confirms that the reasoning required for algorithmic dis-
covery benefits from the increased parameter count and enhanced
"deep thinking" capabilities of the larger model class.
5.4.2
Persona and Context Length. We evaluated the impact of the
expert MLE persona framing by comparing it against an agent that
lacked the expert identity. This comparison confirms that expert

RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
Haochen Wang, Yi Wu, Daryl Chang, Li Wei, and Lukasz Heldt
Table 5: Experimental Velocity vs Type of Workflow
Metric
Human Workflow
Agent Workflow
Exp. Throughput
Θ(1) −Θ(10) / week
Θ(100) / week
Eng. Cost per Exp
Θ(1) −Θ(10) hours / week
0 hours / week
framing influences the relevance and depth of proposed config-
urations, making it critical for model quality. Similarly, context
engineering plays a vital role: providing the full, sorted history
from the Experiment Journal is better than no history, restricted
top-k, or unsorted history. As seen in Table 4, these results suggest
that a comprehensive and ranked distribution of past outcomes is
essential for effective iterative discovery.
5.5
Efficiency and Costs
A critical consideration for autonomous discovery systems is the
trade-off between the velocity gains enabled by the system and the
associated operational costs.
5.5.1
The Velocity Dividend. By decoupling the high-frequency of-
fline discovery from the low-frequency online validation, we have
removed human engineers from the repetitive and manual path.
The "Idea-to-Data" cycle – the latency from hypothesis generation
to experimental results – is significantly cheaper and faster. This ve-
locity dividend now enables the team to produce far more launches
than previously possible (Table 5).
5.5.2
LLM & Infrastructural Costs. The LLM token costs were ap-
proximately $20,000 over a six-month period, representing a mini-
mal fraction of the cost of a full-time MLE. The per-model compute
and memory costs remain identical for both human-driven and
agentic workflows, so the remaining infrastructure costs scale di-
rectly with the number of models tested.
5.6
Lessons Learned
The deployment of an autonomous, self-evolving system provided
several critical insights into the future of recommendation system
engineering, ranging from the practical considerations essential for
production stability (L1-L3) to the transformative reasoning power
unlocked by an agentic system (L4-L5).
• L1: Delta-based vs. Full Configuration Generation The
validity of proposals was significantly enhanced when the
agent was tasked with generating a delta against the produc-
tion file rather than the entire configuration file. Requesting
the complete configuration often led to hallucinations where
the model would omit essential but unchanged parameters
or introduce syntax errors. Furthermore, we find delta-based
generation to offer a decisive advantage in context manage-
ment. Because deltas are compact, we can attach Θ(100)
items from past history as context to each prompt. In con-
trast, existing methods like AlphaEvolve must aggressively
trim context because it is not feasible to include that much
history when the complete files are large.
• L2: Enforcing Diversity via Prompt Tuning Absent ex-
plicit instructions, the agent exhibited a strong bias toward
safe, incremental changes, effectively collapsing into a mode
of minor hyperparameter tuning (e.g., proposing "learning
rate 0.1" followed immediately by "learning rate 0.11"). To
counteract this, it was critical to prompt the agent to "bal-
ance exploration, exploitation, and innovation", forcing it to
attempt the leaps necessary for significant gains.
• L3: Importance of Warm Start The ability to nominate
good configurations is highly dependent on the density of
the Experiment Journal. Without past trials, the agent tends
to propose generic textbook improvements. To jumpstart
the discovery, we warm-start the Offline Agent’s daily run
with the best 𝐾findings from the preceding day, allowing
the agent to ground its reasoning in past learnings.
• L4: Semantic Reasoning vs. Numerical Tuning While
traditional AutoML excels at tuning scalars, our results show
that the highest leverage in mature systems comes from
structural and semantic mutations. For example, the Reward
persona’s ability to redefine the reward provided innovations
that purely numerical tuning could never achieve.
• L5: Generalizability Across Recommendation Surfaces
A critical question for any autonomous framework is trans-
ferability: can the agent adapt to new environments without
re-engineering? We deployed the same dual-agent architec-
ture to a different YouTube recommendation surface with a
completely different feature schema, training dataset, and
model configuration. Despite these differences, the agents
successfully adapted to the new context within the first few
iterations, generated valid hypotheses, and increased north
star metrics (Table 2). This confirms that our framework
optimizes the process of discovery rather than memorizing
a specific dataset, suggesting strong potential for generaliza-
tion across the broader family of recommendation systems.
6
Conclusion
In this paper, we present a comprehensive framework leveraging
Large Language Models (LLMs) for a self-evolving recommenda-
tion system, successfully deploying it at scale on the world’s largest
video delivery platform. By decoupling the discovery process into a
fast Offline Agent (driven by cheap proxy signals) and a reliable but
slow Online Agent (driven by delayed north star business metrics),
we have established a new paradigm for industrial machine learn-
ing that overcomes the limitations of traditional workflows. Our
extensive deployment results illustrate critical contributions of our
work to the field of automated machine learning. We showed that
LLMs, when grounded with the appropriate context and tools, are
capable of structural and semantic innovation in recommendation
systems. And by automating the repetitive mechanics of code gen-
eration, compilation, and experiment orchestration, we noticeably
compressed the "Idea-to-Data" cycle. This order-of-magnitude in-
crease in experimental throughput allows the system to explore the
long tail of the configuration space that human engineers simply
do not have the bandwidth to investigate.
Looking forward, we envision a shift in the role of the Machine
Learning Engineer (MLE). As a self-evolving recommendation sys-
tem executes on modeling improvements, the human engineer
moves focus to defining the strategic guardrails, ethical constraints,

Self-Evolving Recommendation System
RecSys ’26, September 27-October 02, 2026, Minneapolis, MN, USA
and the long-term vision of the system. We believe our work rep-
resents a foundational step toward that future, removing human
cognitive bandwidth as a bottleneck in scientific discovery in rec-
ommendation systems.
References
[1] M. Mehdi Afsar, Trafford Crump, and Behrouz Far. 2022. Reinforcement learning
based recommender systems: A survey. arXiv:2101.06286 [cs.IR] https://arxiv.
org/abs/2101.06286
[2] Bernd Bischl, Martin Binder, Michel Lang, Tobias Pielok, Jakob Richter,
Stefan Coors, Janek Thomas, Theresa Ullmann, Marc Becker, Anne-Laure
Boulesteix, Difan Deng, and Marius Lindauer. 2021.
Hyperparameter Op-
timization: Foundations, Algorithms, Best Practices and Open Challenges.
arXiv:2107.05847 [stat.ML] https://arxiv.org/abs/2107.05847
[3] Franklin Cardenoso and Wouter Caarls. 2025. Leveraging LLMs for reward
function design in reinforcement learning control tasks. arXiv:2511.19355 [cs.LG]
https://arxiv.org/abs/2511.19355
[4] Minmin Chen, Alex Beutel, Paul Covington, Sagar Jain, Francois Belletti, and Ed
Chi. 2021. Top-K Off-Policy Correction for a REINFORCE Recommender System.
arXiv:1812.02353 [cs.LG] https://arxiv.org/abs/1812.02353
[5] Xiangning Chen, Chen Liang, Da Huang, Esteban Real, Kaiyuan Wang, Yao Liu,
Hieu Pham, Xuanyi Dong, Thang Luong, Cho-Jui Hsieh, Yifeng Lu, and Quoc V. Le.
2023. Symbolic Discovery of Optimization Algorithms. arXiv:2302.06675 [cs.LG]
https://arxiv.org/abs/2302.06675
[6] Thomas Elsken, Jan Hendrik Metzen, and Frank Hutter. 2019. Neural Architecture
Search: A Survey. arXiv:1808.05377 [stat.ML] https://arxiv.org/abs/1808.05377
[7] Matthias Feurer, Aaron Klein, Katharina Eggensperger, Jost Tobias Springen-
berg, Manuel Blum, and Frank Hutter. 2015. Efficient and robust automated
machine learning. In Proceedings of the 29th International Conference on Neural
Information Processing Systems - Volume 2 (Montreal, Canada) (NIPS’15). MIT
Press, Cambridge, MA, USA, 2755–2763.
[8] et al. Gheorghe Comanici. 2025. Gemini 2.5: Pushing the Frontier with Ad-
vanced Reasoning, Multimodality, Long Context, and Next Generation Agentic
Capabilities. arXiv:2507.06261 [cs.CL] https://arxiv.org/abs/2507.06261
[9] Daniel Golovin, Benjamin Solnik, Subhodeep Moitra, Greg Kochanski, John Karro,
and D. Sculley. 2017. Google Vizier: A Service for Black-Box Optimization. In
Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge
Discovery and Data Mining (Halifax, NS, Canada) (KDD ’17). Association for
Computing Machinery, New York, NY, USA, 1487–1495. doi:10.1145/3097983.
3098043
[10] Sirui Hong, Mingchen Zhuge, Jiaqi Chen, Xiawu Zheng, Yuheng Cheng, Ceyao
Zhang, Jinlin Wang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou,
Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. 2024.
MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework.
arXiv:2308.00352 [cs.AI] https://arxiv.org/abs/2308.00352
[11] Hanxiao Liu, Karen Simonyan, and Yiming Yang. 2019. DARTS: Differentiable
Architecture Search. arXiv:1806.09055 [cs.LG] https://arxiv.org/abs/1806.09055
[12] Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David
Ha. 2024. The AI Scientist: Towards Fully Automated Open-Ended Scientific
Discovery. arXiv:2408.06292 [cs.AI] https://arxiv.org/abs/2408.06292
[13] Yecheng Jason Ma, William Liang, Guanzhi Wang, De-An Huang, Osbert Bas-
tani, Dinesh Jayaraman, Yuke Zhu, Linxi Fan, and Anima Anandkumar. 2024.
Eureka: Human-Level Reward Design via Coding Large Language Models.
arXiv:2310.12931 [cs.RO] https://arxiv.org/abs/2310.12931
[14] Jaehyun Nam, Jinsung Yoon, Jiefeng Chen, Jinwoo Shin, Sercan Ö. Arık, and
Tomas Pfister. 2025. MLE-STAR: Machine Learning Engineering Agent via Search
and Targeted Refinement. arXiv:2506.15692 [cs.LG] https://arxiv.org/abs/2506.
15692
[15] Alexander Novikov, Ngân V˜u, Marvin Eisenberger, Emilien Dupont, Po-Sen
Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco
J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri,
George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, and Matej
Balog. 2025. AlphaEvolve: A coding agent for scientific and algorithmic discovery.
arXiv:2506.13131 [cs.AI] https://arxiv.org/abs/2506.13131
[16] Carl Edward Rasmussen and Christopher K. I. Williams. 2005. Gaussian Processes
for Machine Learning. The MIT Press. doi:10.7551/mitpress/3206.001.0001
[17] Esteban Real, Alok Aggarwal, Yanping Huang, and Quoc V Le. 2019. Regularized
Evolution for Image Classifier Architecture Search. arXiv:1802.01548 [cs.NE]
https://arxiv.org/abs/1802.01548
[18] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli,
Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. 2023. Toolformer:
Language Models Can Teach Themselves to Use Tools. arXiv:2302.04761 [cs.CL]
https://arxiv.org/abs/2302.04761
[19] Noam
Shazeer.
2020.
GLU
Variants
Improve
Transformer.
arXiv:2002.05202 [cs.LG] https://arxiv.org/abs/2002.05202
[20] Jasper Snoek, Hugo Larochelle, and Ryan P. Adams. 2012. Practical Bayesian
Optimization of Machine Learning Algorithms. arXiv:1206.2944 [stat.ML] https:
//arxiv.org/abs/1206.2944
[21] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu,
Linxi Fan, and Anima Anandkumar. 2023. Voyager: An Open-Ended Embodied
Agent with Large Language Models. arXiv:2305.16291 [cs.AI] https://arxiv.org/
abs/2305.16291
[22] Yuyan Wang, Cheenar Banerjee, Samer Chucri, Fabio Soldo, Sriraj Badam, Ed H.
Chi, and Minmin Chen. 2025. Beyond Item Dissimilarities: Diversifying by Intent
in Recommender Systems. arXiv:2405.12327 [cs.IR] doi:10.1145/3690624.3709429
[23] Yuyan Wang, Mohit Sharma, Can Xu, Sriraj Badam, Qian Sun, Lee Richardson,
Lisa Chung, Ed H. Chi, and Minmin Chen. 2022. Surrogate for Long-Term User
Experience in Recommender Systems. In Proceedings of the 28th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining (Washington DC, USA)
(KDD ’22). Association for Computing Machinery, New York, NY, USA, 4100–4109.
doi:10.1145/3534678.3539073
[24] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei
Xia, Ed Chi, Quoc Le, and Denny Zhou. 2023. Chain-of-Thought Prompting
Elicits Reasoning in Large Language Models. arXiv:2201.11903 [cs.CL] https:
//arxiv.org/abs/2201.11903
[25] Yi Wu, Daryl Chang, Jennifer She, Zhe Zhao, Li Wei, and Lukasz Heldt. 2024.
Learned Ranking Function: From Short-term Behavior Predictions to Long-term
User Satisfaction. arXiv:2408.06512 [cs.LG] https://arxiv.org/abs/2408.06512
[26] Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny
Zhou, and Xinyun Chen. 2024.
Large Language Models as Optimizers.
arXiv:2309.03409 [cs.LG] https://arxiv.org/abs/2309.03409
[27] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan,
and Yuan Cao. 2023. ReAct: Synergizing Reasoning and Acting in Language
Models. arXiv:2210.03629 [cs.CL] https://arxiv.org/abs/2210.03629
[28] Xiangyu Zhao, Long Xia, Jiliang Tang, and Dawei Yin. 2019.
“Deep rein-
forcement learning for search, recommendation, and online advertising: a sur-
vey” by Xiangyu Zhao, Long Xia, Jiliang Tang, and Dawei Yin with Martin
Vesely as coordinator. ACM SIGWEB Newsletter 2019, Spring (July 2019), 1–15.
doi:10.1145/3320496.3320500
[29] Marc-André Zöller and Marco F. Huber. 2021.
Benchmark and Survey of
Automated Machine Learning Frameworks. arXiv:1904.12054 [cs.LG] https:
//arxiv.org/abs/1904.12054
