# YAGO3: A Knowledge Base from Multilingual Wikipedias

[Course index](../../README.md) · [Original source](https://asiabiega.github.io/papers/yago3_cidr2015.pdf) · [Raw file](../../raw/readings/yago3-cidr2015.pdf)

Retrieved: 2026-11-13T16:52:33.385923+00:00

> This is a full text extraction, not a summary. Figures and exact mathematical notation may require the original PDF.

## Page 1

YAGO3: A Knowledge Base from Multilingual Wikipedias

Farzaneh Mahdisoltani
Max Planck Institute
for Informatics, Germany
fmahdisoltani@gmail.com

Joanna Biega
Max Planck Institute
for Informatics, Germany
jbiega@mpi-inf.mpg.de

Fabian M. Suchanek
Télécom ParisTech
France
suchanek@enst.fr

ABSTRACT

We present YAGO3, an extension of the YAGO knowledge
base that combines the information from the Wikipedias in
multiple languages.
Our technique fuses the multilingual
information with the English WordNet to build one coher-
ent knowledge base.
We make use of the categories, the
infoboxes, and Wikidata, and learn the meaning of infobox
attributes across languages. We run our method on 10 dif-
ferent languages, and achieve a precision of 95%-100% in
the attribute mapping. Our technique enlarges YAGO by
1m new entities and 7m new facts.

1.
INTRODUCTION
Motivation.
Wikipedia1 is one of the most popular on-
line encyclopedias.
Several projects construct knowledge
bases (KBs) from Wikipedia, with some of the most promi-
nent projects being DBpedia \[4\], Freebase2, and YAGO \[25\].
These KBs contain millions of entities, including people, uni-
versities, cities, organizations, or artworks. These entities
are structured into a taxonomy of classes, where more gen-
eral classes (such as person) subsume more speciﬁc classes
(such as singer). The KBs also contain hundreds of millions
of facts about these entities, such as which person was born
where, which singer sang which song, or which city is located
in which country. Unlike Wikipedia itself, the KBs store this
knowledge in a structured form of subject-predicate-object
triples, which allows one to query it like a database.
So far, most extraction approaches have focused on the
English version of Wikipedia. With 4.5 million articles, it is
the largest Wikipedia. However, there are dozens of other
Wikipedias in diﬀerent languages.
Several of these have
more than a million articles.
If we could tap the knowl-
edge of these Wikipedias, we could gain thousands, if not
millions of new entities and facts – e.g., those entities that
are too local to be described in the English Wikipedia.

1http://wikipedia.org
2http://freebase.com

This
article
is
published
under
a
Creative
Commons
Attribution
License (http://creativecommons.org/licenses/by/3.0/),
which permits distribution and reproduction in any medium as well as
derivative works, provided that you attribute the original work to the au-
thors and CIDR 2015.
7th
Biennial
Conference
on
Innovative
Data
Systems
Research
(CIDR 2015), January 4-7, 2015, Asilomar, California, USA.

This is the treasure that we want to unearth: Our goal
is to construct a KB from the Wikipedias in diﬀerent lan-
guages. Crucially, we want to build not several KBs, but
one coherent fact collection from these diﬀerent sources.
State of the Art and Limitations. Several projects ex-
tract information from multilingual Wikipedias. However,
these projects either build up one KB per language \[4\], fuse
data across diﬀerent Wikipedias without building a central
KB \[23, 27, 22, 6, 1, 28, 14\], or exclude the facts from the
infoboxes \[21, 8, 20, 3\]. The infoboxes contain information
about the article entity in the form of attribute-value pairs,
and are thus a very rich source of knowledge. Despite a lot
of progress on several aspects of multilingual extraction, the
community does not yet have a coherent KB built from the
Wikipedias in diﬀerent languages.
Challenges.
Building a coherent KB from diﬀerent
Wikipedias is not an easy task. The ﬁrst challenge is ex-
tracting knowledge from the infoboxes.
The infobox at-
tributes usually have foreign language names and are not
shared across diﬀerent Wikipedias. Thus, they have to be
mapped to the canonical relations of the central KB. Since
there are thousands of infobox attributes, this is very hard
to achieve. Furthermore, the extraction from Wikipedia is
error-prone, and so the data has to be cleaned in order to be
of use for a central KB. Finally, the challenge is creating a
taxonomy that reaches across diﬀerent languages, and that
integrates entities from all Wikipedias under the same roof.
Contribution.
In this paper, we propose a holistic ap-
proach for the creation of a full-ﬂedged KB on top of
Wikipedias in diﬀerent languages. Our approach maps mul-
tilingual infobox attributes to canonical relations, merges
equivalent entities into canonical entities by help of Wiki-
data, cleans the data, and arranges all entities into a single
taxonomy. The result is YAGO3, the successor of YAGO.
Our key advantage is that we do not align diﬀerent
noisy extractions from diﬀerent Wikipedias, but diﬀerent
Wikipedias with a central clean KB. This yields an approach
that is remarkably simple and elegant. Most notably, it al-
lows us to deduce the infobox mappings for non-English lan-
guages automatically. Our approach works with European
languages as well as with non-European ones, across diﬀer-
ent scripts, and with an accuracy of 95%-100%. We gain 1m
new entities and 7m new facts over the original YAGO.
The rest of this paper is structured as follows. Section 2
discusses related work, and Section 3 introduces preliminar-
ies. Section 4 presents our approach, and Section 5 shows
our experiments and data. Section 6 shows some applica-
tions of the KB, before Section 7 concludes.

### Page links

- [Link 1](http://creativecommons.org/licenses/by/3.0/)
- [Link 2](http://freebase.com)
- [Link 3](http://wikipedia.org)

## Page 2

2.
RELATED WORK
Several works have harvested the multilingual data from
Wikipedia.
Wikidata.
The Wikidata project builds a KB through
crowd sourcing.
The community members add the facts
manually to the KB. So far, Wikidata has gathered 14 mil-
lion entities. However, most entities have only few facts. On
the long run, Wikidata aims to incorporate, consolidate, and
replace the Wikipedia infoboxes, lists, and categories. Thus,
our approach and Wikidata share the same goal of creating
a common multilingual KB. While Wikidata is a community
eﬀort, our approach is automated. We believe that the two
projects can complement each other: Our approach builds
on Wikidata, and we believe that Wikidata could beneﬁt
from our results in return.
DBpedia. The DBpedia project \[4\] has launched KB con-
struction projects for Wikipedias in diﬀerent languages. The
community maps the infobox attributes to a central ontol-
ogy using diﬀerent approaches.
DBpedia’s crowd-sourced
approach has inspired us to aim at an automated approach
to construct a single KB from the Wikipedias. Another ap-
proach uses classiﬁcation to align the DBpedia classes across
diﬀerent Wikipedia languages \[3\]. Their main goal is to as-
sign novel entities to DBpedia classes automatically. How-
ever, they don’t focus on obtaining new facts. Our technique
in contrast, introduces new facts in addition to new enti-
ties. \[14\] presents a method that maps infobox attributes
of diﬀerent Wikipedias automatically to the central DBpe-
dia properties. Our work aims at a holistic integration of
diﬀerent Wikipedias into one uniﬁed knowledge base, which
includes information from the categories, the infoboxes, and
a taxonomy.
Lexical KBs. Several projects \[8, 20, 19, 21\] make use of
the multilingual data in Wikipedia to construct dictionaries
and concept networks. MENTA \[8, 11\] collects entities from
all editions of Wikipedia as well as WordNet into a single co-
herent taxonomic class hierarchy. BabelNet \[21\] is built by
integrating lexicographic and encyclopedic knowledge from
WordNet and Wikipedia.
We share the goal of a uniﬁed
ontology, but want to add to this structure also the consoli-
dated facts from the infoboxes in diﬀerent Wikipedias. This
is an entirely diﬀerent problem.
\[9\] straightens the inter-language links in Wikipedia. This
task has been addressed also by the Wikidata community,
and we make use of the latter.
Cross-Lingual Data Fusion. A large number of works
extract information from Wikipedia (see, e.g., \[17\] for an
overview). Of these, several approaches consolidate infor-
mation across diﬀerent Wikipedias \[23, 27, 22, 6, 1, 28\]. We
also want to align information across Wikipedias, but our
ultimate goal is diﬀerent: Unlike these approaches, we aim
to build a single coherent KB from the Wikipedias, which in-
cludes a taxonomy. This goal comes with its own challenges,
but it also allows simpliﬁcations.
Our infobox alignment
method is considerably simpler, and requires no similarity
functions or machine learning methods. Still, as we show
in our experiments, we achieve precision and recall values
comparable to previous methods. Second, unlike previous
approaches that have been shown to work on 4 or less lan-
guages \[23, 6, 22, 27, 1, 28\], we can show that our method is
robust enough to run across 10 diﬀerent languages, diﬀerent
scripts, and thousands of attributes. In addition, we con-
struct a coherent knowledge base on top of these knowledge

sources.
Ontology Alignment.
A large number of works have
looked into the alignment of entities, relations, and classes
across KBs (see, e.g., \[24, 29\] and references therein for re-
cent works). PARIS \[24\] is a probabilistic approach for the
automatic alignment of ontologies. It aligns instances, rela-
tions and classes by measuring degrees of matchings based
on probability estimates. We show in our experiments that
we achieve comparable precision to this approach in our
alignment of infobox attributes. At the same time, we con-
struct an entire uniﬁed knowledge base on top of the diﬀerent
knowledge sources. This includes a uniﬁed taxonomy, the
resolution of attribute names across 10 diﬀerent languages,
and the insertion of the data into one central schema.

3.
PRELIMINARIES
RDFS. The Resource Description Framework Schema
(RDFS) is a W3C standard for knowledge representation.
It is used in most major KBs. RDFS is based on a set U
of resources. In most applications, the resources are parti-
tioned into instances I, relations R, literals L, and classes
C, with U = I ˙∪R ˙∪L ˙∪C. An instance is any entity of the
world, such as a person, a city, or a movie.
A class (or
type) is a name for a set of instances. The class city, e.g.,
is the name for the set of all instances that are cities. A
relation is a name for a relationship between resources, such
as loves, or livesIn. Every relation r comes with a domain
dom(r) ∈C and a range ran(r) ∈C. A literal is number,
string, or date. Literals usually take the form "string"^^
datatype.
Here, string is the string representation of a
number, date, or other literal. datatype is a resource. For
YAGO, the datatypes behave exactly like classes: Every lit-
eral is considered an instance of its datatype. Usually, in-
stances, classes, and relations are preﬁxed by a namespace.
We omit the namespace in this paper for legibility. In all
of the following, we assume ﬁxed sets U, I, R, L, C. A state-
ment (or fact) is a triple s ∈(U \ L) × R × U, and usually
for most statements s, s ∈I × R × (I ∪L). The statement
says that the ﬁrst component (the subject) stands in the re-
lation given by the second component (the predicate) with
the third component (the object), as in ⟨Elvis, marriedTo,
Priscilla⟩. We use the statement ⟨Elvis, type, singer⟩
to say that
Elvis is an instance of the class singer. We
use ⟨singer, subClassOf, person⟩to say that singer is a
subclass of person. The subClassOf-relationship is transi-
tive. A knowledge base (KB) is set of statements.
Wikipedia. The online encyclopedia Wikipedia is written
by a community of volunteers.
It is available in 287 lan-
guages, and 9 of them have more than 1m articles.
The
English edition currently has 4.5m articles. The articles are
written in the Wiki markup language. Each article usually
describes one concept or entity. Most articles are members
of one or several categories. The article about Elvis Pres-
ley, e.g., is in the categories American baritones, and 1935
births. Furthermore, many articles have an infobox. An in-
fobox is a set of attribute-value pairs with information about
the article entity, such as {birthplace = Tupelo, birth-
date = 8 January 1935, ...}. The infoboxes are grouped
into templates, which often carry the name of the class of the
article entity. For example, the infobox for Elvis belongs to
the template singer. The templates deﬁne which attributes
may be used. However, the templates are not used consis-
tently, and the attributes vary widely across articles.

## Page 3

Wikidata. The Wikidata project aims to be a structured
version of Wikipedia. It is a KB that is fed with facts by
volunteers.
Wikidata provides central abstract identiﬁers
for entities and links them to the articles in the Wikipedias
in diﬀerent languages. For example, Elvis Presley has the
identiﬁer Q303, and has links to the Wikipedia articles in
147 languages. Wikidata provides similar data for infobox
templates and category names.
WordNet.
The online dictionary WordNet \[18\] aims to
cover all words of the English language. WordNet groups
synonymous nouns together into synsets, which can be in-
terpreted as classes.
For example, person and human are
in the same synset, which is the class of people. WordNet
structures the synsets into an subClassOf hierarchy (a tax-
onomy), where, e.g., the synset of people is below the synset
of animals.
YAGO. YAGO \[25, 26\] is a large KB constructed from
Wikipedia and WordNet. In its new version, YAGO 2 \[15,
5\], several new sources were added, including geonames3 and
the Universal WordNet \[10\]. For this paper, we exclude the
newer sources from the construction process, and stay with
WordNet and Wikipedia.
This subset of YAGO contains
3.4m entities, 17m facts, and 77 manually deﬁned relations.
YAGO Architecture. The architecture of the YAGO ex-
traction system \[5\] is based on extractors and themes.
A
theme is a set of facts stored in a ﬁle. An extractor is a
software module, which takes as input a set of themes and
other data, and produces a set of output themes. Extrac-
tors can extract data from Wikipedia, WordNet, or other
sources.
They can also postprocess themes produced by
other extractors, and perform deduplication, veriﬁcation, or
constraint checking.
These dependencies yield a bipartite
graph of themes and extractors, where every extractor is
connected to the themes it consumes and the themes it pro-
duces. A scheduling module calls the extractors in parallel
so that an extractor starts as soon as all its input themes
are available. Figure 1 shows an excerpt from this graph;
the full graph is available at http://yago-knowledge.org.
Some extractors exist in several instantiations, because they
perform the same task on diﬀerent input data. All in all,
YAGO uses 40 extractor instantiations.

4.
APPROACH
Our input is a list of Wikipedia languages, and our goal
is to create a KB from these multilingual Wikipedias. This
comes with 3 challenges: (1) We have to determine the set
of entities, (2) we have to extract facts about these entities
from Wikipedia, and (3) we have to create a taxonomy.
We will now show how these 3 tasks can be solved holis-
tically. Our key advantage is that we can leverage the ex-
isting English YAGO as a reference KB and as a taxonomic
backbone. Furthermore, the YAGO architecture is modular
enough to allow an organic extension beyond the English
Wikipedia. By adding extractors in the right places, we ar-
rive at an elegant, yet eﬀective solution for the creation of a
full-ﬂedged KB from multilingual Wikipedias.

4.1
Set of Entities
In YAGO, every Wikipedia article becomes an entity.
In YAGO3, we have to take care not to duplicate enti-
ties, because the same entity can be described in diﬀerent

3http://geonames.org

Foreign
Wikipedia

Infobox
Extractor

Foreign
Infobox
Attributes

Term
Extractor

Untranslated
Attribute
Facts

Entity
Translator

Foreign
Attribute
Facts

Attribute
Translator

Attribute
Translations

Attribute
Mapper

Foreign
YAGO Facts

English
Wikipedia

Infobox
Extractor

Infobox
Attributes

Term
Extractor

Attribute
Facts

Attribute
Mapper

English
YAGO Facts

WikiData

WikiData
Extractor

Dictionary

Figure 1: Extraction from infoboxes
In bold: English extraction
In light: multilingual extraction
In green: newly designed extractor modules

Wikipedias.
We use Wikidata for this purpose.
As de-
scribed in Section 3, Wikidata maintains its own repository
of entity and category identiﬁers, and maps them to arti-
cles in Wikipedias in diﬀerent languages.
We designed a
Wikidata extractor (Figure 1 top right), which takes Wiki-
data as input, and produces a theme Dictionary as output.
This theme contains facts that map every foreign category
name and entity name to its English counterpart, as in this
example:

"de/Amerikanische S¨anger" hasTranslation
"American Singer"
de/Elvis hasTranslation Elvis
We preﬁx entities and categories with the language code of
their Wikipedia edition. Some foreign entities have no En-
glish counterpart. In these cases, our method chooses the
ﬁrst language in the input list of languages in which the en-
tity appears. For example if our list of languages is ⟨English,
French, Italian, German⟩, and if the Italian Wikipedia con-
tains the village of Loano, then we will seek this entity ﬁrst
in English and then in French before defaulting to Italian.
This gives us a ﬁle that maps every foreign and English ar-
ticle name to a unique entity name. The set of these unique
names is our set of entities.

4.2
Fact Extraction
In this section, we explain how we extract facts from
infoboxes.
We ﬁrst treat the existing extractors for the
English YAGO and then explain the new extractors for the
multilingual YAGO.

### Page links

- [Link 1](http://geonames.org)
- [Link 2](http://yago-knowledge.org)

## Page 4

4.2.1
English Extraction
Extraction from Infoboxes. The YAGO system extracts
facts about the article entity from infoboxes, such as birth
places, authored books, or physical attributes. We ﬁrst ex-
plain the existing extractors (Figure 1, left). The Infobox
Extractor (top left) parses out attribute-value pairs and pro-
duces the theme Infobox Attributes. These are raw pairs as
they appear in the article, and take, e.g., the following form:

Elvis infobox-spouse "\[Pricilla Presley\], 1967"
The Term Extractor extracts all possible terms from the
attribute value. These are instance names, and literals such
as dates, numbers, and quantities.
The resulting theme,
Attribute Facts, contains, e.g.:

Elvis infobox-spouse Priscilla_Presley
Elvis infobox-spouse "1967-##-##"^^xsd:date
YAGO uses wildcards if components of a date are unknown.
The Attribute Mapper uses manually deﬁned mappings be-
tween the English infobox attributes and the YAGO rela-
tions to produce facts in YAGO’s schema. This yields, e.g.,

Elvis marriedTo Priscilla_Presley
Elvis marriedTo "1967-##-##"^^xsd:date

Type Checking.
YAGO performs several checks on its
facts.
One of them is the type check.
A fact ⟨x, r, y⟩is
accepted, if ⟨x, type, dom(r)⟩and ⟨y, type, ran(r)⟩are
part of the KB. YAGO deﬁnes classes not just for instances,
but also for literals. These include dates, strings, and num-
bers with their subclasses of rational numbers, integers, pos-
itive integers, and so forth. Every such class comes with a
manually deﬁned regular expression that identiﬁes literals of
this class. For example, the class integer comes with the reg-
ular expression“\[+-\]?\[0-9\]+”. The type check y ∈ran(r) is
performed by matching y to the regular expression of ran(r).
This way, the type check can ﬁlter out non-conforming facts
for both entities and literals.
In the example, the type
checker will reduce the facts to

Elvis marriedTo Priscilla_Presley

Funclash Checking. Some of YAGO’s relations have been
deﬁned as functional. If r is a functional relation, this im-
poses ⟨x, r, y⟩∧⟨x, r, y′⟩⇒y = y′
∀x ∈I, y ∈I ∪L.
If two fact candidates ⟨x, r, y⟩, ⟨x, r, y′⟩appear with y ̸= y′

for some functional relation r, we have a functional clash
(funclash for short). In this case, either one or both of the
candidates have to be discarded. In the current YAGO im-
plementation, the input themes are sorted in such a way that
the more precise information (from the infoboxes) precedes
the more coarse information (from the categories). In case
of a funclash, the fact from the ﬁrst theme is kept, and all
potentially following clashing facts are discarded.
Type checking and funclash checking are performed by
extractors that read one or several themes as input, and
produce a theme as output that contains only the facts that
pass the check. Finally, the themes are merged together. In
this process, duplicates are removed. Furthermore, less spe-
ciﬁc facts (such as ⟨Elvis, wasBorn, "1935-##-##"⟩) are
removed if more speciﬁc facts are available (such as ⟨Elvis,
wasBorn, "1935-01-08"⟩).

4.2.2
Multilingual Extraction
Foreign Infoboxes.
The extraction from multilingual

Wikipedias proceeds similar to the English one. The center
branch of Figure 1 uses the same extractors, and is repli-
cated for every input language. For example, for German,
the theme Foreign Infobox Attributes may contain:

de/Elvis de/heirat "\[Priscilla Presley\],
1967 in \[Las Vegas (Stadt)\]"
This fact states that Elvis married Priscilla in 1967 in the
city of Las Vegas. As for the English Wikipedia, the Term
Extractor extracts all possible terms:

de/Elvis de/heirat de/Priscilla_Presley
de/Elvis de/heirat "1967-##-##"^^xsd:date
de/Elvis de/heirat de/Las_Vegas_(Stadt)
Diﬀerent languages have diﬀerent ways to express numbers
and dates (this is true in particular for Farsi). We adopt a
conservative approach: We run our standard term extractor,
and extract only dates and numbers that follow the English
convention. Our date extraction is designed in such a way
that it only extracts dates in which the order of day, month,
and year can be established unambiguously. We leave the
adaptation of the term extractor to diﬀerent languages for
future work. After the term extraction, the Entity Trans-
lator uses the dictionary to translate the entities to their
unique names:

Elvis de/heirat Priscilla_Presley
Elvis de/heirat "1967-##-##"^^xsd:date
Elvis de/heirat Las_Vegas
We call these facts foreign attribute facts.
Attribute Mapping.
While the entities of the for-
eign attribute facts have been mapped to their language-
independent unique names, the attributes still have to be
mapped to the YAGO schema. In the example, we want to
deduce that the German infobox attribute de/heirat corre-
sponds to the YAGO relation marriedTo. Let Fa be the set
of subject-object-pairs that appear in the foreign Wikipedia
with an infobox attribute a (e.g., a = de/heirat). Let Er
be the set of subject-object-pairs that appear in the English
YAGO with a given relation r (e.g., r = marriedTo). We
want to determine whether a maps to r.
In principle, we could deduce this mapping from the fact
that a Fa and Er will share many subject-object pairs. In
practice, this is challenging for several reasons: First, the
term extractor produces dozens of terms per attribute value,
and only very few of them are the intended objects. Second,
the foreign Wikipedia may contain facts that YAGO does
not contain. Vice versa, YAGO may contain facts that the
foreign Wikipedia does not contain. Third, there may be
spurious matches.
The foundation year of a village, e.g.,
may coincide with its number of inhabitants.
Matches. Our Term Extractor can extract several objects
of several types from a single infobox attribute-value pair.
Since the majority of them are usually of the wrong type, we
may not hope to ﬁnd all of them in the English YAGO facts.
Vice versa, the English YAGO facts may be more detailed
than the foreign attribute facts.
For example, they may
know several albums of a singer, while the foreign Wikipedia
may know only a few. Thus, we may not hope to ﬁnd all
English YAGO objects in the foreign Wikipedia. Therefore,
we count as a match between a and r any subject that has
a common object for a and r in Fa and Er, respectively:

matches(Fa, Er) = πsubj(Fa ∩Er)

## Page 5

Clashes. If a YAGO relation r is a functional relation, and
a foreign attribute a contains a diﬀerent object for the same
subject x, then a cannot map to r. We call x a clash. In
practice, Fa will contain several objects of diﬀerent types,
and only few of them will actually match with the English
YAGO. Therefore, we relax the deﬁnition of a clash as fol-
lows: A subject is a clash for a and r, if it has objects in Fa
and in Er, and if these objects are disjoint:

clashes(Fa, Er) = πsubj(Fa) ∩πsubj(Er) \ πsubj(Fa ∩Er)

We call this deﬁnition of clashes and matches the object set
semantics, because, for a given subject and a given relation,
the objects are considered as a set. We look only at disjoint-
ness or non-empty intersections for the deﬁnition of clashes
and matches.
Contributions. The foreign Wikipedias may bring entities
that are unknown to the English YAGO. They may also
bring facts that the English YAGO does not know. Thus,
for a given foreign attribute, not every subject is a clash
or a match. It may also just be a new fact. To quantify
this phenomenon, we introduce the contributions of a foreign
attribute a as the number of distinct subjects:

contrib(Fa) = πsubj(Fa)

The total number of facts that a contributes in the end may
be larger than this number (if most subjects have several
objects), or smaller (if most objects are removed by type
checks).
Given Fa and Er, our goal is to determine whether a maps
to r. Several measures can be envisaged to this end.
Support. The support is simply the number of matches:

support(Fa, Er) = |matches(Fa, Er)|

This measure corresponds to the support in association rule
mining \[2\]. It can be used to map an attribute to a relation if
the number of subject-object pairs exceeds a certain thresh-
old. This measure might be to restrictive for attributes with
a small number of contributions. Vice versa, it may be mis-
leading if there is a large number of contributions and a large
number of spurious matches.
Conﬁdence. The other measure of association rule mining
is the conﬁdence. In our setting, it corresponds to the ratio
of matches out of the total number of contributions:

confidence(Fa, Er) = |matches(Fa, Er)|

|contrib(Fa)|

This measure is rather conservative, because it will punish
mappings that have only few matches, and potentially many
new facts that are unknown to the English YAGO.
PCA Conﬁdence. The PCA-conﬁdence \[13\] measures the
number of matches out of the total number of matches and
clashes:

pca(Fa, Er) =
|matches(Fa, Er)|
|matches(Fa, Er)| + |clashes(Fa, Er)|

It was developed for association rule mining under the open
world assumption, and is used in \[12\] to align relations across
KBs. The PCA conﬁdence admits that a fact that cannot
be found in the English YAGO is not necessarily wrong. It
is merely unknown. Therefore, the measure considers only
facts that are conﬁrmed or rejected explicitly (the matches
and clashes), and ignores other facts.

Probabilistic Measure. Most pairs of a and r will ex-
hibit some proportion of spurious matches. Before mapping
a to r, we want to make sure that the proportion of matches
exceeds that proportion of spurious matches, say 1%. The
problem is that if our sample is small (say, 5 elements),
then already one spurious match will fulﬁll that condition.
Hence, we use a measure that models the mapping problem
as a Bernoulli experiment. We observe that all non-English
Wikipedias are smaller than the English Wikipedia. There-
fore, we assume that Fa is only a subset of the future, yet-
unknown set of infobox attribute facts F ∗
a that the foreign
Wikipedia will eventually comprise. We want to know the
proportion of these infobox attribute facts that match the
English YAGO facts with r. In particular, we want to know
whether this proportion exceeds a threshold θ of spurious
matches.
We make the following simplifying assumptions: We as-
sume that Fa is a uniformly randomly drawn sample from
F ∗
a .
We also assume that Er is ﬁxed.
We want to esti-
mate the proportion of matches, confidence(F ∗
a , Er).
In
particular, we want to know whether confidence(F ∗
a , Er)
exceeds θ. We do not have access to F ∗
a , and cannot compute
confidence(F ∗
a , Er), but only confidence(Fa, Er). Thus, we
aim to estimate a lower bound for a Bernoulli parameter
from the observed parameter in the sample.
There are several ways to estimate a lower bound for a
Bernoulli parameter. Here, we opt for the Wilson Score In-
terval \[7\], because it is particularly well-suited for small sam-
ples. The interval takes the form of a center c and a width δ.
These values are computed from the size of the sample, |Fa|,
and the conﬁdence on the sample, confidence(Fa, Er). The
interval guarantees that with a given probability (set a pri-
ori, usually to α = 95%), the value confidence(F ∗
a , Er) falls
into \[c −δ, c + δ\]. For small samples, the interval width δ
will be very large. With growing sample size, δ shrinks and
the center c converges towards confidence(Fa, Er).
The
properties
of
the
Wilson
interval
imply
that
confidence(F ∗
a , Er) > c −δ with α = 95%. Therefore, we
deﬁne our measure for the matching of a to r as as

wilson(Fa, Er) := c −δ

This measure allows us to judge whether the proportion of
matches is large enough, even if the sample is small.
Mapping. Given any of the measures, m ∈{support, con-
ﬁdence, pca, wilson}, and given a threshold θ ∈R, we can
deﬁne an approximate mapping of foreign infobox attributes
to YAGO relations:

d
map(a) =

(
argmaxr m(Fa, Er),
if maxr m(Fa, Er) > θ
undeﬁned,
else

We designed an extractor for the YAGO system that per-
forms this mapping, the Attribute Matcher (Figure 1). It
takes as input a measure m and a threshold θ, and maps the
foreign attributes in to YAGO relations. In the example,
this will yield:

de/heirat hasTranslation marriedTo
These mappings are then used by an Attribute Mapper, just
as for the English Wikipedia, to produce foreign YAGO facts
from the attribute facts. In the example, we get:

Elvis marriedTo Priscilla_Presley
Elvis marriedTo "1967-##-##"^^xsd:date
Elvis marriedTo Las_Vegas

## Page 6

These facts will undergo the same checking and ﬁltering as
the other YAGO facts. A type check, e.g., will leave us with

Elvis marriedTo Priscilla_Presley
In this example, we just learned a fact that was in the En-
glish YAGO anyway.
However, other foreign infobox at-
tribute facts will give rise to new YAGO facts that were not
in the English Wikipedia. Likewise, in the example, both
Elvis and Priscilla were in the English YAGO. However, we
extracted one million entities from the other Wikipedias that
were not in the English YAGO. These give rise to new nodes
in the YAGO knowledge base.
Further Processing. The facts will also undergo a fun-
clash checking, with the preference rules as follows. First of
all, the preference is given to the facts that were extracted
from the infoboxes over facts from the categories. Within
each group, preference is given to the English Wikipedia,
followed by the other Wikipedias in our input list of lan-
guages. Within the infobox facts, preference is given to the
ﬁrst values. Within an infobox value string, preference is
given to the left-most extracted value. This is just the order
in which the Term Extractor produces the terms. We justify
this choice by our manual analysis in Section 5.1.

4.3
Taxonomy Construction
In this section, we explain how we construct a unique tax-
onomy for YAGO. We ﬁrst explain the existing architecture
for the monolingual case before explaining our extension to
the multilingual case.
English Extraction.
The taxonomy of YAGO comes
mainly from the categories of Wikipedia. Again, the process
is driven by a sequence of extractors that each perform one
particular transformation of data. The Category Extractor
(not shown in the ﬁgure) extracts category memberships. It
creates a theme that contains facts such as

Elvis inCategory "Rock Music"
Elvis inCategory "American Singers"
A subsequent extractor will ﬁlter out categories that do not
correspond to class names (such as Rock Music, see \[25\]),
and produce a theme that contains statements such as

Elvis type American_Singer
A follow-up extractor will use noun phrase parsing to ﬁnd
out that this class is most likely a subclass of the class Singer
of WordNet, thus producing

American_Singer subclassOf Singer
Another extractor will transform the entire WordNet taxon-
omy into triples, which yields, e.g.,

Singer subclassOf Person
Person subclassOf LivingBeing
etc.
This way, the entity Elvis Presley is linked via the subclass
of American Singers into the WordNet taxonomy.
Multilingual Extraction. In the English Wikipedia, the
categories of articles are identiﬁed by the keyword Cate-
gory.
Other languages use other keywords.
To ﬁnd out
these keywords, we made use of Wikidata.
For example,
in our Dictionary from Wikidata, Category:
American
singers is mapped to the German equivalent Kategorie:
Amerikanische S¨anger. This tells us that the categories in
the German Wikipedia are introduced by the keyword Kat-
egorie. We extracted all of these translations from Wiki-

data. We could then modify the existing category extractor
of YAGO to extract category memberships also from foreign
Wikipedias. For German, the Category Extractor extracts:

de/Elvis inCategory "de/Amerikanische S¨anger"
A follow-up extractor uses the dictionary to translate these
foreign entity and category names to their unique names:

Elvis inCategory "American singers"
From this point on, the standard YAGO extractors can do
their work. The categories will be ﬁltered and connected to
the WordNet taxonomy.
Other Processing. Categories such as 1935 births can
also be a source of facts about the article entity.
YAGO
uses manually deﬁned patterns to extract these facts.
In
the multilingual case, we ﬁrst translate the categories to
English through the dictionary, and then use the very same
patterns to extract facts. If an infobox template (such as
singer) is used in an article, this can be indication that
the article entity belongs to a particular class. Hence, we
extract infobox templates in the same way as categories,
and use them to create type facts.

4.4
Overall Integration
Taxonomy.
Every entity is mapped to a language-
independent unique identiﬁer (Section 4.1), so that facts
about the same entity will use the same entity identiﬁer.
Each Wikipedia article is in one or more categories. These
categories are translated to their English counterparts, and
then give rise to classes (Section 4.3). If we cannot establish
a class for an entity, the entity is abandoned. Hence, every
entity, foreign or English, is a member of at least one class.
The classes are linked into the common WordNet taxonomy.
All in all, this process creates a KB in which English entities
and foreign entities live together in the same taxonomy.
Schema. All foreign language attributes have been either
abandoned or mapped to one of the 77 English YAGO re-
lations.
This ensures that every fact has its place in the
common schema.
Final extractors will remove any dupli-
cate facts, so that each fact in YAGO is unique, even if
contributed from several sources.
Manual Work. We note that the only manual eﬀort in the
construction of YAGO3 is the mapping of English infobox
attributes to YAGO relations – which exists already in the
original YAGO. The foreign infobox attributes are mapped
automatically to YAGO relations. The translation of entities
and categories is done with the data from Wikidata.

5.
EXPERIMENTS
We ran the YAGO extraction system on 10 languages: En-
glish, German, French, Dutch, Italian, Spanish, Romanian,
Polish, Arabic, and Farsi. The choice of languages was de-
termined by the proﬁciency of the authors, so as to facilitate
manual evaluation. We cover some of the largest Wikipedias,
and both European and non-European languages.

5.1
Funclashes
As discussed in Section 4.2.1, funclashes occur when a fact
candidate ⟨x, r, y⟩with a functional relation r encounters a
YAGO fact ⟨x, r, y′⟩with y ̸= y′.
Such clashes are often
used to spot contradictions in semantic data. We wanted
to know whether funclashes have this role in our setting,
too. In our setting, facts are collected from the Wikipedias
in the given order of languages (Section 4.2.2). Whenever

## Page 7

Funclashes
Relation
552,693
wasCreatedOnDate
63,473
diedOnDate
50,588
wasBornOnDate
18,437
wasBornIn
15,927
happenedOnDate
12,308
hasHeight
11,185
hasDuration
9,980
hasWeight
4,300
diedIn
3,418
wasDestroyedOnDate

Table 1: Funclashes per relation

an incoming fact clashes with an existing fact from a higher
ranked language, the incoming fact is discarded.
Table 1
shows the relations that produce most funclashes. The vast
majority of clashes stem from date relations, followed by
numeric relations.
We were interested in whether funclashes are really an in-
dication for contradictions. Therefore, we sampled a set of
100 funclashes randomly, and analyzed them manually. In
5 cases, the rejected object was clearly more accurate than
the existing object.
The other cases were as follows: (1)
A Wikipedia article describes several variants of the entity
with diﬀerent properties. For example, a movie may exist in
original and abridged form, where the latter has a shorter
duration. (2) In nearly half of the cases, the rejected object
was wrong or less accurate than the existing object. This
is mainly because Wikipedia often contains complementary
information in the infobox value string after the targeted
value. For example, numerical attributes (such as page num-
bers or population numbers) are often followed by years in
the infobox attribute value. The funclash gives preference
to the ﬁrst number and thus discards the (incorrect) second
number. (3) In one forth of the cases, diﬀerent values can
be justiﬁed. For example, numerical values in diﬀerent units
give rise to slightly diﬀerent objects. The year of foundation
of a city can be either when it was ﬁrst populated, or when
it was incorporated. The height of a tower may or may not
include the antenna. In these cases, the funclash just makes
an arbitrary choice. It would be confusing for applications
if a tower had two height values, because the additional tex-
tual information that is present in Wikipedia is projected
away in the KB.
While we could justify abandoning the functional con-
straints on this basis, they are invaluable to avoid mixing
up diﬀerent versions of the same entity (case (1)), to avoid
extracting years as page numbers (case (2)), and to ensure
overall consistency (case (3)). Therefore, we decided to keep
functional constraints. At the same time, they are not al-
ways an indication for semantic inconsistencies, which makes
them less useful for attribute mapping, as we shall see.

5.2
Choice of Parameters
Gold Standard.
We wanted to measure the precision
and recall of the mapping of infobox attributes to YAGO
relations under diﬀerent measures and thresholds (Section
4.2.2). We created a near-exhaustive mapping, which maps
every infobox attribute a of a particular Wikipedia edition
to every YAGO relation r with matches(Fa, Er) > 0. This
mapping is arguably a superset of the desired mapping. For

every language, we randomly sampled 150 attribute-relation
pairs from this mapping, and evaluated them manually. A
pair ⟨a, r⟩was evaluated to true, if the attribute a will yield
a correct r fact for every entity of type ran(r) in its value.
Thus, our manual gold standard will map the German at-
tribute geboren (born) to both bornInPlace and bornOn-
Date, because the attribute value can contain both a birth
place and a birth date.
Evaluation. We produced attribute mappings by each of
the measures from Section 4.2, for diﬀerent threshold values,
and for all languages under consideration. The threshold θ
was varied between 0 and 1 for the conﬁdences, between 0
and 500 for support, and between 0 and 50% for the Wilson
score. Values outside these ranges decreased recall without
increasing precision. By varying θ, we can trade oﬀprecision
and recall. Figure 2 exempliﬁes this for French and Farsi.
Since YAGO has an accuracy of 95% \[25\], we have to choose
a threshold that achieves at least this precision.
We ﬁnd that only for the Wilson score and the conﬁdence
there exist thresholds that achieve a precision of 95% and
a recall of more than 5% across all languages. This is be-
cause the support is not robust to scaling: languages with
many facts (such as German) need a high threshold, while
languages with few facts (such as Spanish) produce no map-
pings if the threshold is too high. The PCA conﬁdence is
misguided by the clashes, and thus behaves in a very er-
ratic way across languages. The Wilson score consistently
achieves the highest recall across all languages, at compara-
ble precision to the conﬁdence (Table 2). This is because in
order to achieve a high precision, the conﬁdence has to use
a high threshold. This, in turn, hurts recall. The Wilson
score, in contrast, can stay with a low threshold and thus
a high recall, because it cautions automatically against too
small sample sizes. Hence, we chose the Wilson score as our
measure. To achieve a precision of 95%, we chose θ = 4%.
Discussion.
Most erroneous mappings come from two
sources. First, unit-less numbers (such as the number of in-
habitants) produce a disproportionally high number of spuri-
ous matches, coinciding, e.g., with longitude values or years.
Second, there are a number of relations that are strongly
correlated in life, but that are strictly speaking not matches
(such as wasBuriedIn/diedIn), and so we did not count
them as such. Still, we achieve very good precision and re-
call values overall.
If the Wikipedias of two diﬀerent languages share no
knowledge, then our method will not propose any mapping.
However, it is improbable that this happens. There has been
a rapid globalization of Wikipedia, which triggered thou-
sands of volunteers to create, modify, and link millions of
articles. Together with manual translation of articles, this
led to a substantial overlap of the Wikipedias in a lot of
common concepts such as countries, important people, and
prominent events.
Our KB is built on YAGO, and tries to match foreign at-
tributes to YAGO relations. Our method does not consider
attributes that have no mapping to the existing YAGO re-
lations. We leave the introduction of new YAGO relations
for future work.
Comparison.
With respect to attribute matching, the
work of \[23\] reports a recall of 85% at the precision of 95%
that is required for YAGO. This is a combination that our
method cannot achieve. The focus in YAGO3, however, is on
broad language coverage. Our method achieves a weighted

## Page 8

0.5
0.6
0.7
0.8
0.9
1

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9

1

Precision

Recall

Support
Conﬁdence

PCA
Wilson

0.6
0.7
0.8
0.9
1

0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

1

Precision

Recall

Support
Conﬁdence

PCA
Wilson

Figure 2: Precision/Recall for French (left) and Farsi (right)

Conﬁdence 16%
Wilson 4%

Prec
Rec
F1
Prec
Rec
F1
ar
100
73
85
100
82
90
de
100
37
54
98
56
72
es
96
19
32
95
29
45
fa
100
49
66
97
54
69
fr
100
16
27
100
69
82
it
100
7
12
98
23
37
nl
100
19
32
100
22
36
pl
95
10
19
97
64
77
ro
96
52
67
95
70
81

Table 2: Precision and Recall per Language in %

precision of 98% at a recall of 56% for German, a preci-
sion of 99.98% at a recall of 69% for French, and a pre-
cision of 99.99% at a recall of 22% for Dutch. These are
the languages that \[23\] considered. In addition, our system
produces alignments for Italian, which the method of \[23\]
could not run on due to poor infobox naming conventions,
and 5 other languages. These include languages of non-Latin
script, which \[23\] explicitly excludes. Our method thus pro-
vides a robust alternative to \[23\] with much higher language
coverage.
\[1\] solves the slightly diﬀerent problem of merging in-
foboxes across Wikipedia languages.
They report a pre-
cision of 86% for English, Spanish, French, and German.
Our method compares favorably with this precision.
Be-
yond that, we can show that it works for 6 more languages.
\[28\] aligns the English Wikipedia with 2 Chinese online
encyclopedias. They report a precision of 86% at a recall of
88%. Their work concerns non-Wikipedia data sources, and
so we cannot compare directly to them.
\[22\] aligns infobox attributes between the English and
the Portuguese Wikipedia, and the English and the Viet-
namese Wikipedia. For Portuguese, the average weighted
precision on 14 infobox templates is 93%, and the recall is
75%. For Vietnamese, the values are 100% and 75%, respec-
tively. These values are comparable to ours.
\[14\] aligns infobox attributes to DBpedia. The approach

Language
Entities
Facts
Type Facts
Labels

en
3,420,126
6,587,175
10,280,369
477,628
de
349,352
984,830
2,563,246
125,575
fr
255,063
549,321
920,014
361,932
nl
204,566
249,905
398,719
208,521
it
67,330
148,268
160,777
1,424
es
118,467
43,271
512,024
213
ro
11,024
12,871
44,175
946
pl
103,440
235,357
296,398
215,470
ar
50,295
98,285
314,495
2,575
fa
16,243
27,041
121,492
4,553

total
4,595,906
8,936,324
15,611,709
1,398,837

Table 3: Number of entities and facts

was evaluated for Italian, and achieves its highest precision
of 87% at a recall of 37%. These values are comparable to
ours.
Diﬀerent from all of these approaches \[22, 1, 23, 14\], our
alignment method is considerably simpler.
It requires no
similarity functions or machine learning methods – while
achieving comparable results. This is because we can build
on the existing YAGO infrastructure, which is able to pro-
duce a high-precision KB. We also show that our method is
robust enough to treat twice as many languages as previous
work. Finally, our method goes beyond previous work by
constructing a uniﬁed KB on top of these sources, which in-
cludes type facts and a taxonomy. We illustrate this in the
next section.

5.3
Size
Facts. Table 3 shows the total number of distinct new enti-
ties that each language contributed to our uniﬁed KB. Every
entity is counted only for the ﬁrst language in our preference
list in which it appears, even if it is contributed by several
other languages as well. In total, we gain 1m new entities.
The number of new entities does not scale linearly with the
number of languages, because most languages treat the same
global concepts before venturing into local entities. The ta-

## Page 9

de/Kirdorf_(Bedburg),

hasNumberOfPeople, "1204"^^xsd:integer
fr/Ch^ateau_de_Montcony,

isLocatedIn, Burgundy
pl/Henryk_Pietras, wasBornIn

de/Debiensko

fa/
, wasBornIn, Teheran

Table 4: Some sample facts

ble also shows the number of facts contributed by every lan-
guage. Again, every fact is counted only once. The “facts”
column shows ordinary facts extracted from the infoboxes
and categories. We gain 2.5m facts over the English-only ex-
traction. The next column shows type facts extracted from
the template names and the categories. We gain 5m new
facts about types. Not all of these are necessarily about the
new entities that a language contributed; a language can
also contribute a type fact about an English entity.
The
last column shows the label facts.
We gain 1m labels.
This number is complemented by 355k labels that we ex-
tracted from the English disambiguation pages, 11m labels
that come from the redirect pages, 1.5m person names (given
name and family name), and 729k new labels from Wikidata,
and 1.5m facts extracted by other extractors from the En-
glish Wikipedia, bringing the total number of all facts to
40m.
Examples. Our facts include truly hybrid facts, where the
subject or object do not exist in the English Wikipedia.
Table 5 shows some examples.
In the ﬁrst example, the
subject exists only in the German Wikipedia. In the second
example, the subject exists only in French, but the object
is contributed by English. In the third example, neither the
subject nor the object exists in English. The subject exists
only in Polish, and the object exists in German and Polish
(and German is chosen over Polish). We also have a large
number of facts in non-Latin script. We show a fact about
Amir Alam, a former member of the Iranian parliament.
Schema. All foreign language attributes have been either
abandoned or mapped to one of the 77 English YAGO rela-
tions (see Section 4.2.2). Every entity has at least one type
fact (see Section 4.3). The types are connected to the com-
mon WordNet taxonomy. This ensures that every entity has
its place in the common schema. All in all, YAGO contains
488,469 classes.

6.
APPLICATIONS

6.1
DBpedia
Multilingual DBpedia. Our method can be used to align
other KBs. We downloaded the version of the English DBpe-
dia that contains ontological relations. We used our method-
ology to align it with the foreign attribute facts of German.
As in the other scenarios, we produced a gold standard and
evaluated the precision and recall. Our vanilla setting of the
Wilson score interval with θ = 4% achieves a precision of
95% and a recall of 81%. The values are not as high as for
the YAGO-internal alignments, because DBpedia uses dif-
ferent data types (such as xsd:gYear) that our term extrac-
tor does not produce. On the other hand, our system was
run oﬀthe shelf, and DBpedia-speciﬁc adjustments could in-

crease the performance further. For example, by using the
support measure with a dataset-speciﬁc threshold of 100,
we achieve a precision of 96% and a recall of 94%. Thus,
our methodology could help map the infobox attributes of
diﬀerent languages to the common DBpedia properties – a
task that is currently achieved manually by the community.
Ontology Alignment.
Our method can also be used
to align the relations of DBpedia and YAGO. We took
again the English DBpedia with ontological relations, and
matched them with the YAGO facts. We generated a gold
standard, and evaluated the mappings. Our vanilla setting
of a Wilson score threshold of θ = 4% achieves a weighted
precision of 100% and a weighted recall of 76%. This is in
line with the weighted precision of 100% that \[24\] reports
for this alignment, while they report no recall.

6.2
Le Monde
In \[16\], the authors analyze the text of the French newspa-
per Le Monde by mapping all mentions of entities in the text
to YAGO entities. This allows, e.g., statistics on the preva-
lence of foreign companies in diﬀerent countries, or an anal-
ysis of the changing age structure in certain professions over
time. Since YAGO was not available in French, the approach
could use only those YAGO entities that had a French name
and that had enough facts in the English Wikipedia, result-
ing in 3.4m mentions.
With YAGO3, we can boost that
number by 824k new mentions, referring to 32k unique new
entities. 112k of the mentions are people, and of these, 20k
are politicians and 8k are musicians. These entities can con-
tribute more data points to the statistics. For example, we
can add 5 more countries to the analysis of the prevalence
of foreign companies, because we now have enough data for
these countries.

7.
CONCLUSION
In this paper, we have shown how to construct the ﬁrst
full-ﬂedged KB from Wikipedias in multiple languages. By
using YAGO as a central reference KB, and by extending
its existing architecture, we arrive at a simple and elegant,
yet very eﬀective method. Our approach works across 10
languages and diﬀerent scripts, and achieves a precision of
95%-100% in the attribute mapping. The new KB gains 1m
new entities and 7m new facts over the English-only YAGO.
On the technical side, we have compared several measures
for the mapping of infobox attributes, and presented a mea-
sure that is robust to scale and language. We have shown
that our measure can be applied to diﬀerent other relation
alignment problems at high precision and recall. For future
work, we envisage extending our methods to more languages,
and study new applications of the knowledge base. YAGO3
is available at http://yago-knowledge.org.

8.
REFERENCES

\[1\] E. Adar, M. Skinner, and D. S. Weld. Information
arbitrage across multi-lingual wikipedia. In WSDM,
2009.
\[2\] R. Agrawal, T. Imieli´nski, and A. Swami. Mining
association rules between sets of items in large
databases. SIGMOD Rec., 22(2), June 1993.
\[3\] A. P. Aprosio, C. Giuliano, and A. Lavelli. Automatic
expansion of dbpedia exploiting wikipedia
cross-language information. In ESWC, 2013.

### Page links

- [Link 1](http://yago-knowledge.org)

## Page 10

\[4\] S. Auer, C. Bizer, G. Kobilarov, J. Lehmann,
R. Cyganiak, and Z. G. Ives. DBpedia: A Nucleus for
a Web of Open Data. In ISWC, 2007.
\[5\] J. Biega, E. Kuzey, and F. M. Suchanek. Inside
yago2s: A transparent information extraction
architecture. In Proc. WWW (Comp.), 2013.
\[6\] G. Bouma, S. Duarte, and Z. Islam. Cross-lingual
alignment and completion of wikipedia templates. In
Workshop on Cross Lingual Information Access, 2009.
\[7\] L. D. Brown, T. T. Cai, and A. Dasgupta. Interval
Estimation for a Binomial Proportion. Statistical
Science, 16(2), May 2001.
\[8\] G. de Melo and G. Weikum. MENTA: Inducing
multilingual taxonomies from Wikipedia. In CIKM,
2010.
\[9\] G. de Melo and G. Weikum. Untangling the
cross-lingual link structure of wikipedia. In ACL, 2010.
\[10\] G. de Melo and G. Weikum. UWN: A large
multilingual lexical knowledge base. In ACL, 2012.
\[11\] G. de Melo and G. Weikum. Taxonomic data
integration from multilingual wikipedia editions.
Knowl. Inf. Syst., 39(1):1–39, 2014.
\[12\] L. Gal´arraga, N. Preda, and F. M. Suchanek. Mining
rules to align knowledge bases. In AKBC, 2013.
\[13\] L. Gal´arraga, C. Teﬂioudi, K. Hose, and F. M.
Suchanek. Amie: association rule mining under
incomplete evidence. In WWW, 2013.
\[14\] A. P. A. C. Giuliano and A. Lavelli. Towards an
automatic creation of localized versions of dbpedia. In
ISWC, 2014.
\[15\] J. Hoﬀart, F. M. Suchanek, K. Berberich, and
G. Weikum. Yago2: A spatially and temporally
enhanced knowledge base from wikipedia. Artif.
Intell., 194, 2013.
\[16\] T. Huet, J. Biega, and F. M. Suchanek. Mining
history with le monde. In AKBC, 2013.
\[17\] O. Medelyan, D. Milne, C. Legg, and I. H. Witten.
Mining meaning from wikipedia. Int. J.
Hum.-Comput. Stud., 67(9):716–754, Sept. 2009.
\[18\] G. Miller. WordNet: An Electronic Lexical Database.
MIT Press, 1998.
\[19\] V. Nastase and M. Strube. Transforming wikipedia
into a large scale multilingual concept network. Artif.
Intell., 194, 2013.
\[20\] V. Nastase, M. Strube, B. Boerschinger, C. Zirn, and
A. Elghafari. Wikinet: A very large scale multi-lingual
concept network. In LREC, 2010.
\[21\] R. Navigli and S. P. Ponzetto. BabelNet: The
automatic construction, evaluation and application of
a wide-coverage multilingual semantic network.
Artiﬁcial Intelligence, 193:217–250, 2012.
\[22\] T. H. Nguyen, V. Moreira, H. Nguyen, H. Nguyen,
and J. Freire. Multilingual schema matching for
wikipedia infoboxes. PVLDB, 5(2), 2011.
\[23\] D. Rinser, D. Lange, and F. Naumann. Cross-lingual
entity matching and infobox alignment in wikipedia.
Inf. Syst., 38(6):887–907, Sep. 2013.
\[24\] F. M. Suchanek, S. Abiteboul, and P. Senellart. Paris:
Probabilistic alignment of relations, instances, and
schema. PVLDB, 5(3), 2011.
\[25\] F. M. Suchanek, G. Kasneci, and G. Weikum. YAGO:

A core of semantic knowledge - unifying WordNet and
Wikipedia. In WWW, 2007.
\[26\] F. M. Suchanek, G. Kasneci, and G. Weikum. YAGO -
A Large Ontology from Wikipedia and WordNet. J. of
Web Semantics, 6(3), September 2008.
\[27\] E. Tacchini, A. Schultz, and C. Bizer. Experiments
with wikipedia cross-language data fusion. In
Workshop on Scripting and Development, 2009.
\[28\] Z. Wang, J. Li, Z. Wang, and J. Tang. Cross-lingual
knowledge linking across wiki knowledge bases. In
WWW, 2012.
\[29\] D. T. Wijaya, P. P. Talukdar, and T. M. Mitchell.
Pidgin: ontology alignment using web text as
interlingua. In CIKM, 2013.

## Page 11

APPENDIX

A.
DEMO PROPOSAL

A.1
YAGO3
YAGO is a knowledge base extracted from WordNet and
the English Wikipedia \[2\].
YAGO3 extends the original
YAGO by the Wikipedias in 10 languages: English, Ger-
man, French, Dutch, Italian, Spanish, Romanian, Polish,
Arabic, and Farsi. It contains 4,5m entities (such as people,
cities, or organizations), and 24m facts about these entities
(such as which city is in which country, which singer created
which album, or who is the president of which organiza-
tion). Some facts and entities were extracted only from the
English Wikipedia, while others came from both the English
Wikipedia and a foreign Wikipedia, or from several foreign
Wikipedias. Table 5 shows some examples. In the ﬁrst ex-
ample, the subject exists only in the German Wikipedia, and
hence it has a German identiﬁer. In the second example, the
subject exists only in French, but the object is contributed
by English. In the third example, the subject exists only in
Polish, and the object exists in German and Polish (and the
German identiﬁer was chosen). We also have a large num-
ber of facts in non-Latin script. We show a fact about Amir
Alam, a former Iranian member of parliament. The facts,
likewise, stem from Wikipedias of diﬀerent languages.

de/Kirdorf_(Bedburg),

hasNumberOfPeople, "1204"^^xsd:integer
fr/Ch^ateau_de_Montcony,

isLocatedIn, Bresse
pl/Henryk_Pietras, wasBornIn

de/Debiensko

fa/
, wasBornIn, Teheran

Table 5: Some sample facts
A.2
Demo
In our demo proposal, users can explore our multilin-
gual knowledge base.
They can visualize facts about an
entity of their choice in a graphical browser (as in Fig-
ure 3).
The browser shows all facts that YAGO3 knows
about it. In the example, the user can see that the French
province Bresse has certain geographical coordinates, that it
is called “Bresse” in French, and that the Chˆateau de Mont-
cony is located there. When there are several facts with the
same relation (e.g., several rdf:type facts), these can be dis-
played by clicking on “more”. Each fact is annotated with
the Wikipedias in which it was found. In the example, the
fact that Bresse is in the class Provinces of France has been
found in the English, the French, and the Italian Wikipedias.
Facts that stem from Wikidata have no ﬂag. When the user
clicks on another entity, this other entity becomes the cen-
ter of the displayed graph. This way, the user can navigate
through YAGO3 and explore which facts are contributed by
which Wikipedias. For example, clicking on the Chˆateau de
Montcony will display facts that come exclusively from the
French Wikipedia.
By clicking on a ﬂag, the user can show provenance infor-
mation about the fact. This includes the source Wikipedia
URL, the name of the extractor, and the name of the (po-
tentially foreign) infobox attribute or category. For exam-
ple, clicking on the English ﬂag at Provinces of France shows

that this fact was found on the English page of Bresse by the
category type extractor. Some facts are extracted by several
extractors. By clicking on the source Wikipedia URL, the
user can browse through a list of facts extracted from this
Wikipedia.
We also provide a search ﬁeld, where the user can enter
the name of an entity in diﬀerent languages. This allows the
user to navigate, say, to their hometown. Even if this town
does not exist in the original monolingual YAGO, chances
are that it exists in our multilingual YAGO.
In a separate window, users can explore the infobox at-
tribute mappings that we found for our 10 languages.

Figure 3: Browsing YAGO3

A.3
Implementation
Server-Client.
Our browser is implemented as a Java
servlet and runs on the client in a standard Internet browser.
The entire knowledge base resides on the server in a Post-
gres database in a single table.
The frontend is an SVG
image, which is created dynamically to show the data from
the database. The entities in the SVG image are hyperlinks.
When the user clicks on one of them, a request is sent to the
server, which replies with a new SVG image.
Previous Implementation. The browser implementation
for the English YAGO without the provenance annotations
is already online at http://yago-knowledge.org. It has not
been the subject of a demo submission so far. Our WWW
2013 demo \[1\] concerned the extractor architecture of a pre-
vious YAGO version, and did not actually allow browsing
the knowledge base at all.

A.4
Conclusion
Our demo proposal allows users to interactively explore
the new YAGO3 knowledge base in several languages. Users
can see facts contributed by diﬀerent Wikipedias, and dis-
play the provenance of these facts.
Since the conference
participants are international, we believe that our demo will
be of interest to the audience.

B.
REFERENCES
\[1\] J. Biega, E. Kuzey, and F. M. Suchanek. Inside
yago2s: A transparent information extraction
architecture. In Proc. WWW (Comp.), 2013.
\[2\] F. M. Suchanek, G. Kasneci, and G. Weikum. YAGO:
A core of semantic knowledge - unifying WordNet and
Wikipedia. In WWW, 2007.

### Page links

- [Link 1](http://yago-knowledge.org)
