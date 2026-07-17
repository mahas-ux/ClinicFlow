# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ClinicFlow
import unittest
from clinicflow.models import Visit, WaitingRoom
from clinicflow.services.search import find_by_patient, filter_waiting_room


class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.patient = "Alice"
        self.visit1 = Visit(patient=self.patient, priority="high", room_id=5)
        self.visit2 = Visit(patient="Bob", priority="low", room_id=7)
        self.room = WaitingRoom(id=5)

    def test_find_by_patient_returns_matching_visits(self):
        results = find_by_patient(visits=[self.visit1, self.visit2], patient=self.patient)
        self.assertEqual(len(results), 1)
        self.assertIs(results[0], self.visit1)

    def test_find_by_patient_returns_empty_for_missing(self):
        results = find_by_patient(visits=[self.visit1], patient="Charlie")
        self.assertEqual(results, [])

    def test_filter_waiting_room_keeps_visits_in_same_room(self):
        results = filter_waiting_room([self.visit1, self.visit2], room=self.room)
        self.assertTrue(all(v.room_id == 5 for v in results))


if __name__ == "__main__":
    unittest.main()
