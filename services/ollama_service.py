from langchain_ollama import ChatOllama
from config.settings import OLLAMA_MODEL

llm = ChatOllama(
    model=OLLAMA_MODEL,
    temperature=0
)