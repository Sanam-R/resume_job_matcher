import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

SKILL_LIST = [
    "python",
    "django",
    "flask",
    "fastapi",
    "machine learning",
    "deep learning",
    "natural language processing",
    "sql",
    "postgresql",
    "docker",
    "rest api",
    "git",
]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILL_LIST]
matcher.add("SKILLS", patterns)

def extract_skills(text: str):
    doc = nlp(text)
    matches = matcher(doc)

    found_skills = set()
    for _, start, end in matches:
        found_skills.add(doc[start:end].text.lower())

    return list(found_skills)
