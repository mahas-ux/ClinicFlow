# === Stage 44: Add backup creation for the data file ===
# Project: ClinicFlow
import os, shutil, time

DATA_FILE = "clinic_queue.json"

def create_backup():
    if not os.path.exists(DATA_FILE):
        return
    backup_path = f"{DATA_FILE}.bak_{int(time.time())}"
    shutil.copy2(DATA_FILE, backup_path)
    print(f"[Backup] Created {backup_path}")
