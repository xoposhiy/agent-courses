# HW1 Released: assignment1-harness: pyproject.toml

[Course index](../../../README.md) · [Original source](https://github.com/cs329z/assignment1-harness/blob/HEAD/pyproject.toml) · [Raw file](../../../raw/repositories/cs329z-assignment1-harness/pyproject.toml)

Retrieved: 2026-11-13T16:35:03.050392+00:00

```toml
[project]
name = "cs329z-hw1"
version = "26.1.0"
description = "CS329Z Assignment 1: Building an Agent Harness"
requires-python = ">=3.11"
dependencies = [
    "openai>=1.50",
    "python-dotenv>=1.0",
    "jsonschema>=4.20",
    "pytest>=8.0",
    "numpy>=2.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["cs329z_hw1"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-m 'not live' -q"
markers = [
    "live: makes real LLM calls (run with `uv run pytest -m live`)",
]

```
