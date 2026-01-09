from pydantic import BaseModel
from typing import List

class MatchRequest(BaseModel):
    resume_text: str
    job_text: str

class MatchResponse(BaseModel):
    match_score: float
    matched_skills: List[str]
    missing_skills: List[str]
