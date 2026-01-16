import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

client = Client(api_key=os.getenv("GEMINI_API_KEY"))

def embed_text(text: str):
    """
    Returns an embedding vector using Gemini
    """
    response = client.models.embed_content(
        model="text-embedding-004",
        contents=text
    )
    return response.embeddings[0].values

