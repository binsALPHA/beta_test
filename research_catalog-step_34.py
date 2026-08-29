# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ResearchCatalog
TEMPLATES = {
    'paper': {
        'title': '',
        'authors': [],
        'year': '',
        'source': '',
        'hypothesis': '',
        'notes': '',
        'tags': [],
        'conclusion': '',
    },
    'review': {
        'title': '',
        'authors': [],
        'year': '',
        'source': '',
        'hypothesis': '',
        'notes': '',
        'tags': [],
        'conclusion': '',
        'summary': '',
    },
    'quick': {
        'title': '',
        'source': '',
        'notes': '',
        'tags': [],
    },
}

def create_from_template(template_name, existing_records=None):
    if existing_records is None:
        existing_records = []
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: {template_name}. Available: {list(TEMPLATES.keys())}")
    new_record = {k: v for k, v in TEMPLATES[template_name].items()}
    existing_records.append(new_record)
    return existing_records, new_record
