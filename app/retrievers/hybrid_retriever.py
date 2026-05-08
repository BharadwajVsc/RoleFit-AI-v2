from app.retrievers.vector_retriever import retrieve_documents
from app.retrievers.bm25_retriever import create_bm25_retriever

"""Hybrid retrieval combines semantic vector search and BM25 keyword search to improve retrieval accuracy. Vector search understands meaning/context, while BM25 improves exact skill and keyword matching."""


def hybrid_retriever(query, documents):

    # vector retrieval
    vector_results = retrieve_documents(query)

    # BM25 retrieval
    bm25_retriever = create_bm25_retriever(documents)
    bm25_results = bm25_retriever.invoke(query)

    return {"vector_results": vector_results, "bm25_results": bm25_results}
