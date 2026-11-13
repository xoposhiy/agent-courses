# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m1/m1.2-running-a-deep-agent.md

[Course index](../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m1/m1.2-running-a-deep-agent.md) · [Raw file](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m1/m1.2-running-a-deep-agent.md)

Retrieved: 2026-11-13T16:50:31.645872+00:00

[For translation, open lesson in new tab and use Chrome translate](../../../../../lessons/m1.2-running-a-deep-agent.md)

Python TypeScript

<a id="running-a-deep-agent"></a>


# Running a Deep Agent

<a id="your-first-deep-agent"></a>


## Your First Deep Agent

What is an Agent Harness

[What is an Agent Harness](https://www.youtube.com/embed/R0ckdFjUF5U)

Deep Agents is a harness for developers who want to build their own agent. It comes with built-in pieces like a filesystem, subagents, skills, and memory, and each one is yours to configure. You choose the model, the tools, what the agent can read or write, which actions need human approval, and where it runs. This course walks through each of those choices, so you can shape an agent around your own product.

Lesson Video Walkthrough

[Public video walkthrough](../../../../../videos/Qrr9oLMWEmo.md)

The point of this lesson is to get one minimal deep agent running before we start customizing it. By the end, you should know the smallest useful call to `create_deep_agent(...)`, where the shared course model comes from, and what a successful agent invocation returns.

Open `python/m1/m1.2_scratch_agent.py`:

```text
from deepagents import create_deep_agent

from models import model

agent = create_deep_agent(model=model)

result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})

print(result["messages"][-1].text)
```

The point of this lesson is to get one minimal deep agent running before we start customizing it. By the end, you should know the smallest useful call to `createDeepAgent(...)`, where the shared course model comes from, and what a successful agent invocation returns.

Open `typescript/m1/m1.2_scratch_agent.ts`:

```text
import { createDeepAgent } from "deepagents";

import { model } from "../models.js";

const agent = createDeepAgent({ model });

const result = await agent.invoke({
    messages: [{ role: "user", content: "What is an LLM?" }]
});

console.log(result.messages.at(-1)?.text);
```

This is the smallest version of the agent we will build on throughout the course: a model wrapped by the Deep Agents harness, invoked with a normal chat message, and read from the final returned message.

`.text` returns that message as a plain string. Read `.content` instead when you want the raw blocks behind it, which is where a model’s reasoning shows up if you switch to one that returns thinking blocks.

Run it:

```text
cd python
uv run ./m1/m1.2_scratch_agent.py
```

```text
cd typescript
pnpm tsx ./m1/m1.2_scratch_agent.ts
```

**Code output:**

```plaintext
An LLM (Large Language Model) is a type of artificial intelligence system
trained on vast amounts of text data to understand and generate human language.

Key characteristics:
- Scale: Contains billions to hundreds of billions of parameters
- Training: Trained using deep learning on huge text corpora from the internet,
  books, and other sources
- Capability: Can perform a wide range of language tasks: answering questions,
  summarizing, translating, writing, coding, reasoning, and more
- Architecture: Built on transformer architecture, which uses attention
  mechanisms to understand relationships between words across long passages
- Generative: Produces text by predicting the next token one at a time,
  based on context

Examples: GPT-4, Claude, Gemini, LLaMA, Mistral

```

**Troubleshooting**

- **`ModuleNotFoundError: No module named ‘…’`**: you ran the script with `python3` directly. Use `uv run` instead; it activates the project’s virtual environment where all dependencies live.
- **`error: Failed to spawn`** / **`Project directory does not exist`**: you’re in the wrong directory. Run the command from the `lca-deepagents` repo root.

**Troubleshooting**

- **`Cannot find module ‘deepagents’`**: dependencies aren’t installed. Run `pnpm install` from the `typescript` directory.
- **`ENOENT`** / **`no such file or directory`**: you’re in the wrong directory. Run the command from the `lca-deepagents/typescript` directory.
- **`Cannot find module ‘../models.js’`**: relative imports need the `.js` extension even though the source file is `models.ts`. This is how TypeScript’s ESM output resolves at runtime.
- **`Unknown file extension “.ts”`** / **`ERR_UNKNOWN_FILE_EXTENSION`**: you ran the file with plain `node` instead of `pnpm tsx`, which this course’s scripts are set up to use.

↓ click to celebrate ↓

<a id="celebrate-btn"></a>
![](../../../../../../raw/repositories/lca-deepagents/thinkific/src/m1/images/langchain-symbol.png) I ran my first deep agent!

<a id="fireworks-canvas"></a>

<a id="celebration-msg"></a>


```text
<img src="images/langchain-symbol.png" style="width:56px;height:56px;margin-bottom:0.75rem;filter:brightness(0)">
<div style="font-size:1.5rem;font-weight:700;margin-bottom:0.4rem;">Your first deep agent is live!</div>
<div style="font-size:0.95rem;opacity:0.85;">Welcome to the world of agentic AI.</div>
```

```javascript

(function () {
  var canvas, ctx, particles = [], running = false, animId;

  var COLORS = [
    '#006DDD','#3399FF','#7FC8FF','#CCE9FF',
    '#0E9F6E','#34D399','#99F6E4',
    '#ffffff','#B8D4FF','#60B0FF'
  ];

  function Particle(x, y) {
    var angle = Math.random() * Math.PI * 2;
    var speed = 2 + Math.random() * 7;
    this.x = x; this.y = y;
    this.vx = Math.cos(angle) * speed;
    this.vy = Math.sin(angle) * speed - 3;
    this.alpha = 1;
    this.decay = 0.012 + Math.random() * 0.018;
    this.radius = 2 + Math.random() * 4;
    this.color = COLORS[Math.floor(Math.random() * COLORS.length)];
    this.trail = [];
    this.shape = Math.random() < 0.3 ? 'star' : 'circle';
  }

  Particle.prototype.update = function () {
    this.trail.push({x: this.x, y: this.y});
    if (this.trail.length > 7) this.trail.shift();
    this.vy += 0.12;
    this.vx *= 0.99;
    this.x += this.vx; this.y += this.vy;
    this.alpha -= this.decay;
  };

  Particle.prototype.draw = function (ctx) {
    ctx.save();
    for (var i = 0; i < this.trail.length; i++) {
      var t = this.trail[i];
      var a = (i / this.trail.length) * this.alpha * 0.4;
      ctx.globalAlpha = a;
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(t.x, t.y, this.radius * 0.5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = this.alpha;
    ctx.fillStyle = this.color;
    if (this.shape === 'star') {
      drawStar(ctx, this.x, this.y, 5, this.radius * 1.4, this.radius * 0.6);
    } else {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  };

  function drawStar(ctx, cx, cy, spikes, outer, inner) {
    var rot = (Math.PI / 2) * 3, step = Math.PI / spikes;
    ctx.beginPath();
    ctx.moveTo(cx, cy - outer);
    for (var i = 0; i < spikes; i++) {
      ctx.lineTo(cx + Math.cos(rot) * outer, cy + Math.sin(rot) * outer); rot += step;
      ctx.lineTo(cx + Math.cos(rot) * inner, cy + Math.sin(rot) * inner); rot += step;
    }
    ctx.lineTo(cx, cy - outer);
    ctx.closePath();
    ctx.fill();
  }

  function burst(x, y, count) {
    for (var i = 0; i < count; i++) particles.push(new Particle(x, y));
  }

  function randomBurst() {
    var x = 0.1 * window.innerWidth + Math.random() * 0.8 * window.innerWidth;
    var y = 0.1 * window.innerHeight + Math.random() * 0.55 * window.innerHeight;
    burst(x, y, 60 + Math.floor(Math.random() * 50));
  }

  function loop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles = particles.filter(function (p) { return p.alpha > 0; });
    particles.forEach(function (p) { p.update(); p.draw(ctx); });
    if (running || particles.length > 0) animId = requestAnimationFrame(loop);
    else { canvas.style.display = 'none'; }
  }

  window.launchCelebration = function () {
    if (!canvas) {
      canvas = document.getElementById('fireworks-canvas');
      ctx = canvas.getContext('2d');
    }
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    canvas.style.display = 'block';

    var msg = document.getElementById('celebration-msg');
    msg.style.display = 'block';
    msg.style.animation = 'none';
    msg.style.opacity = '1';
    setTimeout(function () {
      msg.style.transition = 'opacity 1s';
      msg.style.opacity = '0';
      setTimeout(function () { msg.style.display = 'none'; }, 1000);
    }, 3200);

    var btn = document.getElementById('celebrate-btn');
    btn.textContent = 'Again!';

    particles = [];
    running = true;

    var shots = 0, maxShots = 22;
    function fire() {
      if (shots >= maxShots) { running = false; return; }
      var count = Math.floor(Math.random() * 3) + 1;
      for (var i = 0; i < count; i++) randomBurst();
      shots += count;
      setTimeout(fire, 120 + Math.random() * 280);
    }

    if (animId) cancelAnimationFrame(animId);
    fire();
    loop();
  };
})();

```

<a id="recap"></a>


## Recap

- `create_deep_agent(model=model)` is the smallest useful deep agent: a model wrapped in the Deep Agents harness.
- The model comes from the shared `models.py`, so every lab uses the same one and you swap it in one place.
- You invoke the agent with a normal chat message, and the reply is the last message in `result["messages"]`.
- `.text` gives that reply as a plain string; `.content` gives the raw blocks, including thinking blocks if the model returns them.

- `createDeepAgent({ model })` is the smallest useful deep agent: a model wrapped in the Deep Agents harness.
- The model comes from the shared `models.ts`, so every lab uses the same one and you swap it in one place.
- You invoke the agent with a normal chat message, and the reply is the last message in `result.messages`.
- `.text` gives that reply as a plain string; `.content` gives the raw blocks, including thinking blocks if the model returns them.

---

<a id="references"></a>


## References

**Documentation:**

- [Deep Agents overview](../../../../../readings/docs-langchain-com-oss-python-deepagents-overview-6f3fda49.md)
- [Models (Deep Agents)](../../../../../readings/docs-langchain-com-oss-python-deepagents-models-d81a8a13.md)
- [deepagents README (GitHub)](../../../../../readings/github-191947403d65.md)

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`graph.py`](../../../../../readings/github-b61dcb5a328d.md): `create_deep_agent`: builds the agent and its default middleware stack

**Go deeper: read the source** *(optional)*

*The lesson shows how to use this. To see how it’s implemented, start with these files:*

- [`agent.ts`](../../../../../readings/github-8221cd675654.md): `createDeepAgent`: builds the agent and its default middleware stack
