from agents.supervisor import supervisor_agent

def test_supervisor_routing():
    from graph import route_from_supervisor

    state_ok = {"within_budget": True, "status": "ok"}
    assert route_from_supervisor(state_ok) == "final"

    state_fail = {"within_budget": False, "status": "fail"}
    assert route_from_supervisor(state_fail) == "end"

def test_supervisor_agent_final():
    state = {"within_budget": True, "total": 19.5}
    result = supervisor_agent(state)
    assert result["status"] == "ok"

def test_supervisor_agent_fail():
    state = {"within_budget": False, "total": 35.0}
    result = supervisor_agent(state)
    assert result["status"] == "fail"




