# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m3/m3.2-skills.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m3/m3.2-skills.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m3/m3.2-skills.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m3.2-skills.md)

Python TypeScript

<a id="skills"></a>


# Skills

```text
<button class="lt-tab active" data-p="skills" role="tab" aria-selected="true">Skills</button>
```

```text
<button class="lt-tab" data-p="lab" role="tab" aria-selected="false">Lab</button>
```

```text
<button class="lt-tab" data-p="quiz" role="tab" aria-selected="false">Quiz</button>
```

```text
<button class="lt-tab" data-p="homework" role="tab" aria-selected="false">Homework</button>
```

<a id="p-skills"></a>


A skill is a directory containing a `SKILL.md` file. Skills follow an [open standard](../../../../../readings/agentskills-io-specification-f36ae400.md), which means they are portable across agents and shareable across teams.

Quick Overview: What is a Skill

[Quick Overview: What is a Skill](https://www.youtube.com/embed/bv1qgkbWhms)


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/0DoYTlG67pf.md)


[Skill directory structure; use arrow keys or Prev/Next to navigate](../../../../../lesson-assets/m3.2-skill-structure.md)

<a id="the-skill.md-file"></a>


### The SKILL.md file

Each skill lives in its own named directory, and the directory name should match the `name` field in the frontmatter (this is the Agent Skills spec convention; if they differ, deepagents logs a warning but still loads the skill):

The `SKILL.md` file has two parts: a YAML frontmatter block at the top, and the skill instructions below it.

![SKILL.md anatomy: YAML frontmatter and skill instructions sections labelled](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m3/images/m3.2-skill-anatomy.svg)

When a thread first runs, `SkillsMiddleware` reads each `SKILL.md` through the backend and keeps only the frontmatter’s `name` and `description`. The model loads the full body with `read_file` when it activates a skill. Write the `description` to clearly answer when the skill should be used. Keep it brief and specific.

The recognized frontmatter fields are:

| Field | Required | Notes |
| --- | --- | --- |
| `name` | yes | Lowercase, alphanumeric, hyphens only. Should match the directory name. |
| `description` | yes | Describes when to use this skill. Kept brief; always in context. |
| `allowed-tools` | no | Space-separated list of tool names the skill may use. |
| `compatibility` | no | Environment or version requirements. |
| `metadata` | no | Arbitrary key-value pairs. |

If a `SKILL.md` is missing `name` or `description`, deepagents skips that skill and logs a warning.

<a id="progressive-disclosure"></a>


## Progressive disclosure

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/pDra5U0wKtN.md)

Skills use a three-stage pattern to keep the agent’s context lean:

**1. Discovery**

Before the model runs, the SDK parses each skill’s frontmatter in code, without any tool call from the model. It then adds every skill’s `name` and `description` to the system prompt on each model call. The SDK writes this section for you. A simplified version looks like this:

```text
## Skills System

Available skills:
- **qualify-lead**: Use when the user wants to qualify a sales lead or prospect.
  -> Read skills/qualify-lead/SKILL.md for full instructions.
- **draft-pitch**: Use when the user wants to write a sales pitch or outreach message.
  -> Read skills/draft-pitch/SKILL.md for full instructions.

```

Both the `name` and `description` are always in context, so keep them short and precise. The `description` in particular should describe only **when** to use the skill, not what it does internally.

**2. Activation**

When a task matches a skill’s description, the agent calls `read_file` on the path shown in the system prompt, which brings the full `SKILL.md` into its context.

**3. Execution**

The agent follows the instructions in the skill body, calling any tools it needs and using any bundled files referenced in the instructions.

You can see all three stages in a LangSmith trace: the Skills System section appears in every system message; the `read_file` call marks the moment of activation; and the subsequent tool calls show execution.

**Skills go further than static text.** An agent can write and edit its own skill files over time, refining them from the preferences and patterns it learns on the job. Skills can also include executable scripts in a `scripts/` subdirectory, which the agent can run in a sandbox, enabling more advanced workflows like code generation, data processing, or multi-step automation.

**Skills vs. Tools:**   
  

- A **tool** is a function the model calls to *do* something: search the web, write a file, hit an API. Calling it takes an action and returns a result.
- A **skill** is markdown instructions (plus optional bundled scripts) that the agent reads via `read_file` when a task matches its `description`.

