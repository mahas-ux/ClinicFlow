# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ClinicFlow
def repair_queue(data):
    """Fix common data integrity issues in a clinic queue record."""
    if isinstance(data, dict):
        if "queue" not in data:
            data["queue"] = []
        q = data["queue"]
        for i, entry in enumerate(q):
            if not isinstance(entry, dict) or "visit_id" not in entry:
                q[i] = {"visit_id": None, "priority": 0}
            p = entry.get("priority", 0)
            try:
                entry["priority"] = int(p)
            except (ValueError, TypeError):
                entry["priority"] = 0

        if isinstance(data.get("visits"), list):
            for i, v in enumerate(data["visits"]):
                if not isinstance(v, dict) or "visit_id" not in v:
                    data["visits"][i] = {"visit_id": None}
                else:
                    try:
                        int(v.get("visit_id", ""))
                    except (ValueError, TypeError):
                        data["visits"][i]["visit_id"] = f"v_{i}"

        if isinstance(data.get("staff"), list):
            for i, s in enumerate(data["staff"]):
                if not isinstance(s, dict) or "name" not in s:
                    data["staff"][i] = {"name": "", "role": ""}

    return data
