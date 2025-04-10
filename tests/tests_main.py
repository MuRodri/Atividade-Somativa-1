from fastapi.testclient import TestClient
from . import main  # Import your FastAPI app

client = TestClient(main)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"greeting": "Teste 1"}