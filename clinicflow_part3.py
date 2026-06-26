# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ClinicFlow
def validate_visit_id(vid): return isinstance(vid, str) and vid.strip() and len(vid) <= 12
def validate_patient_name(name): return name and len(name) >= 3 and len(name) <= 60
def validate_priority(priority): return priority in ('low', 'medium', 'high')
def validate_duration(duration): return isinstance(duration, (int, float)) and duration > 0 and duration <= 480
def validate_phone(phone): return phone and len(phone.replace('-', '').replace(' ', '')) == 10
def sanitize_text(text): return text.strip() if text else ""
