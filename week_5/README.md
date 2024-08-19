In week 5️⃣ of the LLM Zoomcamp we learned about

🚀Orchestration 

This week we used Mage to build our RAG system. In version 0.9.72 Mage provides a dedicated RAG build experience. 

There are two types of pipelines that can be built:

- 📊 Data Preparation
- 🤖 Inference

📊 Data Preparation
This involves the main RAG steps of:

- 📥 Ingesting the data
- ✂️ Chunking
- ✒️ Tokenization
- 🧠 Embedding
- 🗃️ Storing in a vector database

Mage provides default blocks for multiple vector databases (Chroma, Pinecone, Elasticsearch, etc.) as well as for knowledge graphs.

(P.S.: I had a mixed experience using this feature. 😅 Figuring out the right connection string and setting up the Docker Compose file took a lot of time. However, it is nice to have a visual representation for your RAG.)

🤖 Inference
This is where you can interact with the vector database. 💬

👉 In the weekly project, I used Mage to build and update a RAG system based on LLM course FAQ. You can view the code [here](https://github.com/el-grudge/llm-zoomcamp/tree/main/week_5).

#llm_zoomcamp #llm #mage #rag #learning_in_public #data_talks_club