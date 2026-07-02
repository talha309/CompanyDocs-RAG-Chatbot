from langgraph.checkpoint.postgres import PostgresSaver
from dotenv import load_dotenv
import os 
import psycopg

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
_conn = psycopg.connect(DATABASE_URL)
_conn.autocommit = True
checkpointer = PostgresSaver(_conn)
checkpointer.setup() 
