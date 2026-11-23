from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add_returns_sum():
    response = client.get("/add", params={"a": 7, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 10}
