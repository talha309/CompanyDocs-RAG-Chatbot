from langchain_tavily import TavilySearch
from langchain_core.tools import tool

web_search_tool = TavilySearch(
    max_results=5, 
    topic="general"
)