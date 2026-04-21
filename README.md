#  RAG-Based Document Question Answering System with Streamlit UI

A Retrieval-Augmented Generation (RAG) system that enables you to ask questions from your documents (`.txt`, `.pdf`, `.docx`) and get accurate answers using **local LLMs** — no external APIs required.

---

##  Features

*  Supports multiple file formats:

  * `.txt`
  * `.pdf`
  * `.docx`
*  Semantic search using embeddings
*  Local LLM inference via Ollama
*  Fast vector search with FAISS
*  Interactive question-answer loop
*  Streamlit Web UI
*  Fully offline (privacy-friendly)

---

##  Tech Stack

* LangChain
* FAISS (Vector Database)
* HuggingFace Embeddings
* Ollama (Local LLM runtime)
* Sentence Transformers
* Streamlit
* Python
* Jupyter Notebook

---

##  System Requirements

* Python **3.9 or higher**
* RAM:

  * Minimum: 8GB
  * Recommended: 16GB+
* OS: Windows / Linux / macOS

---

##  Installation

###  Install Python

https://www.python.org/downloads/

```bash
python --version
```

---

###  Create Virtual Environment

```bash
python -m venv rag_env
```

Activate:

**Windows**

```bash
rag_env\Scripts\activate
```

**Mac/Linux**

```bash
source rag_env/bin/activate
```

---

###  Install Required Libraries

```bash
pip install langchain langchain-community langchain-huggingface faiss-cpu sentence-transformers pypdf docx2txt streamlit
```

---

###  Install Jupyter Notebook

```bash
pip install notebook
jupyter notebook
```

---

##  Using Jupyter Notebook

Run interactively:

```bash
jupyter notebook
```

Create new file → `rag_demo.ipynb`

---

##  Streamlit App (Web UI)

### ▶️ Run the App

Save your code as `RAG_Streamlit.py`, then run:

```bash
streamlit run RAG_Streamlit.py
```

---

###  What This App Does

* Upload `.txt`, `.pdf`, `.docx`
* Automatically processes document
* Creates embeddings + FAISS index
* Lets you chat with your document

---

###  Project Structure

```
rag-project/
│── RAG_Streamlit.py              # Streamlit app
│── Nature.pdf
│── rag_demo.ipynb
│── README.md
```

---

##  Usage

### 🔹 Option 1: Streamlit UI

```bash
streamlit run RAG_Streamlit.py
```

* Upload document
* Ask questions in chat UI

---

### 🔹 Option 2: Jupyter Notebook

```bash
jupyter notebook
```

* Run cells step-by-step
* Test queries interactively

---

### 🔹 Option 3: Python Script

```bash
python main.py
```

---

##  How It Works

1. Load document
2. Split into chunks
3. Generate embeddings
4. Store in FAISS
5. Retrieve relevant chunks
6. Send to LLM
7. Generate answer

---

##  Example Models (Ollama)

```bash
ollama run tinyllama
```

Other options:

* `llama3`
* `phi`
* `mistral`

---

##  Limitations

* Answers limited to document content
* Small models → lower accuracy
* Large files need tuning

---

##  Future Improvements

* Chat memory
* Multi-file upload
* Better UI
* Hybrid search

---

##  Notes

* Ensure Ollama is running
* Use GPU if available
* Adjust chunk size for performance

---
