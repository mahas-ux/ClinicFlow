# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ClinicFlow
from datetime import date, timedelta


def parse_date_from_string(text):
    """Parse a date from various string formats and return a date object."""
    if isinstance(text, date):
        return text
    
    # Try common formats
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y%m%d"):
        try:
            return date.fromisoformat(text)
        except ValueError:
            continue
    
    raise ValueError(
        f"Unable to parse date from '{text}'. "
        "Please use format YYYY-MM-DD or MM/DD/YYYY."
    )


def add_business_days(current_date, days):
    """Add business days (Mon-Fri), skipping weekends."""
    result = current_date + timedelta(days=days)
    while result.weekday() >= 5:
        result += timedelta(days=1)
    return result
