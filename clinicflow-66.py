# === Stage 66: Add export of a short status dashboard ===
# Project: ClinicFlow
def export_dashboard(visits, waiting_room=None):
    """Export a compact status dashboard."""
    total = len(visits) + (len(waiting_room) if waiting_room else 0)
    lines = [f"ClinicFlow Dashboard ({total} patients)", "=" * 40]
    for v in visits:
        color = "HIGH" if v.priority == "high" else ("MED" if v.priority == "medium" else "LOW")
        lines.append(f"[{color}] {v.patient}: {v.service} - {v.status}")
    if waiting_room:
        lines.append("-" * 40)
        for w in waiting_room:
            lines.append(f"[WAIT] {w.patients} waiting, next: {w.next_slot}")
    return "\n".join(lines) + "\n---\n"
