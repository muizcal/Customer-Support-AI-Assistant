# Customer Support AI Assistant (RAG-Based)

![Alt text](./screenshot.png)


Overview

The Customer Support AI Assistant is a Retrieval-Augmented Generation (RAG) application built using FastAPI, Streamlit, and LangChain/OpenAI. It allows companies to create an AI-powered assistant that can answer questions based on internal documents.

By leveraging document embeddings, vector stores, and large language models, this system ensures that your AI responds accurately, contextually, and efficiently using your company knowledge base.

## Features

- Ask Questions in Natural Language: Users can type a question and receive instant answers from company documents.

- Document-Based Knowledge: The AI reads your internal documents (TXT, PDF, or other supported formats) to generate accurate answers.

- Fully Customizable Knowledge Base: Replace, add, or edit files in the rag/docs/ folder to update the AI’s knowledge. The assistant automatically indexes the new content.

- Vector Search with FAISS: Quickly finds the most relevant information from thousands of documents.

- FastAPI Backend: Provides a robust API for AI question-answering.

- Streamlit Frontend: Modern, interactive interface for internal teams or clients.

- Easy Deployment: Can run locally, in Docker, or on a cloud server.

## Problem It Solves

Companies often face the challenge of knowledge fragmentation: employees waste time searching through manuals, PDFs, or policy documents to answer questions.

This assistant helps:

- Reduce response time for internal or customer support queries.

- Improve knowledge accessibility across the company.

- Minimize training time for new employees.

- Enable data-driven support decisions.

## Folder Structure
Customer Support AI Assistant/
├─ app/                  <- FastAPI backend
│   └─ main.py           <- Backend API endpoints
├─ rag/                  <- Retrieval-Augmented Generation code
│   ├─ llm.py            <- Loads documents, embeddings, and defines QA chain
│   └─ docs/             <- Knowledge base documents
│       ├─ doc1.txt
│       └─ doc2.txt
│   # Replace/add your own documents here to customize the AI
├─ frontend/             <- Streamlit frontend
│   └─ app.py
├─ venv/                 <- Python virtual environment
└─ .env                  <- Environment variables (API keys)

Customizing the AI: You can replace existing files or add new documents in rag/docs/. The assistant will automatically read and index them the next time it runs.

## Installation

1. Clone the repository:
<PRE> git clone https://github.com/muizcal/Customer-Support-AI-Assistant.git
cd Customer-Support-AI-Assistant
</PRE>
2. Create a virtual environment and activate it:
<PRE>python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
</PRE>
3. Install dependencies:
<PRE>pip install -r requirements.txt
</PRE>
4. Add your OpenAI API key in .env:
<PRE>OPENAI_API_KEY="your_openai_api_key_here"
</PRE>

## Running the Application
1. Start the Backend (FastAPI)
<PRE>uvicorn app.main:app --reload
</PRE>
uvicorn app.main:app --reload

2. Start the Frontend (Streamlit)
<PRE>cd frontend
streamlit run app.py
</PRE>

## Usage

- Open the Streamlit app.

- Enter your question in natural language.

- Click Ask AI.

- View the AI-generated answer pulled from your company documents.

- Note: Ensure the FastAPI backend is running before using the frontend.

Tip: Add or modify files in rag/docs/ to expand or update the AI’s knowledge base.


## Technology Stack
Component	Technology
Backend API	FastAPI
Frontend	Streamlit
AI / LLM	OpenAI GPT-3.5 / GPT-4
Document Loader	LangChain TextLoader
Vector Store	FAISS (for semantic search)
Environment Management	Python venv, dotenv