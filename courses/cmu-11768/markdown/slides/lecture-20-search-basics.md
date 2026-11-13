# Lecture 20 slides

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/slides/lecture-20-search-basics.pdf) · [Raw file](../../raw/slides/lecture-20-search-basics.pdf)

Retrieved: 2026-11-13T16:45:34.400556+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Search over Trajectories

Lecture 20 · November 12, 2026

Daniel Fried

11-768: AI Agents

1

## Page 2

Repeated sampling

Generate independent trajectories in parallel from the same starting page.

Same start

Run 1

…
Stop

Fail
Run 2

…
Stop

Pass
Run 3

…
Stop

Fail

Page thumbnails: Fried · VWA search talk (2024) · parallel sampling illustration ↗
2

### Page links

- [Link 1](../optional-readings/arxiv-2407-01476.md)

## Page 3

Sampling methods

Sample the next token from the model’s distribution

Randomness affects reasoning and tool actions

Reasoning models may fix the temperature at 1.0

P
​(x
​ ∣
T
t
x
​) =
<t
softmax(z
​/T)
t

Model-specific sampling settings · Claude docs ↗
DeepSeek-R1 usage recommendations ↗
3

### Page links

- [Link 1](../optional-readings/ref-afad87e802e5.md)
- [Link 2](../optional-readings/ref-5ee636ca2d80.md)

## Page 4

Parallel attempts

Each attempt starts from the same task and samples independently.

Breadth
Round 0

A0

B0

Same task, fresh environment

Each attempt samples a new trajectory

Are independent -> can often be generated in a single batch

Each trajectory can produce an output, e.g. a patch

4

## Page 5

Coverage and pass@k

Pass@k: at least one of k attempts succeeds.
How likely is a success?
Assuming probability of success p:

P(all k fail) = (1 −p)k

P(at least one succeeds) = 1 −(1 −p)k

5

## Page 6

Idealized coverage

Pass@k as a function of p and k:

25.0%
Correct answer, p

pass@k is the success

rate you would get with

an oracle which can

perfectly distinguish

correct/incorrect

candidates

0%

25%

50%

75%

100%

1
10
100
1,000
10,000

Attempts, k (log scale)

Pass rate

pass@k

At k = 1: 25.0%

Independent attempts at one problem, with a fixed success probability p.

6

## Page 7

Improving coverage

Sample more candidates!

Increase the sampling temperature (less applicable for reasoning models)

\[Codex\]

Generate multiple responses in a single pass (less applicable for agents)

\[Verbalized Sampling\]

Use a diverse set of prompts

\[Mode-conditioning\]

Incentivize diversity / optimize for pass@k in training

\[Rewarding the Unlikely; Differential Smoothing; MaxRL\]

Chen et al. (2021) ↗
Wu et al. (2025) ↗
Zhang et al. (2025/2026) ↗
He et al. (2025) ↗
Gai et al. (2026) ↗
Tajwar et al. (2026) ↗
7

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374v2.md)
- [Link 2](../optional-readings/arxiv-2506-02355v2.md)
- [Link 3](../optional-readings/arxiv-2510-01171v4.md)
- [Link 4](../optional-readings/arxiv-2512-01127v1.md)
- [Link 5](../optional-readings/ref-49b28253cab3-pdf.md)
- [Link 6](../optional-readings/ref-245b19b46cbb-pdf.md)

## Page 8

But choosing a candidate can be hard

Codex · HumanEval

A correct answer may be present

Large Language Monkeys · MATH

Coverage
Output vote
Best-of-N
Score + vote

Practical selection can still miss it

Chen et al. · Codex (2021), Figure 7 ↗
Brown et al. · Large Language Monkeys (2024), Figure 7 ↗
8

### Page links

