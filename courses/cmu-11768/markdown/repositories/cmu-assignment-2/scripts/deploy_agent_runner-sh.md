# Assignment 2: scripts/deploy_agent_runner.sh

[Course index](../../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-2/blob/HEAD/scripts/deploy_agent_runner.sh) · [Raw file](../../../../raw/repositories/cmu-assignment-2/scripts/deploy_agent_runner.sh)

Retrieved: 2026-11-13T16:48:13.606223+00:00

```sh
#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
student_dir="$(dirname -- "$script_dir")"
cd "$student_dir"

uv run python -m infrastructure.configure_generation
uv run modal deploy infrastructure/generation_gateway.py
uv run modal deploy infrastructure/agent_runner.py

```
