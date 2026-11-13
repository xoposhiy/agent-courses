1. **[Part 2] Tokenization.** Using the output from the test function in part 2, discuss how the different input sentences
tokenized differently in terms of word-per-token and bytes-per-token. Which failed the round trip check? Why do you think that is?

2. **[Part 2] Your trained BPE tokenizer.** Train your BPE tokenizer using vocab size 300, 500, and 2000. Report the vocabulary you actually got at each and account for any gap. Then tokenize the Part 2 sentences at each size. Which sentences improve as the vocabulary grows and which do not? What does that tell you about how a larger vocabulary would adapt to unseen text?

3. **[Part 3] Training.** Report your training loss at the first and last epoch, alongside your accuracy on the test split. Account for the gap between them. What would happen to the training accuracy if we trained the model for additional epochs? Why do we measure accuracy on the test split, and not train?

4. **[Part 3] Model comparison.**  Play around with the hidden state size in your transformer. Train your model and observe what happens when it's decreased to 16 and increased to 128. Compare and contrast the resulting metrics. What are the tradeoffs as model sze increases?
