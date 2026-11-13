# Constraint Satisfaction Based Retrievers

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-SATIR.pdf) · [Raw file](../../raw/slides/l-satir.pdf)

Retrieved: 2026-11-13T16:49:46.923480+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224V Course

Agentic AI

Lecture 4

Constraint-Satisfaction Based Retrieval

Case study: Clinical Trial Matching

1

Cyrus Zhou and Monica Lam

## Page 2

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

## Page 3

STANFORD
LAM

Cost of VERDICT

m: number of patients; n: number of trials  
 
     #times

•
Trial parsed only once  
 
 
 
 
 
       O(n)

•
Patient record is parsed differently for each trial    O(mn)

•
SMT, MaxSMT calls                                                       O(mn)

Too expensive for 500,000 clinical trials per patient!

Can we use a cheaper retrieval method to come up with a short list for matching?

Embedding-based retrieval has poor recall – may miss life-saving trials.

Goal: (1) Perfect recall

(2) High accuracy

New idea: SatIR, Constraint-satisfaction based retrieval

## Page 4

STANFORD
LAM

Key Idea in SatIR

m: number of patients; n: number of trials  
 
     #times

•
Trial parsed only once  
 
 
 
 
 
       O(n)

•
Patient record is parsed differently for each trial    O(mn)

•
SMT, MaxSMT calls                                                       O(mn)

Too expensive for 500,000 clinical trials per patient!

O(m)

SatIR

2.5K trials: 
0.14ms/patient

O(n)

D: Eligible trials for p (using DBses)

S: Eligible trials for p

(using SMT)
Patient p

S ⊆ D
PERFECT RECALL

INACCURACY 
D – S

KEY: Patient records
are coded once
for all trials

An important math concept

SatIR: Use relational algebra (Databases): less expressive, but much cheaper
          Project SMT formulas to relational algebra

## Page 5

STANFORD
LAM

SatIR: Satisfiability-based information retrieval

The constraints are stored in the databases

## Page 6

STANFORD
LAM

Why is this difficult?

1. SMTs symbols have no meaning!

•
Every nuance and inference needs to be spelled out

2. How to turn SMT satisfaction into database operations?

## Page 7

STANFORD
LAM

Outline of this Lecture

1. High-level concept in SatIR

2. Semantic parsing: NL to SMT for clinical trials

•
Basic concepts

•
Advanced concepts

3. Fast constraint-satisfaction based retrieval

4. Experimental Results

## Page 8

STANFORD
LAM

Outline of this Lecture

1. High-level concept in SatIR

2. Semantic parsing: NL to SMT for clinical trials

•
Basic concepts

•
Advanced concepts

3. Fast constraint-satisfaction based retrieval

4. Experimental Results

## Page 9

STANFORD
LAM

What is a Semantic Parser?

LLM Semantic Parser
Text
Formal Semantics

Translates NL into some formal representation

SMT, Database queries, etc.

## Page 10

STANFORD
LAM

Formal Semantics: SMT Representation

atom = (variable, cmp, target)
variable = (relation, concept, qualifier)
((hasCondition, Type2Diabetes, within5y), =, true)
((hasMeasurement, HbA1c, current), <, 7.0)

An SMT formula:  a set of atoms in a propositional formula (and, or, not)

For clinical trial matching:

## Page 11

STANFORD
LAM

Examples of Qualifiers

patient: type2_diabetes diagnosed three years ago
fact:  
type2_diabetes @@ \[t-3y, now\]

trial: 
type2_diabetes @@within5y
constraint: interval ∩ \[now-5y, now\] ≠ ∅

"steroid-induced osteonecrosis of the jaw"
 
✗steroid_induced, osteonecrosis, jaw
 
✓base: Osteonecrosis
  @@ qualifier: steroid-induced
  @@ qualifier: finding site = jaw

## Page 12

STANFORD
LAM

A parsed trial (Kawasaki disease, SatIR Fig. 3)

or evidence of active inflammation.

(assert (and kawasaki_now

(or coronary_dilatation_now

coronary_aneurysm_now)))
(assert (or

(and z_score_recorded_now@@any_major_segment

(>= z_score 2.5))
(and (or fever_now@@persistent

fever_now@@recrudescent)
(>= body_temp_celsius 38.0)
fever_now@@36h_after_initial_therapy)
acute_inflammation_now))

