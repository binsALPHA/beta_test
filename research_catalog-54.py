# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: ResearchCatalog
class Favorites:
    def __init__(self, catalog):
        self.catalog = catalog
        self.favorites = set()

    def add_favorite(self, record_id):
        self.favorites.add(record_id)

    def remove_favorite(self, record_id):
        self.favorites.discard(record_id)

    def is_favorite(self, record_id):
        return record_id in self.favorites

    def toggle_favorite(self, record_id):
        if self.is_favorite(record_id):
            self.remove_favorite(record_id)
        else:
            self.add_favorite(record_id)

    def get_favorite_ids(self):
        return sorted(self.favorites)

    def show(self):
        if not self.favorites:
            print("Избранных записей нет.")
            return
        print("=== Избранные записи ===")
        for rid in self.get_favorite_ids():
            record = self.catalog.get_record(rid)
            if record:
                print(f"#{rid} [{record.get('title', 'без названия')}]")
