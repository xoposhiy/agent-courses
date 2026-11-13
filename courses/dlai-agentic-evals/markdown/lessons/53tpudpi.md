# A Conversation Between Laurie Voss and Andrew Ng

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/53tpudpi/a-conversation-between-laurie-voss-and-andrew-ng) · [Raw file](../../raw/lessons/53tpudpi.html)

Retrieved: 2026-11-13T17:26:04.689813+00:00

[00:00] Welcome to Evaluating and Improving Agentic Applications,

[00:03] built in partnership with Arize AI and taught by Laurie Voss,

[00:07] who is their Head of Developer Relations.

[00:10] As AI capabilities continue to advance, there are

[00:13] a lot of wonderful applications that we can all build.

[00:16] But I've seen among a lot of teams

[00:19] that when you start out building a new application,

[00:22] often by using quick, iterative tactics,

[00:24] you can get it to some okay level of performance.

[00:28] But then to break through to a higher level of performance,

[00:31] to make something production ready,

[00:33] requires a disciplined, evals-driven

[00:36] method of development.

[00:38] And so, knowing how to build evals and when to put them into place

[00:42] is a key skill for not just building prototypes,

[00:45] but going beyond that to building high-performing AI systems

[00:49] and building high-performing AI agents.

[00:52] And Arize AI has been one of the leading teams

[00:55] on how to do that well.

[00:57] Thanks for inviting me to the course.

[00:59] Now, despite the importance of evals,

[01:03] one thing I often see is many teams will hold off building evals

[01:06] longer than I think would be ideal for that.

[01:09] So Laurie, why do you think that's the case?

[01:12] Well, as you can imagine, we've done some user research on

[01:15] people building evals and what holds them back, and

[01:19] the primary thing holding people back is just knowing where to get started.

[01:22] Anybody who knows what an eval is knows that they're valuable,

[01:26] They're basically tests,

[01:29] and the argument for robust testing test suites in software

[01:32] has been a very long one and very thoroughly made.

[01:35] Nobody's arguing that you don't need tests.

[01:38] The challenge is how to do them at all

[01:40] and then how to do them well.

[01:42] They're quite different from deterministic tests that people are used to.

[01:44] They also come with a lot of baggage from the traditional ML world

[01:47] in terms of terminology that can make them

[01:49] quite intimidating to get started with.

[01:51] So one of my hopes for this course

[01:53] is that we'll be able to blow through

[01:55] the language barrier and get people into the mindset

[01:57] that these are just a new kind of logging, a new kind of testing,

[02:01] and that getting them right takes some new skills, but fundamentally

[02:04] isn't rocket science. Just like testing, getting your evals right

[02:07] can be fun, and then watching your application hill climb

[02:10] as you put a good definition of good in place

[02:14] is really a fun thing to watch.

[02:19] Yeah. I found that one of the

[02:21] most challenging things about working on evals

[02:24] is, um, it's very stage-dependent.

[02:26] So, I've definitely heard some people talk

[02:28] about, "Build rigorous evals with very large datasets,

[02:31] very large golden datasets, um...

[02:33] And there are also fast moving teams

[02:35] that go, "You know what? With Generative AI,

[02:38] you can just change a prompt, add a RAG module,

[02:40] change the context, and very iteratively

[02:43] make quick changes to your system."

[02:45] And I find that when building applications,

[02:48] the most experienced teams will often use

[02:50] the fast iterative methods with very casual evals

[02:53] where you just kind of look at it, see if it works.

[02:56] and that inspires what to change next.

[02:58] But that works best only for the early stages of a project,

[03:01] and then as a project matures you start to

[03:03] get a more systematic understanding of what are the things that

[03:06] are really hard to solve. Like,

[03:08] is your customer service chatbot

[03:10] sometimes pulling up the wrong numbers, so let's evaluate that.

[03:13] Or is the portion for deciding when to offer a return

[03:17] having bad judgments on when to say yes

[03:19] or when to say no. If so, then

[03:21] maybe we need a more rigorous evals for that.

[03:23] There's this gradual process of going from

[03:26] casual look at it to see if it works type of evals

[03:29] to gradually, incrementally more rigorous evals

[03:32] using a range of tactics and measuring performance

[03:34] on a range of different dimensions. And so

[03:37] getting that feel right of when to go

[03:40] really fast and casual

[03:42] to gradually evolve to something really rigorous,

[03:45] is difficult unless you know how to do things at both ends of the spectrum

[03:49] and when to move along that spectrum.

[03:52] Absolutely. One of the things that we're going to be covering in this course

[03:56] is the evolution from the

[03:59] basic stages of observability, where

[04:02] you're just reading traces one by one and applying your human judgment

[04:06] to what went wrong specifically and building your first evals,

