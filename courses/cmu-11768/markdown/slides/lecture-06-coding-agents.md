# Lecture 6 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-06-coding-agents.pdf) · [Raw file](../../raw/slides/lecture-06-coding-agents.pdf)

Retrieved: 2026-11-13T16:45:28.442474+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Agents for Coding and
Software Development

Graham Neubig

Language Technologies Institute

From code completion to software engineering

1

## Page 2

Coding agents

Writes code

single completion

1

Modifies
repositories

modify multiple files

2

Performs
development

full software lifecycle

3

2

## Page 3

Three ingredients

Prompt
Tools
LLM

3

## Page 4

Models that write code

4

## Page 5

Writing code from a prompt

Language

syntax · APIs · idioms

Editing

condition on both sides

Reasoning

specification → behavior

5

## Page 6

Training a coding model

Pre-training

large corpora including code

Mid-training

code mixtures · longer contexts

RL post-training

reasoning · execution rewards

6

## Page 7

Pre-training: learning from code and text

Mix sources: web text, technical prose, mathematics, source code, and documentation.

Preserve structure: indentation, file boundaries, APIs, and text–code relationships.

Evaluate during training: held-out loss by domain + functional coding tasks.

L
​ =
LM
−E
​
​ log p
​(x
​ ∣
x∼D
​
mix ∑t
θ
t
x
​)
<t

Groeneveld et al., 2024 · OLMo, §2 ↗
7

### Page links

- [Link 1](../optional-readings/arxiv-2402-00838.md)

## Page 8

Pre-training: choosing and cleaning data

Filter by language and source: remove generated dumps, broken encodings, and low-

value repetition.

Deduplicate: forks, vendored libraries, near-identical files, and copied solutions.

Control provenance: record licenses, source dates, opt-outs, and sensitive-data

filtering.

Prevent leakage: split by repository or problem family; decontaminate evaluation tasks.

StarCoder · data selection, filtering, and decontamination ↗
8

### Page links

- [Link 1](../optional-readings/arxiv-2305-06161.md)

## Page 9

Pre-training: splitting code into tokens

Learn code-aware subwords: byte-level BPE on code + prose; identifiers can span tokens.

Preserve whitespace: spaces, tabs, and newlines carry syntax and literal content.

Compress frequent runs: merge whitespace into tokens instead of spending one token per

space.

Source
if·ready:↵····return·value↵

Tokens
if | ·ready | : | ↵··· | ·return | ·value | ↵

Actual StarCoder2 split · “·” = space, “↵” = newline, “|” = token boundary

StarCoder §5.3 ↗
Chen et al., 2021 · whitespace-run tokens ↗
StarCoder2 tokenizer ↗
9

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374.md)
- [Link 2](../optional-readings/arxiv-2305-06161.md)
- [Link 3](../optional-readings/ref-507fbf856e86.md)

## Page 10

Pre-training on a large code corpus

StarCoderBase

15.5B parameters

1T tokens · 80+ languages

Source, issues, commits,
notebooks

Most languages improve with
more tokens.

Horizontal: training tokens (billions) · Vertical: pass@1 · Each curve: one language

Li et al., 2023 · StarCoder ↗
10

### Page links

- [Link 1](../optional-readings/arxiv-2305-06161.md)

## Page 11

Mid-training: adding more code

Continue language-model training: increase code exposure while retaining text and

math.

Choose the mixture empirically: compare code gains with general-capability retention.

Code Llama: Llama 2 → 500B additional tokens for 7B / 13B / 34B models.

Then extend context: train on related files and longer sequences with suitable

positions.

Rozière et al., 2023 · Code Llama, §2 ↗
11

### Page links

- [Link 1](../optional-readings/arxiv-2308-12950.md)

## Page 12

Mixing code, text, and math

Code / text / math
Common code
MATH
MMLU

100 / 0 / 0
49.8
10.3
23.8

70 / 20 / 10
48.3
33.2
62.9

Hui et al., 2024 · Qwen2.5-Coder, Table 3 (selected columns) ↗
12

### Page links

- [Link 1](../optional-readings/arxiv-2409-12186.md)

## Page 13

Mid-training: handling longer inputs

types.py

Result.value can be None
→
worker.py

propagates Result
→
caller.py

complete the null check

Coherent sequences: related files, paths, and cross-file dependencies.

Positions + length: Qwen2.5-Coder trains at 8K → 32K; YaRN enables 128K.

