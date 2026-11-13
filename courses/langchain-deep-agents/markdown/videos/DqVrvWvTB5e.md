# Sandboxes and LocalShell

[Course index](../../README.md) · [Original source](https://share.descript.com/embed/DqVrvWvTB5e) · [Raw file](../../raw/videos/DqVrvWvTB5e.html)

Retrieved: 2026-11-13T16:57:36.638323+00:00

[00:00] **also jess**: The file system backends from the last lesson gave the agent file tools

[00:04] **Speaker**: Local shell backend and sandbox backends add one more,  execute, which runs shell commands. That's the file system surface from last lesson. This lesson is about the one tool on top of it  that lets the agent run something

[00:18] **Speaker**: the same tool set from the last lesson flows into a backend. From there, it can go to local shell backend or to a sandbox backend. Either path adds the same tool, execute. Where that command actually runs is the subject of this lesson

[00:35] **Speaker**: Shell-capable backends expose an execute command tool. The agent calls it to run scripts it has written, invoke CLI tools, and compile and test code. The combined command output, exit code, and execution metadata come back as a tool result on the next LLM call.  Now, how do you choose? There are two shell-capable backends available,  local shell backend  and sandbox backends. The deciding factor  is isolation

[01:01] **Speaker**: So with local shell backend We have one boundary here   the host,  and the agent lives inside it When it calls execute, that arrow never leaves the box.  the shell,  network,  file system, all of that is inside the same boundary as the agent. with a sandbox, the agent is inside the host

[01:23] **Speaker**: But this time, execute crosses a boundary into a second box,  the sandbox. We have the same resources, but now on the other side of the line from the agent

[01:33] **Speaker**: Agent-generated code and packages the agent may load are untrusted by nature. You'll want to use a sandbox to isolate that code from your infrastructure

[01:42] **Speaker**: But you'll want to use Local Shell Backend when building a local tool where the agent working directly on your machine is the point, such as a coding assistant or desktop agent. It's not appropriate for production or untrusted input, though.

[01:54] **Speaker**: a sandbox is a temporary isolated workspace containing a file system, command execution environment, and other resources. Sandbox backends run commands inside that workspace instead of on your host machine.  And there are two models for using a sandbox with an agent.

[02:08] **Speaker**: There's agent in sandbox versus sandbox as a tool.

[02:12] **Speaker**: With agent in sandbox, this whole box is the sandbox, and the agent itself runs in here, model calls and all For sandbox as a tool, it's a different setup. The agent stays outside on its own, and it reaches in through execute into the sandbox.   So with agent in sandbox, the LLM API keys live inside the sandbox. To update the agent, you must rebuild the sandbox image. It's useful when you want the execution environment to mirror your production infrastructure.

[02:43] **Speaker**: As for Sandbox as a tool, the LLM API keys stay on your host. Agent code is easy to update, and Sandbox failures don't affect agent state. This is the model used in the course

[02:55] **Speaker**: Sandbox as a tool keeps the LLM API key safely on the host away from untrusted code execution within the sandbox. But what about other keys? An agent may need to access resources on behalf of the user to accomplish tasks. A feature in LangSmith sandboxes allows these keys to be applied to requests without passing them into the insecure sandbox environment.

[03:15] **Speaker**: This diagram goes into it in more detail

[03:17] **Speaker**: So the first step is isolation from the host. Here we see the same host

[03:22] **Speaker**: and sandbox boundary  as before. The agent and the host spawn sandbox code away from the host to isolate code execution within the sandbox  The external API box is whatever third-party service the code is trying to reach, such as Stripe or GitHub   A request has no credentials to send, and putting an API key inside the sandbox so it could send one would expose that key to the agent's own generated code, and we don't want that So LangSmith Sandboxes adds an auth proxy sidecar inside the sandbox boundary It's a separate process from the code, and for now, it holds no secret

[04:03] **Speaker**: So now instead of calling the external API directly, the sandbox code sends its request to the local proxy

[04:11] **Speaker**: And separately, the proxy is provisioned with the real credential from Workspace Secrets injected over. And the secret now lives in the proxy, still inside the sandbox boundary

[04:23] **Speaker**: but in a separate process from the code

[04:28] **Speaker**: the Auth Proxy then attaches the credential and forwards an authenticated request to the external API So isolation keeps the code  away from the host

[04:40] **Speaker**: But the auth proxy keeps the secret away from the code. The auth proxy pattern seen here is specific to LangSmith sandboxes, not sandboxes in general.  The proxy sidecar holds the secrets inside the sandbox, but the code the agent writes and runs never sees them, so the code cannot exfiltrate them

[04:59] **Speaker**: Here's an example of a LangSmith sandbox being configured as a backend.

[05:03] **Speaker**: LangSmith Sandbox is the Deep Agent's backend. Sandbox client talks to the LangSmith Sandbox's API

[05:09] **Speaker**: This is the real network call that provisions the sandbox

[05:13] **Speaker**: And this wraps it into a backend.

[05:15] **Speaker**: the same backend parameter every other backend in this course has used.  Now, the try finally block ensures the sandbox is deleted even if the agent raises. Sandboxes are build resources, so you always want to clean them up

[05:28] **Speaker**: create sandbox provisions a fresh sandbox workspace. Files persist within that sandbox until it is deleted. So a newly created sandbox starts empty unless you upload files first

[05:40] **Speaker**: Local shell backend runs commands directly on the host machine. It can scope file system tools to a root directory, but execute itself runs with host permissions. No process isolation is applied.

[05:51] **Speaker**: and you'll assign virtual mode to true when you want file system tools to be path scoped under root directory. Either way, root directory does not restrict the execute tool.

[06:00] **Speaker**: Shell commands run with host permissions and can access paths outside the file system tool root. That's why local shell backend is unsuitable for production or untrusted input.

[06:10] **Speaker**: Root directory only scopes the file system tools. Execute runs with no path restrictions at all. A command like cat, or password works no matter what the root directory is set to

[06:21] **Speaker**: So be careful

[06:23] **Speaker**: Appropriate use cases  are for local development CLIs  or personal development environments where you trust the agent's code

[06:30] **Speaker**: and CI/CD pipelines with proper secret management

[06:33] **Speaker**: But it's not appropriate  for production environments   or processing untrusted user input or executing untrusted code

[06:40] **Speaker**: The top recommended safeguard is human-in-the-loop approval before anything runs.
