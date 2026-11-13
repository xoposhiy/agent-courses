# Project code: stanford-oval/genie-worksheets: experiments/domain_agents/course_enroll/test_policy.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/domain_agents/course_enroll/test_policy.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/domain_agents/course_enroll/test_policy.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
from course_enroll import agent

from worksheets.components.agent_policy import AgentPolicyManager
from worksheets.core import CurrentDialogueTurn, GenieContext

local_context = GenieContext()
agent.runtime.execute(
    """
main = Main()""",
    local_context,
    sp=True,
)

agent.runtime.update_from_context(local_context)

agent_policy_manager = AgentPolicyManager(agent.runtime)

current_dlg_turn = CurrentDialogueTurn(
    user_target_sp="main.courses_to_take = CoursesToTake(course_0_details=Course(course_name='CS 322'))",
    user_target="""course = Course(course_name='CS 322')
courses_to_take = CoursesToTake(course_0_details=course)
main.courses_to_take = courses_to_take""",
    user_utterance="i will take the third one",
)
current_dlg_turn.context = GenieContext()
current_dlg_turn.global_context = GenieContext()

agent_policy_manager.run_policy(current_dlg_turn)

print(current_dlg_turn.system_action.actions)

```