- [Link 1](../optional-readings/arxiv-2107-03374v2.md)
- [Link 2](https://arxiv.org/abs/2407.21787)

## Page 9

Selecting an answer

9

## Page 10

Verification signals

Ground-truth checks

For math: a proof checker

For code: passes reference test
cases

Predicted correctness

For code: passes predicted test
cases

Use a reward model (e.g. LLM-as-
a-judge)

Similarity to other sampled
outputs

Madaan et al. · Self-Refine (2023), §2 ↗
10

### Page links

- [Link 1](../optional-readings/arxiv-2303-17651v2.md)

## Page 11

Use a reward model

SWE-Gym trains an outcome
verifier on complete OpenHands
runs.

Use task tests to label each
training run

Balance YES / NO examples;
fine-tune on complete runs

Score new runs by YES
probability; return the highest

Pan et al. · SWE-Gym (2024/2025), §5.1.1 & Appendix B.6 · training schematic; Figure 1 (bottom) ↗
11

### Page links

- [Link 1](../optional-readings/arxiv-2412-21139v2.md)

## Page 12

Best-of-N

Candidate A

Candidate B

Candidate C

→

Score: 0.3

Score: 0.8

Score: 0.5

→
Return B

Score each candidate with a reward model

Return the candidate with the highest score

12

## Page 13

Self-consistency

Different reasoning paths can lead to the same final answer.

Minimum Bayes risk with 0–1 answer loss

Sum over trajectories z to get answer probabilities; approximate with sample votes.

Reasoning A

42

Reasoning B

17

Reasoning C

42

​ =
a^MBR
arg

​
​ ≈
a
max

p(a∣x)

​
​p(z, a ∣x)

z
∑
arg

​1{a
=
a
max

i=1
∑

N

(i)
a}

Wang et al. · Self-Consistency (2022/2023) ↗
Welleck et al. · From Decoding to Meta-Generation (2024), §4.2.2 ↗
13

### Page links

- [Link 1](../optional-readings/arxiv-2203-11171.md)
- [Link 2](../optional-readings/arxiv-2406-16838v2.md)

## Page 14

Consensus over execution results

Task: sum the even numbers up to and including n = 12 .

Candidate A

evens = range(2, n + 1, 2)

return sum(evens)

↓ Execute

Candidate B

evens = range(2, n, 2)

return sum(evens)

↓ Execute

Candidate C

m = n // 2

return m * (m + 1)

↓ Execute

Execute programs and group by their outputs.

42
30
42

Shi et al. · MBR-Exec (2022) ↗
Li et al. · AlphaCode (2022) ↗
14

### Page links

- [Link 1](../optional-readings/ref-81298debf83f.md)
- [Link 2](../optional-readings/arxiv-2203-07814.md)

## Page 15

Imperfect verification

Verifier / reward model errors limit the gains from repeated sampling.

25.0%
Correct answer, p

0%
0%

50%

50%

100%

100%

Accept correct, q

Accept wrong, r

q (%) 95
r (%) 10

Perfect
No signal
Imperfect

0%

25%

50%

75%

100%

1
10
100
1,000
10,000

Attempts, k (log scale)

Pass rate

Oracle coverage
Verifier-selected

At k = 1: 25.0% · Limit as k grows: 76.0%

Return the first accepted answer; otherwise return the last response.

15

## Page 16

Iterative refinement

16

## Page 17

Refinement

Refinement uses feedback to revise candidate solutions. Must be done sequentially, but
can refine multiple candidates in parallel

Breadth
Round 0

A0

B0

Round 1

A1

B1

Round 2

A2

B2

Prior work + feedback

17

## Page 18

Remembering feedback on trajectories

attempt
→
evaluator: compute

or predict reward
→
reflection:
generate feedback
→
retry the same task

ATTEMPT 1

“What was a series of battles … fought on October 28, 1776 near White Plains, New York?”

Finish\[Battle of White Plains\] incorrect

GENERATED FEEDBACK

“… the question asked for a series of battles, but I only provided the name of one battle … I will
make sure to provide more context, such as the name of the campaign …”

ATTEMPT 2

Finish\[The New York and New Jersey campaign\] correct

Reflexion · Shinn et al., NeurIPS 2023 ↗
18

### Page links

- [Link 1](../optional-readings/arxiv-2303-11366.md)

## Page 19

Types of feedback

Basically parallel the verification signals we saw earlier:

Ground-truth checks

For math: proof-checker errors

For code: reference test results

\[Self-Debugging\]

Predicted correctness

For code: predicted test results

\[Reflexion\]

Use a reward model (e.g. LLM-as-
a-judge)

Can be the agent itself \[Self-Refine\]

Similarity to other candidates
\[PDR\]

Chen et al. · Self-Debugging (2023), §3 ↗
Shinn et al. · Reflexion (2023), §4.3 ↗
Madaan et al. · Self-Refine (2023), §2 ↗
19

### Page links

- [Link 1](../optional-readings/arxiv-2303-11366.md)
- [Link 2](../optional-readings/arxiv-2303-17651v2.md)
- [Link 3](../optional-readings/arxiv-2304-05128v2.md)
- [Link 4](../readings/arxiv-2510-01123v1.md)

## Page 20

Limits of refinement

Without oracle correctness labels:

Some incorrect answers
become correct

Some correct answers
become incorrect

Self-critique can preserve the
original blind spot

Huang et al. · Intrinsic self-correction study (2023/2024), Figure 1 ↗
20

### Page links

- [Link 1](../optional-readings/arxiv-2310-01798.md)

## Page 21

Combining exploration and refinement

Parallel-Distill-Refine: generate a summary of multiple candidates ("distill"); condition
on this summary in later attempts.

Breadth
Round 0

A0

B0

Round 1

A1

B1

Round 2

A2

B2

Prior work + feedback

Sharing across attempts: bounded workspace

Madaan et al. · PDR (2025), Figure 2 · shared-summary variant ↗
Related: Recursive Self-Aggregation ↗
21

### Page links

- [Link 1](../optional-readings/arxiv-2509-26626v2.md)
- [Link 2](../readings/arxiv-2510-01123v1.md)

## Page 22

Putting it together for agents

22

## Page 23

Summarization

Agents trajectories are long. Use an LLM to generate a structured summary of each
trajectory:

"key_discoveries": \[

"Add(ZeroMatrix, ZeroMatrix) evaluates to scalar 0",
"MatAdd(0, ZeroMatrix, ZeroMatrix) canonicalizes to 0 because rm_id removes all
identities and keeps the first one (0)"
\]

"solution_approach": {

"strategy": "Modify \`get_postprocessor\` in \`sympy/matrices/expressions/matexpr.py\`
to check if \`nonmatrices\` is empty. \[…\]"
}

Kim et al. · Agentic Coding (2026), Appendix G, Figure 23 (excerpts) ↗
23

### Page links

- [Link 1](../readings/arxiv-2604-16529v1.md)

## Page 24

Recursive selection

Recursive Tournament Voting compares rollout summaries in small groups.

Have an LLM-as-a-judge select from multiple summaries

The judge may be noisy; aggregate multiple decisions

Advance the winning summary / rollout; repeat until one rollout remains

Kim et al. · Agentic Coding (2026), §2.3 & Figure 2 ↗
24

### Page links

- [Link 1](../readings/arxiv-2604-16529v1.md)

## Page 25

Selection and reuse

As in PDR, have rollouts condition on selected summaries. Also use selection at the end.

100 SWE-bench tasks; mean rollout success before final selection.

Multiple summaries help; using RTV to select them helps further in this ablation.

Kim et al. · Agentic Coding (2026), Figure 3 & Table 1 ↗
25

### Page links

- [Link 1](../readings/arxiv-2604-16529v1.md)

## Page 26

Harness optimization

26

## Page 27

Agent harnesses

Recall: a harness is the code that controls how we use a model.

Part of a harness for text classification via few shot examples.

Editable
harness code

Fixed model
weights

examples_section = self._format_examples_section(seed=seed)

prompt = PROMPT_TEMPLATE.format(

examples_section=examples_section,

input=input,

)

response = self.call_llm(prompt)

answer = extract_json_field(response, "final_answer")

Lee et al. · Meta-Harness (2026), §3 · released text-classification baseline ↗
27

### Page links

- [Link 1](../readings/arxiv-2603-28052v1.md)

## Page 28

Harness search

Given fixed model weights, optimize the harness around it to maximize task reward.

Store all past experiences in a file system. Use a coding agent to edit the harness.

Proposer agent: reads prior code, scores, and traces; edits the harness.

Task evaluation: run the current harness with the fixed LLM weights; store logs and code.

Lee et al. · Meta-Harness (2026), Figure 2 ↗
28

### Page links

- [Link 1](../readings/arxiv-2603-28052v1.md)

## Page 29

Joint weight and harness optimization

WHALE: joint model training and harness search via alternating optimization

Kim et al. · WHALE (2026), Figure 1(a–b), §§3–4 ↗
29

### Page links

- [Link 1](../optional-readings/arxiv-2609-00196v1.md)

## Page 30

Where would you spend more compute?

Breadth
Round 0

A0

B0

Round 1

A1

B1

Round 2

A2

B2

Prior work + feedback

Sharing across attempts: prior experience

Check / select

Final answer

If pass@k scores are low: increase breadth or feedback conditioning

If final accuracy is much lower than pass@k: improve the selector

30

## Page 31

Thank you, Questions?

Next class: Advanced search

31
