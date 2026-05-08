from app.loaders.pdf_loader import load_pdf
from app.chunking.text_chunker import chunking_docs
from app.vectorstores.chroma_store import get_vectorstore


def ingest_resume(pdf_path: str):
    # Load PDF and chunk it
    documents = load_pdf(pdf_path)
    chunked_docs = chunking_docs(documents)

    for index, chunk in enumerate(chunked_docs):
        chunk.metadata["chunk_id"] = f"chunk{index}"
        chunk.metadata["chunk_index"] = index

    # Insert into vectorstore
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunked_docs)
    print(f"Inserted {len(chunked_docs)} chunks into the vectorstore")

    return chunked_docs
