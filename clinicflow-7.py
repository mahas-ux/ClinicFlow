# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ClinicFlow
def format_visit_summary(visit):
    status = visit.status.capitalize() if visit else "None"
    priority_str = f"[{visit.priority}]" if hasattr(visit, 'priority') and visit.priority else ""
    doctor_name = getattr(visit, 'doctor', None) or "-"
    return f"{status:12} {priority_str:<8} | {str(doctor_name):<30} | Patient: {getattr(visit, 'patient_id', 'N/A')} ({getattr(visit, 'arrival_time', '')})"

def format_waiting_room(room):
    if not room or len(room) == 0:
        return f"{room.name:<25} : Empty"
    lines = [f"{room.name:<25} : {len(room)} patients"]
    for idx, visit in enumerate(room, 1):
        line = format_visit_summary(visit).replace("|", "")
        if len(line) > 40:
            line = line[:37] + "..."
        lines.append(f"      [{idx}] {line}")
    return "\n".join(lines)

def print_daily_report(visits, rooms):
    print("=" * 80)
    print("CLINIC FLOW - DAILY SUMMARY")
    print("=" * 80)
    if visits:
        for visit in visits:
            print(format_visit_summary(visit))
    else:
        print("No visits recorded today.")
    print("-" * 40)
    for room_name, room_visits in rooms.items():
        print(format_waiting_room(room_visits))
    print("=" * 80)
