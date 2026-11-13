# hw1: HW1/part3_classifier.ipynb

[Course index](../../../../README.md) · [Original source](https://designing-agents.github.io/assets/HW1.zip#archive-member=HW1/part3_classifier.ipynb) · [Raw file](../../../../raw/assignments/hw1/HW1/part3_classifier.ipynb)

Retrieved: 2026-11-13T16:41:01.381844+00:00

## Cell 1

# HW1 Part 3 - Training a Classifier

Here, you will use your clean corpus of restaurant reviews from Part 1 and the tokenizer you trained in Part 2 to train a model. You will create and train a small transformer to predict whether a review is positive or negative, then measure how well it does.

A GPU will make training faster, but the model is small enough to train on CPU. To use one in Colab, set **Runtime > Change runtime type > T4 GPU**.

Submit this notebook run top to bottom, with all outputs visible.

## Cell 2

```python
!pip install -q tokenizers
```

## Cell 3

```python
import random
import sys

import torch
import torch.nn as nn

sys.path.insert(0, ".")
torch.manual_seed(1990)
random.seed(1990)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"device: {DEVICE}")
```

## Cell 4

## 3.0 - Load the corpus and the tokenizer

`build_pipeline` should return the cleaned records, and `train_bpe` should turn their text into a tokenizer.

Make sure you train this tokenizer on **the whole review corpus**, NOT on the built-in sentences from Part 2.

## Cell 5

```python
from part1_data_processing import DEFAULT_THRESHOLDS, build_pipeline, load_corpus
from part2_tokenizing import train_bpe

VOCAB_SIZE = 2000

def load_reviews() -> list[dict]:
    """
    In:  nothing
    Out: the cleaned records from your Part 1 pipeline
    """
    # TODO
    return []


def load_tokenizer(texts: list[str], vocab_size: int = VOCAB_SIZE):
    """
    In:  the cleaned review texts and a vocabulary size
    Out: a BPE tokenizer trained on them, using your Part 2 train_bpe
    """
    # TODO
    raise NotImplementedError
```

## Cell 6

## 3.1 - Make a train and test split

The reviews carry a 1-5 star rating, which becomes a binary label. Treat 1 and 2 stars as negative and 4 and 5 as positive. Drop the 3-star reviews, as they are neutral. Keep the two classes balanced in both splits.

  shuffling: https://docs.python.org/3/library/random.html#random.shuffle

## Cell 7

```python
def make_splits(records: list[dict], test_frac: float = 0.2) -> tuple[list, list]:
    """
    In:  the cleaned records, and the fraction to hold out for testing
    Out: (train, test), each a list of (text, label) pairs, where label is
         0 for negative and 1 for positive

    Drop the 3-star reviews. Balance the two classes, and shuffle before
    splitting so the split does not follow the order of the corpus.
    """
    # TODO
    return [], []
```

## Cell 8

## 3.2 - Train the model

Build a simple transformer model. The model embeds each token, lets the tokens attend to each other once, averages the result, and maps that average to two scores. 

Reviews differ in length, so `encode_batch` below pads them to a fixed length and returns a mask marking which positions are real. Use the mask twice: attention should ignore padded positions, and the average at the end should be taken over real tokens only.

  modules:   https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html

  embedding: https://docs.pytorch.org/docs/stable/generated/torch.nn.Embedding.html

  attention: https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html
  
  training:  https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html

## Cell 9

```python
MAX_LEN = 256


def encode_batch(tokenizer, texts: list[str]) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Tokenizes and pads a batch. Written for you.

    In:  a tokenizer and a list of strings
    Out: (ids, mask), both LongTensors shaped (len(texts), n), where n is the
         longest tokenized review in the batch, capped at MAX_LEN. mask is 1 at
         real token positions and 0 at padding.
    """
    rows = [tokenizer.encode(t).ids[:MAX_LEN] for t in texts]
    width = max(len(r) for r in rows)
    ids = torch.zeros(len(rows), width, dtype=torch.long)
    mask = torch.zeros(len(rows), width, dtype=torch.long)
    for i, row in enumerate(rows):
        ids[i, :len(row)] = torch.tensor(row, dtype=torch.long)
        mask[i, :len(row)] = 1
    return ids.to(DEVICE), mask.to(DEVICE)


class ReviewClassifier(nn.Module):
    """
    A token embedding, a position embedding, one self-attention block, a mean
    over the real tokens, and a linear layer to two classes.
    """

    def __init__(self, vocab_size: int, d_model: int = 64, n_heads: int = 4):
        super().__init__()
        # TODO

    def forward(self, ids: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        """
        In:  ids and mask, both (batch, length)
        Out: logits of shape (batch, 2)
        """
        # TODO
        raise NotImplementedError


def train(model, train_split: list, tokenizer, epochs: int = 8,
          batch_size: int = 16, lr: float = 1e-3):
    """
    In:  a model, the training split, a tokenizer, and the usual knobs
    Out: the trained model

    Print the average loss each epoch, so you can monitor training progress.
    """
    # TODO
    raise NotImplementedError
```

## Cell 10

## 3.3 - Evaluate performance

Return your model's overall accuracy. For a more in-depth evaluation, also return precision and
recall for both classes.

For the positive class, precision is the fraction of reviews the model labelled positive that
really were positive, and recall is the fraction of the positive reviews that it found. The
negative class is the same with the labels swapped.

## Cell 11

```python
def evaluate(model, test_split: list, tokenizer) -> dict:
    """
    In:  a trained model, the test split, and a tokenizer
    Out: a dict with keys "accuracy", "precision_negative", "recall_negative",
         "precision_positive", and "recall_positive"
    """
    # TODO
    raise NotImplementedError
```

## Cell 12

### Run it

Written for you. Runs everything above and prints the results.

## Cell 13

```python
records = load_reviews()
print(f"{len(records)} clean reviews")

tokenizer = load_tokenizer([r["text"] for r in records])

train_split, test_split = make_splits(records)
print(f"{len(train_split)} train, {len(test_split)} test")

model = ReviewClassifier(tokenizer.get_vocab_size()).to(DEVICE)
model = train(model, train_split, tokenizer)

results = evaluate(model, test_split, tokenizer)
print()
for name, value in results.items():
    print(f"  {name:<20} {value:.3f}")
```
