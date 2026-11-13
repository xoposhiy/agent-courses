# Choosing Where to Intervene

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/2fnhlq/choosing-where-to-intervene) · [Raw file](../../raw/lessons/2fnhlq.html)

Retrieved: 2026-11-13T17:26:07.286631+00:00

[00:00] In the last video, you tested a prompt change on the Northwind agent.

[00:04] The new grounding rule helped with the problem you
were trying to solve.

[00:07] The agent stopped adding unsupported care advice,
But the comparison has also uncovered something new.

[00:14] On some sizing questions, the agent started making an extra product
lookup, even though it already had the information it needed.

[00:20] So now you have another failure to work on. The question is,
what should change this time?

[00:26] You could edit the prompt again, change the data the agent receives,
how a tool works, or how the workflow is organized.

[00:32] You could even try a different model. All of those are possible
interventions, but they solve different kinds of problems.

[00:39] So before choosing one, look at the evidence you have,
and ask where the failure is actually showing up.

[00:45] A useful way to do that is to work through an intervention hierarchy,
such as this one by Hamel Husain.

[00:50] You start with the data, then look at the prompt, then the tools
and workflow. If those all look sound, consider the model.

[00:57] And finally, there are settings like temperature and other
sampling parameters.

[01:02] You don't have to treat this as a rigid recipe,

[01:05] The idea is to start with the simplest layer that could reasonably
explain the failure and move up when the evidence tells you to.

[01:12] Let's go through those layers with the shelter agent in mind.
The first step is, start with the data.

[01:18] Suppose one dog record says that Atlas pulls hard on walks,
so the information is there,

[01:24] but there's also a structured field that tells the agent whether the
dog requires an experienced handler, and that field is blank.

[01:31] Now imagine the agent matches Atlas with a first-time volunteer.
You could respond by changing the prompt.

[01:37] Maybe you tell the agent, "Make sure you read the behavior notes
before deciding." That might help, but look at the underlying problem.

[01:44] The record already has a place to represent whether this dog needs an
experienced handler, and that field was never populated.

[01:51] If this happens repeatedly, you probably have a data problem.

[01:55] A better fix may be to change the data-entry or processing rule so
that when notes indicate strong pulling,

[02:01] the experienced handler requirement gets set correctly.

[02:04] Then run the same eval again.

[02:07] If the failure disappears,

[02:08] you've improved the information the agent is working from rather than
asking the model to compensate for an inconsistent record.

[02:15] Now suppose the record is complete and the agent has all the
information it needs,

[02:19] but it still schedules an outing without checking whether the
volunteer is eligible.

[02:23] Now the data looks fine, so move on to the instructions.

[02:27] Does the prompt actually tell the agent that eligibility has to be
checked before scheduling? If it doesn't, start there.

[02:35] You might add a clear requirement: "Always check eligibility
before scheduling an outing." Then test it.

[02:41] If the behavior is still inconsistent, examples can help show the
agent what the rule looks like in practice.

[02:47] You could include one example where the volunteer is eligible
and the outing proceeds,

[02:51] and another where the volunteer is not eligible
and the scheduling stops.

[02:55] But be a little careful with examples because they might
open the door for bias.

[02:59] Suppose every example you give the agent involves a large dog.

[03:03] The agent may start associating the eligibility check with large dogs,

[03:07] instead of learning that eligibility should be
checked for every outing.

[03:10] So test the revised prompt on cases that look different from the
examples you gave it.

[03:15] Try a small dog or a dog with a medical restriction.
Phrase your example requests in different ways.

[03:20] If the behavior only works on cases that closely
resemble the examples,

[03:24] your prompt may be teaching a narrower pattern than you intended.

[03:28] Sometimes a clearer instruction is more useful than adding
more and more examples.

[03:32] Now suppose the prompt already says to check eligibility
and the agent is trying to do that.

[03:37] The next question is whether the tools and workflow make the
correct behavior easy.

