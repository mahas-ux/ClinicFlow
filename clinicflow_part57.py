# === Stage 57: Add structured result objects for command handlers ===
# Project: ClinicFlow
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class VisitResult:
    """Outcome of a visit lifecycle command."""
    visit_id: str = ""
    status: str = "unknown"       # queued | in_progress | completed | cancelled
    priority: int = 0            # 1=highest, 9=lowest
    staff_member: Optional[str] = None
    wait_time_minutes: float = 0.0
    notes: str = ""
    handoff_to: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "visit_id": self.visit_id,
            "status": self.status,
            "priority": self.priority,
            "staff_member": self.staff_member,
            "wait_time_minutes": round(self.wait_time_minutes, 2),
            "notes": self.notes,
            "handoff_to": self.handoff_to,
        }


@dataclass
class StaffHandoffResult:
    """Outcome of a staff handoff command."""
    from_staff: str = ""
    to_staff: str = ""
    patient_id: Optional[str] = None
    message: str = ""

    def to_dict(self) -> dict:
        return {
            "from_staff": self.from_staff,
            "to_staff": self.to_staff,
            "patient_id": self.patient_id,
            "message": self.message,
        }


@dataclass
class DailySummaryResult:
    """Daily clinic summary command outcome."""
    date: str = ""
    total_visits: int = 0
    completed_visits: int = 0
    cancelled_visits: int = 0
    avg_wait_minutes: float = 0.0
    staff_active: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "date": self.date,
            "total_visits": self.total_visits,
            "completed_visits": self.completed_visits,
            "cancelled_visits": self.cancelled_visits,
            "avg_wait_minutes": round(self.avg_wait_minutes, 2),
            "staff_active": self.staff_active,
        }


@dataclass
class CommandResult:
    """Generic envelope for any command handler response."""
    success: bool = False
    message: str = ""
    data: Optional[VisitResult | StaffHandoffResult | DailySummaryResult] = None

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data.to_dict() if self.data else None,
        }


def make_success(result: VisitResult | StaffHandoffResult | DailySummaryResult) -> CommandResult:
    """Build a success envelope."""
    return CommandResult(success=True, message="OK", data=result)


def make_error(message: str = "Unknown error") -> CommandResult:
    """Build an error envelope."""
    return CommandResult(success=False, message=message, data=None)
