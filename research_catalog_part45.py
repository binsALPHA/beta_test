# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ResearchCatalog
import shutil
import os
from datetime import datetime

BACKUP_DIR = "backups"

def create_backup():
    """Создаёт резервную копию каталога ResearchCatalog."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    shutil.copytree(".", backup_path, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path

def restore_backup(backup_path):
    """Восстанавливает каталог из резервной копии, если текущая версия старше."""
    if not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return False
    current = os.listdir(".")
    backup = os.listdir(backup_path)
    if len(backup) <= len(current):
        print("Текущая версия не устарела, восстановление отменено.")
        return False
    print("Восстановление из резервной копии...")
    shutil.rmtree(".")
    shutil.copytree(backup_path, ".")
    print("Восстановление завершено.")
    return True

def list_backups():
    """Выводит список доступных резервных копий."""
    if not os.path.exists(BACKUP_DIR):
        print("Резервных копий не найдено.")
        return
    backups = sorted(os.listdir(BACKUP_DIR))
    for b in backups:
        print(f"  {b}")
