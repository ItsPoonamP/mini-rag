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

# Sample Knowledge Document for RAG Evaluation

## Document: Mini RAG System Overview

The Mini RAG system is a retrieval-augmented generation pipeline designed to answer user queries using a combination of vector search and large language models. The system first ingests documents by splitting them into smaller text chunks. Each chunk is converted into a numerical embedding using the Gemini `text-embedding-004` model. These embeddings are stored in Pinecone, which acts as the vector database for similarity search.

When a user submits a query, the query text is embedded using the same embedding model and compared against stored embeddings in Pinecone to retrieve the top-K most relevant chunks. These retrieved chunks may not always be perfectly ordered by relevance, so a reranking step is applied. The reranker uses a Gemini language model to reorder the retrieved chunks based on their semantic relevance to the query.

After reranking, the top-N chunks are passed to a Gemini generative model (`gemini-2.5-flash`) along with the user query. The model generates a final answer using only the provided context. Each answer includes inline citations that correspond to the document chunks used, ensuring transparency and traceability of the generated response.

This architecture improves factual accuracy by grounding the model’s responses in retrieved documents rather than relying solely on the model’s internal knowledge.

---

## Gold Question–Answer Set

These questions are used to evaluate the correctness of the Mini RAG system.

### Q1
**Question:** What is the main purpose of the Mini RAG system?  
**Answer:** The main purpose of the Mini RAG system is to answer user queries by combining document retrieval with large language model generation.

### Q2
**Question:** Which model is used to generate embeddings for document chunks?  
**Answer:** The `text-embedding-004` model from Gemini is used to generate embeddings.

### Q3
**Question:** What role does Pinecone play in the system?  
**Answer:** Pinecone stores the document embeddings and performs similarity search to retrieve relevant chunks.

### Q4
**Question:** Why is a reranking step applied after retrieval?  
**Answer:** Reranking is applied to reorder retrieved chunks based on their semantic relevance to the user query.

### Q5
**Question:** Which Gemini model is used to generate the final answer?  
**Answer:** The `gemini-2.5-flash` model is used to generate the final answer.

