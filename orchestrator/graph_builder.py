from langgraph.graph import StateGraph, END

from orchestrator.state import AgentState

from agents.research_agent import research_agent
from agents.coding_agent import coding_agent
from agents.security_agent import security_agent

from utils.logger import logger


logger.info("Initializing LangGraph Workflow")

workflow = StateGraph(AgentState)

logger.info("StateGraph Created")

# Add nodes
logger.info("Adding Research Agent Node")
workflow.add_node("research", research_agent)

logger.info("Adding Coding Agent Node")
workflow.add_node("coding", coding_agent)

logger.info("Adding Security Agent Node")
workflow.add_node("security", security_agent)

logger.info("All Nodes Added Successfully")

# Entry point
logger.info("Setting Entry Point -> research")
workflow.set_entry_point("research")

# Edges
logger.info("Creating Edge: research -> coding")
workflow.add_edge("research", "coding")

logger.info("Creating Edge: coding -> security")
workflow.add_edge("coding", "security")

logger.info("Creating Edge: security -> END")
workflow.add_edge("security", END)

logger.info("Compiling LangGraph Workflow")

graph = workflow.compile()

logger.info("LangGraph Workflow Compiled Successfully")