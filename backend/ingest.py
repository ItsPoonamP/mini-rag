import uuid
from pypdf import PdfReader
from backend.chunking import chunk_text
from backend.embeddings import embed_text
from backend.pinecone_client import get_index

index = get_index()

def ingest_text(text: str, source="manual"):
    chunks = chunk_text(text)

    vectors = []
    for i, chunk in enumerate(chunks):
        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embed_text(chunk),
            "metadata": {
                "source": source,
                "chunk": i,
                "text": chunk
            }
        })

    index.upsert(vectors)

def ingest_pdf(file):
    reader = PdfReader(file)
    full_text = ""

    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    ingest_text(full_text, source=file.name)
