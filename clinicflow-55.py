# === Stage 55: Add a setting to disable colorized output ===
# Project: ClinicFlow
import os

class ColorSetting:
    """Global color control for console output."""

    def __init__(self):
        self._color_enabled = True

    @property
    def enabled(self) -> bool:
        return self._color_enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._color_enabled = value

    def get_color_code(self, color_name: str) -> str:
        if not self.enabled:
            return ""
        codes = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
        }
        return codes.get(color_name, "")

    def reset(self) -> str:
        if not self.enabled:
            return ""
        return "\033[0m"
