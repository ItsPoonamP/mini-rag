# Mini RAG Project – AI Engineer Assessment

## Live Demo
- **URL:** [Insert your deployed app URL here](#)

## GitHub Repository
- **Repo:** [Insert your GitHub repo link here](#)

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

Limits encountered:
Gemini free-tier API quota exceeded → handled by waiting and retrying
Pinecone index dimension mismatch → ensured embedding dimension matches index

Trade-offs / Design decisions:
Chunk size: 800–1200 tokens with 10% overlap → balances retrieval speed and context preservation
Retriever: basic top-k similarity + reranker for better precision
LLM provider: Gemini 2.5 used for embeddings and reranking

Future improvements:
Add caching layer to reduce repeated embedding calls
Add multi-file upload support
Experiment with alternative rerankers or LLM providers for better results
