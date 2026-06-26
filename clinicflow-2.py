# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ClinicFlow
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

class Priority(Enum):
    EMERGENCY = 1
    URGENT = 2
    ROUTINE = 3

@dataclass
class Patient:
    id: str
    name: str
    phone: str
    birth_date: datetime
    priority: Priority = Priority.ROUTINE
    notes: str = ""

@dataclass
class Visit:
    patient_id: str
    doctor_id: Optional[str]
    scheduled_time: datetime
    actual_start: Optional[datetime] = None
    duration_minutes: int = 30
    status: str = "scheduled"  # scheduled, in_progress, completed, cancelled

@dataclass
class StaffMember:
    id: str
    name: str
    role: str
    department: str
    current_load: int = 0

@dataclass
class DailySummary:
    date: datetime
    total_visits: int = 0
    completed_visits: int = 0
    cancelled_visits: int = 0
    staff_hours_worked: dict[str, float] = field(default_factory=dict)
