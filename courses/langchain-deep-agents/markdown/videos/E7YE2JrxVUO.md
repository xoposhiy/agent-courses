# The Deep Agent Environment

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/E7YE2JrxVUO) · [Raw file](../../raw/videos/E7YE2JrxVUO.html)

Retrieved: 2026-11-13T16:57:36.763827+00:00

[00:01] **Speaker 2**: a Deep Agent runs inside an environment,  the place where it can store files, optionally run commands, and optionally execute code inside the agent loop.   Now, every Deep Agent environment has a file system  The shell  and interpreter are optional.

[00:15] **Speaker**: Now let's take a look at each one, then define the backend layer that implements them

[00:20] **Speaker**: The file system is always present. The LLM calls the same tools regardless of what's behind the back end. The agent sees the same surface even if the back end implementation changes.

[00:31] **Speaker**: A file system gives the agent a place to work, a scratchpad for notes, intermediate results, plans, and generated artifacts.

[00:39] **Speaker**: The backend detail  Where those files actually live is covered in the next section.

[00:45] **Speaker**: Now the shell adds one more tool  Execute. That's the only difference from the file system view. Execute lets the agent run commands:  scripts, tests, package commands, anything the environment supports

[00:59] **Speaker**: two common backend families provide this  Sandbox providers

[01:03] **Speaker**: which run commands in isolated environments   like containers or virtual machines

[01:08] **Speaker**: limits what code can affect compared with running directly on your machine. But safety still depends on sandbox configuration, network access,  credentials, and provider isolation.

[01:17] **Speaker**: Now local shell

[01:19] **Speaker**: runs commands directly on your machine and should only be used when that local access is actually required.  Shell execution, when available, is always provided by the backend

[01:30] **Speaker**: So the client sends a request, and the LLM produces a code block. The interpreter then evaluates it and returns the real result. The LLM then uses that to send its final response.  The interpreter is not part of the back end. It runs in the loop as its own separate tool

[01:52] **Speaker**: Now, the reason this matters  is because most agent work alternates between model reasoning and tool calls.

[01:59] **Speaker**: Each batch of tool calls is fixed the moment the LLM emits it. Nothing can loop, branch on a result  retry a failure, or feed one call's output into the next without another model turn. And every result returns to the model's context.

[02:16] **Speaker**: Interpreters give the agent a runtime for exactly that

[02:19] **Speaker**: A loop runs every iteration,  intermediate values stay in variables, and only a compact result returns to the model

[02:27] **Speaker**: now that you've seen the three capabilities, we can name the implementation layer.  The environment is what the agent sees.    file system tools, optional execute, and the optional interpreter the backend is what implements the file system,  an optional shell behind that environment  the backend answers where do the files live? Is execute available? And if execute is available, where do the commands run? The agent's tool surface stays the same while the backend changes   and the interpreter is separate. It's not part of the back end. It's added as its own capability in the agent loop
