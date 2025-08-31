import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

def ingest(persist="db"):
    # 1. Load your knowledge base (replace with real data file(s))
    loader = TextLoader("data/agriculture.txt", encoding="utf-8")
    documents = loader.load()

    # 2. Split into chunks for embeddings
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(documents)

    # 3. Use Ollama embeddings (fast + small memory)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # 4. Build Chroma DB
    vectorstore = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=persist
    )
    vectorstore.persist()

    print("✅ Ingestion complete. Chroma DB stored at:", persist)

if __name__ == "__main__":
    ingest()
