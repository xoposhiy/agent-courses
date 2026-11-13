# Improving Agents After Deployment

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/zqwvtn/improving-agents-after-deployment) · [Raw file](../../raw/lessons/zqwvtn.html)

Retrieved: 2026-11-13T17:26:07.487971+00:00

[00:01] So far, all the improvements you've made have happened offline.

[00:04] You had a fixed set of cases, you changed the agent, and then you ran
the same cases again to see what improved and what regressed.

[00:11] That gives you a controlled way to make changes before real users ever
see them. But once the agent is live, the environment changes.

[00:19] Now people are going to ask things you didn't put in your test set.

[00:22] They'll phrase familiar requests in unfamiliar ways,
they'll leave out context, combine several things into one message,

[00:29] and sometimes behave in ways that are hard to anticipate in advance.

[00:33] So after deployment, one of the most important questions becomes,
where do the next improvement targets come from?

[00:38] Usually, they come from production. Think about the dog shelter agent.

[00:43] Maybe your offline test set includes a volunteer saying,
"I have limited mobility,"

[00:48] and the agent correctly recognizes that this matters when deciding
which dogs are appropriate.

[00:53] But a real volunteer might say, "I can only walk
for about ten minutes."

[00:58] The underlying constraint is similar, but the wording is different.

[01:01] Or someone might ask, "Is Pepper free Saturday, and if not,
can I switch to Sunday?"

[01:06] Now the agent has to handle availability and a fallback request
in the same message.

[01:11] And some problems have nothing to do with the wording of the request.

[01:14] Maybe the agent gives the right answer,
but it takes 14 seconds instead of 2.

[01:19] Maybe a shelter policy changes, so behavior that was correct last
month is no longer correct today.

[01:25] And what if a new kind of dog record appears with fields your original
benchmark never covered?

[01:29] A good offline benchmark can catch a lot,
but it can only test the situations that made it into the benchmark.

[01:35] That's why production becomes another source of evidence for
optimization. Your offline evals still have an important job.

[01:43] They're where you can test a candidate change against known cases
in a repeatable way.

[01:48] Before releasing a new version,

[01:50] you can run it against the failures you wanted to improve
and the cases you want to protect from regression.

[01:55] You can also automate those checks as part of your development
process, and for some applications,

[02:00] you may decide that certain evals have to meet a threshold
before a release goes out.

[02:04] The exact release rule depends on the product.

[02:07] The important part is that offline evaluation gives you a stable place
to compare versions before the new behavior reaches users.

[02:14] Production gives you something different.

[02:17] It shows you what your benchmark missed, and there are several sources
of information you can use once the agent is live.

[02:23] Let's go over four kinds of evidence that are commonly used.
production monitoring, manual review, user feedback, and A/B testing.

[02:32] In production monitoring, you run evaluators and track metrics across
live traces to see where problems are appearing at scale.

[02:39] Suppose a policy evaluator suddenly starts
flagging more conversations,

[02:43] or a metric such as average tool use or response latency starts
creeping higher after a release.

[02:49] Production monitoring will alert you to that kind of problem
and help you answer a key question: Where should I look?

[02:55] Once you find an interesting issue, you often need to inspect the
traces themselves. That's where manual review comes in.

[03:02] Imagine 37 shelter conversations fail an eligibility evaluator.

[03:06] The count tells you there's a problem, but it doesn't tell you what
kind of problem. Open a few of those traces.

[03:12] Did the agent skip the eligibility check?
Did it call the right tool with the wrong argument?

[03:17] Did the lookup return the correct result, but the agent ignored it?

[03:21] Or did the agent follow the right process and still reach
the wrong conclusion?

[03:25] Reading the trace helps you turn a metric into a failure pattern you
can actually work on.

[03:30] User feedback gives you another source of evidence.
Sometimes that's explicit, like a thumbs down or a complaint.

[03:36] Sometimes it's behavioral.

[03:38] A user asks the same question again and rephrases it three times,
then they abandon the conversation and ask to talk to a human agent.

[03:47] None of those signals tells you exactly what failed on its own, but
they can point you towards interactions that deserve a closer look.

