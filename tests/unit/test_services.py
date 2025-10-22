from src.services.maps_service import get_safe_routes, get_risk_zones
from src.services.firebase_service import submit_report
from src.services.ai_guardian import check_in
from src.services.risk_scoring import calculate_risk_score
from src.services.notifications import send_notification

def test_get_safe_routes():
    # Test case for safe route retrieval
    routes = get_safe_routes(start_location="Location A", end_location="Location B")
    assert isinstance(routes, list)
    assert len(routes) > 0

def test_get_risk_zones():
    # Test case for risk zone retrieval
    risk_zones = get_risk_zones(location="Location A")
    assert isinstance(risk_zones, list)

def test_submit_report():
    # Test case for submitting a community report
    response = submit_report(report_data={"type": "Unsafe crowd", "location": "Location A"})
    assert response["status"] == "success"

def test_check_in():
    # Test case for AI check-in functionality
    response = check_in(user_id="user123")
    assert response["status"] == "checked_in"

def test_calculate_risk_score():
    # Test case for risk score calculation
    score = calculate_risk_score(data={"crowd_density": "high", "lighting": "poor"})
    assert isinstance(score, float)

def test_send_notification():
    # Test case for sending notifications
    response = send_notification(user_id="user123", message="Test notification")
    assert response["status"] == "sent"