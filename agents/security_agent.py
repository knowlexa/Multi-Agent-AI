from utils.logger import logger
from utils.monitor_instance import monitor

from services.llm_factory import llm

def security_agent(state):
    logger.info(
    f"Security Agent Input State: {state}"
)
    
    monitor.start_step(
    "Security Agent"
)

    code = state["code_output"]

    response = llm.invoke(
        f"Review this code for vulnerabilities: {code}"
    )

    monitor.end_step(
    "Security Agent"
)

    return {
        "security_output": response.content 
    }