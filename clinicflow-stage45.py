# === Stage 45: Add restore from backup with validation ===
# Project: ClinicFlow
def restore_backup(backup_path, target_dir="."):
    import os, json
    from datetime import datetime

    if not backup_path.endswith(".json"):
        raise ValueError(f"Not a JSON file: {backup_path}")

    with open(backup_path) as f:
        data = json.load(f)

    required_keys = {"visits", "waiting_rooms", "staff_handoffs"}
    missing = required_keys - set(data.keys())
    if missing:
        raise ValueError(f"Backup missing keys: {missing}")

    for visit in data.get("visits", []):
        for key in ("patient_name", "visit_type"):
            if key not in visit:
                raise ValueError(f"Incomplete visit entry: {visit}")

    os.makedirs(target_dir, exist_ok=True)
    backup_dt = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"clinicflow_restore_{backup_dt}.json"
    path = os.path.join(target_dir, filename)

    with open(path, "w") as out:
        json.dump(data, out, indent=2)

    return path
