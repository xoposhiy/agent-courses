# Introduction to ReAct Agents for Querying Knowledge Bases and Graphs

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-agentic.pdf) · [Raw file](../../raw/slides/l-agentic.pdf)

Retrieved: 2026-11-13T16:49:47.235982+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224v Course

Agentic AI

Lecture 6

Agentic AI for Graphs and Tables

1

Shicheng Liu & Monica Lam & Sina Semnani

## Page 2

L ECTURE G OAL

F OCUS: S EMANTIC P ARSING FOR G RAPHS AND T ABLES

A GENTIC A PPROACH

… SO Y OU CAN A PPLY THEM TO Y OUR P ROJECT

## Page 3

STANFORD
LAM

Outline

•
Data Structures: Graphs and Tables
•
How to query them with SPARQL & SQL
•
Graph QA with SPINACH
•
Challenges and Prior Approaches
•
The Agentic Approach
•
Dataset and Evaluation

•
SQL QA with DataTalk

•
Guest Lecture: Big Local News on DataTalk (15 min)

## Page 4

STANFORD
LAM

Graphs and Tables

Relational database
Knowledge graph

Data
Rows and columns 
Entities and properties

Relationships
Matching keys across tables
Edges between entities

Query language
SQL
SPARQL for RDF graphs

In this lecture
Campaign finance
DataTalk

Wikidata
SPINACH

## Page 5

STANFORD
LAM

A Relational Database

•
Rows are records; columns are attributes with defined types

•
Keys identify records and link related tables

restaurants
reviews

id
location

r1
Bytes

r2
Kali

id
restaurant_id
author

review_1
r1
Shicheng

review_2
r1
Sina

review_3
r2
Monica

## Page 6

STANFORD
LAM

Expressiveness of Query Languages

•
Domain agnostic

•
All queries of any domain in knowledge bases
are compositions of a FEW relational algebra operations
• Basic: Selection, Projection, Cartesian product (Join), 
           Union, Set Difference

• Extended: Sort, Aggregate Operators (Sum, Max, Avg, …)

•
Expressive, succinct, well-defined

Amazing

CS Idea

## Page 7

WHERE clause: filter

Show me Chinese restaurants in Palo Alto

SELECT * FROM restaurants
WHERE location == “Palo Alto”

AND 'chinese' = ANY (cuisines)


SELECT * FROM
table \[WHERE filter\]?

CREATE TABLE restaurants (
    id TEXT PRIMARY KEY,
    location TEXT,
    address TEXT,
    cuisines TEXT\[\],
    rating NUMERIC(2,1), 
…);

## Page 8

WHERE clause: filter

Show me Chinese restaurants in Palo Alto

with at least 4.5 stars

SELECT * FROM restaurants
WHERE location = “Palo Alto”
AND “Chinese” = ANY(cuisines)

AND rating >= 4.5

SELECT * FROM
table \[WHERE filter\]?
CREATE TABLE restaurants (
    id TEXT PRIMARY KEY,
    location TEXT,
    address TEXT,
    cuisines TEXT\[\],
    rating NUMERIC(2,1), 
…);

## Page 9

SELECT clause: Projection

Show me the address of  Chinese restaurants in Palo Alto

with at least 4.5 stars

SELECT address FROM restaurants

WHERE location = “Palo Alto”
AND “Chinese” = ANY(cuisines)

AND rating >= 4.5

SELECT field+ FROM
table \[WHERE filter\]?
CREATE TABLE restaurants (
    id TEXT PRIMARY KEY,
    location TEXT,
    address TEXT,
    cuisines TEXT\[\],
    rating NUMERIC(2,1), 
…);

## Page 10

Subquery

Subquery filter:    
param op 
(SELECT * FROM …)

Show me the address of  Chinese restaurants in Palo Alto

reviewed by Bob

SELECT address FROM restaurants

WHERE location = “Palo Alto”
AND “Chinese” = ANY(cuisines)

AND id IN 
(SELECT restaurant_id FROM reviews WHERE author =~ “Bob” )

Atom filter:           
param op value

SELECT field+

FROM table \[WHERE filter\]?
CREATE TABLE restaurants (
    id TEXT PRIMARY KEY,
    location TEXT,
    address TEXT,
    cuisines TEXT\[\],
    rating NUMERIC(2,1), 
…);

