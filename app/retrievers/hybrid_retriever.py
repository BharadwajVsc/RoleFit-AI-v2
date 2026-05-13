from app.retrievers.vector_retriever import retrieve_documents
from app.retrievers.bm25_retriever import create_bm25_retriever
import logging

"""Hybrid retrieval combines semantic vector search and BM25 keyword search to improve retrieval accuracy. Vector search understands meaning/context, while BM25 improves exact skill and keyword matching."""


def hybrid_retriever(query, documents):

    # vector retrieval
    vector_results = retrieve_documents(query)

    # BM25 retrieval
    bm25_retriever = create_bm25_retriever(documents)
    bm25_results = bm25_retriever.invoke(query)

    # fusion of results

    combined_results = []
    seen_chunks = set()
    # adding vector results first
    for doc, score in vector_results:
        """if score > 1:
        continue"""
        chunk_id = doc.metadata.get("chunk_id")
        if chunk_id not in seen_chunks:
            combined_results.append(
                {"document": doc, "score": score, "retriever": "vector"}
            )

        seen_chunks.add(chunk_id)

    # adding BM25 results next, ensuring no duplicates
    for doc in bm25_results:
        chunk_id = doc.metadata.get("chunk_id")
        if chunk_id not in seen_chunks:
            combined_results.append(
                {"document": doc, "score": "score", "retriever": "bm25"}
            )

        seen_chunks.add(chunk_id)
    logging.info(f"Hybrid retrieval returned {len(combined_results)} results")
    return combined_results
