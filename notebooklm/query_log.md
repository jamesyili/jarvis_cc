# NotebookLM Query Log

> Rolling log of queries sent to NotebookLM notebooks and their outcomes. Helps James see what Leo is consulting, evaluate response quality, and improve query patterns over time.

---

## 2026-04-12T00:11:00Z — Wes Kao Frameworks (spawned via consult-notebook agent)

**Query 1 (session opener):**
James is a Sr. EM at Pinterest framing Q1 learnings for a VP-level (skip-level) review. The VP optimizes for system velocity, clear ownership, and org entropy reduction. Apply Wes Kao's frameworks on executive communication and managing up to answer: (1) What altitude should Q1 learnings be pitched at for a VP audience — what separates a strategic insight from a tactical report? (2) What persuasive structure works best — BLUF, situation-complication-resolution, or something else — and what signals ownership vs. reporting?

**Response 1:**
To pitch your Q1 learnings effectively to a VP who optimizes for system velocity and org entropy reduction, you must elevate your communication from a standard progress report to a strategic business case.

1. ALTITUDE: Make Assertions, Not Just Insights — An insight is simply an observation, which is only a starting point. A tactical report lists insights. A strategic report transforms them into Assertions that answer "so what?", demonstrate a bias toward action, and show ownership of the solution. Avoid the "Pigeonholed Project Management" trap — do not describe learnings through the lens of coordination, process, or workflows. Frame the problem and why it matters to the business. Tie to velocity and entropy metrics. The Bad Things / Good Things framework: "What bad things happen if we don't fix this? What good things happen if we do?" Fewer Status Updates, More Next Steps — spend 20% on Q1 past, 80% on what's ahead.

2. PERSUASIVE STRUCTURE: Use BLUF / 3A Pyramid Principle — Answer first, arguments second, add-ons last. Start Right Before You Get Eaten By the Bear — cut backstory scope creep. Aim for minimum viable backstory (~10-20%). Emotional Signposting — reduce cognitive load by telling the VP how to interpret data, don't make them guess. OAV (Observe, Assert, Validate) to Signal Ownership — a reporter says "here are our bottlenecks, what should we do?" An owner observes, asserts a recommendation, and validates by asking "how does that sound?"

**Query 2 (applied critique):**
Apply those frameworks directly to James's three Q1 learning drafts. For each: (a) flag where framing drifts tactical, (b) give the one-sentence BLUF reframe, (c) identify the missing/weak OAV assertion. [Full drafts included in query — see main session context for full text]

**Response 2:**
LEARNING 1: (a) Drifts into logistics by focusing on the "how" (Full Funnel Logging, agentic AI tooling) and giving a chronological backstory of pain — fails to answer "how will this increase velocity or save money?" (b) BLUF: "We are cutting incident resolution time from days to minutes by deploying AI-driven debugging and Full Funnel Logging, which will recover massive amounts of engineering velocity in Q2." (c) Weak OAV: Draft observes the gap and passively asserts a plan, but lacks a validation step and doesn't force a decision from the VP. Strong OAV: "I noticed debugging incidents take days instead of minutes. I recommend making Full Funnel Logging a P0 requirement across all teams in Q2. Do I have your buy-in to enforce this integration?"

LEARNING 2: (a) "Backstory scope creep" — recounts the Q1 learning journey chronologically, violating "start right before you get eaten by the bear." Spends too much time on past. (b) BLUF: "To drastically reduce organizational entropy and unnecessary parallel work, our new engineering mandate for Q2 is to default to unified, cross-surface architectures and place the burden of proof entirely on divergence." (c) Weak OAV: Assertion is strong but lacks the Validate step to lock in executive alignment. Strong OAV: "I've observed that branching early creates massive organizational entropy. I assert we must enforce a 'unified-first' architecture mandate in Q2. Do you see any risks with me pushing this mandate across the broader engineering org?"

LEARNING 3: (a) "Pigeonholed project management" trap — explains mechanics of the sprint instead of strategic business impact. "We should identify and invest" is weak, hesitant language that avoids responsibility. (b) BLUF: "Cross-team sprints exposed that our biggest velocity bottlenecks exist at the integration seams between ML and UX; in Q2, we are establishing dedicated 'connective tissue' investments to proactively unblock multiple teams." (c) Weak OAV: "We should identify and invest" lacks ownership — doesn't define who does the identifying or investing. Strong OAV: "I noticed our biggest velocity drags are at the integration seams between ML and UX. I recommend we dedicate 15% of Q2 engineering bandwidth specifically to 'connective tissue' accelerators rather than feature work. How does that sound?"

