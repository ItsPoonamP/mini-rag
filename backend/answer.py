import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

    response = genai.models.generate_content(model ="gemini-2.5-flash-lite",content=prompt )

    return response.text, citations



