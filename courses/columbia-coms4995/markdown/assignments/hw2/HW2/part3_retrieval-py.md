# hw2: HW2/part3_retrieval.py

[Course index](../../../../README.md) · [Original source](https://designing-agents.github.io/assets/HW2.zip#archive-member=HW2/part3_retrieval.py) · [Raw file](../../../../raw/assignments/hw2/HW2/part3_retrieval.py)

Retrieved: 2026-11-13T16:41:01.807113+00:00

```python
"""
HW2 Part 3 - Retrieval

The Fossil Falls help desk has thirty help articles. You will build a search
that finds the article answering a guest's question, then have Gemini answer
from it:

    query:   "we were trapped up on the sky train for ages with no electricity"
    article: KB-009, "When the monorail makes an emergency stop"

data/retrieval_queries.jsonl tags each query as a paraphrase of an article's
wording, an exact match on a term in one, or unanswerable from the articles.

An "article" is a dict with keys "id", "title", and "body". A "chunk" is a
piece of an article, with keys "article_id", "chunk_id", and "text". An
"index" is a list of chunks alongside a matrix whose row i embeds chunk i.

    pip install fastembed numpy
    python part3_retrieval.py

"""

from __future__ import annotations

import json
import warnings
from pathlib import Path

import numpy as np

from part2_prompting import chat, parse_json

warnings.filterwarnings("ignore", message=".*encountered in matmul")

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

ARTICLES = DATA / "help_articles.jsonl"        # load_articles reads this
QUERIES = DATA / "retrieval_queries.jsonl"     # main reads this

EMBED_MODEL = "BAAI/bge-small-en-v1.5"

CHUNK_SIZE = 60        # words per chunk
CHUNK_OVERLAP = 15     # words shared by consecutive chunks
K_VALUES = (1, 3, 5)
N_ABSTAIN = 6          # queries of each kind main() sends to answer()

ABSTAIN = "NOT_IN_CORPUS"


def load_articles(path: Path = ARTICLES) -> list[dict]:
    """
    In:  a path to help_articles.jsonl
    Out: records with keys "id", "title", and "body"
    """
    # TODO
    return []


# --- Task 3.0: Chunk ---------------------------------------------------------
# Embedding a whole article dilutes the passage that answers the question, so
# split each article into overlapping windows.

def chunk(article: dict, size: int = CHUNK_SIZE,
          overlap: int = CHUNK_OVERLAP) -> list[dict]:
    """
    In:  one article, and the window and overlap, both counted in words
    Out: chunks with keys "article_id", "chunk_id", and "text", where
         consecutive chunks share `overlap` words

    An article shorter than one window is still one chunk. chunk_id counts from
    0 within each article.
    """
    # TODO
    return []


# --- Task 3.1: Embed ---------------------------------------------------------
# An embedding model maps text to a vector, placing texts with similar meanings
# near one another. Use the following documentation to embed text:
#
#   fastembed: https://qdrant.github.io/fastembed/

def embed(texts: list[str]) -> np.ndarray:
    """
    In:  a list of strings
    Out: an array of shape (len(texts), d), one row per string, in order
    """
    # TODO
    return np.zeros((0, 0))


def build_index(articles: list[dict]) -> tuple[list[dict], np.ndarray]:
    """
    In:  the article records
    Out: (chunks, matrix), where row i of matrix is the embedding of chunks[i]

    Chunk every article, then embed every chunk.
    """
    # TODO
    return [], np.zeros((0, 0))


# --- Task 3.2: Search --------------------------------------------------------
# Cosine similarity is the dot product of two vectors divided by the product of
# their lengths. Score every chunk in one matrix operation rather than a loop.

def cosine_top_k(query_vec: np.ndarray, matrix: np.ndarray,
                 k: int) -> list[tuple[int, float]]:
    """
    In:  a query embedding, the chunk matrix, and how many to return
    Out: (row index, similarity) for the k most similar rows, most similar
         first
    """
    # TODO
    return []


# --- Task 3.3: A baseline ----------------------------------------------------
# Compare the embeddings against something simpler. Score a chunk by the words
# it shares with the query, weighting each word by how rare it is across the
# corpus, so that "the" counts for nothing.
#
#   tf-idf: https://en.wikipedia.org/wiki/Tf%E2%80%93idf

def keyword_top_k(query: str, chunks: list[dict],
                  k: int) -> list[tuple[int, float]]:
    """
    In:  a query, the chunk records, and how many to return
    Out: the same shape as cosine_top_k
    """
    # TODO
    return []


def retrieve(query: str, chunks: list[dict], matrix: np.ndarray, k: int,
             method: str = "embedding") -> list[dict]:
    """
    In:  a query, the index, how many chunks to return, and either "embedding"
         or "keyword"
    Out: the k chunk records, most relevant first
    """
    # TODO
    return []


# --- Task 3.4: Measure -------------------------------------------------------
# How often does the right article turn up in the top k?

def recall_at_k(queries: list[dict], chunks: list[dict], matrix: np.ndarray,
                k: int, method: str) -> float:
    """
    In:  query records with "query" and "gold_article_ids", the index, a k, and
         a retriever
    Out: the fraction of queries whose retrieved chunks include at least one
         gold article

    Queries with no gold article are not counted.
    """
    # TODO
    return 0.0


# --- Task 3.5: Answer --------------------------------------------------------
# Put the top chunks in the prompt and have the model answer from them alone.

def answer(query: str, chunks: list[dict], matrix: np.ndarray,
           k: int = 3) -> dict:
    """
    In:  a query and the index
    Out: {"answer": str, "article_ids": list[str]}

    "article_ids" are the articles the answer came from. "answer" is ABSTAIN
    and "article_ids" is empty when nothing retrieved supports the question.
    Ask for JSON and parse it with parse_json from Part 2.
    """
    # TODO
    return {"answer": ABSTAIN, "article_ids": []}


def abstention_rate(queries: list[dict], chunks: list[dict],
                    matrix: np.ndarray) -> tuple[float, float]:
    """
    In:  the query records and the index
    Out: (the fraction of unanswerable queries abstained on,
          the fraction of answerable queries wrongly abstained on)
    """
    # TODO
    return 0.0, 0.0


# --- Test (written for you) --------------------------------------------------
# Builds the index once, compares the two retrievers, lists the queries only
# one of them gets right at recall@1, and reports both abstention rates on
# the first N_ABSTAIN queries of each kind.

def main() -> None:
    articles = load_articles()
    if not articles:
        print("load_articles returned nothing, so there is nothing to index yet.")
        return

    chunks, matrix = build_index(articles)
    print(f"\n{len(articles)} articles, {len(chunks)} chunks, "
          f"{matrix.shape[1] if matrix.size else 0} dimensions")
    if not chunks:
        return

    queries = [json.loads(line) for line in
               QUERIES.read_text(encoding="utf-8").splitlines() if line.strip()]
    kinds = sorted({q["kind"] for q in queries} - {"unanswerable"})

    for kind in ["all"] + kinds:
        subset = queries if kind == "all" else [q for q in queries if q["kind"] == kind]
        print(f"\n  {kind:<12}" + "".join(f"{'recall@' + str(k):>11}" for k in K_VALUES))
        for method in ("embedding", "keyword"):
            row = "".join(f"{recall_at_k(subset, chunks, matrix, k, method):>11.3f}"
                          for k in K_VALUES)
            print(f"  {method:<12}{row}")

    print("\n  found at recall@1 by only one retriever")
    for q in queries:
        found = {method: any(c["article_id"] in q["gold_article_ids"]
                             for c in retrieve(q["query"], chunks, matrix, 1, method))
                 for method in ("embedding", "keyword")}
        if found["embedding"] != found["keyword"]:
            winner = "embedding" if found["embedding"] else "keyword"
            print(f"  {winner:<12}{q['id']:<7}{q['query'][:64]}")

    sample = []
    for kind in kinds + ["unanswerable"]:
        sample += [q for q in queries if q["kind"] == kind][:N_ABSTAIN]
    caught, false_alarm = abstention_rate(sample, chunks, matrix)
    print(f"\n  abstained when it should have    {caught:>7.3f}")
    print(f"  abstained when it should not     {false_alarm:>7.3f}")

    example = next(q for q in sample if q["gold_article_ids"])
    result = answer(example["query"], chunks, matrix)
    print(f"\n{example['query']!r}")
    print(f"  cited  {result['article_ids']}  (gold {example['gold_article_ids']})")
    print(f"  said   {result['answer']}")


if __name__ == "__main__":
    main()

```
