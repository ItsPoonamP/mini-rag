import os
from google import genai
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

from dotenv import load_dotenv

load_dotenv()


def generate_answer(query, retrieved_chunks):
    if not retrieved_chunks:
        return "I couldn’t find relevant information.", []

    context = ""
    citations = []

    for i, match in enumerate(retrieved_chunks):
        context += f"[{i+1}] {match['metadata']['text']}\n"
        citations.append(match["metadata"])

    prompt = f"""
Answer the question using ONLY the context below.
Add inline citations like [1], [2].

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(model ="gemini-2.5-flash",contents=prompt )

    return response.text, citations












