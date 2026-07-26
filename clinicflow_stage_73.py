# === Stage 73: Add a lightweight HTML report export ===
# Project: ClinicFlow
def export_html_report(self, path="clinicflow_report.html"):
    """Export a lightweight HTML report of all visit records."""
    rows = []
    for v in self._visits:
        rows.append(
            f'<tr><td>{v.id}</td>'
            f'<td>{v.patient_name}</td>'
            f'<td>{v.priority}</td>'
            f'<td>{v.arrival_time.strftime("%Y-%m-%d %H:%M") if v.arrival_time else "N/A"}</td>'
            f'<td>{v.status}</td></tr>'
        )
    html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        '<style>body{font-family:sans-serif;margin:20px}table{border-collapse:collapse;width:100%}'
        'th,td{border:1px solid #ddd;padding:6px 10px;text-align:left}</style></head><body>'
        f'<h1>ClinicFlow Daily Summary</h1>'
        f'<p>Total visits: {len(self._visits)}</p>'
        '<table><thead><tr><th>ID</th><th>Patient</th><th>Priority</th>'
        '<th>Arrival Time</th><th>Status</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table>'
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
