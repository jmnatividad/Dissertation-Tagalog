import calamancy

nlp = calamancy.load("tl_calamancy_md-0.1.0")

def preprocess_text(pages):
    cleaned_pages = []

    for page_data in pages:
        doc = nlp(page_data["text"])

        tokens = [
            token.text.lower()
            for token in doc
            if not token.is_space
        ]

        cleaned_pages.append({
            "page": page_data["page"],
            "cleaned_text": " ".join(tokens)
        })

    return cleaned_pages