Validate: cross-file completion, infilling, and short-context retention.

Qwen2.5-Coder · §3.2.2; see also Lecture 3 ↗
13

### Page links

- [Link 1](../optional-readings/arxiv-2409-12186.md)

## Page 14

Infilling: using code before and after a gap

Fill the return-type annotation

The body is to the right of the hole.

Use both sides to propose the span

The suffix supplies evidence for bool .

def is_positive(x: int) -> ____:
    return x > 0

def is_positive(x: int) -> bool:
    return x > 0

Fried et al. · InCoder, §2 and §4 · illustrative example ↗
14

### Page links

- [Link 1](../optional-readings/arxiv-2204-05999.md)

## Page 15

Infilling: marking and predicting gaps

Original
prefix span  suffix

Training
prefix \[M0\] suffix \[M0\] span  \[END\]

Inference
prefix \[M0\] suffix \[M0\] → generate span

One or more holes: distinct sentinels associate each span with its location.

Zero-shot edits: complete code, infer types, generate comments, rename variables.

Fried et al. · InCoder (2022 preprint; ICLR 2023), §2 and §4 ↗
15

### Page links

- [Link 1](../optional-readings/arxiv-2204-05999.md)

## Page 16

Infilling: the value of right context

Completed functions passing tests (%)

Inference method
Suffix used for
Single-line
Multi-line

Left-to-right · 1 candidate
Not used
48.2%
24.9%

Left-to-right · 10 candidates
Reranking only
54.9%
28.2%

Causal-masked infilling
Generation
69.0%
38.6%

Fried et al. · InCoder, §4.1 · HumanEval-derived infilling tasks ↗
16

### Page links

- [Link 1](../optional-readings/arxiv-2204-05999.md)

## Page 17

Infilling: preserving code completion

Pass@1 · matched 52B-token training budget

Training objective
HumanEval
MBPP

Left-to-right language modeling
6.0%
8.9%

Causal masking
8.0%
10.9%

Fried et al. · InCoder, §5 · objective ablation ↗
Related scaling study: Bavarian et al., 2022 ↗
17

### Page links

- [Link 1](../optional-readings/arxiv-2204-05999.md)
- [Link 2](../optional-readings/arxiv-2207-14255.md)

## Page 18

Beyond infilling: more ways to learn from code

Commit diffs

before + message → after / diff

Muennighoff et al., 2023 · OctoPack ↗

Diagnostics

broken code + error → repair

Yasunaga & Liang, 2020 · DrRepair ↗

Tests

program + test outcomes → reward

Le et al., 2022 · CodeRL ↗

Execution traces

program → executed lines + states

Liu et al., 2023 · CodeExecutor ↗

18

### Page links

- [Link 1](../optional-readings/ref-da2b91ad4c0e.md)
- [Link 2](../optional-readings/arxiv-2207-01780.md)
- [Link 3](../optional-readings/arxiv-2308-07124.md)
- [Link 4](../optional-readings/ref-2adaa3d79c8f-pdf.md)

## Page 19

Evaluating Generated Code

19

## Page 20

Comparing with a reference solution

Exact match: does generated code reproduce the reference?

BLEU-4: measure token n-gram overlap, with a brevity penalty.

Integer x: is it positive?
Code
Behavior

Reference
return x > 0
Specification

Small textual change
return x >= 0
Wrong at x = 0

Different expression
return not (x <= 0)
Equivalent for integers

Yin & Neubig, ACL 2017 · §5.1 ↗
Ren et al., 2020 · CodeBLEU ↗
20

### Page links

- [Link 1](../optional-readings/ref-f42efd394503.md)
- [Link 2](../optional-readings/arxiv-2009-10297.md)

## Page 21

Comparing code structure

Ren et al., 2020 · CodeBLEU · original overview figure ↗
21

### Page links

- [Link 1](../optional-readings/arxiv-2009-10297.md)

## Page 22

Comparing learned code representations

CodeBERTScore

Encode prompt + each code

snippet

Compare contextual token

vectors

Best matches → precision /

recall → F-score

Zhou et al., EMNLP 2023 · CodeBERTScore · original similarity heatmap ↗
22

### Page links

- [Link 1](../optional-readings/ref-c800402e2698.md)

## Page 23

Checking behavior by running code

Candidate

is_positive(x):
 return x >= 0

Test cases

