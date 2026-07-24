# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ClinicFlow
def reset_demo_data():
    """Reset ClinicFlow demo data for manual testing."""
    from clinicflow.models import Visit, WaitingRoom, StaffHandoff, DailySummary
    from clinicflow.services.demo_data_service import DemoDataService

    demo = DemoDataService()
    visit_ids = demo.get_all_visit_ids()
    if visit_ids:
        for vid in visit_ids:
            try:
                visit = Visit.objects.get(id=vid)
                visit.delete()
            except Exception:
                pass
    room_ids = demo.get_all_waiting_room_ids()
    if room_ids:
        for rid in room_ids:
            try:
                WaitingRoom.objects.get(id=rid).delete()
            except Exception:
                pass
    handoff_ids = demo.get_all_handoff_ids()
    if handoff_ids:
        for hid in handoff_ids:
            try:
                StaffHandoff.objects.get(id=hid).delete()
            except Exception:
                pass
    summary_ids = demo.get_all_summary_ids()
    if summary_ids:
        for sid in summary_ids:
            try:
                DailySummary.objects.get(id=sid).delete()
            except Exception:
                pass
    print("Demo data reset complete.")
