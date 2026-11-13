# A Conversation with Aparna Dhinakaran, Co-founder of Arize AI

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/mo0gyiw/a-conversation-with-aparna-dhinakaran%2C-co-founder-of-arize-ai) · [Raw file](../../raw/lessons/mo0gyiw.html)

Retrieved: 2026-11-13T17:26:07.708936+00:00

[00:00] Hey Aparna, welcome to the course.

[00:02] Why don't you introduce yourself to the audience

[00:04] and let everybody know who you are?

[00:06] Awesome. Hey everyone, my name's Aparna.

[00:09] I'm one of the founders of Arize,

[00:11] I've been in the evals and observability category

[00:15] for many years now, and it's a

[00:17] deeply exciting category to be a part of.

[00:19] Cool. So, one of the challenges we had

[00:22] putting this course together is that

[00:24] coding agents are advancing so quickly,

[00:26] a lot of stuff that used to be manual effort

[00:28] is now something that you'd ask an agent to do.

[00:30] What's not in that category?

[00:32] Where is human judgment indispensable?

[00:34] That's a great question. I mean, on one hand I think that

[00:37] if you're still doing things the way that you were doing them last year,

[00:41] Yeah, that's probably not the right thing.

[00:43] Um, but I also think that there's,

[00:45] you know, human judgment and

[00:48] being able to discern what is really good and bad

[00:52] for your business, for your use case,

[00:54] is still something that we really, truly need domain expertise to do.

[00:58] So I think some of the best things that we've seen

[01:01] AI engineers or AI PMs do today is take that judgment

[01:05] and use that to define what really good evals

[01:09] or what data even needs to be traced and observed

[01:12] in order to write those evals.

[01:15] Cool. So, a related

[01:17] question to that is you've said in the past

[01:19] that agents are now capable of coming up with evals themselves,

[01:22] uh, but we also say that, as you just said,

[01:25] domain experts are a huge part of evals.

[01:28] Let's let's square those up. Where do you

[01:30] think that an agent can help, uh, put an eval together,

[01:34] and where's the line where the domain expert needs to get involved?

[01:37] Yeah, uh, great great question. I mean,

[01:40] So, first and foremost, I think,

[01:43] you know, there was a lot of, there's just a lot of

[01:47] traces and telemetry data that is being emitted right now.

[01:51] You have agents that are all being traced.

[01:54] You have agents that now review those traces.

[01:57] You probably have agents that are reviewing those agents on top of it.

[02:01] And so the volume of telemetry that is being,

[02:03] you know, just collected right now is massive.

[02:06] And I just don't think,

[02:08] you know, observability five years ago, ten years ago used to be

[02:11] humans looking at dashboards

[02:13] and looking at metrics and logs.

[02:16] You know, there's just the volume of data has grown to a point where,

[02:19] and maybe it was always, you know, such a great use case for agents,

[02:22] is that you're going to have agents running through those traces.

[02:25] And what they're going to be really good at doing is figuring out patterns

[02:27] of what are types of questions that your users are asking, what are questions

[02:32] or common types of errors that are occurring for your user experience.

[02:37] And what agents can really do is identify

[02:39] categories of things that might be

[02:42] even beyond the categories of what you might have thought

[02:45] evals should contain.

[02:48] So, they're probably really good at figuring out

[02:50] the unknown unknowns.

[02:53] And so what I think is a really great balance between the two right now

[02:56] is, one, you, you know, as

[02:59] the human judgment's really great at figuring out what do you want the end-user

[03:02] experience to be for the product or the agent that you're actually building?

[03:06] What do you want it to be doing? And so there's probably a core set of

[03:09] do you want them to leave feeling less frustrated? Do you want them to

[03:13] kind of reach an outcome

[03:16] of the use case that they're building towards.

[03:19] And that's a great set to get an initial set of evals going.

[03:23] What you can also do with these agents crawling your traces

[03:26] is figure out what are a whole other, you know, types of behaviors and signals

[03:30] that you can gather from the traces to figure out new types of evals.

[03:34] And then, how do you continuously improve those evals so it's not just a,

