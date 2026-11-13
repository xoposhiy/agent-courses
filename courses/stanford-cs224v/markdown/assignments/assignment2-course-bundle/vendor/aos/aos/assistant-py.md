# Homework 2 bundle: vendor/aos/aos/assistant.py

[Course index](../../../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=vendor/aos/aos/assistant.py) · [Raw file](../../../../../../raw/assignments/assignment2-course-bundle/vendor/aos/aos/assistant.py)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```python
"""The meta-assistant: a read-only agent that answers questions about a workspace.

It can query the catalog, list and read files, and read the task records and
git history. It never changes the workspace; when work is needed it proposes a
goal for `aos run`.
"""

from __future__ import annotations

from . import prompts, trace
from .coding_agent import TOOLS as AGENT_TOOLS, CodingAgent, _assistant_message
from .tasks import Task
from .workspace import Workspace

READ_ONLY = ("query_metadata", "list_files", "read_file")

HISTORY_TOOL = {"type": "function", "function": {
    "name": "history",
    "description": "The tasks run in this workspace (goal, status, every step with worker, reason, outputs, "
                   "summary or error) and the recent git commits.",
    "parameters": {"type": "object", "properties": {}, "required": []}}}

TOOLS = [t for t in AGENT_TOOLS if t["function"]["name"] in READ_ONLY] + [HISTORY_TOOL]

SYSTEM_PROMPT = prompts.load("assistant_system")


class Assistant:
    def __init__(self, ws: Workspace, llm, max_turns: int = 12):
        self.ws = ws
        self.llm = llm
        self.max_turns = max_turns
        self.history: list[dict] = []
        self._tools = CodingAgent(llm)

    def ask(self, question: str) -> str:
        system = SYSTEM_PROMPT.format(root=self.ws.root, goal=self.ws.goal or "(none recorded)")
        messages = [{"role": "system", "content": system}, *self.history, {"role": "user", "content": question}]
        answer = "I ran out of steps while looking things up; please narrow the question."
        for _ in range(self.max_turns):
            with trace.context(trace.workspace_log(self.ws.root), purpose="assistant"):
                msg = self.llm.chat(messages, tools=TOOLS)
            if not msg.tool_calls:
                answer = (msg.content or "").strip() or "(no answer)"
                break
            messages.append(_assistant_message(msg))
            for call in msg.tool_calls:
                result = self._execute(call.function.name, call.function.arguments)
                messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
        self.history += [{"role": "user", "content": question}, {"role": "assistant", "content": answer}]
        self.history = self.history[-30:]
        return answer

    def _execute(self, name: str, arguments: str) -> str:
        if name == "history":
            return self.describe_history()
        if name not in READ_ONLY:
            return f"error: the assistant is read-only; tool {name} is not available"
        return self._tools._execute(self.ws, name, arguments)

    def describe_history(self) -> str:
        parts = []
        for task in Task.list(self.ws):
            parts.append(f"{task.id} [{task.data['status']}] goal: {task.goal}\n{task.summary_text()}")
            if task.data.get("result"):
                parts.append(f"  result: {task.data['result'][:500]}")
        parts.append("Recent commits:\n" + "\n".join(
            f"  {e['commit'][:12]} {e['date']} {e['message']}" for e in self.ws.history(20)))
        return "\n\n".join(parts) if parts else "(no tasks yet)"

```
