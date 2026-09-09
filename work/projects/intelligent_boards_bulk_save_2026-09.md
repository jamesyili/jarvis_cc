# Intelligent Boards bulk saves: the discussion and James's response

Private working record for James and Leo. Captured September 8, 2026, Pacific time; updated through Michael's final acceptance reported by James. Includes two source photos, James's views, technical reasoning, and sensitive relationship analysis. The earlier public draft below is superseded. No new reply from James has been reported and Leo has sent nothing to the participants.

## Current recommendation

**Let the exchange stand; do not post the earlier corrective reply.** While this document was being written, Michael supplied a concrete negative dogfood experience, Andrew clarified the metadata proposal and explicitly allowed tuning, and Michael closed with: "Yup. Makes sense. I missed the ‘additional metadata’ suggestion" (reported by James; his exact punctuation is preserved in the continuation transcript below).

The shared ground now on record is distinguishable bulk repins, the option to treat them differently, and the ability to tune their influence. Andrew still prefers the bolder baseline and describes different treatment as optional rather than required. This is not agreement on how much calibration must precede a pinner test, a final weight, or a launch decision. Michael's acceptance settles the conversational misunderstanding; it does not establish product success.

James's substantive concerns remain useful inputs to experiment scoping, especially recovery: Michael reports needing more than a week of deliberate feed interaction to get out of "pool mode." That is a concrete reported example of effortful recovery, while abandonment remains a hypothesis. Let the owners carry the implementation and test design. James's next contribution is a decision or clarification they need from him, not another public restatement while the exchange has just closed. No acknowledgment is required to preserve his position.

## Earlier public reply — superseded by the thread's resolution; not sent

> Andrew, I want to preserve that immediate response too. Keeping the current behavior as a dogfood baseline makes sense, and I'm comfortable with bulk-save metadata if the downstream systems can use it to distinguish these actions.
>
> We will still need to calibrate the impact, particularly through user sequences. Saving a generated board expresses different intent from individually choosing every pin, so we need to be able to tune how much influence it has.
>
> I'd also include whether pinners understand and welcome the feed change, and can easily correct it if they don't, in what we test. We don't yet know how they'll respond to this degree of change. That will tell us how to carry the responsiveness you're describing into the pinner experience.

The draft would have accepted a test baseline, not a launch decision or a prediction that the current strength is right. Its technical requirement remains relevant: an attribute that never reaches the sequence construction/model path cannot enable a change there. Its conversational purpose has now largely been served by Andrew's clarification and Michael's response.

If a later decision would remove the ability to distinguish/adjust the action, or convert the strong baseline into a launch default without a pinner read, James can address that specific decision: "I'm comfortable testing the strong response. I want to make sure we retain the ability to distinguish and adjust these saves, and agree on what would tell us the response is too strong." That is a conditional future line, not a DM to send now. Any resulting decision should come back to the working group.

## Andrew and the relationship context

Andrew is **Andrew Yaroshevsky, Sr. Director of Product**, an important sponsor and collaborator on James's Anticipation and Reflex work. He helped take the anticipation vision to CTO Matt Madrigal and has built Reflex himself. He is personally invested in a responsive, meaningfully different Pinterest. It would be inaccurate to read him as an unfamiliar PM making a casual suggestion about an unrelated system.

