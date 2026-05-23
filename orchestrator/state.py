from typing import TypedDict

class AgentState(TypedDict):
    user_query: str
    research_output: str
    code_output: str
    security_output: str
    final_output: str