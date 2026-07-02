# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ClinicFlow
def dry_run_mode():
    import sys, os
    if '--dry-run' in sys.argv:
        os.environ['CLINICFLOW_DRY_RUN'] = '1'
        print("Dry run mode enabled: no state changes will be persisted.")
        return True
    return False
