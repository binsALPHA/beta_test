# === Stage 20: Добавь восстановление записей из архива ===
# Project: ResearchCatalog
def load_from_archive(archive_path):
    """Restores research records from a JSON archive file."""
    import json
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return [data]
        print(f"Unexpected archive format: {type(data)}")
        return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"[Archive] Failed to load '{archive_path}': {e}")
        return []
