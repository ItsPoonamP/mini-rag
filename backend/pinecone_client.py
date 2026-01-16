import os
from pinecone import Pinecone, ServerlessSpec 
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "pred"
DIMENSION = 768  # Gemini embedding size

pc = Pinecone(api_key=PINECONE_API_KEY)

def get_index():
    existing_indexes = pc.list_indexes().names()

    if INDEX_NAME not in existing_indexes:
        pc.create_index(
            name=INDEX_NAME,
            dimension=DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    return pc.Index(INDEX_NAME)
def clear_index():
    """
    Deletes all vectors from the index (clears memory)
    """
    index = get_index()
    # This removes all vectors in the index
    index.delete(delete_all=True)
    print("✅ Pinecone index cleared!")