CREATE TABLE reviews (
    id TEXT PRIMARY KEY,
    restaurant_id TEXT
    REFERENCES restaurants(id),
    author TEXT,
…);

## Page 11

Sorting

SELECT address FROM restaurants

WHERE location = “Palo Alto”
AND “Chinese” = ANY(cuisines)

AND id IN 
(SELECT restaurant_id FROM reviews WHERE author =~ “Bob” )

ORDER BY rating DESC

Show me the address of top-rated Chinese restaurants in

Palo Alto 
reviewed by Bob

SELECT field+ FROM table \[WHERE filter\]?

ORDER BY field DESC/ASC
CREATE TABLE restaurants (
    id TEXT PRIMARY KEY,
    location TEXT,
    address TEXT,
    cuisines TEXT\[\],
    rating NUMERIC(2,1), 
…);

CREATE TABLE reviews (
    id TEXT PRIMARY KEY,
    restaurant_id TEXT
    REFERENCES restaurants(id),
    author TEXT,
…);

## Page 12

Joins

SELECT * FROM restaurants JOIN reviews ON

restaurants.id = reviews.restaurant_id

WHERE location = “Palo Alto”
AND “Chinese” = ANY(cuisines)

ORDER BY rating DESC

SELECT * FROM
table join table \[WHERE filter\]? \[on filter\]?


Show me top-rated Chinese restaurants in Palo Alto

with their reviews

CREATE TABLE restaurants (
    id TEXT PRIMARY KEY,
    location TEXT,
    address TEXT,
    cuisines TEXT\[\],
    rating NUMERIC(2,1), 
…);

CREATE TABLE reviews (
    id TEXT PRIMARY KEY,
    restaurant_id TEXT
    REFERENCES restaurants(id),
    author TEXT,
…);

## Page 13

STANFORD
LAM

A Knowledge Graph

•
Graph databases represent relations among entities as a graph

•
Nodes are entities

•
Edges are relationships; properties describe them

## Page 14

STANFORD
LAM

Wikidata: The Largest Live Knowledge Graph

•
Stats:

• 15B facts (1B more triples per year)

• 100M entities

• 10K properties (3000 of interest)

• 25K contributors

•
All entities in Wikipedia are in Wikidata

•
Wikidata contains many more entities

## Page 15

STANFORD
LAM

Wikidata Representation – a RDF graph

•
Representation: RDF triples
•
Nodes are entities (represented by unique QIDs)

•
There are many entities with exactly the same name

•
Same ID across all Wikipedia in all languages 
•
Edges are properties (represented by unique PIDs)

SELECT ?x WHERE

{ wd:Q41506    wdt:P112     ?x. }

Stanford
Founded by

Who founded Stanford?

Query with SPARQL

## Page 16

STANFORD
LAM

Running Example: Music Instruments Played

## Page 17

STANFORD
LAM

Edward Rutschman

(Q107705263)

Hokyung Yang
(Q107851778)

Gwynne Kuhner Brown

(Q106627792)

Chad Kirby
(Q107522681)

University of Washington School of Music

(Q98035717)

University of Washington

(Q219563)

Trombone

(Q8350)

Piano
(Q5994)

Affiliation

(P1416)

Educated At

(P69)

Instrument

(P1303)

A Subset of the Knowledge Graph in Wikidata

Zakir Hussain

(Q144719)

Percussion instrument

(Q133163)

Tabla
(Q213100)

## Page 18

STANFORD
LAM

P1303: instrument
P1416: affiliation
P69:     educated at

Q98035717: 
University of Washington 
School of Music

Q219563: 
University of Washington

## Page 19

STANFORD
LAM

The Power of WikiData

•
SPARQL allows relational algebra operations 
across the entire knowledge graph

• Running example needs: filters, projections, joins, counts …

• Query optimizations

•
Dataset for research in 
Mathematics, Biology, Education, Social Sciences, Linguistics, ..

Quiz: Which tables would represent these relationships?

## Page 20

STANFORD
LAM

Why Querying Wikidata with SPARQL is Difficult

•
Heterogeneous data:

•
Entities can have different sets of properties