[04:09] to being much more systematic about it, doing it at much greater scale,

[04:13] and, as you say, uh, turning it into a machine that does evals

[04:18] rather than a human process that does them one by one.

[04:22] Yeah, I think it's a good insight. I think, um,

[04:25] evals are a reflection of what the developer

[04:28] or human preferences are for what is good versus bad,

[04:32] and is often itself an iterative process

[04:36] to get the evals to be that accurate reflection.

[04:39] So often I think about how to evaluate the evals, or eval the evals,

[04:43] um, to figure out when to tune them or when to...

[04:46] improve them in some dimension.

[04:48] Absolutely. And so, one of the things that you'll learn in this course is

[04:51] to test whether an agent does what you need it to do,

[04:55] identify where the changes are needed, and check whether those changes improve its performance,

[04:59] and you're going to put that into practice in hands-on labs.

[05:03] So, what we're going to do is we're going to

[05:05] start by looking at what the agent actually did,

[05:06] using records of its activity, those

[05:10] Traces let you see how it handled the task,

[05:13] including which tools it called and what happened at each step.

[05:16] From there, we'll be able to work out what good performance means for your application

[05:21] and build cases that test it.

[05:23] As you review the results, you'll look for recurring failures

[05:26] and identify situations your tests don't yet cover.

[05:29] Then, you'll learn how to automate those evaluations using code

[05:33] or an LLM-as-a-judge

[05:35] and check how reliably those evaluators work.

[05:38] That gives you a way to test changes and see whether they actually help.

[05:41] And you'll keep that process going after deployment,

[05:44] using what you learn from real users

[05:46] to improve both your agent and your evaluations.

[05:49] And I think it's been interesting watching how the practice of evals has

[05:53] evolved even in the last

[05:55] half year or year.

[05:57] One thing I know that both you and Arize AI co-founder

[06:02] Aparna Dhinakaran have been excited about

[06:05] is having AI agents help with part of this work.

[06:08] I feel like a few years ago we built evals,

[06:10] and then the human engineer would keep on coming up with ways

[06:13] to hill climb on that evals.

[06:15] And now we can, a little bit, have AI agents come up with ways

[06:18] to hill climb on that evals, and that's been exciting.

[06:21] And then the other trend that feels early

[06:23] and flaky and unreliable and needs lots of steering,

[06:25] is to then have AI agents also try to figure out what

[06:29] goes wrong, to fit that into the evals.

[06:33] And times I've tried to do this, you know, results were unreliable,

[06:37] and it'd need a lot of human steering to still insert that

[06:40] human context, that understanding of the hypotheses anyone comes up with,

[06:43] reading the agentic traces, what might be good and what might be bad.

[06:48] But I feel like this disciplined, evals-driven development loop

[06:52] still feels like the core of how to build reliable applications,

[06:56] but gradually, maybe you and I can get

[06:58] agents to help us execute parts of this loop.

[07:00] And I think that's very exciting.

[07:02] Absolutely. I think, as you said, the difference

[07:04] between a year ago or even six months ago

[07:07] is really stark in how effective the agents

[07:10] can be at doing this kind of

[07:13] closed-loop, automatic improvement of software.

[07:16] Every week, a new model comes out, and every time we try them,

[07:20] they are getting better and better at this process.

[07:22] So it's a really exciting time to be working in evals.

[07:26] Yeah, and having said that, I'm confident that evals is still

[07:29] an important human skill to learn, as opposed to an agent skill for...

[07:33] agent execute.

[07:35] Because the process of evals is fundamentally aligning

[07:38] the criteria of optimizing with the human preferences.

[07:42] And usually, the coding agent has no idea what the human prefers.

[07:47] And so that human, the developer, you, have a context advantage

[07:51] over the agents, and

[07:53] until and unless you find a way to give that context to the agent,

[07:57] which we now do by helping shape the evals,

[08:01] it's not possible to take the human out of the loop,

[08:03] which is why this is a human skill, not just

[08:06] an agent skill, to know how to do evals.

[08:08] Absolutely. The way I always put it

[08:10] is that you have the definition of

[08:12] good in your head, and

[08:14] unless you get it out of your head,

[08:16] the agent is never going to know what it is.

[08:18] So, putting that definition of good,

[08:21] making it as expansive as possible, making it as detailed as possible,

[08:23] making it as precise as possible,

[08:26] is really where

[08:28] the human value comes into evals.

[08:31] That's just a great way for me to end.

[08:33] So, knowing how to build and use evals

[08:37] is a key skill of AI engineering.

[08:40] I hope you enjoy the course

[08:42] and that you use these skills to build many exciting AI applications.

[08:46] Let's go on to the next video

[08:48] and put your agents to the test.
