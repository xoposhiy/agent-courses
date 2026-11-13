# Accountable AI: SMT

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-SMT-match.pdf) · [Raw file](../../raw/slides/l-smt-match.pdf)

Retrieved: 2026-11-13T16:49:46.796690+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224V Course

Agentic AI

Lecture 3

Accountable AI: Let AI Read, Let Logic Decide

VERDICT: Clinical Trial Matching with SMT

1

Cyrus Zhou and Monica Lam

Accountable AI with Grounded, Faithful, Consistent, Actionable Rationales: A Case Study in Clinical Trial Matching with VERDICT 
Zikai Zhou, Yufei Jin, Yilin Xu, Yu-Chiang Wang, Chieh-Ju Chao, Monica S. Lam
In The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP) , Budapest, Hungary, 2026.

### Page links

- [Link 1](../readings/arxiv-2609-03366.md)

## Page 2

D EC I SI O N M AK I NG I N H I G H S T AK ES D O MAI N S

M ED IC I NE
M AT CH IN G PAT I EN TS WIT H CL IN ICA L T RI AL S

W H AT I S T HE DI AG NO SI S AND T RE AT M E NT FO R T HI S PAT I EN T?

F I NAN CE

A R E R EG U L AT IO NS FO L L OWE D FO R E ACH CL IE NT?

A R E CO NT RA CTS  FO L L OWE D FO R E ACH T RA NS ACT IO N?

L E G A L

H O W T O DE CI DE O N A DI S PU TE ACC OR DI NG T O T HE L AW,  CO NT RA CT?

## Page 3

T R US TW O R TH I NES S:  I MP R OV E T HE AC CUR AC Y O F A I

A T WH AT ACC UR ACY CAN A I  B E T RU S T ED?

## Page 4

STANFORD
LAM

AI-Based Decisions

•
OpenEvidence is correct 73% on MedExpertQA

•
Is it good enough?

•
Can we deploy without human expert judgment?

•
Is it useful for an expert doctor?

•
Is it useful for a new doctor?

## Page 5

STANFORD
LAM

Why is it not enough to just say “Yes” or “No”

90% accurate → 10% of the users are mishandled!

We need human-in-the-loop: AI must provide a point-by-point rationale

•
Experts need to check the argument
•
Why the decision?

•
What are the assumptions?

•
Ambiguity: Experts need to control the decision with policies
•
Does the decision adhere to the policies?

•
Experts and users need to follow up on the decision: e.g.
•
If the answer is no, an applicant wants to know how to become eligible

•
If the answer is yes, the doctor may need to change the diagnosis as 
certain patient condition changes.

•
What would change the decision? (pivotal condition)

Grounding

Faithfulness

Actionability

Consistency

## Page 6

STANFORD
LAM

Accountable Decision Making

Grounding: Why?
Is the stated reason the real reason?

Faithfulness: What was assumed?
Missing facts, filled in silently?
Assumptions: a check list to ensure they are true

Consistent: Following policies?
Same facts, same answer?

Actionability: What would change it?
Pivotal condition –
       A path to a different outcome

## Page 7

STANFORD
LAM

What are Pivotal Conditions?

•
Pivotal Condition: ”what would change the decision?”

•
If we flip the user’s record based on the pivotal condition
then the decision should change.

User Record
Decision, pivotal condition

Flipped Record

2. Change to satisfy

pivotal condition

1. Satisfies Constraint?

Flipped decision

Given: Constraint

3. Satisfies Constraint?

## Page 8

STANFORD
LAM

Pivotal Conditions are Useful in Practice

Stage=3, …
NO, stage = 4

Stage = 4, …

2. Change to satisfy

pivotal condition

1. Satisfies Constraint? 
Given: Stage = 4 …

3. Satisfies Constraint?

FVC = 50%... …
YES, FVC > 40%

FVC = 39%... …

2. Change to satisfy

pivotal condition

1. Satisfies Constraint?

NO

Given: FVC > 40% …

3. Satisfies Constraint?

YES

Monitor the stage of the 
patient for new eligibility

Update judgment
if relevant results change

FVC: Forced Vital Capacity

(lung capacity)

## Page 9

STANFORD
LAM

Pivotal conditions are applicable to all domains

Accident last year, …
NO, no accident for 3 yrs

Three years past w/o accidents …

2. Change to satisfy

pivotal condition

1. Satisfies Constraint? 
Given: safe-driver discount if 
             accident free for 3 yrs..

