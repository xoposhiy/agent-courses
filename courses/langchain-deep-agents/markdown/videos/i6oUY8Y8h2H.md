# Filesystem Backends

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/i6oUY8Y8h2H) · [Raw file](../../raw/videos/i6oUY8Y8h2H.html)

Retrieved: 2026-11-13T16:57:38.660813+00:00

[00:01] **Speaker**: the agent always sees the same file system tools,  and the file system backend decides where those files are actually stored  So every tool call flows through a backend node. The backend is the pluggable piece. Swap it, and you change where files live without changing the agent.  State is the default. Files live in the agent's in-memory state, scoped to the current thread.

[00:21] **Speaker**: Zero configuration and nothing persists, which is really good for scratch work. Now Filesystem writes to local disk,  scoped to a root directory you specify. Use it when the agent should work with real files in a local directory.  Now custom lets you implement the backend interface yourself for any storage not covered by the built-ins. S3, GitHub, anything you can write an adapter for. And the key idea is that the agent code never changes. The backend is what makes the execution environment configurable.
