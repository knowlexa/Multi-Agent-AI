from services.llm_factory import llm

def coding_agent(state):

    research = state["research_output"]

    response = llm.invoke(
        f"Generate Python enterprise code using this: {research}"
    )

    return {
        "code_output": response.content
    }