# Homework 2 bundle: figures/aos_loop.svg

[Course index](../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=figures/aos_loop.svg) · [Raw file](../../../../raw/assignments/assignment2-course-bundle/figures/aos_loop.svg)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1060 300" width="1060" height="300" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="#1A1E1C">
  <rect width="1060" height="300" fill="#FFFFFF"/>
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1A1E1C"/></marker>
    <marker id="ah-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0E7069"/></marker>
    <marker id="ah-ochre" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#8C5A00"/></marker>
  </defs>
  <text x="20" y="128" font-family="Menlo, monospace" font-size="12">goal</text>
  <line x1="58" y1="124" x2="106" y2="124" stroke="#1A1E1C" stroke-width="1.5" marker-end="url(#ah)"/>

  <rect x="110" y="88" width="190" height="72" rx="6" fill="#D7ECE8" stroke="#0E7069" stroke-width="1.5"/>
  <text x="205" y="114" text-anchor="middle" font-weight="600">1. Planner decides</text>
  <text x="205" y="134" text-anchor="middle" font-size="11.5" fill="#5C665F">an LLM call in JSON mode</text>
  <text x="205" y="150" text-anchor="middle" font-size="11.5" fill="#5C665F">goal + workers + files + history</text>

  <line x1="300" y1="124" x2="378" y2="124" stroke="#0E7069" stroke-width="1.5" marker-end="url(#ah-teal)"/>
  <text x="340" y="110" text-anchor="middle" font-size="11" fill="#5C665F">worker, instructions,</text>
  <text x="340" y="148" text-anchor="middle" font-size="11" fill="#5C665F">inputs, output_dir</text>

  <rect x="382" y="88" width="190" height="72" rx="6" fill="#FFFFFF" stroke="#1A1E1C" stroke-width="1.5"/>
  <text x="477" y="114" text-anchor="middle" font-weight="600">2. Worker runs</text>
  <text x="477" y="134" text-anchor="middle" font-size="11.5" fill="#5C665F">coding agent, SLIDERS, DataSTORM,</text>
  <text x="477" y="150" text-anchor="middle" font-size="11.5" fill="#5C665F">or one you write: reads and writes files</text>

  <line x1="572" y1="124" x2="650" y2="124" stroke="#1A1E1C" stroke-width="1.5" marker-end="url(#ah)"/>
  <text x="611" y="110" text-anchor="middle" font-size="11" fill="#5C665F">diff of the folder:</text>
  <text x="611" y="148" text-anchor="middle" font-size="11" fill="#5C665F">new / changed files</text>

  <rect x="654" y="88" width="190" height="72" rx="6" fill="#FFFFFF" stroke="#1A1E1C" stroke-width="1.5"/>
  <text x="749" y="114" text-anchor="middle" font-weight="600">3. AOS catalogs outputs</text>
  <text x="749" y="134" text-anchor="middle" font-size="11.5" fill="#5C665F">one summary per file (LLM) and a row:</text>
  <text x="749" y="150" text-anchor="middle" font-size="11.5" fill="#5C665F">who made it, in which step, from what</text>

  <line x1="844" y1="124" x2="900" y2="124" stroke="#8C5A00" stroke-width="1.5" marker-end="url(#ah-ochre)"/>

  <rect x="904" y="88" width="136" height="72" rx="6" fill="#F3E6C9" stroke="#8C5A00" stroke-width="1.5"/>
  <text x="972" y="114" text-anchor="middle" font-weight="600">4. git commit</text>
  <text x="972" y="134" text-anchor="middle" font-size="11" fill="#5C665F" font-family="Menlo, monospace">task-004 step 1:</text>
  <text x="972" y="150" text-anchor="middle" font-size="11" fill="#5C665F" font-family="Menlo, monospace">sliders (ok) - ...</text>

  <path d="M972 160 V220 H205 V164" fill="none" stroke="#1A1E1C" stroke-width="1.5" stroke-dasharray="4 4" marker-end="url(#ah)"/>
  <text x="588" y="238" text-anchor="middle" font-size="11.5" fill="#5C665F">the step is recorded in tasks/task-NNN/task.json; the planner sees the new files and the step's summary or error; repeat</text>

  <line x1="205" y1="88" x2="205" y2="46" stroke="#0E7069" stroke-width="1.5" marker-end="url(#ah-teal)"/>
  <text x="214" y="44" font-size="11.5" fill="#5C665F">"done": the task ends. Three invalid replies in a row: the task fails.</text>
  <line x1="60" y1="270" x2="1000" y2="270" stroke="#D3D9D2" stroke-width="1"/>
  <text x="530" y="290" text-anchor="middle" font-size="11.5" fill="#5C665F">the loop also stops before a step at the step limit (12 by default) or when the estimated spend reaches the workspace's budget cap</text>
</svg>

```
