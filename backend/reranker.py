from google import genai
import os

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def rerank(query: str, chunks: list, top_n: int = 5):
    if not chunks:
        return []

    passages = ""
    for i, m in enumerate(chunks):
        passages += f"{i+1}. {m['metadata']['text']}\n\n"

    prompt = f"""
You are a reranking model.

Given a user query and a list of passages,
rank the passages from MOST to LEAST relevant.

Return ONLY a comma-separated list of passage numbers.

Query:
{query}

Passages:
{passages}
"""

    
    response = client.models.generate_content(model="gemini-2.5-flash",
    contents=prompt)

    order = response.text.strip()
    indices = []

    for x in order.split(","):
        try:
            indices.append(int(x.strip()) - 1)
        except:
            pass

    return [chunks[i] for i in indices if i < len(chunks)][:top_n]








