# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ClinicFlow
class SortableQueue:
    def __init__(self, visits):
        self._visits = list(visits) if visits else []

    @property
    def visits(self):
        return self._visits.copy()

    def sort_by_title(self):
        self._visits.sort(key=lambda v: (v.get('title', '').lower(), v['id']))

    def sort_by_date(self):
        self._visits.sort(key=lambda v: v.get('created_at', ''), reverse=True)

    def sort_by_priority(self):
        priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        self._visits.sort(key=lambda v: (priority_map.get(v.get('priority', 'low'), 3), v['id']))

    def sort_by_last_update(self):
        self._visits.sort(key=lambda v: v.get('updated_at', ''), reverse=True)
