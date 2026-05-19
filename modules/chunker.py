import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")
MAX_TOKENS = 500


def count_tokens(text):
    return len(encoding.encode(text))


def create_chunks(text):
    paragraphs = [p.strip() for p in text.split(" ") if p.strip()]

    chunks = []
    current = []
    current_tokens = 0

    for p in paragraphs:
        tokens = count_tokens(p)

        if current_tokens + tokens > MAX_TOKENS:
            chunks.append(" ".join(current))
            current = []
            current_tokens = 0

        current.append(p)
        current_tokens += tokens

    if current:
        chunks.append(" ".join(current))

    return [{"chunk_id": i+1, "text": c} for i, c in enumerate(chunks)]