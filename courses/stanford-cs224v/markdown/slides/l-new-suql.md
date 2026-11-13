# Querying Hybrid (Structured and Unstructured) Data

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-new-suql.pdf) · [Raw file](../../raw/slides/l-new-suql.pdf)

Retrieved: 2026-11-13T16:49:47.371686+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224v Course

Conversational Virtual Assistants with Deep Learning

Lecture 8

Structured and Unstructured Data Queries

1
Monica Lam & Shicheng Liu

## Page 2

STANFORD
LAM

Retrieval + Question Answering

1. Matching a set of records with a set of constraints? \[L3, L4)

Constraints-satisfaction based retrieval and match (SMT→DB)

2. Short questions on free-text (L5)

RAG with embedding-based retrieval

3. Databases and knowledge bases (L6, L7)

Complex queries in SQL, SPARQL (Select, aggregate, joins…)

4. Hybrid: databases + free-text knowledge (L8 - this lecture)

5. Systematic reviews across many documents (L9)

2

## Page 3

STANFORD
LAM

Example 1: Yelp: DB + Free text

•
Blue columns contain structured data
•
Yellow columns are free text
•
A lot of rows (thousands)

3

A lot of info is in free-text

Please find me a spicy

Chinese restaurant.

Corpus does not fit in context windows

## Page 4

STANFORD
LAM

Hybrid Data

4

Structured
Free Text

Wiki
Wikidata, Wikipedia tables
Wikipedia

Restaurants
Cuisines, opening hours, 
address, rating
Reviews, popular dishes

Products
Product ID, cost, ratings, sizes, 
physical dimensions, color
Descriptions, reviews

Courses

Class number, time offered, 
instructor, building, pre-
requisites

Descriptions, reviews

Business 
processes
Receipts, statements
Regulations

Medical
Patient demographics
Prescription
Diagnosis history

## Page 5

STANFORD
LAM

Quiz: 
How would you handle the combo?

5

## Page 6

Method 1. Use a classifier to decide to use databases or text.

Jin et al., 2021; Zhao et al., 2023

Method 2. Use the database to find the records, apply LLM to process text fields.

Jin et al. https://aclanthology.org/2021.dialdoc-1.16/
Zhao et al. https://aclanthology.org/2023.sigdial-1.28/

Does it work?

### Page links

