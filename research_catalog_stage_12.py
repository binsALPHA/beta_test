# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: ResearchCatalog
import json, os


def load_json_data(filepath):
    """Загружает данные из JSON-файла с обработкой ошибок."""
    if not filepath or not os.path.exists(filepath):
        print(f"[WARN] Файл не найден: {filepath}")
        return []
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            data = [data]
        print(f"[INFO] Загружено записей из файла: {len(data)}")
        return data
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"[ERROR] Ошибка парсинга JSON: {e}")
        return []
