# === Stage 31: Add compact table rendering for long lists ===
# Project: ClinicFlow
def render_compact_table(headers, rows):
    """Render a compact table with fixed width columns."""
    col_widths = [max(len(str(h)), 8) for h in headers]
    lines = []
    header_line = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    lines.append("-+-".join("-" * w for w in col_widths))
    for row in rows:
        line = " | ".join(str(row[i]).ljust(col_widths[i]) if i < len(row) else str(row).center(col_widths[i]) for i in range(len(headers)))
        lines.append(line)
    return "\n".join(lines)

def compact_summary(visits):
    """Generate a compact daily summary of visits."""
    stats = {"total": 0, "treated": 0, "waiting": 0}
    for v in visits:
        stats["total"] += 1
        if v.status == "Treated":
            stats["treated"] += 1
        elif v.status == "Waiting":
            stats["waiting"] += 1
    return render_compact_table(
        ["#", "Patient", "Priority", "Status"],
        [(i+1, v.patient_name or f"P{i}", str(v.priority), v.status) for i, v in enumerate(visits)]
    ) + "\n\n" + ", ".join(f"{k}: {v}" for k, v in stats.items())
