from app.ingestion.ingest_resume import ingest_resume
from app.retrievers.hybrid_retriever import hybrid_retriever
from app.vectorstores.chroma_store import get_vectorstore

import logging

logging.basicConfig(level=logging.INFO)

# Reset vectorstore
vectorstore = get_vectorstore()

vectorstore.delete_collection()

vectorstore = get_vectorstore()

# Ingest Resume
documents = ingest_resume("data/resumes/Bharadwaj VSC Resume.pdf")

# Test queries
queries = [
    "Experience with FastAPI and RAG pipelines",
    "retrieval augmented generation systems",
    "machine learning and NLP",
    "REST API development",
    "LangChain workflows",
]

for query in queries:

    print("\n" + "=" * 80)

    print(f"\nQUERY: {query}\n")

    results = hybrid_retriever(query, documents)

    print(f"Total Results: {len(results)}\n")

    for result in results:

        doc = result["document"]

        score = result["score"]

        retriever = result["retriever"]

        print(f"Retriever: {retriever}")
        print(f"Score: {score}")
        print(doc.page_content)
        print(doc.metadata)
        print(f"Section: {doc.metadata.get('section')}")
        print("-" * 50)
