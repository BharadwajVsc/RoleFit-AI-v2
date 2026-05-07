"""from app.vectorstores.chroma_store import get_vectorstore


def retrieve_documents(query: str, k: int = 5):

    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(search_kwargs={"k": k})

    results = retriever.invoke(query)

    return results"""

from app.vectorstores.chroma_store import get_vectorstore


def retrieve_documents(query: str, k: int = 5):
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)
