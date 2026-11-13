# Lecture 3: Retrieval-Augmented Generation (RAG)

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf) · [Raw file](../../raw/slides/lecture03.pdf)

Retrieved: 2026-11-13T16:18:45.157272+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS 329Z:Engineering AI Agents

RAG + Agents

Diyi Yang

## Page 2

Announcements

• Waitlist and Audit

• Compute (see Canvas/email)

• Office hours (hybrid: half Zoom; half in-person)

• Homework 1 will be released on Oct 5

• Project proposal due on Oct 9

2

## Page 3

Lecture Overview

●Project (5 mins)
●Why RAG (5 mins)
●The RAG pipeline (10 mins)
●Indexing: chunking, contextual retrieval (15 mins)
●Retrieval: BM25, DPR, ColBERT (20 mins)
●Agentic RAG: Self-RAG, Search-R1 (10 mins)
●Failure modes (15 mins)

3

## Page 4

Pick A Topic that You’re Excited About

• What task does your agent do?

• What research question drives it?

• What data or APIs does it need?

• Which frameworks will you use?

• How will you evaluate it?

4

## Page 5

Pick A Topic that You’re Excited About

• Goal: design, build, and evaluate an agentic system of your own

• Focus: building agents (retrieval, tool use, memory, multi-agent systems, 
optimization), the data agents need, or evaluating and making agents safe.

• Rigorous evaluation:
• A demo that works once will not score highly
• Define early: tasks, where the data comes from, what counts as success
• Measure: code graders, LLM-as-judge, human ratings, or a mix
• Report: many tasks, baselines, and where and why the agent fails

5

## Page 6

Example Topics for CS329Z Course Projects

Research topics

Evaluating agents on cost, latency, and safety

Adapting to new tools, APIs, or UIs

Robustness to prompt injection and tool errors

Why agents misuse tools

Learning tool use from little data

Interpreting agent behaviors

Long-tail and long-horizon edge cases

Human-agent/agent-agent teaming

Multi-agent systems, memory, planning, 
oversight, reward hacking

6

Example ideas

Syllabus reader that puts deadlines on your calendar

Course-schedule optimizer for next quarter

Research-paper discovery and summarization agent

Campus-event aggregator and recommender

Coding agent specialized for one codebase, 
framework, or language

Rigorous evaluation of an existing agent that 
surfaces its failure modes

## Page 7

Project Team and Key Considerations

• Recommend 1-3 people

• Clearly divide the work among team members

• Reach out to us if you need anything

• Feel free to talk to your neighbors or use Ed Discussion

• Consider the availability of data, agentic frameworks, computation, 
and evaluation

• Example project ideas are coming later this week

7

## Page 8

Recommendations for Successful Projects

• Start early and work on it every week rather than rushing at the end

• Get your data first!

• Have a clear, well-defined research question (creative ones ++)

• Results should teach us something

• Present and visualize results well

• Come to office hours and talk to us!

8

## Page 9

Lecture Overview

●Project (5 mins)
●Why RAG (5 mins)
●The RAG pipeline (10 mins)
●Indexing: chunking, contextual retrieval (15 mins)
●Retrieval: BM25, DPR, ColBERT (20 mins)
●Agentic RAG: Self-RAG, Search-R1 (10 mins)
●Failure modes (15 mins)

Learning Objective: learn how the RAG pipeline is built and where it 
breaks, what to index, and how to search it

9

## Page 10

Why Retrieval?

“Which office hour this week is least crowded?”

10

LLMs Alone

“Try the Wednesday 
afternoon session -  
midweek hours are 
usually quietest.”

LLMs + Retrieval

Retrieved: “Queue log, last 3 weeks — 
Tue 4pm: 14 waiting avg; Thu 9am: 3.”
“Thursday 9am — about 3 
students ahead of you.”

## Page 11

Using Retrieval to Overcome LMs’ Shortcomings

• Instead of asking the LM to memorize everything, can we provide the 
LM with relevant and useful content just-in-time?
• Retrieval is a common mechanism for identifying such relevant 
information.

• Dynamic: it’s easy to update / add documents to your retrieval system
• Interpretable: LM can generate pointers to retrieved documents that support 
human verification of its generations (citations)

## Page 12

Retrieval Often Used in Open-Domain QA

Document
Reader
Document 
Retriever

833,500

https://github.com/facebookresearch/DrQA

Chen et al., 2017. Reading Wikipedia to Answer Open-domain Questions

