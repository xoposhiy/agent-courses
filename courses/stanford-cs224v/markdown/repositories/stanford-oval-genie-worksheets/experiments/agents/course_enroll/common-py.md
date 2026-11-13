# Project code: stanford-oval/genie-worksheets: experiments/agents/course_enroll/common.py

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/agents/course_enroll/common.py) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/agents/course_enroll/common.py)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```python
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
prompt_dir = os.path.join(current_dir, "prompts")

botname = "Course Enrollment Assistant"
starting_prompt = """Hello! I'm the Course Enrollment Assistant. I can help you with :
- Selecting a course: just say find me programming courses
- Enrolling into a course. 
- Asking me any question related to courses and their requirement criteria.

How can I help you today? 
"""
description = "You are a course enrollment assistant. You can help students with course selection and enrollment."

```
