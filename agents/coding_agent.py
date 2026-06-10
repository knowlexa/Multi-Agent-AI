from services.llm_factory import llm
from utils.logger import logger
from utils.monitor_instance import monitor


def coding_agent(state):
    logger.info(
    f"Coding Agent Input State: {state}"
)

    monitor.start_step(
    "Coding Agent"
)
    research = state["research_output"]

    response = llm.invoke(
        f"Generate Python enterprise code using this: {research}"
    )

    monitor.end_step(
    "Coding Agent"
      )

    return {
        "code_output": response.content
    }

    