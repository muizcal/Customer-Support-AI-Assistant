from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

def ingest_docs():
    loader = TextLoader("data/documents/company_policy.txt")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    os.makedirs("vectorstore", exist_ok=True)
    vectorstore.save_local("vectorstore")

    print("✅ Documents ingested and stored")

if __name__ == "__main__":
    ingest_docs()