How many of Warsaw's inhabitants

spoke Polish in 1933?

## Page 13

Retriever-Reader Framework

Input: a large collection of documents 𝒟= 𝐷1, 𝐷2, … , 𝐷𝑁 and 𝑄

Output: an answer string 𝐴

A reading comprehension problem!
K is pre-defined (e.g., 100)
Retriever: 𝑓(𝒟, 𝑄) ⟶𝑃1, … , 𝑃𝐾
Reader:    𝑔(𝑄, {𝑃1, … , 𝑃𝐾}) ⟶𝐴

Retriever = A standard TF-IDF information-retrieval sparse model (a fixed module)

Reader = a neural reading comprehension model
• Could be trained on SQuAD and other distantly-supervised QA datasets
• Or a zero-shot LLM (ChatGPT etc)

## Page 14

Retrieval Augmented Generation (RAG)

See also works like REALM, DPR, etc..
\[Lewis et al., 2021\]

### Page links

- [Link 1](../readings/arxiv-2005-11401.md)

## Page 15

Lecture Overview

●Why RAG (5 mins)

●The RAG pipeline (10 mins)

●Indexing: chunking, contextual retrieval (15 mins)

●Retrieval: BM25, DPR, ColBERT (20 mins)

●Agentic RAG: Self-RAG, Search-R1 (10 mins)

●Failure modes (15 mins)

15

## Page 16

Deep Dive into RAG

●
A retriever 𝑝(𝑧|𝑥) that returns the top-K passages for a query 𝑥

●
A generator 𝑝(𝑦|𝑥, 𝑧) that writes the answer one token at a time, 
given the query 𝑥 and a retrieved passage 𝑧

16

Weight each passage's answer by how 
likely the retriever rates that passage

RAG-Sequence: pick one passage, generate the whole answer with it.  
RAG-Token: re-pick the passage at every token of the answer

𝑝(𝑦|𝑥) ≈
෍

𝑧∈top−𝐾

𝑝(𝑧|𝑥)𝑝(𝑦|𝑥, 𝑧)

## Page 17

Deep Dive into RAG

●
A retriever 𝑝(𝑧|𝑥) that returns the top-K passages for a query 𝑥

●
A generator 𝑝(𝑦|𝑥, 𝑧) that writes the answer one token at a time, 
given the query 𝑥 and a retrieved passage 𝑧

●
Jointly train the retriever and generator to minimize the negative 
marginal log-likelihood σ𝑗−log 𝑝(𝑦𝑗|𝑥𝑗)

17

## Page 18

Retriever: DPR

●
A retriever 𝑝(𝑧|𝑥) that returns the top-K passages for a query 𝑥

18

𝑝(𝑧|𝑥) ∝exp(𝐝(𝑧)⊤𝐪(𝑥))
𝐝(𝑧) = BERT𝑑(𝑧),
𝐪(𝑥) = BERT𝑞(𝑥)

•
top-𝑘(𝑝(· |𝑥)): the k highest-scoring passages, solved using  
Maximum Inner Product Search (MIPS)

## Page 19

Generator: BART

●
A generator 𝑝(𝑦|𝑥, 𝑧) that writes the answer one token at a time, 
given the query 𝑥 and a retrieved passage 𝑧

●
The generator can be modeled using any encoder-decoder

●
𝑥 and 𝑧 are concatenated when generating from BART

19

## Page 20

RAG Performance on Open-Domain QA

20

RAG on Natural Questions (NQ), TriviaQA

(TQA), WebQuestions (WQ) and 
CuratedTrec (CT), using Exact Match score

Human assessments for the

Jeopardy question

generation task

## Page 21

Different Variants of RAG

22

(Gao et al, 2024)

### Page links

