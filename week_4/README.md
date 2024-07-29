In week 4️⃣ of the LLM Zoomcamp we learned about

📊🔍 Evaluation and monitoring

Here's a quick recap to what we covered so far:

In week 1 we discussed the RAG flow, which consists of:

🔎 Search / retrieve ➡️➡️ ✍️ Build a prompt ➡️➡️ 🤖 Generate an answer

In week 2, we focused on the generation part, and discussed open-source alternatives to OpenAI and the Ollama platform.

In week 3 we covered the search / retrieve part, we created a vector database and index using Elasticsearch, and discussed how to evaluate its results using metrics such as hit-rate and MRR.

This week we discuss how to evaluate the entire rag system, from retrieval to generation. Earlier this year in a small claims court case, Air Canada tried disowning its chatbot by claiming that the information provided by it is less trustworthy than information provided elsewhere on its website. Air Canada lost the case ([link](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know)). This is just one example for why evaluate an LLM system.

🧐 There are 2 forms of evaluation:
- 🔌 Offline -> evaluations done before deploying the service (e.g. to determine the best retrieval method, or the best prompt)
- 🌐 Online -> evaluations done after deploying the service (e.g. by collecting user feedback to measure how our LLM is performing)

For offline evaluation we can use:
* 📐 a -> q -> a` cosine similarity: a measure of how close a generated answer is to a ground truth answer 
* 👨‍⚖️ LLM as a judge: as the name implies, an LLM is used to evaluate a generated answer either by comparing it to a ground truth answer, or if that is not available then by comparing it to the question

For online evaluation we can use:
* 🧪 A/B test experiments 
* (👍 / 👎) User feedback (thumbs up / down)

Monitoring 
Observing the overall health of the system using:
- ⚖️ Quality metrics: such as bias and fairness
- 🏅System metrics (the 4x gold signals): latency, traffic, errors, saturation (memory and GPU usage)
- 💰 Cost: of vector store, LLM api calls

👉 In the weekly project, I used cosine similarity and the ROUGE score - a metric that compares overlapping units such as n-grams, word sequences, and word pairs between the generated text and the ground truth - to evaluate generated answers. You can view the code [here](https://github.com/el-grudge/llm-zoomcamp/tree/main/week_4).

#llm_zoomcamp #llm #llm_evaluation #monitoring #cosine_similarity #learning_in_public #data_talks_club