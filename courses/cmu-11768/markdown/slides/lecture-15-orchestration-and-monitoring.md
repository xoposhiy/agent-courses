# Lecture 15 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-15-orchestration-and-monitoring.pdf) · [Raw file](../../raw/slides/lecture-15-orchestration-and-monitoring.pdf)

Retrieved: 2026-11-13T16:45:31.971344+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Orchestration and monitoring

Frameworks 2 · October 20, 2026

Daniel Fried

11-768: AI Agents

1

## Page 2

Structure around agent actions

We have already seen several ways to guide agent actions.

Skills
Instructions guide behavior; executable skills can
constrain execution.

Planning and
decomposition

Break a task into parts and coordinate their execution, as
in MACU, RAO, and RLM.

Automations
Connect agent runs through prescribed steps and checks.

Today: Orchestration frameworks let developers specify parts of a workflow in
advance, while delegating judgments and actions to LLMs.

Lecture 4 · Skills
Lecture 5 · MACU
Lecture 14 · Automations
2

### Page links

- [Link 1](../optional-readings/ref-f36ae4007ec3.md)
- [Link 2](../readings/arxiv-2606-01533.md)
- [Link 3](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en)

## Page 3

Single agents vs. workflows

Both combine LLMs, tools, and application code.

Single agent

LLM

↓ act · observe ↑

Tools

Behavior
determined by
model, prompt, and
environment

Explicit workflow (example)

Classify

LLM
→

Retrieve

Code
Tools
→

Investigate

LLM
Tools
→

Check

Code

More of the behavior is specified by the developer in advance

What do we gain by fixing a workflow?

Lecture 14 · Single-agent baseline
LangGraph · Workflows and agents
3

### Page links

- [Link 1](../optional-readings/ref-be28ccd063ec.md)
- [Link 2](../optional-readings/ref-42f1d27e513b.md)

## Page 4

Workflow benefits

Fixing a workflow for a known procedure reduces the model decisions

Consistency

Prescribe required steps and
enforce checks in code.

Flagged reply → approval → send

Efficiency

Use an appropriate model for
each step, or even just code (no
model at all)

Poll: code

Classify: smaller model

Anthropic · Building effective agents
LangGraph · Thinking in LangGraph
4

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)
- [Link 2](../readings/ref-ffc229d83891.md)

## Page 5

Workflow orchestration

5

## Page 6

Examples

Customer support requests follow different procedures.

Routine question

“How do I reset my password?”

Retrieve guidance → draft reply →
send

Request requiring review

“I was charged twice. Please refund
the extra payment.”

Draft reply → employee approval →
send

LangGraph · Thinking in LangGraph · adapted support scenarios
6

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 7

Workflow steps

Explicit steps encode the required work and its possible continuations.

question / feature / billing

bug

complex

billing / complex / urgent

Read email
Classify

Search docs

Bug ticket
Draft reply

Send reply

Review
proposed reply

LangGraph connects functions implementing these steps.

LangGraph · Thinking in LangGraph
7

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 8

Conditional routing

The request and intermediate results determine which steps execute.

question / feature / billing

bug

complex

billing / complex / urgent

Read email
Classify

Search docs

Bug ticket
Draft reply

Send reply

Review
proposed reply

Routine question: search → draft → send

Billing-classified request: search → draft → review → send

The review path depends on the model’s classification.

LangGraph · Thinking in LangGraph
8

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 9

Inside workflow steps

Each step can combine code, model calls, and tools.

question / feature / billing

bug

complex

billing / complex / urgent

Read email

code

Classify

code + LLM

Search docs

code

Bug ticket

code

Draft reply

code + LLM

Send reply

code

Review
proposed reply

Here, classification and drafting call an LLM from code.

LangGraph · Thinking in LangGraph
9

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 10

Data and human input

Search and review add information

question / feature / billing

bug

complex

Read email

email text

Classify

Search docs

query + docs

Bug ticket
Draft reply

Send reply

Review
proposed reply

approval / edit

Search docs

Input: query
Output: supporting documents

Review proposed reply

Input: request and draft
Output: approval, edit, or rejection

LangGraph · Thinking in LangGraph
10

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 11

Shared state

Passed between nodes in the workflow.

Billing request

Email: “Urgent: Acme
Cloud charged our
company twice…”
Classification: billing,
high urgency
Search result: billing-
review policy
Draft: proposed reply for
review

class SupportState(TypedDict, total=False):
    email_id: str
    email_content: str
    classification: dict
    search_results: list\[dict\]
    draft_response: str
    review_decision: dict

LangGraph · Thinking in LangGraph · Step 3
11

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 12

State updates

