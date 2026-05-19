# Dissertation AES (Automated Essay Scoring) System for Filipino Essays

## Overview

This project is a Python-based Automated Essay Scoring (AES) system designed for evaluating Filipino (Tagalog) essays using Artificial Intelligence and Natural Language Processing (NLP).

The system processes essays from PDF files, preprocesses the text using Calamancy (Tagalog NLP library), divides the essay into manageable chunks, evaluates each chunk using OpenAI, and generates structured scoring reports based on a predefined Filipino essay rubric.

---

# System Objectives

The system aims to:

- Automatically evaluate Tagalog essays
- Provide rubric-based scoring
- Support Filipino language preprocessing
- Generate consistent and structured results
- Reduce manual checking workload for teachers
- Serve as a research-grade AES prototype

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenAI API | AI-based essay scoring |
| Calamancy | Filipino NLP preprocessing |
| PyMuPDF (fitz) | PDF text extraction |
| Tiktoken | Token counting for chunking |
| Docker | Containerized deployment |

---

# Project Structure

```text
dissertation-aes/
│
├── Dockerfile
├── requirements.txt
├── config.py
├── main.py
│
├── input/
│   └── dissertation.pdf
│
├── output/
│   ├── chunks.json
│   ├── scores.json
│   └── final_report.json
│
└── modules/
    ├── pdf_extractor.py
    ├── preprocess_calamancy.py
    ├── cleaner.py
    ├── chunker.py
    ├── scorer.py
    ├── aggregator.py
    └── report.py
```

---

# Application Flow

The system follows the pipeline below:

```text
PDF Input
   ↓
PDF Extraction
   ↓
Tagalog NLP Preprocessing (Calamancy)
   ↓
Text Cleaning
   ↓
Essay Chunking
   ↓
AI-Based Essay Scoring
   ↓
Score Aggregation
   ↓
Final JSON Report Generation
```

---

# Detailed File Documentation

---

# 1. main.py

## Purpose

Acts as the main controller of the application.

This file orchestrates the entire AES pipeline from PDF extraction up to final report generation.

## Responsibilities

- Starts the application
- Calls all processing modules
- Controls processing order
- Saves final outputs

## Flow Inside main.py

```text
Extract PDF
→ Preprocess Text
→ Clean Text
→ Create Chunks
→ Score Chunks
→ Aggregate Scores
→ Generate Reports
```

---

# 2. config.py

## Purpose

Stores application configuration values.

## Responsibilities

- OpenAI API Key
- Model configuration
- Chunk token limits

## Example Variables

```python
OPENAI_API_KEY
MODEL_NAME
MAX_TOKENS
```

---

# 3. modules/pdf_extractor.py

## Purpose

Extracts raw text from PDF files using PyMuPDF.

## Responsibilities

- Opens PDF documents
- Reads each page
- Extracts text content
- Returns page-by-page data

## Input

```text
PDF file
```

## Output

```python
[
    {
        "page": 1,
        "text": "sample text"
    }
]
```

---

# 4. modules/preprocess_calamancy.py

## Purpose

Performs Filipino NLP preprocessing using Calamancy.

## Responsibilities

- Tokenizes Filipino text
- Removes unnecessary spaces
- Normalizes text
- Converts tokens into clean NLP-friendly format

## Why It Is Important

This module improves:
- linguistic consistency
- token quality
- downstream AI scoring accuracy

## Example Process

```text
Raw Text
↓
Calamancy NLP
↓
Clean Tokens
↓
Normalized Text
```

---

# 5. modules/cleaner.py

## Purpose

Performs additional text cleanup after NLP preprocessing.

## Responsibilities

- Removes extra spaces
- Fixes punctuation spacing
- Normalizes formatting

## Why It Is Needed

Even after NLP preprocessing, PDFs may contain:
- broken spacing
- formatting noise
- inconsistent punctuation

This module ensures cleaner input for chunking and AI scoring.

---

# 6. modules/chunker.py

## Purpose

Splits essays into manageable chunks for AI evaluation.

## Responsibilities

- Counts tokens
- Prevents oversized AI prompts
- Maintains chunk coherence
- Groups text into safe scoring blocks

## Why Chunking Is Important

OpenAI models have token limits.

Chunking:
- prevents context overflow
- improves scoring consistency
- reduces API errors

## Chunking Strategy

The system uses:
- token-based chunking
- paragraph-aware splitting
- coherence preservation

---

# 7. modules/scorer.py

## Purpose

Evaluates essay chunks using OpenAI.

## Responsibilities

- Sends essay chunks to OpenAI
- Uses rubric-based evaluation
- Returns structured scores
- Generates Filipino feedback

## Rubric Used

| Category | Weight |
|---|---|
| Nilalaman | 40% |
| Organisasyon | 25% |
| Gamit ng Wika | 20% |
| Mekaniks | 15% |

## Output Example

```json
{
  "nilalaman": 35,
  "organisasyon": 20,
  "gamit_ng_wika": 18,
  "mekaniks": 12,
  "feedback": "Malinaw ang ideya ngunit kulang sa detalye."
}
```

---

# 8. modules/aggregator.py

## Purpose

Combines all chunk scores into one final score.

## Responsibilities

- Averages category scores
- Applies rubric weights
- Computes final grade

## Why Aggregation Is Needed

Essays may contain multiple chunks.

This module ensures:
- fair scoring
- balanced evaluation
- consistent final computation

---

# 9. modules/report.py

## Purpose

Handles JSON report generation.

## Responsibilities

- Saves chunk outputs
- Saves scoring results
- Saves final reports

## Generated Files

| File | Description |
|---|---|
| chunks.json | Essay chunks |
| scores.json | Chunk-level scores |
| final_report.json | Final aggregated result |

---

# Input Folder

## Purpose

Stores PDF essays to be evaluated.

## Example

```text
input/dissertation.pdf
```

---

# Output Folder

## Purpose

Stores generated system outputs.

## Generated Outputs

### chunks.json
Contains essay chunks.

### scores.json
Contains scores per chunk.

### final_report.json
Contains final aggregated scores and feedback.

---

# Docker Usage

## Build Container

```bash
docker build -t dissertation-aes .
```

## Run Container

```bash
docker run -dit --name aes_container -v %cd%:/app dissertation-aes
```

## Enter Container

```bash
docker exec -it aes_container bash
```

## Run Application

```bash
python main.py
```

---

# System Workflow Summary

## Step 1 — PDF Extraction

The system reads PDF essays and extracts page-level text.

## Step 2 — NLP Preprocessing

Calamancy processes Filipino text for normalization and tokenization.

## Step 3 — Cleaning

Additional formatting cleanup is applied.

## Step 4 — Chunking

The essay is divided into AI-safe chunks.

## Step 5 — AI Evaluation

Each chunk is evaluated using OpenAI and the Filipino rubric.

## Step 6 — Aggregation

Chunk scores are merged into a final score.

## Step 7 — Report Generation

Structured JSON reports are saved to the output folder.

---

# Future Improvements

Possible future upgrades:

- Plagiarism Detection
- Human vs AI Score Comparison
- FastAPI Backend
- Web Dashboard
- Real-Time Essay Evaluation
- Batch Essay Processing
- Advanced Filipino Grammar Analysis
- Semantic Chunking
- Teacher Calibration System

---

# Author Notes

This project is intended as:
- an AI-assisted educational tool
- a research prototype
- a Filipino NLP application
- a foundation for future AES systems

The system combines:
- Natural Language Processing
- AI-based evaluation
- rubric-based assessment
- Filipino language processing

to support automated essay scoring in educational environments.

---
