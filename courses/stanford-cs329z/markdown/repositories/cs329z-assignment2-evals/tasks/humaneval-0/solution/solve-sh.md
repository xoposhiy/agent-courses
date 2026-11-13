# Homework 2 alternate repository from resource list: tasks/humaneval-0/solution/solve.sh

[Course index](../../../../../../README.md) · [Original source](https://github.com/cs329z/assignment2-evals/blob/HEAD/tasks/humaneval-0/solution/solve.sh) · [Raw file](../../../../../../raw/repositories/cs329z-assignment2-evals/tasks/humaneval-0/solution/solve.sh)

Retrieved: 2026-11-13T16:35:22.706220+00:00

```sh
#!/bin/bash
set -euo pipefail

python - <<'PY'
from pathlib import Path

path = Path("/app/humaneval_0.py")
text = path.read_text()
text = text.replace(
    "    pass\n",
    """    for index, element in enumerate(numbers):
        for other_index, other_element in enumerate(numbers):
            if index != other_index and abs(element - other_element) < threshold:
                return True
    return False
""",
)
path.write_text(text)
PY

```
