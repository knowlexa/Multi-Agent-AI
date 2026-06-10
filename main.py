from orchestrator import state
from orchestrator.graph_builder import graph
from utils.health_check import check_ollama
from utils.logger import logger
from utils.monitor_instance import monitor



if not check_ollama():
    raise Exception(
        "Ollama is not running. Start it using 'ollama serve'"
    )

query = input("Enter your request: ")
logger.info("Workflow Started")
monitor.start_workflow()

try:

    result = graph.invoke(
        {
            "user_query": query
        }
    )

    monitor.end_workflow()

except Exception as ex:

    monitor.end_workflow()
    print(ex)

for event in graph.stream(state):
    logger.info(f"Graph Event: {event}")

logger.info("Workflow Completed")
    
print("\n========== FINAL OUTPUT ==========\n")

print(result)