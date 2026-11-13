# Homework 1 public teaching repository: vendor/grill/pyproject.toml

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/cs224vf26-assignment1-public/blob/HEAD/vendor/grill/pyproject.toml) · [Raw file](../../../../../raw/repositories/cs224vf26-assignment1-public/vendor/grill/pyproject.toml)

Retrieved: 2026-11-13T16:58:36.902200+00:00

```toml
[project]
name = "methodology-v2"
version = "0.0.1"
description = "Budget-bounded, self-correcting literature-research agent with an online-calibrated belief ledger."
requires-python = ">=3.12"
dependencies = [
    "openai>=1.0",   # text-embedding-3-large for frontier/context scoring (lazily imported)
]

[project.scripts]
methodology-v2 = "src.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src"]

[dependency-groups]
dev = [
    "pytest>=8",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra"

```
