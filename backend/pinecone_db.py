import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeStore

from pinecone import Pinecone
import httpx

load_dotenv()

# ---------------------------
# INIT PINECONE CLIENT
# ---------------------------
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

INDEX_NAME = os.getenv("PINECONE_INDEX", "pdf-chatbot")

print(f"Using Pinecone Index: {INDEX_NAME}")

# ---------------------------
# EMBEDDINGS
# ---------------------------
http_client = httpx.Client()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    http_client=http_client
)

# ---------------------------
# GET VECTOR STORE
# ---------------------------
def get_vectorstore():
    return PineconeStore.from_existing_index(
        index_name=INDEX_NAME,
        embedding=embeddings
    )