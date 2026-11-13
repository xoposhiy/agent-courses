# Minimizing hallucination in task-oriented agents

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-newWorksheet.pdf) · [Raw file](../../raw/slides/l-newworksheet.pdf)

Retrieved: 2026-11-13T16:49:47.458348+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

CS224v

Conversational Virtual Assistants

with Deep Learning

Lecture 9: Task-Oriented Agents

1

Monica Lam and Harshit Joshi

## Page 2

STANFORD
LAM

Air Canada's chatbot promised a discount
that wasn't available to passenger Jake Moffatt.

The British Columbia Civil Resolution Tribunal ruled that 
Air Canada had to pay Moffatt $812.02 (£642.64) in damages and tribunal fees.

## Page 3

STANFORD
LAM

A Case Study
Course Enrollment at Stanford

Let’s consider a CS MS student

## Page 4

STANFORD
LAM

Enrollment Task: invoke enroll

class StudentInfo(TypedDict):

student_name: str

student_ID: str

student_email_address: str

def enroll (student_info: StudentInfo,  
 
  
 
   course_to_take: CourseToTake) 
       -> None:

pass

from typing import TypedDict

from enum import Enum

class GradeType(Enum):

LETTER = "Letter"

CRED_NOCRED = "Cred_noCred”

class CourseToTake(TypedDict):

course_name: str

grade_type: GradeType

num_units: int

confirm: bool
A simple enough task, or is it?

## Page 5

STANFORD
LAM
6

I am studying computer science. 
I want to complete the significant 
implementation requirement.
What are some of the options that require the 
least amount of work?

What course would you like to enroll in?

Course Enrollment Agent

User:

## Page 6

STANFORD
LAM

A Course Enrollment Assistant


Students need to consult:

•
All offered courses

•
Description, instructors, 
offerings, and units

•
Unique to each 
department and 
specialization

•
Program sheets

•
Ratings, reviews, hours 
of work, enrollment 
outcomes, 
and sequencing

What course would you like to enroll in?

Course Enrollment Agent

## Page 7

STANFORD
LAM

AI

## Page 8

STANFORD
LAM

Computational
Biology

## Page 9

STANFORD
LAM

Computer and
Network Security

## Page 10

STANFORD
LAM

Software
Theory

## Page 11

STANFORD
LAM

Systems

## Page 12

STANFORD
LAM

Theory

## Page 13

STANFORD
LAM

## Page 14

STANFORD
LAM

Task assistant are also

knowledge assistants

## Page 15

STANFORD
LAM

Translates Questions into SUQL

I am a sophomore studying computer science. I 
want to complete the significant 
implementation requirement.
What are some of the options that require the 
least amount of work?

SELECT title, course_codes, description, 
average_hours_spent 
FROM courses WHERE 
significant_implementation_requirement = TRUE 
ORDER BY average_hours_spent LIMIT 5;

## Page 16

STANFORD
LAM

Preview of Real User Evaluation

Restaurant
Course Enrollment
Service Now
Ticket Submission

GPT4: function calling
  + Genie DB parser
54.5
10.0
0.0

Genie Worksheet
91.6
80.0
80.0

Goal Completion Rate (%)

GPT-4 results are not acceptable

•
Low completion rate: even 54.5% on restaurant is not good enough!

•
Course enrollment: 
Hallucinates non-existent courses despite using knowledge base results

## Page 17

STANFORD
LAM

An Example of a Conversation

Using Genie Worksheets

## Page 18

STANFORD
LAM

## Page 19

STANFORD
LAM

Consideration: Time Offered

## Page 20

STANFORD
LAM

Consideration: Sort by Course Rating

## Page 21

STANFORD
LAM

Credit or Letter?  Depends on the Workload

## Page 22

STANFORD
LAM

Pick Max. Number of Units

## Page 23

STANFORD
LAM

What makes it hard to implement

task oriented agents?

## Page 24

STANFORD
LAM

1. Task agents are also knowledge agents

25

Structured
Free Text
Tasks

Restaurants
Cuisines, opening hours, 
address, rating

Reviews, popular 
dishes
Book restaurant

Products

Product ID, cost, ratings, 
sizes, physical 
dimensions, color

Descriptions, 
reviews

Purchasing
Ordering food

Courses

Class number, time 
offered, instructor, 
building, pre-requisites

Descriptions, 
reviews
Enrolling in courses

