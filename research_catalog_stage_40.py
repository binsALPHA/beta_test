# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ResearchCatalog
def main():
    import argparse
    parser = argparse.ArgumentParser(description="ResearchCatalog CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_list = sub.add_parser("list", help="list all studies")
    p_show = sub.add_parser("show", help="show a study by id")
    p_add = sub.add_parser("add", help="add a new study")
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--source", help="source URL")
    p_add.add_argument("--hypothesis", help="initial hypothesis")
    p_add.add_argument("--tags", help="comma-separated tags")
    p_add.add_argument("--note", help="initial note")
    p_add.add_argument("--conclusion", help="initial conclusion")
    p_export = sub.add_parser("export", help="export catalog to JSON")
    p_export.add_argument("--file", help="output file path")
    p_import = sub.add_parser("import", help="import studies from JSON")
    p_import.add_argument("--file", help="input JSON file path")
    args = parser.parse_args()
    if args.cmd in ("list", "show", "add", "export", "import"):
        from research_catalog import ResearchCatalog, Study
        catalog = ResearchCatalog()
        if args.cmd == "list":
            for s in catalog.studies:
                print(f"{s.id}: {s.title}")
        elif args.cmd == "show":
            s = catalog.get(args.source_id)
            if s:
                print(s.to_dict())
            else:
                print(f"Study {args.source_id} not found")
        elif args.cmd == "add":
            t = args.title
            source = args.source
            hypothesis = args.hypothesis
            note = args.note
            conclusion = args.conclusion
            tags = args.tags.split(",") if args.tags else []
            s = Study(title=t, source=source, hypothesis=hypothesis, note=note, conclusion=conclusion, tags=tags)
            catalog.add(s)
            print(f"Added {s.id}: {s.title}")
        elif args.cmd == "export":
            data = catalog.to_dict()
            if args.file:
                import json
                with open(args.file, "w") as f:
                    json.dump(data, f, indent=2)
                print(f"Exported to {args.file}")
            else:
                print(json.dumps(data, indent=2))
        elif args.cmd == "import":
            import json
            with open(args.file) as f:
                data = json.load(f)
            catalog.load(data)
            print(f"Imported {len(catalog.studies)} studies")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