In practice, a skill’s instructions just tell the agent which of its existing tools to use, and how.

**New update: pinned skills.** To make sure the agent uses a skill (e.g. when the user names the skill), pass the skill’s name in `pinned_skills`. The skill’s full `SKILL.md` is added to the conversation before the next model call, so the agent doesn’t have to choose to read it.

```text
agent.invoke({
    "messages": [{"role": "user", "content": "Qualify Acme Corp."}],
    "pinned_skills": ["qualify-lead"],
})
```

Added in deepagents 0.7.23. The labs don’t use it.

**New update: skill tools.** A skill can list tools in its frontmatter under `metadata.include_tools`. The agent only sees those tools after it reads that skill’s `SKILL.md`, or after the skill is pinned. Until then, the tools stay out of the prompt.

```text
metadata:
  include_tools: create_customer_request list_customer_requests
```

The tools themselves are passed to `SkillsMiddleware(tools=[...])`.

Added in deepagents 0.7.22. The labs don’t use it.

---

<a id="how-to-use-skills"></a>


## How to use skills

Using a skill has three parts.

<a id="create-a-skill-directory"></a>


### 1. Create a skill directory

Each skill is a directory with a `SKILL.md` file:

```text
skills/
  qualify-lead/
    SKILL.md
  draft-pitch/
    SKILL.md
```

The directory name should match the `name` field in `SKILL.md`.

<a id="write-the-metadata-and-instructions"></a>


### 2. Write the metadata and instructions

```text
---
name: qualify-lead
description: Use when the user wants to qualify a sales lead or prospect.
---

# Qualify a Lead

Follow these steps...
```

The `description` is the trigger. The body is the detailed procedure the agent reads after activation.

<a id="put-the-skills-in-the-agents-backend-and-register-them"></a>


### 3. Put the skills in the agent’s backend and register them

Skills are files, so they must be available through the agent’s backend. The `skills` argument points to a directory path in that backend.

```text
from deepagents.backends import FilesystemBackend

backend = FilesystemBackend(root_dir="/path/to/agent-files", virtual_mode=True)

agent = create_deep_agent(
    model=model,
    backend=backend,
    skills=["/skills"],
)
```

In this example, the backend must contain `/skills/qualify-lead/SKILL.md` and `/skills/draft-pitch/SKILL.md`. The agent discovers each skill’s `name` and `description`, then reads the full `SKILL.md` through its filesystem tools only when needed.

At runtime, the agent:

1. Sees all skill names and descriptions in the system prompt
2. Matches the user request to a skill description
3. Calls `read_file` on that skill’s `SKILL.md`
4. Follows the full instructions in the skill body

In LangSmith, you can debug this by checking the system prompt for the discovery list, the `read_file` call for activation, and the later tool calls or final output for execution.

![LangChain](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m3/images/langchain-symbol.png)

**LangChain Blog**

[How Stripe built their Knowledge AI Platform on Deep Agents](https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents)

Stripe’s internal agent, Kai, runs 1,000+ skills across 100+ teams, using skill selection to decide which of 500+ internal tools get loaded into context. Past a few hundred skills, description-based discovery alone starts to degrade, so Kai adds a second gating pass, using each skill’s `allowedTools` list to filter which tools actually load.

Case Study Video Walkthrough