A node reads state and returns the fields it changes.

Support state

email_content

“Urgent: Acme Cloud
charged our company

twice…”

classification

billing · high urgency

def classify_intent(state):
    classification = model.classify(
        state\["email_content"\]
    ).model_dump()
    return {"classification": classification}

LangGraph · Thinking in LangGraph · Step 3
12

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 13

Node implementations

Nodes read state, do work, and return updates.

Document
retrieval

Search service

Reply
generation

llm : chat model

def search_documentation(state):
    c = state\["classification"\]
    query = f"{c\['intent'\]} {c\['topic'\]}"
    return {"search_results": services.search(query)}

def draft_response(state):
    response = llm.invoke(\[
        ("system", "Draft a reply using these documents."),
        ("human", json.dumps({
            "email": state\["email_content"\],
            "documents": state.get("search_results", \[\]),
        })),
    \])
    return {"draft_response": response.text}

LangGraph · Thinking in LangGraph · Step 4
13

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 14

Graph assembly

Node functions and transitions form the support workflow.

Read email

Classify

Search docs
Bug ticket

Draft reply

Review reply
Send reply

Solid: fixed · Dashed: conditional

g = StateGraph(SupportState)
g.add_node("read_email", read_email)
g.add_node("classify_intent", classify_intent)
g.add_node("search_documentation",
            search_documentation)
g.add_node("draft_response", draft_response)
g.add_edge(START, "read_email")
g.add_edge("read_email", "classify_intent")
g.add_edge(
    "search_documentation", "draft_response"
)
graph = g.compile(checkpointer=checkpointer)

LangGraph · Thinking in LangGraph · Step 5
14

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 15

Classification and routing

The classification selects a path through the assembled graph.

Read email

Classify

Search docs
Bug ticket

Draft reply

Review reply
Send reply

Solid: fixed · Dashed: conditional

intent = classification\["intent"\]
destination = (
    "bug_tracking" if intent == "bug" else
    "search_documentation"
    if intent in {"question", "feature", "billing"}
    else "draft_response"
)
return Command(
    update={"classification": classification},
    goto=destination,
)

LangGraph · Thinking in LangGraph · Step 4
Browse the full source ↗

15

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)
- [Link 2](../readings/ref-cb24aa6892d8.md)

## Page 16

Recoverable progress

Saving search results before generation preserves completed work.

Search docs
Saved search

results
Generate reply

crash during generation

repeat generation

With saved search results, restart generation using completed work.

LangGraph · Thinking in LangGraph · node granularity
16

### Page links

- [Link 1](../readings/ref-cb24aa6892d8.md)

## Page 17

Checkpointing and resuming

Saved state and execution progress let a workflow continue later.

Save progress
A persistent checkpointer records the workflow’s state and
where execution should continue.

Resume
Use the same execution ID to load saved progress and
continue. Supply new input when needed.

Retry a failure
A retry policy repeats a failed node after a temporary error,
such as a timeout.

Human input
An interrupt pauses the workflow. The application collects a
response and supplies it on resume.

LangGraph · Persistence
LangGraph · Interrupts
LangGraph · Retry policies
17

### Page links

- [Link 1](../optional-readings/ref-7dd57631bd24.md)
- [Link 2](../optional-readings/ref-99e58642fe77.md)
- [Link 3](../readings/ref-cb24aa6892d8.md)

## Page 18

Monitoring with execution traces

A record of the execution shows the work done inside each step.

Steps contain model calls, tool
calls, and ordinary code

Each operation can record
inputs, outputs, time, and
errors

LangSmith calls an operation a
run and the whole tree a trace

Course support demo · Open the recorded trace ↗
18

### Page links

