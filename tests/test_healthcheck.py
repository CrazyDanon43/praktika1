from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/health/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": True}