Kawasaki syndrome

with coronary artery dilation or aneurysm,

and ≥ 1 of:

coronary Z-score ≥ 2.5 in any major segment;

Persistent or recrudescent fever 
≥ 38.0 °C 
for ≥ 36 h after initial therapy;

## Page 13

STANFORD
LAM

SMT programs are complex

~360

Each trial is represented by 
a non-trivial SMT program.

Typical number of lines:

## Page 14

STANFORD
LAM

One-shot text-to-SMT is brittle

• Variables redeclared inconsistently

• Qualifiers dropped or misattached

• Polarity flips (esp. exclusions)

• Valid syntax, wrong meaning

• Split cohorts

• Reverse exclusion polarity → one list

• Make entity spans contiguous

• Make and/or precedence explicit

• Split into self-contained units

Problems
Techniques

## Page 15

STANFORD
LAM

Outline of this Lecture

1. High-level concept in SatIR

2. Semantic parsing: NL to SMT for clinical trials

•
Basic concepts

•
Advanced concepts

3. Fast constraint-satisfaction based retrieval

4. Experimental Results

## Page 16

STANFORD
LAM

Disadvantages of SMT Approach

•
SMT solvers operate on variables – they have no meaning

•
All information useful for SMT solvers must be included formally

1. Taxonomy: same concepts → same variable name

2. Implication relations between concepts

e.g. A ⇒ B means A satisfies B

3. Missing Data: most conditions in trials are missing

Canonicalization

Include 
implication relations

Data Imputation

## Page 17

STANFORD
LAM

Challenge 1: Canonicalization

Theorem provers operate on variables – they have no meaning

•
Same concepts must be represented by the same variables

Patient p
Trial t
p ∧ t

English
Has dizzy spells
Has syncope
SAT

Semantic parse
Has-dizzy-spells
Has-syncope
UNSAT

Canonicalized
Has-syncope
Has-syncope
SAT

Canonicalization is complex! So many clinical terms!

Standardization in medicine are important → SNOMED

Example

## Page 18

STANFORD
LAM

SNOMED
Systematized Nomenclature of Medicine – Clinical Terms

US Edition of SNOMED

•
300,000+ unique concepts

•
Over 1,000,000 descriptions

•
903,000 links or semantic relationships between concepts.

## Page 19

STANFORD
LAM

SNOMED Example

•
Top-level classes: Clinical Findings, Procedures, Observable Entities, Substances…

## Page 20

STANFORD
LAM

Using SNOMED in the SMT representation

atom = (variable, cmp, target)
variable = (relation, concept, qualifier)

An SMT formula: a set of atoms in a propositional formula (and, or, not)

Relations: (we defined them empirically)

•
e.g. hasFindingOf, hasCondition, hasMeasurement, hasUndergone

Canonical concepts

•
Use canonical terms from SNOMED in clinical trials and patient records

Non-canonical concepts

•
Many concepts are trials/patient records are NOT in SNOMED

•
Make up non-canonical variables with a description

•
E.g. HasAdequateSocialSupportForFollow

For clinical trial matching:

## Page 21

STANFORD
LAM

Canonicalization Algorithm

•
Problem: NER (Named entity recognizer)

•
Turn the informal English to the closest term in SNOMED

•
Challenges and solutions:

•
Many similar terms in SNOMED → Dense retrieval

•
Find the most precise entity in SNOMED → 
Retrieve, rerank, ensure equivalence, pick the most precise

## Page 22

STANFORD
LAM

How to Canonicalize?

"To be included, the patient 
must have isolated systolic 
high blood pressure”

“isolated systolic
  high blood pressure”

“systolic high blood pressure”

“high blood pressure”

Entity Span 
Identification

Dense retrieval
in SNOMED

1.
Systolic essential 
hypertension
2.
Systolic 
Hypertension
3.
High systolic 
arterial pressure

1.
Hypertension
2.
Primary 
hypertension
3.
Raised blood 
pressure

1.
High systolic 
arterial pressure
2.
Systolic   
Hypertension
3.
Systolic essential 
hypertension

Reranking

Systolic 
Hypertension

Systolic 
Hypertension

Hypertension