Business 
processes
Receipts, statements
Regulations

Filing taxes
Reimbursements 
Customer support

Medical
Patient demographics
Prescription
Diagnosis history
Making diagnoses
Insurance claims

## Page 25

STANFORD
LAM

2. Mixed Initiatives

• Knowledge agents

• Users take the initiatives in asking questions

• Task agents need to take initiatives

• Ask users for required parameters; 
users may not answer the agents’ questions

• Suggest new actions

## Page 26

STANFORD
LAM

3. Scale: Long instructions, conversations, contexts

Long conversations!
Need to track: instructions, user requests, task parameters

What is the solution?

## Page 27

STANFORD
LAM

Common Approach: Multi-agents

A coordinator calls different agents for different functions

Advantages:

• Shorter prompt, shorter conversation context per agent

Disadvantages

• As a user, how would you like to be passed from one agent to 
another?

• How to answer related questions or solve simultaneous 
constraints?

• E.g. hotel reservation needs to know the flight booked

## Page 28

STANFORD
LAM

Summary: Challenges of Task-Oriented Agents

1. Also a knowledge agent

2. Mixed initiatives:

responsive to user requests, must accomplish its tasks

3. Scale: long instructions, contexts

4. SAFETY: chatbots are user-facing – can we trust it?

We need to specify the policies:
what the agent should do under all circumstances!

We need FULL SPECIFICATIONS and to ENFORCE adherence!

There is no free lunch.

## Page 29

STANFORD
LAM

Outline

• Challenges of task-oriented agents

• Genie Worksheets

• Design and Implementation

• Capabilities

• Evaluation

## Page 30

STANFORD
LAM

In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL), 
Vienna, Austria, July 2025.

## Page 31

STANFORD
LAM

Genie Worksheet Design Principles

Genie Worksheet: Full declarative, specification

Knowledge corpora; Tasks
•
What to do under all circumstances
•
What state to keep for the conversation

Genie runtime:

•
Use LLMs to parse user input (with a customized context)

•
Save the conversation state and perform actions
based on the Worksheets

•
Tell LLMs the response to generate (with a customized context)

1. Knowledge

agent

4. Safety

2. Mixed 
initiatives

3. Scale

## Page 32

STANFORD
LAM

Developer Specification

Design principle: Declarative

•
Users just provide declarative info about the resources

•
Genie Runtime handles the conversation flow

•
Minimal information to guarantee safety

2 kinds of worksheets

•
Knowledge Worksheets
•
Schemas of structured and unstructured data. 
(SUQL used)

•
Task Worksheets
•
APIs: Function calling parameters

•
Policies: Actions in Python

developer

Genie Worksheet

Genie Runtime

## Page 33

STANFORD
LAM

1. Course Assistant Knowledge Corpus

courses DB

internal; primary
int
course_id
internal
int
max_units
internal
str
title
internal
str
grading
internal
List\[str\] course_codes
internal
List\[str\] general_requirements
internal
int
min_units
internal
str
description
internal
int
average_hours_spent

internal
Enum
foundations_requirements

logic_automata_and_complexity
probability
algorithmic_analysis

computer_organization_and_systems

principles_of_computer_systems

internal
bool
significant_implementation_requirements
internal
Enum
breadth_requirement

formal_foundations
learning_and_modeling
systems
people_and_society

internal
List\[str\] prerequisite_course_codes

offerings
DB

internal
int
course_id

internal
Enum
days

Monday

Tuesday

Wednesday

Thursday

Friday

Saturday

Sunday

internal
str
start_time

internal
str
end_time

internal
List\[str\]
instructor_names

internal
Enum
season

autumn

winter

spring

summer

programs
DB

internal; primary int
program_id

internal
Enum
level

MS

BS

PhD

internal
Enum
specialization

AI

Computational Biology

Human-Computer Interaction

Information Management & Analytics

Visual Computing

Software Theory

Systems

Theoretical Computer Science

general

Computer & Network Security

internal
str
sheet_requirements

ratings
DB
internal; primary int
rating_id
internal
int
course_id
internal
List\[str\]
instructor_names
internal
int
average_rating
internal
int
num_ratings
internal
int
term_id
internal
int
start_year
internal
int
end_year
internal
Enum
season

autumn
winter
spring
summer
internal
List\[str\]
reviews

## Page 34

STANFORD
LAM

