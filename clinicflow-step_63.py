# === Stage 63: Add relationships between records where useful ===
# Project: ClinicFlow
class Visit:
    def __init__(self, patient_id=None, doctor_id=None, room_id=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.room_id = room_id


class Patient:
    def __init__(self, name="", clinic_id=None):
        self.name = name
        self.clinic_id = clinic_id
        self.visits = []


class Doctor:
    def __init__(self, name="", clinic_id=None):
        self.name = name
        self.clinic_id = clinic_id
        self.schedule = {}  # date -> [Visit]


def link_records(visits, patients, doctors):
    """Attach visit references and doctor schedule to patient/doctor records."""
    for v in visits:
        if v.patient_id is not None:
            p = next((x for x in patients if x.name == "P" + str(v.patient_id)), None)
            if p:
                p.visits.append(v)

        if v.doctor_id is not None:
            d = next((x for x in doctors if x.name == "D" + str(v.doctor_id)), None)
            if d and v.room_id is not None:
                date_key = f"{v.room_id}_{v.patient_id}"
                d.schedule[date_key] = v


if __name__ == "__main__":
    visits, patients, doctors = [], [], []
    for i in range(5):
        visits.append(Visit(patient_id=i + 1, doctor_id=(i % 3) + 1))
        patients.append(Patient(name=f"P{i+1}"))
        doctors.append(Doctor(name=f"D{(i%3)+1}"))

    link_records(visits, patients, doctors)
    for p in patients:
        print(p.name, "visits:", [v.patient_id for v in p.visits])
