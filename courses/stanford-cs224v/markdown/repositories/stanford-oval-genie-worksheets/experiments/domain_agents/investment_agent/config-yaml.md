# Project code: stanford-oval/genie-worksheets: experiments/domain_agents/investment_agent/config.yaml

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/domain_agents/investment_agent/config.yaml) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/domain_agents/investment_agent/config.yaml)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```yaml
validate_response: false

prompt_log_path: "logs/investment_agent_prompts.log"
conversation_log_path: "logs/investment_agent_conversation.json"

semantic_parser:
    model_name: "azure/gpt-4.1"

response_generator:
    model_name: "azure/gpt-4.1"

knowledge_parser:
    model_name: "azure/gpt-4.1"

knowledge_base:
    model_name: "azure/gpt-4.1"


```
