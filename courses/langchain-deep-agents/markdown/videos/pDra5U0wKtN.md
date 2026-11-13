# Progressive Disclosure

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/pDra5U0wKtN) · [Raw file](../../raw/videos/pDra5U0wKtN.html)

Retrieved: 2026-11-13T16:57:39.281300+00:00

[00:01] **jess**: Skills use a three-stage pattern to keep the agent's context lean.

[00:05] **Speaker**: The first stage is discovery.  At startup, the SDK reads the name  and description   from each skill's frontmatter and automatically injects them into the system prompt on every call  You don't write this section. The SDK generates it, and this is roughly what it looks like

[00:22] **Speaker**: Both skills are listed

[00:25] **Speaker**: with their descriptions  and the path to their skillmd

[00:30] **Speaker**: That's all that's in context at this point. Just the names and descriptions, nothing from the skill bodies.

[00:37] **Speaker**: The second stage is activation. When a user's request matches a skill's description, the agent calls  readfile on the path shown in the system prompt loading the full skill MD into context for that turn

[00:49] **Speaker**: This is the moment the instructions actually arrive.   Next, we have execution

[00:54] **Speaker**: The agent follows the instructions in the skill body, calling whatever tools it needs

[00:59] **Speaker**: But skills go further than static text. An agent can write and edit its own skill files over time, refining them from the preferences and patterns it learns on the job.

[01:08] **Speaker**: Skills can also include executable scripts in a scripts subdirectory, which the agent can then run in a sandbox, enabling more advanced workflows like code generation, data processing, or multi-step automation You should head on over to the lab to see how the skills are wired up and watch both activation stages play out in LangSmith
