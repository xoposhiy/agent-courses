# Assignment 2: scripts/deploy_validator_model.sh

[Course index](../../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-2/blob/HEAD/scripts/deploy_validator_model.sh) · [Raw file](../../../../raw/repositories/cmu-assignment-2/scripts/deploy_validator_model.sh)

Retrieved: 2026-11-13T16:48:13.606223+00:00

```sh
#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
student_dir="$(dirname -- "$script_dir")"
cd "$student_dir"

exec uv run modal deploy infrastructure/validator_model.py

```
