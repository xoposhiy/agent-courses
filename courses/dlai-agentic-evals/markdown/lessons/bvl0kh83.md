# The Evals Process Part 1

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/bvl0kh83/the-evals-process-part-1) · [Raw file](../../raw/lessons/bvl0kh83.html)

Retrieved: 2026-11-13T17:26:04.906597+00:00

[00:00] When you build an AI application, you want it to do what you expect.

[00:04] And when it doesn't, you want to know what's going
wrong so you can fix it.

[00:08] But without a clear process for testing and improving your
application, you can end up working blind.

[00:13] You might put your faith in a few successful examples and then chase
after failures as they appear.

[00:18] But fixing the example in front of you doesn't tell you whether you've
solved the broader problem or broken something else along the way.

[00:25] So, how do you put together an effective evaluation process? Broadly
speaking, you can think of the evaluation process in four parts.

[00:33] First, you analyze what the agent should do and how
it actually behaves.

[00:37] You look for situations where it might fail and use error analysis to
identify and group the failures you observe.

[00:44] Second, you use what you've learned to build and refine a
reusable set of test cases,

[00:49] with clear criteria for judging whether the agent succeeds.

[00:52] Third, you use evaluators to judge the results and measure how
well the agent performs.

[00:57] And fourth, you use those findings to make changes,
then test again to see what improved and whether anything got worse.

[01:04] These four parts give you the overall process you'll learn to use
throughout this course.

[01:08] They form an ongoing cycle, with each round informing the next.

[01:12] And once people start using your application,

[01:15] you can monitor how it handles their requests and bring any new
problems you find back into that cycle.

[01:20] So in this video, you'll get a quick overview of how the first two
parts fit together before you explore them further in Module 2.

[01:27] The first part is analyzing the agent's behavior.

[01:30] But to recognize when the agent does something wrong,
you need to know what it should have done.

[01:34] So you start by establishing the requirements for its job, what it
needs to accomplish, what it must get right, and what it must avoid.

[01:42] And you may discover that you haven't fully worked that out yourself.

[01:45] If a Northwind customer leaves out their size, should the agent ask
before recommending clothes, or can it make suggestions first?

[01:52] If you haven't decided what's acceptable, you don't yet have a basis
for calling those responses right or wrong.

[01:58] Sometimes the first problem to address is a gap in your own
understanding of what the job requires.

[02:04] So, where do you turn to work out what the agent should do?

[02:07] You look at what customers need, the company policies the agent must
follow, and the knowledge of people who understand the work.

[02:14] For Northwind, recommend clothes describes the task,
but it doesn't tell you what makes a recommendation good.

[02:20] The recommendations need to suit the customer's needs and reflect the
catalog and stock information.

[02:26] Making those expectations explicit gives you something specific to
judge the agent's behavior against.

[02:31] There may be several good recommendations for the same customer.

[02:34] You can still evaluate how well each one meets their needs without
requiring one correct answer.

[02:39] You won't necessarily have every requirement worked out at the start,
Some may be unclear,

[02:44] or you may not realize something matters until you see
the agent get it wrong.

[02:48] So these are working expectations that you'll clarify and add to,
as you examine what the agent actually does.

[02:54] With those requirements in mind, you can begin error analysis.

[02:58] The goal is to understand where the agent falls short so you can
decide what needs attention.

[03:03] You can start by looking closely at a handful of examples.

[03:06] You don't need a formal evaluation system or metrics to begin learning
what needs improvement.

[03:11] You examine its actual behavior against your requirements
and look for patterns

[03:15] so you can recognize broader problems rather than treating every
mistake as a separate issue.

[03:21] As you examine those failures, there are two kinds of problems to be
aware of as you think forward to improving your application.

[03:27] First, the problem may be in how you've prompted the model
or organized the agent's work.

[03:31] You know what it should do, but its instructions may be vague,
incomplete, or conflicting.

[03:37] For example, you expect Northwind to recommend clothes available in
the customer's size, but you never instructed the agent to check that.

[03:45] In that case, you need to improve the instructions,
or the way that you set up the agent to do the job.

[03:50] Second, even when you've clearly specified what you want,
the model can still struggle to do it reliably.

[03:56] Clear instructions don't guarantee that the model will follow them
successfully every time.

[04:01] Both of these issues call for different responses,

[04:03] so it's good to be thinking ahead to these differences when you begin
investigating improvements later in the course.

[04:09] That brings you to the second part of the evaluation process:
building test cases and defining how you'll judge the results.

[04:15] The problems you found through error analysis give you a starting
point for those cases.

[04:19] Each case describes a situation you want the agent to handle
and what you expect it to do.

[04:25] You collect these into an evaluation set,
so you can check how well the agent performs across those situations.

[04:31] You include examples of past failures because you want to check
whether you've fixed them.

[04:36] But you also need to test the everyday work the agent should do well,
along with challenging situations where it might struggle.

[04:42] Together, these help you assess more than just whether a particular
mistake has been fixed,

[04:47] and you can reuse the same cases after making changes to see what
improved and whether anything got worse.

[04:54] As you discover new problems or clarify your requirements,
you update the set so it continues to test what matters.

[05:01] Once you've decided what situations to test, you need to specify how
you'll judge whether the agent met your requirements.

[05:07] That means deciding what you'll check in each result and what would
count as success or failure.

[05:12] You record those criteria in a rubric, a written guide for
evaluating the results.

[05:18] It also identifies the information needed to make each decision.

[05:21] You can include examples of results that pass or fail,
with explanations of why, to show how they apply the criteria.

[05:28] You need to be specific about what counts as meeting each requirement,
so you don't leave too much open for interpretation.

[05:34] You also need to cover the different requirements of the task.

[05:38] For Northwind, checking availability alone could approve clothes
that don't suit the customer.

[05:43] Checking availability and suitability separately helps you see
which requirement the agent met and which it missed.

[05:49] You can then try the rubric on actual results to see whether it's
clear enough to use.

[05:54] If you can't decide whether a result meets a requirement,
you may need more information or a clearer requirement.

[06:00] Working through those questions helps you judge results more
consistently. So that covers the first half of this overview.

[06:07] You've seen how to analyze the agent's behavior, decide what to test,
and define how to judge the results.

[06:12] In the next video, you'll see the second half of this overview of
the evaluation process,

[06:17] with a look at measuring performance and using the findings to make
and test improvements.

[06:22] I'll see you there.