[03:42] Suppose the agent calls an eligibility lookup and the tool returns "no
match". What should the agent do?

[03:48] Should it ask for more information, should it stop,
or should it send the case to a staff member?

[03:53] If the tool description doesn't say, the model has to decide for
itself. So give the tool a clear contract.

[04:00] Tell the agent when the tool should be used, explain the possible
results, and say what should happen after each one.

[04:06] For example, if the result is eligible, continue.
If it's not eligible, stop.

[04:11] If it's no match, ask for information needed to identify the
volunteer. That removes a lot of ambiguity from the decision.

[04:19] And sometimes the instructions still aren't enough.

[04:22] Suppose checking eligibility is required for every outing,
and even with a clear prompt, the agent occasionally skips it.

[04:29] At that point, you can make the step part of the workflow itself.

[04:33] Instead of letting the model decide whether to check eligibility,
put the lookup as a necessary step directly before scheduling.

[04:40] Now the flow is: receive the request, check eligibility,
and only then continue to scheduling.

[04:46] That can make an important requirement much more reliable.
But remember what you saw in the Northwind experiment.

[04:52] Every extra step has a cost.

[04:54] A new tool call can add latency, it can add API cost,
and it creates another place where something can go wrong.

[05:01] If you're dealing with a safety-related eligibility check, that may be
an easy trade-off to accept. For an optional step, maybe not.

[05:09] You can test that, too. Remove the step, run the same evals,
and see whether anything meaningful gets worse.

[05:16] So far, the interventions we've looked at are fairly local.

[05:20] fix a field, clarify an instruction, improve a tool contract,
change the workflow.

[05:25] But sometimes you work through those layers and the
agent still struggles.

[05:29] The data is good, the instructions are clear, the tools behave
correctly, the workflow gives the agent what it needs,

[05:35] and the task is still beyond what the model handles reliably.

[05:39] Now it makes sense to consider the model itself.

[05:42] Maybe another model is better at the kind of reasoning your agent
needs, but you need to tread carefully.

[05:47] A model change is a much broader intervention than editing one rule in
a prompt. It can affect behavior across many different requests.

[05:54] It can even change latency and cost.

[05:57] So treat a model swap like any other candidate change:
run the same evaluation suite,

[06:02] look at the failures you wanted to improve and the cases
that were already working, and compare the costs as well.

[06:09] At the top of the hierarchy are settings like temperature
and other sampling parameters.

[06:14] Modern models sometimes omit the ability to change
these parameters at all.

[06:18] If present, they can affect how variable the model's outputs are,

[06:21] but they're usually a poor place to start if your actual problem is
that the agent is missing required information, ignoring a rule,

[06:28] or calling the wrong tool.

[06:30] Changing temperature doesn't give the agent a field that isn't there,
it doesn't define what no match means,

[06:36] and it doesn't add a missing eligibility requirement to the prompt.

[06:39] Those settings are more useful when the variability itself is part of
what you're trying to improve.

[06:44] So when you find a failure, try to match the change to the evidence.
If the information is missing or inconsistent, look at the data.

[06:52] If the agent has information, but the requirement is
unclear, look at the prompt.

[06:56] If the agent knows what to do, but struggles to carry it out reliably,
check the tools and workflow.

[07:02] If those layers are working and the task is still too hard,
then consider the model.

[07:06] And if you find that the problem really is about sampling behavior,
then look at your agent's parameters.

[07:12] The point is to avoid making a broad change when a smaller one may
address the problem directly.

[07:17] And whatever layer you change, the same discipline from the last two
videos still applies.

[07:22] Change something you have a reason to believe could help, run the same
evaluation again, check the behavior you wanted to improve,

[07:28] and check what else moved.

[07:30] In the next video, you'll use this hierarchy on the Northwind
regression you found earlier.

[07:35] You already know where the two versions start to behave differently.

[07:38] You'll use that evidence to decide what to change and make the next
iteration more precise.
