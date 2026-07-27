# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ResearchCatalog
def print_catalog_table(catalog):
    """Форматированный вывод каталога в виде таблицы."""
    if not catalog:
        print("Каталог пуст.")
        return

    # Определяем ширину колонок
    col_widths = {}
    for i, item in enumerate(catalog):
        row_idx = 1 if i == 0 else 2
        keys = list(item.keys())
        for j, key in enumerate(keys):
            if j not in col_widths:
                col_widths[j] = len(key)
            val = str(item[key])
            if len(val) > col_widths[j]:
                col_widths[j] = len(val)

    # Добавляем отступы между колонками
    for i, w in list(col_widths.items()):
        col_widths[i] += 2

    total_width = sum(col_widths.values())

    # Заголовок таблицы
    header = " | ".join(f"{k:<{col_widths[j]}}" for j, k in enumerate(catalog[0].keys()))
    separator = "-" * len(header)

    print(separator)
    print(header)
    print(separator)

    for item in catalog:
        row = " | ".join(f"{item[k]:<{col_widths[j]}}" for j, k in enumerate(item.keys()))
        print(row)

    print(separator)
