# 🔍 Trisearch AI

An AI-powered hybrid search engine that combines **semantic search + keyword matching (BM25) + LLM-based answer generation (RAG)** to retrieve and answer questions from multi-format documents.

---

## 🚀 Live Demo

👉 (Add your Streamlit link here after deployment)

---

## 🧠 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline:

1. 🔎 Retrieve relevant document chunks using hybrid search
2. 🧠 Generate contextual answers using an LLM (`gpt-4o-mini`)
3. 📄 Display sources for transparency

---

## ⚙️ Features

* 🔍 Hybrid Retrieval:

  * Semantic search (Sentence Transformers)
  * BM25 keyword matching
* 🧠 LLM Answer Generation (OpenAI API)
* 📄 Multi-format document support:

  * PDF, DOCX, PPTX, Email (.eml), JSON
* ⚡ Query understanding:

  * Broad queries (research questions)
  * Narrow queries (variable definitions)
* 📊 Evaluation:

  * MRR (Mean Reciprocal Rank)
  * Precision@1
* 🌐 Interactive UI with Streamlit

---

## 🏗 Architecture

```
User Query
   ↓
retrieve.py  (Hybrid Retrieval Engine)
   ↓
Top-K Chunks
   ↓
rag.py  (LLM Answer Generation)
   ↓
Streamlit UI (app.py)
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* Sentence Transformers (`all-MiniLM-L6-v2`)
* BM25 (`rank-bm25`)
* OpenAI API (`gpt-4o-mini`)
* NumPy / Scikit-learn

---

## 📁 Project Structure

```
.
├── app.py
├── rag.py
├── retrieve.py
├── test_local.py
├── test_files/
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

```
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```
python -m streamlit run app.py
```

---

## 🔑 Environment Setup

Set your OpenAI API key:

```
export OPENAI_API_KEY="api_key_here"
```

---

## 🧪 Local Testing

```
python test_local.py
```

---

## 💡 Example Queries

```
What is brand awareness?
What does frm_brand_awareness measure?
What are the main findings of the study?
brand awareness
```

---

## 📌 Key Highlights

* Built a **hybrid retrieval system (semantic + lexical)**
* Implemented **query classification (broad vs narrow)**
* Designed a **multi-format document ingestion pipeline**
* Integrated **LLM for answer generation (RAG)**
* Developed an **end-to-end interactive AI application**

---

## 👨‍💻 Author

Yuvanesh Raju
