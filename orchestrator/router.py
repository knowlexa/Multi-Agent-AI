def router(state):

    query = state["user_query"].lower()

    if "security" in query:
        return "security"

    if "code" in query:
        return "coding"

    return "research"