# Prototype Update

## Overview
A full Python-based automated scoring prototype has been created for dissertation evaluation. The system uses a multi-stage pipeline to process academic text and generate structured evaluation outputs using OpenAI API.

## Pipeline Description
The current workflow includes:

1. **Preprocessing**
   - Uses Calamancy NLP (Calamancy / CalamanCy model) for text normalization and linguistic processing
   - Cleans and prepares raw dissertation text for analysis

2. **Chunking**
   - Splits large dissertation documents into manageable sections
   - Ensures context preservation per section for accurate evaluation

3. **AI Scoring (OpenAI Integration)**
   - Each chunk is sent to OpenAI API
   - Uses predefined academic rubrics for evaluation
   - Generates structured scoring and feedback per section

## Current Limitations / Notes

- **OpenAI API Requirement**
  - The system requires an active OpenAI API subscription/key to fully test and run evaluations.

- **Training / Prompt Quality Dependency**
  - No model training is performed.
  - Performance depends heavily on prompt design and reference behavior examples.

- **Need for Verified Dissertation Samples**
  - High-quality, verified doctoral dissertation examples are needed.
  - These samples will be used as *reference behavior inputs* in prompts to improve scoring accuracy.
  - This ensures the system simulates proper doctoral-level evaluation standards without training a model.

## Future Improvement Direction

- Incorporate validated doctoral dissertation cases as prompt references
- Improve rubric engineering for more consistent scoring
- Enhance chunk-level coherence checking before evaluation
- Optimize OpenAI prompt strategy for academic tone consistency