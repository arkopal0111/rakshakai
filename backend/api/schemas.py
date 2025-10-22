from pydantic import BaseModel
from typing import List, Optional

class SafeRoute(BaseModel):
    route_id: str
    safe_points: List[str]
    risk_zones: List[str]
    cctv_coverage: List[str]
    lighting_quality: str
    crowd_density: str

class CommunityReport(BaseModel):
    report_id: str
    report_type: str
    description: str
    location: str
    timestamp: str
    user_id: Optional[str] = None

class UserFeedback(BaseModel):
    user_id: str
    feedback: str
    rating: int

class EmergencyContact(BaseModel):
    contact_id: str
    name: str
    phone_number: str
    relationship: str

class AIResponse(BaseModel):
    status: str
    message: str
    data: Optional[dict] = None