Relevant dated evidence from his [stakeholder profile](../people/stakeholders.md#9-andrew-yaroshevsky--sr-director-of-product):

- **July 9, H1 peer feedback:** Andrew called James one of Pinterest's strongest ML leaders and explicitly supported his continued growth. He praised James's product sense and judgment, and his willingness to speak up and have crucial conversations. His growth feedback was greater patience and appreciation for partners with different profiles and strengths. The [original feedback](../../self/writing_style/aspirational_writing_style.md#1-verbatim-sample--h1-2026-mid-year-peer-feedback) is the primary source, stronger than a paraphrased relationship label.
- **July 20, SM/SL staffing discussion:** Andrew explicitly endorsed James's framing of technical co-ownership and disagree-and-commit; Andrew and Lily thanked him for ownership in front of Dylan and Michael. Direct judgment and constructive partnership have coexisted successfully in this relationship.
- **August 25, anticipation group DM:** Andrew called pUIC the main bet of the anticipation effort and pressed for acceleration. This is a recent example of his strong investment in the program and its pace. The private DM is context for James, not material to quote into this public thread.
- **August 27, org announcement:** the ATG PM team moved under Andrew, with UPP and Anticipation Cupcake named among the reasons his remit was a fit. His scope and importance across these efforts have grown.

The current [Exceeds campaign](../career/exceeds_h2_2026_campaign.md) emphasizes landed results and leaders who can represent the organization with sound judgment. A patient, specific disagreement is consistent with that. February's harsher tone feedback is historical context, not evidence that James remains under a current sanction or that one disagreement will derail his career. Andrew's later written endorsement must travel with the growth feedback.

Michael Weissinger, who agrees with James in the thread, is the PM Director with whom James worked closely at Snap. His agreement adds a real product perspective to the discussion. It should not be converted into a public coalition against Andrew. Anna Kiyantseva is the Anna named in this thread; her exact role is not established in the available profile. Do not conflate her with another Anna in the relationship records.

## What the public intervention does

**Observed:** the photo shows a thread in **#p13n-all**. Andrew's reply is preceded by Slack's **"Also sent to the channel"** label. His message follows several responses expressing concern or agreeing with James. His opening is "wanted to chime in before we throw the baby with the water." He describes the current effect as valuable, warns about quarters of integration/calibration work, states "We can't afford that," prefers the current effect as a baseline, and offers metadata as the alternative. The exact audience/readership is unknown.

James reports that he finds the tone pushy and dislikes it. That is his firsthand reaction, not an inferred emotion supplied by Leo. There is textual support for reading the message as forceful: the opener recasts the accumulating concerns as potentially discarding something valuable, and the timeline language raises the stakes of choosing another path. Broadcasting the reply gives that framing a wider audience. None of this establishes a hostile motive toward James.

Several readings can coexist:

| Reading | Weight from this evidence | Why it remains live |
|---|---|---|
| Protecting the product effect | Strongest | Andrew describes the immediate experience at length and ties it directly to Anticipation. He may think the group is about to normalize away the very thing the project is trying to produce. |
| Avoiding an integration dependency | Strong | His explicit objection is the possibility of the IB team chasing other teams for quarters. Metadata is his proposed way to retain the working path. The feared cost has not been measured in this record. |
| Publicly steering the group after concern starts to converge | Plausible and consequential | His seniority, timing, directive language, and channel broadcast can make the preferred direction feel more settled to readers. This is an effect of the intervention; deliberate embarrassment or dominance is not established. |
| Personally rebuking James or withdrawing support | Weakly supported | The message contains no personal criticism, acknowledges uncertainty, agrees to experiment, and offers a technical accommodation. The broader relationship record includes explicit support for James's judgment and constructive disagreement. |

Before the continuation, a concise public reply acknowledging the immediate product effect and stating the differentiation requirement was appropriate. **After the continuation, the recommendation changes:** Andrew explicitly says they are not disagreeing, permits tuning, and Michael accepts the clarification. The personal-rebuke reading has still less support. Andrew's preference for the bold baseline remains clear, but the thread does not need another participant to restate the resolved representation point. James already expressed his concern publicly; leaving the closing exchange alone does not erase it or imply he endorses every implementation choice.

The relevant communication reminder is [Pattern 7 in work/communication.md](../communication.md#pattern-7-landing-a-question-with-edge-d88-calibration): a valid technical point can land as deflation when the room is excited. Here the specific acknowledgment is the value of an immediate response; the purpose is learning how to make that work for pinners. No invented positive data or performative praise is needed.

**Boundary on the career read:** the credible concern is frustration leaking into a public reply and reinforcing the already-documented patience feedback. The screenshot does not show a career threat. Andrew has positively valued James speaking up. There is no evidence here that silence is required to preserve his support, and no assurance that any wording eliminates all relationship risk.

## Technical and product reasoning from the discussion

### Calibration and differentiation

James's central point is that user sequences are too strong a signal to treat a new action as settled merely because existing pipelines consume it. Andrew's approach may save initial integration work. It does not establish that the inherited influence is appropriate. The distinction is between getting an action into the system and establishing how the system should interpret it.

A pinner selecting twenty pins has expressed preferences through twenty choices. Accepting a generated board is one collection-level choice, potentially without inspecting all of its contents. It is useful evidence of interest, but its specificity differs. If a board with fifty pins produces a stronger feed shift than the same concept represented by ten pins, part of the apparent preference strength may come from how the product constructs the board. This is a mechanism to investigate, not a measured dose-response curve.

Metadata and a separate event type are alternative representations. Either could preserve the distinction if it survives into the relevant consumers and can change their treatment. Merely logging a flag does not prove that sequence construction, models, or other consumers use it. The requirement is differentiation that enables control. The cheapest implementation is not established here.

There is also a potential feedback mechanism: the system selects the board's pins, a pinner accepts the collection, and those contents are then treated as item-level endorsements. This could amplify the original selection as though it were more specific user feedback than it was. Collection acceptance is still informative; the argument is for interpreting it at the appropriate granularity, not discarding it.

The current strong response could win a test. "Calibration is necessary" does not imply that every model must be redesigned before a dogfood experiment or that the effect must be weakened. It means the team needs to evaluate and be able to adjust the treatment rather than assume that inherited repin semantics are right. James's "we save nothing" is strongest when narrowed to **the calibration obligation is not removed**; there could still be integration savings.

### User expectations and recovery

Andrew knows what caused his feed change and welcomes it. An ordinary pinner may believe they saved a collection for later, then encounter a substantially different Homefeed without understanding the connection. The same shift can feel like responsiveness to one person and a malfunction to another. Andrew's experience establishes that the positive reaction is possible, not its prevalence. He explicitly acknowledges that limit.

Some pinners may already expect saves to influence recommendations. The sharper concern is whether they expect **this magnitude and duration** of change from one bulk action, and whether they can easily correct it. A generic statement that saves influence recommendations would not necessarily communicate that magnitude.

James says users have no way to reverse the effect. Pinterest's public [Refine your recommendations](https://help.pinterest.com/en/article/tune-your-home-feed) page, checked September 8, documents board-level controls. It does not establish whether those controls are available and effective for this IB flow, whether they reverse historical user-sequence effects, or how quickly they act. The accurate requirement is a **discoverable and effective way back**. Do not assert either that the current implementation has one or that Pinterest has no recommendation controls.

The continuation adds **one concrete reported outcome**: Michael says his pool-board save dominated Explore and Homefeed, reduced diversity, and took more than a week of active feed interaction to recover from. That is evidence of a burdensome experience for one internal user, not a measured population effect. Confusion among ordinary pinners, reduced return behavior, and abandonment remain risks rather than demonstrated outcomes. Another plausible outcome is reduced willingness to explore: if trying one new interest overwhelms established recommendations, a pinner may avoid trying new interests. Conversely, making a strong change understandable and reversible could make people more willing to accept it. User control can support the more responsive product experience Andrew wants.

### What a useful experiment would resolve

The current dogfood experience is a candidate baseline, not proof of a desirable pinner default. A useful comparison would help choose the degree and persistence of the response, establish whether pinners welcome it, and test whether they can correct unwanted effects. The specific treatments, cohort, timing, and owners are work-side decisions not captured here.

Subsequent voluntary engagement and return behavior matter; repins mechanically created by the bulk action itself do not establish satisfaction. Where feasible, examine the affected users and different bulk-save sizes rather than relying only on a whole-population average. These are Leo recommendations, not experiment requirements already ratified by James or the team.

## James's statements in this conversation

After the first analysis, James said:

> There are two things I disagree with about what Andrew said:
> 1. No matter what we do we have to calibrate this. We have to tune this. The user sequence is just too strong a signal for us to ignore and not calibrate and tune. I don't think we end up saving anything. Being able to differentiate the actions is really the key thing here.
> 2. Also there’s also there's no way for users to know this is the type of impact they could get from the current action and once they know, there's no way to reverse that. For someone who doesn't have intimate knowledge of how their home fee recommendations work, users might just abandon the app altogether because they're confused.
>
> But what do you think? Think this through deeply

James then requested this dedicated file and made the political context explicit:

> I think this is an important enough thread that deserves its own .md file. Let's put the original transcription, as well as your reasoning and the thinking from this discussion, into that.
>
> Now do you know who Andrew is? I want to make sure you actually looked up Andrew and understand the whole context behind all of this as you're replying here, because again it's a politically sensitive topic. The fact that he's making a public showing of it is something that I want to make sure we capture as part of this response.
>
> I also don't like his tone. He is being very pushy in a way that I don't agree with. I don't think this is actually going to work in the way that he thinks it will but I also don't have data either, right? Given how important this is I want to make sure we can respond in a way that doesn't derail my career basically. He is an important stakeholder after all.

The dictated "home fee" is interpreted as Homefeed in analysis; the quoted input is preserved. James's skepticism is a prior he explicitly distinguishes from data. His reaction to the tone is recorded without converting it into a finding about Andrew's intent.

## Original Slack thread — partial transcription from the photo

This is a best-effort transcription, not a Slack export. Line wrapping is normalized. Wording is retained where readable, including awkward grammar. `[clipped]` means text leaves the photo; `[unclear]` marks text that cannot be read reliably; bracketed explanations are editorial. Hyperlink labels are retained where readable, but their destinations are unavailable. Emoji, reactions, and most interface controls are omitted. Two photos were supplied by James; the second makes parts of Andrew's original reply clearer. No image copy is stored in the repository. Other windows and sidebar conversations in the second photo are outside this task and are not transcribed.

### Emun Solomon — Today at 12:19 PM

> HF/explore page drastically homogenize upon IB Save
>
> Collecting a thread here to chat through our findings and next steps. First,
>
> 1. Saving an Intelligent board should count as recent user activity that influences UICs + other exploratory content. However it should be a balanced impact more reflective of all a users interests.
> 2. Unclear currently if a high volume of similar activity is reinforcing one existing cluster or making all the users clusters the same.
>
> Next questions to answer:
>
> @Roderick Gao and @Yutong Jin today confirmed filtering Save action out when IB fetching UIC GSS signal will affect UIC generation for other products like Exploratory Module / Explore Page.
>
> - Do we know how this impacts homefeed ?
> - @Sufyan Suliman [name spelling partly unclear] Do you know what's the timeline for dynamic UIC experiment?
> - Is there some benefit to each indiv event being recorded and passed vs grouping all of them to one (and applying some normalizing coefficient). This informs at which level in the bulk-Save journey we can handle this
>
> Cc @James Li @Anna Kiyantseva @Yan Chen (edited)

**Reading caution:** "confirmed filtering ... will affect" does not establish that a filter is deployed. Leo's first summary over-compressed this into an existing filtering state; that interpretation is withdrawn. The sentence's exact intended dependency remains unclear without the underlying technical discussion.

### James Li — Today at 12:30 PM

> Hi @Emun Solomon, thanks so much for posting about this. I actually have a concern about the bulk saves from an IB being passed in as a bunch of Repin events. As we know, the intentionality and specificity of a repin really matters when it comes to the pinner experience. So when it's bulk imported [clipped]
> this, it may dilutes a lot of the user's intentionality.
>
> For a prerequisite for a AB test, we might consider having a separate event used for this action rather than the actual repin event. I say this because similar efforts have happened in the past with the new NUX experience work, and there were a lot of learnings around what's truly a repin versus not.
>
> cc @Yan Li (P13N) @Balaji Rengarajan (He Him) @Michael Weissinger (edited)

### Balaji Rengarajan — automated out-of-office reply, Today at 12:30 PM

> I'm out of office until Tue, Sep 22. See [coverage link partially unreadable] for my coverage doc.

### James Li — Today at 12:31 PM

> [Quoting:] Do we know how this impacts homefeed ?
>
> A bulk import of 20 repins will impact homefeed recommendations a lot, and the impact is not just through UIC signal but also through user sequence signals that the ranking and retrieval models heavily [unclear word(s)] upon.
>
> This is another reason I would not suggest we treat this event as automatic bulk repin events. (edited)

### Laura Neves — Today at 12:44 PM

> + @Akshanta [surname unclear] @Edward Zhuang as FYI

### Anna Kiyantseva — Today at 1:07 PM

> Can I ask that we also generalize whatever solution we come up with so that similar, non-pinner initiated bulk save use cases such as meal planner, board creation via assistant, etc. can also leverage it?

### James Li — Today at 1:46 PM

> Yup agreed on the generalization of the solution. @Emun Solomon curious what are the next steps?
>
> 1. Do we need a PRD versus finding the right Eng POC to scope out switching over to a new event?
> 2. Curious what the timing looks like for the current IB sprint, sharing of the results, and plans and ETAs for the AB?

### Michael Weissinger — 34 minutes ago

> Thanks for starting the thread, @Emun Solomon. (I personally had this issue with IBs.) I agree with @James Li and @Anna Kiyantseva's thoughts above, as well.

### Andrew Yaroshevsky — 6 minutes ago

[Visible UI label immediately above his reply: **Also sent to the channel**.]

> Hey crew – wanted to chime in before we throw the baby with the water.
>
> After dogfooding I actually feel there is some real beauty in what's happening after I save my IB. My Pinterest changes drastically – and it feels like a new Pinterest to me, pretty fast, with minimal effort. It really makes me feel like I have new reasons to open the app now – because it's not stale anymore
> Previously, as @Mira [surname unclear] (She/Her) formulated well – I could easily predict what I will see; and it gets boring. Nuances aside – the spirit is exactly what we want to do with Anticipation.
>
> The fact that when I save the IB and it adds a BMI to my top nav and changes my Pinterest in homefeed out of the box is actually pretty amazing. Imagine if it was another signal, the IB team would have to chase Retrieval / Ranking / etc teams for quarters to integrate and calibrate it before we see any meaningful impact on pinners HF. We can't afford that.
>
> I acknowledge my story could be not representative and pinners might actually react differently to such a dramatic change. I agree we need to experiment, but I would like to flip the script and have a bolder, more aggressive treatment be the default one as a baseline.
>
> So instead of changing this action to something else – let's just save additional metadata indicate that it came as a 'bulk save', so that we can test treating this metadata differently than a regular re-pin in the stack. (edited)

The baseline sentence above was initially marked unclear; the second photo makes it readable. Andrew explicitly calls for a "bolder, more aggressive treatment" as the default baseline. This still does not establish a pinner-launch decision. The top-nav acronym appears as "BMI"; its expansion is not established here.

## Thread continuation — second photo and James's final update

### Michael Weissinger — 3 minutes ago in the second photo

> @Andrew Yaroshevsky – just a counter to your IB experience, I saved my Backyard Pool IB, and proceeded to see my Explore page dominated by pool modules only, and so was my home feed. It's taken me more than a week of active investment in interacting with my feed to get out of 'pool mode'.
> Totally open to the idea of IBs changing your feed, but at least in my case it actually reduced my feed diversity – which I don't think is the product intent. If not a new signal for saving IBs, perhaps there are ways to experiment putting less emphasis on the Nth save in the last N seconds? (edited)

Michael embeds an earlier message and a screen-recording thumbnail. The recording itself was not viewed. Visible quoted message:

> Hi Edward – is there anything I can do from my end to clear and/or flush this set of interests? I'm still seeing mostly small backyard pool exploratory modules, although today I promisingly got a shoes cluster.

The embedded thread label identifies **#explore-page-mvp**, **Aug 28**. The exact recording filename is omitted. This adds a dated prior report to Michael's current description; it is not an independent second user's experience.

### Andrew Yaroshevsky — Just now in the second photo

> We are not disagreeing. As I wrote in my last paragraph – if we save an additional "flag" with those bulk re-pins (like, "this re-pin came as an IB save"), then we create optionality (rather than a requirement) to treat these bulk saves differently. Then we can tune how much the HF should be discounting those saves. But we're starting with the bolder baseline and working backwards from that, rather than other way around. Does it make sense? (edited)

The typing indicator at the bottom says Michael Weissinger is typing. James initially asks whether to wait for the exchange to settle, then supplies the closing reply:

### Michael's final reply — quoted by James, not shown in the photos

> Yup. Makes sense. I missed the “additional metadata” suggestion

**Evidence limit:** this is Michael accepting Andrew's clarification. It does not retract his pool-mode experience, establish that either treatment works for typical pinners, or bind James to a technical design. It does establish a natural conversational stopping point.

## How the reasoning changed

1. **Initial Leo response:** identified the distinction between immediate responsiveness and strength of inferred preference; recommended accepting metadata while requiring downstream consumers to use it. This was technically useful but reconciled the disagreement too quickly and underweighted the public stakeholder setting.
2. **After James's two objections:** separated potential integration savings from unavoidable evaluation/calibration, distinguished a collection-level acceptance from many individual choices, added the expectation/recovery problem and the possibility of discouraging exploration. Qualified claims about zero savings, literal irreversibility, and abandonment. Suggested retaining the strong response as a test candidate, not a proven default.
3. **After James foregrounded the political stakes:** returned to Andrew's original feedback, recent program involvement, and the public broadcast. Replaced the earlier "I do disagree" draft with a shorter reply preserving the technical point without inviting a public technical correction contest.
4. **After Michael's counterexample, Andrew's clarification, and Michael's acceptance:** the draft itself is superseded. Recommend letting the exchange stand. Distinguish the conversational resolution from the still-open product/calibration choices; retain Michael's burdensome-recovery evidence for experiment scoping.

Leo had read Andrew's stakeholder profile before the first answer. That was insufficient: the recommendation did not give enough weight to the existing relationship and the public effect of the message. This is a failure to apply retrieved context, not an absence of the person's record.

## What remains unknown

- Whether the metadata already exists, where it propagates, and which consumers could act on it.
- The actual scope/cost of using metadata versus a separate event, and the current meaning/deployment state of the UIC filtering discussed in the opener.
- The effect size, persistence, and distribution of the feed shift, and the experience of representative pinners rather than internal dogfood users.
- Whether existing board controls reverse this IB effect through the relevant pipelines and are understandable/discoverable to pinners.
- The agreed experiment, decision owner, engineering owner, timeline, and any later thread messages beyond Michael's closing reply reported by James.

These are evidence limits for this discussion, not a new task list assigned to James. No claim about a launch, experimental result, Andrew's private intent, or a career consequence is established by the photo.

## References and provenance

- Two user-supplied Slack photos and James's statements in this conversation, transcribed above. Attachments viewed directly; automated OCR was unavailable, so uncertain text stays marked rather than reconstructed. Michael's closing acceptance comes from James's explicit quote.
- [Andrew's profile and dated interactions](../people/stakeholders.md#9-andrew-yaroshevsky--sr-director-of-product); [original July peer feedback](../../self/writing_style/aspirational_writing_style.md#1-verbatim-sample--h1-2026-mid-year-peer-feedback).
- [Work communication patterns](../communication.md), especially Pattern 7; [coaching record](../coaching.md), used for response discipline rather than to diagnose James's reaction.
- [Current Exceeds campaign](../career/exceeds_h2_2026_campaign.md), for present career context rather than relying solely on historical feedback.
- [Pinterest recommendation controls](https://help.pinterest.com/en/article/tune-your-home-feed), read September 8. Public documentation is not evidence of this internal IB implementation.

No NotebookLM consultation has been run for this thread. The analysis above is Leo's synthesis of the source, the conversation, and the cited context.
