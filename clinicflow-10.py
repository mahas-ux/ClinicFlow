# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ClinicFlow
class SearchFilter:
    def __init__(self, data):
        self.data = data

    def search(self, query):
        if not query.strip():
            return list(self.data)
        q = query.lower()
        results = []
        for item in self.data:
            fields_to_check = [item.get('patient_name', ''), item.get('doctor_name', ''), 
                              item.get('visit_type', ''), item.get('notes', '')]
            if any(q in str(f).lower() for f in fields_to_check):
                results.append(item)
        return results

    def get_search_stats(self, query):
        count = len(self.search(query))
        return {'query': query, 'matches': count}
