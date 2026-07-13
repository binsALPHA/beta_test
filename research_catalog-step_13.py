# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ResearchCatalog
def search(catalog, query: str):
    q = query.lower().split()
    results = []
    for idx, entry in enumerate(catalog):
        if any(query_tok not in entry['title'].lower() and query_tok not in entry.get('tags', []) for query_tok in q):
            continue
        if all(any(query_tok in field.lower() for field in (entry['title'], *entry.get('tags', []), entry.get('conclusion', ''))) for query_tok in q):
            results.append(entry)
    return results

def find_entry(catalog, title: str):
    return next((e for e in catalog if e['title'].lower() == title.lower()), None)

def filter_by_tags(catalog, tags):
    return [e for e in catalog if any(t in e.get('tags', []) for t in tags)]

def find_notes_for(entry_title: str, notes_list: list):
    return [n for n in notes_list if entry_title.lower() in n['title'].lower()]
