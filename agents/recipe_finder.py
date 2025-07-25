def recipe_agent(state):
    """
    Dummy recipe finder.
    """

    goal = state.get("task", "")
    
    return {
        **state,
        "recipe_name": "Spaghetti Bolognese",
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"]
    }
