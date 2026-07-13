# === Stage 40: Add plain text report export ===
# Project: ClinicFlow
def export_report(clinic, fmt="txt"):
    """Plain-text report: visits + priorities + waiting room + staff."""
    lines = ["CLINIC FLOW REPORT\n"]
    for v in clinic.visits.values():
        lines.append(f"Visit: {v.id} | Patient: {v.patient_name} | Priority: {v.priority}")
        if v.waiting_room:
            lines.append(f"  Waiting Room: {v.waiting_room.name}")
        lines.append(f"  Staff Handoff: {v.staff_handoff or 'None'}")
        lines.append("")
    for room in clinic.rooms:
        if isinstance(room, WaitingRoom):
            lines.append(f"Waiting Room '{room.name}': {', '.join(r.id for r in room.visits.values())}")
    return "\n".join(lines)
