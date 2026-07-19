# === Stage 17: Добавь группировку записей по категориям ===
# Project: ResearchCatalog
def group_by_category(records):
    """Группирует записи по категории (типу: исследование, гипотеза, заметка, вывод)."""
    categories = {}
    for record in records:
        cat = record.get("category", "other")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(record)
    return categories
