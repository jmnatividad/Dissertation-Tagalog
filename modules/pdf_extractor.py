import fitz  # PyMuPDF

def extract_pdf_text(pdf_path):
    full_text = []

    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc):
            text = page.get_text("text")
            full_text.append({
                "page": page_num + 1,
                "text": text
            })

    return full_text