- [Link 1](https://smith.langchain.com/public/5e17b93a-17af-4386-ada0-9bd033f98a74/r)

## Page 19

Monitoring with execution traces

A record of the execution shows the work done inside each step.

Routine password question

“Hi, I forgot my Acme Cloud
password. How can I reset it?”

Workflow trace

Duplicate charge

“Urgent: Acme Cloud charged our
company twice for this month's
subscription. … Please investigate
the duplicate charges and refund
the extra payment.”

Workflow trace pt 1

Workflow trace pt 2

LangSmith · recorded lecture traces
19

### Page links

- [Link 1](https://smith.langchain.com/public/416d3c74-4b43-4883-b189-92a57431a819/r)
- [Link 2](https://smith.langchain.com/public/5e17b93a-17af-4386-ada0-9bd033f98a74/r)
- [Link 3](https://smith.langchain.com/public/aeddf201-687b-4389-acdb-137dd9683000/r)

## Page 20

Unit tests for nodes

Explicit inputs and outputs let us test each step in isolation.

Classification · example test

Given

Email: “I was charged twice.”
Fixed model output: billing

Classify intent

Expect returned values

Classification update: billing
Routing destination: document search

Repeatable checks

Control inputs and external calls. Check
returned updates and routing
decisions.

Scope of the test

Direct node calls bypass checkpoints.
Test persistence and actual routing
through the graph.

LangGraph · Testing individual nodes · support demo example
20

### Page links

- [Link 1](../optional-readings/ref-441c50893712.md)

## Page 21

Workflow and regression tests

Connected steps need controlled tests and checks with real models and services.

Controlled workflow test
Expected behavior

Password question
Retrieve guidance, draft, send

Billing complaint
Pause for approval; nothing sent yet

Rejected reply
Finish without sending

Temporary search failure
Retry search, then continue

Regression checks
Do tests still pass after a change, e.g. swapping in a new model?

Integration testing
Run the end-to-end workflow to test how nodes interact

LangGraph · Graph tests
LangChain · Integration tests
LangSmith · Evaluation
21

### Page links

- [Link 1](../optional-readings/ref-1cb888b65fa5.md)
- [Link 2](../optional-readings/ref-adb9c7fcd887.md)
- [Link 3](../optional-readings/ref-441c50893712.md)

## Page 22

Workflow tradeoffs

Pros

Consistency

Possible efficiency gains

Testability

Cons

Less adaptable

Information flow has to be
explicitly managed

22

## Page 23

Agent / Workflow frameworks

Frameworks package related orchestration ideas around different programming abstractions.

Framework
Programming emphasis

OpenHands
Configurable agent execution and work integrations · previous lecture

LangGraph
Explicit workflow graphs, shared state, and recovery · today's example

OpenAI Agents SDK Agent loops, tools, delegation, and handoffs

AG2
Agent conversations and coordination, including group workflows

DSPy
Modular LLM programs and prompt optimization using examples and
metrics

23

### Page links

- [Link 1](../optional-readings/ref-f06f9bb46535.md)
- [Link 2](../optional-readings/ref-399cf6369bd3.md)
- [Link 3](../optional-readings/ref-7ad558336cab.md)
- [Link 4](../optional-readings/ref-fdd4f07268b9.md)
- [Link 5](../optional-readings/ref-52c5efffa5b8.md)

## Page 24

Monitoring at scale

24

## Page 25

Behavior across executions

Execution traces are useful for debugging when you know there's a problem.
What to do with a large collection of traces?

Reading every trace takes too long

Existing checks only cover behavior we thought to test

A lower score does not explain what changed

Transluce · Terminal-Bench investigation ↗
Zhong et al. · Hodoscope ↗
25

### Page links

- [Link 1](../readings/arxiv-2604-11072.md)
- [Link 2](../readings/ref-5f9387d31d17.md)

## Page 26

Behavioral investigation

Using Transluce's Docent to investigate a regression in Terminal-Bench.

Success rate on Terminal-Bench (89
tasks, 518 runs)

GPT-5 Codex: 40%

GPT-5.1 Codex: 27%

Why does GPT-5.1 Codex succeed less
often than GPT-5 Codex with the same
harness?

Transluce · Walkthrough ↗
Our Docent analysis ↗
26

### Page links

- [Link 1](../optional-readings/docent-plan-81230a32-88e0-42af-82c9-101660ab1d89.md)
- [Link 2](../readings/ref-5f9387d31d17.md)

## Page 27

Pairwise comparison prompt

Prompt excerpt

❯ with docent, For each failed run, compare it to a successful run

from the other model on the same task and write a short
  paragraph explaining the cause of the failure.

Group results by model.

Output excerpt

⏺ I need to explain 108 failed runs: 79 for GPT-5.1-codex
  … and 29 for GPT-5-codex …

Our Docent plan · Pair and explain failures ↗
27

### Page links

- [Link 1](../optional-readings/docent-plan-81230a32-88e0-42af-82c9-101660ab1d89.md)

## Page 28

Paired trajectories in Docent

Select a comparison to read its explanation and follow citations into both runs.

code-from-image: GPT-5 Codex failed; GPT-5.1 Codex used OCR and succeeded.

Our Docent plan · Step $4, result ec42bd06 ↗
Open the cited OCR action ↗
28

### Page links

- [Link 1](https://docent.transluce.org/dashboard/9bafeb94-3f6e-4d03-bd01-1ae8476e3f6e/agent_run/083de394-6f2f-41e7-a290-24b7be803822?transcript_id=b2f312ef-9698-416a-b8ee-923328f8ff49&block_idx=56&target=block_content)
- [Link 2](../optional-readings/docent-plan-81230a32-88e0-42af-82c9-101660ab1d89.md)

## Page 29

Failure mode synthesis

Claude Code · prompt

❯ with docent, Based on the previous result, summarize

the difference in failure modes between the two models.

GPT-5.1 Codex

“GPT-5.1-codex runs out of time
before delivering.”

GPT-5 Codex

“GPT-5-codex delivers, but often in
the wrong form.”

Output excerpts from the synthesis of 108 paired failures.

Our Docent plan · Failure-mode synthesis ↗
29

### Page links

- [Link 1](../optional-readings/docent-plan-81230a32-88e0-42af-82c9-101660ab1d89.md)

## Page 30

Testing the timeout hypothesis

Claude Code · output excerpt · scored runs

Model          Scored runs   Pass rate   Timed out

GPT-5-codex         219          40%       69 (32%)
GPT-5.1-codex       265          27%      132 (50%)

Claude Code · prompt excerpt

❯ with docent, Filter to tasks where neither model times

out across all rollouts. … Then compute the macro-average
  reward per model on this subset of tasks.

Our Docent plan · No-timeout comparison ↗
30

### Page links

- [Link 1](../optional-readings/docent-plan-772c0920-0b0f-4355-a009-825d1dd553b4.md)

## Page 31

Testing with run metadata

On the 28 no-timeout tasks, average success is 0.500 vs. 0.429 for GPT-5.1 vs. GPT-5 Codex.

The ranking reverses on this subset

Our Docent plan · Query and results ↗
Transluce · Step 3 and caveats ↗
31

### Page links

- [Link 1](../optional-readings/docent-plan-772c0920-0b0f-4355-a009-825d1dd553b4.md)
- [Link 2](../readings/ref-5f9387d31d17.md)

## Page 32

Discovering behavioral patterns

32

## Page 33

Why not use model-as-a-judge?

Claude Opus 4.6 evaluates an agent inspecting Git history in SWE-bench.

After a link to the benchmark issue · 2/10 → 7/10

In this example, the judge needed a hint about which behavior to flag.

Zhong, Saxena, and Raghunathan · Hodoscope announcement · The Problem ↗
33

### Page links

- [Link 1](../optional-readings/ref-18261f112927.md)
- [Link 2](https://hodoscope.dev/blog/img/image10.png)

## Page 34

Discovering behavior clusters

Summarize trajectories or actions, then embed the summaries to group similar
behaviors.

Explore clusters and inspect examples to discover behaviors you had not thought to search for.

Examples: Hodoscope (CMU) · Embedding Atlas (Apple)

Zhong, Saxena, and Raghunathan · Hodoscope ↗
Apple · Embedding Atlas ↗
34

### Page links

- [Link 1](../optional-readings/ref-6fa32b7c7361.md)
- [Link 2](../readings/arxiv-2604-11072.md)
- [Link 3](../optional-readings/ref-18261f112927.md)

## Page 35

Representing actions

Summaries emphasize behavior across tasks; Hodoscope embeds action summaries into a
shared map.

Zhong, Saxena, and Raghunathan · Hodoscope, Figure 1 ↗
See also Embedding Atlas ↗
35

### Page links

- [Link 1](../optional-readings/ref-6fa32b7c7361.md)
- [Link 2](../readings/arxiv-2604-11072.md)

## Page 36

Analyzing behavior clusters

Compare models or setups to find distinctive clusters; Hodoscope marks overrepresented
behaviors in red.

Commit0
ImpossibleBench
iQuest / SWE-bench

Inspect the original actions to identify the behavior and judge it in context.

Zhong, Saxena, and Raghunathan · Hodoscope, Figure 2 ↗
36

### Page links

- [Link 1](https://arxiv.org/html/2604.11072v1#S3.F2)

## Page 37

Commit0 investigation

Benchmark setup

Recreate code removed from a
repository.

Earlier commits remained available
in Git history.

Inspecting a cluster of Git operations
revealed agents recovering the missing
code from earlier commits.

Zhong, Saxena, and Raghunathan · Hodoscope, Section 3.1 and Figure 2 ↗
37

### Page links

- [Link 1](../readings/arxiv-2604-11072.md)

## Page 38

Review at scale

Agents produce more context than a person can review in full.

Black Hat USA 2026 · The OpenAI–Hugging Face incident ↗
OpenAI · Incident report overview ↗
38

### Page links

- [Link 1](../optional-readings/ref-d8e6fd2ea614.md)
- [Link 2](../videos/video-87DyyMV0kCY.md)

## Page 39

Thanks!

Next lecture: Safety · Eric Wallace (guest lecture)

39