[03:38] you know, one-shot approach? You're kind of continuously refining that

[03:41] based off of human judgment and the new traces that you're getting is

[03:45] kind of a great way to kind of use them both—the human judgment and the agents—

[03:50] to build better evals. I think one of the things that's also changed a lot

[03:54] is our perception of the data sets.

[03:57] You probably agree with this too, is

[03:59] even 2 years ago we were spending a lot of

[04:01] time figuring out the right way to prompt things.

[04:03] It probably doesn't matter anymore.

[04:05] And so you can probably have the agent write

[04:08] a way better prompt for the evals,

[04:12] define a way better task for other agents

[04:15] than you probably will at this point.

[04:18] And so, it's crazy to think, but really it is comes down to taste.

[04:21] Can you

[04:23] define what good and bad is

[04:25] and help the agent learn that from your judgment.

[04:29] One of the ways that I've seen it expressed is

[04:31] that humans now have to operate at a higher level,

[04:35] a higher level of abstraction on top of a loop

[04:37] that you've built for your evals.

[04:39] Would you say that's a fair summary?

[04:41] I think that's a great way of putting it. It's, you know, at first

[04:45] engineers were writing very, very low-level code,

[04:49] and then there was abstraction languages on top of that.

[04:51] And now, you know, engineers don't even code. They write prompts.

[04:54] And now it's like, you're not even prompting individual eval templates.

[04:59] You're probably prompting how do you have these agents that keep

[05:01] those eval templates up to date, and so there's there's levels to this.

[05:05] So, one thing I've heard you talk a lot about is the coming of

[05:08] agents as judges instead of LLMs as judges.

[05:12] How is an agent as a judge different from an LLM as a judge?

[05:15] Why do we need agents as judges? That's a

[05:18] Good question. Um,

[05:20] so I think what we realized was that,

[05:24] you know, we had spent years of individuals

[05:27] who were building, let's say,

[05:29] slightly less complex applications or agents,

[05:33] where this is kind of a decade of

[05:36] more and more autonomy in the agents that are being built.

[05:40] And so, LLM as judges I think

[05:44] And to be honest, they're still really useful today as well, but they're

[05:47] really great for evaluating the quality of the outputs.

[05:51] But where they tend to have gaps is

[05:55] understanding the entire journey that it took, or the entire trajectory

[06:00] that it often took, in order to debug an application.

[06:04] And, ultimately,

[06:06] how do you then suggest improvements

[06:09] or fixes? And so

[06:11] agent as a judge is, think about it

[06:13] as instead of a single prompt evaluating

[06:16] the outputs of these agents, it is an entire

[06:19] agent evaluating the outputs of another agent.

[06:22] And so here, it can adapt its

[06:25] criteria, it can modify how deep

[06:29] it needs to go in order to get more information to

[06:32] properly evaluate the quality of the output. And then it

[06:36] can be, of course, kicked off, it can kick off either other

[06:39] agents or kick itself off to go and put up improvements

[06:43] to fix

[06:44] the the issues that it had detected. And so,

[06:48] agent as a judge feels like an evolution of

[06:51] having these judges become more autonomous

[06:54] in the way that they evaluate other agents and

[06:57] kind of giving them a way to also

[07:00] close the loop and start improving the agents.

[07:02] What are some of the failure modes for agentic judges

[07:06] that somebody putting them together can be cautious of?

[07:09] Because obviously, you're talking about the frontier of evals,

[07:11] and not everything's going to go perfectly.

[07:14] I mean, I don't know if you think about this this way, Laurie,

[07:16] but sometimes

[07:18] There's just like a slop loop

[07:20] that ends up getting created

[07:23] where there's one piece of slop and then it just kind of snowballs.

[07:26] And, you know, it's the one thing that I think about

[07:29] where human intervention and human judgment ends up becoming really important,

[07:33] so that the evals and how you're thinking about quality kind of stay—

[07:39] You know, they have to evolve. I don't think it's a one-shot type of process,

[07:42] but I think they kind of have to...

[07:44] you need to give it nudges so that

[07:47] it doesn't go you know down

[07:49] and think something's really an issue when it quite might not be.

