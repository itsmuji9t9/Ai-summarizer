from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarizer import get_ai_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatbotRequest(BaseModel):
    text: str

@app.post("/api/summarize")
async def summarize_endpoint(request: ChatbotRequest):
    # Await the new async function
    summary = await get_ai_summary(request.text)
    return {"summary": summary}
