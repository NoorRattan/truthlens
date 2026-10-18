"""Exercise the same application import and lifespan used by Render."""
from fastapi.testclient import TestClient

from main import app


def test_application_starts_and_exposes_health():
    with TestClient(app) as client:
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
        assert client.get("/").json()["message"] == "TruthLens API is running"
