from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from dotenv import load_dotenv
from rag import retriever
import math
import requests
import os 

load_dotenv()

web_search = TavilySearch(
    max_results=5, 
    topic="general",
    search_depth="basic"
)

@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA') 
    using Alpha Vantage with API key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=C9PE94QUEW9VWGFM"
    r = requests.get(url)
    return r.json()

@tool
def calculator(expression:str)->str:
    """
    Useful for simple math calculations.
    Input should be a valid math expression.
    Example: 2 + 2, math.sqrt(16), 10 * 5
    """

    try:
        allowed ={
            "math":math,
            "abs":abs,
            "round":round,
            "min":min,
            "max":max,
            "sum":sum,
        }
        result = eval(expression,{"__builtins__":{}}, allowed)
        return str(result)
    except Exception as e:
        return f"Calculate error:{str(e)}"
    
@tool 
def retreival_tool(query:str):

    """
    Search the document knowledge base and return relevant information.
    Use this tool when:
    - The user asks about document content
    - The answer may exist in the stored documents
    - A summary, explanation, fact, or detail is needed from documents
    Do not guess. Use retrieved results as the source of truth.
    """

    result = retriever.invoke(query)
    context = [doc.page_content for doc in result]
    # metadata = [doc.metadata for doc in metadata]
    return {
        "query": query,
        "context": context,
        # "metadata": metadata,
    }

tools = [calculator, get_stock_price, web_search, retreival_tool]