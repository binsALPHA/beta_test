# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ResearchCatalog
def generate_summary(catalog):
    """Создать краткую сводку по текущим данным каталога."""
    lines = ["=== Сводка ResearchCatalog ==="]
    
    total_researches = len(catalog.get("researches", []))
    total_sources = len(catalog.get("sources", []))
    total_hypotheses = sum(len(r.get("hypotheses", [])) for r in catalog.get("researches", []))
    total_notes = sum(len(r.get("notes", [])) for r in catalog.get("researches", []))
    total_tags = set()
    total_conclusions = 0
    
    for research in catalog.get("researches", []):
        tags = research.get("tags", [])
        if isinstance(tags, list):
            total_tags.update(tags)
        else:
            total_tags.add(tags)
        
        conclusions = research.get("conclusion", "")
        if isinstance(conclusions, list):
            total_conclusions += len(conclusions)
        elif isinstance(conclusions, str):
            total_conclusions += 1
    
    lines.append(f"Исследований: {total_researches}")
    lines.append(f"Источников: {total_sources}")
    lines.append(f"Гипотез всего: {total_hypotheses}")
    lines.append(f"Заметок всего: {total_notes}")
    
    if total_tags:
        sorted_tags = sorted(total_tags)
        tag_str = ", ".join(sorted_tags[:20])  # первые 20 тегов
        lines.append(f"Теги ({len(total_tags)}): {tag_str}")
    
    lines.append(f"Выводов всего: {total_conclusions}")
    
    if total_researches > 0 and "researches" in catalog:
        latest = catalog["researches"][-1]
        title = latest.get("title", "Без заголовка")[:50]
        lines.append(f"\nПоследнее исследование: {title}")
    
    return "\n".join(lines)
