# === Stage 38: Add data integrity checks for broken references ===
# Project: ClinicFlow
def check_integrity(self):
        """Validate that all references in visits, patients, and staff remain valid."""
        errors = []
        
        # Check visit references
        for visit_id, visit in self.visits.items():
            if visit.patient_id not in self.patients:
                errors.append(f"Visit {visit_id} references non-existent patient {visit.patient_id}")
            if visit.staff_id and visit.staff_id not in self.staff:
                errors.append(f"Visit {visit_id} references non-existent staff {visit.staff_id}")
        
        # Check that all patients have valid IDs (no duplicates)
        patient_ids = list(self.patients.keys())
        if len(patient_ids) != len(set(patient_ids)):
            errors.append("Duplicate patient IDs detected")
        
        # Check staff handoff references
        for s_id, staff in self.staff.items():
            if staff.handed_to and staff.handed_to not in self.staff:
                errors.append(f"Staff {s_id} handed to non-existent staff {staff.handed_to}")
            if staff.handed_from and staff.handed_from not in self.patients:
                errors.append(f"Staff {s_id} handed from non-existent patient {staff.handed_from}")
        
        # Check daily summary date consistency
        for date, summary in self.daily_summaries.items():
            if not isinstance(date, datetime.date):
                errors.append(f"Invalid date format in daily_summary: {date}")
        
        return errors
