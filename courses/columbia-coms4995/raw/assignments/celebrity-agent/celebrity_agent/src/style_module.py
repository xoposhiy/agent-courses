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