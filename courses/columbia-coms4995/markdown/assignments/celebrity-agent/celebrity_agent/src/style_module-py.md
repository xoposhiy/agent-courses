# celebrity-agent: celebrity_agent/src/style_module.py

[Course index](../../../../../README.md) · [Original source](https://designing-agents.github.io/assets/celebrity_agent.zip#archive-member=celebrity_agent/src/style_module.py) · [Raw file](../../../../../raw/assignments/celebrity-agent/celebrity_agent/src/style_module.py)

Retrieved: 2026-11-13T16:41:03.995785+00:00

```python
"""Style module: convert content plan into a celebrity-like response."""

from .llm import query_llm

def stylize(content_plan: str) -> str:
    """Turn a content plan string into a celebrity-voiced response."""
    
    style_prompt = f"""
    Add your prompt here. Include the content plan.

    Content plan:
    {content_plan}
    """

    return query_llm(style_prompt, temperature=0.0)
```
