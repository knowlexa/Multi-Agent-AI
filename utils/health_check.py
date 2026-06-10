import requests
from utils.logger import logger

def check_ollama():

    try:
        response = requests.get(
            "http://localhost:11434/api/tags",
            timeout=5
        )

        if response.status_code == 200:
            logger.info("Ollama server is running")
            return True

        logger.error(
            f"Ollama returned status code: {response.status_code}"
        )
        return False

    except Exception as ex:

        logger.error(
            f"Ollama health check failed: {str(ex)}"
        )

        return False