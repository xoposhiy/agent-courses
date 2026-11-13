# Chapter 12 Search and Retrieval in Agentic LLMs

[Course index](../../README.md) · [Original source](https://arxiv.org/html/2610.13455v1#Ch12) · [Raw file](../../raw/originals/book.html)

Retrieved: 2026-11-13T16:41:17.579179+00:00

[Contents](../../CONTENTS.md) · [Full book](../book/full-book-html.md) · [Previous chapter](chapter-11-how-agents-use-tools-to-act-in-the-world.md) · [Next chapter](chapter-13-from-tools-to-assistants-real-world-applications.md)

<a id="Ch12"></a>


### Chapter 12 Search and Retrieval in Agentic LLMs

**What You Will Learn**

In this chapter you will learn why retrieval is a fundamental
capability for agentic systems that need knowledge beyond their
training data. Specifically, you will be able to:

- Describe the full *retrieval-augmented generation* pipeline, from indexing and chunking to query formulation and answer generation.
- Implement adaptive retrieval methods such as *Self-RAG* and *Self-Ask*, and build a dense retrieval system in Python.
- Extend retrieval beyond plain text to graphs, code, tabular data, and multimodal sources.
- Distinguish agentic RAG from simple one-shot retrieval, including real-time and streaming variants.
- Evaluate retrieval systems using standard metrics such as *Recall@$k$*, *Mean Reciprocal Rank*, and *faithfulness* scores.

<a id="Ch12.S1"></a>


#### 12.1 Retrieval in General

<a id="Ch12.S1.p1.1"></a>


Before examining how agentic LLMs consult external knowledge, it is worth situating retrieval within its own, much older, disciplinary history. Information retrieval (IR) is a mature field of computer and information science that predates neural networks by decades. Many of the ideas that power modern retrieval augmented generation (RAG) pipelines are direct descendants of classical information retrieval research. The standard reference works of the field, [Salton and McGill [1983]](#bibk.bib27) and later [Manning et al. [2008]](#bibk.bib33), still provide the conceptual vocabulary such as: indexing, term weighting, ranking and relevance, that this chapter builds on.

<a id="Ch12.S1.SS1"></a>


##### 12.1.1 Bag of Words

<a id="Ch12.S1.SS1.p1.1"></a>


Early information retrieval systems represented documents and queries as *bags of words* and asked a deceptively simple question: which terms make a document a good match for a query? [Spärck Jones [1972]](#bibk.bib28) gave this question a statistical answer with the notion of inverse document frequency (IDF), observing that terms occurring in few documents are more discriminating than terms that occur almost everywhere. Weighting terms by how frequently they occur in a document (term frequency, TF) and how rare they are across the collection (IDF) yields the TF-IDF family of weighting schemes, still one of the most widely deployed representations in production search systems.

Term frequency counts how often a term $t$ occurs in a document $d$:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{TF}(t,d)=\frac{f_{t,d}}{\sum_{t^{\prime}\in d}f_{t^{\prime},d}} $$ |  | (12.1) |

<a id="Ch12.S1.SS1.p2.2"></a>


where $f_{t,d}$ is the raw count of $t$ in $d$. Inverse document frequency, following [Spärck Jones [1972]](#bibk.bib28), down-weights terms that occur in many documents:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{IDF}(t,D)=\log\frac{|D|}{|\{d\in D:t\in d\}|} $$ |  | (12.2) |

where $D$ is the document collection. Combining the two gives the classic TF-IDF weight of term $t$ in document $d$:

<a id="Ch12.E3"></a>


|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{TF\text{-}IDF}(t,d,D)=\mathrm{TF}(t,d)\times\mathrm{IDF}(t,D) $$ |  | (12.3) |

<a id="Ch12.S1.SS2"></a>


##### 12.1.2 Vector Space Models

<a id="Ch12.S1.SS2.p1.1"></a>


[Salton et al. [1975]](#bibk.bib29) formalized this idea into the *vector space model*, representing every document and query as a vector in a high-dimensional term space and ranking documents by their cosine similarity to the query vector. The vector space model established a pattern that persists directly into today’s dense retrievers (Section [12.3](#Ch12.S3 "12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")): reduce documents and queries to points in a shared geometric space, and let distance or similarity stand in for relevance.

More formally, in the vector space model, each document $d$ (and query $q$) is represented as a vector of term weights, $\vec{d}=(w_{1,d},w_{2,d},\dots,w_{n,d})$, typically using TF-IDF weights (Eq. [12.3](#Ch12.E3 "In 12.1.1 Bag of Words ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")). Relevance is then approximated by the cosine similarity between query and document vectors:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{sim}(\vec{q},\vec{d})=\cos(\theta)=\frac{\vec{q}\cdot\vec{d}}{\lVert\vec{q}\rVert\,\lVert\vec{d}\rVert} $$ |  | (12.4) |

<a id="Ch12.S1.SS2.p2.2"></a>


Documents are ranked by decreasing $\mathrm{sim}(\vec{q},\vec{d})$. This same operation, cosine similarity between two learned vectors, reappears in dense retrieval (Section [12.3](#Ch12.S3 "12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")), the only difference being how the vectors are obtained.
Where the vector space model used raw term co-occurrence, modern dense retrievers such as dense passage retrieval (DPR) [[Karpukhin et al., 2020](#bibk.bib6)] use learned neural embeddings, but the underlying geometric intuition is unchanged.

<a id="Ch12.S1.SS3"></a>


##### 12.1.3 Latent and Sparse Representations

<a id="Ch12.S1.SS3.p1.1"></a>


Two further developments bridge classical and modern retrieval. First, [Robertson and Zaragoza [2009]](#bibk.bib31) developed the *probabilistic relevance framework*, which treats retrieval as a problem of estimating the probability that a document is relevant to a query given its term statistics. This framework produced BM25 [Robertson et al. [1994]](#bibk.bib32), a term-weighting and ranking function which ranks document $d$ for query $q$ as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{BM25}(q,d)=\sum_{t\in q}\mathrm{IDF}(t,D)\cdot\frac{f_{t,d}\,(k_{1}+1)}{f_{t,d}+k_{1}\left(1-b+b\,\dfrac{|d|}{\mathrm{avgdl}}\right)} $$ |  | (12.5) |

where $|d|$ is the length of document $d$, $\mathrm{avgdl}$ is the average document length in the collection, and $k_{1}$ and $b$ are free parameters that control term-frequency saturation and length normalization, respectively (typical values: $k_{1}\in[1.2,2.0]$, $b=0.75$). BM25 remains the sparse-retrieval baseline referenced throughout the hybrid retrieval discussions in Section [12.3](#Ch12.S3 "12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").

<a id="Ch12.S1.SS3.p2.1"></a>


Second, [Deerwester et al. [1990]](#bibk.bib30) introduced *latent semantic analysis* (LSA), which applies singular value decomposition to the term-document matrix to uncover latent topics and match documents by meaning rather than by exact term overlap. LSA was the first widely used technique to address the vocabulary mismatch problem, the same problem that motivates dense and semantic retrieval today.

LSA operates on the term-document matrix $X\in\mathbb{R}^{m\times n}$, where $m$ is the vocabulary size and $n$ the number of documents. Its entries are typically TF-IDF weights (Eq. [12.3](#Ch12.E3 "In 12.1.1 Bag of Words ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")). Applying truncated singular value decomposition,

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ X\approx U_{k}\Sigma_{k}V_{k}^{\top} $$ |  | (12.6) |

retains only the $k$ largest singular values in $\Sigma_{k}$, producing a rank-$k$ approximation of $X$. Documents and terms are then represented in this reduced $k$-dimensional latent space, where semantically related terms and documents lie close together even without exact term overlap.

<a id="Ch12.S1.SS3.p4.1"></a>


The final bridge from classical IR to the neural retrieval methods used throughout this chapter is the emergence of learned, dense vector representations of words. [Mikolov et al. [2013]](#bibk.bib34) showed that simple neural network architectures, trained to predict a word from its context, produce continuous word embeddings that capture rich syntactic and semantic regularities. This work, together with the encoder architectures that followed, supplied the representational building blocks on which dense retrieval, DPR-style bi-encoders, and ultimately retrieval-augmented generation are built.

Retrieval, in other words, is a decades-old discipline concerned with a single enduring question: given a query, which pieces of a large collection are actually relevant to it? What has changed with the arrival of LLMs is not the question but the stakes: models now consult retrieved evidence not merely to rank documents for a human reader, but to condition their own generation. We will now discuss why that shift matters.

<a id="Ch12.S2"></a>


#### 12.2 Why Retrieval Matters for Agentic LLMs

Building on this foundation, large language models introduce a new reason to care about retrieval. LLMs are frozen snapshots of world knowledge. The LLM’s parameters
can not contain information that was generated after the corpus
was fixed.
LLMs struggle when tasks require timely, proprietary, or long–tail information that was absent at pretraining time. Retrieval augmentation mitigates these limits by consulting external sources at inference time and conditioning generation on the retrieved evidence.

<a id="Ch12.S2.p2.1"></a>


Retrieval augmented generation (RAG) methods have been developed to integrate data from external knowledge bases with the pretrained knowledge stored in the parameters of language models.
Most RAG approaches work at inference time, although some can work during finetuning or even pretraining.
Most RAG approaches work on unstructured (textual) data sources. These text documents are indexed to increase efficient access, and they can be organized and a knowledge graph can be created. Finally, database-type query optimization is often
performed, where queries can be expanded or complex queries can be
split into sub-queries [[Cong et al., 2024](#bibk.bib2)].

<a id="Ch12.S2.p3.1"></a>


This simple idea, popularized by early systems such as REALM [[Guu et al., 2020](#bibk.bib5)], DPR [[Karpukhin et al., 2020](#bibk.bib6)], and RAG [[Lewis et al., 2020](#bibk.bib3)], has grown into a rich design space spanning indexing, query planning, re-ranking, citation and attribution, and continuous data refresh. Recent surveys synthesize the landscape and evaluation practices [[Gao and others, 2023](#bibk.bib22), [Huang and others, 2024](#bibk.bib23), [Yu and others, 2024](#bibk.bib24), [Sharma and others, 2025](#bibk.bib26), [Peng and others, 2024](#bibk.bib25)].

<a id="Ch12.S2.SS0.SSS0.Px1"></a>


###### When to retrieve.

Retrieval is most beneficial when: (1) the task is knowledge-intensive (definitions, entities, numbers, references), (2) the domain shifts rapidly (news, prices, docs), (3) transparency is required (with citations), or (4) models must respect strict source-of-truth constraints (compliance portals, internal wikis). In agentic settings, retrieval can be interleaved with tool use and planning (see Chapter [11](chapter-11-how-agents-use-tools-to-act-in-the-world.md#Ch11 "Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")).

<a id="Ch12.S3"></a>


#### 12.3 Retrieval-Augmented Generation Pipeline

A practical RAG system typically implements the following seven stages:

1. <a id="Ch12.S3.I1.i1.p1.1"></a>


   Indexing: The indexing phase is the first step. This step involves: Taking all raw source material, such as HTML pages, PDFs, tables, or code, and converting it into clean, consistent text. Keep important structure as metadata (headings, anchors, timestamps, authorship). Break content into chunks with meaningful boundaries (e.g., sentences or sections) and small overlaps so context isn’t lost. Create two types of searchable representations: *sparse* ones, like BM25 (a classic term-matching method) or SPLADE  [[Formal et al., 2021](#bibk.bib7)] (a more modern variant that expands terms), which are good for exact keyword matches; and *dense* ones, which are embeddings that capture meaning for semantic matches. Storing both lets the system find exact matches (IDs, numbers) and semantic matches (paraphrases, synonyms) in the same search.
2. <a id="Ch12.S3.I1.i2.p1.1"></a>


   Query Construction: Turn the user’s question into one or more precise search queries. This can involve rewriting the question for clarity, breaking complex questions into sub-questions (multi-hop), adding related terms (query expansion), or even generating a hypothetical answer to use as a search target (HyDE) [[Gao et al., 2023](#bibk.bib18)]. For structured data sources, generate specific queries such as SQL or graph lookups. The aim is to make the search engine understand exactly what to look for.
3. <a id="Ch12.S3.I1.i3.p1.1"></a>


   Candidate Retrieval: Use the constructed queries to pull in potentially relevant chunks from the index. Dense retrievers (e.g., DPR [[Karpukhin et al., 2020](#bibk.bib6)], Contriever [[Izacard et al., 2022](#bibk.bib8)]) match by meaning; sparse methods (BM25, SPLADE) match by exact terms; hybrids combine both. To search quickly at scale, use approximate nearest neighbor (ANN) indexes like HNSW [[Malkov and Yashunin, 2020](#bibk.bib17)] or IVF-PQ [[Jégou et al., 2011](#bibk.bib10)]. For code or images, use specialized encoders. This step is about casting a wide net without losing focus.
4. <a id="Ch12.S3.I1.i4.p1.1"></a>


   Re-ranking: Take the pool of retrieved candidates and reorder them by relevance using more accurate but slower models, like cross-encoders (BERT, MiniLM). Late-interaction models such as ColBERTv2 [[Santhanam et al., 2022](#bibk.bib9)] balance quality and speed. This ensures that top results are the ones most likely to answer the question.
5. Context Assembly: Remove duplicates, ensure coverage of different aspects of the query (diversity), and prefer recent or domain-relevant sources. Bundle the selected passages, along with their metadata (source, URL, date), into a context package to feed into the LLM. This gives the model a curated, trustworthy information set.
6. <a id="Ch12.S3.I1.i6.p1.1"></a>


   Grounded Generation: Ask the LLM to generate the answer using the provided context, with citations for each claim. If evidence is insufficient, the model should abstain or ask for clarification. Some systems, such as Self-RAG [[Asai et al., 2023](#bibk.bib19)], decide on the fly whether to retrieve more information. The focus is on answers that are both correct and well-supported.
7. Attribution and Logging: Show the sources alongside the answer so readers can verify claims. Log the entire process including queries, retrieved documents and versions, for debugging, evaluation, and compliance. This makes the system transparent and auditable.

A straightforward RAG system follows the seven‑step pipeline outlined above. Listing [12.1](#Ch12.F1 "Figure 12.1 ‣ 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") shows Python‑style pseudo-code for this process. The function takes a user question, rewrites it into one or more search queries, retrieves and re‑ranks candidate passages, assembles a context window and finally generates an answer while tracking which passages were used. We will go into more details below.

<a id="Ch12.F1"></a>


[⬇](data:text/plain;base64,IyBJbnB1dDogcXVlc3Rpb24gcSwgc2VhcmNoIGluZGV4LCBhbmQgbnVtYmVyIG9mIHBhc3NhZ2VzIGsKZGVmIHJhZ19hbnN3ZXIocSwgaW5kZXgsIGs9OCk6CiAgICAjIDEuIENvbnN0cnVjdCBzZWFyY2ggcXVlcmllcyAocG9zc2libHkgZGVjb21wb3NlIG11bHRpLWhvcCBxdWVzdGlvbnMpCiAgICBxdWVyaWVzID0gcmV3cml0ZV9xdWVzdGlvbihxKQogICAgIyAyLiBSZXRyaWV2ZSBjYW5kaWRhdGUgcGFzc2FnZXMgZnJvbSB0aGUgaW5kZXgKICAgIGNhbmRpZGF0ZXMgPSByZXRyaWV2ZShpbmRleCwgcXVlcmllcywgaz0yMDApCiAgICAjIDMuIFJlLXJhbmsgd2l0aCBhIGNyb3NzLWVuY29kZXIgb3IgbGF0ZS1pbnRlcmFjdGlvbiBtb2RlbAogICAgcmFua2VkID0gcmVyYW5rKGNhbmRpZGF0ZXMpCiAgICAjIDQuIEFzc2VtYmxlIGEgY29udGV4dCB3aW5kb3cgZnJvbSB0aGUgdG9wLWsgcGFzc2FnZXMKICAgIGNvbnRleHQgPSBhc3NlbWJsZShyYW5rZWRbOmtdKQogICAgIyA1LiBHZW5lcmF0ZSBhbiBhbnN3ZXIgY29uZGl0aW9uZWQgb24gdGhlIGNvbnRleHQgYW5kIHByb3ZpZGUgY2l0YXRpb25zCiAgICBhbnN3ZXIsIGNpdGF0aW9ucyA9IGdlbmVyYXRlX2Fuc3dlcihxLCBjb250ZXh0KQogICAgcmV0dXJuIGFuc3dlciwgY2l0YXRpb25z)

1
*# Input: question q, search index, and number of passages k*

2
**def** rag_answer(q, index, k=8):

3
 *# 1. Construct search queries (possibly decompose multi-hop questions)*

4
 queries = rewrite_question(q)

5
 *# 2. Retrieve candidate passages from the index*

6
 candidates = retrieve(index, queries, k=200)

7
 *# 3. Re-rank with a cross-encoder or late-interaction model*

8
 ranked = rerank(candidates)

9
 *# 4. Assemble a context window from the top-k passages*

10
 context = assemble(ranked[:k])

11
 *# 5. Generate an answer conditioned on the context and provide citations*

12
 answer, citations = generate_answer(q, context)

13
 **return** answer, citations

Figure 12.1: High Level Flow of a Basic RAG Setup

<a id="Ch12.S4"></a>


#### 12.4 Adaptive Retrieval Methods

Traditional RAG systems retrieve a fixed number of passages regardless of whether any retrieval is actually needed. This *always–on* strategy simplifies engineering but can hurt both efficiency and accuracy. Recent research explores *adaptive* or *gated* retrieval strategies that teach the model to decide when to search and how much evidence to consult. These methods align with the self‑reflection ideas introduced in Section [6.2.4](chapter-06-multi-step-reasoning-in-llms.md#Ch6.S2.SS4 "6.2.4 Agentic Harness for Prompt Improvement ‣ 6.2 Self-Reflection and State ‣ Chapter 6 Multi-step Reasoning in LLMs ‣ Part II Reasoning ‣ Agentic Large Language Models"): rather than blindly ingest retrieved text, the language model introspects about its own confidence and triggers retrieval only when it recognizes a knowledge gap.

<a id="Ch12.S4.p2.1"></a>


Concretely, [Asai et al. [2023]](#bibk.bib19) propose Self‑RAG, which trains a single model to generate answers, request retrieval, and critique its own outputs using special *reflection tokens*. When the model’s draft answer is uncertain, it emits a <RETRIEVE> token to call the search tool and incorporates the retrieved passages in the next step. Experiments show that this learned gating improves factuality over static RAG while avoiding unnecessary calls.

<a id="Ch12.S4.p3.1"></a>


A more lightweight approach is Self‑Ask [[Press et al., 2022](#bibk.bib4)], where the model decomposes a complex question into simpler sub‑questions, issues them to a search tool, and uses the answers to compose a final response. Self‑Ask can be combined with planning agents, enabling models to interleave reasoning, tool calls, and retrieval. Graph Toolformer [[Zhang, 2023](#bibk.bib1)] extends this idea by training a policy to insert search queries into a program graph. At inference time the LLM dynamically decides whether to retrieve from a text index, a knowledge graph, or a database, based on the current state of reasoning.

Beyond these specific examples, adaptive retrieval can be implemented in several ways:

- Confidence‑based Gating: The model estimates its uncertainty (e.g., from entropy or calibration metrics) and triggers retrieval when confidence falls below a threshold.
- Iterative Retrieval: Rather than pulling all evidence at once, the system retrieves a few passages, reasons about them, and then decides whether additional rounds of search are needed. This approach is useful for multi-hop questions.
- Query Planning: An agent decomposes the user query into sub‑tasks, dispatches them to different tools (search, database, calculator), and integrates the results. Retrievers are called only when the plan requires external knowledge.
- Learning to Retrieve: Reinforcement learning or supervised finetuning can teach the model to emit <RETRIEVE> tokens at appropriate times. Self‑RAG is one instantiation; other methods explore training retrieval policies end‑to‑end with the generator.

Adaptive retrieval reduces latency and cost by avoiding unnecessary searches, and it often improves answer quality by focusing attention on missing knowledge. Designing effective gating policies, however, requires careful evaluation (see Section [12.7](#Ch12.S7 "12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")) and may demand additional supervision during training.

<a id="Ch12.S4.SS1"></a>


##### 12.4.1 Adaptive Retrieval via Self‑RAG and Self-Ask

<a id="Ch12.S4.SS1.p1.1"></a>


The Self‑RAG framework of [Asai et al. [2023]](#bibk.bib19) teaches the model to request retrieval on demand by emitting a special <RETRIEVE> token during generation. The pseudo-code in Listing [12.2](#Ch12.F2 "Figure 12.2 ‣ 12.4.1 Adaptive Retrieval via Self‑RAG and Self-Ask ‣ 12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") sketches how such a loop operates. The model maintains a growing context and alternates between generating output tokens and pulling in new evidence when needed.

<a id="Ch12.F2"></a>


[⬇](data:text/plain;base64,IyBJbnB1dDogcXVlc3Rpb24gcSwgc2VhcmNoIGluZGV4LCBhbmQgdHJhaW5lZCBTZWxmLVJBRyBtb2RlbApkZWYgc2VsZl9yYWdfYW5zd2VyKHEsIGluZGV4LCBtb2RlbCk6CiAgICBjb250ZXh0ID0gW10KICAgIG91dHB1dF90b2tlbnMgPSBbXQogICAgIyBHZW5lcmF0ZSB0b2tlbnMgc2VxdWVudGlhbGx5CiAgICBmb3IgdG9rZW4gaW4gbW9kZWwuZ2VuZXJhdGVfc3RyZWFtKHEsIGNvbnRleHQpOgogICAgICAgIGlmIHRva2VuID09ICI8UkVUUklFVkU+IjoKICAgICAgICAgICAgIyBNb2RlbCByZXF1ZXN0cyBtb3JlIGluZm9ybWF0aW9uCiAgICAgICAgICAgIG5ld19kb2NzID0gcmV0cmlldmUoaW5kZXgsIHJld3JpdGVfcXVlc3Rpb24ocSksIGs9NSkKICAgICAgICAgICAgY29udGV4dC5leHRlbmQobmV3X2RvY3MpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgb3V0cHV0X3Rva2Vucy5hcHBlbmQodG9rZW4pCiAgICAgICAgaWYgdG9rZW4gPT0gIjxFTkQ+IjoKICAgICAgICAgICAgYnJlYWsKICAgIHJldHVybiBkZXRva2VuaXplKG91dHB1dF90b2tlbnMp)

1
*# Input: question q, search index, and trained Self-RAG model*

2
**def** self_rag_answer(q, index, model):

3
 context = []

4
 output_tokens = []

5
 *# Generate tokens sequentially*

6
 **for** token **in** model.generate_stream(q, context):

7
 **if** token == "<RETRIEVE>":

8
 *# Model requests more information*

9
 new_docs = retrieve(index, rewrite_question(q), k=5)

10
 context.extend(new_docs)

11
 **else**:

12
 output_tokens.append(token)

13
 **if** token == "<END>":

14
 **break**

15
 **return** detokenize(output_tokens)

Figure 12.2: High Level Pseudo-Code Demonstrating Self-RAG

<a id="Ch12.S4.SS1.p2.1"></a>


It should be noted that for Self-RAG to work, the foundation model should be trained or fine-tuned to produce the <RETRIEVE> token.
Self‑Ask [[Press et al., 2022](#bibk.bib4)] on the other hand is not dependent on the language model. Self-Ask decomposes a complex question into simpler sub‑questions, retrieves evidence for each and synthesizes the final answer. The following high‑level pseudo-code shows one way to implement this strategy:

[⬇](data:text/plain;base64,ZGVmIHNlbGZfYXNrKHEsIGluZGV4KToKICAgIHN1Yl9xdWVzdGlvbnMgPSBkZWNvbXBvc2UocSkKICAgICMgZS5nLiAiV2hlbiB3YXMgRWluc3RlaW4gYm9ybj8iIGFuZCAiV2hhdCBpcyB0aGUgTm9iZWwgUHJpemU/IgogICAgaW50ZXJtZWRpYXRlX2Fuc3dlcnMgPSBbXQogICAgZm9yIHNxIGluIHN1Yl9xdWVzdGlvbnM6CiAgICAgICAgZG9jcyA9IHJldHJpZXZlKGluZGV4LCByZXdyaXRlX3F1ZXN0aW9uKHNxKSwgaz01KQogICAgICAgIGFuc3dlciA9IHN1bW1hcml6ZShkb2NzKQogICAgICAgIGludGVybWVkaWF0ZV9hbnN3ZXJzLmFwcGVuZChhbnN3ZXIpCiAgICBmaW5hbF9hbnN3ZXIgPSBjb21wb3NlKGludGVybWVkaWF0ZV9hbnN3ZXJzKQogICAgcmV0dXJuIGZpbmFsX2Fuc3dlcg==)

1
**def** self_ask(q, index):

2
 sub_questions = decompose(q)

3
 *# e.g. "When was Einstein born?" and "What is the Nobel Prize?"*

4
 intermediate_answers = []

5
 **for** sq **in** sub_questions:

6
 docs = retrieve(index, rewrite_question(sq), k=5)

7
 answer = summarize(docs)

8
 intermediate_answers.append(answer)

9
 final_answer = compose(intermediate_answers)

10
 **return** final_answer

Figure 12.3: High Level Pseudo-Code Demonstrating Self-Ask

<a id="Ch12.S4.SS2"></a>


##### 12.4.2 A Simple Dense Retrieval Example in Python

Dense retrieval libraries such as the sentence_transformers toolkit make it easy to index a small corpus and perform semantic search. Listing [12.4](#Ch12.F4 "Figure 12.4 ‣ 12.4.2 A Simple Dense Retrieval Example in Python ‣ 12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") illustrates how to embed a corpus of sentences, compute similarities to a query and display the top results.

<a id="Ch12.F4"></a>


[⬇](data:text/plain;base64,ZnJvbSBzZW50ZW5jZV90cmFuc2Zvcm1lcnMgaW1wb3J0IFNlbnRlbmNlVHJhbnNmb3JtZXIsIHV0aWwKCiMgUHJlcGFyZSBhIHNtYWxsIGNvcnB1cwp0ZXh0cyA9IFsKICAgICJUaGUgRWlmZmVsIFRvd2VyIGlzIGluIFBhcmlzLiIsCiAgICAiVGhlIGNhcGl0YWwgb2YgRnJhbmNlIGlzIFBhcmlzLiIsCiAgICAiQmVybGluIGlzIHRoZSBjYXBpdGFsIG9mIEdlcm1hbnkuIiwKICAgICJUaGUgR3JlYXQgV2FsbCBpcyBpbiBDaGluYS4iCl0KCm1vZGVsID0gU2VudGVuY2VUcmFuc2Zvcm1lcigiYWxsLU1pbmlMTS1MNi12MiIpCmNvcnB1c19lbWJlZGRpbmdzID0gbW9kZWwuZW5jb2RlKHRleHRzLCBjb252ZXJ0X3RvX3RlbnNvcj1UcnVlKQoKZGVmIHNlbWFudGljX3NlYXJjaChxdWVzdGlvbiwgaz0yKToKICAgIHF1ZXJ5X2VtYiA9IG1vZGVsLmVuY29kZShxdWVzdGlvbiwgY29udmVydF90b190ZW5zb3I9VHJ1ZSkKICAgIHNjb3JlcyA9IHV0aWwuY29zX3NpbShxdWVyeV9lbWIsIGNvcnB1c19lbWJlZGRpbmdzKVswXQogICAgdG9wX3Jlc3VsdHMgPSBzY29yZXMudG9wayhrKQogICAgZm9yIHNjb3JlLCBpZHggaW4gemlwKHRvcF9yZXN1bHRzLnZhbHVlcywgdG9wX3Jlc3VsdHMuaW5kaWNlcyk6CiAgICAgICAgcHJpbnQodGV4dHNbaWR4XSwgIihzY29yZToiLCBzY29yZS5pdGVtKCksICIpIikKCiMgRXhhbXBsZSB1c2FnZQpzZW1hbnRpY19zZWFyY2goIldoYXQgaXMgdGhlIGNhcGl0YWwgb2YgRnJhbmNlPyIp)

1
**from** sentence_transformers **import** SentenceTransformer, util

2

3
*# Prepare a small corpus*

4
texts = [

5
 "The␣Eiffel␣Tower␣is␣in␣Paris.",

6
 "The␣capital␣of␣France␣is␣Paris.",

7
 "Berlin␣is␣the␣capital␣of␣Germany.",

8
 "The␣Great␣Wall␣is␣in␣China."

9
]

10

11
model = SentenceTransformer("all-MiniLM-L6-v2")

12
corpus_embeddings = model.encode(texts, convert_to_tensor=True)

13

14
**def** semantic_search(question, k=2):

15
 query_emb = model.encode(question, convert_to_tensor=True)

16
 scores = util.cos_sim(query_emb, corpus_embeddings)[0]

17
 top_results = scores.topk(k)

18
 **for** score, idx **in** **zip**(top_results.values, top_results.indices):

19
 **print**(texts[idx], "(score:", score.item(), ")")

20

21
*# Example usage*

22
semantic_search("What␣is␣the␣capital␣of␣France?")

Figure 12.4: A Simple Dense Retrieval Example in Python

<a id="Ch12.S4.SS3"></a>


##### 12.4.3 Query Rewriting and Expansion

Effective retrieval often starts with transforming the original question into a form that the index can match. Large language models can act as query re-writers by paraphrasing, expanding acronyms, adding synonyms or even producing a hypothetical answer to use as a pseudo‑query (the HyDE technique).<a id="Ch12.footnote1"></a>
11
1
HyDE stands for Hypothetical Document Embeddings and generates a plausible answer which is then embedded and used to retrieve supporting passages [[Gao et al., 2023](#bibk.bib18)]. Listing [12.5](#Ch12.F5 "Figure 12.5 ‣ 12.4.3 Query Rewriting and Expansion ‣ 12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") sketches a simple function that calls an LLM to produce multiple rewrites and expansions and then merges the results into a set of search queries.

<a id="Ch12.F5"></a>


[⬇](data:text/plain;base64,ZGVmIHJld3JpdGVfcXVlc3Rpb24ocSwgbl92YXJpYW50cz0zKToKICAgICIiIgogICAgVXNlIGFuIExMTSB0byBnZW5lcmF0ZSBhbHRlcm5hdGl2ZSBwaHJhc2luZ3MgYW5kIGh5cG90aGV0aWNhbCBhbnN3ZXJzLgoKICAgIDpwYXJhbSBxOiBUaGUgdXNlciBxdWVzdGlvbi4KICAgIDpwYXJhbSBuX3ZhcmlhbnRzOiBOdW1iZXIgb2YgcmV3cml0ZXMgdG8gZ2VuZXJhdGUuCiAgICA6cmV0dXJuOiBBIGxpc3Qgb2YgZXhwYW5kZWQgcXVlcmllcy4KICAgICIiIgogICAgdmFyaWFudHMgPSBbcV0KICAgICMgQXNrIHRoZSBtb2RlbCBmb3IgcGFyYXBocmFzZXMgYW5kIGNsYXJpZmljYXRpb25zCiAgICBwYXJhcGhyYXNlcyA9IGxsbS5nZW5lcmF0ZShbIlJld3JpdGU6ICIgKyBxXSAqIG5fdmFyaWFudHMpCiAgICB2YXJpYW50cy5leHRlbmQocGFyYXBocmFzZXMpCiAgICAjIEFzayB0aGUgbW9kZWwgdG8gZ3Vlc3MgYW4gYW5zd2VyIChIeURFKSBhbmQgdXNlIGl0IGFzIGEgcHNldWRvLXF1ZXJ5CiAgICBndWVzcyA9IGxsbS5nZW5lcmF0ZShbIkFuc3dlciBicmllZmx5OiAiICsgcV0pWzBdCiAgICB2YXJpYW50cy5hcHBlbmQoZ3Vlc3MpCiAgICAjIE9wdGlvbmFsbHkgYWRkIGVudGl0eSBhbGlhc2VzIGZyb20gYSBrbm93bGVkZ2UgYmFzZQogICAgYWxpYXNlcyA9IGxvb2t1cF9hbGlhc2VzKHEpCiAgICB2YXJpYW50cy5leHRlbmQoYWxpYXNlcykKICAgIHJldHVybiB2YXJpYW50cw==)

1
**def** rewrite_question(q, n_variants=3):

2
 """

3
␣␣␣␣Use␣an␣LLM␣to␣generate␣alternative␣phrasings␣and␣hypothetical␣answers.

4

5
␣␣␣␣:param␣q:␣The␣user␣question.

6
␣␣␣␣:param␣n_variants:␣Number␣of␣rewrites␣to␣generate.

7
␣␣␣␣:return:␣A␣list␣of␣expanded␣queries.

8
␣␣␣␣"""

9
 variants = [q]

10
 *# Ask the model for paraphrases and clarifications*

11
 paraphrases = llm.generate(["Rewrite:␣" + q] \* n_variants)

12
 variants.extend(paraphrases)

13
 *# Ask the model to guess an answer (HyDE) and use it as a pseudo-query*

14
 guess = llm.generate(["Answer␣briefly:␣" + q])[0]

15
 variants.append(guess)

16
 *# Optionally add entity aliases from a knowledge base*

17
 aliases = lookup_aliases(q)

18
 variants.extend(aliases)

19
 **return** variants

Figure 12.5: A Simple Example of Query Rewriting

In practice, the rewrite_question function might call an API such as OpenAI’s gpt-5 to generate paraphrases and hypothetical answers, then use a thesaurus or entity‑linking tool to add aliases. Query expansion improves recall but can also introduce noise.

<a id="Ch12.S5"></a>


#### 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal

While most RAG systems operate over unstructured text, many agentic applications require reasoning over structured data, source code, or images. Extending retrieval beyond plain text opens up new opportunities but also introduces modeling challenges.

<a id="Ch12.S5.SS0.SSS0.Px1"></a>


###### Graph‑RAG

<a id="Ch12.S5.SS0.SSS0.Px1.p1.1"></a>


A knowledge graph encodes entities as nodes and relations as edges. Building a lightweight graph over the corpus allows the retriever to follow links (e.g., *works for*, *located in*) rather than relying solely on bag‑of‑words similarity. The GraphRAG survey formalizes a three‑step workflow: graph‑based indexing, graph‑guided retrieval, and graph‑enhanced generation [[Peng and others, 2024](#bibk.bib25)]. Indexing extracts entities and relations from text, canonicalizes them and builds neighborhood structures. Retrieval then expands the query through the graph to find related nodes and associated passages; this supports global reasoning and disambiguation. Finally, the generation model can use the graph structure to organize facts into a coherent narrative and avoid contradictions.

<a id="Ch12.S5.SS1"></a>


##### 12.5.1 Graph‑based retrieval example

<a id="Ch12.S5.SS1.p1.1"></a>


GraphRAG systems represent knowledge as a graph of entities and relations and use graph traversals to retrieve relevant nodes [[Peng and others, 2024](#bibk.bib25)]. A lightweight implementation can be built with the networkx library. In the example in Listing [12.6](#Ch12.F6 "Figure 12.6 ‣ 12.5.1 Graph‑based retrieval example ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") we construct a small knowledge graph and implement two simple retrieval primitives: (1) get the immediate neighborhood of an entity, and (2) find the shortest path between two entities. These operations can support multi‑hop reasoning.

<a id="Ch12.F6"></a>


[⬇](data:text/plain;base64,aW1wb3J0IG5ldHdvcmt4IGFzIG54CgpkZWYgYnVpbGRfa25vd2xlZGdlX2dyYXBoKCk6CiAgICBHID0gbnguRGlHcmFwaCgpCiAgICAjIEFkZCBub2RlcyByZXByZXNlbnRpbmcgZW50aXRpZXMKICAgIEcuYWRkX25vZGUoIkFsYmVydCBFaW5zdGVpbiIsIHR5cGU9InBlcnNvbiIpCiAgICBHLmFkZF9ub2RlKCJOb2JlbCBQcml6ZSIsIHR5cGU9ImF3YXJkIikKICAgIEcuYWRkX25vZGUoIlBoeXNpY3MiLCB0eXBlPSJmaWVsZCIpCiAgICBHLmFkZF9ub2RlKCIxOTIxIiwgdHlwZT0ieWVhciIpCiAgICAjIEFkZCBlZGdlcyByZXByZXNlbnRpbmcgcmVsYXRpb25zCiAgICBHLmFkZF9lZGdlKCJBbGJlcnQgRWluc3RlaW4iLCAiTm9iZWwgUHJpemUiLCByZWxhdGlvbj0icmVjZWl2ZWQiKQogICAgRy5hZGRfZWRnZSgiTm9iZWwgUHJpemUiLCAiUGh5c2ljcyIsIHJlbGF0aW9uPSJjYXRlZ29yeSIpCiAgICBHLmFkZF9lZGdlKCJOb2JlbCBQcml6ZSIsICIxOTIxIiwgcmVsYXRpb249InllYXIiKQogICAgcmV0dXJuIEcKCmRlZiBuZWlnaGJvdXJzKEcsIGVudGl0eSk6CiAgICAiIiJSZXR1cm4gYWxsIG91dGdvaW5nIG5laWdoYm91cnMgb2YgYW4gZW50aXR5LiIiIgogICAgcmV0dXJuIGxpc3QoRy5zdWNjZXNzb3JzKGVudGl0eSkpCgpkZWYgc2hvcnRlc3RfcGF0aChHLCBzb3VyY2UsIHRhcmdldCk6CiAgICAiIiJSZXR1cm4gdGhlIHNlcXVlbmNlIG9mIGVudGl0aWVzIG9uIHRoZSBzaG9ydGVzdCBwYXRoLiIiIgogICAgdHJ5OgogICAgICAgIHJldHVybiBueC5zaG9ydGVzdF9wYXRoKEcsIHNvdXJjZSwgdGFyZ2V0KQogICAgZXhjZXB0IG54Lk5ldHdvcmtYTm9QYXRoOgogICAgICAgIHJldHVybiBbXQoKIyBFeGFtcGxlIHVzYWdlCkcgPSBidWlsZF9rbm93bGVkZ2VfZ3JhcGgoKQpwcmludChuZWlnaGJvdXJzKEcsICJBbGJlcnQgRWluc3RlaW4iKSkKIyBbJ05vYmVsIFByaXplJ10KcHJpbnQoc2hvcnRlc3RfcGF0aChHLCAiQWxiZXJ0IEVpbnN0ZWluIiwgIlBoeXNpY3MiKSkKIyBbJ0FsYmVydCBFaW5zdGVpbicsICdOb2JlbCBQcml6ZScsICdQaHlzaWNzJ10=)

1
**import** networkx as nx

2

3
**def** build_knowledge_graph():

4
 G = nx.DiGraph()

5
 *# Add nodes representing entities*

6
 G.add_node("Albert␣Einstein", **type**="person")

7
 G.add_node("Nobel␣Prize", **type**="award")

8
 G.add_node("Physics", **type**="field")

9
 G.add_node("1921", **type**="year")

10
 *# Add edges representing relations*

11
 G.add_edge("Albert␣Einstein", "Nobel␣Prize", relation="received")

12
 G.add_edge("Nobel␣Prize", "Physics", relation="category")

13
 G.add_edge("Nobel␣Prize", "1921", relation="year")

14
 **return** G

15

16
**def** neighbours(G, entity):

17
 """Return␣all␣outgoing␣neighbours␣of␣an␣entity."""

18
 **return** **list**(G.successors(entity))

19

20
**def** shortest_path(G, source, target):

21
 """Return␣the␣sequence␣of␣entities␣on␣the␣shortest␣path."""

22
 **try**:

23
 **return** nx.shortest_path(G, source, target)

24
 **except** nx.NetworkXNoPath:

25
 **return** []

26

27
*# Example usage*

28
G = build_knowledge_graph()

29
**print**(neighbours(G, "Albert␣Einstein"))

30
*# [’Nobel Prize’]*

31
**print**(shortest_path(G, "Albert␣Einstein", "Physics"))

32
*# [’Albert Einstein’, ’Nobel Prize’, ’Physics’]*

Figure 12.6: An Example of Graph-based Retrieval Primitives in Python

In a full GraphRAG system the graph nodes would store pointers to the original text passages, and the retrieval procedure would return both the sequence of nodes and the associated passages to the LLM. Graph‑guided retrieval can reduce hallucinations by grounding reasoning in explicit edges and by encouraging consistency between related facts.

<a id="Ch12.S5.SS1.SSS0.Px1"></a>


###### Code‑RAG

<a id="Ch12.S5.SS1.SSS0.Px1.p1.1"></a>


Source code has a rich syntax-structure. The semantics of source code differs from natural language. For code retrieval to be effective, it should index at the function or module level, including signatures, docstrings, abstract syntax trees (ASTs) and dependency graphs. Models such as CodeBERT [[Feng et al., 2020](#bibk.bib11)] learn joint embeddings for code and natural language; they support tasks like natural‑language code search, code summarization, and documentation generation. In Code‑RAG, the retriever can fetch relevant functions, APIs and test cases, and the re-ranker can use code‑aware cross‑encoders or graph neural networks to prioritize exact matches. Retrieved code snippets, comments and dependency metadata are then provided to the LLM, which can answer questions, suggest fixes, or generate new code while citing the source files. Evaluation should consider correctness of the code, type safety and adherence to dependencies.

<a id="Ch12.S5.SS2"></a>


##### 12.5.2 Code retrieval example using ASTs and embeddings

<a id="Ch12.S5.SS2.p1.1"></a>


Retrieving source code requires understanding its syntax and semantics. An easy approach is to embed code snippets and natural language queries with a pretrained model such as CodeBERT [[Feng et al., 2020](#bibk.bib11)]. Another complementary approach is to parse the code into an abstract syntax tree (AST) and search its structure. The example in Listing [12.7](#Ch12.F7 "Figure 12.7 ‣ 12.5.2 Code retrieval example using ASTs and embeddings ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") demonstrates both: we embed functions with CodeBERT for semantic search and use Python’s ast module to extract function definitions and docstrings for indexing.

<a id="Ch12.F7"></a>


[⬇](data:text/plain;base64,ZnJvbSB0cmFuc2Zvcm1lcnMgaW1wb3J0IEF1dG9Ub2tlbml6ZXIsIEF1dG9Nb2RlbAppbXBvcnQgdG9yY2gsIGFzdCwgaW5zcGVjdAoKdG9rZW5pemVyID0gQXV0b1Rva2VuaXplci5mcm9tX3ByZXRyYWluZWQoIm1pY3Jvc29mdC9jb2RlYmVydC1iYXNlIikKbW9kZWwgPSBBdXRvTW9kZWwuZnJvbV9wcmV0cmFpbmVkKCJtaWNyb3NvZnQvY29kZWJlcnQtYmFzZSIpCgpkZWYgZW5jb2RlX2NvZGUoY29kZV9zdHIpOgogICAgaW5wdXRzID0gdG9rZW5pemVyKGNvZGVfc3RyLCByZXR1cm5fdGVuc29ycz0icHQiKQogICAgd2l0aCB0b3JjaC5ub19ncmFkKCk6CiAgICAgICAgZW1iZWRkaW5ncyA9IG1vZGVsKCoqaW5wdXRzKS5sYXN0X2hpZGRlbl9zdGF0ZS5tZWFuKGRpbT0xKQogICAgcmV0dXJuIGVtYmVkZGluZ3MKCmRlZiBleHRyYWN0X2Z1bmN0aW9ucyhtb2R1bGUpOgogICAgIiIiUmV0dXJuIGEgbGlzdCBvZiAobmFtZSwgc291cmNlLCBkb2NzdHJpbmcpIHR1cGxlcy4iIiIKICAgIGZ1bmN0aW9ucyA9IFtdCiAgICBmb3IgbmFtZSwgb2JqIGluIGluc3BlY3QuZ2V0bWVtYmVycyhtb2R1bGUsIGluc3BlY3QuaXNmdW5jdGlvbik6CiAgICAgICAgc291cmNlID0gaW5zcGVjdC5nZXRzb3VyY2Uob2JqKQogICAgICAgIGRvYyA9IGluc3BlY3QuZ2V0ZG9jKG9iaikgb3IgIiIKICAgICAgICBmdW5jdGlvbnMuYXBwZW5kKChuYW1lLCBzb3VyY2UsIGRvYykpCiAgICByZXR1cm4gZnVuY3Rpb25zCgojIEluZGV4IGEgbW9kdWxlJ3MgZnVuY3Rpb25zCmltcG9ydCBleGFtcGxlX21vZHVsZSAgIyB5b3VyIGNvZGViYXNlCmZ1bmN0aW9ucyA9IGV4dHJhY3RfZnVuY3Rpb25zKGV4YW1wbGVfbW9kdWxlKQplbWJlZGRpbmdzID0gW2VuY29kZV9jb2RlKHNyYykgZm9yIChfLCBzcmMsIF8pIGluIGZ1bmN0aW9uc10KCmRlZiBzZWFyY2hfY29kZShxdWVyeSwgaz0yKToKICAgIHF1ZXJ5X2VtYiA9IGVuY29kZV9jb2RlKHF1ZXJ5KQogICAgc2NvcmVzID0gW3RvcmNoLm5uLmZ1bmN0aW9uYWwuY29zaW5lX3NpbWlsYXJpdHkocXVlcnlfZW1iLCBlbWIpWzBdCiAgICAgICAgZm9yIGVtYiBpbiBlbWJlZGRpbmdzXQogICAgIyBSZXR1cm4gdGhlIHRvcC1rIGZ1bmN0aW9ucyB3aXRoIGhpZ2hlc3Qgc2ltaWxhcml0eQogICAgdG9wayA9IHNvcnRlZCh6aXAoc2NvcmVzLCBmdW5jdGlvbnMpLCBrZXk9bGFtYmRhIHg6IHhbMF0sIHJldmVyc2U9VHJ1ZSlbOmtdCiAgICBmb3Igc2NvcmUsIChuYW1lLCBzcmMsIGRvYykgaW4gdG9wazoKICAgICAgICBwcmludChuYW1lLCAiKHNjb3JlOiIsIHNjb3JlLml0ZW0oKSwgIilcbiIsIGRvYykKCiMgRXhhbXBsZSB1c2FnZTogc2VhcmNoIGZvciBhIHNvcnRpbmcgZnVuY3Rpb24Kc2VhcmNoX2NvZGUoInNvcnQgYSBsaXN0IG9mIG51bWJlcnMiKQ==)

1
**from** transformers **import** AutoTokenizer, AutoModel

2
**import** torch, ast, inspect

3

4
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")

5
model = AutoModel.from_pretrained("microsoft/codebert-base")

6

7
**def** encode_code(code_str):

8
 inputs = tokenizer(code_str, return_tensors="pt")

9
 with torch.no_grad():

10
 embeddings = model(\*\*inputs).last_hidden_state.mean(dim=1)

11
 **return** embeddings

12

13
**def** extract_functions(module):

14
 """Return␣a␣list␣of␣(name,␣source,␣docstring)␣tuples."""

15
 functions = []

16
 **for** name, obj **in** inspect.getmembers(module, inspect.isfunction):

17
 source = inspect.getsource(obj)

18
 doc = inspect.getdoc(obj) **or** ""

19
 functions.append((name, source, doc))

20
 **return** functions

21

22
*# Index a module’s functions*

23
**import** example_module *# your codebase*

24
functions = extract_functions(example_module)

25
embeddings = [encode_code(src) **for** (_, src, _) **in** functions]

26

27
**def** search_code(query, k=2):

28
 query_emb = encode_code(query)

29
 scores = [torch.nn.functional.cosine_similarity(query_emb, emb)[0]

30
 **for** emb **in** embeddings]

31
 *# Return the top-k functions with highest similarity*

32
 topk = **sorted**(**zip**(scores, functions), key=**lambda** x: x[0], reverse=True)[:k]

33
 **for** score, (name, src, doc) **in** topk:

34
 **print**(name, "(score:", score.item(), ")\n", doc)

35

36
*# Example usage: search for a sorting function*

37
search_code("sort␣a␣list␣of␣numbers")

Figure 12.7: An Example of Code-based Retrieval in Python

This example indexes the functions in an imported module and performs a cosine similarity search between the query and the encoded source code. In practice one might combine code embeddings with lexical features (identifiers, comments) and incorporate AST‑based matching to handle structural queries (e.g., find all functions that call a specific API). Code‑aware retrieval is essential for agentic systems that need to read, execute or modify existing code during tool use.

<a id="Ch12.S5.SS3"></a>


##### 12.5.3 Multi-modal and heterogeneous sources

<a id="Ch12.S5.SS3.SSS0.Px1"></a>


###### Tabular and other heterogeneous documents

<a id="Ch12.S5.SS3.SSS0.Px1.p1.1"></a>


Existing RAG approaches face critical limitations when applied to heterogeneous documents, comprising both textual and tabular components [[Yu et al., 2025](#bibk.bib12)]. A primary challenge is *Structural Information Loss*. When tabular data is linearized or chunked for text-based RAG, its inherent relational structure, the interdependence of rows and columns, is compromised. This loss of structure impedes the LLM’s ability to perform accurate multi-hop heterogeneous reasoning. This indicates that merely converting non-textual data to text is insufficient. To address these challenges, hybrid frameworks such as *TableRAG* [[Yu et al., 2025](#bibk.bib12)] have been proposed, that unify textual understanding and complex manipulations over tabular data.

<a id="Ch12.S5.SS3.SSS0.Px1.p2.1"></a>


TableRAG employs SQL programming and execution to treat table-related queries as indivisible reasoning units, thereby enhancing both computational efficiency and reasoning fidelity. Similarly, *MixRAG* [[Zhang et al., 2025](#bibk.bib13)] has been shown to significantly improve retrieval performance for heterogeneous document RAG, which demands joint retrieval and reasoning across textual and hierarchical tabular data.

The success of these approaches demonstrates that a purely neural (embedding-based) RAG approach is insufficient for structured data. The integration of symbolic reasoning (e.g., SQL) alongside neural retrieval is a critical design pattern for heterogeneous RAG, reflecting a broader trend in Agentic LLMs towards neuro-symbolic integration for enhanced data understanding and fidelity.

<a id="Ch12.S5.SS3.SSS0.Px2"></a>


###### Multi-modal RAG

Many knowledge bases contain tables, figures, diagrams, audio and video. A straightforward approach is to extract any textual content using OCR and treat the remainder as plain text. A richer approach stores embeddings for images or other modalities (e.g., CLIP or ViT representations) and pairs them with captions and context. Queries can be encoded jointly across modalities, allowing the system to retrieve relevant figures or equations that accompany the text. For example, a research agent might retrieve a plot and its caption to answer a data‑analysis question, or an educational agent might fetch diagrams from a textbook.

Multi-modal RAG remains an active research area. Challenges include cross‑modal alignment and efficient indexing of high‑dimensional embeddings. Furthermore, non‑textual evidence should be properly grounded in the generated answer.

<a id="Ch12.S5.SS4"></a>


##### 12.5.4 Multi-modal retrieval example

Agentic systems sometimes need to retrieve images, diagrams or audio clips in addition to text. Multi-modal models such as CLIP or Contrastive Language‑Audio Pretraining (CLAP) embed both natural language and other modalities into a shared space. The high‑level pseudo-code in Listing [12.8](#Ch12.F8 "Figure 12.8 ‣ 12.5.4 Multi-modal retrieval example ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") outlines how to use CLIP to find images relevant to a textual query:

<a id="Ch12.F8"></a>


[⬇](data:text/plain;base64,ZnJvbSBQSUwgaW1wb3J0IEltYWdlCmltcG9ydCBjbGlwLCB0b3JjaAoKbW9kZWwsIHByZXByb2Nlc3MgPSBjbGlwLmxvYWQoIlZpVC1CLzMyIikKCmRlZiBlbWJlZF9pbWFnZShwYXRoKToKICAgIGltYWdlID0gcHJlcHJvY2VzcyhJbWFnZS5vcGVuKHBhdGgpKS51bnNxdWVlemUoMCkKICAgIHdpdGggdG9yY2gubm9fZ3JhZCgpOgogICAgICAgIHJldHVybiBtb2RlbC5lbmNvZGVfaW1hZ2UoaW1hZ2UpCgpkZWYgZW1iZWRfdGV4dCh0ZXh0KToKICAgIHRleHRfdG9rZW5zID0gY2xpcC50b2tlbml6ZShbdGV4dF0pCiAgICB3aXRoIHRvcmNoLm5vX2dyYWQoKToKICAgICAgICByZXR1cm4gbW9kZWwuZW5jb2RlX3RleHQodGV4dF90b2tlbnMpCgojIEJ1aWxkIGFuIGluZGV4IG9mIGltYWdlIGVtYmVkZGluZ3MKaW1hZ2VfcGF0aHMgPSBbImNhdC5qcGciLCAiZG9nLnBuZyIsICJjaXR5LnBuZyJdCmltYWdlX2VtYnMgPSBbZW1iZWRfaW1hZ2UocCkgZm9yIHAgaW4gaW1hZ2VfcGF0aHNdCgpkZWYgc2VhcmNoX2ltYWdlcyhxdWVyeSwgaz0yKToKICAgIHF1ZXJ5X2VtYiA9IGVtYmVkX3RleHQocXVlcnkpCiAgICBzY29yZXMgPSBbdG9yY2gubm4uZnVuY3Rpb25hbC5jb3NpbmVfc2ltaWxhcml0eShxdWVyeV9lbWIsIGVtYilbMF0KICAgICAgICBmb3IgZW1iIGluIGltYWdlX2VtYnNdCiAgICB0b3BrID0gc29ydGVkKHppcChzY29yZXMsIGltYWdlX3BhdGhzKSwga2V5PWxhbWJkYSB4OiB4WzBdLCByZXZlcnNlPVRydWUpWzprXQogICAgcmV0dXJuIHRvcGsKCiMgRXhhbXBsZSB1c2FnZTogc2VhcmNoIGZvciBhIHBpY3R1cmUgb2YgYSBjaXR5CnByaW50KHNlYXJjaF9pbWFnZXMoImEgc2t5bGluZSBvZiBhIGxhcmdlIEV1cm9wZWFuIGNpdHkiKSk=)

1
**from** PIL **import** Image

2
**import** clip, torch

3

4
model, preprocess = clip.load("ViT-B/32")

5

6
**def** embed_image(path):

7
 image = preprocess(Image.**open**(path)).unsqueeze(0)

8
 with torch.no_grad():

9
 **return** model.encode_image(image)

10

11
**def** embed_text(text):

12
 text_tokens = clip.tokenize([text])

13
 with torch.no_grad():

14
 **return** model.encode_text(text_tokens)

15

16
*# Build an index of image embeddings*

17
image_paths = ["cat.jpg", "dog.png", "city.png"]

18
image_embs = [embed_image(p) **for** p **in** image_paths]

19

20
**def** search_images(query, k=2):

21
 query_emb = embed_text(query)

22
 scores = [torch.nn.functional.cosine_similarity(query_emb, emb)[0]

23
 **for** emb **in** image_embs]

24
 topk = **sorted**(**zip**(scores, image_paths), key=**lambda** x: x[0], reverse=True)[:k]

25
 **return** topk

26

27
*# Example usage: search for a picture of a city*

28
**print**(search_images("a␣skyline␣of␣a␣large␣European␣city"))

Figure 12.8: An Example of How to Use CLIP to Find Relevant Images in Python

The multimodal retrieval returns the filenames of the most similar images. In a RAG setting the retrieved images could be fed through a vision encoder to extract captions or objects, which are then incorporated into the context for the language model. Multimodal agents can thus ground their outputs in both textual and visual evidence.

<a id="Ch12.S6"></a>


#### 12.6 Agentic RAG: Beyond Simple Retrieval

<a id="Ch12.S6.p1.1"></a>


While traditional RAG systems augment LLMs with external knowledge, they are often passive, relying on a static, pre-defined pipeline. A significant and recent advancement is the concept of *Agentic RAG*, which integrates autonomous AI agents directly into the retrieval-augmented generation pipeline [[Singh et al., 2025](#bibk.bib14)]. This paradigm shift moves RAG from a mere tool to an active, intelligent, and agent-driven process. Agentic RAG systems are characterized by their ability to dynamically manage retrieval strategies, iteratively refine contextual understanding, and adapt workflows to meet complex task requirements.

<a id="Ch12.S6.p2.1"></a>


Agentic RAG represents a more sophisticated form of a retrieval loop, where the LLM agent itself is responsible for orchestrating the retrieval process. This differs from simpler RAG methods by embracing a continuous feedback loop that is fundamental to advanced agentic systems. Rather than a single-shot query transformation, the agent can actively refine its queries based on intermediate results and ongoing interaction. This approach addresses the limitations of conventional RAG systems, which are often constrained by static workflows and lack the adaptability required for multistep reasoning and complex task management [[Singh et al., 2025](#bibk.bib14)].

<a id="Ch12.S6.SS1"></a>


##### 12.6.1 Key Components of Agentic RAG

Agentic RAG frameworks typically incorporate several key components that enable their dynamic behavior:

- Dynamic Query Generation: The agent formulates queries based on its current understanding of the task and the retrieved context, allowing for more precise and effective searches. This can include query expansion, decomposition, or rewriting in response to initial retrieval failures.
- Iterative Refinement: The agent evaluates the quality of the retrieved information and, if necessary, initiates a new retrieval cycle with a refined query. This iterative process ensures that the final response is grounded in the most relevant and accurate information.
- Autonomous Tool Use: The agent can select and use a variety of tools, including different retrieval models (e.g., dense vs. sparse), ranking algorithms, and external APIs, to optimize its retrieval strategy. See Chapter [11](chapter-11-how-agents-use-tools-to-act-in-the-world.md#Ch11 "Chapter 11 How Agents Use Tools to Act in the World ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models") for additional information on how an agent can use tools.
- Self-Correction and Reflection: The agent can assess its own output for accuracy and completeness. If it detects a hallucination or an unsupported claim, it can trigger a new retrieval and reasoning process to correct the error.

The rise of Agentic RAG indicates a shift in the role of RAG in LLM systems. Retrieval shifts from a passive data lookup to an active, intelligent capability that is integral to the agent’s cognitive functions, allowing for more sophisticated, adaptive interactions with external knowledge sources. This shift is crucial for developing robust and reliable LLM agents capable of handling complex, real-world tasks.

<a id="Ch12.S6.SS2"></a>


##### 12.6.2 Real-Time and Streaming RAG

While traditional RAG systems are effective for static data, they are often not designed for applications that require continuous, real-time information. This section looks into the architectural considerations and challenges of RAG systems that operate on continuously updating, high-throughput data streams. Examples of such streams are found in news feeds, social media, or financial markets. For streaming data, simply querying an updated static index no longer suffices. Retrieval now involves dynamic index management and continuous knowledge assimilation.

<a id="Ch12.S6.SS2.p2.1"></a>


In traditional RAG systems, designed for static data, preprocessing is slow, and unsuitable for real-time analysis [[Zhu, 2025](#bibk.bib15), [Sankaradas et al., 2025](#bibk.bib16)]. How should we maintain data freshness and semantic coverage under memory budgets and high data ingestion rates? Methods such as *StreamingRAG* [[Sankaradas et al., 2025](#bibk.bib16)] try to overcome these issues with knowledge graphs that evolve dynamically in real-time.

LLM agents for dynamic domains such as medicine, logistics and finance, must have access to real-time, continuously updated information. Static RAG would yield obsolete or inaccurate information in such fast-changing environments. In many agentic applications real-time RAG is necessary for advanced, timely, and reliable information.

<a id="Ch12.S7"></a>


#### 12.7 Evaluation

Evaluating a retrieval‑augmented system is more difficult than evaluating a stand‑alone language model because both the retriever and the generator contribute to the final answer. Good evaluation should separate these components and also judge their joint behavior.

<a id="Ch12.S7.SS0.SSS0.Px1"></a>


###### Retrieval metrics

For a given query, we compare the retrieved passages to a set of gold documents. Standard metrics include:

1. recall@k (Eq. [12.7](#Ch12.E7 "In Retrieval metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")) and precision@k (Eq. [12.8](#Ch12.E8 "In Retrieval metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")), the fraction of relevant documents retrieved among the top $k$
2. mean reciprocal rank (Eq. [12.9](#Ch12.E9 "In Retrieval metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"))
   and mean average precision, which capture ranking quality
3. normalized discounted cumulative gain (NDCG) (Eq. [12.10](#Ch12.E10 "In Retrieval metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")), which weights higher ranks more heavily

<a id="Ch12.S7.SS0.SSS0.Px1.p1.2"></a>


BEIR presents a heterogeneous benchmark of 18 datasets covering tasks like question answering, fact checking and entity retrieval; their experiments show that late‑interaction and re‑ranking models improve zero‑shot performance but at increased cost [[Thakur et al., 2021](#bibk.bib20)].

<a id="Ch12.S7.SS0.SSS0.Px1.p2.1"></a>


KILT evaluates knowledge‑intensive tasks under a unified Wikipedia snapshot and measures both task performance and provenance, encouraging models to cite the passages they used [[Petroni et al., 2021](#bibk.bib21)].

<a id="Ch12.E7"></a>


|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{Recall@}k=\frac{|\{\text{relevant documents}\}\cap\{\text{top-}k\text{ retrieved}\}|}{|\{\text{relevant documents}\}|} $$ |  | (12.7) |

<a id="Ch12.E8"></a>


|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{Precision@}k=\frac{|\{\text{relevant documents}\}\cap\{\text{top-}k\text{ retrieved}\}|}{k} $$ |  | (12.8) |

<a id="Ch12.E9"></a>


|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{MRR}=\frac{1}{|Q|}\sum_{i=1}^{|Q|}\frac{1}{\mathrm{rank}_{i}} $$ |  | (12.9) |

where $\mathrm{rank}_{i}$ is the position of the first relevant document for query $i$.

<a id="Ch12.E10"></a>


|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{nDCG@}k=\frac{\mathrm{DCG@}k}{\mathrm{IDCG@}k} $$ |  | (12.10) |

with

|  |  |  |
| --- | --- | --- |
|  | $$ \mathrm{DCG@}k=\sum_{i=1}^{k}\frac{2^{\mathrm{rel}_{i}}-1}{\log_{2}(i+1)} $$ |  |

and $\mathrm{rel}_{i}$ the graded relevance of the document at rank $i$.

<a id="Ch12.S7.SS0.SSS0.Px2"></a>


###### Generation metrics

Once context is assembled, we must assess the quality of the generated answer. Automatic metrics such as BLEU, ROUGE and BERTScore are of limited use because there is often no single ground‑truth answer. More appropriate are *faithfulness* and *helpfulness*. Faithfulness is often measured via entailment models. It works as follows for generated output $y$ and retrieved context $x$ (Eq. [12.11](#Ch12.E11 "In Generation metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")): check whether every claim is supported by the cited passages, for example via natural language inference models or quote checking.

<a id="Ch12.E11"></a>


|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{Faithfulness}=\frac{\text{\# outputs entailed by context}}{\text{\# total outputs}} $$ |  | (12.11) |

Helpfulness (or utility) indicates whether the answer satisfies the user’s information need. To measure this, often human evaluation or specialized LLM‑based evaluators are needed. In interactive settings latency and cost are also important.

Helpfulness is based on human or model scoring:

|  |  |  |  |
| --- | --- | --- | --- |
|  | $$ \mathrm{Helpfulness}=\frac{\sum_{i=1}^{N}\text{score}(y_{i},\text{query}_{i})}{N} $$ |  | (12.12) |

where score is a Likert-scale or pairwise preference judgment.

<a id="Ch12.S7.SS0.SSS0.Px3"></a>


###### Joint evaluation and new metrics

<a id="Ch12.S7.SS0.SSS0.Px3.p1.1"></a>


A key challenge is to evaluate retrieval and generation separately. For example, a system may retrieve irrelevant documents but still guess the right answer, or retrieve perfect evidence but fail to use it. Recent work therefore proposes unified evaluation frameworks. The Auepora process recommends reporting separate retrieval and generation scores and then to combine them into a holistic measure [[Yu and others, 2024](#bibk.bib24)]. RAGAS and similar toolkits provide automated pipelines that compute context recall, answer correctness, and citation accuracy using small models. When we evaluate adaptive methods (Section [12.4](#Ch12.S4 "12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")), we also need to measure the trigger decisions: how often does the model retrieve when it should, and how often does it skip retrieval unnecessarily?

<a id="Ch12.S7.SS0.SSS0.Px4"></a>


###### Attribution and freshness

In many applications the model must cite its sources and avoid outdated information. Claims can be aligned with evidence by attribution tests. Such tests use natural language inference and ensure URL–answer consistency. Freshness metrics measure whether the answer reflects the most recent valid sources. This metric can also quantify version drift.

Attribution and freshness are especially important for time‑sensitive domains like finance or medicine.

A good system design is based on careful evaluation. When we find high retrieval recall but low faithfulness, then better re‑ranking is needed. Similarly, high faithfulness but poor helpfulness may indicate insufficient context coverage. To support error analysis and auditing, evaluations should be accompanied by transparent logging of queries, retrieved passages and model outputs.

<a id="Ch12.S8"></a>


#### 12.8 Concluding Remarks

Retrieval is an essential element of any agentic LLM system that needs to provide up-to-date information. Large language models are static snapshots of knowledge; RAG helps them stay up to date, transparent and grounded. Effective RAG requires careful engineering across indexing, query planning, retrieval, re‑ranking, context assembly and grounded generation, along with adaptive techniques that let the model decide when and how to search. We have also seen how retrieval can be extended beyond plain text to graphs, code and multimodal assets. For building trustworthy systems, rigorous evaluation is essential.

<a id="Ch12.S8.SS0.SSS0.Px1"></a>


###### Operational considerations

In production systems the retriever is a living service, not a one‑off script, and it should be maintained carefully. Crawlers, webhooks and document pipelines should continuously ingest new data. Be careful to track versions and deprecations, and maintain per‑entity timelines to prefer recent facts. Your system should apply access control lists at retrieval time and redact personally identifiable information during indexing. Latency and cost matter: cache embeddings and top-$k$ results, reuse retrieval across conversational turns, compress context with extractive summarization, tune $k$ and chunk sizes per domain, and re‑rank only the top candidates.

<a id="Ch12.S8.SS0.SSS0.Px2"></a>


###### Practical suggestions

When you create a RAG system, start with a hybrid approach: combine a strong dense retriever with BM25 or SPLADE and re-rank the top hundred hits with a cross‑encoder before sending six to twelve passages to the LLM. Be careful to chunk your corpus thoughtfully, for example using 300–500 token windows with 10–15 % overlap and preserved headings and tables, also attach timestamps or other metadata. For query writing, craft your queries carefully. Rewrite complex questions, decompose multi‑hop queries, expand entity aliases and enforce domain filters. For transparency, always require citations. If, however, the evidence is weak, ask follow‑up questions, or else abstain.

Finally, use evidence-based system design, measure what you build. You should track retrieval recall, groundedness, timeliness and cost. A further suggestion is to experiment with re-rankers. For debugging, you should log system traces.

**Try it yourself!**

Want to experiment with Retrieval-Augmented Generation?
Open our:
  
[**RAG tutorial** in Google Colab](https://colab.research.google.com/github/Agentic-LLMs/Agentic-AI-tutorials/blob/main/rag_tutorial.ipynb)

<a id="Ch12.S8.SS0.SSS0.Px3"></a>


###### Integration into agentic AI

Retrieval is an integral element of agentic LLMs, it is used in planning, self-reflection, and while acting in the real world (see Chapter [13](chapter-13-from-tools-to-assistants-real-world-applications.md#Ch13 "Chapter 13 From Tools to Assistants: Real-World Applications ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models")). Agentic pipelines can call the retriever dynamically based on the model’s confidence or plan, as in Self‑RAG and Graph Toolformer. They can query different data sources such as text, graphs, code and images, and leverage the strengths of each. The line between the *model* and its *memory* therefore blurs: RAG becomes part of the agent’s cognitive loop.

<a id="Ch12.S8.SS0.SSS0.Px4"></a>


###### Further Reading

<a id="Ch12.S8.SS0.SSS0.Px4.p1.1"></a>


For in‑depth exploration, consult the surveys on RAG, evaluation and graph‑based methods [[Gao and others, 2023](#bibk.bib22), [Huang and others, 2024](#bibk.bib23), [Yu and others, 2024](#bibk.bib24), [Sharma and others, 2025](#bibk.bib26), [Peng and others, 2024](#bibk.bib25)]. Foundational works include REALM, DPR and the original RAG formulation [[Guu et al., 2020](#bibk.bib5), [Karpukhin et al., 2020](#bibk.bib6), [Lewis et al., 2020](#bibk.bib3)]. The GraphRAG, evaluation and agentic RAG communities are evolving rapidly; following their latest papers and benchmarks is the best way to stay current.

<a id="bibk"></a>


### References

<a id="bibk.bib19"></a>
- Asai et al. (2023)
  A. Asai, V. Zhong, S. Chen, H. Hajishirzi, et al.
  Self-rag: learning to retrieve, generate, and critique for language models.
  arXiv preprint arXiv:2310.11511.
  Cited by: [item 6](#Ch12.S3.I1.i6.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.4.1](#Ch12.S4.SS1.p1.1 "12.4.1 Adaptive Retrieval via Self‑RAG and Self-Ask ‣ 12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.4](#Ch12.S4.p2.1 "12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib2"></a>
- Cong et al. (2024)
  Y. Cong, C. Wang, P. S. Akash, and K. C. Chang
  Query optimization for parametric knowledge refinement in retrieval-augmented large language models.
  arXiv preprint arXiv:2411.07820.
  Cited by: [§12.2](#Ch12.S2.p2.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib30"></a>
- Deerwester et al. (1990)
  S. Deerwester, S. T. Dumais, G. W. Furnas, T. K. Landauer, and R. Harshman
  Indexing by latent semantic analysis.
  Journal of the American Society for Information Science 41 (6), pp. 391–407.
  External Links: [Document](https://dx.doi.org/10.1002/%28SICI%291097-4571%28199009%2941%3A6%3C391%3A%3AAID-ASI1%3E3.0.CO%3B2-9)
  Cited by: [§12.1.3](#Ch12.S1.SS3.p2.1 "12.1.3 Latent and Sparse Representations ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib11"></a>
- Feng et al. (2020)
  Z. Feng, D. Guo, D. Tang, N. Duan, X. Feng, M. Gong, L. Shou, B. Qin, T. Liu, D. Jiang, and M. Zhou
  CodeBERT: a pre-trained model for programming and natural languages.
  Note: Accepted to Findings of EMNLP 2020
  External Links: 2002.08155,
  [Link](https://arxiv.org/abs/2002.08155)
  Cited by: [§12.5.1](#Ch12.S5.SS1.SSS0.Px1.p1.1 "Code‑RAG ‣ 12.5.1 Graph‑based retrieval example ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.5.2](#Ch12.S5.SS2.p1.1 "12.5.2 Code retrieval example using ASTs and embeddings ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib7"></a>
- Formal et al. (2021)
  T. Formal, C. Lassance, B. Piwowarski, and S. Clinchant
  SPLADE v2: sparse lexical and expansion model for information retrieval.
  arXiv preprint arXiv:2109.10086.
  Cited by: [item 1](#Ch12.S3.I1.i1.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib18"></a>
- Gao et al. (2023)
  L. Gao, Z. Dai, and J. Callan
  HyDE: Hypothetical document embeddings for zero-shot dense retrieval.
  In NeurIPS,
  Cited by: [item 2](#Ch12.S3.I1.i2.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [footnote 1](#Ch12.footnote1 "In 12.4.3 Query Rewriting and Expansion ‣ 12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib22"></a>
- Gao et al. (2023)
  Y. Gao et al.
  Retrieval-augmented generation for large language models: a survey.
  arXiv preprint arXiv:2312.10997.
  Cited by: [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib5"></a>
- Guu et al. (2020)
  K. Guu, K. Lee, Z. Tung, P. Pasupat, and M. Chang
  Retrieval augmented language model pre-training.
  In Proceedings of the 37th International Conference on Machine Learning, H. D. III and A. Singh (Eds.),
  Proceedings of Machine Learning Research, Vol. 119, pp. 3929–3938.
  External Links: [Link](https://proceedings.mlr.press/v119/guu20a.html)
  Cited by: [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib23"></a>
- Huang et al. (2024)
  Y. Huang et al.
  A survey on retrieval-augmented text generation for large language models.
  arXiv preprint arXiv:2404.10981.
  Cited by: [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib8"></a>
- Izacard et al. (2022)
  G. Izacard, M. Caron, L. Hosseini, S. Riedel, P. Bojanowski, A. Joulin, and E. Grave
  Unsupervised dense information retrieval with contrastive learning.
  Transactions on Machine Learning Research.
  Note: 
  External Links: ISSN 2835-8856,
  [Link](https://openreview.net/forum?id=jKN1pXi7b0)
  Cited by: [item 3](#Ch12.S3.I1.i3.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib10"></a>
- Jégou et al. (2011)
  H. Jégou, M. Douze, and C. Schmid
  Product quantization for nearest neighbor search.
  IEEE Transactions on Pattern Analysis and Machine Intelligence 33 (1), pp. 117–128.
  External Links: [Document](https://dx.doi.org/10.1109/TPAMI.2010.57)
  Cited by: [item 3](#Ch12.S3.I1.i3.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib6"></a>
- Karpukhin et al. (2020)
  V. Karpukhin, B. Oguz, S. Min, P. Lewis, L. Wu, S. Edunov, D. Chen, and W. Yih
  Dense passage retrieval for open-domain question answering.
  In Empirical Methods in Natural Language Processing,
  Cited by: [§12.1.2](#Ch12.S1.SS2.p2.2 "12.1.2 Vector Space Models ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [item 3](#Ch12.S3.I1.i3.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib3"></a>
- Lewis et al. (2020)
  P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, et al.
  Retrieval-augmented generation for knowledge-intensive nlp tasks.
  Advances in Neural Information Processing Systems 33, pp. 9459–9474.
  Cited by: [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib17"></a>
- Malkov and Yashunin (2020)
  Y. A. Malkov and D. A. Yashunin
  Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.
  IEEE Trans. Pattern Anal. Mach. Intell. 42 (4), pp. 824–836.
  External Links: ISSN 0162-8828,
  [Link](https://doi.org/10.1109/TPAMI.2018.2889473),
  [Document](https://dx.doi.org/10.1109/TPAMI.2018.2889473)
  Cited by: [item 3](#Ch12.S3.I1.i3.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib33"></a>
- Manning et al. (2008)
  C. D. Manning, P. Raghavan, and H. Schütze
  Introduction to information retrieval.
   Cambridge University Press, Cambridge, UK.
  Cited by: [§12.1](#Ch12.S1.p1.1 "12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib34"></a>
- Mikolov et al. (2013)
  T. Mikolov, K. Chen, G. Corrado, and J. Dean
  Efficient estimation of word representations in vector space.
  In 1st International Conference on Learning Representations, ICLR 2013,
  Scottsdale, Arizona, USA, May 2-4, 2013, Workshop Track Proceedings, Y. Bengio and Y. LeCun (Eds.),
  External Links: [Link](http://arxiv.org/abs/1301.3781)
  Cited by: [§12.1.3](#Ch12.S1.SS3.p4.1 "12.1.3 Latent and Sparse Representations ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib25"></a>
- Peng et al. (2024)
  B. Peng et al.
  Graph retrieval-augmented generation: a survey.
  arXiv preprint arXiv:2408.08921.
  Cited by: [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.5](#Ch12.S5.SS0.SSS0.Px1.p1.1 "Graph‑RAG ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.5.1](#Ch12.S5.SS1.p1.1 "12.5.1 Graph‑based retrieval example ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib21"></a>
- Petroni et al. (2021)
  F. Petroni, A. Piktus, A. Fan, P. Lewis, et al.
  KILT: a benchmark for knowledge intensive language tasks.
  In NAACL,
  Cited by: [§12.7](#Ch12.S7.SS0.SSS0.Px1.p2.1 "Retrieval metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib4"></a>
- Press et al. (2022)
  O. Press, M. Zhang, S. Min, L. Schmidt, N. A. Smith, and M. Lewis
  Measuring and narrowing the compositionality gap in language models.
  arXiv preprint arXiv:2210.03350.
  Cited by: [§12.4.1](#Ch12.S4.SS1.p2.1 "12.4.1 Adaptive Retrieval via Self‑RAG and Self-Ask ‣ 12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.4](#Ch12.S4.p3.1 "12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib32"></a>
- Robertson et al. (1994)
  S. E. Robertson, S. Walker, S. Jones, M. M. Hancock-Beaulieu, M. Gatford, et al.
  Okapi at trec.
  NIST special publication.
  Cited by: [§12.1.3](#Ch12.S1.SS3.p1.1 "12.1.3 Latent and Sparse Representations ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib31"></a>
- Robertson and Zaragoza (2009)
  S. Robertson and H. Zaragoza
  The probabilistic relevance framework: bm25 and beyond.
  Foundations and Trends in Information Retrieval 3 (4), pp. 333–389.
  External Links: [Document](https://dx.doi.org/10.1561/1500000019)
  Cited by: [§12.1.3](#Ch12.S1.SS3.p1.1 "12.1.3 Latent and Sparse Representations ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib27"></a>
- Salton and McGill (1983)
  G. Salton and M. J. McGill
  Introduction to modern information retrieval.
   McGraw-Hill, New York, NY.
  Cited by: [§12.1](#Ch12.S1.p1.1 "12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib29"></a>
- Salton et al. (1975)
  G. Salton, A. Wong, and C. Yang
  A vector space model for automatic indexing.
  Communications of the ACM 18 (11), pp. 613–620.
  External Links: [Document](https://dx.doi.org/10.1145/361219.361220)
  Cited by: [§12.1.2](#Ch12.S1.SS2.p1.1 "12.1.2 Vector Space Models ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib16"></a>
- Sankaradas et al. (2025)
  M. Sankaradas, R. K. Rajendran, and S. T. Chakradhar
  StreamingRAG: real-time contextual retrieval and generation framework.
  External Links: 2501.14101,
  [Link](https://arxiv.org/abs/2501.14101)
  Cited by: [§12.6.2](#Ch12.S6.SS2.p2.1 "12.6.2 Real-Time and Streaming RAG ‣ 12.6 Agentic RAG: Beyond Simple Retrieval ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib9"></a>
- Santhanam et al. (2022)
  K. Santhanam, O. Khattab, C. Potts, and M. Zaharia
  ColBERTv2: effective and efficient retrieval via lightweight late interaction.
  In NAACL,
  Cited by: [item 4](#Ch12.S3.I1.i4.p1.1 "In 12.3 Retrieval-Augmented Generation Pipeline ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib26"></a>
- Sharma et al. (2025)
  C. Sharma et al.
  Retrieval-augmented generation.
  arXiv preprint arXiv:2506.00054.
  Cited by: [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib14"></a>
- Singh et al. (2025)
  A. Singh, A. Ehtesham, S. Kumar, and T. T. Khoei
  Agentic retrieval-augmented generation: a survey on agentic rag.
  arXiv preprint arXiv:2501.09136.
  Cited by: [§12.6](#Ch12.S6.p1.1 "12.6 Agentic RAG: Beyond Simple Retrieval ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.6](#Ch12.S6.p2.1 "12.6 Agentic RAG: Beyond Simple Retrieval ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib28"></a>
- Spärck Jones (1972)
  K. Spärck Jones
  A statistical interpretation of term specificity and its application in retrieval.
  Journal of Documentation 28 (1), pp. 11–21.
  External Links: [Document](https://dx.doi.org/10.1108/eb026526)
  Cited by: [§12.1.1](#Ch12.S1.SS1.p1.1 "12.1.1 Bag of Words ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.1.1](#Ch12.S1.SS1.p2.2 "12.1.1 Bag of Words ‣ 12.1 Retrieval in General ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib20"></a>
- Thakur et al. (2021)
  N. Thakur, N. Reimers, J. Daxenberger, and I. Gurevych
  BEIR: a heterogeneous benchmark for zero-shot evaluation of information retrieval models.
  In NeurIPS Datasets and Benchmarks,
  Cited by: [§12.7](#Ch12.S7.SS0.SSS0.Px1.p1.2 "Retrieval metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib24"></a>
- Yu et al. (2024)
  H. Yu et al.
  Evaluation of retrieval-augmented generation: a survey.
  arXiv preprint arXiv:2405.07437.
  Cited by: [§12.2](#Ch12.S2.p3.1 "12.2 Why Retrieval Matters for Agentic LLMs ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.7](#Ch12.S7.SS0.SSS0.Px3.p1.1 "Joint evaluation and new metrics ‣ 12.7 Evaluation ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models"),
  [§12.8](#Ch12.S8.SS0.SSS0.Px4.p1.1 "Further Reading ‣ 12.8 Concluding Remarks ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib12"></a>
- Yu et al. (2025)
  X. Yu, P. Jian, and C. Chen
  TableRAG: a retrieval augmented generation framework for heterogeneous document reasoning.
  External Links: 2506.10380,
  [Link](https://arxiv.org/abs/2506.10380)
  Cited by: [§12.5.3](#Ch12.S5.SS3.SSS0.Px1.p1.1 "Tabular and other heterogeneous documents ‣ 12.5.3 Multi-modal and heterogeneous sources ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib13"></a>
- Zhang et al. (2025)
  C. Zhang, Q. Chen, and M. Zhang
  Mixture-of-rag: integrating text and tables with large language models.
  External Links: 2504.09554,
  [Link](https://arxiv.org/abs/2504.09554)
  Cited by: [§12.5.3](#Ch12.S5.SS3.SSS0.Px1.p2.1 "Tabular and other heterogeneous documents ‣ 12.5.3 Multi-modal and heterogeneous sources ‣ 12.5 Beyond Text: Graphs, Code, Tabular Data and Multi-Modal ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib1"></a>
- Zhang (2023)
  J. Zhang
  Graph-toolformer: to empower llms with graph reasoning ability via prompt augmented by chatgpt.
  arXiv preprint arXiv:2304.11116.
  Cited by: [§12.4](#Ch12.S4.p3.1 "12.4 Adaptive Retrieval Methods ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
<a id="bibk.bib15"></a>
- Zhu (2025)
  Y. Zhu
  From static to dynamic: a streaming rag approach to real-time knowledge base.
  External Links: 2508.05662,
  [Link](https://arxiv.org/abs/2508.05662)
  Cited by: [§12.6.2](#Ch12.S6.SS2.p2.1 "12.6.2 Real-Time and Streaming RAG ‣ 12.6 Agentic RAG: Beyond Simple Retrieval ‣ Chapter 12 Search and Retrieval in Agentic LLMs ‣ Part IV Tools and Assistants ‣ Agentic Large Language Models").
