# Skills Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/XxEWKNe2z1p) · [Raw file](../../raw/videos/XxEWKNe2z1p.html)

Retrieved: 2026-11-13T16:57:38.099482+00:00

[00:00] **Speaker 6**: This lab introduces skills, which are a way to package reusable instructions that the agent loads on demand rather than carrying in context at all times.

[00:09] **Speaker**: The backend is a file system backend rooted at the m3 directory. Everything under Python and m3 is visible to the agent through its file system tools. That includes the skills directory we're about to look at

[00:21] **Speaker**: There are a few things here

[00:23] **Speaker**: Name gives the agent an identity that shows up in LangSmith. It's just easier to find your run this way

[00:28] **Speaker**: Backend is the file system that we just set up

[00:30] **Speaker**: And skills is a list of paths in the backend where skills live. This argument tells the agent where to look. That resolves to Python, then M3, then skills on disk

[00:43] **Speaker**: We have two skills here, qualify_lead and draft_pitch. Each one is a directory with a skill.md file inside. That's the entire structure, a named directory with one file.  I've already opened them here    this bit right here is front matter with two required fields.  Name  which must match the directory name exactly  and description

[01:07] **Speaker**: Which is clear and concise and is what the agent sees when it's deciding to activate the skill or not.

[01:12] **Speaker**: Below it is the full instruction body  The BANT framework

[01:17] **Speaker**: the four steps,  and output classification This entire body stays unread until the agent matches a task to this skill's description. Draft pitch has the same structure

[01:29] **Speaker**: A description that says when to use it

[01:32] **Speaker**: and a body with steps for writing a pitch. This is invisible to the agent until activation    Now the user message asks to qualify a lead.

[01:43] **Speaker**: We've given it some descriptors so that there's enough to work through the BANT framework without asking follow-up questions.

[01:51] **Speaker**: And this print will show the final response

[01:57] **Speaker**: So the agent ran through the BANT criteria and produced a classification.

[02:01] **Speaker**: The budget is confirmed at 45,000  Authority is confirmed  Our person is the decision maker

[02:10] **Speaker**: need is defined

[02:12] **Speaker**: and the timeline is concrete.

[02:14] **Speaker**: Woo-hoo! Our lead is qualified. So this output came from the skill_md body. It told the agent exactly what to extract and how to classify the result. The agent read it, followed the steps, and structured its response accordingly

[02:28] **Speaker**: When the agent saw qualify a lead in the user message, it matched qualify lead's description, read that skill MD, and followed the body. Draft pitch was never loaded. That selective loading is the whole point of skills, to keep the context lean by only loading what the current task needs.
