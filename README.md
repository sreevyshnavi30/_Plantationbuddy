<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 56be44e (serve.py)
# PlantationBuddy RAG Starter

This is a Retrieval-Augmented Generation (RAG) starter kit for building a farmer knowledge base.

## Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your URLs (ICAR, FAO, TNAU, etc.) into `kb/urls.txt`.

3. Build knowledge base:
   ```bash
   python ingest.py --urls kb/urls.txt --persist ./chroma_store
   ```

4. Start Q&A:
   ```bash
   python serve.py --persist ./chroma_store
   ```

5. Optional: Log to Google Sheets:
   ```bash
   python serve.py --persist ./chroma_store      --sheet "PlantationBuddy_QA"      --service_json "path/to/service_account.json"
   ```
<<<<<<< HEAD
=======
# plantation-Buddy
>>>>>>> 6f71636 (Initial commit)
=======
>>>>>>> 56be44e (serve.py)
