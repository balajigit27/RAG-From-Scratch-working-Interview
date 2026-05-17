from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

def build_chain(llm, retriever):
    
    prompt = PromptTemplate.from_template("""Answer the following question based on the provided context:

Context:
{context}

Question: {input}

Answer:""")
    
    chain = (
        {
            "context": RunnableLambda(lambda x: x["input"]) | retriever,
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain