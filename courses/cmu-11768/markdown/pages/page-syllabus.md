# CMU 11-768: Syllabus

[Course index](../../README.md) · [Original source](https://www.cmu-agents.com/#/syllabus) · [Raw file](../../raw/pages/syllabus.html)

Retrieved: 2026-11-13T16:45:18.257124+00:00

## Syllabus

### Prerequisites

- Prior experience training neural language models.
- Recommended background includes 11-667, 11-711, 10-202, or equivalent experience.

### Class Format

The first half of the course emphasizes individual implementation assignments on core agent capabilities and domains. The second half centers on a team-based mini research project on advanced agent topics.

### Target Audience

Graduate students with prior experience training neural language models. Relevant background includes coursework such as 11-667, 11-711, or 10-202, or equivalent experience.

### Course Themes

- **Agent Capabilities:** Instruction following, tool use, planning, and memory systems.
- **Application Domains:** General tool use, coding agents, GUI agents, and social agents.
- **Training Methods:** Supervised fine-tuning plus reinforcement learning algorithms and systems.
- **Frameworks:** OpenHands, LangGraph, and other agent development frameworks.
- **Safety:** Sandboxing, credentialing, and adversarial attacks on agents.
- **Advanced Topics:** Human-agent interaction, multi-agent systems, and search-based reasoning.

### What You'll Learn

By the end of this course, students will be able to:

- Implement an agent from scratch on top of an open-source LLM.
- Design evaluations for multi-step tasks.
- Train agents to improve their capabilities.
- Reason about safety and reliability tradeoffs.
- Pursue an open research question in agents.

### Grading

| Component | Weight | Format |
| --- | --- | --- |
| Assignment 1: Harness | 10% | Individual |
| Assignment 2: Eval | 15% | Individual |
| Assignment 3: Training | 15% | Individual |
| Lecture highlights | 10% | Individual |
| Project Hours | 5% | Team of 2–4 |
| Poster Presentation | 15% | Team of 2–4 |
| Report | 30% | Team of 2–4 |

### Related Courses

Courses with overlapping content that students may also consider:

- [11-711: Advanced NLP](https://cmu-l3.github.io/anlp-spring2026) — Roughly two weeks on RL and agents, with stronger emphasis on RL methods.
- [11-766: Large Language Model Applications](https://cmu-llms.org/schedule/) — Roughly two weeks on agent-adjacent applications such as tool calling, security, multi-agent systems, and code assistants.
- [11-891: Neural Code Generation](https://cmu-codegen.github.io/f2025/) — Roughly two weeks on code generation agents.
- [11-777: Multimodal Machine Learning](https://cmu-mmml.github.io/) — Roughly one week on GUI agents.

## Course Policies

The assignments and research project are designed to build the implementation, evaluation, and research skills needed to create capable and reliable LLM-based agents. By the end of the course, students should be able to build an agent on top of an open-source language model, evaluate it on multi-step tasks, train it, and investigate an open research question.

**Read each assignment and project description carefully.** You are responsible for following all instructions, including requirements about permitted resources, collaboration, formats, and deadlines. Failure to follow the stated requirements may result in a deduction even if the underlying work is otherwise correct.

### Individual and team work

Assignments 1–3 must be completed individually. You may discuss course concepts and general approaches with classmates, but the code, analysis, and writing you submit must be your own unless an assignment explicitly permits additional collaboration. Do not share solutions or view another student's solution.

The research project must be completed in a team of 2–4 students. Project teammates may share code, writing, results, and ideas with one another. Each teammate is expected to understand the entire submission and to make a substantive contribution. Course staff may use project materials, version history, and conversations with the team to understand individual contributions.

If you have difficulty finding a project team, contact the course staff by the team-formation deadline. We will help match ungrouped students.

### Submission

Unless an assignment description says otherwise, submit work through Canvas by the posted deadline. Each description will specify the required materials, which may include source code, system outputs or evaluation results, a PDF report, and a link to a code repository.

You are responsible for confirming that:

- all required files are present, correctly named, and readable;
- the submitted archive opens successfully;
- repository links are accessible to the course staff by the deadline, including when the repository is private;
- the submitted code runs in the required environment; and
- the submission does not contain credentials, private data, model API keys, or other secrets.

The version received through the designated submission system is the version that will be graded. Submit early enough to correct upload, permission, or packaging problems before the deadline.

### Late work and slack days

Each of Assignments 1–3 includes two slack days. A slack day is a 24-hour extension and may be used without advance permission. Slack days are attached to each assignment: they cannot be transferred between assignments, shared with another student, or applied to another course component. Any part of a 24-hour period counts as one slack day.

After both slack days for an assignment have been used, 5% of that assignment's total possible score will be deducted for each additional day or part of a day that it is late.

The project Report is due Friday, December 4, 2026, at 11:59 PM and allows up to three late days without penalty, through Monday, December 7, 2026, at 11:59 PM. Report submissions after that time will not be accepted. No late days may be used for Project Hours or the Poster Presentation.

Documented health conditions, disability accommodations, religious observances, and other circumstances covered by university policy will be handled in accordance with CMU policy. Job interviews, recruiting events, routine personal travel, and other ordinary personal conflicts are *not* excused absences. Plan these activities around class whenever possible. For other serious or exceptional circumstances, contact the instructors as soon as reasonably possible.

### Lecture highlights

After each eligible lecture, submit a lecture highlight through the corresponding Canvas quiz **within 24 hours after the lecture ends**. A lecture highlight should contain one thoughtful takeaway or question that demonstrates engagement with the lecture. It should be specific enough to show what idea, argument, method, result, or unresolved issue prompted your response. A generic summary or a statement that could have been written without attending or reviewing the lecture will not receive credit.

There will be 22 opportunities to submit lecture highlights, and this portion of the grade will be calculated from 20 submissions. The two additional opportunities provide built-in flexibility for occasional absences for any reason. If an excused absence affects additional submissions, contact the course staff promptly so that an appropriate accommodation can be arranged.

Lecture highlights are graded for timely, thoughtful engagement, not for agreeing with the instructors or asking a question with a known answer. Because they are intended to capture your own engagement with the class, the response you submit must be written by you rather than generated by another person or an AI tool.

### Use of AI tools

You *may* generally use AI tools to assist with assignments and project report work unless a particular assignment or project description restricts or prohibits their use. We prohibit AI tools for lecture highlights. Assignment-specific rules always take precedence over this general permission.

Regardless of how AI tools are used, you are responsible for:

- the accuracy and validity of every claim, result, citation, and piece of code you submit;
- complying with all requirements and restrictions in the assignment or project description;
- understanding all submitted code, methods, analyses, and writing; and
- ensuring that your submission represents permitted work and does not incorporate another student's solution or otherwise violate academic-integrity rules.

AI output is not an authoritative source. Check generated code and factual claims, verify citations against the original sources, and test all submitted work. You may not use an AI tool to bypass a requirement that you implement, analyze, or write something yourself.

**We will assess your understanding through quizzes** about the assignments and project reports. You may be asked to explain design decisions, code behavior, experimental results, limitations, or written claims in your submission. You are responsible for being able to explain and defend the work even when an AI tool helped produce or revise part of it.

### Academic integrity, external resources, and code reuse

All course work is governed by the [Carnegie Mellon University academic-integrity policy](https://www.cmu.edu/student-affairs/ocr/). Violations may result in penalties including no credit for the work, failure of the course, and university disciplinary action.

Unless an assignment explicitly says otherwise:

- Code, pseudocode, templates, and starter materials supplied by the instructors or TAs may be used for that assignment.
- When an assignment asks you to implement a method, you may not substitute an existing implementation written by someone else for your own work.
- You may not use code or solutions written by another current or former student. Project teammates may share work only within their own team for the team project.
- Any permitted external code, data, text, figures, or ideas must be used consistently with its license and cited appropriately. A citation does not make otherwise prohibited reuse permissible.
- Do not post assignment solutions publicly unless the instructors give permission.

If your course project may overlap with work you are doing elsewhere—for example, another course or a separate research project with individuals not in this course—consult the instructors early. Generally, they should be separate projects.

### Consulting the course staff

For assignments and projects, you are free to consult with the TAs and instructors during office hours, project hours, and through Piazza. If you don't have much experience with NLP, it will be helpful to consult with the instructors and TAs to learn about how to do the assignments and course project.

Because this is a project-based course, we assume that many of the students taking the course will be interested in turning their assignments or project into research papers. In this case, if you have received useful advice from the instructor or TAs that made the project significantly better, consider inviting them to be co-authors on the paper. Of course, you do not need to do so just because the paper is a result of the class, only if you feel that their advice or help made a contribution. Do not add individuals as authors to a paper without consulting with those individuals first!