**Session ID:** b6a33876


---

## 2026-04-12T01:22:00Z — Coaching Patterns (spawned via consult-notebook agent)

**Query:**
James is a Senior Engineering Manager with a Di DISC profile (D:88%, i:88%) navigating competitive organizational dynamics. His AI tooling work (Pinsight + Reflex) is gaining traction, but he's experiencing competitive anxiety because a peer Sr. EM (Roberto) had his tools celebrated org-wide by a VP, and James perceives the VP and Sr. Director are giving warmer reception to peers than to him. He's spending Saturday ruminating on these dynamics instead of recovering.

Three targeted questions:

1. What coaching frameworks apply to competitive anxiety and status-comparison triggers in high-D/high-i leaders? James's pattern: status sensor fires → jealousy/competition activation → reactive behavior or rumination spiral. What is the underlying identity dynamic at work, and what intervention breaks the cycle fastest?

2. James faces a structural trap: he could end up as the implementer while a Sr. Director (Andrew) owns the Reflex narrative, and the VP celebrates it as Andrew's win. What frameworks help him read organizational power dynamics clearly — distinguishing real threats from perceived slights — and what's the coaching move for knowing when to assert vs. when to observe and let the work speak?

3. James's growth edges are: recovery time from triggering events, reading rooms for political context, knowing when NOT to speak, and observation-as-contribution. How do these connect to his Di identity pattern — where does the Di drive create blind spots in competitive environments specifically? What would a coach advise about channeling competitive energy productively vs. letting it drive reactive under-managing-up behavior?

**Response:**
Question 1: Coaching Frameworks for Competitive Anxiety and Status-Comparison Triggers
For a high-D/high-i leader experiencing competitive anxiety, the most relevant frameworks are Tool 8 ("Signal, Not Truth"), the Rumination Framework, and Module 2/3 of the Executive Coaching Syllabus (Somatic Mapping & Reframing Status).
The underlying identity dynamic driving James's spiral stems from childhood patterns where love and approval were tied to achievement, comparisons, and an unspoken debt of success. As a result, James's internal "status sensor" translates a peer's success (like Roberto's) into a literal threat to his identity, making him feel he has to constantly "earn his place" rather than feeling he is fundamentally enough. He equates his position in an organizational ranking with his human worth.
The fastest intervention to break this rumination cycle is the action-oriented "Signal, Not Truth" (Tool 8) framework, which builds a gap between sensation and identity. Because "sitting with the feeling" doesn't work for his action-oriented Di profile, he must execute the following reps:
- Name it: Overtly state, "The status sensor is firing. Signal, not truth"
- Locate it physically (Somatic Mapping): Identify where the anxiety sits in the body (chest, stomach, etc.) to detach from the story and recognize it as merely a physical sensation
- Redirect the fuel within 10 minutes: Recognize the anxiety as energy, not a fire alarm. Immediately point that energy toward his own internal scoreboard — such as writing 30 minutes of code, learning a new retrieval path, or building something tangible
To stop the mental spin, he should apply the Rumination Framework and ask himself one factual question: "What do I actually know right now? Everything else is creative writing."

Question 2: Structural Traps and Organizational Power Dynamics
James is falling into the "Coordinator Trap" combined with a failure to "Match Altitude to Audience Appetite." He defaults to a strategic "Director" move — orchestrating and framing the AI transition — in a room where the VP specifically rewards "IC" moves, like shipping and demoing tangible tools. Executives at that level do not buy blueprints; they buy demos. By coordinating the narrative for Andrew or others, James makes himself invisible.
To read these power dynamics clearly and distinguish real threats from perceived slights, James should use Module 4: The "Impact Over Approval" Audit. This requires him to ruthlessly assess whether he is acting merely to gain executive approval or to drive actual systemic impact. He must also utilize the Tai Chi Base (Tool 4) to absorb the external force of Roberto's celebration without internalizing it as a reflection of his own worth.
For the coaching move on asserting vs. observing:
- Observation-as-Contribution (The Dhruvil Pattern): Instead of strongly advocating for a position, frame input as practitioner observations from the field. Saying, "What we're seeing on the retrieval side is..." adds immense value without sounding territorial.
- Letting the Work Speak: When asserting work, stop narrating the architecture. Put the tool in the leader's hands, show the before/after, and let them experience the value directly.

