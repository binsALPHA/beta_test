# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ResearchCatalog
def run_cli():
    from rich.console import Console
    console = Console()
    print("ResearchCatalog CLI v0.8")
    while True:
        try:
            cmd = input("\nКоманда (1-5, q=выход): ").strip().lower()
            if not cmd: continue
            elif cmd == "q": break
            elif cmd in ("1", "2"): print("Функция 1/2 скоро будет доступна")
            else: console.print(f"[red]Неизвестная команда: {cmd}[/red]")
        except KeyboardInterrupt:
            print("\nВыход из CLI.")
            break
