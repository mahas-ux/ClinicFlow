# === Stage 72: Add Markdown report export ===
# Project: ClinicFlow
def export_markdown_report(self):
    """Generate a compact Markdown summary of clinic operations."""
    import datetime
    lines = []
    lines.append(f"# ClinicFlow Report - {datetime.date.today()}")
    lines.append("")
    for day, entry in self.daily_summaries.items():
        lines.append(f"## Day: {day}")
        if not entry:
            continue
        total = sum(entry.values())
        lines.append(f"- **Total visits**: {total}")
        lines.append(f"- **By priority**:")
        for p, count in sorted(entry.items()):
            lines.append(f"  - Priority {p}: {count}")
    lines.append("")
    return "\n".join(lines)
