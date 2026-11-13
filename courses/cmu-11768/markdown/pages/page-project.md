# CMU 11-768: Project

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/#/project) · [Raw file](../../raw/pages/project.html)

Retrieved: 2026-11-13T16:45:18.207110+00:00

## Research Project

Work in a team of 2–4 students to make a novel contribution to LLM-based agents. Develop a focused idea, study relevant prior work, implement and evaluate your approach, and communicate what you learn. The project has three components: Project Hours, Poster Presentation, and Report.

The [course policies](page-syllabus.md) apply to collaboration, submission, academic integrity, and AI tool use. Every teammate should make a substantive contribution and understand the project as a whole.

Project components and weights in the final course grade

| Component | Course grade | Format |
| --- | --- | --- |
| Project Hours | 5% | Team of 2–4 |
| Poster Presentation | 15% | Team of 2–4 |
| Report | 30% | Team of 2–4 |

### Project scope and expectations

Aim for work at or close to the level of a workshop submission: a focused novel contribution, meaningful experiments, and thoughtful analysis. Keep the scope manageable, for example by focusing on a few models, a limited set of tasks, and a few well-chosen experiments or analyses. We do not expect experimental evidence at the scale or scope of a full conference submission in this project, although if your results are promising your work could lay a foundation for one.

Expect to spend approximately **9 hours per week per person** on the project now that the assignments are complete. When grading, we will account for your team size and the roughly one-month project timeline.

### Project Hours

**Thu, Nov 5, 2026, during class time (3:30–4:50 PM).** Meet with your assigned TA as a team to discuss your research plan and get early feedback. Each team has a **10-minute slot**. Aim to present for **6–7 minutes**, leaving the remaining time for questions and discussion.

