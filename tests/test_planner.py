import pytest
from agents.planner import planner_agent

def test_planner_agent_mock(monkeypatch):
    class DummyConversation:
        def predict(self, input):
            return f"[MOCK] Ответ на: {input}"
    
    from agents import planner
    planner.conversation = DummyConversation()

    input_state = {"input": "Хочу пасту", "budget": 20}


    result = planner_agent(input_state)


    assert result["task"] == "Find recipe"
    assert result["status"] == "ok"
    assert "Ответ на: Хочу пасту" in result["description"]


def test_planner_agent_real():
    from agents.planner import planner_agent

    input_state = {"input": "Хочу острое блюдо с курицей", "budget": 30}
    result = planner_agent(input_state)

    assert "куриц" in result["description"].lower()
    assert result["status"] == "ok"

