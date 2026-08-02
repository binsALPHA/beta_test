# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ResearchCatalog
def project_metrics():
    """Count key research metrics and print summary."""
    sources = len([r for r in catalog if hasattr(r, 'sources')])
    hypotheses = sum(len(getattr(r, '_hypotheses', [])) for r in catalog)
    notes_count = sum(len(getattr(r, '_notes', [])) for r in catalog)
    tags_set = set()
    conclusions_count = 0
    for r in catalog:
        if hasattr(r, 'tags'):
            tags_set.update(r.tags)
        if hasattr(r, 'conclusion') and getattr(r, 'conclusion', None):
            conclusions_count += 1

    print(f"Total sources: {sources}")
    print(f"Hypotheses: {hypotheses}")
    print(f"Notes: {notes_count}")
    print(f"Tags ({len(tags_set)}): {sorted(tags_set)}")
    print(f"Conclusions: {conclusions_count}")

project_metrics()
