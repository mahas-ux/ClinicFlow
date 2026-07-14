# === Stage 42: Add CSV export without external dependencies ===
# Project: ClinicFlow
import csv, io


def export_visits_to_csv(visits):
    """Export a list of visit dicts to an in-memory CSV string."""
    if not visits:
        return ""
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["VisitID", "PatientName", "Priority", "Status", "ArrivalTime"])
    for v in visits:
        writer.writerow([v["VisitID"], v.get("patient_name",""),
                         v.get("priority",""), v.get("status",""), v.get("arrival_time","")])
    return buf.getvalue()