3. Satisfies Constraint?

No accidents in last 3 years
YES, no accident for 3 yrs

Accident in next year

2. Change to satisfy

pivotal condition

1. Satisfies Constraint? 
Given: safe-driver discount if 
             accident free for 3 yrs..

3. Satisfies Constraint?

NO

YES

Remind client how
they can get discount

Warn client that they
can lose discount if 
they get into an accident

## Page 10

STANFORD
LAM

Self-faithful matchers

•
A self-faithful matcher: Flipping the reported pivotal condition flips the decision!

•
However, a matcher may make mistakes

•
Self-faithfulness is a useful automatic metric for evaluating rationales
•
Measures % time 
flipping the record (according to the pivotal condition) flips decision

User Record
Decision, pivotal condition

Flipped Record

2. Change to satisfy

pivotal condition

1. Satisfies Constraint?

?

Given: Constraint

3. Satisfies Constraint?

Self-faithful test: 
Is the decision flipped?

## Page 11

STANFORD
LAM

Outline

•
Decision making with AI
•
Introduction to accountability

•
A real use case: Clinical trial matching
•
Complexity in missing data, handling of policies, and scale

•
LLM-based decision making: ChatGPT
•
Retrieval has poor recall; matching accuracy is OK, poor accountability

•
VERDICT: leveraging a theorem prover

•
Semantic parse from LLM to formal representation is challenging

•
Evaluation and comparison

•
An automatic evaluation metric: Self-faithfulness
•
VERDICT has similar accuracy!  But much better accountability

## Page 12

STANFORD
LAM

Outline

•
Decision making with AI
•
Introduction to accountability

•
A real use case: Clinical trial matching
•
Complexity in missing data, handling of policies, and scale

•
LLM-based decision making: ChatGPT
•
Retrieval has poor recall; matching accuracy is OK, poor accountability

•
VERDICT: leveraging a theorem prover

•
Semantic parse from LLM to formal representation is challenging

•
Evaluation and comparison

•
An automatic evaluation metric: Self-faithfulness
•
VERDICT has similar accuracy!  But much better accountability

## Page 13

STANFORD
LAM

Clinical trials

Trial Phases
Volunteers
Main question

1
a few dozen
Is it safe? What dose?

2
a few hundred
Does it seem to work?

3
thousands
Better than prior care?

For some patients, a trial is the only route to the newest treatment.

For drug manufacturers: trials are needed before releasing new drugs

## Page 14

STANFORD
LAM

What is the Problem?

~80%

of trials miss enrollment targets or timelines

$1.9B

spent on recruitment per year

## Page 15

STANFORD
LAM

All trials in US are in ClinicalTrials.gov!

## Page 16

C AVE AT

T H E T RI AL S U S ED I N PR ACT IC E AR E M O RE CO M PL ICA TE D

T HA N T HO S E I N CL IN ICA LT R IAL S . G OV

W E H AVE ACC ES S T O R EAL CL IN ICA L T RI AL CO NS T RAI NT S

T H RO U G H CO L LA BO R AT IO N WIT H S T ANFO R D M E D S CH O OL

## Page 17

STANFORD
LAM

Major bleeding;

Full 
Example

## Page 18

STANFORD
LAM

Eligibility criteria are constraints written in NL

•
Boolean structure:

•
and / or / one of / not both

•
Thresholds:

•
CrCl ≥ 60 mL/min

•
Time windows:

•
no chemo within 6 months

•
Exceptions:

•
unless disease is stable

•
Qualifiers:

•
documented, at screening visit

“Weakness attributable to ALS and 
documented SOD1 mutation. 
FVC ≥ 50% of predicted; 
stable FVC < 50% but ≥ 45% may be considered. 
If taking riluzole, dose must be stable.”

An example excerpt: 
Tofersen trial, simplified (SatIR Fig. 1)

FVC: Forced Vital Capacity (lung capacity)

## Page 19

STANFORD
LAM

3 pages of a real patient record

Pages of semi-structured text: history, medications, vitals, labs. Most of what a trial asks about is never mentioned at all.

## Page 20

STANFORD
LAM

Complexities in real-life decision making

1.   Objective alignment

2.   Constraints can be hard or soft

Trial intent
treat · prevent · diagnose

Patient objectives & preferences

chief complaint, geographic, treatment choice, ,,,

Text
Kind

Must have documented SOD1 mutation
Hard

