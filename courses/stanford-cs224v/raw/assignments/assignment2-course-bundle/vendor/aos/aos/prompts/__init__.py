"""Every prompt AOS sends to the model, as text files next to this module.

| file | used by | placeholders |
|---|---|---|
| ``planner_system.txt`` | the planner's system message | – |
| ``planner.txt`` | the planner's decision request | ``{goal}``, ``{workers}``, ``{tree}``, ``{history}`` (literal braces doubled) |
| ``summary.txt`` | one-sentence catalog summaries of new files | ``{context}``, ``{files}`` |
| ``coding_agent_system.txt`` | the coding agent's system message | – |
| ``coding_agent_turn_limit.txt`` | asks the coding agent to wrap up after its last turn | – |
| ``assistant_system.txt`` | the read-only assistant's system message | ``{root}``, ``{goal}`` |
| ``nl2sql.txt`` | the UI's plain-English to SQL box | ``{schema}``, ``{counts}``, ``{samples}``, ``{question}`` |

Edit the files to change AOS's behaviour; the code formats them with ``str.format``. The runner
scripts under ``capabilities/runners/`` keep their prompts inline because they run in the external
systems' own virtualenvs and are copied into workspaces, where this package is not importable.
"""

from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent


def load(name: str) -> str:
    """The prompt text in ``<name>.txt`` (without the file's final newline)."""
    return (PROMPTS_DIR / f"{name}.txt").read_text().rstrip("\n")
