# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: ResearchCatalog
def export_catalog_json(catalog):
    """Export the full catalog to a JSON file with proper formatting."""
    import json
    output_path = "research_catalog.json"
    json_data = {
        "title": catalog.get("title", "Research Catalog"),
        "researches": [
            {
                "id": r["id"],
                "title": r["title"],
                "sources": r.get("sources", []),
                "hypotheses": r.get("hypotheses", []),
                "notes": r.get("notes", []),
                "tags": r.get("tags", []),
                "conclusions": r.get("conclusions", []),
            }
            for r in catalog.get("researches", [])
        ]
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    print(f"Catalog exported to {output_path}")
