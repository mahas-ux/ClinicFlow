# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ClinicFlow
import unittest
from clinicflow.core.models import Visit, Priority
from clinicflow.core.queue import Queue


class TestQueueEdgeCases(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_delete_nonexistent_visit(self):
        visit = Visit(name="A", priority=Priority.LOW)
        with self.assertRaises(ValueError):
            self.q.delete(visit)

    def test_update_preserves_existing_visits(self):
        v1 = Visit(name="V1", priority=Priority.HIGH)
        v2 = Visit(name="V2", priority=Priority.MEDIUM)
        self.q.add(v1)
        self.q.add(v2)
        updated = self.q.update(Visit(name="V1-Updated", priority=Priority.HIGH))
        self.assertEqual(updated, [v2])

    def test_update_empty_queue(self):
        with self.assertRaises(ValueError):
            self.q.update(Visit(name="X", priority=Priority.LOW))


if __name__ == "__main__":
    unittest.main()
