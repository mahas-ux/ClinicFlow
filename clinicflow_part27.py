# === Stage 27: Add monthly summary calculations ===
# Project: ClinicFlow
def monthly_summary(records):
    """Aggregate clinic queue records by month and return a summary dict."""
    months = {}
    for r in records:
        date_str = r.get("date", "")[:7]  # YYYY-MM
        if date_str not in months:
            months[date_str] = {"visits": 0, "total_wait_min": 0, "staff_handoffs": 0}
        months[date_str]["visits"] += 1
        wait = r.get("wait_minutes", 0)
        if isinstance(wait, (int, float)):
            months[date_str]["total_wait_min"] += wait
        months[date_str]["staff_handoffs"] += r.get("handoff_count", 0)

    result = {}
    for date_str, stats in sorted(months.items()):
        avg_wait = stats["total_wait_min"] / stats["visits"] if stats["visits"] else 0
        result[date_str] = {
            "visits": stats["visits"],
            "avg_wait_minutes": round(avg_wait, 1),
            "staff_handoffs": stats["staff_handoffs"],
        }
    return result


# Example usage:
# summary = monthly_summary(visit_records)
# print(summary)
