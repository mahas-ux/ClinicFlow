# === Stage 46: Add a schema version field and migration helper ===
# Project: ClinicFlow
SCHEMA_VERSION = 5


def migrate_to(version):
    """Apply schema migrations up to the target version."""
    if version < SCHEMA_VERSION:
        # Migration v4 -> v5: introduce `schema_version` column on Visit
        print(f"Migration {version} -> {SCHEMA_VERSION}: added schema_version field.")
