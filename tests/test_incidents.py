from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_incident():
    payload = {
        "title": "Database connection failure",
        "description": "The production database is refusing new connections.",
        "severity": "critical",
    }

    response = client.post("/incidents/", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["severity"] == "critical"
    assert data["status"] == "open"
    assert "id" in data


def test_reject_invalid_severity():
    payload = {
        "title": "Invalid incident",
        "description": "This request uses an unsupported severity value.",
        "severity": "urgent",
    }

    response = client.post("/incidents/", json=payload)

    assert response.status_code == 422


def test_list_incidents():
    response = client.get("/incidents/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)