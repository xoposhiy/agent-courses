# Assignment 2: labels.example.json

[Course index](../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-2/blob/HEAD/labels.example.json) · [Raw file](../../../raw/repositories/cmu-assignment-2/labels.example.json)

Retrieved: 2026-11-13T16:48:13.606223+00:00

```json
{
  "labels": [
    {
      "run_id": "example__qwen",
      "errors": [
        {
          "family": "wrong_chart",
          "evidence": "The task requested vertical bars but the figure uses a line."
        }
      ]
    },
    {
      "run_id": "example__ministral",
      "errors": [
        {
          "family": "execution_failure",
          "evidence": "The program raised an exception and no figure.png was produced."
        }
      ]
    },
    {
      "run_id": "example__glm",
      "errors": []
    }
  ]
}

```
