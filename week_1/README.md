In week 1️⃣ of the LLM Zoomcamp we learned about

**📚 LLM**

In its most basic form, a language model predicts the next token based on an input prompt. A large language model is a language model with millions of parameters that has been trained on a very large corpus of text.

**🔍🤖 Retrieval Augmented Generation (RAG)**

RAGs do two things:

* 🔎 Retrieval -> search a knowledge base  
* ✍️ Generation -> LLM generates an answer  

The process can be summarized in the following steps:

* ❓ Question: user asks a question  
* 📂 Context: A search is conducted against a knowledge base to retrieve documents relevant to the question  
* ✅ Answer: An LLM is used to generate an answer using the retrieved context  

RAGs can help restrict the context for an LLM so it can generate more relevant answers and make it less prone to hallucinations.

**🏗️ Building a RAG**

To build a RAG, you will need a knowledge base. A knowledge base is a corpus of documents that you want to search, e.g., a FAQ page.

Next, you'll need to index your documents. We'll be using Elasticsearch to create our index. To use it, we need to parse the document into a list of dictionaries, then use the es_client.index() method to add our documents to the knowledge base. You can think of an Elasticsearch index as a table with multiple documents:

Elasticsearch ➡️ Clusters ➡️ Indices ➡️ Shards ➡️ Documents with key-value pairs

Now that we have our index, we can search it for documents that are relevant to a search query. Then, we can use the retrieved documents to build a prompt for an LLM.

When building a prompt, assign your LLM a role for better results. Prompt engineering is an iterative process, so be creative and patient.

Finally, pass your prompt to an LLM and generate a response to the query.

A RAG pipeline looks like this:

query ➡️ search results ➡️ prompt ➡️ LLM response

In the first weekly project, I used Elasticsearch to build a RAG to search and retrieve answers from the FAQ document of datatalkclubs. You can view the code here.

#llm_zoomcamp #LLM #RAG #Elasticsearch #learning_in_public