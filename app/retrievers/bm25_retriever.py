from langchain_community.retrievers import BM25Retriever

"""BM25 retrieval is used for exact keyword matching. It helps retrieve documents containing specific skills, acronyms, or technical terms like FastAPI, RAG, and NLP. This complements vector retrieval, which captures semantic meaning but may miss exact matches"""


def create_bm25_retriever(documents, k: int = 5):
    return BM25Retriever.from_documents(documents, k=k)
