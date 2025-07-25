def budgeting_agent(state):
    products = state.get("product_list", [])
    budget = state.get("budget", 0.0)
    total = sum(p["price"] for p in products)

    return {
        **state,
        "total": total,
        "within_budget": total <= budget
    }
