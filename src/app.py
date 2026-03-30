from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.summarizer import summarize_text
import os

app = FastAPI(title="News Summarizer API")

class ArticleRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize_endpoint(request: ArticleRequest):
    if len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
        
    summary = summarize_text(request.text)
    return {"summary": summary}

@app.get("/health")
def health():
    return {"status": "ok"}
