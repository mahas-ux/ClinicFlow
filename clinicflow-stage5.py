# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ClinicFlow
def update_visit(visit_id: str, **kwargs) -> dict:
    if visit_id not in visits_db:
        return {"status": "error", "message": f"Visit {visit_id} not found"}
    record = visits_db[visit_id]
    for key, value in kwargs.items():
        if hasattr(record, key):
            setattr(record, key, value)
        elif key in record:
            record[key] = value
    return {"status": "success", "message": f"Visit {visit_id} updated"}

def update_staff_status(staff_id: str, status: str) -> dict:
    if staff_id not in staff_db:
        return {"status": "error", "message": f"Staff {staff_id} not found"}
    staff_db[staff_id]["current_status"] = status
    return {"status": "success", "message": f"Staff {staff_id} status set to {status}"}

def update_waiting_room(room_id: str, capacity: int) -> dict:
    if room_id not in waiting_rooms_db:
        return {"status": "error", "message": f"Waiting room {room_id} not found"}
    waiting_rooms_db[room_id]["capacity"] = capacity
    return {"status": "success", "message": f"Room {room_id} capacity updated to {capacity}"}

def update_daily_summary(date: str, summary_data: dict) -> dict:
    if date not in daily_summaries_db:
        daily_summaries_db[date] = {}
    for key, value in summary_data.items():
        daily_summaries_db[date][key] = value
    return {"status": "success", "message": f"Summary for {date} updated"}
