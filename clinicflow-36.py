# === Stage 36: Add templates for quickly creating common records ===
# Project: ClinicFlow
class RecordTemplates:
    """Factory helpers to quickly create common ClinicFlow records."""

    @staticmethod
    def new_visit(name, priority="normal"):
        return Visit(name=name, priority=priority)

    @staticmethod
    def normal_visit(name):
        return Visit(name=name, priority="normal")

    @staticmethod
    def urgent_visit(name):
        return Visit(name=name, priority="urgent")

    @staticmethod
    def new_patient(name, age=0):
        return Patient(name=name, age=age)

    @staticmethod
    def new_staff(first_name, last_name):
        return Staff(first_name=first_name, last_name=last_name)

    @staticmethod
    def new_waiting_room(capacity=20):
        return WaitingRoom(capacity=capacity)

    @staticmethod
    def daily_summary(date=None):
        if date is None:
            from datetime import date as _date
            date = _date.today()
        return DailySummary(date=date)
