from services.llm_factory import llm

def research_agent(state):

    query = state["user_query"]

    response = llm.invoke(
        f"Research this topic deeply: {query}"
    )

    return {
        "research_output": response.content
    }