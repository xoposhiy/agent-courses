# Analyze and Label Failures

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/9i8rmo/analyze-and-label-failures) · [Raw file](../../raw/lessons/9i8rmo.html)

Retrieved: 2026-11-13T17:26:05.486465+00:00

[00:00] In the last video, you learned how to build a set of test
cases for a requirement.

[00:05] Each case specifies what to give the application,
and what it should do in that situation.

[00:10] Now, you can run those test cases and review the results manually.

[00:14] That manual review is where you learn what the application is actually
getting wrong before you try to automate the evaluation.

[00:20] So, your goal is to compare what the application does
with what you expected,

[00:25] and that will help you decide what needs improving in your application
so these mistakes don't keep happening.

[00:31] You'll do that by describing what went wrong, grouping cases that show
the same problem, and deciding which problems deserve attention first.

[00:38] Let's look at one case from a test set for the requirement,
only match volunteers with dogs they can safely handle.

[00:45] In this case, an experienced volunteer wants to walk a 130-lb dog,
but the dog is too strong for them to control safely.

[00:52] We expect the agent to reject the match,
but the agent approved the match.

[00:56] So next, you want to look at the trace to see the information the
agent received and what it did.

[01:02] This will help you describe what went wrong.

[01:05] Now, as you review other cases, you may not always have enough
information to tell whether the application met the requirement.

[01:11] If that happens, check the relevant facts,
or ask for help interpreting the requirement.

[01:16] And if you and another reviewer disagree, compare your reasons. You
may have noticed different facts or interpreted the rule differently.

[01:23] If you still can't tell whether the application met the
requirement, don't guess.

[01:27] Mark the case as unresolved and write down what evidence
or decision is missing.

[01:32] Now, for each run, write down whether it passed or failed and why.

[01:36] Keep that judgment with the result and trace you reviewed
because another run of the same case could turn out differently.

[01:42] For runs you haven't resolved, write down what you
still need to find out.

[01:46] For our unsafe match, your reason could be, the agent approved a match
with a dog the volunteer couldn't safely handle.

[01:53] That explains why you marked it as a failure,
but it doesn't tell you why the agent approved the match.

[01:58] Maybe the agent never received the information about
the volunteer's limits,

[02:02] or maybe it had that information and still made the wrong decision.

[02:05] So check the trace before you say it ignored the volunteer's limits.
You can still record the mistake without knowing why it happened.

[02:12] And if you have an explanation you haven't checked,
write it down as a possibility.

[02:16] Now that you've described what went wrong in individual cases,
the next step is to group the ones that show the same problem.

[02:22] That will help you see which mistakes keep happening across the test
set and how many cases each problem affects,

[02:28] so you can decide which problems to work on first.

[02:31] Take our unsafe match and compare it with another case where a
first-time volunteer was matched with a dog

[02:36] that requires an experienced handler.

[02:38] If the traces show that the agent received the information about the
volunteer's limits and the dog's requirements in each case,

[02:44] you can group them together.

[02:46] It had the information it needed, but it still approved a match it
should have rejected.

[02:51] But if the agent retrieved the wrong dog's record,
you want to keep that separate.

[02:55] The result might be an unsafe match,

[02:57] but getting the wrong record is a different problem from making the
wrong decision with the right record.

[03:01] Once you have a group, give it a clear name and write a short
explanation of what the name means with an example.

[03:07] That way, you can use the name consistently as you review more cases.

[03:11] Across this course, we use five broad categories to help
name these problems.

[03:16] The two matches we grouped together fit under Judgment, because the
agent had the relevant information but made the wrong decision.

[03:23] More specifically, we'd call that a reasoning error.

[03:26] Groundedness covers problems with the evidence the agent retrieves
or the claims it makes.

[03:31] So retrieving the wrong dog's record belongs here,

[03:34] and so does saying a dog completed an evaluation when there's no
record to support that claim.

[03:39] Execution covers mistakes in carrying out required actions,
like skipping the eligibility check before approving a match.

[03:45] Completion is about whether the intended result actually happened.

[03:49] So if the agent says an outing is scheduled,
but no calendar entry was created, that's a Completion failure.

[03:55] Propagation is when a mistake carries into later steps,
or information or instructions get lost along the way.

[04:01] For example, the agent retrieves the wrong dog's record,
uses it to approve a match, and then confirms the wrong dog.

[04:08] These are broad categories, and you can still use names that describe
a problem specific to your application.

[04:14] Don't force a case into a group that doesn't fit. Then save the labels
with each reviewed run alongside your description of what went wrong.

[04:22] And a run can have more than one label.

[04:24] The wrong record is a Groundedness problem, and carrying that mistake
through to the confirmation is also a Propagation problem.

[04:31] If you choose one main label, keep the others, too.

[04:34] As you work through more cases, you may need to clarify what a label
means, or separate two problems you'd grouped together,

[04:40] and then update the earlier labels to match.

[04:43] Now you can use those groups to decide which
problems to work on first.

[04:47] You'll want to look at how often each problem showed up
and how much harm it

[04:50] could cause because the most common mistake isn't always the most
important one to fix.

[04:56] To see how common each problem was, count the runs that show it out of
all the runs you checked for it, including the ones that passed.

[05:03] Otherwise, a problem can look more common or less common simply
because you only counted failures.

[05:08] Make sure you haven't missed that problem in runs where you found
another error, and see if some runs still need checking.

[05:14] These counts describe your test results,
so if you choose especially difficult cases,

[05:20] don't assume the problems happen just as often for your users.

[05:24] Then, think about what could happen when the agent makes that mistake.

[05:27] For our unsafe match, the volunteer could lose control of the dog
and someone could get hurt. And harm isn't just about physical safety.

[05:34] If the Northwind support agent invents a return policy,
a customer could rely on it and expect the company to honor it.

[05:40] Even if someone corrects the answer later, the customer may have
already acted on it, and the company could lose their trust.

[05:47] So you'll want to consider whether anyone would catch the mistake
before it causes harm, and how easy it would be to put things right.

[05:53] Then, compare the problems using both how often they appeared
and how serious they could be.

[05:59] Suppose awkward formatting appeared in many of your results,
but an unsafe match appeared only once.

[06:04] You might still put the unsafe match first because the risk of injury
matters more than the inconvenience of awkward formatting.

[06:11] Write down which problems you'll work on first and why.

[06:14] And if a problem could cause serious harm, you don't have to wait for
more examples before giving it attention.

[06:20] You started with an initial set of test cases, and now the problems
you've found can help you decide what else to test.

[06:26] If the agent approves an unsafe match, for example,

[06:29] you'll want to try other situations where a volunteer might not be
able to handle the dog,

[06:34] so you can see whether the same mistake happens in
those situations, too.

[06:38] Up next, you'll use those failure labels and review notes to expand
your coverage and curate a benchmark that you can keep running

[06:44] as the application changes.
