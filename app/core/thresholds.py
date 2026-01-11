def match_level(score: float) -> str:
    if score >= 75:
        return "Strong Match"
    elif score >= 50:
        return "Partial Match"
    else:
        return "Weak Match"
