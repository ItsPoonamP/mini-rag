import tiktoken

tokenizer = tiktoken.get_encoding("cl100k_base")

def chunk_text(text, chunk_size=1000, overlap=150):
    tokens = tokenizer.encode(text)
    chunks = []

    start = 0
    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]
        chunks.append(tokenizer.decode(chunk_tokens))
        start += chunk_size - overlap

    return chunks