- [Link 1](https://aclanthology.org/2021.dialdoc-1.16/)
- [Link 2](https://aclanthology.org/2023.sigdial-1.28/)

## Page 7

Method 3. Linearize structured data into free text

Oguz et al., 2022

Oguz et al., https://aclanthology.org/2022.findings-naacl.115/

### Page links

- [Link 1](https://aclanthology.org/2022.findings-naacl.115/)

## Page 8

STANFORD
LAM

Problems with Linearization

Do not take advantage of the power of SQL

• How to combine different clauses together?
e.g. multiple clauses: "Are there any restaurants that have a great view of 
the Golden Gate bridge in San Francisco?"

• Hard to do column computations 
(rank, max, min, average, count) on flattened data

•
e.g. "what is the top-rated Chinese restaurant?"

8

## Page 9

STANFORD
LAM

HybridQA: An illustrative dataset

9

## Page 10

STANFORD
LAM

HybridQA Dataset (1 out of 13000 tables)

Wikipedia Tables
Wikipedia Pages
hyperlinked

10

Flag bearers of

Myanmar 
at the Olympics

## Page 11

STANFORD
LAM
11

T: Table
P: Passage
Quiz: How many total # of types can there be?

## Page 12

STANFORD
LAM

Challenges

•
Arbitrary composition of database and text accesses
•
Joins – combines information of columns and free-text
•
Superlatives – find max on entire columns

•
Database queries are optimized for large datasets
•
Many many compiler optimizations e.g. order of joins, 
blocking the computation to improve locality, etc.
•
Any free-text search breaks up the queries, 
preventing optimizations across the whole query.

12

## Page 13

STANFORD
LAM

Previous techniques

Can these approaches handle the HybridQA questions 
(assuming large tables)?

1. Classify query to decide to retrieve from DB or Text

2. Retrieve answers from DB first and use LLM to process the text fields

3. Linearize DB to text; use Text Retrieval

## Page 14

STANFORD
LAM

Lecture Goals

• Understanding hybrid queries

• SUQL Language – Design and Rationale

• SUQL Implementation – Semantic parser & Compiler

• Evaluation in a real life app: Yelp

• Evaluation with a large dataset: HybridQA

14

## Page 15

STANFORD
LAM

Goals for Handling Hybrid Data

1. Maximize available information retrieval capability

• Keep text as text and KBs as KBs

• Combine the best of two worlds!

2. Hybrid multi-hop: Support arbitrary composition of IR and KB

• Efficient searching of free text (using embedded similiarity)

• Relational algebra operations (select, aggregate, rank, …)

15

NEW!

## Page 16

STANFORD
LAM

• Create the SUQL (Structured & Unstructured Query Language)

• Leverages LLM familiarity 
with the most popular DB query language

• Extends SQL to include free-text operations

• The language supports arbitrary composition

• Create an optimizing compiler to evaluate efficiently

16

## Page 17

STANFORD
LAM

SUQL Free-Text Support

• Add free-text primitives into SQL, implemented with IR & LLM

• Two functions: summary, answer

“I want a family-friendly restaurant in Palo Alto”

SELECT *, summary(reviews) FROM restaurants

WHERE location = 'Palo Alto’
AND answer(reviews, ‘is it a family friendly restaurant’) = 'Yes' LIMIT 1;

17

Quiz: How do you implement summary and answer?

## Page 18

STANFORD
LAM

HybridQA Dataset

Wikipedia Tables
Wikipedia Pages
hyperlinked

18

Flag bearers of

Myanmar 
at the Olympics

## Page 19

STANFORD
LAM
19

T: Table
P: Passage

## Page 20

STANFORD
LAM

HybridQA Questions in SUQL

Type I (T->P)

Where was the XXXl Olympic held?

SELECT answer("Event year_Info",

'where is this event held?’)

FROM ”Flag" WHERE "Name" = 'XXXI’

20

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

Where was the XXXI Olympic held?

## Page 21

STANFORD
LAM

HybridQA Questions in SUQL

Type I (T->P)

Where was the XXXl Olympic held?

SELECT answer("Event year_Info",

'where is this event held?’)

FROM ”Flag" WHERE "Name" = 'XXXI’

21

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

Where was the XXXI Olympic held?

## Page 22

STANFORD
LAM

HybridQA Questions in SUQL

Type II (P->T)

What was the name of the Olympic event held in Rio?

SELECT "Name" FROM ”Flag"

WHERE answer("Event year_Info",

'where is this event held?') = 'Rio’

22

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 23

STANFORD
LAM

HybridQA Questions in SUQL

Type II (P->T)

What was the name of the Olympic event held in Rio?

SELECT "Name" FROM ”Flag"

WHERE answer("Event year_Info",

'where is this event held?') = 'Rio’

23

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 24

STANFORD
LAM

HybridQA Questions in SUQL

Type III (P->T->P)

When was the flag bearer of Rio Olympic born?

SELECT answer("Flag Bearer_Info",

'when is this person born?’)

FROM ”Flag"

WHERE answer("Event year_Info", 'where is this event

held?') = 'Rio’

24

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 25

STANFORD
LAM

HybridQA Questions in SUQL

Type III (P->T->P)

When was the flag bearer of Rio Olympic born?

SELECT answer("Flag Bearer_Info",

'when is this person born?’)

FROM ”Flag"

WHERE answer("Event year_Info", 'where is this event

held?') = 'Rio’

25

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 26

STANFORD
LAM

HybridQA Questions in SUQL

Type IV (T&P)

Which male bearer participated in Men's 100kg event in the

Olympic game?

SELECT "Flag Bearer" FROM ”Flag" WHERE

"Gender" = 'Male' AND

answer("Flag Bearer_Info",

'what event did this person participate in?’)

= “Men’s 100kg event”

26

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 27

STANFORD
LAM

HybridQA Questions in SUQL

Type IV (T&P)

Which male bearer participated in Men's 100kg event in the

Olympic game?

SELECT "Flag Bearer" FROM ”Flag" WHERE

"Gender" = 'Male' AND

answer("Flag Bearer_Info",

'what event did this person participate in?’)

= “Men’s 100kg event”

27

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 28

STANFORD
LAM

HybridQA Questions in SUQL

Type V (T-Compare | P-Compare)

For the 2012 and 2016 Olympic Event, when was the younger

flag bearer born?

SELECT MAX

(answer("Flag Bearer_Info",

'when is this person born?')::date)

FROM ”Flag" WHERE "Event year" IN ('2016', '2012’)

28

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 29

STANFORD
LAM

HybridQA Questions in SUQL

Type V (T-Compare | P-Compare)

For the 2012 and 2016 Olympic Event, when was the younger

flag bearer born?

SELECT MAX

(answer("Flag Bearer_Info",

'when is this person born?')::date)

FROM ”Flag" WHERE "Event year" IN ('2016', '2012’)

29

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 30

STANFORD
LAM

HybridQA Questions in SUQL

Type VI (T-Superlative | P-Superlative)

When did the youngest Burmese flag bearer participate

in the Olympic opening ceremony?

SELECT "Event year" FROM ”Flag” ORDER BY

answer("Flag Bearer_Info",

'when is this person born?')::date

DESC LIMIT 1;

30

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 31

STANFORD
LAM

HybridQA Questions in SUQL

Type VI (T-Superlative | P-Superlative)

When did the youngest Burmese flag bearer participate

in the Olympic opening ceremony?

SELECT "Event year" FROM ”Flag” ORDER BY

answer("Flag Bearer_Info",

'when is this person born?')::date

DESC LIMIT 1;

31

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

T: Table
P: Paragraph

## Page 32

STANFORD
LAM

At-A-Glance: HybridQA Questions in SUQL

CREATE TABLE Flag (
"Name" TEXT, 
"Flag Bearer" TEXT, 
"Flag Bearer_Info" TEXT\[\],
"Gender" TEXT, 
"Event year" TEXT, 
"Event year_Info" TEXT\[\]);

Type I (T->P)
Where was the XXXl Olympic held?

SELECT
answer("Event year_Info", 
              'where is this event held?’) 
FROM ”Flag" WHERE "Name" = 'XXXI'

Type II (P->T) What was the name of the 
Olympic event held in Rio?

SELECT "Name" FROM ”Flag" 
WHERE answer("Event year_Info", 
'where is this event held?') = 'Rio’

Type III (P->T->P) When was the flag bearer of 
Rio Olympic born?

SELECT answer("Flag Bearer_Info", 
'when is this person born?’) 
FROM ”Flag" 
WHERE answer("Event year_Info", 
'where is this event held?') = 'Rio’

Type IV (T&P) Which male bearer 
participated in Men's 100kg event in the 
Olympic game?

SELECT "Flag Bearer" FROM ”Flag" 
WHERE "Gender" = 'Male' AND 
answer("Flag Bearer_Info", 
'what event did this person 
participate in?’) 
= “Men’s 100kg event”

Type V (T-Compare | P-Compare) For the 
2012 and 2016 Olympic Event, when was the 
younger flag bearer born?

SELECT MAX
(answer("Flag Bearer_Info", 
  'when is this person born?')::date) 
FROM ”Flag" 
WHERE "Event year" IN ('2016', '2012’)

Type VI (T-Superlative | P-Superlative) When 
did the youngest Burmese flag bearer 
participate in the Olympic opening ceremony?

SELECT "Event year" FROM ”Flag” 
ORDER BY answer("Flag Bearer_Info", 
'when is this person born?')::date 
DESC LIMIT 1;

32
Quiz: Where can ’answer’ be used in a query?

## Page 33

STANFORD
LAM

Conversational Example: Restaurant

Restaurants

Do you have a recommendation for a first date restaurant in Palo Alto?

We're thinking sushi but not sure what's good around here.

SELECT *, summary(reviews) FROM restaurants 
WHERE 'sushi' = ANY (cuisines) AND location = 'Palo Alto' AND rating >= 4.0

AND answer(reviews, 'is this restaurant good for a first date?') = 'Yes’

ORDER BY num_reviews DESC LIMIT 1;

33

## Page 34

STANFORD
LAM

Laptops

I need a laptop with a Thunderbolt 3 port and

at least 16GB RAM for my workstation setup.


SELECT *, summary(reviews) FROM laptops

WHERE ram >= 16 AND
(answer(about, 'does this laptop have Thunderbolt 3?') = 'Yes’ 
OR answer(description, 'does this laptop have Thunderbolt 3?') = 'Yes’)

LIMIT 3;

Conversational Example: Shopping

34

CREATE TABLE laptop (
”ram" int, 
…,
”about" TEXT, 
“description" TEXT\[\],
”reviews” TEXT);

It is often unclear where the answer is in the text, 
useful/easy to search for all possibly relevant text fields.

## Page 35

QUIZ

W HA T C A N W E U S E S UQ L F OR?

35

## Page 36

STANFORD
LAM

Advantages of SUQL

•
Formal representation combining IR and DB query
•
Succinct, expressive, domain independence

•
Full compositionality: combining IR and relational algebra

•
Interpretability

•
We can read the query back 
so users know what question is being answered

•
Quiz: Is the answer always correct given a formal query?

•
It is true for the database part

•
But there is a potential for error in free-text Q&A 
(Information retrieval error, answer error)

•
SUQL is a high-level programming language
•
Optimization issues handled by compilers, abstracted from programmers

36

## Page 37

STANFORD
LAM

Lecture Goals

• Understanding hybrid queries

• SUQL Language – Design and Rationale

• SUQL Implementation – Semantic parser & Compiler

• Evaluation in a real life app: Yelp

• Evaluation with a large dataset: HybridQA

37

## Page 38

STANFORD
LAM

SUQL-based agent on HybridQA
A simple prompt-based system

38

Predicted SUQL

answer fcn

summary fcn

Semantic parser

Result conversion

prompt

Test query

SUQL compiler

Database
results

Templates written in jinja syntax

• SQL can run SUQL 
programs without 
modification

• summary / answer are 
just external functions

• But it is slow

Repeat if there are no results

### Page links

- [Link 1](https://docs.google.com/document/d/1O3nNFuhdlAetvweOUCVubNHaceq30M3um7QllxYkyzc/edit?usp=sharing)
- [Link 2](https://docs.google.com/document/d/1k5Ye067o2pewfNULpofTUX21lFALpyzcN5fVO_NXT7Q/edit?usp=sharing)
- [Link 3](https://docs.google.com/document/d/1vg2Kjww5hbykJVeaoRzzwr5uuDt4W0rijbzwfjLm6uQ/edit?usp=sharing)
- [Link 4](https://docs.google.com/document/d/1z15eFt9HhatPpAzabxKYa5MbUo28SL8wyfs_OxqpW4g/edit?usp=sharing)
- [Link 5](https://jinja.palletsprojects.com/en/3.1.x/)

## Page 39

SUQL OPTIMIZING COMPILER

39

## Page 40

STANFORD
LAM

Example

“I want a family-friendly restaurant in Palo Alto”

SELECT *, summary(reviews) FROM restaurants 
WHERE  answer(reviews, ‘is it a family friendly restaurant’) = 'Yes’

and  location = 'Palo Alto’ 
•
Consider a naïve implementation
•
Retrieve each review from the table
•
For each review, call LLM to answer the question
•
Filter on location 
•
Summarize all the returned reviews
•
Report the first few

40

Quiz: How would you optimize the query?

## Page 41

STANFORD
LAM

1. Use embedding to implement filter

• Use embedding model (vector similarity) to return top 
candidates, inside faiss (Facebook AI Similarity Search)

• For applications such as recommendation, 
it is not necessary to return all the answers

• Return only top results to LLM-based answer functions

answer(reviews, ‘is it a family friendly restaurant’) =

‘Yes’

## Page 42

2. ENUM classification

WHERE ‘coffee’ = ANY(cuisines)

• “cuisines” is an enumerated type.
• Here, database only contains
• ‘coffee & tea’
• ‘café’
• Overload = operator
• Use LLM to implement a ENUM classifier 
to match against similar values

## Page 43

STANFORD
LAM

3. Predicate Ordering

• Execution of structured predicates is much cheaper

• Always execute structured predicates first

43

answer(reviews, ‘is it a family friendly restaurant’) = ‘Yes’

AND

and  location = 'Palo Alto’

## Page 44

STANFORD
LAM

4. Lazy Evaluation

• Lazy evaluation: Evaluate only when the result is needed

• Stop calling answer as soon as LIMIT 1 is reached

44

answer(reviews, ‘is it a family friendly restaurant’) = ‘Yes’

AND
answer(reviews, ’is it easy to park’) = ‘Yes’

AND
and  location = 'Palo Alto’ LIMIT 1

## Page 45

STANFORD
LAM

SUQL Compiler Implementation

•
SUQL is implemented by modifying the SQL compiler
•
To support arbitrary composition of SQL and summary/answer 
statements
•
Process the syntax tree of SQL recursively
•
Start from the bottom node with no sub-queries
•
And move to the top
•
For each SELECT statement with answer in it 
Apply optimizations to the SELECT statement 
•
Store the processed results in a temporary table temp
•
Substitute this statement with SELECT from temp
•
SQL compiler handles the final processing

45

## Page 46

STANFORD
LAM

Compiler Optimizations

Compiler optimization needs to operate across the entire query

46

Quiz: Is the optimization necessary?

Quiz: What if we use an agent 
that uses “function calling” to call IR

and query databases separately?

## Page 47

STANFORD
LAM

Lecture Goals

• Understanding hybrid queries

• SUQL Language – Design and Rationale

• SUQL Implementation – Semantic parser & Compiler

• Evaluation in a real life app: Yelp

• Evaluation with a large dataset: HybridQA

47

## Page 48

STANFORD
LAM

Experiment

A real, large dataset

•
Yelp on San Francisco, Palo Alto, Cupertino, 
Sunnyvale
•
Scraped reviews and popular dishes 
information
Components
•
LLM: gpt-3.5-turbo
•
Information retrieval on text fields 
•
indexed with Coco-DR
•
A new optimizing SUQL compiler

48

COCO-DR reference: https://arxiv.org/abs/2210.15212

## Page 49

STANFORD
LAM

Evaluation (in Restaurants)

• We solicit user queries via crowdsourcing on Prolific.

• We do not disclose to the workers what fields are 
available in the database.

• The Yelp Dataset:

1. Just Q&A: 100 crowdsourced questions about restaurants.

2. Conversational: 20 conversations with 96 turns

49

## Page 50

STANFORD
LAM

The Need for Hybrid QA in Real Life?

50

(59%)
(41%)

## Page 51

STANFORD
LAM

Evaluation (in Restaurants)

• In real-world tasks: Difficult to label the gold answers:

• For each query, there are many possible “gold restaurants”

• We manually inspect whether 
restaurants returned satisfy all criteria

• Calculate Query precision: #correct results /  #results

51

Quiz: how do you evaluate its accuracy?

## Page 52

STANFORD
LAM

Using SUQL

53

## Page 53

STANFORD
LAM

Evaluation

54

Quiz: Why are there errors in SUQL answers?

(Linearization @ n: n answers)

## Page 54

STANFORD
LAM

Always verbalize the user query

Allows the user to spot mistakes in the answer

Even when it fails, so users can adjust the query.

I searched for 5-star restaurants in Sunnyvale that serve kids food.

Unfortunately, I couldn't find any search results.

Is there anything else I can help you with?

Defensive Programming: 
What if the Semantic Parser is Wrong?

55

## Page 55

STANFORD
LAM

Hard to find all missing restaurants. 
We performed analysis only when no answers are returned

14 false negatives on our single-turn set (100 questions)

•
Parsing: 2 errors (one syntactic, one enum field confusion)

•
Query evaluation
•
Structured:

•
4 unsupported location service

•
2 opening hours errors

•
2 dishes: searched in popular dishes, but results are in reviews

•
Free-text: 4 false negatives from ‘answer’ (ChatGPT)

Recall Error Analysis

56

 Can be improved

## Page 56

STANFORD
LAM

Lecture Goals

• Understanding hybrid queries

• SUQL Language – Design and Rationale

• SUQL Implementation – Semantic parser & Compiler

• Evaluation in a real life app: Yelp

• Evaluation with a large dataset: HybridQA

60

## Page 57

STANFORD
LAM

HybridQA Dataset: Based on Wikipedia

• 13000 tasks on Amazon Turk:

• Given one crawled Wikipedia table  + its hyperlinked passages.

• Write 6 questions  & answers.

• Each task takes 12 minutes on average, and payment is $2.3 U.S.

• 5 CS graduate students to decide on the acceptance.

61

## Page 58

STANFORD
LAM

A Custom Retriever for HybridQA with model training on training set

Only uses LLM in the "generation-based reasoner" step

https://github.com/wenhuchen/HybridQA#recent-papers
SOTA model: https://arxiv.org/abs/2305.11725
63

### Page links

- [Link 1](https://arxiv.org/abs/2305.11725)
- [Link 2](https://github.com/wenhuchen/HybridQA#recent-papers)

## Page 59

• SUQL outperforms all ICL methods and comes within 8.9% EM and 7.1% F1 
to the SOTA trained on 62k examples
• None of the approaches on HybridQA generalizes to large databases

## Page 60

QUIZ

W HA T S HO U LD W E D O N E XT?

65

## Page 61

STANFORD
LAM

Error Analysis
 We analyzed 72 randomly sampled error cases

Evaluation Issues (61% of errors)

• Format mismatches: 37.5%. 
Predicted “Johnson City, 
Tennessee” 
vs. “Johnson City”.

• The gold label is either wrong or 
incomplete: 23.6%

• There is only 1 gold answer 
when there should be more!

66

A lot of format problems !

True accuracy may reach 84.2%

True Errors (39% of errors)

• Semantic parsing errors: 
22.2%

• Errors from LLM-based 
functions: 11.1%

• Type-related conversation 
errors: 5.6%

 Handled by fine-tuning, but it is not intrinsically important

## Page 62

STANFORD
LAM

Conclusion: SUQL

• Hybrid data queries are natural and important

• Requires arbitrary composition of textual and DB retrieval

• Requires query optimization to support arbitrary composition

• Solution: SUQL

• Zero-Shot semantic parser: IR + relational algebra

• An optimizing compiler

• Evaluation

• Needed in real-life conversations (Yelp)

• Handles composition of queries well (HybridQA)

67
