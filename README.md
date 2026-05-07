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

Unlike V1, which was primarily a terminal-based prototype using procedural scripts and FAISS, RoleFit AI V2 introduces a modular architecture with scalable retrieval pipelines, structured outputs, semantic reranking, and production-style backend design.

---

# Features

* AI-powered Resume ↔ JD semantic matching
* ATS-style candidate evaluation
* Local LLM inference using Ollama
* ChromaDB vector storage
* Semantic search using embeddings
* Hybrid retrieval pipeline
* Prompt-engineered RAG workflows
* Structured JSON outputs
* FastAPI backend APIs
* Metadata-aware retrieval
* Modular GenAI architecture
* Local-first and privacy-friendly design

---

# Tech Stack

| Category          | Technology        |
| ----------------- | ----------------- |
| Backend           | FastAPI           |
| LLM Orchestration | LangChain         |
| LLM Runtime       | Ollama            |
| Vector Database   | ChromaDB          |
| Embedding Model   | nomic-embed-text  |
| Primary LLM       | Gemma / Qwen2.5   |
| Retrieval         | Hybrid Retrieval  |
| Reranking         | BGE Reranker      |
| PDF Parsing       | LangChain Loaders |
| API Docs          | Swagger/OpenAPI   |

---

# V1 vs V2

| Feature         | RoleFit AI V1         | RoleFit AI V2       |
| --------------- | --------------------- | ------------------- |
| Architecture    | Terminal Script       | Modular Backend     |
| Vector DB       | FAISS                 | ChromaDB            |
| LLM Integration | Manual                | LangChain + Ollama  |
| API Layer       | None                  | FastAPI             |
| Retrieval       | Basic Semantic Search | Hybrid Retrieval    |
| Prompting       | Static Prompts        | Prompt Templates    |
| Output Parsing  | Manual JSON Cleaning  | Structured Outputs  |
| Embeddings      | MiniLM                | nomic-embed-text    |
| Scalability     | Prototype             | Production-Oriented |

---

# Project Architecture

```text
Resume Upload
      ↓
PDF Loader
      ↓
Semantic Chunking
      ↓
Embeddings
      ↓
ChromaDB
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

# Project Structure

```text
rolefit-ai-v2/
│
├── app/
│   ├── api/
│   ├── chains/
│   ├── prompts/
│   ├── retrievers/
│   ├── vectorstores/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── chroma_db/
├── data/
├── tests/
│
├── main.py
├── requirements.txt
├── .env
└── README.md
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

## In Progress

* Resume ingestion pipeline
* Semantic chunking
* Hybrid retrieval
* Prompt engineering
* Reranking
* Match scoring engine
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

[https://ollama.com/download](https://ollama.com/download)

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
* Metadata-aware retrieval
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
* Local LLM Deployment
* Prompt Engineering
* LangChain Orchestration
* AI Backend Engineering
* Production-Style GenAI Architecture
* Hybrid Retrieval Systems
* LLM Evaluation Pipelines

---

# Author

VSC Bharadwaj

---

# License

This project is for educational, research, and portfolio purposes.
