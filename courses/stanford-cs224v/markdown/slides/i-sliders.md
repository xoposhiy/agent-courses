# Long-Context Long-Horizon Deep Researcher

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/I-sliders.pdf) · [Raw file](../../raw/slides/i-sliders.pdf)

Retrieved: 2026-11-13T16:49:47.666582+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224v Course

Agentic AI

Lecture 10

Systematic Review of Long Document Sets

SLIDERS: Evidence Synthesis with Autonomous
Database Reconciliation for Systematic Reviews

1

Harshit Joshi     Monica Lam

## Page 2

STANFORD
LAM

2

Lecture Goal

•
What are systematic reviews and why are they hard?

•
Failures of LLMs, and chunking methods

•
SLIDERS

•
Key concept: Reconciliation

•
Building autonomous database reconciliation agent

•
The lack of benchmarks and what it takes for testing SOTA 
methods

## Page 3

STANFORD
LAM

3

Systematic Reviews

•
Cornerstone of evidence-based research across medicine, social 
sciences, policy analysis, finance, law, and other technical domains

## Page 4

STANFORD
LAM

4

Usual systematic review process

Question

Select relevant

Documents

Extract evidence

from documents

Reconcile

evidence

A transparent
report

Takes 67.3 weeks to complete one review

(from the web, journals,

private documents)

## Page 5

STANFORD
LAM

5

Usual systematic review process

Question

Select relevant

Documents

Extract evidence

from documents

Reconcile

evidence

A transparent
report

Number of documents ranges from 20 to 72 
documents per review!

(from the web, journals,

private documents)

## Page 6

STANFORD
LAM

6

Types of questions over document set

Document Set
Question
Type

Collect of Restaurant 
Reviews

What are some good restaurants in Palo Alto?
Simple 
Lookup

Financial Document
How many AI companies have positive net profit? Count all

evidences

Clinical Documents
What patient and disease factors should be used 
to select patients with stage I–III hormone 
receptor-positive for neoadjuvant therapy?

Compare 
all 
evidences

Historical Documents
Which communities were flourishing under 
Chandragupta Murya empire and what led to 
their demise?

Tracing a 
story with 
ordering

## Page 7

STANFORD
LAM

7

Why is systematic review difficult?

Long Context
Large set of long documents

Retrieve All 
Instances

Need to find every relevant information – high recall

Reconcile
Compare all the evidences

Transparent 
Reporting

Require context about every evidence to make a 
coherent story

## Page 8

STANFORD
LAM

8

Systematic reviews for oncology

1. Identify eligible documents

2. Extract characteristics of clinical studies

3. Extract or compute significance

4. Perform literature review based on underlying documents.

5. Curate the final set of guidelines

Sheldon

SLIDERS

SLIDERS

SLIDERS

SLIDERS

## Page 9

STANFORD
LAM

9

Why is systematic review difficult?

Long Context
65 documents

Retrieve All 
Instances

A single document contains several evidences.
Example: need to get underlying number to compute significance

Reconcile
Need to check for which value to keep. 
Example total patients admitted vs total patients in actual trial
Transparent 
Reporting

Build the report based on additional context, talk 
about caveats and contextualize the information

What patient and disease factors should be used to select patients 
with stage I-III hormone receptor-positive, HER2-negative breast 
cancer to whom neoadjuvant therapy should be offered?

## Page 10

STANFORD
LAM

10

Outline

•
Can LLMs perform systematic reviews?

•
High-level approaches: Training vs. Chunking

•
Introduction to SLIDERS

•
Design

•
Evaluation

## Page 11

STANFORD
LAM

11

LLMs Long-Context Capability

•
Ever increasing context window of LLMs

•
Near perfect needle in a haystack capabilities

## Page 12

STANFORD
LAM

12

LLMs Lack Precision for Long Contexts

•
Context length increases → performance for the same task decreases

•
Attention is not uniform across the entire context window.

“Lost in the middle” Liu et. al 2023
“Loong Benchmark” Wang et. al 2024

## Page 13

STANFORD
LAM

13

What is the accounts payable of BIOLARGO, INC.?

BIOLARGO,

INC

Agape ATP

Corp

Ameritek Ventures,

Inc.

1847 Holdings LLC

BATTALION OIL

CORP

AppTech Payments

