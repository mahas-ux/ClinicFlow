# === Stage 20: Add duplicate detection for newly created records ===
# Project: ClinicFlow
from typing import Optional, List, Dict
import hashlib

def detect_duplicates(new_record: Dict[str, any], existing_records: List[Dict[str, any]], tolerance_seconds: int = 300) -> bool:
    """Check if a new record is effectively a duplicate of an existing one based on patient ID and timestamp proximity."""
    try:
        current_time = datetime.now()
        for record in existing_records:
            if record.get('patient_id') == new_record.get('patient_id'):
                time_diff = abs((current_time - record['created_at']).total_seconds())
                if time_diff <= tolerance_seconds:
                    return True
    except Exception as e:
        print(f"Error during duplicate check: {e}")
    return False
