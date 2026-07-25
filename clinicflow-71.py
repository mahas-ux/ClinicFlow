# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ClinicFlow
def seed_demo_data(db):
    """Populate ClinicFlow with deterministic sample data for demonstration."""
    if db.get("visits"):
        return  # already seeded
    
    patients = [
        {"name": "Alice Johnson", "age": 42, "id_number": "P001"},
        {"name": "Bob Smith", "age": 35, "id_number": "P002"},
        {"name": "Carol Williams", "age": 67, "id_number": "P003"},
    ]
    
    visits = []
    for i, p in enumerate(patients):
        priority = ["urgent", "normal", "routine"][i] if i > 0 else "normal"
        status = "in_progress" if i == 1 else ("waiting" if i < 2 else "completed")
        visits.append({
            "patient": {"name": p["name"], "age": p["age"], "id_number": p["id_number"]},
            "priority": priority,
            "status": status,
            "arrival_time": f"08:{i+15:02d}",
        })
    
    db["visits"] = visits
    db["patients"] = patients
    
    staff = [
        {"name": "Dr. Evans", "role": "doctor"},
        {"name": "Nurse Lee", "role": "nurse"},
    ]
    db["staff"] = staff
    
    db["summary"] = {
        "date": "2024-06-15",
        "total_visits": len(visits),
        "by_priority": {"urgent": 1, "normal": 1, "routine": 1},
        "by_status": {"waiting": 1, "in_progress": 1, "completed": 1},
    }
