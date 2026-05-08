from app.ingestion.ingest_resume import ingest_resume
from app.retrievers.vector_retriever import retrieve_documents
from app.vectorstores.chroma_store import get_vectorstore

# reset collection for testing
vectorstore = get_vectorstore()
vectorstore.delete_collection()
vectorstore = get_vectorstore()
# ingest resume
ingest_resume("data/resumes/Bharadwaj VSC Resume.pdf")
# query
results = retrieve_documents("Experience with RAG pipelines")


for doc, score in results:
    print(f"Score: {score}")
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 50)
