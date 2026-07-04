# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ClinicFlow
from datetime import datetime, timedelta
import json
from pathlib import Path

def archive_old_records(clinic_db: dict, days_threshold: int = 30):
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    archived_count = 0
    for patient_id in list(clinic_db['visits'].keys()):
        record = clinic_db['visits'][patient_id]
        if record.get('status') == 'completed' and record.get('end_time'):
            end_dt = datetime.fromisoformat(record['end_time'])
            if end_dt < cutoff_date:
                archive_path = Path(__file__).parent / f"archive_{patient_id}.json"
                with open(archive_path, "w", encoding="utf-8") as f:
                    json.dump({**record, 'archived_at': datetime.now().isoformat()}, f)
                del clinic_db['visits'][patient_id]
                archived_count += 1
    return archived_count

def restore_from_archive(clinic_db: dict, patient_id: str):
    archive_path = Path(__file__).parent / f"archive_{patient_id}.json"
    if not archive_path.exists():
        raise FileNotFoundError(f"No archive found for patient {patient_id}")
    with open(archive_path, "r", encoding="utf-8") as f:
        record_data = json.load(f)
    clinic_db['visits'][patient_id] = record_data
    return True
