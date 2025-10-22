from datetime import datetime
import json
import os

class ReportIngestor:
    def __init__(self, report_file='reports.json'):
        self.report_file = report_file
        self.load_reports()

    def load_reports(self):
        if os.path.exists(self.report_file):
            with open(self.report_file, 'r') as file:
                self.reports = json.load(file)
        else:
            self.reports = []

    def save_reports(self):
        with open(self.report_file, 'w') as file:
            json.dump(self.reports, file, indent=4)

    def ingest_report(self, report_data):
        report_data['timestamp'] = datetime.now().isoformat()
        self.reports.append(report_data)
        self.save_reports()
        return report_data

if __name__ == "__main__":
    ingestor = ReportIngestor()
    sample_report = {
        "type": "Unsafe crowd",
        "location": "Sector 15, Noida",
        "description": "Large group of people loitering around.",
        "user_id": "user123"
    }
    ingestor.ingest_report(sample_report)