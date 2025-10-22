from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_api_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_submit_report():
    report_data = {
        "type": "Broken streetlight",
        "location": {"lat": 28.6139, "lng": 77.2090},
        "description": "Streetlight is not functioning.",
    }
    response = client.post("/api/reports", json=report_data)
    assert response.status_code == 201
    assert response.json()["message"] == "Report submitted successfully."

def test_get_reports():
    response = client.get("/api/reports")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_safe_route():
    route_params = {
        "start": {"lat": 28.6139, "lng": 77.2090},
        "end": {"lat": 28.7041, "lng": 77.1025},
    }
    response = client.post("/api/safe-route", json=route_params)
    assert response.status_code == 200
    assert "route" in response.json()