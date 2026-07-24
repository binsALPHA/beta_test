# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ResearchCatalog
class Reminder:
    def __init__(self, title, date, note=""):
        self.title = title
        self.date = date
        self.note = note
        self.done = False

    def is_overdue(self):
        return datetime.now() > datetime.strptime(self.date, "%Y-%m-%d")

    def __str__(self):
        status = "⚠️  Просрочено" if self.is_overdue() else "✅"
        return f"{status} {self.title} ({self.date}) — {self.note}"
