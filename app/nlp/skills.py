SKILLS_DB = {
    "python", "django", "flask", "fastapi",
    "sql", "postgresql", "docker",
    "nlp", "machine learning", "rest"
}

def extract_skills(text: str):
    words = set(text.split())
    return list(words & SKILLS_DB)
