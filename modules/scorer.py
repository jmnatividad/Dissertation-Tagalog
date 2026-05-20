from openai import OpenAI
import json
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

EVALUATION_PROMPT = """
Ikaw ay isang eksperto sa pagsusuri ng akademikong sanaysay sa Filipino.

Ang iyong gawain ay bigyan ng patas, obhetibo, at mahigpit na marka ang isang bahagi ng sanaysay.

HUWAG maging maluwag sa pagbibigay ng marka. Batay lamang sa nilalaman ng teksto ang iyong pagsusuri.

---

PAMANTAYAN SA PAGMAMARKA (Kabuuan = 100):

1. Nilalaman (40%)
- Kaugnayan sa paksa
- Lalim ng ideya
- Pagsuporta sa argumento

2. Organisasyon (25%)
- Lohikal na pagkakaayos ng ideya
- Daloy ng talata

3. Gamit ng Wika (20%)
- Gramatika
- Estruktura ng pangungusap
- Kalinawan ng pagpapahayag

4. Mekaniks (15%)
- Baybay
- Bantas
- Tamang gamit ng salita

---

MGA PANUNTUNAN:
- Ang bawat kategorya ay dapat may tamang score base sa bigat nito
- Ang kabuuang marka ay ang suma ng lahat ng kategorya
- Karaniwang sanaysay ng estudyante: 60–75
- Mahusay na akademikong sulatin: 80–100

---

OUTPUT FORMAT (JSON LAMANG):

{
  "chunks": [
    {
      "chunk_id": "id ng chunk",
      "scores": {
        "nilalaman": number,
        "organisasyon": number,
        "gamit_ng_wika": number,
        "mekaniks": number
      },
      "overall_score": number
    }
  ],

  "overall_score": number,
  "feedback": "Tagalog feedback",
  "justification": "Maikling paliwanag kung bakit ibinigay ang score"
}

---

MGA TAGUBILIN:
- Ang feedback at justification ay dapat nasa wikang Filipino.
- Huwag lalampas sa 3–5 pangungusap ang feedback.
- Dapat malinaw, diretso, at may mungkahi para sa pagpapabuti.
- Ang overall_score sa bawat chunk ay dapat eksaktong suma ng apat (4) na kategorya:
  nilalaman + organisasyon + gamit_ng_wika + mekaniks
- Ang "overall_score" sa bawat chunk ay isang (1) value lamang.
- Hindi ito maaaring i-average o i-scale — eksaktong suma lamang.

- Ang FINAL overall_score (sa labas ng chunks) ay ang kabuuang average o pinagsamang resulta ng lahat ng chunks (depende sa evaluator design), ngunit dapat malinaw na hiwalay sa per-chunk scores.

FORMULA (per chunk):
overall_score = nilalaman + organisasyon + gamit_ng_wika + mekaniks



ESSAY:
\"\"\"{text}\"\"\"
"""


def score_chunk(chunk):
    response = client.chat.completions.create(
        model=config.MODEL_NAME,
        messages=[
            {"role": "system", "content": "Strict Filipino academic evaluator."},
            {"role": "user", "content": EVALUATION_PROMPT.format(text=chunk["text"])}
        ],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)