# celebrity-agent: celebrity_agent/src/memory_store.py

[Course index](../../../../../README.md) · [Original source](https://designing-agents.github.io/assets/celebrity_agent.zip#archive-member=celebrity_agent/src/memory_store.py) · [Raw file](../../../../../raw/assignments/celebrity-agent/celebrity_agent/src/memory_store.py)

Retrieved: 2026-11-13T16:41:03.995785+00:00

```python
"""Memory store skeleton: ingest sources -> index -> retrieve."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class MemoryChunk:
    """Single memory chunk stored in the index."""

    text: str
    topic: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class MemoryStore:
    """Container for memory chunks and retrieval interface."""

    chunks: list[MemoryChunk] = field(default_factory=list)

    def retrieve(self, query: str) -> list[dict]:
        """Return the most relevant chunks for a given user query."""
        raise NotImplementedError


def build_memory_store(out_dir: str = "data/index") -> None:
    """Build the memory store from the sources."""
    # Step 1: populate data/sources.json with sources you find
    # Step 2: parse through sources and create MemoryChunks
    # Step 3: Index the MemoryChunks
    # Step 4: Save the memory store to out_dir
    raise NotImplementedError


def load_memory_store(index_dir: str = "data/index") -> MemoryStore:
    """Load a memory store from disk."""
    raise NotImplementedError


def main() -> None:
    build_memory_store()


if __name__ == "__main__":
    main()


```
