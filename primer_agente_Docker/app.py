from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title= "Mi primer agente")

@tool
def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números enteros."""
    return a * b

tools = [multiplicar]

# LLM Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)