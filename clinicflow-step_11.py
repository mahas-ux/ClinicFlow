# === Stage 11: Add JSON export for the current application state ===
# Project: ClinicFlow
def export_state_to_json(self, filename="clinic_flow.json"):
    import json
    state = {
        "visits": [self._visit_dump(v) for v in self.visits],
        "waiting_rooms": list(self.waiting_rooms.items()),
        "staff_handoffs": list(self.staff_handoffs.items()) if hasattr(self, 'staff_handoffs') else [],
        "daily_summary": {k: len([v for v in self.visits if v.status == k]) for k in ["completed", "cancelled"]}
    }
    with open(filename, "w") as f:
        json.dump(state, f, indent=2)
