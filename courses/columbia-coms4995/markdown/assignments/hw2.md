# HW2

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/HW2.html) · [Raw file](../../raw/assignments/hw2.html)

Retrieved: 2026-11-13T16:40:49.926222+00:00

COMS 4995-15

# Introduction to Designing LLM Agents

[← Back to Course Home](../pages/index.md)

# Homework 2: Decoding, Prompting, Retrieval, and Memory

**Due:** Monday, October 19 @ 11:59 PM Eastern Time

## Overview

In this assignment, you will implement the decoding strategies that turn model scores into text, write prompts that return a fixed schema, retrieve documents the model was not trained on, and build a three-layer conversation memory.

The assignment includes four code files and five written responses, totaling 100 points.

* **Part 1: Decoding (15 pts)** — `part1_decoding.py`
* **Part 2: Prompting and structured output (20 pts)** — `part2_prompting.py`
* **Part 3: Retrieval (20 pts)** — `part3_retrieval.py`
* **Part 4: Memory (20 pts)** — `part4_memory.py`
* **Short answer questions (25 pts)** — separate PDF

**Assignment files**

Download the HW2 starter files and instructions.

[Download HW2.zip](archive-hw2.md)

## Setup

You need Python 3.10 or newer.

```
pip install transformers torch google-genai fastembed numpy
```

Get an API key from [Google AI Studio](../references/google-ai-studio-api-key-markdown.md) and set `GEMINI_API_KEY` in your environment. The free tier limits requests per minute and per day, so please budget multiple days to finish this homework. Complete the parts in order.

All functions you have to implement yourself are marked with `# TODO`. Each file also contains a test function to help you check your work. Parts 1 and 3 download a model the first time they run.

## Part 1 — Decoding (15 pts)

`part1_decoding.py`

* **1.0:** Load GPT-2 and return the scores for the next token.
* **1.1–1.4:** Implement greedy decoding, temperature, top-k decoding, and top-p decoding.
* **1.5 Repetition penalty:** Lower the score of every token already produced.
* **1.6 Generate:** Compose the settings into a sampler and run it in a loop.
* **1.7 Evaluate:** Report the share of n-grams that are distinct.

Run the file to print the next-token distribution and one generation per setting.

## Part 2 — Prompting and Structured Output (20 pts)

`part2_prompting.py`

* **2.0 Client:** Write a Gemini wrapper with retries and a disk cache.
* **2.1 Extract:** Get the schema out of a ticket with no examples in the prompt.
* **2.2 Few-shot:** Do the same with worked examples in the prompt.
* **2.3 Chain-of-thought:** Have the model reason before it answers.
* **2.4 Self-consistency:** Sample several reasoned answers and take the majority.
* **2.5 Validate:** Check each extraction against the schema.

Run the file to score all four prompts on schema validity and per-field accuracy.

## Part 3 — Retrieval (20 pts)

`part3_retrieval.py`

* **3.0 Chunk:** Split thirty articles into overlapping windows.
* **3.1 Embed:** Turn each chunk into a vector.
* **3.2 Search:** Rank chunks by cosine similarity.
* **3.3 Baseline:** Rank them again by shared words.
* **3.4 Measure:** Report recall@k for both retrievers.
* **3.5 Answer:** Answer from what you retrieved, cite it, and abstain when the corpus does not cover the question.

Run the file to compare the two retrievers and print both abstention rates.

## Part 4 — Memory (20 pts)

`part4_memory.py`

* **4.0 Buffer:** Keep the last n turns in a conversation and report what is removed.
* **4.1 Summary:** Compact everything the buffer drops into a running summary.
* **4.2 Fact store:** Pull durable facts out of each turn and search them with your Part 3 retriever.
* **4.3 Compose:** Combine 4.0–4.2 to build a full memory context.
* **4.4 Replay:** Replay a scripted conversation into your memory.

Run the file to see the context your memory builds at three buffer sizes.

## Short Answer Questions (25 pts)

Answer all five questions in a separate PDF.

1. **[Part 1] Decoding.** Using the table from Part 1, discuss which settings lead to repetition and which lead to incoherent text. What are the pros and cons of each setting? Give an example of a real-world application that would be best suited to each.
2. **[Parts 1 and 2] gpt2 vs. Gemini.** Use generate from Part 1 and chat from Part 2 to give gpt2 and Gemini the same instructions at a temperature of 0.7. Try two or three instructions of your own and quote the outputs. How does gpt2 handle instructions compared to Gemini? Why do you think that is?
3. **[Part 3] Retrieval.** Report recall@k for both retrievers, split by query kind. Find a query that embedding retrieval does better on, and a query that keyword (TF-IDF) retrieval does better on. What aspects of a query make it better suited to each?
4. **[Part 3] Grounded answers.** Report both abstention rates. Change your answer prompt to make the model more willing to answer, then less willing, and report how the two rates change. Which prompt changes had the biggest effect? For the park's help desk, which mistake is worse: answering a question the articles do not cover, or abstaining on one they do? Where would you want the two rates to be?
5. **[Part 4] Memory.** Compare the contexts main prints at buffer sizes 2 and 8. What are the biggest differences? Then rerun Part 4 with longer and shorter values of `SUMMARY_WORDS`. At what length does your summary start losing details, and which details are lost first?

## Submission Instructions

Upload five files to Gradescope:

1. `part1_decoding.py`
2. `part2_prompting.py`
3. `part3_retrieval.py`
4. `part4_memory.py`
5. `HW2_short_answers.pdf`

## Policies

* **Generative AI:** AI may be used for the coding parts as long as you understand and can explain everything you submit. For the short answers, AI may be used to organize your thoughts, but not to generate your responses.
* **Late days:** Late days apply automatically from your remaining balance. Beyond that, late work is not accepted.
* **Collaboration:** Homeworks should be completed individually.
