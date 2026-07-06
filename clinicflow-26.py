# === Stage 26: Add weekly summary calculations ===
# Project: ClinicFlow
def weekly_summary(reporter, week_start):
    """Compute a compact summary for each day of a given ISO-week."""
    days = []
    for d in range(7):
        date = week_start + timedelta(days=d)
        total_visits = sum(v["duration_min"] for v in reporter.visits if _date_in_week(v["visit_date"], week_start))
        avg_duration = (total_visits / sum(1 for v in reporter.visits if _date_in_week(v["visit_date"], week_start))) if total_visits else 0.0
        high_priority = sum(1 for v in reporter.visits if _date_in_week(v["visit_date"], week_start) and v["priority"] == "high")
        handoffs = sum(1 for h in reporter.handoffs if _date_in_week(h["handoff_date"], week_start))
        days.append({
            "day": date,
            "visits": total_visits,
            "avg_duration_min": round(avg_duration, 1),
            "high_priority_count": high_priority,
            "staff_handoffs": handoffs,
        })
    return {"week_start": week_start, "days": days}

def _date_in_week(date, week_start):
    """Return True if date falls in the ISO-week that contains week_start."""
    weekday = (date - week_start).days % 7
    return weekday < 7 and weekday >= 0
