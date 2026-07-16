# === Stage 50: Add unit tests for import and export behavior ===
# Project: ClinicFlow
import unittest, os
from clinicflow.core import Visit, QueueConfig
from clinicflow.io.export import Exporter

class TestExport(unittest.TestCase):
    def test_export_csv(self):
        q = QueueConfig("TestQueue", 30)
        v1 = Visit("V001","John Doe","fever",priority=2)
        v2 = Visit("V002","Jane Smith","cough",priority=1)
        q.add(v1); q.add(v2)
        exporter = Exporter(q, "/tmp/test_export")
        csv_path = exporter.export_csv()
        self.assertTrue(os.path.exists(csv_path))
        with open(csv_path) as f:
            lines = [l.strip() for l in f if l.strip()]
        self.assertEqual(lines[0], "visit_id,name,symptom,priority,arrival_time")
        self.assertIn("V001", lines[2])

    def test_export_json(self):
        q = QueueConfig("TestQueue", 30)
        v1 = Visit("V001","John Doe","fever",priority=2)
        q.add(v1)
        exporter = Exporter(q, "/tmp/test_export")
        json_path = exporter.export_json()
        self.assertTrue(os.path.exists(json_path))

    def test_import_csv(self):
        csv_content = "visit_id,name,symptom,priority\nV003,Alice,headache,1"
        with open("/tmp/test_import.csv","w") as f: f.write(csv_content)
        exporter = Exporter(None,"/tmp/test_import")
        visits = exporter.import_csv("/tmp/test_import.csv")
        self.assertEqual(len(visits), 1)
        self.assertEqual(visits[0].name, "Alice")

if __name__ == "__main__": unittest.main()
