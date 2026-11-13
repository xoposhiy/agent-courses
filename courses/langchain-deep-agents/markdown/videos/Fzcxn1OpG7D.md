# Single vs Composite + Permissions

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/Fzcxn1OpG7D) · [Raw file](../../raw/videos/Fzcxn1OpG7D.html)

Retrieved: 2026-11-13T16:57:37.074947+00:00

[00:00] **Speaker**: The simplest setup  is one backend passed directly to create_deep_agent. Here it's StateBackend, the default. All file system tool calls land in thread state  Composite is for when different files have different requirements. You define path prefix routes, and anything that doesn't match falls through to the default.

[00:18] **Speaker**: Here, reference goes to a local file system backend, real files on disk, while everything else stays in state backend. The agent never sees the routing. It just calls read file and the backend handles the rest

[00:32] **Speaker**: In code, the single backend case is one argument, backend equals StateBackend. If you want local disk instead

[00:39] **Speaker**: Swap it for file system backend. Same interface, but different storage

[00:46] **Speaker**: CompositeBackend takes a default and a routes dictionary. That's the entire routing configuration  One route sends reference to a file system backend pointed at a local directory. Everything else falls back to state backend.

[01:00] **Speaker**: permissions are a separate layer enforced in code. The model cannot bypass them

[01:05] **Speaker**: Pass a list of file system permission rules  to create Deep Agent.  And the rules are evaluated in order of the first match winning.  If nothing matches, the operation is allowed.  And each rule has three fields

[01:17] **Speaker**: Operations,  read or write,  paths,  which are glob patterns,  and mode,  allow,  deny,  or interrupt  Interrupt is the same human-in-the-loop pattern  instead of silently blocking, it pauses and surfaces the pending action for human approval

[01:34] **Speaker**: So here the rule denies all rights

[01:38] **Speaker**: to reference

[01:40] **Speaker**: So the agent can read the reference files, but any attempt to write is blocked but other paths still hit the default state backend route unaffected