See the Project Hours post on [Piazza](https://piazza.com/cmu/fall2026/11768/home) for your group’s room and time assignment. Room assignments are organized by TA.

Prepare a concise presentation covering:

- **Research topic:** What question are you investigating, and why does it matter?
- **Related work:** What are the most relevant prior results, and what gap or opportunity do you see?
- **Experimental plan:** What tasks, data, baselines, and evaluation metrics will you use? Cite the work behind your comparisons and check that the experiments fit your compute and API budget.
- **Proposed approach:** What will you try, and what specific experiment would test your idea?

We recommend preparing slides and presenting from a teammate’s laptop.

#### Grading

Project Hours are primarily an opportunity for feedback. Grading is based on completion: address all four topics above to receive full credit, with each topic worth one quarter of the Project Hours grade. Every team member must attend and participate. A team member who misses Project Hours receives zero for this component.

### Poster Presentation

**Tue, Dec 1 and Thu, Dec 3, 2026, during class time (3:30–4:50 PM).** Present your project in person during your team’s assigned poster session. Use the session to practice explaining the work, learn about classmates’ projects, and gather feedback to improve your report.

Your poster should make three things easy to understand:

- The problem and why it matters.
- Your approach and experimental setup.
- Your results and the main lessons from them.

Choose a readable layout with clear figures and concise text. A three-column layout organized around the problem, method, and results is one option; there is no required poster template.

#### Grading

The poster is graded pass/fail based on completing a poster and attending your assigned session to present it. Every team member must attend and participate to receive credit.

### Report

**Due Friday, December 4, 2026, at 11:59 PM.** You may use up to three late days to submit without penalty through **Monday, December 7, 2026, at 11:59 PM**. Submissions after that time will not be accepted.

Carry out the project and refine your approach as you learn from experiments and feedback. Write a research report that explains the question, the work you completed, and the evidence supporting your conclusions.

#### Report contents

Abstract
:   Summarize the research question, why it matters, your approach, the main findings, and the contribution.

Introduction
:   Explain the problem in AI agents and the gap that motivates your work. Introduce your approach and give a brief overview of the results and insights.

Related Work
:   Situate the project in the relevant research landscape. Discuss the closest studies in enough detail to explain how your work builds on them and which limitations or open questions it addresses.

Data
:   Describe your tasks, environments, and datasets, including their sources, sizes, domains, and splits. Explain why they suit your research question and document any collection, annotation, filtering, or preprocessing.

Method
:   Describe your approach and comparison baselines, justify the design choices, and explain your experimental setup and evaluation metrics. Include the model, agent harness, tools, training or inference procedure, compute budget, and hyperparameters needed to understand and reproduce the work. Additional implementation details may go in the appendix.

Results
:   Present the evidence for your claims using tables, plots, and concrete examples. Compare against appropriate baselines, report uncertainty or significance where appropriate, and analyze failures as well as successes. Include qualitative findings when relevant.

Discussion
:   Interpret the findings in relation to your research question. Explain the strengths and weaknesses of the approach, unexpected behavior, and what the results imply for building or studying agents.

Conclusion & Future Work
:   State the main takeaway and its significance beyond your particular setup. Identify useful follow-up experiments or research directions.

Limitations
:   Explain the boundaries of the evidence: constraints in the data, tasks, models, resources, or evaluation, and settings to which the findings may not generalize.

Ethical Considerations
:   Discuss relevant risks from the agent’s capabilities, tool access, data, or deployment. Address privacy, bias, potential misuse, and safeguards where applicable.

Team Member Contributions
:   Describe each team member’s contributions to the project, including implementation, experiments, analysis, and writing.

#### Submission

Submit a PDF report through Canvas, written in LaTeX using [ACL format](../references/ref-9f9fd61adb31.md). Aim for **6–9 pages** of main text, with a maximum of **9 pages**. References and an optional appendix do not count toward this limit. Length itself earns no credit; do not pad a complete, concise report to reach nine pages. Follow the course submission policies and ensure any submitted repository links are accessible to course staff. Describe each team member’s contribution to the project.

#### Grading

The report is evaluated on the clarity and completeness of the sections above, the motivation and scope of the research question, the quality of the implementation and experiments, and the depth of the analysis. Explain what you completed and support your claims with evidence.

### FAQ

#### Can I use AI tools for the project?

Yes. You may use AI tools for your project, consistent with the [course policy on AI tools](page-syllabus.md#ai-tools). You are responsible for the accuracy of your work and for understanding all submitted code, methods, results, and writing. We will test your understanding of your project through the poster presentation, and we may interview you about your report after you have submitted it.

#### How much space in the report should we allocate to each subsection?

There is no fixed allocation across sections. Spend space on the details needed to understand your contribution and evidence, while staying within the overall page limit. Papers on similar topics can help you judge the balance. Use an appendix for supporting material rather than essential claims or results.

#### How can I use late days for the project?

You may use up to three late days for the Report, which is due Friday, December 4, 2026, at 11:59 PM. Reports submitted by Monday, December 7, 2026, at 11:59 PM incur no penalty; submissions after that time will not be accepted. You cannot use late days for Project Hours or the Poster Presentation.

#### Team issues / Unfair Distribution of Work / Team Changes

Communicate regularly and agree on responsibilities with your teammates. Try to resolve disagreements within the team first. If a problem continues or a team change is needed, contact the instructors promptly so they can help and assess contributions fairly.

#### Project Hours/Poster Session Conflicts

Attendance and participation in person are required for both Project Hours and your assigned poster session. Missing either event results in zero for that component. If you have a serious conflict, contact course staff in advance through a private post on [Piazza](https://piazza.com/cmu/fall2026/11768/home) and include your team name. Exceptional circumstances will be considered individually in accordance with course policies.

#### Poster Printing

Arrange printing early enough to bring a printed poster to your session. Check the printing service’s file requirements and turnaround time before submitting your PDF. Contact the TAs in advance if you need help arranging printing.

#### Negative Results

A carefully executed project can earn a good grade even when the proposed approach does not improve the results. Explain the hypothesis and why it was plausible, document the experiments, and investigate why the outcome differed from your expectations. Strong analysis and clear evidence of a serious research effort are especially valuable here.

Adapted from the [Spring 2026 Advanced NLP project guidance](../references/ref-1388ecaae243.md).
