import argparse, datetime, gspread
from oauth2client.service_account import ServiceAccountCredentials
from langchain_community.vectorstores import Chroma
from langchain_ollama import Ollama, OllamaEmbeddings


def log_to_sheets(sheet_name, creds_file, user, query, intent, confidence, reply):
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([user, timestamp, query, intent, confidence, reply])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist", required=True)
    parser.add_argument("--sheet")
    parser.add_argument("--service_json")
    parser.add_argument("--model", default="mistral")  # Ollama model
    args = parser.parse_args()

    # Use Ollama embeddings
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma(persist_directory=args.persist, embedding_function=embeddings)

    # Ollama LLM
    llm = Ollama(model=args.model)

    while True:
        query = input("Farmer: ")
        if query.lower() in ["exit", "quit"]: 
            break

        # Retrieve context
        docs = db.similarity_search(query, k=3)
        context = "\n\n".join([d.page_content for d in docs])

        # Generate answer
        reply = llm.invoke(f"Context:\n{context}\n\nQuestion: {query}\nAnswer:")

        print("Bot:", reply)

        # Optional logging
        if args.sheet and args.service_json:
            log_to_sheets(args.sheet, args.service_json, "User1", query, "N/A", "N/A", reply)


if __name__ == "__main__":
    main()