•
The query must match the properties actually stored

•
Inspect entities and examples before choosing a property

•
Many properties (3000): Hard to memorize all the properties

•
Many similar properties:

•
Often unclear which property or entity should be used

•
Questions on locations: “Where did Isaac Newton live?” “Where is Salesforce?”

•
Possible properties – depends on what is available for the node

•
administrative territorial entity

•
residence, state, country, place of birth, place of death

•
headquarters location, location of formation

•
Need to look at a node’s properties to determine the right SPARQL

•
Queries can be complex

A natural language interface can greatly expand access!

## Page 21

STANFORD
LAM

Outline

•
Data Structures: Graphs and Tables

•
Graph QA with SPINACH
•
Challenges and Prior Approaches

•
The Agentic Approach

•
Dataset and Evaluation

•
SQL QA with DataTalk

•
Guest Lecture: Big Local News on DataTalk (15 min)

## Page 22

Previous Work

Knowledge Base Query Answering (KBQA)

S EMANTIC P ARSER: G ENERATING S PARQL

(F INE- TUNING, LLM)

S UBGRAPH T RAVERSAL: T RAVERSING THE K NOWLEDGE G RAPH

WITHOUT U SING SPARQL

## Page 23

STANFORD
LAM

Semantic Parser
(Llama fine-tuned with 3K samples)

From Wikidata, the filming location of 
‘A Bronx Tale’ includes New Jersey 
and New York

Where did Bronx take place?

GPT-3

GPT-3 guesses that the movie 
took place in Bronx, New York

Entity Linker

(‘A Bronx Tale’, ‘Q1130705’)

No 
Response

1. Semantic Parsing with Fine-Tuning

Response

Silei Xu et al. Fine-tuned LLMs Know More, Hallucinate Less with Few-Shot Sequence-to-Sequence Semantic Parsing over Wikidata.. EMNLP 2023

## Page 24

STANFORD
LAM

2. Semantic Parsing with Prompting LLMs

•
LLMs know the syntax of SPARQL

• And just a few PIDs and QIDs of entities

• Cannot parse “research questions” 
(with many joins, group-bys, ranks, …)

## Page 25

STANFORD
LAM

3. Subgraph Retrieval (No SPARQL)

Quiz: Can this provide the full generality of SPARQL

Subgraph Retrieval Enhanced Model for Multi-hop Knowledge Base Question Answering (Zhang et al., ACL 2022)

Retrieve a part of the graph based on a question

Quiz: Can this find the tallest mountain?

### Page links

