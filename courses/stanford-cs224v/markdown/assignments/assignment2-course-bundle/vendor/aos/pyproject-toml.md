# Homework 2 bundle: vendor/aos/pyproject.toml

[Course index](../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/pyproject.toml) · [Raw file](../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/pyproject.toml)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```toml
[project]
name = "aos"
version = "0.1.0"
description = "Agentic Operating System: filesystem-first, git-first orchestration of research capabilities and coding agents"
requires-python = ">=3.10"
dependencies = [
    "openai>=1.40",
    "pandas>=2.3.3",
    "python-dotenv>=1.0",
]

[project.scripts]
aos = "aos.cli:main"

[dependency-groups]
dev = ["pytest>=8"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["aos"]

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = ["live: calls the real LLM endpoint or external systems (opt in with AOS_LIVE=1)"]

```
