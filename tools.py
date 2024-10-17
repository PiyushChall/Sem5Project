import os

from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI

# LLM Initialization
google_api_key = os.environ['GOOGLE_API_KEY']
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=google_api_key,
)

# Search Tool Initialization
serper_api_key = os.environ['SERPER_API_KEY']
search_tool = SerperDevTool()

# Web Search Tool Initialization
web_search_tool = WebsiteSearchTool(
    config = dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-flash",
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    )
)