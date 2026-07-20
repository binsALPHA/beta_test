# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ResearchCatalog
def add_tag(tag: str) -> None:
    tag = tag.strip().lower()
    if not tag: raise ValueError("Tag cannot be empty")
    tags_set.add(tag)

def remove_tag(tag: str) -> bool:
    tag = tag.strip().lower()
    if not tag: return False
    removed = tags_set.discard(tag)
    return bool(removed)
