# === Stage 64: Add validation for relationship references ===
# Project: ClinicFlow
import re


def _clean_name(name: str) -> str:
    return re.sub(r'[^A-Za-z0-9 \-_]', '', name).strip()


def validate_visit(visit: dict) -> None:
    if not visit.get('patient_id'):
        raise ValueError("Visit must have a patient_id")
    if not isinstance(visit['priority'], int):
        raise TypeError("Priority must be an integer")
    if visit['priority'] not in (1, 2, 3, 4, 5):
        raise ValueError(f"Priority must be between 1 and 5; got {visit['priority']}")
    if not isinstance(visit.get('notes', ''), str):
        raise TypeError("Notes field must be a string")


def validate_patient(patient: dict) -> None:
    if not patient.get('name') or _clean_name(patient['name']).strip() == '':
        raise ValueError("Patient name cannot be empty after cleaning")
    if not isinstance(patient.get('phone', ''), str):
        raise TypeError("Phone must be a string")
    try:
        int(re.sub(r'[^0-9]', '', patient['phone']))
    except (ValueError, TypeError):
        raise ValueError(f"Invalid phone number format: {patient['phone']}")


def validate_staff(staff: dict) -> None:
    if not staff.get('name') or _clean_name(staff['name']).strip() == '':
        raise ValueError("Staff name cannot be empty after cleaning")
    if not isinstance(staff.get('role', ''), str):
        raise TypeError("Role must be a string")


def validate_waiting_room(room: dict) -> None:
    if not room.get('room_name') or _clean_name(room['room_name']).strip() == '':
        raise ValueError("Room name cannot be empty after cleaning")
    if not isinstance(room.get('capacity', 0), int):
        raise TypeError("Capacity must be an integer")


def validate_handoff(handoff: dict) -> None:
    if not handoff.get('from_staff_id') or not handoff.get('to_staff_id'):
        raise ValueError("Handoff requires both from and to staff IDs")
    if not isinstance(handoff.get('timestamp', ''), str):
        raise TypeError("Timestamp must be a string (ISO format recommended)")


def validate_summary(summary: dict) -> None:
    for key in ('date', 'total_visits', 'avg_wait_min', 'staff_notes'):
        if key not in summary:
            raise ValueError(f"Missing required field in daily summary: {key}")
