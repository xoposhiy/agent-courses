# Official course repository: Python, TypeScript, lesson sources, and agent UI: python/m1/m1.6_dice_server.py

[Course index](../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/python/m1/m1.6_dice_server.py) · [Raw file](../../../../../raw/repositories/lca-deepagents/python/m1/m1.6_dice_server.py)

Retrieved: 2026-11-13T16:50:31.645872+00:00

```python
import random

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("dice", log_level="WARNING")  # hide per-request logs


@mcp.tool()
def roll_dice(sides: int = 6) -> int:
    """Roll a die with the given number of sides and return the result."""
    return random.randint(1, sides)  # the same tool as Lesson 1.5


if __name__ == "__main__":
    mcp.run()  # start the server and wait for a client

```
