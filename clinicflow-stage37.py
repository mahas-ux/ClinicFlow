# === Stage 37: Add recommendations for the next useful action ===
# Project: ClinicFlow
def suggest_next_action(visit, staff_handoff):
    """Generate a recommendation for the next useful action based on current state."""
    if visit['status'] == 'waiting' and visit['priority'] >= 3:
        return "Schedule a follow-up call to check patient's condition."
    elif visit['status'] == 'in_progress' and staff_handoff.get('next_action'):
        return f"Perform the next action: {staff_handoff['next_action']}."
    elif not any(v['status'] in ['waiting', 'scheduled'] for v in _get_all_visits()):
        return "Run a daily summary report to review today's clinic activity."
    else:
        return "Continue monitoring queue and assist arriving patients."