NOT SAME

SAME

SAME

Which is more 
specific?

Systolic 
Hypertension

Top Candidate  = Entity?

Entities

Candidates

## Page 23

STANFORD
LAM

A Full Trial Example

## Page 24

STANFORD
LAM

Challenge 2: Implication Relations Between Concepts

•
SNOMED includes implication relations between terms: 
  
 
 
∃ an edge (x,y) if y ⟹ x

Has-acute-chest-pain

Has-chest-pain
Has-acute-chest-pain ⟹ Has-chest-pain

•
Codifying the patient

•
If patient has x, includes ancestors of x

•
If patient has ¬ x, includes the ¬  of all descendants of x

¬ Has-chest-pain ⟹ ¬ Has-acute-chest-pain

Patient p
Trial t
p ∧ t

Canonicalized
Has-acute-chest-pain
Has-chest-pain
UNSAT

With 
implications

Has-acute-chest-pain
(Has-chest-pain)
Has-chest-pain
SAT
Example

## Page 25

STANFORD
LAM

Different kinds of subsumption

• Concept: AcuteAppendicitis ⊑Appendicitis

• Relation: HasDiagnosisOf ⊑HasFindingOf

• Qualifier: specific ⊑general

• Causal: 
postop hemorrhage ⊑underwent surgery

The patient records include all the implications

–42%

True positives 
if we don’t use the ontology

(TREC 2022, GPT-5 judge)

An important concept

## Page 26

STANFORD
LAM

Challenge 3. Missing Data

Trial asks about If missing,

assume:
Why

Pregnancy
false
Pregnancy is salient

Ability to walk
true
Inability to walk
is salient

Hospitalized 
now
unconstrained Could go either way

Per-condition LLM question

"If this were true, 
would it plausibly be in the note?"

1,190

stored default values (TREC)
–7 to –9%

true positives without them

Use salience of property in question to impute data
Assume: Important facts get written down

## Page 27

STANFORD
LAM

Using salience in handling specificity:

Note: "appendicitis"

Acute appendicitis

✓match allowed: "acute" is often left unwritten

Ruptured suppurative appendicitis

✗no match: 
an emergency would be documented

Widen to a more specific trial target only if the detail could plausibly be omitted.

when may a vague note match a specific trial?

Hierarchy of diseases

## Page 28

STANFORD
LAM

Other constraints

Objective
A trial matches if it…

treat-chief
treats the chief complaint

treat-any
treats any documented condition

relevant-to-any
is meaningfully related to any condition

The objective is a formula too: a product decision, made explicit.

Explicit matching objective

Trial constraints need to be classified as hard, soft, operational (ignored)

## Page 29

STANFORD
LAM

Size of patient records

49 patients  2,578 source fact lines → 48,845 SMT fact lines

patient facts after ontology enrichment (TREC, 49 patients)

## Page 30

STANFORD
LAM

Implementation Complexities

Reuse symbols

↓

Attach qualifiers

↓

New variables if needed

↓

Translate fragment

↓

Validate syntax · sorts and logic consistency · faithfulness

↓

Commit if valid; else roll back with error feedback

Each requirement 
its SMT lines: errors are attributable to a sentence.

Many steps to ensure the SMT program is correct

## Page 31

STANFORD
LAM

Summary: Disadvantages of SMT Approach

•
SMT solvers operate on variables – they have no meaning

•
All information useful for SMT solvers must be included formally

1. Taxonomy: same concepts → same variable name

2. Implication relations between concepts

e.g. A ⇒ B means A satisfies B

3. Missing Data: most conditions in trials are missing

Canonicalization

Include 
implication relations

Data Imputation

## Page 32

STANFORD
LAM

Outline of this Lecture

1. High-level concept in SatIR

2. Semantic parsing: NL to SMT for clinical trials

•
Basic concepts

•
Advanced concepts

3. Fast constraint-satisfaction based retrieval

4. Experimental Results

## Page 33

STANFORD
LAM

Projection of SMT to Relational Algebra

SatIR: Use relational algebra (Databases): less expressive, but much cheaper
          Project SMT formulas to relational algebra

D: Eligible trials for p (using DBses)

S: Eligible trials for p

(using SMT)
Patient p

S ⊆ D
PERFECT RECALL

