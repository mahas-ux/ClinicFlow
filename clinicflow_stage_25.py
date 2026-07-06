# === Stage 25: Add daily summary calculations ===
# Project: ClinicFlow
def daily_summary(agenda):
    """Return a dict with total visits, priority distribution, and average wait time."""
    counts = {}
    waits = []
    for visit in agenda:
        key = f"P{visit.priority}" if isinstance(visit.priority, int) else str(visit.priority).upper()
        counts[key] = counts.get(key, 0) + 1
        if hasattr(visit, 'duration') and visit.duration > 0:
            waits.append(visit.duration)
    avg_wait = sum(waits) / len(waits) if waits else 0.0
    return {'visits': len(agenda), 'by_priority': counts, 'avg_wait_minutes': round(avg_wait, 1)}
