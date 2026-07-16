# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ResearchCatalog
def weekly_stats(self):
        """Возвращает статистику по неделям: для каждой недели — количество исследований,
        гипотез и заметок."""
        if not self.researches:
            return {}
        weeks = {}
        for r in self.researches:
            week_key = r.created_at.replace(day=1) + timedelta(weeks=r.created_at.day // 7)
            # Проще использовать isoformat для ключа недели
            week_start = r.created_at - timedelta(days=(r.created_at.weekday() + 1) % 7)
            week_key = week_start.isoformat()
            weeks[week_key] = {"researches": 0, "hypotheses": 0, "notes": 0}
            if isinstance(r, Research):
                weeks[week_key]["researches"] += 1
                for h in r.hypotheses:
                    weeks[week_key]["hypotheses"] += 1
                for n in r.notes:
                    weeks[week_key]["notes"] += 1
        return weeks
