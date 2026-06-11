# Michael Truell — The rise of Cursor: The $300M ARR AI tool that engineers can't stop using
*Theme: ai-practical | Extracted: 2026-04-04*

## Custom model stack powering every magic Cursor moment

Lenny Rachitsky (00:32:05):
What is the most counterintuitive thing you've learned so far about building Cursor, building AI products?

Michael Truell (00:32:11):
I think one thing that's been counterintuitive for us, [inaudible 00:32:14] added a little bit before, but is, we definitely didn't expect to be doing any of our own model development when we started. As mentioned, when we got into this, there were companies that were immediately from the get-go going and just focusing on training model from scratch. And we had done the calculation for what it to train before, and just knew that that was not [inaudible 00:32:36] going to be able to do. And also felt a bit like focusing one's attention in the wrong area, because there were lots of amazing models out there, and why develop all this work to replicate what other players had done. Especially on the pre-training side of things, taking a neural network that knows nothing, and then teaching it the whole internet.

And so we thought we weren't going to be doing that at all, and it seems clear to us from the start that the existing models, there were lots of things that they could be doing for us that they weren't doing, because there wasn't the right tool built for them. In fact though, we do a ton of model development, and internally, it's a big focus for us on the hiring front, and have assembled a fantastic team there.

And it's also been a big win on the product quality side of things for us. And at this point, every magic moment in Cursor involves a custom model in some way. So that was definitely counterintuitive, and surprising, and it's been a gradual thing, where there was an initial use case for training our own model, where it really didn't make sense to use any of the biggest foundation models. That was incredibly successful, moved to another use case that worked really well, and had been going from there. And one of the helpful things in doing this sort of model development is picking your spots carefully, not trying to reinvent the wheel, not trying to focus on places, and maybe where the best foundation models are excellent, but instead kind of focusing on their weaknesses, and how you can complement them.

Lenny Rachitsky (00:34:05):
I think this is going to be surprising to a lot of people hearing that you have your own models. When people talk about Cursor and all the folks in the space, they would kind of call them GPT wrappers, they're just sitting on top of ChatGPT or Sonnet. What you're saying is that you have your own models, talk about just the stack behind the scenes.

Michael Truell (00:34:21):
Yeah, of course. So we definitely use the biggest foundation models a bunch of different ways, they're really important components of bringing the Cursor experience to people. The places where we use our own models, so sometimes it's to survey a use case that a foundation model wouldn't be able to serve at all for cost or speed reasons. And so one example of that is the autocomplete side of things. And so this can be a little bit tricky for people who don't code to understand, but code is this weird form of work, where sometimes, really, the next 5, 10, 20, 30 minutes of your work is entirely predictable from looking over your shoulder.

And I would contrast this with writing. So writing, lots of people are familiar with Gmail's autocomplete, and the different forms of autocomplete that show up when you're trying to post text messages, or emails, or things like that. They can only be so helpful, because often, it's just really not clear what you're going to be writing just by looking at what you've written before. But in code sometimes, when you edit a part of a code base, you're going to need to change things, and in other parts of code base, and it's entirely clear how you're going to need to change things.

So one core part of Cursor is this really suit to autocomplete experience, where you predict the next set of that you're going to be doing across multiple files, across multiple places within a file. And making models good at that use case, one, there's a speed component of, those models need to be really fast, they need to give you a completion within 300 milliseconds. There's also this cost component of, we're running tons, and tons, and tons of molecules, every keystroke, we need to be changing our prediction for what you're going to do next. And then it's also this really specialty use case of, you need models that are really good, not at completing the next token, just a generic tech sequence, but are really good at autocompleting a series of diffs, looking at what's changed within a code base, and then creating the next set of things that are going to change, both deleted and added and all of that, and we found a ton of success in training models specifically for that task.

So that's a place where no foundation models are involved, it's kind of our own thing. We don't have a lot of labeling or branding about this in the app, power is a very core part of Cursor. And then another set of places where a user own models are to help things like Sonnet, or Gemini, or GPT, and those sit both on the inputs of those big models, and on the output. On the input side of things, those models are searching throughout a code base, try to figure out the parts of a code base to show to one of these big models. You can kind of think about this as a mini Google search that's specifically built for finding the relevant parts of the code base to show one of these big models.

