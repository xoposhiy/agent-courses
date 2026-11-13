# Lang2LTL: Translating Natural Language Commands to Temporal Specification with Large Language Models

[Course index](../../README.md) · [Original source](https://openreview.net/references/pdf?id=fuEQkAYpTi) · [Raw file](../../raw/readings/lang2ltl.pdf)

Retrieved: 2026-11-13T16:52:31.363921+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Lang2LTL: Translating Natural Language
Commands to Temporal Specification with Large
Language Models

Anonymous Author(s)
Affiliation
Address
email

Abstract: Robotic systems interacting with humans through natural language
1

must adequately represent a wide range of challenging tasks. Linear temporal
2

logic (LTL) has become a prevalent specification language to represent challeng-
3

ing non-Markovian tasks, such as completing subtasks in a specific order and
4

repetitive task execution. In this work, we frame the problem of grounding natural
5

language commands to an LTL expression as a neural machine translation prob-
6

lem, leveraging the capabilities of pre-trained large language models (LLMs). A
7

key challenge for translation tasks is the collection of a large corpus of paired lan-
8

guage and translated specifications. LLMs have demonstrated few-shot learning
9

capabilities in many natural language tasks and can be used to overcome data-
10

complexity challenges. We propose Lang2LTL, a new model architecture for
11

translating natural language commands to LTL specifications. Results in naviga-
12

tion domains show that our modular approach outperforms our end-to-end base-
13

lines in translation accuracy and is more sample efficient than the encoder-decoder
14

baseline at generalization across environments.
15

Keywords: Robots, Language, Linear Temporal Logic
16

1
Introduction
17

Commanding robotic systems through natural language represents a promising interaction modality
18

for taskable multi-purpose robotic systems in the future. For example, human users can command
19

an autonomous drone to always avoid certain air spaces while visiting a sequence of landmarks in
20

a specific order and ask a robot to repetitively patrol regions of a school campus. Linear temporal
21

logic (LTL) \[1\] is a widely used specification language that can express a range of challenging non-
22

Markovian tasks, such as completing subtasks in a specific order, defining avoidance states, and
23

repetitive task execution. This work proposes to ground natural language commands given to a
24

robot to LTL expressions which serve as a task specification for downstream planning and learning
25

algorithms. Following prior works \[2, 3\], we model this grounding procedure as a neural machine
26

translation problem.
27

Existing methods \[2, 3\] using RNN encoder-decoder models for translation are only applicable
28

within the environment the model was trained on and require retraining in every new environment.
29

We take advantage of the recent success of large language models (LLMs) in many natural lan-
30

guage tasks, such as name-entity recognition and machine translation. LLMs are generative models
31

pretrained on a vast amount of data in varied linguistic contexts. We hypothesize that the large
32

pre-trained corpus combined with a modular approach to deploying LLMs can outperform narrow
33

environment-specific translation models developed in prior work in terms of sample efficiency and
34

generalization ability. The key advantage of deploying pre-trained LLMs for command translation
35

Submitted to the 6th Conference on Robot Learning (CoRL 2022). Do not distribute.

## Page 2

is its ability to transfer to a wide range of domains utilizing similar task descriptions, for example,
36

navigation at multiple scales ranging from a single house to city-wide.
37

We examined three approaches for translating natural language commands to LTL specifications
38

with varying levels of inductive bias and structure built into the model architecture. We propose de-
39

composition of translation problem into subtasks, namely name-entity recognition (NER), ground-
40

ing, and translation, where name entities in language commands are replaced by placeholder sym-
41

bols during translation, and tested such a modular approach where each task is solved separately.
42

We also propose two variants of the modular approach. In the first variant, the LLM is first called
43

to solve the NER, and the grounding task. The model then translates the natural language command
44

into LTL specification without explicitly replacing named entities in the commands with the place-
45

holders. In the second variant the LLM is directly prompted to translate the input natural language
46

command into an LTL formula without explicitly solving any of the subtasks. Results in navigation
47

domains show that our modular approach outperforms our end-to-end baseline in translation accu-
48

racy and is more sample efficient across environments than a previously proposed encoder-decoder
49

baseline.
50

2
Preliminaries
51

2.1
Linear Temporal Logic for Task Specification
52

Linear temporal logic (LTL) is a promising alternative to a numerical reward function for express-
53

ing task specifications. An LTL formula φ is a Boolean function that determines whether a given
54

trajectory has satisfied the objective expressed by the formula. Littman et al. \[4\] argue that such task
55

specifications are more natural than numerical reward functions, and they have subsequently been
56

used as a target language for acquiring task specifications in several settings, including from natural
57

language \[3\] and learning from demonstration \[5\]. Formally, an LTL formula is interpreted over
58

traces of Boolean propositions over discrete time, and is defined through the following recursive
59

syntax:
60

φ := α | ¬φ | φ1 ∨φ2 | Xφ | φ1 U φ2
(1)

Here α ∈AP represents a Boolean proposition, mapping a state to a Boolean value; φ, φ1, φ2 are
61

any valid LTL formulas. The operator X (next) is used to define a property Xφ that holds if φ holds
62

at the next time step. The binary operator U (until) is used to specify ordering constraints. The
63

formula φ1 U φ2 holds if φ1 holds until φ2 first holds at a future time instant. The operators ¬ (not)
64

and ∨(or) are identical to propositional logic operators. We also utilize the following abbreviated
65

operators: ∧(and), F (finally or eventually), and G (globally or always). Fφ specifies that the
66

formula φ must hold at least once in the future, while Gφ specifies that φ must always hold in the
67

future.
68

2.2
Prompting with Large Language Models
69

Large language models (LLMs) are large neural networks pretrained on huge text corpora in an
70

unsupervised fashion. LLMs have successfully demonstrated few-shot adaptation on a wide gamut
71

of tasks when framed as a text completion problem \[6\]. Deploying an LLM involves prompting
72

the model with a priming text, followed by the model generating a completion. Generating a well
73

performing prompt involves the largest amount of engineering effort. A successful prompt typically
74

enables in-context learning by providing task descriptions and examples for the model to follow.
75

For instance, the prompt to the LLM for one translation task may start with the task description,
76

“Your task is to translate English utterances into linear temporal logic (LTL) formulas” followed by
77

an example and another English utterance to be translated,
78

2

## Page 3

Utterance: go to A but avoid going through B
LTL: F A ∧G ! B

Utterance: go to A then go to B
LTL:

3
Related Work
79

Prior work proposed using RNN encoder-decoder models to translate natural language commands
80

to LTL expressions \[2, 3, 7\] that require training on a parallel corpus for every environment. Our
81

approaches use LLMs to help generalize across environments. Patel et al. \[3\] introduced a weakly
82

supervised approach where a latent LTL expression is fed into a planner that generates a trajectory to
83

provide training signals. After examining the dataset and the model, we discovered that the interme-
84

diate LTL expressions mostly represent simple sequential tasks. We work on more diverse datasets
85

that cover a wider range of LTL expressions. To improve the generalizability of encoder-decoder
86

models to new environments, Berg et al. \[7\] used CopyNet \[8\] to resolve novel landmark names.
87

However, the performance decreased significantly when there are more than one unseen landmarks.
88

We used LLMs for name-entity recognition which showed better performance at identifying novel
89

landmarks in input utterances.
90

Early works in navigational language grounding focused on utilizing semantic parsers to ground
91

natural language into representations and then into robot actions \[9, 10, 11, 12, 13\]. Mei et al.
92

\[14\] introduced a Bi-LSTM model that directly translated instructions into low-level actions. Fried
93

et al. \[15\] applied pragmatic inference to further improve the performance. Neural end-to-end meth-
94

ods require the input utterance to be descriptive of low-level actions. In contrast, LTL expressions
95

can model high-level language instructions describing complex robot behaviors and provide safety
96

guarantees.
97

4
Translating Natural Language to LTL Specification
98

Consider a natural language command such as “The robot has to go to the cafe on Main street, then
99

stop by a bank, then go to McDonald’s, but only after visiting the bank”, and a set of landmarks
100

{Starbucks, Chase, McDonald, ...} as propositions for constructing a valid LTL expression. The
101

desired LTL formula of this command can be expressed as follows:
102

φ = F (Starbucks ∧F Chase) ∧F McDonalds ∧¬McDonalds U Chase
(2)

We decompose such translation of language to LTL specifications into the following subproblems:
103

1. Identification of substrings referring to Boolean propositions, in this case, “the cafe on
104

Main street”, “McDonald’s” and “bank”, but not “the robot”.
105

2. Grounding referring substrings to environment propositions, i.e., knowing that the phrases
106

“the cafe on Main street”, “the bank” and “McDonald’s” refer to the pre-defined environ-
107

ment propositions Starbucks, Chase, McDonalds.
108

3. Translating the input instruction into the LTL formula and simultaneously swapping the
109

identified substrings into corresponding environment propositions.
110

In this section, we propose a modularized pipeline with pretrained large language models for tackling
111

each of these subproblems and completing the translation of natural language to LTL specifications
112

for the robotic system in the context of navigation, where the language propositions are grounded to
113

known landmarks within the task environment.
114

3

## Page 4

We hypothesize that this task decomposition should produce a higher translation accuracy as com-
115

pared to an approach that translates an input utterance directly into an LTL formula through a single
116

prompt completion problem given to an LLM.
117

Figure 1: Lang2LTL-Modular Approach: Green blocks are pretrained or off-the-shelf models. Yel-
low blocks are input or output data of each module.

4.1
Name-Entity Recognition for Landmarks
118

In order to extract word sequences from given utterances, we add a name-entity recognition (NER)
119

module based on a separate call to a pretrained LLM. Moreover, the task here is dissimilar to the
120

typical NER task where all name entities are extracted and labeled. Instead, an NER module in our
121

proposed pipeline must only output name entities with the required type as mentioned previously,
122

and include informative words into each entity, e.g., “the cafe on Main street” rather than “the cafe”
123

and “Main street”.
124

The former can be solved by only selecting entities with location labels, while the latter is generally
125

challenging to all existing pretrained NER models, especially without adequate examples for fine-
126

tuning. We demonstrate high performance on the latter task by adapting the GPT-3 prompt with task
127

description and examples to enable in-context learning. An example prompt is shown as follows,
128

Your task is to repeat exact strings that refer to landmarks from the given utterance.

Utterance: go to the bank then go to the restaurant
Landmarks: the bank; the restaurant

Utterance: go to the cafe on Main street, then a bank, then McDonald’s
Landmarks:

4.2
Grounding Name Entities to Environment Propositions
129

Due to the diversity of natural language, a single landmark can be referred to using multiple ex-
130

pressions. Grounding these expressions to the correct propositions is challenging. We approach
131

this by labeling propositions with unique identifying language token. The problem of grounding
132

expressions to propositions is then equivalent to mapping the expression to the most similar token.
133

We propose leveraging the latent embeddings computed by LLM encoders as the metric space for
134

measuring similarity. Following Berg et al. \[7\], we match the referring expressions to the proposition
135

tokens by matching their respective embeddings using the cosine similarity metric. This approach
136

enables us to handle a variety of referring expressions, as the entire substring, e.g., attributes such
137

4

## Page 5

as “building” and “facility” or physical addresses such as “99 Main street”, are transformed into the
138

latent embedding by the LLM encoder.
139

4.3
Abstract Translation with Placeholders
140

A straight-forward way of translating natural language to LTL is to treat the language utterances as
141

input and target LTLs as output. However, language generation is inherently difficult partly due to
142

the large size of the target vocabulary, and generating language with strict syntactical restrictions
143

heavy the burden. Even if LLMs are capable of performing in-context generation tasks, having a
144

larger vocabulary can significantly deteriorate the translation performance.
145

In our modular approach, we add a translation module that replaces all the landmarks in a grounded
146

language command with placeholder tokens (for example, letters of an alphabet). A separate call to
147

the LLM with a prompt, including examples of commands and corresponding LTL formulas with the
148

placeholders, is used to obtain the structure of the output LTL formula. An example of such prompt
149

is shown in Section 2.2. Finally, the mapping from placeholder propositions to the substrings and
150

the mapping from substrings to the environment propositions are used to transform the output LTL
151

formula into the requisite output.
152

4.4
Proposed Lang2LTL model architectures
153

Our proposed modular approach, Modular-NER+Placeholders, is shown in Figure 1. The NER
154

module takes natural language utterance as input and output identified landmark entities, and then the
155

grounding module grounds each entity into a proposition, and then the translation module performs
156

abstract translation with the placeholder map built on landmark entities and generates the grounded
157

LTL expression as the final output.
158

We hypothesize that the key benefit of our modular approach is the decoupling of the problem of
159

proposition recognition from the formula structure translation, thus allowing the language model to
160

operate over a wide variety of LTL formula templates.
161

In addition to the modular approach, we also present two approaches in which the model makes a
162

trade-off between inductive bias and generalization:
163

1. Naive Translation is a modular approach with a module that directly translates utterances
164

with environmental propositions to final LTLs. This approach is proposed for evaluating
165

the influence of abstract translation with placeholders, and it demands three calls to an
166

LLM, the same as the modular approach. We refer to this approach as Modular-NER in
167

subsequent sections.
168

2. End-to-End Approach takes as input a natural language command and a list of known
169

landmarks situated in the environment and produces the corresponding LTL expression
170

where the propositions are grounded to known landmarks. The approach translates the
171

language commands into an LTL specification with a single call to an LLM. We refer to
172

this approach as End-to-End in subsequent sections.
173

5
Experiments
174

Our experiments are aimed to evaluate the following hypotheses:
175

• H1: A modular approach performs better than an end-to-end approach at translating natural
176

language to LTL specification.
177

• H2: A modular approach combined with LLMs is better than an RNN encoder-decoder
178

model at generalizing across different domains that share similar task descriptions.
179

A number of per-trained language models can be used for each module, e.g., BERT \[16\] and GPT-
180

3 \[17\]. We chose GPT-3 because it is one of the largest language models that was pretrained on a
181

5

## Page 6

vast amount of data in varied linguistic contexts, and it has shown state-of-the-art performance in
182

many natural language tasks.
183

5.1
Cleanup World Dataset
184

We evaluated the three Lang2LTL approaches on a subset of an annotated corpus of natural language
185

commands paired with LTL expressions collected by Gopalan et al. \[2\]. The task environment,
186

first introduced in \[18\], is partitioned into distinctly colored rooms, and the language commands
187

instruct a robot to move through rooms in a specific order while possibly avoiding certain rooms.
188

We chose this dataset as our test set because of the diverse natural language commands and LTL
189

types compared to similar datasets from other prior work. Our test set contains 697 natural language
190

commands corresponding to 14 unique LTL expressions in 4 different types. Some example pairs of
191

language instructions and LTL expressions are shown in Table 2.
192

5.2
OpenStreetMap Dataset
193

To evaluate the generalization capability of our approaches that use LLMs, we randomly sampled 50
194

data points of similar task descriptions from the OpenStreetMap (OSM) dataset presented in \[19\].
195

With the same model architecture and prompts, we hypothesize that the LLM approach can achieve
196

better translation accuracy on the OSM dataset than the baseline RNN encoder-decoder method.
197

This test set consists of 48 unique LTL expressions in 4 different types, one of which is not presented
198

in the prompt to the translation module. The language commands contain a diverse number of
199

landmark names, which increases the difficulty of translation. Some example pairs of language
200

instructions and LTL expressions are shown in Table 4.
201

5.3
Evaluation
202

To evaluate the performance of different approaches, we compare the output LTL expression with the
203

ground truth one, and report an accuracy as the percentage of the test data that the two expressions
204

are a match. We use Spot library \[20\] to test the logical equivalence of the two LTL expressions and
205

the syntax of the output LTL expressions. Spot does the equivalence check by first converting the
206

output and ground truth LTL formulas f and g and their negation into four automata Af, A¬f, Ag
207

and A¬g, then evaluating if that the multiplicative conjunctions Af ⊗A¬g and A¬f ⊗Ag are empty.
208

6
Results and Discussion
209

The accuracy of Modular-NER+Placeholders approach on the Cleanup World dataset is 84.10%,
210

significantly higher that of Modular-NER (75.50%) and End-to-End (78.65%). The results show
211

that building inductive bias into the system pipeline helps improve translation performance, and
212

the choice of inductive biases are important, thus supporting H1. Some examples of successful
213

and failed translations of the Modular-NER+Placeholders model on the Cleanup World dataset are
214

shown in Table 2 and 3, respectively.
215

Table 1: Summary of Model Accuracies

Model
Accuracy
End-to-End
78.65%
Modular-NER
75.50%
Modular-NER+Placeholders
84.10%

Next, we evaluated the Modular-NER+Placeholders system using GPT-3 on the OSM dataset, and
216

got a 72% translation accuracy. Some examples of successful and failed translations of the Modular-
217

NER+Placeholders model on the OSM dataset are shown in Table 4 and 5, respectively. Given that
218

the baseline RNN encoder-decoder model \[2\] was only trained on the Cleanup World dataset, its
219

6

## Page 7

Table 2: Examples Successful Translations in Cleanup World

Input Natural Language Command
Output and Ground Truth LTL Expression
move to the red room
F red room
go through blue room to green room
∧F blue room F green room
go to the blue room but avoid the red room
∧F blue room G ! red room
go through red or yellow to get to green
F ∧∨red room yellow room F green room

Table 3: Examples Failed Translations in Cleanup World

Input Natural Language Command
Ground Truth LTL Expression
Output LTL Expression

move to the red room and stop after entering
F red room
F ∧red room X

go to the blue room via the green room
F ∧green room F blue room
F ∧∨green room F blue room
go from the blue room to the red room
F ∧red room F green room
and then go from the red room to the green room
F ∧blue room F red room ∧F green room

enter the blue room without crossing the red room
∧F blue room G ! red room
F ∧blue room G ! red room

Table 4: Examples Successful Translations in OSM

Input Natural Language Command
Output and Ground Truth LTL Expression
find science library
F science library
go to fedex office and then go to cvs
F ∧fedex office F cvs
stay away from main st and find chipotle
∧G ! main st F chipotle
stay on main st and find bookstore
∧F bookstore G main st

Table 5: Examples Failed Translations in OSM

Input Natural Language Command
Ground Truth LTL Expression
Output LTL Expression

find bookstore and then find fedex office
F ∧bookstore F fedex office
∧F bookstore GF fedex office

go to citizens bank and then go to marston hall
F ∧citizens bank F marston hall
F citizens bank F marston hall

do not leave main st and find science library
∧G main st F science library
∧G ! main st F science library

transfer ability to the OSM dataset is limited because the OSM contains more diverse language
220

commands with a completely different set of named entities. This result supports H2.
221

We note that a large number of errors was due to the invalid syntax of the output LTL expressions,
222

which shows the limited ability of GPT-3 to master LTL grammar with few-shot prompts. In ad-
223

dition, GPT-3 tends not to understand negation well, e.g., the translation of “go through the room
224

which is not red to get to the blue room” is F ∧red room F blue room while the ground truth
225

translation is ∧F blue room G! red room.
226

7
Conclusion & Future Work
227

We introduced Lang2LTL, a novel model architecture that translates natural language commands
228

with temporal specifications to LTL expressions, and showed that decomposing this task into sub-
229

tasks and using an LLM for each module performs better than end-to-end approaches. We demon-
230

strated the ability of LLM approaches to generalize across domains without retraining on parallel
231

corpora. Lang2LTL enables human users to interact with robots via natural language commands
232

containing complex temporal specifications.
233

7

## Page 8

For future work, there are several fruitful directions to explore: (1). Handling longer LTL specifi-
234

cation generation tasks is beneficial to implementations in real scenarios, and could be potentially
235

realized by further task decomposition with LLMs. (2). Resolving ambiguity in natural language,
236

e.g., does “Go to the red room and then to the blue room” restrict the agent not to visit the blue room
237

before reaching the red room? (3). In robotic applications, LTL formulas can be used to specify
238

tasks for a planner, and the learned policy is executed on a real robot.
239

8

## Page 9

References
240

\[1\] A. Pnueli. The temporal logic of programs. In 18th Annual Symposium on Foundations of
241

Computer Science (sfcs 1977), pages 46–57. ieee, 1977.
242

\[2\] N. Gopalan, D. Arumugam, L. Wong, and S. Tellex. Sequence-to-Sequence Language Ground-
243

ing of Non-Markovian Task Specifications. In Proceedings of Robotics: Science and Systems,
244

Pittsburgh, Pennsylvania, 2018. doi:10.15607/RSS.2018.XIV.067.
245

\[3\] R. Patel, E. Pavlick, and S. Tellex. Grounding language to non-markovian tasks with no super-
246

vision of task specifications. In Robotics: Science and Systems, 2020.
247

\[4\] M. L. Littman, U. Topcu, J. Fu, C. Isbell, M. Wen, and J. MacGlashan.
Environment-
248

independent task specifications via gltl. arXiv preprint arXiv:1704.04341, 2017.
249

\[5\] A. Shah, P. Kamath, J. A. Shah, and S. Li. Bayesian inference of temporal task specifications
250

from demonstrations. Advances in Neural Information Processing Systems, 31, 2018.
251

\[6\] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan,
252

P. Shyam, G. Sastry, A. Askell, et al. Language models are few-shot learners. Advances
253

in neural information processing systems, 33:1877–1901, 2020.
254

\[7\] M. Berg, D. Bayazit, R. Mathew, A. Rotter-Aboyoun, E. Pavlick, and S. Tellex. Grounding
255

Language to Landmarks in Arbitrary Outdoor Environments. In IEEE International Confer-
256

ence on Robotics and Automation (ICRA), 2020.
257

\[8\] J. Gu, Z. Lu, H. Li, and V. O. Li.
Incorporating copying mechanism in sequence-to-
258

sequence learning. In Proceedings of the 54th Annual Meeting of the Association for Com-
259

putational Linguistics (Volume 1: Long Papers), pages 1631–1640, Berlin, Germany, Aug.
260

2016. Association for Computational Linguistics. doi:10.18653/v1/P16-1154. URL https:
261

//aclanthology.org/P16-1154.
262

\[9\] M. Macmahon. Marco: A modular architecture for following route instructions. AAAI Work-
263

shop - Technical Report, 01 2005.
264

\[10\] M. MacMahon, B. Stankiewicz, and B. Kuipers. Walk the talk: Connecting language, knowl-
265

edge, and action in route instructions. In Proceedings of the 21st National Conference on
266

Artificial Intelligence - Volume 2, AAAI’06, page 1475–1482. AAAI Press, 2006.
ISBN
267

9781577352815.
268

\[11\] Y. Artzi and L. Zettlemoyer. Weakly supervised learning of semantic parsers for mapping
269

instructions to actions. Transactions of the Association for Computational Linguistics, 1:49–
270

62, 2013. doi:10.1162/tacl a 00209. URL https://aclanthology.org/Q13-1005.
271

\[12\] J. Kim and R. Mooney. Unsupervised PCFG induction for grounded language learning with
272

highly ambiguous supervision. In Proceedings of the 2012 Joint Conference on Empirical
273

Methods in Natural Language Processing and Computational Natural Language Learning,
274

pages 433–444, Jeju Island, Korea, July 2012. Association for Computational Linguistics.
275

URL https://aclanthology.org/D12-1040.
276

\[13\] D. L. Chen and R. J. Mooney. Learning to interpret natural language navigation instructions
277

from observations. In Proceedings of the Twenty-Fifth AAAI Conference on Artificial Intelli-
278

gence, AAAI’11, page 859–865. AAAI Press, 2011.
279

\[14\] H. Mei, M. Bansal, and M. R. Walter. Listen, attend, and walk: Neural mapping of navigational
280

instructions to action sequences. In Proceedings of the Thirtieth AAAI Conference on Artificial
281

Intelligence, AAAI’16, page 2772–2778. AAAI Press, 2016.
282

9

### Page links

- [Link 1](http://dx.doi.org/10.1162/tacl_a_00209)
- [Link 2](http://dx.doi.org/10.15607/RSS.2018.XIV.067)
- [Link 3](http://dx.doi.org/10.18653/v1/P16-1154)
- [Link 4](https://aclanthology.org/D12-1040)
- [Link 5](https://aclanthology.org/P16-1154)
- [Link 6](https://aclanthology.org/Q13-1005)

## Page 10

\[15\] D. Fried, J. Andreas, and D. Klein. Unified pragmatic models for generating and following
283

instructions. In Proceedings of the 2018 Conference of the North American Chapter of the As-
284

sociation for Computational Linguistics: Human Language Technologies, Volume 1 (Long Pa-
285

pers), pages 1951–1963, New Orleans, Louisiana, June 2018. Association for Computational
286

Linguistics. doi:10.18653/v1/N18-1177. URL https://aclanthology.org/N18-1177.
287

\[16\] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova.
BERT: Pre-training of deep bidirec-
288

tional transformers for language understanding. In Proceedings of the 2019 Conference of
289

the North American Chapter of the Association for Computational Linguistics: Human Lan-
290

guage Technologies, Volume 1 (Long and Short Papers), pages 4171–4186, Minneapolis, Min-
291

nesota, June 2019. Association for Computational Linguistics. doi:10.18653/v1/N19-1423.
292

URL https://aclanthology.org/N19-1423.
293

\[17\] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan,
294

P. Shyam, G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan,
295

R. Child, A. Ramesh, D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin,
296

S. Gray, B. Chess, J. Clark, C. Berner, S. McCandlish, A. Radford, I. Sutskever, and
297

D. Amodei. Language models are few-shot learners. In H. Larochelle, M. Ranzato, R. Had-
298

sell, M. Balcan, and H. Lin, editors, Advances in Neural Information Processing Systems,
299

volume 33, pages 1877–1901. Curran Associates, Inc., 2020. URL https://proceedings.
300

neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.
301

\[18\] J. MacGlashan, M. Babes-Vroman, M. desJardins, M. Littman, S. Muresan, S. Squire,
302

S. Tellex, D. Arumugam, and L. Yang. Grounding English Commands to Reward Functions.
303

In Robotics: Science and Systems, 2015.
304

\[19\] J. Liu, E. Rosen, S. Zheng, S. Tellex, and G. Konidaris. Leveraging temporal structure in
305

safety-critical task specifications for pomdp planning. 2021.
306

\[20\] A. Duret-Lutz, A. Lewkowicz, A. Fauchille, T. Michaud, E. Renault, and L. Xu. Spot 2.0 —
307

a framework for LTL and ω-automata manipulation. In Automated Technology for Verification
308

and Analysis, 2016.
309

10

### Page links

- [Link 1](http://dx.doi.org/10.18653/v1/N18-1177)
- [Link 2](http://dx.doi.org/10.18653/v1/N19-1423)
- [Link 3](https://aclanthology.org/N18-1177)
- [Link 4](https://aclanthology.org/N19-1423)
- [Link 5](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)