[03:54] Once you have a candidate improvement, you may also want to compare
versions on real traffic. That's where an A/B test can be useful.

[04:01] You can send some traffic to the current version and some to
the revised version,

[04:05] then compare the outcomes that matter for your application.

[04:09] The new version might help reduce policy failures or the amount of
follow-up turns users need to get to the outcome they're looking for.

[04:16] Or it might lead the agent to answer just
as accurately but take longer.

[04:20] The important thing is that these methods answer different questions.
Monitoring helps you find where something is happening.

[04:27] Manual review helps you understand what happened. User feedback helps
surface problems that matter to the people using the system.

[04:34] And A/B testing can help you see whether a change still looks
useful under real traffic.

[04:39] You'll often use more than one of them on the same problem. There's
another thing production makes much more visible: operational cost.

[04:47] Earlier, you saw this with the grounding rule you added to
the Northwind agent.

[04:51] "Never state a product detail unless a tool result supports it."
Remember what happened?

[04:56] You got rid of ungrounded answers, but the new rule caused the agent
to start making unnecessary tool calls.

[05:02] At a small scale, one extra call may not look important.
But imagine that behavior repeating thousands of times a day.

[05:09] You'll end up getting significantly more latency and cost.

[05:12] The same is true for token use, model choice, repeated tool calls,
unnecessary handoffs,

[05:18] or conversations where users have to keep asking for the same thing.

[05:21] So when you monitor an agent in production,
don't look only at whether the answer was correct.

[05:26] A useful system also has to behave efficiently enough for the
environment it runs in.

[05:32] This is where the offline and production sides of the improvement
loop start to connect.

[05:36] For the dog shelter agent, suppose production monitoring starts
flagging conversations where volunteers mention physical limitations.

[05:43] You open one of those traces and see a volunteer say,
"I can only walk for about ten minutes. Is Pepper free on Saturday?"

[05:49] The agent checks Pepper's availability and schedules the outing,

[05:53] but it never considers whether Pepper is a suitable match for someone
who can only walk for ten minutes.

[05:58] most likely because of a physical impairment.
Now you have a specific production failure.

[06:03] Open the trace, and find the first place the behavior goes wrong.

[06:07] In this case, the agent understood the scheduling request,

[06:10] but it didn't recognize the walking time limit as information
that should affect the match.

[06:15] Next, decide what the agent should have done instead.

[06:18] It should have treated "I can only walk for about 10 minutes"
as a constraint on the kind of dog this volunteer can handle,

[06:24] checked Pepper against that constraint,
and only then continued with scheduling.

[06:29] Now, save that conversation as a new test case.

[06:32] Keep the volunteer's original wording because that wording is part of
what your old test set was missing.

[06:38] Record the behavior you expect and add the case to your
offline evaluation set.

[06:43] Then, you can make a targeted change to the agent and run the updated
version against this new case. But don't run only this one.

[06:50] Run the rest of your benchmark, too.

[06:52] You still want the agent to handle the older mobility cases correctly,

[06:56] and you don't want a change made for this new phrasing to break
scheduling requests that were already working.

[07:02] If the new version now handles the 10-minute walking constraint
correctly and the rest of the benchmark stays healthy,

[07:08] you have a stronger candidate to release.

[07:10] Once that version is live, keep monitoring the same
kinds of conversations.

[07:15] Maybe the next volunteer says, "I'm fine with short walks,
but nothing strenuous."

[07:19] That may reveal another phrasing your offline set doesn't cover yet.
And when that happens, you do the same thing again.

[07:26] inspect the trace, establish the expected behavior,
add the case to your benchmark, and use it to guide the next change.

[07:33] That's how production starts feeding the offline eval set.

[07:36] Each real failure you decide is worth fixing becomes a case the next
version has to handle too. That gives you a continuous loop.

[07:44] Production reveals something your existing tests missed,
you inspect it and turn it into a reproducible case,

[07:50] make a change and test it offline, then you release the new version
and see what real users show you next.

[07:57] Over time, your benchmark becomes more representative of the
situations your agent actually encounters,

[08:02] and your optimization process gets better, too, because each new
failure gives you another piece of evidence to work with.

[08:09] In the next video, you'll follow that loop with
Northwind. See you there!