Corp.
GPT 4.1: 
The accounts payable of BIOLARGO, INC. as of March 31, 2024, is $1,740,000.

Line 271: accounts payable and accrued expenses
Line 1735: accounts payable, 
                  separate from accrued expenses (line 1737)

Correct 
Answer

GPT 4.1 
Answer

Examples of Imprecision

## Page 14

STANFORD
LAM

14

We hope you will carefully study the provided papers and determine 
the citation relationships between them.

1. Reference: references are about what the given paper is using.

2. Citation: citations are about who is using the given paper.

The paper you need to analyze: 
Risk Taxonomy, Mitigation, and Assessment Benchmarks of Large Language Model Systems

{
'Reference’: \['# Evil Geniuses: Delving into the Safety of LLM-based Agents ‘,
                        '# Towards Optimal Statistical Watermarking ‘\],
 'Citation’:

\['# Unbridled Icarus: A Survey of the Potential Perils of Image Inputs in Multimodal Large Language Model Security ‘\]
}

{
"Reference": \[\], 
 'Citation’:

\['# Unbridled Icarus: A Survey of the Potential Perils of Image Inputs in Multimodal Large Language Model Security ‘\]
}

Gold Answer
GPT

Given 4 academic papers

Misses several references

Examples of Imprecision

## Page 15

STANFORD
LAM

15

Contexts are never long enough

•
Is 1 million tokens enough?

•
A pubmed article is around 100k tokens.

•
Can fit around 10 pubmed papers can fit in

•
A financial document (10-Q) is around 300k tokens.

•
Can fit around 3 financial document

•
A book 300 page book is about 2M tokens

•
Cannot even fit a single book in context!

## Page 16

STANFORD
LAM

16

Outline

•
Can LLMs perform systematic reviews?

•
High-level approaches: Training vs. Chunking

•
Introduction to SLIDERS

•
Design

•
Evaluation

## Page 17

STANFORD
LAM

17

Approaches

•
Training based: to improve precision

•
Chunking based: to improve precision and scaling

•
Representations for chunks

•
Natural language

•
Structured representation

•
Coding Agents

## Page 18

TRAINING BASED

## Page 19

STANFORD
LAM

19

## Page 20

STANFORD
LAM

20

Training-Based Methods

QwenLong-L1:

•
Curate a long-context dataset using existing benchmarks,

•
Progressively increase the context size with RL 
using rule-based verification and LLM-as-a-judge

•
Improve over baseline models, 
but not SOTA with proprietary/open-source models

Cartridges

•
Train KV cache on a document set by generating & answering questions

•
Reuse cache to answer new questions across the trained document set

•
Lose to complete in-context documents

“QWENLONG-L1: Towards Long-Context Large Reasoning Models with Reinforcement Learning” Wan et. al 2025
“Cartridges: Lightweight and general-purpose long context representations via self-study”, Eyuboglu et. al 2025

## Page 21

STANFORD
LAM

21

Is training all we need?

What training can improve?

•
Use of information within a 
model’s context

•
Long context reasoning on 
trained tasks

What does not guarantee?

•
Coverage of a collection 
large than the context 
window

•
Exact enumeration and 
consistent outputs across 
inferences

•
Interface for interpretability

Training is complementary -- not by itself a solution for

exhaustive evidence synthesis.

## Page 22

STANFORD
LAM

22

Which problems can training solve?

Long Context
Training already fails here

Retrieve All 
Instances

Reconcile

Transparent 
Reporting

## Page 23

CHUNKING-BASED

## Page 24

STANFORD
LAM

24

RAG Methods

## Page 25

STANFORD
LAM

25

RAG Methods

•
Technical data is usually spread across different paragraph 
and documents

## Page 26

STANFORD
LAM

26

RAG Methods

•
Technical data is usually spread across different paragraphs 
and documents

•
Need to collect all the evidence 
-- not just a small set of semantically relevant chunks

•
Increase the number of passages to retrieve again 
leads to yet another long-context problem.

## Page 27

STANFORD
LAM

27

Which problems can RAG solve?

Long Context
RAG can cover all documents

Retrieve All 
Instances

Fails miserably

Reconcile

Transparent 
Reporting

## Page 28

STANFORD
LAM

28

Coding Agents

•
Increasingly people are using coding agents for document 
QA

•
Agents with access to files execute shell commands to 
retrieve passages and generate answer

•
Usually use grep/keyword search to find relevant passages

Can using grep or keyword search cover all the cases?

## Page 29

STANFORD
LAM

29

Chunking-based Methods

## Page 30

STANFORD
LAM

30

Chunk 1

Chunking-Based Methods

•
Divide the context into multiple chunks.

•
Answer question based on individual chunk

•
Combine them together and get the final answer

Chunk 2

Chunk n

Single step approach
Decomposing the problem

Long 
Document
…

Processed by LLM

Processed by LLM

Processed by LLM

LLM 
generates 
answer
Long 
Document

LLM 
generates 
answer

## Page 31

STANFORD
LAM

31

Chunking-Based Methods

•
Chain of Agents:

•
An LLM processes a chunk and passes on summary w.r.t. 
the task to the next LLM call along with the next chunk.

•
Final agent synthesizes the answer based on last provided summary.

•
DocETL:

•
User provides a schema for the representation

•
Each chunk is processed by an LLM that outputs structured data.

•
The user prompts the LLM to reduce/resolve the output 
from each chunk to answer the question.

“Chain of Agents: Large Language Models Collaborating on Long-Context Tasks” Zhang et. al 2024
“DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing” Shankar et. al 2024

## Page 32

STANFORD
LAM

32

Advantages of Chunking-Based Methods

•
Precision: 
Processing each chunk individually increases attention to local details

•
Scalability: Enables natural scalability to large document collections 
                    far beyond model limits

Chunk 1

Chunk 2

Chunk n

Decomposing the problem

Long 
Document
…

Processed by LLM

Processed by LLM

Processed by LLM

LLM 
generates 
answer

## Page 33

STANFORD
LAM

33

Disadvantages of Chunking

•
Loss of context around each chunk

•
Inconsistency in independent extractions

•
Extracted evidence might be very “dirty”

•
Collected evidence might still exceed context length of LLMs

## Page 34

STANFORD
LAM

34

Independently extracted information is “dirty”

•
Extract similar information

•
Different extractions might have 
complimentary information

•
Contains conflicting information with 
different context

Results in overcounting

Leads to missing information

Contradictory information 
and cannot form answer

## Page 35

STANFORD
LAM

35
Chunking solves input length,
not answer synthesis

Process many

short chunks 
independently

Generate many

chunk-level

answers

A final LLM must 
compile thousands

of outputs

Bottleneck

When synthesis is just “put everything in one more prompt,” 
the long-context problem returns.

## Page 36

STANFORD
LAM

36

Is chunking all we need?

What chunking buys?

•
Precision

•
Scalability

Where chunking can fail?

•
Inconsistent extraction

•
Loss of context

•
Dirty evidence collection

•
Might still exceed the context

## Page 37

STANFORD
LAM

37

Which problems can chunking solve?

Long Context
Chunking methods work

Retrieve All 
Instances

Chunking methods can work

Reconcile
Loses context across chunks and fails

Transparent 
Reporting

Loses context across chunks and fails

## Page 38

STANFORD
LAM

38

For large document sets

Question
Type
Long 
context LLM

RAG
Chunking 
Methods

What are some good restaurants in 
Palo Alto?

Simple Lookup

How many AI companies have 
positive net profit?

Count all 
evidences

What patient and disease factors 
should be used to select patients with 
stage I–III hormone receptor-positive 
for neoadjuvant therapy?

Compare all 
evidences

Which communities were flourishing 
under Chandragupta Murya empire 
and what lead to their demise?

Tracing a story 
with ordering

## Page 39

STANFORD
LAM

39

Challenges of Chunking

1. How do we represent the information in each chunk?

2. Problem answering separated into two steps

a. Correct extraction of information chunk by chunk?

•
Extraction Inconsistencies: might have different scale, units, etc
 
•
Loss of Context: interpretation might be different

b. Compile correct answer from the set of extracted information

•
Extracted information is “dirty”
 
•
How to automatically find issues and fix them autonomously?

## Page 40

STANFORD
LAM

40

Our Solution: Chunk and Reconcile

1. How do we represent the information in each chunk?

As rows in tables, database can scale
2. Problem answering separated into two steps

a. Correct extraction of information chunk by chunk?

•
Extraction Inconsistencies: might have different scale, units, etc
 Automatically-induced schema with extraction rules
•
Loss of Context: interpretation might be different
Contextualized information extraction
b. Compile correct answer from the set of extracted information

•
Extracted information is “dirty”
We discovered: duplications, incomplete information…
•
How to automatically find issues and fix them autonomously?
Autonomous database reconciliation coding agent

## Page 41

STANFORD
LAM

41

Which problems can chunking-reconcile solve?

Long Context
Chunking methods work

Retrieve All 
Instances

Chunking methods can work

Reconcile
Need explicit reconciliation

Transparent 
Reporting

Need to preserve all the context

## Page 42

STANFORD
LAM

42

Kinds of Questions

Question
Type
LLM
RAG
Chunking 
Methods

Chunk-
Reconcile

What are some good restaurants in 
Palo Alto?

Simple 
Lookup

How many AI companies have 
positive net profit?

Count all 
evidences

What patient and disease factors 
should be used to select patients with 
stage I–III hormone receptor-positive 
for neoadjuvant therapy?

Compare 
all 
evidences

Which communities were flourishing 
under Chandragupta Murya empire 
and what lead to their demise?

Tracing a 
story with 
ordering

SLIDERS

## Page 43

STANFORD
LAM

43

To be presented at NeurIPS 2026, Sydney, Australia

## Page 44

STANFORD
LAM

44

Outline

•
Can LLMs perform systematic reviews?

•
High-level approaches: Training vs. Chunking

•
Introduction to SLIDERS

•
Design

•
Evaluation

## Page 45

STANFORD
LAM

45

SLIDERS design

•
Database: Use database for storing evidences

•
Schematization: Automatically determines the database schema

•
Chunking and Extraction: Extracts information chunk by chunk 
with provenance

•
Reconciliation: Chunk-based extraction requires reconciliation

•
Autonomous database reconciliation coding agent: Uses 
provenance and rationale

•
Coding agent: To answer from reconciled tables

## Page 46

STANFORD
LAM

46
Divide and Conquer

text

Sets of Long

Documents

answer

answer

answer

Final answer
(Reduction
 operation)

Chunk 1

Chunk 2

Chunk n

…

Question

Sets of Long

Documents Semantic

Chunking +
Contextualized

Extraction

Schema

Question

+

Schematization

Row 1

Row 2

Row m

…

reconciled

table

Row 1

Row 2

Row n

…

raw table

Autonomous
Reconciliation
Coding Agent

SQL programs
Coding Agent

Final 
Answer
DB
Execution

SLIDERS

-
Inconsistent extraction
-
Loss of context
-
Dirty evidence collection
-
Might still exceed the context

## Page 47

STANFORD
LAM

47

SLIDERS design

•
Database

•
Schematization

•
Chunking and Extraction

•
Reconciliation

•
Autonomous database reconciliation coding agent

•
Coding Agent for reconciled database

## Page 48

STANFORD
LAM

48

Advantages of using Database

•
Can contain arbitrary amount of data

•
Use columns to bring information together using groupby, 
projects etc

•
LLMs are good at generating SQL

## Page 49

STANFORD
LAM

49

SLIDERS design

•
Database

•
Schematization

•
Chunking and Extraction

•
Reconciliation

•
Autonomous database reconciliation coding agent

•
Coding Agent for reconciled database

## Page 50

STANFORD
LAM

50

Sets of Long

Documents Semantic

Chunking +
Contextualized

Extraction

Schema

Question

+

Schematization

Row 1

Row 2

Row m

…

reconciled

table

Row 1

Row 2

Row n

…

raw table

Autonomous
Reconciliation
Coding Agent

SQL programs
Coding Agent

Final 
Answer
DB
Execution

SLIDERS

## Page 51

STANFORD
LAM

51

Schematization

•
Why?
•
 Users commonly refine their questions and will ask for followup 
questions

•
Can we guess the followup questions the user might ask?

•
How? LLMs are capable of knowing what schema is required.
•
We need to provide sample documents

•
Explicitly prompt to find a broader latent schema and 
anticipate future questions

•
Need units and scale for extraction – happens in parallel.

Extracting extra information can amortize cost and don’t have 
to read documents again for follow-up questions.

## Page 52

STANFORD
LAM

52

SLIDERS design

•
Database

•
Schematization

•
Chunking and Extraction

•
Reconciliation

•
Autonomous database reconciliation coding agent

•
Coding Agent for reconciled database

## Page 53

STANFORD
LAM

53

Sets of Long

Documents Semantic

Chunking +
Contextualized

Extraction

Schema

Question

+

Schematization

Row 1

Row 2

Row m

…

reconciled

table

Row 1

Row 2

Row n

…

raw table

Autonomous
Reconciliation
Coding Agent

SQL programs
Coding Agent

Final 
Answer
DB
Execution

SLIDERS

## Page 54

STANFORD
LAM

54

Contextualized Extraction Technique

•
LLMs still like to hallucinate

•
When given text contains no useful information (common for chunks)

•
When extracting a JSON object

→ Relevance gating.

•
Use a lightweight LLM to decide if a chunk is relevant

Chunk
Relevant?
Extract

null

Yes

No

JSON 
object

Contextualized Information Extractor

## Page 55

STANFORD
LAM

55

SLIDERS design

•
Database

•
Schematization

•
Chunking and Extraction

•
Reconciliation

•
Autonomous database reconciliation coding agent

•
Coding Agent for reconciled database

## Page 56

STANFORD
LAM

56

How do long term borrowing patterns differ across companies and sectors?

Extracted example from our 100 
annual financial filings

Chunk-wise extraction can be “dirty”

## Page 57

STANFORD
LAM

57

Chunk-wise extraction can lead to:
• Duplicates
• Incomplete information
• Conflicting information

Chunk-wise extraction can be “dirty”

## Page 58

STANFORD
LAM

58

Traditional database cleaning

•
Past works focus on either detecting errors or fixing errors

•
Traditionally use statistical methods and integrity constrains

•
Recent LLM methods identify typos, or find semantic outliers, 
or require labelled human data

•
Doesn’t work when you need to address gross redundancies, 
inconsistencies and incompleteness caused by chunk-wise 
extraction

Example: two different cities connot have the same pincode

Example: datetime conversion, fix “united states of amerida” to 
“united states of America”

## Page 59

STANFORD
LAM

59
Need context for database cleaning

We can extract provenance, text span,

and extraction rationale

## Page 60

STANFORD
LAM

60

SLIDERS design

•
Database

•
Schematization

•
Chunking and Extraction

•
Reconciliation

•
Autonomous database reconciliation coding agent

•
Coding Agent for reconciled database

## Page 61

STANFORD
LAM

61

Database Agents

•
Example SUQL

•
User provides the problem      Agent generates the SQL

•
Challenge: we need to identify the problem as well

SLIDERS: First database reconciliation agent 
that figures out the problem and comes up with 
the solution

## Page 62

STANFORD
LAM

62

Can LLM agent do it?

•
Will load the first few rows (10) and generalize the rule

Example: The best value among the first 10 rows for long term 
debt is MAX. So for each company I will keep the maximum 
long term debt

•
Will try to load the whole database!

•
Which exceeds the context if we have large amount of 
evidence

•
Makes irreversible updates which are incorrect!

## Page 63

STANFORD
LAM

63
Autonomous Database Reconciliation
Coding Agent

Analyze tables

using SQL

Reasons about 
issues in the table

Perform updates on

tables using SQL

Verify updates or

rollback

Discover Issues
Fixing Issues

## Page 64

STANFORD
LAM

64
Autonomous Database Reconciliation
Coding Agent

•
Group the table by primary key

•
Select primary key from the schema and inspecting the table

•
LLMs are inconsistent, use majority vote

•
Provide explicit examples of primary keys

- Metrics over time: Key = entity + time_period

- Events with content: Key = entity + timestamp

- Entity relationships: Key = source + target

•
Canonicalize values for consistent results

## Page 65

STANFORD
LAM

65
Autonomous Database Reconciliation
Coding Agent

Analyze tables

using SQL

Reasons about 
issues in the table

Discover Issues

Kinds of errors possible:
-
Duplicate

-
Trigger: Multiple rows with redundant problems
-
Purpose: Remove redundant rows, keeping the best representation
-
Kinds of fixes: Select best row
-
If there are different values, nulls its not issue is not duplication
-
Requires aggregation:

-
Trigger: requires holding multiple values or need to sum, average, etc
-
Purpose: Combine multiple valid values into a unified representation
-
Kinds of fixes: SUM, ARRAY_AGG, MIN/MAX
-
Incomplete information

-
Trigger: Information is scattered across rows with incomplete data that can be 
filled by copying values
-
Purpose: Broadcast complete information to fill missing data
-
Kinds of fixes: Will copy consistent values without combining or transforming them
-
Returns multiple rows, use when values need copying, not merged
-
Conflicting information

-
Trigger: Different values exist for a field, and only One is correct
-
Purpose: Select the single best value based on evidence, source and exactness
-
Kinds of fixes: Evaluate which value to keep and discard others

Default to conflicting information when uncertain 
about aggregate or resolve conflict

## Page 66

STANFORD
LAM

66
Autonomous Database Reconciliation
Coding Agent

Perform updates on

tables using SQL

Verify updates or

rollback

Fixing Issues

• Instructions
• Read the quote and rationale fields to 
understand what each row represents
• Compare ALL non-primary-key measured 
fields (date, amount, description, etc.)
• Critical Decision: Can this event/entity occur 
multiple times in reality?
• Select extracted value over computed
• Select higher precision value if available

SELECT 
  * EXCLUDE(col_a, col_a_quote, col_b),
  -- Aggregate multi-valued column across all rows in this PK group
  STRING_AGG(DISTINCT col_a, ' | ') OVER (PARTITION BY pk_col1, pk_col2) AS col_a,
  STRING_AGG(DISTINCT col_a_quote, ' | ') OVER (PARTITION BY pk_col1, pk_col2) AS col_a_quote,
  -- Sum numeric values across rows
  SUM(col_b) OVER (PARTITION BY pk_col1, pk_col2) AS col_b
FROM {{table_name}}
WHERE pk_col1 = '...' AND pk_col2 = '...'

## Page 67

STANFORD
LAM

67
Autonomous Database Reconciliation
Coding Agent

Perform updates on

tables using SQL

Verify updates or

rollback

Fixing Issues

• We observed that even if LLMs reason correctly 
for how to fix an issues they still make errors in 
updates
• Need a verifier that checks if the update on the 
database matches the intent

• If not, rollback the changes and give 
feedback to the LLM.

## Page 68

STANFORD
LAM

68
Autonomous Database Reconciliation
Coding Agent

Analyze tables

using SQL

Reasons about 
issues in the table

Perform updates on

tables using SQL

Verify updates or

rollback

Discover Issues
Fixing Issues

## Page 69

STANFORD
LAM

69

Reasoning for finding issues

There are 8 rows for the same PK (’3M’, ’2022-12-31’), all in the OperatingMarginMetrics table. 
The main data columns (operating_income, net_sales, operating_margin) show several 
repeated values for total company (operating_income=6539, net_sales=34229, 
operating_margin~19.1), but also several rows for business segments (Safety and Industrial, 
Transportation and Electronics, Health Care, Consumer) with distinct values. Some rows have 
calculated margins, some have explicit margins, and some have missing values. The segment 
rows are not redundant with the total company rows---they represent different aspects. 
However, among the total company rows, there are clear redundancies (same values, slightly 
different margin due to rounding/calculation, some with explicit margin, some with 
calculated). To move toward a single consolidated row, we need to resolve conflicts where 
the same field has slightly different values (e.g., operating_margin 19.10 vs 19.11), and select 
the best representative for total company. For the segment rows, aggregation may be 
needed later, but first, resolving conflicts among total company rows will reduce redundancy 
and clarify which rows are truly distinct. Therefore, the next step is to resolve conflicts.

## Page 70

STANFORD
LAM

70

The 8 rows represent both consolidated company-level metrics and business segment breakdowns for 3M for FY2022. There 
are true conflicts in the measured values for operating_income, net_sales, and operating_margin, but these are not errors---
they reflect distinct entities: the consolidated company and its segments (Safety & Industrial, Transportation & Electronics, 
Health Care, Consumer). The schema is for company-level metrics, but the extraction includes segment-level rows, which 
are valuable for analysis. However, the merge objective is to deduplicate and resolve conflicts for the company-level row, 
not to preserve segment rows as separate events.

Upon inspection, two rows (row_id=1 and row_id=10, also row_id=13) provide the consolidated

company-level metrics:

- operating_income: 6539

- net_sales: 34229

- operating_margin: 19.1% (explicit in row_id=1, calculated in row_id=10/13)

Row_id=1 is extracted from a table labeled ’Total Company’ and provides explicit values for all three metrics, with direct 
quotes and clear rationale. Row_id=10 and row_id=13 are from the Consolidated Statement of Income and Business 
Segment Information, also authoritative, but the operating margin is calculated, not quoted. Row_id=1 best matches the 
field definition alignment, extraction location relevance, and source authority criteria.

Segment rows (row_id=2,4,6,8) are not company-level and should not be merged into the company-level output row. 
Row_id=0 is a summary/narrative row with less direct metric extraction. Therefore, the best approach is to select row_id=1 
as the single authoritative company-level row for FY2022, preserving all original columns

SELECT * FROM OperatingMarginMetrics_69ffa681 WHERE row_id = 1

Reasoning for fixing the issue

## Page 71

STANFORD
LAM

71

SLIDERS design

•
Database

•
Schematization

•
Chunking and Extraction

•
Reconciliation

•
Autonomous database reconciliation coding agent

•
Coding Agent for reconciled database

## Page 72

STANFORD
LAM

72

Coding Agent for Final Answer

•
Autonomous database reconciliation coding agent gives 
use the reconciled table

•
We can now use a coding agent that generates sql to 
generate answers for us

•
Uses SQL, tries to perform group by, get stats, captures 
provenance from the database

•
Generates a final report with caveats (if any)

## Page 73

STANFORD
LAM

73

108 more rows

How do long term borrowing patterns differ across companies and sectors?

Step 1: before comparing sectors, understand how skewed borrowings are. Bucket 
companies by size, keep only High or Very High confidence rows, and sum each bucket to 
see where the debt sits

SELECT CASE WHEN long_term_borrowings = 0    THEN '0 (no debt)'
            WHEN long_term_borrowings < 10   THEN '<10M'
            WHEN long_term_borrowings < 100  THEN '10M-100M'
            WHEN long_term_borrowings < 1000 THEN '100M-1B'
            WHEN long_term_borrowings < 5000 THEN '1B-5B'
            ELSE '>5B' END AS bucket,
       COUNT(DISTINCT company_name) AS companies,
       ROUND(SUM(long_term_borrowings), 0) AS total_usd_m
FROM CompanyLongTermBorrowings
WHERE long_term_borrowings IS NOT NULL
  AND long_term_borrowings_confidence IN ('High', 'Very High')
GROUP BY bucket
ORDER BY MIN(long_term_borrowings);

Coding agent for final answer generation

## Page 74

STANFORD
LAM

74
Step 2: the top bucket holds half the total with nine 
companies. Quantify how concentrated debt is 
before drawing sector conclusions.

WITH per_company AS (
  SELECT company_name, MAX(long_term_borrowings) AS v
  FROM CompanyLongTermBorrowings
  WHERE long_term_borrowings IS NOT NULL
  GROUP BY company_name
), ranked AS (
  SELECT *, ROW_NUMBER() OVER (ORDER BY v DESC) AS rk FROM per_company
)
SELECT ROUND(100.0 * SUM(CASE WHEN rk <= 5  THEN v END) / SUM(v), 1) AS top5_share_pct,
       ROUND(100.0 * SUM(CASE WHEN rk <= 10 THEN v END) / SUM(v), 1) AS top10_share_pct,
       COUNT(*) AS companies_with_value
FROM ranked;

Step 5: retail has the widest range and the single largest 
borrower. List its companies to see whether the pattern is uniform 
or driven by one name, and check for repeated periods.

SELECT company_name, period_end, long_term_borrowings
FROM CompanyLongTermBorrowings
WHERE sector = 'Retail' AND long_term_borrowings IS NOT NULL
ORDER BY long_term_borrowings DESC
LIMIT 50;

## Page 75

STANFORD
LAM

75

Long-term borrowings across the 100 filings are extremely skewed. Of 100 companies with a 
reported figure, the median is about 123 million USD while the mean is about 1.2 billion, and the 
five largest borrowers account for 39% of all reported debt, the top ten for 59%. Nine companies 
above 5 billion USD hold roughly 89.6 billion USD, more than the other hundred combined.

Capital-intensive and consumer-financing sectors carry the most debt. Semiconductors shows 
the highest median at about 11.8 billion USD, driven by Micron at 11.76 billion and Marvell at 4.5 
billion. Retail has the widest spread: CarMax leads the entire dataset at 17.35 billion USD, 
reflecting its auto-finance receivables funding, followed by AutoZone at 8.6 billion, Macy's at 7.2 
billion, Costco at 5.7 billion, and GameStop at 4.2 billion. Software is bimodal: Salesforce reports 
8.5 billion and Accenture 5.0 billion, while Okta reports none.

At the other end, 14 companies report zero long-term borrowings and another 31 report under 10 
million USD. These are predominantly shell or acquisition companies, early-stage technology firms, 
and small restaurant operators, which fund themselves through equity rather than term debt.

Two caveats apply. Micron appears under two name spellings with nearly identical values, so 
sector totals should treat it as one company. Macy's contributes figures for three different period 
ends, so the 2.78 billion rows reflect earlier comparative periods rather than current borrowings. In 
addition, 92 of the 233 reconciled rows have no borrowings figure, so companies that did not 
state a long-term debt line are absent from these comparisons.

How do long term borrowing patterns differ across companies and sectors?

Also tell you what might have gone 
wrong

## Page 76

STANFORD
LAM

76

Ask follow up questions

•
Once we have extracted these values, we can ask follow up 
questions like the company with minimum debt, with 
maximum debt, etc.

•
We can create the database once and then reuse it with 
amortized cost

108 more rows

## Page 77

EVALUATION

## Page 78

STANFORD
LAM

78

Lack of benchmarks!

•
Real-world applications of systematic reviews often use 
documents which far exceed the context windows

•
No benchmark exists which requires all

•
Extraction from several documents

•
Extract large amount of data

•
Requires comparing information

## Page 79

STANFORD
LAM

79

New Benchmarks

WikiCeleb100

•
100 Wikipedia pages on 
recently trending 
celebrities

•
Research Question: Who is 
the youngest celebrity?

FinQ100

•
100 10-Q documents 
from 2025 Nov – 2026 Jan

•
Research Question: 
Which company has the 
lowest long-term debt?

(3.9M tokens)
(36M tokens)

Manually annotated reconciled tables
Manually verified final answer
Additional follow-up questions for each domain

## Page 80

STANFORD
LAM

80

Evaluation on existing benchmarks

•
Doesn’t fit in the context:

•
Browsecomp+: Given several documents answer multi-hop 
questions

•
Fits in the context:

•
FinanceBench: single document

•
Loong: multiple document

•
Oolong: Synthetically created text

## Page 81

STANFORD
LAM

81

Evaluation Results

•
RAG fails on questions that 
requires high evidence 
recall

•
Chunking method are 
better than RAG

•
SLIDERS outperforms even 
with a weaker model

•
SLIDERS can reuse its 
evidence table

## Page 82

STANFORD
LAM

82

Analysis

•
SLIDERS mains performance with varying input token length 
on BrowseComp+

•
Even as number of evidence increases, SLIDERS still holds up 
across BrowseComp+, WikiCeleb100 and FinQ100

## Page 83

STANFORD
LAM

83

Benchmarks that fit in the context window

•
Keyword search 
(RLM) can be worse 
than giving the LLM 
the whole document

•
SLIDERS can even 
help when the input 
fits in the LLM’s 
context

## Page 84

STANFORD
LAM

84

Which stage in SLIDERS helps?

•
Direct table: provide the extracted table to the LLM

•
No Recon: Do not perform reconciliation using autonomous 
coding agent

•
No chunk extraction: Ask the llm to put information in a 
database direction (when the input fits)

## Page 85

STANFORD
LAM

85

Conclusions

•
Important to analyze across large sets of long documents
•
Need to scale beyond model context limit
•
Precision degrades with document length in the context
•
Approaches
•
Training: for precision – not successful
•
Chunking: for precision and scalability
•
SLIDERS: 
•
Leverages SUQL: text → databases 
•
Use Autonomous Coding Agent for reconciliation
•
Semantic chunking, contextualized extraction
•
Long-context benchmarks: SOTA (despite annotation errors)
•
Scale beyond long-context benchmarks
