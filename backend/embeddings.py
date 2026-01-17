from dotenv import load_dotenv

load_dotenv()
from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])





def embed_text(text: str):
    """
    Returns an embedding vector using Gemini
    """
    response = client.models.embed_content(
        model="text-embedding-004",
        content=text
    )
    return response.embedding








