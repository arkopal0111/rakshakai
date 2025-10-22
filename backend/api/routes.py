from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class SafetyReport(BaseModel):
    report_type: str
    description: str
    location: str

class CommunityReportResponse(BaseModel):
    message: str
    report_id: int

@router.post("/reports", response_model=CommunityReportResponse)
async def submit_report(report: SafetyReport):
    # Logic to save the report to the database
    report_id = 1  # Placeholder for the generated report ID
    return CommunityReportResponse(message="Report submitted successfully", report_id=report_id)

@router.get("/reports", response_model=List[SafetyReport])
async def get_reports():
    # Logic to retrieve reports from the database
    return []  # Placeholder for the list of reports

@router.get("/health")
async def health_check():
    return {"status": "healthy"}