# Skills

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/0DoYTlG67pf) · [Raw file](../../raw/videos/0DoYTlG67pf.html)

Retrieved: 2026-11-13T16:57:36.246128+00:00

[00:01] **jess**: A skill is a directory containing a skill.md file.  Skills follow an open standard, which means they're portable across agents and shareable across teams.

[00:10] **Speaker**: the directory structure is simple. Under your skills folder, each skill gets its own name subdirectory. Inside that, skill.md is the only required file. It's highlighted here in yellow. Everything else is optional. A scripts folder for executable code, references for documentation, assets for template or resources. Importantly, the agent can't see any of these optional files unless the skill body explicitly mentions them This slide shows two skills side by side  Notice what's shown underneath each skill MD, just the name and description. These two fields are always injected into the system prompt on every call.

[00:50] **Speaker**: The full body, the steps, output format, everything else is only loaded when the agent activates the skill by calling read file

[01:00] **Speaker**: and this is what it looks like inside the file.

[01:02] **Speaker**: The top block here in yellow is the YAML front matter, always in context and always compact. Below it are the markdown instructions, the actual behavior, like the BANT framework here as an example. This stays out of context until activation

[01:17] **Speaker**: So the front matter is always present but compact, and the instructions are only loaded when needed. That's the core of how Skills stay lightweight

[01:27] **Speaker**: there are only two required frontmatter fields,  name  and description.  The name must be lowercase with hyphens and must match the directory name

[01:36] **Speaker**: the description is brief and describes when to use the skill

[01:40] **Speaker**: The rest of the fields are optional
