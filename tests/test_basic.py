from app.agent import run_agent

def test_basic():
    response = run_agent("What is this system?")
    assert response is not None
