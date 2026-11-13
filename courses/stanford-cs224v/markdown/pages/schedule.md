# Course schedule

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/schedule.html) · [Raw file](../../raw/pages/schedule.html)

Retrieved: 2026-11-13T16:49:21.364894+00:00

# CS 224V

## Agentic AI

## Fall 2026

## Course Schedule

| Date | Topic | Description | Events | Deadlines |
| --- | --- | --- | --- | --- |
| 9/23 | [Introduction](../slides/l-introduction.md) | LLMs hallucinate. How to turn LLMs into useful, dependable agents? Concept of computational thinking. Carefully designed LLM-based algorithms for reading, writing, retrieving data; scientific research—curation, insight discovery. Accountable AI. Course design and outline. |  |  |
| 9/28 | [Knowledge Curation](../slides/i-deepresearch.md) | How to use LLMs to curate knowledge in an open domain? Research in the pre-writing stage by iteratively searching and reading from different perspectives; adding interactivity to allow personalization. System: STORM / Co-STORM | [Homework 1 out](../assignments/cs224v-2026-hw1.md) |  |
| 9/30 | Research project ideas | What are the ongoing research projects that students can participate in? AOS architecture. Knowledge retrieval, curation, discovery. Harnesses: scientific reasoning, accountable decision making, conversational management. Domain-specific agents. Harness training. |  | Student intro form due |
| 10/5 | [Accountable AI: SMT](../slides/l-smt-match.md) | Accountability means that LLMs can provide a faithful rationale that is sound and complete. High-stakes decision making such as clinical trial matching requires better recall and precision than conventional embedding-similarity based retrieval. Constraint-satisfaction-based retrieval. Formulating constraints as SMT (satisfiability modulo theories) permits the use of a theorem prover as an accountable decision maker. Systems: SatIR, VERDICT |  | Homework 1 due (Oct 6, 11:59PM) |
| 10/7 | Student project ideas | Students pitching preliminary project ideas | [Homework 2 out](../assignments/cs224v-2026-hw2.md) [Project proposal assignment out](https://forms.gle/BD8VXCCkEGKLpMwG8) |  |
| 10/12 | [Constraint Satisfaction Based Retrievers](../slides/l-satir.md) | How to create a high-recall, high-precision retriever for documents containing many constraints? The retriever needs to be scalable and should retrieve all the documents whose constraints are satisfied while introducing very few false positives. Canonicalization, logic implications, salience for data imputation. Projection from SMT to relational algebra. System: SatIR |  |  |
| 10/14 | [Constraint Satisfaction Based Retrievers](../slides/l-satir.md) + Project Proposals | Continuation of constraint satisfaction based retrievers. Groups present their proposals. |  |  |
| 10/19 | [How to RAG without hallucination](../slides/l-freetext.md) | How to create a hallucination-free conversational bot grounded on free text? RAG text retrieval; Summarization; Verifying generation; Response generation; Factuality in Persuasive Agents. Evaluation methodology. System: WikiChat |  | Homework 2 and project proposal due (Oct 18, 11:59PM) |
| 10/21 | Project Proposals | Groups present their proposals |  |  |
| 10/26 | [Introduction to ReAct Agents for Querying Knowledge Bases and Graphs](../slides/l-agentic.md) | The ability to query knowledge databases and graphs using natural language greatly improves access of non-CS professionals to large troves of data (e.g. Wikidata has 15B facts). Semantic parsing. ReAct agents. Systems: SPINACH (Wikidata), DataTalk (FEC) |  |  |
| 10/28 | [Agentic Data-Driven Research](../slides/l-data-driven-deep-research.md) | Can we use agents to assist in data-driven research, which requires extracting insights from large tables of data? Reproduction of published research is an important step in the scientific process; can an agent automatically reproduce published findings? Principles from Exploratory Data Analysis and Data Storytelling. Reframes deep research over structured data as a thesis-driven analytical process. System: DataSTORM |  |  |
| 11/2 | [Querying Hybrid (Structured and Unstructured) Data](../slides/l-new-suql.md) | How to answer questions combining structured and unstructured data? SUQL: the first query language that combines information retrieval (NL) with database queries (SQL); Language design; Evaluation methodology. |  |  |
| 11/4 | [Minimizing hallucination in task-oriented agents](../slides/l-newworksheet.md) | How to create a task-oriented agent that does not hallucinate? Genie Worksheet is the first high-level task-oriented agent specification language that lets users focus on the task to be done; low-level dialogue implementation details are left to the implementation of the language. How to scale the creation of effective and reliable agents across different domains easily? Implementation of the Genie Worksheet; formal dialogue state representation; semantic parsing; dialogue state tracking; response generation. |  |  |
| 11/9 | [VLMs for Transcription](../slides/l-churro.md) | Transcription of historical manuscripts and prints is challenging due to the use of old languages, unusual layouts, and the quality of the digitization. Data sets and fine-tuning of vision-language models to make historical documents accessible. |  |  |
| 11/11 | [Long-Context Long-Horizon Deep Researcher](../slides/i-sliders.md) | How to answer questions that require reading, analyzing, and comparing across large documents in a set? LLM contexts are never large enough. Automatic schematization, database construction, and data reconciliation. System: SLIDERS |  |  |
| 11/16 | Agent Context Management | How do we manage the context of long-horizon agents? Designs of existing harnesses; context compression; external storage; long-term memory and skills. |  |  |
| 11/18 | Behavior of LLM-based Harnesses | This lecture addresses how we should build agents in the face of many of the recent developments of frontier LLMs: Can coding agents perform general-purpose tasks? Can meta-optimizations improve custom-built agents? Can we trust the results of LLM outputs given their reward-hacking behavior? |  |  |
| 11/23, 11/25 |  | Thanksgiving Break |  |  |
| 11/30 |  | No class |  |  |
| 12/2 | Project Presentations | Groups present their final projects. |  | Final project presentation |

Past offerings: [Fall 2025](https://web.stanford.edu/class/cs224v/schedule_2025.html) · [Fall 2024](https://web.stanford.edu/class/cs224v/schedule_2024.html) · [Fall 2023](https://web.stanford.edu/class/cs224v/schedule_2023.html)
