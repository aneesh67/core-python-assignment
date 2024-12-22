def feedback(ratings):
    if not ratings:
        return "No ratings available."
    pos = sum(1 for r in ratings if r >= 4)
    return f"Positive Feedback: {pos / len(ratings) * 100:.1f}%"

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(feedback(ratings))
