# === Stage 14: Add file load support with fallback demo data ===
# Project: ClinicFlow
import json, os

def load_data(path: str = "clinic.json") -> dict:
    try:
        with open(path) as f: return json.load(f)
    except FileNotFoundError:
        demo = {
            "visits": [{"id": 101, "patient": "Alice", "priority": 2, "status": "waiting"}],
            "staff": [{"name": "Dr. Smith", "shifts": ["morning"]}],
            "rooms": {"A": {"capacity": 5}}
        }
        with open(path, "w") as f: json.dump(demo, f)
        return demo
