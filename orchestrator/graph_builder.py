from langgraph.graph import StateGraph, END

from orchestrator.state import AgentState

from agents.research_agent import research_agent
from agents.coding_agent import coding_agent
from agents.security_agent import security_agent

workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("research", research_agent)
workflow.add_node("coding", coding_agent)
workflow.add_node("security", security_agent)

# Define workflow
workflow.set_entry_point("research")

workflow.add_edge("research", "coding")
workflow.add_edge("coding", "security")
workflow.add_edge("security", END)

# Compile graph
graph = workflow.compile()