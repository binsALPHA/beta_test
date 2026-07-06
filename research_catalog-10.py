# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ResearchCatalog
def export_to_json():
    """Export the current state of the ResearchCatalog to a JSON string."""
    import json
    
    catalog = {
        "sources": sources,
        "hypotheses": hypotheses,
        "notes": notes,
        "tags": tags,
        "results": results
    }
    
    return json.dumps(catalog, indent=2)

# Example usage:
# json_string = export_to_json()
# print(json_string)
