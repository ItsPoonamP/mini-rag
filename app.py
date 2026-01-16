import streamlit as st
from backend.ingest import ingest_text, ingest_pdf
from backend.retrieve import retrieve_chunks
from backend.answer import generate_answer
import time
from backend.reranker import rerank
from backend.pinecone_client import clear_index, get_index

st.set_page_config(page_title="Mini RAG", layout="wide")
st.title("📚 Mini RAG App")

with st.sidebar:
    st.header("Upload Data")
    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
    pasted_text = st.text_area("Or paste text")

    if st.button("Ingest"):
        if uploaded_pdf:
            ingest_pdf(uploaded_pdf)
            st.success("PDF ingested!")
        elif pasted_text:
            ingest_text(pasted_text)
            st.success("Text ingested!")

query = st.text_input("Ask a question")

if query:
    start = time.time()
    retrieved = retrieve_chunks(query, top_k=10)
    reranked = rerank(query, retrieved, top_n=5)

    answer, citations = generate_answer(query, reranked)
    end = time.time()

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for i, c in enumerate(citations):
        st.markdown(f"**[{i+1}] Source:** {c['source']} (chunk {c['chunk']})")

    st.caption(f"⏱️ Time: {round(end-start, 2)}s")
if st.button("Clear Memory"):
    clear_index()
    st.success("🗑️ Memory cleared! All vectors removed from Pinecone.")