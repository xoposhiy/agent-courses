# Wiring the sandbox backend

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/8eYw2UxU4gV) · [Raw file](../../raw/videos/8eYw2UxU4gV.html)

Retrieved: 2026-11-13T16:57:36.464681+00:00

[00:00] **Speaker**: This  is make_graph,  which essentially decides  which backend the agent gets, and we wrap it  in this decorator, turning it into an async context manager  Now we use yield create_deep_agent here instead of return,  and everything before the yield, resolving which backend to use, runs first as setup. Then yield hands the agent off to actually be used.

[00:23] **Speaker**: If we ever wrote code after the yield, that code would only run once the run is over as cleanup. Right now, there's nothing after it, so no cleanup happens  But the decorator leaves that slot open in case we ever need to close out the sandbox connection when a run ends. Now inside the function

[00:40] **Speaker**: It checks runtime.execution_runtime. If that's true, we're in a real run

[00:45] **Speaker**: so it  resolves a SandboxBackend for this thread. Otherwise

[00:49] **Speaker**: It just falls back to a plain state backend. And that's the introspection case. langgraph dev and Studio calling make_graph just to read the graph schema with no real thread behind it,  so there's no reason to spin up a sandbox

[01:00] **Speaker**: Now whichever backend it resolved, it gets passed straight

[01:03] **Speaker**: and to create Deep Agent here. And that's what actually gets yielded back

[01:08] **Speaker**: this whole shape,  a factory function that sets up runtime-dependent resources and hands them off, is a documented LangGraph pattern,   now here's a complication. A sandbox isn't like this Deep Agent. It's not created fresh every run. It might already exist for this thread. It might be idle and stopped, or it might have expired entirely

[01:26] **Speaker**: So MakeGraph needs to coordinate with it before it can hand back a backend.

[01:31] **Speaker**: and that coordination lives in Sandbox Backend for Thread

[01:35] **Speaker**: the first step is to look up or create the sandbox for this thread  in a background thread since it's making blocking API calls. It reuses an existing ready sandbox, wakes one that's idle, waits on one mid-transition, or creates a brand-new one

[01:51] **Speaker**: The second step is to wrap whatever Sandbox came back in a LangSmith Sandbox backend

[01:57] **Speaker**: And the third step, which only applies if this sandbox is brand new, is to seed it with skills and agents.md from local disk. A sandbox that already existed skips this since it was already seeded the first time around.

[02:08] **Speaker**: that backend comes back out of sandbox_backend_for_thread back into make_graph and straight into create_deep_agent.  That's the full wiring start to finish

[02:20] **Speaker**: Now, the one consequence of all of this is that outputs like plots and reports now live on the sandbox's file system  instead of your local disk,  the chat UI has a download button built in to pull those files out to your machine, and start.sh launches that UI locally alongside the mock mail server
