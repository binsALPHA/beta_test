# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: ResearchCatalog
import json
from datetime import datetime

DATA_FILE = "research_catalog.json"


def load_catalog():
    if not os.path.exists(DATA_FILE):
        return {"studies": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_catalog(catalog):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)


def add_change_log(catalog, action, target_id, details):
    catalog.setdefault("change_log", []).append({
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "target_id": target_id,
        "details": details,
    })


def log_change(action, target_id, details):
    add_change_log(load_catalog(), action, target_id, details)
    save_catalog(load_catalog())
