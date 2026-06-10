
from utils.logger import logger
from utils.tracing import track_execution
from services.llm_factory import llm
from utils.monitor_instance import monitor


@track_execution
def research_agent(state):
    logger.info(
    f"Research Agent Input State: {state}"
    
)
    
    monitor.start_step(
        "Research Agent"
    )

    logger.info("Research Agent Started")

    try:

        query = state["user_query"]

        response = llm.invoke(
            f"Research this topic deeply: {query}"
        )

        monitor.end_step(
            "Research Agent"
        )


        logger.info("Research Agent Completed")

        logger.info(f"Research Agent Response: {response.content}"
        )

        return {
            "research_output": response.content
        }
     

    except Exception as ex:

        monitor.fail_step(
            "Research Agent",
            ex
        )

        raise



