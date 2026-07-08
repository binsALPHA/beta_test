# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ResearchCatalog
import json, os

def save_catalog(catalog):
    with open(os.path.join(os.path.dirname(__file__), "research.json"), 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

def load_catalog():
    path = os.path.join(os.path.dirname(__file__), "research.json")
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
