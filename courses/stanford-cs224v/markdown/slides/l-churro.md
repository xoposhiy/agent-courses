# VLMs for Transcription

[Course index](../../README.md) · [Original source](https://web.stanford.edu/class/cs224v/lectures_2026/l-churro.pdf) · [Raw file](../../raw/slides/l-churro.pdf)

Retrieved: 2026-11-13T16:49:47.521415+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

Stanford CS224v Course

Conversational Virtual Assistants with Deep Learning

Lecture 10

Vision-Language Models

to Make Historical Documents Accessible

1

Sina Semnani & Monica Lam

## Page 2

Thousands of Years of Cultural Heritage

2

## Page 3

It Can Take Years Just to Read One Language

3

Knowledge of at least two years of modern 
Turkish is required to study Ottoman. 
Knowledge of Arabic and/or Persian is a great 
asset. First-year Ottoman Turkish offers an 
introduction to the usage of the Arabic script in 
Ottoman and relevant facts of Arabic and Persian 
grammar. Readings are in print, generally with 
examples from the 18th to early 20th 
centuries. … Intensive Ottoman summer 
course at the ANAMED Center of Koç University 
in Istanbul.

Osman Aga of Temesvar, Die Autobiographie des Dolmetschers Osman Aga aus Temeschwar, ed. R. F. Kreutel, The E. J. W. Gibb Memorial 
Trust, Cambridge, 1980.

## Page 4

Many Historical Document Digitization Projects

But without text extraction, they are unsearchable and unreadable

4
Library of Congress, Newspapers Collection Overview, Library of Congress, 2025.
British Library, Endangered Archives Programme, British Library, 2025.

173 million items

Over 16 million images

## Page 5

Transformation of 
mainstream narratives with 
historic evidence

Some examples from our colleagues

1
1842 – 1948
Hong Kong
Chinese and English newspapers since it became a British colony

2
1859 – 1861
Italy
Italian founding papers of unification

3
1884 – 1960s
West Africa
English newspapers on life not captured by history written by colonists

4
1895 – 1952
South Africa
Erased indigenous heritage: Khoi and San place names

5
1909 – 1979
California
Eugenic violence: forced sterilization of people with disabilities

6
1950s – 1970s
Caribbean
Operation Legacy: Destruction of British colonial records

7
1986
Ukraine
Documents from Chernobyl (recently destroyed by drones)

## Page 6

Text Extraction: 
The Gateway to AI-Driven Knowledge Access

6

Archives

Text 
Extraction

Text Search

Chat

Pre-writing

Translation

Entity Linking

## Page 7

P REV IO U S W O RK

## Page 8

Existing Document Datasets

CC-OCR
PubLayNet

MMT-Bench
OCRBench

8

Zhong et al., PubLayNet: largest dataset ever for document layout analysis, ICDAR, 2019.
Liu et al., OCRBench: On the Hidden Mystery of OCR in Large Multimodal Models, arXiv, 2024.
Yang et al., CC-OCR: A Comprehensive and Challenging OCR Benchmark for Evaluating Large Multimodal Models in Literacy, arXiv, 2024.
Ying et al., MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI, ICML, 2024.

## Page 9

Performance of Flagship Models on Churro-DS

58.4

49.7

45.3

48.8

52.9

46.8

45.6

40

45

50

55

60

September-2024
December-2024
March-2025
June-2025
August-2025

Anthropic

OpenAI

9

LLMs Regress on Tasks Not Tracked by Model Developers

## Page 10

Text Extraction from Historical 
Corpora Is Challenging

Classic approach

• Manually annotate:

• Text region boundaries
• Text inside each region

• Reading order between text regions

• Train a custom neural model

• Repeat for every new corpus

Major bottleneck

• Many historical datasets lack fine-grained 
annotations

• Many languages have no annotated datasets at all

## Page 11

Summary

• Tons of “digitized” material – they are just images
• Many years of work to understand old text
• AI can make all this material easily accessible:
• Read, search, translate, summarize, analyze, discover new insights
• Existing AI-based OCR tools need fine-grain annotations
• Not enough training data

11

## Page 12

K EY I D EA

S O UR CE O F VA LUA BLE D AT A:

Scholarly publications on history have page-level transcriptions!

## Page 13

Recent Breakthroughs in VLMs

13

Dosovitskiy et al., An Image is Worth 16X16 Words: Transformers for Image Recognition at Scale, ICLR 2021.
Dehghani et al., Patch n’ Pack: NaViT, a Vision Transformer for any Aspect Ratio and Resolution, NeurIPS 2023.
Wang et al., Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution, arXiv 2024.
Bai et al., Qwen2.5-VL Technical Report, arXiv 2025
Poznanski et al., olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models, arXiv 2025.

Vision transformer \[Dosovitskiy et al., 2021\]

•
224 x 224 pixel inputs

Dynamic resolution \[Dehghani et al., 2023\]

•
Qwen 2 VL \[Wang et al., 2024\]

•
A pretrained VLM with dynamic resolution

Shift towards page-level OCR models:

•
CHURRO VLM \[Semnani, 2025\]

•
Qwen 2.5 VL \[Bai et al., 2025\]

•
OlmOCR \[Poznanski et al., 2025\]

## Page 14

In EMNLP 2025

CHURRO: Collection of Historical Unified Resources for Robust OCR

## Page 15

L EC T UR E G O AL


CHURR O: A G RA SS-R O OT M O VEMEN T T O

M A KE W O RLD H IS TO RY R E ADA BLE

Original Document

Vision Language Model (VLM)

Whole document in HDML
Historical Document Markup Language

3. Churro VLM: Train an Open-Weight VLM

1. Design of HDML

2. Churro DS:    An Open, Academic Historical Corpus

## Page 16

Remove Fine-Grained Annotation Requirements

• Use Vision Language Models (VLMs) for full-page OCR
• No manual annotation of text regions required

16

V

die durch meine Phantasie zogen und sie beleb-
ten, als das stille Volk betrachten, das einst
die einsamen Vesten Deutschlands durchwandel-
ten, und Freude mir, wenn diese Gebilde ihnen
nicht ganz unlieblich erscheinen.

Wie die Lust an Mährchen sich in mir
entwickelte, oder die Geschichte der
Entstehung dieses Büchleins.

Meinen Eltern geboren, um sie einiger-
maßen über den Tod eines innigst und höchst ge-
liebten Töchterleins, der wenige Zeit nach mei-
ner Geburt erfolgte, zu trösten, mit der ich
zugleich alle jüngern Geschwister verlor, gingen
meine ersten Entwickelungsjahre einsam hin.
Das Kind fühlt dies noch nicht, die nährende
Amme, die mit ihm tändelnden und scherzenden
Eltern sind ihm genug. Aber schon um mein
drittes Jahr erinnere ich mich einer großen
Sehnsucht nach einem Gefährten und Gespielen,
und wohl weiß ich noch die Freude, die ich
hatte, als mir ein Brüderlein geboren ward.

Example 1

VLM

## Page 17

Example 2

17

Einzelne Zeitungsseite, 
Illustrierte Kronen-Zeitung vom 1. 
Juli 1933, Seite 10.

Full-page Extraction with Meta Data
Full Extracted Text: here

### Page links

- [Link 1](https://suif.stanford.edu/~lam/Churro-Annotation.xml)

## Page 18

Representation of the Text Extraction Result
(OCR-Oriented)

• Proposed Specifically for OCR:
• ALTO: Analyzed Layout and Text Object XML Schema by Library of Congress
• PAGE: Page Analysis and Ground Truth Elements
• DocTags Markup by IBM research
• QwenVL HTML by Qwen Team, Alibaba Group
• Limitations:
• Represent the location of elements on the page 
without specifying their semantics or relationship
• Have tons of optional syntax that are not used in practice
• Do not account for “Gaps”, “Marginal notes”… that can impact the meaning of the content

18

## Page 19

Representation of the Text Extraction Result
(Scholar Oriented)

• TEI (Text Encoding Initiative)
• Widely used by libraries and archives, but not OCR systems
• 500+ concepts
• Multiple ways to encode the same page
• Permits arbitrarily deep nesting
• No native support for elements like Header, Footer, Margin

19

## Page 20

A New HDML
(Historical Document Markup Language)

Design Goal: Suitable for training page-level text extraction systems

• Represent the whole document and nothing but the document

• Capture key information for downstream AI tasks

• Information available in many corpora -- No manual annotation needed

• Unique representation for training efficiency

Design: Refined from TEI

• A subset of TEI (45 concepts): Header, PageNumber, MarginalNote, Paragraph ...

• Provides a rough layout order -- no physical coordinate information

20

HDML: an abstract representation that enables automation

– a classical example of CS contributions

## Page 21

Metadata

21

## Page 22

Table

22

## Page 23

Headings

23

## Page 24

Math!

24

## Page 25

Marginal Notes

25

## Page 26

Interlinear Notes and Catchword

26

## Page 27

Decorations and Musical Notation

27

## Page 28

Figures

28

## Page 29

Stamps and Seals

29

## Page 30

Deletion and Addition

30

## Page 31

Damages and Gaps

31

## Page 32

L EC T UR E G O AL


CHURR O: A G RA SS-R O OT M O VEMEN T T O

M A KE W O RLD H IS TO RY R E ADA BLE

Original Document

Vision Language Model (VLM)

Whole document in HDML
Historical Document Markup Language

3. Churro VLM: Train an Open-Weight VLM

1. Design of HDML

2. Churro DS:    An Open, Academic Historical Corpus

## Page 33

STANFORD
LAM

CHURRO Dataset: A Human-Annotated Full-Page 
Historical Document Dataset

## Page 34

Sources of CHURRO Dataset

Restrictive License

Not Convertible to Full-Page

Not Historical

Inaccessible

Machine Labels

• Zenodo

• GitHub

• Universities

• Libraries

• Books

34

~2 TB of data

155 corpora
Tens of custom data 
formats

Zenodo: Open repository for EU-funded research outputs from 
Horizon Europe, Euratom and earlier Framework Programmes.

Sources

## Page 35

CHURRO-DS Spans 22 Centuries

Zenon or Zeno (3rd century BC) was a public 
official in Ptolemaic Egypt around the 250s–230s 
BC.

Personal letter written in Arabic. The letter is 
dated October 17, 1960, from Lebanon. The 
sender, Malvina from Dhour El Choueir, writes to 
her niece Ajni Jbeili.

Ground-Truthed Data Set of Zenon Papyri for Handwritten Text Recognition. Isabelle et al. Zenodo. 2022
Muharaf: Manuscripts of Handwritten Arabic Dataset for Cursive Text Recognition. Saeed et al. NeurIPS Datasets. 2024.

35

## Page 36

CHURRO Contains 46 Language Clusters

German
Middle High German

Low German
Old High German

Swiss German

36
ISO 639-3: Language Coding Agency, 2007.

## Page 37

STANFORD
LAM

Distribution of Languages

Print (32 Languages)

German
French
Spanish
Latin
Czech
Dutch

Polish
Slovenian
English
Japanese
Bulgarian
Sanskrit

Finnish
Swedish
Romanian
Hindi
Bangla
Chinese

Italian
Serbian
Malayalam
Slovak
Estonian
Latvian

Sorbian
Indonesian
Corsican
Portuguese
Catalan
Greek

Russian
Slavic
Occitan
Yiddish
Hungarian
Malay

Javanese
Croatian

Handwriting (28 Languages)

Chinese
Spanish
French
English
Dutch
German

Arabic
Latin
Japanese
Khmer
Swedish
Italian

Norwegian
Greek
Vietnamese
Persian
Sanskrit
Turkish

Hebrew
Catalan
Portuguese
Czech
Newari
Finnish

Pali
Russian
Danish
Yiddish

## Page 38

STANFORD
LAM

CHURRO-DS: Summary

•
Unified 150 existing datasets, 100K manuscripts and prints, 3 writing 
directions
•
22 centuries: 3rd century BC to 20th century AD
•
Page-level annotation with a standardized metadata schema in our HDML
•
Macrolanguage classification: ISO 639-3 (Agency, 2007)
•
Script classification: 
•
ISO 14924 (International Organization for Standardization, 2002)
•
Glottolog
•
Reading order: ALTO XML (library of Congress, 2025), PAGE XML
•
Faithfulness: Diplomatic transcriptions

## Page 39

Distribution of Corpus Sizes

39

## Page 40

CHURRO Dataset Splits

Handwritten Documents
Printed Documents

Train: 98,131

Validation: 1,170
             Test: 1,170

40

## Page 41

L EC T UR E G O AL


CHURR O: A G RA SS-R O OT M O VEMEN T T O

M A KE W O RLD H IS TO RY R E ADA BLE

Original Document

Vision Language Model (VLM)

Whole document in HDML
Historical Document Markup Language

3. Churro VLM: Train an Open-Weight VLM

1. Design of HDML

2. Churro DS:    An Open, Academic Historical Corpus

## Page 42

CHURRO VLM: 
A Vision–Language Model 
for Reading Historical Documents

Fine-tuned on CHURRO-DS from 3B-parameter Qwen VL 2.5 model

42
Bai et al., Qwen2.5-VL Technical Report, arXiv, 2025.

## Page 43

Experimental Setup

• Benchmark 32 VLMs and OCR systems in a zero-shot setting

• Accuracy Metric: Mormalized Levenstein similarity score

1 −(𝑐ℎ𝑎𝑟𝑎𝑐𝑡𝑒𝑟 𝑙𝑒𝑣𝑒𝑙 𝑒𝑑𝑖𝑡 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒)

• Normalized to lie within \[0, 1\]
• Evaluated against the gold transcription

43

## Page 44

Results

44

From left to right: Bangla, Bulgarian, Czech, German, English, Finnish, French, Hindi, Japanese, 
Latin, Dutch, Polish, Romanian, Sanskrit, Slovenian, Spanish, Swedish, Chinese

## Page 45

45
From left to right: Bangla, Bulgarian, Czech, German, English, Finnish, French, Hindi, Japanese, 
Latin, Dutch, Polish, Romanian, Sanskrit, Slovenian, Spanish, Swedish, Chinese

Results

## Page 46

Summary of Results for Printed Documents

80.9

71.9
72.7

67.8

82.3

50

60

70

80

90

Average

Normalized Edit Distance

Gemini 2.5 Pro
Azure OCR
NuMarkdown (8B)
Qwen VL 2.5 (3B)
Churro (3B)

14.5

46

## Page 47

Summary of Results for Handwritten 
Documents

63.6

47.7

51.2

42.9

70.1

30

40

50

60

70

80

Average

Normalized Edit Distance

Gemini 2.5 Pro
Azure OCR
NuMarkdown
Qwen VL 2.5 (3B)
Churro (3B)

27.2

47

## Page 48

Summary of Per-Language Results

• Handwriting accuracy is 80%+ in:
• Catalan, Dutch, English, French, German, Italian, Swedish

• Print accuracy is 90%+ in:
• Bulgarian, Czech, Dutch, English, Hindi, Latin, Sanskrit, Slovenian, 
Spanish

48

## Page 49

49

15.5× cheaper
4.1% better

The Accuracy-Cost Trade-off

## Page 50

W H AT SH OU LD WE D O N EXT?

## Page 51

51

## Page 52

Three College Courses Have Used History Genie
to Teach History with Authentic Sources

Research into
entirely new topics
that have previously been

missed by historical

researchers

Scholarship that
adds African perspectives

to modify existing 
understandings of such topics

Research that
provides new insights

into existing theme

Example: The execution of a 
Sierra Leonean leader named 
Whobay and subsequent 
protests.

Example: the impact of the 
industrialization of agriculture in 
Liberia or attempts to set up 
independent states on the coast 
of Ghana.

Example: Nineteenth century 
Zionism, anti-slavery movements, 
and the abolition of alcohol.

Stanford University

• AFRICAAM 240 Knowledge Outside the 
Colonial Library

San Francisco State University

• HISTORY 366 and Anthropology 609 
Approaches to the African Pasts

• HISTORY 305 AI and Historical Inquiry

52

Trevor Getz

Professor of 
African and World History at 
San Francisco State University

President
World History Association

## Page 53

Historians Have Used History Genie to 
Discover New Evidence

My aim was to center local sources, but it was difficult to achieve that 
until you shared History Genie with me.

History Genie allowed me to complement dairies and narratives by 
British military men with those authored in the African Times by West 
Africans who lived along the Atlantic Coast.

Tony Yeboah
Assistant Professor of

African Art History

Tulane University

Benjamin Wendorf
Professor of History
Quinsigamond Community College

The History Genie tool was immensely helpful in what otherwise would 
have been a lengthy process of reading entirely through each edition of 
these newspapers to find relevant material.

53

## Page 54

A Grass-Root Movement to
            Make Historical Documents Accessible

• CHURRO-DS dataset with a new HDML language
• 99,491 pages
• 22 centuries
• 46 language clusters
• Handwriting and print
• CHURRO-VLM: a compact open-weight vision-language model
• Comparable to state-of-the-art commercial system  (Gemini 2.5 Pro)
• 15.5x cheaper
• HistoryGenie: AI assistant for historical documents

54
Semnani et al., CHURRO: Making History Readable with an Open-Weight Large Vision-Language Model for High-Accuracy, Low-Cost 
Historical Text Recognition, EMNLP, 2025.
