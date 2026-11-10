# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: ResearchCatalog
def import_from_text(self, path):
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split("|")]
            if len(parts) < 2:
                continue
            title = parts[0]
            source = parts[1] if len(parts) > 1 else ""
            records.append({"title": title, "source": source})
    for rec in records:
        self.add_record(**rec)
    return len(records)
