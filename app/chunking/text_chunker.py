from langchain_text_splitters import RecursiveCharacterTextSplitter

# Why metadata-aware chunking?
#
# Adding section metadata improves retrieval quality by helping
# the system understand whether a chunk belongs to skills,
# experience, projects, education, etc.
#
# This enables smarter ATS matching and future section-aware retrieval.


def detect_section(text):
    text = text.lower()

    if "skills" in text:
        return "skills"
    elif "experience" in text:
        return "experience"
    elif "projects" in text:
        return "projects"
    elif "education" in text:
        return "education"

    return "general"


def chunking_docs(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    for index, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = f"chunk{index}"
        chunk.metadata["chunk_index"] = index
        chunk.metadata["section"] = detect_section(chunk.page_content)
    return chunks