INACCURACY 
D – S

## Page 34

STANFORD
LAM

SMT vs. Propositional Logic (PL) example
At least three of the following disorders: A, B, C, D, E, F, G

(assert (>= (+
 
 
 
   (ite A 1 0)
 
 
 
   (ite B 1 0)
 
 
 
   (ite C 1 0)
 
 
 
   (ite D 1 0)
 
 
 
   (ite E 1 0)
 
 
 
   (ite F 1 0)
 
 
 
   (ite G 1 0))
 
 
  3))

SMT
PL

(A∧B∧C) ∨(A∧B∧D) ∨(A∧B∧E) ∨(A∧B∧F)
∨(A∧B∧G) ∨(A∧C∧D) ∨(A∧C∧E) ∨(A∧C∧F)
∨(A∧C∧G) ∨(A∧D∧E) ∨(A∧D∧F) ∨(A∧D∧G)
∨ (A∧E∧F) ∨(A∧E∧G) ∨(A∧F∧G) ∨ (B∧C∧D)
∨(B∧C∧E) ∨(B∧C∧F) ∨(B∧C∧G) ∨ (B∧D∧E)
∨(B∧D∧F) ∨(B∧D∧G) ∨(B∧E∧F) ∨(B∧E∧G)
∨(B∧F∧G) ∨(C∧D∧E) ∨(C∧D∧F) ∨(C∧D∧G)
∨(C∧E∧F) ∨(C∧E∧G) ∨(C∧F∧G) ∨ (D∧E∧F) 
∨(D∧E∧G) ∨(D∧F∧G) ∨ (E∧F∧G)

Ite: If This Then
SMT is direct and succinct

Some requirements representable in SMT cannot be expressed in propositional logic

(e.g. counting incidents in a time window)

## Page 35

STANFORD
LAM

Projection designed to not lose recall 
sacrificing precision if necessary

(and T2DM@@within5y

(>= hba1c 7.0) (<= hba1c 10.0)
HasAdequateSocialSupportForFollowUp)

(and T2DM@@within5y

(>= hba1c 7.0) (<= hba1c 10.0))
; non-canonical atom projected away

A patient without social support 
matches
→ no loss in recall, loss in precision

## Page 36

STANFORD
LAM

Quiz: Why do we bother to include non-canonical atoms?

•
In retrieval:

•
In matching:

(OR T2DM@@within5y

(>= hba1c 7.0) (<= hba1c 10.0)
HasAdequateSocialSupportForFollowUp)

## Page 37

STANFORD
LAM

Projecting SMT Matching to Database Queries

1. Project away non-canonical parts

2. Represent as Canonical Normal Form 
    (AND of ORs of atoms)

3. Match = Table joins + aggregation

Projection: every step is conservative (in the paper)

Theorem: 
SatIR has perfect recall (assuming the SMT formulation is correct)

## Page 38

STANFORD
LAM

Representing PL formulas in DB: Example

(has_bipolar OR has_depression OR has_schizo) 
AND (NOT has_undergone_PCI) 
AND ((NOT is_smoking) OR (NOT is_drinking))

∧ (and)
clauses

C
∧

c1
a1

c1
a2

c1
a3

c2
…

c2
…

c3
…

∧ 
∨

a1
o1

a1
o2

a1
o3

a2
o4

a3
o5

a3
o6

∨ (or)
clauses

∨
Variables
Is Pos

o1
has_bipolar
1

o2
has_depression
1

o3
has_schizo
1

o4
has_undergone_PCI
0

o5
is_smoking
0

o6
is_drinking
0

Constraints

c1

a1
a2
a3

## Page 39

STANFORD
LAM

Matching Patient 1

pid
Variable
Val

123
has_bipolar
1

123
has_depression
1

123
has_schizo
0

123
has_undergone_PCI
0

123
is_smoking
0

123
Is_drinking
0

Patient Fact Table

has_bipolar AND has_depression

Constraints
∧ (and)
 clauses

C
∧

c1
a1

c1
a2

c1
a3

∧ 
∨

a1
o1

a1
o2

a1
o3

a2
o4

a3
o5

a3
o6

∨ (or)
clauses

∨
Variable
Is Pos

o1
has_bipolar
1

o2
has_depression
1

