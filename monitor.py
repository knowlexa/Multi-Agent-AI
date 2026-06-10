import json
import time
import os

while True:

    os.system("cls")

    with open(
        "execution_history.json",
        "r"
    ) as f:

        data = json.load(f)

    print("\n=== Workflow Status ===")

    print(
        data["workflow"]
    )

    print("\n=== Steps ===")

    for step in data["steps"]:

        print(step)

    time.sleep(2)