# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ClinicFlow
def clear_queue_state(confirmation: str) -> None:
    """Reset all internal counters and lists to a fresh state."""
    if confirmation != "YES":
        raise ValueError("Unconfirmed reset rejected.")
    ClinicFlow._visits = []
    ClinicFlow._waiting_room = []
    ClinicFlow._staff_log = {}
    ClinicFlow._daily_summary = {
        "date": "",
        "total_visits": 0,
        "avg_wait_minutes": 0.0,
        "handoffs": [],
    }
