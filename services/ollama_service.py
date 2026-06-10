from langchain_ollama import ChatOllama
from config.settings import OLLAMA_MODEL
from utils.logger import logger

try:

    logger.info("Initializing Ollama LLM")

    llm = ChatOllama(
        model=OLLAMA_MODEL,
        temperature=0
    )

    logger.info("Testing Ollama connection")

    response = llm.invoke(
        "Reply with exactly: OK"
    )

    logger.info(
        f"Ollama connectivity test passed: {response.content}"
    )

except Exception as ex:

    logger.exception(
        f"Ollama initialization failed: {str(ex)}"
    )

    raise