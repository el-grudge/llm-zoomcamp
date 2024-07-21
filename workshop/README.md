In workshop 1️⃣ of the LLM Zoomcamp we learned about


📥 dlt (Data Load Tool) Library 


dlt is an open-source python library that automates data ingestion pipelines.


The library abstracts data ingestion tasks such as data extraction, schema management, and data type detection. It helps create a self-healing, self-maintaining, fully normalized pipeline, in a simple and fast way.


`pip install dlt` to install the tool 


⛏️ Data Extraction 


One of the core principles of dlt is loading with generators. Using generators to yield data is recognized as a data extraction best practice, as it enables more efficient memory management by preventing the loading of an indeterminate amount of data into RAM.


Define a pipeline using `dlt.pipeline` command. When ingesting data, simply pass the generator, target table name and the write disposition.


📏 Normalization


dlt provides automatic schema detection and normalization upon ingestion.


🔼 Incremental Loading


When running your pipeline, you can set the `write_dsposition` to append or merge and dlt will update the state of the data accordingly.


🗄️ We also learned about lancedb, a scalable open source vector db which stores the data, embeddings and metadata all in one place. 


👉 For a demo of dlt and lance check out this colab notebook: 

https://colab.research.google.com/drive/1nNOybHdWQiwUUuJFZu__xvJxL_ADU3xl?usp=sharing#scrollTo=sQhykrlGZoId


For the weekly project, I used dlt + lancedb to build a RAG that extracts from the Notion API. You can view the code here:


##llm_zoomcamp #llm #rag #dlt #data_ingestion #embedding #lancedb #learning_in_public