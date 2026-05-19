def aggregate(scores):
    weights = {
        "nilalaman": 0.40,
        "organisasyon": 0.25,
        "gamit_ng_wika": 0.20,
        "mekaniks": 0.15
    }

    total = {}

    for k in weights:
        total[k] = sum(s[k] for s in scores) / len(scores)

    total["final_score"] = round(
        sum(total[k] * weights[k] for k in weights),
        2
    )

    return total