# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ClinicFlow
def changelog(activities, max_entries=10):
    """Produce a compact, reverse-chronological changelog from the activity log."""
    seen = set()
    lines = []
    for act in reversed(activities):
        summary = act.get("summary", "") or ""
        if not summary:
            continue
        if summary.lower() in seen:
            continue
        seen.add(summary.lower())
        ts = act.get("timestamp", "")
        entry = f"{ts} - {summary}" if ts else summary
        lines.append(entry)
        if len(lines) >= max_entries:
            break
    return "\n".join(reversed(lines))
