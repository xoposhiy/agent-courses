# Module 1: Foundations of Evals

[Course index](../../README.md) · [Original source](https://global.discourse-cdn.com/dlai/original/3X/5/5/5511474bc19c467f66a1d5b76ae6301c58e464d5.pdf) · [Raw file](../../raw/slides/module-1.pdf)

Retrieved: 2026-11-13T17:18:06.733766+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Evaluating & Improving

Agentic Applications

Laurie Voss

## Page 2

Why evals matter

Module 1 · Video 1

## Page 3

Meet Northwind Apparel

Product

names

Sizes
Prices
Inventory

Product

details

## Page 4

Meet the Northwind support agent

Find suitable products

Check stock

Add to cart

## Page 5

Some tasks follow rules, others need judgment

Rule in code
Recommendation

Wool sweater, size L

Stock: 0

First winter 
camping trip

Hoodie

Fleece pullover

Deterministic
Requires 
judgment

Out of stock

Holds heat 
at night

Easy to 
layer

## Page 6

An agent works toward a goal

Instructions from Northwind

Goal: a winter
camping outfit

Tools: search catalog · 
check stock · add to cart

## Page 7

More you can build, harder to trust

Understand requests

Make judgments

Use tools toward a goal

A few new abilities
A huge range of possibilities

Support agents
Coding agents

Research tools
Tutoring apps

Travel planners
Data analysis

But can you trust what you’ve built?

## Page 8

The same request can produce different decisions

Cargo shorts
Summer wear
Fleece pullover
Cold-weather layer

Cargo shorts are a
great pick for
this trip!

A fleece pullover will
keep you warm
at camp.

Run 1
Run 2

One passing run doesn’t make it reliable

What should I wear 
on my first winter 
camping trip?

Request

Customer
First winter camping trip

## Page 9

A reasonable answer can hide a bad decision

Done! I added a sweater, 
cargo shorts, and a beanie 
to your cart.

What should I wear on my 
first winter camping trip?

Good answer,
wrong decision

Cart updated

These cargo shorts will 
keep you warm on your 
winter trip.

## Page 10

The result doesn’t show what the agent did

Done! I added a sweater, cargo 
shorts, and a beanie to your cart.

Search catalog
Check product

details
Check product

details

Recommend

products
Add to cart
What the 
agent did

What you 
see

Cart updated

Skipped

## Page 11

People ask in ways you can’t anticipate

What should I wear
for winter camping?

Here are some picks:
a T-shirt, cargo 
shorts, and sandals.

My friend invited me on a trip to 
the mountains. We’ll hike to a 
lake and camp for two nights. It’s 
winter, so we’ll cook over a fire. 
What should I buy in size large? 
A fleece, wool socks,
and a beanie will
keep you warm.

Said directly
Buried in a longer description

## Page 12

Every reply opens new paths

Customer

request

Recommends

products

Asks a 
follow-up

Asks a 
follow-up
Checks stock

“Too pricey”

“Wrong size”

“It’s in 
January”

“Why do you

ask?”

“Other 
options?”

“I’ll wait”

Test cases with

real variety

Keep checking

real use

## Page 13

Three reasons AI apps are harder to test

Behavior changes

run to run

Mistakes can look

like success

Too many 
situations to cover

Checking only code and tools misses these

## Page 14

Systematic evaluation gives you evidence

“I can prove it’s

working”
“I think it’s

working”
“I think it’s

working”

Against what the

task requires
Realistic situations
Repeated runs

## Page 15

Evaluate systematically 
as you scale

Evaluate before and after every change

Find where it

struggles

Change the…

Instructions

Evaluate again

Keep the change

Try something

else

Model

Tool

1
Look closely
at a few examples
2

## Page 16

The Evals Process Part 1

Module 1 · Video 2

## Page 17

Fixing one failure at a time leaves you guessing

Fixed this example

Solved the
broader problem?

Broke something

else?

## Page 18

The evaluation process in four parts

Observe
Benchmark
Evaluate
Improve

Analyze behavior,

group failures

Build test cases 
with clear criteria

Judge the results

and measure

Make changes, 
then test again

Monitor real use

## Page 19

Parts 1 and 2: Investigate and Define

Observe
Benchmark
Evaluate
Improve

Analyze behavior,

group failures

Build test cases 
with clear criteria

Overview in this video,

more in Module 2

## Page 20

A failure is a comparison

What should I wear on my 
first winter camping trip?

Cargo shorts
Summer wear

Fleece pullover
Cold-weather layer

What the agent did
What it should have done

Requirements: what to accomplish · what to get right · what to avoid

## Page 21

You can’t judge what you haven’t decided

No size given

What size do 
you wear?

Here are three warm 
jackets you might like.

PASS
FAIL

I need a warm jacket 
for winter camping.

Ask first
Suggest first

PASS
FAIL

## Page 22

Where requirements come from

Only recommend items that

are in stock

Requirements

Customer needs
Company

policies

People who know

the work

## Page 23

Make your expectations explicit

Suits the customer’s needs

Reflects the catalog and stock

+ Clarify and add as you learn

Requirements
Task: recommend clothes

More than one good answer

Fleece pullover
Hoodie

## Page 24

Start with error analysis

Observe
Benchmark
Evaluate
Improve

Look closely
at a few examples

Compare with

requirements
Group into patterns

## Page 25

Are the instructions clear

and complete?

Can the model follow

them reliably?

Two kinds of problems to tell apart

Missing: check the size

Instructions: Recommend 
warm clothes that suit the 
customer’s trip.

Instructions: Recommend 
clothes that suit the trip, in 
sizes that are in stock.

Suggests a sold-out jacket

## Page 26

Part 2: Define

Observe
Benchmark
Evaluate
Improve

Build test cases

Define criteria

Look closely at
a few examples

Compare with

requirements

Group into

patterns

## Page 27

Each case pairs a situation with what you expect

Fleece and 
hoodie in stock

Recommend warm, 
in-stock layers
What should I wear on my 
first winter camping trip?

I need a warm jacket for 
winter camping.

Do you have the wool 
sweater in size L?

No size given
Ask for the size first

Stock: 0
Say it’s out of stock

Customer query
Context
Expected outcome

Evaluation set

## Page 28

Test more than past failures

Past failures
Everyday work
Challenging

situations

Cargo shorts
for a winter trip

A fleece for
a cold night

A long request,

no size given

Reuse after every change · Update as you learn

## Page 29

A rubric is a written guide

What to check in each result

What counts as pass or fail

Information needed to decide

Pass/fail examples, explained

Rubric

## Page 30

Check each requirement separately

Size L is in stock

Availability

Not warm enough

Suitability

Cargo shorts, size L

## Page 31

Try the rubric on real results

I need a warm jacket 
for winter camping.

This jacket will work 
well for your trip.

PASS
FAIL

You may need more information or a clearer requirement

Suits the customer’s needs

## Page 32

Module 1 · Video 3

The Evals Process Part 2

## Page 33

Part 3: Evaluate

Observe
Benchmark
Evaluate
Improve

Build test cases

Define criteria

Look closely at a

few examples

Compare with

requirements

Group into

patterns

Build evaluators

Run test cases,

record results

## Page 34

Three ways to judge the results

Code-based
LLM judge
Human-based

Is the item in stock
in the requested size?

Do these clothes suit
a winter camping trip?
Is this a good answer

for this customer?

## Page 35

Build evaluators in code or on a platform

Both kinds of evaluator,

no platform needed

Your own Python code

Runs the checks and
organizes the results

An evaluation platform
</>

Phoenix · open source · from Arize

## Page 36

Check the evaluator against people

Reviewer

A person

Evaluator
Code or LLM judge

PASS
FAIL

Same result,
same criteria

Disagree? Check the
evaluator, the reviewer

or the criteria

## Page 37

Measure across cases and repeated runs

Customer’s needs met in 80% of runs

Run 1
Run 2
Run 3
Run 4
Run 5

Winter camping layers

Stock check

Request with no size

Same request, 
different result

Some request types

fail more often

## Page 38

Part 4: Optimize

Observe
Benchmark
Evaluate
Improve

Build test cases

Define criteria

Look closely at a

few examples

Compare with

requirements

Group into

patterns

Build evaluators

Run test cases,

record results

Decide what 
needs attention

Investigate 
before changing

## Page 39

Match the fix to what went wrong

What the tool returned
What the agent said
The agent’s instructions

Merino wool 
sweater. Machine 
washable on 
wool cycle

Catalog

Use tools when helpful. 
Give concise answers.
Here is what to keep in mind:

●
Machine washable on wool cycle 
●
Cool-water machine wash
●
Wool-specific detergent
●
Cedar blocks for moths

Never state a product 
detail unless a tool 
result supports it.

Other fixes to try
Better information
Tools and workflow
A different model

## Page 40

Change the agent, but keep the evaluation fixed

Agent v1
Agent v2

Test cases
Test cases

Evaluators
Evaluators

Baseline results
New results

New instruction

## Page 41

Catch what your change breaks

Merino wool care

Hiking shoe materials

Denim jacket care

Jeans size availability

New season items

Basic shirt colors

Regression: losing behavior that worked before

Did the target improve?
Still doing what it did well?

## Page 42

Improvement can introduce tradeoffs

●
Less unsupported advice
●
Target failure fixed
●
Catalog-backed answers

●
Unnecessary tool calls
●
Slower responses
●
Higher cost

Keep
Revise
Try something else

Better than before doesn’t mean good enough

## Page 43

The evaluation cycle

Observe
Benchmark
Evaluate
Improve

Analyze behavior,

group failures

Build test cases 
with clear criteria

Judge the results

and measure

Make changes, 
then test again

Monitor real use

## Page 44

The output doesn’t show what the agent did

What should I wear on my 
first winter camping trip?

A fleece pullover will keep 
you warm at camp.

What you see
What the output doesn’t show

Which information did it use?

Which tools did it call?

Did it skip something important?

## Page 45

Traces

Module 1 · Video 4

## Page 46

Input and output hide the steps between

01

Look up

jacket

02

Check 
inventory

02

Check 
inventory

03

Interpret

results

04

Answer

You can’t see this 
from the answer

Only this!

Is this jacket 
available in my size?

Yes, it’s available in 
your size.

Trace: a window into

agent behavior

## Page 47

Each step in a trace is recorded as a span

Look up order
Check return

policy
Request refund

Trace

Span: order lookup
Span: refund

A span is one recorded operation, with a

beginning and end

## Page 48

A trace shows how the spans fit together

Look up order
Check return

policy
Request refund

Refund request

Root span

## Page 49

What a tool-call span records

Look up

order

{
  "name": "lookup_order",
  "span_type": "tool",

"input": {
    "order_id": "A99"
  },

"output": {
    "item": "Wool jacket",
    "quantity": 1,
    "purchase_price": 89.00
  }
}

Which operation ran, 
and its type

What was sent to 
the tool

What came back

## Page 50

What a model-call span records

Model call

{
  "input": {
    "customer_message": "I want to return my jacket",
    "instructions": "You are Spark, a support agent",
    "tool_results": "Order A99: wool jacket, $89.00"
  },

"output": {
    "type": "tool_request",
    "tool": "process_refund"
  },

"attributes": {
    "model_version": "v2.1",
    "prompt_version": 3,
    "total_tokens": 412
  }
}

## Page 51

A trace connects the steps in a run

Trace

Model call
Model call
Model call
process_refund

{"order_id": "A99"}
{"order_id": "A99"}

{"price": 89.00}
{"status": "done"}

Your refund 
is on its way

lookup_order

## Page 52

Spans record timing

Correct answer, unnecessary work

0.8 s

0.6 s

0.6 s

3.0 s
3.0 s

0.6 s

Model call

lookup_order

lookup_order

Model call

process_refund

Time

Model call or order lookup?

## Page 53

A trace doesn’t show the model’s internals

Trace

Model call
Model call
Model call
process_refund
lookup_order

Inside the model: not recorded
"reasoning": "Order A99 
qualifies for a refund"

Reasoning text is generated output, not a view inside

## Page 54

Instrumentation records the spans

Your own functions

Tracing integration

Source of the spans
What gets recorded

You add recording around code

the integration doesn’t cover

Captures model calls and tool

calls: inputs, outputs, timing

## Page 55

Inspect traces in Phoenix

Your agent

Tracing integration

Phoenix

1  Open a run

2  Follow the tree

3  Select a span

## Page 56

A missing span isn’t a skipped step

Model call
Look up order
Model call

Trace

Absent span ≠ skipped action

not instrumented

## Page 57

Follow the trace to where the decision went wrong

Look up order
Request refund
Respond

Refund request

Root span

Start here
Then open the spans that led to it

not completed
“Your refund
is on its way”

!

## Page 58

Evaluate one operation or the whole run

Look up order
Request refund
Respond

Refund request

Refund handled correctly?

Right order looked up?

## Page 59

Record your assessment as an annotation

Look up order
Request refund
Respond

Refund request

Annotation
Label: fail
Score: 0
Explanation: refund not completed, but

the reply said it was on its way

## Page 60

Trace vs. session

I’d like a refund for order A99
How long will the refund take?

{
 "trace_id": "t1",
 "session_id": "s42",
 "spans": 4,
 "output": "Refund requested"
}

{
 "trace_id": "t2",
 "session_id": "s42",
 "spans": 2,
 "output": "5 business days"
}

Trace
Trace

Session ID