- [Link 1](https://arxiv.org/pdf/2312.10997)

## Page 22

Lecture Overview

●Why RAG (5 mins)

●The RAG pipeline (10 mins)

●Indexing: chunking, contextual retrieval (15 mins)

●Retrieval: BM25, DPR, ColBERT (20 mins)

●Agentic RAG: Self-RAG, Search-R1 (10 mins)

●Failure modes (15 mins)

23

## Page 23

What Makes A Good Retriever? Embeddings

Type
Examples
One vector covers

Static word
word2vec, GloVe
a word type

Contextual
BERT, RoBERTa
a token in context

Passage
Sentence-BERT, DPR, E5
a chunk

Multimodal
CLIP
text or image, shared space

Graph
node2vec, GNN encoders
a node or relation

Retrieval needs both a fixed-dimension vector per chunk, and a similarity 
metric (cosine or inner product).

## Page 24

Chunking: Basic Unit in Retrieval

Fixed-size chunking:

●Segment based on size (e.g., 100–500 tokens)

○Too small: the vector has no context

○Too large: one vector averages many topics

●Overlap: 10–20%; no sentence lost at chunk boundary

Semantic chunking: segment via logical boundaries (e.g., sentences, sections)

Context-enriched chunking: carry additional metadata or summaries per chunk

AI-driven dynamic chunking: use LLMs to detect natural breakpoints

25
https://community.databricks.com/t5/technical-blog/the-ultimate-guide-to-chunking-strategies-for-rag-applications/ba-p/113089

## Page 25

Chunking: Same Text, Three Splits

26

Grading. The project milestone is due Week 6, Thursday 11:59pm. Late days may not be 
applied to the milestone. The final report is due Week 10.

Fixed-size chunking (50 tokens)

… The project milestone is 
due Week 6, Thursday

11:59pm. Late days may not be 
applied to the milestone …

Fixed-size chunking  +  overlap

… The project milestone is 
due Week 6, Thursday 11:59pm.

… due Week 6, Thursday 
11:59pm. Late days may not be 
applied …

Structure (split on headings)

Grading — Milestone: Week 6, 
Thu 11:59pm. Late days: not 
allowed on the milestone. 
Final report: Week 10.

## Page 26

Why Contextual Retrieval

27

Chunk

“The company’s revenue grew by 3% 
over the previous quarter.”

Contextualized Chunk

“From ACME Corp’s Q2 2023 SEC 
filing; Q1 2023 revenue was $314M. 
The company’s revenue grew by 3% 
over the previous quarter.”

Query: “What was the revenue growth for ACME Corp in Q2 2023?”

## Page 27

Contextual Retrieval

28
https://www.anthropic.com/engineering/contextual-retrieval

Hybrid retrieval: embeddings

catch meaning, TF-
IDF/BM25 catches exact 
terms; results are merged

## Page 28

Contextual Retrieval

29
https://www.anthropic.com/engineering/contextual-retrieval

{{WHOLE_DOCUMENT}} 
Here is the chunk we want to situate 
within the whole document 
{{CHUNK_CONTENT}} 
Please give a short succinct context to 
situate this chunk within the overall 
document for the purposes of improving 
search retrieval of the chunk. Answer 
only with the succinct context and 
nothing else.

## Page 29

Contextual Embeddings Reduced Retrieval Failure Rate

30

## Page 30

Late Chunking

• Late chunking: embed the 
whole document with a long-
context encoder; then mean-
pool the token vectors within 
each chunk’s span

• Compared to Contextual 
Retrieval: no LLM call and no 
added tokens per chunk; the 
context is carried in the vector

31

(Günther et al., 2024)

### Page links

- [Link 1](https://arxiv.org/abs/2409.04701)

## Page 31

Retrieval Results with Long Late Chunking for Different Chunk Sizes

32

## Page 32

Hierarchical/Tree-Structured Indexing: RAPTOR

33

•
For questions whose answer is spread across a document, single chunk representation can’t help

•
Build a tree, bottom up: embed chunks → cluster them → summarize each cluster with an LLM 
→ embed the summaries → repeat

•
Retrieve across levels: a detail question matches a leaf, a thematic question matches a node

(Sarthi et al., 2025)

### Page links

- [Link 1](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a2acd174940dbca361a6398a4f9df91-Paper-Conference.pdf)

## Page 33

Cinderella queries: Q1 “central theme of the story?” and Q2 “how did she find a happy ending?”

Highlighted = RAPTOR’s selection; arrows = DPR’s leaves.

RAPTOR’s context usually already contains DPR’s, directly or inside a summary.

Hierarchical/Tree-Structured Indexing: RAPTOR

## Page 34

GraphRAG: query-focused over LLM-built graph

(Edge et al., 2024)

Graph communities detected

### Page links

- [Link 1](https://arxiv.org/pdf/2404.16130)

## Page 35

GraphRAG: More Variants (Han et al., 2025)

36

### Page links

- [Link 1](https://arxiv.org/pdf/2501.00309)

## Page 36

Vector Search

•
The task: given a query vector, return the top-k of N chunk vectors

•
Exact search: brute-force scan, 𝑂(𝑁⋅𝑑) per query

•
Approximate nearest neighbor (ANN): trade a little recall for a lot of speed

○Inverted File Index (IVF): cluster the index, probe only the nearest centroids

○Product Quantization (PQ): compress each vector into a short code

○HNSW: multi-layer proximity graph, greedy descent from a coarse layer

## Page 37

HNSW 
(Hierarchical Navigable Small World )

• Layers: all vectors at the 
bottom, thinner samples above

• Search: start at the top, greedy 
hop toward the query, drop a 
layer when stuck

• Fast: ~log N hops, high recall

## Page 38

HNSW 
How the graph is built (backup)

• Insert one vector at a time

• Pick its top layer at random: most 
nodes stay in layer 0, few reach the top

• Link it at each layer: M nearest 
neighbors, plus a heuristic link across to 
another cluster so the greedy walk 
cannot get trapped

## Page 39

Lecture Overview

●Why RAG (5 mins)

●The RAG pipeline (10 mins)

●Indexing: chunking, contextual retrieval (15 mins)

●Retrieval: BM25, DPR, ColBERT (20 mins)

●Agentic RAG: Self-RAG, Search-R1 (10 mins)

●Failure modes (15 mins)

40

## Page 40

Different Types of Retrievers

How should we retrieve relevant passages for our retrieval system?

●
Word-overlap (BM25)

●
Vector retrieval (DPR, Sentence vectors)

●
Other, neural systems (ColBERT)

## Page 41

BM25:  the most widely used (even today)

score(𝐷, 𝑄) = ෍

𝑖=1

𝑛

IDF(𝑞𝑖) ·
𝑓(𝑞𝑖, 𝐷) ·
𝑘1  +  1

𝑓(𝑞𝑖, 𝐷) + 𝑘1  ·
1 − 𝑏 +  𝑏 ·
|𝐷|
avgdl

IDF(𝑞𝑖) = ln 𝑁 − 𝑛(𝑞𝑖) +  0.5

𝑛(𝑞𝑖) +  0.5

How often 𝑞𝑖 occurs in 𝐷

Doc length vs. the average
Docs in the collection

Docs that contain 𝑞𝑖

How rare 𝑞𝑖 is

## Page 42

IDF Comparison and Term Frequency Saturation

Figure credit to https://mbrenndoerfer.com/writing/bm25-search-algorithm-elasticsearch-implementation

## Page 43

DPR: dense passage retrieval (Karpukhin et al., 2020)

44

## Page 44

DPR: dense passage retrieval (Karpukhin et al., 2020)

45

## Page 45

Scoring a Retriever: Hit@k, Failed@k, nDCG@k

Hit@𝑘= 1

𝑄෍

𝑞∈𝑄

𝟙𝑅𝑞∩Top𝑘𝑞≠∅

Failed@𝑘= 1

𝑄෍

𝑞∈𝑄

𝟙𝑅𝑞∩Top𝑘𝑞= ∅= 1 −Hit@𝑘

nDCG@𝑘= 1

𝑄෍

𝑞∈𝑄

DCG𝑞@𝑘
IDCG𝑞@𝑘
DCG𝑞@𝑘= ෍

𝑖=1

𝑘
rel𝑞,𝑖
log2 𝑖+ 1

1 if any relevant passage is in the top k, else 0

Position in the top k does not matter

Queries with no relevant passage in the top k

Normalized by the ideal ranking's DCG

Relevance of the passage at rank i

Discounted by rank position

## Page 46

Scoring a Retriever: MRR@k, Recall@k

MRR@𝑘 =
1
𝑄෍

𝑞∈𝑄

1
rank𝑞

Recall@𝑘 =
1
𝑄෍

𝑞∈𝑄

𝑅𝑞 ∩ Top𝑘(𝑞)

𝑅𝑞

Rank of the first relevant passage

Counts as 0 if not in the top k

Relevant passages found in the top k

All relevant passages for the query

Average over all queries

## Page 47

DPR beats BM25 on 4 of 5 datasets (Karpukhin et al., 2020)

Training: contrastive loss with in-batch negatives + BM25 hard negatives

48

Top-20 & Top-100 retrieval accuracy on test sets. Single and Multi denote that our Dense Passage 
Retriever (DPR) was trained using individual or combined training datasets

## Page 48

1,000 QA pairs are enough to beat BM25

No extra pretraining: DPR 
also beats ORQA and 
REALM end to end

## Page 49

Hybrid Search and Reciprocal Rank Fusion

• The two approaches fail differently: BM25 misses paraphrase, dense 
retrieval misses rare literals (e.g., error codes, product IDs)

• Hybrid search: run both retrievers, then fuse the two ranked lists

• Reciprocal rank fusion: merge positions instead of raw scores

o no per-corpus tuning and works with any number of retrievers

50

RRF(𝑑) = ෍

𝑟∈𝑅

1
𝑘+ rank𝑟(𝑑)
𝑘= 60

## Page 50

Cross-Encoders and Reranking

•
Bi-encoder (retrieval): query and passage encoded separately

•
Cross-encoder (reranking): query and passage go through the model 
together, full attention across both

51

(Humeau et al., 2020)

### Page links

- [Link 1](https://arxiv.org/pdf/1905.01969)

## Page 51

Late Interaction: Score Tokens, Not Documents

52

Late interaction: keep one vector per token, encode query and passage 
independently, and interact only at scoring time; scoring is MaxSim

𝑆q,d = ෍

𝑖∈q

max

𝑗
𝐪𝑖⋅𝐝𝑗

## Page 52

General Architecture of ColBERT

Khattab, Omar, and Matei Zaharia. "Colbert: Efficient and effective passage search via contextualized late interaction over bert." SIGIR 2020.

## Page 53

ColBERT vs. Other Approaches

## Page 54

Fast vs Slow Retrievers

Retriever
Precomputed 
offline
Query latency
Wins on
Breaks on

BM25 (sparse)
Inverted index
62 ms  fast
Exact terms: IDs, 
names, error codes

Paraphrase, 
synonyms

DPR (bi-encoder)
One vector per 
passage
Tens of ms  fast
Semantic match at 
corpus scale

Rare literals; needs 
labeled pairs

ColBERT (late 
interaction)

One vector per 
token

458 ms end-to-end  
middle

Token-level 
evidence at scale

Index size: tokens, 
not documents

Cross-encoder 
(BERT-base)
Nothing
10,700 ms per 1k 
passages  slow

Accuracy on a 
shortlist

Cannot scan a 
corpus

Latencies from Khattab & Zaharia (2020), MS MARCO; DPR from Karpukhin et al. (2020), different hardware

## Page 55

Lecture Overview

●Why RAG (5 mins)

●The RAG pipeline (10 mins)

●Indexing: chunking, contextual retrieval (15 mins)

●Retrieval: BM25, DPR, ColBERT (20 mins)

●Agentic RAG: Self-RAG, Search-R1 (10 mins)

●Failure modes (15 mins)

56

## Page 56

Agentic RAG: Retrieval inside the Loop

Everything so far answers one question well. None of it decides 
whether to retrieve, what to ask, or when to stop.

• Retrieval should be an action the agent takes
• Three decisions: (1) retrieve or answer directly; (2) what query to 
issue; (3) whether the result is good enough

57

## Page 57

Self-RAG: Self-reflective RAG (Asai et al., 2024)

58

SELF-RAG learns to 
retrieve, critique, and 
generate text 
passages
to enhance overall 
generation quality, 
factuality, and 
verifiability.

## Page 58

CRAG: a critic grades the retrieval (Yan et al., 2024)

59

To evaluate the relevance

of the retrieved docs to 
the input, and estimate a

confidence based on

which different 
knowledge retrieval 
actions can be triggered.

## Page 59

Search-R1: learn the search policy with RL (Jin et al., 2025)

60
Search-R1 optimizes LLM reasoning trajectories with multi-turn search interactions

## Page 60

61

Search-R1: learn the search policy with RL (Jin et al., 2025)

## Page 61

62

Search-R1: learn the search policy with RL (Jin et al., 2025)

## Page 62

Lecture Overview

●Why RAG (5 mins)

●The RAG pipeline (10 mins)

●Indexing: chunking, contextual retrieval (15 mins)

●Retrieval: BM25, DPR, ColBERT (20 mins)

●Agentic RAG: Self-RAG, Search-R1 (10 mins)

●Failure modes (15 mins)

63

## Page 63

Issues with RAG

64

Retrieval-side

Recall ceiling
Missing evidence limits agent

Stale index
Embeddings not update

Permission leak
Use content not allowed to access

Reader-side

Lost in the middle
Position bias

Distraction
Similar but irrelevant content

Evidence conflict
Sources or knowledge conflicts

Loop-side

Compounding error
Early mistakes affect later decision

No stopping rule
Lack clear conditions for finishing

Prompt injection
Retrieved text steers the agent
