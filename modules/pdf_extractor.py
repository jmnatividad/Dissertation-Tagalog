import fitz  # PyMuPDF

def extract_pdf_text(pdf_path):
    pages = []

    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc):
            text = page.get_text("text")
            text = text.replace("\n", " ").strip()

            pages.append({
                "page": page_num + 1,
                "text": text
            })

    return pages