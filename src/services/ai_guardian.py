from datetime import datetime
import json

class AIGuardian:
    def __init__(self, user_id):
        self.user_id = user_id
        self.check_in_time = None
        self.emergency_contacts = []
        self.active = False

    def start_check_in(self):
        self.check_in_time = datetime.now()
        self.active = True
        # Logic to notify user and emergency contacts
        self.notify_contacts("Check-in started.")

    def stop_check_in(self):
        self.active = False
        self.check_in_time = None
        # Logic to notify user and emergency contacts
        self.notify_contacts("Check-in stopped.")

    def notify_contacts(self, message):
        for contact in self.emergency_contacts:
            # Logic to send notification to contact
            print(f"Notifying {contact}: {message}")

    def add_emergency_contact(self, contact):
        self.emergency_contacts.append(contact)

    def remove_emergency_contact(self, contact):
        self.emergency_contacts.remove(contact)

    def trigger_sos(self):
        if self.active:
            # Logic to send SOS alert
            self.notify_contacts("SOS alert triggered!")
            print("SOS alert sent to emergency contacts.")
        else:
            print("No active check-in. SOS alert cannot be sent.")

    def get_check_in_status(self):
        return {
            "user_id": self.user_id,
            "active": self.active,
            "check_in_time": self.check_in_time.isoformat() if self.check_in_time else None,
            "emergency_contacts": self.emergency_contacts
        }