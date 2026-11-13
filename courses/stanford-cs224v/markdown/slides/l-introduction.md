# Introduction

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-introduction.pdf) · [Raw file](../../raw/slides/l-introduction.pdf)

Retrieved: 2026-11-13T16:49:46.510941+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS224v

Agentic AI

Lecture 1: Introduction

1

Monica Lam

## Page 2

STANFORD
LAM

Conversational

Q&A
Direct chat with multi-
turn context retention

across a session

RAG & Retrieval

Grounding answers in 
external docs and live

web search, with

citations

Function Calling

The model decides 
when to call an API, 
database, or external

tool

Agentic 
Workflows
Multi-step planning,

tool use, and self-
correction with less

supervision

Computer Use

Operating a GUI 
directly — clicking, 
typing, navigating on

a user's behalf

Code Execution

Running and iterating

on code in a live 
sandbox, not just

generating text

Extended 
Reasoning
Step-by-step chain-of-

thought for math, 
logic, and complex

problem solving

Multimodal I/O

Understanding and 
generating images,

audio, and video

alongside text

Core User-Facing Capabilities of LLMs

## Page 3

T O D A Y’ S A I  A G E N T S A R E N O T D E PL O YE D I N H I G H- S T A KE S S E R VI C E S

( M E D I C I N E,  S C I E N CE ,  F I N A N C E,  L A W)

F UN D A M E N T A L T E C H N I QU E S T O I M P RO VE :

A C C U R A C Y,  A C C O U N T A B I L I T Y,  L O N G H O R I Z O N,  L O N G C O N T E X T

I M P A C T

A F F O R DA B L E H I G H- S T A KE S S E R VI C E S

K N O W L E DG E D I S C O VE R Y A C C E L E R A TI O N

## Page 4

STANFORD
LAM

Date
Incident
Why it matters
Citation

May 
2023
Mata v. Avianca
ChatGPT-assisted legal filing included fake 
cases and citations; court imposed sanctions.
NYT, 5/27/2023

Dec 
2023

Michael Cohen 
filing

AI-generated fabricated legal citations 
appeared in a high-profile legal matter.

Reuters, 
12/29/2023

Dec 
2023

Chief Justice 
Roberts report

Chief Justice Roberts urged caution when 
using AI in legal contexts.

U.S. Supreme 
Court,12/31/2023

Jan 
2024

Stanford legal 
hallucination study

Found 69%–88% hallucination rates on legal 
tasks across GPT-3.5, PaLM 2, and Llama 2.

Dan Ho, Stanford 
arXiv, 1/11/2024

Feb 
2024

Moffatt v. 
Air Canada.

Company held responsible after chatbot 
gave incorrect fare/refund guidance.

The Guardian
2/16/2024

Feb 
2024

Colorado sanctions 
case

Lawyers sanctioned for AI-generated filings 
with fake court citations.

Reuters, 
2/22/2024

LLM Hallucinations

## Page 5

H ALLUCINATION IS S TILL R AMPANT WITH RAG

T ODAY

## Page 6

STANFORD
LAM

NYT, April 7, 2026

SCALED CONSUMER
PRODUCTS

Estimated Hallucination Rate:

10%

## Page 7

JOURNALISM
Perplexity, Gemini, Copilot, ChatGPT Hallucinate With RAG

51% of AI answers to news problems

have significant issues.

19% of AI answers which cited BBC

content introduced factual errors.

13% of the quotes sourced from BBC

articles were either altered or 
didn’t actually exist in that article.

BBC, Feb 11, 2025

https://www.bbc.com/mediacentre/2025/bbc-research-shows-issues-with-answers-from-artificial-intelligence-assistants

## Page 8

STANFORD
LAM

LEGAL

Journal of Legal Analysis, Volume 16, Issue 1, 2024, Pages 64–93, https://doi.org/10.1093/jla/laae003

The content of this slide may be subject to copyright: please see the slide notes for details.

Stanford, June 26, 2024

### Page links

