# HW1 Released: assignment1-harness: tests/fixtures/personas/15-email-foxglove-deposit.json

[Course index](../../../../../../README.md) · [Original source](https://github.com/cs329z/assignment1-harness/blob/HEAD/tests/fixtures/personas/15-email-foxglove-deposit.json) · [Raw file](../../../../../../raw/repositories/cs329z-assignment1-harness/tests/fixtures/personas/15-email-foxglove-deposit.json)

Retrieved: 2026-11-13T16:35:03.050392+00:00

```json
{
  "id": "email-foxglove-deposit",
  "category": "email_multihop",
  "role": "An events coordinator at Cardinal Energy who is planning next year's charity golf day.",
  "disposition": "Cheerful. One or two short sentences.",
  "sessions": [
    {
      "goal": "Find out from the email archive how large a deposit the caterer asked for at the 2001 Foxglove Classic. After you get that, ask how much the event raised in the end.",
      "opening": "For the 2001 Foxglove Classic, how much did the caterer want up front to hold the date?",
      "max_user_turns": 4
    }
  ],
  "knowledge": [
    "You do not remember the caterer's name."
  ],
  "checks": [
    {
      "type": "any_reply_contains_any",
      "values": [
        "2,250"
      ]
    },
    {
      "type": "any_reply_contains_any",
      "values": [
        "64,300"
      ]
    },
    {
      "type": "no_agent_error"
    }
  ],
  "rubric": [
    "The agent says the caterer asked for a deposit of $2,250. Reference: the caterer's order email ($2,250 up front, balance of $2,100 on delivery).",
    "The agent says the 2001 Foxglove Classic raised $64,300."
  ],
  "mode": "auto"
}

```
