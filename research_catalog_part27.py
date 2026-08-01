# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ResearchCatalog
def reset_demo_data(catalog, notes_db):
    """Сбрасывает каталог исследований до демо-данных."""
    demo_researches = [
        {
            "id": 1,
            "title": "Влияние сна на когнитивные способности",
            "source": "Journal of Neuroscience Research",
            "hypotheses": ["Сон улучшает память", "Недостаток сна снижает реакцию"],
            "notes": [
                {"author": "Ольга", "content": "Интересный пример из статьи"},
                {"author": "Алексей", "content": "Нужно проверить статистику"}
            ],
            "tags": ["сон", "память", "нейронауки"],
            "conclusions": ["Сон критически важен для обучения"]
        },
        {
            "id": 2,
            "title": "Эффективность интервального обучения (spaced repetition)",
            "source": "Applied Cognitive Psychology Journal",
            "hypotheses": [
                "Интервальное повторение эффективнее массового",
                "Длина интервала влияет на заучивание"
            ],
            "notes": [
                {"author": "Мария", "content": "Практический опыт использования"},
                {"author": "Иван", "content": "Сравнение с другими методами"}
            ],
            "tags": ["обучение", "spaced-repetition", "когнитивные-науки"],
            "conclusions": [
                "Интервальное повторение значительно повышает удержание информации"
            ]
        },
        {
            "id": 3,
            "title": "Связь микробиома и психического здоровья",
            "source": "Nature Microbiology Review",
            "hypotheses": [
                "Микрофлора кишечника влияет на настроение",
                "Диета изменяет состав микробиома"
            ],
            "notes": [
                {"author": "Дмитрий", "content": "Возможные механизмы влияния"},
                {"author": "Елена", "content": "Клинические наблюдения"}
            ],
            "tags": ["микробиом", "психическое-здоровье", "диета"],
            "conclusions": [
                "Микробиом тесно связан с депрессией и тревогой"
            ]
        }
    ]

    catalog.clear()
    for research in demo_researches:
        catalog.add(research)

    notes_db.clear()
