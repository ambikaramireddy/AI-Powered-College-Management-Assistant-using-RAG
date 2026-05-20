from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

from src.router import classify_query
from src.pdf_rag import get_retriever
from src.llm_client import hf_chat
from src.prompts import general_prompt, college_prompt

# ---------------------------------------------------
# FASTAPI APP
# ---------------------------------------------------

app = FastAPI(
    title="College Management RAG API",
    description="AI-powered College Management Assistant using RAG",
    version="1.0.0"
)

# ---------------------------------------------------
# LOAD RETRIEVER
# ---------------------------------------------------

try:

    retriever = get_retriever("data")

    print("✅ Knowledge base loaded successfully")

except Exception as e:

    retriever = None

    print(f"❌ Error loading retriever: {e}")

# ---------------------------------------------------
# REQUEST / RESPONSE MODELS
# ---------------------------------------------------

class QueryRequest(BaseModel):
    question: str


class SourceResponse(BaseModel):
    source: str
    page: int
    text: str


class QueryResponse(BaseModel):
    route: str
    question: str
    answer: str
    sources: Optional[List[SourceResponse]] = []


# ---------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------

@app.get("/")
async def root():

    return {
        "message": "🎓 College Management RAG API Running",
        "status": "success"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }

# ---------------------------------------------------
# MAIN QUERY API
# ---------------------------------------------------

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):

    user_input = request.question.strip()

    if not user_input:

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    # ---------------------------------------------------
    # QUERY CLASSIFICATION
    # ---------------------------------------------------

    route = classify_query(user_input)

    history = ""

    # ---------------------------------------------------
    # GENERAL CHAT
    # ---------------------------------------------------

    greetings = ["hi", "hello", "hey"]

    if user_input.lower() in greetings:

        return {
            "route": "GENERAL",
            "question": user_input,
            "answer": "Hello 👋 How can I help you today?",
            "sources": []
        }

    if "your name" in user_input.lower():

        return {
            "route": "GENERAL",
            "question": user_input,
            "answer": "I am Alex, your AI College Assistant 🎓",
            "sources": []
        }

    # ---------------------------------------------------
    # GENERAL RESPONSE
    # ---------------------------------------------------

    if route == "GENERAL":

        answer = hf_chat(
            general_prompt(
                user_input,
                history
            )
        )

        return {
            "route": route,
            "question": user_input,
            "answer": answer,
            "sources": []
        }

    # ---------------------------------------------------
    # RAG RESPONSE
    # ---------------------------------------------------

    if retriever is None:

        raise HTTPException(
            status_code=500,
            detail="Knowledge base not loaded"
        )

    docs = retriever.retrieve(
        user_input,
        top_k=5
    )

    if not docs:

        return {
            "route": route,
            "question": user_input,
            "answer": "❌ Information not found in college documents.",
            "sources": []
        }

    # ---------------------------------------------------
    # CONTEXT CREATION
    # ---------------------------------------------------

    context = "\n\n".join([

        f"[Source: {d['source']}, page {d['page']}]\n{d['text']}"

        for d in docs
    ])

    # ---------------------------------------------------
    # LLM RESPONSE
    # ---------------------------------------------------

    answer = hf_chat(
        college_prompt(
            user_input,
            history,
            context
        )
    )

    # ---------------------------------------------------
    # SOURCE FORMATTING
    # ---------------------------------------------------

    formatted_sources = []

    for d in docs:

        formatted_sources.append({

            "source": d["source"],
            "page": d["page"],
            "text": d["text"][:300]

        })

    # ---------------------------------------------------
    # FINAL RESPONSE
    # ---------------------------------------------------

    return {

        "route": route,
        "question": user_input,
        "answer": answer,
        "sources": formatted_sources
    }

# ---------------------------------------------------
# RUN SERVER
# ---------------------------------------------------

if __name__ == "__main__":

    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )