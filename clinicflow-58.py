# === Stage 58: Add bulk update behavior for selected records ===
# Project: ClinicFlow
def bulk_update_visits(self, updates: dict):
    """Apply a batch of visit-field changes returned by staff handoff."""
    for vid, fields in updates.items():
        if vid not in self._visits:
            print(f"[WARN] {vid} does not exist – skipping")
            continue
        for k, v in fields.items():
            if hasattr(self._visits[vid], k):
                setattr(self._visits[vid], k, v)

def bulk_update_staff_notes(self, updates: dict):
    """Apply a batch of staff-note changes."""
    for sid, fields in updates.items():
        if sid not in self._staff:
            print(f"[WARN] {sid} does not exist – skipping")
            continue
        for k, v in fields.items():
            if hasattr(self._staff[sid], k):
                setattr(self._staff[sid], k, v)

def bulk_update_waiting_room(self, updates: dict):
    """Apply a batch of waiting-room changes."""
    for k, v in updates.items():
        if hasattr(self._waiting_room, k):
            setattr(self._waiting_room, k, v)
