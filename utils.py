from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 

load_dotenv()
# using for the main conversation with the user and to generate the final answer
gemini_llm1=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.environ.get("GOOGLE_API_KEY"),
    temperature=0.2,
    streaming=True
)
# used for summarization the old messages for short term memory
groq_llm = ChatGroq(
    model= "llama-3.3-70b-versatile",
)
# using for with structure output for to desgin the user query 
gemini_llm2=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=os.environ.get("GEMINI_API_KEY"),
    temperature=0.2,
    streaming=True
)
# using for embedding the user query and the documents to find the relevant documents
embeddings = GoogleGenerativeAIEmbeddings(
    model ="models/gemini-embedding-001",
    api_key=os.environ.get("GEMINI_API_KEY")
)