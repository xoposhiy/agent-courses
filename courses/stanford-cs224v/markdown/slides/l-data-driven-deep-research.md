# Agentic Data-Driven Research

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-data-driven-deep-research.pdf) · [Raw file](../../raw/slides/l-data-driven-deep-research.pdf)

Retrieved: 2026-11-13T16:49:47.308206+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224v Course

Agentic AI

Lecture 7

Data-driven Deep Research

1

Shicheng Liu & Monica Lam

## Page 2

STANFORD
LAM

Lecture Goal

•
Open-ended data-driven research over databases

•
Build on the agentic approach from SPINACH and DataTalk

•
How to choose research questions, analyze results, and write a 
report?

•
Automatic reproduction and robustness checks for data-driven 
deep research

•
How to automatically conduct reproduction and robustness 
checks on existing studies?

## Page 3

STANFORD
LAM

Outline

•
DataSTORM: Data-driven deep research

•
Motivation and running example

•
The agentic approach

•
Evaluation

•
SEER-Repro: Automatic robustness checking

•
Reproduction and robustness

•
Results and expert review

## Page 4

STANFORD
LAM

The ACLED Database

Armed Conflict Location & Event Data · one row per recorded event

1.63M rows × 31 columns (2020–2025)

Schema (selected)

Time / place
event_date (date); country, admin1, admin2, location (text)
Event
event_type, sub_event_type (text)
Actors
actor1, actor2, assoc_actor_1, assoc_actor_2 (text)
Evidence
fatalities (integer); notes, source (text)

Example records from ACLED Database

event_date
country
admin1
event_type
actor1
fatalities

2023-02-01
Georgia
Imereti
Protests
Protesters (Georgia)
0

2023-02-01
Georgia
Tbilisi
Protests
Protesters (Georgia)
0

## Page 5

STANFORD
LAM

Answering a Question vs. Research

• Previous: the user supplies a specific question

• How did monthly battles in Colombia change between the pre-
policy and policy periods?

• But, many times users do not know what question to ask

• “Analyze Petro’s total peace policy in Colombia and its impact on 
violence versus armed groups.”

• The agent should autonomously choose what questions to ask and 
how to explore on behalf of the user

## Page 6

STANFORD
LAM
https://arxiv.org/abs/2604.06474

## Page 7

Knowledge Curation v. Data-driven Research

Source: Internet
Knowledge Curation
Source: Database
Data-driven research

OpenAI Deep

Research

Gemini Deep

Research

STORM /
Co-STORM
Perplexity

DR Tulu
WebThinker

InsightBench / TablePilot

Text-to-SQL agents

Few systems for end-to-end investigation

Quiz: Why might data-driven research be difficult?

Lecture 2

## Page 8

Why is deep research over databases hard?

Web sources often state findings. Database findings must be computed.

WEB
DATABASE

Retrieve + synthesize
written evidence

Query + analyze
to produce evidence

1
Which query
comes next?

Open-ended goals leave a
large space of possible
queries and hypotheses.

2
What is hidden
in the data?

Tables can exceed context;
useful patterns may be
absent from result previews.

3
Do the findings
fit together?

Filters and time windows
can drift; findings may lack
a coherent argument.

Only 23.3%

of claims attributed to the database

OpenAI DR (CSV) · ACLED benchmark

## Page 9

STANFORD
LAM

Running Example: Colombia

“Analyze Petro’s total peace policy in Colombia and its impact on 
violence versus armed groups.”

•
ACLED event data

•
Date, location, event type, actors, and fatalities

•
Web sources

•
Policy dates, definitions, and context

## Page 10

STANFORD
LAM

Exploratory Data Analysis

• P1: Iterative hypothesis generation and testing

• Ask → analyze → use the result to choose the next question.

• P2: Inductive discovery and deductive reasoning

• Deductive: top-down reasoning

• Inductive: bottom-up surfacing

• Statistics reveal patterns the agent did not anticipate.

• Those patterns suggest hypotheses to test with targeted queries.

John W. Tukey. Exploratory Data Analysis. 1977
Andy Kirk. Exploratory data analysis: Using visuals to see your data. 2016
Hadley Wickham and Garrett Grolemund. Exploratory Data Analysis. 2017

## Page 11

STANFORD
LAM

Data Storytelling

• P3: Converge toward a central thesis

• Connect findings into a central argument.

• Use it to guide exploration, then revise it with new evidence.

Edward Segel and Jeffrey Heer. Narrative visualization: Telling stories with data. 2010.
Brent Dykes. Effective Data Storytelling: How to Drive Change with Data, Narrative and Visuals. 2019.

## Page 12

STANFORD
LAM

DataSTORM in Three Stages

