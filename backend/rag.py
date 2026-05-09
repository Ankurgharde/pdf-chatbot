import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from backend.pinecone_db import get_vectorstore

load_dotenv()

# ---------------------------
# CHECK API KEY
# ---------------------------
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY missing in .env")

# ---------------------------
# LLM (GPT)
# ---------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# ---------------------------
# ASK QUESTION
# ---------------------------
def ask_question(query: str):

    vectorstore = get_vectorstore()

    # Retrieve relevant chunks
    docs = vectorstore.similarity_search(query, k=5)

    if not docs:
        return {
            "answer": "No relevant information found in uploaded PDFs."
        }

    # Build context
    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
You are a helpful AI assistant.
Answer ONLY using the context below.

Context:
{context}

Question:
{query}

If answer is not present, say: "I don't know based on uploaded documents."
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content,
        "sources": [d.metadata for d in docs]
    }