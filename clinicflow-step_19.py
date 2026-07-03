# === Stage 19: Add undo support for the last simple mutation ===
# Project: ClinicFlow
class UndoManager:
    def __init__(self, max_history=10):
        self._history = []
        self._max_size = max_history

    def record(self, action_name, state_snapshot):
        if len(self._history) >= self._max_size:
            self._history.pop(0)
        self._history.append((action_name, state_snapshot))

    def undo_last(self):
        if not self._history:
            return None
        last_action, snapshot = self._history.pop()
        # Apply restoration logic here based on 'last_action' and 'snapshot'
        return last_action
