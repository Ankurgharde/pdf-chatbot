import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeStore

from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# ---------------------------
# INIT PINECONE CLIENT
# ---------------------------
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = os.getenv("PINECONE_INDEX")

# ---------------------------
# EMBEDDINGS (VERY IMPORTANT)
# ---------------------------
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# ---------------------------
# GET VECTOR STORE
# ---------------------------
def get_vectorstore():
    return PineconeStore.from_existing_index(
        index_name=INDEX_NAME,
        embedding=embeddings
    )