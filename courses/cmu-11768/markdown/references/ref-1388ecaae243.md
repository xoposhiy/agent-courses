# Project report: referenced Advanced NLP guidance

[Course index](../../README.md) · [Original source](https://cmu-l3.github.io/anlp-spring2026/assignments/assignment3&4) · [Raw file](../../raw/references/ref-1388ecaae243.html)

Retrieved: 2026-11-13T17:05:18.790857+00:00

|  |
| --- |
|  |
  

  

|  |

# Assignments 3 & 4

**Type:** Group Assignment

### Table of Contents

- [Summary](ref-1388ecaae243.md)
- [Timeline](ref-1388ecaae243.md)
- [Component-Wise Course Grade Proportions](ref-1388ecaae243.md)
- [Assignment 3.1: Project Proposal](ref-1388ecaae243.md)
- [Project Hours](ref-1388ecaae243.md)
- [Assignment 3.2: Baseline Reproduction](ref-1388ecaae243.md)
- [Assignment 4: Full Project](ref-1388ecaae243.md)
- [Poster Presentation](ref-1388ecaae243.md)
- [FAQ](ref-1388ecaae243.md)

## Summary

Assignments 3 and 4 are interrelated and are designed to guide you through the research project lifecycle, including literature review and project ideation, baseline reproduction, implementation, analysis, and presentation.

### **Timeline**

The full timeline for assignments 3 & 4 is below.

| Date | Item |
| --- | --- |
| 3/12 | [Submit TA matching form](https://forms.gle/FrtJxeYoXcGuP5jo6) |
| **3/24** | **Project Hours (Assignment 3.1 Presentations)** |
| **3/24** | **Assignment 3.1 Due** |
| 3/31 | Project Hours/Assignment 3.1 Grades and Feedback Released |
| **4/2** | **Assignment 3.2 Due** |
| 4/14 | Assignment 3.2 Grades and Feedback Released |
| 4/14 | Regrade Form for Project Hours, Assignment 3.1, and Assignment 3.2 Released |
| **4/21** | **Poster Session 1** |
| **4/23** | **Poster Session 2** |
| 4/21 | Regrade Form for Project Hours, Assignment 3.1, and Assignment 3.2 Closed |
| **4/27** | **Assignment 4 Due** |
| 4/27 | Regrade Decisions for Project Hours, Assignment 3.1, and Assignment 3.2 Released |
| TBD | Assignment 4 Grades and Feedback Released |

  

### Component-Wise Course Grade Proportions

| Component | Weight in Final Course Grade (%) |
| --- | --- |
| Assignment 3: Project Hours | 4% |
| Assignment 3.1: Project Proposal | 6% |
| Assignment 3.2: Baseline Reproduction | 5% |
| Assignment 4: Poster Presentation | 5% |
| Assignment 4: Full Project | 20% |

See the subsections below for component-level grading rubrics.

  

## Assignment 3.1: Project Proposal

Conduct a literature review on a topic of interest. Then, based on the gaps, trends, or opportunities identified, propose a relevant and feasible project topic.

Below, we outline the key elements of this assignment. Your report should include each of these sections.

- Motivation
  - What is the general research topic?
  - What is the significance of the research topic? Why is this topic worth working on?
- Literature Review
  - Provide a broad view of the relevant research landscape
  - Provide concrete descriptions on a small handful of the most highly related works.
  - Identify major trends/patterns across prior work.
  - Identify shortcomings with prior work and/or other opportunities that motivate this work
- Initial Proposed Approaches
  - Provide high-level descriptions for at least 2 potential approaches to innovate on the research topic
    - *see "Suggestions for Brainstorming Project Ideas" below for concrete advice*
    - be sure to consider compute requirements, and provide an estimate in your report
- Initial Proposed Data
  - Identify data sources that will be useful for training (if applicable) and evaluation.
- Initial Proposed Evaluation
  - Which concepts or theoretical constructs are most relevant for evaluating your method, and why?
  - If the constructs can’t be directly measured, what metrics will serve as acceptable proxies?
  - If your system consists of multiple components, what constructs/metrics will you use to evaluate the sub-components?
  - What qualitative analyses do you plan to conduct?

#### Suggestions for Brainstorming Project Ideas

Your project should be a novel contribution in NLP. Successful projects generally fall into one of these two broad categories:

1. New Method, Existing Problem
   1. Propose a new technique—such as architecture modifications, different training/inference paradigms or objective functions, data augmentation, inference strategies—for solving a well-established NLP task. The emphasis here is on technical innovation and sophistication, ideally building on advanced concepts introduced in the course.
2. Applying/Adapting Existing Methods to a New Problem
   1. Apply known NLP methods to a new task, domain, or language. The novelty in this type of project lies in problem formulation and thoughtful adaptation—tailoring existing methods to address the unique challenges of the new context.

To help brainstorm, it can be useful to consider how ideas popular in certain areas of NLP/ML may be applicable to a new task or domain. Alternatively, depending on your topics of interest, you might consider how theoretical frameworks or concepts from other fields–such as cognitive science, social sciences, or the humanities–could be usefully operationalized in an NLP context. Finally, we encourage you to talk to your classmates and the TAs to help generate and refine ideas!

#### Submission Requirements

Please submit a LaTeX report in ACL format: [ACL Overleaf Template](https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj). Page Limit: at most 5 pages for main body; unlimited pages for references and (optional) appendix.

#### Grading Rubric

| Criteria | Points |
| --- | --- |
| Motivation | 10 |
| Related Work | 50 |
| Initial Proposed Approach | 20 |
| Initial Proposed Data | 10 |
| Initial Proposed Evaluation Strategy | 10 |

  

## Project Hours

On 3/24, we will have in-person project hours instead of a lecture. This is the same day that the project proposal is due.

The purpose of the project hours is to ensure that your team has started planning the next phase of your project (baseline reproduction), practice presenting a work-in-progress research project, and get some early feedback from your team's assigned TA. You will have approximately 15 minutes with your TA. You should aim to present for about 10 minutes to ensure a few minutes are left for questions and discussion.

Your presentation should cover the following:

- introduce the research topic
- discuss key related work, including trends and shortcomings or opportunities to intervene
- your plan for baseline reproduction
  - You must cite a specific paper. If the paper proposes multiple models or tasks, identify the specific variants you plan to reproduce.
  - Verify that the baseline reproduction is feasible within your resource constraints (compute, API credits, etc)
- your initial ideas for new methods to address the research topic
  - What's one specific experiment you could run to test your idea?

Due to the time constraint, it is essential to be concise yet informative in your presentation and your responses. These are key skills in communicating effectively in virtually any research or industry context.

We recommend that you prepare a slide deck for the presentation. You can present directly from one of your teammates' laptop.

If you'd like to briefly chat with Prof. Welleck about your project, he will be at Project Hours and will be available to talk to teams for a few minutes on a first-come, first-served basis. You are also welcome to visit his or the TAs' office hours for additional discussion.

TA assignments and presentation slots will be announced no later than 3/20.

#### Grading Rubric

These presentations are intended primarily as an opportunity for you to get feedback, so grading is intended to be generous and largely based on completion. As long as your team addresses each of the major points (research topic, related work, baseline reproduction plan, initial proposed approach) in your presentation, you will receive full points (1 for each, and in total 4).

| Criteria | Points |
| --- | --- |
| Research topic | 1 |
| Related work | 1 |
| Baseline reproduction plan | 1 |
| Initial proposed approach | 1 |

It is critical that each team member is present and participates in the presentation. Any team member who does not attend project hours will receive a 0.

## Assignment 3.2: Baseline Reproduction

Reproduce a competitive baseline result for your project topic. Conduct an error analysis on the baseline performance. Refine your proposal in light of this analysis.

Below, we outline the key elements of this assignment. Your report should include each of these sections.

- Baseline Reproduction
  - Is there an existing baseline model/result for your research topic/task in the literature? If not, you must have a strong justification that the baseline you reproduce or develop is closely related to your task.
  - Describe the baseline you are reproducing
  - Is the baseline you selected the current state-of-the-art (SOTA) approach for the task? If not, justify why the one you picked is still a strong and fair baseline.
    - It is reasonable to define the scope of comparable models in terms of accessibility (e.g. open source vs. proprietary), or compute resources (e.g. small models vs large models).
  - Report your reproduction results alongside the originally reported results. Discuss any differences in the results. If the differences cannot be attributed to minor experimental quirks (e.g. randomness due to original paper not using random seed, variability in non-deterministic API outputs, etc), then you must offer some potential explanations for the differences.
- Error Analysis
  - Systematically analyze the baseline model behavior by looking at specific examples.
    - What cases does the model fail on? How did you identify these failure patterns?
    - Why do you think the model fails on these cases?
- Reflection
  - What have you learned about the task through this baseline reproduction and error analysis exercise?
    - What capabilities would a hypothetical model need to better handle the failure cases identified above?
    - Are there particular strengths of the baseline model that your initial proposed approach might lack?
  - How might you refine your initial proposed approach in light of these error analysis findings?
  - What if your initial proposed approach totally fails? Did the error analysis lead you to any new ideas worth exploring in the next phase of the project?

#### Submission Requirements

Please submit a LaTeX report in ACL format: [ACL Overleaf Template](https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj). Page Limit: up to 5 pages for main body; unlimited pages for references and (optional) appendix.

#### Grading Rubric

| Criteria | Points |
| --- | --- |
| Baseline Reproduction | 50 |
| Error Analysis | 30 |
| Reflection | 20 |

  

## Assignment 4: Full Project

Execute the project. Expect to iteratively refine your approach based on feedback from the course staff and any other issues or opportunities you identify during development and evaluation. Create a final report and present a poster for your project.

Your final report should include the following sections:

- Abstract
  - introduce significance of topic and state why your research intervention is necessary
  - high-level description of your approach
  - key results / insights
  - broad takeaway / contribution
- Introduction
  - Contextualize the problem and its significance
  - State what the research gap is
  - State your high-level approach and how it addresses the research gap
  - High-level summary of results
  - Gesture to the unique insights generated through your work and highlight their relevance to the field
- Related Work
  - Provide a broad view of the relevant research landscape
  - Provide concrete descriptions on a small handful of the most highly related works.
  - Identify major trends/patterns across prior work.
  - Identify shortcomings or problems with prior work and/or other opportunities that motivate this work
- Data
  - Description of dataset(s) used (source, size, domains, splits)
    - level of required detail depends on whether you are reusing existing dataset vs. introducing a new dataset you created.
  - Why are these dataset(s) appropriate for your task?
  - Preprocessing steps (filtering, cleaning, annotation)
- Method
  - Baseline reproduced: which paper/model/task, and why chosen
  - Description of your proposed method(s) (architecture, training, modifications)
  - Rationale: how your method addresses shortcomings of prior work
  - Implementation details (frameworks, compute, hyperparameters, training setup)
    - much of this info can be moved to the appendix to save space if needed
  - Experimental design: what experiments you ran to test your approach
    - state and motivate which constructs / metrics are used for evaluation
- Results
  - table(s) and/or plot(s) with key results, including
    - baseline results (according to your eval metric)
    - your method’s results (according to your eval metric)
    - statistical significance (if applicable)
  - if you have qualitative analysis results, report those as well
  - examples and error analysis for your method
    - If this takes up a lot of space, you can consider moving some or all of it to the appendix
- Discussion
  - interpretation of results: what do they tell us about the problem and your approach?
  - strengths of your method compared to baselines
  - weaknesses or surprising findings
  - theoretical and/or practical implications of findings
- Conclusion & Future Work
  - Recap of problem, method, and key results
  - Broader takeaway: why does this matter beyond your specific setup?
  - Future research directions (follow-up experiments, scaling, alternative methods, applications)
- Limitations
  - What are the key limitations with your data, method, or evaluation that readers should know about?
- Ethical Considerations
  - What are the key ethical risks you wrestled with during this research, or what risks are associated with your research artifacts (e.g., datasets, models) or results?
  - Are there any limitations in terms of incomplete, simplified, or biased representations in your data or task definition?
  - How can researchers, industry, and/or policymakers build on your work responsibly?

#### Submission Requirements

Please submit a LaTeX report in ACL format: [ACL Overleaf Template](https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj). Page Limit: up to 9 pages; unlimited pages for references and (optional) appendix.

#### Grading Rubric

| Criteria | Percentage (%) |
| --- | --- |
| Abstract | 5 |
| Introduction | 10 |
| Related Work | 10 |
| Data | 10 |
| Method | 25 |
| Results | 10 |
| Discussion | 10 |
| Conclusion & Future Work | 5 |
| Limitations & Ethical Considerations | 5 |
| Project Scope and Completion | 20 |

The first 80% evaluates the quality and completeness of each report section, while the remaining 20% in “Project Scope and Completion” evaluates the overall project scope, execution quality, and completion level rather than any specific written section.

## Poster Presentation

See <https://cmu-l3.github.io/anlp-spring2026/#poster> for information about the poster session.

## FAQ

#### How much flexibility does my team have to change our project direction throughout this process?

It is expected that your project direction and scope may change or sharpen slightly as you work through assignment 3.

For large and/or late project direction changes, you should speak with your TA and/or the instructor. Keep in mind that these changes may lead to additional work, e.g. if you totally abandon the project direction you used for project 3.1 in assignment 4, you will have to do a new lit review for the final report. Last minute changes to project direction for assignment 4 also means you won’t have gotten feedback on the idea throughout assignment 3.1 and 3.2.

For these reasons, we strongly advise against major project direction changes late in the semester.

#### What counts as ‘reproducing a competitive baseline result’?

- You are only required to reproduce one baseline, although you are welcome to reproduce multiple
- You may reuse existing code and pretrained models. You may not reuse precomputed model outputs (e.g., if the original authors saved raw output files).
  - You must have raw model predictions (not just aggregated eval statistics) that you generated yourself. These are needed for error analysis and may also be needed in the future (for assignment 4) to run statistical tests comparing the baseline with your proposed model.
- ‘Scaling down’ a baseline, e.g. by following a similar architecture but selecting smaller models, is not permitted for this assignment. Find a prior work that reports a baseline that is within your compute budget, as we want a fair comparison between the baseline you select and your eventual proposed method

#### Can my team’s primary contribution be proposing a new metric or dataset, rather than a model?

The answer is likely yes, but we recommend you discuss details with the instructor and TAs.

While in the typical case where the contribution is a model, data and metric are held constant in order to discriminate among models, in the alternative case that the contribution is a new metric, for example, you would probably treat model and data constant in your experimental design. In this setting, your ‘baseline’ might be another metric.

#### How many papers are expected to be covered in the literature review?

There is no set amount, as the requirements for a thorough and relevant literature review depends on the specific research topic.

#### Can I use a generative tool like Deep Research for the literature review?

The point of the literature review is to perform and write a literature review yourself. This involves searching for sources, reading the sources, synthesizing the ideas, and writing about them. You may only use AI tools (e.g., Deep Research, ChatGPT, etc.) for searching, i.e., identifying papers that may be relevant to your project. However, you must open and read the papers yourself, synthesize ideas, and write without the tool. You are also fully responsible for the quality of the selected literature, e.g., whether it is relevant and covers the requirements of the review, and any statements made about the literature. If we find evidence that a generative AI tool was used for purposes other than searching (e.g., summarizing papers, synthesizing ideas, drafting any portion of the literature review), you will receive a zero for the literature review and related sections. Since this is up to the grader’s discretion, the safest option is to not use the tool. Similarly, if the definitions above such as searching versus not searching are not clear, the safest option is to not use the tool at all. Similar policies apply to similar parts of the assignment that involve references, such as the introduction and related work. Again, we emphasize that a key objective of the assignment is to get experience performing a literature review on your own.

#### Can I use a generative AI tool to assist with writing other parts of the assignment?

First, be sure to read the FAQ question above about the literature review, as stricter policies apply to sections involving references. For all other written parts of the assignment, you may only use AI tools for minor, surface-level edits such as grammar checking or rephrasing individual sentences for clarity. However, AI cannot be used for substantive generation or editing of the writeups, such as producing substantial portions of text (paragraphs, sections, etc), synthesizing ideas, etc. If we determine that substantive content was AI generated, you will receive a zero for that section. Since this is up to the grader’s discretion, the safest option is to not use the tools beyond things that are clearly minor edits. If the definition of minor edits is not clear, the safest option is to not use the tool at all.

#### How much space in the report should we allocate to each subsection?

There are no hard requirements here, apart from the overall report page limit. If you’re confused, find some similar papers in the [ACL anthology](https://aclanthology.org/events/acl-2025/) to calibrate.

#### How can I use grace days for these assignments?

You may use grace days for Assignments 3.1 and 3.2.

You may not use grace days for the Project Hours, the Poster Session, or Assignment 4.

#### Team issues / Unfair Distribution of Work / Team Changes

We encourage teams to first try to resolve disputes around unfair distribution of work among themselves. Please be a good teammate and communicate regularly with your team.

If the problem persists, please reach out to the instructor, who will work with your team on a case-by-case basis to ensure people are graded fairly for their contributions.

#### Project Hours/Poster Session Conflicts

You must attend the project hours and the poster session in person. There will be sign-in sheets on these days. Note that missing your team’s scheduled project hours or poster session day will result in a 0 grade for that component. You are required to attend the project hours and present your poster in person.

If you have a serious conflict with one of the project hours or poster session days (e.g. for academic conference travel), let us know in advance (make a private post on Piazza and provide your team name). Exeptional circumstances will be handled on a case by case basis.

#### Poster Printing

See <https://cmu-l3.github.io/anlp-spring2026/#poster> for details.

#### Negative Results

Sometimes experiments don’t work as planned. If you try to get positive results but are not successful, you may still get a good grade by clearly describing why you thought your methods would work, and then performing an analysis of why your initial assumptions were incorrect, leading to results that did not match your initial expectations. The bar for paper writing, experimentation, and analysis will be a bit higher in these cases, as we want to make sure that you really made a serious effort.