Stable FVC 45–50% may be considered
Stable: soft / permissive

Able to attend weekly visits
Operational 
(ignored in matching)

## Page 21

STANFORD
LAM

Complexities in real-life decision making

3.   Data missingness

•
Most facts needed are missing

•
Data imputation: we need to guess the values

•
We hypothesize a guidance: if a fact is salient, it will be mentioned in the record.

•
Patient record with “appendix“ condition satisfies trial
asking for “acute appendix” but not “burst appendix”

•
Imputations become assumptions: must disclose to expert, in case expert disagrees

4.
Control with policies

•
Experts do not want to leave it to LLMs ”probabilistic solution”
→ No consistency, different treatments to different applicants!

•
Example: Unspecified biomarker reads as negative

## Page 22

STANFORD
LAM

Policies: expressed in natural language

By type
e.g. 
any unreported biomarker → negative.

Context-dependent
e.g. 
a missing lab is OK for prescreening

By direction of

Constraints
Silence suggests…

Exclusion
probably fine (soft)

Inclusion
probably doesn't qualify (soft)

## Page 23

STANFORD
LAM

Problem statement for matching against constraints

Given

1.
A clinical trial
2.
A patient record
3.
Policies

Rationale

Reasons why (grounding)

Assumptions made (faithfulness)

Pivotal condition (actionability)


Info needed for

matching
Value from
Source

OBSERVED
the record
evidence span

IMPUTED
a policy
which policy, how

UNRESOLVED
--
—

Provenance: how we derive the patient info

Decision (Eligible, Not eligible)
Rationale
Provenance

## Page 24

STANFORD
LAM

Why is clinical trial hard?

• Complexities in real-life decision making

• Hard and soft constraints

• Objectives and preferences

• Data imputation, assumptions, policies

• Logic: must hold jointly, not on average

• Vocabulary: synonyms and hierarchies

• Scale: 500k trials × dozens of rules

~80%

of trials miss enrollment targets or timelines

$1.9B

spent on recruitment per year

recall
precision
efficiency
controllability
interpretability

## Page 25

CO M PL EX I T IE S I N CL IN I CAL T R I AL MA TC HI NG

Q UI Z:  H O W DI D WE FI G UR E O UT T HE M O UT?

• Hard and soft constraints

• Objectives and preferences

• Data imputation, assumptions, policies

## Page 26

C L I NI C AL T R I AL M AT CH I NG H AS M UL TI P L E S UB P R OB L EMS

## Page 27

STANFORD
LAM

Two directions of matching

Trial → patients
One constraint set × many records. 
A standard database query.

Patient → trials

One record × 500,000+ constraint sets. 
Find every trial the patient satisfies.

Constraints
Candidates

Job Requirements
Resumes

Diagnosis guidelines
Patient records

System fault diagnosis
Conditions

Quiz: Which direction is harder?

Other Examples of Constraint Matching

## Page 28

STANFORD
LAM

Finding trials has 2 subproblems

How to retrieve relevant trials?

•
Find the likely candidates with high recall
•
Goal: 1. perfect recall: 0 false negatives (missed trials)
           2. as accurate as possible: few false positives
•
Preview of future lecture: 
New retrieval technique: constraint-satisfaction based
Much better recall and accuracy than embedding

Given a short list of trials: how to match a trial with a patient?

•
High accuracy and high accountability (this lecture)

## Page 29

STANFORD
LAM

Outline

•
Decision making with AI
•
Introduction to accountability

•
A real use case: Clinical trial matching
•
Complexity in missing data, handling of policies, and scale

•
LLM-based decision making: ChatGPT
•
Retrieval has poor recall; matching accuracy is OK, poor accountability

•
VERDICT: leveraging a theorem prover

•
Semantic parse from LLM to formal representation is challenging

•
Evaluation and comparison

•
An automatic evaluation metric: Self-faithfulness
•
VERDICT has similar accuracy!  But much better accountability

## Page 30

STANFORD
LAM

Architecture of typical LLM Matchers

Represent
text / keywords / embeddings

Retrieve
BM25 · dense retrieval
→

Judge
LLM, per criterion, 
with Chain-of-Thought
→

Example: TrialGPT (Jin et al., Nature Communications 2024)

## Page 31

STANFORD
LAM

TrialGPT: Finding Trials for Patients

Clinical

Trials

Keyword 
Generation
Parkinson 
Disease,
Cognitive 
Impairment,
CVID,
Biopsy,
……