2. Stanford Course Enrollment Form

Form Name
Kind
Type
Name
Enum Values
Description
WS Action

Main
WS
course_enrollment

Say(enroll(StudentInfo, 
        courseToTake))

input CourseToTake course_to_take
The course to enroll
input StudentInfo
student_info_details
Information on the student
StudentInfo
worksheet
input str
student_name
Name of the student
input str
student_id
Student's ID number

input str
student_email_address
Student's email address

CourseToTake
worksheet
input str
course_name
Name of the course 
input Enum
grade_type
The desired grading basis

Cred/No Cred Taken for credits
Letter
Taken for grades
input int
num_units
The number of units taken
input confirm
confirm
Confirm the course

## Page 35

STANFORD
LAM

Predicates needed for data dependent fields

• Some fields are needed only for some users

Agent: Are you an international student?

User: yes, I am currently on a study visa.

Agent: What type of visa is it? F1 or J1?

## Page 36

STANFORD
LAM

+ Data-Dependent Worksheets/Fields
+ Field actions

FALSE

## Page 37

STANFORD
LAM

Task Worksheets

A task is like a function, with predication

•
Task Definition: Name, Predicate (when is it active), Kind (Task or DB), 
  
 
 
         Action (result of task)

•
Field Definition: Name, Predicate, Kind (input, output, internal)
  
 
 
 
     Type (WS name, str, enum, …, confirm),  
  
 
 
 
     Description, 
  
 
 
 
     Don’t Ask (Capture if info is offered), 
  
 
 
 
     Required (Ask but may be optional),
  
 
 
          Action (code to execute on input)

•
Built-in actions: say, propose

•
User-define actions as python code

Whether confirmation is needed 
before task action is performed

## Page 38

STANFORD
LAM

Discussion

What can Genie Worksheets do?

Or not do?

## Page 39

STANFORD
LAM

How Genie Handles Long Conversations

Partial Worksheets

(dialogue state)

Genie Run Time 
LLM-Based Parser

last turn + 
current user input

Updates to Worksheets

INPUT

Genie Run Time 
Executor
Knowledge DB/API calls

EXECUTE POLICY

Queries
Activated actions

OUTPUT

Responses from above
Asks for confirmation
Asks for missing parameters 
      in the worksheet

Genie Run Time 
LLM Response Generator
Agent Act

Response to User

Last agent output +

current user input

Query
API call

## Page 40

STANFORD
LAM

Example: One Conversational Turn

dt : dialogue state at time t

dt-1

Executor

ut : user utterance at time t

: agent act at time t

Parser

dt

Assistant: Absolutely! HCI 347 can be taken 
up to 5 units. Would you like to take it? 
at

Response Generator

at

at : agent utterance at time t

at

## Page 41

STANFORD
LAM

Outline

• Challenges of task-oriented agents

• Genie Worksheets

• Design and Implementation

• Capabilities

• Evaluation

## Page 42

STANFORD
LAM

Managing Mixed Initiatives

ASSISTANT

Sure.  How much money do you want to transfer?

You have $157.00
How much money would you like to transfer?

USER:

I want to transfer money.

How much money do I have in the account?

## Page 43

STANFORD
LAM

User Changing Previous Answers

ASSISTANT

I have found 3 flights for you. ... Which one would you pick?

USER:

I want to fly from New York to Los Angeles on 8th this month.

Oh wait, I have a meeting on 8th, I think I will leave on 9th.

## Page 44

STANFORD
LAM

Support Multiple Knowledge Queries

ASSISTANT
USER:

Can you suggest some highly rated NLP courses? Also, 
when does the next semester start?

CoursesDB (
SELECT * FROM courses WHERE 
    answer(“is this NLP course?”, description) AND ratings > 4.5)

CoursesDB(answer(“when does the semester start?”,  ,,,)

## Page 45

STANFORD
LAM

Composition of Queries & Function Calls

Use the result of a worksheet as input to another worksheet

User: I want to book an Italian restaurant in NYC

for two on Valentine’s day.

BookRestaurant(restaurant=
    RestaurantsDB (“SELECT * FROM restaurants WHERE 
           ‘italian’ = ANY(cuisines) AND location = ‘NYC;’)”), 
    date=“02/14/2024”, and num_people=2)

## Page 46

STANFORD
LAM

Another Example

ASSISTANT

