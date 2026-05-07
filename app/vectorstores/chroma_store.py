import os
from langchain_chroma import Chroma
from app.utils.embeddings import get_embedding_function
from app.config import CHROMA_DB_PATH, COLLECTION_NAME


def get_vectorstore():
    # os.makedirs(CHROMA_DB_PATH, exist_ok=True)
    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DB_PATH,
        embedding_function=get_embedding_function(),
    )