[Case Study Video Walkthrough](https://www.youtube.com/embed/rduH9wnXto8)

<a id="recap"></a>


## Recap

- A skill is a directory with a `SKILL.md`: YAML frontmatter (`name`, `description`) plus markdown instructions. Skills follow the open Agent Skills spec, so they’re portable across agents.
- Skills use **progressive disclosure**. The middleware reads each frontmatter in code and lists only each skill’s name, description, and path in the system prompt. The model calls `read_file` to load the full body when a task matches, then follows it.
- Write the `description` to say **when** to use the skill, since it’s what the agent matches against.
- Skills are files, so they live in the agent’s backend; the `skills` argument points at a directory in that backend.
- A skill doesn’t do anything by itself. It tells the agent how to use the tools it already has.
- In LangSmith, the skills list in the system prompt is discovery, the `read_file` call is activation, and the tool calls after it are execution.

---

<a id="references"></a>


## References

**Documentation:**

- [Skills (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-skills-f5e8a740.md)
- [Agent Skills specification](../../../../../readings/agentskills-io-specification-f36ae400.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/skills.py`](../../../../../readings/github-68d211f35aae.md): how skills are discovered and added to the system prompt

A skill is a directory containing a `SKILL.md` file. Skills follow an [open standard](../../../../../readings/agentskills-io-specification-f36ae400.md), which means they are portable across agents and shareable across teams.

Quick Overview: What is a Skill

[Quick Overview: What is a Skill](https://www.youtube.com/embed/bv1qgkbWhms)


Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/0DoYTlG67pf.md)


[Skill directory structure; use arrow keys or Prev/Next to navigate](../../../../../lesson-assets/m3.2-skill-structure.md)

<a id="the-skill.md-file-1"></a>


### The SKILL.md file

Each skill lives in its own named directory, and the directory name should match the `name` field in the frontmatter (this is the Agent Skills spec convention; if they differ, deepagents logs a warning but still loads the skill):

The `SKILL.md` file has two parts: a YAML frontmatter block at the top, and the skill instructions below it.

![SKILL.md anatomy: YAML frontmatter and skill instructions sections labelled](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m3/images/m3.2-skill-anatomy.svg)

When a thread first runs, `SkillsMiddleware` reads each `SKILL.md` through the backend and keeps only the frontmatter’s `name` and `description`. The model loads the full body with `read_file` when it activates a skill. Write the `description` to clearly answer when the skill should be used. Keep it brief and specific.

The recognized frontmatter fields are:

| Field | Required | Notes |
| --- | --- | --- |
| `name` | yes | Lowercase, alphanumeric, hyphens only. Should match the directory name. |
| `description` | yes | Describes when to use this skill. Kept brief; always in context. |
| `allowed-tools` | no | Space-separated list of tool names the skill may use. |
| `compatibility` | no | Environment or version requirements. |
| `metadata` | no | Arbitrary key-value pairs. |

If a `SKILL.md` is missing `name` or `description`, deepagents skips that skill and logs a warning.

<a id="progressive-disclosure-1"></a>


## Progressive disclosure

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/pDra5U0wKtN.md)

Skills use a three-stage pattern to keep the agent’s context lean:

**1. Discovery**

Before the model runs, the SDK parses each skill’s frontmatter in code, without any tool call from the model. It then adds every skill’s `name` and `description` to the system prompt on each model call. The SDK writes this section for you. A simplified version looks like this:

```text
## Skills System

Available skills:
- **qualify-lead**: Use when the user wants to qualify a sales lead or prospect.
  -> Read skills/qualify-lead/SKILL.md for full instructions.
- **draft-pitch**: Use when the user wants to write a sales pitch or outreach message.
  -> Read skills/draft-pitch/SKILL.md for full instructions.

```

Both the `name` and `description` are always in context, so keep them short and precise. The `description` in particular should describe only **when** to use the skill, not what it does internally.

**2. Activation**

When a task matches a skill’s description, the agent calls `read_file` on the path shown in the system prompt, which brings the full `SKILL.md` into its context.

**3. Execution**

The agent follows the instructions in the skill body, calling any tools it needs and using any bundled files referenced in the instructions.

You can see all three stages in a LangSmith trace: the Skills System section appears in every system message; the `read_file` call marks the moment of activation; and the subsequent tool calls show execution.

**Skills go further than static text.** An agent can write and edit its own skill files over time, refining them from the preferences and patterns it learns on the job. Skills can also include executable scripts in a `scripts/` subdirectory, which the agent can run in a sandbox, enabling more advanced workflows like code generation, data processing, or multi-step automation.

**Skills vs. Tools:**   
  

- A **tool** is a function the model calls to *do* something: search the web, write a file, hit an API. Calling it takes an action and returns a result.
- A **skill** is markdown instructions (plus optional bundled scripts) that the agent reads via `read_file` when a task matches its `description`.

In practice, a skill’s instructions just tell the agent which of its existing tools to use, and how.

**New update: pinned skills and skill tools.** The Python SDK can now force a skill’s `SKILL.md` into the conversation (`pinned_skills`), and can hide a skill’s tools until the agent reads that skill (`metadata.include_tools`). Neither is in the TypeScript SDK yet.

---

<a id="how-to-use-skills-1"></a>


## How to use skills

Using a skill has three parts.

<a id="create-a-skill-directory-1"></a>


### 1. Create a skill directory

Each skill is a directory with a `SKILL.md` file:

```text
skills/
  qualify-lead/
    SKILL.md
  draft-pitch/
    SKILL.md
```

The directory name should match the `name` field in `SKILL.md`.

<a id="write-the-metadata-and-instructions-1"></a>


### 2. Write the metadata and instructions

```text
---
name: qualify-lead
description: Use when the user wants to qualify a sales lead or prospect.
---

# Qualify a Lead

Follow these steps...
```

The `description` is the trigger. The body is the detailed procedure the agent reads after activation.

<a id="put-the-skills-in-the-agents-backend-and-register-them-1"></a>


### 3. Put the skills in the agent’s backend and register them

Skills are files, so they must be available through the agent’s backend. The `skills` argument points to a directory path in that backend.

```text
import { createDeepAgent, FilesystemBackend } from "deepagents";

const backend = new FilesystemBackend({ rootDir: "/path/to/agent-files", virtualMode: true });

const agent = createDeepAgent({
  model,
  backend,
  skills: ["/skills"],
});
```

In this example, the backend must contain `/skills/qualify-lead/SKILL.md` and `/skills/draft-pitch/SKILL.md`. The agent discovers each skill’s `name` and `description`, then reads the full `SKILL.md` through its filesystem tools only when needed.

At runtime, the agent:

1. Sees all skill names and descriptions in the system prompt
2. Matches the user request to a skill description
3. Calls `read_file` on that skill’s `SKILL.md`
4. Follows the full instructions in the skill body

In LangSmith, you can debug this by checking the system prompt for the discovery list, the `read_file` call for activation, and the later tool calls or final output for execution.

![LangChain](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m3/images/langchain-symbol.png)

**LangChain Blog**

[How Stripe built their Knowledge AI Platform on Deep Agents](https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents)

Stripe’s internal agent, Kai, runs 1,000+ skills across 100+ teams, using skill selection to decide which of 500+ internal tools get loaded into context. Past a few hundred skills, description-based discovery alone starts to degrade, so Kai adds a second gating pass, using each skill’s `allowedTools` list to filter which tools actually load.

Case Study Video Walkthrough

[Case Study Video Walkthrough](https://www.youtube.com/embed/rduH9wnXto8)

<a id="recap-1"></a>


## Recap

- A skill is a directory with a `SKILL.md`: YAML frontmatter (`name`, `description`) plus markdown instructions. Skills follow the open Agent Skills spec, so they’re portable across agents.
- Skills use **progressive disclosure**. The middleware reads each frontmatter in code and lists only each skill’s name, description, and path in the system prompt. The model calls `read_file` to load the full body when a task matches, then follows it.
- Write the `description` to say **when** to use the skill, since it’s what the agent matches against.
- Skills are files, so they live in the agent’s backend; the `skills` argument points at a directory in that backend.
- A skill doesn’t do anything by itself. It tells the agent how to use the tools it already has.
- In LangSmith, the skills list in the system prompt is discovery, the `read_file` call is activation, and the tool calls after it are execution.

---

<a id="references-1"></a>


## References

**Documentation:**

- [Skills (Deep Agents)](../../../../../readings/docs-langchain-com-oss-javascript-deepagents-skills-b3b63e4f.md)
- [Agent Skills specification](../../../../../readings/agentskills-io-specification-f36ae400.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`middleware/skills.ts`](../../../../../readings/github-5711e73a42da.md): how skills are discovered and added to the system prompt

<a id="p-quiz"></a>


## Check your understanding

<a id="p-lab"></a>


<a id="sales-assistant-with-skills"></a>


## Sales Assistant with Skills

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/XxEWKNe2z1p.md)

**Inspect your own run in LangSmith.** Notice the skill descriptions are visible upfront, but the matching `SKILL.md` is only read once the agent decides it needs it.

LangSmith Video Walkthrough

[Public video walkthrough](../../../../../videos/KqVlE3klzVJ.md)

This lab uses a sales assistant with two skills: one for qualifying leads and one for drafting pitches. Using two skills makes the discovery and activation stages visible: both descriptions are always in the system prompt, but only the relevant skill’s `SKILL.md` is read when needed.

All files are already in the repo under `python/m3/`. Open `m3.2_scratch_agent_skills.py` and run it directly, or use a coding agent to explore the setup.

---

<a id="qualify-leadskill.md"></a>


### 1. `qualify-lead/SKILL.md`

Located at `python/m3/skills/qualify-lead/SKILL.md`:

```text
---
name: qualify-lead
description: Use when the user wants to qualify a sales lead or prospect.
---

# Qualify a Lead

Use the BANT framework to qualify the prospect systematically.

**Step 1: Budget**: Ask what budget range they are working with and how purchasing decisions are made in their organisation.

**Step 2: Authority**: Confirm whether you are speaking with the decision maker. If not, ask who is and whether they can be involved.

**Step 3: Need**: Understand the specific pain point. What problem are they trying to solve? What happens if it stays unsolved?

**Step 4: Timeline**: Ask when they are looking to make a decision and when they would need the solution running.

## Output

After gathering responses, classify the lead and summarise your findings:

- **Qualified**: clear budget, authority confirmed, defined need, decision within 90 days
- **Nurture**: one or more gaps; recommend a follow-up in 30 days
- **Disqualify**: no budget, no authority, or no real need identified
```

---

<a id="draft-pitchskill.md"></a>


### 2. `draft-pitch/SKILL.md`

Located at `python/m3/skills/draft-pitch/SKILL.md`:

```text
---
name: draft-pitch
description: Use when the user wants to write a sales pitch or outreach message for a prospect.
---

# Draft a Sales Pitch

Follow these steps to write a concise, effective pitch.

**Step 1: Research**: Ask for the prospect's company name, their role, and any context about their situation or pain points.

**Step 2: Hook**: Open with one sentence that names the problem they are likely experiencing.

**Step 3: Value proposition**: One to two sentences explaining what the product does and who it is for.

**Step 4: Social proof**: One brief example: "We helped [similar company] achieve [specific result]."

**Step 5: Call to action**: End with a specific, low-friction ask; a 15-minute call or a short reply.

Keep the final pitch under 150 words.
```

---

<a id="m3.2_scratch_agent_skills.py"></a>


### 3. `m3.2_scratch_agent_skills.py`

Here’s how `python/m3/m3.2_scratch_agent_skills.py` wires the skills into the agent:

```text
# python/m3/m3.2_scratch_agent_skills.py
from pathlib import Path

from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend

from models import model

m3_dir = Path(__file__).parent
backend = FilesystemBackend(root_dir=str(m3_dir), virtual_mode=True)

agent = create_deep_agent(
    model=model,
    name="Sales_Assistant",
    backend=backend,
    skills=["/skills"],
    system_prompt="You are a sales assistant.",
)

result = agent.invoke({"messages": [{"role": "user", "content": "Qualify this lead: Acme Corp, 200-person logistics company. I spoke with Sarah Chen, VP of Sales: she's the decision maker. They have $45k budgeted for CRM this year. Main pain: deals are slipping through the cracks due to poor pipeline visibility. They want a solution live by end of Q3."}]})
print(result["messages"][-1].text)
```

Try swapping in either question to see both skills activate:

- `"Qualify this lead: Acme Corp, 200-person logistics company. I spoke with Sarah Chen, VP of Sales: she's the decision maker. They have $45k budgeted for CRM this year. Main pain: deals are slipping through the cracks due to poor pipeline visibility. They want a solution live by end of Q3."`
- `"Write a cold outreach message for a prospect at a mid-size logistics company."`

---

<a id="run-it"></a>


### Run it

Before running it, make sure your model API key from setup is available in the Python environment.

From the repo root:

```text
cd python
uv run ./m3/m3.2_scratch_agent_skills.py
```

---

<a id="what-to-look-for-in-langsmith"></a>


### What to look for in LangSmith

Open the run and check the system message on the first LLM call. You should see a **Skills System** section listing both skill names and descriptions, but no body content from either `SKILL.md`. This is discovery.

To see activation, turn on **Hidden runs** in LangSmith to show the full execution tree, including middleware. Find the `read_file` entry nested inside `FilesystemMiddleware` and click into it, then open the **Output** tab. You will see the full body of whichever skill matched: the BANT steps for a qualify-lead request, or the pitch steps for a draft-pitch request. That is activation: the agent loaded exactly one skill body, on demand, because the task matched its description.

Try both questions in two separate runs and compare which skill body appears in the `read_file` output.

**Why the name and description are what matter at discovery**  
 The name and description are the discovery text the agent sees before deciding whether to activate a skill. The full body, the steps, the output format: none of it is visible until `read_file` is called. Write the description to clearly answer: “In what situation should this skill be used?” Keep it brief and specific.

<a id="sales-assistant-with-skills-1"></a>


## Sales Assistant with Skills

Lab Video Walkthrough

[Public video walkthrough](../../../../../videos/XxEWKNe2z1p.md)

**Inspect your own run in LangSmith.** Notice the skill descriptions are visible upfront, but the matching `SKILL.md` is only read once the agent decides it needs it.

LangSmith Video Walkthrough

[Public video walkthrough](../../../../../videos/KqVlE3klzVJ.md)

This lab uses a sales assistant with two skills: one for qualifying leads and one for drafting pitches. Using two skills makes the discovery and activation stages visible: both descriptions are always in the system prompt, but only the relevant skill’s `SKILL.md` is read when needed.

All files are already in the repo under `typescript/m3/`. Open `m3.2_scratch_agent_skills.ts` and run it directly, or use a coding agent to explore the setup.

---

<a id="qualify-leadskill.md-1"></a>


### 1. `qualify-lead/SKILL.md`

Located at `typescript/m3/skills/qualify-lead/SKILL.md`:

```text
---
name: qualify-lead
description: Use when the user wants to qualify a sales lead or prospect.
---

# Qualify a Lead

Use the BANT framework to qualify the prospect systematically.

**Step 1: Budget**: Ask what budget range they are working with and how purchasing decisions are made in their organisation.

**Step 2: Authority**: Confirm whether you are speaking with the decision maker. If not, ask who is and whether they can be involved.

**Step 3: Need**: Understand the specific pain point. What problem are they trying to solve? What happens if it stays unsolved?

**Step 4: Timeline**: Ask when they are looking to make a decision and when they would need the solution running.

## Output

After gathering responses, classify the lead and summarise your findings:

- **Qualified**: clear budget, authority confirmed, defined need, decision within 90 days
- **Nurture**: one or more gaps; recommend a follow-up in 30 days
- **Disqualify**: no budget, no authority, or no real need identified
```

---

<a id="draft-pitchskill.md-1"></a>


### 2. `draft-pitch/SKILL.md`

Located at `typescript/m3/skills/draft-pitch/SKILL.md`:

```text
---
name: draft-pitch
description: Use when the user wants to write a sales pitch or outreach message for a prospect.
---

# Draft a Sales Pitch

Follow these steps to write a concise, effective pitch.

**Step 1: Research**: Ask for the prospect's company name, their role, and any context about their situation or pain points.

**Step 2: Hook**: Open with one sentence that names the problem they are likely experiencing.

**Step 3: Value proposition**: One to two sentences explaining what the product does and who it is for.

**Step 4: Social proof**: One brief example: "We helped [similar company] achieve [specific result]."

**Step 5: Call to action**: End with a specific, low-friction ask; a 15-minute call or a short reply.

Keep the final pitch under 150 words.
```

---

<a id="m3.2_scratch_agent_skills.ts"></a>


### 3. `m3.2_scratch_agent_skills.ts`

Here’s how `typescript/m3/m3.2_scratch_agent_skills.ts` wires the skills into the agent:

```text
// typescript/m3/m3.2_scratch_agent_skills.ts
import { dirname } from "node:path";
import { fileURLToPath } from "node:url";

import { context } from "langchain";
import { createDeepAgent, FilesystemBackend } from "deepagents";

import { model } from "../models.js";

const m3Dir = dirname(fileURLToPath(import.meta.url));
const backend = new FilesystemBackend({ rootDir: m3Dir, virtualMode: true });

const agent = createDeepAgent({
  model,
  name: "Sales_Assistant",
  backend,
  skills: ["/skills"],
  systemPrompt: "You are a sales assistant.",
});

const result = await agent.invoke({
  messages: [
    {
      role: "user",
      content: context`
        Qualify this lead: Acme Corp, 200-person logistics company. I spoke with
        Sarah Chen, VP of Sales: she's the decision maker. They have $45k budgeted
        for CRM this year. Main pain: deals are slipping through the cracks due to
        poor pipeline visibility. They want a solution live by end of Q3.`,
    },
  ],
});

console.log(result.messages.at(-1)?.text);
```

Try swapping in either question to see both skills activate:

- `"Qualify this lead: Acme Corp, 200-person logistics company. I spoke with Sarah Chen, VP of Sales: she's the decision maker. They have $45k budgeted for CRM this year. Main pain: deals are slipping through the cracks due to poor pipeline visibility. They want a solution live by end of Q3."`
- `"Write a cold outreach message for a prospect at a mid-size logistics company."`

---

<a id="run-it-1"></a>


### Run it

Before running it, make sure your model API key from setup is available in the TypeScript environment.

From the repo root:

```text
cd typescript
pnpm tsx ./m3/m3.2_scratch_agent_skills.ts
```

---

<a id="what-to-look-for-in-langsmith-1"></a>


### What to look for in LangSmith

Open the run and check the system message on the first LLM call. You should see a **Skills System** section listing both skill names and descriptions, but no body content from either `SKILL.md`. This is discovery.

To see activation, turn on **Hidden runs** in LangSmith to show the full execution tree, including middleware. Find the `read_file` entry nested inside `FilesystemMiddleware` and click into it, then open the **Output** tab. You will see the full body of whichever skill matched: the BANT steps for a qualify-lead request, or the pitch steps for a draft-pitch request. That is activation: the agent loaded exactly one skill body, on demand, because the task matched its description.

Try both questions in two separate runs and compare which skill body appears in the `read_file` output.

**Why the name and description are what matter at discovery**  
 The name and description are the discovery text the agent sees before deciding whether to activate a skill. The full body, the steps, the output format: none of it is visible until `read_file` is called. Write the description to clearly answer: “In what situation should this skill be used?” Keep it brief and specific.

<a id="p-homework"></a>


<a id="bundle-a-reference-file-into-your-skill"></a>


## Bundle a Reference File Into Your Skill

The lab’s two skills, qualify-lead and draft-pitch, are each a single flat `SKILL.md` file with everything inline. This homework asks you to go one step further: write a skill for a topic or workflow of your choosing (not sales) that bundles a second file, `reference.md` (holding details the agent needs but that aren’t written into `SKILL.md` itself), then confirm from the trace that the agent actually called `read_file` on that second file before answering.

Open `python/m3/m3.2_homework.py`.

1. **TODO 1**: write your own `SKILL.md` content, frontmatter and all, for a workflow of your choosing (planning a workout, reviewing a resume, triaging a bug report, etc.). It must instruct the agent to read `reference.md` for specific details and must not restate those details inline. The `name` field in your frontmatter must exactly match `SKILL_NAME` in the file.
2. **TODO 2**: write `reference.md`’s content, the specific facts, numbers, or template your `SKILL.md` points to and depends on.
3. **TODO 3**: write a system prompt for the agent and a user question that should activate your skill, matching your skill’s `description`.

The script checks the returned messages for a `read_file` call on your `reference.md` path and prints whether it found one.

<a id="run-it-2"></a>


### Run it

```text
cd python
uv run ./m3/m3.2_homework.py
```

Stuck, or want to see the finished shape before you start? `m3.2_homework_filled.py` is a reference copy with every TODO filled in (using a workout-planning skill and a hype personal-trainer persona); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a skill for a new topic of your choosing (e.g. a trip-planning checklist, a code-review rubric, a meal-prep guide…), with none of the wiring given.

**Requirements:**

- Set up your own `backend` (a `FilesystemBackend` pointed at a real directory, not a temp one) and pick the skills directory layout yourself.
- Wire skills with the `skills=[...]` shorthand on `create_deep_agent`, or with `SkillsMiddleware(backend=..., sources=[...])` via `middleware=[...]` for per-source display labels. Write this in a new file under `python/m3/`.
- Bundle more than one supporting file if it fits your idea:
  - Add a `scripts/` subdirectory with a helper script, an extra reference doc, or a config file.
  - Point to these from `SKILL.md` by absolute path (the same way it points to `reference.md`).
  - If you bundle a script, give the agent an execution tool (a shell/execute tool, or a sandbox) so it can actually run it. No execution tool -> tell `SKILL.md` to just read and reason about the script instead.

```text
# Example skill directory layout
skills/
  your-skill/
    SKILL.md
    reference.md
    scripts/
      helper.py
```

- Write the agent call and a triggering question from scratch, then confirm activation from the trace yourself.

<a id="bundle-a-reference-file-into-your-skill-1"></a>


## Bundle a Reference File Into Your Skill

The lab’s two skills, qualify-lead and draft-pitch, are each a single flat `SKILL.md` file with everything inline. This homework asks you to go one step further: write a skill for a topic or workflow of your choosing (not sales) that bundles a second file, `reference.md` (holding details the agent needs but that aren’t written into `SKILL.md` itself), then confirm from the trace that the agent actually called `read_file` on that second file before answering.

Open `typescript/m3/m3.2_homework.ts`.

1. **TODO 1**: write your own `SKILL.md` content, frontmatter and all, for a workflow of your choosing (planning a workout, reviewing a resume, triaging a bug report, etc.). It must instruct the agent to read `reference.md` for specific details and must not restate those details inline. The `name` field in your frontmatter must exactly match `SKILL_NAME` in the file.
2. **TODO 2**: write `reference.md`’s content, the specific facts, numbers, or template your `SKILL.md` points to and depends on.
3. **TODO 3**: write a system prompt for the agent and a user question that should activate your skill, matching your skill’s `description`.

The script checks the returned messages for a `read_file` call on your `reference.md` path and prints whether it found one.

<a id="run-it-3"></a>


### Run it

```text
cd typescript
pnpm tsx ./m3/m3.2_homework.ts
```

Stuck, or want to see the finished shape before you start? `m3.2_homework_filled.ts` is a reference copy with every TODO filled in (using a workout-planning skill and a hype personal-trainer persona); run it the same way to see what “done” looks like end to end.

Try to avoid peeking unless you’re really stuck. You’ll get more out of this by working through the TODOs yourself first.

---


Optional Extension: Want To Code From Scratch?

**What you’ll build:** a skill for a new topic of your choosing (e.g. a trip-planning checklist, a code-review rubric, a meal-prep guide…), with none of the wiring given.

**Requirements:**

- Set up your own `backend` (a `FilesystemBackend` pointed at a real directory, not a temp one) and pick the skills directory layout yourself.
- Wire skills with the `skills: [...]` shorthand on `createDeepAgent`, or with `SkillsMiddleware({ backend, sources })` via `middleware: [...]` for per-source display labels. Write this in a new file under `typescript/m3/`.
- Bundle more than one supporting file if it fits your idea:
  - Add a `scripts/` subdirectory with a helper script, an extra reference doc, or a config file.
  - Point to these from `SKILL.md` by absolute path (the same way it points to `reference.md`).
  - If you bundle a script, give the agent an execution tool (a shell/execute tool, or a sandbox) so it can actually run it. No execution tool -> tell `SKILL.md` to just read and reason about the script instead.

```text
# Example skill directory layout
skills/
  your-skill/
    SKILL.md
    reference.md
    scripts/
      helper.py
```

- Write the agent call and a triggering question from scratch, then confirm activation from the trace yourself.

```javascript

(function () {
  var tabs = document.querySelectorAll('.lt-tab');
  function show(p) {
    tabs.forEach(function (t) {
      var on = t.getAttribute('data-p') === p;
      t.classList.toggle('active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    document.querySelectorAll('.lt-panel').forEach(function (panel) {
      panel.classList.toggle('active', panel.id === 'p-' + p);
    });
  }
  tabs.forEach(function (t) {
    t.addEventListener('click', function () { show(t.getAttribute('data-p')); });
  });
})();

```
