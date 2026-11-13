# Define Application Requirements

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/a4ui1p/define-application-requirements) · [Raw file](../../raw/lessons/a4ui1p.html)

Retrieved: 2026-11-13T17:26:05.264175+00:00

[00:01] In this course, you're learning how to use evals to find out whether
the applications you build are doing the job you want them to do.

[00:07] And as you've seen, that can be challenging,
because mistakes in AI applications can be subtle.

[00:13] For example, the application might keep running without an error
message or a failing test and still do something wrong.

[00:19] So you need to look carefully at what your application actually does
and compare that with what you expected.

[00:24] If those don't match, you've found a problem to investigate and fix.

[00:28] In module one, you focused on seeing what the
application actually did.

[00:32] You learned to make requests, run the application,
and use traces to follow the steps it took.

[00:37] But seeing what the application did is only one
part of the comparison.

[00:41] So in this video, you'll learn how to find and develop requirements
that describe what your application must do and must not do.

[00:48] Those requirements tell you what to test for and what
would count as a failure.

[00:52] At the end of this module, those requirements will become part of a
benchmark, a reusable set of cases, expected outcomes,

[00:59] and labels you can run as the application changes.

[01:02] You'll do this in three steps. First, you'll find requirements
and write them down.

[01:06] then you'll turn specific observations into requirements
that cover more than one case.

[01:12] Finally, you'll review what you've written for unclear wording
or situations you haven't covered.

[01:17] So let's start by exploring some sources for requirements.
There are three useful places to look.

[01:22] As you explore each one, ask yourself, "What does this tell me the
application should do or should avoid doing?"

[01:28] Your goal is to write down that expectation as a requirement.

[01:32] To see how this works,

[01:33] let's look at an application that helps an animal shelter arrange
outings where volunteers take dogs out for the day.

[01:39] It checks whether volunteers are eligible, matches them with suitable
dogs, and helps schedule the outings.

[01:45] Now, the first place to look is existing rules.

[01:48] For example, an animal shelter may have a rule that volunteers with a
do-not-adopt flag cannot take dogs on outings.

[01:55] Ask yourself, what does the application need to do
to follow that rule?

[01:59] If it arranges these outings, it must not match a flagged volunteer
with any dog. That's a requirement.

[02:05] Notice that you don't need to see the application make that mistake
before adding this requirement.

[02:09] The shelter's rule already tells you what should happen,
but not every expectation has been written down,

[02:15] so the second place to look is people who understand the work.

[02:18] They may know what the application should do in situations the
existing rules don't address.

[02:23] For the shelter application, you could talk to staff who regularly
match volunteers with dogs.

[02:28] Ask what they consider when making a match and what would
make them reject one.

[02:32] As they explain, ask yourself, what should the application do to
make the same decision?

[02:38] Now, people close to the work may not think of every requirement
just because you asked.

[02:43] It can be easier to explain why they would accept or reject a
particular match than to list every rule they use.

[02:48] So you can show them a set of volunteer descriptions and dog records,
and ask which matches they would recommend and why.

[02:55] Use their explanations to write down what the
application should do and when.

[03:00] keep the reason with the requirement, so it's clear why the
application should behave that way.

[03:05] Talking to others helps you understand what should happen, but it's
hard to anticipate every requirement through discussion alone.

[03:11] So the third place to look is the application's traces.

[03:14] Looking directly at how the application handles requests can reveal
situations you hadn't considered.

[03:20] One place to start is with traces you've already saved,
whether they came from real users or requests you tried yourself.

[03:26] If you don't have traces yet, write a few realistic requests yourself
or with an LLM and run them through the application.

[03:33] This lets you start learning from behavior before you have real users.

[03:37] Now, let's use the Northwind application from your labs to see how a
trace can help you write a requirement.

[03:43] A customer asks, "How should I care for my merino wool sweater?"

[03:47] The application answers, "You can machine wash it on a wool cycle
and then tumble dry."

[03:52] To check that advice, you look at the product information the
application received, which is recorded in the trace.

[03:58] It says machine washable on wool cycle. It says nothing about drying.

[04:02] So the washing advice comes from the product information, but the
application added drying advice it didn't have the information for,

[04:09] and that could ruin the sweater.

[04:11] You could record the mistake like this:
the application recommended tumble drying,

[04:16] even though it had no drying instructions for this sweater.

[04:19] Keep that note with the trace and the product information, so you have
a record of what went wrong and why you judged it a mistake.

[04:26] To turn that observation into a requirement, ask yourself,
what should the application do to avoid this kind of mistake?

[04:32] You could tell it not to recommend tumble-drying this sweater,
but it could still invent other instructions for another product.

[04:38] You need a requirement that covers those recommendations too.

[04:42] So you could write, "Only make claims about products that are
supported by Northwind data."

[04:47] That requirement is broader than the sweater case.

[04:49] It can also catch unsupported claims about sizing, color,
availability, care instructions, or return policies.

[04:56] Now, when you review what the application says about a
product, you can ask,

[05:00] "Does the Northwind data support what the
application told the customer?"

[05:04] That helps you catch invented details about other products too.

[05:07] Keep any further examples with their traces and notes,
so you can use them to test and refine the requirement.

[05:12] So that was the first step where you find and
develop your requirements.

[05:16] The second step is to review and refine what you've written.

[05:20] Look for unclear wording and situations you haven't covered,

[05:22] so you can improve the requirements and see what still
needs to be worked out.

[05:26] There are two useful things to check.
First, look for words in your requirements that need more explanation.

[05:32] For example, "Recommend a suitable dog" depends on what
you mean by "suitable".

[05:37] If you leave that unexplained, whoever evaluates the recommendation
has to supply their own interpretation.

[05:43] To make "suitable" more specific, you could start by asking what would
make a match unsuitable. The shelter's rules can help you answer that.

[05:51] For example, a dog that requires an experienced handler should not be
matched with a volunteer who lacks that experience.

[05:57] Write that restriction into the requirement. You're taking a rule
that was hidden inside the word "suitable" and making it explicit.

[06:03] Now, a person or an LLM evaluating the recommendation can check
that rule instead of guessing what you meant.

[06:10] Second, look for situations your requirements don't yet cover.

[06:13] It's easy to describe what should happen when the application has
complete information,

[06:18] but it's harder to spot what it should do when that information is
missing or conflicting.

[06:22] For the shelter, also check what the application should do
when none of the suitable dogs are available.

[06:27] Check whether the shelter has a rule for that situation.
If it does, add what the application should do to your requirements.

[06:34] If it doesn't, you need to decide what should happen when no
suitable dog is available.

[06:38] Until that's settled, you won't know whether the application handled
the situation correctly.

[06:43] You've learned how to find requirements and review them for unclear
wording and situations you may have missed.

[06:48] This helps you spell out what your application should do.

[06:51] But to find out whether your application meets those requirements,
you need requests that put each one to the test.

[06:57] So in the next video,

[06:58] you'll learn to build test sets that cover different situations
for your requirements

[07:01] and spell out what the application should do in each.

[07:04] I'll see you there.
