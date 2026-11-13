# Writing a Custom Rubric

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/pu28bj/writing-a-custom-rubric) · [Raw file](../../raw/lessons/pu28bj.html)

Retrieved: 2026-11-13T17:26:05.980975+00:00

[00:00] In the last video, you saw how an LLM judge uses a rubric to check
whether an application's responses meet its requirements.

[00:08] But if you just ask the judge, "Is this a good response?",
it has to decide for itself what good means.

[00:14] You need to tell it what you expect from the response, what to look
for, and what would make the response acceptable or unacceptable.

[00:21] So in this video, you'll look at how to turn a requirement
into a custom rubric,

[00:26] instructions that describe how the response should be evaluated,
with examples that show how to apply them.

[00:32] Let's work through what you need to include in that custom rubric,
using the shelter's safe matching requirement.

[00:37] You'll organize it into five parts, each with a different job:
the Role, the Criteria, the Inputs, Labeled examples,

[00:44] and the Output instructions.

[00:46] The first is the role, which tells the judge what job it's doing.

[00:50] For the shelter, you might write:

[00:52] "You are evaluating whether a proposed volunteer-dog match is safe for
both the volunteer and the dog."

[00:58] A sentence or two is usually enough to name the task and what matters.

[01:03] Simply saying "You are an expert evaluator" doesn't tell the judge
what you want evaluated, so give it that specific job.

[01:10] Now the judge knows it's evaluating the safety of a match,
but it still needs to know what makes a match safe.

[01:15] That's what the criteria explain.

[01:17] For the shelter, tell the judge to check that the volunteer can
physically handle the dog, has experience relevant to the dog's needs,

[01:24] and can manage the behavior risks in the dog's record.

[01:28] To apply those criteria, the judge needs information for the case.

[01:32] These are the inputs: the volunteer's profile, the dog's record,
and the agent's recommendation.

[01:37] Label each input so the judge can tell which information came from the
volunteer, which came from the shelter,

[01:43] and which decision the agent made.

[01:45] If relevant evidence is missing, the judge may not be able to apply
the criteria reliably.

[01:50] The case information sits in the same prompt as your instructions,
so separate the two clearly.

[01:56] For example, you can put each input inside tags that mark
where it begins and ends.

[02:01] The instructions tell the judge how to evaluate,
and the tagged inputs identify what it should evaluate.

[02:06] The inputs will vary by application, but keep the case information
separate from the instructions.

[02:12] Next, you can add labeled examples to show how those criteria apply.
A judge can interpret written criteria differently from a reviewer.

[02:20] So use cases from the benchmark that reviewers have already labeled
and include the case evidence, the expected label,

[02:26] and the reason for it.

[02:28] Include both safe and unsafe matches, especially cases where it's
harder to decide which label applies,

[02:33] and make sure reviewers agree with the labels before
using them as examples.

[02:37] Though examples can help, they don't always improve
the judge's decisions.

[02:41] Sometimes the judge follows the examples too closely,

[02:44] basing its decision on similarities to those cases rather than
checking whether the new case meets the criteria.

[02:50] So try the rubric with and without examples, and compare both versions
on the same cases that people have already reviewed.

[02:56] Use cases that aren't included as examples in the prompt,
and see which version agrees more often with the reviewers,

[03:02] especially on difficult cases.

[03:04] The final part of the rubric tells the judge how to
report its decision.

[03:08] For safe matching, you can ask for one label, SAFE or UNSAFE, and
define what each means. Those labels are easy to compare and filter.

[03:16] A score from 1 to 10 is hard to use if you haven't explained what
makes a 6 different from a 7.

[03:22] If some cases need human review, you can add a NEEDS_REVIEW label,
but define when the judge should use it.

[03:28] For example, you might require human review for a match with a large
dog when the volunteer has some experience,

[03:34] but no history with large breeds.

[03:36] For those cases, the rubric should tell the judge to use
the label NEEDS_REVIEW.

[03:41] Only add extra labels or scores when you can explain what each means
and why you need it.

[03:46] So those five parts tell the judge what it's evaluating,
how to make the decision, what information to use,

[03:52] how the criteria apply to the examples, and how to report the result.

[03:57] They work together in one prompt to explain the assessment you
want the judge to make.

[04:02] Now, let's look at a few good practices for writing custom rubrics.
First, don't ask one rubric to judge everything about a response.

[04:10] One of the biggest mistakes is cramming a bunch of evaluations into a
single prompt across multiple dimensions.

[04:16] For example, you might want to check whether a match is safe
and whether the agent speaks politely to the volunteer.

[04:22] If you combine both into one pass or fail result,

[04:25] a failure won't tell you whether the problem was an unsafe match
or how the agent spoke to the volunteer.

[04:31] So give each evaluator one dimension with a single,
specific question to answer: "Is this match safe?"

[04:37] for one, and "Did the agent respond politely?" for another. You'll get
a separate result for each, so you can see what needs fixing.

[04:45] Then you can combine them with whatever rule makes sense
for your application.

[04:49] Keeping the results separate lets you track improvement for each
requirement, and it also lets you treat failures differently.

[04:55] An unsafe match is more serious than a safe match that misses a
volunteer's preferences.

[04:59] So you might accept a missed preference for now, but a safety problem
is a more serious issue that might act as a guardrail.

[05:06] you probably don't want to ship your app, even if you implemented some
fixes that improved performance in other, less critical areas.

[05:13] Another good practice is to treat your rubric like code.

[05:16] Changing the prompts can change the judge's decision,
so keep a record of each version and its results.

[05:22] When you revise a rubric, change one thing at a time and test it on
the same cases so you can see what effect each edit has.

[05:30] Keep earlier versions so you can go back if a change makes
the judgments worse.

[05:34] You've now seen how to put a custom rubric together
and revise it over time.

[05:39] In the next video, you'll learn how to test whether you can trust
the judge's decisions.
