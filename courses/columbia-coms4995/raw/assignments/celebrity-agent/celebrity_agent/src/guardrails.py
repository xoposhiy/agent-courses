"""Guardrails: decline questions the celebrity would not know about."""


def out_of_scope(user_message: str, history: list[dict]) -> bool:
    """Return True if the message asks about events after the knowledge cutoff or outside the celebrity's expertise."""
    raise NotImplementedError

def decline(user_message: str) -> str:
    """Return an in-character response saying the celebrity doesn't know."""
    raise NotImplementedError
