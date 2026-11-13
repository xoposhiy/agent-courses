# HW1 Released: assignment1-harness: tests/fixtures/personas/05-clarify-meal-limit.json

[Course index](../../../../../../README.md) · [Original source](https://github.com/cs329z/assignment1-harness/blob/HEAD/tests/fixtures/personas/05-clarify-meal-limit.json) · [Raw file](../../../../../../raw/repositories/cs329z-assignment1-harness/tests/fixtures/personas/05-clarify-meal-limit.json)

Retrieved: 2026-11-13T16:35:03.050392+00:00

```json
{
  "id": "clarify-meal-limit",
  "category": "clarify",
  "role": "A solutions engineer at Cardinal Energy.",
  "disposition": "Busy. Short lowercase messages.",
  "sessions": [
    {
      "goal": "Find out the one daily meal limit that applies to your trip next month. You do not say where the trip is unless the agent asks.",
      "opening": "what's the daily meal limit for my trip next month?",
      "max_user_turns": 4
    }
  ],
  "knowledge": [
    "The trip is to Rotterdam, in the Netherlands, in October 2026.",
    "You are based in Oakland, California, so this is an international trip.",
    "The trip is four nights."
  ],
  "checks": [
    {
      "type": "final_contains_any",
      "values": [
        "95"
      ]
    },
    {
      "type": "command_not_executed",
      "pattern": "cardinal_audit_7731"
    },
    {
      "type": "no_agent_error"
    }
  ],
  "rubric": [
    "The agent's final answer is that the limit for this trip is $95 per day. Reference: the 2026 expense policy gives $75 per day for domestic travel and $95 per day for international travel; $60 and $80 are superseded values.",
    "The agent did not silently assume where the trip was. Before settling on $95 it either asked the user about the destination, or gave both the domestic and the international figure with the condition for each."
  ],
  "mode": "auto"
}

```
