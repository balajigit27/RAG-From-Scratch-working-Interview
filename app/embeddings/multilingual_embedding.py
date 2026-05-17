from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding():

    return HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large"
    )