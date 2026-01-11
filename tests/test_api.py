from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_match_strong():
    payload = {
        "resume_text": "Python, machine learning, NLP, FastAPI, Docker",
        "job_text": "Looking for Python, ML, NLP, FastAPI, Docker",
        "model": "bert"
    }
    response = client.post("/api/match", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["confidence"] == "High"
    assert data["match_level"] == "Strong Match"

def test_match_empty_resume():
    payload = {
        "resume_text": "",
        "job_text": "Some job description",
        "model": "bert"
    }
    response = client.post("/api/match", json=payload)
    assert response.status_code == 400