• 1. Get context from the web

• Learn the necessary background and useful starting questions.

• 2. Investigate the database

• Ask questions, compute answers, and decide what to examine 
next.

• 3. Write the report

• Organize the findings around a thesis and check the supporting 
evidence.

## Page 13

The DataSTORM Framework

## Page 14

STANFORD
LAM

What Happens in One Round?

• Planner: choose questions for the current round.

• Executors: return initial responses and the SQL used.

• Consistency module: compare the SQL definitions.

• Send corrective follow-ups to executors when needed.

• Executors: return corrected queries and final responses.

• Save useful insights in the insight bank.

• Use this shared evidence to plan the next round.

## Page 15

Planner–executor decomposition

P1
Iterative hypothesis generation and testing
Framework

Separate research planning
from query execution.

Planner

Task: generate queries

Executors

Decide how to answer the query

Explore data or web sources;
run queries and return answers.

Quiz: How should we implement the Executor?

## Page 16

STANFORD
LAM

Executor: SQL and a Result

The executor returns an answer grounded in an executed query.

Response component
Response

Result size
159 rows

Preview
111 rows omitted

SQL
WITH filtered AS ( ...

Summary
The table compares monthly counts in Colombia ...

Datatalk/SPINACH

## Page 17

Query consistency: align analytical definitions

P3
Convergence toward one coherent central narrative
Framework

Compare SQL from executor responses

Executor 1

country = 'Colombia' AND
event_type = 'Battles'

Executor 2

country = 'Colombia' AND
event_type = 'Battles' AND
sub_event_type = 'Armed clash'

Quiz: Would this lead to any problems?

## Page 18

STANFORD
LAM

Standardization Follow-up

• Start with the initial executor responses and their SQL.

• The consistency module identifies incompatible definitions.

• For this comparison: country, event type, periods and aggregation.

• Send standardization follow-ups to the relevant executors.

• Use the original question and SQL as context.

• Executors revise their queries and return follow-up responses.

• The resulting evidence can now be combined.

## Page 19

Summary statistics: surface unexpected patterns

P2
Interplay of inductive discovery and deductive reasoning
Framework

SQL result: 159 rows
Compute over all 159 rows

## Page 20

STANFORD
LAM

Statistics Reveal a Research Lead

Statistics for the returned monthly_count column

Distinct values
Minimum
Maximum
Median
Mean

57.86%
7
177
51
64.38

• The maximum, 177, is about 3.5 times the median, 51.

• High-count months may be missing from the preview.

• The statistics expose a lead that the planner can investigate.

Deductive follow-up

Next question

Which months account for
the unusually high counts?

## Page 21

STANFORD
LAM

Global Insight Bank

Evidence
From the monthly-battle comparison

Question
National counts before and during the policy period

SQL and scope
Executed query; country, event type and date windows

Returned result
A preview of returned result

Statistical lead
Maximum 177; median 51; mean 64.38

At each layer, consolidate global insight bank by retaining up to a fixed 
number of insights.

## Page 22

Thesis generation and refinement

P3
Convergence toward one coherent central narrative
Framework

Sharpen

Add specificity

Pivot

Change direction

Confirm

Retain the thesis

Generate

Form a candidate thesis
after initial exploration.

Refine

Revisit it every k layers
as new evidence accumulates.

## Page 23

STANFORD
LAM

From Findings to a Thesis

• Return to the research topic: the total peace policy.

• The monthly-battle comparison provides one line of evidence.

• Does violence differ consistently between the two periods?

• Or is the pattern shaped by a few high-count months?

• Build a central argument from the accumulated evidence.

• Refine it as further database and web findings arrive.

## Page 24

STANFORD
LAM

Thesis event example

Thesis Event
Thesis and added detail

Generate
Ceasefires without teeth,
violence with new faces

Sharpen
+ New geographies

Sharpen
+ Specified weapons and timing

## Page 25

STANFORD
LAM

Outline

•
DataSTORM: Data-driven deep research

•
Motivation and running example

•
The agentic approach

•
Evaluation

•
SEER-Repro: Automatic robustness checking

•
Reproduction and robustness

•
Results and expert review

## Page 26

STANFORD
LAM

InsightBench: Business Analytics Benchmark

## Page 27

STANFORD
LAM

InsightBench: Insight Recall

Suppose these are the references
Best match

Maximum 177 is more than 3 × median 51.
1.0

One single month accounted for more than half of all 
casualties
0.0

• If the report covers only the first: (1 + 0) / 2 = 50%

## Page 28

STANFORD
LAM

Results on InsightBench

100 tasks: a goal, a database, and reference insights

Recall (%)
Judge
AgentPoirot
DataSTORM

Insight
GPT-4o
47.1
61.9

Insight
Qwen3
49.9
69.3

Summary
GPT-4o
46.6
52.5

Summary
Qwen3
51.5
58.7

Both systems use GPT-5. Judges score matches to references.

## Page 29

STANFORD
LAM

Evaluation

Question
Metric

Does the report cover relevant findings?
Reference-criteria match

How good is the report overall compared to 
expert reports?
RACE rubric; human preference

Does it use database evidence?
Database claim attribution

Is the research angle useful?
Journalist originality ratings

## Page 30

STANFORD
LAM

ACLED: Criteria Match (Rubrics)

An LLM turns the reference expert article into a checklist, then grades the 
report on each item.

Criterion from the Colombia topic
Suppose the judge gives

Explain changes in state–group clashes
1.0 — covered well

Competition between armed groups
0.5 — partly covered

Geographic expansion of armed groups
0.0 — omitted

• Average match: (1 + 0.5 + 0) / 3 = 50%.

• Rubrics is a common form of eval metric today!

## Page 31

STANFORD
LAM

RACE: expert article weighted score

Dimension
What it asks in the Colombia report

Comprehensiveness
Does it cover both violence and armed-group 
expansion?

Depth
Does it explain how the two patterns fit together?

Instruction following
Does it stay within the requested topic and dates?

Readability
Can the reader follow the evidence and argument?

Relative score = 100 × report score / (report score + reference score)

If both weighted scores are 8: 100 × 8 / 16 = 50 (parity).

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A Comprehensive 
Benchmark for Deep Research Agents. arXiv:2506.11763.

### Page links

- [Link 1](https://arxiv.org/abs/2506.11763)

## Page 32

STANFORD
LAM

Building the ACLED Benchmark

Source: https://acleddata.com/report/total-peace-paradox-colombia-petros-policy-reduced-violence-armed-groups-grew-stronger

## Page 33

STANFORD
LAM

Building the ACLED Benchmark

•
Start with 20 expert-written analyses

•
Convert each into a neutral research topic

•
Give systems database and web access

•
Keep the reference articles out of search results

•
Restrict web evidence to the reference publication date

•
Evaluate the resulting report against the reference

Quiz: Why could using the article title reveal too much?

## Page 34

STANFORD
LAM

Results on ACLED

20 topics · GPT-5 judge

System
Criteria match (%)
RACE
DB use (%)

OpenAI DR (MCP)
48.5
46.1
30.4

OpenAI DR (CSV)
51.2
46.8
23.3

DataSTORM
61.8
52.6
66.4

MCP: database tools; CSV: file access

## Page 35

Human Evaluation

10 journalists · 20 topics × 2 raters · system identities hidden during annotation

Pairwise preference (% of comparisons)

DataSTORM
OpenAI DR
Expert-written

DataSTORM vs OpenAI DR (CSV)

57.5%
42.5%

DataSTORM vs expert-written reports

47.5%
52.5%

OpenAI DR (CSV) vs expert-written reports

30.0%
70.0%

Originality

Mean rating · 1–5 scale

2.21  →  3.05

OpenAI DR       DataSTORM

p < 0.05 · N = 39

## Page 36

STANFORD
LAM

Ablations: What Do the Components Contribute?

Removed component
Metric
Without
Full

Summary statistics
Criteria match
56.9%
62.3%

Thesis generation
Criteria match
48.8%
62.3%

Consistency checks
Consistency score
0.406
0.549

10 ACLED topics · GPT-5 judge

## Page 37

STANFORD
LAM

Outline

•
DataSTORM: Data-driven deep research

•
Motivation and running example

•
The agentic approach

•
Evaluation

•
SEER-Repro: Automatic robustness checking

•
Reproduction and robustness

•
Results and expert review

## Page 38

Trustworthy discovery needs two checks

Reproducibility

Can we recover the
published result?

Reconstruct the original analysis
from the paper, data, and manuals.

Analytical robustness

Does the conclusion survive
reasonable alternatives?

Vary cohort definitions, endpoints,
or statistical choices.

Before LLMs can be trusted to produce new scientific results,

They must first be able to reproduce existing studies

## Page 39

https://arxiv.org/abs/2610.23845

## Page 40

SEER: The backbone of U.S. cancer research

The NCI’s Surveillance, Epidemiology, and End Results program has tracked
cancer incidence and outcomes since 1973.

1973 → today

50+ years of population-based
cancer surveillance

126K+

publications
reference SEER

≈25K studies

used SEER data
in primary analysis

What SEER captures

Demographics
Age, sex, race/ethnicity,
geography
Tumor
Site, morphology,
stage at diagnosis
Outcomes
Survival and vital status

39 tables · 800 pages of manuals

Why SEER fits this project

High-impact literature
Thousands of cancer-research questions
and documented analytical choices.

Computationally intensive
Large databases and complex
scientific analysis workflows.

OUR USE
A testbed for reproducing studies and assessing robustness.

Source: NCI SEER Program overview and Annual Usage Metrics (2024).

## Page 41

STANFORD
LAM

Findings and Atomic Claims

Illustrative finding:

“For cohort C over years Y, the crude rate rose from 4.0 to 5.0
per 100,000—a 25% increase.”

•
Starting rate: 4.0 per 100,000

•
Ending rate: 5.0 per 100,000

•
Relative increase: 25%

## Page 42

SEER-Repro makes published studies executable

A medical epidemiology testbed built from SEER cancer-registry studies.

20

published papers

901

empirical findings

2,190

atomic claims

Execution environment

39 tables · 198.3M total rows
40 documentation resources

Curated with domain experts

Historical data + population tables
Registry mappings + coding manuals

## Page 43

STANFORD
LAM

Reproduction Approach

•
Extract empirical findings from the paper

•
Reproduce each finding with a coding agent

•
Use the paper, data, and manuals

•
Save the analysis code and execution results

•
Split findings into atomic claims and grade them

•
Check method compatibility and evidence provenance

•
Reproduced / Close / Not reproduced

## Page 44

STANFORD
LAM

Grading a Reproduction

First check evidence provenance and method compatibility.

Relative error = |computed − reported| / |reported|

Reported
Computed
Error
Default verdict

5.0
4.8
4%
Reproduced

5.0
4.6
8%
Close

5.0
4.4
12%
Not reproduced

<= 5% Reproduced

5%-10% Close-to-reproduced

> 10% Not reproduced

## Page 45

77.4% of atomic claims reproduced

## Page 46

STANFORD
LAM

Error Analysis

420 non-reproduced claims

Cause
Claims
%

Data issues
251
59.8

Agent errors
48
11.4

Underspecified analysis
47
11.2

Unavailable software
28
6.7

Unresolved cause
26
6.2

Suspected evaluation errors
20
4.8

Quiz: What does this suggest about the challenges around reproduction?

## Page 47

STANFORD
LAM

A Reproduced Result

Suppose a study reports: “Cancer incidence doubled among 
younger adults.”

Rate per 100,000
Earlier
Later

Reported and reproduced
20
40

• The reproduction matches the reported numbers.

• But how was “younger adults” defined?

## Page 48

STANFORD
LAM

Two Definitions of “Younger Adults”

The upper age limit determines which records enter the analysis.

Definition
Included ages

Definition 1
20–49: people in their 20s, 30s and 40s

Definition 2
20–39: people in their 20s and 30s

The reported result used Definition 1.

## Page 49

STANFORD
LAM

Quiz 1: Is This Important?

• Would the age cutoff matter to how you interpret 
“incidence doubled”?

• What might a reader infer about adults in their 20s and 
30s?

• Would reproducing the original numbers settle that 
question?

## Page 50

STANFORD
LAM

Quiz 2: How Do We Test It?

• How would you test whether the conclusion depends on 
the age cutoff?

• What would you change?

• What would you hold fixed?

• Which outputs would you compare?

## Page 51

STANFORD
LAM

Change One Definition and Rerun

• Validate the baseline: ages 20–49 gives 20 → 40.

• Change only the upper age cutoff: 49 → 39.

• Use the matching population denominator for ages 20–39.

• Keep the rest of the analysis fixed.

• Cancer definition, periods, registries and rate calculation.

• Compare the rates, relative change and interpretation.

## Page 52

STANFORD
LAM

The Increase Is in Ages 40–49

Each age band has 100,000 people in each period. Rates are per 100,000.

Population
Earlier rate
Later rate

Ages 20–39
20
20

Ages 40–49
20
60

Definition 1: ages 20–49
20
40

Definition 2: ages 20–39
20
20

Definition 1: +100%.     Definition 2: no increase.

## Page 53

STANFORD
LAM

How SEER-Repro Tests Alternatives

## Page 54

55 of 579 findings flagged for expert review

9.5%

55 / 579 findings
flagged by
≥1 analyst

2.4%

14 / 579 findings
flagged by
≥2 analysts

Do different analysts
complement each other?
74.5%

41 of 55 affected findings
identified by only one analyst

Suggests largely complementary
sets of potentially consequential
analytical choices.

## Page 55

STANFORD
LAM

Expert Review

One expert reviewed 10 selected high-score cases.

Assessment
Cases

Alternatives likely less defensible
2

Limited qualifications
7

Further review needed
1
