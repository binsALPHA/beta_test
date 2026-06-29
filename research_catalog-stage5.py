# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ResearchCatalog
def delete_record(record_id: str, record_type: str) -> bool:
    if not record_id or not record_type:
        print(f"Ошибка: отсутствуют идентификаторы для удаления типа '{record_type}'")
        return False
    
    try:
        key = f"{record_type}:{record_id}"
        records[key] = None
        print(f"Запись {key} успешно удалена.")
        return True
    except KeyError as e:
        missing_key = str(e)
        print(f"Ошибка: запись '{missing_key}' не найдена в каталоге.")
        return False
