from graph import build_graph

def test_full_strategy_success():
    graph = build_graph()
    input_state = {
        "input": "Паста с соусом",
        "budget": 25.0
    }

    result = graph.invoke(input_state)
    
    assert "shopping_list" in result
    assert result["total_cost"] <= 25.0


def test_full_strategy_budget_fail():
    graph = build_graph()
    input_state = {
        "input": "Очень дорогой стейк с трюфелем",
        "budget": 1.0  # заведомо маленький
    }

    result = graph.invoke(input_state)
    
    assert "shopping_list" not in result  # тк ушли в "end"
    assert result.get("status") == "fail"
