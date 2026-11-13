# HW2 Released: assignment2-harness: tasks/humaneval-0/task.toml

[Course index](../../../../../README.md) · [Original source](https://github.com/cs329z/assignment2-harness/blob/HEAD/tasks/humaneval-0/task.toml) · [Raw file](../../../../../raw/repositories/cs329z-assignment2-harness/tasks/humaneval-0/task.toml)

Retrieved: 2026-11-13T16:35:14.032514+00:00

```toml
# Local Harbor port of OpenAI HumanEval/0.
schema_version = "1.3"
artifacts = []

[task]
name = "humaneval/0"
description = "Complete HumanEval/0: determine whether any two numbers are closer than a threshold."
authors = [{ name = "OpenAI HumanEval authors" }, { name = "CS329Z staff", role = "Harbor port" }]
keywords = ["humaneval", "python", "function-completion"]

[metadata]
difficulty = "introductory"
category = "function-completion"
source = "https://github.com/openai/human-eval"
source_task_id = "HumanEval/0"

[verifier]
timeout_sec = 60.0
collect = []

[verifier.env]

[agent]
timeout_sec = 600.0

[environment]
network_mode = "public"
build_timeout_sec = 600.0
os = "linux"
mcp_servers = []

[environment.env]

[solution.env]

```
