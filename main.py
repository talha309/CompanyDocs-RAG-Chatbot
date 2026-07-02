from fastapi import FastAPI
from langchain_core.messages import HumanMessage
from agent import graph, config

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Welcome to CompanyDocs-RAG-Chatbot"
    }

@app.get("/chat")
def chat_route(query: str):
    try:
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
            "message":str(e)
        }