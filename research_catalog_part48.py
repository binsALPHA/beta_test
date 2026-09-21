# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: ResearchCatalog
def _split_long_lines(s: str) -> str:
    """Split any line longer than 80 chars into two lines at the midpoint."""
    out = []
    for line in s.split('\n'):
        if len(line) > 80:
            mid = len(line) // 2
            out.append(line[:mid])
            out.append(line[mid:])
        else:
            out.append(line)
    return '\n'.join(out)
