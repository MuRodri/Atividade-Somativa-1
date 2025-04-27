from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Teste 1"}


def test_root_endpoint_content_type():
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

def test_invalid_endpoint():
    response = client.get("/invalid")
    assert response.status_code == 404

def test_root_endpoint_method_not_allowed():
    response = client.post("/")
    assert response.status_code == 405

def test_response_time():
    import time
    start_time = time.time()
    response = client.get("/")
    end_time = time.time()
    assert response.status_code == 200
    assert (end_time - start_time) < 0.5 