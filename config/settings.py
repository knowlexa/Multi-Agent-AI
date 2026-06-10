from dotenv import load_dotenv
import os

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
OLLAMA_MODEL = "llama3" #os.getenv("OLLAMA_MODEL", "llama3")