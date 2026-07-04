from langgraph.graph import StateGraph, START,END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import BaseMessage, SystemMessage,HumanMessage
from typing_extensions import Annotated, TypedDict
from utils import groq_llm, groq_llm_with_tools,gemini_llm1_with_tools
from database import checkpointer
from prompts import SYSTEM_PROMPT
from tools import tools


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = [SystemMessage(content=SYSTEM_PROMPT)]+state['messages']
    response = groq_llm_with_tools.invoke(messages )
    return {'messages':[response]}

tool_node = ToolNode(tools)

workflow = StateGraph(ChatState)

workflow.add_node("Chat",chat_node)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "Chat")
workflow.add_conditional_edges("Chat", tools_condition)
workflow.add_edge("tools", "Chat" )



graph = workflow.compile(checkpointer=checkpointer)
# config = {'configurable':{'thread_id':'6'}}

# while True:
#     user_input = input("User: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     result = graph.invoke(
#         {'messages':[HumanMessage(content=user_input)]},
#         config=config)
#     ai_response = result['messages'][-1]
#     print(f"AI: {ai_response.content}")


