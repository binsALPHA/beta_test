# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ResearchCatalog
def paginate(items, page_size=10):
    """Return (current_page, total_pages, pages_list) for long item lists.

    Args:
        items: iterable of items (list, tuple, etc.).
        page_size: number of items per page.

    Returns:
        tuple: (current_page, total_pages, pages_list)
              where pages_list is a list of lists, each of length <= page_size.
    """
    items = list(items)
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    pages = [items[i:i + page_size] for i in range(0, len(items), page_size)]
    return pages
