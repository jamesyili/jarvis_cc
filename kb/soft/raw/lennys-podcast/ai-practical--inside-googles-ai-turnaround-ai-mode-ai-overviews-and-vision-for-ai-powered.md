# Robby Stein — Inside Google's AI turnaround: AI Mode, AI Overviews, and vision for AI-powered search
*Theme: ai-practical | Extracted: 2026-04-05*

## AI Mode architecture: query fan-out, real-time data, and search-native design

Lenny Rachitsky (00:09:45): And along the same lines, you guys recently launched AI Mode, which I don't think enough people are talking about. Talk about just what people should know about AI Mode, maybe what they don't really understand about the power of this thing.

Robby Stein (00:10:31): I can tell you there's three big components to how we can think about AI search and the next generation of search experiences. One is obviously AI Overviews, which are the quick and fast AI you get at the top of the page many people have seen, and that's obviously been something growing very, very quickly. This is when you ask a natural question, you just put it into Google, you get this AI now, it's really helpful for people.

The second is around multimodal. This is visual search and lens. That's the other big piece. You go to the camera in the Google app and that's seeing a bunch of growth. And then really with AI Mode, it really brings it all together. It creates an end-to-end frontier search experience on state-of-the-art models to really truly let you ask anything of Google search.

One of the cool things that I think it does is it's able to understand all of this incredibly rich information that's within Google. There's 50 billion products in the Google shopping graph, for instance. They're updated 2 billion times an hour by merchants with live prices. You have 250 million places in maps. You have all of the finance information, and not to mention, you have the entire context of the web and how to connect to it so that you can get context but then go deeper.

Lenny Rachitsky (00:17:45): It's interesting your point about how it goes in searches. When you use it, it's searching a thousand pages or something like that. Is that just a different core mechanic to how other popular chatbots work?

Robby Stein (00:18:00): Yeah. This is something that we've done uniquely for our AI. It obviously has the ability to use parametric memory and thinking and reasoning and all the things a model does, but one of the things that makes it unique for designing it specifically for informational tasks, we wanted to be the best at informational needs, that's what's Google's all about, and so how does it find information? How does it know if information is right? How does it check its work? These are all things that we built into the model, and so there is a unique access to Google. Obviously, it's part of Google search, so it's Google search signals everything from spam, what's content that could be spam? And we don't want to probably use in a response all the way to, wow, this is the most authoritative helpful piece of information. We're going to link to it and we're going to explain, hey, according to this website, check out that information and then you're going to go probably go see that yourself. That's how we've thought about designing this.

---

## AI products becoming easier to steer with natural language — less fine-tuning needed

Lenny Rachitsky (00:18:51): You've worked on a lot of AI products at this point, and it's not just Google or Artifact and Instagram, you did a lot of AI stuff. What's something you've learned about building AI products that you find maybe people don't truly understand, maybe something that's surprised you by building successful AI products?

Robby Stein (00:19:07): I think the most recent one, and this is true, something even within the last week or two, is that it's so obvious how human-like the interface is becoming with how you can communicate and steer AI. I think it used to be even just months back that you had to do a lot of work to get the AI to do the thing you're trying to get it to do, right? You had to do these incantations, you had to prompt in a really specific way. People would have all these hacks like, "Hey, act like you're a coach and you do these things," and you have to really push it, or to use a tool more on the technical side. You had to do post-training, you had to take this foundational model and you had to show it data, you had to train it and actually update its weights to do more sophisticated things.

Tell it, "Hey, here's documentation for an API. If you ever have a problem, ping this API. Here's the data," as if it's an engineer that you had that you could talk to and it would have no idea what to do with that, or it would have some idea and wouldn't really do it.

But increasingly, you can just use language. Almost if you were to write up an order, you could be like, "Wow, I'm a new startup. Here's my data internally. Here are the APIs to it. Here's the schema and the URL. Here's when to use it. By the way, make sure that if you get this kind of a question, you really make sure to get it right." And that'll end up doing a lot in the model.

The model's been now encoded to be able to say, "Okay, I'm going to use more reasoning or thinking budget for that kind of a question." Or, "I'm going to use tools or code, use code execution in order to connect to this API I'm told about." That's a relatively new thing. So I think it's going to open up a lot of this democratization of accessing these models and building incredible things because you don't even need to do a lot. To get the most sophisticated outcomes increasingly, I don't think you need to do a lot of this heavy duty fine-tuning.

---
