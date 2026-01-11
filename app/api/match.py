from fastapi import APIRouter, HTTPException
from app.models.schemas import MatchRequest, MatchResponse
from app.nlp.preprocessing import preprocess_text
from app.nlp.skills import extract_skills
from app.nlp.similarity import tfidf_similarity, bert_similarity
from app.core.thresholds import match_level

router = APIRouter(tags=["Resume–Job Matching"])


def normalize_score(raw_score: float, model: str) -> float:
    if model == "tfidf":
        score = raw_score * 120
    else:
        score = raw_score * 100
    return min(round(score, 2), 100.0)


def confidence_label(score: float) -> str:
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"


@router.post("/match", response_model=MatchResponse)
def match_resume_job(payload: MatchRequest):
    if not payload.resume_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty")

    if not payload.job_text.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty")

    if len(payload.resume_text.strip()) < 10 or len(payload.job_text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Text too short for meaningful comparison")

    # 1️⃣ Preprocess
    resume_clean = preprocess_text(payload.resume_text)
    job_clean = preprocess_text(payload.job_text)

    # 2️⃣ Similarity
    if payload.model == "tfidf":
        raw_score = tfidf_similarity(resume_clean, job_clean)
    else:
        raw_score = bert_similarity(resume_clean, job_clean)

    final_score = normalize_score(raw_score, payload.model)

    # 3️⃣ Labels
    confidence = confidence_label(final_score)
    level = match_level(final_score)

    # 4️⃣ Skills
    resume_skills = extract_skills(payload.resume_text)
    job_skills = extract_skills(payload.job_text)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    return MatchResponse(
        match_score=final_score,
        confidence=confidence,
        match_level=level,
        model_used=payload.model,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )
