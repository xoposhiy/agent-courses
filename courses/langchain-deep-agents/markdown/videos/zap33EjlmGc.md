# Newsletter Agent Lab

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/zap33EjlmGc) · [Raw file](../../raw/videos/zap33EjlmGc.html)

Retrieved: 2026-11-13T16:57:39.993374+00:00

[00:00] **Speaker**: This lab has two files. This one defines the agents and the other one runs them. Let's start here. So the setup is an editor that delegates to four researchers running in parallel, one per genre: and there's only one researcher type. The genre is just the task it's handed   Top genres is the hardcoded list of genres the editor will cover. The editor system prompt is built from this list at module load time

[00:29] **Speaker**: This is the researcher's only external tool. It wraps the Tavily search API, and the researchers use this while the editor doesn't.  We'll see how that's enforced in a moment   This is the editor's only custom tool, pure Python. It takes the assembled Markdown newsletter, converts it to HTML with a styled template, sanitizes it with nh3 to strip anything dangerous that came in from web search results, and returns the full HTML string.

[00:53] **Speaker**: The editor calls this at the end before writing the final file

[00:58] **Speaker**: This is the researcher system prompt. There are three steps  search the web for recent developments in the genre

[01:04] **Speaker**: Save the complete raw search output to

[01:07] **Speaker**: This  Then write one polished word segment. The key instruction is in step two

[01:13] **Speaker**: to paste the results verbatim. That raw material stays in the file and never goes back to the editor

[01:20] **Speaker**: There are two permission rules for the researchers

[01:23] **Speaker**: The first rule allows reads and writes under research

[01:26] **Speaker**: And the second rule denies all writes everywhere else.  Rules are evaluated in order, and first match wins. So a researcher trying to write  to research

[01:36] **Speaker**: hits the first rule  and is allowed. A researcher trying to write anything outside of research  hits the second rule,  and is blocked. This is how you scope a subagent to its scratch space without any prompt engineering

[01:49] **Speaker**: This is the subagent definition. There are five fields

[01:53] **Speaker**: Name is the handle the editor uses to call it via the task tool

[01:57] **Speaker**: Description is how the editor decides when to delegate to it

[02:00] **Speaker**: The system prompt is the researcher's own brain, and it's never inherited from the editor

[02:05] **Speaker**: And tools replaces the inherited tool set with just internet search.

[02:08] **Speaker**: Permissions replaces the inherited permissions with the scoped rules that we just saw earlier. One thing to note about tools, replacing the inherited set  With internet search Might look like it removes file system tools too, but it doesn't. The built-in file system tools are always provided by the harness and survive the override. That's why the researcher can still write its notes

[02:30] **Speaker**: The editor's permission rule is much simpler

[02:33] **Speaker**: Deny writes  to research. The editor can read the research area but cannot write into it. Everything else is allowed by default

[02:42] **Speaker**: The editor here

[02:43] **Speaker**: gets the stronger model

[02:46] **Speaker**: which is Sonnet.

[02:47] **Speaker**: Previously, we were using Haiku unless you changed it  But our editor will default to this. You can also change it though

[02:55] **Speaker**: So our editor gets the stronger model,  the Markdown to HTML tool

[02:59] **Speaker**: Its system prompt,  the genre researcher subagent,  and the editor permissions.

[03:05] **Speaker**: Now, this file runs the agent and handles getting the files off of AgentState and onto disk

[03:11] **Speaker**: Here's a single invoke with one message

[03:14] **Speaker**: put together this week's newsletter   we set the recursion limit to 50 to give the agent enough headroom to run four researchers in parallel plus assembly steps.    After invoke, we pull the files

[03:25] **Speaker**: Out of here. This is the state-backed file system. The agent ran on state-backed by default, so every writefile call landed in AgentState, not on your disk. We check that the newsletter was actually produced before proceeding

[03:39] **Speaker**: This loop mirrors the state back files to disk. For each file path the agent wrote, we map it into Python, M4, and output and write it there. There are two things to notice

[03:50] **Speaker**: First, paths that start  with output

[03:54] **Speaker**: gets stripped to just the filename

[03:57] **Speaker**: Paths that start with research keep their folder structure So the newsletter goes to output/newsletter.html, and the research notes go to output/research/Rock/sources.md, and so on.   Next, the path traversal line These file paths come from the agent which ran on web search content. before writing anything, we verify the resolve destination stays inside out directory

[04:23] **Speaker**: Any of these tricks get caught here and skipped

[04:28] **Speaker**: After writing, it prints the path to open the newsletter in a browser

[04:37] **Speaker**: Amazing. I've sped up this video, so it doesn't look like it took a lot of time, but when you're doing it, don't worry if it takes a while. The editor is firing off four researchers in parallel and each running several Tavily searches, so it's totally normal.

[04:50] **Speaker**: Anyways,  now we have our newsletter

[04:54] **Speaker**: Let's look at our newsletter

[05:00] **Speaker**: So here we have our four genre sections

[05:04] **Speaker**: with specific artists and releases, and all ready to read. This came entirely from four parallel researchers coordinated by a single editor

[05:15] **Speaker**: Let's open one of the sources.md files

[05:20] **Speaker**: So this is what it looks like on the inside. Tens of kilobytes of raw search results, titles, URLs, full snippets, everything Tavily returned. The researcher read all of this while drafting its segment. None of it crossed back to the editor. The editor only ever saw that tiny summary. That's the context isolation doing its job

[05:43] **Speaker**: The reason the research stayed isolated is that the researcher's system prompt told it to save raw results to a file and return only the polished segment

[05:52] **Speaker**: The reason the editor couldn't accidentally pollute the research area is the editor's permission rules deny it.
