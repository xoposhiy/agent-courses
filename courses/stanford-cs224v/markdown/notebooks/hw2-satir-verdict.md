# hw2-satir-verdict

[Course index](../../README.md) · [Original source](https://colab.research.google.com/drive/1YwmG0Nn9_XUiMmJltLnC4zjzzvcJHBwz) · [Raw file](../../raw/notebooks/hw2-satir-verdict.ipynb)

Retrieved: 2026-11-13T16:58:36.888602+00:00

## Cell 1

# Homework 2 Part 2 — Turning clinical text into constraints

**CS224V**

To decide whether a patient qualifies for a clinical trial, someone has to
compare two documents written in prose: the patient's chart and the trial's
eligibility criteria. A common approach today is to give both documents to a
language model and ask it for an answer.

This homework studies a different approach. A language model first
**translates** the criteria and the chart into SMT (satisfiability modulo
theories) — named variables and logical
constraints. A solver then **decides** eligibility from those constraints. You
will see what this makes possible (searching thousands of trials quickly, and
checking *why* a decision was made) and where it falls short.

## Cell 2

### Where all of this comes from

Everything in this notebook is a real system, and you can read all of it. Open
these now if you want to follow along in the source; later sections point at
specific files.

| | |
|---|---|
| **the code** | [`stanford-oval/clinical-trial-matching`](https://github.com/stanford-oval/clinical-trial-matching) — start at [`docs/QUICKSTART.md`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/docs/QUICKSTART.md), then [`docs/ARCHITECTURE.md`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/docs/ARCHITECTURE.md) for how the pieces fit |
| **retrieval (Part 2)** | **SatIR**, the system that searches trials with constraints; its paper is [arxiv.org/abs/2604.08849](../readings/arxiv-2604-08849.md) |
| **the audit (Part 3)** | **VERDICT**, the method for checking why a decision was made; its paper is [arxiv.org/abs/2609.03366](../readings/arxiv-2609-03366.md) |

You do not need any of it to do the homework. The notebook runs on saved
outputs, and the questions are answerable from what you see here.

## Cell 3

### Who does what

Every system in this notebook uses both a language model and ordinary code.
They do different jobs:

| | what it is good at | what it does here |
|---|---|---|
| **the language model** | reading messy prose, e.g. turning "FEV1 < 50% pred" (a lung-function test result) into something named | **translation**: text → named variables and constraints |
| **the code** | giving the same answer for the same input, showing its work, searching 3,621 trials in about three seconds | **decision**: solve the constraints, retrieve, explain, probe |

All of the language-model work is translation, and translation is not a single
call. It is a **chain** of them: the trial text is split into separate
requirements, its medical terms are linked to a standard vocabulary, the
constraints are written piece by piece, and further calls check the earlier
output. The two compilers in the real system use over 160 prompts in total.

## Cell 4

### When the model is called

It depends on what is being read:

- **Trials** are translated once, offline, before any patient arrives.
- **Patients, for retrieval** (Part 2), are also read once and on their own,
  into
  constraints over the shared vocabulary. No trial is involved, so this too can
  be done ahead of time.
- **Patients, for a verdict** (Parts 1 and 3), have to be read *against one
  specific trial* — the model is asked about exactly the variables that trial
  declared. That is a **pairwise** call, made when the pair is considered;
  precomputing it would require a model call for every patient–trial pair.

Everything after that read is code: deciding, retrieving, and every audit step
in Part 3.

Whenever you are looking at something a model wrote, the text says so. Watch
that hand-off: the code treats the model's translation as correct, so if the
translation is wrong, the code's results may also be incorrect.

We say *language model* rather than *LLM* because some of the models are not
large: the baseline in Part 2 turns text into vectors with a BERT-sized model,
much smaller than the models that do the translation.

## Cell 5

### What you will do

| part | |
|---|---|
| 1 | watch text become constraints, and solve one |
| 2 | turn the constraints into database rows and use them to search for trials |
| 3 | audit a decision: policy, assumptions, pivotal conditions, self-faithfulness |
| 4 | propose how SatIR/VERDICT could improve GRILL from Homework 1 on rare-disease diagnosis |

### Ground rules

- **No API key, no model calls, nothing to install.** Every model step was run
  in advance, and its real output is saved in this notebook. You read those
  outputs instead of calling a model yourself.
- Reflections are graded on reasoning, not on agreeing with us.

## Cell 6

## Setup

The cell below is the data: every model output, solver verdict and evaluation
number this notebook uses, compressed into one string so the notebook is a
single
self-contained file. You never need to read it, but run it (and the unpacking
cell after it) before any other code cell: every later cell uses the variables
they define. `extract_artifacts.py` in the
course repo regenerates it from the research pipeline.

## Cell 7

```python
# The data, packed. Skip past this one; the next cell unpacks it.
ARTIFACTS = (
    "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"
    "Ic67"
)

```

## Cell 8

```python
# Everything this notebook needs is embedded in the cell below: real outputs
# from real runs, about 187 KB, compressed. No pip install, no API key, no
# download, no files beside this one.
import base64, json, zlib, pathlib, re, collections, itertools, contextlib, io

_BUNDLE = json.loads(zlib.decompress(base64.b64decode(ARTIFACTS)))
PAIRS = _BUNDLE['pairs']
RETRIEVAL = _BUNDLE['retrieval']
POLICY = _BUNDLE['policy']
CATEGORY = _BUNDLE['predicate_categories']
PROJECTION = _BUNDLE['projection']

def clip(text, n):
    """Shorten text for display, marking the cut with an ellipsis."""
    text = text.strip()
    return text if len(text) <= n else text[:n].rstrip() + ' …'

BY_ID = {p['pair_id']: p for p in PAIRS}

# Variable names are long on purpose -- Part 1 explains why -- and they are
# printed in full. Shortening them was tried and abandoned: two different
# variables kept rendering as the same string, which made them impossible to tell apart.
def short(name, width=None):
    return name

def pair_of(p):
    """A pair dict, or the id of one -- so both of these work:

        verdict(PAIRS[0])
        verdict('sigir-20144__NCT02114099')

    Anything else is told what was wanted."""
    if isinstance(p, dict) and 'pair_id' in p:
        return p
    if isinstance(p, str) and p in BY_ID:
        return BY_ID[p]
    if isinstance(p, str):
        raise KeyError(f"no pair {p!r}. Ids look like {PAIRS[0]['pair_id']}")
    raise TypeError(f'expected a pair or a pair id, got {type(p).__name__}. '
                    f'Try PAIRS[0], or a key of BY_ID.')

def readable(line):
    """An assertion without its SMT wrapper or its :named label."""
    body = re.sub(r'\s*:named.*', '', line.strip())
    for prefix in ('(assert (! ', '(assert '):
        if body.startswith(prefix):
            return body[len(prefix):]
    return body

print(f'{len(PAIRS)} patient-trial pairs, already parsed and solved')
print(f"  {sum(1 for p in PAIRS if p['eligible'])} eligible, "
      f"{sum(1 for p in PAIRS if not p['eligible'])} ineligible")
print()
print('they come from the SIGIR clinical-trial collection:')
print(f"  {RETRIEVAL['corpus']['patients']} patients, "
      f"{RETRIEVAL['corpus']['trials']:,} trials")

```

```text
12 patient-trial pairs, already parsed and solved
  5 eligible, 7 ineligible

they come from the SIGIR clinical-trial collection:
  59 patients, 3,621 trials

```

## Cell 9

---
# Part 1 — Text becomes constraints

Here is one real patient and one real trial. Read both before looking at any
code: everything in Part 1 is about turning these two pieces of prose into
something a solver can check.

## Cell 10

```python
# Print the patient note and the trial criteria.
# The case we follow through Parts 1 and 3.
pair = BY_ID['sigir-20144__NCT02114099']

print('PATIENT', pair['patient_id'])
print(clip(pair['patient_note'], 520))
print()
print('TRIAL', pair['trial_id'], '--', clip(pair['trial_title'], 70))
print(clip(pair['trial_criteria'], 620))

```

```text
PATIENT sigir-20144
A 2-year-old boy is brought to the emergency department by his parents for 5 days of high fever and irritability. The physical exam reveals conjunctivitis, strawberry tongue, inflammation of the hands and feet, desquamation of the skin of the fingers and toes, and cervical lymphadenopathy with the smallest node at 1.5 cm. The abdominal exam demonstrates tenderness and enlarged liver. Laboratory tests report elevated alanine aminotransferase, white blood cell count of 17,580/mm, albumin 2.1 g/dL, C-reactive protein …

TRIAL NCT02114099 -- Trial of Atorvastatin on the Persistent Coronary Aneurysm in Children …
Inclusion criteria: inclusion criteria: 

 Clinical diagnosis of Kawasaki Disease with giant aneurysm 

 Must be older than 10 years old 

 
Exclusion criteria: : 

 Subjects ever received coronary artery bypass graft (CABG) surgery. 

 Subjects have active hepatitis or persistent abnormal liver function such as elevated GOT and GPT. 

 Subjects have the past history of rhabdomyolysis. 

 Female subjects are pregnant or plan for child-bearing during study periods.

```

## Cell 11

A person would read both documents and decide. For a solver to decide, the prose
first has to be turned into variables and yes/no conditions. That takes three
steps.

### Step 1 — the language model names things

A model reads the criteria and writes SMT **declarations**: one typed variable
for each thing the trial cares about. This step uses a language model because a
phrase like "FEV1 less than 50% of predicted" has to become a *number with a
unit*, and the model interprets the clinical English to do that.

In the real system, this is a chain of calls, not one: the criteria are split
into separate requirements, each medical term is linked to a standard clinical
vocabulary (so two trials that mean the same thing get the same variable name),
and further calls check that work.

Here is what Step 1 produced for this trial. Each variable is shown with its
type and the meaning the compiler wrote down for it:

## Cell 12

```python
# Step 1's output for this trial: the declared variables (language-model output).
decls = [l for l in pair['smt'] if l.lstrip().startswith('(declare')]
meaning = pair['annotations']['variables']
print(f'{len(decls)} variables the trial cares about:\n')
for line in decls:
    name = line.split()[1]
    kind = 'number' if 'Real' in line or 'Int' in line else 'true/false'
    print(f'   {kind:10s} {name}')
    print(f"              means: {meaning.get(name, '(no note)')}")

```

```text
4 variables the trial cares about:

   true/false patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now
              means: Boolean indicating whether the patient currently has a clinical diagnosis of Kawasaki disease (acute febrile mucocutaneous lymph node syndrome).
   true/false patient_has_diagnosis_of_giant_aneurysm_now
              means: Boolean indicating whether the patient currently has a clinical diagnosis of giant aneurysm.
   true/false patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_inthehistory
              means: Boolean indicating whether the patient has a past clinical diagnosis of Kawasaki disease (acute febrile mucocutaneous lymph node syndrome).
   number     patient_age_value_recorded_now_in_years
              means: Numeric value indicating the patient's current age in years.

```

## Cell 13

The variable names are long on purpose.
`patient_age_value_recorded_now_in_years`
says *whose* attribute, *which* attribute, *when*, and *in what unit*. A short
name like `age` could mean different things in two documents written by
different people; the long name helps clarify the intended attribute in both the
trial and the chart.

### Step 2 — the language model writes the constraints

For simplicity, Part 1 works with the **inclusion criteria only**; exclusion
criteria are handled the same way and we set them aside here. (The verdict
printed in Step 3 does combine both sides.)

Next the model writes **assertions** over those variables — one per
requirement. Each is written in **SMT-LIB**, the standard text format that SMT
solvers such as Z3 read (an open standard maintained by the SMT-LIB initiative
since 2002). Each assertion carries a label attached through `:named`, such as
`REQ0_COMPONENT0`. The labels are what let the solver later report *which*
requirements failed, not just that something did.

Here is what Step 2 produced: each requirement first in the compiler's own
words, then as the SMT-LIB assertion the solver will check.

## Cell 14

```python
# Step 2's output for this trial: one assertion per requirement (language-model output).
asserts = [l for l in pair['smt'] if l.lstrip().startswith('(assert')]
said = pair['annotations']['requirements']
print(f'{len(asserts)} requirements:\n')
for line in asserts:
    tag = re.search(r':named (\S+?)\)', line).group(1)
    print(f'   {tag}')
    print(f"      in words : {said.get(tag, '(no note)')}")
    print(f'      in SMT   : {readable(line)}')
    print()

```

```text
3 requirements:

   REQ0_COMPONENT0_PRESCREEN_NOTES_MUST_COMPLETELY_SUFFICE
      in words : To be included, the patient must have a clinical diagnosis of Kawasaki disease.
      in SMT   : (or patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_inthehistory)

   REQ0_COMPONENT1_PRESCREEN_NOTES_MUST_COMPLETELY_SUFFICE
      in words : To be included, the patient must have a clinical diagnosis of giant aneurysm.
      in SMT   : patient_has_diagnosis_of_giant_aneurysm_now

   REQ1_COMPONENT0_OTHER_REQUIREMENTS
      in words : To be included, the patient must be age > 10 years.
      in SMT   : (> patient_age_value_recorded_now_in_years 10)


```

## Cell 15

Next to the trial text, the translation can be compared with the criteria. The
criterion
*"Clinical diagnosis of Kawasaki Disease with giant aneurysm"* became two
requirements, `REQ0_COMPONENT0` (Kawasaki disease, now **or** in the past) and
`REQ0_COMPONENT1` (a giant aneurysm). The criterion *"Must be older than 10
years old"* became `REQ1_COMPONENT0`, `(> age 10)`.

What you see here is trimmed for reading. In the compiled file, each declaration
also carries instructions for when the variable is true, false, or unknown, so
the real program is several times longer.

### Reading the chart

A model also reads the patient's chart, asks about exactly the variables Step 1
declared, and records what the chart says. When the chart says nothing, a value
has to come from somewhere else. By **policy** we mean the written rule for that
case: for each kind of variable, what a silent chart should be taken to mean.
Part 3 covers it in detail. Here is what the chart gave for this trial's
variables, and what the policy filled in:

## Cell 16

```python
# The chart read (language-model output), plus what the policy fills in.
def policy_value(var, side='inclusion'):
    """What the policy assumes when the chart is silent about var.

    Every pair program in this notebook is inclusion-only, hence the default.
    (Don't take the side from CATEGORY's 'polarity': it is stored once per
    variable name, not per trial, so it can name the wrong side.)"""
    c = CATEGORY.get(var, {})
    rule = POLICY['rules'].get(f"{c.get('level1')}|{c.get('level2')}", {})
    return rule.get(side, 'unknown_defer')

for line in decls:
    name = line.split()[1]
    if name in pair['observed']:
        print(f"   chart says      {name} = {pair['observed'][name]}")
    else:
        print(f'   chart is silent {name}')
        print(f'                   policy: {policy_value(name)}')
```

```text
   chart says      patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now = True
   chart is silent patient_has_diagnosis_of_giant_aneurysm_now
                   policy: assumed_false
   chart is silent patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_inthehistory
                   policy: assumed_false
   chart says      patient_age_value_recorded_now_in_years = 2.0

```

## Cell 17

So the solver gets: Kawasaki now = `True` and age = `2.0` from the chart, and
*no giant aneurysm* and *no past Kawasaki diagnosis* from the policy
(`assumed_false`: the policy assumes that a condition this rare would have been
written down).

### Step 3 — the solver decides

The language model's part is finished. From here on, everything is code: it
never reads the trial or the chart again, only the variables, the assertions,
and the patient's facts. Together these form an **SMT** problem, and Z3 answers
it: `SAT` if some assignment satisfies every assertion, `UNSAT` if none can.

Here, the answers have a direct meaning. `SAT` means "this patient could
qualify"; `UNSAT` means "these requirements cannot all hold for this patient,"
i.e. the patient is ineligible. The same reading applies to the exclusion
criteria, whose program asserts that the patient is *not* excluded: there,
`UNSAT` means the patient meets an exclusion criterion. For example, this trial
excludes *"Subjects ever received coronary artery bypass graft (CABG) surgery"*,
and its exclusion program asserts `(not
patient_has_undergone_coronary_artery_bypass_graft_inthehistory)`. A patient who
has had a CABG makes that assertion false, so the exclusion side is `UNSAT` and
the patient is excluded.

Before the verdict, here is the check done by hand, one requirement at a time,
with the values above plugged in. (Which requirements fail was computed with Z3
when this notebook's data was prepared; Z3 itself is not installed here.)

## Cell 18

```python
# Step 3, traced: plug the patient's values into each requirement.
for line in asserts:
    tag = re.search(r':named (\S+?)\)', line).group(1)
    fails = tag in pair['violated']
    print(f"   {'FAILS   ' if fails else 'can hold'}  {said.get(tag, tag)}")
failing = [t for t in pair['violated']]
print()
if failing:
    print(f'{len(failing)} requirement(s) fail for this patient, so the assertions cannot')
    print('all be true at once: the inclusion side is UNSAT -> INELIGIBLE.')
else:
    print('every requirement can hold: the inclusion side is SAT.')

```

```text
   can hold  To be included, the patient must have a clinical diagnosis of Kawasaki disease.
   FAILS     To be included, the patient must have a clinical diagnosis of giant aneurysm.
   FAILS     To be included, the patient must be age > 10 years.

2 requirement(s) fail for this patient, so the assertions cannot
all be true at once: the inclusion side is UNSAT -> INELIGIBLE.

```

## Cell 19

Kawasaki can hold (the chart says the child has it now), but the giant aneurysm
fails (the policy assumes none), and the age fails (2 is not over 10). Z3
reaches the same conclusion, and reports it like this:

## Cell 20

```python
# The solver's verdict, computed in advance by Z3. No model involved.
def verdict(p):
    """Print what the solver concluded and why; return True if eligible.

    The bool lets you count: with quiet output, sum(verdict(p) for p in
    PAIRS) is how you would score a whole run."""
    p = pair_of(p)
    print(f"{p['pair_id']}")
    print(f"   inclusion criteria : {p['inclusion_status'].upper()}")
    print(f"   exclusion criteria : {p['exclusion_status'].upper()}")
    print(f"   -> {'ELIGIBLE' if p['eligible'] else 'INELIGIBLE'}")
    if p['unsat_core']:
        print(f"   the requirements that could not all hold at once:")
        for name in p['unsat_core']:
            print(f'      {name}')
    return p['eligible']

verdict(pair)

```

```text
sigir-20144__NCT02114099
   inclusion criteria : UNSAT
   exclusion criteria : SAT
   -> INELIGIBLE
   the requirements that could not all hold at once:
      REQ0_COMPONENT0_PRESCREEN_NOTES_MUST_COMPLETELY_SUFFICE
      REQ0_COMPONENT1_PRESCREEN_NOTES_MUST_COMPLETELY_SUFFICE
      REQ1_COMPONENT0_OTHER_REQUIREMENTS

```

```text
False
```

## Cell 21

That list of requirement names is an **unsat core**: when a set of assertions
has no satisfying assignment, the solver can report a *subset* of them that
already cannot hold together. Here: the Kawasaki requirement, the
giant-aneurysm requirement and the age-over-10 requirement cannot all be true of
this patient.

The core is a by-product of the proof: when asked, the solver records which
assertions it used to prove `UNSAT`, and the labels from Step 2 turn that into
requirement names.

Read it carefully, though. A core is *a* set that conflicts, not a list of what
the patient fails. This one includes the Kawasaki requirement, which the patient
actually meets. Part 3 shows how to get the requirements the patient really
violates. Either way, the decision comes with checkable requirement names; a
free-text matcher may instead return a paragraph.

## Cell 22

### The same patient, a different trial

The patient is two years old, so the patient was not eligible for the aneurysm
trial. But
they have Kawasaki disease, and there is another trial for it.

A `SAT` verdict has no core, because there is no conflict. So "why eligible" is
answered differently: for each thing the trial asks about, did the **chart**
answer it, or was it left to the **policy** introduced above? Anything decided
by the policy is marked, because it is not evidence.
The first example below is this same patient; the second is a different patient
and trial, chosen because it has values the chart did not provide.

## Cell 23

```python
# For an eligible pair: which requirements did the chart answer, and which were assumed?
def basis(p):
    """For an eligible pair: evidence from the chart vs filled in by policy."""
    p = pair_of(p)
    decl = [l.split()[1] for l in p['smt'] if l.lstrip().startswith('(declare')]
    from_chart = [v for v in decl if v in p['observed']]
    from_policy = [v for v in decl if v not in p['observed']]
    print(f"{p['pair_id']}  ->  {'ELIGIBLE' if p['eligible'] else 'INELIGIBLE'}")
    print(f"   {clip(p['trial_title'], 58)}")
    print(f'   the trial asks about {len(decl)} things')
    for v in from_chart:
        print(f"      CHART   {short(v)} = {p['observed'][v]}")
    for v in from_policy:
        c = CATEGORY.get(v, {})
        where = f"{c.get('level1', '?')} / {c.get('level2', '?')}"
        side = 'inclusion'   # pair programs are inclusion-only, see policy_value()
        rule = POLICY['rules'].get(f"{c.get('level1')}|{c.get('level2')}", {})
        outcome = rule.get(side, 'no rule on file')
        print(f'      POLICY  {short(v)}')
        print(f"                 the chart is silent. It is {c.get('type', '?')}-valued"
              f' and comes from an {side} criterion.')
        print(f'                 classified as:  {where}')
        print(f'                 the rule for that class says:  {outcome.upper()}')
        print(f"                 which means:  {POLICY['states'].get(outcome, '')}")
    if from_policy:
        print(f'   -> {len(from_policy)} of {len(decl)} rest on a rule, not the chart.')
    else:
        print( '   -> every requirement was answered by the chart.')

basis(BY_ID['sigir-20144__NCT00000520'])
print()
basis(BY_ID['sigir-201522__NCT01259336c'])

```

```text
sigir-20144__NCT00000520  ->  ELIGIBLE
   Prevention of Coronary Aneurysms in Kawasaki Syndrome
   the trial asks about 4 things
      CHART   patient_is_child = True
      CHART   patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now = True
      CHART   patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now@@diagnosed_according_to_centers_for_disease_control_and_prevention_criteria = True
      CHART   patient_presented_to_participating_center_on_or_before_tenth_day_of_illness = True
   -> every requirement was answered by the chart.

sigir-201522__NCT01259336c  ->  ELIGIBLE
   Efficacy Of Itraconazole In Chronic Cavitary Pulmonary Asp …
   the trial asks about 6 things
      CHART   patient_has_finding_of_sputum_culture_positive_for_aspergillus_inthehistory = True
      CHART   patient_has_finding_of_hyphae_of_aspergillus_detected_inthehistory@@specimen_is_sputum = True
      CHART   patient_has_finding_of_hyphae_of_aspergillus_detected_inthehistory = True
      POLICY  patient_has_undergone_aspergillus_fumigatus_1_precipitin_level_inthehistory_outcome_is_positive
                 the chart is silent. It is Bool-valued and comes from an inclusion criterion.
                 classified as:  Procedure / Past or Ongoing Diagnostic Procedure
                 the rule for that class says:  UNKNOWN_DEFER
                 which means:  chart is silent; policy refuses to guess, defer to the visit
      POLICY  patient_has_finding_of_hyphae_of_aspergillus_detected_inthehistory@@specimen_is_bronchoalveolar_lavage_fluid
                 the chart is silent. It is Bool-valued and comes from an inclusion criterion.
                 classified as:  Symptom/Sign / Other Symptom/Sign
                 the rule for that class says:  UNKNOWN_DEFER
                 which means:  chart is silent; policy refuses to guess, defer to the visit
      POLICY  patient_has_undergone_aspergillus_species_culture_inthehistory_outcome_is_positive
                 the chart is silent. It is Bool-valued and comes from an inclusion criterion.
                 classified as:  Procedure / Past or Ongoing Diagnostic Procedure
                 the rule for that class says:  UNKNOWN_DEFER
                 which means:  chart is silent; policy refuses to guess, defer to the visit
   -> 3 of 6 rest on a rule, not the chart.

```

## Cell 24

Both verdicts say `ELIGIBLE`, but they differ in how much recorded information
supports them. The first rests
entirely on the chart (for the things listed above). In the second, half of the
things the trial asks about (three of six) were never recorded, and for each the
policy says `unknown_defer`: it leaves those items unresolved, so the solver may
treat them as
true. That eligibility is therefore *conditional*, and a coordinator should
check those three before contacting the patient.

**Accuracy does not show this difference**: both count as one correct answer.
Part 3 is about making it visible.

> **TODO 1.** Pick any other pair from `PAIRS` and run `verdict` on it. Then
> answer, in a few sentences:
>
> **(a)** Which step would you expect to be the fragile one — the model naming
> variables, the model writing assertions, or the solver? Say why, and what a
> failure of that step would look like in the output above.
>
> **(b)** The text above says a coordinator should check the second pair's three
> unrecorded, deferred items before phoning anyone. Push on that. Look at what
> those three actually are, and say which one you would check *first* and why —
> then say what would have to be true for you to skip the check entirely and
> trust the policy.

*Where this is implemented:* The compilers that produced those variables are
[`trial_compiler/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/trial_compiler)
and
[`patient_compiler/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/patient_compiler);
[`examples/01_decide_a_pair.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/01_decide_a_pair.py)
decides one pair end to end.

## Cell 25

```python
# YOUR TURN (TODO 1) -- run verdict() on other pairs and look for yourself.
#
#   for p in PAIRS: print(p['pair_id'], p['eligible'])
#   verdict(BY_ID['sigir-20144__NCT00000520'])   # an eligible one

for p in PAIRS[:3]:
    verdict(p)
    print()

```

```text
sigir-20144__NCT00000520
   inclusion criteria : SAT
   exclusion criteria : SAT
   -> ELIGIBLE

sigir-20151__NCT02150941a
   inclusion criteria : SAT
   exclusion criteria : SAT
   -> ELIGIBLE

sigir-201522__NCT01259336c
   inclusion criteria : SAT
   exclusion criteria : SAT
   -> ELIGIBLE


```

## Cell 26

```python
# YOUR ANSWERS for TODO 1. Replace the placeholder text, then run the cell.
# Keep the triple quotes. Running it again overwrites the previous answer.

todo_1a = """
(your answer to 1(a) here)
"""

todo_1b = """
(your answer to 1(b) here)
"""

print('TODO 1: recorded 2 answer(s).')

```

```text
TODO 1: recorded 2 answer(s).

```

## Cell 27

---
# Part 2 — The same constraints, used for search

Part 1 asked whether one patient is eligible for one trial. In practice, the
question is different: **given one patient and 3,621 trials, which trials are
worth checking?** Running the solver 3,621 times for every patient can be
time-consuming.

So the constraints are turned into database rows that can be searched quickly.
This step is called a **projection**. Two symbols name the before and after:

- **Φ** (phi) is the **original constraint set**: everything the trial's program
  and the patient's record say, in full.
- **Ψ** (psi) is the **projected constraint set**: what remains of Φ after
  dropping the parts a database cannot check.

The projection is **lossy on purpose**. Ψ keeps only conditions that are
*guaranteed* to follow from Φ, so

> **Φ ⇒ Ψ** — every patient–trial pair that Φ would match, Ψ also matches.

This is called **recall-preserving**: Ψ may match pairs that Φ would reject, but
it never misses a pair Φ would accept. In other words, Ψ holds
**necessary conditions, not sufficient ones**. A pair that Ψ rules out is truly
ruled out; a
pair that Ψ matches only goes on a shortlist, and the full solver checks it
against Φ.

**Example.** The aneurysm trial from Part 1 excludes patients with *active*
hepatitis. "Active" is not in the shared vocabulary, so Ψ cannot express this
condition and drops it. A patient with active hepatitis can therefore match Ψ —
a false match, which is allowed — and the solver then rejects them using Φ. The
reverse cannot happen: Ψ never rules out a patient that Φ would accept.

Below, the trial's part of Ψ is called its **gate**, and the patient's part is
called the **patient-side constraints**.

## Cell 28

### What gets dropped

The projection drops every variable that uses a **non-canonical** predicate —
wording that was not mapped to the shared vocabulary, so no patient record can
be compared against it. The technique is called **quantifier elimination**: it
removes those variables and keeps everything that still follows without them.
It is applied to trials and to patients separately, before either goes into the
database.

### Three words for the pieces

What remains is a set of requirements, each an OR of simple statements. Three
terms describe these pieces:

- An **atom** is one indivisible statement about one predicate: in Part 1,
  `patient_has_diagnosis_of_giant_aneurysm_now`, or
  `(> patient_age_value_recorded_now_in_years 10)`. Atoms become rows.
- A **clause** is the group of atoms the trial wrote as **one requirement**,
  where the atoms are *alternative* ways of meeting it — any one of them will
  do. `REQ0_COMPONENT0` in Part 1 was a clause holding *Kawasaki now OR Kawasaki
  in the past*: two atoms, either of which satisfies the requirement. That is
  why Level 2 of the search (see "How a search runs" below) marks a clause
  supported as soon as **one** of its atoms
  matches, and why splitting clauses into atom rows loses nothing — the `clause`
  column remembers which requirement the alternatives belong to.
- A **canonical predicate** is the name two atoms must share to be comparable at
  all, and getting there is work in two directions. Across the sides, trial and
  chart were written by different people and must end up in one vocabulary.
  Also *within* each side: one trial can phrase the same condition two ways, one
  chart can record a finding in the narrative and again in a lab table, and
  those must collapse onto one name or the same fact counts twice. That is why
  the Part 1 variable names were so long — the names include details used to map
  two
  phrasings to one name.

## Cell 29

### How the projection works

Here is the projection of a real trial from Part 1 (its exclusion side, which
has
more to project). The cell prints the full program and the gate it becomes, so
you can see what survives and what is dropped.

## Cell 30

```python
# The real projection, read off a real run. Nothing here is recomputed:
# PROJECTION holds each trial's normalised program and the quantifier-
# eliminated gate that the retrieval database actually stores for it.

side = PROJECTION['NCT02114099']['exclusion']

print('THE FULL EXCLUSION PROGRAM for this trial:')
print(f"   {len(side['variables'])} variables, {len(side['program'])} assertions")
print('   two of those assertions, shortened:')
for a in side['program'][:2]:
    print(f'      {a[:96]}...')

print(f"\nTHE GATE stored for retrieval: {len(side['gate'])} clauses, all of it:")
for a in side['gate']:
    print(f'   {a}')

kept = {v for v in side['variables'] if any(v in g for g in side['gate'])}
gone = [v for v in side['variables'] if v not in kept]
print(f'\n{len(gone)} of the {len(side["variables"])} variables survive into no clause at all:')
for v in gone[:6]:
    print(f'   {v}')
if len(gone) > 6:
    print(f'   ... and {len(gone) - 6} more')

```

```text
THE FULL EXCLUSION PROGRAM for this trial:
   16 variables, 16 assertions
   two of those assertions, shortened:
      (assert (! (not patient_has_undergone_coronary_artery_bypass_graft_inthehistory) :named REQ0_COM...
      (assert (! (=> patient_has_finding_of_inflammatory_disease_of_liver_now@@active patient_has_find...

THE GATE stored for retrieval: 4 clauses, all of it:
   (assert (not patient_has_undergone_coronary_artery_bypass_graft_inthehistory))
   (assert (not patient_has_diagnosis_of_rhabdomyolysis_inthehistory))
   (assert (or (not patient_has_finding_of_ast_sgot_level_raised_now) (not patient_has_finding_of_alt_sgpt_level_raised_now)))
   (assert (or (not patient_sex_is_female_now) (not patient_is_pregnant_now)))

10 of the 16 variables survive into no clause at all:
   patient_has_finding_of_inflammatory_disease_of_liver_now
   patient_has_finding_of_inflammatory_disease_of_liver_now@@active
   patient_has_finding_of_abnormal_liver_function_now
   patient_has_finding_of_abnormal_liver_function_now@@persistent
   patient_has_finding_of_inflammatory_disease_of_liver_now@@active@@strong_clinical_support
   patient_has_finding_of_abnormal_liver_function_now@@persistent@@strong_clinical_support
   ... and 4 more

```

## Cell 31

Sixteen assertions over sixteen variables became **four clauses**. The
shrinking is intended.

The variables that disappeared are mostly the ones with `@@` qualifiers, such as
`..._now@@active` and `..._inthehistory@@strong_clinical_support`. (A plain
variable can drop out too:
`patient_has_finding_of_inflammatory_disease_of_liver_now`
appears in this program only alongside its `@@active` refinement, so once the
refinement is dropped nothing is left to test.) The `@@` variables are
**non-canonical** refinements: no patient record is indexed by them, so a
database search could not test them. Quantifier elimination removes them and
keeps only what still follows.

The result is weaker than the program. The program excludes patients with
*active* hepatitis; the gate cannot see "active", so it keeps only what holds
without it. A patient can therefore pass the gate and still be excluded by the
full program.

## Cell 32

### The rule, on cases small enough to check by hand

Here is the same operation on small formulas that you can check by hand. Let `a`
and `b` be canonical predicates (a patient record can be indexed by them), and
let `w` be a non-canonical one that must be dropped. The gate keeps a condition
exactly when the program **entails** it — that is, when it must hold no matter
what `w` is.

| the program says | the gate keeps | why |
|---|---|---|
| `a AND w` | `a` | `a` has to hold whatever happens to `w` |
| `a OR b` | `a OR b` | both are canonical, so the alternatives are kept |
| `a OR w` | *nothing* | if `w` might be true, `a` need not be — nothing is guaranteed |
| `w AND (w implies a)` | `a` | `a` follows, even though `w` itself is dropped |

The third row illustrates the effect of a non-canonical alternative. A
requirement that offers a choice between something
testable and something untestable becomes **no constraint at all**. This is
where most of the shrinking comes from. It is also why the gate never rejects a
patient it should keep: dropping a condition can only let *more* patients
through.

### Across all the demo trials

Here is how much each demo trial's program shrinks.

## Cell 33

```python
# How much each trial's program shrinks when it is projected.
print(f"{'trial':14s} {'side':10s} {'variables':>10s} {'assertions':>11s} {'gate':>6s}")
tot_a = tot_g = 0
for trial, sides in sorted(PROJECTION.items()):
    for name, d in sorted(sides.items()):
        print(f"{trial:14s} {name:10s} {len(d['variables']):10d} "
              f"{len(d['program']):11d} {len(d['gate']):6d}")
        tot_a += len(d['program']); tot_g += len(d['gate'])
print(f'\n{tot_a} assertions in total become {tot_g} gate clauses.')
zero = sum(1 for v in PROJECTION.values() for d in v.values() if not d['gate'])
sides = sum(len(v) for v in PROJECTION.values())
print(f'{zero} of the {sides} sides project to nothing at all: for those the gate')
print('cannot rule anybody out, so every patient passes and the solver decides.')

```

```text
trial          side        variables  assertions   gate
NCT00000520    exclusion           3           2      0
NCT00000520    inclusion           6           2      1
NCT00233194a   exclusion          43          35      8
NCT00233194a   inclusion           7           3      0
NCT00393913    exclusion          20          20      8
NCT00393913    inclusion           6           4      1
NCT00774137a   exclusion          14          13      1
NCT00774137a   inclusion          13           3      0
NCT00796913    exclusion           4           5      1
NCT00796913    inclusion           2           2      0
NCT00851487    exclusion          56          47     14
NCT00851487    inclusion           8           8      0
NCT00929721    exclusion           6           6      1
NCT00929721    inclusion           4           4      1
NCT01084239    exclusion          53          42     10
NCT01084239    inclusion          30           9      1
NCT01259336c   exclusion          12          11      5
NCT01259336c   inclusion           6           1      0
NCT01991314a   exclusion          15          16      5
NCT01991314a   inclusion           3           4      1
NCT02114099    exclusion          16          16      4
NCT02114099    inclusion           5           3      0
NCT02150941a   exclusion          15          11      2
NCT02150941a   inclusion           3           1      0

268 assertions in total become 64 gate clauses.
8 of the 24 sides project to nothing at all: for those the gate
cannot rule anybody out, so every patient passes and the solver decides.

```

## Cell 34

Some sides project to **zero** clauses (8 of the 24 in the table above): none of
their logic can be expressed in the shared vocabulary, so the gate cannot
exclude anyone. That is still recall-preserving; it just saves no work for that
trial.

The gate has a second limit. Each clause is checked on its own, so **a set of
rows cannot express that one atom rules another out**. Nothing stops a patient
from matching "under five" in one clause and "over ten" in another, or a finding
from being treated as both present and absent.

Both limits are associated with the gate's speed-oriented design. They are
covered by running the full solver
afterward on every trial the gate lets through — which is why `NCT02114099` is
retrieved and only then found `INELIGIBLE`.

## Cell 35

> **TODO 2.** Reflect on the projection you just watched:
>
> **(a)** The gate is a set of independent rows, so it cannot record that one
> atom rules another out — nothing stops one clause being supported by *age
> under 5* while another is supported by *age over 10*. Describe a concrete pair
> of requirements that the gate would let through together but no real patient
> could satisfy.

## Cell 36

```python
# YOUR ANSWERS for TODO 2. Replace the placeholder text, then run the cell.
# Keep the triple quotes. Running it again overwrites the previous answer.

todo_2a = """
(your answer to 2(a) here)
"""

print('TODO 2: recorded 1 answer(s).')

```

```text
TODO 2: recorded 1 answer(s).

```

## Cell 37

### How a search runs

Once trials and patients are both stored as rows, a search is three database
joins:

| level | what gets joined | what comes out |
|---|---|---|
| **1. atom** | trial atoms ↔ patient atoms sharing a canonical predicate | compatible atom pairs |
| **2. clause** | atom pairs ↔ the clause each belongs to | a clause is *supported* if ≥1 of its atoms matches |
| **3. trial** | supported clauses back up to the trial | the trial is returned only if every retrieval-relevant clause is supported |

No model is called during a search; all model work happened earlier, when each
document was indexed. **Search runs without model calls**, and it takes about
three
seconds across all 3,621 trials.

## Cell 38

### What it is being compared against

The baseline works in two steps. A language model reads the patient note and
writes a short list of **keywords** (the conditions and findings worth searching
on). Those keywords are turned into a vector, and so is each trial. Retrieval
returns the trials whose vectors are closest.

Both approaches use language models, and both do that work ahead of time; at
search time, both are pure code. So this is not "with a model" versus "without".
The difference is *what the model is asked to write down*:

| | what the model writes down | what the query does with it |
|---|---|---|
| **embedding baseline** | keywords, then a vector of them | nearest neighbours by distance |
| **the constraint side** | named variables and constraints | a join on shared atoms |

That difference is what the comparison tests. A vector is a single point: it
does not explicitly identify *which* keyword matched, and the keyword list may
not preserve
whether a finding was present or absent. Named constraints keep that
information, which is why a join can report the reason for each match.

## Cell 39

```python
# Recall for each retrieval objective, from the evaluation on the
# full corpus. 'Recall' = of the trials a clinician judged useful for this
# patient, what fraction did the system actually return?
print(f"{RETRIEVAL['corpus']['patients']} patients, "
      f"{RETRIEVAL['corpus']['trials']:,} trials\n")
print(f"{'objective':30s} {'constraints':>12s} {'embeddings':>11s} {'gap':>7s}")
for o in RETRIEVAL['objectives']:
    gap = o['satir_recall'] - o['embedding_recall']
    print(f"{o['name']:30s} {o['satir_recall']:11.1f}% {o['embedding_recall']:10.1f}%"
          f" {gap:+6.1f}")
print()
print(f"query time, constraint side: "
      f"{RETRIEVAL['query_seconds_per_patient_satir']}s per patient "
      f"over {RETRIEVAL['corpus']['trials']:,} trials")

```

```text
59 patients, 3,621 trials

objective                       constraints  embeddings     gap
treat the chief complaint             93.7%       62.4%  +31.2
treat any condition                   92.1%       53.7%  +38.4
relevant to any condition             92.5%       70.3%  +22.3

query time, constraint side: 2.95s per patient over 3,621 trials

```

## Cell 40

**Recall** is the fraction of the trials a clinician judged useful for a patient
that the system actually returned. The constraint side's recall is 20 to 40
points higher. Two things about how recall was measured matter here:

- Recall is measured against **what a clinician judged useful**, not against a
  text-similarity score. A system optimized for text similarity is not being
  scored on its own objective.
- There are **three different objectives** ("treat the chief complaint", "treat
  any condition", "relevant to any condition"), and the constraint side can be
  *told which one you mean*. The embedding side does not explicitly encode that
  choice: the vector representation does not include a dedicated field for
  "I want trials that treat this, not merely mention it."

The second point may explain much of the gap, so it does not show that
constraints
are simply better than embeddings.

## Cell 41

```python
# How many trials each system hands back per patient. Recall is
# high if you return everything, so always look at this alongside it.
print(f"{'objective':30s} {'constraints':>12s} {'embeddings':>11s}")
for o in RETRIEVAL['objectives']:
    print(f"{o['name']:30s} {o['satir_trials_per_patient']:11.2f} "
          f"{o['embedding_trials_per_patient']:10.2f}")
print()
s = RETRIEVAL['patients_served_with_at_least_one_useful_trial']
print(f"patients given at least one useful trial: "
      f"{s['satir']} vs {s['embedding']} of {RETRIEVAL['corpus']['patients']}")

```

```text
objective                       constraints  embeddings
treat the chief complaint             3.25       2.17
treat any condition                   5.12       2.98
relevant to any condition            11.76       8.93

patients given at least one useful trial: 54 vs 50 of 59

```

## Cell 42

### Patient-side constraints

The patient's record is projected just as a trial's is, into **patient-side
constraints** over the same canonical predicates — the yes/no findings the
chart records as present. Each says how the patient relates to the fact: a
`disease`
recorded as present, or some other `positive finding`. These are what retrieval
starts from: for each patient-side constraint, which trials are aimed at it?

**Example.** For the 2-year-old from Part 1, the patient-side constraints
include *has Kawasaki disease now* (a `disease`), and *is a child* and
*presented by day ten of the illness* (both `positive finding`s).

The cell below runs that join by hand. Every trial it lists comes with the
patient-side constraints that brought it in, so "why was this retrieved" has an
answer identifying the patient-side constraints used in retrieval.

One caveat: this notebook does not include the patient's standalone retrieval
read, so the cell uses the facts from this patient's pairwise read against
`NCT00000520` as a stand-in. Those facts answer exactly what that trial asked,
so it is bound to surface; the informative part is *which* other trials do.

## Cell 43

```python
# Level 1 of the join, on the pairs you already have.
#
# A patient's recorded facts are p['observed']; what a trial asks about is
# its declared variables. Matching those is the atom level.
#
# Three restrictions below are not simplifications -- they are what the real
# join does, and leaving any of them out changes the answer:
#
#   1. only BOOLEAN facts, and only those recorded TRUE, can be matched.
#      The engine joins on `kind='bool'` and a truthy value. A number like
#      age is never a key: every patient has an age and every trial asks
#      about it, so it would match everything and discriminate nothing.
#      Numbers are constraints to CHECK later, not keys to retrieve on.
#   2. each patient-side constraint is TYPED: the patient is linked to it by a
#      relation, and the engine keeps them apart: a disease the patient is
#      recorded as having, versus any other positive finding. The real
#      system also canonicalises names before comparing them.
#   3. no @@ refinements. They are non-canonical (see "What gets dropped"
#      in the projection section), so the index has no rows for them.

def hit_kind(var):
    """How is the patient related to this fact? Disease, or other finding."""
    level1 = CATEGORY.get(var, {}).get('level1')
    return 'disease' if level1 == 'Disease/Disorder' else 'positive finding'

def is_key(var, value):
    """Usable as a retrieval key: boolean, recorded True, and canonical."""
    return value is True and '@@' not in var

def shared_facts(patient_pair, trial_pair):
    """The atoms that let this trial surface, each with its relation type.

    Boolean, recorded True, and canonical only -- see the restrictions above."""
    patient_pair, trial_pair = pair_of(patient_pair), pair_of(trial_pair)
    asked = {l.split()[1] for l in trial_pair['smt']
             if l.lstrip().startswith('(declare')}
    return sorted((hit_kind(v), v) for v in asked & set(patient_pair['observed'])
                  if is_key(v, patient_pair['observed'][v]))

me = BY_ID['sigir-20144__NCT00000520']
usable = [v for v, val in me['observed'].items() if is_key(v, val)]
print(f"patient {me['patient_id']}: {len(me['observed'])} recorded facts, "
      f"{len(usable)} of them usable as retrieval keys")
print('the rest are numbers, recorded False, or @@ refinements, and are not used as keys:')
for v, val in me['observed'].items():
    if not is_key(v, val):
        if not isinstance(val, bool):
            why = 'a number'
        elif val is False:
            why = 'recorded False'
        else:
            why = 'an @@ refinement, not canonical'
        print(f"      {v} = {val}  ({why})")
print()
missed = []
for other in PAIRS:
    shared = shared_facts(me, other)
    if shared:
        print(f"{other['trial_id']} would surface, because this patient has:")
        for kind, v in shared:
            print(f"      [{kind:16s}]  {v}")
    else:
        missed.append(other['trial_id'])
print(f"\nno shared atom, so never even looked at: {len(missed)} trials")
print('   ' + ', '.join(missed))
```

```text
patient sigir-20144: 6 recorded facts, 3 of them usable as retrieval keys
the rest are numbers, recorded False, or @@ refinements, and are not used as keys:
      exclusion_presented_after_tenth_day_of_illness = False  (recorded False)
      patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now@@diagnosed_according_to_centers_for_disease_control_and_prevention_criteria = True  (an @@ refinement, not canonical)
      patient_time_of_illness_onset_value_recorded_at_presentation_withunit_days = 5.0  (a number)

NCT00000520 would surface, because this patient has:
      [disease         ]  patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now
      [positive finding]  patient_is_child
      [positive finding]  patient_presented_to_participating_center_on_or_before_tenth_day_of_illness
NCT02114099 would surface, because this patient has:
      [disease         ]  patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now

no shared atom, so never even looked at: 10 trials
   NCT02150941a, NCT01259336c, NCT01991314a, NCT00393913, NCT00929721, NCT00796913, NCT00774137a, NCT00233194a, NCT00851487, NCT01084239

```

## Cell 44

### Retrieval uses both sides

That is the patient side. Retrieval applies **both**:

- the **patient-side constraints** bring trials in: a trial is a candidate
  because it targets something the patient has;
- the **trial-side constraints** — the gate from the projection section — then
  rule candidates out if the patient's facts violate one of the gate's
  clauses, which every eligible patient must satisfy.

So the explanation has two halves: *why it was found* (the patient-side
constraints above) and *why it was not ruled out* (the gate clauses it passed).
A vector similarity score of `0.83` alone does not provide either explanation.

The two types are kept separate rather than counted as one "overlap", because
they license different things: a shared diagnosis is a reason to consider a
trial, but a shared incidental finding usually is not. `NCT02114099` comes in on
the Kawasaki diagnosis — it is a Kawasaki trial — and Part 1 showed
the solver finds this patient `INELIGIBLE` for it. That is not a retrieval
failure. Retrieval's job is to produce a short list worth checking; the solver's
job is to decide.

*Where this is implemented:* The joins are implemented in
[`sql_retrieval/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/sql_retrieval)
(its `README.md` provides a description), and
[`examples/06_satir_retrieval.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/06_satir_retrieval.py)
runs a retrieval. The argument is in the SatIR paper,
[arxiv.org/abs/2604.08849](../readings/arxiv-2604-08849.md).

## Cell 45

---
# Part 3 — Auditing a decision

The audit provides information beyond the verdict. A coordinator told
"ineligible" needs to know what
the decision rests on, what the system assumed, and what would change it.

This part takes one decision through four questions. **All four are answered by
code**, not by the language model: the model's work (translating the criteria
and reading the chart) is already done, and the audit only examines the
solver's work.

| question | what it asks | who answers |
|---|---|---|
| **policy** | the chart is silent here — what do we do about that? | code, reading a written-down policy |
| **assumptions** | what did we fill in that nobody actually recorded? | code |
| **pivotal** | which conditions is this verdict actually resting on? | code, reading the solver's output |
| **self-faithful** | if those conditions changed, would the verdict change? | code, by re-running |

**A note on terms.** A *variable* is one declared name. A *requirement* is one
named assertion from the trial's criteria; helper assertions the compiler adds
(named `..._AUXILIARY...`, e.g. "a qualified finding implies the plain one") are
definitions, not requirements. The *pivotal conditions* are the requirements the
patient's evidence actually violates. As in Part 1, the audit below works on
each pair's **inclusion** requirements only, so counts of chart facts versus
assumptions cover those; assumptions on the exclusion side are not listed.

## Cell 46

### 1. Policy — what silence means

Charts are incomplete. A trial requires "no history of multiple sclerosis" and
the chart does not mention MS. There are three options: assume the
patient does not have it, assume they might, or refuse to decide and pass it to
a person.

This choice can affect matcher reliability, and its effects may go unnoticed. So
it is not left to the model or to whoever wrote the code. It is a
**written policy** that says, for each kind of predicate, what silence means.

Numbers need one extra step, because "the chart is silent about age" cannot be
read as true or false — a number is not a yes/no. So a numeric predicate is
**curried** first: the threshold and the condition on it are folded into a
single yes/no predicate. `age > 10` stops being *a number and a comparison* and
becomes one boolean, *age is over ten*, and that boolean gets an evidence state
like any other.

## Cell 47

```python
# The policy is a fixed, versioned document, not a prompt to a model.
print(f"policy: a fixed table of {len(POLICY['rules'])} rules, one per kind of predicate\n")
print('the five states a predicate can be in:')
for state, meaning in POLICY['states'].items():
    print(f'   {state:16s} {meaning}')
print()
print('what silence means depends on the KIND of predicate:')
for c in POLICY['categories']:
    print(f"   {c['id']}  {c['what']:26s} silent -> {c['silent_means']}")
    print(f"       e.g. {', '.join(c['examples'][:3])}")
    print(f"       why: {c['why']}")

```

```text
policy: a fixed table of 29 rules, one per kind of predicate

the five states a predicate can be in:
   assumed_false    chart is silent; policy reads silence as false
   assumed_true     chart is silent; policy reads silence as true (rare)
   explicit_false   the chart documents that this does NOT hold
   explicit_true    the chart documents that this holds
   unknown_defer    chart is silent; policy refuses to guess, defer to the visit

what silence means depends on the KIND of predicate:
   1a  common chronic disease     silent -> unknown_defer
       e.g. hypertension, type 2 diabetes, asthma
       why: common enough that a silent chart is weak evidence either way
   1b  named specific disease     silent -> assumed_false
       e.g. cystic fibrosis, multiple sclerosis, end-stage renal disease
       why: a condition this salient would have been written down
   1c  recent acute event         silent -> assumed_false
       e.g. MI within 30 days, acute exacerbation
       why: a recent event would be in the note

```

## Cell 48

Silence is interpreted differently depending on the condition. A chart that does
not mention **asthma** tells you little — many people have mild asthma that is
not in the note — so the policy says `unknown_defer`. A chart that does not
mention **cystic fibrosis** is treated as informative under this policy, because
the policy assumes that a chart for a CF patient would mention it, so the policy
says `assumed_false`.

That reflects the policy's clinical assumptions. It is written down **once** by
a person and applied
the same way to every pair, instead of having a model decide again, and possibly
differently, each time.

Here is one case of each state from the demo pairs:

| state | example |
|---|---|
| `explicit_true` | the chart says the 2-year-old has Kawasaki disease now |
| `explicit_false` | the chart for patient `sigir-201522` records that the patient is not pregnant |
| `assumed_false` | the 2-year-old's chart never mentions a giant aneurysm; it is a rare, specialist-managed disease that the policy assumes would be recorded, so silence is read as "no" |
| `unknown_defer` | the aspergillosis patient's chart never mentions an *Aspergillus fumigatus* precipitin test; for that class of diagnostic test the policy leaves the status unresolved |
| `assumed_true` | rarely used: silence is read as "yes" |

### 2. Assumptions — what we filled in

Whenever the policy fills in a value that the chart did not provide, that value
is an **assumption**. The system lists every one, because these are the parts of
the verdict that rest on a rule rather than on evidence, so a reviewer can
check them first.

## Cell 49

```python
# `observed` is what the pipeline actually read off the chart.
# Anything the trial asks about that is NOT in there is an assumption.
def evidence_states(p):
    """Per variable: did the chart say, or is it an assumption?"""
    p = pair_of(p)
    rows = []
    for line in p['smt']:
        if not line.lstrip().startswith('(declare'):
            continue
        var = line.split()[1]
        cat = CATEGORY.get(var, {})
        rows.append(dict(var=var,
                         observed=var in p['observed'],
                         value=p['observed'].get(var),
                         kind=cat.get('level2', 'uncategorised'),
                         why=cat.get('rationale', '')))
    return rows

rows = evidence_states(pair)
print(pair['pair_id'])
print()
for r in rows:
    state = None if r['observed'] else policy_value(r['var'])
    mark = 'CHART   ' if r['observed'] else ('DEFERRED' if state == 'unknown_defer' else 'ASSUMED ')
    val = f" = {r['value']}" if r['observed'] else ''
    print(f"  [{mark}] {short(r['var'])}{val}")
    print(f"           kind: {r['kind']}")
    if not r['observed'] and r['why']:
        print(f"           policy: {state} -- {r['why'][:70]}")
print()
n_ass = sum(1 for r in rows if not r['observed'] and policy_value(r['var']) != 'unknown_defer')
n_def = sum(1 for r in rows if not r['observed'] and policy_value(r['var']) == 'unknown_defer')
print(f'{n_ass} of {len(rows)} are assumptions (a value the policy filled in);')
print(f'{n_def} are deferred (left open); the rest are chart facts.')

```

```text
sigir-20144__NCT02114099

  [CHART   ] patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_now = True
           kind: Uncommon Acute Disease
  [ASSUMED ] patient_has_diagnosis_of_giant_aneurysm_now
           kind: Uncommon Chronic Disease
           policy: assumed_false -- Giant aneurysm is rare and specialist-managed.
  [ASSUMED ] patient_has_diagnosis_of_acute_febrile_mucocutaneous_lymph_node_syndrome_inthehistory
           kind: Uncommon Acute Disease
           policy: assumed_false -- Kawasaki disease (the syndrome) is rare and acute.
  [CHART   ] patient_age_value_recorded_now_in_years = 2.0
           kind: Age/Sex

2 of 4 are assumptions (a value the policy filled in);
0 are deferred (left open); the rest are chart facts.

```

## Cell 50

### 3. Pivotal conditions — what the verdict rests on

Part 1 showed the unsat core. Z3 returns *a* subset of the assertions that
cannot
hold together — not necessarily the smallest one, and not the only one. A
different random seed or assertion order can give a different core.

So the core is not "the reasons". It can even name a requirement the patient
*meets*: the Kawasaki trial's core included the Kawasaki requirement, and this
patient has Kawasaki disease.

What VERDICT reports instead are the **pivotal conditions**: every requirement
the patient's evidence actually **violates** — each checked against the chart
facts plus the policy's assumptions. Fixing **all** of them is necessary for the
decision to flip: if a patient violates three requirements, fixing one or two
changes nothing — each remaining violation is enough on its own to keep them
ineligible.

**Example.** For the 2-year-old and the aneurysm trial, two requirements are
violated: *older than 10* (the chart says 2) and *giant aneurysm* (the chart is
silent, and the policy assumes no). Those two are the pivotal conditions. Fixing
only the age still leaves no aneurysm, so the patient stays ineligible; only
fixing both flips the verdict. The unsat core, by contrast, also named the
Kawasaki requirement, which the patient meets.

We found them with Z3 when preparing this notebook's data and saved the result
with each pair.

## Cell 51

```python
# A bigger trial: how many of its requirements does this patient violate?
big = BY_ID['sigir-20141__NCT01084239']
named = {re.search(r':named (\S+?)\)', l).group(1)
         for l in big['smt'] if ':named' in l}
reqs = {n for n in named if 'AUXILIARY' not in n}   # helpers are definitions
print(clip(big['trial_title'], 66))
print(f'   requirements in this trial : {len(reqs)}')
print(f"   violated by this patient   : {len(big['violated'])}")
print()
n = len(big['violated'])
print(f"   {'both' if n == 2 else f'all {n}'} must be fixed for the verdict to flip.")

```

```text
Multicenter Study to Rule Out Myocardial Infarction by Cardiac Com …
   requirements in this trial : 6
   violated by this patient   : 2

   both must be fixed for the verdict to flip.

```

## Cell 52

```python
# Every requirement the patient's evidence violates, in readable form.
def pivotal(p):
    """The pivotal conditions: requirements the evidence actually violates."""
    p = pair_of(p)
    if p['eligible']:
        print(f"{p['pair_id']}: eligible -- nothing is violated.")
        return []
    by_name = {}
    for line in p['smt']:
        tag = re.search(r':named (\S+?)\)', line)
        if tag:
            by_name[tag.group(1)] = line.strip()
    print(f"{p['pair_id']}: INELIGIBLE -- {len(p['violated'])} requirement(s) violated")
    for name in p['violated']:
        body = by_name.get(name, '')
        shown = re.sub(r'\s+', ' ', readable(body))
        print(f'   {name}')
        print(f'      {shown}')
    return p['violated']

violated = pivotal(pair)

```

```text
sigir-20144__NCT02114099: INELIGIBLE -- 2 requirement(s) violated
   REQ0_COMPONENT1_PRESCREEN_NOTES_MUST_COMPLETELY_SUFFICE
      patient_has_diagnosis_of_giant_aneurysm_now
   REQ1_COMPONENT0_OTHER_REQUIREMENTS
      (> patient_age_value_recorded_now_in_years 10)

```

## Cell 53

### 4. Self-faithfulness — does the verdict actually depend on that?

So far, the pivotal conditions are the system's *claim* about why it made the
decision.
To test whether that claim is true, you cannot just reread the explanation. You
have to:

> **change what the system says the decision depends on, re-run it, and see
> whether the answer changes.**

Here, remove every pivotal condition and solve again. If the verdict is still
`INELIGIBLE`, those conditions do not account for the decision. For the aneurysm
trial, removing the age and aneurysm requirements leaves only the Kawasaki
requirement, which the patient meets, so the verdict becomes `ELIGIBLE`.

For a constraint system, this can be tested by re-solving. We re-solved
with Z3 when preparing the data; the cell below reads the result.

## Cell 54

```python
# Retract every pivotal condition, then read the re-solve (done with Z3
# when the data was prepared -- this notebook does not run a solver).
def retract_pivotal(p):
    """Remove every violated requirement; did the verdict flip?"""
    p = pair_of(p)
    if p['eligible']:
        print(f"{p['pair_id']}: eligible already -- nothing to retract.")
        return None
    flipped = p['flips_after_retraction']
    print(f"{p['pair_id']}  (verdict was INELIGIBLE)")
    print(f"   pivotal conditions retracted : {len(p['violated'])}")
    print(f"   verdict after re-solving     : {'ELIGIBLE -- it flipped' if flipped else 'still INELIGIBLE'}")
    return flipped

retract_pivotal(pair)
print()
inel = [q for q in PAIRS if not q['eligible']]
with contextlib.redirect_stdout(io.StringIO()):
    n = sum(bool(retract_pivotal(q)) for q in inel)
print(f'across all {len(inel)} ineligible demo pairs: {n} flip.')

```

```text
sigir-20144__NCT02114099  (verdict was INELIGIBLE)
   pivotal conditions retracted : 2
   verdict after re-solving     : ELIGIBLE -- it flipped

across all 7 ineligible demo pairs: 7 flip.

```

## Cell 55

**What this shows.** Every pair flips. That is expected: once every violated
requirement is gone, what's left can all hold for the patient, and for a
constraint system the verdict follows directly from the constraints. The full
version, run on a modified chart, is
[`examples/01_decide_a_pair.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/01_decide_a_pair.py).

**Why run it anyway.** The same experiment works on systems where the outcome
is not a foregone conclusion. For a matcher that explains itself in a paragraph, you edit
the chart to remove the reasons it gave, ask the model again, and check whether
the answer changes. Published results find that free-text matchers often do
*not* change: they give a reason, but their answer remains unchanged after its
removal, so the stated
reason may not account for the answer.

## Cell 56

Two limits of this test:

- **Passing it is not the same as being right.** A system that always answered
  "ineligible, because the patient is under 18" would flip perfectly whenever
  age changed, yet its decisions could still be wrong. Flipping provides
  evidence that the stated reasons
  affect the system's answer; it says nothing about whether they are *good*
  reasons.
- **Our setting differs from testing a model.** Re-running a solver does not require a
  model call and gives the
  same answer for the same input. Doing this with a model costs one call per
  edited
  chart, requires a way to make each edit and a way to check that the edit
  changed only what it should, and systems tested this way may score below
  perfect performance.

## Cell 57

> **TODO 3.** Reflect:
>
> **(a)** Of the four things in this part — policy, assumptions, pivotal
> conditions, self-faithfulness — which would you most want if you were the
> coordinator who has to phone the patient? Which would you most want if you were
> the regulator auditing the service a year later? Say why they differ, if they
> do.
>
> **(b)** Here the policy is a written document, fixed in advance. The
> alternative is to let a model judge each chart on its merits. Make the case for
> **both**: what is good and what is bad about each approach? Then say which you
> would use, and when.

*Where this is implemented:* The audit artifacts live in
[`verdict/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/verdict)
and
[`audit/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/audit),
and
[`examples/02_read_the_artifacts.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/02_read_the_artifacts.py)
prints them for one pair. The chart-editing experiment for model-based matchers
is in
[`counterfactual_modifier/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/counterfactual_modifier).
The VERDICT paper is
[arxiv.org/abs/2609.03366](../readings/arxiv-2609-03366.md).

## Cell 58

```python
# YOUR TURN (TODO 3) -- the audit tools, on any pair you like.
#
#   verdict(p) / evidence_states(p) / pivotal(p) / retract_pivotal(p)

for p in PAIRS:
    if p['unsat_core']:
        pivotal(p)
        print()
        break

```

```text
sigir-201524__NCT00929721: INELIGIBLE -- 1 requirement(s) violated
   REQ0_COMPONENT0_PRESCREEN_NOTES_MUST_COMPLETELY_SUFFICE
      (>= patient_age_value_recorded_now_in_years 50.0)


```

## Cell 59

```python
# YOUR ANSWERS for TODO 3. Replace the placeholder text, then run the cell.
# Keep the triple quotes. Running it again overwrites the previous answer.

todo_3a = """
(your answer to 3(a) here)
"""

todo_3b = """
(your answer to 3(b) here)
"""

print('TODO 3: recorded 2 answer(s).')

```

```text
TODO 3: recorded 2 answer(s).

```

## Cell 60

---
### Summary: who did what

| step | language model | code |
|---|---|---|
| read criteria, name the variables | ✅ | |
| write the assertions over those variables | ✅ | |
| read the patient's chart against those variables | ✅ | |
| decide sat / unsat | | ✅ |
| project atoms into tables | | ✅ |
| retrieve across 3,621 trials | | ✅ |
| apply the policy on silence | | ✅ |
| list assumptions | | ✅ |
| find the unsat core and the pivotal conditions | | ✅ |
| retract and re-solve | | ✅ |

The model owns the top three rows and nothing else. Each row is a job done by a
chain of calls: the trial side happens offline, the patient read happens once
per pair. Nothing below those rows calls a model. That is what makes Parts 2 and
3 possible: code can be re-run and can say why it decided.

The cost is that the code only knows what the translation gave it. If the model
translated a criterion wrongly, downstream results may reflect that translation
error. Part 4
asks how this approach could be combined with GRILL from Homework 1, where the
criteria are not written down in advance.

## Cell 61

---
# Part 4 — Combining the two

The tasks above used **criteria that were written down**. A trial
sponsor wrote "FEV1 < 50% of predicted", and the model's job was translation.

Homework 1 gave you the opposite situation. A rare disease, a cohort of patients
described by HPO terms (codes from the Human Phenotype Ontology, a standard list
of symptoms and findings), exactly one of whom has it — and no provided document
stating what the disease requires. GRILL had to go and find that out.

The two systems address different aspects of the same problem.

## Cell 62

### The two halves

**GRILL finds out what the criteria might be.** It searches the literature and
keeps a belief ledger — a running record, only ever added to, holding the
hypotheses it is entertaining, the evidence for and against each, and the
questions it has not answered. When a hypothesis is refuted it becomes a new
question rather than being deleted. What it produces is a report and a ranking
of the cohort.

**SatIR and VERDICT decide, and show their work.** Given criteria already in
hand, Parts 1-3 turned them into constraints, retrieved against them at scale,
and made the decision inspectable in four ways:

| | what it gives you |
|---|---|
| **policy** | a written-down rule for what a silent record means, per kind of finding |
| **assumptions** | the list of values the system supplied that nobody recorded |
| **pivotal conditions** | every requirement the patient violates; all must be fixed for the verdict to flip |
| **self-faithfulness** | change those requirements, re-run, see whether the answer moves |

Neither half is the whole system. GRILL can propose criteria but has no formal
account of what it assumed or what its ranking rests on. SatIR and VERDICT can
give that account, but only once somebody hands them the criteria.

## Cell 63

> **TODO 4.** Open question, argued rather than computed. In roughly 400 words:
>
> **How would you combine GRILL with SatIR/VERDICT to do better at rare-disease
> diagnosis than GRILL alone?** Sketch the combined system, then give at least
> two **concrete** examples of a case it would get right that GRILL by itself
> would not, or an error it would catch that GRILL would miss.
>
> Then name **one or two specific challenges** that would make it hard to build,
> and work each through a concrete example: what goes wrong, on what kind of
> case, and how you might get around it.
>
> There is no expected answer. Be specific about mechanism.
>
> Threads worth pulling, if you want a start:
>
> - Homework 1's own example: the report treats "hypotonia" as typically
>   present, but the top-ranked patient's record notes its **absence**. Which
>   part of Part 3 is about exactly that?
> - A record lists the HPO terms a patient *has*. What does a term's absence
>   mean, and which of the five evidence states would you give it?
> - Homework 1 asked what separates rank 1 from rank 2. What would the pivotal
>   conditions give you there?
> - Homework 1 asked whether repeated runs agreed. What does the Part 3
>   self-faithfulness probe add to that?
> - What does `UNSAT` mean when the constraints are themselves a hypothesis?

## Cell 64

```python
# YOUR ANSWER for TODO 4. Replace the placeholder text, then run the cell.
# Keep the triple quotes. Running it again overwrites the previous answer.

todo_4 = """
(your answer to TODO 4 here)
"""

print('TODO 4: recorded.')

```

```text
TODO 4: recorded.

```

## Cell 65

```python
# Save every answer you wrote above into one file to hand in.
import json

answers = {k: v.strip() for k, v in sorted(globals().items())
           if k.startswith('todo_') and isinstance(v, str)}
blank = [k for k, v in answers.items() if v.startswith('(your answer')]

with open('todo_answers.json', 'w') as f:
    json.dump(answers, f, indent=1)

print(f'wrote todo_answers.json with {len(answers)} answers')
if blank:
    print(f'still on the placeholder text: {", ".join(blank)}')
else:
    print('none are still on the placeholder text.')

```

```text
wrote todo_answers.json with 6 answers
still on the placeholder text: todo_1a, todo_1b, todo_2a, todo_3a, todo_3b, todo_4

```

## Cell 66

### Where the real code lives

Everything in this notebook came from a real system, and it is open source:

**https://github.com/stanford-oval/clinical-trial-matching**

It includes runnable examples for each part above. To explore a part further,
start with its example rather than with the module code.

| part | the example to run | the module behind it |
|---|---|---|
| 1 — text → constraints | [`examples/05_the_demo_pair.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/05_the_demo_pair.py) | [`trial_compiler/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/trial_compiler), [`patient_compiler/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/patient_compiler) |
| 1 — solving a pair | [`examples/01_decide_a_pair.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/01_decide_a_pair.py) | [`smt_core/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/smt_core), [`smt_matcher/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/smt_matcher) |
| 2 — retrieval | [`examples/06_satir_retrieval.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/06_satir_retrieval.py) | [`sql_retrieval/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/sql_retrieval), [`db_indexer/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/db_indexer) |
| 2 — screening one patient | [`examples/04_screen_a_patient.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/04_screen_a_patient.py) | `sql_retrieval/ops/` |
| 3 — the audit trail | [`examples/02_read_the_artifacts.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/02_read_the_artifacts.py) | [`verdict/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/verdict), [`audit/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/audit) |
| 3 — self-faithfulness | — | [`counterfactual_modifier/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/counterfactual_modifier) |
| adding your own matcher | [`examples/03_add_your_own_matcher.py`](https://github.com/stanford-oval/clinical-trial-matching/blob/main/examples/03_add_your_own_matcher.py) | [`matchers/`](https://github.com/stanford-oval/clinical-trial-matching/tree/main/matchers) |

The repository and the two papers are linked at the top of this notebook.

The data embedded in this notebook was extracted from real runs of the
trial-matching code over the SIGIR collection (a public benchmark of 59
patient notes and 3,621 clinical trials). Nothing here is synthetic.
