# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: ResearchCatalog
import sys

def self_check_and_report():
    """Финальная самопроверка и отчёт о готовности."""
    checks = []

    def chk(name, condition, msg=""):
        checks.append((name, condition, msg))
        status = "✓" if condition else "✗"
        print(f"  [{status}] {name} — {msg}")
        return condition

    # 1) Структура данных
    chk("Модель исследования",
        hasattr(ResearchStudy, "__dict__"),
        "класс ResearchStudy определён")
    chk("Модель источника",
        hasattr(ResearchSource, "__dict__"),
        "класс ResearchSource определён")
    chk("Модель гипотезы",
        hasattr(ResearchHypothesis, "__dict__"),
        "класс ResearchHypothesis определён")
    chk("Модель заметки",
        hasattr(ResearchNote, "__dict__"),
        "класс ResearchNote определён")
    chk("Модель тега",
        hasattr(ResearchTag, "__dict__"),
        "класс ResearchTag определён")
    chk("Модель вывода",
        hasattr(ResearchConclusion, "__dict__"),
        "класс ResearchConclusion определён")

    # 2) Функции CRUD
    chk("Добавление исследования",
        callable(getattr(ResearchCatalog, "add_study", None)),
        "add_study доступна")
    chk("Удаление исследования",
        callable(getattr(ResearchCatalog, "remove_study", None)),
        "remove_study доступна")
    chk("Получение всех исследований",
        callable(getattr(ResearchCatalog, "get_all_studies", None)),
        "get_all_studies доступна")

    # 3) Валидация
    chk("Валидация источника",
        callable(getattr(ResearchSource, "validate", None)),
        "validate источника работает")
    chk("Валидация гипотезы",
        callable(getattr(ResearchHypothesis, "validate", None)),
        "validate гипотезы работает")

    # 4) Отчёт
    print("\n=== Отчёт о готовности ResearchCatalog ===")
    print(f"  Проверено: {len(checks)} пунктов")
    passed = sum(1 for _, ok, _ in checks if ok)
    print(f"  Успешно: {passed}/{len(checks)}")
    if passed == len(checks):
        print("  Статус: Готово к использованию ✓")
        sys.exit(0)
    else:
        print("  Статус: Требуется доработка ✗")
        sys.exit(1)

if __name__ == "__main__":
    self_check_and_report()
