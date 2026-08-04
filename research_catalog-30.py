# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ResearchCatalog
_profiles = {}


def register_profile(name: str, email: str = "") -> None:
    _profiles[name] = {"name": name, "email": email}


def get_current_profile() -> dict | None:
    return _profiles.get("current")


def switch_profile(profile_name: str) -> bool:
    if profile_name not in _profiles or _profiles[profile_name].get("active"):
        return False
    for p in _profiles.values():
        p["active"] = False
    _profiles[profile_name]["active"] = True
    return True


def list_profiles() -> list:
    return [p for p in _profiles.values() if not p.get("active")]


def active_profile() -> dict | None:
    for p in _profiles.values():
        if p.get("active"):
            return p
    return None
