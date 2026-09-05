# === Stage 39: Добавь документационную строку с описанием сценариев использования ===
# Project: ResearchCatalog
def demo_scenarios(self):
        """Демонстрирует типичные сценарии использования каталога."""
        print("=== Сценарий 1: Поиск исследований по ключевому слову ===")
        keyword = "machine learning"
        results = self.search(keyword)
        for r in results[:3]:
            print(f"  - {r['title']} (теги: {r['tags']})")

        print("\n=== Сценарий 2: Фильтрация по дате и статусу ===")
        recent_active = self.filter(date_from="2024-01-01", status="active")
        print(f"  Активных исследований с 2024: {len(recent_active)}")

        print("\n=== Сценарий 3: Группировка по тегам ===")
        grouped = self.group_by_tag()
        for tag, items in grouped.items():
            print(f"  Тег '{tag}': {len(items)} исследований")

        print("\n=== Сценарий 4: Экспорт в JSON ===")
        export_path = "catalog_export.json"
        self.export_to_json(export_path)
        print(f"  Экспорт сохранён в {export_path}")

        print("\n=== Сценарий 5: Подсчёт статистики ===")
        stats = self.get_statistics()
        print(f"  Всего: {stats['total']}, по тегам: {len(stats['tags'])}")
