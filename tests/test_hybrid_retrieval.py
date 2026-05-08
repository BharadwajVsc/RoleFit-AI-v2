from app.ingestion.ingest_resume import ingest_resume
from app.retrievers.hybrid_retriever import hybrid_retriever
from app.vectorstores.chroma_store import get_vectorstore

# Reset vectorstore
vectorstore = get_vectorstore()

vectorstore.delete_collection()

vectorstore = get_vectorstore()


# Ingest Resume
documents = ingest_resume("data/resumes/Bharadwaj VSC Resume.pdf")

# Query
query = (
    "Experience with Generative AI, RAG, prompt engineering, and FastAPI development"
)

# Hybrid Retrieval
results = hybrid_retriever(query, documents)

print("\n================ VECTOR RETRIEVAL ================\n")
for doc, score in results["vector_results"]:

    print(f"Score: {score}")

    print(doc.page_content)

    print(doc.metadata)

    print("-" * 50)

print("\n================ BM25 RETRIEVAL ================\n")
for doc in results["bm25_results"]:
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 50)