- [Link 1](https://aclanthology.org/2022.acl-long.396)

## Page 26

STANFORD
LAM

4. LLM-Based Graph Exploration

Explore a sub-graph by walking the graph one edge at a time

Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph, Sun et al, ICLR 2024

Quiz: Can this provide the full generality of SPARQL

## Page 27

STANFORD
LAM

Outline

•
Data Structures: Graphs and Tables

•
Graph QA with SPINACH
•
Challenges and Prior Approaches

•
The Agentic Approach

•
Dataset and Evaluation

•
SQL QA with DataTalk

•
Guest Lecture: Big Local News on DataTalk (15 min)

## Page 28

A GENTIC AI

A N AI SY STEM

THAT CAN MAKE DECISIONS AND TAKE ACTIONS ON ITS OWN

TO ACHIEVE A GOAL

## Page 29

SPINACH:

SPARQL-Based Information Navigation for

Challenging Real-World Questions

Shicheng Liu*     Sina J. Semnani*
Harold Triedman1   Jialiang Xu   Isaac Dan Zhao     Monica S. Lam

Stanford University

* Equal contribution
1 Cornell Tech;  Work conducted while at the Wikimedia Foundation

EMNLP 2024

## Page 30

STANFORD
LAM

Https://spinach.genie.stanford.edu

## Page 31

STANFORD
LAM

v.       Combines the Best of Semantic Parsing (SPARQL), 
                                                 Subgraph Retrieval, & LLMs

•
Semantic parsing to SPARQL: 
• Expressiveness, implementation/query optimizations

•
Graph retrieval: exam actual properties in the data

•
LLM agentic approach combines the 2 above                 
• If human experts can do it: we can do it!

• Automate the human expert’s approach

• Humans don’t memorize the nodes and properties

→ we don’t need fine-tuning! Just use In-Context Learning

## Page 32

STANFORD
LAM

How a Human Expert Write a SPARQL Query

1. Start by writing simple SPARQL queries;

2. Look up Wikidata entity or property pages when needed

• To understand the structure of the knowledge graph

• Check what properties exist for a node

3. Add new SPARQL clauses to build towards the final SPARQL

LLM Agent weaves together 
-
Knowledge inquiry
-
Query writing
-
Execution and evaluation of results (subgraph retrieval)

## Page 33

STANFORD
LAM

SPINACH: An Agentic Approach

User Query

Agent

thinks
Issues actions

Observes

results

Agent response

ReAct: Synergizing Reasoning and Acting in Language Models, Yao et al, ICLR 2023

The same think–act–observe loop
powers coding agents such as
Claude Code and Codex.

## Page 34

STANFORD
LAM

Actions Useful for Writing SPARQL

Provided by Wikidata

search_wikidata(string):         http://wikidata.org (search bar): 
  
 
 
 
 
 
 
 
 
 
text → returns QIDs and PIDs

get_wikidata_entry(QID): 
  https://www.wikidata.org/wiki/QID:<QID>
  
 
 
 
 
 
 
 
 
 
QID → Wikidata page for entity

get_property_examples(PID): https://www.wikidata.org/wiki/Property:<PID>:

PID → examples of how property PID is used

execute_sparql(SPARQL):       https://query.wikidata.org:
  
 
 
 
 
 
 
 
 
 
 SPARQL → result

### Page links

- [Link 1](http://wikidata.org/)
- [Link 2](https://query.wikidata.org/)
- [Link 3](https://www.wikidata.org/wiki/Property:PID)
- [Link 4](https://www.wikidata.org/wiki/QID)

## Page 35

STANFORD
LAM

Running Example

## Page 36

STANFORD
LAM

search_wikidata("musical instrument")

This step performs Named Entity Disambiguation (NED) with LLM!

Action: search_wikidata

## Page 37

STANFORD
LAM

search_wikidata("affiliation")

Action: search_wikidata

## Page 38

STANFORD
LAM

Action: get_wikidata_entry

get_wikidata_entry 
("Q98035717")

## Page 39

STANFORD
LAM

Action: get_property_examples

get_property_examples("P1416")

Affiliation (P1416)

Raoul Bott -> Institute for Advanced Study
Hannah Sipe -> University of Washington School
of Environmental and Forest Sciences

## Page 40

STANFORD
LAM

Action: execute_sparql

## Page 41

STANFORD
LAM

The SPINACH Agent

•
Imitates what the user does with an agentic approach

•
Uses the full expressiveness of SPARQL for exploration

•
For N steps:
•
Given the history of agent actions,

•
Prompt LLM to generate a thought and an action

•
Execute an action against the KG

•
Add an observation to the history

Main agent code available in this file,
implemented with LangGraph (part of LangChain) in Python

### Page links

- [Link 1](https://github.com/stanford-oval/spinach/blob/main/spinach_agent/part_to_whole_parser.py)

## Page 42

STANFORD
LAM

Zero-Shot LLM Policy Prompt

# instruction

Your task is to write a Wikidata SPARQL query to answer the given question. Follow a step-by-step process:

1. Start by constructing very simple fragments of the SPARQL query.

2. Execute each fragment to verify its correctness. Adjust as needed based on your observations.

3. Confirm all your assumptions about the structure of Wikidata before proceeding.

4. Gradually build the complete SPARQL query by adding one piece at a time.

5. Do NOT repeat the same action, as the results will be the same.

6. The question is guaranteed to have an answer in Wikidata, so continue until you find it.

7. If the user is asking a True/False question with only one answer, use ASK WHERE to fetch a True/False answer at the very end.

8. In the final SPARQL projections, do not only ask for labels. 
    Ask for the actual entities whenever needed (e.g. instead of doing \`SELECT xLabel\`, do \`SELECT x\`).

9. If the final result was contained in last round's \`get_wikidata_entry\` and you are ready to stop, 
    use \`execute_sparql\` and generate a SPARQL to retrieve that results.

Form exactly one "Thought" and perform exactly one "Action", then wait for the "Observation".

Possible actions are:

- get_wikidata_entry(QID): Retrieves all outgoing edges (linked entities, properties, and qualifrs) of a specified Wikidata entity using its QID.

- search_wikidata(string): Searches Wikidata for entities or properties matching the given string.

- get_property_examples(PID): Provides a few examples demonstrating the use of the specified property (PID) in Wikidata.

- execute_sparql(SPARQL): Runs a SPARQL query on Wikidata and returns a truncated result set for brevity.

- stop(): Marks the last executed SPARQL query as the final answer and ends the process.

### Page links

- [Link 1](https://github.com/stanford-oval/spinach/blob/main/spinach_agent/prompts/controller.prompt)

## Page 43

STANFORD
LAM

# input
{% for i in range(0, conversation_history|length) %}
User Question: {{ conversation_history\[i\]\["question"\] }}
{% for j in range(0, conversation_history\[i\]\["action_history"\]|length) %}
{{ conversation_history\[i\]\["action_history"\]\[j\] }}
{% endfor %}
--
{% endfor %}

User Question: {{ question }}

{% if action_history %}
{% for i in range(0, action_history|length) %}

{{ action_history\[i\] }}
{% endfor %}
{% endif %}

Output one "Thought" and one "Action":

Templates written in jinja syntax

### Page links

- [Link 1](https://jinja.palletsprojects.com/en/3.1.x/)

## Page 44

STANFORD
LAM

Problem: Looping

•
SPINACH needs to explore different queries during iteration

• Run policy prompt with temperature 1.0

•
LLM can fall into a loop of executing the same action

execute_sparql(“SELECT ?x WHERE {wd:Q1 wdt:P1 ?x.}”)

Did not find any results

execute_sparql(“SELECT ?x WHERE {wd:Q1 wdt:P1 ?x.}”)

Did not find any results

execute_sparql(“SELECT ?x WHERE {wd:Q1 wdt:P1 ?x.}”)

…

Quiz: Why would this happen?

Quiz: How to solve this?

## Page 45

STANFORD
LAM

Solution: Detecting & Stopping Loops

•
If repeated actions are found,

• Agent resets exploration state to the one before the repetition

• Continues from there

•
We cap number of actions by either:

• 15 actions after taking “rollbacks” into account

• a total of 30 actions including “rollbacks”

## Page 46

STANFORD
LAM

The SPINACH Agent in Action (1)

## Page 47

STANFORD
LAM

The SPINACH Agent in Action (2)

## Page 48

STANFORD
LAM

The SPINACH Agent in Action (3)

## Page 49

STANFORD
LAM

P1303: instrument
P1416: affiliation
P69:     educated at

Q98035717: 
University of Washington 
School of Music

Q219563: 
University of Washington

## Page 50

STANFORD
LAM

Outline

•
Data Structures: Graphs and Tables

•
Graph QA with SPINACH
•
Challenges and Prior Approaches

•
The Agentic Approach

•
Dataset and Evaluation

•
SQL QA with DataTalk

•
Guest Lecture: Big Local News on DataTalk (15 min)

## Page 51

STANFORD
LAM

KBQA Data Sets (Crowdsourcing)

•
Datasets with natural questions originally collected through 
search engines or crowdsourcing

•
WebQuestionSP (Yih et al., 2016)

•
QALD datasets (Usbeck et al., 2017, 2018, 2023; Perevalov et al., 2022)

•
RuBQ (Korablinov and Braslavski, 2020)

•
SimpleQuestions (Bordes et al., 2015)

Simple Queries

 Quiz: Is this OK?

## Page 52

STANFORD
LAM

KBQA Data Sets (Synthesized)

•
Datasets with synthetically generated logical forms & questions

•
ComplexWebQuestions (Talmor and Berant, 2018)
•
GrailQA (Gu et al., 2021)
•
KQA Pro (Cao et al., 2022a)
•
CFQ (Keysers et al., 2020)
•
CWQ (Talmor and Berant, 2018)
•
LC-QuAD2 (Dubey et al., 2019)

Limited NL variety
& Unique query patterns

## Page 53

STANFORD
LAM

Wikidata SPARQL 
Forum

https://m.wikidata.org/wiki/Wikidata:Request_a_query

Initial Question

Response with

SPARQL

Refined SPARQL

Acknowledgement

•
To help Wikidata users write 
SPARQL queries

•
People exchange 
conversations on how to 
write SPARQLs

•
The queries are real, 
but difficult

### Page links

- [Link 1](https://m.wikidata.org/wiki/Wikidata:Request_a_query)

## Page 54

STANFORD
LAM

The SPINACH Dataset

From discussions on Wikidata Request Query forum (July 2016 – May 2024)

•
From the natural (real) SPARQL, we annotate its corresponding English question

•
Disambiguate entities and properties
•
Natural verbalizations
•
Accurately capturing optional clauses and projections

•
We removed these categories of clauses:

•
Wikimedia presentation queries
•
Questions on complex SPARQL code
•
Queries obscured by optimizations
•
Formatting clauses

•
155 validation examples and 165 test examples

Quiz: These numbers seem small.

Are they enough?

## Page 55

STANFORD
LAM

SPINACH dataset: 
natural questions + complex logical forms

SPINACH dataset: natural questions + complex logical forms

## Page 56

STANFORD
LAM

Results on the SPINACH Dataset

Fine-tuned LLMs Know More, Hallucinate Less with Few-Shot Sequence-to-Sequence Semantic Parsing over Wikidata, Xu et al, EMNLP 2023
Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph, Sun et al, ICLR 2023

Fine-tuned model ->
SOTA. Ask LLM to walk the graph ->

SPINACH agent achieves considerable gain over prior approaches!

See calculation of F1 for tables in the Appendix of this lecture

## Page 57

STANFORD
LAM

Results on Other Datasets

Zero-shot ICL (in-context learning) achieves new SOTA on QALD Wikidata datasets

Comes within 1.6 F1 on WikiWebQuestions to WikiSP, fine-tuned on WikiWebQuestions

## Page 58

STANFORD
LAM

The Importance of Agent Actions

All actions make meaningful contribution to the agent performance

## Page 59

STANFORD
LAM

Live Demo:

https://spinach.genie.stanford.edu/

Code:

https://github.com/stanford-oval/spinach

As a bot on Wikidata:

https://www.wikidata.org/wiki/User:SpinachBot

### Page links

- [Link 1](https://github.com/stanford-oval/spinach)
- [Link 2](https://spinach.genie.stanford.edu/)
- [Link 3](https://www.wikidata.org/wiki/User:SpinachBot)

## Page 60

STANFORD
LAM

Error Analysis

40%: Property-related problems: 
         Fails to fetch the correct property or incorrectly uses a property

30%: Complicated SPARQL: 
         Fails to write complex SPARQL to fetch results.

15%: Not enough exploration: 
         Insufficient exploration within limit of actions allowed.

10%: Inaccurate semantic parsing: 
         LLM injecting an extra clause.

5%: Formatting issues

## Page 61

STANFORD
LAM

SPINACH Deployed on Wikidata Forum

•
22,000+ conversations in the wild: all real and hard queries!

•
198 randomly selected conversations

•
Success rate: 78% (154 cases)

•
Failures: 22% (44 cases)

•
50% (22 cases) similar to queries in the dataset

•
50% (22 cases) are not similar:
underspecified queries, query correction/modification, 
string manipulation

https://m.wikidata.org/wiki/Wikidata:Request_a_query

A higher success rate in practice!

### Page links

- [Link 1](https://m.wikidata.org/wiki/Wikidata:Request_a_query)

## Page 62

STANFORD
LAM

Outline

•
Data Structures: Graphs and Tables

•
Graph QA with SPINACH
•
Challenges and Prior Approaches

•
The Agentic Approach

•
Dataset and Evaluation

•
SQL QA with DataTalk

•
Guest Lecture: Big Local News on DataTalk (15 min)

## Page 63

STANFORD
LAM

From SPINACH to DataTalk

•
SPINACH: question answering over a knowledge graph
• Find entities and properties; build and execute SPARQL

•
DataTalk: question answering over relational tables
• Find tables, columns and join keys; build and execute SQL

•
The same agentic loop
• Inspect the data, write a query, execute, observe and 
revise

## Page 64

STANFORD
LAM

From SPARQL Actions to SQL Actions

User Query

Agent

Graph Knowledge Base actions:

SPINACH agent

Relational Database actions:

DataTalk agent

Agent response

thinks
Issues actions

Observes

results
get_tables()
retrieve_tables_details(\[table1, table2, …\])
execute_SQL(SQLquery)
entity_linking(search_str, \[column1, column2, …\])
location_linking(search_str)
stop()

search_wikidata(string)
get_wikidata_entry(QID)
get_property_examples(PID)
execute_sparql(SPARQL)
stop()

## Page 65

STANFORD
LAM

The DataTalk Agent – Expert Instructions

execute_sql(

)

•
When using \`pac_and_party_summary_2023_2024\` about money raised, 
exclude committees whose IDs start with C9 because C9 committees 
are mostly only useful when analyzing expenditures. Apperance of 
them here likely correspond to errenous filings.
•
When using \`pac_and_party_summary_2023_2024\`, include 
\"CMTE_FILING_FREQ\" and \"CVG_END_DT\" columns to qualify results.
•
…

Also Shows specific instructions related 
to a SQL after the agent calls 
“execute_sql” in Observation

NEW!

## Page 66

Guest Lecture

DataTalk & Role of Expert Knowledge

Big Local News

15 minutes

## Page 67

Appendix

Calculating F1 for Tables

## Page 68

STANFORD
LAM

The F1 metric

TP: True Positive
FP: False Positive
FN: False Negative

## Page 69

STANFORD
LAM

But: traditional EM & F1does not work

what are the top 3 counties with most people in

South Dakota?

Minnehaha

County

206,930

Pennington

County

115,903

Lincoln County
73,238

Predicted
Gold

Minnehaha

County

Pennington

County

Lincoln County

Question: Do we want to penalize this column?

## Page 70

STANFORD
LAM

New Metric: row-major EM & F1
1. Assignment of rows

Q5994
piano
99

Q8350
trombone
11

Q8338
trumpet
8

Predicted
Gold

Q8350
11

Q5994
99

Q1467690
2

Q83509
1

Assigned

rows

Step 1: Run an assignment algorithm to maximize total overlap (recall)

Without penalizing extra columns in prediction

𝑦𝑖 a row in gold

𝑦′𝑖 assigned row of 𝑦𝑖 in prediction

Matching rows with 0 recall is not allowed

## Page 71

STANFORD
LAM

New Metric: row-major EM & F1
2. True positives

Q5994
piano
99

Q8350
trombone
11

Q8338
trumpet
8

Predicted
Gold

Q8350
11

Q5994
99

Q1467690
2

Q83509
1

Assigned

rows

Step 2: Calculate true positives as sum of recalls in assigned rows

= 2

## Page 72

STANFORD
LAM

New Metric: row-major EM & F1
3. false positives

Q5994
piano
99

Q8350
trombone
11

Q8338
trumpet
8

Predicted
Gold

Q8350
11

Q5994
99

Q1467690
2

Q83509
1

Assigned

rows

False 
Positives

= 1

Step 3: Each unassigned row in prediction counts as a false positive

𝑛′: number of rows in prediction

𝑟: number of rows in matching

## Page 73

STANFORD
LAM

New Metric: row-major EM & F1
4. false negatives

Q5994
piano
99

Q8350
trombone
11

Q8338
trumpet
8

Predicted
Gold

Q8350
11

Q5994
99

Q1467690
2

Q83509
1

Assigned

rows

= 2

False 
Negatives

False 
Positives

Step 4: Each unassigned row in gold counts as a false negative

plus sum of 1– recall in the matching (0 in this case)

𝑛: number of rows in gold

𝑟: number of rows in matching

## Page 74

STANFORD
LAM

New Metric: row-major EM & F1
5. F1

Q5994
piano
99

Q8350
trombone
11

Q8338
trumpet
8

Predicted
Gold

Q8350
11

Q5994
99

Q1467690
2

Q83509
1

Assigned

rows

False 
Negatives

False 
Positives

Step 5: Calculate F1 with the usual formula

𝐹1 =

2𝑡𝑝
2𝑡𝑝+𝑓𝑛+𝑓𝑝 = 0.66
