from langchain_core.documents import Document

from app.vectorstores.chroma_store import get_vectorstore
from app.retrievers.vector_retriever import retrieve_documents
import logging

logging.basicConfig(level=logging.INFO)

vectorstore = get_vectorstore()
vectorstore.delete_collection()

vectorstore = get_vectorstore()

documents = [
    Document(
        page_content="Experienced in FastAPI and LangChain development",
        metadata={"source": "resume", "doc_id": "resume_001"},
    ),
    Document(
        page_content="Built RAG pipelines using ChromaDB and Ollama",
        metadata={"source": "resume", "doc_id": "resume_001"},
    ),
    Document(
        page_content="Worked with machine learning and NLP systems",
        metadata={"source": "resume", "doc_id": "resume_001"},
    ),
]

vectorstore.add_documents(documents)

logging.info("Documents inserted successfully")

results = retrieve_documents("Experience with RAG pipelines")

print("\nRetrieved Results:\n")

for doc, score in results:

    print(f"Score: {score}")

    print(doc.page_content)

    print(doc.metadata)

    print("-" * 50)
