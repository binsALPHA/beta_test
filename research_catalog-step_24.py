# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ResearchCatalog
def print_record(record):
    """Compact single-record view with details."""
    print("\n" + "=" * 50)
    print(f"[ID]      {record.id}")
    print(f"[Title]   {record.title or '(untitled)'}")
    print("-" * 30)
    
    if record.hypothesis:
        print(f"  Hypothesis : {record.hypothesis}")
    if record.conclusion:
        print(f"  Conclusion  : {record.conclusion}")
    
    for note in (record.notes or []):
        print(f"  Note       : {note.text}")
        if note.metadata:
            for k, v in note.metadata.items():
                print(f"              ({k}: {v})")
    
    print("-" * 30)
    for src in (record.sources or []):
        print(f"  Source     : [{src.url}] - {src.title}")
    if not record.sources:
        print("  Sources    : (none)")
    
    tags = record.tags or []
    if tags:
        print(f"  Tags       : {', '.join(tags)}")
    else:
        print("  Tags       : (none)")
    
    if record.status and record.status != "completed":
        print(f"  Status     : {record.status}")

# --- Example usage ---
sample = ResearchRecord(
    id=1, title="AI vs Humans", hypothesis="LLMs will replace analysts",
    conclusion="Assists but doesn't replace", notes=[
        Note(text="Initial draft flawed", metadata={"version": "v0.1"})
    ], sources=[Source(url="https://example.com/ai-paper", title="AI Paper 2024")],
    tags=["research", "hypothesis"], status="ongoing"
)
print_record(sample)
