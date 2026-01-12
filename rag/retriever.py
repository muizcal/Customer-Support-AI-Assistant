from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever

def get_retriever():
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(
        "vectorstore", 
        embeddings,
        allow_dangerous_deserialization=True  # Required for FAISS
    )
    return vectorstore.as_retriever(search_kwargs={"k": 3})