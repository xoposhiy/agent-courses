# Lecture slides: week6

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/assets/lecture_slides/week6.pdf) · [Raw file](../../raw/slides/week6.pdf)

Retrieved: 2026-11-13T16:40:58.222032+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Shreya Havaldar

Week 6

The Agentic Harness

COMS 4995-15

## Page 2

●
HW 2 is due today

○
You don’t need to ask for permission to use late days!!

●
HW 3 will be released tomorrow

Announcements

2

## Page 3

Even with instruction tuning, LLMs struggle with complexity:

●
They are fundamentally next-token predictors.
●
They do not inherently manage control flow.
●
They struggle with long-horizon tasks.
●
No built-in mechanism for recovering from failure

We need structure around individual model calls.

Why are single prompts not enough?

3

## Page 4

Example task:

“Research competitors to my startup, determine their business 
models, compare positioning, generate strategy memo for profit.”

How many distinct things are we actually asking the model to do here?

Single Prompts: Failure Modes

4

## Page 5

Example task:

“Research competitors to my startup, determine their business 
models, compare positioning, generate strategy memo for profit.”

How many distinct things are we actually asking the model to do here?
Research → extract → compare → reason → write.

Single Prompts: Failure Modes

5

## Page 6

Example task:

“Research competitors to my startup, determine their business 
models, compare positioning, generate strategy memo for profit.”

Failure modes: Hallucinated data, missed constraints, incorrect structure, 
shallow reasoning

→ Too much cognitive load is forced into one generation.

Single Prompts: Failure Modes

6

## Page 7

Long-horizon tasks require extended sequences of actions over a 
prolonged period (e.g., several minutes) to achieve a specific goal.

Examples:

1.
Schedule a meeting with my advisor next week
2.
Refactor this repository from Java to Python

Long-Horizon Tasks

7

## Page 8

Long-horizon tasks require:

1.
Decomposition
2.
State tracking
3.
Tool use
4.
Branching
5.
Error recovery

Long-Horizon Tasks

8

## Page 9

Schedule a meeting with my advisor next week

-
Access my calendar, check when I am free, access my advisor’s 
calendar, check when my advisor is free, find the intersection of this 
set, use a calendar tool, send the meeting invite

Long-Horizon Tasks

9

## Page 10

Refactor this repository from Java to Python

-
Understand the repo goal, understand the repo structure, divide repo 
into standalone refactorable modules, write test cases to ensure correct 
refactoring, iteratively {refactor module → run tests → edit until tests 
pass}

Long-Horizon Tasks

10

## Page 11

METR

https://metr.org/time-horizons/

“To estimate the time horizons of frontier AI agents, we first estimate the duration it 
takes a human expert to complete each of our tasks. For each agent, we fit a 
logistic curve to predict the probability it successfully completes tasks as a function 
of human task duration.”

### Page links

