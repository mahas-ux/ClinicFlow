# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ClinicFlow
def import_text_file(path):
    """Read a simple line-based text file and return its contents as a list of lines."""
    with open(path, 'r') as f:
        return [line.rstrip('\n') for line in f]


def export_to_text(queues, output_path):
    """Write the current state of all queues to a plain text file."""
    lines = []
    lines.append("ClinicFlow Queue Export")
    lines.append("=" * 30)
    for name, queue in queues.items():
        lines.append(f"Queue: {name}")
        for visit in queue.get_visits():
            lines.append(visit.to_text())
        lines.append("-" * 25)
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))
