# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ResearchCatalog
import json, sys

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект корень")
        
        # Валидация обязательных полей
        required_fields = ["researches", "tags"]
        for field in required_fields:
            if field not in data:
                print(f"Предупреждение: отсутствует поле {field}", file=sys.stderr)
        
        return data

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (замените эту строку на ваш источник данных):
initial_data = load_initial_data('{"researches": [], "tags": []}')
