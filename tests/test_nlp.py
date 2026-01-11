from app.nlp.preprocessing import preprocess_text
from app.nlp.skills import extract_skills

def test_preprocess_text_basic():
    text = "Worked on Machine Learning and NLP!"
    processed = preprocess_text(text)
    assert "machine" in processed
    assert "learning" in processed
    assert "nlp" in processed
    assert processed == processed.lower()

def test_extract_skills_found():
    text = "Experience in Python, FastAPI, and Docker."
    skills = extract_skills(text)
    assert "python" in skills
    assert "fastapi" in skills
    assert "docker" in skills

def test_extract_skills_none():
    text = "This candidate is skilled in cooking and painting."
    skills = extract_skills(text)
    assert skills == []
