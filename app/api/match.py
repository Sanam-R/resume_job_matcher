from fastapi import APIRouter
from app.models.schemas import MatchRequest, MatchResponse
from app.nlp.preprocessing import preprocess_text
from app.nlp.skills import extract_skills
from app.nlp.similarity import semantic_similarity

router = APIRouter(tags=["Matching"])

@router.post("/match", response_model=MatchResponse)
def match_resume_job(payload: MatchRequest):
    resume_clean = preprocess_text(payload.resume_text)
    job_clean = preprocess_text(payload.job_text)

    score = semantic_similarity(resume_clean, job_clean)

    resume_skills = extract_skills(resume_clean)
    job_skills = extract_skills(job_clean)

    return MatchResponse(
        match_score=round(score * 100, 2),
        matched_skills=list(set(resume_skills) & set(job_skills)),
        missing_skills=list(set(job_skills) - set(resume_skills))
    )
