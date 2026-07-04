# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ClinicFlow
class FavoriteManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                visit_id INTEGER UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db.commit()

    def add_favorite(self, visit_id):
        try:
            self.cursor.execute('INSERT INTO favorites (visit_id) VALUES (?)', (visit_id,))
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def remove_favorite(self, visit_id):
        self.cursor.execute('DELETE FROM favorites WHERE visit_id = ?', (visit_id,))
        self.db.commit()
        return self.cursor.rowcount > 0

    def is_favorited(self, visit_id):
        self.cursor.execute('SELECT COUNT(*) FROM favorites WHERE visit_id = ?', (visit_id,))
        return self.cursor.fetchone()[0] > 0

    def get_favorite_visits(self, limit=10):
        self.cursor.execute('''
            SELECT v.id, v.patient_name, v.priority, v.status 
            FROM visits v
            JOIN favorites f ON v.id = f.visit_id
            ORDER BY f.created_at DESC
            LIMIT ?
        ''', (limit,))
        return self.cursor.fetchall()

    def close(self):
        self.db.close()
