def finalizer_agent(state):
    products = state.get("product_list", [])
    total = state.get("total", 0.0)

    return {
        **state,
        "shopping_list": products,
        "total_cost": total
    }
