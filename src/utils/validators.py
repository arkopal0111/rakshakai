def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())

def is_valid_phone_number(phone):
    return phone.isdigit() and len(phone) in [10, 12]  # Assuming 10 or 12 digit phone numbers

def validate_contact_form(name, email, subject, message):
    if not is_non_empty_string(name):
        return "Name cannot be empty."
    if not is_valid_email(email):
        return "Invalid email address."
    if not is_non_empty_string(subject):
        return "Subject cannot be empty."
    if not is_non_empty_string(message):
        return "Message cannot be empty."
    return None  # No validation errors

def validate_report_submission(report_type, description):
    if report_type not in ["Broken streetlight", "Unsafe crowd", "Harassment report", "Empty area"]:
        return "Invalid report type."
    if not is_non_empty_string(description):
        return "Description cannot be empty."
    return None  # No validation errors