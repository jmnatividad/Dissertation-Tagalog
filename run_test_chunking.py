import json
from modules.pdf_extractor import extract_pdf_text
from modules.preprocess import preprocess_text
from modules.chunker import chunk_text

PDF_PATH = "input/dissertation_tagalog.pdf"

def run_test():
    print("🚀 Starting chunking test pipeline...\n")

    # 1. Extract PDF
    pages = extract_pdf_text(PDF_PATH)
    print(f"✔ Extracted pages: {len(pages)}")

    # Debug (optional)
    print("Sample page text:")
    print(pages[0]["text"][:300], "\n")

    # 2. Preprocess (calamanCy step)
    cleaned_pages = preprocess_text(pages)
    print("✔ Preprocessing done")

    # Debug cleaned sample
    print("Cleaned sample:")
    print(cleaned_pages[0]["cleaned_text"][:300], "\n")

    # 3. Chunking ONLY
    chunks = chunk_text(cleaned_pages)
    print(f"✔ Total chunks created: {len(chunks)}\n")

    # 4. Save output
    output_path = "output/chunks.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"✔ Chunks saved to {output_path}")

    # 5. Show preview of chunks
    print("\n📦 Chunk Preview:")
    for i, chunk in enumerate(chunks[:2]):
        print(f"\n--- Chunk {i+1} ---")
        print(chunk["text"][:300])

if __name__ == "__main__":
    run_test()