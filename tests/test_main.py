from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)





def test_hello_world() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_health_check() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_tasks_check() -> None:

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) == 2

    assert data[0]["id"] == 1

    assert data[0]["title"] == "Learn FastAPI"

    assert data[0]["completed"] is False