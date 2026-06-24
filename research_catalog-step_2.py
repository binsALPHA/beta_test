# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ResearchCatalog
class ValidationError(Exception): pass

def validate_source(source: dict) -> bool:
    if not source.get('url') or 'http' not in source['url']: return False
    if not source.get('title'): raise ValidationError("Source title is required")
    return True

def validate_hypothesis(hyp: str) -> bool:
    hyp = hyp.strip()
    if len(hyp) < 10 or len(hyp) > 500: raise ValidationError("Hypothesis length must be between 10 and 500 chars")
    return True

def validate_note(note: dict) -> bool:
    if not note.get('text'): raise ValidationError("Note text is required")
    if len(note['text']) > 2000: raise ValidationError("Note too long")
    return True

def validate_tag(tag: str) -> bool:
    tag = tag.lower().strip()
    if not tag or len(tag) < 1 or len(tag) > 30: raise ValidationError("Invalid tag format")
    if any(c in tag for c in [' ', '/', '\\']): raise ValidationError("Tag contains invalid characters")
    return True

def validate_conclusion(conc: dict) -> bool:
    if not conc.get('text'): raise ValidationError("Conclusion text is required")
    if len(conc['text']) > 1000: raise ValidationError("Conclusion too long")
    return True
