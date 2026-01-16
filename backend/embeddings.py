import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def embed_text(text: str):
    """
    Returns an embedding vector using Gemini
    """
    response = genai.embed_content(
        model="text-embedding-004",
        content=text
    )
    return response["embedding"]






