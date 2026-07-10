# === Stage 35: Add active user switching and user-specific records ===
# Project: ClinicFlow
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class User:
    name: str
    email: str
    role: str = "patient"


@dataclass
class PatientRecord:
    patient_id: int
    user: User
    visit_history: List[Visit] = field(default_factory=list)
    priority_count: Dict[str, int] = field(default_factory=lambda: {"low": 0, "medium": 0, "high": 0})


class ClinicFlowUserContext:
    def __init__(self):
        self.active_user: Optional[User] = None
        self.patient_records: Dict[int, PatientRecord] = {}

    def register_patient(self, user: User) -> int:
        pid = len(self.patient_records) + 1
        record = PatientRecord(patient_id=pid, user=user)
        self.patient_records[pid] = record
        return pid

    def set_active_user(self, patient_record: Optional[PatientRecord]):
        if patient_record is not None:
            self.active_user = patient_record.user
            self._update_priority_counts(patient_record)

    def _update_priority_counts(self, record: PatientRecord):
        for visit in record.visit_history:
            for level in ("low", "medium", "high"):
                if visit.priority == level:
                    record.priority_count[level] += 1

    def get_active_user_info(self) -> Optional[Dict]:
        if self.active_user is None:
            return None
        record = self._find_record_for_user(self.active_user)
        if record is None:
            return {"user": self.active_user, "visit_count": len(record.visit_history)}
        return {**record.to_dict(), "active": True}

    def _find_record_for_user(self, user: User) -> Optional[PatientRecord]:
        for rec in self.patient_records.values():
            if rec.user == user:
                return rec
        return None
