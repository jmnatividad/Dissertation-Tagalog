from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def score_chunk(chunk_text):
    prompt = f"""
You are a doctoral dissertation evaluator.

Evaluate this dissertation chunk based on:
1. Clarity
2. Grammar
3. Academic Tone
4. Methodological Rigor
5. Originality

Return ONLY valid JSON:
{{
  "clarity": 0-100,
  "grammar": 0-100,
  "academic_tone": 0-100,
  "methodology": 0-100,
  "originality": 0-100,
  "overall_score": 0-100,
  "feedback": "Detailed critique"
}}

TEXT:
{chunk_text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": "You are an academic dissertation evaluator."},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content)