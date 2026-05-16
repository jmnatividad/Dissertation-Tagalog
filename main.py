import json
from modules.pdf_extractor import extract_pdf_text
from modules.preprocess import preprocess_text
from modules.chunker import chunk_text
from modules.scorer import score_chunk
from modules.aggregator import aggregate_scores

PDF_PATH = "input/dissertation.pdf"

# Extract
pages = extract_pdf_text(PDF_PATH)

# Preprocess
cleaned_pages = preprocess_text(pages)

# Chunk
chunks = chunk_text(cleaned_pages)

# Score
all_scores = []

for chunk in chunks:
    score = score_chunk(chunk["text"])
    all_scores.append(score)

# Aggregate
final_report = aggregate_scores(all_scores)

# Save
with open("output/final_report.json", "w", encoding="utf-8") as f:
    json.dump(final_report, f, indent=4, ensure_ascii=False)

print("Evaluation Complete!")
print(final_report)