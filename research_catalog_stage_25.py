# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: ResearchCatalog
def normalize_date(raw):
    """Return a tuple (year, month, day) or None if the date is malformed."""
    import datetime as dt
    
    def _try_parse(s: str):
        for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d.%m.%Y", "%d/%m/%Y", "%m-%d-%Y", "%m/%d/%Y"):
            try:
                return dt.datetime.strptime(s, fmt).date()
            except ValueError:
                continue
        return None
    
    if not raw or not isinstance(raw, str):
        return None
    
    s = raw.strip().lower()
    year = month = day = 0
    
    parts = re.split(r'[^\w.]', s)
    nums = [int(p) for p in parts if p.isdigit()]
    
    if len(nums) < 3:
        return None
    
    # Try to assign year/month/day from first three numbers
    candidate_year, candidate_month, candidate_day = nums[0], nums[1], nums[2]
    
    if not (400 <= candidate_year <= 999):
        return None
    if not (1 <= candidate_month <= 12):
        try:
            dt.date(candidate_year, candidate_month, candidate_day)
        except ValueError:
            return None
    
    return (candidate_year, candidate_month, candidate_day)
