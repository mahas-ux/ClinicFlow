# === Stage 4: Implement create operations for the primary records ===
# Project: ClinicFlow
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Visit:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    patient_name: str
    priority: int  # 1=high, 2=medium, 3=low
    scheduled_time: datetime
    status: str = "scheduled"

@dataclass
class StaffMember:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    role: str
    current_room: int | None = None

def create_visit(clinic_db, patient_name, priority, scheduled_time):
    visit = Visit(patient_name=patient_name, priority=priority, scheduled_time=scheduled_time)
    clinic_db["visits"].append(visit)
    return visit

def create_staff(clinic_db, name, role):
    staff = StaffMember(name=name, role=role)
    clinic_db["staff"].append(staff)
    return staff
