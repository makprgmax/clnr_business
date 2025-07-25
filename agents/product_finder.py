def product_finder_agent(state):
    """
    Convert ingredients to mock products with prices.
    Selects a recipe for the goal.
    """
    ingredients = state.get("ingredients", [])
    product_map = {
        "spaghetti": ("Spaghetti Pasta 500g", 2.5),
        "ground beef": ("Ground Beef 400g", 6.0),
        "tomato sauce": ("Tomato Sauce Can", 1.8),
        "onion": ("Onion 1kg", 1.2),
        "garlic": ("Garlic Bulb", 0.9),
    }
    products = [
        {"ingredient": ing, "product": product_map[ing][0], "price": product_map[ing][1]}
        for ing in ingredients if ing in product_map
    ]
    return {
        **state,
        "product_list": products
    }


def recipe_agent(goal_info):
    """
    Подбирает рецепт под цель. Может быть расширено до API.
    """
    recipes_db = {
        "dinner": {
            "name": "Spaghetti Bolognese",
            "ingredients": ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"]
        },
        "meal": {
            "name": "Grilled Cheese Sandwich",
            "ingredients": ["bread", "cheddar cheese", "butter"]
        }
    }

    goal = goal_info.get("goal", "meal")
    recipe = recipes_db.get(goal, recipes_db["meal"])
    
    return {
        "recipe_name": recipe["name"],
        "ingredients": recipe["ingredients"],
        "servings": goal_info.get("servings", 1)
    }

