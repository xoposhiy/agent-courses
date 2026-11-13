# Module 5: Improving Agentic Applications

[Course index](../../README.md) · [Original source](https://global.discourse-cdn.com/dlai/original/3X/b/f/bf828ca0e9d7ad63146803dca92ed5b3d204e39b.pdf) · [Raw file](../../raw/slides/module-5.pdf)

Retrieved: 2026-11-13T17:18:11.167310+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Improving agentic

applications

Module 5

## Page 2

Planning an 
improvement test

Module 5 · Video 1

## Page 3

Improve

Plan an improvement test

Observe
Benchmark
Evaluate

Target behavior
Candidate change
Stable comparison

## Page 4

Experience is not current handling ability

Experience with

large dogs

Buddy, 130 lb
pulls strongly on walks
Agent: approved

Evaluator:

rejected
Current handling ability: not assessed

Failed matches

Physical capacity

wasn’t assessed

Experience with large dogs

was treated as sufficient

The dog’s pulling strength

wasn’t considered

## Page 5

Find a behavior worth improving

Past experience treated

as enough evidence

Physical capacity

wasn’t assessed

Experience with large dogs

was treated as sufficient

The dog’s pulling strength

wasn’t considered

Assess current physical

handling ability

QA

## Page 6

Write an eval for a capability

Don’t schedule me for walks after six

Pamela

Agent

Regression eval:
preserve an ability

Capability eval:
develop an ability

New capability

Expected to fail at first → Target to develop

## Page 7

A plausible answer can add unsupported claims

How should I care for the 
merino wool sweater?

Here is what to keep in mind:

●
Machine washable on wool cycle
●
Cool-water machine wash
●
Wool-specific detergent
●
Cedar blocks for moths

Machine washable on wool cycle

Faithfulness

error
Agent

Unsupported product claims

## Page 8

Test a grounding hypothesis

Agent
Baseline

Agent
Grounding rule

Use tools when helpful.

Give concise answers.

Use tools when helpful.

Give concise answers.
Never state a product detail unless a tool

result supports it.

Machine washable on wool cycle.
Use only retrieved care information

A hypothesis, not a proof

## Page 9

Change one thing, keep the comparison stable

Agent
Baseline

Agent
Grounding rule

Same cases · Same evaluators · Same model

Same other configuration

Hypothetical: score +8 points

Different cases?
Different evaluators?
Different model?

## Page 10

Test capability and protect known-good behavior

Merino wool care

Other unsupported product claims

Does it improve?

Capability

Sizing questions

Product-information requests

Does it still work?

Regression protection

Capability cases
Known-good cases

## Page 11

Set the bar before you iterate

Value of improvement
Safety /
policy reliability

Remaining 
regressions + effort

Good enough for this application?

Target behavior
Candidate change
Stable comparison

## Page 12

Comparing versions

and assessing

tradeoffs

Module 5 · Video 2

## Page 13

Run the improvement comparison

Observe
Benchmark
Evaluate
Improve

Save cases
Run both versions
Inspect changes

Capability
Regression

## Page 14

Save the cases you will reuse

Faithfulness traces: unsupported product details

Merino wool care

Other unsupported product claims

Target improvement

Sizing questions

Product-information requests

Protect working behavior

Northwind faithfulness failures
Known-good cases

## Page 15

Run the same experiment on both versions

Agent
Baseline

Agent
Grounding rule

Same model · Other instructions · Evaluators

Dataset

Experiment

Evaluators

Faithfulness

Builder

Task

One question → 
Northwind → Response

Apply the same task

to every example

Code 
evaluator
Results + Traces

Merino care

Known-good

## Page 16

Keep the care answer grounded

How should I care for the merino wool sweater?

Here is what to keep in mind:
Machine washable
on wool cycle
Cool-water machine wash
Wool-specific detergent
Cedar blocks for moths

Machine washable on wool cycle

Agent

Faithfulness: unsupported claims

Baseline
Grounding rule

The sweater can be machine

washed on the wool cycle.

Faithfulness: improved in this case

## Page 17

The answer stayed correct; the trajectory changed

Agent
Baseline

Agent
Grounding rule

Action / tool call
Trajectory
Session
System outcome

What size should I get?
Known-good
Sizing information already available

Same correct answer

Trace · same question + context

Uses available information
No additional lookup

Trace · same question + context

Redundant product lookup
One additional lookup

Hypothesis: fresh evidence required?

## Page 18

Read failure categories separately

First-time

volunteer

Buddy, 130 lb

Experienced 
handlers only

First-time

volunteer
Daisy, 45 lb, calm

Unsafe matches ↓
Eligible volunteers rejected ↑

One overall score can hide both movements

## Page 19

Decide whether the tradeoff is worth it

Agent
Baseline

Agent
Grounding rule

Faithfulness: unsupported

Final-answer correctness: correct

Redundant tool use: none

Faithfulness: grounded

Final-answer correctness: correct

Redundant tool use: extra lookup

Faithfulness

Code evaluator
Risk of unsupported claims
Tool cost + latency

Next hypothesis: use available support; look up only when missing

## Page 20

Weigh value, severity and effort

Another iteration?

Value of improvement
Severity of
remaining failures
Engineering effort

QA

Large cluster
Smaller group
Rare cases

Rare safety failure can still matter

## Page 21

Let the comparison guide the next decision

Required performance
Acceptable regressions?

Good enough for now
Another round

Open changed traces
Evidence for the
next intervention

Data
Prompt
Tools
Workflow
Model

## Page 22

Choosing where

to intervene

Module 5 · Video 3

## Page 23

Choose the intervention from the evidence

Observe
Benchmark
Evaluate
Improve

Locate the failure
Consider interventions
Start from evidence

Northwind: extra sizing lookup

Prompt · Data · Tools · Workflow · Model

Where does the failure show up?

## Page 24

Start at the simplest plausible layer

Data quality
Does the agent have 
the right information?

Prompting
Are the instructions 
clear enough?

Tools & workflow
Can the agent act 
correctly and in the 
right order?

Model
Is the model capable 
enough for the task?

Hyperparameters
Do settings materially 
affect the behavior?

## Page 25

Start with the data

Maria
First-time volunteer

Atlas
pulls hard

Agent
Matches Atlas with Maria

Experienced handler required: blank

Prompt workaround?
“Make sure you read the behavior notes before deciding.”

Data quality

## Page 26

Populate the requirement at the source

Maria
First-time volunteer

Atlas
pulls hard

Experienced handler

required: yes

Data-entry / processing rule

Same eval again: did the failure disappear?

Data quality

## Page 27

Clarify the requirement in the prompt

Can you book me with Pepper

for Saturday afternoon?

Great, you’re booked

with Pepper
for Saturday at 2 PM.
Agent

Pamela
Can safely handle

large dogs
Record complete

Pepper, 100 lb

Retrieve record

Pamela

Eligibility check

missing

Match volunteer
and dog: Pepper

Create booking

Saturday, 2 PM

Does the prompt require the check?

Prompt

## Page 28

Clarify the requirement in the prompt

Always check eligibility before scheduling an outing

Pamela
eligible → continue

Volunteer 2983
not eligible → stop

Prompt

## Page 29

Test beyond the examples you gave

Prompt examples

Large dog
Large dog

Different test cases

Small dog
Medical restriction

Different wording

Learn the requirement, not a narrow pattern

Prompt

## Page 30

Give tools a clear contract

Tool contract: when to use it + possible results + next action

eligible
continue

not eligible

stop

no match
ask for identifying

information

No match.
Agent

Prompt requires an eligibility check

What happens next?

Tools & 
workflow

## Page 31

Make the required check part of the workflow

Receive request
Check eligibility
Schedule

Pamela
Agent
Pepper, 100 lb

Still skipped despite clear instructions?
Tools & 
workflow

## Page 32

Every added step has a cost

Northwind sizing
One additional lookup

Latency
API cost
Another failure point

What size should I get?
Known-good
Sizing information already available

Required safety step
Optional step

Test removing an optional step → Same evals

## Page 33

Consider the model after local layers

Local interventions

Agent
Current model

Agent
Candidate model

Many requests affected

Latency · Cost

Merino wool care

Other unsupported

product claims

Sizing questions

Product-information

requests

Capability cases
Known-good cases

Same evaluation suite

Model

Data
Prompt
Tools & workflow

## Page 34

Tune sampling when variability is the problem

Temperature
Sampling
Output variability

If the model exposes these settings

Missing field
Undefined no match
Missing eligibility

instruction

Match the setting to a variability problem

Hyperparameters

## Page 35

Match the change to the evidence

Where does the evidence point?

Missing or 
inconsistent

information

Unclear 
requirement

Execution

difficulty

Task still
too hard

Sampling

problem

Data quality

Prompting

Tools & workflow

Model

Hyperparameters

## Page 36

Refining a change

after a regression

Module 5 · Video 4

## Page 37

Refine a change after a regression

Observe
Benchmark
Evaluate
Improve

Care: grounded
Sizing: extra lookup
Evidence for
the next change

Northwind: first grounding rule

## Page 38

The answer stayed correct; the trajectory changed

Agent
Baseline

Agent
Grounding rule

What size should I get?
Known-good
Sizing information already available

Same correct answer

●
Uses available information
●
No additional lookup

Trace: same question + context

●
Redundant product lookup
●
One additional lookup

Same request
Same available information
Product tool works

Decision to make an extra lookup

## Page 39

Investigate the prompt first

Data: present
Tool: working, 
unnecessary lookup
Changed instruction

Does grounding imply a fresh lookup?

Sizing information already available

Prompt

## Page 40

Make the ambiguity visible

Never state a product detail unless a tool result supports it.

Earlier tool result

Current context
Retrieve evidence again?

Care: supported 
information only

Prompt

## Page 41

Clarify when another lookup is needed

Never state a product detail unless supported by the information available. If the 
information available is insufficient, call the product tool to get additional information

Candidate refined rule

Use available
catalog information
Lookup if insufficient
Preserve grounding

Hypothesis → Run another experiment

Prompt

## Page 42

Compare three versions on the same benchmark

Baseline
Grounding rule
Refined rule

Capability cases
Known-good cases

How should I care for the

merino wool sweater?
Machine washable on wool

cycle.

What size should I get?

Sizing information

already available
Faithfulness
Code evaluator

Faithfulness: still grounded?

Redundant tool use: removed?

Other known-good behavior · Tool use · Latency + cost

Same benchmark

## Page 43

If the refined rule works as hoped

Agent · Baseline
Agent · Grounding rule
Agent · Refined rule

How should I care for the

merino wool sweater?
Machine washable on wool

cycle.

What size should I get?

Sizing information

already available
Faithfulness
Code evaluator

Care:
Unsupported claims

Sizing:
No additional lookup

If other cases stay stable, keep the improvement

Hypothetical outcome

Care:
Grounded

Care:
Grounded

Sizing:
One additional lookup

Sizing:
No additional lookup

Same benchmark

Capability cases
Known-good cases

## Page 44

Different results guide the next iteration

Agent
Refined rule

Fewer lookups,
unsupported claims return

Sizing fixed,
new problem elsewhere

Alternative outcomes

Inspect changed

cases

More specific

candidate
Test again

Alternative A
Alternative B

## Page 45

Keep the cases that protect what you learned

Other unsupported product claims

Not yet reliable

Former role:
Capability target

Machine washable on wool cycle.

Fixed behavior: preserve

Capability cases
Regression protection,

once reliable

Unfixed failures: learn

Failure → Evidence-based change → Compare and inspect

How should I care for the 
merino wool sweater?

The sweater can be machine 
washed on the wool cycle.
Expected:

Tool:

## Page 46

Improving agents

after deployment

Module 5 · Video 5

## Page 47

Find the next targets in production

Observe
Benchmark
Evaluate
Improve

Unfamiliar wording
Missing or
combined context
New targets

Live users

## Page 48

Production changes how requests are phrased

I have limited mobility.
Is Pepper free Saturday, and if

not, can I switch to Sunday?

Offline wording
Production wording

I can only walk for about

ten minutes.

Right answer
2 → 14 seconds
Changed shelter policy
New dog record fields

The benchmark covers only the situations it contains

## Page 49

Keep offline tests and add production evidence

Repeatable offline benchmark

Mobility wording
Working scheduling requests

Capability cases
Known-good cases

Code evaluator

Candidate change → Same benchmark → Before release

Automated checks
Product-specific release rule
QA

Production 
monitoring
Manual review
User feedback
A/B testing

## Page 50

Monitoring locates; review explains

Production monitoring
Manual review

Policy flags

Tool use

Response latency
Hypothetical: 37 eligibility failures

Policy evaluator

Where should I look?

Inspect live traces

Skipped check?
Wrong argument?

Ignored result?
Wrong conclusion?

Count → Trace → Pattern

## Page 51

Use feedback to choose what to inspect

Behavioral: abandon the conversation

User feedback

Inspect the interaction

A signal points to an interaction; it does not diagnose the cause

Explicit: thumbs-down

## Page 52

Compare versions on real traffic

Agent
Current

Agent
Revised

Real traffic

Policy failures
Follow-up turns
Accuracy
Latency

Monitoring:

where

Review:
what happened

Feedback:
user problems

A/B:
useful in traffic

Different questions, complementary evidence

## Page 53

Small inefficiencies grow with traffic

Agent · Baseline
Agent · Grounding rule

What size should I get?

Uses available information

No additional lookup

Redundant product lookup

One additional lookup

First grounding rule: Never state a product detail unless a tool result supports it.

Care: grounded
Sizing: extra lookup

Hypothetical: One extra call → Thousands of times a day

Latency
API cost
Tokens
Handoffs
Repeated turns

Correctness + Operational efficiency

## Page 54

Locate the missed constraint in a live trace

I can only walk for about ten minutes.

Is Pepper free on Saturday?

Outing scheduled

Agent

Short-walk volunteer
Pepper, 100 lb

Energetic
Production trace

Availability checked

Walking constraint not considered

QA
Recognize constraint before matching

## Page 55

Save the original wording and expected behavior

Recognize constraint
Check compatibility
Schedule only

if appropriate

I can only walk for about ten minutes.

Is Pepper free on Saturday?

Short-walk volunteer
Pepper, 100 lb

Energetic

Saved case:
Original message +

Expected behavior

Targeted change →

Run the
whole benchmark

Older mobility wording

Working scheduling

requests

QA
Builder

## Page 56

Feed production evidence back into offline evals

1
Production trace
2
Expected behavior
3
Saved case

4
Offline comparison
5
Release & monitor

I can only walk for about 
ten minutes. Is Pepper free

on Saturday?
Short-walk volunteer

If the constraint is handled

and the rest stays healthy

I’m fine with short walks,

but nothing strenuous.

QA
LLM judge
Builder

## Page 57

Turning production

failures into 
regression tests

Module 5 · Video 6

## Page 58

Bring production failures into the improvement loop

Observe
Benchmark
Evaluate
Improve

Which cases?
Which wording?
What is missing?

Hypothetical offline policy compliance: 96%

## Page 59

A high score covers the cases you tested

Hypothetical offline score: 96%

Refund order 1842

I want a refund for order 2271

No similar wording in this offline set

I bought this last week and it doesn’t fit.

Can I get my money back?

No “refund” keyword

Offline examples
Production wording

Customer C103

96% describes tested cases, not unseen wording

## Page 60

The failure starts before the refund tools

Trace · Missing actions

get_customer: Not called

Action / tool call
Trajectory
Session
System outcome

I bought this last week and it

doesn’t fit. Can I get my

money back?

I’m sorry it didn’t work 
out! Would you like to fill

out our feedback form?
Customer C103
Agent

order_lookup: Not called
process_refund: Not called

QA

Refund intent not recognized
Original message

→ Offline dataset

Save exactly as it appeared

## Page 61

Save expected behavior with separate checks

Expected: recognize refund intent

Follow policy
Required checks before processing
Code evaluator
Policy evaluator

Tool evaluators
Required lookups and actions

present, in order?

Policy evaluator
Refund rules followed?

QA
Repeatable test case
Original message + Expected behavior + Evaluators

## Page 62

Investigate the entry to the refund workflow

Refund intent not recognized

Before any refund tool call

Routing instruction

A concrete hypothesis, not the final fix

Examples of intent

Builder

Clarify when to enter
Vary refund intent wording

QA

Prompt

## Page 63

Run the expanded benchmark

Expanded benchmark

I bought this last week and it doesn’t fit.

Can I get my money back?

Refund order 1842

I want a refund for order 2271.

New capability case
Known-good protection

How should I care for the

merino wool sweater?

Code evaluator
Policy evaluator
Agent · Updated

## Page 64

Check the new case and what was already working

I bought this last week and it doesn’t fit.

Can I get my money back?

Expected: recognize refund intent

and follow the refund workflow

Questions for this comparison

Older refund requests:

still working?

Other known-good cases:

Unintended change?

Future versions must preserve this behavior

Development

failure
New capability
Introduced

regression
Production
Case origins:

Take what you learned and add it to the next eval

## Page 65

Feed production evidence back into offline evals

1
Get eval results
2
Choose what to 
improve
3
Make a targeted 
change

4
Compare 
versions
5
Inspect and 
refine

## Page 66

The evaluation cycle

Observe
Benchmark
Evaluate
Improve
Improve

Trace + failure

evidence

Criteria +

labeled 
examples

Automated 
checks + human

judgment

Targeted change

Stable test set
Regression tests

New traces
Refined criteria
Updated 
evaluations

Next
improvement
