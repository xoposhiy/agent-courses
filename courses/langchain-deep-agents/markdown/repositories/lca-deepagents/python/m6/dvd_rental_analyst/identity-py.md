# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m6/dvd_rental_analyst/identity.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m6/dvd_rental_analyst/identity.py) · [Raw file](../../../../../../raw/repositories/lca-deepagents/python/m6/dvd_rental_analyst/identity.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
from managed_deepagents import define_identity, auth

identity = define_identity(auth=auth.langsmith_api_key())

```
