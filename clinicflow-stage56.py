# === Stage 56: Add compact error classes for domain failures ===
# Project: ClinicFlow
class ClinicFlowError(Exception):
    """Base class for all ClinicFlow domain errors."""
    pass


class VisitAlreadyScheduled(ClinicFlowError):
    """A visit has already been assigned to a slot."""
    def __init__(self, patient_id: str, scheduled_at: datetime) -> None:
        self.patient_id = patient_id
        self.scheduled_at = scheduled_at
        super().__init__(f"Patient {patient_id} already scheduled at {scheduled_at}")


class VisitCancelled(ClinicFlowError):
    """A previously scheduled visit was cancelled."""
    def __init__(self, patient_id: str, original_slot: datetime) -> None:
        self.patient_id = patient_id
        self.original_slot = original_slot
        super().__init__(f"Visit for {patient_id} cancelled at {original_slot}")


class PriorityConflict(ClinicFlowError):
    """A visit with higher priority tries to occupy a slot already taken."""
    def __init__(self, patient_name: str, existing_patient: str) -> None:
        super().__init__(f"Priority conflict: {patient_name} vs {existing_patient}")


class StaffHandoffInProgress(ClinicFlowError):
    """A staff handoff is currently active and cannot be interrupted."""
    def __init__(self, current_staff_id: str, target_staff_id: str) -> None:
        super().__init__(f"Handoff from {current_staff_id} to {target_staff_id} still in progress")


class DailySummaryIncomplete(ClinicFlowError):
    """A daily summary cannot be generated because not all visits were processed."""
    def __init__(self, missing_visits: int) -> None:
        super().__init__(f"Daily summary incomplete: {missing_visits} visits unprocessed")


class WaitingRoomFull(ClinicFlowError):
    """The waiting room capacity has been exceeded."""
    def __init__(self, max_capacity: int, current_count: int) -> None:
        self.max_capacity = max_capacity
        self.current_count = current_count
        super().__init__(f"Waiting room full ({current_count}/{max_capacity})")


class InvalidPatientId(ClinicFlowError):
    """The patient identifier does not match the expected format."""
    def __init__(self, raw_id: str) -> None:
        super().__init__(f"Invalid patient ID format: {raw_id}")
