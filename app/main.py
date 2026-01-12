from fastapi import FastAPI
from pydantic import BaseModel
from rag.llm import get_qa_chain

app = FastAPI(title="Customer Support AI Assistant")

qa_chain = get_qa_chain()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(payload: Question):
    answer = qa_chain.run(payload.question)
    return {"answer": answer}
