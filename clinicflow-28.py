# === Stage 28: Add overdue item detection based on due dates ===
# Project: ClinicFlow
def detect_overdue_visits(visit_queue, today=None):
    """Identify visits whose due date has passed and return a list of overdue visit records."""
    if today is None:
        from datetime import date as _date
        today = _date.today()

    overdue = []
    for visit in visit_queue:
        if hasattr(visit, 'due_date') and visit.due_date < today:
            overdue.append({
                'patient_name': getattr(visit, 'patient_name', 'Unknown'),
                'visit_id': getattr(visit, 'visit_id', None),
                'priority': getattr(visit, 'priority', 3),
                'due_date': visit.due_date.isoformat() if hasattr(visit.due_date, 'isoformat') else str(visit.due_date),
            })

    overdue.sort(key=lambda x: (x['priority'], x['due_date']))
    return overdue


def print_overdue_summary(overdue_list):
    """Print a human-readable summary of overdue visits."""
    if not overdue_list:
        print("\n✓ All visits are up-to-date. No overdue items found.")
        return

    print(f"\n⚠ OVERDUE VISITS REPORT ({len(overdue_list)} item{'s' if len(overdue_list) > 1 else ''})")
    print("-" * 50)
    for idx, item in enumerate(overdue_list, start=1):
        due = item['due_date']
        priority_label = {1: 'Critical', 2: 'High', 3: 'Medium', 4: 'Low'}.get(item['priority'], f"P{item['priority']}")
        print(f"  {idx}. [{priority_label}] Patient: {item['patient_name']} | Due: {due} (Visit ID: {item['visit_id']})")


# Example usage:
if __name__ == "__main__":
    today = None  # set to date.today() for real-time check; leave None to use today automatically

    sample_queue = [
        type('Visit', (), {'due_date': '2025-11-01', 'patient_name': 'Alice', 'visit_id': 'V001', 'priority': 3})(),
        type('Visit', (), {'due_date': '2025-12-20', 'patient_name': 'Bob', 'visit_id': 'V002', 'priority': 2})(),
        type('Visit', (), {'due_date': '2026-03-15', 'patient_name': 'Charlie', 'visit_id': 'V003', 'priority': 4})(),
    ]

    overdue = detect_overdue_visits(sample_queue, today)
    print_overdue_summary(overdue)
