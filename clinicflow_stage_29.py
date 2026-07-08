# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ClinicFlow
def upcoming_visits(visit_dict, days_ahead=7):
    """Return visits due within `days_ahead` days as sorted (date, visit_id) tuples."""
    import datetime
    today = datetime.date.today()
    cutoff = today + datetime.timedelta(days=days_ahead)
    result = []
    for vid, v in visit_dict.items():
        if isinstance(v.get('scheduled_date'), str):
            d = datetime.datetime.strptime(v['scheduled_date'], '%Y-%m-%d').date()
        else:
            d = v['scheduled_date']
        if today <= d <= cutoff:
            result.append((d, vid))
    return sorted(result)

def upcoming_staff_handoffs(handoff_dict, days_ahead=7):
    """Return staff handoffs due within `days_ahead` as (date, handoff_id) tuples."""
    import datetime
    today = datetime.date.today()
    cutoff = today + datetime.timedelta(days=days_ahead)
    result = []
    for hid, h in handoff_dict.items():
        if isinstance(h.get('scheduled_date'), str):
            d = datetime.datetime.strptime(h['scheduled_date'], '%Y-%m-%d').date()
        else:
            d = h['scheduled_date']
        if today <= d <= cutoff:
            result.append((d, hid))
    return sorted(result)

def upcoming_summaries(summary_dict):
    """Return all pending daily summaries as (date_str, summary_id) tuples."""
    return [(s.get('date'), s.get('summary_id')) for s in summary_dict.values() if not s.get('completed', False)]
