# HW2 Released: assignment2-harness: tasks/humaneval-0/tests/test.sh

[Course index](../../../../../../README.md) · [Original source](https://github.com/cs329z/assignment2-harness/blob/HEAD/tasks/humaneval-0/tests/test.sh) · [Raw file](../../../../../../raw/repositories/cs329z-assignment2-harness/tasks/humaneval-0/tests/test.sh)

Retrieved: 2026-11-13T16:35:14.032514+00:00

```sh
#!/bin/bash
set -uo pipefail

if python /tests/test_outputs.py; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

```
