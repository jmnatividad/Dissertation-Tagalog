# Dissertation-Tagalog
AI-powered Dissertation Evaluation Pipeline that processes large PDF documents through extraction, NLP preprocessing (calamanCy), intelligent chunking, and OpenAI-based scoring to generate structured academic assessment and aggregated results.


# 🧠 AI Dissertation Evaluation Pipeline

A Python-based prototype system that evaluates large academic dissertations (200–300+ pages) using a modular AI pipeline. The system breaks down documents into manageable components, applies NLP preprocessing, and uses OpenAI API to generate structured scoring with final aggregation.

---

## 🚀 Project Goal

To build a scalable and intelligent evaluation system for doctoral dissertations that can:

- Handle large PDF documents (200–300+ pages)
- Perform language-aware preprocessing (including Tagalog support)
- Break content into meaningful chunks
- Evaluate sections using AI scoring (OpenAI API)
- Aggregate results into a final structured grade

---

## 🏗️ System Pipeline

The system follows this step-by-step architecture:

### 1. 📄 PDF Extraction
- Extract raw text from dissertation PDFs
- Preserve structure when possible (chapters, headings, sections)

### 2. 🧹 NLP Preprocessing (calamanCy)
- Language processing using **calamanCy**
- Tokenization, sentence segmentation, and normalization
- Support for Tagalog / Filipino text preprocessing

### 3. ✂️ Chunking Engine
- Splits document into logical sections
- Prevents token overflow
- Maintains context per section

### 4. 🤖 OpenAI API Evaluation
- Each chunk is sent to OpenAI API
- Generates:
  - Section score
  - Feedback
  - Rubric-based evaluation

### 5. 📊 Score Aggregator
- Combines all section scores
- Computes final weighted score
- Generates summary evaluation report

---

## 🧰 Tech Stack

- Python 3.10+
- PyPDF2 / pdfminer.six (PDF extraction)
- calamanCy (NLP preprocessing)
- OpenAI API
- NumPy / Pandas (score aggregation)
- (Optional) FastAPI for future API layer

---

## 📁 Project Structure
ai-dissertation-evaluator/
│
├── data/ # Sample PDFs
├── extractor/ # PDF extraction module
├── preprocessing/ # calamanCy NLP pipeline
├── chunking/ # text segmentation logic
├── evaluator/ # OpenAI scoring engine
├── aggregator/ # score aggregation logic
├── utils/ # helpers and configs
├── main.py # pipeline entry point
└── README.md


---

## ⚙️ How It Works

1. Load PDF file
2. Extract raw text
3. Preprocess using calamanCy
4. Split into chunks
5. Send each chunk to OpenAI API for scoring
6. Collect and aggregate results
7. Output final evaluation report

---

## 📦 Installation

```bash
