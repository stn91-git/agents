from pathlib import Path
from typing import List, Union
from xml.dom.minidom import Document
from agno.agent import Agent
from agno.vectordb.mongodb import MongoDb
from agno.knowledge.json import JSONKnowledgeBase
from agno.document.reader.json_reader import JSONReader
import urllib.parse
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder

# MongoDB Atlas connection string
username = "itskashyap26"
password = "@gitartham1"
encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)
mdb_connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.swuj2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


knowledge_base = JSONKnowledgeBase(
    path="cleaned_emails.json",
    vector_db=MongoDb(
        collection_name="gmail",
        db_url=mdb_connection_string,
        search_index_name="gamil",
        wait_until_index_ready=10,  # 10 seconds wait for index
        wait_after_insert=10,  # 10 seconds wait after insert
        embedder=OpenAIEmbedder(),
    ),
)

knowledge_base(
    recreate=True,
    upsert=True,
)  # Comment out after first run

agent = Agent(knowledge=knowledge_base, show_tool_calls=True, search_knowledge=True)
agent.print_response("Can you tell me about Meenakshi?", markdown=True)
