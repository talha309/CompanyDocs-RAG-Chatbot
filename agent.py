from langgraph.graph import StateGraph, START,END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage
from typing_extensions import Annotated, TypedDict
from utils import groq_llm
from database import checkpointer

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState) -> ChatState:
    """Your main chat node where the user interacts with the agent."""
    messages = state['messages']
    response = groq_llm.invoke(messages )
    return {'messages':[response]}

workflow = StateGraph(ChatState)
workflow.add_node("Chat",chat_node)

workflow.add_edge(START, "Chat")
workflow.add_edge("Chat", END)



graph = workflow.compile(checkpointer=checkpointer)


# while True:
#     user_input = input("User: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     result = graph.invoke(
#         {'messages':[HumanMessage(content=user_input)]},
#         config=config)
#     ai_response = result['messages'][-1]
#     print(f"AI: {ai_response.content}")