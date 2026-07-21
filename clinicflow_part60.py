# === Stage 60: Add saved views for frequently used filters ===
# Project: ClinicFlow
class SavedView:
    """A named filter snapshot that can be re-applied to a visit list."""

    def __init__(self, name: str, filters: dict):
        self.name = name
        self.filters = filters  # e.g. {"priority": "high", "status": "in_progress"}

    def apply(self, visits: list) -> list:
        result = []
        for v in visits:
            if all(v.get(fk) == fv for fk, fv in self.filters.items()):
                result.append(v)
        return result

    def __repr__(self):
        return f"SavedView({self.name!r}, {self.filters})"
