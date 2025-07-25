from langgraph.graph import StateGraph, END


from agents.planner import planner_agent
from agents.recipe_finder import recipe_agent
from agents.product_finder import product_finder_agent
from agents.budgeting import budgeting_agent
from agents.finalizer import finalizer_agent

def supervisor_agent(state):
    if not state.get("within_budget", True):
        return {
            **state,
            "status": "over_budget",
            "message": "Бюджет превышен. Список не может быть финализирован."
        }
    else:
        return {
            **state,
            "status": "ok"
        }


def end_agent(state):
    return state


def build_graph():

    graph = StateGraph(state_schema=dict)


    graph.add_node("planner", planner_agent)
    graph.add_node("recipe", recipe_agent)
    graph.add_node("finder", product_finder_agent)
    graph.add_node("budget", budgeting_agent)
    graph.add_node("supervisor", supervisor_agent)
    graph.add_node("final", finalizer_agent)
    graph.add_node("end", end_agent)


    graph.set_entry_point("planner")


    graph.add_edge("planner", "recipe")
    graph.add_edge("recipe", "finder")
    graph.add_edge("finder", "budget")
    graph.add_edge("budget", "supervisor")


    graph.add_conditional_edges(
        "supervisor",
        lambda state: "final" if state.get("status") == "ok" and state.get("within_budget") else "end",
        {
            "final": "final",
            "end": "end"
        }
    )

    return graph.compile()
