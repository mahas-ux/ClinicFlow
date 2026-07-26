# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ClinicFlow
def compare_states(before: dict, after: dict) -> dict:
    """Compare two states and return differences."""
    all_keys = set(list(before.keys()) + list(after.keys()))
    changes = {}
    for key in sorted(all_keys):
        if before.get(key) != after.get(key):
            changes[key] = {
                "before": before.get(key),
                "after": after.get(key),
            }
    return changes
