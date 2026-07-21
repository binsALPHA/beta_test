# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ResearchCatalog
def archive_records(records, target_dir="archive"):
    archived = []
    for r in records:
        if getattr(r, "status", None) == "completed" or (getattr(r, "tags", []) and any(t.startswith("old") for t in r.tags)):
            r.status = "archived"
            r._original_path = r.get("_path", "")
            archived.append(r)
    return archived
