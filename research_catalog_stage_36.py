# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ResearchCatalog
def check_and_fix_data(data):
    """Проверяет целостность данных и пытается автоматически исправить простые проблемы."""
    fixed = False
    for i in range(len(data)):
        item = data[i]
        if not isinstance(item, dict):
            data[i] = {}
            fixed = True
            continue
        if 'id' not in item:
            item['id'] = i
            fixed = True
        if 'source' in item and item['source'] and not isinstance(item['source'], dict):
            item['source'] = {'url': str(item['source']), 'title': ''}
            fixed = True
        if 'hypothesis' in item and item['hypothesis'] and not isinstance(item['hypothesis'], str):
            item['hypothesis'] = str(item['hypothesis'])
            fixed = True
        if 'tags' in item and item['tags'] and not isinstance(item['tags'], list):
            item['tags'] = [str(item['tags'])]
            fixed = True
        if 'notes' in item and item['notes'] and not isinstance(item['notes'], str):
            item['notes'] = str(item['notes'])
            fixed = True
        if 'conclusions' in item and item['conclusions'] and not isinstance(item['conclusions'], list):
            item['conclusions'] = [str(item['conclusions'])]
            fixed = True
    if fixed:
        return data, "Исправлено {} проблем".format(fixed)
    return data, "Данные целостны"
