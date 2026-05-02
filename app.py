from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

from rag import load_data, build_index, retrieve
from prompts import generate_prompt
from database import log_query

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.on_event("startup")
def startup():
    load_data()
    build_index()

@app.post("/ask")
def ask_question(req: QueryRequest):
    context = retrieve(req.query)
    prompt = generate_prompt("\n".join(context), req.query)

    response = model.generate_content(prompt)
    answer = response.text

    log_query(req.query, answer)

    return {
        "query": req.query,
        "answer": answer,
        "context_used": context
    }