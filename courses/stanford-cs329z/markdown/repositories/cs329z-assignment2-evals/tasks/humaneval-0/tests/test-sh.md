# Homework 2 alternate repository from resource list: tasks/humaneval-0/tests/test.sh

[Course index](../../../../../../README.md) · [Original source](https://github.com/cs329z/assignment2-evals/blob/HEAD/tasks/humaneval-0/tests/test.sh) · [Raw file](../../../../../../raw/repositories/cs329z-assignment2-evals/tasks/humaneval-0/tests/test.sh)

Retrieved: 2026-11-13T16:35:22.706220+00:00

```sh
#!/bin/bash
set -uo pipefail

if python /tests/test_outputs.py; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

```
