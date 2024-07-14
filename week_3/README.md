In week 3️⃣ of the LLM Zoomcamp we learned about

🔍 Semantic Search 

Semantic search uses word embeddings to search for answers to user queries. Previously, we used Elasticsearch's multi-match method to search an index; multi-search allows us to define the specific fields to search and gives us flexibility with prioritizing certain fields. 

This time, we used the KNN (K-Nearest Neighbors) method to conduct our search, searching for more nuanced similarities across our embedding space. Elasticsearch's implementation of this search technique is optimized to conduct a fast search and accurate search without having to search the entire vector space - which could be costly if dealing with a large documents corpus.

The multi-match method's boosted-fields feature is good for keyword matches, but might not capture semantic similarities. KNN is better optimized to capture more general semantic similarities.

📊 Evaluation

LLMs are notorious for their hallucinations (aka confabulations). On the Machine Learning Street Talk [podcast](https://www.youtube.com/watch?v=4JF1V2hzGKE), Nick Frosst, Cohere's cofounder, said that all that LLMs do is hallucinate, but sometimes their hallucinations match our realities, which I thought was interesting.

So, when working with LLM, we have to consider how to evaluate their answers, and to do that we need to establish ground truths. There are multiple ways we can get our ground truth, such as: 

* ✍️ Humman annotation - manual, slow, expensive, gold standard
* 🧠 Domain expertize - manual, faster than human annotation, expensive, good enough standard
* 🤖 Using LLMs - automated, very fast, cheap, good as a starting point but not a reliable standard

Then, we can use different metrics to evaluate an LLM's responses including:

Hit Rate (recall):

- Step 1: for each document, return 1 if any of the LLM's responses matches the right answer, else return 0
- Step 2: sum the answers from step 1 and divide by the document count

MRR (Mean Reciprocal Rank):
Very similar to Hit Rate, but accounts for the rank (position) of the returned answer

- Step 1: for each document, return 1/r if the LLM response matches the right answer, else return 0, where r is the rank of the response
- Step 2: sum the answers from step 1 and divide by the document count

📈 These metrics allow us to measure the reliability of our LLM applications, and to compare different LLMs in a standard way.

In the third weekly project, I used conducted vector search with and without Elasticsearch and compared the performance. You can view the code [here](https://github.com/el-grudge/llm-zoomcamp/tree/main/week_3).

#llm_zoomcamp #llm #elasticsearch #llm_evaluation #semantic_search #learning_in_public