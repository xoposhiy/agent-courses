# Traces

[Course index](../../README.md) · [Original source](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/gy3a4e/traces) · [Raw file](../../raw/lessons/gy3a4e.html)

Retrieved: 2026-11-13T17:26:05.153905+00:00

[00:00] You've now seen the big picture of how to evaluate
and improve an agent.

[00:04] Before you put that process into practice, you need a way to see what
the agent actually does as it works through a task.

[00:11] That's because if you only look at the agent's input and output,
you miss what it does in between.

[00:16] For example, a customer might ask Northwind whether a jacket is
available in their size, and the agent says yes.

[00:22] But between that question and the answer, the agent may be calling
tools to look up the jacket and check inventory,

[00:28] interpreting the results, and deciding what to do next as it goes.

[00:32] Problems can occur at any of those steps.

[00:34] For example, the agent might have skipped the inventory check
and simply made up the answer that the jacket was in stock.

[00:40] From the response alone, you wouldn't know whether the agent had
actually checked the inventory.

[00:44] So before you get into evaluations, you need a window into agent
behavior. That's what a trace provides.

[00:50] So in this video, you'll see how traces are put together,
what their different parts record,

[00:55] and how you can use them to investigate the agent's behavior.

[00:58] A trace brings together the recorded steps from one run of your agent.

[01:02] A run is a single execution of the agent, from receiving a request to
finishing its response.

[01:07] To see how that works, imagine a Northwind customer
asking for a refund.

[01:12] The agent might look up their order, check the return policy,
and request the refund.

[01:16] A trace records the model calls and tool calls along the way.
Each recorded operation is called a span, with a beginning and an end.

[01:24] So the order lookup could be one span,
and processing the refund could be another.

[01:29] Larger operations can contain smaller operations,
with their spans nested inside. That gives you a tree of spans.

[01:36] The root span covers the whole request, with child spans beneath it
for operations such as the order lookup and refund.

[01:41] The root is their parent, and those child spans can have
children of their own.

[01:45] The tree shows what happened during the run,
based on the operations your application records.

[01:50] It isn't a fixed plan for the agent to follow,
so another run might include different tool calls or repeated steps.

[01:57] Now that you've seen how spans fit together,
let's look at what each span records about an operation.

[02:02] Take the span for looking up the customer's order. Its name tells you
which operation ran, and its type identifies it as a tool call.

[02:10] The recorded input shows what was sent to the tool,
such as an order ID.

[02:14] The output shows what came back, such as the order details
and the purchase price.

[02:18] If the agent refunds the wrong amount, you can check whether it looked
up the right order and what purchase price the tool returned.

[02:25] A model-call span gives you a different view.

[02:28] Its input can include the customer's message,
the agent's instructions, and information returned by earlier tools.

[02:34] Its output records what the model generated,
that might be an answer for the customer or a request to use a tool.

[02:41] For model calls, you can also capture token usage,
a measure of how much text the model took in and generated,

[02:47] along with the model version and the prompt used.

[02:50] These details can be recorded as attributes on the span.

[02:53] They help you understand the conditions of each run and check what
changed when comparing results.

[02:58] Together, the model-call and tool-call spans let you follow
which tools the model called, what they returned,

[03:04] and how the model responded afterward.

[03:07] Spans also record when each operation started and ended,
so you can see how long it took.

[03:12] If the customer waited a long time, you can check whether the delay
came from the model call or the order lookup.

[03:18] You can also spot repeated tool calls that added unnecessary work,
even if the agent eventually gave a correct answer.

[03:25] Just remember, a trace doesn't show everything
happening inside the model.

[03:29] Even any reasoning text it includes is generated output,
not a direct view of the model's internal workings.

[03:35] So how do you get your application to record these traces? You add
code that captures information about the operations as they happen.

[03:43] Adding that recording is called instrumentation.
You don't necessarily have to write all that code yourself.

[03:49] Depending on the framework and tracing integration,
you can automatically capture model calls and tool calls,

[03:54] including their inputs, outputs, and timing.

[03:57] You can also add recording around your own functions when you need to
capture something the integration doesn't cover.

[04:02] In this course, you'll use Phoenix to collect and inspect the traces.
The tracing integration sends it the recorded spans.

[04:09] You can then open a run, follow the tree, and select a span to inspect
its recorded inputs, outputs, and other details.

[04:16] The lab takes you through setting up that connection.
The concepts aren't specific to Phoenix though.

[04:20] You can use other tracing tools or write your own code to record
and inspect the same information.

[04:26] The important limit is that a trace only contains what
your setup recorded.

[04:31] If an order lookup wasn't instrumented, you might see the model calls,
but miss the lookup between them.

[04:35] So an absent span doesn't automatically mean the
agent skipped an action.

[04:40] Before drawing that conclusion, you need to know that the relevant
work was being captured.

[04:44] With those records in place, now suppose a refund for a
customer goes wrong.

[04:49] The agent tells the customer their refund was processed, but the trace
shows that the refund tool reported it hadn't been completed.

[04:55] The model got that failure message, but still told the customer the
refund was on its way.

[05:00] The trace gives you evidence you can use to evaluate the agent.

[05:03] You can evaluate one operation, such as whether the agent looked up
the right order, or the overall result,

[05:09] such as whether it handled the refund correctly.

[05:12] Once you've evaluated it, you can record your assessment
alongside the trace.

[05:16] In Phoenix, that's called an annotation, which can include a label
or a score and an explanation.

[05:22] Also note that a conversation between a customer and the agent can
include several runs.

[05:27] For example, the agent handles a refund request and responds,
then handles the customer's follow-up question in another run.

[05:34] Each run has its own trace, which can contain multiple model
calls and tool calls.

[05:39] A shared session ID groups those traces so you can follow the whole
conversation. That wraps up module one.

[05:45] You've seen why evals matter, how the evaluation process fits
together, and how traces let you see what an agent actually did.

[05:52] You'll get more practice working with traces in the lab
and graded assignment.

[05:56] Then, in module two, you'll start putting that evaluation
process into practice,

[06:01] working out what the agent needs to do and investigating
where it falls short.

[06:05] I'll see you there.
