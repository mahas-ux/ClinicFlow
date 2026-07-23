# === Stage 67: Add a function that returns key project metrics ===
# Project: ClinicFlow
def project_metrics(visits=None, waiting_rooms=None, staff_handoffs=None):
    """Return a compact dictionary of key ClinicFlow metrics."""
    if visits is None:
        visits = []
    if waiting_rooms is None:
        waiting_rooms = []
    if staff_handoffs is None:
        staff_handoffs = []

    total_visits = len(visits)
    completed = sum(1 for v in visits if getattr(v, 'status', '').lower() == 'completed')
    priority_counts = {}
    for v in visits:
        p = getattr(v, 'priority', 0) or 0
        priority_counts[p] = priority_counts.get(p, 0) + 1

    avg_wait_seconds = (
        sum(getattr(v, 'wait_time_seconds', 0) for v in visits if completed) / max(completed, 1)
    )

    total_handoffs = len(staff_handoffs)
    handoff_by_staff = {}
    for h in staff_handoffs:
        s = getattr(h, 'staff_id', '') or ''
        handoff_by_staff[s] = handoff_by_staff.get(s, 0) + 1

    return {
        "total_visits": total_visits,
        "completed_visits": completed,
        "completion_rate": completed / max(total_visits, 1),
        "priority_distribution": priority_counts,
        "avg_wait_seconds": round(avg_wait_seconds, 2),
        "total_handoffs": total_handoffs,
        "handoffs_by_staff": handoff_by_staff,
    }
