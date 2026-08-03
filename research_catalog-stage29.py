# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: ResearchCatalog
APP_CONFIG = {
    "app_name": "ResearchCatalog",
    "version": 1,
    "storage_path": "./catalog_data/",
    "default_tags": ["research", "science"],
    "max_note_length": 5000,
    "display_language": "ru",
}

def get_config():
    return APP_CONFIG.copy()

config = get_config()
