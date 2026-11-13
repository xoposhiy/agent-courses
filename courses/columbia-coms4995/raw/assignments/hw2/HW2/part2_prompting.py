"""
HW2 Part 2 - Prompting and Structured Output

Fossil Falls is a dinosaur theme park. A "ticket" is a message a guest sent
the park's help desk, stored as a dict with keys "id" and "body". You will
prompt Gemini to read a ticket and fill in the six fields in SCHEMA. That
output is an "extraction":

    ticket:     {"id": "T-004", "body": "Our Swamp Safari jeep stalled halfway
                 through the tour this afternoon and we sat there for forty
                 minutes next to the spinosaurus pond. ..."}
    extraction: {"category": "ride", "severity": "medium",
                 "park_area": "Swamp Safari",
                 "incident_time": "this afternoon",
                 "guest_sentiment": "frustrated", "needs_human": false}

You will implement different strategies to prompt for the same extraction.
main() scores each strategy against the labels in data/tickets_labeled.jsonl.

    pip install google-genai
    export GEMINI_API_KEY=...
    python part2_prompting.py

"""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path

# The Gemini SDK logs a warning about "automatic function calling" on the first
# request, for a feature this file does not use.
logging.getLogger("google_genai.models").setLevel(logging.ERROR)

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"

TICKETS = DATA / "tickets_labeled.jsonl"    # load_tickets reads this
CACHE = HERE / ".gemini_cache.json"

MODEL = "gemini-3.5-flash-lite"
SEED = 1990
N_SAMPLES = 3          # how many votes Task 2.4 collects
N_SCORE = 10           # how many tickets main() scores, out of the whole file

UNKNOWN = "unknown"    # park_area and incident_time take this when the ticket
                       # does not say

CATEGORY = ("tickets", "safety", "ride", "food", "lost-item", "feedback")
SEVERITY = ("low", "medium", "high", "critical")
SENTIMENT = ("angry", "frustrated", "neutral", "pleased")
AREA = ("Raptor Paddock", "T. rex Kingdom", "Swamp Safari", "Canopy Monorail",
        "Dino Diner", "Ticketing", UNKNOWN)

# Each field maps to either the values it allows or the type it has to be.
SCHEMA = {
    "category":        CATEGORY,
    "severity":        SEVERITY,
    "park_area":       AREA,
    "incident_time":   str,
    "guest_sentiment": SENTIMENT,
    "needs_human":     bool,
}


# --- Disk cache (written for you) --------------------------------------------
# Saves each reply so an identical request is never sent twice. A request is
# any dict describing the call, such as the messages and settings. Delete
# .gemini_cache.json to force fresh replies.

def _key(request: dict) -> str:
    return hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()


def cache_get(request: dict):
    """The saved reply for this request, or None."""
    if not CACHE.exists():
        return None
    return json.loads(CACHE.read_text(encoding="utf-8")).get(_key(request))


def cache_put(request: dict, reply) -> None:
    """Saves the reply for this request."""
    store = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    store[_key(request)] = reply
    CACHE.write_text(json.dumps(store), encoding="utf-8")


# --- Task 2.0: Query the model ---------------------------------------------
# Use the following documentation to call the Gemini API:
#
#   sdk:     https://googleapis.github.io/python-genai/
#   api:     https://ai.google.dev/api/generate-content

def chat(messages: list[dict], temperature: float = 0.0, seed: int = SEED,
         max_tokens: int = 512) -> str:
    """
    In:  a list of {"role", "content"} messages and the sampling settings
    Out: the assistant's reply text

    Read the key from GEMINI_API_KEY. Gemini calls the assistant role "model"
    and takes the system message separately from the other turns. Check
    cache_get before calling the API and cache_put after. Implement exponential
    backoff for when the API returns 429.
    """
    # TODO
    return ""


def chat_n(messages: list[dict], n: int, temperature: float = 0.8) -> list[str]:
    """
    In:  messages, how many replies to draw, and a temperature
    Out: n reply texts

    Send n separate requests, each with a different seed so the replies
    differ. Only Task 2.4 needs this; everything else uses chat. Cache each
    request the same way as chat.
    """
    # TODO
    return []


# --- Task 2.1: Extract -------------------------------------------------------
# Put the ticket body and a description of each SCHEMA field in the prompt, and
# ask for JSON back.

