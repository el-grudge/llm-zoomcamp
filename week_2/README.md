In week 2️⃣ of the LLM Zoomcamp we learned about

🌐 Open-Source LLMs

Last week we used OpenAI API to create a RAG that can answer questions from the FAQ document of datatalkclubs. 

This week, we tried 3 alternatives to OpenAI:

* [google/flan-t5-xl](https://huggingface.co/google/flan-t5-xl)  

A better version of the the T5, FLAN-T5 has the same number of parameters (~2.85B), and have been fine-tuned on more than 1000 additional tasks covering also more languages. 

* [microsoft/Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct)  

This 3.8 billion-parameter, lightweight, state-of-the-art open model has been trained using the Phi-3 datasets which includes both synthetic data and filtered publicly available website data, with an emphasis on high-quality and reasoning-dense properties. The model belongs to the Phi-3 family with the Mini version in two variants 4K and 128K which is the context length (in tokens) that it can support.

* [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)

A pretrained generative text model with 7 billion parameters. Mistral-7B-v0.1 is a transformer model, with Grouped-Query Attention, Sliding-Window Attention, and Byte-fallback BPE tokenizer.

There are a number of different factors that need to be considered when working with open source models:  
* Model size vs. GPU memory size: If a model is too large it might not fit in the GPU memory, especially When working with free-tier GPU resources such as those available in Google Colab or Saturn Cloud.  
* User agreements: To access the Mistral model you must agree to share your contact information  
* Different models will respond differently to the same prompt, so try different approaches. Also, the prompt size can have an effect on how a model responds  
* There's also a difference in speed, some models taking longer to respond than others (Mistral was the slowest, FLAN-T5 was the quickest)  

To find more about open source LLMs, checkout these leaderboards:

* [open-llm-leaderboard/open_llm_leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
* [optimum/llm-perf-leaderboard](https://huggingface.co/spaces/optimum/llm-perf-leaderboard)

Also, check out trending Models on [HuggingFace](https://huggingface.co/models). You can also always use google, social media, ChatGPT.

🖥️ Working with LLMs locally

Using the Ollama platform (created by Meta), we can interact with / deploy LLMs locally. The command-line interface is easy to use; here are some basic commands:

* `Ollama pull` --> Pulls a model from a registry

* `Ollama run` --> Runs a model. You need to have the model weights downloaded to use this command.

* `Ollama list` --> Lists the available models

Ollama supports a lot of models, such as Mistral, Phi-2, Llama2, Gemma 2b.

You can start running Ollama by using docker (more details [here](https://github.com/ollama/ollama/blob/main/README.md#quickstart)).

```docker
FROM ollama/ollama

# Copy the weights from your local machine to the Docker image
COPY ollama_files/ /root/.ollama
```

In our second weekly project, I used Ollama to download the Gemma 2b weights locally and used it to build a docker container around the RAG I created last week. You can view the code [here](https://github.com/el-grudge/llm-zoomcamp/tree/main/week_2).

#llm_zoomcamp #LLM #RAG #open_source #ollama #local_llms #learning_in_public