# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ClinicFlow
class CommandDispatcher:
    def __init__(self, handlers):
        self._handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text_command):
        if not isinstance(text_command, str) or not text_command.strip():
            return None
        command_map = self._handlers.get(text_command.lower())
        if callable(command_map):
            return command_map()
        return None
