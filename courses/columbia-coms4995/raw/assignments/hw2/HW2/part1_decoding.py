"""
HW2 Part 1 - Decoding

A language model scores every token in its vocabulary as a candidate for the
next position. A decoding strategy turns those scores into a single token,
and repeating this loop is what generates text.

    pip install transformers torch
    python part1_decoding.py

"""

from __future__ import annotations

import textwrap

import torch

MODEL = "gpt2"
SEED = 1990
MAX_NEW_TOKENS = 40

PROMPT = "The keeper unlocked the gate to the raptor paddock and"

SETTINGS = [
    ("greedy",              dict(temperature=0.0)),
    ("temperature 0.7",     dict(temperature=0.7)),
    ("temperature 1.5",     dict(temperature=1.5)),
    ("top-k 5",             dict(temperature=1.0, k=5)),
    ("top-p 0.9",           dict(temperature=1.0, p=0.9)),
    ("top-p 0.9 + penalty", dict(temperature=1.0, p=0.9, penalty=1.2)),
]


# --- Task 1.0: Load ----------------------------------------------------------
# Use the following documentation to load gpt2 and run text through it:
#
#   auto classes: https://huggingface.co/docs/transformers/model_doc/auto
#   generation:   https://huggingface.co/docs/transformers/llm_tutorial
#   outputs:      https://huggingface.co/docs/transformers/main_classes/output

def load_model() -> tuple:
    """
    In:  nothing
    Out: (model, tokenizer) for MODEL, with the model in evaluation mode
    """
    # TODO
    return None, None


def next_token_logits(model, tokenizer, text: str) -> torch.Tensor:
    """
    In:  a model, its tokenizer, and a non-empty string
    Out: a 1-D float tensor of length vocab_size, the scores for the token that
         comes after the string
    """
    # TODO
    return torch.zeros(1)


# --- Task 1.1: Greedy --------------------------------------------------------
# The simplest strategy: take the highest-scoring token.

def greedy(logits: torch.Tensor) -> int:
    """
    In:  1-D logits
    Out: the id of the highest-scoring token
    """
    # TODO
    return 0


# --- Task 1.2: Temperature ---------------------------------------------------
# Logits become probabilities through a softmax. Rescaling them before that
# softmax changes how peaked the distribution is without changing the ranking.
#
#   softmax: https://pytorch.org/docs/stable/nn.functional.html

def apply_temperature(logits: torch.Tensor, temperature: float) -> torch.Tensor:
    """
    In:  1-D logits and a temperature of 0 or more
    Out: 1-D logits of the same shape, rescaled

    A temperature of 0 has to end up picking the token greedy would.
    """
    # TODO
    return logits


# --- Task 1.3: Top-k ---------------------------------------------------------
# Sampling across the whole vocabulary lets a long tail of unlikely tokens win
# occasionally. Top-k keeps only the k highest-scoring tokens.

def top_k_filter(logits: torch.Tensor, k: int) -> torch.Tensor:
    """
    In:  1-D logits and a k of 1 or more
    Out: the same logits with everything outside the k highest scores set to
         negative infinity
    """
    # TODO
    return logits


# --- Task 1.4: Top-p ---------------------------------------------------------
# A fixed k is too small when the model is uncertain and too large when it is
# confident. Top-p cuts by probability mass rather than by count.

def top_p_filter(logits: torch.Tensor, p: float) -> torch.Tensor:
    """
    In:  1-D logits and a p in (0, 1]
    Out: the same logits with everything outside the smallest set of tokens
         whose probabilities reach p set to negative infinity
    """
    # TODO
    return logits


# --- Task 1.5: Repetition penalty --------------------------------------------
# Models fall into loops and repeat the same phrase. A repetition penalty lowers
# the score of every token already produced. Implement the CTRL repetition
# penalty from section 4.1: https://arxiv.org/abs/1909.05858

def repetition_penalty(logits: torch.Tensor, generated_ids: list[int],
                       penalty: float) -> torch.Tensor:
    """
    In:  1-D logits, the ids generated so far, and a penalty of 1.0 or more
    Out: the same logits with the scores of ids in generated_ids moved down

    Repeated ids are penalized once.
    """
    # TODO
    return logits


# --- Task 1.6: Put it together -----------------------------------------------
# Use sample() to pick a token, and generate() to generate text by calling
# sample iteratively.
#
#   random sampling: https://pytorch.org/docs/stable/torch.html#random-sampling

def sample(logits: torch.Tensor, temperature: float = 1.0, k: int | None = None,
           p: float | None = None, generated_ids: list[int] | None = None,
           penalty: float = 1.0) -> int:
    """
    In:  1-D logits and the decoding settings
    Out: one token id

    Apply whichever settings are given, then sample one token from what is
    left. Apply temperature before top-k and top-p.
    """
    # TODO
    return 0


def generate(model, tokenizer, prompt: str,
             max_new_tokens: int = MAX_NEW_TOKENS, **params) -> str:
    """
    In:  a model, its tokenizer, a prompt, how many tokens to add, and settings
         passed through to sample
    Out: the prompt and its continuation, decoded

    Pass sample the ids generated so far, for the penalty. Stop early if the
    end-of-text token comes up.
    """
    # TODO
    return prompt


# --- Task 1.7: Measure repetition --------------------------------------------
# distinct-n is the share of a text's n-grams that are distinct. Text that loops
# and repeats words should score low.

def distinct_n(text: str, n: int) -> float:
    """
    In:  a string and an n of 1 or more
    Out: the number of distinct n-grams over the total number of n-grams,
         counted on whitespace-split tokens, and 0.0 when the text has fewer
         than n tokens
    """
    # TODO
    return 0.0


# --- Test (written for you) --------------------------------------------------
# Prints the ten most likely next tokens, then generates once per setting.

def main() -> None:
    model, tokenizer = load_model()
    if model is None:
        print("load_model returned nothing, so there is nothing to decode yet.")
        return

    print(f"\n{PROMPT!r}")

    logits = next_token_logits(model, tokenizer, PROMPT)
    if logits.numel() > 1:
        top = torch.topk(torch.softmax(logits, dim=-1), 10)
        print(f"\n  {'next token':<16}{'probability':>12}")
        for prob, token_id in zip(top.values, top.indices):
            print(f"  {tokenizer.decode(token_id)!r:<16}{prob:>12.4f}")

    print(f"\n  {'setting':<22}{'distinct-2':>11}")
    for label, params in SETTINGS:
        torch.manual_seed(SEED)
        text = generate(model, tokenizer, PROMPT, **params)
        tail = text[len(PROMPT):].strip().replace("\n", " ")
        print(f"\n  {label:<22}{distinct_n(tail, 2):>11.3f}")
        print(textwrap.fill(tail, 96, initial_indent="    ", subsequent_indent="    "))


if __name__ == "__main__":
    main()
