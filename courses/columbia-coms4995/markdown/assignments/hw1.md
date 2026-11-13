# HW1

[Course index](../../README.md) · [Original source](https://designing-agents.github.io/HW1.html) · [Raw file](../../raw/assignments/hw1.html)

Retrieved: 2026-11-13T16:40:49.716508+00:00

COMS 4995-15

# Introduction to Designing LLM Agents

[← Back to Course Home](../pages/index.md)

# Homework 1: Data Processing, Tokenization, and Training

**Due:** Monday, October 5 @ 11:59 PM Eastern Time

## Overview

In this assignment, you will build an end-to-end model training pipeline. You will clean a corpus of raw restaurant reviews, write the tokenizer that turns them into model inputs, and train a small transformer to classify them.

The assignment includes three code files and four written responses, totaling 100 points.

* **Part 1: Data processing (25 pts)** — `part1_data_processing.py`
* **Part 2: Tokenization (25 pts)** — `part2_tokenizing.py`
* **Part 3: Training a classifier (30 pts)** — `part3_classifier.ipynb`
* **Short answer questions (20 pts)** — separate PDF

**Assignment files**

Download the HW1 starter files and instructions.

[Download HW1.zip](archive-hw1.md)

## Setup

You need Python 3.10 or newer.

```
pip install transformers tokenizers torch
```

Parts 1 and 2 are independent, so you may do them in either order. Complete Part 3 last, as it builds on functions you write in Parts 1 and 2.

All functions you have to implement yourself are marked with `# TODO`. Each file also contains a small test function to help you check your work.

## Part 1 — Data Processing (25 pts)

`part1_data_processing.py`

Clean a corpus of 1,000 restaurant reviews containing HTML, broken encodings, contact details, duplicates, and junk.

* **1.0 Load:** Load the corpus from JSONL.
* **1.1 Normalize:** Strip markup, decode HTML entities, fix Unicode, and collapse whitespace.
* **1.2 Scrub PII:** Replace emails, URLs, phone numbers, and handles with placeholders while leaving alone strings that only look like personal information.
* **1.3 Quality filter:** Drop documents by length, by how little text is real language, and by near-duplication against documents already kept.
* **1.4–1.5 Pipeline:** Run the stages in order and report how many records each stage drops.

Run the file to score your work against 52 test cases in `data/test_cases.json`.

## Part 2 — Tokenization (25 pts)

`part2_tokenizing.py`

* **2.0–2.2:** Load GPT-2, multilingual BERT, and T5, and measure tokens per word and bytes per token across six sentences.
* **2.3 Round-trip fidelity:** Check whether text survives being encoded and decoded sequentially.
* **2.4 Byte pair encoding:** Implement BPE yourself, then train a byte-level tokenizer on a corpus.

Run the file to print all three comparison tables.

## Part 3 — Training a Classifier (30 pts)

`part3_classifier.ipynb`

* **3.0:** Load your cleaned corpus and train a tokenizer on it.
* **3.1:** Split into training and test sets, balanced across the two classes.
* **3.2:** Build and train a small transformer with token and position embeddings, one self-attention block, mean pooling, and a linear classifier head.
* **3.3:** Evaluate it on accuracy plus class-wise precision and recall.

A GPU makes training faster but is not required. In Colab, upload the whole `hw1` folder and set Runtime > Change runtime type > T4 GPU. Uploading only the notebook will fail because it imports the Part 1 and Part 2 files from the same folder.

## Short Answer Questions (20 pts)

Answer all four questions in a separate PDF. You will need to replace numbers in some functions and re-run your code, so plan your time accordingly.

1. **[Part 2] Tokenization.** Using the output from the test function in Part 2, discuss how the different input sentences tokenized differently in terms of word-per-token and bytes-per-token. Which failed the round trip check? Why do you think that is?
2. **[Part 2] Your trained BPE tokenizer.** Train your BPE tokenizer using vocab sizes 300, 500, and 2000. Report the vocabulary you actually got at each size and account for any gap. Then tokenize the Part 2 sentences at each size. Which sentences improve as the vocabulary grows and which do not? What does that tell you about how a larger vocabulary would adapt to unseen text?
3. **[Part 3] Training.** Report your training loss at the first and last epoch, alongside your accuracy on the test split. Account for the gap between them. What would happen to the training accuracy if you trained the model for additional epochs? Why do we measure accuracy on the test split, and not train?
4. **[Part 3] Model comparison.** Experiment with the hidden state size in your transformer, decreasing it to 16 and increasing it to 128. Compare and contrast the resulting metrics. What are the tradeoffs as model size increases?

## Submission Instructions

Upload four files to Gradescope:

1. `part1_data_processing.py`
2. `part2_tokenizing.py`
3. `part3_classifier.ipynb`, run top to bottom with all outputs visible
4. `HW1_short_answers.pdf`

## Policies

* **Generative AI:** AI may be used for the coding parts as long as you understand and can explain everything you submit. For the short answers, AI may be used to organize your thoughts, but not to generate your responses.
* **Late days:** Late days apply automatically from your remaining balance. Beyond that, late work is not accepted.
* **Collaboration:** Homeworks should be completed individually.