Encode
(e.g., w/ MedCPT)

<•••••>

Trial-Side
Embedding

Patient

Note

Keyword 
Generation

Dementia,
Cough,
Dysphagia,
X-ray,
Tobacco,
Edema,
……

Encode
(e.g., w/ MedCPT)

<•••••>

Patient-Side
Embedding

Compare

1. Retrieval based on embedding similarity

2. Matching: Use LLM to patch patient record with retrieved trials

## Page 32

STANFORD
LAM

Two Problems with TrialGPT

Retrieval: constraints as soft signals

Negation, thresholds, time barely move a similarity score. 
 
Ineligible-but-relevant trials crowd out eligible ones.

Top results by similarity

✗Similar words, ineligible patient

✗Similar words, ineligible patient

✗Similar words, ineligible patient

✗Similar words, ineligible patient

✗Similar words, ineligible patient

✓The eligible match, ranked last

Judgment: plausible ≠ faithful

Rationales are generated to sound right,

not to trace the derivation

(Jacovi & Goldberg 2020; Lanham et al. 2023).

## Page 33

STANFORD
LAM

Benchmarks

SIGIR

59 synthetic patient vignettes
3,621 ClinicalTrials.gov trials

TREC 2021
50 synthetic patient vignettes
26,581 trials

Real clinical trials
Synthetic patient vignettes

## Page 34

STANFORD
LAM

Recall of 
Dense Retrieval

Recall
#Retrieved

SIGIR
93%
500

TREC 2021
92%
1000

TREC 2022
88%
1000

QUIZ: 
What if the life-saving trial
is not retrieved?

## Page 35

STANFORD
LAM

LLM-based matching

Invented blocker (grounding)

Trial:       Obstructive Sleep Apnea 
Patient: 10-year-old with sleep apnea 
               symptoms

LLM matcher result
Decision: ineligible
Reason: His age, 
                 since the trial does not specify
                 pediatric inclusion. 
Problem: The trial has no age criterion.

Silent assumption (faithfulness)

Trial: Pulmonary Embolism
Patient:  Suspected Pulmonary Embolism
               after hip surgery.

LLM matcher result: 
Decision: ineligible
Reason:  Imaging and labs not in the note.

Problem: Missing treated as failed.

LLM-based pipelines have around 90% accuracy, but poor accountability

Examples of inaccurate matching

## Page 36

Q UI Z:  
H O W D O ES AN L L M  MA TC HER HA ND L E T HE

CO M PL EX I T IE S I N CL IN I CAL T R I AL MA TC HI NG?

H O W T O I MP R OV E AC CO UNT AB I L I T Y?

• Hard and soft constraints

• Objectives and preferences

• Data imputation, assumptions, policies

## Page 37

STANFORD
LAM

Outline

•
Decision making with AI
•
Introduction to accountability

•
A real use case: Clinical trial matching
•
Complexity in missing data, handling of policies, and scale

•
LLM-based decision making: ChatGPT
•
Retrieval has poor recall; matching accuracy is OK, poor accountability

•
VERDICT: leveraging a theorem prover

•
Semantic parse from LLM to formal representation is challenging

•
Evaluation and comparison

•
An automatic evaluation metric: Self-faithfulness
•
VERDICT has similar accuracy!  But much better accountability

## Page 38

STANFORD
LAM

Tackle complexity with a theorem prover

LLM + Theorem Prover

VERDICT

Problems

Decision + Rationale + Provenance

Model Distillation

(Future)

Agentic System

LLM with improved native accuracy and accountability

Fine-Tune an LLM

## Page 39

STANFORD
LAM

VERDICT: Separate understanding from reasoning

LLM reads
text → formal representation (SMT)

SMT/MaxSMT Solver reasons
To derive decision, rationale, provenance
→

errors are attributable
representation is inspectable

reasoning is consistent
Let AI read. Let logic decide.

## Page 40

STANFORD
LAM

Logic-based reasoning has been used before

SatLM
LLM writes a declarative spec; 
a SAT solver solves it

Logic-LM
Several solvers + self-refinement 
from solver errors

Lang2LTL
Commands → 
linear temporal logic for planners

P
Previous AI 
Benchmarks
Clinical trial matching

Information
complete
mostly missing

Vocabulary
a few entities Large medical ontology

(350k+ terms & relations)

Setting
one answer
scale + 
a clinician in the loop

