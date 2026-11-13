# Module 4: Evaluating Agent Actions and Outcomes

[Course index](../../README.md) · [Original source](https://global.discourse-cdn.com/dlai/original/3X/2/b/2bde11f1c30ca57f2de23cfe4e779fafc9de0b7c.pdf) · [Raw file](../../raw/slides/module-4.pdf)

Retrieved: 2026-11-13T17:18:10.486645+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Actions, 
Conversations, and

Outcomes

Module 4

## Page 2

Evaluating the work

behind a response

Module 4 · Video 1

## Page 3

Evaluate the work behind the response

Observe
Benchmark
Evaluate
Improve

Response

Retrieve
information
Decide
Call tools
Change state

?

## Page 4

A correct response can hide a missing step

Response: clear and accurate

Can you book me with Pepper

for Saturday afternoon?

Great, you’re booked with Pepper

for Saturday at 2 PM.

Retrieve

record

Inspect the work, not only the response

Agent

Pamela
Can safely handle

large dogs

Pepper, 100 lb

Match volunteer

and dog

Create
booking
Eligibility
check missing

## Page 5

A wrong record can mislead the whole run

Request: Pamela

Retrieve

record

Retrieved

record
Retrieved record:

Maria

First-time volunteer

Daisy,
45 lb, calm

Eligibility checked

for Maria
Eligibility checked

for Maria

Match:
Maria + Daisy

Match:
Maria + Daisy

Agent

Booking +
confirmation:

Maria

Booking +
confirmation:

Maria

Wrong volunteer

Valid steps can use the wrong input

## Page 6

Separate the input from the matching decision

Record

Maria
Record

Maria
Record

Maria

Eligibility

Maria

Action

Maria
Action

Maria
Action

Maria

Response

Maria

Only match volunteers with dogs they can safely handle.

Matching input:

Maria
Matching input:

Maria

Agent

Same 
matching

Bad match

Wrong input?
Matching logic?

Correct record:

Pamela

Matching result?

## Page 7

Match the evidence to the requirement

Action / tool call
Action / tool call

One action
Name + arguments

Trajectory
Trajectory
Trajectory

Several actions

Steps + order

Session
Session
Session

Earlier turns
Context + constraints

System outcome
System outcome

External system

Actual state
Correct record:

Pamela

Agent

Same 
matching

If appropriate match:

retrieval failure

If bad match:
inspect matching logic too

Locate the failure and what it affected

## Page 8

Check Northwind’s actions too

What’s the status of order 4521?

Response
Agent

Orders
Customers
Products
Refunds

Right order?
Right customer?
Required action?

Customer C103

## Page 9

Evaluating actions

and tool calls

Module 4 · Video 2

## Page 10

Evaluate one action

Observe
Benchmark
Evaluate
Improve

Action / tool call
Trajectory
Session
System outcome

Pamela

I can’t make Saturday anymore.

Please cancel my outing.

## Page 11

Choose the action, then check its details

I can’t make Saturday anymore. Please

cancel my outing.
Can you book me with Pepper

on Friday at 5:30?

Great, you’re booked with Pepper

for Saturday at 2 PM.
Create booking

Agent

Pamela
Can safely handle

large dogs

Pepper, 100 lb

Booking: Pamela · Pepper

Saturday · 2 PM

Action choice: FAIL

Requested: cancel
Chosen: confirm

Action choice: PASS

Expected: Friday, 5:30
Written: Saturday, 5:30

Action details: FAIL

## Page 12

Check choice, details, and required actions

Action choice: PASS

Volunteer · Dog · Day · Time

Action details: FAIL
Expected Friday, 5:30
Written Saturday, 5:30

Retrieve

record

Eligibility
check missing

Match volunteer

and dog

Create
booking

Pamela
Can safely handle

large dogs

Pepper, 100 lb

Agent

Required action present?
Required action missing

Booking: Pamela · Pepper

Saturday · 2 PM

## Page 13

Some actions must not happen

Can I take Pepper home permanently?

Outings only
No adoption authority

Agent

Pamela
Can safely handle

large dogs

Pepper, 100 lb

Permanent placement

Should not happen

Right action?
Right details?
Required action?
Prohibited action?

Define permitted behavior before checking execution

## Page 14

Check the tool and its arguments

Expected: Order lookup
Tool result
Arguments

Tool invocation: FAIL

Product search
Tool success
Expected: 4521
Argument: 4512

Tool selection: PASS

Customer C103

Agent

Where is order 4521?

Actions are tool calls

Code evaluator

order_lookup(
  order_id="4512"
)

## Page 15

Check selection, invocation, presence, and absence

Tool selection

Customer C103

Agent

Tool invocation

Correct tool?
Order lookup

Correct arguments?

Expected: 4521
Argument: 4512

Current order status

Required:
order_lookup
Missing in trace: FAIL

Refund outside window

Prohibited:
process_refund
Present in trace: FAIL

Code evaluator

## Page 16

Define what to do when information is missing

Action / tool call
Trajectory
Session
System outcome

Customer C103

Agent

Can you refund my purchase?

Order ID: missing

Ask which order before acting

Which order would you like refunded?
Guess / refund now
Requirement
Trace evidence
Check

Define correct behavior first

## Page 17

Passing tool checks does not approve the response

Tool selection: PASS
Tool invocation: PASS
Incorrect availability claim
Code evaluator

order_lookup(
  order_id="4512"
)

Tool name
Arguments
Required calls
Prohibited calls

4521 ≠ 4512
Deterministic check: FAIL

Customer C103
Agent

check_inventory

Requested product · Correct argument

Stock: 0
Yes, it’s available.
Yes, it’s available.

Order?
Valid call
Valid call
Valid call

Correct calls can still form a failed run

## Page 18

Evaluating 
trajectories

Module 4 · Video 3

## Page 19

Evaluate how actions fit together

Observe
Benchmark
Evaluate
Improve

Action / tool call
Trajectory
Session
System outcome

Action
Result
Next action

## Page 20

Follow the path through the task

Action / tool call
Trajectory
Session
System outcome

Retrieve record

Pamela

Check eligibility

Passed
Match volunteer 
and dog: Pepper

Match volunteer
and dog: Pepper

Check eligibility

Passed

Create booking
Pamela · Pepper

Saturday, 2 PM

Pamela
Agent
Pepper, 100 lb

Can you book 
me with Pepper

for Saturday at

2 PM?

## Page 21

{
  "retrieved_id": "Pamela"
}

{
  "matching_input": "Maria"
}

{
  "retrieved_id": "Pamela"
}

Find trajectory failures

Retrieve record

Pamela
Retrieve record

Pamela

Match volunteer
and dog: Pepper

Eligibility
\[missing\]

Check eligibility

Passed
Match volunteer
and dog: Pepper

Create booking

Saturday, 2 PM
Create booking

Saturday, 2 PM

Pamela
Agent
Pepper, 100 lb
Maria
First-time volunteer

Check eligibility before matching
Required step missing

Propagation failure: Pamela ≠ Maria

## Page 22

Reconstruct the trajectory from evidence

Action / tool call
Trajectory
Session
System outcome

Ordered calls + returned values

1  get_customer → Customer verified
2  order_lookup → $49.99
3  process_refund → Tool success

Required steps
Did every required

step happen?

Correct order
Did order-sensitive steps

happen in order?

Correct propagation
Did the next step use the

returned data?

Trace
Events in this run

1
2
3

## Page 23

Returned value
Call 3

Returned value
Call 2

Returned value
Call 1

The same calls can violate the required order

order_lookup(order_id="4521")
process_refund(order_id="4521", amount=49.99)
Refundable amount: $49.99
Tool success

Customer C103

Agent

Please refund order 4521.

Northwind refund request
Requirement: verify before refund

get_customer(customer_id="C103")
order_lookup(order_id="4521")
Customer verified
Refundable amount: $49.99

process_refund(order_id="4521", amount=49.99)
get_customer(customer_id="C103")
Tool success
Customer verified · late

Valid calls can happen in the wrong order

## Page 24

Check order and propagated values directly

Customer C103

Agent

Please refund order 4521.
identity_before_refund
Compare propagated values

Ordered calls + returned values
Verification succeeded

Before process_refund

Same customer: C103

Same order: 4521

Code evaluator

get_customer(customer_id="C103")

order_lookup(order_id="4521")

process_refund(order_id="4521", amount=49.99)

Customer verified

Refundable amount: $49.99

Tool success

order_lookup(order_id="4521") → Refundable amount: $49.99

process_refund(order_id="4521", amount=59.99)

Amount propagation: FAIL · 49.99 ≠ 59.99

## Page 25

Focused requirement check
Broad policy check

Keep focused results beside the broad judgment

Customer C103
Agent

Refund · C103 · Order 4521 · $49.99

policy_compliance

Identity
Refund eligibility
Amount
Sequence

LLM judge

Policy: FAIL
Which requirement?

Code evaluator

identity_before_refund:

FAIL

Keep separate requirements as separate results

## Page 26

Use direct evidence when it answers the question

Requirement

Relevant evidence

Code evaluator
LLM judge

Direct evidence
Verification before refund
Inspect ordered successful events

Verification before refund
Inspect ordered successful events

Correct amount
Compare returned and used values

Semantic requirement
Semantic requirement

Interpretation when needed

## Page 27

Current run
Only this trace is visible

Later run
Refund before confirmation

A trajectory stops at the boundary of one run

Action / tool call
Trajectory
Trajectory
Session
Session
System outcome

Required steps

get_customer
Customer verified

get_customer
Customer verified

get_customer
Customer verified

Correct order

order_lookup
Refundable: $49.99

order_lookup
Refundable: $49.99

order_lookup
Refundable: $49.99

Correct propagation

process_refund

Amount: 49.99
process_refund

Amount: 49.99
process_refund

Amount: 49.99

Trajectory · One run

Earlier turn · instruction outside this run
Don’t refund anything until I confirm the amount.

Customer C103
Agent · acknowledged

Earlier instructions need session evidence

## Page 28

Evaluating across 
conversation turns

Module 4 · Video 4

## Page 29

Evaluate across the session

Observe
Benchmark
Evaluate
Improve

Action / tool call
Trajectory
Session
System outcome

Earlier turn → Later turn

Pamela

I can only do walks before 6 PM.
Acknowledged

## Page 30

A later booking can break an earlier instruction

Earlier turn
Session
I can only do walks before 6 PM.

Pamela
Agent

Pepper, 100 lb

Pepper sounds good. Can you book

me for tomorrow?
Tomorrow, 7 PM
Booking 
succeeded

Before 6 PM ≠ 7 PM · Instruction drift

## Page 31

Carry the order context across turns

Customer C103
Agent

Earlier turn

My order number is 4521

Later turn

Can you refund it?

Failure variant A
Asks for the order again

Failure variant B

Uses 4512

Context loss

Possible continuation A
Possible continuation B

## Page 32

A narrow evaluator can miss prior verification

Action / tool call
Trajectory
Trajectory
Trajectory
Session
Session
System outcome

get_customer(
customer_id="C103")

C103 verified successfully

order_lookup(
order_id="4521")

Refundable amount: $49.99

process_refund(order_id="4521",

amount=49.99)

Earlier turn
Refund turn · Order 4521

Verification not found in this trace

Scope: refund trace only

Identity before refund: PASS

Scope: earlier turn + refund turn
Verify customer before refund

Code 
evaluator

Match the scope to the requirement

Call
Right order ID?

Trajectory
Verification before refund?

Session
Verified in an earlier turn?

## Page 33

Wait for the customer to confirm the amount

Action / tool call
Trajectory
Session
System outcome

Customer C103

Agent

1. Customer instruction
2. Agent acknowledgement

3. Ask for the amount
4. Look up the amount

5. Customer confirmation
6. Refund not sent

Don’t refund anything until I

confirm the amount.

Understood. I won’t process a

refund until you confirm.

How much did I pay

for order 4521?

You paid $49.99.
order_lookup · 4521

Okay, go ahead

with the refund.

process_refund(
order_id="4521",

amount=49.99)

## Page 34

Late confirmation cannot authorize an earlier refund

Action / tool call
Trajectory
Session
System outcome

Customer C103

Agent

1. Customer instruction
2. Agent acknowledgement

3. Ask for the amount
4. Look up the amount

5. Refund not sent
6. Customer confirmation

Don’t refund anything until I

confirm the amount.

Understood. I won’t process a

refund until you confirm.

How much did I pay

for order 4521?

You paid $49.99.
order_lookup · 4521

process_refund(
order_id="4521",

amount=49.99)

Okay, go ahead.

Confirmation arrived too late

## Page 35

Control the user side when comparing versions

Scripted user

Agent
Version 1

Agent
Version 2

Same messages, same situations

Waits: PASS
Refunds early: FAIL

Illustrative variants

Same user behavior makes the comparison meaningful

Standing instruction

Amount question

Permission after the amount

Don’t refund anything until I confirm the amount.

How much did I pay for order 4521?

After $49.99 is reported: Okay, go ahead.

## Page 36

Let a simulated user respond to the agent

Agent
Scripted user

I want my money back.

Sure. Which order do you mean?

Fixed script: no reply defined

Simulated user · LLM

Goal: refund

Order: 4521

Order 4521

The refundable amount is $49.99.

Would you like me to proceed?

Yes.

Agent question → User reply
LLM chooses the next reply
Customer goal +

known order

Next agent response → Next user reply

## Page 37

Choose control or conversational flexibility

Scripted user
Simulated user · LLM

Exact wording

Order 4521

Order 4521  /  It’s 4521
Same goal and order; different wording

Tighter control
Same interaction across versions

More natural paths
More user-side variation

Fixed interactions: scripted · Branching: simulated

User messages fixed
User goal and data fixed

## Page 38

Test the evaluator on known sessions

1. Start with a known-good session

2. Test the broken session

Look up 4521

Look up 4521

Show $49.99

Show $49.99

Customer

confirms

Refund $49.99

Refund $49.99

Customer

confirms

confirmation_before_refund → PASS
If this fails: evaluator or setup?

confirmation_before_refund → FAIL

Validate the check before diagnosing the agent

Comparison case · fixed test inputs

Customer C103
Order 4521
Amount $49.99
Check event

order

## Page 39

Use enough evidence for the requirement

Action / tool call
Trajectory
Session
Session
System outcome

get_customer(
customer_id="C103")

C103 verified successfully

order_lookup(
order_id="4521")

Refundable amount: $49.99

process_refund(order_id="4521",

amount=49.99)

Turn 1: verification
Turn 6: refund

Verify customer before refund

Code 
evaluator

Identity before refund: PASS

Action: one call
Wrong tool argument?
Trajectory: steps + order
Sequence problem?
Session: earlier turns
Standing instruction?

Enough context, not all context by default

## Page 40

Process checks do not prove a system change

Action / tool call
Trajectory
Session
System outcome

Right order ID?
Verification before

refund?

Customer 
confirmed first?

Call argument:

4521

Verified first
Then refunded

Earlier permission

→ refund

External state?

Your refund has been processed.

System outcome:

not checked

A claim is not a system record

Tool call
Task trace
Earlier turns

Outside the 
conversation

Agent response

## Page 41

Verifying task

outcomes

Module 4 · Video 5

## Page 42

Verify the system outcome

Observe
Benchmark
Evaluate
Improve

Action / tool call
Trajectory
Session
System outcome

Pamela
Pepper, 100 lb

Can you book me with Pepper

for Saturday at 2 PM?

## Page 43

Check the booking system, not only the confirmation

Volunteer
Dog
Day
Time

Can you book me with Pepper

for Saturday at 2 PM?

Great, you’re booked with Pepper

for Saturday at 2 PM.

Agent

Pamela

Eligibility checked
Pepper available
Booking system
Before this run: no matching booking
After this run: new matching booking
Alternative run

Pamela
Pepper
Saturday
2 PM
No new matching booking
No new matching booking · Outcome: FAIL

Verify the external state directly

Pepper, 100 lb

## Page 44

Compare the refund record with the expected result

Customer C103
Agent

Please refund order 4521.

Your refund has been processed.

Customer ID
Order ID
Amount

Code 
evaluator

Customer verified
Order eligible
Refund tool called

Refunds · Before: no matching row / After: inspect new rows

C103
4521
$49.99

Expected: C103 · 4521 · $49.99
Outcome: PASS

Please refund order 4521.

## Page 45

Check changes and non-changes

Refund not eligible
Expected: no new refund row
Compare before and after this run

Code 
evaluator

Eligible refund
New C103 / 4521 / $49.99 row

Outcome: PASS

Eligible refund
No new matching row

Outcome: FAIL

Before this run
No matching refund

After this run
No new refund row

After this run
No new refund row

Outcome: PASS

Sometimes success means no state change

refunds table
New rows from this run
C103 · 4521 · $49.99 expected

Customer ID
Order ID
Amount

C103
4521
$49.99

Refunds · Expected new row

## Page 46

Inspect two views of the same refund run

Customer C103
Agent
Code evaluator

Expected change
Verify a new matching row

Expected non-change
Verify no new refund row

System outcome
Trajectory

Customer ID
Order ID
Amount

C103
4521
$49.99

Same run
Actions not yet inspected

Outcome: PASS

Refunds
Inspect new rows from this run

## Page 47

Keep outcome and process results separate

Customer C103
Agent
Code evaluator

System outcome
Trajectory

Customer ID
Order ID
Amount

C103
4521
$49.99

Outcome: PASS

order_lookup → process_refund

get_customer → Customer verified

After the refund

Identity before refund: FAIL

Keep separate requirements as separate results

## Page 48

A booking can exist after an invalid process

Agent

Pamela

Volunteer
Dog
Day
Time

Pamela
Pepper
Saturday
2 PM

Booking system · New row from this run
Another run · Booking system

Outcome: PASS
Outcome: FAIL

Retrieve

record

Eligibility
check missing
Check eligibility
Match volunteer

and dog

Create
booking

Process: FAIL
Process: PASS

No new matching booking

Different failures need different fixes

Pepper, 100 lb

## Page 49

Match the evidence to the requirement

Action / tool call
Action / tool call
Action / tool call
Trajectory
Trajectory
Trajectory
Session
Session
Session
System outcome
System outcome
System outcome

order_lookup(
  order_id="4521"
)

Agent

Your refund has been processed.

get_customer → Customer verified
then process_refund(order_id=4521, amount=49.99)

Don’t refund anything until I confirm the amount.
Earlier instruction → explicit permission → refund

Customer ID
Order ID
Amount

C103
4521
$49.99
order_lookup
order_id="4521"

Customer verified

then refund

Earlier instruction
Confirm amount first

New refund row

C103 · 4521

$49.99

Each view answers a different question

Your refund has been processed.

## Page 50

Interpreting 
evaluation results

together

Module 4 · Video 6

## Page 51

Interpret results from the same task

Observe
Benchmark
Evaluate
Improve

Action / tool call
Trajectory
Session
System outcome

Agent

Don’t refund anything until I confirm the amount.

Identity verified · Order 4521
Refundable amount $49.99
Customer C103

## Page 52

Keep outcome and process results separate

Customer C103
Agent
Code evaluator

Customer ID
Order ID
Amount

C103
4521
$49.99

Outcome: PASS

Keep separate requirements as separate results

Don’t refund 
anything until I

confirm the

amount.

process_refund(
 order_id="4521", amount=49.99
)

Before customer confirmation
Refunds · New row

Your $49.99 refund

has been 
processed.

Tool selection
Tool selection: PASS

Tool invocation
Tool invocation: PASS

Identity before refund
Identity before refund: PASS

Session confirmation
Session confirmation: FAIL

Earlier instruction ignored

Refunds
Awaiting database inspection

Identity verified

## Page 53

The same score can hide different failures

Customer C103
Agent
Code evaluator

Keep the individual results and their evidence

Run A: 3/4

Run A: 3/4 · Process checks

Run B: 3/4

Run B: 3/4 · Process checks

Four process checks

Outcome not 
included in this score

Tool selection
Tool selection: PASS

Tool invocation
Tool invocation: FAIL · 4512 ≠ 4521

Identity before refund
Identity before refund: PASS

Confirmation before refund
Confirmation before refund: PASS

Tool selection
Tool selection: PASS

Tool invocation
Tool invocation: PASS

Identity before refund
Identity before refund: FAIL · Verified too late

Confirmation before refund
Confirmation before refund: PASS

## Page 54

Define the requirement, then choose the evidence

Investigate what happened

Code evaluator

Choose evidence that can answer the requirement

Action / tool call
Trajectory
Session
System outcome

Customer C103

Response from C103’s run:
Your $49.99 refund has been processed.

Your $49.99 refund has been processed.

Call
Trajectory
Earlier turns
Database

Define correct behavior
Evaluate with the relevant evidence

Order ID: 4521
Verify before refund
Wait for 
confirmation
New refund row

## Page 55

Match the evidence to the requirement

Action / tool call
Trajectory
Session
System outcome

The task is complete.
You’re booked with Pepper for

Saturday at 2 PM

Retrieve record

Pamela

Agent
Pamela
Pepper, 100 lb

Match volunteer

and dog

Create
booking
Check eligibility
One action
Name + arguments

Right action?
Right information?

Several actions

Steps + order
Required steps?

Right order?

Earlier turns
Context + constraints

Earlier context

preserved?

External system

Actual state
Expected state

created?
Earlier constraint: Before 6 PM

Independent session check

Volunteer
Dog
Day
Time

Pamela
Pepper
Saturday
2 PM

Evidence shows what needs attention