[07:53] And so that nuance is sometimes really helpful, and

[07:57] I think that that's

[07:59] it just so much again depends on the application.

[08:01] You know, we obviously have an agent built inside of our own product, AX,

[08:04] and I think we've learned a lot from

[08:06] you know, kind of dogfooding and writing evals for our own agent.

[08:10] And sometimes, you know, we realize that it can take AX

[08:13] you know, a couple different

[08:16] turns to understand ultimately what the user wants. But

[08:19] if the user's question didn't often start asking that,

[08:23] and actually their true intent was something else,

[08:26] sometimes the turns that they took was is actually fine.

[08:29] Probably would have been similar to what a human did.

[08:31] But if it took those turns even when the user was super direct,

[08:34] then then that's an issue. And so

[08:36] having that ability to figure out when

[08:38] you know, the trajectory is valid

[08:41] and when it's not, I think is is really interesting.

[08:44] Um I think we're also going to see

[08:46] a ton of, not just quality,

[08:49] you know, there's a lot of quality um

[08:52] evals that teams tend to write on

[08:55] the actual outputs of the agents, but

[08:59] I think there's deeply more and more, you know, think about it more like

[09:02] cost-type evals or safety-type evals to

[09:05] kind of consider, you know, is the output,

[09:08] uh, you know, worth the ROI that was invested?

[09:12] Speaking of agents inside of our products,

[09:15] Arize AX has Signal,

[09:17] a built-in agent that reads your traces for you

[09:20] and suggests fixes to your app, which I think we can agree is pretty cool.

[09:23] How do you see that fitting into the

[09:25] observe, benchmark, evaluate, improve workflow

[09:28] that we've been talking about in this course so far?

[09:31] I mean, I think it really is kind of just the

[09:35] future of how we're going to build these loops.

[09:38] In the beginning, there was traces that were collected,

[09:42] and humans had to go through, read those traces,

[09:45] and look and try to find where the errors are in those traces.

[09:49] Well, now you can have agents go through, and

[09:52] again, it doesn't replace the human, but it does a first pass

[09:55] to identify categories of issues and kind of—hence why we call it signal—

[09:58] find the signals within the traces.

[10:02] And, you know, I know so many of us talk about this, but

[10:05] the most important way to improve your agent, I really think, is actually

[10:08] reading your traces and understanding the telemetry.

[10:13] Even just spending and reading through five,

[10:15] six, seven traces, you start to understand—

[10:18] I feel like I end up walking away learning something

[10:20] from our own agent's traces. So,

[10:23] Signal first kind of does a bit of that heavy work

[10:26] and actually reviews the traces of your agent.

[10:29] And there's a ton of flexibility to set it up

[10:32] so if you want it to— sample, if you want it to run on a cadence,

[10:36] if you want it to run on some kind of trigger, you can essentially

[10:39] define agents to do the agentic review of the traces.

[10:43] It can surface up patterns of behavior and then

[10:47] highlight the ones that need a human's attention.

[10:51] Um, it can also, if given access to

[10:54] a repo, if given access to additional context,

[10:58] it can actually go ahead and put up a fix for the issue.

[11:01] If there's enough evidence and it feels confident about, hey, there's

[11:05] a root cause here that four or five, maybe

[11:07] 20 different traces are kind of all alluding to,

[11:09] it can go ahead and put up a fix.

[11:12] which is pretty incredible because now

[11:14] the same traces that a human had to go through,

[11:17] understand the pattern, and figure out what to go

[11:20] fix, you can kind of

[11:22] get the fix. You can then just test the fix,

[11:24] which also, of course, an agent can do, so test it,

[11:28] run the benchmark on it, make sure it didn't

[11:30] break anything,

[11:32] And so that that's a bit of how we're thinking about

[11:35] this next gen of observability is that it's no longer dependent on

[11:39] the human having to be the person who kicks off the loop

[11:43] every time.

[11:47] it can be an agent that kicks off the loop,

[11:49] and it can be a human that actually reviews,

[11:51] makes it better, and like you always say, moves a level up

[11:54] where you are now kind of the controller

