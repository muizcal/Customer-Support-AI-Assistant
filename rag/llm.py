import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env")


docs_folder = "rag/docs/"
loaders = [TextLoader(os.path.join(docs_folder, file)) for file in os.listdir(docs_folder)]
documents = []
for loader in loaders:
    documents.extend(loader.load())


text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)


embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

vectorstore = FAISS.from_documents(chunks, embeddings)


llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)


retriever = vectorstore.as_retriever(search_kwargs={"k": 3})


prompt = ChatPromptTemplate.from_template("""
You are a helpful customer support assistant. Answer the question based on the provided context.
If you don't know the answer, just say that you don't know.

Context: {context}

Question: {question}

Answer:
""")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


qa_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

def get_qa_chain():
    return qa_chain


def query(question: str):
    return qa_chain.invoke(question)