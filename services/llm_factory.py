from config.settings import LLM_PROVIDER

if LLM_PROVIDER == "azure":

     from services.azure_openai import llm

elif LLM_PROVIDER == "ollama":

    from services.ollama_service import llm

else:

    raise Exception("Unsupported LLM Provider")