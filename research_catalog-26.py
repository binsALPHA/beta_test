# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ResearchCatalog
def demo_quick_test():
    print("=== ResearchCatalog Demo ===")
    catalog = Catalog()
    
    source1 = Source(title="Nature Paper 2024", url="https://example.com/nature")
    source2 = Source(title="ArXiv Preprint", url="https://arxiv.org/example")
    catalog.add_source(source1)
    catalog.add_source(source2)

    note = Note(text="Interesting findings on neural networks.", tags=["AI", "research"])
    hypothesis = Hypothesis(statement="LLMs improve with larger datasets.")
    conclusion = Conclusion(summary="Confirmed by multiple experiments.")
    
    research = Research(
        title="LLM Scaling Study",
        sources=[source1, source2],
        notes={note},
        hypotheses={hypothesis},
        conclusions={conclusion}
    )
    catalog.add_research(research)

    print(f"Sources: {catalog.sources}")
    print(f"Research count: {len(catalog.researches)}")
    for r in catalog.researches:
        print(f"  Title: {r.title}, Notes: {len(r.notes)}, Hypotheses: {len(r.hypotheses)}")
