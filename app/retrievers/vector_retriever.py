from app.vectorstores.chroma_store import get_vectorstore


def retrieve_documents(query: str, k: int = 5):

    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search_with_score(query, k=k)

    return results
