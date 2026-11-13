1. **[Part 1] Decoding.** Using the table from Part 1, discuss which settings lead to repetition and which lead to incoherent text. What are the pros and cons of each setting? Give an example of a real-world application that would be best suited to each.

2. **[Parts 1 and 2] gpt2 vs. Gemini.** Use generate from Part 1 and chat from Part 2 to give gpt2 and Gemini the same instructions at a temperature of 0.7. Try two or three instructions of your own and quote the outputs. How does gpt2 handle instructions compared to Gemini? Why do you think that is?

3. **[Part 3] Retrieval.** Report recall@k for both retrievers, split by query kind. Find a query that embedding retrieval does better on, and a query that keyword (TF-IDF) retrieval does better on. What aspects of a query make it better suited to each?

4. **[Part 3] Grounded answers.** Report both abstention rates. Change your answer prompt to make the model more willing to answer, then less willing, and report how the two rates change. Which prompt changes had the biggest effect? For the park's help desk, which mistake is worse: answering a question the articles do not cover, or abstaining on one they do? Where would you want the two rates to be?

5. **[Part 4] Memory.** Compare the contexts main prints at buffer sizes 2 and 8. What are the biggest differences? Then rerun Part 4 with longer and shorter values of SUMMARY_WORDS. At what length does your summary start losing details, and which details are lost first?