Inputs: −1, 0, 1
Expected: F, F, T

Run code

Isolated runtime
Time + memory limits

Compare outputs

Input
Actual
Expected

−1
F
F

0
T
F

1
T
T

Fail: zero is not positive

Chen et al., 2021 · functional evaluation · classroom example ↗
23

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374.md)

## Page 24

Benefits and limits of execution checks

Benefit
Disadvantage / limit

Accepts different correct
implementations
Finite tests can miss incorrect behavior

Detects semantic errors through
execution

Needs trusted tests, dependencies, and isolated
execution

Matches observed behavior
Requires time and a stable execution environment

Chen et al., 2021 · functional evaluation ↗
Liu et al., 2023 · EvalPlus / test adequacy ↗
24

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374.md)
- [Link 2](../optional-readings/arxiv-2305-01210.md)

## Page 25

Evaluating functions and full programs

HumanEval

164 Python functions

docstring → completion

hidden unit tests

CodeContests

competitive problems · includes Codeforces

statement → full program

compile + test

HumanEval ↗
CodeContests / AlphaCode ↗
25

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374.md)
- [Link 2](../optional-readings/arxiv-2203-07814.md)

## Page 26

Success across multiple attempts

pass@k: probability that at least one of k sampled programs passes all tests

Chen et al., 2021 · HumanEval ↗
26

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374.md)

## Page 27

Non-functional requirements

Existing program

“Make this code faster”

Code LM

Edit the code

Revised program

Same outputs; less time

How is the requested improvement checked?

Runtime efficiency

Run tests + time execution
Score: speedup

Latency / resource use

Compare reference edits
Score: DiffBLEU

Maintainability / security

Static checks + edit match
CodeQL × DiffBLEU

Singhal et al., 2024 · NoFunEval · 397 code-editing tasks ↗
27

### Page links

- [Link 1](../optional-readings/arxiv-2401-15963.md)

## Page 28

Learning from test results

Sample responses

Problem → reasoning
+ final code

Run tests

Execute final code
Pass / fail → reward

Update model

Make rewarded
responses more likely

Sample again with the updated model

Luo et al., 2025 · DeepCoder · execution-reward RL ↗
28

### Page links

- [Link 1](../optional-readings/ref-833b519c816e.md)

## Page 29

Reasoning toward a solution

Compute 1 + … + n, for 0 ≤ n ≤ 10¹²

Iterate

Add every integer

sum(range(n + 1))

Too slow at large n

Pair endpoints

Derive formula; check 0, 1

n * (n + 1) // 2

Correct and efficient

Recall a formula

Mistranscribe the expression

n * (n - 1) // 2

Wrong already at n = 1

29

## Page 30

Coding accuracy after reinforcement learning

16K → 32K: response-token limit during RL (K = 1,000 tokens).
★ / 64K: more tokens at evaluation, no further RL. Orange dashed line: o3-mini.

Luo et al., 2025 · DeepCoder · LiveCodeBench coding tasks ↗
30

### Page links

- [Link 1](../optional-readings/ref-833b519c816e.md)

## Page 31

Agentic coding

31

## Page 32

From single-step to agentic coding

Single-step coding
Self-contained

prompt
→
Reasoning

+ code
→
Evaluate
the answer

Agentic coding
Issue +
existing files
→
Search → edit

→ run tests ↺
→
Patch +
evidence

32

## Page 33

The localize–edit–verify loop

Repository

cli.py

config.py

test_config.py

Localize

Where does zero
become the default?

Edit

Default only when
the value is None.

Verify

Zero + default cases
+ caller regressions

Failure → revise the hypothesis

Interaction-loop concepts: SWE-agent · original teaching diagram ↗
33

### Page links

- [Link 1](../optional-readings/arxiv-2405-15793.md)

## Page 34

Localize: find the cause

Localize the implementation

Zero is falsy: inspect the defaulting rule.

Reproduce the behavior

Now repair the condition, not the test.

$ rg 'retries' buggy_config.py
return config.get("retries") or 3

$ RETRY_MODULE=buggy_config python3 \
  -m unittest test_config.RetryTests.test_zero
AssertionError: 3 != 0
FAILED (failures=1)

34

## Page 35

Edit: change the defaulting rule

Before

All falsy values select the default.

After

An explicit zero now survives.

return config.get("retries") or 3
value = config.get("retries")
return 3 if value is None else value

35

## Page 36

