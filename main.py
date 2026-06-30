from gemini_service import get_ai_response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Backend Working"}

@app.post("/chat")
def chat(request: ChatRequest):

    ai_reply = get_ai_response(request.message)

    return {
        "reply": ai_reply
    }