## Page 41

STANFORD
LAM

Introduction to Formal Notations

•
Propositional Logic (PL)
•
Variables: Boolean
•
Operators: and, or, not 
•
Conjunctive Normal Form: A and (B or C) and (A or D)…
•
SAT solver: checks if a set of PL statements are satisfiable

•
SMT (Satisfiability Modulo Theories)
•
Variables: Boolean, number, … 
•
Operators: and, or, not, arithmetic, numeric comparison
•
Conjunctive Normal Form: 
A and (B > 10  or  C + B > D) and (A or E)…
•
SMT solver: checks if a set of SMT statements are satisfiable

 More expressive than PL, 
     SMT solver more expensive than SAT solver
     but cheap compared to LLM matching

## Page 42

STANFORD
LAM

Satisfiability: can all of these be true at once?

(declare-const a Bool)
(declare-const b Bool)
(declare-const c Bool)
(assert (=> a b))
(assert (not (and b c)))
(assert c)
(check-sat)
; sat
; model: c=true, b=false, a=false

(assert a)
(check-sat)
; unsat
; core: a, a→b, ¬(b ∧ c), c

• SAT → a model 
(a witness assignment)

• UNSAT → an unsat core 
(the reason of UNSAT)

Add:

## Page 43

STANFORD
LAM

: -- An SMT Solver

•
Open-source solver by Microsoft Research, released 2007

•
Used in analysis, verification, testing for software and hardware,

•
E.g. Does there exist an input that causes errors in a program 
(CS 243)

•
NP-complete:

•
Propositional satisfiability

•
Uninterpreted functions, linear integer arithmetic

•
Highly optimized today with continuous research to this date

## Page 44

STANFORD
LAM

Matching with SMT

(assert (or has_cough has_fever))

(assert (>= age 18))

(assert (not is_pregnant))

