# Build a Test Set You Can Trust

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/a4ui13bl/build-a-test-set-you-can-trust) · [Raw file](../../raw/lessons/a4ui13bl.html)

Retrieved: 2026-11-13T17:26:05.572053+00:00

[00:00] In the last video, you learned how to review your test results,
group the mistakes you found,

[00:05] and decide which problems need attention first.

[00:08] That review also helps you understand the application better, so you
now have more to go on than when you chose your first test cases.

[00:14] That will help you make your test set more useful.

[00:17] In this video, you'll look at how to use that understanding to expand
your test coverage by looking for important situations

[00:23] you haven't tested or haven't tested enough.

[00:26] You'll look for real examples to add and use synthetic cases where you
still need more coverage.

[00:31] And as you add cases, you'll decide which ones are worth keeping,

[00:35] so you have a set you can keep running to check the behaviors
and failures you care about as you improve the application.

[00:41] A good place to start is by looking through what you already have for
clues about what else to test,

[00:46] such as the mistakes you found in the last video, your requirements,
and real requests or bug reports.

[00:52] For example, think back to the unsafe match in the shelter app,
where a volunteer was matched with a dog they couldn't safely handle.

[00:59] You can use that mistake to help you think of other cases to test.

[01:02] Here, the agent approved a match it should have rejected,
so you might think about other reasons a match should be rejected.

[01:08] For example, the shelter also requires volunteers to be eligible for
outings. What if the volunteer is experienced, but isn't eligible?

[01:16] If you haven't tested that situation yet, it could be worth checking
whether the agent follows the eligibility rule.

[01:21] You can also go back to your requirements for inspiration.

[01:24] You've already used them to come up with cases,
but now you've seen what actually happened,

[01:28] that list might help you think of situations you missed.

[01:31] Also, don't skip a requirement just because all of
your test cases passed.

[01:36] You could take one of those cases and change a detail that matters
for the requirement.

[01:40] Think about what the agent should do with that change,
and you have another situation to test.

[01:45] Looking back, you might also realize you only tested straightforward
situations, and so you might think of something more difficult to try.

[01:52] And finally, have another look at real requests, bug reports,
and recorded runs too.

[01:57] There may be some useful examples you didn't include in your first
test set or new ones that have come up since.

[02:03] Once you've chosen some situations worth testing,
look for real requests and records you can use in those cases,

[02:09] because they help your test set reflect the situations your
application is actually encountering.

[02:14] So you might look through cases from manual review, user requests,
bug reports, support tickets, or recorded runs,

[02:20] starting with any examples you found while looking for gaps.

[02:23] For example, you might find a support ticket for the shelter about an
experienced volunteer who wasn't eligible for outings.

[02:30] The original request and volunteer record can give you the information
to use in your test.

[02:35] Alternatively, if you can't find a real example of the situation you
want to test, you can write the request and records yourself,

[02:42] or describe the situation you need to an LLM and ask it to fill in the
details for the case you've already chosen.

[02:48] This is all very similar to when you put together your original cases,

[02:52] so check that the requests and records describe the situation you
meant to test and that the details are realistic,

[02:58] and write down what the application should do under the requirement.

[03:01] Keep a note of where the information came from,
including anything you've created or changed.

[03:07] Now, as you put these cases together, compare them with the
ones you already have.

[03:12] Some may repeat a check you're already doing,
while others test a difference worth keeping.

[03:17] For example, suppose you already have a shelter case where the
volunteer's experience is missing.

[03:22] If another case only changes the volunteer's name,
you probably don't need both.

[03:27] But a case where the dog's handling notes are missing checks
something different.

[03:31] Handling missing volunteer information correctly doesn't tell you
whether the agent will also handle missing dog information correctly.

[03:38] So both cases can be useful, even if they test the same requirement
and have the same expected outcome.

[03:44] As you tune your test sets, remember each case takes work to
run and review again.

[03:49] So think about what you'd stop checking if you left it out.

[03:52] A useful case should either cover a meaningful situation,
protect against an important regression,

[03:58] or clarify a boundary in the requirement.

[04:00] You'll also want to review your existing cases to see
which ones you no longer need.

[04:05] But be careful about removing a case just because you fixed a mistake,
because later changes could bring that mistake back.

[04:12] There are good reasons to remove cases though,
such as when the shelter drops a rule that a case was testing.

[04:17] And if a rule changes, but the case is still useful,
update what you expect the application to do.

[04:23] And as you choose which cases to keep, make sure the important,
difficult situations get enough attention.

[04:29] Because lots of straightforward cases can make the overall results
look good, even when the application struggles with difficult ones.

[04:36] For example, suppose the agent passes 98 straightforward cases
but fails the only two difficult ones.

[04:42] That's a 98% pass rate, even though it got both difficult cases wrong.

[04:47] So look at the difficult cases separately,

[04:49] and keep enough useful examples to see whether changes to the
application help with those situations.

[04:54] Keep ordinary cases, too, so you can check that those changes don't
break something that already worked.

[04:59] You can include more difficult cases than you'd normally see in
everyday use, so you have enough examples to check them.

[05:05] Just remember that the overall score describes performance on the
benchmark you built,

[05:09] not the true frequency of success or failure in production.

[05:13] Together, those cases give you a benchmark that you can reuse
as you improve your application.

[05:18] When you compare versions, use the same cases
and expected results for both,

[05:23] so a change in the tests doesn't make one version look
better than the other.

[05:27] In the next video, you'll apply the full benchmark workflow to
Northwind and see how the curated test set becomes the benchmark

[05:34] you'll use in Module 3.
