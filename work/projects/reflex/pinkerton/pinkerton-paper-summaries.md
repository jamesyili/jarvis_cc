# Agentic Recommender Systems — Paper Summaries

Comprehensive summaries of the five papers in this folder, written as Pinkerton-relevant reading notes. Each entry covers: core contribution, method detail, key findings, strengths + limitations, and relevance to Pinkerton's roadmap. See `work/projects/pinkerton-agentic-vision.md` for the synthesis against Pinkerton.

**Papers covered (in rough order of relevance to Pinterest's homefeed context):**

1. [Adobe 2025] *Towards Agentic Recommender Systems in the Era of Multimodal Large Language Models* — the taxonomy anchor.
2. [Google 2026] *Multi-Agent Video Recommenders (MAVR): Evolution, Patterns, and Open Challenges* — direct analog for visual-first platforms.
3. [Tsinghua 2024] *MACRec: a Multi-Agent Collaboration Framework for Recommendation* — concrete, minimal multi-agent recipe.
4. [Amherst/MIT 2024] *Building Cooperative Embodied Agents Modularly with Large Language Models (CoELA)* — cognitive architecture for coordinated agents (not recsys, but the modular pattern is load-bearing).
5. [Renmin U 2024] *User Behavior Simulation with Large Language Model based Agents (RecAgent)* — LLM agents as simulated users for offline eval.

---

## 1. Towards Agentic Recommender Systems in the Era of Multimodal LLMs

**Citation:** Huang, Wu, Xia, Yu, Wang, Yu, Zhang, Rossi, Kveton, Zhou, McAuley, Yao. *Towards Agentic Recommender Systems in the Era of Multimodal Large Language Models.* Adobe Research / UNSW / UCSD, 2025. 12 pages. arXiv:2503.16734.

**Core contribution:** This is a perspective / survey paper that positions LLM-based Agentic Recommender Systems (LLM-ARS) as the next paradigm in recsys. It does three things: (1) proposes a four-level evolution of RSs, (2) gives a formal four-module task formulation for agentic RSs, and (3) enumerates seven research questions that frame open problems in the field.

**Four-level evolution of RS:**

| Level | Name | Key characteristics |
|---|---|---|
| 0 | Traditional | Rule-based, collaborative filtering, content-based. Static, one-way. |
| 1 | Advanced | Deep learning, feedback integration, enhanced personalization but still predefined model structures. |
| 2 | Intelligent | Interactive, multi-modal input, dynamic adaptation, clarifying dialogue. |
| 3 | Agentic | Autonomous decision-making, continuous self-evolution, comprehensive memory + multi-modal perception, proactive + reactive. |

Pinterest's CLR-based HF recsys sits firmly at Level 1, with some Level 2 characteristics in tabs / query refinement surfaces. Pinkerton's trajectory is about moving the *tooling* that surrounds the recsys toward Level 3, not replacing the Level 1 recsys itself.

**Formal four-module LLM-ARS formulation:** An ARS is a tuple $(U, I, A, E, R)$ where $U$ = users, $I$ = items, $A$ = agents, $E$ = environmental contexts, and $R: U \times E \times A \to P(I)$ is the recommendation function. Each agent $a$ has a policy $\pi_a(s)$ over states $s = f(u, e)$. The authors decompose every ARS into four modules:

1. **User Profiling Module** — $P(u, t) = f(H(u,t), C(u,t), X(u,t); \theta_P)$. Dynamic profile from history, context, external signals. Examples cited: RecAgent, MACRec, AgentCF, SUBER.
2. **Planning Module** — Uses MDPs / RL / chain-of-thought over the profile + current environment state. Examples: BiLLP (LLM as learnable planner), RecMind, AutoConcierge (hierarchical planning).
3. **Memory Module** — $M(u,t) = g(H(u,t), C(u,t); \theta_M)$. Short-term + long-term + cross-session. Examples: RecMind, AgentCF (collaborative memory across agents), SUBER (RL sim for long-term preference).
4. **Action Module** — $A(s,a) = \pi_a(s)$, selects items to surface. Examples: Agent4Rec (generative agents), RecAgent, MACRec, MACRS (multi-agent conversational), InteRecAgent (LLM as brain + recsys models as tools), LLM4Rerank.

**Three LLM-ARS architecture patterns:**

- **Single-agent frameworks** — RAH (Learn-Act-Critic loop), Self-Inspiring Planning (retrospective path analysis), InteRecAgent (LLM core + tool-augmented with retrieval/ranking modules + candidate memory bus). Strengths: simpler, better for single-domain tasks. Weaknesses: scalability, no collaborative reasoning.
- **Multi-agent frameworks** — MACRec (Manager / Analyst / Reflector), PUMA (shared memory across agents). Strengths: modularity, parallelized reasoning, specialization. Weaknesses: coordination overhead, redundancy, consistency.
- **Human-LLM hybrid** — Learn-Act-Critic with user feedback (RAH), user embedding integration (Ning et al.), vector-quantization preference alignment (Shao et al.). Strengths: interpretability, fairness, trust. Weaknesses: requires user engagement.

**Seven research questions (RQ1-RQ7) the paper frames:**

1. How can LLM agents benefit RSs through reasoning, planning, collaboration?
2. How can they improve user understanding and decision-making?
3. What architectures / learning paradigms enable agentic RSs?
4. How to integrate multimodal reasoning?
5. How to evaluate and benchmark LLM-ARS?
6. How to balance autonomy and controllability?
7. How to achieve lifelong personalization without catastrophic forgetting?

**Key open problems named:**

- **Hallucination** — LLMs generate out-of-vocabulary items or fabricate user preferences. Mitigations: database-grounded generation, reflective instruction tuning, hallucination-detection frameworks, adaptive grounding at inference.
- **Efficiency** — orchestrating multiple LLMs / tools is expensive. Directions: lightweight distilled agents, shared intermediate outputs, model compression.
- **Benchmarking** — offline metrics don't capture multi-turn interaction, cross-modal effectiveness, adaptability to feedback.
- **Controllability and safety** — prompt injection, data poisoning, filter bubble reinforcement, over-personalization.
- **Lifelong personalization** — catastrophic forgetting, preference drift, scaling interaction history.

**Strengths:** Clean taxonomy, comprehensive citation of 100+ recent works in the space. The four-module formulation (Profiling / Planning / Memory / Action) is useful as a mental model for any agentic recsys — including Pinkerton, which currently collapses all four into one LLM prompt per session.

**Limitations:** Perspective paper, no original experiments. Reads like a call-to-arms more than a rigorous analysis. The four-level evolution is a useful narrative but not a falsifiable claim.

**Relevance to Pinkerton:** Use the four-module decomposition (Profiling / Planning / Memory / Action) as the mental model when refactoring M1 + M2 into a multi-agent crew (our Phase 2). The seven RQs are a useful checklist when scoping what Pinkerton can and cannot claim to do. Hallucination mitigations (database-grounded, reflective) map directly to our Reflector agent design.

---

## 2. Multi-Agent Video Recommenders (MAVR): Evolution, Patterns, and Open Challenges

**Citation:** Ranganathan, Dharmaratnakar, Sinha, Das. *Multi-Agent Video Recommenders: Evolution, Patterns, and Open Challenges.* Google LLC, WSDM Companion '26, Feb 2026. 8 pages. arXiv:2604.02211.

**Core contribution:** A domain-specific survey of multi-agent video recommender systems (MAVRS). Unlike the Adobe survey, which is broader, MAVR focuses on the video domain and introduces a taxonomy of **four collaboration patterns** that multi-agent recsys can take. The paper argues that video is a uniquely good testbed for agentic recsys because of the "modality gap" — video is too high-dimensional for a single LLM to ingest directly, forcing agentic decomposition.

**Why video forces agentic decomposition:** Text and product IDs can be tokenized into an LLM's context window. Video cannot — no current foundation model can ingest a user's full pixel-level watch history for reasoning. Multi-agent systems solve this by decoupling perception from reasoning: "Perception Agents" compress raw video into semantic summaries; "Reasoning Agents" operate on the compressed text. The same argument applies to Pinterest — pins are visual, and per-pin VLM perception must be cached and reusable.

**Four collaboration patterns:**

### 2.1 Hierarchical Orchestration (e.g., MMRF, MMAgentRec)

A central coordinating agent directs specialized subordinate agents. Subordinates can be collaborative (jointly propose a recommendation) or competitive (propose distinct recommendations, coordinator picks).

- **MMRF** (Model-based Multi-agent Ranking Framework): main agent maximizes primary objective (WatchTime); auxiliary agents each maximize a secondary signal (Follow, Like, Comment). An "Attentive Collaboration Mechanism" lets the main agent dynamically weight auxiliary inputs. This is a recsys analog of multi-head attention for competing objectives.
- **MMAgentRec** (tourism domain): prompts a single LLM to simulate multiple expert personas (natural sciences, humanities, etc.) that provide interdisciplinary advice. Includes a reflection mechanism for self-critique.

**Strengths:** Clear control flow, explicit objective balancing.
**Failure modes:** Coordinator bottleneck (single point of failure). Conflicting goals across auxiliary agents can harm the primary objective.

### 2.2 Pipeline-based Modular Collaboration (e.g., VRAgent-R1, MACRec)

Agents operate sequentially, forming a processing pipeline where each agent's output is the next agent's input. Analogous to traditional non-agentic industry pipelines (video processing, user history summarization, model training) where distinct teams manage stages.

- **VRAgent-R1**: Two-stage pipeline. (1) Item Perception (IP) Agent processes raw multimodal video content using "human-like progressive thinking" to generate enhanced semantic summaries. (2) User Simulation (US) Agent uses the enriched representations to simulate user decisions in an RL loop with GRPO (Group Relative Policy Optimization). Rewards: predicting the next video the user actually watched, plus chain-of-thought reasoning about whether a user would like a specific video.
- **MACRec** (see paper #3 for full treatment): Manager, Reflector, User/Item Analyst, Searcher, Task Interpreter operating in sequence with feedback loops.

**Strengths:** Modular, easy to debug, each stage can be independently improved.
**Failure modes:** Compounding errors and brittleness — an error in an early agent (e.g., the IP Agent) degrades the entire chain.

### 2.3 User-Agent Collaboration (e.g., TKGPT)

Multiple agents collaborate *internally* to power a single user-facing conversational interface. The goal is not just recommendations but to empower the end-user with direct natural-language control, enhancing "sense of agency."

- **TKGPT**: Modifies TikTok "For You" via natural language. Two internal assistants — Recommender Assistant interprets user requests into keywords; Sorting Assistant assigns weights to the keywords, which determine the proportion of videos for each topic in the next batch of 32 videos. The user sees a standard feed but has natural-language control.

**Strengths:** Users feel in control. Natural language → algorithmic action is the holy grail of recsys agency.
**Failure modes:** Misinterpretation of ambiguous intent can lead to drastic, undesired feed changes.

### 2.4 User Simulation Agent Ensembles (e.g., Agent4Rec, VRAgent-R1 US Agent)

Agents are used not as the core recommender but as a simulated user population to generate high-fidelity synthetic interaction data for offline evaluation, training, or studying emergent behaviors (filter bubbles, conformity).

- **Agent4Rec**: 1,000 LLM-empowered generative agents, each initialized from real data with profile + taste + social traits (activity level, conformity). Central goal is "agent alignment" — ensuring simulated behaviors match real humans.
- **VRAgent-R1 US Agent**: Uses GRPO for in-loop alignment with real user decisions.

**Strengths:** Sandbox for risk-free experimentation. Can study emergent phenomena without A/B tests.
**Failure modes:** Overfitting to initialization data. Prohibitive cost (thousands of LLM agents). Real-world validity uncertain.

**Evaluation framework — five dimensions:**

1. **Task-specific quality** — per-agent performance on sub-task (ROUGE/BERTScore for perception agents, qualitative logical coherence for reasoning agents, proxy metrics for specialized recommenders).
2. **Coordination efficiency** — communication overhead (tokens / API calls), latency, contribution alignment (do auxiliary agents actually help the main objective?).
3. **System-level emergent properties** — robustness / fault tolerance, adaptability to distribution shift, emergent behavior accuracy (KL divergence from real data).
4. **Human-alignment** — controllability / agency (user studies), explainability, trustworthiness (longitudinal), fairness (Jain's Index, Gini, Equalized Odds).
5. **Scalability / economic viability** — token cost per request, end-to-end latency, training cost.

**Five open challenges:**

1. **Computational cost and scalability** — Agent4Rec is "prohibitively expensive for most research labs." Direction: lightweight distilled agents, shared intermediate outputs.
2. **Multimodal grounding and reasoning** — lossy compression from video → text summary loses information. Direction: deep cross-modal reasoning.
3. **Evaluation** — offline metrics (nDCG, MRR) insufficient. Direction: integrate real-user feedback loops into benchmarks.
4. **Controllability and trustworthiness** — subordinate agents can silently diverge. Direction: transparent dashboards, value alignment testing.
5. **Incentive alignment** — agents with conflicting objectives (WatchTime vs Likes) can enter conflict. Direction: borrow from computational economics (auctions, contract theory). Note that incentives in LLM agents are configured via natural language, which the LLM may reinterpret.

**Four future research directions:**

1. **Hybrid RL-LLM architectures** — LLM as high-level "planner" setting goals / reward-shaping functions for a downstream RL policy that does fine-grained action selection. "Planner-executor" hybrids.
2. **Lifelong personalization and agent memory** — long-term dynamic memory of user preferences. Federated Collaboration: a local User Profile Agent co-located with the user (on-device) performs lifelong personalization with raw data that never leaves the device.
3. **Human-in-the-loop validation** — crowdsourced critique and ranking as continuous supervision. Interactive dashboards visualizing reasoning and fairness trade-offs. Eventually, derive signals via multimodal affect detection (facial expression, tone).
4. **Self-improving recommenders** — meta-agents that evaluate reasoning quality, detect distribution shifts, autonomously propose schema / policy updates.

**Strengths:** The four-pattern taxonomy is the most actionable contribution of any paper in this folder. It maps cleanly onto architectural decisions for Pinkerton. The evaluation framework (five dimensions) is comprehensive and reusable.

**Limitations:** Like the Adobe survey, no original experiments — it's an evolution survey. Published at WSDM Companion (workshop, not main track), so the claims are exploratory rather than validated.

**Relevance to Pinkerton:** This is the most Pinterest-applicable paper in the folder.

- **Pattern adoption**: Use Pipeline-modular at the top level (M1 → M2 → M3 already maps to this), with Hierarchical Orchestration *inside* the diagnosis step (Manager + specialized Analysts).
- **IP Agent analog**: The VLM pin perception cache (Building Block 2.6 in the vision doc) is a direct implementation of VRAgent-R1's Item Perception Agent.
- **Simulation as eval**: Agent4Rec pattern is the model for Pinkerton Phase 4 (offline simulation harness). The paper's honest account of cost + fidelity challenges is our warning label.
- **Hybrid RL-LLM**: MAVR's "planner-executor" hybrid is the template for Pinkerton's speculative Phase 6.

---

## 3. MACRec: a Multi-Agent Collaboration Framework for Recommendation

**Citation:** Wang, Yu, Zheng, Ma, Zhang. *MACRec: a Multi-Agent Collaboration Framework for Recommendation.* Tsinghua University. SIGIR '24 (accepted), 5 pages. arXiv:2402.15235v3, Nov 2024. Code: https://github.com/wzf2000/MACRec.

**Core contribution:** A concrete, open-source multi-agent framework that tackles recommendation tasks *directly* — in contrast to prior agent-based recsys work that used agents only for user / item simulation. MACRec provides customizable multi-type agents with different roles that collaborate on a specific recommendation task. The paper is deliberately practical: it ships a framework with a web interface and applies it to four canonical recsys tasks.

**Five agent roles:**

1. **Manager** — Central orchestrator. Operates a ReAct-style Thought → Action → Observation loop. In the Thought phase, reasons about the current task state (is analysis sufficient? do we need more info?). In the Action phase, either produces an answer to end the task or calls another agent for help. In the Observation phase, receives responses from other agents.

2. **Reflector** — Judges the correctness of the Manager's answer. Only activates when the Manager is about to perform a second or subsequent attempt on the same task. If the Reflector judges the answer has no room for improvement, the Manager stops. Otherwise, the Reflector summarizes where the Manager can improve (e.g., "not considering the few highly-rated items in the user's historical interactions").

3. **User/Item Analyst** — Specializes in examining and understanding user preferences and item attributes. Has access to two tools: (1) **info database** (retrieves user profiles and item attributes), (2) **interaction retriever** (retrieves user-item interaction history up to current time). Combining these, the Analyst produces in-depth analysis of user or item.

4. **Searcher** — Executes search queries over external tools (e.g., Wikipedia) and summarizes results for the Manager. Two-stage search: (1) retrieve most relevant entry, (2) retrieve passages matching keywords, (3) summarize to the Manager's query. This is the "external knowledge" agent.

5. **Task Interpreter** — Translates user dialogs into executable recommendation tasks. Gets conversation history, summarizes (if long) via text summarization tool, produces a specific task description that guides Manager runs.

**Framework flow for a sequential recommendation task:**

1. Task Interpreter translates user input → structured task.
2. Manager starts calling other agents for analysis.
3. Searcher + User/Item Analyst provide inputs.
4. Manager attempts an answer (e.g., ranking of candidate sets).
5. Reflector evaluates the answer, provides feedback.
6. Manager reattempts with reflection incorporated.
7. Final answer returned.

**Four applications demonstrated:**

| Task | Required agents | Notes |
|---|---|---|
| **Rating Prediction (RP)** | Manager, User Analyst, Item Analyst | Each user has different rating tendencies; target item characteristics matter. |
| **Sequential Recommendation (SR)** | Manager, User Analyst, Reflector (required); Item Analyst, Searcher optional | Long-term and short-term interest modeling; Reflector helps with complex output format (ranking of candidate set). |
| **Explanation Generation (EG)** | Manager, User Analyst, Item Analyst, Searcher | Both user and item analysis needed; Searcher retrieves extra context (e.g., director info not in dataset). |
| **Conversational Recommendation (CR)** | Manager, Task Interpreter, Searcher | Task Interpreter translates ambiguous dialog; Searcher grounds unknown entities. |

**Comparison table (from the paper):**

| Model | Objective | Single-type agents | Multi-type agents | Diverse scenarios | Open-source |
|---|---|---|---|---|---|
| RecAgent | User Sim | ✓ | | | ✓ |
| Agent4Rec | User Sim | ✓ | | | ✓ |
| AgentCF | U-I Sim | | ✓ | | |
| RAH | Recommender | | ✓ | | |
| RecMind | Recommender | ✓ | | ✓ | |
| InteRecAgent | Recommender | ✓ | | | |
| **MACRec** | **Recommender** | | **✓** | **✓** | **✓** |

MACRec is positioned as the first open-source framework supporting multi-type agents for diverse recommendation scenarios.

**Web interface:** Configuration panel (task selection, agent config) + interaction panel (live collaboration visualization). Demonstrated case: user expresses preference for "Schindler's List," seeks similar historical movies. Task Interpreter summarizes → Manager calls Searcher twice (one for "movies about history," one for "movies similar to Schindler's List") → Manager recommends "Amistad."

**Strengths:** This is the cleanest, most practical multi-agent recsys recipe in the literature. The role decomposition is minimal but covers the important jobs. Open-source, usable off-the-shelf. The Thought / Action / Observation loop is the same pattern Claude Code uses, so the mental model is already familiar.

**Limitations:** Short paper (5 pages). No rigorous quantitative comparison to single-agent baselines — the emphasis is on framework design and demonstrability, not on proving the multi-agent approach wins. The Reflector is described as only activating on retries, which may be too conservative for production use. The framework is research-quality, not production-ready.

**Relevance to Pinkerton:** **The most directly applicable paper for Pinkerton's multi-agent refactor (Phase 2).** The five roles map 1:1 to diagnosis work we already do:

- Manager → the current SKILL.md orchestrator.
- User/Item Analyst → Funnel Analyst (stage semantics) + User Analyst (M2 profile) + Content Analyst (pin perception).
- Reflector → diagnosis critic (catches hallucinated signals, validates causal claims).
- Searcher → Pinterest-internal knowledge retrieval (wiki, runbooks, prior sessions).
- Task Interpreter → parses natural-language debugging asks into structured investigations.

Don't literally import the MACRec codebase; use the role taxonomy as our blueprint.

---

## 4. Building Cooperative Embodied Agents Modularly with Large Language Models (CoELA)

**Citation:** Zhang, Du, Shan, Zhou, Du, Tenenbaum, Shu, Gan. *Building Cooperative Embodied Agents Modularly with Large Language Models.* UMass Amherst, Tsinghua, SJTU, MIT, MIT-IBM Watson AI Lab. ICLR 2024. 29 pages. Project: https://vis-www.cs.umass.edu/Co-LLM-Agents/

**Core contribution:** This is **not** a recsys paper — it's an embodied multi-agent cooperation paper. Included in the folder because its **cognitive architecture is the cleanest modular design pattern** in the broader LLM agent literature, and the pattern transfers to any multi-agent problem including recsys. CoELA (Cooperative Embodied Language Agent) solves multi-agent cooperation problems under the hardest version of the problem: decentralized control, raw sensory observations, costly communication, long-horizon multi-objective tasks. Two agents (or one agent + human) must coordinate via natural language to complete household rearrangement tasks in simulated environments.

**Why this matters for recsys work:** The cognitive architecture (Perception / Memory / Communication / Planning / Execution) is a load-bearing decomposition that any agentic system benefits from — including a diagnostic tool like Pinkerton that has no physical embodiment but does have perception (querying data), memory (trace DB), communication (between agents), planning (investigation steps), and execution (writing reports).

**Five-module architecture:**

1. **Perception Module** — Processes raw sensory observations (ego-centric 512×512 RGB-D images in the embodied setting). Uses Mask-RCNN for visual processing. In a recsys setting, "perception" becomes querying the data substrate (Presto tables, event logs, features).

2. **Memory Module** — Three distinct memory types inspired by cognitive architectures (Laird 2019):
   - **Semantic memory** — CoELA's knowledge about the world: semantic map, task progress, self state, other agents' state. Updated on each new observation. Note that semantic memory may be inaccurate because other agents can change world state without CoELA's awareness.
   - **Episodic memory** — Action history and dialogue history. Every action (including sending/receiving a message) is appended.
   - **Procedural memory** — Code for carrying out high-level plans in specific environments, plus neural model parameters. This is the "how to do X" knowledge.

3. **Communication Module** — Addresses the "what to send" problem with deliberate prompting. Retrieves related info from Memory (semantic map, task progress, agent states, action + dialogue history), converts to text descriptions via templates, prompts LLM with (Instruction Head + Goal Description + State Description + Action History + Dialogue History) to generate the message. Two seed messages appended at the beginning of dialogue history to elicit desired communication behavior. Key insight: **communication is costly, so deliberately decide what and when to send before actually sending**.

4. **Planning Module** — Retrieves info from Memory, converts to text, compiles an **Action List** of all available high-level plans proposed from current state + procedural knowledge, then prompts LLM with current info + Action List to select the plan. Uses zero-shot chain-of-thought. Key design choice: rather than letting the LLM freeform a plan, constrain it to picking from an enumerated list — this keeps the LLM focused on reasoning, not on syntactic correctness of plan output.

5. **Execution Module** — Generates primitive actions to carry out the high-level plan. Explicitly separated from Planning because LLMs are good at high-level planning but bad at low-level control. The Execution module retrieves the procedure from Procedural Memory and executes it. This design reduces LLM inference time and cost.

**Experiments and results:**

- **Environments**: TDW-MAT (ThreeDWorld Multi-Agent Transport, 24 episodes) and C-WAH (Communicative Watch-And-Help, 10 episodes).
- **Metrics**: Transport Rate (TR) and Efficiency Improvement (EI = ∆M/M₀).
- **Baselines**: MCTS-based Hierarchical Planner (MHP), Rule-based Hierarchical Planner (RHP), Multi-Agent Transformer (MAT, a MARL baseline).
- **Key results**:
  - On TDW-MAT, CoELA (GPT-4) + CoELA achieves TR = 0.71, +39% over RHP alone.
  - On C-WAH, CoELA + CoELA achieves +49% efficiency improvement vs baseline.
  - With Oracle Perception on TDW-MAT, CoELA + CoELA hits TR = 0.85.
  - Replacing GPT-4 with LLAMA-2 causes a significant performance drop, but **fine-tuning a CoLLAMA via LoRA on agent-collected data recovers competitive performance** (0.70 TR) and even surpasses GPT-4 on the Stuff subtask.
  - Multi-Agent Transformer (MAT) baseline, trained with full observability, achieves only 0.15 TR — decisively beaten.

**Human study findings:** 8 subjects, 80 trials, cooperated with MHP, CoELA, CoELA-without-communication, and alone. Key findings:
- Humans trust CoELA (communicating in natural language) more than MHP.
- Ablation: the Memory Module and a strong LLM for Planning are both critical.
- The Communication Module matters *more* when cooperating with humans than with other AI agents — natural-language communication is the trust enabler.
- CoELA exhibits emergent cooperative behaviors: sharing progress / information, knowing when to request help, adapting plans considering others, and **knowing when not to communicate**.

**Strengths:** Rigorous experimental setup with strong baselines. Ablation study that isolates the contribution of each module. Demonstrates that open LLMs can be fine-tuned to match GPT-4 in this framework with minimal data. The cognitive architecture is cleanly decomposed and each module has a well-defined interface.

**Limitations:** Embodied / household domain is far from recsys. Two-agent setting (paper notes generalization to more agents is theoretically possible but not demonstrated). Cost constraints limited evaluation to 1 run of CoELA vs 5 of baselines.

**Relevance to Pinkerton:** Three load-bearing transfers.

1. **Memory decomposition (Semantic / Episodic / Procedural)** maps directly to Building Block 2.4 (semantic memory = HF domain knowledge), 2.1 (episodic = SQLite trace DB), and 2.5 (procedural = playbooks / debugging recipes). This is a more principled decomposition than just "store session traces."
2. **Costly communication principle** — even though Pinkerton's agents will run in a single process (not distributed), the principle of "deliberately decide what and when to surface before surfacing" is valuable. It's the justification for having a Reflector critique intermediate outputs before they propagate.
3. **Separation of Planning from Execution** — the insight that "LLMs are good at high-level planning but bad at low-level control" applies to SQL query generation in Pinkerton. A Funnel Analyst should select a query *template* from a library (planning), not freestyle SQL (execution). This is the justification for Building Block 2.2 (funnel query library).

---

## 5. User Behavior Simulation with LLM-based Agents (RecAgent)

**Citation:** Wang, Zhang, Yang, Chen, Tang, Zhang, Chen, Lin, Sun, Song, Zhao, Xu, Dou, Wang, Wen. *User Behavior Simulation with Large Language Model based Agents.* Renmin University of China, UCL. Feb 2024. 28 pages. arXiv:2306.02552v3.

**Core contribution:** Introduces **RecAgent**, a simulator where LLM-based agents act as simulated users interacting with a recommender system, each other, and the environment. The framework is cognitive-neuroscience-inspired (profile + memory + action modules) and includes a sandbox environment that is *intervenable* (agents can be edited mid-simulation) and *resettable*. Evaluated for behavioral fidelity against real human behaviors, then applied to study two social phenomena (information cocoons and user conformity) with proposed mitigation strategies.

**Why simulation matters:** Three motivations stated in the paper:
1. Real human data is expensive to acquire and raises privacy / ethical concerns.
2. Existing simulators use simple functions (inner product, MLP) that don't capture human decision complexity.
3. Existing simulators have a "chicken-and-egg" problem — they need real data to learn simulators, which limits their generalization to novel patterns.
4. Existing simulators are limited to single environments (recsys OR social network), but real user behavior crosses environments.

LLMs change this: they've learned web-scale corpora that include user behavior patterns, which enables near-zero-shot simulation and multi-environment modeling.

**RecAgent framework — three modules:**

1. **Profile Module** — Background features per user: ID, name, age, gender, career, traits (e.g., "compassionate," "ambitious"), interests (item categories like "sci-fi movies"). Traits drive personality; interests drive behavior.

2. **Memory Module** — Three memory types inspired by cognitive neuroscience:
   - **Sensory memory** — Directly interacts with the environment, summarizes raw observations into more informative content with importance scores.
   - **Short-term memory** — Intermediate layer. If an agent repeatedly encounters similar observations, related short-term memories are *enhanced* and transformed into long-term memories.
   - **Long-term memory** — Stores important information for reuse, generalizes to unseen observations, supports self-reflection (generating high-level abstract info from specific observations).
   
   Memory retrieval is similarity-based (embeddings). There's also a "forget ratio" to prevent unbounded growth.

3. **Action Module** — Six behavior types:
   - **Recsys actions**: Searching, Browsing, Clicking, Next-page
   - **Social actions**: One-to-one chatting, One-to-many broadcasting

**Sandbox characteristics:**
- **Round-based simulation** — Each round, a subset of agents take actions.
- **Pareto-distributed activity** — Agent activity follows a Pareto distribution (small number highly active, majority low frequency) to match real-world long-tail behavior.
- **Agnostic to recsys algorithm** — Any recommendation model can be plugged in.
- **Intervenable** — Can edit agent profiles mid-simulation (change gender, career, interests) to study counterfactuals.
- **Human-in-the-loop** — Real humans can also participate as agents.

**Believability experiments:**

- **Recsys behavior fidelity** (MovieLens-1M, 20 users): The task is "given a user's early interactions, predict their future selections from a candidate list of $(a+b)$ items with $a$ ground truths." Baselines: Embedding method, RecSim, Real Human. Across $(a,b)$ pairs, **RecAgent surpasses best baseline by ~68% on average and is only ~8% lower than Real Human**. For generative capability (sequence prediction), adversarial subjective evaluation with human annotators shows RecAgent's win rate is 45.0% vs RecSim's 33.3% (N=5 rounds); advantage persists at longer sequences (N=10).
- **Chatting / broadcasting behavior** — 20 agents run for 5/10/15 rounds; 3 annotators rate believability on 1-5 scale. Most scores > 4 (believable). **Caveat: after 15 rounds, scores drop below 4** — the authors speculate the LLM loses attention as memory accumulates.
- **Memory mechanism ablation** — Remove short-term memory → informativeness drops. Remove long-term memory or reflection → relevance drops. Complete module achieves best relevance + comparable informativeness.

**Information cocoon study:**

- 50 agents, Matrix Factorization recsys, incremental training.
- Measure entropy $E = -\frac{1}{|U|} \sum_u \sum_c f_{u,c} \log f_{u,c}$ over item categories.
- Baseline simulation (blue): entropy declines over 50 rounds → cocoon forms (-8.5% from peak).
- **Rec-Strategy** (replace 1 of 5 recommended items with random): every-round intervention enhances entropy by 15.3-19.6% vs 5- / 10-round, but user satisfaction drops.
- **Soc-Strategy** (add N=1,3,5 friends with different interests): more friends → better cocoon alleviation.
- **Combined strategy**: further improvement.
- Replacing N=3 or N=5 items improves entropy by 30.8% / 52.6% but user satisfaction drops further.

**Conformity study** (not detailed above but in the paper): agents can see social cues (evaluations from others) and adjust their own ratings. Demonstrates that LLM agents replicate conformity bias observed in humans.

**Strengths:** Rigorous believability evaluation with real human baselines. Successfully reproduces known phenomena (cocoons, conformity). The sandbox design (intervenable + resettable + algorithm-agnostic) is genuinely reusable infrastructure. Three-layer memory is principled.

**Limitations:**
- Only 20 users for recsys believability experiments.
- Believability degrades as memory accumulates (15+ rounds) — long-horizon simulation is an open problem.
- No production deployment — this is a research simulator, not a battle-tested tool.
- The MovieLens movie domain is simple compared to visual recsys. No equivalent experiments on Pinterest-like visual data.
- The information cocoon result is a known phenomenon the simulator reproduces — it doesn't prove the simulator can discover novel phenomena.

**Relevance to Pinkerton:** This is the paper that defines the **best-case scenario for Pinkerton Phase 4** (offline simulation harness).

- **Architecture template**: Profile (from Pinkerton M2) + Memory (three-layer adapted for session-level behavior) + Action (click / save / skip / long-dwell / search) is directly adoptable.
- **Fidelity validation approach**: The 20-user held-out experiment is exactly the gate we need to pass before committing to Phase 4 — can M2 profiles predict held-out behavior better than baselines?
- **Honest limitations**: The 15-round memory degradation is a warning about simulator decay over longer horizons. The 8% gap to real humans is probably the floor for Pinterest-scale fidelity expectations.
- **Phase 4 MVP scoping**: The information-cocoon experiment (50 agents, MF recsys, 50 rounds, entropy metric) is roughly the right size for a first Pinkerton simulation. Ambitious but not absurd.

The critical question the paper *doesn't* answer for us: can simulator fidelity transfer from MovieLens (text-based, small, well-studied) to Pinterest (visual, massive, noisy)? The only way to know is to build the held-out prediction test on M2 and run it.

---

## Appendix: Cross-Paper Themes

### Modules and agent roles — side-by-side

| Paper | Profiling | Planning | Memory | Action / Execution | Coordination |
|---|---|---|---|---|---|
| Adobe survey | User Profiling Module | Planning Module | Memory Module | Action Module | Single / multi / hybrid |
| MAVR | User Analyst (in MACRec pattern); user profile in Agent4Rec | Reasoning agents | Lifelong memory (future direction) | Recommender actions | 4 patterns: hierarchical / pipeline / user-agent collab / sim ensemble |
| MACRec | User Analyst | Manager (Thought/Action/Observation) | (implicit, via tools) | Final ranking / explanation | Manager orchestrates; Reflector critiques |
| CoELA | (implicit in Semantic memory) | Planning Module | Semantic / Episodic / Procedural | Execution Module (primitive actions) | Two-agent decentralized, costly comms |
| RecAgent | Profile Module | (implicit in LLM action selection) | Sensory / Short / Long-term | Six action types | Multi-agent sandbox, Pareto activity |

### Common challenges across all five papers

1. **Cost and latency** — every paper names this; none solve it.
2. **Hallucination / out-of-vocabulary** — solved partially by database grounding, reflective tuning, verification at inference.
3. **Evaluation / fidelity** — offline metrics insufficient; sim-to-real gap is open.
4. **Controllability vs autonomy** — all papers converge on human-in-the-loop as the answer for now.
5. **Memory management at scale** — short-term vs long-term vs procedural distinctions matter; unbounded memory causes LLM attention loss.
6. **Multi-agent coordination** — orchestration bottleneck, compounding errors, incentive misalignment.

### What's converged and what's not

**Converged (adopt with confidence):**
- Modular decomposition (perception, memory, planning, action) wins over monolithic prompts.
- ReAct-style Thought/Action/Observation loops are the default orchestration pattern.
- Reflector / Critic loops improve output quality at low cost.
- Human-in-the-loop is necessary for production deployment.
- Separating item / content *perception* from *reasoning* unlocks scale for multimodal content.

**Not converged (build carefully):**
- Simulator fidelity for offline eval — unproven at scale.
- Hybrid RL-LLM architectures — no production examples yet.
- Lifelong personalization / catastrophic forgetting — open research.
- Multi-agent incentive alignment — borrowing from economics is proposed but not demonstrated.
- Agentic candidate generation as primary retrieval — currently loses to deep models.
