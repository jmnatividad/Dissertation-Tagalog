def aggregate_scores(scores):
    total = {
        "clarity": 0,
        "grammar": 0,
        "academic_tone": 0,
        "methodology": 0,
        "originality": 0,
        "overall_score": 0
    }

    for score in scores:
        for key in total:
            total[key] += score[key]

    count = len(scores)

    return {key: round(value / count, 2) for key, value in total.items()}