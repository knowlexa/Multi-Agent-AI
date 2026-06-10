import json
import time
from datetime import datetime

class ExecutionMonitor:

    def __init__(self):

        self.workflow_start = None

        self.execution_data = {
            "workflow": {},
            "steps": []
        }

    def start_workflow(self):

        self.workflow_start = time.time()

        self.execution_data["workflow"] = {
            "start_time": str(datetime.now()),
            "status": "Running"
        }

        self.save()

    def end_workflow(self):

        duration = round(
            time.time() - self.workflow_start,
            2
        )

        self.execution_data["workflow"].update({
            "end_time": str(datetime.now()),
            "duration_seconds": duration,
            "status": "Completed"
        })

        self.save()

    def start_step(self, agent_name):

        self.execution_data["steps"].append({
            "agent": agent_name,
            "start_time": str(datetime.now()),
            "status": "Running"
        })

        self.save()

    def end_step(self, agent_name):

        for step in reversed(
            self.execution_data["steps"]
        ):

            if step["agent"] == agent_name:

                step["end_time"] = str(datetime.now())
                step["status"] = "Completed"

                break

        self.save()

    def fail_step(self, agent_name, error):

        for step in reversed(
            self.execution_data["steps"]
        ):

            if step["agent"] == agent_name:

                step["status"] = "Failed"
                step["error"] = str(error)

                break

        self.save()

    def save(self):

        with open(
            "execution_history.json",
            "w"
        ) as f:

            json.dump(
                self.execution_data,
                f,
                indent=4
            )