# Lecture 2 transcript: LLMs for Builders

[Course index](../../README.md) · [Original source](https://youtu.be/Vr1NzH8bT44) · [Raw file](../../raw/videos/Vr1NzH8bT44.json)

Retrieved: 2026-11-13T16:18:20.969507+00:00

[00:05] So first of all, welcome to the second

[00:07] lecture of CS 329 Z Engineering AI

[00:10] Agents. I'm Michael. I'm another one of

[00:13] the instructors. I'm super excited to

[00:15] give this lecture because a little bit

[00:16] of inside lore. This is the first time

[00:19] I've prepared a lecture and given it. So

[00:21] I am really excited to share it with you

[00:23] all, but if there's anything at all

[00:24] that's confusing, please, you know, stop

[00:27] me, let me know, you know, raise your

[00:28] hand because, you know, I'm learning

[00:30] here too and I'd appreciate your

[00:31] feedback afterwards too.

[00:33] Great. Okay. So today we're talking

[00:36] about large language models, which I'm

[00:37] sure you're all aware of what a large

[00:39] language model is. But language models

[00:42] have a lot of depth to them. So we're

[00:43] going to talk about what I consider it

[00:45] to be the large language model stack.

[00:47] There is three layers here, but you

[00:49] know, this is kind of arbitrary. This is

[00:50] my own little creation here. So I'd say

[00:53] there's kind of these three levels, LLM

[00:55] engineering, LLM adaptation where you

[00:57] swap it to to work in your setting, and

[01:00] then applications you build on top of

[01:01] large language models. And so what does

[01:03] this actually contain? Well, LLM

[01:06] engineering is all of these things that

[01:07] you're seeing here. How do you set up

[01:09] distributed compute to train models on

[01:11] massive clusters? How do you write GPU

[01:13] kernels that can efficiently do all of

[01:15] the matrix multiplications that we need

[01:17] to process text? You have architecture,

[01:20] scaling laws, post training.

[01:23] Then on the LLM adaptation layer, this

[01:25] is about adapting LLMs to work in your

[01:28] context and your situation. So we have

[01:30] things like fine tuning, distillation,

[01:32] in context learning, low rank

[01:34] adaptation. And then on the applications

[01:36] layer,

[01:38] I mean there's way more than this, but

[01:39] you can imagine agents, chatbots, rag,

[01:42] these are like things that you build on

[01:43] top of LLMs. And so I wanted to paint a

[01:45] little picture of, you know, what we're

[01:47] what we're doing here and what you

[01:49] should expect to learn about language

[01:51] models because it's it's not all of

[01:52] this.

[01:53] So at the bottom of the stack here, I

[01:56] would say that's the the goal of CS 336

[01:59] here at Stanford, which language models

[02:00] from scratch, and that's to teach you,

[02:02] you know, everything you need to know to

[02:03] like build a language model, which is a

[02:05] lot.

[02:06] Uh, then uh we have this kind of like

[02:09] broad uh

[02:11] part of the uh you know, broad circle

[02:13] here, which is CS 224N, which is the

[02:16] introduction uh natural language

[02:17] processing class. Um, and then at the

[02:20] very very top of this stack is kind of

[02:23] where we are going to sit for this

[02:24] class. So we are going to be building on

[02:26] top of large language models mostly. Uh,

[02:28] so that's CS 329Z. Uh, now you might

[02:31] notice that the the circles overlap a

[02:33] bit, so I did want to emphasize that we

[02:35] have some several things that would not

[02:36] be covered in CS 224N. But um this is

[02:39] just to paint a picture here. Um, I'm

[02:41] going to say that, you know, we're going

[02:43] to operate at this highest level of the

[02:44] large language model stack. Uh, but

[02:48] today's goal uh is to teach you a bit

[02:50] more about how they work because there

[02:51] are pieces of it that you need to

[02:53] understand about how language models are

[02:54] built uh that will inform how you build

[02:57] things with language models.

[02:58] Um, so the learning objectives today are

[03:01] to understand and explain the core

[03:03] design decisions that go into training

[03:05] and inferencing modern large language

[03:07] models. Uh, and we're going to

[03:08] synthesize how these design decisions um

[03:11] will lead to limitations uh that impact

[03:14] the way we leverage large language

[03:15] models. So knowing things about like how

[03:17] the KV cache works and how different

[03:19] forms of attention work will actually

[03:21] let you select which model that you

[03:22] should use for your application,

[03:24] understand will this work in long

[03:25] context settings or not um and give you

[03:28] kind of these uh

[03:30] this insight into how the underlying

[03:32] technology is working. But then in the

[03:34] rest of the class we're just going to be

[03:35] using language models.

[03:37] Um, so the lecture overview today we're

[03:39] going to start with, you know, what even

[03:41] is a language model? Uh, we're going to

[03:42] talk about language model architectures,

[03:45] training, inference, and finally we will

[03:47] cover, you know, large language models

[03:48] for agents in particular.

[03:50] So before I get started, uh any

[03:52] questions on, you know, the goal of

[03:54] today's lecture?

[03:57] Cool.

[03:58] Then we're going to get started with

[04:00] what is a language model, which I'm sure

[04:01] many of you have a sense of what a

[04:03] language model is, but we're going to

[04:04] actually take it back to uh the

[04:06] underlying equation. Uh so this is uh

[04:10] this right here is a language model. Um

[04:13] we're saying here the probability of a

[04:15] sequence of tokens is equal to uh the

[04:19] product from the first to last token,

[04:21] and you can think of tokens as as words,

[04:23] for example, of the probability of the

[04:26] current token given all the previous

[04:27] tokens. And we're just going to take

[04:28] this product over all the all the

[04:30] tokens. So let me let me uh represent

[04:33] this. I know this is going to be a

[04:34] background knowledge for a lot of

[04:35] people, but I promise that this will be

[04:37] informative for when we get to the

[04:38] deeper stuff.

[04:40] Uh so we can say, okay, the probability

[04:42] of the um I'm going to say it's a black

[04:44] box for now, and I'll peel that black

[04:46] box away in a second. Uh the probability

[04:48] of the is 0.0377.

[04:50] Okay, the probability of class given the

[04:53] is .0001.

[04:55] Uh and we can do this for every token in

[04:57] this sequence. Uh and what we'll do is

[05:00] we will take the product of all of that,

[05:02] and we will say that this is the

[05:05] probability of this sequence of text,

[05:07] okay?

[05:09] Uh and so in practice we typically take

[05:10] the sum of the log of the probabilities

[05:12] because we're operating with such such

[05:13] small numbers and numerical stability is

[05:15] a real concern. Uh but this is what a

[05:17] language model does. It's actually just

[05:19] predicting the probability of a sequence

[05:20] of text.

[05:22] Uh and so this this part here is the

[05:24] language model. Um and now I want to

[05:26] say, you know, what can we do with

[05:28] language models? So first of all, uh

[05:30] let me point out what the difference

[05:32] between generative and discriminative

[05:33] models are. Um so discriminative models

[05:36] are learning to distinguish classes. So

[05:38] you may know about classifiers or uh

[05:40] logistic regressions, support vector

[05:42] machines. And really this is like let's

[05:44] say the blue is a population of images

[05:47] of cats, red is a population of images

[05:50] of dogs. Uh what we're doing here is

[05:52] like you're learning a separator, like

[05:53] what is the difference between dogs and

[05:55] cats? Or is a generative model would be

[05:57] able to uh produce an image of a cat and

[06:00] tell you how probable is this set of

[06:02] pixels, how likely is it that that is a

[06:05] Or that this set of pixels is a dog? Um,

[06:08] so I have a quick question uh for the

[06:12] class here. So are language models that

[06:15] model the probability of a token

[06:16] sequence as shown below, uh is this a

[06:19] generative or discriminative model? Uh

[06:21] someone want to raise their hand and and

[06:24] make a statement?

[06:30] Uh do we have some?

[06:32] So I think that this is a good point to

[06:35] I would say the difference between

[06:37] generative and discriminative is a fuzzy

[06:39] boundary. I'm I'm going to say that it's

[06:41] generative, but the reason for that is

[06:43] because

[06:44] any uh the definition of generative

[06:46] means that any um you can basically

[06:49] model the probability of any um

[06:52] uh

[06:53] input here. And so because the tokens we

[06:55] are deciding between the tokens, which

[06:57] is why it's a little bit fuzzy that it's

[06:59] a you could think of it as a

[07:00] discriminative model. But because we can

[07:02] model any token sequence and find the

[07:03] probability of it given a token

[07:05] sequence, we can just say what's the

[07:07] probability of this token sequence. So

[07:08] we're not necessarily saying like what

[07:10] is the difference between this token and

[07:12] this token. We're just modeling the

[07:13] probability of the token sequence. Then

[07:15] I I want to say that it's generative,

[07:16] but I that's why I wrote that this is

[07:18] kind of a tricky question because the

[07:19] the notation makes it seem like we are

[07:22] saying that we are modeling the

[07:23] difference between tokens. Uh but but uh

[07:26] in general people will say that language

[07:28] models are generative because we are

[07:30] modeling the probability uh and of the

[07:32] of the whole sequence of tokens. It also

[07:34] means that we can sample uh from the

[07:37] language model. Uh so let me explain how

[07:40] we can sample from language models.

[07:43] Uh so I had this sequence of tokens. The

[07:45] class was about

[07:47] um and then what we can do is we can

[07:49] have our entire vocabulary of all

[07:52] possible things that we could say next.

[07:55] Uh now if we were saying uh that the uh

[07:58] the class was about to or as, you know,

[08:01] if we trained a model specifically for

[08:02] that, that would be more of like a

[08:03] discriminative model. But because we say

[08:05] the entire vocabulary um again the

[08:08] discriminative and generative is a

[08:09] little bit of a fuzzy term, but we can

[08:12] say we're measuring the uh probability

[08:14] of all of these things. And so what

[08:16] we'll do is we will take this and we

[08:18] will say what is the probability of two

[08:21] given the class was about, what is the

[08:22] probability of as given the class was

[08:25] about, so on, and we get a probability

[08:27] for each of these.

[08:29] Uh and so what we will do is we will

[08:31] look uh I have this little animation. We

[08:33] will represent the probabilities here,

[08:36] and we're going to sample from it. So

[08:37] we'll say, okay, two was the most likely

[08:39] thing. Uh so we're going to say that

[08:41] that's the next token.

[08:43] Um and then we'll go and we will slide

[08:46] it over here and now we have the class

[08:47] was about two and we can continue. So

[08:49] now we have be, begin, go. Uh but

[08:52] another thing that you can do when

[08:53] you're sampling is this is a probability

[08:55] distribution, so you don't actually have

[08:56] to take the most likely thing. Uh so you

[08:59] can say uh actually I'm going to sample

[09:01] begin. Uh and there's a couple ways that

[09:03] you can do this sampling. Uh so greedy

[09:05] is always taking the most likely next

[09:08] token. Um then uh you have top P, which

[09:11] is like let's say you're saying I'm

[09:13] going to look amongst the top 30% of

[09:15] things, so you'll sum up these

[09:16] probabilities until it gets above 30%

[09:18] and then you'll say I'm going to sample

[09:19] from those. Uh top K is like I'm going

[09:21] to say I'm only going to pick from like

[09:23] the top five most likely things, so it

[09:24] would be be, begin, go, start, get. So

[09:27] this is the the various decoding

[09:29] strategies here. Um and then so I had

[09:32] said begin and I put this little cute

[09:34] animation the class is about to begin.

[09:36] So

[09:37] uh and then um the last things I wanted

[09:40] to talk about with sampling are that um

[09:42] the other considerations is that

[09:43] temperature is a a way you can

[09:45] manipulate language model sampling. So

[09:48] um here we have um from this uh post I

[09:51] had this um next token distribution for

[09:54] I am tired, I will take a blank. And

[09:56] what we'll do here is you take you set

[09:58] this temperature T uh and this is a

[10:01] hyperparameter type of thing you can

[10:02] tune for your setting. And if T is high

[10:05] uh it means that your text is going to

[10:07] be more diverse. If T is low, it's going

[10:09] to be closer to picking the most likely

[10:11] thing. And what you do is just take all

[10:13] of those probabilities or you actually

[10:14] take the the logits uh before you turn

[10:17] them into probabilities and you'll

[10:19] essentially divide them by this

[10:20] temperature and then make sure you

[10:22] renormalize so everything sums to one.

[10:24] Um and so this is how you can kind of

[10:26] manipulate how diverse of a sample

[10:28] you're looking at. Uh and the other

[10:29] thing uh that's kind of an interesting

[10:31] way of using language models for

[10:33] decoding is using beam search. Uh so you

[10:35] don't actually have to just pick the

[10:37] next token at every time step. Uh you

[10:39] could also peer deeper into the chain.

[10:42] Uh but the important thing uh and so you

[10:43] could see like maybe we wanted to start

[10:45] with the or arrived. So we're going to

[10:47] try decoding on both and then eventually

[10:49] decide which one we'll continue with. Uh

[10:51] the tricky thing about uh this is like

[10:54] you can imagine this is a a lot more

[10:55] expensive on time [clears throat]

[10:56] complexity and memory uh complexity

[10:59] because you have to store um you know

[11:02] all of these states uh to do this. But

[11:04] um the last thing I'll note about

[11:06] sampling here is that uh each sampling

[11:08] strategy has these different trade-offs.

[11:10] So you can use temperature, top P, top K

[11:12] to help with diversity. Um the strategy

[11:14] that you'll use will depend on your

[11:16] task. Um so math and code uh can be more

[11:19] predictable uh which means uh you might

[11:22] use a lower temperature or something

[11:23] like that. Uh creative writing you might

[11:25] benefit from having a higher temperature

[11:27] to get higher diversity. Um and your

[11:30] strategy will also depend on your

[11:31] budget. Uh so uh beam search like I

[11:34] mentioned has a higher time and memory

[11:36] complexity.

[11:38] So uh now we're going to get a little

[11:40] bit deeper into how language models

[11:42] work, but I wanted to ask for now does

[11:45] anyone have a question about what is a

[11:46] language model?

[11:50] Yes.

[11:51] >> Given temperature and you like think 0.1

[11:54] to are those the bounds in general? I

[11:56] assume not, but

[11:57] >> No, so the the the temperature is

[11:59] specifically um what you're

[12:02] you're using that to divide the

[12:04] probability. So it's not extremely

[12:06] interpretable like to say like a

[12:08] temperature of five means like you'll

[12:12] see this, but basically it's just a

[12:14] scaling factor. So you can kind of see

[12:16] that how we had nap was like very very

[12:19] spiky here, but as we divide and spread

[12:22] out the probability mass, it becomes

[12:24] lower. So it's just basically a factor

[12:26] that we are dividing the probabilities

[12:27] by um and it allows us to smooth out the

[12:30] distribution.

[12:31] Question.

[12:33] Yes.

[12:33] >> Is taking

[12:35] the probabilities of all possible

[12:37] sequences that how do we absorb the

[12:39] language or not?

[12:41] >> Yes. So this is your vocabulary size and

[12:43] so I kind of glossed over tokenization,

[12:46] but basically

[12:48] and I called it kind of words, but what

[12:49] we actually do is split

[12:51] uh language into like these small chunks

[12:54] and those are tokens. And so you might

[12:56] have a tokenized you might have a

[12:57] vocabulary of like 128,000 possible

[13:00] things um and that's what we're doing

[13:03] the probability over. So it is this

[13:04] fixed set of things, but those are

[13:06] chunks that could be used to represent

[13:08] any text essentially. Good question.

[13:10] Yeah.

[13:15] >> Yeah. And so I think about 128k is uh

[13:20] one it's it's a sort of a design

[13:22] decision with the model, but um yeah,

[13:25] good question.

[13:27] >> Do you go throughout the use of the

[13:29] model or

[13:29] >> Yes. That's a that's a I haven't seen a

[13:32] ton of that, but I think you could do

[13:35] like hot swapping of the temperature and

[13:36] I off the top of my head can't think of

[13:39] an issue that it would like invalidate

[13:40] the KV cache or anything. I think that

[13:42] would be fine.

[13:44] >> This context have to be possibly

[13:46] discriminate between beams and beam

[13:48] search? Cuz in like a traditional search

[13:49] context there's a check that you have to

[13:51] do, but here

[13:52] you can't really compare I the

[13:54] conditional probability.

[13:55] >> Yeah, so it could be dependent on your

[13:57] task. Like for instance, I might have a

[14:00] external verifier. Uh so I could be

[14:02] trying to solve like a math problem or

[14:04] something like that and I could have

[14:06] some value function that's steering me

[14:08] or something like that. But that is a

[14:10] good question that I kind of didn't talk

[14:12] about in detail, but you you can have

[14:13] some way of selecting which beam is

[14:15] best. And you could also use the

[14:16] language model itself to try to say if

[14:19] like the probability of this sequence

[14:21] when we look five tokens into the future

[14:22] was actually better. Yeah, it's a good

[14:25] question.

[14:28] >> What does it learn to predict?

[14:29] >> Um not typically.

[14:32] Yeah, it's typically something you set

[14:33] afterwards. You train with a certain

[14:36] Yeah, you don't use temperature in

[14:37] training at all. But yeah, you use you

[14:39] you use temperature for

[14:42] RL actually because you have to

[14:43] inference the model. And so you'll

[14:45] you'll produce

[14:47] you'll use a certain temperature when

[14:48] you're doing like RL for a model. But

[14:50] it's it's not

[14:53] usually something that you learn because

[14:54] I guess there isn't like a gradient

[14:55] signal for that since we're using it for

[14:58] inference primarily.

[15:00] But yeah.

[15:01] >> When we're talking about sampling in

[15:02] this class, are we referring to that

[15:06] its usability in like RLHF or

[15:09] pre-training or inference or

[15:10] >> I mean sampling is important in like

[15:12] every aspect of the language model

[15:14] because it's going to be used for

[15:16] generating text from the language model,

[15:17] which obviously the agent needs to be

[15:19] able to generate text.

[15:21] We will use it for RL because you

[15:22] generate rollouts.

[15:24] So

[15:25] yeah, we'll use it. Anytime you use a

[15:27] language model, we have to In the

[15:28] context of this class, we'll be sampling

[15:30] from it.

[15:31] Yeah.

[15:32] Cool. Maybe if there's one more

[15:33] question, I'll take it. And then I think

[15:34] I should move on.

[15:37] Yeah.

[15:38] >> But currently the model seems for do

[15:40] some reasoning first before answer the

[15:43] questions. So I wonder is the

[15:45] temperature still recording?

[15:47] >> Good question about reasoning. So we're

[15:48] going to actually cover reasoning models

[15:50] in a bit. But yeah, so it actually

[15:53] it does affect the reasoning as well.

[15:55] But I think it's

[15:58] Yeah, another one of the design

[15:59] decisions is like tuning the temperature

[16:00] for a reasoning model too. But yeah,

[16:02] we'll talk about that in a moment. Good

[16:03] question. All right, I'm going to move

[16:04] on.

[16:05] So the next topic is language model

[16:08] architecture. And I'm going to start

[16:11] with just a very brief history of

[16:12] language model architectures.

[16:14] So we had N-gram models in the pre-2010s

[16:17] and all this was doing was just counting

[16:19] how many times you see uh certain token

[16:22] in a vocabulary and estimating the

[16:23] probability based on raw counts. So,

[16:25] you'd say like I see the comes after uh

[16:28] or I see like dog comes after the, you

[16:31] know, a thousand times. Uh so and then

[16:34] I've I've looked at a million tokens.

[16:36] So, it's like that my percentage of

[16:38] seeing dog condition on the is based on

[16:40] that. Um we have first neural language

[16:43] model in 2003, recurrent neural networks

[16:46] in 2010, uh LSTMs in like 2014 was when

[16:50] they were popularized for LLMs. We won't

[16:52] really talk about this in the interest

[16:53] of time, although I I did prepare slides

[16:55] for all of these, but I I got some

[16:56] feedback that this this needs to be cut

[16:58] down. So, we won't be talking about

[17:00] these, but hopefully um if you're

[17:01] interested, this is kind of like prior

[17:03] stuff that you can look at 224N and

[17:05] learn about. So, we're going to talk

[17:06] about Transformers, which are powering

[17:09] most of the modern large language

[17:11] models, um some variants of

[17:12] Transformers.

[17:13] Uh so uh the this is the architecture

[17:17] for a Transformer. It comes from this

[17:18] Attention Is All You Need paper from

[17:20] Google in 2017. Uh and this is actually

[17:23] an encoder-decoder model. Uh the encoder

[17:26] is on the left and it is turning the

[17:28] input text into embeddings uh which are

[17:31] then fed into the uh decoder model and

[17:35] mixed together uh and outputs the log

[17:37] probabilities that I talked about, the

[17:39] probabilities of the text. Uh but we

[17:41] will go way more uh in depth into what

[17:42] this actually means. I'm going to cut

[17:44] the encoder out. A lot of modern

[17:45] language models are decoder only uh and

[17:48] it's all the same building blocks

[17:49] anyway. So, I'm going to talk about how

[17:51] a decoder works. Um

[17:54] so let's uh let's take this step by step

[17:56] here. Okay. So, um this this is going to

[17:59] be how we uh model this. So, we're going

[18:01] to have the class was about. These are

[18:04] the tokens across the bottom here uh and

[18:07] I'm going to compute the probability of

[18:09] the next token from this sequence. So,

[18:12] first of all, we're going to embed these

[18:14] uh tokens, which just means we're going

[18:16] to convert them into a vector

[18:18] representation. Uh I'm not going to talk

[18:20] too much about embedding, but you can

[18:22] have like an embedding table that is

[18:23] trained that converts the tokens into uh

[18:27] vector embeddings.

[18:28] Uh then we're going to have a positional

[18:30] embedding. Uh this is because as you'll

[18:32] see as we build out this architecture,

[18:34] um position is not uh baked into

[18:37] anything in the architecture itself. So

[18:39] you actually need to uh mix this vector

[18:42] together to say like this is token in

[18:44] position one. This is position two,

[18:45] three, four, so on.

[18:48] Um and then we're going to uh just sort

[18:50] of stack these all together into a

[18:51] matrix because it's going to make the

[18:52] representation look easier here.

[18:54] Um so

[18:56] here's an important thing and I can tell

[18:57] everyone's paying close attention. So

[18:58] this is good. I was worried, you know,

[19:00] that maybe I would have lost people by

[19:01] now, but I think people are paying great

[19:03] attention. So important pay close

[19:06] attention here because we're going to

[19:07] talk about attention and this is

[19:09] incredibly important for the rest of the

[19:12] lecture and also probably the rest of

[19:14] your time working with Transformers. Um

[19:16] so this is how the attention layer

[19:18] works. Um so we're going to take a layer

[19:20] norm uh of these vectors, which is

[19:22] basically um you're normalizing based on

[19:25] the mean and variance to get sort of a

[19:26] uniform uh

[19:28] uh a unit vector for these uh embeddings

[19:31] that have been, you know, added with the

[19:32] positional embeddings.

[19:34] And we're going to take three matrix

[19:36] multiplications, okay? So I'm

[19:38] representing weights here by these

[19:40] blocks. Uh activations, which are like

[19:43] the product of of doing the matrix

[19:45] multiplication are the dots, okay? And

[19:47] the the weights are the blocks. And so

[19:49] what we're doing is we're going to take

[19:50] this matrix of uh the embeddings and

[19:54] we're going to multiply it by WQ, which

[19:57] is the query uh weights and we're going

[20:00] to get our our query vectors, which are

[20:02] our activations here. So you can see uh

[20:04] I tried to make the shapes make sense

[20:06] here. I'm going a little I'm going to go

[20:08] slow and step by step, but we have um

[20:10] four tokens here. So you can see when we

[20:12] have four things, uh that's the sequence

[20:14] length. Uh so you can see the sequence

[20:17] length

[20:18] is shown here and then this is the

[20:19] dimension of our uh our hidden state uh

[20:23] for the the uh key query values. Uh so

[20:26] we we do this matrix multiplication for

[20:29] the weights of the keys, the weights of

[20:30] the values, the weights of the queries.

[20:32] Uh and we're going to transpose uh the

[20:34] the key activations um just because

[20:38] it'll make the matrix multiplications

[20:39] work. Um and so then what we're going to

[20:42] do is I have the equation for attention

[20:44] here on the left. We're going to do the

[20:45] matrix uh multiplication between the

[20:48] keys sorry the the queries and the

[20:51] transposed keys. And we're going to get

[20:53] this n by n attention scores. Um and so

[20:57] this is uh a function of the sequence

[20:59] length here.

[21:00] Uh and we're going to apply a causal

[21:02] attention mask. The reason for doing

[21:03] that is because you can't look ahead uh

[21:06] and your your uh

[21:07] it would not work for decoding

[21:10] essentially. Like it works now. We can

[21:11] we can have the attend to about and the

[21:14] attend to was when we have all of our

[21:16] data. But when we're actually decoding

[21:18] uh we don't know what the next sequence

[21:19] is going to be. So we're going to mask

[21:21] these out uh which just means that about

[21:24] can interact with the but the cannot you

[21:28] know

[21:28] uh

[21:29] create its uh attention map based on

[21:32] about. Um so it's just enforcing that

[21:34] the next token is what we're looking at.

[21:37] Um and then we just divide by the

[21:39] dimension for um you know uh changing

[21:43] the size of the numbers there for

[21:45] stability. And we take the softmax which

[21:48] just means that we make sure all of

[21:49] these rows will sum to one.

[21:53] We'll then take the matrix

[21:54] multiplication between those activations

[21:56] and the uh value activations. And we'll

[21:59] get um our uh matrix there which we

[22:02] multiply by a projection back to the

[22:05] model dimensions. So you notice that

[22:07] this is the same shape as that. Uh and

[22:10] so uh

[22:11] then we just have a residual connection

[22:13] which helps with stability in training

[22:14] so that the gradients will flow nicely

[22:16] through the network.

[22:17] Uh and then um that's actually that's

[22:20] the attention uh layer. So I know this

[22:23] is this is dense uh

[22:25] and might be frightening if you haven't

[22:27] seen it before.

[22:29] I guess

[22:31] Are there questions about what is

[22:33] happening here? Yeah.

[22:34] >> What are the small three dot vectors in

[22:38] Aha, good question. Yes, these are bias

[22:41] biases. So it's just the shape the

[22:44] correct shape and you just add that to

[22:46] everything. So not that important to

[22:47] your understanding, but I included in

[22:49] the diagram. Good question. Yes.

[23:00] >> Uh oh, so we're going to fine tune. So

[23:02] you would randomly initialize all of

[23:03] these weights. So we'll talk about

[23:07] training in a moment, but this will all

[23:09] be randomly initialized. So like when

[23:10] you actually run it the first time, it's

[23:11] going to produce absolute nonsense.

[23:14] And yeah.

[23:19] >> Uh these these are fixed numbers that

[23:21] will be the same

[23:23] for all for everything. Yeah, yeah,

[23:25] exactly.

[23:27] Good question.

[23:29] Any other Yes.

[23:36] >> Yeah, so this is necessary because at

[23:38] training time, I know that my whole

[23:40] sequence is the class was about. So I

[23:43] could have and there are situations

[23:45] where that would be true for

[23:46] bidirectional

[23:48] attention, but in the case that we want

[23:51] to use this now for inference, I cannot

[23:53] say I cannot like have my

[23:56] I cannot be making predictions for for

[23:58] the based on the things that come in the

[24:00] future.

[24:01] So that's why we need to apply this

[24:02] causal attention mask because otherwise

[24:06] our prediction for the thing that comes

[24:08] after the, which you know, should be

[24:10] class, would be conditioned on class

[24:12] already. So so it's it's for that making

[24:14] sure that the training and generation

[24:15] are the same. Yeah.

[24:17] Yes.

[24:18] >> It appears that the causal attention

[24:20] mask is designed based on the

[24:25] order that the vectors are placed in the

[24:27] matrix. So then why do you need on top

[24:30] of that the positional embedding?

[24:33] >> Uh oh uh this is a good question, but

[24:35] basically everything uh here is not like

[24:40] this this will uh

[24:42] operate the same based on uh like I'll

[24:44] show in a second when we do decoding.

[24:46] Like each vector will kind of add on a

[24:48] row here. Um but the uh idea of the

[24:53] positional embedding is like really if

[24:57] you were to run this without the

[24:58] positional embedding like it it wouldn't

[25:00] be able to know like all the

[25:02] multiplications happen in in this order

[25:04] and so like basically uh the and was

[25:08] will you know attend to each other uh in

[25:10] the in the same spot each time, but it

[25:12] wouldn't know that was came before class

[25:14] and and like it it mixes up the order of

[25:16] the of the tokens if you don't have the

[25:18] positional embeddings. Uh I think this

[25:20] is a deeper discussion, but uh it's it

[25:22] is a good question, yeah.

[25:24] Um

[25:26] >> Work just very poorly because it is

[25:28] correct that this is actually the one

[25:29] and only place in which there's actually

[25:30] some ordering information in the

[25:31] network, but it's so little of it that

[25:34] the networks generally don't pick it up.

[25:36] Thank you.

[25:36] >> Works for our architecture, so it's good

[25:38] to get get thoughts, yeah.

[26:19] Thank you, yeah. Sweet. Uh I think maybe

[26:22] I'll take one last question, but then I

[26:23] do have to move on cuz I have a lot of

[26:25] slides.

[26:27] Uh any other burning questions about

[26:29] attention?

[26:31] Cool. All right, I will move on. So uh

[26:34] the next thing is just multi-headed

[26:36] attention uh which is actually kind of a

[26:38] simple extension to attention. We're

[26:40] just going to stack the weight matrices

[26:42] and so you can imagine we're just

[26:43] stacking everything here and doing it a

[26:44] bunch of times. Uh the next thing we

[26:46] have to do is just concatenate those

[26:48] outputs. So I had the three stacked. I'm

[26:50] just going to put them next to each

[26:51] other and then I'm going to project uh

[26:54] with a bigger projection matrix, but I'm

[26:55] still going to end up with the same

[26:56] size. So just so you know like the one

[26:59] attention thing I showed you isn't

[27:00] actually what people do. They do this

[27:01] multi-headed attention and it lets you

[27:03] have uh different you know

[27:05] representations for the same sequence so

[27:07] you can do multi you can kind of have

[27:09] multiple ways of representing the

[27:10] sequence uh and stack them on top of

[27:12] each other.

[27:13] Uh so we'll take this uh we'll just call

[27:15] it our attention layer

[27:19] uh multi-headed causal self-attention

[27:20] layer

[27:21] and then we'll take the layer norm of

[27:23] that and we will uh attach our residual

[27:27] connection and just have a traditional

[27:28] feed forward which is just a matrix

[27:30] multiplication. So it's simple uh and

[27:32] then we uh add a residual there and this

[27:35] all together is what is called a

[27:38] transformer block and then to make it a

[27:40] deep neural network we stack a bunch of

[27:42] these and that is actually you know

[27:45] roughly uh oh and then we have a

[27:46] language modeling head which is just the

[27:48] shape of your vocabulary that will go

[27:50] from this hidden dimension back to the

[27:52] number of tokens in your vocabulary and

[27:54] that is how we ultimately get uh our

[27:57] final vectors. So we'll take that. We

[27:59] can split this back up because remember

[28:01] we kind of like made this for

[28:02] representation purposes. Stack them all

[28:04] like this. We unstack them and then uh

[28:08] right here is our last prediction. So

[28:11] that

[28:12] is our prediction of the next token. So

[28:15] you'll remember that we had this and

[28:17] this is how we can then you know make

[28:19] our prediction about what the next token

[28:21] should be.

[28:22] So

[28:23] that is how a transformer works. Um

[28:26] hopefully that wasn't too bad to follow.

[28:29] I know it was a little bit you know in

[28:30] the weeds, but I think it's important.

[28:33] So, any questions about

[28:37] Cool. Then uh I'm going to talk about

[28:39] attention versus recurrence. So, uh if

[28:41] you look here, this is a table from the

[28:43] original Attention Is All You Need

[28:44] paper. Uh and so we're looking at the

[28:46] complexity per layer here. Uh and this

[28:50] is um also the number of sequential

[28:53] operations. And so the uh O of 1

[28:56] sequential operations is a huge deal for

[28:58] parallel training on GPUs. And this is a

[29:01] big reason why Transformers were as uh

[29:04] incredible as they were is because, you

[29:06] know, we can I showed you uh that whole

[29:08] thing we processed all four of those

[29:10] tokens all at once. So, if you have a

[29:12] huge corpus of text, you can just do a

[29:15] forward pass through your model and you

[29:16] get um you know, it's O of 1 in order to

[29:19] process this whole sequence of text, uh

[29:22] one forward pass through the model.

[29:23] Whereas a recurrent model, which I

[29:25] didn't get to picture, but hopefully you

[29:27] remember that, you know, you generate a

[29:29] a token, you get a hidden dimension, and

[29:31] you get to use that to generate the next

[29:32] token and the next token and the next

[29:33] token. That's O of N in the sequence. Um

[29:36] but on the other hand, O of N squared in

[29:38] the sequence length means that long

[29:40] context becomes extremely expensive for

[29:43] uh Transformer models.

[29:45] Um but at the time, this is a table from

[29:47] the paper. Uh Transformers were better

[29:50] and cheaper. Uh you can see, funny

[29:53] enough, big in this table here when

[29:55] they're comparing to all these

[29:55] architectures, I think it was about 200

[29:57] million parameters or so, uh which if

[30:00] you know, large language models today

[30:01] are in the trillions of parameters. So,

[30:03] this would not be considered a big This

[30:05] would be extra extra extra small in

[30:07] today's tables. Uh but that is uh you

[30:10] know, Transformers for you.

[30:12] Um so then I'll quickly talk about

[30:14] linear attention, which is just um going

[30:16] to be a way that we're going to

[30:17] manipulate the uh attention layer here.

[30:20] Um and this is going to help us with

[30:22] some of that O of N squared context

[30:24] length issue. But basically, um we're

[30:27] going to go and we're going to drop the

[30:30] softmax, uh which now means that this

[30:33] whole sequence of matrix multiplications

[30:35] is linear

[30:38] um is is linear, which means that we can

[30:40] change the associativity. Um so what

[30:42] we'll do is instead multiply uh K and V

[30:46] instead of Q and K.

[30:49] Uh so I'll show you what I mean by that.

[30:50] We're going to take this and now you can

[30:52] see we have a 3 x 3 uh matrix here,

[30:55] which is the dimension of the the hidden

[30:58] dimension, not the sequence length. So

[30:59] we had a 4 x 4 matrix before. Now we

[31:01] have a 3 x 3. Um and this is our state.

[31:05] Uh and so it's S1 denoted because we

[31:07] only have one token so far. Um and we're

[31:10] going to matrix multiply that with Q.

[31:12] And now we're going to uh multiply by

[31:15] our projection and we're going to get

[31:16] our output for the layer. Um and so what

[31:19] is the update rule? How does that

[31:21] change? Well, we clear the memory that

[31:23] we don't need. And what we'll do is

[31:25] slide that state over, save it. And when

[31:28] we generate when we take the next token,

[31:31] what we're going to do is run it through

[31:32] here and we will produce another 3 x 3

[31:35] matrix by multiplying the Q and the V.

[31:37] And we actually just add those together

[31:39] and that is our state. Uh and then we

[31:41] multiply that by K. We get our next

[31:43] thing. We clear, we slide it over, and

[31:46] we can just keep doing this for every

[31:47] token. We just keep updating the state.

[31:50] Um and so this is kind of nice because

[31:54] it means that our memory uh it grow it's

[31:58] is constant. We only have to keep track

[32:00] of the same fixed state matrix here and

[32:03] just keep updating that. But on the

[32:06] downside um all right, and this is what

[32:08] I wanted to say here. Linear attention

[32:09] has is way faster and has a better

[32:11] memory footprint because we have less

[32:13] things we need to store. We can just

[32:15] kind of um store just that state in

[32:17] between the tokens.

[32:20] Um and it's not O of N squared. Now it's

[32:23] D squared, the the the dimension of the

[32:25] model. Um but on the other hand, it

[32:28] struggles with long context. So this is

[32:30] a benchmark that's doing needle in a

[32:31] haystack. So you'll give it an essay and

[32:34] say one of the special magic numbers is

[32:36] this. And then you have more text and

[32:39] then asked like what was the special

[32:40] magic number? And if you think about

[32:42] what's happening to happen in the model,

[32:44] it needs to somehow remember all of this

[32:46] in that little condensed matrix. Instead

[32:48] of being able to say when I ask what is

[32:50] the special number, I attend back to the

[32:52] sequence and find it. I have to have

[32:54] remembered this whole way through

[32:55] condensed into that matrix. So it it

[32:57] matters for long context. You can see um

[33:00] llama is uh is the standard attention,

[33:03] whereas RWKV and Mamba use this linear

[33:06] attention and they degrade more on

[33:10] longer sequence tasks.

[33:12] Uh and a note about context length is

[33:14] that nothing in the transformer or

[33:15] linear attention enforce a strict

[33:17] context length

[33:18] except for the positional embeddings,

[33:21] which means in practice we need the

[33:23] model to learn how to use these

[33:24] positional embeddings. And so our

[33:26] context length limitations come from how

[33:29] long do we train the model?

[33:31] How long context did we train the model

[33:33] with?

[33:34] Uh all right.

[33:36] Uh any questions about that?

[33:38] Otherwise, I think we're going to be

[33:40] moving on. I'm going to do a quick note

[33:41] about bringing it together.

[33:43] Uh full softmax attention is O of N

[33:45] squared in context length, whereas

[33:47] linear attention is O of N in context

[33:49] length.

[33:50] Um in full softmax attention, all tokens

[33:52] can refer back to all prior tokens,

[33:54] which helps for long context.

[33:56] But in linear attention, we have to

[33:58] condense it into that state

[33:59] representation,

[34:00] which makes it harder for long context.

[34:03] In the full softmax, the KV grows in O

[34:06] of N and I'll show that when we get to

[34:08] inference. But in linear attention, the

[34:10] state representation uses constant

[34:12] memory. And so in practice, people will

[34:14] mix these. So DeltaNet here is a linear

[34:17] attention and then we have global

[34:19] attention layers. And so it helps

[34:21] because most of the layers can do this

[34:23] linear attention, but every once in a

[34:24] while we'll have this full global

[34:26] attention to get full interaction. And

[34:27] you can see that that helps on these

[34:30] tasks. For example,

[34:32] the retrieval, which is this task of

[34:34] pulling things from your context,

[34:36] improves when you add either sliding

[34:38] window attention or global attention is

[34:40] the one that I I I was talking about.

[34:42] Um, whereas like common sense, uh,

[34:45] asking a very simple question, uh, which

[34:47] you don't need to think back to your

[34:48] context for, uh, does not degrade when

[34:50] you add that. So this is just like an

[34:52] architecture change here. And then the

[34:54] last thing is like Kimi K 3 is obviously

[34:56] like a pretty hot model to talk about

[34:58] right now. It's like one of the best

[34:59] open models available. And now, uh, if

[35:02] you look at the architecture, ideally

[35:04] you'll have a little bit of a sense of,

[35:05] you know, what's going on here. We have

[35:06] linear attention, feed forward, uh,

[35:09] multi-head, uh, attention, which is what

[35:11] I talked about, although it does it on

[35:12] latents. Um, so there's a some

[35:14] modifications here. Um, and also there's

[35:17] like gates in the linear attention, but

[35:18] roughly speaking, like you get at a high

[35:20] level, you know, what's going on in

[35:22] these, uh, modern state-of-the-art large

[35:24] language models.

[35:25] Uh, so why does all this matter for

[35:27] agents? Well, agents have to deal with

[35:28] extremely long contexts and inference

[35:30] efficiency is a design consideration in

[35:33] building these agentic systems. Uh, so

[35:35] knowing the underlying model

[35:36] architectures will help you select the

[35:38] right model for your agentic

[35:39] application. And when you're developing

[35:42] a harness or a scaffold for the agent,

[35:44] it'll help to know the limitations of

[35:46] that model, like am I going to be using

[35:48] a a model with a linear attention and

[35:51] uh, maybe in this case I should use a

[35:53] model with, you know, uh, full global

[35:55] attention because I'm handling long

[35:57] context tasks and stuff like that. And

[35:59] it gives you some vocabulary to talk

[36:00] about these things and and try things

[36:02] out.

[36:03] Uh, so that is the architecture section.

[36:05] Uh, I'm going to move on now to language

[36:07] model training.

[36:09] Um, and we're going to start by defining

[36:11] the loss function. Uh, for any deep

[36:14] learning, uh,

[36:16] model you need to have a loss function,

[36:18] uh, that will help you update, uh, the

[36:20] weights of the model based on, you know,

[36:22] how far off it is from completing the

[36:24] objective.

[36:25] And so I'm going to give you an example

[36:26] of a training data, uh, a piece of

[36:28] training data, um, that that we'll use

[36:30] this as training data. It's going to be

[36:32] uh, the class was about how agents work

[36:34] and how to build AI systems. So it's a

[36:35] little thing about about our class. Um,

[36:38] and you'll see these the class was about

[36:40] because I've been using that as our

[36:41] token in this whole time. And so we

[36:43] have, uh, if you remember we have the

[36:45] classes about, we have all of these uh

[36:48] probabilities of the next token uh that

[36:50] we can model here and we look at our

[36:53] training data and we said the class was

[36:55] about how agents work. So how is the

[36:58] actual ground truth next token? Uh and

[37:01] that was one of the things that our

[37:03] model gave some probability mass to. Uh

[37:05] so that's uh that's good. It was like

[37:07] one of the one of the top things. And

[37:09] what we'll do for our loss function is

[37:11] we're going to take the uh negative log

[37:15] of the probability there uh from the

[37:17] model and say that that is our score

[37:20] that we're assigning. So the model if it

[37:22] had given a higher probability to this,

[37:24] it would have scored a lower loss which

[37:27] is uh good you want to have a lower

[37:29] loss. Um and so what we'll do is this is

[37:33] called the cross entropy loss. It's

[37:35] basically for every token in your

[37:36] vocabulary uh you're going to take this

[37:39] sort of like indicator where this is a

[37:41] one when the token is in the data uh

[37:44] sorry when the token is the next token

[37:45] that you should have predicted. It's a

[37:47] zero when it is not the token that you

[37:49] should have predicted. Uh and then we'll

[37:51] just take the log of the probability of

[37:52] what the model generated for that token

[37:54] and we can use that to train the model

[37:56] um.

[37:58] So that uh that's just a kind of quick

[38:00] summary of what the loss function is. Um

[38:03] any questions?

[38:06] Excellent. Then we'll talk about

[38:07] pre-training and this is all going to be

[38:09] a bit at a higher level. So uh you can

[38:11] take a breather because I know the

[38:12] attention was very very deep. This we're

[38:15] going to be kind of just talking at a

[38:16] high level. So pre-training uh the way

[38:19] that we process our data is uh in a lot

[38:22] of ways it's we get data from the

[38:23] internet. Uh so um we start with these

[38:26] HTML files that are taken from these web

[38:29] scrapes uh these crawls of the internet

[38:32] and we extract the text from them using

[38:34] rule-based extraction tools uh that will

[38:36] turn it from the raw HTML that you you

[38:40] know has to be rendered by a browser

[38:42] into just like plain text. So you can

[38:43] these are things like Mozilla parse

[38:45] trafulatura. There's like a bunch of

[38:47] tools for this. You'll run a language ID

[38:49] on it, depending on if you want it to be

[38:50] an English data set or not. Uh then

[38:53] there's all these rule-based filters

[38:54] that say like, oh, if the uh if there's

[38:57] this many symbols compared to letters in

[38:59] the document, it might be kind of junk

[39:01] data um or if it has, you know, too many

[39:04] repetitions of the same sequence of

[39:06] text, it might be junk because it's

[39:07] really trying to find the highest

[39:08] quality data. Then you run a model uh

[39:11] that does quality filtering. Uh you

[39:13] deduplicate the data, so if the same

[39:15] page shows up a bunch of times, it's not

[39:16] repeating in your training data because

[39:18] that's bad for the model. It's uh you

[39:20] don't want to epoch on your data too

[39:21] much, although there's exceptions to

[39:23] that. Uh and then you produce your final

[39:25] training data. So an example of this is

[39:27] like DCLM is a uh open source effort to

[39:30] train model or to to produce the highest

[39:32] quality training data that they possibly

[39:34] can and they've made it like a

[39:35] competition. And so you can see what

[39:37] they they how they actually fill out

[39:38] filter out their data. So we have um the

[39:41] common crawl. Maybe I should do this

[39:42] with my mouse just so it's uh easier for

[39:44] people online. Uh so we have the common

[39:47] crawl, which is all of the uh documents

[39:50] on the internet that they've pulled. And

[39:53] you can see they filter out some using

[39:55] the English filter, which actually

[39:56] filters out a lot of the content. They

[39:58] have all of these like word length

[39:59] filters, page length repetition. Uh they

[40:01] have the deduplication, model based

[40:03] filtering and stuff. And finally they

[40:04] keep 1.4% of the content that they

[40:07] process and that's that's what they'll

[40:09] train on. Uh yeah.

[40:10] >> Is it just like .txt files I think

[40:13] >> It basically, yeah. I mean it's it's

[40:16] it's, you know, the actual like when you

[40:18] write the code, you can, you know,

[40:19] manipulate it as you want. But it it is

[40:21] just text, yeah. Yeah.

[40:23] Um

[40:24] yeah. I mean you have to tokenize it and

[40:26] then uh but yeah.

[40:28] Um and then uh this is another example

[40:30] of a data set. So this one was math

[40:32] focused and so they they applied

[40:34] additional math filters and stuff like

[40:36] that. But you can see like generally

[40:37] these sequences look very similar. It's

[40:39] like you take the raw data, you filter

[40:41] it, you turn it into text, uh you know,

[40:43] and then you deduplicate and

[40:45] decontaminate and you end up with like a

[40:46] nice distribution of text based on what

[40:48] you're trying to get.

[40:49] Um, and so I I pulled some examples of

[40:51] data from DCLM so you can get a sense

[40:53] that like the data that models are

[40:55] training on is a little wacky sometimes

[40:56] and like kind of uh

[40:59] you know there's there's some quirks to

[41:01] the data. So uh this is like I I

[41:03] randomly pulled these documents, but

[41:04] this looks like uh some sort of anime

[41:07] about hacking that somebody wants to

[41:08] find. So it's some forum. Uh so the

[41:10] model would be trained to predict the

[41:11] tokens here. Uh we have um something

[41:15] about like the Culinary Institute of

[41:16] America and this is like the start of an

[41:18] article about about that. Um we have uh

[41:22] this is like a programming thing. So

[41:24] some EO shift function in assembly

[41:26] language and it just happens to be on

[41:28] the internet that there's documentation

[41:29] for this. Uh so you can see this is

[41:31] after extensive filtering. This is the

[41:34] type of data that that you end up

[41:35] training the model on. It's very very uh

[41:37] like disparate topics to try to get the

[41:39] model to have a broad knowledge. Um and

[41:42] so uh then if you look in the middle

[41:44] here this is the internet but this is uh

[41:47] this is a data set that was publicly

[41:48] released called the pile. Um and so they

[41:51] also pull from academic sources um

[41:54] dialogue miscellaneous things. Um uh

[41:56] there was I think some books included in

[41:59] this originally, but they may have been

[42:01] removed for for copyright. Um but um

[42:04] essentially this is like you'll collect

[42:06] other sources besides the internet and

[42:08] then what you have to do is mix them

[42:09] together. I I think it's in the interest

[42:11] of time not worth talking too in depth

[42:13] about this, but basically the idea is

[42:15] that you train a bunch of really small

[42:17] models or there's you have to have some

[42:18] sort of proxy to predict is this

[42:20] distribution of data actually useful for

[42:22] what I care about? Uh and then you

[42:24] optimize the mixture. So you say like

[42:25] okay I want 30% of my content to come

[42:27] from the internet. I want 20% to come

[42:29] from GitHub. I want you know so you set

[42:30] those weights. Um

[42:32] and then we go on to mid training

[42:35] which is where you change your data mix

[42:37] to be focused more on your target

[42:38] domains. So this is an example from uh

[42:41] Marin which is this open language

[42:42] modeling effort. Uh they're training

[42:44] their model in the open right now and

[42:45] you can see they've got two data mixes

[42:47] here. They've got their pre-training mix

[42:48] and their cooldown mix. Uh and you can

[42:50] see the the weights that they put on

[42:52] everything changes. So the quality they

[42:55] they put a little bit more weight on

[42:57] like business software in the cool down

[43:00] phase of training than what they had put

[43:02] on during pre-training.

[43:04] And there's just some evidence in the

[43:06] literature that mixing in more of your

[43:08] target domain data during, you know,

[43:10] pre-training, mid-training tends to

[43:11] help. So what this is showing here is

[43:13] like when you have a specialized domain

[43:17] like math or something that you want to

[43:18] make your model especially good at,

[43:21] if you mix it into the pre-training data

[43:24] and then you fine tune on this data

[43:26] later, then your domain test loss, which

[43:28] is like math test loss, will get better

[43:31] with the specialized model. But

[43:32] interestingly, it doesn't like after you

[43:35] do this fine tuning, it actually even

[43:36] seems to help with like other domains as

[43:38] well. So it's it's good that if you know

[43:40] what you're going to fine tune your

[43:41] model for, you mix a little bit of that

[43:42] into the pre-training data.

[43:45] And then the kind of intuition for this

[43:47] is like that your mid-training, so

[43:49] eventually you want to have the model be

[43:51] good at doing, you know, specifically

[43:53] responding to queries or doing agentic

[43:55] tasks or things of that nature.

[43:58] So that is the like theta target where

[44:01] you want to get to, but mid-training can

[44:03] kind of be a way to bridge bridge that

[44:05] gap.

[44:07] And then I will talk about

[44:08] post-training. So post-training comes

[44:11] from

[44:12] a couple of things that we do for

[44:13] post-training. So one is instruction

[44:15] fine tuning, which is still important

[44:17] and relevant today, where we basically

[44:19] give models an instruction. So this is

[44:23] kind of like also called like, you know,

[44:25] supervised fine tuning as a part of the

[44:27] phase of training where we'll say like,

[44:29] okay, please answer the following

[44:30] question, you know, what's the boiling

[44:32] point of nitrogen? And we have the

[44:33] answer and we have it in a in a nicely

[44:36] written like thing that we want the

[44:37] language model to actually say and we're

[44:38] going to just update the model to to

[44:40] speak more like this chat assistant and

[44:41] stuff like that. So this is like very

[44:43] focused data, nothing like how we had on

[44:45] the internet where we are going to throw

[44:46] everything at the model. This is very

[44:48] specifically tuned to how we want the

[44:50] model to actually behave.

[44:52] We'll also do some learning from

[44:53] preferences. So, the idea here is uh we

[44:57] uh this is from the original like

[44:59] instruct GBT paper um

[45:01] behind like

[45:02] chat GBT eventually. Uh and the idea was

[45:05] you have uh a prompt where uh somebody,

[45:09] you know, writes a response and then you

[45:11] SFT on that. So, that's what I was

[45:13] talking about in the prior slide. Then

[45:14] what you do is you have a prompt and you

[45:16] generate a bunch of responses and you

[45:18] ask people which ones do you like, which

[45:19] ones do you not like, please rank them,

[45:21] and use that to train a model that

[45:23] predicts what people like and don't

[45:24] like. And then you use reinforcement

[45:27] learning on the model in order to make

[45:29] the model generate more of the things

[45:31] that people like and less of the things

[45:32] they don't like. However, there are some

[45:34] problems with human feedback. I mean,

[45:36] for one, human annotations are

[45:37] unreliable. So, I've done some studies

[45:39] on personalization, for instance, and

[45:41] you'll ask somebody which response do

[45:42] you like better, you know, this one or

[45:43] this one? Uh and then they'll tell you,

[45:45] oh I I like this one, you know, it was

[45:47] uh it was a bit more it was styled in a

[45:50] way that I really liked. And you can ask

[45:52] them like a few weeks later like the

[45:54] same thing like which one do you like

[45:55] better? And they're like, oh I like the

[45:56] other one, it was a bit more to the

[45:57] point. Uh so, it's like uh people's

[46:00] preferences are not consistent. And so,

[46:02] this is a this is tricky. Uh everyone

[46:04] also has different preferences. Uh so,

[46:06] it's also when you say like I'm we're

[46:08] RLing on human human preferences, what

[46:10] does that actually mean? Uh it can lead

[46:13] to bad incentives for model

[46:14] optimization. Uh for example, people

[46:16] like it when the model says good things

[46:17] about them. And so, the models can

[46:19] become kind of sycophantic.

[46:21] Um and also uh

[46:23] originally um the data could have been

[46:25] sourced kind of unethically and you

[46:27] know, it's there's still some some

[46:29] questions about the data sourcing, but

[46:30] definitely there were annotators uh in

[46:32] very low income areas being paid to look

[46:34] at really nasty data, uh not very much

[46:37] money. So, there was a lot of that going

[46:39] on. And even today, the working hours of

[46:41] some of these data workers are are not

[46:43] great. So, it's it is important to think

[46:45] about the considerations of of the human

[46:48] feedback here.

[46:49] Um so, one thing uh we can do otherwise

[46:52] is uh reinforcement learning with

[46:54] verifiable rewards. And instead of

[46:56] having the reward model be a try trying

[46:59] to predict what humans like or don't

[47:01] like, uh we can actually rely on things

[47:03] that we can have a ground truth of is

[47:05] this correct or not? Uh and so we can

[47:07] make the reward verifiable, uh which is

[47:10] really great for math and code for

[47:12] instance because we can check was the

[47:13] answer correct. Um and then you apply

[47:16] your reward based on, you know, did you

[47:18] pass these test cases in the code when I

[47:21] generate uh an answer or did I get the

[47:23] correct answer to the math problem? Uh

[47:25] and so that that is uh another way that

[47:27] we can do this uh reinforcement learning

[47:29] to make the models better. Um

[47:31] and then uh I wanted to talk about agent

[47:34] specific training a little bit. Um uh so

[47:37] one thing that we can do is try to get

[47:39] coding specific tasks. And so what they

[47:41] did in this paper, this is just an

[47:42] example, there's many papers like this,

[47:44] uh but they will take uh

[47:47] GitHub repositories and have an existing

[47:49] agent turn this into like try to install

[47:52] the repo and see if they can get it

[47:54] working. And if it can, then they'll

[47:55] make a Docker image out of this repo and

[47:58] they'll procedurally generate bugs in

[48:00] the repo. So they'll like reverse a PR

[48:03] using a language model to say like undo

[48:04] all the changes here. Uh they will uh

[48:07] take uh functions in the the code and

[48:10] purposely introduce bugs into them and

[48:12] and stuff like that. And then they

[48:13] generate like a a description of like oh

[48:16] uh please solve this task, you know? And

[48:17] and if it passes all of the test cases

[48:20] when it solves the task, then we can say

[48:22] that the model was successful here. And

[48:24] we can just train on a bunch of this

[48:25] synthetically generated environment. Um

[48:27] so uh this uh paper showed that they

[48:30] were able to get a uh Quen 2.5 like 32B

[48:34] model up to like 40% on this Swe-bench

[48:36] verified task where I think it started

[48:38] off around like 9% or something like

[48:40] that. So just by doing the synthetic

[48:42] data where you're generating all of

[48:43] these things uh in the uh in the

[48:46] repository all introducing bugs and then

[48:48] training on the solutions. Um

[48:51] so that's uh and and it can be the model

[48:53] itself that's, you know, generating the

[48:54] solutions and you're just checking them

[48:55] against the test cases.

[48:57] So

[48:58] that is all I wanted to talk about for

[48:59] training. I think we have about a half

[49:01] hour left, which is good because I have

[49:03] um a a good amount of content for

[49:05] inference and LLMs for agents. So, uh

[49:07] any any questions though before I move

[49:09] on about like how we train large

[49:11] language models to be agents?

[49:14] Yes.

[49:15] >> For uh training for model tasks kind of

[49:19] last days or maybe even weeks, what type

[49:22] of training data is typically used?

[49:25] >> That's a good question. So, one thing I

[49:26] didn't actually mention is um long

[49:29] context extension is an important part

[49:31] of training too. So, this happens um in

[49:34] the So So, I'll answer your question

[49:36] specifically and then also mention long

[49:37] context extension happens like because

[49:39] we train pre-training on like a certain

[49:41] token length, and then we also care like

[49:43] the model should be able to process

[49:45] really really long

[49:46] context as well. So, you can extend out

[49:49] and train on longer docs during

[49:50] pre-training as well because I mentioned

[49:52] that we have to train those positional

[49:53] embeddings. For long horizon tasks, a

[49:55] lot of it is these like agentic

[49:56] environments. So, there's a lot of

[49:58] companies out there that are producing

[50:00] RL environments. It's a very lucrative

[50:02] business to be in these days um where

[50:04] you basically do what I just talked

[50:06] about in that that last slide about

[50:08] creating environments in in repos and

[50:10] stuff like that. And what uh these

[50:12] companies will do is either hire people

[50:14] or create very very very high quality

[50:16] synthetic data uh where they are taking

[50:19] these repositories and making it like a

[50:21] really long hard task, and you can

[50:23] either use that to evaluate is our model

[50:25] good or you can use it for training. And

[50:27] it is the same sort of RL environment

[50:29] setting.

[50:31] Uh code is one of the most popular ones

[50:32] for sure. There's There's lots of work

[50:34] on like trying to make them productive

[50:36] for work and using like GDP val related

[50:38] things and stuff, but code is by far the

[50:40] the easiest and most common one, yeah.

[50:45] Uh yes.

[50:48] >> data quality someday as all the human

[50:50] wisdom or can we are there already?

[50:52] >> Yeah, this is a good question. I uh I

[50:55] have a lot I could say about this

[50:57] because I have um I have a paper coming

[50:59] out that's kind of related to how we can

[51:02] make pre-training data better uh and and

[51:05] push the internet further for our

[51:07] pre-training. I think eventually a lot

[51:09] of data these days is synthetic. Uh so I

[51:12] mean every day trillions of tokens are

[51:14] generated and to pre-train a model you

[51:17] typically don't use today uh in an open

[51:20] model you don't use more than like 36

[51:22] trillion tokens to train the model. So

[51:25] we actually have the like infrastructure

[51:27] ability to completely generate our

[51:29] pre-training data at this point in time.

[51:31] It's not recommended because

[51:34] the diversity of the internet is

[51:35] actually its strength. Um

[51:38] but I think that we will

[51:40] like reach a time where yeah we've

[51:43] saturated on what we can get out of the

[51:44] internet and we have to rely on things

[51:46] like RL to push the models further. Um I

[51:48] think that that's potentially true. It's

[51:50] a good question. Mhm.

[51:52] Yeah.

[51:54] >> Versus between pre-training and

[51:55] mid-training?

[51:56] >> It's honestly a very vibes thing. So so

[52:00] I mean not a it's not a super concrete

[52:02] answer there but really it's mostly like

[52:04] you might change you might change

[52:06] something about the learning rate

[52:07] cooldown but really you're just changing

[52:09] the data distribution and I think the

[52:11] way that people have described it to me

[52:13] is pre-training you really don't know

[52:15] what the heck is in your data. Um

[52:17] mid-training you have a sense that like

[52:20] we probably got some good math and stuff

[52:22] but I'm not looking at that data that

[52:23] much. I mean I'm looking at samples but

[52:25] I don't really know what's in that data

[52:26] that well. Uh it's just a volume still

[52:29] matters quite a bit and then

[52:30] post-training it's like yeah I really

[52:31] know what I post-training the model on.

[52:33] Uh so that's that's kind of the

[52:36] vibes based sort of

[52:38] yeah.

[52:39] Yeah. All right I'm going to move on in

[52:41] the interest of time and we're going to

[52:43] talk about LLM inference now. Um so

[52:46] we're going to talk about prefill and

[52:47] decode which are the two stages. So this

[52:50] is going to be a little systemsy. Um so

[52:53] hopefully that's interesting to folks.

[52:55] Um we're going to talk about GPUs for a

[52:57] moment. So this is the kind of hierarchy

[53:01] of a GPU

[53:02] as opposed to a CPU. With a CPU, uh if

[53:05] you've taken, you know, some some intro

[53:07] CS uh

[53:08] classes, you'll know that they have

[53:10] arithmetic logic units that you will use

[53:14] and you'll dispatch instructions to the

[53:16] arithmetic logic units and they'll you

[53:18] know follow those instructions and then

[53:19] mainly you're processing

[53:21] and you have like this the central

[53:23] processor is dispatching to the the

[53:25] ALUs. But in a GPU, we actually are we

[53:28] care way more about like massive amounts

[53:30] of computing power and less about the

[53:32] you know control and like being able to

[53:34] branch and and um so what we actually

[53:37] care about is just

[53:38] maximize, maximize, maximize the amount

[53:40] of

[53:41] compute power and then we just want to

[53:44] throw a bunch of parallel operations at

[53:45] it. Um so there's this roofline

[53:47] performance model

[53:49] and the idea here is peak flops per

[53:51] second is the absolute maximum that your

[53:55] chip is able to handle in terms of how

[53:58] much compute that you're processing at

[54:00] any given time. So flops is floating

[54:01] point operations and so flops per second

[54:04] we're looking at how many

[54:06] basically like you can think of how many

[54:08] multiplications can I do in a second. Um

[54:11] and then what we have is bandwidth

[54:13] gigabytes per second and so this is

[54:15] about data transfer. So because to

[54:17] actually run something on the GPU, you

[54:19] need to get the data there. So like if I

[54:22] need to you know I need to

[54:24] have my

[54:26] I I need to pulse like my KV cache from

[54:29] a different part of memory and stuff.

[54:30] Like this is how much it takes to move

[54:32] the data onto the GPU. And so when we

[54:35] have

[54:37] when we have fewer

[54:40] like gigabytes per second

[54:42] getting to the GPU than it can actually

[54:43] process, we are bound by memory and it's

[54:46] about how

[54:47] how much time it takes to actually

[54:48] transfer the memory into the GPU.

[54:51] When we are above that point, now we're

[54:53] bound by compute and the thing that's

[54:55] bottlenecking us is like how powerful is

[54:57] the chip.

[54:58] So this is important because prefill and

[55:01] decode will actually be bottlenecked in

[55:03] different ways.

[55:04] So

[55:05] Uh,

[55:06] is kind of what I you before. Uh, so

[55:09] we're going to process the entire

[55:10] sequence at the same time. So you can

[55:12] imagine this is like I have my whole

[55:14] prompt. I say uh

[55:17] this is still sort of next token

[55:19] prediction on the same sequence. But

[55:20] like you can imagine I send my prompt

[55:21] off to ChatGPT. I say like help me with

[55:23] uh revising my essay. I paste my essay

[55:25] in. Well, I have all of those tokens

[55:27] already ready to go. So I can process

[55:29] them all in one uh forward pass here and

[55:32] that will get me um to be quite compute

[55:35] bound because there's a lot of matrix

[55:36] multiplications happening. But when

[55:38] ChatGPT is determined it's ready to

[55:40] respond, you know, and it's processed

[55:42] all this, now we care about the next

[55:43] token. So uh because it was easier for

[55:46] me to to write the visualization, I

[55:47] didn't uh change like to make this an

[55:49] extension. But you can imagine like

[55:51] we've processed the prompt and now we're

[55:53] going on to the next part. So we start

[55:54] with the and we send that over and now

[55:57] we just have a single vector uh for all

[55:59] of this. Um and then we can clear out so

[56:02] so remember we have the attention here

[56:04] that we talked about earlier and now

[56:06] it's like just the top row. Everything's

[56:08] just the top row here. Um and then uh we

[56:11] can clear out everything that we don't

[56:12] need for the next token uh which is

[56:14] everything really besides the the K

[56:16] activations and the V activations. And

[56:19] then we have our next token. So we fill

[56:21] in the second row for everything here uh

[56:23] and then we clear everything out and we

[56:25] fill in the next one and we fill in the

[56:26] next one. And what you'll notice here is

[56:29] like everything is uh clearing out for

[56:31] the most part except for we need we

[56:33] always need these full K and V

[56:35] activations uh to generate the next

[56:37] token. And so this is actually called

[56:39] the KV cache uh which we which is

[56:42] important um and we'll talk about you

[56:44] know managing the KV cache in a bit. Uh

[56:46] but this is like what grows in memory

[56:48] when we're doing decode on a language

[56:50] model.

[56:51] Um and so if we go back to this roofline

[56:53] performance model uh

[56:55] I just talked about uh prefill and

[56:57] decode. So prefill is compute bound

[56:59] because we're doing a ton of these

[57:00] matrix multiplications on not that much

[57:02] data. We just have to load the initial

[57:04] weights in uh and the the mod uh the

[57:06] embeddings for the uh uh

[57:09] and then we can just process it, you

[57:10] know? But uh in the decode phase now

[57:13] we're not actually saturating as much on

[57:16] uh how what our actual maximum

[57:18] performance could be and so now we're

[57:19] back to like being memory bound and so

[57:21] there's interesting ways that we can try

[57:23] to make the memory transfer more

[57:24] efficient and stuff like that. Um but

[57:26] the metrics to care about are time to

[57:28] first token for prefill and time per

[57:31] output token for decode. Um and so

[57:34] uh

[57:35] one thing that you can do to improve

[57:37] this Oh, I had a I had a nicer version

[57:38] of this slide is that you have um

[57:41] speculative decoding. So uh because we

[57:45] what we would like to do is be able to

[57:46] process a bunch of tokens at a time to

[57:49] make us better saturate the amount of

[57:51] compute we have available. What we could

[57:53] do is have a tiny model that we generate

[57:55] a bunch of tokens with uh and that is

[57:57] decode. So this is you can see is decode

[57:59] once upon a time there. Uh we've run the

[58:02] one token at a time decode and then we

[58:05] have our actual model that we care about

[58:07] as like our our main model our our

[58:09] bigger model that we trust uh and we can

[58:11] actually process them all at the same

[58:13] time. And so this is one of these ways

[58:14] like there's different different tricks

[58:16] that you can use to try to get more

[58:17] efficiency out of things. Uh but this is

[58:19] all kind of like

[58:21] sort of this philosophy I have of like

[58:23] we're peeling it back because like if

[58:24] you want to make things faster maybe you

[58:25] can use speculative decoding for

[58:26] instance and that's that's a tool. Yeah.

[58:31] >> work [clears throat] of the smaller

[58:32] model or

[58:33] >> Exactly. So what we do is like we run it

[58:35] the same way and we get the the log

[58:36] probs for each of these things and then

[58:38] we'll see um depending on our decoding

[58:40] strategy like let's say we were using

[58:41] decoding greedy decoding where the most

[58:45] probable next uh the the the thing that

[58:48] we always pick is the thing that was

[58:50] most likely to be generated. Uh then we

[58:52] would check for all of these was that

[58:54] actually the thing that would would have

[58:55] been most likely to be generated in that

[58:57] position. Um and so and then you can

[59:00] reject like if I rejected it at the A

[59:02] spot instead of there then I would have

[59:05] gone back to the draft model and

[59:06] continued from there instead of So this

[59:08] is like how we can speed things up

[59:10] because we we

[59:11] rejected at a certain point in the

[59:13] decoding, if that makes sense. Yeah.

[59:16] Uh, any other questions?

[59:19] Cool. So speculative decoding uh it

[59:22] leads to nice results here. You can see

[59:24] that changing the number of draft

[59:26] tokens, which is how many things we

[59:28] generate with that smaller model uh

[59:29] allows us to uh improve the sampling

[59:32] time uh and uh we can see the acceptance

[59:36] rate between human eval,

[59:38] [clears throat] confusingly is a coding

[59:39] benchmark and XSum is a summarization

[59:42] benchmark. So you can see that some

[59:43] domains are more predictable because we

[59:44] actually accept more code than we do

[59:47] like summarizations because like

[59:49] maybe code is actually more compressible

[59:51] and easy to to model thing.

[59:53] Um,

[59:54] so uh the last inference thing I want to

[59:56] talk about is inference time scaling or

[59:59] test time scaling and now we're getting

[60:00] back to reasoning models which was

[60:02] brought up earlier. So the first thing

[60:04] is chain of thought prompting. Uh so

[60:07] this is kind of a classic it feels

[60:08] classic to me at this point technique

[60:10] where basically uh you have your prompt

[60:12] and you want the model to reason about

[60:15] generating an answer. So at the time

[60:17] what people do is either put like let's

[60:18] think step by step or you could also

[60:20] have like in the example here you do few

[60:22] shot where you put examples of reasoning

[60:24] in the prompt and you wanted to continue

[60:27] to reason. And the difference is like uh

[60:29] here the model had to just output

[60:31] directly uh whereas in the chain of

[60:33] thought setting the model generated its

[60:35] reasoning before and generating the

[60:37] answer. And so this is a form of test

[60:39] time scaling or inference time scaling

[60:40] because we're actually having the model

[60:42] uh do more spend more compute uh on the

[60:45] task at hand to solve it. Uh and so now

[60:48] we have reasoning LLMs which are trained

[60:50] to do this more uh than just prompted.

[60:52] Um and so uh given a query uh such as

[60:55] this math problem, maybe a traditional

[60:57] LLM even using chain of thought you know

[60:59] would generate a little bit uh but a

[61:01] reasoning LLM has been specifically

[61:02] trained to reason at length. And I'll

[61:05] talk about a little bit how how this is

[61:06] done. Uh but you can see like this uh

[61:09] sequence of text that's generated here

[61:11] has like mistakes where it's like wait

[61:13] uh the the cancellation would require

[61:15] both percentages to so it can catch its

[61:17] own mistakes, it can reflect. And this

[61:19] helps the model be better at the task,

[61:21] but obviously it's more expensive. So

[61:22] this is why it's inference time scaling.

[61:26] And you also get these like aha moments

[61:28] where the model is like reasoning and

[61:30] it's like, wait, that can't be right.

[61:32] And so you can see like this is going to

[61:33] lead to better solutions because the

[61:35] model is less likely to kind of go

[61:37] commit to to making a mistake in its

[61:40] reasoning.

[61:41] So to just make this a little more

[61:43] concrete, if you see model releases

[61:45] today, you'll you'll often see these

[61:47] kind of curves. And what this is showing

[61:50] is like cost per task on the x-axis and

[61:52] score, but cost is really

[61:54] tokens, you know? So when we generate

[61:57] more tokens using different reasoning

[61:58] modes, we can score better on these

[62:00] tasks. In this case, it's agents last

[62:02] exam and this is from the GPT Astro

[62:04] release. But this is another axis of

[62:07] scaling. And then the nice thing about

[62:08] inference scaling as opposed to like

[62:10] weights, parameter scaling and things

[62:12] like that is like this is very much in

[62:13] the hands of the user. You can kind of

[62:14] say like, I know this task is going to

[62:16] be really hard. I'm willing to spend

[62:17] more on it

[62:18] and and scale up the amount of tokens

[62:20] that are spent on that task.

[62:22] So

[62:24] this is kind of the way you set the

[62:25] reasoning level in in GPT-4 for

[62:28] instance.

[62:29] You can actually put it in the system

[62:30] prompt and you say low, medium, high.

[62:32] And and it will generate more tokens for

[62:34] each of these. And the way that this is

[62:36] actually done, there are two models that

[62:39] I'll talk about here. Thinking Machines

[62:41] has their Inkling model. And so remember

[62:43] we were talking about these RL with

[62:44] verifiable rewards where you basically

[62:46] put the the model in a coding

[62:48] environment, have it try to solve the

[62:50] task, and you can verify did it solve

[62:51] the coding task correctly or not. What

[62:53] they'll do is they'll have a reward that

[62:55] they would have already given for the

[62:56] task. And then based on if you would set

[62:59] the reasoning to low, medium, or high,

[63:01] they penalize the number of tokens it

[63:02] took to solve the task differently. And

[63:04] so that's how they encourage the model

[63:06] to learn that when I say low, you need

[63:09] to generate less.

[63:11] And then Kimi K3, what they do is they

[63:14] have a separate reward structure where

[63:16] they say uh get one point for being

[63:19] correct. You get zero points if you're

[63:21] wrong and you actually get negative one

[63:23] points if you're wrong and you exceed

[63:25] the budget. Uh so I guess it's it's this

[63:28] you can think of like the optimum here,

[63:30] but it's I guess nice in a way that like

[63:32] if you if you're going to be right like

[63:34] okay you can go over budget a little

[63:35] bit, but if you're going to be wrong you

[63:36] better not go over budget. Um and then

[63:39] what they'll do is they actually train

[63:40] nine models. They have a general task,

[63:42] general agent, and a coding agent which

[63:44] is like these domain specific training

[63:45] environments where they specifically RL

[63:47] the model in high, medium, low reasoning

[63:49] and then they do um multi teacher

[63:52] distillation where they basically train

[63:53] the outputs of these models into one

[63:56] student model which is you know the Kimi

[63:57] K 3 model that they release.

[64:00] So um the other things I was going to

[64:02] talk about briefly is like you can

[64:03] sample a bunch of times. There's another

[64:05] inference time strategy where if you

[64:07] have a hard verifier you can check the

[64:09] answers so you can just generate a bunch

[64:11] and then you can say okay I found one

[64:13] that's correct. Um and then this leads

[64:16] to nice scaling properties where you can

[64:17] see the number of samples scales with uh

[64:20] how many times you can get the task at

[64:22] right at least once. It's kind of

[64:24] intuitive, but it's worth noting. Um

[64:27] and then uh what if you don't have a

[64:28] verifier and you want to do this? Well

[64:30] what you could do is actually generate

[64:33] the answer multiple times and use the

[64:35] self-consistency as your verifier. So

[64:37] what we we have here is like uh we had

[64:39] this uh model trying to solve a math

[64:41] problem. It said the answer is $18, $26,

[64:44] $18 when we sampled it multiple times

[64:46] and we can say well it said $18 the most

[64:48] so that's the the answer we'll go with.

[64:51] Uh and then this also leads to some nice

[64:53] scaling properties based on how many

[64:55] times you sample and stuff like that.

[64:57] Um all right this is our last topic. So

[64:59] any questions about inference?

[65:02] Otherwise I will talk about LLMs for

[65:05] agents which is I guess what you all

[65:07] came for.

[65:08] So um if you remember from lecture one D

[65:11] had kind of motivated this agent

[65:13] architecture here.

[65:15] Um and the idea uh or what we've been

[65:18] talking about today is the LLM core. So

[65:20] it's going to be worth talking about,

[65:21] you know, how do we structure things to

[65:23] to pass it into this LLM core.

[65:25] Uh so first I'm going to talk about

[65:26] structured input and output.

[65:28] Um and so um increasingly models are

[65:31] being used in these compound systems

[65:33] where we have to call them and call

[65:34] tools and all these things. And so we

[65:36] actually need a shared contract for how

[65:38] these systems are going to communicate.

[65:40] Um and so what one thing we can do is

[65:42] constrain decoding. And so you can

[65:44] actually define um this is the output

[65:47] format that I want. I need a JSON format

[65:49] and I need it to start with summary

[65:51] colon, you know, so I say I'm I'm going

[65:53] to be processing something and I need it

[65:55] to be in this in this particular format.

[65:57] Uh one thing this comes from this

[65:59] library SGLang. Uh they can they

[66:01] actually produce a finite state machine

[66:03] uh for for decoding. And what they do is

[66:06] uh you can see

[66:08] normally what you'd have to do is have

[66:10] the language model generate um you'd

[66:12] have it generate the open like this is

[66:14] one token, the squiggly brace and then

[66:16] the quote and then you process again and

[66:18] now it says summary and then you process

[66:20] again and it puts the closing quote. Uh

[66:22] one thing is like if we know the output

[66:24] we've forced the model to, we could

[66:25] actually go to a finite state machine

[66:27] and only call the model when we don't

[66:30] know like deterministically what the

[66:32] next token needs to be. And even if we

[66:34] have like a branch, we could actually

[66:35] limit the number of like the token the

[66:37] vocabulary to just those two tokens and

[66:39] look at those tokens and stuff like

[66:41] that. So we can actually force the model

[66:43] to respond a certain way.

[66:45] Um and this leads to actually uh way

[66:47] faster decoding as well um which like is

[66:50] a nice problem like the accuracy of

[66:52] outputting the format you care about is

[66:53] nice. It's also nice that it's just way

[66:55] faster because we don't have to always

[66:57] call the language model to to output a

[66:59] token that we know what it should be.

[67:01] Um another example is DSPy signatures.

[67:04] So here I have this example where we've

[67:06] defined and we're I'm going to talk

[67:07] about DSPy when I come back to lecture

[67:09] in a in a a few weeks or I think next

[67:11] week. Um and what we uh have is like you

[67:14] can define inputs and outputs. Uh so

[67:16] you'll say okay, I want to uh take as

[67:19] input a message and I want to produce a

[67:21] name, email, and intent. And so I've

[67:25] defined it as input, output, output, um

[67:27] and output here. And then when I pass a

[67:29] message to the model

[67:31] where it's like I'm Sarah, let's meet

[67:34] Thursday, and she provides her email,

[67:35] then when we call the model, we can get

[67:38] the output in a very specific structure

[67:39] where it's just parsed the details that

[67:41] we need.

[67:42] And the way that this actually works for

[67:43] DSP behind the scenes is like it creates

[67:46] this like prompt that says like this is

[67:48] how you have to respond and this is the

[67:49] details. And then it can interact with

[67:51] libraries like SGLang to make sure that

[67:53] it actually does that. But this is kind

[67:55] of how it forces the model to generate

[67:57] that way. Um

[67:59] and then the other thing you could do is

[68:01] like if you know exactly which things

[68:03] you want scores for, you could train a

[68:04] classifier and you can take the model

[68:06] and you train put a little head on it

[68:08] and say if I go from these embeddings, I

[68:11] actually want to produce just two

[68:13] outputs. I'm going to decide if it's

[68:14] positive or negative. And this could be

[68:16] like a way to use a language model

[68:17] within a broader system. You could

[68:19] imagine I just want the

[68:20] this to use as a classifier. And the

[68:22] reason I bring this up is it's actually

[68:23] very hot topic right now, these system

[68:25] one models.

[68:27] So if you've been on Twitter in the last

[68:28] few weeks, people have been really

[68:29] talking about these.

[68:31] And I mean this is like a thing that's

[68:32] existed for a while, but it's very very

[68:33] hyped right now. And like they're very

[68:35] secretive about how they actually do it

[68:36] at the company that's doing this. But

[68:39] there's an example in the open that may

[68:42] or may not be similar to what they're

[68:43] doing at the company. I'm not going to

[68:44] make any claims about that, but this is

[68:46] like a Stanford blog that came out

[68:47] recently where what they'll do is they

[68:50] actually have state which in this case

[68:52] is represented as a game, but you can if

[68:54] we're talking about language models, you

[68:55] can think of this as like just text

[68:58] also.

[68:59] And you have actions, which is like your

[69:00] multiple choice answers or I have my

[69:02] positive or negative for sentiment or I

[69:04] have my list of tools and I don't know

[69:05] which one to call. And what you do is

[69:07] you embed both of these and you just

[69:09] look at

[69:10] you compare the

[69:13] you know take the dot product and you

[69:14] see which ones are similar and which

[69:15] ones are most different and that gives

[69:17] you scores. So in this instance, it was

[69:19] able to say okay, given this is where

[69:22] Mario is and my actions are left, right,

[69:24] you know jump. Uh, Mario should jump.

[69:27] And this is another way of doing this

[69:28] like constrained. Like, I'm just going

[69:30] to use the model to output this exact

[69:32] set of of outputs that I care about.

[69:35] Uh, and an example of where you would

[69:36] care about this is tool calling. So, uh,

[69:39] we actually care a lot that the model

[69:41] outputs the tools in a way that we can

[69:42] use them. So I took this from the tool

[69:44] former uh paper. Uh, in practice people

[69:47] have many, many different ways of of

[69:48] actually having the models call tools.

[69:50] Maybe perhaps the most common and maybe

[69:52] most effective is actually to have it

[69:54] write code to do bash calls and stuff

[69:56] like that. Um, but uh you care that the

[69:59] model outputs it in a way that you know

[70:00] how to parse that tool, you know?

[70:01] Because because the model can say this,

[70:03] but if we can parse it, uh

[70:06] then we [clears throat] wouldn't know to

[70:07] call the calculator tool or to to call

[70:09] the search tool and stuff like that.

[70:11] Um, so any questions about structured IO

[70:14] for models?

[70:16] Excellent. Then we are onto our last few

[70:19] topics here, which is context

[70:20] engineering.

[70:21] Uh, and so uh prompt engineering and

[70:23] context engineering are kind of hot

[70:25] terms. And if you, you know, think back

[70:28] in the day when ChatGPT was first coming

[70:29] a thing, people were really, really

[70:31] focused on like what is how should I do

[70:33] prompt engineering and how should I uh

[70:35] write my thing and say like uh the world

[70:37] is going to end if you don't answer this

[70:39] question and this stuff like that and

[70:40] like really, really have the model, you

[70:42] know, uh answer in a

[70:44] uh

[70:45] in a way that you've crafted your

[70:46] prompts to make it behave well. Uh, but

[70:48] now what matters is context engineering,

[70:50] which is kind of a a whole layer on top

[70:51] of this where we have so much

[70:53] information we can give to the model.

[70:55] Uh, what really matters is like how do

[70:57] we structure that and how do we trim it

[70:59] down? Um, so what goes into the context

[71:01] of an agent? Uh, well these are a few

[71:02] things. You can imagine even more than

[71:03] this, but system prompt matters. Uh, the

[71:06] message history if you're interacting

[71:08] with the agent over multiple turns. Um,

[71:10] things like memories. Uh, if the model

[71:12] has saved memories and D talked about

[71:13] that last week and and we'll have a

[71:15] whole lecture on how how to do memory.

[71:17] Um, tool call results. So if I call my

[71:19] tool and it returns my file and stuff

[71:21] like that uh or like uh returns a search

[71:24] and stuff, how do I incorporate that

[71:25] into the context? Um, and then uh

[71:28] attached

[71:29] and and things like that. So um

[71:31] we I guess one thing you could think is

[71:33] like why not just put everything in the

[71:35] context? Uh well the reason for that is

[71:37] is context rot. Uh and also I I

[71:39] mentioned earlier and now you know that

[71:41] attention is n squared in context

[71:43] length. So it's very expensive to do

[71:44] this, but even if we could uh we

[71:46] wouldn't want to because um here's

[71:48] here's an example of a benchmark uh

[71:50] where it's similar in like this needle

[71:52] in the haystack type thing, but

[71:53] basically um here's like all of these

[71:56] articles and it asks like were there

[71:57] more news articles about the economy in

[71:59] September or August? And the model has

[72:00] to look through all of these documents

[72:03] and uh and determine like is it a

[72:05] document about the economy and uh when

[72:08] was it? And and count these things. And

[72:10] this is like a really really long

[72:11] context task. And if we look

[72:13] at how models do on this task, uh this

[72:15] is called Ulong is the benchmark. Uh and

[72:18] you can see that as the context length

[72:20] gets longer and longer, the models get

[72:22] worse and worse at this task. Um so you

[72:24] can see like maybe this yellow line is

[72:26] pretty pretty illustrative of Gemini. Uh

[72:28] it's really quite good almost 90 to

[72:31] it's getting there at uh and and almost

[72:34] 100% accuracy when you have a short

[72:35] context and only a few documents, but

[72:37] once you add a bunch of documents like

[72:39] it's getting like 10% accuracy. So we

[72:41] don't want to throw everything into the

[72:43] context. Um and so

[72:45] there's no one way to build the context.

[72:47] Um and this will be something that you

[72:49] have to do in homework one is design the

[72:51] context for your agent, um but instead

[72:53] we'll provide some practical tips and

[72:55] considerations that you should should

[72:56] focus on.

[72:58] Um so one thing is to avoid bloat. Uh

[73:00] sometimes a few tools is all you need.

[73:03] So this is a benchmark that came out

[73:05] recently or a paper blog called the

[73:07] harness task attacks. And they were

[73:09] looking at Codex, Claude Code, and Pi,

[73:12] which uh I'm sure you know Codex and

[73:14] Claude Code, but Pi is this open source

[73:16] agent harness. Um and it just has the

[73:18] tools read, write, edit, and bash. And

[73:20] for every model they tested and this

[73:22] table goes or this plot goes down

[73:23] further, uh except for Claude Fable, it

[73:26] was best to use Pi uh for the for the

[73:29] solving the the bench tasks. And so um

[73:33] sometimes like a very focused set of

[73:36] context is really all you need and you

[73:37] don't need to bloat it with a bunch of

[73:39] extra tools and

[73:40] uh the other thing you might want to use

[73:42] is retrieval to recover the most

[73:44] relevant memories or files. So next

[73:47] lecture is on retrieval, so I'm not

[73:48] going to go in in depth here, but

[73:50] essentially you can take a prompt and

[73:52] you can use it to search over your

[73:54] documents and then only put those

[73:56] documents into the context of the model.

[73:58] Um

[73:59] another thing uh that you should

[74:00] consider is adding to the context

[74:01] sequentially like over multiple

[74:03] conversation turns. So uh I talked about

[74:05] the KV cache here. Let's say that I

[74:07] wanted to add in a document at the

[74:09] beginning of the context for for some

[74:10] reason uh or like I think it's a natural

[74:12] thing to think if you don't think about

[74:14] the KV cache. Like maybe I want to put

[74:16] the at the very beginning I'm having a

[74:17] conversation and then I'm like oh I'm

[74:19] asking about this document. I've

[74:21] attached it to the front of your

[74:22] context. Um well [clears throat] the

[74:24] issue there is that um you've slid

[74:27] everything over to add this in, so

[74:28] actually the class was about uh and this

[74:31] just invalidated like changed all of

[74:33] your position embeddings and the KV

[74:35] cache was dependent on those position

[74:36] embeddings. So now the whole KV cache is

[74:39] invalidated. Uh so you should add

[74:41] sequentially over time to your to your

[74:43] context.

[74:44] Um the last thing is uh to evaluate

[74:48] context choices empirically. So I have

[74:50] this example from the tool former paper

[74:52] where they test with and without tools,

[74:54] which is kind of a simple like that's

[74:56] important for that paper, but this is a

[74:57] simple example. But you can imagine like

[74:59] I might try uh should I format my

[75:01] context in markdown or uh YAML or

[75:04] something like that and like you should

[75:05] just experiment with these different

[75:07] things and try them out and and run

[75:09] benchmarks and see what happens because

[75:11] this is like a good way to turn this

[75:12] into an engineering practice.

[75:14] Um last thing to note is um

[75:17] compaction.

[75:18] And so uh

[75:20] once you've reached compaction your

[75:21] context is already grown extremely long

[75:23] and it is with modern agent harnesses.

[75:25] I'll talk in a second about a way to

[75:28] avoid compaction potentially, but with

[75:30] modern harnesses this is is thing that

[75:31] happens. You get too long, so then your

[75:33] design decision is now like, now what do

[75:35] we keep? And if you make this mistake, I

[75:36] I included this after D mentioned it in

[75:38] the last lecture. But somebody had this

[75:41] situation where they had an AI read

[75:42] their entire inbox and and they said

[75:45] like you can delete emails but confirm

[75:47] with me before deleting. And then they

[75:49] put the whole inbox in and it was just

[75:51] way too long. So it immediately

[75:52] compacted and was like I don't need the

[75:54] instructions anymore. And so it got rid

[75:56] of that and then just deleted their

[75:57] emails. So you got to be careful about

[75:59] compaction.

[76:01] This is I believe the very last topic

[76:03] today and it is recursive language

[76:07] models. So this is a different

[76:09] philosophy to avoid compaction.

[76:11] And this is like kind of recent and new

[76:13] work. But basically the idea is what if

[76:16] you take the prompts to the language

[76:18] model itself and make it a part of your

[76:20] environment. So you put it in a variable

[76:22] and you say the prompt is in this

[76:23] variable and the language model has

[76:26] access to this code environment where it

[76:29] can actually manipulate the prompt. And

[76:31] so we can say like I want to look at the

[76:33] first 100 characters of the prompt. I

[76:35] want to split the prompt by this and

[76:36] that. And then it can also call itself.

[76:38] So you have this LLM query function and

[76:41] then it can call and now we're passing a

[76:43] prompt to this. So you can see this is

[76:44] like a recursive structure because the

[76:46] prompt was always a variable to begin

[76:48] with. But when we pass it to the sub

[76:50] agent, it's also a prompt. And so this

[76:52] is a kind of way of handling long

[76:54] context as well because

[76:56] then we can essentially rely on the sub

[77:00] agents to process parts of the context

[77:02] and return just what we want and and

[77:04] parse just the you know contents that we

[77:07] care about from the final answer and

[77:08] return that. So it's a sort of recursive

[77:10] structure.

[77:11] And you can see that this helps GPT-5

[77:13] mini on this Ulong benchmark, the same

[77:15] one that I showed earlier. It gets GPT-5

[77:18] mini to

[77:19] the best performance on the benchmark

[77:22] out pacing you know GPT-5.

[77:25] So in summary, what we talked about

[77:27] today, what are language models? We

[77:30] talked about language model

[77:30] architectures. We talked about language

[77:32] model training,

[77:34] also inference. And we concluded with a

[77:36] bit about how to use LLMs for agents. So

[77:39] I hope this was kind of a helpful

[77:40] introduction to LLMs and we won't be

[77:43] talking much about how LLMs work

[77:44] anymore, so we'll just be using them and

[77:46] thank you everyone.
