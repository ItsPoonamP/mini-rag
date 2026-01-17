# Mini RAG Project – AI Engineer Assessment

## Live Demo
- **URL:** [https://mini-rag-lehspggeytczj9emkpk4mc.streamlit.app/](#)

## GitHub Repository
- **Repo:** [https://github.com/ItsPoonamP/mini-rag](#)
 ## Resume Link
- **URL:** [https://drive.google.com/drive/folders/10nZb4vzsGZXrhFHa-uWslCOcj3oNfN7g?usp=sharing](#)

---
## Setup Instructions

# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate


pip install -r requirements.txt


git clone <your-repo-url>
cd <repo-folder>

# 📚 Mini-RAG: Retrieval-Augmented Generation System

A lightweight Retrieval-Augmented Generation (RAG) application that allows users to upload documents and ask questions grounded strictly in those documents. The system uses **Google Gemini** for embeddings, reranking, and answer generation, **Pinecone** for vector storage, and **Streamlit** for the UI.

---

##  Features

- PDF and text ingestion
- Semantic search using vector embeddings
- LLM-based reranking for higher precision
- Context-grounded answers with citations
- Streamlit-based interactive UI
- Memory reset / index clear option

---

##  Architecture Overview
User Query
↓
Query Embedding (Gemini)
↓
Vector Search (Pinecone)
↓
Top-K Retrieved Chunks
↓
LLM Reranker (Gemini)
↓
Top-N Context Chunks
↓
Answer Generation (Gemini)
↓
Final Answer + Citations


---

## System Components

### 1. Document Ingestion
- Extracts text from PDFs or raw input
- Splits text into overlapping chunks
- Generates embeddings for each chunk
- Stores vectors in Pinecone

**Files**
- `backend/ingest.py`
- `backend/chunking.py`
- `backend/embeddings.py`

---

### 2. Embedding Layer
- Model: `text-embedding-004`
- Used for document chunks and queries
- Ensures semantic similarity search

---

### 3. Vector Database (Pinecone)
- Stores embeddings with metadata
- Enables fast similarity search
- Scalable and production-ready

---

### 4. Retrieval Layer
- Embeds user query
- Retrieves top-K similar chunks from Pinecone
- Optimized for recall

---

### 5. Reranking Layer
- Model: `gemini-2.5-flash`
- Reorders retrieved chunks using LLM reasoning
- Improves relevance precision

---

### 6. Answer Generation
- Model: `gemini-2.5-flash`
- Uses only retrieved context
- Produces grounded answers with inline citations

---

## 🗂 Data Schema

### Pinecone Vector Format

json
{
  "id": "uuid",
  "values": [0.0123, -0.4567, ...],
  "metadata": {
    "text": "chunk content",
    "source": "document.pdf",
    "chunk": 3
  }
}

Limits encountered:
Gemini free-tier API quota exceeded → handled by waiting and retrying
Pinecone index dimension mismatch → ensured embedding dimension matches index
Reranking adds latency due to LLM calls
Context window limits maximum chunk size
No conversational memory across sessions
PDF extraction quality depends on document formatting

Trade-offs / Design decisions:
Chunk size: 800–1200 tokens with 10% overlap → balances retrieval speed and context preservation
Retriever: basic top-k similarity + reranker for better precision
LLM provider: Gemini 2.5 used for embeddings and reranking

Future improvements:
Add caching layer to reduce repeated embedding calls
Add multi-file upload support
Experiment with alternative rerankers or LLM providers for better results
Hybrid search (BM25 + vectors)
Streaming answers
Multi-document citation grouping
Conversational memory support
Evaluation metrics (Recall@K, MRR)