[11:57] or the the augmenter of that loop,

[11:59] and so you can make it better when it puts up PRs that

[12:03] are helpful, and we've seen this.

[12:05] Like it doesn't always get it right. How do you give it feedback

[12:07] so that the agents get better?

[12:10] So now we're going to go into a little bit of a deep cut.

[12:14] You've written that

[12:15] picking the best model doesn't fix a failing agent,

[12:19] and you've split the system into model, context, harness layers.

[12:23] Walk me through that mental model. Why is that important?

[12:26] What do you get out of splitting up the model that way?

[12:30] I mean, I think I read this on X somewhere,

[12:33] someone said, you know, "If you can't get the value

[12:36] with the models we have today,

[12:38] yeah, I think it's a you problem, not the model problem."

[12:41] And I think what the person was maybe trying to say there was that

[12:45] even though the models are really powerful,

[12:48] how you actually use them,

[12:50] how do you build these loops and how do you actually use the contexts

[12:53] Yeah, I still think that those are really important engineering skills.

[12:57] There's a whole, you know, new category around harness engineering,

[12:59] context engineering.

[13:02] Um, and so when I think about

[13:04] What is the loop? And you've probably mentioned this as well, is that it's

[13:07] how do you repeatedly, you know, improve the harness,

[13:10] improve the context, or, I guess if you're a frontier lab,

[13:14] you know, improve the models. And the things that most AI engineers

[13:18] probably have within their control is the harness and the context.

[13:21] And if you're using...

[13:25] an out-of-the-box kind of harness,

[13:27] like a Claude Code or Codex or Cursor harness,

[13:31] then really it's about how do you wield the context

[13:34] that you're giving the harness in order to get the best output.

[13:37] I think it's just really helpful to think

[13:38] about it in terms of what you can control

[13:40] and what you can kind of change in order to test.

[13:45] to see if you can get better outcomes.

[13:47] We, I think, have gone through, you know, for our own agent and product, AX,

[13:50] we've actually built a harness.

[13:53] And some of the things we learned in building the harness around

[13:56] you know, giving the agent and the model access to a file

[14:00] system and CLI tooling and having it have access to

[14:03] that to do the work was just, it was, I think, some

[14:07] of the same decisions that some of the harnesses by the frontier

[14:10] labs had also gotten to. But every time we did that,

[14:13] we also, I think we tried to keep other things constant.

[14:17] Tried to keep the model constant, we tried to keep the context constant,

[14:21] and then we tested changes to the harness to be able to

[14:24] evaluate and see what really moved the needle.

[14:26] It's helpful so that you kind of can run tests

[14:30] on what changes the game for your agents.

[14:33] Speaking of which, lots of people are concerned about being locked into

[14:37] a particular harness or a specific model.

[14:40] Talk me through how evals help avoid that problem.

[14:43] Well, if you know what the performance with a frontier model and,

[14:46] you know, an out-of-the-box harness can be,

[14:49] it gives you a really good starting place to benchmark

[14:52] this is how good your agent is, and then

[14:55] is, the frontier models can be really expensive.

[14:58] So you can swap them out for open-source models

[15:01] or just lower-cost models, and then

[15:03] evaluate to make sure that

[15:06] the things that really matter, you're not

[15:08] missing out on the quality of the

[15:10] agent you're building. So,

[15:12] I think evals are

[15:15] I mean, evals are kind of the best way to

[15:17] give yourself a benchmark, and then

[15:19] kind of either decide to verify regressions,

[15:22] or it's a benchmark for you to hill climb

[15:24] and see where you can get better.

[15:26] So in this course, we got

[15:29] all the way up to production. We talked about

[15:32] taking your production traces and bringing them into your dataset,

[15:35] and improving your dataset that way. But one of the things

[15:37] that we didn't get into is post-production stuff,

[15:40] online evals, and monitoring. What are the

[15:43] big things that somebody who's just getting into

[15:46] observability and evaluations should know about

[15:49] using monitoring and dashboards to be really production-ready?

[15:55] Yeah, I

[15:56] think evals ends up being a really big term,

