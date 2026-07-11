# Hamel Husain & Shreya Shankar — Why AI evals are the hottest new skill for product builders
*Theme: decision-making | Extracted: 2026-04-04*

## Binary scoring and the benevolent dictator principle

Lenny Rachitsky (00:25:17):
Cool. Another term that you used in your posts that I love and that fits into this step is this idea of a benevolent dictator. Maybe just talk about what that is, and maybe, Shreya, cover that.

Shreya Shankar (00:25:27):
Yeah, so Hamel actually came up with this term.

Lenny Rachitsky (00:25:29):
Okay, maybe Hamel cover that, actually.

Hamel Husain (00:25:41):
No problem. And we'll actually show the LLM automation in this example, because we're going to take this example, we're going to go all the way through.

And so benevolent dictator is just a catchy term for the fact that when you're doing this open coding, a lot of teams get bogged down in having a committee do this. And for a lot of situations, that's wholly unnecessary. People get really uncomfortable with, "Okay, we want everybody on board. We want everybody involved," so on and so forth. You need to cut through the noise. And a lot of organizations, if you look really deeply, especially small, medium-sized companies, you can appoint one person whose tastes that you trust. And you can do this with a small number of people and often one person, and it's really important to make this tractable. You don't want to make this process so expensive that you can't do it. You're going to lose out.

So that's the idea behind benevolent dictator, is, "Hey, you need to simplify this across as many dimensions as you can." Another thing that we'll talk about later is when it goes to building an LLM as a judge, you need a binary score. You don't want to think about, "Is this like a 1, 2, 3, 4, 5?" Like, assign a score to it. You can't. That's going to slow it down.

Lenny Rachitsky (00:26:59):
Just to make sure this benevolent dictator point is really clear, basically, this is the person that does this note-taking, and ideally they're the expert on the stuff. So if it's law stuff, maybe there's a legal person that owns this, it could be a product manager. Give us advice on who this person should be?

Hamel Husain (00:27:16):
Yeah. It should be the person with domain expertise. So in this case, it would be the person who understands the business of leasing, apartment leasing, and has context to understand if this makes sense. It's always a domain expert, like you said. Okay. For legal, it would be a law person. For mental health, it would be the mental health expert, whether that's a psychiatrist or someone else.

Lenny Rachitsky (00:27:41):
Cool.

Hamel Husain (00:27:42):
Though oftentimes, it is the product manager.

Lenny Rachitsky (00:27:44):
Cool. So the advice here is pick that person. It may not feel so super fair that they're the one in charge and they're the dictator, but they're benevolent. It's going to be okay.

Hamel Husain (00:27:52):
Yeah. It's going to be okay. It's not perfection. You're just trying to make progress and get signal quickly so you have an idea of what to work on because it can become infinitely expensive if you're not careful.

---
