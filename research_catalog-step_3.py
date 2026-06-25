# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ResearchCatalog
class ResearchCatalog:
    def __init__(self):
        self.records = []

    def add_record(self, title: str, source: str, hypothesis: str | None = None, 
                    notes: list[str] | None = None, tags: list[str] | None = None, conclusion: str | None = None) -> dict:
        record = {
            "id": len(self.records) + 1,
            "title": title,
            "source": source,
            "hypothesis": hypothesis,
            "notes": notes or [],
            "tags": tags or [],
            "conclusion": conclusion
        }
        self.records.append(record)
        return record

    def get_all(self) -> list[dict]:
        return self.records.copy()
