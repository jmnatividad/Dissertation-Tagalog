import tiktoken
from config import MAX_CHUNK_TOKENS

encoding = tiktoken.encoding_for_model("gpt-4")

def count_tokens(text):
    return len(encoding.encode(text))

def chunk_text(cleaned_pages):
    chunks = []
    current_chunk = []
    current_tokens = 0
    chunk_id = 1

    for page in cleaned_pages:
        page_tokens = count_tokens(page["cleaned_text"])

        if current_tokens + page_tokens > MAX_CHUNK_TOKENS:
            chunks.append({
                "chunk_id": chunk_id,
                "text": "\n".join(current_chunk)
            })
            chunk_id += 1
            current_chunk = []
            current_tokens = 0

        current_chunk.append(page["cleaned_text"])
        current_tokens += page_tokens

    if current_chunk:
        chunks.append({
            "chunk_id": chunk_id,
            "text": "\n".join(current_chunk)
        })

    return chunks