def parse_json(reply: str) -> dict:
    """
    In:  a reply that should contain a JSON object
    Out: the object, or {} when the reply does not carry one

    Replies often wrap the JSON in prose or code fences.
    """
    # TODO
    return {}


def extract_zero_shot(ticket: dict) -> dict:
    """
    In:  a ticket
    Out: an extraction, or {} when the reply does not parse

    No examples in the prompt.
    """
    # TODO
    return {}


# --- Task 2.2: Few-shot ------------------------------------------------------
# The same task as 2.1, with a few worked examples in the prompt: a ticket and
# the extraction you want for it.

def extract_few_shot(ticket: dict) -> dict:
    """
    In:  a ticket
    Out: an extraction, or {} when the reply does not parse

    Take your examples from tickets after the first N_SCORE. main() only scores
    the first N_SCORE, so examples from those would leak the answers.
    """
    # TODO
    return {}


# --- Task 2.3: Chain-of-thought ----------------------------------------------
# Have the model reason about the ticket before it answers.
# Implement chain-of-thought from https://arxiv.org/abs/2201.11903

def extract_cot(ticket: dict) -> dict:
    """
    In:  a ticket
    Out: an extraction, or {} when the reply does not parse

    Start from your Task 2.2 prompt and ask for reasoning first and the JSON
    last. One reply.
    """
    # TODO
    return {}


# --- Task 2.4: Self-consistency ----------------------------------------------
# Sample several reasoned replies and let them vote.
# Implement self-consistency from https://arxiv.org/abs/2203.11171

def extract_consistent(ticket: dict, n: int = N_SAMPLES) -> dict:
    """
    In:  a ticket and how many samples to draw
    Out: an extraction, each field set to its most common value across the
         samples

    Use the Task 2.3 prompt. Draw n replies with chat_n and parse each one,
    skipping any that do not parse.
    """
    # TODO
    return {}


# --- Task 2.5: Validate ------------------------------------------------------
# A reply that parses is not necessarily usable.

def validate(obj: dict) -> list[str]:
    """
    In:  an extraction
    Out: the names of every field that is missing, the wrong type, or outside
         its allowed values, and [] when there are none

    {"severity": "urgent"} returns all six names: severity is not an allowed
    value and the other five are missing.
    """
    # TODO
    return []


# --- Scoring -----------------------------------------------------------------

def load_tickets(path: Path = TICKETS) -> tuple[list[dict], dict]:
    """
    In:  a path to tickets_labeled.jsonl
    Out: (tickets, gold), where tickets holds each line's "id" and "body", and
         gold maps each ticket id to that line's "gold" extraction
    """
    # TODO
    return [], {}


def validity_rate(predictions: dict) -> float:
    """
    In:  a map of ticket id to extraction
    Out: the fraction whose validate() came back empty
    """
    # TODO
    return 0.0


def field_accuracy(predictions: dict, gold: dict) -> dict:
    """
    In:  a map of ticket id to extraction, and the same for the correct fields
    Out: a map of field name to the fraction of tickets it is right on, plus
         "exact_match" for the fraction of tickets where every field is right

    Compare fields ignoring case and surrounding whitespace, except
    incident_time, which is right when both or neither are UNKNOWN. A missing
    field counts as wrong.
    """
    # TODO
    return {}


# --- Test (written for you) --------------------------------------------------
# Scores the four prompts over the first N_SCORE tickets.

def main() -> None:
    tickets, gold = load_tickets()
    if not tickets:
        print("load_tickets returned nothing, so there is nothing to score yet.")
        return

    tickets = tickets[:N_SCORE]
    print(f"\nscoring {len(tickets)} tickets")

    header = "".join(f"{f.split('_')[0][:9]:>10}" for f in SCHEMA)
    print(f"\n  {'prompt':<12}{'valid':>7}{header}{'exact':>8}")
    for label, extract in (("zero-shot", extract_zero_shot),
                           ("few-shot", extract_few_shot),
                           ("cot", extract_cot),
                           ("consistent", extract_consistent)):
        predictions = {t["id"]: extract(t) for t in tickets}
        accuracy = field_accuracy(predictions, gold)
        row = "".join(f"{accuracy.get(f, 0.0):>10.3f}" for f in SCHEMA)
        print(f"  {label:<12}{validity_rate(predictions):>7.3f}{row}"
              f"{accuracy.get('exact_match', 0.0):>8.3f}")


if __name__ == "__main__":
    main()
