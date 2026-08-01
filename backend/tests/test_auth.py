from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_register_user() -> None:
    response = client.post(
        "/api/v1/auth/register",
        json={"username": "demo", "email": "demo@example.com", "password": "secret123"},
    )
    assert response.status_code == 201
