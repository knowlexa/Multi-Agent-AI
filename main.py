from orchestrator.graph_builder import graph

query = input("Enter your request: ")

result = graph.invoke({
    "user_query": query
})

print("\n========== FINAL OUTPUT ==========\n")

print(result)