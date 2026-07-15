# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ClinicFlow
def main():
    clinic = Clinic("Oaks Family Health")

    # --- Visits with priorities ---
    v1 = Visit("Cough", priority=3, duration="5m")
    v2 = Visit("Broken arm", priority=4)
    v3 = Visit("Follow-up bloodwork", priority=1, duration="10m")
    v4 = Visit("Earache", priority=2, duration="8m")

    # --- Staff handoff ---
    nurse = Nurse("R. Chen")
    clinic.register_staff(nurse)

    # --- Daily summary ---
    day = clinic.new_day()
    clinic.add_visits(day, [v1, v2, v3, v4])
    clinic.queue_by_priority([v1, v2, v3, v4])
    nurse.set_next_patient(v3)
    report = clinic.daily_summary(nurse, day)

    print(report)


if __name__ == "__main__":
    main()
