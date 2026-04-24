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

- 🔍 Hybrid Retrieval:
  - Semantic search (Sentence Transformers)
  - BM25 keyword matching
- 🧠 LLM Answer Generation (OpenAI API)
- 📄 Multi-format document support:
  - PDF
  - DOCX
  - PPTX
  - Email (.eml)
  - JSON glossary
- ⚡ Query understanding:
  - Broad queries (research questions)
  - Narrow queries (variable definitions)
- 📊 Built-in evaluation:
  - MRR (Mean Reciprocal Rank)
  - Precision@1
- 🌐 Interactive UI with Streamlit

---

## 🏗 Architecture
