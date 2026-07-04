from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pathlib import Path
from uuid import uuid4
import os
import shutil
from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader("company_data.pdf")  # Load your PDF document
docs = loader.load()
print (len(docs), "documents loaded")  # Print the number of documents loaded


# Split the document into smaller chunks for better processing
text_splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=150)
chunks = text_splitter.split_documents(docs)
length_of_chunks = len(chunks)
print(f"Document split into {length_of_chunks} chunks")  # Print the number of chunks created

embeddings = GoogleGenerativeAIEmbeddings(
    model ="models/gemini-embedding-001",
    api_key=os.environ.get("GEMINI_API_KEY")
)
# Path("chroma_db").mkdir(exist_ok=True)
# Create a Chroma vector store from the split documents and embeddings
vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4},
)
