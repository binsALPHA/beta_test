# === Stage 32: Добавь журнал действий пользователя ===
# Project: ResearchCatalog
import json
from datetime import datetime

class ResearchActionLog:
    def __init__(self):
        self.actions = []

    def log(self, action_type, description, user=None):
        self.actions.append({
            "timestamp": datetime.now().isoformat(),
            "type": action_type,
            "description": description,
            "user": user
        })

    def get_log(self):
        return self.actions

    def clear_log(self):
        self.actions.clear()