Question 3: Di Identity Pattern Blind Spots and Channeling Energy
James's Di profile creates specific blind spots under pressure. His drive for efficiency (High D) can make his tone read as dismissive or harsh to people with whom he hasn't yet built relationship capital. Simultaneously, his drive to influence (High i) causes him to fill silence with contribution. When stressed, this manifests as over-explaining, burying the lead, and rambling about backstory or architecture instead of delivering brief, high-leverage insights.
A coach would advise James to channel his competitive energy away from high-heat "Catalytic Clarity" and toward "Boring Consistency." Instead of needing to be the "owner of the truth" who defensively litigates a point, he should channel his energy into being the steady "mechanic fixing the car."
To prevent competitive energy from driving reactive, validation-seeking managing-up, James should systematically use the Three-Beat Managing Up Framework:
1. Share what is hardest about his job right now.
2. Show how he is crushing it despite those difficulties.
3. Enlist the manager's help on a specific unblocker.
This channels his drive into creating structural leverage and demonstrating capability, rather than seeking a mirror to prove he is "good enough."

**Session ID:** e44987e0

---

## 2026-04-12T21:29:00Z — Wes Kao Frameworks (spawned via consult-notebook agent)

**Query:**
I'm helping a Sr. EM named James who is building two agentic AI tools at Pinterest: Pinsight (his own, agentic rec system analysis tool, already in production) and Reflex (co-developing with Andrew Yaroshevsky, Sr. Director Product with a line to the CTO — an autonomous DS agent for recommendation quality monitoring).

