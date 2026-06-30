# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ResearchCatalog
def filter_records(status=None, category=None, tags=None):
    filtered = records.copy()
    if status is not None:
        filtered = [r for r in filtered if r.get('status') == status]
    if category is not None:
        filtered = [r for r in filtered if r.get('category') == category]
    if tags is not None:
        def has_any_tags(record, tag_list):
            record_tags = set(r.get('tags', []))
            return any(tag in record_tags for tag in tag_list)
        filtered = [r for r in filtered if has_any_tags(r, tags)]
    return filtered
