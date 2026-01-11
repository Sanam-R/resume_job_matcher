from pydantic import BaseModel
from typing import List, Literal

class MatchRequest(BaseModel):
    resume_text: str
    job_text: str
    model: Literal["tfidf", "bert"] = "bert"


class MatchResponse(BaseModel):
    match_score: float
    confidence: str
    match_level: str
    model_used: str
    matched_skills: List[str]
    missing_skills: List[str]

