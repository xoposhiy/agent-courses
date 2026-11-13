# Module 2: Observing and Benchmarking Agents

[Course index](../../README.md) · [Original source](https://global.discourse-cdn.com/dlai/original/3X/4/2/42b96553ad0415e8fc965096711ee974d49f4196.pdf) · [Raw file](../../raw/slides/module-2.pdf)

Retrieved: 2026-11-13T17:18:08.222315+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Module 2

Observing & 
Benchmarking

Agents

## Page 2

Define application

requirements

Module 2 · Video 1

## Page 3

Compare actual vs. expected behavior

Observe
Benchmark
Evaluate
Improve

Capture what

the agent did

Mistakes in agentic applications can be subtle

## Page 4

Find and develop requirements for your agent

Observe
Benchmark

Define what the agent

should do and not do

Evaluate
Improve

Find requirements and

write them down

Review wording and

coverage
Turn observations into

requirements

## Page 5

Look for requirements in three places

Do-not-adopt

flag

Reject

Requirements

What should the application do or avoid doing?

Existing rules
Traces
People who 
know the work

Which matches would you

recommend and why?

{
 "volunteer_id": "2563",
 "dog_id": "182",
 "time": "SAT 10:00",
 "status": "confirmed"
}

## Page 6

How should I care for my 
merino wool sweater?

You can machine wash 
it on a wool cycle and 
then tumble dry

You can machine wash 
it on a wool cycle and 
then tumble dry

Catalog:
Machine washable on wool cycle

A trace shows what the answer was based on

The agent recommended 
tumble drying, but the sweater 
didn’t have drying instructions.

## Page 7

Turn one observation into a broader requirement

No drying 
instructions

Says to 
tumble dry

Too narrow

Don’t recommend 
tumble-drying this sweater

Broader 
requirement

Only make claims about 
products that are supported

by Northwind data

Review question

Does the Northwind data

support what the 
application told the

customer?

## Page 8

Review and refine what you’ve written

Observe
Benchmark
Evaluate
Improve

Find requirements and

write them down

Review wording and

coverage
Turn observations into

requirements

Unclear wording

Situations not covered

## Page 9

Make vague words explicit

Vague
requirement

What makes a
match unsuitable?

Recommend a 
suitable dog

Recommend a suitable 
dog: never match a 
dog that requires an 
experienced handler 
with a first-time 
volunteer

First-time

handler

Experienced 
handlers only

Explicit 
requirement

## Page 10

Cover situations your requirements miss

Covered

Not yet covered

Complete information

Missing or conflicting information

Shelter rule?

Yes: Add it to the

requirements

No: Decide what

should happen

No suitable dog

available

## Page 11

Turn requirements

into test cases

Module 2 · Video 2

## Page 12

Turn requirements into test cases

Define 
requirements

Build test

cases

Analyze & 
label failures

Expand 
coverage

Curate the 
benchmark

User request
Relevant records

or context
Expected outcome
Test case:

Observe
Benchmark
Evaluate
Improve

## Page 13

One requirement applies in many situations

Experience levels
Handling needs

Test both:

Only match volunteers with dogs 
they can safely handle
Requirement

Missing information

Experience
Physical ability

First time
Experienced
Calm
Experienced 
handlers only

Experience 
not recorded

No handling

notes

## Page 14

Find situations from different angles

Safe or unsafe match
What the application

knows

How the request is

worded

Start with: likely situations, mistakes you’ve seen,  risky cases

First-time

Experienced, 
physically able

Experienced, 
dog too strong

Handling notes:
experienced only

Handling notes:
\[missing\]

Note A: beginner OK
Note B: experienced only

Can I take Buddy out for a 
walk?

I’d like to take Buddy. 
Would that be okay?

can i wlk budy

## Page 15

Each case pairs the facts with an expected outcome

Reject the match
Can I take Buddy 
out for a walk?

Can I take Daisy out 
for a walk?

Approve the match, if

eligible and available

User request
Volunteer & dog info
Expected outcome

Experienced
130 lb, too strong

Experienced
45 lb, calm

## Page 16

or

Test cases can reveal requirement gaps

Once decided: add it to the requirement and the expected outcome

Ask for more 
information?

Reject the match?

Only match volunteers with dogs 
they can safely handle. 
Requirement

Check the shelter’s policy

Or ask shelter staff

Experienced
No handling

notes

## Page 17

Not every case has one exact answer

Experienced. Can

safely handle

large dogs

45 lb, calm
Energetic, 100 lb
Reactive, 
experienced 
handler required

All three are acceptable matches

Suitable dog: the volunteer has

the experience and physical

ability to handle it

Daisy would be a good match: she’s 
calm, and you’ve handled large dogs

Example of one suitable response

## Page 18

Know where each example came from

Test case 
generator
Examples you 
already have

Realistic

Fit the situation

Source: real request
Source: LLM

Later, the source helps decide: weight of the case, in the benchmark or not

New examples

## Page 19

Analyze and label

failures

Module 2 · Video 3

## Page 20

Define 
requirements

Next step: Analyze and label failures

Define 
requirements

Build test

cases

Expand 
coverage

Curate the 
benchmark
Build test

cases

Analyze & 
label failures

Manual review: label failures, group them and prioritize

Observe
Benchmark
Evaluate
Improve

## Page 21

Start by manually reviewing the failure

Expected 
outcome
Do not match

Matched
Agent 
response

What went 
wrong

Ignored physical

handling  ability
Test case

Experienced
130 lb, too

strong

Only match volunteers with 
dogs they can safely handle. 
Requirement
Trace

PASS
FAIL

Human 
review

Not sure
UNRESOLVED

## Page 22

Keep the information information from each run

Outcome and

explanation

Trace

Pending 
information

For each run,

write down:

Test case

Experienced
130 lb, too

strong

What went 
wrong

Matched a dog the 
volunteer couldn’t safely

handle

If you have an explanation you haven’t 
checked, write it down as a possibility

## Page 23

Group cases by problem category

Failure 1
Failure 2

Test case

Experienced
130 lb, too

strong

First-time

volunteer

Reactive, needs

experienced

handler

What went 
wrong

Approved an unsafe 
match with the right

information

Approved an unsafe 
match with the right

information

Group them together

## Page 24

Group cases by problem category

Failure 1
Failure 2

Test case

Experienced
130 lb, too

strong

First-time

volunteer

Reactive, needs

experienced

handler

What went 
wrong

Approved an unsafe 
match with the right

information

Retrieved the wrong

dog’s record

Reasoning went

wrong

Information retrieval

went wrong

## Page 25

Use categories to label recurring failure patterns

Failure category
Description
Example

Judgment
The agent made the wrong 
decision

Unsafe volunteer-dog 
match

Groundedness
Response is not grounded 
in evidence

Retrieved the wrong dog’s 
record

Execution
Did not carry out actions as 
required
Skipped eligibility check

Completion
Did not produce the 
intended result

Failed to effectively schedule 
an outing

Propagation
An error carried forward 
into later steps

Wrong record leads to 
wrong match

## Page 26

Assign the label to the failed case

Test case

What went wrong
Ignored physical

handling ability

Retrieved the wrong

dog’s record

Broad error category
Judgment
Groundedness

Experienced
130 lb, too

strong

First-time

volunteer

Reactive, needs

experienced

handler

Propagation

Update labels as you go

## Page 27

Look at how often each problem showed up

Judgment

Reasoning error x 4

Scope violation x1

Groundedness

Hallucination x2

Faithfulness drift x3

Execution

Missing action x1

Make sure to count problems in runs with more than one error

Completion
0 failures

Needs checking

## Page 28

Harm depends on consequences

Volunteer could lose

control of the dog
High severity

I need to return 
these shoes

Sure. Returns are 
accepted within 30 days

No return policy

Dog shelter

Northwind

Customer trust

is lost
Moderate severity

Experienced
130 lb, too

strong

## Page 29

Prioritizing what to fix

Failure type
Expected 
frequency
Severity

Inconsistent 
formatting
Common
Low: information still correct
Improve later

Unsafe match
Occasional
High: volunteer could lose 
control of the dog
Fix now

Experienced
130 lb, too

strong

First-time

volunteer

Reactive, needs

experienced

handler

Try similar situations

Priority

## Page 30

Build a test set

you can trust

Module 2 · Video 4

## Page 31

A four-step workflow to build coverage

Find coverage

gaps

Add real 
examples

Generate 
missing cases

Curate the

test set

Expand coverage

Test case 
generator

## Page 32

Look for clues in what you already have

Mistakes you

found

Your 
requirements

First-time

volunteer

45 lb, calm

Experienced

volunteer

130 lb, too

strong

Experienced, but not 
eligible for outings

Real requests &

bug reports

Change one

detail

Try a more 
difficult case

Examples you

left out

New ones 
since then

## Page 33

Manual review

User requests

Bug reports

Support tickets

Support ticket:

experienced 
volunteer, not 
eligible for outings
Recorded runs

New test case

Original request

Volunteer record

Fill coverage gaps with real examples

Where to look:

Experienced volunteer, not eligible for outings

## Page 34

Use synthetic data for gaps you still can’t fill

Test case 
generator

Ask an LLM to fill in

the details

Experienced, but not

eligible for outings

Matches the situation

Realistic details

Expected outcome 
written down

Source noted, 
including edits

Write request

and records

Check before keeping

## Page 35

Keep cases that test a real difference

Dog handling 
notes missing

Volunteer 
experience

missing

Same case, 
different name

Remove: it repeats a check

you already have

Keep: it checks something

different

Same requirement, same expected outcome, still a different check

## Page 36

Curate the benchmark

Covers a meaningful situation

Protects against an important

regression

Clarifies a requirement boundary

Mistake

fixed

Still 
needed?

Keep: it could come

back

Remove
Rule 
dropped

Update the 
expected outcome
Rule 
changed

## Page 37

Include enough difficult cases in your benchmark

Test set A

Test set B

98%

The score describes your benchmark, not production metrics

98 straightforward cases

Straightforward
Difficult

More difficult cases than in everyday use

Straightforward: 98/98 passed
Difficult: 0/2 passed

## Page 38

Build the 
Northwind 
benchmark

Module 2 · Video 5

## Page 39

The benchmark workflow

Define 
requirements

Build test

cases

Analyze & 
label failures

Expand 
coverage

Curate the 
benchmark

Observe
Benchmark
Evaluate
Improve

## Page 40

Start with a behavior you already found

How should I care for my 
merino wool sweater?

You can machine wash 
it on a wool cycle and 
then tumble dry

You can machine wash 
it on a wool cycle and 
then tumble dry

Catalog:
Machine washable on wool cycle

The agent recommended 
tumble drying, but the sweater

didn’t have drying instructions

## Page 41

Turn one observation into a broader requirement

No drying 
instructions

Says to 
tumble dry

Too narrow

Don’t recommend 
tumble-drying this sweater

Broader 
requirement

Only make claims about 
products that are supported

by Northwind data

Review question

Does Northwind data 
support the claims in

this response?

## Page 42

Save the expected outcome for each case

No return policy 
information

Situation
Customer query
Northwind data
Expected outcome

Say the information is 
not available
What’s your return 
policy?

How should I care 
for my merino 
wool sweater?

What colors does 
the Classic Tee 
come in?

Machine 
washable on wool 
cycle

Use the supported 
washing instruction; no 
drying advice

White, black, navy, 
heather gray

Answer with the listed 
colors; add none
Complete 
info

Partial info

Missing info

## Page 43

Vary the customer side of the cases

What colors does the 
Classic Tee come in?

Do you have the Classic 
Tee in size medium and 
what colors are available?

Keep both

What colors does the 
Classic Tee come in?

Do you have the 
Classic tee in different 
colors?

Keep one of

them

## Page 44

Compare each run with its expected outcome

Pass run
Fail run

Expected 
outcome

Test case

White, black, navy,
heather gray, and forest green
White, black, navy,

heather gray
Agent 
response

What went 
wrong

Named a color not supported

by Northwind data

Groundedness →

Hallucination

What colors does the 
Classic Tee come in?

Catalog:
White, black, navy, heather gray

Answer with the listed colors; add none

Failure label

## Page 45

Label why a case failed

Pass run
Fail run

Expected 
outcome

Test case

You can return items

within 30 days
I do not have return Policy

information available
Agent 
response

Scope violation

What’s your return policy?
Northwind data:
No return-policy information

Say the information is not available

Failure label

## Page 46

Look across the set to find coverage gaps

Questions to ask
Cases by topic

Cases by expected response

Catch failures and confirm normal cases still work

Several unsupported product 
claims?

Invented policies outside of scope?

Cases where the agent should
say information is missing?

Cases where the agent should 
answer directly?

Care instructions ×6
Colors ×1

Materials 0
Sizing 0

Availability 0
Compatibility 0

Info is missing ×5
Answer directly ×1

## Page 47

Traces

Reviewed runs

User questions

Bug reports

Fill coverage gaps with real examples

Where to look:

Real question:
“Can the sweater

shrink in the

wash?”

Colors, materials, and

sizing questions

Support examples

Add to benchmark

Customer query

Expected outcome

## Page 48

Use synthetic data for gaps you still can’t fill

Right situation?

Realistic data?

Clear expected outcome?

Requirement unchanged?

Check before keeping

Test case 
generator

Use an LLm to 
generate them

Colors, materials, and

sizing questions

Create the 
case yourself

Which Classic Tee colors 
are selling out faster?

## Page 49

Curate the Northwind test set

Define 
requirements

Build test

cases

Analyze & 
label failures

Expand 
coverage

Curate the 
benchmark

Is the Classic Tee 
available in medium?

Is the Classic Tee available in 
medium, and what is your 
return policy?

Keep
Remove one

Do you have the 
Classic Tee in size M?

Covers a meaningful 
situation

Protects against an 
important regression

Clarifies a requirement 
boundary

A useful case:

## Page 50

Include enough difficult cases to measure them

Test set A

Test set B

98%

Read it in context: benchmark ≠ production

Straightforward product questions ×98

Straightforward
Difficult

More difficult cases during development

Straightforward: 98/98 passed
Missing information: 0/2 passed

## Page 51

What a complete benchmark case looks like

No return 
policy 
information

Customer query
Northwind 
data
Expected outcome
Source
Failure label

Say 
information is 
not available

Scope 
violation
What’s your return 
policy?

How should I care 
for the Merino 
Wool Sweater?

What colors does 
the Classic Tee 
come in?

Machine 
washable on 
wool cycle

Use only 
supported 
information

Faithfulness 
drift

White, black, 
navy, heather 
gray

Answer with 
the listed 
colors

Hallucination

Support 
example

Trace

Synthetic

## Page 52

1
Requirements

2
Test cases

3
Expected outcomes

4
Reviewed judgments

5
Failure labels

Your curated test set becomes a benchmark

Northwind
benchmark

Version 1

Version 2

Compare versions

against a stable

standard

Run it again as the

app changes
