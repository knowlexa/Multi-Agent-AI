from services.llm_factory import llm

def security_agent(state):

    code = state["code_output"]

    response = llm.invoke(
        f"Review this code for vulnerabilities: {code}"
    )

    return {
        "security_output": response.content 
    }