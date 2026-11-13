# Homework 2 bundle: figures/worker.svg

[Course index](../../../../README.md) · [Original source](https://drive.google.com/file/d/1VPlTDJULw4qIkQuVcHxxPh4Q50Nvmi-z/view#archive-member=figures/worker.svg) · [Raw file](../../../../raw/assignments/assignment2-course-bundle/figures/worker.svg)

Retrieved: 2026-11-13T17:00:50.402745+00:00

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 280" width="760" height="280" font-family="Helvetica, Arial, sans-serif" font-size="12.5" fill="#1A1E1C">
  <rect width="760" height="280" fill="#FFFFFF"/>
  <defs>
    <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#1A1E1C"/></marker>
    <marker id="ah-teal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#0E7069"/></marker>
  </defs>
  <!-- what comes in -->
  <rect x="16" y="60" width="170" height="110" rx="6" fill="#FFFFFF" stroke="#1A1E1C" stroke-width="1.2"/>
  <text x="101" y="82" text-anchor="middle" font-weight="600">a Step</text>
  <text x="101" y="104" text-anchor="middle" font-family="Menlo, monospace" font-size="11.5">instructions</text>
  <text x="101" y="122" text-anchor="middle" font-family="Menlo, monospace" font-size="11.5">inputs (workspace paths)</text>
  <text x="101" y="140" text-anchor="middle" font-family="Menlo, monospace" font-size="11.5">output_dir</text>
  <text x="101" y="160" text-anchor="middle" font-size="11" fill="#5C665F">from the planner or from you</text>
  <line x1="186" y1="115" x2="236" y2="115" stroke="#1A1E1C" stroke-width="1.4" marker-end="url(#ah)"/>

  <!-- the worker -->
  <rect x="240" y="26" width="300" height="196" rx="8" fill="#F4F6F2" stroke="#1A1E1C" stroke-width="1.6"/>
  <text x="390" y="50" text-anchor="middle" font-weight="700" font-size="14">class MyWorker(Worker)</text>
  <g font-family="Menlo, monospace" font-size="11.5">
    <text x="258" y="80">name = "outcome_auditor"</text>
    <text x="258" y="100">description = "what it does, what inputs</text>
    <text x="258" y="116">    it needs, what files it writes"</text>
    <text x="258" y="144">def run(self, ws, step, log):</text>
    <text x="258" y="162">    ... read inputs, call the model,</text>
    <text x="258" y="178">    ... write files under output_dir</text>
    <text x="258" y="194">    return "one-line summary"</text>
  </g>
  <text x="390" y="214" text-anchor="middle" font-size="11" fill="#0E7069">the planner reads description to decide when to use it</text>

  <!-- what comes out -->
  <line x1="540" y1="115" x2="590" y2="115" stroke="#1A1E1C" stroke-width="1.4" marker-end="url(#ah)"/>
  <rect x="594" y="60" width="150" height="110" rx="6" fill="#FFFFFF" stroke="#1A1E1C" stroke-width="1.2"/>
  <text x="669" y="82" text-anchor="middle" font-weight="600">files</text>
  <text x="669" y="104" text-anchor="middle" font-family="Menlo, monospace" font-size="11.5">output_dir/*.json</text>
  <text x="669" y="122" text-anchor="middle" font-family="Menlo, monospace" font-size="11.5">output_dir/audits.csv</text>
  <text x="669" y="146" text-anchor="middle" font-size="11" fill="#5C665F">found by diffing the folder,</text>
  <text x="669" y="160" text-anchor="middle" font-size="11" fill="#5C665F">cataloged and committed by AOS</text>

  <line x1="60" y1="244" x2="700" y2="244" stroke="#D3D9D2"/>
  <text x="380" y="266" text-anchor="middle" font-size="11.5" fill="#5C665F">Rules: resolve paths with ws.abspath (never outside the workspace) · fail by raising StepFailed · never commit or edit the catalog yourself</text>
</svg>

```
