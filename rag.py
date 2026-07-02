from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader, 
    TextLoader, 
    UnstructuredWordDocumentLoader,
    WebBaseLoader,
)
from langchain_core.vectorstores import Chroma
from utils import embeddings
from pathlib import Path
from uuid import uuid4
import os
import shutil


loader = PyPDFLoader("data/your_document.pdf")  # Load your PDF document
docs = loader.load()
print (len(docs), "documents loaded")  # Print the number of documents loaded


# Split the document into smaller chunks for better processing
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(docs)
length_of_chunks = len(chunks)
print(f"Document split into {length_of_chunks} chunks")  # Print the number of chunks created


# Create a Chroma vector store from the split documents and embeddings
vector_store = Chroma.from_documents(documents= chunks,embeddings=embeddings, collection_name="company_docs", persist_directory="chroma_db")

retriever = vector_store.as_retriever(
    search_type = "similarity",
    search_kwargs = {"k": 4}
)