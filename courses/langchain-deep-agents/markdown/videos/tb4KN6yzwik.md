# Building A Subagent Team

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/tb4KN6yzwik) · [Raw file](../../raw/videos/tb4KN6yzwik.html)

Retrieved: 2026-11-13T16:57:39.510236+00:00

[00:01] **Speaker**: In the last lesson, you learned what delegation is and why it's useful. In this one  you'll see it built

[00:07] **Speaker**: An editorial agent that puts out a weekly music newsletter. The main agent is the editor. It knows the distributor's top four genres—rock, Latin, metal, and alternative and kicks off a research sub-agent for each one all at once. Each researcher goes off, searches for what's new in its genre, and hands back a short, polished segment.

[00:28] **Speaker**: The editor collects those four segments, assembles them into one newsletter, and renders it as a styled HTML page

[00:36] **Speaker**: This flow box summarizes the six steps.  First,  the user asks for this week's newsletter.  Then the editor calls the task tool once per genre  Then the researcher searches the web, writes raw notes, and returns one polished segment.  The editor assembles the returned segments into markdown

[00:52] **Speaker**: The editor calls the Markdown to HTML tool.  And finally, the editor writes the newsletter

[00:58] **Speaker**: Notice how there's only one kind of researcher. We don't write a separate rock subagent or a separate metal subagent because they'd all do the same thing. Instead, we define a single genre researcher type, and the editor delegates to it four times, once per genre. The genre is just the task it's handed

[01:14] **Speaker**: So a subagent is just a plain dictionary. Let's walk through each field  the name is the handle the main agent uses to call it.  The description is how the main agent knows when to pick it, the same way it decides to call any other tool  The system prompt is a subagent's own brain.

[01:30] **Speaker**: It is never inherited from the main agent, so you always need to provide one.

[01:34] **Speaker**: now tools overrides the inherited set, and here we give the researcher only internet search

[01:39] **Speaker**: Model here overrides to the cheaper Haiku 4.5 since the editor gets the stronger model,  And permissions scopes what the researcher can read and write on the file system

[01:51] **Speaker**: One subtlety, setting tools replaces the inherited set entirely. So listing only  Internet search would seem to leave the researcher unable to write files. But

[02:01] **Speaker**: the built-in file system tools

[02:04] **Speaker**: are always provided by the harness and survive the override

[02:08] **Speaker**: That's why the researcher can still save its notes even though we only listed one tool.

[02:14] **Speaker**: each researcher is assigned a scratch folder named for its genre. It saves its raw search results there and reads them back while drafting

[02:22] **Speaker**: The first rule allows the researcher to read and write under  Research

[02:27] **Speaker**: Now the second rule is a broad write deny for everything else.  So the researcher can't write outside its research area

[02:33] **Speaker**: The editor's permissions are separate and simpler. The editor's permissions are separate and simpler

[02:37] **Speaker**: There's only one rule. It denies rights to research. The editor can read the research area but cannot touch it

[02:47] **Speaker**: Permissions are first match wins. The researcher-specific allow_for_research beats the broad deny at the end

[02:56] **Speaker**: The editor is a normal deep agent. It gets the stronger model, a single custom tool,  Markdown to HTML, and the genre researcher subagent passed in

[03:07] **Speaker**: because a subagent is invoked like a tool, the editor can call the task tool four times in a single step

[03:13] **Speaker**: All four researchers run in parallel and the editor blocks until the slowest one returns, then assembles the segments.

[03:20] **Speaker**: markdown to HTML is a plain Python tool. It drops the assembled Markdown into a fixed style template and returns the full HTML page as a string

[03:28] **Speaker**: the newsletter text comes from web search, which is untrusted input, so the tool runs it through an allowlist sanitizer before inserting it into the page. That strips anything like script tags or event handlers out of the body before it goes into the HTML.

[03:44] **Speaker**: you define one subagent type, but every Deep Agent also ships with a built-in   general purpose subagent for free.  It has the same tools and model as the main agent and a generic prompt. It's the agent's escape hatch. When a task doesn't match any subagent you define, the main agent can still delegate to it to get context isolation rather than doing the work inline

[04:05] **Speaker**: It's the one subagent that also inherits the main agent's skills. You won't call it explicitly in this lab, but it's worth knowing it's always there.