Organizational dynamics:
- Allies: Andrew (Reflex co-dev, Sr. Director), Darren Regers (Director Infra, staffing Pinsight contributors, great at managing up his chain), Brian Lee (EM Growth, AI forum host), Dylan Wang (James's Sr. Director manager, peak trust), Dhruvil (peer Sr. EM, coalition partner)
- Competitive threat: Roberto (Sr. EM under Kurchi, built Search Debugger/Replay celebrated by Jeff VP, expanding into agentic eval tooling that overlaps with Pinsight, not responding to collaboration outreach, interrupted James's pitch at a meeting)
- Structural tension: Roberto reports to Kurchi (Sr. Director SSJ), who is structurally adversarial to Dylan's org. The Roberto-James competition is partly a proxy for Dylan-vs-Kurchi at Director level.
- James's known pattern: under-manages-up. Defaults to reactive "+1" in leadership threads while peers initiate and frame. Needs to build visibility with Jeff (VP) and Rajat (VP) through office hours and peer-level multi-org momentum.

Three focused questions: (1) FRAMING FOR LEADERSHIP — narrative structure and framing moves for VP-level positioning; (2) NAVIGATING ROBERTO — how to handle overlap without looking territorial; (3) BUILDING VISIBILITY THROUGH ALLIES — activating Andrew, Darren, Dylan as amplifiers.

**Response:**
To elevate James from a tactical engineer to a strategic AI leader, he must shed his reactive "+1" habits and proactively manage the narrative.

1. FRAMING FOR LEADERSHIP: From "Cool Tools" to "Org-Wide Capability"
Sales, Not Logistics: VPs don't care about architecture until sold on business value. Spend 90% pitching how tools accelerate the business, 10% on how they work. Answer the #1 Business Case Question / "Bad Things / Good Things": Every business case must answer "How will this save money or make money?" Frame Pinsight/Reflex through Bad Things / Good Things — what bad things happen without them (lost engineering hours, missed incidents), what good things with them (automated anomaly detection, recovered system velocity). BLUF and The 3A Pyramid Principle: Answer first, arguments second, add-ons last. Start right before getting eaten by the bear — cut irrelevant backstory, start at highest business impact. Make Assertions, Not Just Observations: Formulate Assertions instead of being "+1" guy. "Based on X, I recommend Y across the org. If we don't, we risk Z."

2. NAVIGATING ROBERTO: Strategy vs. Self-Expression
Strategy is optimizing for VP buy-in and organizational clarity; self-expression is complaining or trying to prove Roberto wrong. Address the MOO (Most Obvious Objection) proactively — leadership will notice the overlap, James must address it before Roberto can weaponize it. Avoid Incepting Negative Ideas — never say "we aren't trying to step on Roberto's toes" — this plants the negative. Use "At the Same Time" (not "but") to differentiate: "Roberto's Search Debugger is fantastic for Search-specific evaluation. At the same time, Pinsight is purpose-built for the unique scale and latency requirements of RecSys. Together, they give us comprehensive coverage across both surfaces." Address the QBQ (Question Behind the Question) — Jeff's QBQ is "Are my two orgs wasting headcount building the same thing?" Frame tools as complementary; act like an owner who cares about company resources.

3. BUILDING VISIBILITY THROUGH ALLIES: Reduce Their Cognitive Load
Don't expect allies to figure out how to advocate — give them the exact narratives to carry upward. Frame 90% Around the Other Person. For Darren: "Your org gets the visibility it deserves for accelerating RecSys velocity — here's a 3-bullet update, would you drop this in your next sync with Jeff?" For Andrew: "Reflex will drastically reduce manual quality monitoring for your PMs — here's a slide on ROI you can use in your next CTO review." OAV (Observe, Assert, Validate) for Dylan: "Observe: Jeff is pushing for AI evaluation tooling across the board. Assert: I recommend we position Pinsight and Reflex as the default RecSys standards in Q3 to own the narrative before Search expands. I've prepared a 2-page BLUF memo on our AI ROI. Validate: Does it make sense for you to circulate this at the upcoming Sr. Director sync?"

**Session ID:** b4a0d58b


---

## 2026-04-20T00:00:00Z — Coaching Patterns (spawned via consult-notebook agent)

**Query:**
James Li is a Sr. Engineering Manager (Di DISC profile, high-ambition, Director-track) preparing for a career progression conversation with his manager Dylan. SITUATION: He just sat in a meeting where his peer (Dhruvil) visibly "asked for things" from the manager — resource alignment, team leverage — and James didn't. James is now internally comparing himself to Dhruvil, wondering "what about myself?", questioning whether he's sabotaging his career by not thinking about org setup, and feeling uncertain how his AI impact work translates to promotion. He has a hard deadline conversation with Dylan in ~6 weeks (5/30 cutoff). Prior feedback from Dylan: "Director-level impact but emotional tax too high — I can't put you in rooms with VPs if you might explode."

Four questions asked:
1. STATUS SENSOR / COMPARISON PATTERNS — status-sensor activation, peer comparison loop, healthy vs. spiral comparison
2. RUMINATION VS. REAL STRATEGIC GAP — coaching framework for distinguishing genuine strategic blind spots from anxiety-driven catastrophizing
3. CENTERED AMBITION VS. APPROVAL-SEEKING — pre-conversation practice to shift out of reactive mode into grounded ambition
4. ASKING FOR FEEDBACK WITHOUT READING AS INSECURE — gap-closure feedback posture, over-explanation pattern, low-heat executive presence

**Response:**
Q1 — STATUS SENSOR: Notebook identifies "status sensor" activation where "I feel low status" instantly converts to "I AM low status" with zero gap. Prescribes DIJM framework (Describe, Interpret, Judge, Manage) + Tool 8 "Signal, not truth": Name it ("status sensor is firing"), locate it physically, redirect fuel within 10 min. Treat anxiety as energy, point it at internal scoreboard.

Q2 — RUMINATION: Apply Rumination Framework — "What do I actually know right now? Everything else is creative writing." Run Module 1 fear-setting exercise (Deconstructing the Catastrophic Default). Shift from "victimhood/validation" to "what story am I telling myself vs. what if there's another story?" Identify what's within control, translate to strategic action plan.

Q3 — CENTERED AMBITION: Module 3 Reframing Status — stop pretending he doesn't have high status need; reframe from human worth measure to utilitarian leverage tool. Module 4 "Impact Over Approval" Audit. Pre-conversation practice: Tai Chi Base (Tool 4) — visualize inner foundation before interaction. Self-Worth Pie Chart — expand identity anchors beyond work performance.

Q4 — FEEDBACK POSTURE: "Rambling Index" named explicitly — rambling scales with anxiety. Smart Brevity as counter. Primary pattern: "Boring Consistency > Catalytic Clarity" (low-heat, steady light, zero defensiveness). Three-Beat Managing Up: (1) share what's hardest about landscape, (2) show crushing it despite constraints, (3) enlist Dylan's help on specific unblockers. Ask open questions ("What does success look like?"), then "Authentic talking less" — ask, look her in the eye, smile, stay silent.

**Session ID:** 6937ec90

---

## 2026-04-20T00:30:00Z — Wes Kao Frameworks (spawned via consult-notebook agent)

**Query:**
Context: James is a Senior Engineering Manager (M17, 20 direct reports, Director-track) at Pinterest preparing a career-path conversation with his Senior Director Dylan before early June 2026. This is NOT a "promote me to Director" ask. It is a "here's the non-traditional path I want to build — is there a destination for it here?" ask. James wants to lead his team to build an AI multiplier on the recsys platform via agentic AI, with a small pod of 3-5 engineers added (not 10-20 more). He will end up at ~25 reports — below Pinterest's typical Director scope of 30-40. His load-bearing claim: AI multiplier makes effective output equivalent to a 30-40 person team without it.

Key Dylan context: CD DISC profile. De-charges heavy asks reflexively. Autonomy = love language. Evaluates based on "adds or subtracts from her cognitive load." Won't make peer comparisons public. She accepted the career conversation by reframing it as "quarterly regular conversation" — deliberately de-charging it. She has said "very happy James is leaning into AI, haven't seen that from some of my other folks under me... but everyone is excited by different things." She has been actively unblocking James (on-call capacity yes, escalating infra delays, shielding from low-value convos). She's asked about burnout twice in one week.

Q1. Dylan de-charged the career ask to "quarterly regular conversation." What REGISTER should James match — light-touch to mirror her framing, or deliberate/weighty to re-signal importance? How does he get the rubric ask answered without over-weighting the conversation and adding cognitive load?

Q2. What is the exec-presence, POV-forward OPENING SENTENCE for this conversation? James wants to articulate the non-traditional path (AI-native builder-leader, retrieval platform, team AI-fluency) without it sounding like a promotion ask or a strategy monologue. Give one concrete candidate opening sentence.

Q3. How should James pre-empt a potential "honestly Pinterest isn't ready for that as a Director path" response without sounding defensive? What is the frame that acknowledges org reality while keeping the question honest and forward-looking?

Q4. How does James land the "AI multiplier as effective scope" claim so memorably that Dylan can REPEAT IT UPWARD to Rajat and Jeff in calibration? What makes a claim of this kind sticky and repeatable by the sponsor?

Q5. Dylan's "everyone is excited by different things, which is fine" line — what is she signaling about what she will and won't do publicly? How should James position his ask given that ceiling?

**Response:**
FAILED — mcp__notebooklm__ask_question tool was unavailable at call time. Auth state: cookie-based auth requires manual browser extraction (notebooklm-mcp-auth --file mode). Chrome remote debugging port 9222 was also unavailable. MCP call was NOT made. No synthesis generated.

**Session ID:** N/A — call not completed

---

## 2026-04-21T00:00:00Z — Coaching Patterns (spawned via consult-notebook agent)

**Query:**
James is a Senior Engineering Manager at Pinterest, M17, Director-track (Di DISC profile). He worked through a status-sensor/comparison pattern yesterday, then received uniformly positive signals today from director Dylan (public technical lead designation, vision endorsement, career conversation accepted, Sr Staff MLE assigned to project, shielded from low-value work). Yet worry persists. "I don't know what I'm worried about, to be honest."

Six questions posed:
Q1. Why does worry not dissipate after working through the status-sensor pattern AND receiving positive signals? Mechanism and practice.
Q2. How does James hold Dylan's "everyone is excited by different things, which is fine" structurally — she won't publicly rank him above peers. What move, what language?
Q3. Signal vs. commitment gap (warm endorsement but no "I'm putting you up for Director"). How to hold that gap without rumination fuel?
Q4. Dylan flagged burnout concern twice in one week — care, warning, structural signal, all three? What does this mean for the next 4-5 weeks?
Q5. Concrete emotional-prep practice across 4-5 weeks before the career conversation, given that "walking in with the Dhruvil loop active will bleed through regardless of words."
Q6. What does James DO in the moment when a positive signal arrives, to make it land on the internal scoreboard without waiting for the sensor's approval?

Notebook: Coaching Patterns (05132ad9-3803-472e-b917-42f8bf301782)

**Response:**
TOOL CALL FAILED — mcp__notebooklm__ask_question returned "No such tool available" despite notebooklm-mcp server showing Connected status in `claude mcp list`. Auth was refreshed via `notebooklm-mcp-auth` immediately prior. Tool is not exposed in the spawned agent's tool namespace. This is a tool-availability failure, not a content failure.

**Session ID:** N/A — call did not complete

**Action taken:** Returning ERROR string per failsafe protocol. Main session should escalate to direct MCP query in primary Leo context where tool namespace may differ.
