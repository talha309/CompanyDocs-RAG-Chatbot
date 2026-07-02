from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from agent import graph
import uuid

# config = {"configurable": {"thread_id": str(uuid.uuid4())[:255]}}

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Welcome to CompanyDocs-RAG-Chatbot"
    }

@app.get("/chat")
def chat_route(query: str, thread_id: str):
    try:
        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }
        result = graph.invoke(
        {'messages':[HumanMessage(content=query)]},
        config=config)
        ai_response = result['messages'][-1]
        response = ai_response.content
        return{
            "AIMessage":response
        }
    except Exception as e:
        return {
            "error":str(e)
        }