[16:00] and there's kind of evals you do during development

[16:03] and testing so that you can, again,

[16:06] check for regressions, hill climb, but

[16:09] I would really equally say

[16:11] evals in production are so,

[16:14] important to how you can detect

[16:16] your next set of—what are your next set of improvements

[16:19] or your next set of hills to climb.

[16:21] And so really the telemetry

[16:24] and the traces that you end up

[16:27] collecting end up being a really good way for teams

[16:31] to run online evaluations, so evals that run

[16:34] on your live production traffic and

[16:37] can be used to identify if there's common problems or

[16:41] patterns that you see from that trace, from the traces.

[16:46] You know, online evals can have an interesting thing where

[16:49] you're evaluating your known,

[16:51] problems that you'll tend to quantify.

[16:54] This is where I'm really excited about the future of agents as judges,

[16:58] so that they can find the unknown unknowns in your traces.

[17:01] Exactly. Um, but I

[17:05] might even have a hot take here, which is that

[17:08] I think that the evals you run on your traces are honestly more,

[17:12] important for AI engineers and AI PMs

[17:16] who are actually building these AI products,

[17:20] because you don't— yeah, it's just like shipping a product.

[17:23] You don't really know until it's out there in the real world

[17:26] and it's touching real users, and so you can—

[17:28] you can benchmark it all day long, but until—

[17:31] it's out there and you have real

[17:33] you know, real telemetry.

[17:35] I think you learn, you end up learning a lot more from them.

[17:38] Absolutely.

[17:40] So, let's talk about the harder side of things.

[17:44] You've obviously seen a ton of success stories of people using evals in production.

[17:47] Let's talk about some of the failures.

[17:49] What are some of the pitfalls that people new to the space fall into

[17:53] that mean they don't get to value with evals?

[17:56] That's an awesome question, actually.

[17:59] I think they see a lot of new

[18:01] folks try to write some of the most complex

[18:03] evals possible,

[18:05] so a trace eval that looks at a specific span

[18:08] in order to evaluate

[18:11] if the agent did exactly this step

[18:13] in its entire trajectory. And

[18:15] to be honest, my my honest answer is you could start simple.

[18:19] can start simple, can literally be,

[18:21] you know, a simple, is user happy, frustrated,

[18:25] or, you know, some way for you to get some signal on

[18:28] is the system working as intended or not.

[18:31] the the product KPI

[18:33] or the agent KPI, I guess, that matters, but

[18:36] um, I'd say start simple,

[18:38] and it might be that you

[18:40] actually don't want to overspecify

[18:43] and let the agents find

[18:46] as many of these unknown unknowns in your traces.

[18:49] And so I I think that's that's maybe the the thing I'd say for

[18:52] people who are starting new with evals. Cool.

[18:56] And looking ahead a little bit,

[18:59] multi-agent systems are a super hot topic.

[19:03] How does evaluation of multi-agent systems differ

[19:06] from what we've been talking about in this course?

[19:09] Oh man, that's a great question.

[19:12] It's also a topic of a lot of some of the coolest research happening right now.

[19:15] Um, I think two things. So, so one is

[19:18] the multi-agent systems again comes back down to the use cases.

[19:21] You have kind of the product KPIs that

[19:23] the end-user evals that I think about.

[19:26] I don't think those changes much whether you use

[19:29] a multi-agent system in order to deliver

[19:31] the right outcome, and so I think the quality-

[19:33] type evals

[19:36] still probably don't change that much,

[19:39] but I think the stuff that does matter

[19:41] for the people who are maybe building the harness

[19:43] or building the agent itself is, one,

[19:46] was it really more efficient to use multiple agents?

[19:50] Noam, I think, did a podcast on...

[19:53] the Dwarkesh podcast, where he was saying it's not always linear.

[19:56] And sometimes you might need to do four agents to get a 2x,

[20:00] improvement in the efficiency.

[20:02] And so, did it actually improve?

[20:04] And are the agents actually, just like humans,

[20:06] are we collaborating effectively?

[20:09] And so did they pass the information that they needed to each other?

[20:13] Were they able to self-organize,

