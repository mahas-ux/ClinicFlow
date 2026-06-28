# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ClinicFlow
class FilterMixin:
    def filter_visits(self, status=None, category=None, owner=None, tag=None):
        filtered = self.visits.copy()
        if status is not None and status != "all":
            filtered = [v for v in filtered if v.get("status") == status]
        if category is not None:
            filtered = [v for v in filtered if v.get("category") == category]
        if owner is not None:
            filtered = [v for v in filtered if v.get("owner") == owner]
        if tag is not None:
            filtered = [v for v in filtered if any(tag.lower() in t.lower() for t in v.get("tags", []))]
        return filtered

    def get_active_visits(self):
        return self.filter_visits(status="active")

    def get_completed_today(self, date=None):
        today = date or datetime.now().date()
        completed = [v for v in self.visits if v.get("status") == "completed" and v.get("scheduled_date", "").startswith(today.isoformat())]
        return completed