(assert (= age 67)

(assert has_cough)

(assert (not is_pregnant))

Trial Req:

Patient Fact

SAT
Trial Req +

(assert (= age 67)
(assert (not has_cough)

(assert (not is_pregnant))

(assert (not has_fever)

Patient Fact

Trial Req +  
UNSAT

## Page 45

STANFORD
LAM

MaxSMT: Maximum SMT (solved by Z3)

Given a Boolean formula (a set of clauses)

SMT 
  
Does there exist an assignment to variables 
  
that makes the formula completely true (satisfiable)?

MaxSMT: maximize the number of satisfied clauses

Find an assignment 
       that makes the maximum number of clauses true

Weighted MaxSMT: maximize weighted sum of satisfied clauses

Hard constraints: infinite weight
  
Soft constraints:   finite weights
       Unsatisfied clauses of answer → Violated set (pivotal condition)

## Page 46

STANFORD
LAM

Formulating clinical trial matching

(declare-const crcl Real)
(declare-const ecog Int)
(assert (>= crcl 60.0))
(assert (<= ecog 2))

Clinical trial

Trial 
LLM Semantic Parser

Patient record

Patient record
LLM Semantic Parser

(assert (= ecog 3))

MaxSMT Solver

ecog is 3
 crcl not mentioned → a free variable

(<= ecog 2)

SMT Solver

UNSAT

Assumptions

Pivotal condition

LLM Verbalizer

Decision
Rationale
Provenance
+

Trace
(verifiable reason)

## Page 47

STANFORD
LAM

SMT decides; MaxSMT further explains

SMT returns a decision SAT/UNSAT, a trace (verifiable rationale), model/unsat core

Use MaxSMT to find assignment to unknown variables to maximize eligibility (Assumptions)

If SMT returns UNSAT (INELIGIBLE)
•
Use MaxSMT to find pivotal conditions that turn INELIGIBILITY to ELIGIBILITY
•
Hard constraints in trial (infinite weight)
•
Soft constraints (weight 1)
•
Pivotal conditions: soft facts violated by the optimum returned by MaxSMT

SMT returns SAT (ELIGIBLE)
•
Use MaxSMT to find pivotal conditions that turn ELIGIBILITY to INELIGIBILITY
•
Hard constraints: ¬(original constraints) (infinite weight)
•
Soft constraints: original soft constraints and assumptions (weight 1)
•
Pivotal conditions: soft facts violated by the optimum returned by MaxSMT

## Page 48

STANFORD
LAM

Example: Stage IV NSCLC, EGFR trial 
(VERDICT Fig. 1)

Trial constraint

(ecog ≤ 2) ∧egfr ∧¬platinum
∧(crcl ≥ 60)
; + stage IIIB–IV

Condition
Value
State

ecog
1
OBSERVED

platinum
false
OBSERVED

egfr
false
IMPUTED (Policy 1)

crcl
⊥
UNRESOLVED

• SMT: UNSAT → INELIGIBLE,

• MaxSMT: 
pivotal condition { egfr = false }

• Assumption assigned by model: 
crcl = 72 (to satisfy crcl ≥ 60)

Patient constraint

## Page 49

STANFORD
LAM

What the clinician sees

Decision: Not eligible as recorded

Why
an activating EGFR mutation is 
required; No result is on file.

Imputation
policy P1 reads the missing 
EGFR test as negative, 
not observed.

Assumption
no creatinine clearance on file, 
no policy supplies one; 
assume ≥ 60.

To reverse
confirm EGFR status.

Monolithic LLM
"Likely ineligible — no EGFR result on file."  
No artifact to inspect or rerun.

VERDICT

## Page 50

STANFORD
LAM

Returning to the Examples of LLM Failures

Invented blocker (grounding)

Trial:       Obstructive Sleep Apnea 
Patient: 10-year-old with sleep apnea 
               symptoms

LLM matcher result
Decision: ineligible
Reason: His age, 
                 since the trial does not specify
                 pediatric inclusion. 
Problem: The trial has no age criterion.

Silent assumption (faithfulness)

Trial: Pulmonary Embolism
Patient:  Suspected Pulmonary Embolism
               after hip surgery.

LLM matcher result: 
Decision: ineligible
Reason:  Imaging and labs not in the note.

Problem: Missing treated as failed.

VERDICT

Decision: Eligible in both,
Result:      Includes a list of items to confirm at the in-person visit.

## Page 51

STANFORD
LAM

Formulating clinical trial matching

(declare-const crcl Real)
(declare-const ecog Int)
(assert (>= crcl 60.0))
(assert (<= ecog 2))

Clinical trial

Trial 
LLM Semantic Parser

Patient record

Patient record
LLM Semantic Parser

(assert (= ecog 3))

MaxSMT solver

ecog is 3
 crcl not mentioned → a free variable

(<= ecog 2)

SMT solver

UNSAT

Assumptions

Pivotal condition

LLM Verbalizer

Decision
Rationale
Provenance
+

Trace
(verifiable reason)
Grounding
Faithfulness

Actionability

Consistency 
guaranteed by solver

Quiz: Are we 100% accurate and accountable?

## Page 52

STANFORD
LAM

VERDICT: Errors confined to LLM parser

Parser (NL → SMT)

where errors live now: visible, local, fixable

Solver

exact about the formula it's given
→

## Page 53

STANFORD
LAM

Formalism is not easy to work with!

(declare-const fvc_pct Real)
(declare-const fvc_stable Bool)
(assert (or (>= fvc_pct 50.0)

(and (>= fvc_pct 45.0) fvc_stable)))

• How to handle "May be considered"
-- ignored

• If "Stable" is not in the note: 
what do we assume?
-- treated as a free variable
   solver choose value to get a
   SAT decision. 
   (The value is the assumption)

• Should we use ≥ or >? 
-- simple decisions can change 
   the final outcome completely

The solver faithfully executes whichever the parser chooses.

Example: 
    FVC is greater than 50%; 
    If FVC is stable 45–50% may be considered

LLMS need to write down clearly how to interpret the NL → accountability

## Page 54

STANFORD
LAM

Details of semantic parser in the next lecture

## Page 55

Q UI Z:

C AN LO G I C- B ASE D B E WO R SE I N MA TC HI NG

T HAN L L M  MA TC HI NG?

## Page 56

STANFORD
LAM

Outline

•
Decision making with AI
•
Introduction to accountability

•
A real use case: Clinical trial matching
•
Complexity in missing data, handling of policies, and scale

•
LLM-based decision making: ChatGPT
•
Retrieval has poor recall; matching accuracy is OK, poor accountability

•
VERDICT: leveraging a theorem prover

•
Semantic parse from LLM to formal representation is challenging

•
Evaluation and comparison

•
An automatic evaluation metric: Self-faithfulness
•
VERDICT has similar accuracy!  But much better accountability

## Page 57

E V AL UAT I O N

H O W T O EV ALUA TE AC CO UNT AB I L I T Y?

1 .  H UM AN JU DG E ( N EC ESS AR Y,  EX PE NSI V E)

2 .  S EL F- FA IT H FUL NES S –  AN AU TO M AT IC ME TR I C!

## Page 58

STANFORD
LAM

Benchmarks

SIGIR-derived labels

552 patient-trial patients
5 GPT-5 judges with different review framings; 
Use majority vote -- 80.8% unanimous. 
Clinician audit of a stratified sample.

TREC 2021

363 patient-trial pairs
Official human judgments are based on 
relevance and not eligibility

Caveat
No benchmark states a missing-data policy: 
Accuracy partly measures agreement with 
an unstated one.

Real clinical trials
Synthetic patient vignettes

## Page 59

STANFORD
LAM

What matching costs

~45 min

552 pairs · 8 threads · ≈4,000 GPT-4.1 calls

< $ 1,000

final reported runs (≈$2,500 incl. early runs)

SatIR: pay once per trial
Heavy one-time parsing per trial, 
amortized over every patient; 
then fast retrievals (0.15s)

## Page 60

STANFORD
LAM

Accuracy: VERDICT similar to LLM matchers

SIGIR-derived, GPT-4.1, F1

0.359

0.721

0.835

0.884

0.900

TrialGPT

CoT LLM

ZSPM

LLMMatch

VERDICT

TREC 2021 F1
VERDICT
best LLM
DLSC

GPT-5-mini
0.828
0.776
0.700

Claude Haiku 4.5
0.800
0.704
0.700

Qwen2.5-7B
0.738
0.695
0.470

LoRA-tuned Qwen2.5-7B formalizer: 
0.738 → 0.829 F1 (≈ GPT-5-mini).

LLM-based matcher:

TrialGPT, CoT LLM, ZSPM, LLMMatch

Logic-based matcher: DLSC

BASELINES

## Page 61

STANFORD
LAM

Four pillars of accountability

Pillar
How LLMs fail it
Countermeasure

Grounding
reason ≠ the real reason
verified rationales

Faithfulness
gaps filled silently
assumptions (explicit ledger)

Consistency
same facts, different logic
policy adherence

Actionability
a bare "no"
pivotal conditions

## Page 62

STANFORD
LAM

Consistency and self-faithfulness

71–81%

Policy adherence of LLM matchers, 
even with the policy applied per condition

Putting the rules in the prompt lowered 
LLMMatch agreement (67.5 → 64.8).

Pivotal flip rate (ineligible → eligible)

26.6%

48.9%

57.7%

61.1%

65.0%

84.3%

ZSPM

LLMMatch

LLMMatch-Pivotal

TrialGPT

CoT LLM

VERDICT-E2E

QUIZ: Why is VERDICT-E2E not 100%

VERDICT-E22: end-to-end system including the parser

Consistency

Self-faithfulness

## Page 63

STANFORD
LAM

Error analysis

59 TREC disagreements

31

14

10

3

1

Missing-evidence imputation

Eligibility ≠ TREC relevance

Semantic parsing

Non-chart-decidable criteria

Incomplete trial input

(2.8% of decisions)

Gold answer is ambiguous

## Page 64

STANFORD
LAM

Clinician ratings

Mean accountability rating: VERDICT (top) vs. ZSPM (bottom)

5.00

4.69

5.00

4.25

5.00

3.62

5.00

3.12

Completeness · VERDICT

Completeness · ZSPM

Traceability · VERDICT

Traceability · ZSPM

Coherence · VERDICT

Coherence · ZSPM

Actionability · VERDICT

Actionability · ZSPM

90.6%
preferred VERDICT vs. ZSPM 75.0%

Preferred VERDICT vs. LLMMatch

Overall Preference

Completeness: does it address the criteria that matter?
Traceability:      does every claim trace to the record or to an explicit imputation? 
Coherence:      are the claims consistent with each other? 
Actionability:    does it say what is unresolved and what would change the decision?

## Page 65

STANFORD
LAM

Conclusions

Grounding: Why?
Is the stated reason the real reason?

Faithfulness: What was assumed?
Missing facts, filled in silently?
Assumptions: a check list to ensure they are true

Consistent: Following policies?
Same facts, same answer?

Actionability: What would change it?
Pivotal condition –
       A path to a different outcome

Accountability for High-Stakes Decision Making

Complexity of real-life decision making: Missing data, policies

Let AI read. Let logic decide
