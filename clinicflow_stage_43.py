# === Stage 43: Add CSV import for the primary record type ===
# Project: ClinicFlow
def import_visits_from_csv(csv_path: str) -> list[Visit]:
    """Read a ClinicFlow CSV with columns: visit_id, patient_name, priority, start_time."""
    from datetime import datetime
    visits = []
    with open(csv_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            v = Visit(
                visit_id=row["visit_id"].strip(),
                patient_name=row["patient_name"].strip(),
                priority=int(row["priority"]),
                start_time=datetime.fromisoformat(row["start_time"].strip()),
            )
            visits.append(v)
    return visits
