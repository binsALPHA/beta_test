# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ResearchCatalog
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(item):
        val = item.get(key)
        if isinstance(val, str):
            try: int(val); return (0, val)
            except ValueError: return (1, '')
        elif callable(getattr(item, key, None)):
            return getattr(item, key)
        return 0
    sorted_records = sorted(records, key=get_sort_key, reverse=reverse)
    if key == 'priority':
        priority_map = {'high': -2, 'medium': -1, 'low': 0}
        def get_priority_key(item):
            p = item.get('priority', 'medium')
            return (priority_map.get(p.lower(), 0), item.get('date', ''), item.get('title', ''))
        sorted_records = sorted(records, key=get_priority_key)
    elif key == 'name':
        sorted_records = sorted(records, key=lambda x: (x.get('title') or '').lower())
    return sorted_records
