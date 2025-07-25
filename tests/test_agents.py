from agents.budgeting import budgeting_agent

def test_budgeting_agent():
    products = [
        {"product": "A", "price": 5.0},
        {"product": "B", "price": 10.0}
    ]
    budget = 20
    result = budgeting_agent(products, budget)
    assert result["within_budget"] == True
    assert result["total"] == 15.0

