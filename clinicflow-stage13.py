# === Stage 13: Add file save support using a configurable path ===
# Project: ClinicFlow
import json, os
from pathlib import Path

class Config:
    def __init__(self):
        self.data_dir = Path.home() / ".clinicflow"
        self.state_file = self.data_dir / "queue_state.json"
    
    def ensure_dirs(self):
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def save_state(self, state: dict):
        self.ensure_dirs()
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)

config = Config()
