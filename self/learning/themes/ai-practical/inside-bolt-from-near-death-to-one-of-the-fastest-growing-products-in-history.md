# Eric Simons — Inside Bolt: From near-death to one of the fastest-growing products in history
*Theme: ai-practical | Extracted: 2026-04-05*

## Claude Sonnet was the zero-to-one moment that made AI coding viable

Lenny Rachitsky (01:06:29):
This is a potentially new job, for now at least, just unstuck the AI. Which I think over time, it'll get better and better, and we maybe won't need these people. But I love that it's now AI first, and person second. Versus person building the thing, and then AI. Like when Copilot launched, it was just like, "Cool, here's a little suggestion for this function," and now it's flipped. "Here's everything." And then, "Oh, I don't know what to do here. Help us here." And then, it's like a human suggestion. Isn't that interesting? It's like, human Copilot is flipping it.

Eric Simons (01:06:58):
Totally. Yeah. That's what's wild is, I think Sonnet was really the first model that flipped the equation, because that was really us, and old Cursor, and all these other things. The rapid growth started the second Sonnet went online. We actually tried building Bolt almost exactly a year ago, with the frontier models at the time. Spent a week or two building it. It just didn't work. The output, the code output was not reliable enough. It would constantly, it would be a broken app, or it would look ugly, or whatever. And then we got a sneak peek of the Sonnet stuff in May and we were like, "Oh. Okay, we should take that project back off the shelf and green line it, because this might be it."

And lo and behold, that's exactly what has happened. But yeah, that's the big deal that is, kind of under the hood, this is... What's going on here is, a very critical threshold has been passed with LLM's ability to write production grade code and apps that actually look beautiful, and actually function well. It's not perfect, but there's kind of this zero to one moment that's happened where it's like, "Okay, so now, yeah. Now the AI is the first thing," and then you're kind of popping a developer in every now and then, versus the other way around.

Lenny Rachitsky (01:08:11):
I did not know that. I didn't realize that so much of this was unlocked with, like it's sitting on top of Anthropix work, and specifically Sonnet. That was the first model, you're saying, that could code well enough.

Eric Simons (01:08:22):
Yeah, zero question.

Lenny Rachitsky (01:08:24):
Wow.

Eric Simons (01:08:25):
Zero question. Absolutely.

Lenny Rachitsky (01:08:25):
That is fascinating. Just the amount of, I don't know, revenue and business and ecommerce that that one model has unlocked, is insane. I did not realize that.

Eric Simons (01:08:39):
It is. And in retrospect, I'd mentioned, we'd never done an AI product at StackBlitz, and it's tempting. Like when of ChatGPT went online, everyone started adding AI to their products. We just didn't see a clear place for a really added value. So I was not super bullish on, you know, a lot of people were like, "AGI is going to be here in 2023." You know what I mean? There's all this stuff that was being said, and I was like, "I just don't know if I necessarily buy how fast people say that it's going to move." And to a certain degree, that was the correct view.

What I didn't really think about though, is if AI, if LLMs are going to get better at a specific vertical, which are going to be the things that it would be. And if you look at law, for example, you want to make the best LLM for looking at case law. The problem with that stuff is, it's not deterministic. The judge's ruling is dependent on society's view of things at a time, political stuff going on, the jury. There's a ton of things, that it's not deterministic. And so you can't really create a lot of training data that's going to be super reliable, and produce really good results.

Software is deterministic. When you write code and you hit run, it either runs or it doesn't. And that's the key insight Anthropic really had. They just went deep. And then, this is what they're doing, is just reinforcement learning on basically permutating every type of app you could ever build, and just spinning up tens of thousands of cores or whatever to do that. Just building tons of training data, and doing reinforcement learning, and making their LLMs the best in the world at building beautiful, reliable applications. I'm extremely bullish. It makes technical sense why, of anything, LLMs are going to get insanely better at writing code than probably most other types of applications for LLMs. Simply because it's something that can be extremely deterministic, and permutated thousands and thousands and thousands of times per second.

---

## WebContainer: browser-based compute as the architectural differentiator

Lenny Rachitsky (00:10:41):
Let's get to a demo of Bolt, so people can actually see what this looks like in action. And as you go through it, if you can even point out stuff that is different from other products in the space, say Lovable, VZERO, Replit, that other folks have heard about, that'd be useful.

Eric Simons (00:10:57):
Awesome. Cool. Yeah, so this is Bolt, you just go to bolt.new. Things that I think are really interesting about Bolt. One is, it's just dead simple. Whether you're logged in or logged out, it's the same UI, it's extremely simple, it's just a text box. And I think that the biggest difference between Bolt and the other stuff out there, it's actually subtle. It's not like something you'd necessarily see in the UI, but it's how fast it is, and how reliable it is.

