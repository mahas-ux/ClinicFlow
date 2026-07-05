# === Stage 24: Add grouped summaries by category or status ===
# Project: ClinicFlow
def generate_grouped_summary(visits):
    from collections import defaultdict
    groups = defaultdict(list)
    for v in visits:
        key = f"{v['status']}_{v.get('priority', 'normal')}"
        groups[key].append(v)
    lines = ["=== Daily Grouped Summary ==="]
    for (status, priority), items in sorted(groups.items()):
        count = len(items)
        if status == "completed":
            color = "\033[92m"  # Green
        elif status == "waiting":
            color = "\033[33m"   # Yellow
        else:
            color = "\033[91m"   # Red
        reset = "\033[0m"
        lines.append(f"{color}{status.upper()} ({priority}):{reset} {count}")
        for item in items[:5]:  # Limit preview to first 5 per group
            lines.append(f"  - {item['patient_id']} | Dr. {item.get('doctor', 'N/A')}")
    if len(groups) > 5:
        remaining = sum(len(v) for k, v in groups.items() if not any(k.startswith(s) and s == "completed" for s in ["waiting", "cancelled"]))
        lines.append(f"... and {remaining} more visits grouped above.")
    return "\n".join(lines)
