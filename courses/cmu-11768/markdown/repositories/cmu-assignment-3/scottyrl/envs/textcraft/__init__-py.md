# Assignment 3: scottyrl/envs/textcraft/__init__.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/cmu-agents/assignment-3/blob/HEAD/scottyrl/envs/textcraft/__init__.py) · [Raw file](../../../../../../raw/repositories/cmu-assignment-3/scottyrl/envs/textcraft/__init__.py)

Retrieved: 2026-11-13T16:48:20.158886+00:00

```python
"""TextCraft-Synth environment package (given): env + recipe book."""

from scottyrl.envs.textcraft.env import TextCraftEnv
from scottyrl.envs.textcraft.recipe_book import RecipeBook, default_recipe_book

__all__ = ["TextCraftEnv", "RecipeBook", "default_recipe_book"]

```
