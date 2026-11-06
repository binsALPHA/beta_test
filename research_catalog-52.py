# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: ResearchCatalog
def export_report():
    print("=" * 60)
    print("ResearchCatalog — краткий отчёт")
    print("=" * 60)
    for r in researches:
        print(f"\nИсследование: {r.title}")
        print(f"  Автор: {r.author}")
        print(f"  Статус: {r.status}")
        for src in r.sources:
            print(f"  Источник: {src.title}")
        for hyp in r.hypotheses:
            print(f"  Гипотеза: {hyp.text}")
        for tag in r.tags:
            print(f"  Тег: #{tag}")
        for note in r.notes:
            print(f"  Заметка: {note.text}")
        print(f"  Вывод: {r.conclusion}")
    print("\n" + "=" * 60)