And then on the output side of things, we take the sketches of the changes that these models are suggesting, you make with that code base. And then we have models that then fill in the details of, the high level thinking is done by the smartest models, they spend a few tokens on doing that, and then these smaller specialty incredibly fast models, coupled with some inference tricks, then take those high level changes and turn them actually into full code diffs. And so it's been super helpful for pushing on quality in places where you need a specialty task, and it's been super helpful for pushing on speed, which is such an important dimension of product quality for us too.

---

## How to actually use AI coding tools well

Lenny Rachitsky (00:46:15):
I want to come back to Cursor. A question I like to ask everyone that's building a tool like this, if you could sit next to every new user that uses Cursor for the first time, just whisper a couple tips in their ear to be more successful, most successful with Cursor, what would be 1 or 2 tips?

Michael Truell (00:46:32):
I think right now, and we'd want to fix this at a product level, a lot of being successful with Cursor is kind of having a taste for what the models can do, both what complexity of a task they can handle, and how much you need to specify things to that model, but having a taste for the quality of the model, and where its gaps exist, and what it can do and what it can't. And right now, we don't do a good job in the product of educating people around that, and maybe giving people some swim lanes, giving people some guidelines.

But to develop that taste, would give two tips. So one is, as mentioned before, would bias less toward, trying in one go to tell the model, "Hey, here's exactly what I want you to do." Then seeing the output, and then either being disappointed or accepting the entire thing for an entire big task. Instead what I would do is I would chop things up into bits, and you can spend basically the same amount of time specifying things overall, but chopped up more. So you're specifying a little bit, you're getting a little bit of work, you're specifying a little bit, getting a little bit of work, and not doing as much the, "Let's write a giant thing telling the model exactly what to do." I think that will be a little bit of a recipe for disaster right now.

And so biasing toward chopping things up. At the same time, and it might make sense to do this on a side project and not on your professional work, I would encourage people to, especially developers who are used to existing workflows for building software, I would encourage people to explicitly try to fall on their face, and try to discover the limits of what these models can do by being ambitious in a safe environment, like perhaps a side project, and trying to kind of go around town, use AI to the fullest. Because a lot of the time, we run into people who haven't given the AI yet a fair shake, and are underestimating its abilities. So generally biasing towards chopping things up and making things smaller, but to discover the limits of what you can do there, explicitly just try to go for broke in a safe environment, and get a taste for... You might be surprised in some of the places where the model doesn't break.

Lenny Rachitsky (00:48:45):
What I'm essentially hearing is build a gut feeling of what the model can do, and how far it can take an idea versus just kind of guiding it along. And I bet that you need to rebuild this gut every time there's a new model launch, when it's on... I don't know, 4.0 comes out, you have to do this again. Is that generally right?

Michael Truell (00:49:04):
Yes. For the past few years, it hasn't been as big as I think the first experience people have had with some of these big models. This is also a problem we would hope to solve much better just for users, and take the burden off of them. But each of these things have slightly different quirks and different personalities.

---

## Junior vs. senior engineer AI anti-patterns

Lenny Rachitsky (00:49:26):
Along these lines, something that people are always debating tools like Cursor, are they more helpful to junior engineers, or are they more helpful to senior engineers? Do they make senior engineers 10X better? Do they make junior engineers more like senior engineers? Who do you think benefits most today from Cursor?

Michael Truell (00:49:43):
I think across the board. Both of these cohorts benefit in big ways. It's a little hard to say on the relative ranking. I will say, they fall into different anti-patterns. The junior engineers we see going a little too wholesale, relying on AI for everything, and we're not yet in a place where you can kind of do that end-to-end on a professional tool, working with tens, hundreds of other people within a long-lived code base. And then the senior engineers... For many folks, it's not true for all, and we actually often... One of the ways these tools are adopted is, there's developer experience teams within companies, often those are staffed by incredibly senior people, because often, those are people who are building tools to make the rest of the engineers within an organization more productive.

And we've seen some very, very boundary pushing kind of... We've seen people who are on the front lines of really trying to adopt the technology as much as possible there. But by and large, I would say on average, as a group, the senior engineers underrate what AI can do for them, and stick to their existing workflows. And so the relative ranking is a little hard, I think they fall into different anti-patterns, but they both, by and large, yet get big benefits with these tools.

Lenny Rachitsky (01:04:04):
That makes absolute sense. I love that it's two ends of the spectrum, expect too much, don't expect enough. It's like the three bears allegory.

Michael Truell (00:51:18):
Yeah. Maybe the sort of senior, but not staff, right in the middle.

---
