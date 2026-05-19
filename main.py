import argparse
import os

from modules.pdf_extractor import extract_pdf_text
from modules.preprocess_calamancy import preprocess_text
from modules.cleaner import clean_text
from modules.chunker import create_chunks
from modules.scorer import score_chunk
from modules.aggregator import aggregate
from modules.report import save_json


def run_pipeline(mode):
    # 1. Extract PDF
    pages = extract_pdf_text("input/dissertation.pdf")

    # 2. Preprocess
    cleaned_pages = preprocess_text(pages)

    # 3. Merge pages
    merged_text = " ".join([p["cleaned_text"] for p in cleaned_pages])

    # 4. Clean text
    final_text = clean_text(merged_text)

    # 5. Chunking (always needed)
    chunks = create_chunks(final_text)
    save_json(chunks, "output/chunks.json")

    if mode == "chunking":
        print("DONE - Chunking only")
        return

    # 6. Scoring
    scores = []
    for c in chunks:
        result = score_chunk(c)
        result["chunk_id"] = c["chunk_id"]
        scores.append(result)

    save_json(scores, "output/scores.json")

    if mode == "scoring":
        print("DONE - Chunking + Scoring only")
        return

    # 7. Aggregation
    final = aggregate(scores)
    save_json(final, "output/final_report.json")

    print("DONE - Full pipeline complete")


def main():
    parser = argparse.ArgumentParser(description="AES Dissertation Pipeline")

    parser.add_argument(
        "--mode",
        type=str,
        default="full",
        choices=["chunking", "scoring", "full"],
        help="Pipeline mode to run"
    )

    args = parser.parse_args()

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    run_pipeline(args.mode)


if __name__ == "__main__":
    main()