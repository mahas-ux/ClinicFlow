# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ClinicFlow
def get_visit_summary(visit: Visit) -> dict:
    """Return a summary dictionary for a single visit containing patient name, priority level, and whether the visit is completed."""
    return {
        "patient": visit.patient_name or "Unknown",
        "priority": visit.priority_level,
        "status": visit.status if hasattr(visit, 'status') else "pending"
    }

def get_daily_summary(day_visits: list) -> dict:
    """Aggregate a day's visits into counts by priority and overall completion rate."""
    total = len(day_visits)
    completed = sum(1 for v in day_visits if hasattr(v, 'status') and v.status == "completed")
    return {
        "total_visits": total,
        "completed": completed,
        "completion_rate": f"{(completed / total * 100) if total else 0:.1f}%"
    }

def format_handoff_log(handoffs: list[str]) -> str:
    """Format a list of handoff log entries into a readable string."""
    return "\n".join(f"- {h}" for h in handoffs) if handoffs else "No handoffs recorded."
