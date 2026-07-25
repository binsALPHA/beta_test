# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ResearchCatalog
def check_overdue_reminders():
    """Проверяет напоминания, срок которых прошёл, и возвращает список просроченных."""
    overdue = []
    now = datetime.datetime.now()
    for reminder in reminders:
        if reminder['date'] is not None and reminder['date'] < now:
            overdue.append({**reminder, 'status': 'overdue'})
    return overdue

check_overdue_reminders()
