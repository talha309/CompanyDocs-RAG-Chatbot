# CompanyDocs-RAG-Chatbot

An Agentic AI-powered Company Documentation RAG Chatbot built with **LangGraph**, **LangChain**, **Gemini**, **FastAPI**, **ChromaDB**, and **PostgreSQL Memory**.

The chatbot can answer questions from company documents, search the web for real-time information, perform calculations, retrieve stock prices, and maintain conversation memory.

---

# Features

- 📄 Chat with company documents using Retrieval-Augmented Generation (RAG)
- 🤖 AI-powered conversational assistant using Google Gemini
- 🌐 Real-time web search with Tavily
- 🧠 Persistent conversation memory using PostgreSQL
- 📊 Stock price lookup
- 🧮 Built-in calculator tool
- ⚡ FastAPI backend
- 🔄 Streaming responses
- 🛠️ Tool Calling with LangGraph

---

# Tech Stack

- LangGraph
- LangChain
- Google Gemini
- FastAPI
- ChromaDB
- PostgreSQL
- Tavily Search
- React (Frontend)
- PyPDFLoader
- RecursiveCharacterTextSplitter

---

# Tools

| Tool | Description |
|------|-------------|
| `retrieval_tool` | Searches company documentation |
| `web_search` | Retrieves real-time information from the web |
| `calculator` | Performs mathematical calculations |
| `get_stock_price` | Fetches the latest stock prices |

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/talha309/CompanyDocs-RAG-Chatbot.git

cd CompanyDocs-RAG-Chatbot
```

---

## Install Dependencies

If using **uv**

```bash
uv sync
```

or

```bash
uv add langgraph
```

Install other packages as required.

---

# Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=

GROQ_API_KEY=

TAVILY_API_KEY=

LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=

DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

---

# Running the Project

## Test the Agent

```bash
uv run agent.py
```

## Run FastAPI

```bash
uv run uvicorn main:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

---

# API Usage

### Chat Endpoint

```
GET /chat
```

Parameters

| Parameter | Description |
|-----------|-------------|
| query | User question |
| thread_id | Unique conversation ID |

Example

```
/chat?query=What is the leave policy?&thread_id=12345
```

---

# Project Features

- Company document question answering
- Retrieval-Augmented Generation (RAG)
- Persistent memory
- Real-time web search
- AI chat assistant
- Stock price search
- Mathematical calculations
- Streaming responses

---

# Project Structure

```
CompanyDocs-RAG-Chatbot/
│
├── agent.py
├── main.py
├── tools.py
├── utils.py
├── company_data.pdf
├── .env
├── test.py
├── prompt.py
├── pyproject.toml
└── README.md
```

---
 LangGraph Workflow

![LangGraph Workflow](image.png)

**Description**

This workflow illustrates how the LangGraph agent processes a user's query, selects the appropriate tool, retrieves relevant information, manages memory, and generates the final response.
## FastAPI API Documentation

![FastAPI](Screenshot_21.png)
![FastAPI](Screenshot_3.png)

## LangSmith Observability & Tracing 

![LangSmith](Screenshot_4.png)
# Technologies Used

- Python
- LangGraph
- LangChain
- Google Gemini
- FastAPI
- FAISS
- PostgreSQL
- Tavily Search
- PyPDFLoader
- RecursiveCharacterTextSplitter

---

# Future Improvements

- Authentication
- Multi-user support
- PDF upload API
- Docker deployment
- CI/CD
- React dashboard

---

# License

MIT License

---

# Author

Talha

GitHub:
https://github.com/talha309