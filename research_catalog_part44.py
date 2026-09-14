# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ResearchCatalog
def backup_data(filepath):
    """Создаёт резервную копию файла данных с timestamp и зацикленным хранением."""
    import os, shutil, datetime
    if not os.path.exists(filepath):
        print(f"[Backup] Файл {filepath} не найден, ничего не скопировано.")
        return None
    backup_dir = os.path.join(os.path.dirname(filepath), "__backups__")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base = os.path.basename(filepath)
    ext = os.path.splitext(base)[1]
    backup_path = os.path.join(backup_dir, f"{base[:-len(ext)]}_{timestamp}{ext}")
    shutil.copy2(filepath, backup_path)
    backups = sorted(os.listdir(backup_dir))
    max_backups = 10
    while len(backups) > max_backups:
        oldest = sorted(backups)[0]
        os.remove(os.path.join(backup_dir, oldest))
    print(f"[Backup] Скопирован {backup_path} ({len(backups)} шт. в хранилище).")
    return backup_path
