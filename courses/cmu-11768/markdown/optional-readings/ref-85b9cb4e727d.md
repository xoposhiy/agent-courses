# E2B sandbox persistence

[Course index](../../README.md) · [Original source](https://docs.e2b.dev/sandbox/persistence) · [Raw file](../../raw/optional-readings/ref-85b9cb4e727d.html)

Retrieved: 2026-11-13T16:57:11.810941+00:00

Sandbox

# Sandbox persistence

Copy pageCopy page

Pause a sandbox and resume it later from the exact state it was in, including the filesystem and the memory, so running processes and loaded variables survive. A paused sandbox is kept indefinitely with no automatic deletion.

Copy pageCopy page

The sandbox persistence allows you to pause your sandbox and resume it later from the same state it was in when you paused it.
This includes not only state of the sandbox’s filesystem but also the sandbox’s memory. This means all running processes, loaded variables, data, etc.
A paused sandbox is kept **indefinitely**. There is no time-to-live and no automatic deletion, and E2B never kills a paused sandbox on its own. It is removed only when you explicitly kill it. See [How long does a sandbox live?](https://docs.e2b.dev/faq/sandbox-lifetime).

## Sandbox state transitions

Understanding how sandboxes transition between different states is crucial for managing their lifecycle effectively. Here’s a diagram showing the possible state transitions:


### State descriptions

- **Running**: The sandbox is actively running and can execute code. This is the initial state after creation.
- **Paused**: The sandbox execution is suspended but its state is preserved.
- **Snapshotting**: The sandbox is briefly paused while a persistent snapshot is being created. It automatically returns to Running. See [Snapshots](https://docs.e2b.dev/sandbox/snapshots).
- **Killed**: The sandbox is terminated and all resources are released. This is a terminal state.

### Changing sandbox’s state

JavaScript & TypeScript

Python

```
import { Sandbox } from 'e2b'

const sandbox = await Sandbox.create() // Starts in Running state

// Pause the sandbox
await sandbox.pause() // Running → Paused

// Resume the sandbox
await sandbox.connect() // Running/Paused → Running

// Kill the sandbox (from any state)
await sandbox.kill() // Running/Paused → Killed
```

```
from e2b import Sandbox

sandbox = Sandbox.create()  # Starts in Running state

# Pause the sandbox
sandbox.pause()  # Running → Paused

# Resume the sandbox
sandbox.connect()  # Running/Paused → Running

# Kill the sandbox (from any state)
sandbox.kill()  # Running/Paused → Killed
```

## Pausing sandbox

When you pause a sandbox, both the sandbox’s filesystem and memory state will be saved. This includes all the files in the sandbox’s filesystem and all the running processes, loaded variables, data, etc.

JavaScript & TypeScript

Python

```
import { Sandbox } from 'e2b'

const sbx = await Sandbox.create()
console.log('Sandbox created', sbx.sandboxId)

// Pause the sandbox
// You can save the sandbox ID in your database to resume the sandbox later
await sbx.pause()
console.log('Sandbox paused', sbx.sandboxId)
```

```
from e2b import Sandbox

sbx = Sandbox.create()
print('Sandbox created', sbx.sandbox_id)

# Pause the sandbox
# You can save the sandbox ID in your database to resume the sandbox later
sbx.pause()
print('Sandbox paused', sbx.sandbox_id)
```

By default a pause saves **both** the filesystem and the memory. To save only the filesystem — a lighter snapshot that reboots on resume — pass `mode: 'filesystem'` (JavaScript) / `mode="filesystem"` (Python). The older `keepMemory: false` / `keep_memory=False` form is deprecated but still works. See [Filesystem-only snapshots](https://docs.e2b.dev/sandbox/filesystem-only-snapshots).

### When a pause is refused

Rolling out. The refusal behavior below is being enabled region by region. Until it reaches your region, a pause in this situation fails with a `500` error instead. `ServiceBusyError` and `ServiceBusyException` are available in the JavaScript and Python SDKs (the `e2b` package) starting with version `2.48.0`.

A pause can be refused when the node running the sandbox is still finishing the previous snapshot of the same sandbox. Instead of failing the sandbox, the API answers with HTTP `503` and the sandbox **keeps running with its state intact**. Nothing was paused and nothing was lost. The SDKs surface this as `ServiceBusyError` (JavaScript) / `ServiceBusyException` (Python), the same error every other 503 from the API raises, for example when there is no capacity to place a new sandbox.
The right reaction is to retry the pause after a short wait, or simply to keep using the sandbox and pause it later:

JavaScript & TypeScript

Python

```
import { Sandbox, ServiceBusyError } from 'e2b'

const sbx = await Sandbox.create()

try {
  await sbx.pause()
} catch (error) {
  if (error instanceof ServiceBusyError) {
    // The sandbox is still running; try again in a few seconds
    await new Promise((resolve) => setTimeout(resolve, 5_000))
    await sbx.pause()
  } else {
    throw error
  }
}
```

```
import time
from e2b import Sandbox, ServiceBusyException

sbx = Sandbox.create()

try:
    sbx.pause()
except ServiceBusyException:
    # The sandbox is still running; try again in a few seconds
    time.sleep(5)
    sbx.pause()
```

`ServiceBusyError` / `ServiceBusyException` is not a `SandboxError` / `SandboxException`, so catch it explicitly.

### When the sandbox is not responding

Before taking a snapshot, E2B checks that `envd`, the E2B daemon inside the sandbox, answers a health check. A sandbox whose `envd` does not answer is usually hung. What the pause does next depends on what you ask for:


| Pause | `envd` does not answer |
| --- | --- |
| Default (memory and filesystem) | The pause **goes ahead** and the snapshot is marked as taken while the sandbox was not responding. The sandbox can later be resumed only by [rebooting it](https://docs.e2b.dev/sandbox/resume-without-memory). |
| With `strict: true` (JavaScript) / `strict=True` (Python) | The pause is **refused** with HTTP `503`. The sandbox keeps running, nothing is paused, and you can retry later. |
| [Filesystem-only](https://docs.e2b.dev/sandbox/filesystem-only-snapshots) (`mode: 'filesystem'`) | The pause is always **refused** with HTTP `503`, because capturing the filesystem needs `envd` to freeze it. |

[Forks](https://docs.e2b.dev/sandbox/fork) and [snapshots](https://docs.e2b.dev/sandbox/snapshots) are refused the same way as a filesystem-only pause.
The default keeps the pause from failing: you get a paused sandbox with its disk and memory saved, but you won’t be able to resume it with its memory. Pass `strict: true` (JavaScript) / `strict=True` (Python) when you would rather keep the memory and retry the pause later than end up with a sandbox that can only reboot. Like a busy node, the refusal surfaces as `ServiceBusyError` (JavaScript) / `ServiceBusyException` (Python).

JavaScript & TypeScript

Python

```
import { Sandbox, ServiceBusyError } from 'e2b'

const sbx = await Sandbox.create()

try {
  await sbx.pause({ strict: true })
} catch (error) {
  if (error instanceof ServiceBusyError) {
    // Not paused: the sandbox is still running with its memory intact
  } else {
    throw error
  }
}
```

```
from e2b import Sandbox, ServiceBusyException

sbx = Sandbox.create()

try:
    sbx.pause(strict=True)
except ServiceBusyException:
    # Not paused: the sandbox is still running with its memory intact
    pass
```

`strict` needs SDK 2.63.0 or later.
A sandbox paused while it was not responding shows `envdUnresponsiveAtPause: true` in [`GET /sandboxes/{sandboxID}`](https://docs.e2b.dev/api-reference/sandboxes/get-sandbox) and in the list of paused sandboxes. In the SDK (2.63.0 or later), `getInfo()` returns it as `envdUnresponsiveAtPause` (JavaScript) and `get_info()` as `envd_unresponsive_at_pause` (Python). The field is omitted for a running sandbox and for a snapshot taken while `envd` answered.

## Resuming sandbox

When you resume a sandbox, it will be in the same state it was in when you paused it.
This means that all the files in the sandbox’s filesystem will be restored and all the running processes, loaded variables, data, etc. will be restored.

JavaScript & TypeScript

Python

```
import { Sandbox } from 'e2b'

const sbx = await Sandbox.create()
console.log('Sandbox created', sbx.sandboxId)

// Pause the sandbox
// You can save the sandbox ID in your database to resume the sandbox later
await sbx.pause()
console.log('Sandbox paused', sbx.sandboxId)

// Connect to the sandbox (it will automatically resume the sandbox, if paused)
const sameSbx = await sbx.connect()
console.log('Connected to the sandbox', sameSbx.sandboxId)
```

```
from e2b import Sandbox

sbx = Sandbox.create()
print('Sandbox created', sbx.sandbox_id)

# Pause the sandbox
# You can save the sandbox ID in your database to resume the sandbox later
sbx.pause()
print('Sandbox paused', sbx.sandbox_id)

# Connect to the sandbox (it will automatically resume the sandbox, if paused)
same_sbx = sbx.connect()
print('Connected to the sandbox', same_sbx.sandbox_id)
```

### When a resume is refused

A sandbox that was [paused while it was not responding](ref-85b9cb4e727d.md) cannot be resumed with its memory: restoring that memory would bring the hung sandbox back. A plain `connect()` is refused with HTTP `409`, error code `sandbox_snapshot_guest_agent_unresponsive`, and this message:

```
Sandbox '<sandboxID>' cannot be resumed with its memory: its snapshot was taken while the sandbox guest agent was not responding, and resuming the memory would bring that back. Resume it without memory (memory: false) to cold-boot it from its disk
```

In SDK 2.63.0 and later this refusal raises a typed error: `GuestUnresponsiveError` in JavaScript and `GuestUnresponsiveException` in Python, both exported from `e2b`. Other `409` answers, such as a sandbox that is still being paused, do not raise it. In older SDKs the same refusal is a generic `SandboxError` (JavaScript) / `SandboxException` (Python) carrying the message above. The same refusal answers the resume endpoint and [auto-resume](https://docs.e2b.dev/sandbox/auto-resume) on traffic. Nothing is consumed: the sandbox stays paused with its snapshot intact.
To get the sandbox back, [reboot it](https://docs.e2b.dev/sandbox/resume-without-memory): catch the error and connect again with `onResume: 'reboot'` (JavaScript) / `on_resume="reboot"` (Python). It boots from its disk, so files written and flushed before the pause are there, while running processes and in-memory state are gone, and writes not flushed before the pause may be lost. This works for every team, with no enablement needed for such a sandbox.

JavaScript & TypeScript

Python

```
import { Sandbox, GuestUnresponsiveError } from 'e2b'

let sbx
try {
  sbx = await Sandbox.connect(sandboxId)
} catch (err) {
  if (err instanceof GuestUnresponsiveError) {
    sbx = await Sandbox.connect(sandboxId, { onResume: 'reboot' })
  } else {
    throw err
  }
}
```

```
from e2b import Sandbox, GuestUnresponsiveException

try:
    sbx = Sandbox.connect(sandbox_id)
except GuestUnresponsiveException:
    sbx = Sandbox.connect(sandbox_id, on_resume="reboot")
```

|  | SDK version (JavaScript and Python) |
| --- | --- |
| Reboot with `onResume: 'reboot'` / `on_resume="reboot"` | 2.48.0 or later |
| Typed `GuestUnresponsiveError` / `GuestUnresponsiveException` | 2.63.0 or later |

On an SDK between 2.48.0 and 2.62.x you can still reboot the sandbox, but you have to recognize the refusal by its message. Upgrade to 2.63.0 or later to catch it by type.
Once the rebooted sandbox is running, pause it again to record a new, healthy snapshot. If it reaches its timeout without being paused, it reverts to the snapshot you resumed from, and the next plain `connect()` is refused again (see [Keep a snapshot afterwards](https://docs.e2b.dev/sandbox/resume-without-memory#keep-a-snapshot-afterwards)).

## Listing paused sandboxes

You can list all paused sandboxes by calling the `Sandbox.list` method and supplying the `state` query parameter.
More information about using the method can be found in [List Sandboxes](https://docs.e2b.dev/sandbox/list).

JavaScript & TypeScript

Python

```
import { Sandbox, SandboxInfo } from 'e2b'

// List all paused sandboxes
const paginator = Sandbox.list({ query: { state: ['paused'] } })

// Get the first page of paused sandboxes
const sandboxes = await paginator.nextItems()

// Get all paused sandboxes
while (paginator.hasNext) {
  const items = await paginator.nextItems()
  sandboxes.push(...items)
}
```

```
# List all paused sandboxes
from e2b import Sandbox, SandboxQuery, SandboxState

paginator = Sandbox.list(SandboxQuery(state=[SandboxState.PAUSED]))

# Get the first page of paused sandboxes
sandboxes = paginator.next_items()

# Get all paused sandboxes
while paginator.has_next:
  items = paginator.next_items()
  sandboxes.extend(items)
```

## Removing paused sandboxes

You can remove paused sandboxes by calling the `kill` method on the Sandbox instance.

JavaScript & TypeScript

Python

```
import { Sandbox } from 'e2b'

const sbx = await Sandbox.create()
console.log('Sandbox created', sbx.sandboxId)

// Pause the sandbox
// You can save the sandbox ID in your database to resume the sandbox later
await sbx.pause()

// Remove the sandbox
await sbx.kill()

// Remove sandbox by id
await Sandbox.kill(sbx.sandboxId)
```

```
from e2b import Sandbox

sbx = Sandbox.create()

# Pause the sandbox
sbx.pause()

# Remove the sandbox
sbx.kill()

# Remove sandbox by id
Sandbox.kill(sbx.sandbox_id)
```

## Sandbox’s timeout

When connecting to a sandbox, the timeout is not reset. `Sandbox.connect()` only ever extends the sandbox’s lifetime - the new expiry is the later of the current expiry and now plus the timeout you pass (default 5 minutes). So a sandbox with 20 minutes left stays at 20 minutes even if you connect with the default timeout, while a sandbox with only 1 minute left is bumped up to 5. To set an exact timeout that can also shorten the remaining lifetime, use `setTimeout()` / `set_timeout()` instead.

JavaScript & TypeScript

Python

```
import { Sandbox } from 'e2b'

const sbx = await Sandbox.connect(sandboxId, { timeoutMs: 60 * 1000 }) // 60 seconds
```

```
from e2b import Sandbox

sbx = Sandbox.connect(sandbox_id, timeout=60) # 60 seconds
```

### Auto-pause

Auto-pause is configured in the sandbox lifecycle on create. `onTimeout`/`on_timeout` defaults to `"kill"`, meaning the sandbox is terminated when its timeout expires. Set it to `"pause"` to auto-pause on timeout instead.

JavaScript & TypeScript

Python

```
import { Sandbox } from 'e2b'

const sandbox = await Sandbox.create({
  timeoutMs: 10 * 60 * 1000, // Optional: change default timeout (10 minutes)
  lifecycle: {
    onTimeout: 'pause', // Defaults to 'kill'; set to 'pause' to auto-pause on timeout
    autoResume: false, // Optional (default is false)
  },
})
```

```
from e2b import Sandbox

sandbox = Sandbox.create(
    timeout=10 * 60,  # Optional: change default timeout (10 minutes)
    lifecycle={
        "on_timeout": "pause",  # Defaults to "kill"; set to "pause" to auto-pause on timeout
        "auto_resume": False,   # Optional (default is False)
    },
)
```

Auto-pause is persistent, meaning if your sandbox resumes and later times out again, it will pause again.
If the node refuses a memory auto-pause because it is still finishing the sandbox’s previous snapshot, E2B keeps the sandbox running and retries the pause for up to about two minutes past its timeout. Only if the node keeps refusing for that whole window is the sandbox paused **filesystem-only**: the disk is preserved and the next resume reboots the sandbox, so the memory state is lost. Under normal conditions this never happens. It protects your sandbox during snapshot backlogs on a node, where the alternative would be losing the sandbox entirely. This behavior is rolling out region by region together with the refusal handling above. To see whether it happened to a sandbox, check its `sandbox.lifecycle.paused` event: `pause_mode` is `filesystem` (see [lifecycle events](https://docs.e2b.dev/sandbox/lifecycle-events-webhooks#webhook-payload)).
If the sandbox is [not responding](ref-85b9cb4e727d.md) when its timeout expires, E2B keeps it running and retries the auto-pause for about two minutes, in case it recovers. If it is still not responding after that, it is paused with its memory anyway and marked, so the next resume has to [reboot it](ref-85b9cb4e727d.md).
To make the auto-pause filesystem-only — dropping memory so resume reboots the sandbox — use the object form `onTimeout: { action: 'pause', mode: 'filesystem' }` (JavaScript) / `"on_timeout": {"action": "pause", "mode": "filesystem"}` (Python). See [Filesystem-only snapshots](https://docs.e2b.dev/sandbox/filesystem-only-snapshots).
If you call `.kill()`, the sandbox is permanently deleted and cannot be resumed.
For auto-resume behavior, see [AutoResume](https://docs.e2b.dev/sandbox/auto-resume).

## Network

If you have a service (for example a server) running inside your sandbox and you pause the sandbox, the service won’t be accessible from the outside and all the clients will be disconnected.
If you resume the sandbox, the service will be accessible again but you need to connect clients again.

## Limitations

### Pause and resume performance

- Pausing a sandbox takes approximately **4 seconds per 1 GiB of RAM**
- Resuming a sandbox takes approximately **1 second**

### Paused sandbox retention

- Paused sandboxes are kept **indefinitely**; there is no automatic deletion or time-to-live limit
- There is currently **no configurable “auto-kill after N days” option**; a paused sandbox will not expire on its own
- You can resume a paused sandbox at any time
- To remove a paused sandbox, you must kill it explicitly with an API call (`sandbox.kill()` / `Sandbox.kill(sandboxId)`), as shown in [Removing paused sandboxes](ref-85b9cb4e727d.md)

### Continuous runtime limits

- A sandbox can remain running (without being paused) for:
  - **24 hours** on the **Pro tier**
  - **1 hour** on the **Hobby tier**
- After a sandbox is paused and resumed, the continuous runtime limit is **reset**

Was this page helpful?

YesNo
