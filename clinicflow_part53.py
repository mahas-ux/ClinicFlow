# === Stage 53: Add command help text and usage examples ===
# Project: ClinicFlow
def print_help():
    """Display usage info and examples for ClinicFlow."""
    help_lines = [
        "ClinicFlow — a clinic queue coordinator",
        "",
        "Usage:",
        "  python clinic_flow.py <command> [--help]",
        "Commands: new, add-visit, list-visits, serve-next, handoff, summary, exit",
        "",
        "Examples:",
        '  ClinicFlow > new',
        '  ClinicFlow > add-visit name="Dr. Lee" priority=high duration=30',
        '  ClinicFlow > list-visits',
        '  ClinicFlow > serve-next',
        '  ClinicFlow > handoff staff="Nurse Kim"',
        '  ClinicFlow > summary',
    ]
    print("\n".join(help_lines))
