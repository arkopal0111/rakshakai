from firebase_admin import credentials, initialize_app, firestore

# Initialize Firebase app
cred = credentials.Certificate("path/to/your/firebase/credentials.json")
initialize_app(cred)

# Firestore client
db = firestore.client()

def add_report(report_data):
    """Add a community safety report to Firestore."""
    db.collection('reports').add(report_data)

def get_reports():
    """Retrieve all community safety reports from Firestore."""
    reports_ref = db.collection('reports')
    reports = reports_ref.stream()
    return [report.to_dict() for report in reports]

def get_report_count():
    """Get the total number of reports."""
    reports_ref = db.collection('reports')
    return reports_ref.get().size