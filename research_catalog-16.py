# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ResearchCatalog
def monthly_stats(catalog):
    """Return a dict of month-year -> list of studies."""
    stats = {}
    for study in catalog:
        if not hasattr(study, 'date') or not study.date:
            continue
        key = study.date.strftime('%Y-%m')
        stats.setdefault(key, []).append(study)
    return stats

def print_monthly_stats(stats):
    """Pretty-print the monthly statistics."""
    for month in sorted(stats):
        studies = stats[month]
        print(f"{month}: {len(studies)} study{'ies' if len(studies) != 1 else ''}")
