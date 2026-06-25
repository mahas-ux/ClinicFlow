# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ClinicFlow
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import uuid

@dataclass
class Visit:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    patient_name: str
    priority: int  # 1=high, 3=low
    scheduled_time: datetime
    status: str = "waiting"  # waiting, in_progress, completed

@dataclass
class StaffMember:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    specialty: str
    current_patients: List[str] = field(default_factory=list)

class ClinicQueue:
    def __init__(self):
        self.visits: Dict[str, Visit] = {}
        self.staff: Dict[str, StaffMember] = {}
    
    def add_visit(self, patient_name: str, priority: int, scheduled_time: datetime):
        visit = Visit(patient_name=patient_name, priority=priority, scheduled_time=scheduled_time)
        self.visits[visit.id] = visit
    
    def assign_to_staff(self, staff_id: str, visit_id: str):
        if visit_id in self.visits and staff_id in self.staff:
            visit = self.visits[visit_id]
            visit.status = "in_progress"
            self.staff[staff_id].current_patients.append(visit_id)

clinic = ClinicQueue()
clinic.add_visit("Alice Smith", 1, datetime.now())
clinic.add_visit("Bob Jones", 2, datetime.now() + timedelta(minutes=30))
clinic.add_visit("Charlie Brown", 3, datetime.now() + timedelta(hours=1))
