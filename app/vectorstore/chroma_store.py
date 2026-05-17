from langchain_community.vectorstores import Chroma

def create_vectorstore(chunks, embeddings):

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="./vector_db/chroma_db"
    )

    return db