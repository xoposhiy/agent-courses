# Official course repository: Python, TypeScript, lesson sources, and agent UI: thinkific/src/m1/images/m1.6-mcp-slides-1.html

[Course index](../../../../../../../README.md) · [Original source](https://github.com/langchain-ai/lca-deepagents/blob/HEAD/thinkific/src/m1/images/m1.6-mcp-slides-1.html) · [Raw file](../../../../../../../raw/repositories/lca-deepagents/thinkific/src/m1/images/m1.6-mcp-slides-1.html)

Retrieved: 2026-11-13T16:50:31.645872+00:00

<a id="stage"></a>


<a id="slides"></a>


<a id="s3fa"></a>

MCP: one standard interface
any MCP-aware client connects to any MCP server


Your Agent
LangChain / deepagents


MCP Server
standard protocol
run by anyone, anywhere

no custom code in your agent


Service
Gmail, GitHub,
LangChain Docs…

The MCP server handles the service-specific details.
Your agent only speaks the MCP protocol.

What an MCP server exposes
this course focuses on tools


MCP Server


Tools
functions the agent can call: search, read, write, query


Resources
structured data the server exposes: files, records, configs


Prompts
reusable prompt templates the server provides

This course uses tools. Resources and prompts are part of the MCP spec
but require separate client calls and are not covered here.

<a id="s5a"></a>

MCP tools are just BaseTool objects
the agent cannot tell them apart from locally-defined tools


MCP Server

list\_emails

read\_email

search\_emails


langchain-mcp-
adapters
wraps as BaseTool


Agent's tool list
source is invisible

web\_search
local

list\_emails
MCP

read\_email
MCP

Tool results come back as ToolMessages in the conversation history.
The model decides what to do next exactly as it would with any other tool.

<a id="tag"></a>
**Click → to begin**
<a id="cap"></a>
Step through the MCP overview one diagram at a time. Click the diagram or use the arrows to advance. The three diagrams cover the standard interface, what servers expose, and how tools reach your agent.

<a id="prev"></a>
←
<a id="next"></a>
→

<a id="dots"></a>

```javascript

(function () {
  var STEPS = [
    { tag: 'MCP: one standard interface',
      cap: 'MCP replaces the one-integration-per-service pattern with a single standard protocol. Any MCP-aware client connects to any MCP server; the MCP server handles all service-specific details.' },
    { tag: 'What an MCP server exposes',
      cap: 'Servers can expose three primitives: tools (callable functions), resources (structured data to read), and prompts (reusable prompt templates). This course focuses on tools; get_tools() retrieves them as BaseTool objects ready to pass to your agent. Resources and prompts require separate client calls.' },
    { tag: 'MCP tools as BaseTool objects',
      cap: 'langchain-mcp-adapters wraps each server tool as a standard BaseTool. The agent sees MCP tools identically to locally-defined tools; results come back as ToolMessages in the conversation history.' }
  ];

  var slides = document.querySelectorAll('#slides .slide');
  var dotsEl = document.getElementById('dots');
  var tagEl  = document.getElementById('tag');
  var capEl  = document.getElementById('cap');
  var prevBtn = document.getElementById('prev');
  var nextBtn = document.getElementById('next');
  var stage  = document.getElementById('stage');
  var cur = 0;

  slides.forEach(function (_, i) {
    var d = document.createElement('div');
    d.className = 'sd-dot' + (i === 0 ? ' active' : '');
    d.addEventListener('click', function () { goTo(i); });
    dotsEl.appendChild(d);
  });

  function goTo(n) {
    if (n < 0 || n >= slides.length) return;
    slides[cur].classList.remove('active');
    dotsEl.children[cur].classList.remove('active');
    cur = n;
    slides[cur].classList.add('active');
    dotsEl.children[cur].classList.add('active');
    tagEl.textContent = STEPS[cur].tag;
    capEl.textContent = STEPS[cur].cap;
    prevBtn.disabled = cur === 0;
    nextBtn.disabled = cur === slides.length - 1;
  }

  stage.addEventListener('click', function () {
    if (cur < slides.length - 1) goTo(cur + 1);
  });

  prevBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    if (cur > 0) goTo(cur - 1);
  });

  nextBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    if (cur < slides.length - 1) goTo(cur + 1);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight') { if (cur < slides.length - 1) goTo(cur + 1); }
    if (e.key === 'ArrowLeft')  { if (cur > 0) goTo(cur - 1); }
  });
})();

```
