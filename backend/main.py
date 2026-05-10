import os
from fastapi import FastAPI, UploadFile, File
from typing import List
from dotenv import load_dotenv
from ingest import process_pdf
from rag import ask_question

load_dotenv()

app = FastAPI(title="PDF Chatbot API")


# ---------------- HOME ----------------
@app.get("/")
def home():
    return {"message": "API running successfully "}


# ---------------- UPLOAD ----------------
@app.post("/upload")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    results = []

    for file in files:
        content = await file.read()

        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as f:
            f.write(content)

        chunk_count = process_pdf(temp_path)

        os.remove(temp_path)

        results.append({
            "file": file.filename,
            "chunks": chunk_count
        })

    return {
        "message": "Upload successful",
        "data": results
    }


# ---------------- CHAT ----------------
@app.get("/chat")
def chat(query: str):
    return ask_question(query)