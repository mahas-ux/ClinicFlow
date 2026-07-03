# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ClinicFlow
class ActivityLog:
    def __init__(self):
        self._log = []

    def log(self, action_name, details=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_name,
            "details": details or {}
        }
        self._log.append(entry)
        return entry

    def get_log(self):
        return list(reversed(self._log))