o3
has_schizo
1

o4
has_undergone_PCI
0

o5
is_smoking
0

o6
is_drinking
0

(has_bipolar OR has_depression OR has_schizo) 
AND (NOT has_undergone_PCI) 
AND ((NOT is_smoking) OR (NOT is_drinking))

+ Eval  literals

(SQL query)

## Page 40

STANFORD
LAM

Matching Patient 1

literal-Evaluated

pid
∨
Variable
Val
Is_pos
Eval

123
o1
has_bipolar
1
1
1

123
o2
has_depression
1
1
1

123
o3
has_schizo
0
1
0

123
o4
has_undergone_PCI
0
0
1

123
o5
is_smoking
0
0
1

123
o6
is_drinking
0
0
1

Constraints
∧ (and)
clauses

C
∧

c1
a1

c1
a2

c1
a3

∧ 
∨

a1
o1

a1
o2

a1
o3

a2
o4

a3
o5

a3
o6

has_bipolar AND has_depression

(has_bipolar OR has_depression OR has_schizo) 
AND (NOT has_undergone_PCI) 
AND ((NOT is_smoking) OR (NOT is_drinking))

+ Eval v 
(SQL query)

## Page 41

STANFORD
LAM

Matching Patient 1

∧
eval

a1
1

a2
1

a3
1

C
∧

c1
a1

c1
a2

c1
a3

Constraints
v evaluated

has_bipolar AND has_depression

(has_bipolar OR has_depression OR has_schizo) 
AND (NOT has_undergone_PCI) 
AND ((NOT is_smoking) OR (NOT is_drinking))

Eval ∧

C
C_eval

C1
1
SAT!

(SQL query)

## Page 42

STANFORD
LAM

Matching Patient (unsat)

∧
∧_eval

a1
1

a2
1

a3
0

C
∧

c1
a1

c1
a2

c1
a3

Constraints
∧ (and) Evaluated

(has_bipolar OR has_depression OR has_schizo) 
AND (NOT has_undergone_PCI) 
AND ((NOT is_smoking) OR (NOT is_drinking))

+Eval ∧

C
C_eval

C1
0
UNSAT!

has_schizo AND is_smoking
 
     AND is_drinking

(SQL query)

## Page 43

STANFORD
LAM

Theorem: projection never loses recall

The price: precision
Relational constraints are less expressive to evaluate; 
a downstream matcher re-checks candidates.

146 ms

per patient · 3,621 trials · laptop

## Page 44

STANFORD
LAM

Outline of this Lecture

1. High-level concept in SatIR

2. Semantic parsing: NL to SMT for clinical trials

•
Basic concepts

•
Advanced concepts

3. Fast constraint-satisfaction based retrieval

4. Experimental Results

## Page 45

STANFORD
LAM

More of the right trials

SIGIR 2016, treat-chief (59 patients, 3621 trials)
Relevant & eligible per patient

1.75

2.17

3.25

ClinBest (clinician keywords)

TrialGPT

SatIR

Union of good trials across techniques

54–70%

92–94%

TrialGPT

SatIR

TREC 2022 subset (50 patients, 2658 trials)
recall, treat-chief, qrel = 2 (highly relevant)

0.162

0.139

0.445

BM25

TrialGPT

SatIR

Labels: GPT-5 judge; validated a sample by 2 clinicians, strong agreement

## Page 46

STANFORD
LAM

Where SatIR still fails

74

found only by TrialGPT
(200 candidates per patient)

253

found only by SatIR

57 clear failures, by source

14

13

8

6

16

Patient-side parsing

Trial-side parsing

Under-specified evidence

Missing evidence

Other / design limits

"age over 15"  →  (> age 15)
; patient is 15
should it be (>= age 15)?
-- visible, arguable, fixable

Error Analysis

## Page 47

STANFORD
LAM

SatIR: a new retriever based on constraint satisfaction

Constraints in documents are stored as first-class objects in databases

1.  Be conservative: don't let unformalizable content exclude candidates

2.  Compile domain knowledge into constraints (largest effect)

3.  Store missing-data assumptions as data you can inspect and ablate

4.  Build programs incrementally, validated at every step

5.  Relax technique for speed if necessary

-- only with a proof of the properties you maintain
