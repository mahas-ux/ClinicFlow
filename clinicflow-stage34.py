# === Stage 34: Add support for multiple local user profiles ===
# Project: ClinicFlow
import os, json, hashlib, secrets


class ProfileManager:
    """Manages multiple local user profiles for ClinicFlow."""

    def __init__(self, data_dir):
        self.data_dir = data_dir

    def _profile_path(self, name):
        return os.path.join(self.data_dir, "profiles", f"{name}.json")

    def list_profiles(self):
        path = os.path.join(self.data_dir, "profiles")
        if not os.path.isdir(path):
            return []
        return [f.replace(".json", "") for f in sorted(os.listdir(path)) if f.endswith(".json")]

    def get_profile(self, name):
        with open(self._profile_path(name), "r") as f:
            return json.load(f)

    def save_profile(self, name, data):
        os.makedirs("profiles", exist_ok=True)
        with open(self._profile_path(name), "w") as f:
            json.dump(data, f, indent=2)

    def delete_profile(self, name):
        path = self._profile_path(name)
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    def create_anonymous_profile(self):
        name = f"anon_{secrets.token_hex(4)}"
        profile = {
            "name": name,
            "token": secrets.token_hex(16),
            "settings": {},
        }
        self.save_profile(name, profile)
        return name

    def verify_token(self, token):
        for p in self.list_profiles():
            try:
                prof = self.get_profile(p)
                if prof["token"] == token:
                    return p
            except Exception:
                continue
        return None
