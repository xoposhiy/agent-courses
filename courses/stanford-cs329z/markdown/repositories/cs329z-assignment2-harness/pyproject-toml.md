# HW2 Released: assignment2-harness: pyproject.toml

[Course index](../../../README.md) · [Original source](https://github.com/cs329z/assignment2-harness/blob/HEAD/pyproject.toml) · [Raw file](../../../raw/repositories/cs329z-assignment2-harness/pyproject.toml)

Retrieved: 2026-11-13T16:35:14.032514+00:00

```toml
[project]
name = "assignment2-harness"
version = "26.1.0"
description = "CS329Z Assignment 2: Building an Evaluation Task."
requires-python = ">=3.12,<3.14"
# Harbor is the eval framework. Pinned for reproducibility across the class.
dependencies = [
  "harbor==0.18.0",
  # For the Section 3.4 trajectory figures.
  "matplotlib==3.11.2",
]

[project.optional-dependencies]
# Funded cloud sandbox backend (run with `-e modal`). Not needed for local
# Docker runs; install with `uv sync --extra modal` if you want it.
modal = [
  "harbor[modal]==0.18.0",
]

[build-system]
requires = ["hatchling==1.33.0"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
# Only the pinned Harbor agent is importable; the rest is task definitions.
only-include = ["pinned_agent.py"]

[tool.uv]
# litellm 1.106.x crashes on import without `mcp`; every litellm release caps
# filelock below 4, but only filelock>=4.2.1 is free of known advisories.
constraint-dependencies = ["litellm==1.105.7"]
override-dependencies = ["filelock==4.2.6"]

```
