# Retrieval, data, and knowledge techniques

Ways to retrieve evidence, query data, extract structured knowledge, and reconcile information.

Preparation of data for weight updates belongs under training. Retrieval metrics belong under evaluation. Research applications remain separate from their methods.

[All categories](README.md) · [CSV](retrieval-knowledge.csv) · [Category method](METHOD.md) · [Full analysis](../README.md)

**19 concepts**: 18 confirmed in courses; 1 confirmed only in the book.

## Frequency dictionary

Frequency counts distinct courses. Taught and assigned counts form the total. The book and schedule-only topics do not increase course frequency. Original types are preserved from the shared dictionary.

| Concept | Original type | Courses / 7 | Taught | Assigned | Courses | Schedule only | Book |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| [Retrieval-augmented generation](#concept-rag) | topic | 5 | 4 | 1 | S329, COL, CMU, S224, CU |  | yes |
| [Embedding-based retrieval](#concept-embeddings) | method | 4 | 4 | 0 | S329, COL, CMU, S224 |  | yes |
| [Sparse retrieval](#concept-sparse-retrieval) | method | 4 | 4 | 0 | S329, COL, CMU, S224 |  | yes |
| [Document chunking and indexing](#concept-chunking) | method | 3 | 3 | 0 | S329, COL, S224 |  | yes |
| [Knowledge curation and synthesis](#concept-knowledge-curation) | topic | 3 | 2 | 1 | CMU, S224, CU |  |  |
| [Agentic retrieval](#concept-agentic-rag) | pattern | 2 | 2 | 0 | S329, CMU |  | yes |
| [Hybrid retrieval](#concept-hybrid-search) | method | 2 | 2 | 0 | S329, COL |  | yes |
| [Reranking and late interaction](#concept-reranking) | method | 2 | 2 | 0 | S329, S224 |  | yes |
| [Schema induction and information extraction](#concept-schema-induction) | method | 2 | 1 | 1 | S224, CU |  |  |
| [Concept canonicalization and ontologies](#concept-canonicalization) | method | 1 | 1 | 0 | S224 |  |  |
| [Constraint-satisfaction retrieval](#concept-constraint-retrieval) | method | 1 | 1 | 0 | S224 |  |  |
| [Database reconciliation and deduplication](#concept-data-reconciliation) | method | 1 | 1 | 0 | S224 |  |  |
| [Graph-based retrieval](#concept-graph-rag) | method | 1 | 1 | 0 | S329 |  | yes |
| [Hypothesis and evidence ledger](#concept-hypothesis-ledger) | pattern | 1 | 1 | 0 | S224 |  |  |
| [Missing-data imputation and assumptions](#concept-imputation) | method | 1 | 1 | 0 | S224 |  |  |
| [Perspective-guided research](#concept-perspective-search) | pattern | 1 | 1 | 0 | S224 |  |  |
| [Queries over structured and unstructured data](#concept-hybrid-data) | method | 1 | 1 | 0 | S224 |  |  |
| [Semantic parsing to formal queries](#concept-semantic-parsing) | method | 1 | 1 | 0 | S224 |  |  |
| [Query rewriting and expansion](#concept-query-rewriting) | method | 0 | 0 | 0 |  |  | yes |

## Course codes

- **S329**: [Engineering AI Agents](../courses/stanford-cs329z.md)
- **COL**: [Designing LLM Agents](../courses/columbia-coms4995.md)
- **CMU**: [AI Agents](../courses/cmu-11768.md)
- **LC**: [Introduction to Deep Agents](../courses/langchain-deep-agents.md)
- **S224**: [Agentic AI](../courses/stanford-cs224v.md)
- **EVAL**: [Evaluating and Improving Agentic Applications](../courses/dlai-agentic-evals.md)
- **CU**: [Building AI Agents](../courses/colorado-csci7000.md)
- **BOOK**: [Agentic Large Language Models](../courses/agentic-large-language-models.md)

## Definitions and evidence

Entries follow frequency order. Related categories are navigation links; they do not create additional category membership or frequency.

<a id="concept-rag"></a>

### Retrieval-augmented generation

`rag` · Retrieval and indexing · original type: topic

Retrieve external information and use it to generate an answer.

**Aliases:** RAG; retrieval augmented generation.

**Evidence:** [S329, taught, p. 14](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [COL, taught, p. 47](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 6](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 15](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [CU, assigned, p. 10](../../courses/colorado-csci7000/markdown/readings/arxiv-2409-02977.md); [BOOK, taught, line 78](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-embeddings"></a>

### Embedding-based retrieval

`embeddings` · Retrieval and indexing · original type: method

Encode queries and documents as vectors and retrieve similar documents.

**Aliases:** dense retrieval; vector search.

**Related terms:** DPR.

**Evidence:** [S329, taught, p. 43](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [COL, taught, p. 51](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 101](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 17](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [BOOK, taught, line 368](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-sparse-retrieval"></a>

### Sparse retrieval

`sparse-retrieval` · Retrieval and indexing · original type: method

Rank documents with token-based relevance scores.

**Aliases:** lexical retrieval.

**Related terms:** BM25.

**Evidence:** [S329, taught, p. 41](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [COL, taught, p. 51](../../courses/columbia-coms4995/markdown/slides/week5.md); [CMU, taught, p. 100](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 18](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [BOOK, taught, line 39](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-chunking"></a>

### Document chunking and indexing

`chunking` · Retrieval and indexing · original type: method

Split source documents and build an index for retrieval.

**Aliases:** chunking; document indexing.

**Evidence:** [S329, taught, p. 24](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [COL, taught, p. 48](../../courses/columbia-coms4995/markdown/slides/week5.md); [S224, taught, p. 45](../../courses/stanford-cs224v/markdown/slides/i-sliders.md); [BOOK, taught, line 20](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-knowledge-curation"></a>

### Knowledge curation and synthesis

`knowledge-curation` · Knowledge processing · original type: topic

Search, organize, compare, and combine information into an evidence-based account.

**Aliases:** knowledge synthesis; evidence synthesis.

**Evidence:** [CMU, taught, p. 124](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2603-22327.md).

<a id="concept-agentic-rag"></a>

### Agentic retrieval

`agentic-rag` · Retrieval and indexing · original type: pattern

Let an agent decide when and how to retrieve and revise a search.

**Aliases:** agentic RAG.

**Related terms:** corrective RAG.

**Also relevant to:** [Architectural patterns](architecture.md).

**Evidence:** [S329, taught, p. 3](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [CMU, taught, p. 54](../../courses/cmu-11768/markdown/slides/lecture-10-deep-research-agents.md); [BOOK, taught, line 906](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-hybrid-search"></a>

### Hybrid retrieval

`hybrid-search` · Retrieval and indexing · original type: method

Combine lexical and embedding-based retrieval results.

**Aliases:** hybrid search.

**Related terms:** reciprocal rank fusion.

**Evidence:** [S329, taught, p. 49](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [COL, taught, p. 52](../../courses/columbia-coms4995/markdown/slides/week5.md); [BOOK, taught, line 106](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-reranking"></a>

### Reranking and late interaction

`reranking` · Retrieval and indexing · original type: method

Rescore retrieved candidates with richer query-document comparisons.

**Aliases:** cross-encoder reranking.

**Related terms:** ColBERT.

**Evidence:** [S329, taught, p. 50](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [S224, taught, p. 17](../../courses/stanford-cs224v/markdown/slides/l-freetext.md); [BOOK, taught, line 181](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-schema-induction"></a>

### Schema induction and information extraction

`schema-induction` · Knowledge processing · original type: method

Define or infer a structured schema and extract source evidence into it.

**Aliases:** automatic schematization; schema induction.

**Evidence:** [S224, taught, p. 40](../../courses/stanford-cs224v/markdown/slides/i-sliders.md); [CU, assigned, p. 1](../../courses/colorado-csci7000/markdown/readings/arxiv-2603-22327.md).

<a id="concept-canonicalization"></a>

### Concept canonicalization and ontologies

`canonicalization` · Knowledge processing · original type: method

Map varied terms to shared concepts and logical relations.

**Aliases:** terminology normalization; canonical concepts.

**Evidence:** [S224, taught, p. 17](../../courses/stanford-cs224v/markdown/slides/l-satir.md).

<a id="concept-constraint-retrieval"></a>

### Constraint-satisfaction retrieval

`constraint-retrieval` · Retrieval and indexing · original type: method

Retrieve records whose formal constraints are satisfied instead of relying only on similarity.

**Aliases:** satisfiability-based retrieval.

**Related terms:** SatIR.

**Evidence:** [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/slides/l-satir.md).

<a id="concept-data-reconciliation"></a>

### Database reconciliation and deduplication

`data-reconciliation` · Knowledge processing · original type: method

Resolve duplicate, conflicting, or partial extracted records while keeping provenance.

**Aliases:** chunk and reconcile; data reconciliation.

**Evidence:** [S224, taught, p. 40](../../courses/stanford-cs224v/markdown/slides/i-sliders.md).

<a id="concept-graph-rag"></a>

### Graph-based retrieval

`graph-rag` · Retrieval and indexing · original type: method

Use graph relations or graph summaries to support retrieval.

**Aliases:** GraphRAG; graph RAG.

**Evidence:** [S329, taught, p. 34](../../courses/stanford-cs329z/markdown/slides/lecture03.md); [BOOK, taught, line 526](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).

<a id="concept-hypothesis-ledger"></a>

### Hypothesis and evidence ledger

`hypothesis-ledger` · Research information management · original type: pattern

Track competing hypotheses, supporting evidence, refutations, and open questions.

**Aliases:** belief ledger; hypothesis tracking.

**Evidence:** [S224, taught, p. 1](../../courses/stanford-cs224v/markdown/assignments/cs224v-2026-hw1.md).

<a id="concept-imputation"></a>

### Missing-data imputation and assumptions

`imputation` · Knowledge processing · original type: method

Fill missing facts using stated policies and expose the resulting assumptions.

**Aliases:** data imputation.

**Related terms:** salience-based imputation.

**Also relevant to:** [Safety, security, and trust](safety-trust.md).

**Evidence:** [S224, taught, p. 21](../../courses/stanford-cs224v/markdown/slides/l-smt-match.md).

<a id="concept-perspective-search"></a>

### Perspective-guided research

`perspective-search` · Research information management · original type: pattern

Use several viewpoints to generate questions and broaden evidence collection.

**Aliases:** multi-perspective research; perspective-guided question asking.

**Evidence:** [S224, taught, p. 12](../../courses/stanford-cs224v/markdown/slides/i-deepresearch.md).

<a id="concept-hybrid-data"></a>

### Queries over structured and unstructured data

`hybrid-data` · Knowledge processing · original type: method

Compose database operations with free-text retrieval and language processing.

**Aliases:** hybrid data queries.

**Related terms:** SUQL.

**Evidence:** [S224, taught, p. 16](../../courses/stanford-cs224v/markdown/slides/l-new-suql.md).

<a id="concept-semantic-parsing"></a>

### Semantic parsing to formal queries

`semantic-parsing` · Knowledge processing · original type: method

Translate natural language to a formal query or logical representation.

**Related terms:** text-to-SQL; text-to-SPARQL; NL-to-SMT.

**Also relevant to:** [Prompting, reasoning, and planning techniques](reasoning-techniques.md).

**Evidence:** [S224, taught, p. 7](../../courses/stanford-cs224v/markdown/slides/l-satir.md).

<a id="concept-query-rewriting"></a>

### Query rewriting and expansion

`query-rewriting` · Retrieval and indexing · original type: method

Change or extend a search query to retrieve more useful evidence.

**Aliases:** query expansion; search query reformulation.

**Evidence:** [BOOK, taught, line 444](../../courses/agentic-large-language-models/markdown/chapters/chapter-12-search-and-retrieval-in-agentic-llms.md).