Verify: check the fix and regressions

Run the existing tests
Use failures to guide the next step

Zero still becomes three?

Localize where the value changes.

A default case breaks?

Edit the rule, then verify again.

$ python3 -m unittest -v test_config

missing   → 3   PASS
None      → 3   PASS
zero      → 0   PASS
positive  → 2   PASS

Ran 4 tests: OK

36

## Page 37

An alternative: a fixed workflow

Xia et al. · Agentless, original overview figure ↗
37

### Page links

- [Link 1](../optional-readings/arxiv-2407-01489.md)

## Page 38

Coding toolsets

38

## Page 39

Coding with a shell-only toolset

Model

Choose a command

One shell interface

Read / search
rg, cat, find

Edit files
sed, Python, patch

Execute checks
pytest, build commands

bash

Output + exit status + timeout

mini-SWE-agent · shell-only interface and execution model ↗
39

### Page links

- [Link 1](../optional-readings/ref-ad5dac935a68.md)

## Page 40

Editing with shell commands

Replace text with sed

Match the line, write the result, replace the
file.

One shell, many editing methods

sed / awk

Text patterns and line-based changes

Python scripts

Compute replacements across files

sed 's/^RETRIES = 3$/RETRIES = 5/' \
  settings.py > settings.new
mv settings.new settings.py

40

## Page 41

Whole files and text replacements

Whole file · settings.py

Simple to apply; repeats unchanged code.

Pi write · OpenCode write · OpenHands create

Search / replace · send old and new

Compact; needs an unambiguous match.

OpenHands · Pi · OpenCode edit

RETRIES = 5
TIMEOUT = 30

settings.py
<<<<<<< SEARCH
RETRIES = 3
=======
RETRIES = 5
>>>>>>> REPLACE

Aider · formats ↗
OpenHands ↗
Pi ↗
OpenCode ↗
41

### Page links