- [Link 1](https://doi.org/10.1093/jla/laae003)

## Page 9

STANFORD
LAM

https://www.nature.com/articles/d41586-026-00969-z

SCIENCE

## Page 10

STANFORD
LAM

MEDICINE

https://www.nbcnews.com/tech/tech-news/openevidence-ai-doctor-
medical-physician-login-app-what-npi-uptodate-rcna341064

NBC News

May 13, 2026

Sept 2026

MedXPertQA: 
Expert-Level Specialty Board Questions

Accuracy: 72.8%

## Page 11

STANFORD
LAM

FINANCE: AI Hallucination not Publicized

An enterprise: 
“The bot says ‘the investment is made’ but it was not.”

A large consulting firm: 
“Evaluation shows many hallucinations in an enterprise chatbot”

A popular chatbot vendor: 
“Does not sell bots for high-stakes applications.”

A large enterprise infrastructure vendor: 
“No enterprises deployed AI in high-stakes applications.”

## Page 12

STANFORD
LAM

0%

20%

40%

60%

80%

100%

0
10
20
30
40
50
60
70
80
90
100

Accuracy

Time to Build

70% 
Direct
Application

85%
With Professional

Support

95%
Research

High-Stakes LLM Agents are Hard to Build!

My Rule of Thumb

The Last 10% is 90% of the problem.
IMPORTANT:

## Page 13

STANFORD
LAM

LLM Weaknesses 
from Next-Word Prediction Training

Out-of-Distribution Tasks

• New information

• Long-tail information

• Long instructions

• Long documents

• Long horizon

• Long contexts

RAG (Retrieval Augmented Generation)

Context management
e.g. automatic compression

## Page 14

F O CU S O F CS 2 2 4 V

T O D A Y’ S A I  A G E N T S A R E N O T D E PL O YE D I N H I G H- S T A KE S A P PS

( M E D I C I N E,  S C I E N CE ,  F I N A N C E,  L A W)

F UN D A M E N T A L T E C H N I QU E S T O I M P RO VE :

A C C U R A C Y,  A C C O U N T A B I L I T Y,  L O N G H O R I Z O N,  L O N G C O N T E X T

I M P A C T

A F F O R DA B L E H I G H- S T A KE S S E R VI C E S

K N O W L E DG E D I S C O VE R Y A C C E L E R A TI O N

## Page 15

STANFORD
LAM

Outline of This Lecture

1. Problem: LLM Hallucination in High-Stakes Applications

2. Basic concept: Decompose problems into reliable LLM tasks

3. Course information

4. Course syllabus preview

Stanford A-OS Agentic Operating System

• Long-Horizon, Long-Context Custom-Facing Agents

• Long-Horizon, Long-Context Researcher for Science

• Accountable Decision Making

## Page 16

STANFORD
LAM

Outline of This Lecture

1. Problem: LLM Hallucination in High-Stakes Applications

2. Basic concept: Decompose problems into reliable LLM tasks

3. Course information

4. Course syllabus preview

Stanford A-OS Agentic Operating System

• Long-Horizon, Long-Context Custom-Facing Agents

• Long-Horizon, Long-Context Researcher for Science

• Accountable Decision Making

## Page 17

W HY IS T HERE H ALLUCINATION WITH RAG

1. R ETRIEVAL D OES NOT R ETURN THE A NSWER

2. LLM S S UPPLY THE A NSWER FROM M EMORY

## Page 18

STANFORD
LAM

• Conversational Q&A in open domain with 97% accuracy

• Winner of the Wikimedia’s Research of the Year Award, 2024

• In Proceedings of Association for Computational Linguistics: 
EMNLP, Singapore, December 2023.

## Page 19

STANFORD
LAM

WikiChat (7 Prompts)

1.
Formulate query from input
•
Retrieve documents
2.
Filter each retrieved doc

3.
Ask GPT to generate answer

4.
Extract claims

5.
Fact-check/remove each claim

•
Retrieve documents

6.
Draft
7.
Refine

Traditional (Factuality)

LLM (Conversationality + Factuality)

# LLM calls: 5 + n + c
n: # documents retrieved based on user queries
   c: # claims generated

## Page 20

T HE PROBLEM IS H ARDER THAN E XPECTED

3 STUDENTS, 4 MONTHS

T HE D EVIL IS I N THE D ETAILS

R EQUIRES N EW E VALUATION T ECHNOLOGY

D ECOMPOSE P ROBLEMS INTO R ELIABLE LLM T ASK

S PEED CAN BE R EGAINED VIA D ISTILLATION

A  K E Y B UI L D I N G B L OC K - - P UB L I CL Y A VA I L A B LE  A S O P E N S O UR CE

## Page 21

STANFORD
LAM

Simulated Dialogues: WikiChat-GPT4

94.9

56

47.5

66.1

98.8
94.6
98.5
97.3

0

20

40

60

80

100

Head
Tail
Recent
All

Factuality

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA

Semnani, Sina et al. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia, EMNLP Findings 2023

## Page 22

STANFORD
LAM

Simulated Dialogues: WikiChat-GPT3.5

94.9

56

47.5

66.1

98.8
94.6
98.5
97.3
97.1

82.2

88.2
89.2

0

20

40

60

80

100

Head
Tail
Recent
All

Factuality

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA

Semnani, Sina et al. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia, EMNLP Findings 2023

## Page 23

STANFORD
LAM

94.9

56

47.5

66.1

98.8
94.6
98.5
97.3
97.1

82.2

88.2
89.2
95.2

87.1
90.9
91.1

0

20

40

60

80

100

Head
Tail
Recent
All

Factuality

GPT-4
WikiChat-GPT4
WikiChat-GPT3.5
WikiChat-LLaMA

Simulated Dialogues: WikiChat-LLaMA

Semnani, Sina et al. WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia, EMNLP Findings 2023

(Distilled)

## Page 24

STANFORD
LAM

Real User Evaluation

• Real user evaluation was seldom performed before LLM
because of poor accuracy

• Most important metric!

User study: User reads the first sentence of a new Wikipedia page

Model
User Rating (out of 5)
Factuality

GPT-4
3.4
42.9%

WikiChat using GPT-4
3.8
97.9%

GPT-4: Users are not even aware that over half of the statements are false

## Page 25

F UTURE LLM M ODELS W ILL S TILL H ALLUCINATE

A H IGHER R ATE FOR H ARDER Q UESTIONS

1. D O N OT T RUST D EMOS

2. U NDERSTAND THE U NDERLYING T ECHNOLOGY

3. E VALUATE S YSTEMATICALLY

## Page 26

STANFORD
LAM

Outline of This Lecture

1. Problem: LLM Hallucination in High-Stakes Applications

2. Basic concept: Decompose problems into reliable LLM tasks

3. Course Information

4. Course syllabus preview

Stanford A-OS Agentic Operating System

• Long-Horizon, Long-Context Custom-Facing Agents

• Long-Horizon, Long-Context Researcher for Science

• Accountable Decision Making

## Page 27

STANFORD
LAM

History of this Course

•
Actively create and advance new technologies
Adopted by real Users

•
Course publications: 2023(2), 2024(5), 2025(6), 2026(3)

•
Each CS224V class builds on previous year’s research

•
Promising class projects continue as research in 2026-2027

•
Results used in next year’s CS224V!

Secret to Success 
Working software supports increasingly complex research

## Page 28

Live Demos: wwknowledge.org

### Page links

- [Link 1](http://https/wwknowledge.org)

## Page 29

STANFORD
LAM

Course Objectives

Prepare you to push the limits of agentic AI

2 Assignments in 2 weeks: To prepare you for your project

Lectures:

1. Core techniques to build reliable agents

2. Advanced techniques to push the limit of LLMs

Hands-on quarter-long projects on topics of your choice

1. Create or improve general tools

2. Use any tools on any applications

## Page 30

STANFORD
LAM

Purpose of the Assignments

Goal: Prepare you for your project proposal

• Hands-on experience with state-of-the-art tools

• An example of a compelling, challenging, yet doable project

Hopefully it will help you propose more exciting projects!

## Page 31

STANFORD
LAM

Homework: Rare Diseases

• In partnership with Rare Genomics Institute
(A winner of the Anthropic's Rare Disease AI Grant Program)

• About 400 million people live with one of more than 7,000 
rare diseases

• Topics covered by the homeworks:

• Deep research on rare diseases

• Extraction of diagnosis information

• Diagnosis of rare diseases in real patient records

Success of such projects will have a huge impact on society

### Page links

- [Link 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC11881545/)

## Page 32

STANFORD
LAM

Project Apprenticeship

• Assistance with project selection: Hardest part in research!

• We have about 20 suggested projects on the website

• Student-initiated projects are also welcome

• Weekly group mentorship meeting

• We want to make you succeed!

## Page 33

STANFORD
LAM

Project Mentorship

All homeworks and projects are to be done in pairs

•
Week 4: Project proposal, with a weekly plan

•
Weeks 5-10 (excluding Thanksgiving break):

•
Submit a written weekend update (every Monday)

•
Group meeting with mentors during the week

•
Week 11: Poster presentation (Dec 2)

•
Final project report due Dec 8, 2026.

## Page 34

STANFORD
LAM

This Course

Grade

Participation
15%

Assignment
25%

Final Project
60%

Participation includes

• Class attendance and participation

• Ed discussion

• Meetings with project mentors

## Page 35

STANFORD
LAM

Outline of This Lecture

1. Problem: LLM Hallucination in High-Stakes Applications

2. Basic concept: Decompose problems into reliable LLM tasks

3. Course Information

4. Course syllabus preview

Stanford A-OS Agentic Operating System

• Long-Horizon, Long-Context Custom-Facing Agents

• Long-Horizon, Long-Context Researcher for Science

• Accountable Decision Making

## Page 36

SEMANTIC FILE SYSTEM

SEMANTIC

RETRIEVAL

KNOWLEDGE

CURATION

Text, Tables, PDFs, Images, Handwriting,

Historical Languages (CHURRO)

QA 
(Wikichat)

Constraint-Satisfaction

Based DB

(SatIR)

DBs Extracted from

Long Documents

(SLIDERS)

Meta KG
DATA SOURCES
Text

Databases

Knowledge graphs

INGESTION

Interactive 
Researcher 
(STORM, Co-STORM)

Systematic Reviews

& Insight Discovery
(DataTalk, DataStorm, GRILL)

APP PLATFORMS

Interactive Agent
(GENIE Worksheet)

Constraint-based

Decision Making

(VERDICT)

TEAMS

Collaboration UI

Workspace Mgmt
USER CONSOLE

SUQL Text/DB
Query Language

Stanford AGENTIC OS (A-OS)

Embeddings

## Page 37

STANFORD
LAM

Basic Knowledge Access

Topic
Key Ideas
Significance

Transcribing 
historical texts:

CHURRO VLM

2025

Fine-tune on manuscripts & prints 
(22 centuries, 45 languages)

vs. Gemini-Pro:
    15.5x cheaper, 
     similar accuracy
history.genie.Stanford.edu

1-Pager Research

Storm/Co-Storm

2024

Search-read-search loop. 
Interactive exploration into the 
Unknown-Unknowns.

1st deep researcher
1 Million organic users
storm.genie.Stanford.edu

Accessing Texts,

Databases, 
Knowledge graphs

SUQL

2024

Structured/Unstructured Query Lang
for hybrid DB + text. 
1st use of agentic workflow for KGs.

Deployed in practice: 
DataTalk for journalists
Wikidata agent
datatalk.biglocalnews.org
Spinach Wikidata bot

### Page links

- [Link 1](http://history.genie.stanford.edu/)
- [Link 2](http://storm.genie.stanford.edu/)
- [Link 3](https://datatalk.biglocalnews.org/)
- [Link 4](https://spinach.genie.stanford.edu/)

## Page 38

STANFORD
LAM

References

•
CHURRO: Making History Readable with an Open-Weight Large Vision-Language Model for High-
Accuracy, Low-Cost Historical Text Recognition 
Sina J. Semnani, Han Zhang, Xinyan He, Merve Tekgürler, Monica S. Lam
In The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP) , Suzhou, 
China, 2025.

•
Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models 
Yijia Shao, Yucheng Jiang, Theodore A. Kanell, Peter Xu, Omar Khattab, Monica S. Lam
In Proceedings of the North American Chapter of Association for Computational Linguistics 
(NAACL) , Mexico City, Mexico, June

•
Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model 
Agent Conversations 
Yucheng Jiang, Yijia Shao, Dekun Ma, Sina J. Semnani, Monica S. Lam
In The 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP) , Miami, 
Florida, November 12 –16, 2024

•
SPINACH: SPARQL-Based Information Navigation for Challenging Real-World Questions 
Shicheng Liu*, Sina J. Semnani*, Harold Triedman, Jialiang Xu, Isaac Dan Zhao, Monica S. Lam
In Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP) , 
Miami, Florida,

•
SUQL: Conversational Search over Structured and Unstructured Data with Large Language Models 
Shicheng Liu, Jialiang Xu, Wesley Tjangnaka, Sina J. Semnani, Chen Jie Yu, Monica S. Lam
In Findings of the North American Chapter of Association for Computational Linguistics (NAACL) , 
Mexico City, Mexico, June 2024.

### Page links

- [Link 1](https://almond-static.stanford.edu/papers/emnlp2025_historical_ocr.pdf)
- [Link 2](../readings/arxiv-2311-09818.md)
- [Link 3](../readings/arxiv-2402-14207.md)
- [Link 4](../readings/arxiv-2407-11417.md)
- [Link 5](../readings/arxiv-2408-15232.md)

## Page 39

H IGH-S TAKES A GENTS

A CCURACY, A CCOUNTABILITY

L ONG-C ONTEXT, L ONG-H ORIZON

1. C USTOMER-F ACING A GENTS

2. R ESEARCHER FOR S CIENCE

3. D ECISION M AKING

## Page 40

STANFORD
LAM

Genie Worksheet: 
High-Stakes Customer-Facing Agents

• How to stop the agents from hallucinating?

• Key Idea: Full specifications are necessary
• Not just functions to call!

• Genie Worksheet: A Domain-Specific Language
• Specification of knowledge corpora + task workflow

• Similar to workflow on webpages
• Run-time to manage the long context

Controllable and Reliable Knowledge-Intensive and Task-Oriented Conversational Agents with Declarative GenieWorksheets 
Harshit Joshi, Shicheng Liu, James Chen, Robert Weigle, Monica S. Lam
In Proceedings of the 63rd Annual Meeting of the ACL , Vienna, Austria, 2025.

### Page links

- [Link 1](../readings/arxiv-2407-05674.md)

## Page 41

STANFORD
LAM

Real User Evaluation

GPT-4 results are not acceptable

•
Low completion rate: even 54.5% on restaurant is not good enough!

•
Course: Hallucinates non-existent courses despite using knowledge base results

0
20
40
60
80
100

Restaurants
Ticket
Submission

Course
Enrollment

Task Completion Rate

GPT-4
Genie

Restaurant Reservation:  
Real-life database from Yelp

Ticket Submission: 
A subset of Service Now

Course Enrollment: 
Multiple real-life databases of 
courses at Stanford University.

## Page 42

H IGH-S TAKES A GENTS

H IGH-R ECALL, L ONG-C ONTEXT, L ONG-H ORIZON

1. C USTOMER-F ACING A GENTS

2. R ESEARCHER FOR S CIENCE

3. A CCOUNTABLE D ECISION M AKING

## Page 43

C ONTEXTS ARE N EVER L ONG E NOUGH

A CCOUNTABILITY: 
N EEDS TO T RACK THE E VIDENCE

## Page 44

S LI DE RS : A N ALYZ I NG L A RG E S E TS O F L O NG D O CU ME N TS

S Y STE MA TI C R EV I E WS

Sets of Long

Documents

Semantic
Chunking +
Contextualized

Extraction

Schema

Question

+

Schematization

Chunk 1

Chunk 2

Chunk n

…

reconciled

table

Chunk 1

Chunk 2

Chunk n

…

raw table

Reconciliation

Dynamic
Coding Agent

SUQL Question 
(Structured & Unstructured Query Language) 
Semantic Parsing

Final 
Answer
DB
Execution

Key: Paragraph level provenance

## Page 45

A N ALYZ I NG L A RG E S E TS O F L O NG D O CU ME N TS

S Y STE MA TI C R EV I E WS

SLIDERS: Systematic Reviews via Automated Evidence Synthesis and Reconciliation 
Harshit Joshi, Priyank Shethia, Jadelynn Dao, Monica S. Lam
In Pre-print. Under Review.

### Page links

- [Link 1](../readings/arxiv-2604-22294.md)

## Page 46

STANFORD
LAM

Grill: Long-Horizon Deep Researcher

Creates hypotheses, finds supports and refutations iteratively

RNA Sequencing Research
•
“What are the gene responsible for cancer drug resistance?”
•
Our results informed the direction of the experiment design

Rare Diseases
•
“For patients with genetic alterations in the Stxbp1 gene, what 
are the different clinical phenotypes associated with the gene, 
detailing the specific variations that has impact?”
•
Researcher: “Grill is an order of magnitude better than Codex”

## Page 47

STANFORD
LAM

DataSTORM

Automatically derive insights from databases

Insights on international conflicts

DataSTORM: Deep Research on Large-Scale Databases using Exploratory Data Analysis and Data Storytelling 
Shicheng Liu, Yucheng Jiang, Sajid Farook, Camila Nicollier Sanchez, David Fernando Castro Pena, Monica S. Lam
In The 2026 Conference on Language Modeling (COLM) , San Francisco, USA, 2026.

### Page links

- [Link 1](../readings/arxiv-2604-06474.md)

## Page 48

H IGH-S TAKES A GENTS

H IGH-R ECALL, L ONG-C ONTEXT, L ONG-H ORIZON

1. C USTOMER-F ACING A GENTS

2. R ESEARCHER FOR S CIENCE

3. A CCOUNTABLE D ECISION M AKING

## Page 49

STANFORD
LAM

High-Stakes Clinical Decisions

• Clinical trial matching

• Rare disease diagnosis

• Treatment guideline conformance

## Page 50

STANFORD
LAM

Clinical Trials are critical for medical advances
80% Clinical trials fail for missing enrollment targets

500,000+
Clinical Trials
Millions of

patients

Match?

Many complex
 inclusion and exclusion

constraints

C LINICAL T RIAL M ATCHING

## Page 51

STANFORD
LAM

Previous State of the Art

•
Retrieval of eligible trials: Embedding-based retrieval

•
Low precision: returns many ineligible trials – wastes time
•
Low recall: misses potentially life-saving trials

•
LLM-based trial matching: 90% Accuracy
•
Decision may still be wrong 10% of the time
•
Clinicians do not just want a Yes/No answer
•
They need information for continued health care
•
They need accountability

## Page 52

STANFORD
LAM

Accountability for High-Stakes Decisions

•
Verified:  Verified rationale
•
LLM: the patient does not meet the eligibility criteria

•
Faithful:  Explicit assumptions
•
LLM: No clinically significant cardiovascular disease 
         satisfied by controlled hypertension

•
Consistent: Policy adherence
•
LLM: Does not adhere to given policies: 
Missing HIV status should remain unknown

•
Actionable: Pivotal conditions
•
LLM: Ineligible because ECOG > 1
But changing ECOG = 0 because of other conditions

Case-level accuracy. 
Should we trust it?

Over-ridable.
There are lots of missing data:
Has it made wrong assumptions?

Steerable and Fair. 
Ambiguity needs decision policies.
Are all patients treated equally?

Actionable.
Guarantees that decision will flip 
if actions are taken.

## Page 53

STANFORD
LAM

Core Idea

Language Understanding

(LLM)
Decision Making (Theorem Solver)

Function

Correctness

Formalization forces disclosure 
of ambiguity & missing values.

SMTs may not be 100% faithful. 
But they are interpretable.

Verifiably correct with respect to SMTs
Yes/No decision with

A proof for the derivation
Assumptions: all the residual constraints
Adherence to policies is guaranteed!
Pivotal conditions (MaxSAT)

Clinical trials
Patient records

LLM
SMT
SMT

SMT + MaxSAT

Solver
Accountable

Decision

## Page 54

STANFORD
LAM

Experimental Results (TREC 2021)

Qwen2.5-7B (with distillation)
0.830

VERDICT

## Page 55

STANFORD
LAM

Clinician Study

0
1
2
3
4
5

Actionability

Consistency

Faithfulness

Verifiability

LLM
VERDICT

Accountable AI with Grounded, Faithful, Consistent, Actionable Rationales: A Case Study in Clinical Trial Matching with VERDICT 
Zikai Zhou, Yufei Jin, Yilin Xu, Yu-Chiang Wang, Chieh-Ju Chao, Monica S. Lam
In The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP) , Budapest, Hungary, 2026.

### Page links

- [Link 1](../readings/arxiv-2609-03366.md)

## Page 56

STANFORD
LAM

Trial Retrieval

• Cost of matching patients with 
SMTs for all pairs is too high

• Project SMTs to DBs

• 0.15s/patient over 3,621 trials
0

20

40

60

80

100

BM25
TrialGPT
SatIR

TREC2022

Recall

NL
LLM
SMT Projection DB

SatIR: Scalable High-Recall Constraint-Satisfaction-Based Information Retrieval for Clinical Trials Matching 
Zikai Zhou, Yufei Jin, Yilin Xu, Yu-Chiang Wang, Chieh-Ju Chao, Monica S. Lam
In The 2026 Conference on Language Modeling (COLM) , San Francisco, USA, 2026.

### Page links

- [Link 1](../readings/arxiv-2604-08849.md)

## Page 57

SEMANTIC FILE SYSTEM

SEMANTIC

RETRIEVAL

KNOWLEDGE

CURATION

Text, Tables, PDFs, Images, Handwriting,

Historical Languages (CHURRO)

QA 
(Wikichat)

Constraint-Satisfaction

Based DB

(SatIR)

DBs Extracted from

Long Documents

(SLIDERS)

Meta KG
DATA SOURCES
Text

Databases

Knowledge graphs

INGESTION

Interactive 
Researcher 
(STORM, Co-STORM)

Systematic Reviews

& Insight Discovery
(DataTalk, DataStorm, GRILL)

APP PLATFORMS

Interactive Agent
(GENIE Worksheet)

Constraint-based

Decision Making

(VERDICT)

TEAMS

Collaboration UI

Workspace Mgmt
USER CONSOLE

SUQL Text/DB
Query Language

Stanford AGENTIC OS (A-OS)

Embeddings

## Page 58

STANFORD
LAM

Course Schedule at a Glance

Dates
Lectures / Homeworks
Projects

9/23 - 10/ 5

Introduction; 
Hallucination-free chat, researcher
2 homeworks

Research Project Ideas

10/ 7 - 10/21
Structured and unstructured data retrieval 
and query language

Student-initiated ideas
Project discussions
Project proposals

10/26 - 11/2
Agentic workflow, task-oriented agents, Deep 
researcher. 
Weekly meetings with mentor

11/ 4  - 11/11
Insight discovery, accountable decision-
making. meta-optimizations
Weekly meetings with mentor

11/16 – 11/18
VLM:Historical Transcription; Training LLMs
Weekly meetings with mentor

11/23 - 11/25
Thanksgiving

12/2
Final project posters 
(3:00-5:40)