I can help you with enrolling in an AI course. Here are some top-rated AI courses:

CS 224V, CS 224N, CS205. Which one would you like to take?

USER:

I want to take an AI course for 3 units and letter grade.

Enroll(
    course=CoursesDB (“SELECT * FROM courses WHERE 
       answer(description, “is the course on AI”)=“yes””),       
    num_units=3, grade_type=Letter)

## Page 47

STANFORD
LAM

Summary: Genie Worksheets Can

• Support data-dependent parameter queries

• Support multiple queries and requests in a single utterance

• Support arbitrary interleaving of queries & action requests

• Keep track of essential information in long conversations

• Allow unhappy paths, eg. User changing their answers

Developer only needs to supply the Genie Worksheets

## Page 48

STANFORD
LAM

Outline

• Challenges of task-oriented agents

• Genie Worksheets

• Design and Implementation

• Capabilities

• Evaluation

## Page 49

STANFORD
LAM

Evaluation

• To compare with existing work: STARV2 Dataset (2022)

• Wizard-of-Oz: 3 hardest domains--bank, trivia, trip

• Annotated with: “user and agent dialogue acts”

Mosig, Johannes EM, Shikib Mehri, and Thomas Kober. "Star: A schema-guided dialog dataset for transfer learning.”
Zhao, Jeffrey, et al. "Anytod: A programmable task-oriented dialog system."

## Page 50

STANFORD
LAM

STARv2 Evaluation

•
SOTA: AnyTOD (AT XXL)

•
finetuned T5 (13B) on 6000 examples 
(all domains but the test)

•
Implement programs to handle logic

•
Genie:

•
Semantic parsing prompt: 3 examples

•
Agent Policy: 9 lines in a Worksheet

System Action F1: The next agent action

Most errors caused by inconsistent data annotations

## Page 51

STANFORD
LAM

Evaluation

• To compare with existing work: STARV2 Dataset (2022)

• Wizard-of-Oz: 3 hardest domains--bank, trivia, trip

• Annotated with: “user and agent dialogue acts”

• WOZ benchmarks:

• not realistic -- few unhappy paths

• too easy for LLMs (simple slot fills)

• Worse annotations than LLM outputs!

Mosig, Johannes EM, Shikib Mehri, and Thomas Kober. "Star: A schema-guided dialog dataset for transfer learning.”
Zhao, Jeffrey, et al. "Anytod: A programmable task-oriented dialog system."

LLM out-ran 
traditional NLP evaluation!

## Page 52

STANFORD
LAM

Quiz
What should we do next?

## Page 53

STANFORD
LAM

Evaluation with real users

Three diverse applications with varying complexities.

• Restaurant Reservation: Uses the real-life database from Yelp

• Ticket Submission: A subset of Service Now api

• Course Enrollment: Uses multiple real-life databases of 
courses at Stanford University.

Note the difference 
in complexity

## Page 54

STANFORD
LAM

Baseline and Study Design

• Compare to GPT-4 turbo with Function Calling. 
• Gives GPT-4 the same KB-Parser as Genie Worksheet

• Users 
• Restaurant Reservation and Ticket Submission:

• 22 and 20 users from Prolific crowdsource platform
• Course enrollment:

• 20 university students 
• Randomly assigned Genie Agent or GPT-4 (FC)

## Page 55

STANFORD
LAM

Real User Evaluation

Restaurant
Course Enrollment
Ticket submission

GPT4: function calling
  + Genie DB parser
54.5
10.0
0.0

Genie Worksheet
91.6
80.0
80.0

Goal Completion Rate

GPT-4 results are not acceptable

•
Low completion rate: even 54.5% on restaurant is not good enough!

•
Hallucinates non-existent courses despite using knowledge base results

Genie Worksheets – deployable with additional engineering

•
Only LLM-based technique that does not hallucinate on Query results/Actions

## Page 56

STANFORD
LAM

Summary: 
Genie Worksheet Design Principles

Genie Worksheet: Full declarative, specification

Knowledge corpora; Task signatures; Policies
•
What to do under all circumstances
•
What state to keep for the conversation

Genie runtime:

•
Use LLMs to parse user input (with a customized context)

•
Save the conversation state and perform actions
based on the Worksheet

•
Tell LLMs the response to generate (with a customized context)

1. Knowledge

agent

4. Safety

2. Mixed 
initiatives

3. Scale
