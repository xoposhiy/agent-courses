# Turn Requirements into Test Cases

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/sh7zq0bk/turn-requirements-into-test-cases) · [Raw file](../../raw/lessons/sh7zq0bk.html)

Retrieved: 2026-11-13T17:26:05.345708+00:00

[00:00] In the last video, you learned how to find and define requirements
that describe what your application should and shouldn't do.

[00:07] But to find out whether your application meets those requirements,
you need to run it through those situations that test them.

[00:13] So in this video, you'll learn how to come up with those situations
and turn them into test cases,

[00:18] specifying what you'll give the application and what
you expect it to do.

[00:21] Each test case should keep together the user request,
the relevant records or context, and the expected outcome.

[00:28] This can be tricky because a single requirement can apply in lots of
different situations,

[00:32] so you'll want an initial set of cases that covers a meaningful range.

[00:36] For example, the shelter application must only match volunteers with
dogs they can safely handle.

[00:41] That includes volunteers with different levels of experience,
dogs with different handling needs,

[00:46] and situations where information about either one of those is missing.

[00:49] One case won't tell you whether the application follows the rule
across those different situations.

[00:55] So, let's start choosing situations for that safe
matching requirement.

[00:59] A volunteer needs the experience and physical ability to handle the
dog safely, and you'll want cases that test both.

[01:06] Otherwise, you could have lots of cases about experience without ever
checking whether the volunteer can physically control the dog.

[01:12] You can get those situations from a few different angles.
One approach is to think about what would make a match safe or unsafe.

[01:20] For a dog that needs an experienced handler,
you could consider a first-time volunteer,

[01:24] and then someone with the experience and physical ability to
handle that dog safely.

[01:28] You could also consider an experienced volunteer who can't
physically control the dog.

[01:33] These situations let you check whether the application considers both
experience and physical ability when making a match.

[01:40] Another approach is to consider what information the application will
have about the volunteer or dog.

[01:44] You might try a situation with clear handling notes,
one where those notes are missing,

[01:49] and one where two notes disagree about whether a
beginner can handle the dog.

[01:53] That lets you test what the application does when the information it
has is incomplete or contradictory.

[01:59] A third approach is to change how the request is written while keeping
the facts the same. For example, "Can I take Buddy out for a walk?"

[02:07] and "I'd like to walk Buddy. Would that be okay?" ask for the same
thing. And you can also try shorter messages or spelling mistakes.

[02:15] You're checking whether the application makes the same decision
when someone asks in a different way.

[02:19] These are ways to get ideas, so you don't have to apply all three to
every case or try every possible combination.

[02:26] Start with situations the application is likely to face and problems
you've already seen,

[02:30] especially where a mistake could put someone at risk.

[02:33] Once you've chosen some situations to test your requirement,
the next step is to work out what goes into each test case.

[02:40] For the shelter, you'll need the volunteer request, the volunteer
and dog information, and what you expect the agent to do.

[02:46] So let's put those together for our unsafe match example.

[02:50] The volunteer is experienced, but the 130-pound dog is too strong for
them to control safely.

[02:55] Those are facts you'll include,

[02:57] and the expected outcome is to reject the match because experience
alone isn't enough to meet the safe matching requirement.

[03:03] Now take a dog the same volunteer has both the experience
and physical ability to handle.

[03:08] You'd expect approval, provided the other eligibility
and availability conditions are met,

[03:13] and the shelter's policy calls for approving suitable matches.

[03:17] But if the dog's handling notes are missing,
should the agent ask for more information or reject the match?

[03:22] The safe matching requirement doesn't settle that question.

[03:25] Check the shelter's policy, and if it doesn't answer the question,
ask the people responsible to decide.

[03:31] If the decision is to ask for the missing information
before recommending a match,

[03:35] add that to the requirement and write it down as the expected outcome.

[03:39] Until that decision is made, you don't yet know what response
to count as correct.

[03:43] That's a requirement problem that the test case helped reveal.
And sometimes, more than one answer can be right.

[03:49] If several dogs would be safe matches, don't make one particular dog
the only acceptable answer.

[03:55] Instead, describe what makes a dog suitable. The volunteer must have
the experience and physical ability to handle it safely.

[04:02] You can also include an example of an acceptable response if
that helps make the expectation clear.

[04:07] Check that it follows the requirement, but remember that another
suitable dog or different wording can still be correct.

[04:13] For the information you'll give the application,

[04:15] you can use examples you already have or create new ones for the
situations you want to test.

[04:20] If an LLM helps generate them, check that they're realistic
and fit the situation. Keep a note of where each example came from.

[04:28] Later, that source will help you decide how much weight to give the
case and whether it belongs in the reusable benchmark.

[04:34] So now you know how to take a requirement,
choose some situations to test,

[04:38] and work out what information goes into each case and what the
application should do.

[04:42] Next, you'll run those cases and see what the
application actually does.

[04:46] We'll review the results together, describe the problems we find,

[04:50] and group similar mistakes so we can decide which ones
need attention first.

[04:54] I'll see you there.