And this is because of how we are actually doing the compute, because what's going on here is when you type into, whether it's Bolt or another product, it has to spin up a dev environment to actually make that application. So there needs to be some operating system somewhere that's running it. Everyone else runs those things on cloud servers, which those can take minutes to boot up, and they often will run into issues, and then you can end up literally stuck and have to contact support to get it done, and get it unstuck.

With Bolt, and for the past seven years, what our company's been doing has been building an operating system that runs inside of your browser locally, using your CPU. So we have a very permissive free tier, and it's insanely fast, and it's insanely reliable.

So if I want to, just as a quick example of this say, "Make a clone of Spotify," and just hit enter. This thing's already getting to work, and already, on the right here, this is a full dev environment. This is an actual operating system, running inside of my browser. And I can run commands on it, et cetera. And really, what you're seeing down here, this terminal and kind of what's backing it, this is what took us really five, six, seven years to build, and make so reliable. There would not be a Bolt without this technology called WebContainer, that allows us to run an operating system in the browser.

Because what's going on here is, our AI agent for Bolt has bidirectional communication with this operating system. It's writing code, it's running the dev server for this thing, it's going to go ahead and spin this up. You can see how fast this is, in a matter of 60 seconds I said, "Make me a Spotify clone," and now we have one. And it looks pretty darn good.

Lenny Rachitsky (00:12:55):
That looks really good.

Eric Simons (00:12:58):
And that's one of the other aspects around Bolt is, this technology we made for the operating system side, the guys that have been working with us for the past five-plus years on it, before this they were actually doing machine learning AI stuff. And so when it came time to write the agent for Bolt, we had just an incredible amount of in-house expertise on how to actually merge these two different technology sets, to have this really reliable experience that produces really beautiful, really functional stuff.

---

## 67% of Bolt users are non-developers — PMs best positioned to use AI tools

Lenny Rachitsky (00:52:24):
So what would you say are the major limitations of Bolt today, where people should just know, "Okay, it's not going to get you here yet. Maybe in the future it will."

Eric Simons (00:52:39):
I would say that's probably the main one, because I think if you have a large existing code base, you're going to need something like Cursor. And you're going to need to be a developer, meaningfully, to be editing that stuff. I think outside of that, there's a, just like using any other productivity tool, like Photoshop or Figma, or like a DSLR or whatever. There's some level of education, and using the tool, and learning how to use it, that's required to really unlock a lot of the maximum capabilities of the thing.

And the people that we see that are most successful with Bolt, outside of developers, the people we see that are most successful are people that are amazing PMs, for example. Because these are people that understand enough about how the technology works, typically, and their job is to direct developers on how to go and improve the product. And go and look into how to actually spec this thing out in a way that's executable, without lossiness in the communication. And when you think about, "Okay, how would you best interact with an AI developer agent?" It's basically that. You really want to be good at defining scope, and helping it go and debug various things, or whatever have you. There's a huge overlap of the skill set of being a rock star PM, and being really good at using, frankly, any of these text to apps or Cogen tools.

Lenny Rachitsky (01:04:08):
I love that you made that point. That's exactly the point I've been trying to make, I have a newsletter post about this. Because when all these tools came out, there was so many people saying, "Okay, PMs are dead. We don't need them anymore. We can just build things so quickly and easily, what's the point?" But I completely see the world the way you see it. The hard part now is, now it's easy to build the thing. Now it's, "What the hell should we build? Can we clearly articulate what it is we want to build?" And then, "Can we just have the taste to know, is this right, is this correct? Is this good? Is this going to solve the problem?" And then it's like, grow it, which is something also PMs think about. So, I completely agree. Basically it feels like PMs are, and a lot of PMs listen to this, so they'll love hearing this. To me, it feels like PMs are the best positioned role to thrive in this world.

Eric Simons (00:54:54):
Zero question. I mean that was, as Bolt was growing and we were like... Because we were a developer product before this, and so we expected the audience to be 100% developers that were using this. And we just kept seeing more and more and more people that were not developers using it, to the point where it's like, 67% of our users are not developers, at this point. And when I started talking to these folks, at first I was just weird, or whatever. It was like, "Well, what's going on here?" But then it just kind of clicked as like, "Oh, well, this is going to change everything. The entire software world order is going to get rewritten, here."

Because the way that companies are organized to build software today, totally going to change. The idea that again, PMs are the people that really understand, to the pixel level, what matters into making a great product experience. And often they're having... And listen, I'm a developer, myself. They have to go and harangue the developers to get things to be how they really ought to be, to the smallest levels. And now, how this is going to work, if you fast-forward one, two, five years, whatever. PMs, they're going to be "writing code", quote, unquote, instead of just writing a JIRA ticket and waiting for a developer to do it. The developers are going to be able to work on intellectually challenging tasks that LLMs are not well suited for, and still being augmented by LLMs to do it. But PMs are going to be able to go in and just make the changes themselves.

---
