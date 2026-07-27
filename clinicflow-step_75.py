# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ClinicFlow
class ValidationReport:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def check_no_duplicate_visits(self, visits_by_id):
        if len(visits_by_id) != len(visits_by_id.values()):
            for eid in visits_by_id:
                if visits_by_id[eid] > 1:
                    self.errors.append(
                        f"Duplicate visit ID(s): {eid}"
                    )

    def check_orphaned_waiting_room(self, waiting_rooms, active_visit_ids):
        for wr in waiting_rooms.values():
            ids = set(v["visit_id"] for v in wr.get("visits", []))
            orphaned = [vid for vid in ids if vid not in active_visit_ids]
            if orphaned:
                self.warnings.append(
                    f"Waiting room {wr['id']} has no active visits: {orphaned}"
                )

    def check_staff_handoff_gap(self, handoffs):
        for h in handoffs.values():
            gap = (h["end_time"] - h["start_time"]).total_seconds() / 3600
            if gap > 24:
                self.warnings.append(
                    f"Handoff {h['id']} spans {gap:.1f} hours (possible gap): "
                    f"{h['staff']}"
                )

    def validate(self, visits_by_id=None, waiting_rooms=None, handoffs=None):
        if visits_by_id:
            self.check_no_duplicate_visits(visits_by_id)
        if waiting_rooms:
            active = set()
            for v in visits_by_id.values():
                for vid in v:
                    active.add(vid)
            self.check_orphaned_waiting_room(waiting_rooms, active)
        if handoffs:
            self.check_staff_handoff_gap(handoffs)

    def report(self):
        lines = ["=== ClinicFlow Validation Report ===\n"]
        if not self.errors and not self.warnings:
            return "\n".join(lines + ["All checks passed."])
        for e in self.errors:
            lines.append(f"ERROR  : {e}")
        for w in self.warnings:
            lines.append(f"WARN   : {w}")
        if not self.errors and self.warnings:
            lines[-1] = f"WARN   : {self.warnings[0]}"
        return "\n".join(lines)
