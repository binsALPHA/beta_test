# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ResearchCatalog
import json, os, uuid
from dataclasses import asdict, field
from typing import List, Optional

class ResearchItem:
    def __init__(self, title: str, hypothesis: str = "", tags: List[str] = None):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.hypothesis = hypothesis
        self.tags = tags or []
        self.sources: List[dict] = []
        self.notes: List[dict] = []
        self.conclusions: List[str] = []

    def add_source(self, url: str, author: Optional[str] = None):
        self.sources.append({"url": url, "author": author})

    def add_note(self, text: str, context: Optional[str] = None):
        self.notes.append({"text": text, "context": context})

    def conclude(self, conclusion: str):
        self.conclusions.append(conclusion)

def load_or_create_db(path="research_catalog.db"):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"items": []}

def save_db(data, path="research_catalog.db"):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# --- Demo Data & Entry Point ---
if __name__ == "__main__":
    db = load_or_create_db()
    
    # Create demo items
    item1 = ResearchItem(
        title="Влияние сна на когнитивные функции",
        hypothesis="Хронический недосып снижает скорость обработки информации.",
        tags=["сон", "когнитология"]
    )
    item1.add_source("https://www.sleepfoundation.org/sleep-and-cognition")
    item1.add_note("Эксперимент с 4-часовым циклом сна показал падение на 20%.")
    item1.conclude("Необходимо нормализовать режим сна для рабочих задач.")

    db["items"].append(asdict(item1))
    
    # Add another simple item
    item2 = ResearchItem(title="Эффективность удаленной работы", tags=["работа"])
    db["items"].append(asdict(item2))

    save_db(db)
    print(f"Инициализация завершена. Записано {len(db['items'])} исследований.")
