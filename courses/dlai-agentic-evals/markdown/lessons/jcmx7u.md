# Evaluating Trajectories

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/jcmx7u/evaluating-trajectories) · [Raw file](../../raw/lessons/jcmx7u.html)

Retrieved: 2026-11-13T17:26:06.505145+00:00

[00:00] In the last video, you looked at individual actions.

[00:04] You saw that an agent can choose the wrong action, choose the right
action but use the wrong details, skip something required,

[00:10] or do something that shouldn't happen at all.

[00:13] But even if you check every action one at a time,
there are still failures you can miss.

[00:18] Sometimes the problem is in how the actions fit together. Think about
the dog shelter. Suppose Pamela asks to go on an outing with Pepper.

[00:26] A successful run might look something like this.

[00:28] First, the agent retrieves Pamela's volunteer record Then,
it checks whether she's eligible.

[00:34] Once it knows she's eligible, it chooses Pepper as a suitable dog,
and finally, it creates the booking.

[00:40] That ordered sequence of steps is the trajectory.
tells you more than which actions happened.

[00:46] It tells you the path the agent took through the task.
Now imagine the same four actions happen in a different order.

[00:53] The agent retrieves Pamela's record, chooses Pepper,
checks eligibility, and then creates the booking.

[00:59] If you evaluated each action separately, you might not see an obvious
problem. The right volunteer record was retrieved.

[01:05] Pepper may actually be a suitable dog. The eligibility check was
performed correctly, and the booking contains the right details.

[01:13] But the sequence is still wrong. The agent chose the dog
before it had established that Pamela was eligible for the outing.

[01:20] So one thing trajectory evaluation can check is whether
order-sensitive steps happened in the right order.

[01:25] Now consider another run. The agent retrieves Pamela's record,
selects Pepper, and creates the booking.

[01:32] This time, the eligibility check is missing completely.

[01:35] Again, the booking itself could look perfectly valid,
but the trajectory shows that a required step never happened.

[01:41] So now you have a second question to ask about the trajectory:
did every step that was required actually occur?

[01:47] There's one more kind of failure that's especially easy to miss
if you inspect actions separately.

[01:52] Suppose the first step correctly retrieves Pamela's record and returns
her volunteer ID, but when the agent gets to the matching step,

[01:59] it accidentally uses Maria's ID instead.

[02:02] The retrieval worked, perhaps the matching action worked okay too,

[02:06] but the information from one step didn't carry into
the next one correctly.

[02:10] That's a propagation failure.

[02:12] So when you look at a trajectory, there are three useful questions you
can ask: Did all of the required steps happen?

[02:19] Did the steps happen in the right order? And did the information
produced by one step get used correctly in the steps that followed?

[02:25] The shelter example makes those questions fairly easy to see
because the workflow itself is simple.

[02:31] You already know the four main steps the agent is supposed to follow.
Northwind is a little different.

[02:37] The Northwind agent can decide which tools to call based on
the customer's request.

[02:41] There isn't always one fixed sequence that every run should follow.

[02:45] So instead of starting with a pre-defined workflow,
you reconstruct the trajectory from the trace.

[02:50] Suppose a customer asks Northwind for a refund.

[02:53] One run might contain these tool calls:
get_customer(customer_id="C103"), then order_lookup(order_id="4521"),

[03:04] And then, process_refund, order ID equals 4521, amount equals 49.99.

[03:10] If you collect those calls in the order they happened, along with what
each tool returned, you have the trajectory for that run.

[03:17] Now you can evaluate the sequence as a whole. For example, Northwind
may require the customer to be verified before a refund is processed.

[03:26] So imagine another run where the same three tools appear,
but in this order: order_lookup, then process_refund,

[03:32] and only after that, get_customer.

[03:35] Each tool call may be valid on its own.

[03:37] The order lookup works, the refund call used a real order,
The customer lookup also worked,

[03:42] but the policy was still violated because the refund happened
before the customer was verified.

[03:48] This is the kind of failure that action-level evaluation won't catch
very well. You need to compare the relative positions of the steps.

[03:56] And because the tool calls are structured,
you can often check that directly.

[04:00] For example, an evaluator like identity_before_refund can look
through the trajectory

[04:04] and ask whether a successful customer verification step happened
before process_refund.

[04:10] That's a focused question, and it can often be
answered deterministically.

[04:14] You don't need a judge to reason broadly about the whole interaction,
just to determine whether one event came before another.

[04:20] The same idea applies to propagation. Suppose order_lookup returns
that the refundable amount is $49.99.

[04:27] Later in the same trajectory, the agent calls
process_refund, amount=59.99.

[04:34] The tool selection is correct, and the refund action is in roughly the
right place in the workflow, But look at the refund amount.

[04:41] It's evident that the value returned earlier wasn't
carried forward correctly.

[04:45] Here, the trajectory tells you something that neither tool
call reveals by itself.

[04:50] You can also build broader evaluators that look across several
requirements at once.

[04:55] For example, a policy compliance evaluator might consider whether the
customer was verified, whether the order was eligible for refund,

[05:03] whether the amount was correct, and whether the required
sequence was followed.

[05:07] That kind of evaluator can give you a useful overall judgment.

[05:11] But there's a trade-off: if policy compliance fails,
you still need to know why.

[05:16] A more focused evaluator, like identity_before_refund,
can point directly to one specific requirement.

[05:22] So, these checks can complement each other.

[05:24] On the one hand, a broad evaluator can tell you that the run violated
policy, On the other hand,

[05:30] focused evaluators can help you locate which part
of the policy failed.

[05:35] And this brings us back to a principle you saw in the last video.

[05:38] When the requirement you care about is represented clearly in
structured data, it's often useful to check that evidence directly.

[05:45] If you want to know whether identity verification happened
before a refund, inspect the trajectory.

[05:51] If you want to know whether the refund amount matches the amount
returned by the order lookup, compare those values.

[05:56] You only need a broader semantic judge when the requirement itself
really calls for that kind of interpretation.

[06:03] So trajectory evaluation gives you a wider view of the agent's
behavior. You're no longer asking whether each action was valid.

[06:10] You're trying to figure out whether the whole path through the task
made sense. Were the required steps there?

[06:16] Were they in the right order? Did information flow correctly from
one step to the next?

[06:21] Now, you have to be mindful that even a full trajectory has a
boundary. It tells you what happened within the scope of one run.

[06:29] But what if the requirement the agent violated was given several turns
earlier in the conversation?

[06:34] Maybe a customer said, "Don't refund anything until I confirm the
amount," and the agent followed that instruction at first,

[06:41] then forgot it later.

[06:42] To catch a failure like that, you need to look beyond one trajectory
and evaluate across turns. That's what you'll do next.
