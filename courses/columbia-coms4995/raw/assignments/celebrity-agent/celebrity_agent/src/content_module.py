"""Content module: retrieval-backed response planning."""
from .llm import query_llm
from .memory_store import MemoryStore


def make_content_plan(user_message: str, retrieved: list[dict], history: list[dict]) -> str:
    """Create a response outline using the retrieved evidence and the conversation so far."""

    content_plan_prompt = f'''
    Add your prompt here. Include the conversation so far, the user message, and the retrieved evidence.

    Conversation so far:
    {history}
    User message: {user_message}
    Retrieved evidence:
    {retrieved}
    '''

    llm_text = query_llm(content_plan_prompt, temperature=0.0)

    return llm_text



def content_step(memory: MemoryStore, user_message: str, history: list[dict]) -> dict:
    """Retrieve evidence and convert it into a content plan."""
    retrieved_chunks = memory.retrieve(query=user_message)
    plan = make_content_plan(user_message=user_message, retrieved=retrieved_chunks, history=history)
    return {"content_plan": plan, "retrieved_chunks": retrieved_chunks}