- [Link 1](../optional-readings/ref-1d7f752bff82.md)
- [Link 2](https://github.com/OpenHands/software-agent-sdk/blob/df2ea8fa5542d5d2a543e108bc8b2d4fbbab34b1/openhands-tools/openhands/tools/file_editor/definition.py)
- [Link 3](https://github.com/anomalyco/opencode/blob/57ef3828431790c53f8f333c7ffbfe88770a1812/packages/opencode/src/tool/edit.ts)
- [Link 4](https://github.com/badlogic/pi-mono/blob/c1d4c801114545f47c440921d8b3e04aeb1e565d/packages/agent/src/harness/tools/edit.ts)

## Page 42

Diffs and patch commands

Unified diff

Standard: line positions + context.
Aider: omit hunk line numbers.

File-operation patch · Codex syntax

File operations + context; no line counts.

Codex · OpenCode / OpenHands (preset-dependent)

--- a/settings.py
+++ b/settings.py
@@ -1,2 +1,2 @@
-RETRIES = 3
+RETRIES = 5
 TIMEOUT = 30

*** Begin Patch
*** Update File: settings.py
@@
-RETRIES = 3
+RETRIES = 5
 TIMEOUT = 30
*** End Patch

Aider · unified diffs ↗
Codex · parser ↗
OpenCode · selection ↗
OpenHands · GPT-5 preset ↗
42

### Page links

- [Link 1](../optional-readings/ref-d36656dbba24.md)
- [Link 2](https://github.com/OpenHands/software-agent-sdk/blob/df2ea8fa5542d5d2a543e108bc8b2d4fbbab34b1/openhands-tools/openhands/tools/preset/gpt5.py)
- [Link 3](https://github.com/anomalyco/opencode/blob/57ef3828431790c53f8f333c7ffbfe88770a1812/packages/opencode/src/tool/registry.ts)
- [Link 4](https://github.com/openai/codex/blob/16ff14c266179e6a762dc8081e9dab73a96683e0/codex-rs/apply-patch/src/parser.rs)

## Page 43

Diff format can make a big difference

Method inside

a large class
→

Move to a
top-level function
→

Check syntax
and code preservation

Aider refactoring benchmark: 89 Python tasks

GPT-4 Turbo (gpt-4-1106-preview) · benchmark success rate

SEARCH / REPLACE
20%

Simplified unified diff
61%

Aider · unified-diff experiment and refactoring benchmark ↗
43

### Page links

- [Link 1](../optional-readings/ref-d36656dbba24.md)

## Page 44

Finding relevant code

Start with the symptom

A flag, a loader, and a retry loop may all
match.

Follow the value

Configuration input

Where is zero first read?

Defaulting logic

Where does zero become three?

rg 'retries' .

44

## Page 45

Navigating code with dependency graphs

Issue

Zero becomes three

config.py

retry_count(config)

cli.py

configure_client

calls

test_config.py

Zero / None / missing

tests

client.py

Retry loop

uses result

Retrieve the relevant neighborhood,
then check it with execution.

Chen et al., 2025 · LocAgent ↗
45

### Page links

- [Link 1](../optional-readings/arxiv-2503-09089.md)

## Page 46

Coding agent evaluation and

training

46

## Page 47

Evaluating issue resolution

Fail → pass  requested repair
Pass → pass  preserved behavior

Jimenez et al. · SWE-bench evaluation pipeline, original source figure ↗
47

### Page links

- [Link 1](../optional-readings/arxiv-2310-06770.md)

## Page 48

Building runnable training tasks

Runnable task

Starting state
Files + dependencies + test command

Issue
Requested behavior + reproduction

Checks
Bug fails before; repair restores behavior

Validate the environment before collecting training trajectories.

SWE-Gym · executable training environments ↗
48

### Page links

- [Link 1](../optional-readings/arxiv-2412-21139.md)

## Page 49

RL for multi-step code repairs

Assistant actions: training targets

Search

Find config.py

Edit

Preserve zero

Test / finish

Check regressions

Files found
Patch applied
Test output

Context only

Terminal reward: repaired or not

A late failure does not identify which earlier decision was wrong.

max
​ E
​\[R(τ)\]
θ
τ∼π
​θ

Jain et al., 2025 · R2E-Gym ↗
49

### Page links

- [Link 1](../optional-readings/arxiv-2504-07164.md)

## Page 50

Training data and inference compute

Training scale
Inference scale: learned-verifier selection

Pan et al., 2024 · SWE-Gym · 32B model ↗
50

### Page links

- [Link 1](../optional-readings/arxiv-2412-21139.md)

## Page 51

Creating repair tasks by injecting bugs

Prepare  executable baseline
Mutate  code, not tests
Keep  new test failures

Yang et al., 2025 · SWE-smith, original pipeline figure ↗
51

### Page links

- [Link 1](../optional-readings/arxiv-2504-21798.md)

## Page 52

Injecting and checking a bug

Working baseline

All four existing tests pass.

Mutate the condition

Zero now becomes three; its test fails.

Before  4 pass
Mutated  3 pass · 1 fail
Restored  4 pass

value = config.get("retries")
return 3 if value is None else value

value = config.get("retries")
return 3 if not value else value

SWE-smith · procedural mutation and execution validation ↗
52

### Page links

- [Link 1](../optional-readings/arxiv-2504-21798.md)

## Page 53

Working across programming languages

Python

pyproject.toml

src/

tests/

pytest

TypeScript

package.json

src/

tests/

npm test

Rust

Cargo.toml

src/

tests/

cargo test

Read the project configuration before choosing build and test commands.

Multi-SWE-bench ↗
SWE-bench Multilingual ↗
53

### Page links

- [Link 1](../optional-readings/arxiv-2504-02605.md)
- [Link 2](../optional-readings/ref-c18ff82e46ba.md)

## Page 54

Multi-harness training

Harness = prompts + tools + agent loop + context management

Shared model

Same weights

Example harnesses

OpenHands

OpenCode

Codex

Task checks

Patch → test reward

Trajectories + rewards → update the model

Nemotron 3 Ultra: ≥2 harnesses per task distribution
Polar: native harnesses call a shared model API proxy

Nemotron 3 Super ↗
Nemotron 3 Ultra ↗
Polar ↗
Harness implementations ↗
54

### Page links

- [Link 1](https://arxiv.org/abs/2604.12374)
- [Link 2](https://arxiv.org/abs/2605.24220)
- [Link 3](https://arxiv.org/abs/2606.15007)
- [Link 4](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server/tree/6a1ead6bfac054fce6c1e62d1a77b330d96c58db/src/polar/agent)

## Page 55

Frontend development

55

## Page 56

Agent-powered frontend development

Localize

Find components
and event handlers

Edit

Change logic
and styles

Verify in the browser

Exercise behavior

Type → click → check saved state

Inspect the rendered page

Screenshot → visual understanding

Revise when a check fails

Yang et al., 2024 · SWE-bench Multimodal · browser and screenshot tools for SWE-agent ↗
56

### Page links

- [Link 1](../optional-readings/arxiv-2410-03859.md)

## Page 57

Browser agents and automation scripts

Browser agent
Model chooses each next action

Observe → choose action

Type / click in the browser

Adaptive exploration · next class

Playwright script
Model writes a repeatable check

1 Fill Name with spaces
fill()

2 Click Save contact
click()

3 Assert saved state
expect()

4 Capture an image
screenshot()

Programmed sequence + assertions

Screenshots → visual inspection or approved-baseline comparison

Koh et al., 2024 · VisualWebArena ↗
Playwright actions ↗
Assertions ↗
Screenshot comparisons ↗
57

### Page links

- [Link 1](../readings/arxiv-2401-13649.md)
- [Link 2](../optional-readings/ref-00b186b0142c.md)
- [Link 3](https://playwright.dev/docs/test-assertions)
- [Link 4](https://playwright.dev/docs/test-snapshots)

## Page 58

Verifying a frontend repair

Before: blank record saved
After: blank name rejected

Edit
value.length
→
value.trim().length

Behavior

0 records; valid names still save

Appearance

Error visible and readable beside Name

Runnable classroom example ↗
Playwright assertions ↗
Visual checks ↗
58

### Page links

- [Link 1](http://localhost:12445/examples/blank-name.html?mode=fixed)
- [Link 2](https://playwright.dev/docs/test-assertions)
- [Link 3](https://playwright.dev/docs/test-snapshots)

## Page 59

Evaluating visual issue resolution

Issue + image

Observed: blank name
Expected: reject it
Starting repository

Candidate patch

Change validation

Execution checks

Blank → error
No new record

Regression checks

Valid name → save
Existing tests pass

An image in the issue does not make image similarity the grading rule.

SWE-bench Multimodal · issue images and test-based patch evaluation ↗
59

### Page links

- [Link 1](../optional-readings/arxiv-2410-03859.md)

## Page 60

Broader software development

60

## Page 61

From requirements to maintenance

Requirements

User needs
Compatibility

Review

Diff + evidence
Release decision

Deploy / monitor

Production signals
Rollback path

Maintain

New requests
Observed failures

Implementation loop

Edit
Test

A test pass is one step,
not the release decision.

61

## Page 62

Where developers spend their time

15%

0%
10%
20%
30%

Share of reported workday

Meetings + email

Debugging / bug fixing

Running tests

Code review

Requirements + documentation

Helping + sync-ups + networking

Learning + admin + various

Breaks

25%

14%

8%

5%

6%

11%

8%

8%
Coding

Reading / writing

code and tests

Other activities: 85% combined

Meyer et al., 2019 · Table 2 · 5,928 self-reported Microsoft workdays ↗
62

### Page links

- [Link 1](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/04/devtime-preprint-TSE19.pdf)

## Page 63

Comparing software development tasks

Task
Artifact
Environment / verifier
Horizon

Repair
Patch
Repository / regression tests
One issue

Library
creation
Implementation
Scaffold / package tests
Many functions

Test generation
New test
Buggy + fixed versions /
discrimination
One behavior

CI repair
Code or configuration
Workflow / required checks
Build run

Evolution
Accumulated
changes

Persistent app / milestone +
regressions

Dependent
tasks

63

## Page 64

Task: localization

Search policy

Issue + repository
Inspect / search

Predicted file

django/…/datetime.py

Module: TruncDate

Function: as_sql

Reward

F1 at each
of 3 levels

Compare with locations in the gold patch; the patch is not policy input.

CodeScout, 2026 ↗
64

### Page links

- [Link 1](https://arxiv.org/abs/2603.17829)

## Page 65

Task: app creation and modification

Requirements

Product / feature
description

Zero-to-One

Build a new application
15 apps

Vibe-on-Ref

Extend a reference MVP
45 apps

Vibe-on-Vibe

Extend the agent’s earlier MVP
45 apps

Each result is checked using human-authored browser test plans.

ViBench · collection and evaluator definitions checked 2026-09-07 ↗
65

### Page links

- [Link 1](https://vibench.ai/)

## Page 66

Task: library implementation

Commit0
ProgramBench

Library scaffold

parse(…) → \[missing body\]
evaluate(…) → \[missing body\]
Documentation + tests

Implement together

Run integrated package tests

Reference executable

Probe inputs → observe outputs

New implementation

Match observable behavior
Check against the reference
Different internal designs can work

Commit0 ↗
ProgramBench ↗
66

### Page links

- [Link 1](../optional-readings/arxiv-2412-01769.md)
- [Link 2](../optional-readings/arxiv-2605-03546.md)

## Page 67

Task: software maintenance

SWE-Milestone, 2026 ↗
67

### Page links

- [Link 1](../optional-readings/arxiv-2603-13428.md)

## Page 68

Task: test generation

Mündler et al., 2024 · SWT-Bench ↗
68

### Page links

- [Link 1](../optional-readings/arxiv-2406-12952.md)

## Page 69

Task: CI repair

Observed build failure

Inspect the package’s supported runtime.

Causally relevant change

Rerun install, build, and tests.

Runtime: Node 16
Package requires: Node >=18
npm ci: EBADENGINE

# setup-node configuration
with:
  node-version: '20'

LCA CI Builds Repair · dataset revision ebf12dad ↗
69

### Page links

- [Link 1](https://huggingface.co/datasets/JetBrains-Research/lca-ci-builds-repair/blob/ebf12dad7a97c3c0cdc38705403d8bc8ddde47dc/README.md)

## Page 70

Learning skills for new tasks

Find relevant code

Search / dependencies

Implement functions

Specification → code

Write bug tests

Issue → executable check

Train policy

SFT or RL

Held-out tasks

New repositories

Repair an issue
Build a library
Detect a new bug
Equal inference budget

70

## Page 71

Generating projects for coding practice

Zhu, Gandhi & Neubig · SWE-Playground ↗
71

### Page links

- [Link 1](../optional-readings/arxiv-2512-12216.md)

## Page 72

Transferring training to new development tasks

Base 32B
Hybrid-Gym 32B

SWE-bench Verified
Repair

7

32.4

SWT-Bench Verified
Test generation

9.01

16.86

Commit0 Lite
Library building

8.34

13.45

0
10
20
30
40
Success (%)
Defined separately per task

Hybrid-Gym, 2026 · selected 32B results ↗
72

### Page links

- [Link 1](../optional-readings/arxiv-2602-16819.md)

## Page 73

Models that predict code

behavior

73

## Page 74

Choosing actions and predicting their effects

History h

Inspected code
Tool results

Policy π(a | h)

Choose: run test

Real environment

Execute the test
Observed: assertion fails

World model p(o | h, a)

Predict the test result
Prediction can be wrong
History also conditions the prediction

74

## Page 75

Predicting execution: shared references

Predict the next state

What are items and result?

True execution

Wrong prediction: treating alias as a copy.

items = \[1\]
alias = items
alias.append(2)
result = len(items)

items  = \[1, 2\]
alias  = \[1, 2\]
result = 2

75

## Page 76

When predictions help an agent

Two repairs

A: correct patch
B: wrong patch

Predict test outcomes

Model says A fails
Model says B passes
Illustrative mistake

Wrong decision

Choose B; discard A

Run both candidates to check the model’s judgment.

Compare task success AND total latency / tokens / tool calls.

76

## Page 77

Learning from program execution

FAIR CodeGen Team et al., 2025 · CWM ↗
77

### Page links

- [Link 1](https://arxiv.org/abs/2510.02387)

## Page 78

Building and using simulators

Dainese et al., 2024 · Code World Models / GIF-MCTS ↗
78

### Page links

- [Link 1](../optional-readings/arxiv-2405-15383.md)

## Page 79

Open questions about predicting code behavior

Better decisions? Measure prediction errors and task success on the same problems.

Lower cost? Include latency, tokens, and real environment calls.

New settings? Hold out programs, dependencies, and environments.

When to execute? Vary the fallback threshold and measure failures as well as

savings.

79

## Page 80

Conclusion

80

## Page 81

Designing a coding agent

Code models: pre-training, mid-training, and RL from execution rewards.

Agentic coding: localize, edit, and verify with the right tools.

Agent training: runnable tasks, repair rewards, and diverse harnesses.

Frontend development: browser interaction and visual verification.

Broader development: localization, apps, libraries, maintenance, tests, and CI.

Code-behavior prediction: learned models that support execution and planning.

81

## Page 82

Questions

Next Class: Domains 2 — GUI Agents

82
