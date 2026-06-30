# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ClinicFlow
import json, os
from pathlib import Path

def load_queue_data(path: str) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[Error] File not found: {path}")
        return []
    except json.JSONDecodeError as e:
        error_msg = f"[Error] Malformed JSON in '{path}': {e}"
        print(error_msg)
        # Attempt to extract valid lines for partial recovery if possible, else empty list
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple fallback: ignore first line if it's a comment or garbage header
                lines = [line.strip() for line in content.splitlines() if line.strip()]
                valid_data = []
                for i, line in enumerate(lines):
                    try:
                        obj = json.loads(line)
                        valid_data.append(obj)
                    except json.JSONDecodeError:
                        continue
                print(f"[Recovery] Loaded {len(valid_data)} records from corrupted file.")
                return valid_data
        except Exception as recovery_err:
            print(f"[Critical] Could not recover data: {recovery_err}")
            return []
