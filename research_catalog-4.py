# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ResearchCatalog
def edit_research_record(record_id, updates):
    if record_id not in research_catalog:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    existing = research_catalog[record_id]
    
    for key, value in updates.items():
        if hasattr(existing[key], 'append') and isinstance(value, list):
            existing[key].extend(value)
        else:
            existing[key] = value
            
    print(f"Запись {record_id} успешно обновлена.")
    return True

# Пример вызова: edit_research_record(1, {"tags": ["новое_тег"], "notes": ["новая заметка"]})
