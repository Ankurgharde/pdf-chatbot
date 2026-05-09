from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from backend.pinecone_db import get_vectorstore

def process_pdf(file_path, metadata=None):
    # -------------------------
    # Load PDF (more powerful loader)
    # -------------------------
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()

    # Safety check
    if not docs:
        raise ValueError("PDF could not be read or is empty")

    # Combine text to validate extraction
    full_text = "\n".join([doc.page_content for doc in docs]).strip()

    if not full_text:
        raise ValueError("No readable text found in PDF (maybe scanned PDF)")

    # -------------------------
    # Split into chunks
    # -------------------------
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    if not chunks:
        raise ValueError("No chunks created from PDF")

    # -------------------------
    # Add metadata
    # -------------------------
    if metadata:
        for chunk in chunks:
            chunk.metadata.update(metadata)

    # -------------------------
    # Store in Pinecone
    # -------------------------
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)

    return len(chunks)