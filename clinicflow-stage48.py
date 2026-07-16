# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ClinicFlow
import unittest


class TestVisit(unittest.TestCase):
    def test_creation(self):
        from clinicflow.models import Visit
        v = Visit(visit_id="v1", patient_name="Alice", priority=3, notes="Mild flu")
        self.assertEqual(v.visit_id, "v1")
        self.assertEqual(v.patient_name, "Alice")

    def test_validation(self):
        from clinicflow.models import Visit
        with self.assertRaises(ValueError):
            Visit(visit_id="", patient_name="Bob", priority=3)


class TestPriority(unittest.TestCase):
    def test_levels(self):
        from clinicflow.enums import Priority
        self.assertEqual(Priority.URGENT.value, 1)
        self.assertEqual(Priority.NORMAL.value, 2)
        self.assertEqual(Priority.LOW.value, 3)

    def test_sorting(self):
        from clinicflow.enums import Priority
        order = sorted([Priority.LOW, Priority.URGENT, Priority.NORMAL], key=lambda p: p.value)
        self.assertEqual(order, [Priority.URGENT, Priority.NORMAL, Priority.LOW])


if __name__ == "__main__":
    unittest.main()
