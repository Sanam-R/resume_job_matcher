from fastapi import FastAPI
from app.api.match import router as match_router

app = FastAPI(
    title="Resume Job Matcher",
    version="1.0.0"
)

app.include_router(match_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "OK"}
