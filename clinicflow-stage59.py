# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ClinicFlow
def bulk_delete(self, visits: list[Visit], confirm: bool = False) -> int:
    """Remove multiple visits after optional confirmation."""
    if not confirm:
        raise PermissionError("Bulk delete requires explicit confirmation (set confirm=True).")
    deleted = 0
    for v in visits:
        if v.id is None or v._deleted:
            continue
        self.visits.remove(v)
        deleted += 1
    return deleted
