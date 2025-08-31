import argparse
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.chains import RetrievalQA

def run_query(query, persist="db", model="gemma:2b"):
    """Run a single query (used by Streamlit or CLI)"""
    # Use Ollama embeddings (nomic-embed-text is lightweight & fast)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Load existing Chroma DB
    vectorstore = Chroma(
        persist_directory=persist,
        embedding_function=embeddings
    )

    # Use Gemma (or another Ollama LLM passed via CLI)
    llm = OllamaLLM(model=model)

    # Retrieval-based QA chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
    )

    result = qa.invoke(query)
    return result["result"]

# ---------------- CLI mode ----------------
def get_args():
    parser = argparse.ArgumentParser(description="Query the Chroma DB with Ollama")
    parser.add_argument(
        "--persist",
        type=str,
        default="db",
        help="Folder where Chroma DB is stored"
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gemma:2b",
        help="Ollama model for answering queries (default: gemma:2b)"
    )
    return parser.parse_args()

def main():
    args = get_args()
    print(f"✅ Ready! Using model: {args.model}")
    print("Type your questions (or 'exit' to quit):")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        try:
            result = run_query(query, persist=args.persist, model=args.model)
            print("Bot:", result)
        except Exception as e:
            print("⚠️ Error:", str(e))

if __name__ == "__main__":
    main()
