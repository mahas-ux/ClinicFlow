# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ClinicFlow
# ClinicFlow - Settings Module (Step 33)
# Provides a global settings dictionary and functions to update settings.


def get_settings():
    """Retrieve the current clinic settings."""
    return {
        "clinic_name": "Community Health Center",
        "max_wait_time_min": 60,
        "priority_levels": ["critical", "high", "normal", "low"],
        "staff_handoff_enabled": True,
        "daily_summary_hour": 18,
        "notification_sound": True,
    }


def update_settings(settings_dict):
    """Update specific settings and return the updated dictionary."""
    current = get_settings()
    current.update(settings_dict)
    if not current["priority_levels"]:
        current["priority_levels"] = ["critical", "high", "normal", "low"]
    return current


def reset_settings():
    """Reset all settings to default values."""
    return {
        "clinic_name": "Community Health Center",
        "max_wait_time_min": 60,
        "priority_levels": ["critical", "high", "normal", "low"],
        "staff_handoff_enabled": True,
        "daily_summary_hour": 18,
        "notification_sound": True,
    }


def validate_settings(settings_dict):
    """Validate that provided settings are valid and return errors if any."""
    errors = []
    if not isinstance(settings_dict.get("max_wait_time_min"), int) or settings_dict["max_wait_time_min"] < 0:
        errors.append("max_wait_time_min must be a non-negative integer")
    if "priority_levels" in settings_dict and not isinstance(settings_dict["priority_levels"], list):
        errors.append("priority_levels must be a list")
    return errors


if __name__ == "__main__":
    print("Current Settings:", get_settings())
    updated = update_settings({"clinic_name": "City Clinic"})
    print("Updated Settings:", updated)
    reset = reset_settings()
    print("Reset Settings:", reset)
