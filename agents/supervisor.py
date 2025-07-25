def supervisor_agent(state):
    if not state.get("within_budget", True):
        return {
            **state,
            "final_output": "Бюджет превышен. Уточните бюджет или уменьшите список."
        }
    return state


graph.add_node("supervisor", supervisor_agent)

# Пример ветвления
graph.add_conditional_edges(
    "supervisor",
    lambda state: "final" if state.get("within_budget", True) else None,
    {
        "final": "final",
    }
)
