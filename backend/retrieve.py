from backend.embeddings import embed_text
from backend.pinecone_client import get_index

index = get_index()

def retrieve_chunks(query, top_k=10):
    query_vector = embed_text(query)

    res = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    return res["matches"]
