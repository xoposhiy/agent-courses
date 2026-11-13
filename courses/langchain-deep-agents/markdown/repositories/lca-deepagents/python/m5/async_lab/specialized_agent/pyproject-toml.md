# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m5/async_lab/specialized_agent/pyproject.toml

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m5/async_lab/specialized_agent/pyproject.toml) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/python/m5/async_lab/specialized_agent/pyproject.toml)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "async-lab-specialized-agent"
version = "0.1.0"
requires-python = ">=3.11,<3.15"

dependencies = [
    "deepagents==0.7.0",
    "langgraph>=1.0.0,<2.0",
    "langchain-anthropic",
    "langchain-openai",
    "langgraph-cli[inmem]>=0.4.0",
    "pandas>=2.2.0",
]

```
