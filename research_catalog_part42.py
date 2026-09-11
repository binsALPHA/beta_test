# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ResearchCatalog
ANSI_RESET = "\033[0m"
ANSI_RED = "\033[31m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_CYAN = "\033[36m"
ANSI_BLUE = "\033[34m"
ANSI_BOLD = "\033[1m"


def _supports_color():
    try:
        import os
        return os.name != "nt" or os.environ.get("FORCE_COLOR")
    except Exception:
        return True


def _colorize(text, color):
    if _supports_color():
        return f"{color}{text}{ANSI_RESET}"
    return text


def print_research_catalog(research_catalog):
    print(_colorize("╔════════════════════════════════════════════╗", ANSI_CYAN))
    print(_colorize("║         📚 Research Catalog 📚              ║", ANSI_CYAN))
    print(_colorize("╚════════════════════════════════════════════╝", ANSI_CYAN))
    print()

    for research in research_catalog:
        print(_colorize(f"{'─' * 60}", ANSI_BLUE))
        print(_colorize(f"🔬 Исследование: {research.name}", ANSI_BOLD))
        print(_colorize(f"   Автор: {research.author}", ANSI_GREEN))
        print(_colorize(f"   Дата: {research.date}", ANSI_GREEN))
        print(_colorize(f"   Статус: {research.status}", ANSI_GREEN))
        print()

        if research.hypothesis:
            print(_colorize(f"   🎯 Гипотеза: {research.hypothesis}", ANSI_CYAN))
        if research.sources:
            print(_colorize(f"   📖 Источники:", ANSI_CYAN))
            for source in research.sources:
                print(_colorize(f"      - {source}", ANSI_CYAN))
        if research.tags:
            print(_colorize(f"   🏷️  Теги: {', '.join(research.tags)}", ANSI_YELLOW))
        if research.notes:
            print(_colorize(f"   💡 Заметки: {research.notes}", ANSI_YELLOW))
        if research.conclusion:
            print(_colorize(f"   ✅ Вывод: {research.conclusion}", ANSI_GREEN))

        print()

    print(_colorize(f"{'─' * 60}", ANSI_BLUE))
    print(_colorize(f"   Всего исследований: {len(research_catalog)}", ANSI_CYAN))
    print(_colorize(f"{'─' * 60}", ANSI_BLUE))
