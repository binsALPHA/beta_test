# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ResearchCatalog
def undo(self):
        """Откат последнего добавленного объекта.

        Сохраняет откат в стек undo-записей:
          - id объекта (для удаления)
          - его тип
          - его данные в момент добавления

        Для удаления объектов (Research, Source, Hypothesis,
        Note, Tag, Conclusion) — удаляет из соответствующей коллекции
        и из undo_stack.
        """
        if not self.undo_stack:
            raise RuntimeError("Нет откатываемых действий")

        record = self.undo_stack.pop()
        obj_id = record["id"]
        obj_type = record["type"]

        if obj_type == "Research":
            self.researches.remove(obj_id)
        elif obj_type == "Source":
            self.sources.remove(obj_id)
        elif obj_type == "Hypothesis":
            self.hypotheses.remove(obj_id)
        elif obj_type == "Note":
            self.notes.remove(obj_id)
        elif obj_type == "Tag":
            self.tags.remove(obj_id)
        elif obj_type == "Conclusion":
            self.conclusions.remove(obj_id)
        else:
            raise ValueError(f"Неизвестный тип для отката: {obj_type}")
