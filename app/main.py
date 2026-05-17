from ingestion.document_loader import load_documents

from chunking.recursive_chunking import recursive_chunk

from embeddings.multilingual_embedding import get_embedding

from vectorstore.chroma_store import create_vectorstore

from retriever.basic_retriever import get_retriever

from llm.openai_llm import load_llm

from chains.rag_chain import build_chain


documents = load_documents()

chunks = recursive_chunk(documents)

embeddings = get_embedding()

vectorstore = create_vectorstore(
    chunks,
    embeddings
)

retriever = get_retriever(vectorstore)

llm = load_llm()

qa_chain = build_chain(
    llm,
    retriever
)

query = "Explain transformer architecture"

response = qa_chain.invoke({"input": query})

print(response)