from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# O Render vai injetar essa chave para nós depois
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


class ChatRequest(BaseModel):

    message: str


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = model.generate_content(request.message)
    return {"response": response.text}