[20:15] or did they need guidance in order to self-organize?

[20:19] And so those are all really interesting things I think about in more of the

[20:23] how did the multi-agent system ultimately arrive at the

[20:26] end result, or the answer, um, which is

[20:30] probably more interesting for the person who is actually building the system.

[20:34] uh to understand things like efficiency and coordination

[20:38] of the agents.

[20:40] Do you think the uh model capability is

[20:44] a barrier to multi-agent systems?

[20:46] Do you think we're going to see a leap forward in multi-agent systems

[20:49] as the models get better, or do you think it's more about

[20:51] the design of the multi-agent system?

[20:54] I, I mean, I think the models,

[20:57] I don't want to discount the models getting better at all

[21:00] because I think, definitely from the stuff we're reading

[21:03] and what the frontier labs are putting out there,

[21:06] I think multi-agent is on the top of everyone's mind.

[21:11] Um, which, you know, going back to your point,

[21:13] it's going to be like another layer on top. Today you are

[21:16] the controller of multiple agents. Well, now you're going to be a director

[21:19] who's controlling multiple teams of agents, and so everyone's going to get

[21:22] a promotion in terms of the layers of hierarchy.

[21:24] everyone's gonna have to move higher and higher up the stack.

[21:28] So I think the models, that I think will happen.

[21:32] The part that's still interesting to me is the harness design,

[21:36] because there is a lot of the merging of the harness and the model

[21:40] that's happened in some of the popular coding agents today.

[21:43] but I think there's a whole

[21:45] world of the open source models

[21:48] and the open source harnesses that I think we're going to see the,

[21:50] I'm excited as the ability to really

[21:54] manipulate and kind of

[21:57] build on top of the open source harnesses becomes more common.

[22:00] Mm-hmm. So, for somebody who's just finished this course,

[22:04] what's the thing they might be tempted to do

[22:06] that you'd warn them away from, like what's the

[22:09] most obvious trap that they'd fall into?

[22:12] I'd probably go back to the first, to the thing I said before,

[22:14] which is building really complex evals.

[22:17] I think starting small, you know, evals is

[22:19] a is a way to accomplishing the

[22:22] business outcome.

[22:25] product or the agent you're ultimately trying to build. And so, start simple

[22:28] and kind of expand on it as as it gets more complex.

[22:32] Cool. Looking further ahead,

[22:35] what's something that's definitely part of the world of observability and evals right now

[22:39] that you think is going to go away in the next one to two years?

[22:42] Oh, um, easily just

[22:45] the prompt testing,

[22:47] prompt iterations is-

[22:50] I don't think anyone's doing that today.

[22:52] But I do think that there's a lot of

[22:55] Yeah, still education on that.

[22:57] Um, it's just uh I think

[23:00] the way you prompt does not matter as much anymore.

[23:04] That's a really good point.

[23:06] So now, what's probably going to be your favorite question,

[23:09] is what is your spiciest take on evals?

[23:12] What's something you believe about the space that

[23:15] you think other people in the space might disagree with?

[23:18] I think that the decision models have kind of changed

[23:21] the evals category forever. Um,

[23:25] if you're using a frontier model to do,

[23:29] more decision evals, so,

[23:34] you know, you have a very specific

[23:38] yes no classification

[23:40] use case type eval,

[23:43] I just don't think you should be using a frontier model for that.

[23:45] You're just overpaying by 10 to 100x to do that

[23:49] um, for pretty much equivalent performance

[23:52] and significantly lower cost.

[23:55] So I I think

[23:57] Decision models have kind of changed the game for evals.

[24:00] And so now, what's interesting is, do you use

[24:03] a decision model to do the eval,

[24:05] and then you use maybe some of the more

[24:08] expensive frontier models,

[24:10] to then take actions based off of that

[24:12] eval's decision. So, that,

[24:14] where, that's where I think

[24:17] the space is probably going to go.

[24:19] Cool. It's a super exciting time to be in evals for that reason.

[24:22] Thank you so much for coming and joining us on the course,

[24:26] and thank you for giving your perspective.

[24:28] Happy to be here. Thank you so much for having me.
