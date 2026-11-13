# Project code: stanford-oval/genie-worksheets: experiments/domain_agents/investment_agent/test_policy.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/domain_agents/investment_agent/test_policy.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/domain_agents/investment_agent/test_policy.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import asyncio

from experiments.domain_agents.investment_agent.investment_agent import (
    agent_builder,
    config,
)
from worksheets.components.agent_policy import AgentPolicyManager
from worksheets.core import CurrentDialogueTurn, GenieContext
from worksheets.utils.annotation import get_context_schema


async def main():
    agent = agent_builder.build(config)

    current_dlg_turn = CurrentDialogueTurn(
        user_target_sp="""FundInvestment(
    fund_allocations = FundAllocation(
        fund_to_invest_in = answer("Find Fidelity Low-Priced Stock K", datatype=Fund),   # Fidelity Low-Priced Stock K
        investment_amount = GetAccountBalance()  # all the user's money
    )
)""",
        user_utterance="i will invest all my money in the fidelity low-priced stock k",
    )
    current_dlg_turn.context = GenieContext()
    current_dlg_turn.global_context = GenieContext()

    genie_agent_policy_manager = AgentPolicyManager(agent.runtime)

    await agent.genie_parser.parse(current_dlg_turn, [])

    genie_agent_policy_manager.run_policy(current_dlg_turn)

    print(current_dlg_turn.system_action.actions)
    print(get_context_schema(current_dlg_turn.context))
    print("hola")


if __name__ == "__main__":
    asyncio.run(main())

```
