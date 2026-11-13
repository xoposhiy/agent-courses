# Project ethics: ACL guidelines

[Course index](../../README.md) · [Original source](https://2021.aclweb.org/ethics/Ethics-FAQ/) · [Raw file](../../raw/references/project-ethics-acl-guidelines.html)

Retrieved: 2026-11-13T16:35:41.399761+00:00

## Ethics FAQ

As announced in the call for papers for ACL 2021:

> Authors are required to honour the ethical code set out in the ACL Code of Ethics. The consideration of the ethical impact of our research, use of data, and potential applications of our work has always been an important consideration, and as artificial intelligence is becoming more mainstream, these issues are increasingly pertinent. We ask that all authors read the code, and ensure that their work is conformant to this code. Where a paper may raise ethical issues, we ask that you include in the paper an explicit discussion of these issues, which will be taken into account in the review process. We reserve the right to reject papers on ethical grounds, where the authors are judged to have operated counter to the code of ethics, or have inadequately addressed legitimate ethical concerns with their work. Indeed, the ACL-IJCNLP 2021 review form includes a section addressing these issues. Papers flagged for ethical concerns by reviewers or ACs will be further reviewed by the Ethic Advisory Committee (EAC).

This page provides an FAQ about the ethics review process and guidance to authors for how to address ethical considerations in your ACL papers. This applies in the first instance to papers submitted to the main conference (including industry track papers and demo papers). We encourage ACL workshops to follow similar principles.

### **How is ACL 2021 handling ethics review?**

Ethics review is handled at several levels:

- In the [CFP](https://2021.aclweb.org/calls/papers/) and this page: information is given concerning what is expected from the authors and reviewers concerning ethics.
- ACL reviewers are asked to consider the points listed in the [ethics review questions page](https://2021.aclweb.org/ethics/Ethics-review-questions/) and then indicate whether a paper should be flagged for further ethics review and, if so, what considerations lead them to that recommendation.
- A reviewing committee dedicated to ethical issues will review papers flagged by the reviewers or the ACs during the review process. The committee membership will be listed on the ACL 2021 webpage in due course.
- The ethics committee will recommend for each flagged paper whether to (a) accept as is, (b) conditional accept (with specification of what must be addressed for camera-ready), or (c) reject on ethical grounds (with explanation). These judgments will complement, but not replace, review for technical merits from the primary reviewers.
- Camera-ready versions of papers designated as (b) conditional accept will be re-reviewed by the ethics committee to determine whether the concerns have been adequately addressed. If the given conditions are found not to be met, the paper will be rejected.
- The ethics committee is available to respond to questions from authors about the feedback they have received, regardless of whether the decision was acceptance, conditional acceptance, or rejection on ethical grounds. In the case of (b) conditional accept, the committee’s goal is to ensure that the authors have the resources to meet the criteria for acceptance. To that end, the authors are encouraged to reach out to the committee with any questions about how to respond to feedback as they prepare their camera-ready submission.

### **Can papers be rejected from ACL due to ethical concerns?**

Yes. Papers may be rejected on the basis of ethical or legal concerns. Recommendations for such decisions will come from the ethics committee, with input from the initial reviewers. The final accept/reject decisions remain with the Program Chairs. The reviewing timeline is set up to allow for conditional acceptance pending resolution of ethical issues as one possible recommendation. Papers in this category will be re-reviewed only for ethical considerations before the camera-ready version is accepted. Please note that acceptance is not guaranteed in this case; it is conditional on the concerns raised being adequately addressed.

ACL has adopted the [ACM Code of Ethics](https://www.acm.org/code-of-ethics) as its own ACL Code of Ethics for all members to respect. Please ensure that your paper complies with the rules expressed in it.

### **Should I have an “ethical considerations” section in my paper?**

Ethical questions may arise when working with a variety of types of computational work with language, including (but not limited to) the collection and release of data, inference of information or judgments about individuals, real-world impact of the deployment of language technologies, and environmental consequences of large-scale computation. **If you are uncertain about whether your paper merits a section or not, we recommend you include one.** Depending on the work, this section may be quite brief (a few sentences), or longer to address novel issues in the paper.

Authors are granted extra space after the 8th page (4th page for short papers) for an ethics/broader impact statement and we strongly encourage you to use it. At submission time, if you need extra space for the ethical considerations section, it should be placed after the conclusion so that it is possible to rapidly check that the rest of the paper still fits in 8 pages (4 pages for short papers). In some cases, it may be more natural to include some of this information in other sections, and that is fine; you may also choose to include a brief ethical considerations section that references these sections.

The sections below outline the kind of information that should be included in an ethical considerations section, depending on the type of research presented in the paper. An additional resource is the [ethics review question list](https://2021.aclweb.org/ethics/Ethics-review-questions/) that will be supplied to reviewers when considering the ethical impact of your work. Papers that report on research that raises ethical issues that do not discuss such issues are likely to be rejected on ethical grounds.

### **What should I be aware of if my paper presents a new dataset?**

- Ensure that your dataset has been collected in a manner which is consistent with the terms of use of any sources and the intellectual property and privacy rights of the original authors of the texts. The fact that a dataset has already been used previously does not necessarily make it acceptable. If appropriate, check that informed consent was signed. Your institution may have a data officer or a review board charged with helping researchers navigate these issues and we encourage you to reach out to them for assistance. Such reviews may take time, so we advise you to contact them early if needed.
- Detail the dataset collection process and conditions. If manual work was involved, describe measures taken to ensure that crowd workers or other annotators were fairly compensated and how fair compensation was determined.
- Please indicate if your project was approved by an IRB (institutional review board). (For a discussion of IRBs in the US context, see <https://www.apa.org/advocacy/research/defending-research/review-boards>)
- Describe the characteristics of the dataset in enough detail for a reader to understand which speaker populations the technology could be expected to work for. (For suggestions of what kind of information to include, see [Bender and Friedman 2018](https://aclweb.org/anthology/papers/Q/Q18/Q18-1041/), [Mitchell et al 2019](https://research.google/pubs/pub48120/) and [Gebru et al 2018](https://arxiv.org/abs/1803.09010).)
- Finally, describe the steps taken to ensure that potential problems with the quality of the dataset do not create additional risks.

### **… if my paper involves an NLP application?**

Here we are concerned with papers involving tasks outside of language, including both tasks "close to" language like sentiment analysis as well as those that are more clearly connected to specific real-world applications, such as automated essay scoring, hate speech or other toxic language detection, chatbots, or systems which flag electronic medical records as indicating the need for specific treatments. For such papers, we urge authors to carefully consider how the technology could be deployed in actual use cases and ensure that there is good alignment between the task carried out automatically and the use case. Furthermore, you should consider and address the following questions:

- **Intended use**. If the technology is functioning as intended, who benefits? Who might be harmed, and how?
- **Failure modes.** What are the failure modes, and in case of failure, who might be harmed and how?
- **Biases.** What are the biases included in the dataset and trained model, and how might they contribute to those failure modes? (On bias in NLP, see [Blodgett et al 2020.](https://www.aclweb.org/anthology/2020.acl-main.485/))
- **Misuse potential.** What kinds of potential misuse is there for the technology and what harms might ensue? What could be done to prevent such misuse/what should regulators know about this technology?
- **Collecting data from users.** If the system as deployed would learn from further user input, what further risks of harm might ensue and how can these be mitigated?
- **Potential harm to vulnerable populations.** Are any of the possible harms you’ve identified likely to fall disproportionately on populations that already experience marginalization or are otherwise vulnerable?

### **… if my paper uses demographic or identity characteristics in formation?**

Please take care to avoid either attributing (i.e. assigning, without asking) identity characteristics to the people whose language is studied (i.e. guessing their gender, race, nationality, etc) or essentializing identity characteristics (i.e. suggesting that people speak or write a certain way because of their demographic description). We encourage you, wherever possible, to use self-identified characteristics. We understand that that is not always possible. In some cases, it may make sense to reframe the research question so as to avoid attributing identity characteristics. In others, best practice may be to acknowledge the source of the identity characteristic data. In addition, we encourage ACL authors to consult with their institutional review boards (IRB) or equivalent for input on working with data from human subjects.
Please do be sure to motivate the range of values used for identity characteristics in terms of how they relate to the research question and to discuss the ethical implications of categorizing people, either in training datasets or in the deployment of the technology. For further discussion of this point as it pertains to gender specifically, see [Larson 2017](https://www.aclweb.org/anthology/W17-1601/).

### **… if my paper reports on experiments that involve lots of compute time/power?**

Given the urgency of addressing climate change, we have a responsibility to also consider the energy resources expended on our research. A first step in this direction is increasing awareness about the potential increased energy and carbon costs of large-scale projects ([Strubell et al 2019](https://www.aclweb.org/anthology/P19-1355/)), in relation to more efficient alternatives. We encourage authors to use tools such as [Henderson et al’s (2020)](https://arxiv.org/abs/2002.05651) [experiment impact tracker](https://github.com/Breakend/experiment-impact-tracker) or other available information to estimate the energy requirement of the experiments reported in the paper (including prior runs that helped shape the research question) and of the model in its suggested deployment context. If such information is not feasible to obtain for completed experiments, proxies such as computing platform and running time are also informative. We also suggest that the authors discuss steps that have been or could be taken to reduce the carbon costs of the proposed methods.

### **Additional resources**

Here are links to some additional resources that are useful to read before writing ethical considerations sections.

- [A Guide to Writing the NeurIPS Impact Statement](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832) by Carolyn Ashurst, Markus Anderljung, Carina Prunkl, Jan Leike, Yarin Gal, Toby Shevlane, and Allan Dafoe
- [Research on Machine Learning for Disaster Response: what makes a good paper?](https://towardsdatascience.com/research-on-machine-learning-for-disaster-response-b65f3e97c018?source=friends_link&sk=e2e8e7ef66cae276bde29298b7516955) by Rob Munro

*Most of the text above comes from the [NAACL 2021 Ethics FAQ](https://2021.naacl.org/ethics/faq/); we thank NAACL 2021 Ethics Chairs, Emily M. Bender and Karën Fort for drafting the prior version.*
