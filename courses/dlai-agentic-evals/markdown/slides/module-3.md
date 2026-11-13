# Module 3: Building Evaluators You Can Trust

[Course index](../../README.md) · [Original source](https://global.discourse-cdn.com/dlai/original/3X/d/0/d0a8a01b0dd03a3502bd9e3a03b6ea994cbc28df.pdf) · [Raw file](../../raw/slides/module-3.pdf)

Retrieved: 2026-11-13T17:18:09.199628+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Building Evaluators

You Can Trust

Module 3

## Page 2

Building code

evaluators

Module 3 · Video 1

## Page 3

Automate the checks you can

Code evaluator
LLM judge
Human review

Was a flagged
volunteer rejected?

Does the explanation

make sense?
Is this shelter response

clear?

Next: are their judgments right?

## Page 4

Use code when a rule decides the answer

Response
Requirement

Code evaluator: ordinary code,

exact pass or fail rules

A rule decides

Under 500 characters?
Count them, compare with the limit.

312 < 500: pass

Needs interpretation

“This dog needs an 
experienced handler 
and you are new, so…”

A human or an LLM judge

## Page 5

A code evaluator: inputs, logic, output

Python function:
deterministic logic

Code evaluator

Request and response

as text or database

record, tool call details

score: 1
label: pass

or
score: 0
label: fail

In:
Out:

Questions a specific rule can answer

Did a required step run?
Does a claim match the

records?
Are all required fields there?

## Page 6

A flagged volunteer must be rejected

Flagged
Reject

Volunteer 2983

Volunteer ID: 2983

Record: flagged

Decision: 
approved
label: fail

score: 0

The rule determines the result: no LLM needed

## Page 7

Deterministic doesn’t mean simple

Get trace
Check Do-Not-Adopt

records
Apply evaluation criteria
Report

result

trace = (
 requests.get(
  "/traces/2983"
 ).json()
)

API call
Database query
Deterministic check

SELECT EXISTS (
   SELECT 1
   FROM 
do_not_adopt_records
   WHERE
  volunteer_id = '2983'
) AS is_flagged;

checked = (
  check_do_not_adopt_was_called
)
passed = checked and (
  not is_flagged or
  decision == "rejected"
)
score = int(passed)
label = ("fail", "pass")\[score\]

{
 "score": 0,
 "label": 
"fail"
}

Deterministic: same trace, same record, same judgment

## Page 8

Check the steps, not only the decision

Required step: check the do-not-adopt records

Approved

{
  "volunteer_id": "7623",
  "status": "approved",
  "check_do_not_adopt":
    "not executed",
  "score": 0, "label": "fail"
}

fail → 0
the decision was right, the process

wasn’t

Experienced

volunteer

Daisy
45 lb, calm

## Page 9

More checks you can write in code

Length
Under 500 characters

Forbidden phrase

“as an AI assistant”
Format
Valid JSON: volunteer ID,

dog ID, approval status

Facts vs records
Does the volunteer ID exist?
Does eligibility match record?

Required steps vs trace

Did it check the records

before approving?

{"volunteer_id": "7623", "dog_id": "182", "status": "approved"}

## Page 10

Make checks robust, then use them first

Explicit rule: automate it with code

if agent_output == "approved":
   return "pass"

return "fail"

Exact match: brittle
Normalized: robust

Get trace
Query records
Apply criteria
Report result

normalize whitespace
" ".join(text.split())

ignore capitalization: text.lower()

accept valid alternative wording:
{"approved", "cleared", "eligible"}

## Page 11

Code and judges share one workflow

Code evaluator

Was a flagged 
volunteer rejected?

LLM judge

Does the explanation

make sense?

Retrieve recorded runs
Run each evaluator
Save scores and labels

Recorded run
code: fail · 0

judge: UNSAFE

Is the explanation clear?

Is it empathetic?

Does it address their needs?

## Page 12

Using an LLM judge

Module 3 · Video 2

## Page 13

Some requirements need interpretation

Was the response helpful?

Did it answer the real question?

Was the tone right for someone 
who’s frustrated?
Human review

LLM judge: 
automates the

judgment

An LLM judge: a model + written criteria

## Page 14

Safe matching needs interpretation

Only match volunteers with dogs they can safely handle

Agent

Recommended match

Dog record:
Lunges at children
Experienced handler
Calm dogs up to 50 lb

Does this experience prepare them for this dog?

Experienced does not mean safe

## Page 15

A judge needs a model, a rubric and data

Judge model

The LLM that makes

the evaluation

Rubric: the criteria

and instructions
Data

Volunteer’s profile

Dog’s record
Agent’s decision

SAFE / UNSAFE

⇄  Rubric      ⇄  Judge model
Change one without the others

1.  Identify behavior risks

2. Compare
relevant experience

3. SAFE only if
risks can be managed

## Page 16

The judge’s model can differ from the agent’s

Agent
LLM judge

Type of model

Optimize for

Small

Speed and cost

Large

Accuracy

Judge mistakes change your results

Provider
Provider A
Provider B

Same provider: shared biases, similar blind spots

## Page 17

Check the judge against a reviewer

Reviewer

A person

Evaluator
An automated system

PASS
FAIL

Same responses,

same criteria

Is it applying your criteria correctly?

Coming up: how well do they agree?

## Page 18

Start with a built-in evaluator

Is the answer correct?

Was the right tool selected and 
called?

Is the document relevant?

Was it refused correctly?

Built-in evaluators

Criteria and expected output
You provide: model and evidence

Correctness doesn’t know how

the shelter judges a match

Custom rubric:
which details matter,

what is acceptable

## Page 19

The judge workflow, step by step

Recorded
application

runs

Retrieve spans:

a dataframe

Evaluate:
judge model +

rubric

Evaluate:
judge model +

rubric

Save judgments

back

Prepare the evidence for each example

Volunteer

profile

Dog
record

Agent
recommendation

## Page 20

Don’t record the judge’s own calls

Maya · run the evaluator

Application runs

Judge’s own traces

with suppress_tracing():

Judge’s own traces

Scores and labels:

saved

Traces of the grading:

not added

Volunteer

profile

Dog
record

Agent
recommendation

{ "label": "UNSAFE",
  "score": 0,
  "explanation": "…" 
}

## Page 21

Use the judgments to decide where to look

Evaluators tell you what failed. Traces show you why.

Annotations linked to runs

Run 01     SAFE       1
Run 01     SAFE       1

Run 02     UNSAFE     0
Run 02     UNSAFE     0

Run 03     SAFE       1
Run 03     SAFE       1

Run 04     UNSAFE     0
Run 04     UNSAFE     0

Sort by score
Filter by label

Open an unsafe run

Profile: experienced handler

Calm dogs up to 50 lb

Dog record:
Lunges at children

Agent recommendation:

Match these two

Judge: calm-dog experience

doesn’t establish ability to
manage this behavior risk.

## Page 22

Writing a 
custom rubric

Module 3 · Video 3

## Page 23

A custom rubric has five parts

1. Role
2. Criteria
3. Inputs
4. Labeled

examples

5. Output
instructions

Only match volunteers with dogs

they can safely handle.

Custom rubric:
instructions + examples

## Page 24

Parts 1 and 2: Role and criteria

You are evaluating whether a proposed 
volunteer-dog match is safe for both the volunteer 
and the dog.

Weak: “You are an

expert evaluator”

Specific: names the task and

what matters

Rubric author

The volunteer can physically handle the dog

Their experience is relevant to the dog’s needs

They can manage the behavior risks in the record

1. Role
2. Criteria
3. Inputs
4. Labeled

examples

5. Output
instructions

## Page 25

Part 3: Give the judge the evidence

1. Role
2. Criteria
3. Inputs
4. Labeled

examples

5. Output
instructions

From the volunteer
From the shelter
The agent’s decision

<volunteer_profile>Experienced</volunteer_profile>
<dog_record>130 lb, too strong</dog_record>
<recommendation>Match them</recommendation>

Instructions:
how to evaluate

Tagged inputs:
what to evaluate

Volunteer profile:

Experienced

Dog record:
130 lb, too strong

Agent 
recommendation

Match them

## Page 26

Part 4: Add labeled examples, then test them

<case>Experienced ·
130 lb, too strong</case>

<label>UNSAFE</label>

<reason>Experience alone
is not enough</reason>

1. Role
2. Criteria
3. Inputs
4. Labeled

examples

5. Output
instructions

Reviewed
benchmark cases

Case evidence · Expected label · Reason
The judge may copy the examples instead of applying the criteria

Experienced · 45 lb, calm

SAFE
Within the volunteer’s ability

Rubric with examples
Rubric without examples

Which rubric agrees more with reviewers?

Same reviewed cases
Not used as prompt examples

## Page 27

Part 5: Constrain the output

A score from 1 to 10:

what makes a 6 
different from a 7?

One label:
SAFE or UNSAFE
Define each label.

Easy to compare

and filter

NEEDS_REVIEW:

Large dog +
some experience,

no history with

large breeds

1. Role
2. Criteria
3. Inputs
4. Labeled

examples

5. Output
instructions

What it
evaluates

How to
decide

Which
information

How criteria

apply

How to

report

## Page 28

One rubric, one question

Is the match safe?

Does the agent speak politely?

FAIL: unsafe match or rude tone?

All in one prompt
Safety
Tone

Is this match safe?

SAFE / UNSAFE

Did the agent respond politely?

POLITE / NOT_POLITE

## Page 29

Treat failures differently

Preference fit: MISSED
Safety: UNSAFE

Missed preference: safe match,

not the dog they wanted
Unsafe match

Experienced
45 lb, calm
First-time

volunteer

Reactive, requires

experience

Accept for now
Guardrail: don’t ship

## Page 30

Treat the rubric like code

Version
One change,

same cases

Keep earlier versions

rubric_v1.md

Agreement with

reviewers: 70%

- Consider experience.
+ Check experience AND
  physical control.

rubric_v2.md

Rubric author

## Page 31

Validating 
LLM judges

Module 3 · Video 4

## Page 32

Treat the judge like a classifier

Can you trust its labels?

Volunteer profile

First-time

Dog record
Reactive poodle

Agent
recommendation

LLM judge

SAFE

UNSAFE

A label that looks definitive is still an interpretation of the rubric

Classifier: cases in, labels out

Reviewed labels

(benchmark)

Compare

## Page 33

Test on cases you didn’t use to build the rubric

Reviewed cases

Case
Case
Case
Case
Case
Case
Case
Case

Case
Case
Case
Case
Case
Case
Case
Case

Case
Case
Case
Case
Case
Case
Case
Case

Case
Case
Case
Case
Case
Case
Case
Case

75% · Used to write
and tune the rubric

Results look better

than they are

🔒 25% · Held-out set
Not prompt examples
Not used to refine the rubric

Run held-out cases

Compare judge and reviewed labels

First-time
Reactive poodle

Reviewed: UNSAFE
Judge: SAFE

Disagreement: the judge missed a failure

## Page 34

Precision and recall

Experienced
Buddy, 130 lb
First-time

volunteer

Reactive

poodle

Judge: UNSAFE
Judge: SAFE

Reviewed:

UNSAFE

Reviewed:

SAFE
Correctly safe ✓

Caught

Precision:
How often are warnings right?

Experienced
Daisy
45 lb, calm

False alarm · Precision goes down

Recall:
How many unsafe matches are caught?

Missed failure · Recall goes down

## Page 35

Read precision and recall as costs

Which mistake costs more?

False alarm

Experienced
Daisy · 45 lb calm

Judge: UNSAFE
Unnecessary review costs time.

Missed failure

First-time

volunteer
Reactive poodle

Judge: SAFE
An unsafe match moves forward.

Volunteer or dog could be at risk.

Shelter: prioritize recall for UNSAFE · Accept some extra false alarms

Recall up / precision down
Too many flags: too noisy to use

## Page 36

High agreement can hide a missed failure

Cohen’s kappa

Reviewed

SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
UNSAFE

Judge

SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
SAFE
SAFE

Agree: 9 of 10
90%

The only unsafe case: missed

## Page 37

Kappa is a signal, not proof

K adjusts for agreement by chance

K = 1
Every label matches

K = 0
No better than chance

K < 0
Worse than chance

A small set: one disagreement moves it a lot

Kappa compares two sets of labels

Reviewers agree
Judge agrees

Both can be wrong

Reviewer missed a detail

Rubric is unclear
Everyone applies the wrong standard

## Page 38

A disagreement tells you where to look

Reviewers: UNSAFE
Judge: SAFE

Inspect the case

Volunteer profile

First-time

Dog record
Reactive poodle

Agent
recommendation

Judge’s explanation

Judge applied the requirement:

correct the reviewed label

The reviewed label is right:
the judge misapplied the rubric

Could go either way:
the rubric boundary is unclear

A disagreement doesn’t mean “fix the judge”

## Page 39

A careful tone can hide a physical limit

Experienced

volunteer
Calm senior dog

Agent

“He’s gentle, and you’ve
handled many dogs before.”

Calm dogs

up to 50 lb
80 lb

Judge: SAFE

The recommendation ignores a physical handling limit

## Page 40

Look for patterns, then change one thing

Risk is obvious: caught

Experienced
Lunges at

children

Risk is a number: missed

Experienced
Calm senior

dog, 80 lb

Calm dog + careful tone:

recall drops

Agent
Calm senior

dog

The judge weighs the agent’s explanation more than the evidence

Rubric change

Before assigning a label:
1. State the volunteer’s handling limit.
2. State the dog’s weight.
3. Compare them.

## Page 41

Test every rubric change on fresh cases

1
Change one thing

2

Test on fresh reviewed cases

3

Compare old and new

4
Keep it only if it improved overall;
otherwise revise or go back

The case behind the change is no longer clean

Recall
Precision
Kappa
Explanations

Change the rubric

## Page 42

Use several checks before you trust a judge

Recall

Does it catch
the failures you

care about?

Precision

Are its warnings

usually right?

Cohen’s kappa

Agreement
beyond chance

Disagreements

& explanations

Does it use the
right evidence?

Only then: guide improvement or block a change

Code evaluator
LLM judge
Rubric
Validated labels

## Page 43

Applying evaluators

to Northwind

Module 3 · Video 5

## Page 44

Three requirements, three evaluators

Code evaluator
LLM judge
Rubric
Validated labels

Northwind

agent

product_exists

Are the products real?

correctness

Does it answer the 
customer’s question?

policy_compliance

Does it stay within 
Northwind’s capabilities?

result
result
result

## Page 45

Set aside a held-out set

Northwind benchmark

Reviewed cases

Case
Case
Case
Case
Case
Case
Case
Case

Case
Case
Case
Case
Case
Case
Case
Case

Case
Case
Case
Case
Case
Case
Case
Case

Case
Case
Case
Case
Case
Case
Case
Case

Customer

question

Agent
response

Reviewer’s

label

NON_COMPLIANT

🔒 Held-out validation set

Save for later; not used to

refine the evaluators

Development cases
Build and refine the evaluators

90-day
return window

Can I return this

after 60 days?

## Page 46

Design the validation set for coverage

Benchmark: scope violations are rare

Validation set: enough important failures to test

Design for coverage, not production frequency

Mostly routine requests

Routine requests
Scope violations + hallucinations

Random split: only one or two scope violations
⚠ One miss changes recall a lot

## Page 47

Requirement 1: every product must exist

Every product mentioned should exist in the catalog

Catalog:
source of truth
product_exists

Code evaluator

I need a warm jacket

for winter camping.

Try the Summit 
Shell Jacket

Compare
names or IDs

Pass
Every product exists

Fail
Product is not in the catalog

## Page 48

Requirement 2: does it answer the question?

product_exists: pass

Which shoes are best for rainy weather?

Trail Runner
Everyday Sneaker

Products exist ✓
Doesn’t answer

the question ✗

Built-in correctness judge

CorrectnessEvaluator
Question + response → does it

answer?

product_exists: are the products real?
correctness: did it answer the question?

## Page 49

Requirement 3: stay within what Northwind can do

Another requirement: scope

Can: product and catalog

questions

Cannot: look up orders · process returns · issue refunds

check shipping status · other support systems

Can I return this after 60 days?

I can help with product and 
catalog questions, but I can’t

process returns.

Absolutely! Northwind

offers a 90-day

return window.

Needs a custom LLM judge
General correctness: pass
Misses the scope violation

## Page 50

1. Role
2. Criteria
2. Criteria
1. Role
1. Role

Role and criteria for the policy judge

3. Inputs
4. Labeled

examples

5. Output
instructions

Role
You are evaluating whether a Northwind customer-support response

stays within the agent’s capabilities.

COMPLIANT
Product/catalog support only.
Otherwise, Northwind can’t help.

NON_COMPLIANT
Invents a process or capability

the agent was never given

Return

policy

Refund
process

Shipping

lookup

Support
channel

## Page 51

3. Inputs
4. Labeled

examples
4. Labeled

examples

5. Output
instructions

5. Output
instructions
4. Labeled

examples
3. Inputs

Inputs, examples and output

1. Role
2. Criteria

<customer_query>

…
</customer_query>

<agent_response>

…
</agent_response>

Reviewed development cases

COMPLIANT
I can help with product and catalog 
questions, but I can’t process returns.

NON_COMPLIANT
You have 90 days to return the item.
Northwind never provided that policy

One fixed label

COMPLIANT
NON_COMPLIANT

## Page 52

Separate results for each requirement

product_exists
correctness
policy_compliance

Can I return this after 60 days?

annotation
annotation
annotation

Mentions only a real product:

the Classic Tee

Sounds complete

and helpful

Invents a return process
Northwind doesn’t support

One overall score: two of three pass and the policy failure disappears

## Page 53

Validate the judge, inspect disagreements

Reviewed labels
COMPLIANT
NON_COMPLIANT
Compare for the
same responses

Apply the rubric

The judge missed an
invented refund process

The reviewed label

was wrong

The rubric didn’t make the

capability boundary clear

🔒 Held-out set

Recall: how many real policy

violations did it catch?

Precision: how often were its

flags right?

Cohen’s kappa: agreement

beyond chance

Disagreement: open the case

Customer

question

Agent
response

Judge’s
explanation
?

## Page 54

Build, validate, inspect, revise, test again

1
Build on
development cases
2
Validate on
held-out cases
3
Inspect
disagreements

4
Revise carefully
5
Then test again

Change one thing at a time; test on fresh reviewed cases

A case that shaped the rubric is no longer a clean validation case

## Page 55

Choose the simplest evaluator that works

Define the requirement

Identify the evidence that can answer it

Choose the simplest evaluator

that can apply it reliably

Code evaluator

Directly checkable

Built-in LLM judge

Interpretive but general

Custom rubric

Application-specific rules

Keep separate requirements as separate results