- [Link 1](https://metr.org/time-horizons/)

## Page 12

12

## Page 13

[No extractable text on this page. See the original PDF.]

## Page 14

As agents become capable of

longer tasks, managing the 
sequence of actions becomes

increasingly important.

## Page 15

An LLM is not an agent

-
it is a function that maps input text → output text

An individual LLM call does not inherently:

-
retain persistent task state
-
call itself again
-
manage a multi-step workflow
 
Something outside the LLM has to control these things

The Agent Harness

15

## Page 16

Agent harness: the runtime infrastructure surrounding an LLM that turns 
individual model calls into a stateful system.

The harness is responsible for:

●
constructing context
●
maintaining task state
●
controlling execution
●
deciding what happens next
●
deciding when to stop

The Agent Harness

16

## Page 17

17

## Page 18

1.
User request

2.
Build context

3.
Call LLM

4.
Interpret output

5.
Update state

6.
What happens next?

7.
continue / branch / replan / finish

The Harness Loop

18

## Page 19

1.
User request

2.
Build context

3.
Call LLM

4.
Interpret output

5.
Update state

6.
What happens next?

7.
continue / branch / replan / finish

The Harness Loop

19

Designing your agent well is 
important for this step to run

smoothly!!

## Page 20

STATE = Everything the system currently knows

CONTEXT = What this LLM call is allowed to see

You have to determine what parts of state to select and incorporate 
into the context of the next LLM call

State != Context

20

## Page 21

STATE = Everything the system currently knows

CONTEXT = What this LLM call is allowed to see

You have to determine what parts of state to select and incorporate 
into the context of the next LLM call

-
You almost never want to include ALL information into the context 
(token cost, confusion due to extraneous information, etc.)

State != Context

21

## Page 22

Static vs. dynamic workflows

22

Static
Dynamic

Code decided what happens next
Model participates in deciding 
what happens next

Predefined control flow
runtime control flow

model fills in individual steps
can adapt to observations

## Page 23

Static or Dynamic? (5 min)

23

A customer support

system classifies a 
user request as billing,

looks up the user’s 
account information, 
and writes a response.

A coding assistant 
investigates a latency 
spike, checks metrics 
and logs, and decides

what to inspect next 
based on what it finds.

You ask a travel 
planning system for a 
trip under $1,000. The

system searches 
options, adjusts the 
itinerary, and gives you 
a suggested travel plan.

## Page 24

Static or Dynamic? (5 min)

24

A customer support

system classifies a 
user request as billing,

looks up the user’s 
account information, 
and writes a response.

Static

A coding assistant 
investigates a latency 
spike, checks metrics 
and logs, and decides

what to inspect next 
based on what it finds.

Dynamic

You ask a travel 
planning system for a 
trip under $1,000. The

system searches 
options, adjusts the 
itinerary, and gives you a

suggested travel plan.

Dynamic

## Page 25

More static 
More dynamic

Single prompt → Chaining → Routing → Planning → Agentic loop

Developer specifies 
LLM determines 
control flow 
control flow

A spectrum of control

25

## Page 26

Single Prompt: no developer involvement

Chaining: developer specifies the path

Routing: developer specifies multiple possible paths

Planning: model creates the path(s)

Agentic loop: model repeatedly plans and acts until goal is reached

A spectrum of control

26

## Page 27

Prompt chaining decomposes a task into sequential stages:

𝑂𝑢𝑡𝑝𝑢𝑡𝑖→𝐼𝑛𝑝𝑢𝑡𝑖+1

It creates a pipeline of transformations, where the output of 
prompt 𝑖 serves as the input to prompt 𝑖+1

Prompt Chaining

27

## Page 28

[No extractable text on this page. See the original PDF.]

## Page 29

We're moving complexity 
out of a single generation 
and into the application's

architecture.

## Page 30

Instead of: “Summarize and analyze this report.”

1.
Summarize
2.
Extract trends
3.
Extract evidence
4.
Generate executive memo

summary = llm("Summarize this document: " + doc)
trends = llm("Extract key trends from: " + summary)
memo = llm("Write executive memo using: " + trends)

Example: Document Workflow

## Page 31

Intermediate outputs are useful

When implementing prompt chaining, keeping track of intermediate states:

{
  "trends": \[...\],
  "risks": \[...\],
  "recommendations": \[...\]
}

1.
Easy revising or retrying (upon errors)
2.
Easy revision to an earlier state

## Page 32

Prompt Chaining ≠ Chain-of-Thought

Chain-of-thought

ONE model call → model reasons → answer

Prompt chaining

model call → program receives output → model call → 
program receives output → … → answer

*Prompt chaining is an application architecture pattern, not a prompting technique.

## Page 33

Smaller stages:

-
reduce instruction overload
-
isolate responsibilities
-
make intermediate results visible
-
make failures easier to localize

Chaining doesn't prevent errors. But, it does make errors easier to 
find and recover from.

Chaining Improves Reliability

33

## Page 34

Limitations of Chaining

Failure Propagates Through a Chain

Decomposition creates inspectable failure points, but downstream 
steps still inherit upstream mistakes.

Chaining assumes:

●
Known task structure
●
Linear progression
●
Identical workflow for every input

## Page 35

Limitations of Chaining

Chaining is only applicable to a subset of tasks:

●
there is a natural sequence of transformations
●
later steps genuinely depend on earlier outputs
●
intermediate results are useful artifacts

Probably don't chain:
“Rewrite this paragraph more concisely”

Probably do chain:
“Read 100 reviews → extract complaints → group themes → 
write report”

## Page 36

Limitations of Chaining

Chaining is only applicable to a subset of tasks:

●
there is a natural sequence of transformations
●
later steps genuinely depend on earlier outputs
●
intermediate results are useful artifacts

Probably don't chain:
“Rewrite this paragraph more concisely”

Probably do chain:
“Read 100 reviews → extract complaints → group themes → 
write report”

## Page 37

Control Flow as a Graph

Node = computation
Edge = what happens next
State = information carried through the graph

Read 
100 
reviews

extract 
complai
nts

Group 
themes

Write 
report

## Page 38

Control Flow as a Graph

Node = computation
Edge = what happens next
State = information carried through the graph

Read 
100 
reviews

extract 
complai
nts

Group 
themes

Write 
report

What happens if a node can have multiple possible next steps?

## Page 39

Routing

Routing decides:

Which prompt, model, or workflow should handle this input?

It introduces branching control flow.

## Page 40

Why Routing is Necessary

Example: Customer support agent

User input could be related to:

●
Billing

●
Technical bug

●
Refund

●
Feature inquiry

Different problems require different 
specialized prompts, tools, etc.

## Page 41

Routing Chooses Among 
Predefined Paths

Developer still determines:

1.
What routes exist
2.
What each route means
3.
What each route does

Read 
100 
reviews

Extract 
complai
nts

Extract 
praises

Find 
bots

## Page 42

Routing can be for prompts, models, or workflows

Example: deciding 
what information to

use for RAG

## Page 43

Routing can be for prompts, models, or workflows

Example: Maximizing

performance/cost

## Page 44

Routing can be for prompts, models, or workflows

Example: Multi-agent

systems

Each agent has its own internal 
chaining, routing, tool-calling, etc.

## Page 45

Rule-Based Routing

if "refund" in query:
    handler = refund_prompt
elif "error" in query:
    handler = technical_prompt

LLM-Based Routing

category = llm(
  "Classify this query into: \[refund, tech, refund, other\]: "

+ query
)

## Page 46

Embedding-Based Routing

1.
Compute embedding of input
2.
Compare to category embeddings
3.
Select nearest match

Multi-LLM Routing

# Route based on: Complexity, Cost, Latency, Specialization
if complexity_score(query) < 0.3:
    model = small_model
else:
    model = large_model

## Page 47

Routing is a classification problem

r(x) → y

-
(x): current input/state
-
(y): destination

Rule, embedding, and LLM-based routing differ mainly in how we 
implement (r).

## Page 48

Routing is a classification problem

Routes: FAQ pages to feed into the LLM based on an input query
1. Billing
2. Refund
3. Account

Input: “I cancelled yesterday but was charged this morning. Can I 
get my money back?”

What FAQ page should we use?

## Page 49

Routing is a classification problem

Routes: FAQ pages to feed into the LLM based on an input query
1. Billing
2. Refund
3. Account

Input: “I cancelled yesterday but was charged this morning. Can I 
get my money back?”

Routing becomes difficult when categories are not mutually exclusive.

## Page 50

Recap: Routing vs Chaining

Chaining:

●
Linear
●
Predictable

Routing:

●
Branching
●
Input-dependent

## Page 51

Recap: Routing vs Chaining

Chaining:

●
Linear
●
Predictable

Routing:

●
Branching
●
Input-dependent
Con: Both

assume 
predefined 
workflows.

## Page 52

Planning

Planning enables goal-directed behavior:

1.
Interpret + set goal
2.
Decompose into task(s)
3.
Execute task(s)
4.
Observe results
5.
Replan using observations

It introduces adaptive control.

## Page 53

A plan is not always a list

Identify candidates

↓
┌──────────|──────────┐

↓
↓ 
↓
Research A Research B Research C

└──────────|──────────┘

↓
Compare

↓
Recommend

Some tasks have 
dependencies. So, a plan may

be represented as a DAG

## Page 54

Iterative Planning

Standard:

1.
Plan once
2.
Execute

Iterative (supports uncertainty):

1.
Plan partially
2.
Execute
3.
observe
4.
Adjust

## Page 55

Agentic Planning Loop

An agent integrates planning, routing, tool use, memory, and looping control

while not goal_satisfied:
    plan = llm("What should I do next?")
    action = select_tool(plan)
    result = execute(action) #can involve prompt chaining
    update_memory(result)

## Page 56

Planning vs. ReAct

ReAct:

-
Reasoning + acting in a tight loop (only plans next action)
-
No explicit global plan

-
Used for a single task

Planning:

-
Planner generates explicit sequence of tasks before execution
-
Used for a large goal containing many tasks (e.g. long-horizon)

-
Tasks are often executed by ReAct Agents

## Page 57

Planning vs. ReAct

## Page 58

Planning Strategies

Strategy 
Replan when?

Plan-then-execute 
Never

Adaptive 
Something goes wrong

Continuous 
After every observation

Hierarchical 
When a sub-plan is needed/completed

## Page 59

Plan-then-execute

Advantages:

-
Simple
-
Less repeated deliberation
-
Global structure

Weakness:

-
The entire plan is based only on 
information available before 
execution begins.
-
Brittle and cannot adapt

Goal
↓
Generate plan
↓
1 → 2 → 3 → 4 → answer

## Page 60

Plan-then-execute

Initial plan: Find the cheapest nonstop flight from NYC to London.

1. Check airline A
2. Check airline B
3. Compare
4. Book cheapest

Observation: Airline A has no nonstop service that day.
Execution reveals information the planner did not have.

## Page 61

Adaptive Planning

Advantages:

-
Keeps global structure
-
Can adapt to unknown 
information

Weakness:

-
Must detect when to replan
-
Can continue with a bad plan for 
too long

execute step

↓
observe

↓
Is plan still valid?

↙
 
↘
yes 
no
↓
 ↓
continue 
replan

## Page 62

Continuous Planning

Advantages:

-
Maximum adaptability – 
incorporates every new 
observation

Weakness:

-
more deliberation
-
more latency/cost
-
easier to “wander”

-
LLM may lose sight of final 
goal, since it only ever plans 
the immediate next step

observe
↓
reconsider
↓
choose next action
↓
observe

## Page 63

Hierarchical Planning

Advantages:

-
Plan high-level first, then plan 
each subtask only when needed  
-
Saves time + avoids over-planning

Weakness:

-
More complex to implement
-
Mistakes in high-level plan can 
propagate down into subplans

Plan Japan Trip

↓
┌──────|──────┐
Transportation
Hotels
Activities
|
|— search flights
|— compare flights
|— select flights
|— search trains
|— check connections

## Page 64

How big should a planning step be?

Too coarse
Too broad
Useful

1. Build website
2. Launch

1. Open editor
2. Create file
3. Type <h>
4. Type <br>
...

1. Define site structure
2. Implement pages
3. Add content
4. Verify navigation
5. Deploy

Goal: Build and launch a course website.

* A useful step should be independently 
executable and produce an observable result.

## Page 65

Design Principles: Recap

When building an agent…

-
Use chaining when structure is predictable + intermediate outputs needed.

-
Use routing when inputs vary widely and specialization is important.

-
Use static planning when overall goal is complex but easily decomposable.

-
Use dynamic planning when overall goal is complex and plans need multiple 
iterations with intermediate feedback.

Most agents use multiple of these patterns in combination.
