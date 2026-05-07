from langchain_core.documents import Document

from app.vectorstores.chroma_store import get_vectorstore
from app.retrievers.vector_retriever import retrieve_documents

vectorstore = get_vectorstore()

documents = [
    Document(
        page_content="Experienced in FastAPI and LangChain development",
        metadata={"source": "resume"},
    ),
    Document(
        page_content="Built RAG pipelines using ChromaDB and Ollama",
        metadata={"source": "resume"},
    ),
    Document(
        page_content="Worked with machine learning and NLP systems",
        metadata={"source": "resume"},
    ),
]

vectorstore.add_documents(documents)

print("Documents inserted successfully")

results = retrieve_documents("Experience with retrieval augmented generation")

print("\nRetrieved Results:\n")

for doc in results:
    print(doc.page_content)
