# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: ResearchCatalog
def demo():
    print("=" * 60)
    print("  ResearchCatalog — демонстрация пользовательского сценария")
    print("=" * 60)

    # Создаём исследовательские данные
    studies = [
        {
            "id": "study-001",
            "title": "Влияние сна на когнитивные способности",
            "sources": ["Sleep & Cognition, 2023", "Nature Neuroscience, 2024"],
            "hypotheses": [
                "Гипотеза: 8 часов сна улучшает память на 30%",
                "Гипотеза: Недосып снижает скорость реакции на 20%"
            ],
            "tags": ["сон", "когнитивные", "здоровье"],
            "notes": "Интересные результаты, но нужна репликация",
            "conclusions": "Сон критически важен для когнитивных функций"
        },
        {
            "id": "study-002",
            "title": "Механизмы старения клеток",
            "sources": ["Cell, 2022", "Science, 2023"],
            "hypotheses": [
                "Гипотеза: Теломеры укорачиваются с возрастом",
                "Гипотеза: Окислительный стресс ускоряет старение"
            ],
            "tags": ["старение", "клетки", "биология"],
            "notes": "Перспективная область для терапии",
            "conclusions": "Старение связано с укорочением теломер и окислительным стрессом"
        },
        {
            "id": "study-003",
            "title": "Эффективность новых вакцин",
            "sources": ["Lancet, 2023", "NEJM, 2024"],
            "hypotheses": [
                "Гипотеза: mRNA-вакцинация обеспечивает иммунитет на 2 года",
                "Гипотеза: Комбинированные вакцины эффективнее моновалентных"
            ],
            "tags": ["вакцинация", "иммунитет", "здоровье"],
            "notes": "Важно отслеживать побочные эффекты",
            "conclusions": "Новые вакцины показывают высокую эффективность"
        }
    ]

    # Отображаем каталог исследований
    print("\n📊 Каталог исследований:")
    print("-" * 40)
    for study in studies:
        print(f"  [{study['id']}] {study['title']}")
        print(f"      Источники: {', '.join(study['sources'])}")
        print(f"      Гипотезы: {len(study['hypotheses'])} шт.")
        print(f"      Теги: {', '.join(study['tags'])}")
        print(f"      Выводы: {study['conclusions']}")
        print()

    # Статистика
    total_studies = len(studies)
    total_hypotheses = sum(len(s["hypotheses"]) for s in studies)
    total_tags = sum(len(s["tags"]) for s in studies)
    total_sources = sum(len(s["sources"]) for s in studies)

    print("=" * 60)
    print("  Статистика каталога:")
    print(f"  Всего исследований: {total_studies}")
    print(f"  Всего гипотез:      {total_hypotheses}")
    print(f"  Всего тегов:        {total_tags}")
    print(f"  Всего источников:   {total_sources}")
    print("=" * 60)
    print("\n✅ Демонстрация завершена!")
