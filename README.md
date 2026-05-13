# RoleFit AI V2

## AI-Powered Resume ↔ Job Description Matching System

RoleFit AI V2 is the upgraded and production-oriented version of the original RoleFit AI project.

This version focuses on building a modern GenAI-powered ATS-style candidate evaluation system using:

* FastAPI
* LangChain
* Ollama
* ChromaDB
* Hybrid Retrieval
* Semantic Search
* Local LLMs
* Prompt Engineering
* RAG Pipelines

Unlike V1, which was primarily a terminal-based prototype using procedural scripts and FAISS, RoleFit AI V2 introduces a modular architecture with scalable retrieval pipelines, structured outputs, hybrid retrieval systems, metadata-aware chunking, and production-style backend design.

---

# Features

* AI-powered Resume ↔ JD semantic matching
* ATS-style candidate evaluation
* Local LLM inference using Ollama
* ChromaDB vector storage
* Semantic search using embeddings
* BM25 keyword retrieval
* Hybrid retrieval pipeline
* Metadata-aware chunking
* Section-aware retrieval metadata
* PDF resume ingestion pipeline
* Text chunking pipeline
* Similarity score retrieval
* Prompt-engineered RAG workflows
* Structured JSON outputs
* FastAPI backend APIs
* Modular GenAI architecture
* Local-first and privacy-friendly design

---

# Tech Stack

| Category | Technology |
|---|---|
| Backend | FastAPI |
| LLM Orchestration | LangChain |
| LLM Runtime | Ollama |
| Vector Database | ChromaDB |
| Embedding Model | nomic-embed-text |
| Primary LLM | Gemma / Qwen2.5 |
| Retrieval | Hybrid Retrieval |
| Reranking | BGE Reranker |
| PDF Parsing | LangChain Loaders |
| API Docs | Swagger/OpenAPI |

---

# V1 vs V2

| Feature | RoleFit AI V1 | RoleFit AI V2 |
|---|---|---|
| Architecture | Terminal Script | Modular Backend |
| Vector DB | FAISS | ChromaDB |
| LLM Integration | Manual | LangChain + Ollama |
| API Layer | None | FastAPI |
| Retrieval | Basic Semantic Search | Hybrid Retrieval |
| Prompting | Static Prompts | Prompt Templates |
| Output Parsing | Manual JSON Cleaning | Structured Outputs |
| Embeddings | MiniLM | nomic-embed-text |
| Scalability | Prototype | Production-Oriented |

---

# Project Architecture

```text
Resume Upload
      ↓
PDF Loader
      ↓
Section Detection
      ↓
Metadata-Aware Chunking
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Vector Retrieval
      ↓
BM25 Retrieval
      ↓
Hybrid Retrieval
      ↓
Reranking
      ↓
LangChain Chains
      ↓
Ollama LLM
      ↓
Structured Match Analysis
      ↓
FastAPI JSON Response
```

---

# Current Retrieval Stack

* ChromaDB semantic retrieval
* BM25 keyword retrieval
* Hybrid retrieval architecture
* Metadata-aware chunk retrieval
* Section-aware chunk metadata
* Local Ollama embeddings

---

# Project Structure

```text
rolefit-ai-v2/
│
├── app/
│   ├── chunking/
│   ├── ingestion/
│   ├── loaders/
│   ├── retrievers/
│   ├── utils/
│   └── vectorstores/
│
├── chroma_db/
├── data/
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Current Development Status

## Completed

* FastAPI project setup
* Ollama integration
* ChromaDB integration
* Semantic vector retrieval pipeline
* Local embedding pipeline
* LangChain integration
* Persistent vector storage
* PDF resume ingestion pipeline
* PDF parsing using LangChain loaders
* Text chunking pipeline
* Metadata-aware chunk storage
* Section-aware metadata tagging
* Similarity score retrieval
* BM25 keyword retrieval
* Hybrid retrieval architecture
* Retrieval fusion logic
* Retrieval comparison testing

## In Progress

* Retrieval fusion optimization
* Retrieval reranking pipelines
* Prompt engineering
* ATS scoring engine
* Query optimization
* Advanced resume section classification
* FastAPI endpoints

---

# Local Setup

## 1. Clone Repository

```bash
git clone <repo_url>
cd rolefit-ai-v2
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama:

https://ollama.com/download

---

## 5. Pull Required Models

```bash
ollama pull gemma4:latest
ollama pull nomic-embed-text:latest
```

Optional:

```bash
ollama pull qwen2.5:14b
```

---

## 6. Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

# API Documentation

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Planned Features

* Resume upload APIs
* JD upload APIs
* ATS scoring system
* Resume improvement suggestions
* Skill gap analysis
* Metadata-aware retrieval filtering
* Cross-encoder reranking
* Resume section classification
* Dashboard frontend
* Deployment support
* LangGraph-based agent workflows (future)

---

# Learning Goals Behind This Project

This project is being built to deeply explore:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Hybrid Retrieval Systems
* Metadata-Aware Retrieval
* Local LLM Deployment
* Prompt Engineering
* LangChain Orchestration
* AI Backend Engineering
* Production-Style GenAI Architecture
* Retrieval Evaluation Pipelines

---

# Author

VSC Bharadwaj

---

# License

This project is for educational, research, and portfolio purposes.
